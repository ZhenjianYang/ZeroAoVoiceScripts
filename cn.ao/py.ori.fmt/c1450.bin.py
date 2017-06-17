from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1450.bin",                # FileName
        "c1450",                    # MapName
        "c1450",                    # Location
        0x0033,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 51, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1450",                  # 0
        "坦特斯老人",             # 1
        "盖特纳",                 # 2
        "盖巴尔",                 # 3
        "柯洛娜",                 # 4
        "利玛",                   # 5
        "梅尔斯",                 # 6
        "实习医生米修",           # 7
        "莉夏",                   # 8
        "帕欧拉婆婆",             # 9
        "王",                     # 10
        "露茜",                   # 11
        "亚泽尔",                 # 12
        "男人的声音",             # 13
        "巴克斯",                 # 14
    ))

    AddCharChip((
        "chr/ch24000.itc",                   # 00
        "chr/ch21000.itc",                   # 01
        "chr/ch47700.itc",                   # 02
        "apl/ch50375.itc",                   # 03
        "chr/ch21002.itc",                   # 04
        "chr/ch24400.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch05200.itc",                   # 09
        "chr/ch47702.itc",                   # 0A
        "chr/ch23300.itc",                   # 0B
        "chr/ch20702.itc",                   # 0C
        "chr/ch26202.itc",                   # 0D
        "chr/ch24002.itc",                   # 0E
        "chr/ch23000.itc",                   # 0F
        "chr/ch24700.itc",                   # 10
        "chr/ch23400.itc",                   # 11
    ))

    DeclNpc(4269,    0,       -52159,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(52340,   29,      959,     180,  389,  0x0, 0,   1,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(51130,   0,       3210,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(51200,   0,       54049,   0,    261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  261,  0x0, 0,   7,   0,   0,   2,   0,   15,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-45860,  0,       3589,    90,   389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-1639,   29,      56029,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   27,  255,  0)
    DeclNpc(51200,   0,       54049,   270,  389,  0x0, 0,   11,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(16379,   3500,    3470,    180,  389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(16379,   3500,    2069,    0,    389,  0x0, 0,   16,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(17899,   3500,    -39,     0,    126,  0x0, 0,   10,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(32799,   -6500,   -36950,  315,  389,  0x0, 0,   17,  0,   0,   0,   0,   26,  255,  0)

    DeclActor(5800,    0,       4000,    2000,    5800,    1200,    4000,    0x007C, 0,  29, 0x0000)
    DeclActor(17900,   3500,    -40,     1500,    17900,   4800,    -40,     0x007C, 0,  19, 0x0000)

    ChipFrameInfo(824, 0)                                        # 0

    ScpFunction((
        "Function_0_338",          # 00, 0
        "Function_1_3E8",          # 01, 1
        "Function_2_413",          # 02, 2
        "Function_3_43E",          # 03, 3
        "Function_4_469",          # 04, 4
        "Function_5_937",          # 05, 5
        "Function_6_AE8",          # 06, 6
        "Function_7_182C",         # 07, 7
        "Function_8_1977",         # 08, 8
        "Function_9_1A8C",         # 09, 9
        "Function_10_1B7B",        # 0A, 10
        "Function_11_268B",        # 0B, 11
        "Function_12_281D",        # 0C, 12
        "Function_13_2999",        # 0D, 13
        "Function_14_2C26",        # 0E, 14
        "Function_15_3599",        # 0F, 15
        "Function_16_3A07",        # 10, 16
        "Function_17_3ADF",        # 11, 17
        "Function_18_3B7F",        # 12, 18
        "Function_19_3DE3",        # 13, 19
        "Function_20_4425",        # 14, 20
        "Function_21_4458",        # 15, 21
        "Function_22_4531",        # 16, 22
        "Function_23_45E0",        # 17, 23
        "Function_24_4696",        # 18, 24
        "Function_25_4723",        # 19, 25
        "Function_26_4A77",        # 1A, 26
        "Function_27_4B80",        # 1B, 27
        "Function_28_4CDF",        # 1C, 28
        "Function_29_559F",        # 1D, 29
        "Function_30_5695",        # 1E, 30
        "Function_31_6EF6",        # 1F, 31
        "Function_32_762A",        # 20, 32
        "Function_33_7911",        # 21, 33
        "Function_34_7FC6",        # 22, 34
    ))


    def Function_0_338(): pass

    label("Function_0_338")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_370"),
        (1, "loc_37C"),
        (2, "loc_388"),
        (3, "loc_394"),
        (4, "loc_3A0"),
        (5, "loc_3AC"),
        (6, "loc_3B8"),
        (SWITCH_DEFAULT, "loc_3C4"),
    )


    label("loc_370")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_37C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_388")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_394")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3A0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3AC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3D0")

    label("loc_3E7")

    Return()

    # Function_0_338 end

    def Function_1_3E8(): pass

    label("Function_1_3E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_412")
    OP_94(0xFE, 0xC602, 0xFFFFF538, 0xCFDA, 0xF50, 0x3E8)
    Sleep(300)
    Jump("Function_1_3E8")

    label("loc_412")

    Return()

    # Function_1_3E8 end

    def Function_2_413(): pass

    label("Function_2_413")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43D")
    OP_94(0xFE, 0x1CFC, 0x208A, 0x2FBC, 0x337C, 0x3E8)
    Sleep(300)
    Jump("Function_2_413")

    label("loc_43D")

    Return()

    # Function_2_413 end

    def Function_3_43E(): pass

    label("Function_3_43E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_468")
    OP_94(0xFE, 0xCC74, 0xBCCA, 0xD8C2, 0xC4C2, 0x3E8)
    Sleep(300)
    Jump("Function_3_43E")

    label("loc_468")

    Return()

    # Function_3_43E end

    def Function_4_469(): pass

    label("Function_4_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B8")
    SetChrPos(0xC, 8650, 3500, 10630, 0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xD, 8650, 3500, 11630, 180)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_4B3")

    Jump("loc_936")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_550")
    SetChrPos(0xC, 54580, 30, 48540, 135)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 55550, 200, 52190, 270)
    SetChrChipByIndex(0xD, 0xD)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x15, 52830, 20, -50640, 0)
    SetChrPos(0x11, 52800, 20, -48960, 180)
    SetChrPos(0x12, 51720, 0, -48250, 180)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x11, 0x10)
    Jump("loc_936")

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_59D")
    SetChrPos(0xA, 52340, 30, 960, 180)
    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0xC, 11610, 3500, 10750, 180)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xB, 11700, 3500, 9390, 0)
    Jump("loc_936")

    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_5C0")
    SetChrPos(0x8, 3800, 0, 1500, 270)

    label("loc_5C0")

    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60D")
    SetChrPos(0x10, 52570, 30, 53820, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F2")
    SetChrFlags(0x13, 0x10)

    label("loc_5F2")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 4100, 30, -56450, 90)
    Jump("loc_634")

    label("loc_60D")

    SetChrPos(0x10, 52660, 30, 50020, 135)
    SetChrPos(0xB, 53860, 30, 48820, 315)
    SetChrFlags(0x10, 0x10)

    label("loc_634")

    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_936")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0xA, 51130, 0, 3210, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_936")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6C2")
    SetChrPos(0xA, 3400, 0, 3610, 270)
    SetChrPos(0xB, 1320, 0, 3550, 90)
    SetChrPos(0xC, 2020, 0, 2420, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_936")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_73A")
    SetChrPos(0x8, 1590, 200, -55120, 270)
    SetChrChipByIndex(0x8, 0xE)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 10560, 3500, 10830, 135)
    SetChrPos(0xB, 11700, 3500, 9390, 315)
    SetChrPos(0xC, 12540, 3500, 11160, 225)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    Jump("loc_936")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_779")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, 3400, 30, -54370, 315)
    SetChrPos(0xA, 2200, 30, -53180, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_936")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_787")
    Jump("loc_936")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_831")
    SetChrPos(0xA, -1400, 150, -54970, 90)
    SetChrPos(0x8, 1590, 150, -55120, 270)
    SetChrChipByIndex(0xA, 0xA)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0x8, 0xE)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 55550, 200, 52190, 270)
    SetChrChipByIndex(0xC, 0xC)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 52380, 200, 52200, 90)
    SetChrChipByIndex(0xD, 0xD)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_936")

    label("loc_831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_86E")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xA, 51130, 0, 3210, 0)
    SetChrFlags(0xA, 0x10)
    Jump("loc_936")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 8650, 3500, 10630, 0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xD, 8650, 3500, 11630, 180)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_936")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_923")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8FC")
    SetChrPos(0x9, 2200, 30, -53180, 135)
    SetChrPos(0x8, 3400, 30, -54370, 315)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_91E")

    label("loc_8FC")

    SetChrPos(0x9, 2200, 30, -53180, 135)
    SetChrPos(0x8, 3400, 30, -54370, 315)

    label("loc_91E")

    Jump("loc_936")

    label("loc_923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_936")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_936")

    Return()

    # Function_4_469 end

    def Function_5_937(): pass

    label("Function_5_937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_952")
    OP_65(0x1, 0x1)
    Jump("loc_95C")

    label("loc_952")

    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)

    label("loc_95C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_974")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_991")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A9")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_9A9")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C4")
    OP_66(0x0, 0x1)
    Jump("loc_9F2")

    label("loc_9C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E0")
    OP_66(0x0, 0x1)
    Jump("loc_9F2")

    label("loc_9E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F2")
    OP_66(0x0, 0x1)

    label("loc_9F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A0B")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_A11")

    label("loc_A0B")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A5A")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A99")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACB")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8")
    Sound(1020, 1, 60, 0)
    Jump("loc_ACB")

    label("loc_AC8")

    OP_24(0x3FC)

    label("loc_ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE7")
    ClearMapObjFlags(0x6, 0x4)

    label("loc_AE7")

    Return()

    # Function_5_937 end

    def Function_6_AE8(): pass

    label("Function_6_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_BA8")
    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "在盖巴尔先生担任议员的时候，\x01",
            "有个人曾多番关照过他，\x01",
            "那个人现在就住在西街。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "好象是住在雷……\x01",
            "一个叫『雷什么』的\x01",
            "公寓里。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "那个人说不定知道\x01",
            "盖巴尔先生的行踪。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_BA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD1")
    Call(0, 32)
    Return()

    label("loc_BD1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA4")

    #C0004
    ChrTalk(
        0xFE,
        (
            "不良团伙的那些孩子\x01",
            "正在同心协力\x01",
            "保卫这个旧城区。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "虽然他们以前经常在广场\x01",
            "大打出手，让人不敢靠近，\x01",
            "但年轻人果然还是可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "这样一来，旧城区总算\x01",
            "有种团结一心的感觉了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D15")

    label("loc_CA4")


    #C0007
    ChrTalk(
        0xFE,
        (
            "不良团伙的那些孩子\x01",
            "正在保卫这个旧城区，\x01",
            "年轻人果然可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "这样一来，旧城区总算\x01",
            "有种团结一心的感觉了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D15")

    Jump("loc_1828")

    label("loc_D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D91")

    #C0009
    ChrTalk(
        0xFE,
        (
            "飘散在外面的那些蓝色雾气\x01",
            "到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "总之，我得提醒\x01",
            "公寓里的住户们，\x01",
            "让他们千万不要外出。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1828")

    label("loc_D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0F")

    #C0011
    ChrTalk(
        0xFE,
        (
            "我也听了总统的\x01",
            "那番演讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "虽说可以理解他的想法……\x01",
            "可是，真的没有\x01",
            "和平解决的方法吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E5C")

    label("loc_E0F")


    #C0013
    ChrTalk(
        0xFE,
        "虽然我可以理解总统的想法……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "可是，真的没有\x01",
            "和平解决的方法吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5C")

    Jump("loc_1828")

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_100D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_F3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_EE2")

    #C0015
    ChrTalk(
        0x8,
        (
            "等蔬菜炖透之后，\x01",
            "就要开始调味了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "你们就尽管期待\x01",
            "『强壮苦番茄猪骨汤』吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F37")

    label("loc_EE2")


    #C0017
    ChrTalk(
        0x8,
        (
            "好了，我该去准备\x01",
            "分发赈济食物时要用到的器皿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "希望今天所有人都能分到……\x02",
    )

    CloseMessageWindow()

    label("loc_F37")

    Jump("loc_FAA")

    label("loc_F3C")


    #C0019
    ChrTalk(
        0x8,
        (
            "赈济食物是在这个房间\x01",
            "和科洛娜小姐的房间\x01",
            "准备的。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "要准备的食物实在太多了，\x01",
            "不管有几个厨房\x01",
            "都不够用。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAA")

    Jump("loc_1008")

    label("loc_FAF")


    #C0021
    ChrTalk(
        0xFE,
        (
            "呵呵，大家似乎都\x01",
            "觉得我的猪骨汤很好吃，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "这也要多谢\x01",
            "你们的帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1008")

    Jump("loc_1828")

    label("loc_100D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_110E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C9")

    #C0023
    ChrTalk(
        0xFE,
        (
            "昨天傍晚时分，\x01",
            "有客人来拜访盖巴尔先生，\x01",
            "这真是相当少见……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "但自那之后，\x01",
            "他的样子就一直有些奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "还说有人正在\x01",
            "追查他的行踪……\x01",
            "唔，真让人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1109")

    label("loc_10C9")


    #C0026
    ChrTalk(
        0xFE,
        (
            "盖巴尔先生说，\x01",
            "有人正在追查他的行踪……\x01",
            "唔，真让人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1109")

    Jump("loc_1828")

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1166")

    #C0027
    ChrTalk(
        0xFE,
        (
            "盖巴尔先生好像\x01",
            "已经开始习惯\x01",
            "这里的生活了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "呵呵，这真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1828")

    label("loc_1166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_126D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E8")

    #C0029
    ChrTalk(
        0xFE,
        (
            "（大嚼）……\x01",
            "盖巴尔先生做的煮豆子真好吃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "呵呵，本想留到\x01",
            "晚饭时再吃，\x01",
            "但忍不住都快吃完了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1268")

    label("loc_11E8")


    #C0031
    ChrTalk(
        0xFE,
        (
            "话说回来，盖巴尔先生能\x01",
            "慢慢敞开心扉，真是让人高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "听说他在当议员的时候十分傲慢，\x01",
            "但现在看来，他的本质还是很善良的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1268")

    Jump("loc_1828")

    label("loc_126D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_127E")
    Call(0, 7)
    Jump("loc_1828")

    label("loc_127E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135E")

    #C0033
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立为自主国家吗……\x01",
            "虽然是个再正当不过的主张，\x01",
            "但似乎太过急进了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "两大国肯定不会\x01",
            "给我们好脸色看，\x01",
            "我不认为独立一事可以和平实现……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "哎呀呀，迪塔市长的提案\x01",
            "实在是太大胆了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13D0")

    label("loc_135E")


    #C0036
    ChrTalk(
        0xFE,
        (
            "让克洛斯贝尔独立为自主国家吗……\x01",
            "我不认为这件事可以和平实现……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "哎呀呀，迪塔市长的提案\x01",
            "实在是太大胆了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D0")

    Jump("loc_1828")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_143B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F0")
    Call(0, 8)
    Jump("loc_1436")

    label("loc_13F0")


    #C0038
    ChrTalk(
        0xFE,
        "嗯，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "既然发生了那种事，\x01",
            "没能抵御住诱惑\x01",
            "也不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1436")

    Jump("loc_1828")

    label("loc_143B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1505")

    #C0040
    ChrTalk(
        0xFE,
        (
            "揭幕式啊……那个活动\x01",
            "好像在市区引起了很大的反响呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "新市政厅大楼\x01",
            "就好像象征着这个\x01",
            "克洛斯贝尔的繁华……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "但希望他们也不要忘记\x01",
            "我们这些默默生活在\x01",
            "城市角落的居民。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_155D")

    label("loc_1505")


    #C0043
    ChrTalk(
        0xFE,
        (
            "话说回来，盖巴尔先生还是\x01",
            "整天都闷闷不乐的。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "干脆再把他叫来，\x01",
            "听他吐吐苦水吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_155D")

    Jump("loc_1828")

    label("loc_1562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_15D8")

    #C0045
    ChrTalk(
        0xFE,
        (
            "通商会议将从明天开始，\x01",
            "那些警察也来\x01",
            "旧城区巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "不过，首脑们肯定\x01",
            "不会来这种萧条的\x01",
            "地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1828")

    label("loc_15D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_16AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1643")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15FD")
    Call(0, 9)
    Jump("loc_163E")

    label("loc_15FD")


    #C0047
    ChrTalk(
        0xFE,
        (
            "盖特纳，看你这么有精神，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "我真心为你高兴。\x02",
    )

    CloseMessageWindow()

    label("loc_163E")

    Jump("loc_16AA")

    label("loc_1643")


    #C0049
    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "你们可以让盖巴尔先生\x01",
            "一个人静一静吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "他经历了很多事，暂时还\x01",
            "无法平复自己的心情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AA")

    Jump("loc_1828")

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AE")

    #C0051
    ChrTalk(
        0xFE,
        (
            "正如你所见，旧城区\x01",
            "是个被排除在都市计划\x01",
            "之外的区域。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "虽然治安较差，但由于房租便宜，\x01",
            "所以有很多背负着各种往事的人\x01",
            "聚集于此。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "同时，也有人\x01",
            "在这里重整旗鼓，\x01",
            "并走向成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "呵呵，这里可是个\x01",
            "充满人生百态的\x01",
            "地方哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1828")

    label("loc_17AE")


    #C0055
    ChrTalk(
        0xFE,
        (
            "这个旧城区聚集着很多\x01",
            "背负着各种往事的人，\x01",
            "同时，也有人从这里走向成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "呵呵，这里可是个\x01",
            "充满人生百态的\x01",
            "地方哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1828")

    TalkEnd(0xFE)
    Return()

    # Function_6_AE8 end

    def Function_7_182C(): pass

    label("Function_7_182C")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190B")

    #C0057
    ChrTalk(
        0x8,
        (
            "（大嚼）……\x01",
            "哦哦，真美味。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        "盖巴尔先生，这些煮豆子是你亲手做的……？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xA,
        (
            "嗯，好久没进过\x01",
            "厨房，一不小心\x01",
            "就做多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xA,
        (
            "能合您的口味，\x01",
            "真是再好不过。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "呵呵，真是让你费心了，\x01",
            "谢谢啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_196E")

    label("loc_190B")


    #C0062
    ChrTalk(
        0x8,
        (
            "对了，如果还有多余的，\x01",
            "也拿给其他人尝尝\x01",
            "如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "大家一定会\x01",
            "很高兴的。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xA,
        "是、是吗……？\x02",
    )

    CloseMessageWindow()

    label("loc_196E")

    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_7_182C end

    def Function_8_1977(): pass

    label("Function_8_1977")


    #C0065
    ChrTalk(
        0xA,
        "坦特斯先生，您听我说。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "我当年也是个充满理想的\x01",
            "年轻人。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "呵呵，我知道，\x01",
            "你都跟我说过好几次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "你想用自己的方式去\x01",
            "改变这座城市，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "是的，正是如此。\x01",
            "当年我志气满满，\x01",
            "以无党派候选人的身份当选议员……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "但有一天，某个帝国派议员\x01",
            "突然对我说……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_8_1977 end

    def Function_9_1A8C(): pass

    label("Function_9_1A8C")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0071
    ChrTalk(
        0x8,
        (
            "哦哦，盖特纳，\x01",
            "看你这么有精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "你的生意做得\x01",
            "还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "嗯，托您的福，\x01",
            "目前还算顺利。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "对了，我今天给您\x01",
            "带了一盒点心。\x01",
            "请尝尝吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "哦哦，太谢谢啦。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "我去泡壶茶，\x01",
            "咱们一起吃吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_9_1A8C end

    def Function_10_1B7B(): pass

    label("Function_10_1B7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C80")

    #C0077
    ChrTalk(
        0xFE,
        (
            "在协会的帮助下，\x01",
            "我终于联系上了\x01",
            "身在利贝尔的阿鲁姆他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "听说利贝尔也出现了混乱状况，\x01",
            "但相比帝国和共和国，已经算是很和平了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的混乱局势似乎\x01",
            "还要再持续一段时间……\x01",
            "能听到他们的声音，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1CFB")

    label("loc_1C80")


    #C0080
    ChrTalk(
        0xFE,
        (
            "我终于联系上了\x01",
            "身在利贝尔的阿鲁姆他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的混乱局势似乎\x01",
            "还要再持续一段时间……\x01",
            "但我一定能努力坚持下去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFB")

    Jump("loc_1DF5")

    label("loc_1D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9E")

    #C0082
    ChrTalk(
        0xFE,
        (
            "总统被拘捕，随后又出现了\x01",
            "那种莫名其妙的大树……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "如果我的心中能有个希望，\x01",
            "应该也能撑过这次的难关……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "女神啊，请救救我们吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DF5")

    label("loc_1D9E")


    #C0085
    ChrTalk(
        0xFE,
        (
            "如果我的心中能有个希望，\x01",
            "应该也能撑过这次的难关……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "女神啊，请救救我们吧……\x02",
    )

    CloseMessageWindow()

    label("loc_1DF5")

    Jump("loc_2687")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F89")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA7")

    #C0087
    ChrTalk(
        0xFE,
        "虽然很担心这里的情况……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "但我更加担心身在利贝尔的\x01",
            "阿鲁姆他们是否平安……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "儿孙是我的希望，\x01",
            "怎么才能和他们取得联系呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F19")

    label("loc_1EA7")


    #C0090
    ChrTalk(
        0xFE,
        (
            "自从独立宣言发表之后，\x01",
            "就再也无法联络到国外的人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "阿鲁姆他们是我的希望，\x01",
            "怎么才能和他们取得联系呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F19")

    Jump("loc_1F84")

    label("loc_1F1E")


    #C0092
    ChrTalk(
        0xFE,
        "出现在城市里的那些怪物究竟是什么……\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "虽然它们并没有\x01",
            "进入旧城区，\x01",
            "但这样下去真的没问题吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F84")

    Jump("loc_2687")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_22D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2069")

    #C0094
    ChrTalk(
        0xFE,
        (
            "我、我在东街听了那场演讲，\x01",
            "老实说，简直不敢相信自己的耳朵……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "那番发言的是非对错暂且不论，\x01",
            "至少两大国肯定\x01",
            "不会善罢甘休的。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "如此看来，\x01",
            "想办法离开自治州\x01",
            "才是明智之举啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_216D")

    label("loc_2069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2107")

    #C0097
    ChrTalk(
        0xFE,
        "阿鲁姆他们都在利贝尔，不如就……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "哼、哼……我在\x01",
            "胡思乱想些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "我永远都是克洛斯贝尔人……\x01",
            "无论发生什么事，都要留在这里。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_216D")

    label("loc_2107")


    #C0100
    ChrTalk(
        0xFE,
        (
            "真是的……我在\x01",
            "胡思乱想些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "我永远都是克洛斯贝尔人……\x01",
            "无论发生什么事，都要留在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_216D")

    Jump("loc_22CC")

    label("loc_2172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223D")

    #C0102
    ChrTalk(
        0xFE,
        (
            "我、我在东街听了那场演讲，\x01",
            "老实说，简直不敢相信自己的耳朵……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "那番发言的是非对错暂且不论，\x01",
            "至少两大国肯定\x01",
            "不会善罢甘休的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "如此看来，\x01",
            "想办法离开自治州\x01",
            "才是明智之举啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_22CC")

    label("loc_223D")


    #C0105
    ChrTalk(
        0xFE,
        (
            "……哼，我在胡思乱想些什么啊。\x01",
            "事到如今，我怎能舍弃自治州，\x01",
            "逃到别的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "我永远都是克洛斯贝尔人……\x01",
            "无论发生什么事，都要留在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CC")

    Jump("loc_2687")

    label("loc_22D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22DF")
    Jump("loc_2687")

    label("loc_22DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_233D")

    #C0107
    ChrTalk(
        0xFE,
        (
            "这、这可不是开玩笑的……\x01",
            "得赶紧藏起来！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "可、可是，\x01",
            "到底该逃到哪里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2687")

    label("loc_233D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_234E")
    Call(0, 11)
    Jump("loc_2687")

    label("loc_234E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_235F")
    Call(0, 12)
    Jump("loc_2687")

    label("loc_235F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2370")
    Call(0, 7)
    Jump("loc_2687")

    label("loc_2370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2452")

    #C0109
    ChrTalk(
        0xFE,
        (
            "唔……迪塔市长的胆子\x01",
            "可真大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "这样一来……\x01",
            "帝国派、共和国派议员的处境\x01",
            "就会更加糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "……唔，我为何要站在\x01",
            "这种角度讨论政治问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "呼，差不多也该认真考虑一下\x01",
            "今后的立身之计了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2484")

    label("loc_2452")


    #C0113
    ChrTalk(
        0xFE,
        (
            "第二次人生吗……\x01",
            "如今的我，\x01",
            "到底还有什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2484")

    Jump("loc_2687")

    label("loc_2489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_250E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A4")
    Call(0, 8)
    Jump("loc_2509")

    label("loc_24A4")


    #C0114
    ChrTalk(
        0xFE,
        (
            "其实我很清楚，\x01",
            "那种事完全不能\x01",
            "算是理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "可是……当时的我真的只是个\x01",
            "什么都不懂的年轻人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2509")

    Jump("loc_2687")

    label("loc_250E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2563")

    #C0116
    ChrTalk(
        0xFE,
        "各国首脑来访算什么！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "真是的，每个人都像\x01",
            "过节一样吵吵闹闹的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2687")

    label("loc_2563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_262D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F2")

    #C0118
    ChrTalk(
        0xFE,
        "哼……通商会议又如何。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "现在的我不仅不再关心议会，\x01",
            "对任何政治问题都\x01",
            "毫无兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "让他们自己闹腾去吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2628")

    label("loc_25F2")


    #C0121
    ChrTalk(
        0xFE,
        "哼……通商会议又如何。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        "让他们自己闹腾去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2628")

    Jump("loc_2687")

    label("loc_262D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_267E")

    #C0123
    ChrTalk(
        0xFE,
        "你、你们还有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "如果没什么事的话，\x01",
            "就赶快出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2687")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2687")

    label("loc_2687")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B7B end

    def Function_11_268B(): pass

    label("Function_11_268B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BF")

    #C0125
    ChrTalk(
        0xB,
        (
            "那个……\x01",
            "我烤了一些曲奇，\x01",
            "希望您也尝尝。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        (
            "嘿嘿，\x01",
            "妈妈亲手做的曲奇\x01",
            "很好吃哦～¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0127
    ChrTalk(
        0xA,
        "这、这怎么好意思。\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xA,
        (
            "这样一来，我就像是\x01",
            "为了得到回礼才……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xB,
        (
            "呵呵，请您\x01",
            "不要多心。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "我和您一样，\x01",
            "只是做多了\x01",
            "一些而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        "是、是吗，那我就收下了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2810")

    label("loc_27BF")


    #C0132
    ChrTalk(
        0xA,
        (
            "（轻咬）……\x01",
            "嗯！很美味啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "嘿嘿，对吧对吧～¤\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xB,
        "呵呵，您喜欢就好。\x02",
    )

    CloseMessageWindow()

    label("loc_2810")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_268B end

    def Function_12_281D(): pass

    label("Function_12_281D")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290E")

    #C0135
    ChrTalk(
        0xC,
        (
            "妈妈，这个豆子\x01",
            "真好吃～\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "呵呵，看来利玛\x01",
            "很爱吃啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xB,
        (
            "盖巴尔先生，我们真的\x01",
            "可以收下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        "当、当然。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "我一个人也吃不完\x01",
            "这么多，\x01",
            "请别客气，尽管收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xB,
        "呵呵，那就谢谢您了。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        "谢谢叔叔！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_298C")

    label("loc_290E")


    #C0142
    ChrTalk(
        0xC,
        (
            "（狼吞虎咽）\x01",
            "嗯～真好吃～！\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        (
            "呵呵，利玛可真是的，\x01",
            "不能用手抓着吃哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "哈哈，\x01",
            "看这孩子吃得这么开心，\x01",
            "我也很愉快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298C")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_12_281D end

    def Function_13_2999(): pass

    label("Function_13_2999")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_29AA")
    Jump("loc_2C22")

    label("loc_29AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_29B8")
    Jump("loc_2C22")

    label("loc_29B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_29C6")
    Jump("loc_2C22")

    label("loc_29C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29D4")
    Jump("loc_2C22")

    label("loc_29D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_29E2")
    Jump("loc_2C22")

    label("loc_29E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6D")

    #C0145
    ChrTalk(
        0xFE,
        "唉，每天从这里去医院，还真是辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "但我已经在这里结识了\x01",
            "很多好邻居……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "实在是不想\x01",
            "离开这里啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2ACC")

    label("loc_2A6D")


    #C0148
    ChrTalk(
        0xFE,
        (
            "虽然路上比较辛苦，\x01",
            "但我已经在这所公寓里\x01",
            "结识了很多好邻居……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "实在是不想\x01",
            "离开这里啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACC")

    Jump("loc_2C22")

    label("loc_2AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ADF")
    Jump("loc_2C22")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AED")
    Jump("loc_2C22")

    label("loc_2AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2AFB")
    Jump("loc_2C22")

    label("loc_2AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B09")
    Jump("loc_2C22")

    label("loc_2B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2B17")
    Jump("loc_2C22")

    label("loc_2B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8E")

    #C0150
    ChrTalk(
        0xFE,
        (
            "嗯……新生学习班的资料，\x01",
            "还有……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "唉，刚刚入学就开始丢三落四了，\x01",
            "今后可怎么办啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C22")

    label("loc_2B8E")


    #C0152
    ChrTalk(
        0xFE,
        (
            "呵呵，话说回来，\x01",
            "我居然真的考上了\x01",
            "乌尔斯拉医科大学。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "今后也许会比备考的那段时期\x01",
            "更加辛苦……不过，还是再享受\x01",
            "一下这通过考试的兴奋感觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C22")

    TalkEnd(0xFE)
    Return()

    # Function_13_2999 end

    def Function_14_2C26(): pass

    label("Function_14_2C26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2CAA")

    #C0154
    ChrTalk(
        0xFE,
        (
            "看到那棵巨大的蓝白色大树，\x01",
            "我就会感到不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "在外工作的丈夫应该\x01",
            "也是一样的心情吧……\x01",
            "我一定要努力支持他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3595")

    label("loc_2CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D23")

    #C0156
    ChrTalk(
        0xFE,
        (
            "虽说事先就接到了戒严通知，\x01",
            "但真没想到情况会严重到这种程度……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "……做饭的时候，我的手都在发抖呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3595")

    label("loc_2D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2DBD")

    #C0158
    ChrTalk(
        0xFE,
        (
            "我已经从坦特斯先生\x01",
            "那里听说了演讲内容……\x01",
            "老实说，现在真是非常不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "我丈夫今天也和平时一样，\x01",
            "出门工作了……\x01",
            "真希望他能早点回家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3595")

    label("loc_2DBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E52")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E05")

    #C0160
    ChrTalk(
        0xFE,
        (
            "白萝卜很难煮透，\x01",
            "所以要在背面切几刀……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E4D")

    label("loc_2E05")

    OP_4B(0x10, 0x0)

    #C0161
    ChrTalk(
        0xB,
        (
            "好了，想想晚上\x01",
            "该做什么\x01",
            "赈济菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x10,
        "嗯，做什么好呢？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0x0)

    label("loc_2E4D")

    Jump("loc_3595")

    label("loc_2E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2EC3")

    #C0163
    ChrTalk(
        0xFE,
        (
            "听说玛因兹那边发生了\x01",
            "很可怕的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "警备队的队员至今\x01",
            "仍在战斗……\x01",
            "真希望事件能尽早解决。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3595")

    label("loc_2EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2ED4")
    Call(0, 11)
    Jump("loc_3595")

    label("loc_2ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2EE5")
    Call(0, 12)
    Jump("loc_3595")

    label("loc_2EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F58")

    #C0165
    ChrTalk(
        0xFE,
        (
            "我丈夫开始在\x01",
            "新工地工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "他日复一日，一直都在为\x01",
            "这个家努力工作……\x01",
            "真不知该怎么感谢他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3595")

    label("loc_2F58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3135")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A6")

    #C0167
    ChrTalk(
        0xFE,
        (
            "前不久，我丈夫告诉我……\x01",
            "不少外国建筑公司也参与了\x01",
            "兰花塔的建造工程。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "听说工程完全是按照\x01",
            "楼层来分配的……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "我丈夫参与施工的是\x01",
            "上层的ＶＩＰ区\x01",
            "和国际会议区。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "说到国际会议区，\x01",
            "也就是不久前举办了\x01",
            "通商会议的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "呵呵，一想到那么重要的会议\x01",
            "在我丈夫参与施工的地方举办，\x01",
            "就觉得很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3130")

    label("loc_30A6")


    #C0172
    ChrTalk(
        0xFE,
        (
            "说到国际会议区，\x01",
            "也就是不久前举办了\x01",
            "通商会议的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "呵呵，一想到那么重要的会议\x01",
            "在我丈夫参与施工的地方举办，\x01",
            "就觉得很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3130")

    Jump("loc_3595")

    label("loc_3135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3189")

    #C0174
    ChrTalk(
        0xFE,
        (
            "我正在泡莉夏小姐\x01",
            "之前送给我的绿茶呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "呵呵，这茶叶\x01",
            "真香啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3595")

    label("loc_3189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3197")
    Jump("loc_3595")

    label("loc_3197")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3246")

    #C0176
    ChrTalk(
        0xFE,
        (
            "兰花塔已经全面竣工，\x01",
            "接下来就等着正式揭幕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "这样一来，我丈夫的\x01",
            "工作总算是\x01",
            "告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "我明天一定要去\x01",
            "亲眼见证我丈夫的工作成果。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_329C")

    label("loc_3246")


    #C0179
    ChrTalk(
        0xFE,
        (
            "兰花塔终于要在明天\x01",
            "正式揭幕亮相了……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "我一定要去\x01",
            "亲眼见证我丈夫的工作成果。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329C")

    Jump("loc_3595")

    label("loc_32A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338F")

    #C0181
    ChrTalk(
        0xFE,
        (
            "我的丈夫在\x01",
            "建筑工地工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "在最近这几个月里，他一直都在\x01",
            "那座著名的新市政厅大楼——\x01",
            "兰花塔的建筑现场挥洒汗水。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "听说内部装潢已经完成，\x01",
            "现在只差外部\x01",
            "加工了……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "呵呵，真期待兰花塔的全面竣工啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_33EF")

    label("loc_338F")


    #C0185
    ChrTalk(
        0xFE,
        (
            "建造兰花塔的工作是我丈夫\x01",
            "至今为止参与的\x01",
            "最大型工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "呵呵，真期待兰花塔的全面竣工啊。\x02",
    )

    CloseMessageWindow()

    label("loc_33EF")

    Jump("loc_3595")

    label("loc_33F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3507")

    #C0187
    ChrTalk(
        0xFE,
        (
            "听说在最近几年，自治州议会\x01",
            "曾经商讨过改建\x01",
            "旧城区的计划……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "但经过新议会的审议之后，\x01",
            "那项计划被\x01",
            "正式冻结了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "虽然只是暂时冻结，\x01",
            "还不能彻底安心……\x01",
            "但听到那个消息之后，我还是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "如果这里被拆毁，\x01",
            "我们一家人就\x01",
            "无处可去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3595")

    label("loc_3507")


    #C0191
    ChrTalk(
        0xFE,
        (
            "听说主导旧城区改建计划的议员\x01",
            "与教团事件存在干系，\x01",
            "已经被逮捕了……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "而且那项计划并不周全，\x01",
            "有很多因素都没有考虑到，\x01",
            "所以就被搁置了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3595")

    TalkEnd(0xFE)
    Return()

    # Function_14_2C26 end

    def Function_15_3599(): pass

    label("Function_15_3599")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35B7")
    Call(0, 16)
    Jump("loc_3602")

    label("loc_35B7")


    #C0193
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "爸爸仍然在为我和妈妈\x01",
            "努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "好～\x01",
            "我也要加油！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3602")

    Jump("loc_3A03")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_364B")

    #C0195
    ChrTalk(
        0xFE,
        "爸爸和妈妈都很不安呢。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "不知道会不会有事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A03")

    label("loc_364B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3696")

    #C0197
    ChrTalk(
        0xFE,
        (
            "妈妈……\x01",
            "好像很担心的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "真希望她能打起精神来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A03")

    label("loc_3696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36A4")
    Jump("loc_3A03")

    label("loc_36A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_36F1")

    #C0199
    ChrTalk(
        0xFE,
        (
            "莉夏姐姐今天\x01",
            "没什么精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "是不是发生什么事了呢～？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A03")

    label("loc_36F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3702")
    Call(0, 11)
    Jump("loc_3A03")

    label("loc_3702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3713")
    Call(0, 12)
    Jump("loc_3A03")

    label("loc_3713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3807")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BD")

    #C0201
    ChrTalk(
        0xFE,
        (
            "今天早上，我和妈妈一起\x01",
            "送爸爸出门。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "好像是因为今天是去新工地的第一天，\x01",
            "所以不用急着走。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "虽然不太懂，但能送\x01",
            "爸爸出门，真是开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3802")

    label("loc_37BD")


    #C0204
    ChrTalk(
        0xFE,
        (
            "我和妈妈都亲了爸爸，\x01",
            "让他路上小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        "爸爸还害羞了，真可爱。\x02",
    )

    CloseMessageWindow()

    label("loc_3802")

    Jump("loc_3A03")

    label("loc_3807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_384C")

    #C0206
    ChrTalk(
        0xFE,
        (
            "奇幻乐园\x01",
            "真好玩～\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "以后还要和爸爸妈妈一起去～\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A03")

    label("loc_384C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3885")

    #C0208
    ChrTalk(
        0xFE,
        "下午茶～下午茶¤ 大家一起喝下午茶～¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A03")

    label("loc_3885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3893")
    Jump("loc_3A03")

    label("loc_3893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_38EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AE")
    Call(0, 17)
    Jump("loc_38E7")

    label("loc_38AE")


    #C0209
    ChrTalk(
        0xFE,
        (
            "来，亲爱的，\x01",
            "饭菜已经做好了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "快趁热吃吧～¤\x02",
    )

    CloseMessageWindow()

    label("loc_38E7")

    Jump("loc_3A03")

    label("loc_38EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3981")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    #C0211
    ChrTalk(
        0xFE,
        (
            "我爸爸每天\x01",
            "都在建筑工地\x01",
            "工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "今天应该也会回来得很晚。\x01",
            "唉……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_397C")

    label("loc_3950")


    #C0213
    ChrTalk(
        0xFE,
        (
            "爸爸今天应该\x01",
            "也会回来得很晚吧。\x01",
            "唉……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_397C")

    Jump("loc_3A03")

    label("loc_3981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3A03")

    #C0214
    ChrTalk(
        0xFE,
        (
            "最近，那些爱欺负人的\x01",
            "政府官员都没有来了，\x01",
            "妈妈很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "虽然我不大明白为什么，\x01",
            "但只要妈妈高兴，我就也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A03")

    TalkEnd(0xFE)
    Return()

    # Function_15_3599 end

    def Function_16_3A07(): pass

    label("Function_16_3A07")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0216
    ChrTalk(
        0xC,
        "爸爸，你今天也要去工作吗？\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xD,
        "是啊，工地又开工啦。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        (
            "利玛，我知道你很担心，\x01",
            "但要和妈妈一起好好看家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xC,
        "嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xC,
        (
            "爸爸，路上小心！\x01",
            "……啾⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xD,
        "哈哈，我出门了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 6)
    Return()

    # Function_16_3A07 end

    def Function_17_3ADF(): pass

    label("Function_17_3ADF")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0222
    ChrTalk(
        0xD,
        (
            "利玛～\x01",
            "今天玩什么好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xC,
        (
            "嗯～\x01",
            "玩过家家好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xC,
        (
            "利玛要当妈妈，\x01",
            "爸爸就当爸爸吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xD,
        (
            "哈哈，让爸爸当爸爸吗？\x01",
            "原来如此，我知道了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_17_3ADF end

    def Function_18_3B7F(): pass

    label("Function_18_3B7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9D")
    Call(0, 16)
    Jump("loc_3C2C")

    label("loc_3B9D")


    #C0226
    ChrTalk(
        0xFE,
        (
            "哎呀，哈哈哈……\x01",
            "虽然有点不好意思，\x01",
            "但被女儿这么一亲，一下就打起精神了。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "好！虽然心中仍然很不安……\x01",
            "但为了家人，我今天也要努力工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C2C")

    Jump("loc_3DDF")

    label("loc_3C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3CA5")

    #C0228
    ChrTalk(
        0xFE,
        (
            "居然会发生这种事，\x01",
            "我已经不知道该怎么办了……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "但无论发生什么事，\x01",
            "我都会保护好柯洛娜和利玛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DDF")

    label("loc_3CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CB3")
    Jump("loc_3DDF")

    label("loc_3CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CC1")
    Jump("loc_3DDF")

    label("loc_3CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3CCF")
    Jump("loc_3DDF")

    label("loc_3CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3CDD")
    Jump("loc_3DDF")

    label("loc_3CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3CEB")
    Jump("loc_3DDF")

    label("loc_3CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CF9")
    Jump("loc_3DDF")

    label("loc_3CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3D07")
    Jump("loc_3DDF")

    label("loc_3D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3D58")

    #C0230
    ChrTalk(
        0xFE,
        (
            "呼……已经很久没有\x01",
            "这么轻松过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "全家团聚的感觉真好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DDF")

    label("loc_3D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D66")
    Jump("loc_3DDF")

    label("loc_3D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3DC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D81")
    Call(0, 17)
    Jump("loc_3DC3")

    label("loc_3D81")


    #C0232
    ChrTalk(
        0xFE,
        "啊，谢谢了。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "（大嚼）……\x01",
            "嗯，今天的饭菜\x01",
            "也非常美味啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC3")

    Jump("loc_3DDF")

    label("loc_3DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3DD6")
    Jump("loc_3DDF")

    label("loc_3DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3DDF")

    label("loc_3DDF")

    TalkEnd(0xFE)
    Return()

    # Function_18_3B7F end

    def Function_19_3DE3(): pass

    label("Function_19_3DE3")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3E4F")
    Call(0, 20)

    #C0234
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "喂，迪塔……\x01",
            "独立之后我们就能幸福了吗……？\x01",
            "……嗝……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4421")

    label("loc_3E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3E5D")
    Jump("loc_4421")

    label("loc_3E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3EB7")
    Call(0, 20)

    #C0236
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "梦想的国度在哪里啊……\x01",
            "王～赶快带我去吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4421")

    label("loc_3EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F6C")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2A")

    #C0238
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x01",
            "是谁啊，搞出这场雨的到底是谁……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "害得我都想上厕所了……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3F67")

    label("loc_3F2A")


    #C0240
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x01",
            "要是忍不住尿在裤子里，可该如何是好……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F67")

    Jump("loc_4421")

    label("loc_3F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3FBA")
    Call(0, 20)

    #C0241
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "我是今朝有酒……\x01",
            "今朝醉的……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "男人……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4421")

    label("loc_3FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4095")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_405C")

    #C0243
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "好不容易……挣到的……\x01",
            "一千米拉钞票啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "去巴鲁卡稍微玩了玩……等回过神时……\x01",
            "就已经全没了……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4090")

    label("loc_405C")


    #C0246
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "还我……还我米拉啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4090")

    Jump("loc_4421")

    label("loc_4095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_418D")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4134")

    #C0248
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝嗝。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "看见了没有，王～！\x01",
            "这下你就没话可说了吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "我这个顶梁柱……\x01",
            "赚到钱了……\x01",
            "呜哇，好想吐……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4188")

    label("loc_4134")


    #C0251
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "我这个顶梁柱……\x01",
            "赚到钱了……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "但房租还得再等等……\x01",
            "呜哇，好想吐……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4188")

    Jump("loc_4421")

    label("loc_418D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_426F")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4234")

    #C0253
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗯……？\x01",
            "哦哦，这不是有酒嘛。\x01",
            "干得好啊，王。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "（狂饮）…………\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "呜哇！？呸！呸……！\x01",
            "怎么回事！？这不是醋吗！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_426A")

    label("loc_4234")


    #C0256
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "这是谁干的……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "我饶不了他………呼……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_426A")

    Jump("loc_4421")

    label("loc_426F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_432C")
    Call(0, 20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42E8")

    #C0258
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "什么？已经没钱了～？\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "没办法……只能去做\x01",
            "一天短工了……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4327")

    label("loc_42E8")


    #C0261
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "没办法……只能去做\x01",
            "一天短工了……\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4327")

    Jump("loc_4421")

    label("loc_432C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4382")
    Call(0, 20)

    #C0263
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒……酒……\x01",
            "我最好的朋友～就是酒……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4421")

    label("loc_4382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_43D6")
    Call(0, 20)

    #C0265
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "喂，王～！\x01",
            "怎么还没把酒给我拿来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4421")

    label("loc_43D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4421")
    Call(0, 20)

    #C0267
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "嗝……嗝……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x8),
            "酒……酒～\x01",
            "……快给我拿酒来……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4421")

    TalkEnd(0x14)
    Return()

    # Function_19_3DE3 end

    def Function_20_4425(): pass

    label("Function_20_4425")

    SetChrName("")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧关着，\x01",
            "但可以听到里面的声音。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Return()

    # Function_20_4425 end

    def Function_21_4458(): pass

    label("Function_21_4458")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4477")
    Call(0, 9)
    Jump("loc_44DF")

    label("loc_4477")


    #C0270
    ChrTalk(
        0x9,
        (
            "坦特斯先生也是啊，看到您\x01",
            "这么有精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x9,
        (
            "说心里话，我对这里的\x01",
            "各位居民真是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44DF")

    Jump("loc_452D")

    label("loc_44E4")


    #C0272
    ChrTalk(
        0x9,
        (
            "我一定会在今天上交\x01",
            "迁居登记表。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        "给你们添了麻烦，真是不好意思。\x02",
    )

    CloseMessageWindow()

    label("loc_452D")

    TalkEnd(0xFE)
    Return()

    # Function_21_4458 end

    def Function_22_4531(): pass

    label("Function_22_4531")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4594")

    #C0274
    ChrTalk(
        0xFE,
        "啊，请问是哪位？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "赈济的食物还要\x01",
            "再过一段时间才能做好，\x01",
            "请再等等吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45DC")

    label("loc_4594")

    OP_4B(0xB, 0x0)

    #C0276
    ChrTalk(
        0xB,
        (
            "好了，想想晚上\x01",
            "该做什么\x01",
            "赈济菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x10,
        "嗯，做什么好呢？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0x0)

    label("loc_45DC")

    TalkEnd(0xFE)
    Return()

    # Function_22_4531 end

    def Function_23_45E0(): pass

    label("Function_23_45E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_465D")

    #C0278
    ChrTalk(
        0xFE,
        (
            "（老爸最近一直没酒喝，\x01",
            "  本以为他会很消沉，结果却……）\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "（真肉麻啊……\x01",
            "  完全不像平时的老爸……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4692")

    label("loc_465D")


    #C0280
    ChrTalk(
        0xFE,
        (
            "哈哈哈，老爸的酒已经基本喝完了，\x01",
            "钱也快用光了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4692")

    TalkEnd(0xFE)
    Return()

    # Function_23_45E0 end

    def Function_24_4696(): pass

    label("Function_24_4696")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_46A7")
    Jump("loc_471F")

    label("loc_46A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_46DC")

    #C0281
    ChrTalk(
        0xFE,
        (
            "（嘻嘻……\x01",
            "  还是喝醉时更好呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_471F")

    label("loc_46DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_46EA")
    Jump("loc_471F")

    label("loc_46EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_471F")

    #C0282
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "既然如此，就得\x01",
            "出去赚些钱啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_471F")

    TalkEnd(0xFE)
    Return()

    # Function_24_4696 end

    def Function_25_4723(): pass

    label("Function_25_4723")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4756")
    Call(0, 31)
    Return()

    label("loc_4756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetItemNumber('五谷味噌', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('魔兽兽肉', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('百药精酒', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('香油', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('黑暗菇', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('万能青葱', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你胡萝卜', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('热辣椒', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C4")
    Call(0, 33)
    Return()

    label("loc_47C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_4A12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 1)), scpexpr(EXPR_END)), "loc_4A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_END)), "loc_483D")

    #C0283
    ChrTalk(
        0x13,
        (
            "嗯，有这么多材料，\x01",
            "应该足够用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x13,
        (
            "真是太感谢你们了，\x01",
            "大家肯定也会很高兴的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A0D")

    label("loc_483D")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "确认所需食材\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49AF")

    #C0285
    ChrTalk(
        0x13,
        (
            "哦，还要再确认一次\x01",
            "需要的食材吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x13,
        (
            "首先是１０个『五谷味噌』，\x01",
            "１０个『魔兽兽肉』。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x13,
        (
            "接下来是１０瓶『百药精酒』\x01",
            "和１０瓶『香油』。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x13,
        (
            "此外，还需要３０个『黑暗菇』\x01",
            "和３０根『万能青葱』。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x13,
        (
            "最后就是３０根『迷你胡萝卜』\x01",
            "和３０个『热辣椒』。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x13,
        (
            "总共就是以上这些，\x01",
            "麻烦你们啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A0D")

    label("loc_49AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A0D")

    #C0291
    ChrTalk(
        0x13,
        (
            "这次的赈济菜式\x01",
            "是『猪骨汤』。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x13,
        (
            "里面含有肉类和蔬菜，\x01",
            "营养价值\x01",
            "非常高。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A0D")

    Jump("loc_4A73")

    label("loc_4A12")


    #C0293
    ChrTalk(
        0x13,
        (
            "唔……现有的食材太少了，\x01",
            "做出的食物恐怕又会被\x01",
            "瞬间分光的。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x13,
        (
            "能不能再往里面\x01",
            "掺点水呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A73")

    TalkEnd(0xFE)
    Return()

    # Function_25_4723 end

    def Function_26_4A77(): pass

    label("Function_26_4A77")

    TalkBegin(0xFE)
    OP_4B(0x15, 0xFF)
    OP_4B(0x11, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B33")

    #C0295
    ChrTalk(
        0x15,
        (
            "王，小丫头，你们两个听好，\x01",
            "一定要乖乖待在房间里。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x15,
        (
            "爸爸我一定会保护好自己的\x01",
            "宝贝儿子和儿子的好朋友。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0297
    ChrTalk(
        0x11,
        "（好肉麻啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4B74")

    label("loc_4B33")


    #C0298
    ChrTalk(
        0x15,
        (
            "王，小丫头，\x01",
            "我一定会保护好你们两个的。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x11,
        "（真啰嗦……）\x02",
    )

    CloseMessageWindow()

    label("loc_4B74")

    OP_4C(0x15, 0xFF)
    OP_4C(0x11, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_26_4A77 end

    def Function_27_4B80(): pass

    label("Function_27_4B80")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B95")
    Call(0, 28)
    Jump("loc_4CDB")

    label("loc_4B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C5A")

    #C0300
    ChrTalk(
        0xF,
        (
            "#01803F好了，我也该准备一下，\x01",
            "动身去市政府了……\x02\x03",

            "#01802F各位，关于谢莉小姐的事情，\x01",
            "谢谢你们的提醒。\x02\x03",

            "#01806F我本来就已经常被\x01",
            "伊莉娅小姐骚扰了……\x01",
            "一定会小心提防谢莉小姐的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4CDB")

    label("loc_4C5A")


    #C0301
    ChrTalk(
        0xF,
        (
            "#01802F各位，关于谢莉小姐的事情，\x01",
            "谢谢你们的提醒。\x02\x03",

            "#01806F我本来就已经常被\x01",
            "伊莉娅小姐骚扰了……\x01",
            "一定会小心提防谢莉小姐的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDB")

    TalkEnd(0xFE)
    Return()

    # Function_27_4B80 end

    def Function_28_4CDF(): pass

    label("Function_28_4CDF")

    EventBegin(0x0)
    Fade(500)
    OP_93(0xF, 0xB4, 0x0)
    OP_4B(0xF, 0xFF)
    OP_68(-1970, 1230, 54740, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17780, 0)
    SetChrPos(0x101, -1680, 30, 54360, 0)
    SetChrPos(0x102, -2670, 30, 54080, 0)
    SetChrPos(0x103, -620, 30, 54080, 0)
    SetChrPos(0x104, -1660, 30, 52940, 0)
    SetChrPos(0x109, -2910, 30, 52790, 0)
    SetChrPos(0x105, -330, 30, 52680, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0302
    ChrTalk(
        0xF,
        "#01802F啊，各位，你们好。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#12P#00000F哦，莉夏，\x01",
            "你在家啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xF,
        (
            "#01802F嗯，我今天下午有事\x01",
            "要去市政府，\x01",
            "所以请了假。\x02\x03",

            "啊……缇欧终于\x01",
            "回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x103,
        (
            "#12P#00202F是的，昨天刚刚\x01",
            "回到支援科。\x02\x03",

            "#00204F听说彩虹剧团昨晚举行了\x01",
            "招待各国首脑的演出……\x01",
            "真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x102,
        "#12P#00100F呵呵，昨晚肯定很紧张吧？\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xF,
        (
            "#01809F哈哈，确实和平时表演的\x01",
            "感觉有些不同呢。\x02\x03",

            "#01804F修利虽然只扮演配角，\x01",
            "但毕竟是初次登台演出，\x01",
            "所以紧张得不得了……\x02\x03",

            "#01802F不过，伊莉娅小姐倒是\x01",
            "和平时完全一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#12P#00309F哈哈，伊莉娅小姐的字典里\x01",
            "根本就没有紧张二字吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xF,
        (
            "#01804F嗯，只要登上舞台，\x01",
            "伊莉娅小姐瞬间就会变得无比专注……\x02\x03",

            "#01802F呵呵，像我这样的人，\x01",
            "恐怕永远都无法超越她。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x109,
        (
            "#12P#10103F嗯……对演员来说，\x01",
            "伊莉娅小姐确实是个极高的目标呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，她毕竟是被称为\x01",
            "真正天才的超级明星啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#12P#00000F不过，我倒觉得莉夏总有一天\x01",
            "可以追上伊莉娅小姐的脚步。\x02\x03",

            "#00004F你昨天稳稳当当地接住了\x01",
            "从吊灯上掉下来的小猫，\x01",
            "动作相当轻盈流畅。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xF,
        (
            "#01809F哈哈……谢谢称赞。\x02\x03",

            "#01802F不过，那只是下意识地\x01",
            "动了起来而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    #C0314
    ChrTalk(
        0xF,
        (
            "#01803F对了，昨天那个女孩……\x01",
            "是叫谢莉吧？\x02\x03",

            "#01802F听说是兰迪先生的堂妹……\x01",
            "她到底是个什么样的人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#00005F这、这个嘛……\x02\x03",

            "#00003F（如果说出不该说的话，\x01",
            "  说不定会把莉夏也\x01",
            "  卷进来……）\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#12P#00304F……哈哈，就如你所见，\x01",
            "是个超级疯丫头啊。\x02\x03",

            "#00302F那家伙很麻烦，如果被她缠上了，\x01",
            "就想办法脱身逃掉吧。\x02\x03",

            "#00309F看样子，她好像\x01",
            "挺喜欢莉夏小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，如果不加防范，\x01",
            "说不定会像艾莉一样\x01",
            "惨遭毒手哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x102,
        (
            "#12P#00113F真、真是的……\x01",
            "赶快把那件事忘掉吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    #C0319
    ChrTalk(
        0xF,
        (
            "#01808F（血腥谢莉……）\x02\x03",

            "#01803F（今后说不定会和\x01",
            "  作为『银』的我……）\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#12P#00005F……怎么了，莉夏？\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xF,
        (
            "#01802F……呵呵，没什么，\x01",
            "谢谢你们的提醒。\x02\x03",

            "#01806F我本来就已经常被\x01",
            "伊莉娅小姐骚扰了……\x01",
            "一定会小心提防谢莉小姐的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0322
    ChrTalk(
        0x109,
        "#12P#10112F哈、哈哈……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#12P#00206F莉夏小姐也很不容易呢。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1CB, 4)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_93(0xF, 0x0, 0x0)
    OP_4C(0xF, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1680, 30, 54360, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_4CDF end

    def Function_29_559F(): pass

    label("Function_29_559F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x90, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55CD")
    Call(0, 34)
    Return()

    label("loc_55CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55F6")
    Call(0, 30)
    Return()

    label("loc_55F6")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5607")
    Jump("loc_5691")

    label("loc_5607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5632")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5691")

    label("loc_5632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5640")
    Jump("loc_5691")

    label("loc_5640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_566B")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5691")

    label("loc_566B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5691")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5691")

    TalkEnd(0xFF)
    Return()

    # Function_29_559F end

    def Function_30_5695(): pass

    label("Function_30_5695")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3530, 1300, 3570, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 3800, 0, 3500, 90)
    SetChrPos(0x102, 3500, 0, 4800, 90)
    SetChrPos(0x109, 2800, 0, 3200, 90)
    SetChrPos(0x105, 2300, 0, 4500, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0327
    ChrTalk(
        0x101,
        (
            "#6P#00000F旧城区的莲花公馆……\x01",
            "嗯，应该就是这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#00000F打扰一下，\x01",
            "请问有人在吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    #C0329
    ChrTalk(
        0x109,
        "#6P#10103F没有反应啊……\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        "#6P#00100F门锁着吗？\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0331
    ChrTalk(
        0x101,
        (
            "#11P#00001F嗯，紧紧锁着。\x02\x03",

            "#00003F但我总觉得里面好像有人，\x01",
            "是错觉吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x102,
        "#6P#00105F是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x105,
        (
            "#6P#10303F说不定只是故意不吭声。\x02\x03",

            "#10300F如果真的是这样，又该怎么办？\x01",
            "要强行破门而入吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#11P#00003F嗯，如果没有其它办法，\x01",
            "也只能选择这种最糟糕的手段了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 50, 0)
    Sound(857, 0, 80, 0)
    Sleep(200)
    Sound(856, 0, 30, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x5DC)

    #C0335
    ChrTalk(
        0x109,
        "#6P#10105F刚才的是……？\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        "#6P#00000F嗯，像是餐具之类的东西发出的声音。\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x102,
        (
            "#6P#00103F看来里面\x01",
            "真的有人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#6P#00003F我再喊一次看看吧。\x02\x03",

            "#00001F打扰一下！\x01",
            "里面有人吧！？\x02\x03",

            "我们想问您几个问题！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)

    #C0339
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，是打算死撑到底吗？\x02\x03",

            "#10302F说不定会从\x01",
            "窗户逃出去吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x101,
        (
            "#6P#00006F唔……如果真是那样，\x01",
            "可就有点麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(1000)
    OP_68(3720, 1000, 2530, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16200, 3000)
    SetChrPos(0x8, 8000, 0, -3500, 0)
    SetChrPos(0x9, 8000, 0, -2500, 0)

    def lambda_5BCC():
        OP_95(0x9, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5BCC)
    Sleep(100)

    def lambda_5BE9():
        OP_95(0x8, 8000, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5BE9)
    Sleep(100)
    WaitChrThread(0x9, 1)

    def lambda_5C0A():
        OP_95(0x9, 3060, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5C0A)
    Sleep(100)
    WaitChrThread(0x8, 1)

    def lambda_5C2B():
        OP_95(0x8, 4059, 0, 0, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C2B)
    WaitChrThread(0x9, 1)

    def lambda_5C49():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5C49)
    WaitChrThread(0x8, 1)
    Sleep(100)

    def lambda_5C5D():
        OP_93(0x8, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5C5D)
    WaitChrThread(0x8, 1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0341
    ChrTalk(
        0x8,
        (
            "#12P怎么吵闹个没完没了……\x01",
            "是你们几个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x9,
        "#12P到底发生什么事了？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5D15():
        OP_93(0x101, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D15)
    Sleep(10)

    def lambda_5D25():
        OP_93(0x102, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D25)
    Sleep(10)

    def lambda_5D35():
        OP_93(0x109, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5D35)
    Sleep(10)

    def lambda_5D45():
        OP_93(0x105, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D45)
    Sleep(10)

    #C0343
    ChrTalk(
        0x101,
        (
            "#5P#00005F啊，抱、抱歉。\x02\x03",

            "#00000F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的人……\x02\x03",

            "#00003F有点事情要找\x01",
            "这个房间的住户。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        (
            "#5P#00105F请问二位认识\x01",
            "这个房间的住户吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "#12P嗯，当然\x01",
            "认识……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x2D, 0x0)

    #C0346
    ChrTalk(
        0x9,
        (
            "#12P唔……你们可以先把\x01",
            "事情说给我听听吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        "#5P#00000F好的，其实是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0348
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将调查可疑住户的情况\x01",
            "做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()

    #C0349
    ChrTalk(
        0x8,
        (
            "#12P原来如此……\x01",
            "所以你们要来调查\x01",
            "现在的住户啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x9,
        (
            "#12P唔～我好像给你们\x01",
            "添了麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x109,
        "#5P#10105F哎，这是什么意思……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x0)

    #C0352
    ChrTalk(
        0x9,
        (
            "#12P实不相瞒，其实我就是\x01",
            "这个房间的前任住户\x01",
            "盖特纳。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        "#5P#00005F原、原来是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x9,
        (
            "#12P嗯，听各位的意思，\x01",
            "我必须要去上交\x01",
            "迁居登记表吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x9,
        "#12P现在去交，应该还不晚吧……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x9,
        (
            "#12P总之，我一定会在\x01",
            "今天之内上交登记表的。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#5P#00100F好的，您愿意配合，\x01",
            "真是十分感谢。\x02\x03",

            "#00103F另外，可以顺便请教一下\x01",
            "您的迁居原因吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        (
            "#12P哦，简单来说，\x01",
            "可以用『缘分』一词来概括。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x9,
        (
            "#12P大概在一年前，\x01",
            "我因为生意失败，\x01",
            "被迫住进了这个公寓……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        (
            "#12P当年曾经一起经商的伙伴\x01",
            "知晓了我的情况之后，\x01",
            "邀请我去和他一起做生意。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x9,
        (
            "#12P所以我在两周前\x01",
            "移居到那位伙伴所在的\x01",
            "共和国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x109,
        "#5P#10105F既然如此，您今天为何会在这里？\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x9,
        (
            "#12P哦，当时一直承蒙各位邻居的照顾，\x01",
            "这次是特地回来向大家道谢的。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x9,
        (
            "#12P在那段时间，\x01",
            "各位对我真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x8,
        "#12P呵呵，你真是客气。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#5P#00004F原来如此，我们已经了解\x01",
            "盖特纳先生的情况了。\x02\x03",

            "#00000F那么，现在的\x01",
            "新住户又是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        "#12P唔……这个嘛。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x102,
        (
            "#5P#00105F……是不是有什么\x01",
            "不太方便说的话？\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x8,
        (
            "#12P不，主要还在于\x01",
            "他自己的心理问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        "#12P让我来吧……\x02",
    )

    CloseMessageWindow()

    def lambda_6385():
        OP_9B(0x1, 0x8, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6385)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_63A1():
        OP_9B(0x1, 0x101, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63A1)
    Sleep(50)

    def lambda_63B9():
        OP_9B(0x1, 0x102, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63B9)
    Sleep(50)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_63D8():
        OP_9B(0x1, 0x109, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63D8)
    Sleep(50)

    def lambda_63F0():
        OP_9B(0x1, 0x105, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63F0)
    Sleep(50)
    OP_93(0x9, 0x2D, 0x0)
    WaitChrThread(0x8, 1)
    OP_9B(0x0, 0x8, 0x5A, 0x3E8, 0x3E8, 0x0)
    Sleep(100)
    Sound(808, 0, 100, 0)
    Sleep(500)

    #C0371
    ChrTalk(
        0x8,
        (
            "#6P我是坦特斯……\x01",
            "你在里面吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        (
            "#6P如果听到了我们刚才说的话，\x01",
            "能不能把门打开？\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#6P他们都是警察。\x01",
            "就算知道你的名字，\x01",
            "也不会有什么麻烦的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    Sound(806, 0, 100, 0)
    Sleep(300)

    #C0374
    ChrTalk(
        0x102,
        "#6P#00105F啊……\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x8,
        "#6P哦哦，他开门了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0376
    ChrTalk(
        0x8,
        (
            "#5P那就请各位尽量在不引起乱子的前提下，\x01",
            "进去确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        "#12P#00000F好的，谢谢您的帮助。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(52110, 1430, -1830, 0)
    MoveCamera(73, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    SetChrPos(0xA, 55000, 30, -2100, 90)
    OP_4B(0xA, 0xFF)
    SetChrPos(0x101, 48300, 30, 100, 90)
    SetChrPos(0x102, 48300, 30, 100, 90)
    SetChrPos(0x109, 48300, 30, 100, 90)
    SetChrPos(0x105, 48300, 30, 100, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_668F():
        OP_95(0x101, 51800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_668F)

    def lambda_66A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66A9)
    Sleep(500)

    def lambda_66BD():
        OP_95(0x102, 51800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_66BD)

    def lambda_66D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66D7)
    Sleep(500)

    def lambda_66EB():
        OP_95(0x109, 50800, 30, -800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_66EB)

    def lambda_6705():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6705)
    Sleep(500)

    def lambda_6719():
        OP_95(0x105, 50800, 30, 200, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6719)

    def lambda_6733():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6733)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_674B():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_674B)
    WaitChrThread(0x102, 1)

    def lambda_675C():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_675C)
    WaitChrThread(0x109, 1)

    def lambda_676D():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_676D)
    WaitChrThread(0x105, 1)

    def lambda_677E():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_677E)

    #C0378
    ChrTalk(
        0x101,
        "#6P#00000F打扰了。\x02",
    )

    CloseMessageWindow()

    #N0379
    NpcTalk(
        0xA,
        "？？？",
        "#11P你们是来嘲笑我的吗？\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x101,
        "#12P#00005F什么……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #N0381
    NpcTalk(
        0xA,
        "？？？",
        (
            "#11P我在问，你们是来\x01",
            "嘲笑我的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #N0382
    NpcTalk(
        0xA,
        "？？？",
        (
            "#11P来嘲笑已经落魄至此，\x01",
            "却还对过去风光\x01",
            "念念不忘的我！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0383
    ChrTalk(
        0x101,
        "#6P#00011F这、这个人是……\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x102,
        (
            "#6P#00103F……是前帝国派议员盖巴尔啊。\x02\x03",

            "#00101F渎职行为被曝光之后，\x01",
            "他不是一直在乌尔斯拉医院\x01",
            "住院吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xA,
        (
            "#11P哼、哼！你们果然\x01",
            "认识我啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xA,
        (
            "#11P特地追到这里来，\x01",
            "到底想干什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xA,
        "#11P如、如你们所见，我可没钱。\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xA,
        (
            "#11P就连租住这个公寓的房租，\x01",
            "都是从老朋友那里东拼西借，\x01",
            "好不容易才凑够的。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xA,
        (
            "#11P哈，难道你们连我\x01",
            "那点小小的人脉关系\x01",
            "也想利用吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0390
    ChrTalk(
        0x102,
        (
            "#6P#00106F不是的，我们完全\x01",
            "没有那种想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#6P#00000F我们只是想\x01",
            "亲眼确认一下\x01",
            "您的情况。\x02\x03",

            "#00003F盖巴尔先生，请问……\x01",
            "您就是这个房间的\x01",
            "新住户吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xA,
        "#11P是、是啊……没错。\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x109,
        (
            "#6P#10106F呼，总算调查清楚了。\x02\x03",

            "#10100F原来这里并没有被人用于犯罪行为，\x01",
            "总算可以放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x105,
        (
            "#6P#10303F但您为何\x01",
            "要在表格里填一个\x01",
            "童话作家的名字？\x02\x03",

            "#10300F这实在太可疑了，\x01",
            "反倒会引起别人的注意啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#6P#00006F是啊，看到之后就觉得\x01",
            "这个住户最奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xA,
        "#11P哼、哼……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xA,
        (
            "#11P因为我一直都很喜欢\x01",
            "肖恩·阿尔纳姆。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xA,
        (
            "#11P当时一下就想到了这个名字，\x01",
            "然后就填上去了，\x01",
            "你们有意见吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0399
    ChrTalk(
        0x109,
        (
            "#6P#10112F是、是吗……\x01",
            "这真是有点意外。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x102,
        (
            "#6P#00103F不、不过，那位作者的作品\x01",
            "确实受到各年龄层读者的喜爱……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，这种反差\x01",
            "也挺有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#6P#00005F是、是吗……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0403
    ChrTalk(
        0xA,
        "#11P可恶……烦死了烦死了！\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xA,
        (
            "#11P你们的事情已经办完了吧！？\x01",
            "那就赶快给我出去！\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x102,
        (
            "#6P#00106F好、好的，打扰了。\x02\x03",

            "#00100F罗伊德，\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯。\x02\x03",

            "我们告辞了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1400", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_30_5695 end

    def Function_31_6EF6(): pass

    label("Function_31_6EF6")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1320, -56500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2600, 20, -55850, 90)
    SetChrPos(0x105, 2600, 20, -57050, 90)
    SetChrPos(0x104, 1400, 20, -56100, 90)
    SetChrPos(0x103, 1100, 20, -57150, 90)
    SetChrPos(0x102, 2790, 20, -54460, 135)
    SetChrPos(0x109, -90, 20, -56800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x13, 0xFF)
    OP_0D()

    #C0407
    ChrTalk(
        0x105,
        "#10300F嘿，亚泽尔。\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x101, 500)

    #C0408
    ChrTalk(
        0x13,
        "啊，瓦吉。\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x13,
        (
            "你莫非是来\x01",
            "帮忙的？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x105,
        "#10302F嗯，算是吧。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x101,
        (
            "#00000F你们正在准备用于赈济的\x01",
            "食物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x102,
        "#00100F有没有需要帮忙的地方？\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x13,
        "嗯，让我想想……\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x13,
        (
            "对了……\x01",
            "其实，我们做饭的食材\x01",
            "严重不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x13,
        (
            "如果可以，我想请你们\x01",
            "帮忙采购一些。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x104,
        (
            "#00300F采购食材吗？\x01",
            "没问题，小事一桩。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x103,
        (
            "#00205F你们需要哪些食材？\x01",
            "数量又是多少呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x13,
        (
            "哦，我现在就告诉你们，\x01",
            "请记好。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x13,
        (
            "首先是１０个『五谷味噌』，\x01",
            "１０个『魔兽兽肉』。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x13,
        (
            "接下来是１０瓶『百药精酒』\x01",
            "和１０瓶『香油』。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x13,
        (
            "此外，还需要３０个『黑暗菇』\x01",
            "和３０根『万能青葱』。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x13,
        (
            "最后就是３０根『迷你胡萝卜』\x01",
            "和３０个『热辣椒』。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x13,
        "总共就是以上这些。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0424
    ChrTalk(
        0x109,
        "#10106F数量可真不少呢。\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x13,
        (
            "是啊，因为大家\x01",
            "都很能吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x13,
        (
            "昨天的食物不够，有些人没能分到，\x01",
            "还引起了些许混乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x13,
        (
            "所以我们今天想尽量\x01",
            "避免那种情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        "#00003F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x105,
        (
            "#10300F对了，\x01",
            "你们到底在做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x13,
        (
            "哦，是可以温暖身心的\x01",
            "『猪骨汤』哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x13,
        (
            "做好之后，一定也会给\x01",
            "你们尝尝的。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        "#00100F呵呵，真让人期待。\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x13,
        (
            "对了对了，得把采购\x01",
            "食材的钱给你们。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0434
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    AddMira(500)

    #C0435
    ChrTalk(
        0x104,
        (
            "#00306F这、这好像……\x01",
            "完全不够吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x13,
        (
            "唔，抱歉啦，\x01",
            "我们的预算很紧张。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x13,
        (
            "剩下的部分就只能\x01",
            "请你们帮帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x109,
        (
            "#10100F没关系，不足的部分\x01",
            "就当作是我们的捐款吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x103,
        (
            "#00203F嗯，在这种状况下，\x01",
            "我们贡献些也是应该的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x103, 500)

    #C0440
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，既然决定了，\x01",
            "那就赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0441
    ChrTalk(
        0x101,
        (
            "#00000F嗯，这就去\x01",
            "采购食材吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 1)
    OP_29(0x8E, 0x1, 0x2)
    OP_93(0x13, 0x5A, 0x0)
    OP_4C(0x13, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2600, 20, -56450, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_6EF6 end

    def Function_32_762A(): pass

    label("Function_32_762A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7830")

    #C0442
    ChrTalk(
        0x8,
        (
            "哦，听说你们\x01",
            "正在帮忙采购\x01",
            "赈济食材？\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x8,
        (
            "太感谢了，\x01",
            "那就拜托你们啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0444
    ChrTalk(
        0x8,
        (
            "啊，对了，\x01",
            "如果可以，我还想\x01",
            "麻烦你们一件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x8,
        (
            "我需要浓缩了\x01",
            "苦西红柿成分的酱料……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x8,
        (
            "要是你们能找到，\x01",
            "可以给我\x01",
            "拿来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        (
            "有了那个，我就能\x01",
            "给大家做一锅特制的\x01",
            "『强壮苦番茄猪骨汤』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x101,
        (
            "#00005F酱料……？\x01",
            "直接用『苦西红柿』\x01",
            "不行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x8,
        (
            "哦，如果直接用苦西红柿，\x01",
            "烹饪时间就会相当久了。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x8,
        (
            "总之，你们有空时顺便找找就行了。\x01",
            "没有那东西也没什么关系的。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x102,
        "#00100F好的，我记下了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x196, 2)
    OP_29(0x8E, 0x1, 0x3)
    Jump("loc_790D")

    label("loc_7830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 5)), scpexpr(EXPR_END)), "loc_7895")

    #C0452
    ChrTalk(
        0xFE,
        (
            "哦，你们真的帮我找到\x01",
            "苦西红柿酱了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xFE,
        (
            "非常感谢。\x01",
            "这下就能让\x01",
            "大家打起精神了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_7895")


    #C0454
    ChrTalk(
        0x8,
        (
            "我需要浓缩了\x01",
            "苦西红柿成分的酱料……\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x8,
        (
            "要是你们能找到，\x01",
            "可以给我\x01",
            "拿来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x8,
        (
            "总之，你们有空时\x01",
            "顺便找找就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")

    TalkEnd(0x8)
    Return()

    # Function_32_762A end

    def Function_33_7911(): pass

    label("Function_33_7911")

    EventBegin(0x0)
    Fade(500)
    OP_68(2720, 1320, -56500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 2600, 20, -55850, 90)
    SetChrPos(0x105, 2600, 20, -57050, 90)
    SetChrPos(0x104, 1400, 20, -56100, 90)
    SetChrPos(0x103, 1100, 20, -57150, 90)
    SetChrPos(0x102, 2790, 20, -54460, 135)
    SetChrPos(0x109, -90, 20, -56800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x13, 0xFF)
    TurnDirection(0x13, 0x101, 0)
    OP_0D()

    #C0457
    ChrTalk(
        0x13,
        (
            "啊，你们已经\x01",
            "采购好食材了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交出食材\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7A95")

    #C0458
    ChrTalk(
        0x13,
        (
            "怎么？莫非还没\x01",
            "集齐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x13,
        (
            "等你们准备好之后\x01",
            "再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x5A, 0x0)
    OP_4C(0x13, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    label("loc_7A95")


    #C0460
    ChrTalk(
        0x101,
        "#00000F是的，请收下吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0461
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#20I五谷味噌　　　\x07\x00",
            "×１０\x01\x07\x02",

            "#20I魔兽兽肉　　　\x07\x00",
            "×１０\x01\x07\x02",

            "#20I百药精酒　　　\x07\x00",
            "×１０\x01\x07\x02",

            "#20I香油　　　　　\x07\x00",
            "×１０\x01\x07\x02",

            "#20I黑暗菇　　　　\x07\x00",
            "×３０\x01\x07\x02",

            "#20I万能青葱　　　\x07\x00",
            "×３０\x01\x07\x02",

            "#20I迷你胡萝卜　　\x07\x00",
            "×３０\x01\x07\x02",

            "#20I热辣椒　　　　\x07\x00",
            "×３０　交出去了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    SubItemNumber('五谷味噌', 10)
    SubItemNumber('魔兽兽肉', 10)
    SubItemNumber('百药精酒', 10)
    SubItemNumber('香油', 10)
    SubItemNumber('黑暗菇', 30)
    SubItemNumber('万能青葱', 30)
    SubItemNumber('迷你胡萝卜', 30)
    SubItemNumber('热辣椒', 30)

    #C0462
    ChrTalk(
        0x13,
        "嗯，正是我要的食材。\x02",
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x13,
        (
            "真是麻烦你们了，\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('苦西红柿酱', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DE8")
    OP_2C(0x8E, 0x1)

    #C0464
    ChrTalk(
        0x103,
        (
            "#00205F对了，罗伊德前辈……\x01",
            "把那个也交出去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0465
    ChrTalk(
        0x101,
        (
            "#00005F哦，说的对。\x02\x03",

            "#00000F请收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0466
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '苦西红柿酱'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出去了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('苦西红柿酱', 1)

    #C0467
    ChrTalk(
        0x13,
        "这是……？\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，这是坦特斯先生\x01",
            "让我们找的东西。\x02\x03",

            "#10302F听说用上这个，\x01",
            "就能做出特殊的猪骨汤。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x13,
        (
            "哦哦，\x01",
            "我也听他说过。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x13,
        (
            "好，我去向坦特斯先生\x01",
            "请教一下使用方法，\x01",
            "一定会用到它的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 4)

    label("loc_7DE8")


    #C0471
    ChrTalk(
        0x104,
        (
            "#00300F那我们的任务\x01",
            "就算结束了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x13,
        (
            "嗯，辛苦大家了。\x01",
            "多亏有你们帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x13,
        (
            "等外面的工作告一段落之后，\x01",
            "我们就开始向大家分发赈济食物。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x13,
        (
            "到时候，你们也一定\x01",
            "要来品尝哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x102,
        "#00100F嗯，好的。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F3A")

    #C0476
    ChrTalk(
        0x101,
        (
            "#00004F好，接下来的事情\x01",
            "交给他们就可以了。\x02\x03",

            "#00000F我们已经把所有任务完成了，\x01",
            "这就去向阿巴斯报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8E, 0x1, 0xC)
    Jump("loc_7F8C")

    label("loc_7F3A")


    #C0477
    ChrTalk(
        0x101,
        (
            "#00004F好，接下来的事情\x01",
            "交给他们就可以了。\x02\x03",

            "#00000F我们再去其它地方\x01",
            "看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F8C")

    SetScenarioFlags(0x196, 3)
    OP_93(0x13, 0x5A, 0x0)
    OP_4C(0x13, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2600, 20, -56450, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_33_7911 end

    def Function_34_7FC6(): pass

    label("Function_34_7FC6")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4030, 1300, 3430, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 4790, 0, 4019, 90)
    SetChrPos(0x102, 3300, 0, 4710, 90)
    SetChrPos(0x103, 2990, 0, 3570, 90)
    SetChrPos(0x104, 1690, 0, 5630, 90)
    SetChrPos(0x109, 1230, 0, 4280, 90)
    SetChrPos(0x105, 1640, 0, 3020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0478
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0479
    ChrTalk(
        0x101,
        (
            "#00000F打扰了，盖巴尔先生。\x01",
            "请问您在里面吗？\x02",
        )
    )

    CloseMessageWindow()
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

    #C0480
    ChrTalk(
        0x101,
        "#00003F……好像不在呢。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x102,
        (
            "#00100F这里应该是\x01",
            "盖巴尔先生的房间没错啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3910, 1300, 1040, 3000)
    SetChrPos(0x8, 8000, 0, -3500, 0)
    OP_4B(0x8, 0xFF)
    OP_95(0x8, 8000, 0, 0, 2000, 0x0)
    OP_95(0x8, 4059, 0, 0, 2000, 0x0)
    OP_93(0x8, 0x0, 0x1F4)

    #C0482
    ChrTalk(
        0x8,
        (
            "你们在做\x01",
            "什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8293():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8293)
    Sleep(50)

    def lambda_82A3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82A3)
    Sleep(50)

    def lambda_82B3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_82B3)
    Sleep(50)

    def lambda_82C3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_82C3)
    Sleep(50)

    def lambda_82D3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_82D3)
    Sleep(50)

    def lambda_82E3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_82E3)
    Sleep(300)

    #C0483
    ChrTalk(
        0x8,
        (
            "哦，你们是之前的……\x01",
            "特别任务支援科吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3630, 1300, 2880, 2000)
    OP_95(0x8, 3800, 0, 1500, 1500, 0x0)
    OP_6F(0x1)

    #C0484
    ChrTalk(
        0x105,
        (
            "#10302F呵呵……\x01",
            "你好，坦特斯先生。\x02\x03",

            "请问住在这里的\x01",
            "那位前议员大叔\x01",
            "去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x8,
        (
            "哦，他上个星期就出门了，\x01",
            "也不知道去了哪里……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x8,
        "怎么？发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#00000F不，其实是这样……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0488
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将接受了阿鲁姆的委托，\x01",
            "正在寻找盖巴尔的情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0489
    ChrTalk(
        0x8,
        (
            "哦哦，就是从利贝尔远道而来的\x01",
            "那对夫妇啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x8,
        (
            "呵呵，盖巴尔先生\x01",
            "真有福气啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        (
            "#00205F老爷爷，您也见过\x01",
            "阿鲁姆先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x8,
        (
            "其实他们上个星期\x01",
            "就来过这所公寓了，\x01",
            "当时我们还聊了很久。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x8,
        (
            "可惜的是，盖巴尔先生\x01",
            "正好在他们到来之前出了门，\x01",
            "然后就不知所踪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x8,
        (
            "我当时也没有问，\x01",
            "不知他到底去了哪里……\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        "#00306F唉，毫无线索吗？\x02",
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x109,
        "#10106F这可麻烦了啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0497
    ChrTalk(
        0x8,
        "哦，对了……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x8,
        (
            "有个人也许会\x01",
            "知道盖巴尔先生的\x01",
            "行踪。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        "#00005F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x8,
        (
            "嗯，我听盖巴尔先生说过，\x01",
            "在他当议员的时候，\x01",
            "住在西街的一个人曾对他多方照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x8,
        (
            "当初搬迁到这里时，\x01",
            "那个人也帮了他很多忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x8,
        (
            "我记得那个人住在雷、雷……\x01",
            "好像住在一个叫\x01",
            "雷什么的公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x103,
        (
            "#00203F雷什么……？\x01",
            "总觉得有点\x01",
            "耳熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x101,
        (
            "#00003F总之，我们先去西街\x01",
            "找找看吧。\x02\x03",

            "#00000F老爷爷，\x01",
            "多谢您的帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x8,
        "哪里哪里，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x8,
        (
            "请你们多加努力，让盖巴尔先生\x01",
            "和他的儿子儿媳见上一面吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x90, 0x1, 0x1)
    SetScenarioFlags(0x19A, 7)
    SetScenarioFlags(0x1, 2)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 1030, 0, 1180, 225)
    SetChrPos(0x8, 3800, 0, 1500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_34_7FC6 end

    SaveToFile()

Try(main)
