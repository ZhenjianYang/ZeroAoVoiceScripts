from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1040.bin",                # FileName
        "c1040",                    # MapName
        "c1040",                    # Location
        0x0015,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 21, 0, 6, 0, 7],
    )

    BuildStringList((
        "c1040",                  # 0
        "玛西",                   # 1
        "莎丽娜",                 # 2
        "尤格特",                 # 3
        "克拉莉丝",               # 4
        "本德",                   # 5
        "库雷优",                 # 6
        "萨妮塔",                 # 7
        "玛丽",                   # 8
        "塞比娅",                 # 9
        "乌娜",                   # 10
        "亚泽尔",                 # 11
    ))

    AddCharChip((
        "chr/ch27600.itc",                   # 00
        "chr/ch33300.itc",                   # 01
        "chr/ch34400.itc",                   # 02
        "chr/ch39000.itc",                   # 03
        "chr/ch27602.itc",                   # 04
        "chr/ch33302.itc",                   # 05
        "chr/ch34200.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch21802.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch21800.itc",                   # 0B
        "chr/ch34202.itc",                   # 0C
        "chr/ch34402.itc",                   # 0D
        "chr/ch20500.itc",                   # 0E
        "apl/ch50375.itc",                   # 0F
    ))

    DeclNpc(48880,   29,      -55000,  135,  261,  0x0, 0,   11,  0,   0,   2,   0,   14,  255,  0)
    DeclNpc(3789,    0,       55279,   90,   261,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-2410,   29,      52169,   225,  261,  0x0, 0,   6,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(3660,    29,      -56599,  90,   261,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(53729,   0,       52729,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(53729,   0,       50729,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(53729,   0,       51729,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(48349,   0,       3900,    90,   261,  0x0, 0,   3,   0,   0,   3,   0,   19,  255,  0)
    DeclNpc(48880,   29,      -55000,  135,  389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(48880,   29,      -55000,  135,  389,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-17389,  -300,    16750,   90,   389,  0x0, 0,   15,  0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 28,  52.0,                  -6.980000019073486,    -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -26.0,                 3.490000009536743,     0.20000000298023224,   1.0])

    DeclActor(51870,   0,       5760,    2000,    51870,   2000,    5760,    0x007C, 0,  29, 0x0000)

    ChipFrameInfo(772, 0)                                        # 0

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_3E7",          # 02, 2
        "Function_3_412",          # 03, 3
        "Function_4_43D",          # 04, 4
        "Function_5_468",          # 05, 5
        "Function_6_493",          # 06, 6
        "Function_7_D35",          # 07, 7
        "Function_8_DE9",          # 08, 8
        "Function_9_238E",         # 09, 9
        "Function_10_2615",        # 0A, 10
        "Function_11_347E",        # 0B, 11
        "Function_12_353D",        # 0C, 12
        "Function_13_3AFE",        # 0D, 13
        "Function_14_3E1F",        # 0E, 14
        "Function_15_49E4",        # 0F, 15
        "Function_16_4B15",        # 10, 16
        "Function_17_5532",        # 11, 17
        "Function_18_5E23",        # 12, 18
        "Function_19_6827",        # 13, 19
        "Function_20_6A9E",        # 14, 20
        "Function_21_6BA3",        # 15, 21
        "Function_22_6C48",        # 16, 22
        "Function_23_809F",        # 17, 23
        "Function_24_8982",        # 18, 24
        "Function_25_8AF7",        # 19, 25
        "Function_26_8D49",        # 1A, 26
        "Function_27_9232",        # 1B, 27
        "Function_28_9DAA",        # 1C, 28
        "Function_29_9DF5",        # 1D, 29
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E6")
    OP_94(0xFE, 0xFFFFF204, 0xCD3C, 0xFFFFFA24, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_1_3BC")

    label("loc_3E6")

    Return()

    # Function_1_3BC end

    def Function_2_3E7(): pass

    label("Function_2_3E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_411")
    OP_94(0xFE, 0xBC16, 0xFFFF213A, 0xBDCE, 0xFFFF2FB8, 0x3E8)
    Sleep(300)
    Jump("Function_2_3E7")

    label("loc_411")

    Return()

    # Function_2_3E7 end

    def Function_3_412(): pass

    label("Function_3_412")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_94(0xFE, 0xC8B4, 0xC9C2, 0xD426, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_3_412")

    label("loc_43C")

    Return()

    # Function_3_412 end

    def Function_4_43D(): pass

    label("Function_4_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_467")
    OP_94(0xFE, 0xB734, 0xDAC0, 0xAF64, 0xD642, 0x3E8)
    Sleep(300)
    Jump("Function_4_43D")

    label("loc_467")

    Return()

    # Function_4_43D end

    def Function_5_468(): pass

    label("Function_5_468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_492")
    OP_94(0xFE, 0xC832, 0xFFFF3396, 0xD188, 0xFFFF2036, 0x3E8)
    Sleep(300)
    Jump("Function_5_468")

    label("loc_492")

    Return()

    # Function_5_468 end

    def Function_6_493(): pass

    label("Function_6_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xD, 50370, 30, 55730, 0)
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xF, 54250, 30, 52430, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    Jump("loc_D25")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5D2")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5800, 30, -100, 270)
    SetChrPos(0xB, 5800, 30, -1290, 270)
    SetChrPos(0x9, -340, 30, 55650, 270)
    SetChrPos(0xA, -1340, 30, 55650, 90)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 50330, 30, 52130, 90)
    SetChrPos(0xD, 51660, 30, 52130, 270)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xE, 46100, 500, 54620, 180)
    SetChrChipByIndex(0xE, 0xD)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xF, 47200, 20, 53740, 300)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_D25")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_63B")
    SetChrPos(0xD, 50370, 30, 55730, 0)
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xF, 54250, 30, 52430, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    Jump("loc_D25")

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_652")
    SetChrFlags(0xB, 0x80)

    label("loc_652")

    SetChrPos(0xD, 50370, 30, 55730, 0)
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xE, 46100, 500, 54620, 180)
    SetChrChipByIndex(0xE, 0xD)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xF, 47200, 20, 53740, 300)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_D25")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_73D")
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 49270, 130, 53870, 90)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xF, 47420, 0, 3460, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 48680, 0, 3250, 270)
    Jump("loc_D25")

    label("loc_73D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7CE")
    SetChrPos(0xC, 45360, 500, 54620, 180)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrSubChip(0xC, 0x1)
    SetChrPos(0xE, 46100, 500, 54620, 180)
    SetChrChipByIndex(0xE, 0xD)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrSubChip(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x40)
    SetChrPos(0xF, 51660, 0, 51090, 315)
    BeginChrThread(0xF, 0, 0, 3)
    SetChrPos(0xD, 48180, 0, 4450, 270)
    SetChrFlags(0xD, 0x10)
    Jump("loc_D25")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_863")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, 1230, 30, 54660, 225)
    SetChrPos(0xA, 1600, 130, 53880, 270)
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 0xC)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 50370, 30, 55730, 45)
    SetChrPos(0xF, 51660, 0, 51090, 315)
    BeginChrThread(0xF, 0, 0, 3)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    TurnDirection(0xE, 0xF, 0)
    Jump("loc_D25")

    label("loc_863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_94E")
    SetChrPos(0x9, 760, 0, 55810, 270)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xA, -1320, 0, 56010, 90)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 52980, 30, 55720, 45)
    SetChrPos(0xF, 54250, 30, 52430, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F6")
    SetChrFlags(0xE, 0x10)

    label("loc_8F6")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, 49050, 30, -54780, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x10, 49280, 30, -52920, 180)
    SetChrPos(0x11, 52690, 30, -54950, 135)
    SetChrFlags(0x10, 0x10)
    BeginChrThread(0x11, 0, 0, 5)
    Jump("loc_D25")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9D0")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, 49050, 30, -54780, 0)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_99F")
    SetChrFlags(0x8, 0x10)

    label("loc_99F")

    SetChrPos(0x10, 49280, 30, -52920, 180)
    SetChrPos(0x11, 47330, 30, -54190, 135)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x10, 0x10)
    Jump("loc_D25")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A48")
    SetChrPos(0xC, 52120, 20, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 52980, 30, 55720, 45)
    SetChrPos(0xF, 45490, 650, 55410, 180)
    SetChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 4)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xE, 46740, 30, 53780, 300)
    SetChrFlags(0xE, 0x10)
    Jump("loc_D25")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B5E")
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACA")
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x40)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 53730, 0, 52730, 180)
    ClearChrFlags(0xD, 0x40)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, 53730, 0, 50730, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrPos(0xE, 53730, 0, 51730, 90)
    Jump("loc_B59")

    label("loc_ACA")

    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xF, 48700, 30, 54850, 0)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, 46190, 350, 52460, 0)
    ClearChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 45240, 400, 52480, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xE, 48700, 0, 55600, 180)

    label("loc_B59")

    Jump("loc_D25")

    label("loc_B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BDB")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xC, 52120, 20, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 52980, 30, 55720, 45)
    SetChrPos(0xF, 45430, 0, 53990, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 46740, 30, 53780, 270)
    SetChrFlags(0xE, 0x10)
    Jump("loc_D25")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D08")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_END)), "loc_C7B")
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, 49200, 150, 53560, 90)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 52040, 150, 53650, 270)
    SetChrPos(0xE, 48350, 0, 2900, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xF, 48350, 0, 3900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_END)), "loc_C76")
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_C76")

    Jump("loc_D03")

    label("loc_C7B")

    SetChrPos(0x8, 48470, 30, -54870, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xC, 49040, 20, -52990, 180)
    SetChrPos(0xD, 47900, 20, -52950, 180)
    SetChrPos(0xE, 49070, 20, -51720, 180)
    SetChrPos(0xF, 48050, 20, -51680, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_CFD")
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0xD, 0x10)

    label("loc_CFD")

    BeginChrThread(0xF, 0, 0, 0)

    label("loc_D03")

    Jump("loc_D25")

    label("loc_D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D25")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D34")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_D34")

    Return()

    # Function_6_493 end

    def Function_7_D35(): pass

    label("Function_7_D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7E")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DBD")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_DBD")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DD0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DD0")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x0, 0x1)

    label("loc_DE8")

    Return()

    # Function_7_D35 end

    def Function_8_DE9(): pass

    label("Function_8_DE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10D8")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E17")
    Call(0, 9)
    Jump("loc_F80")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F16")

    #C0001
    ChrTalk(
        0xFE,
        "如果你爸爸还活着……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "肯定还会选择警备队这条路，\x01",
            "并且永不放弃，\x01",
            "坚持战斗到最后一刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……特别任务支援科的各位，\x01",
            "诺艾尔和芙兰就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "为了解决这次的事件，\x01",
            "你们可以随意使唤她们哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x109,
        "#10109F妈妈……你可真是的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_F80")

    label("loc_F16")


    #C0006
    ChrTalk(
        0xFE,
        (
            "特别任务支援科的各位，\x01",
            "诺艾尔和芙兰就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "为了解决这次的事件，\x01",
            "你们可以随意使唤她们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F80")

    Jump("loc_10D3")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1069")

    #C0008
    ChrTalk(
        0xFE,
        "如果诺艾尔的爸爸还活着……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "肯定还会选择警备队这条路，\x01",
            "并且永不放弃，\x01",
            "坚持战斗到最后一刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……特别任务支援科的各位，\x01",
            "诺艾尔和芙兰就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "为了解决这次的事件，\x01",
            "你们可以随意使唤她们哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_10D3")

    label("loc_1069")


    #C0012
    ChrTalk(
        0xFE,
        (
            "特别任务支援科的各位，\x01",
            "诺艾尔和芙兰就交给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "为了解决这次的事件，\x01",
            "你们可以随意使唤她们哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D3")

    Jump("loc_238A")

    label("loc_10D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1248")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1103")
    Call(0, 9)
    Jump("loc_11CB")

    label("loc_1103")


    #C0014
    ChrTalk(
        0xFE,
        (
            "亚泽尔也来帮忙了，\x01",
            "这里不会有问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "就算那种怪物真的闯进来，\x01",
            "我也不会让它碰到\x01",
            "尤格特和萨妮塔一根汗毛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CB")

    #C0016
    ChrTalk(
        0x109,
        "#10101F妈妈，你要多加小心哦。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "呵呵，你们也是，\x01",
            "一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_11CB")

    Jump("loc_1243")

    label("loc_11D0")


    #C0018
    ChrTalk(
        0xFE,
        (
            "亚泽尔也来帮忙了，\x01",
            "这里不会有问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "就算那种怪物真的闯进来，\x01",
            "我也不会让它碰到\x01",
            "尤格特和萨妮塔一根汗毛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1243")

    Jump("loc_238A")

    label("loc_1248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_142F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1372")

    #C0020
    ChrTalk(
        0xFE,
        (
            "迪塔先生他……\x01",
            "恐怕一直都无法接受\x01",
            "至今为止发生过的那些事情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔发生过无数\x01",
            "充满不公，但却又只能\x01",
            "强迫自己去接受的荒唐事……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "…………………………………\x01",
            "……我们一家也………………\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00005F咦…………？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……呵呵，抱歉。\x01",
            "我只是在自言自语而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_142A")

    label("loc_1372")


    #C0025
    ChrTalk(
        0xFE,
        (
            "话说回来，那个所谓的国防军……\x01",
            "与它的前身警备队相比，\x01",
            "给人一种难以接近的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "那套雪白的制服也是一样，\x01",
            "总觉得过于严肃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "我还是更喜欢丈夫在世时穿的\x01",
            "那种警备队制服。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142A")

    Jump("loc_238A")

    label("loc_142F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1602")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AD")

    #C0028
    ChrTalk(
        0xFE,
        (
            "我看看……\x01",
            "芙兰的换洗衣服，\x01",
            "有这些应该就够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "啊，对了，\x01",
            "再带些水果吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10100F妈妈……\x01",
            "你回来啦。\x02\x03",

            "你上午去乌尔斯拉医院\x01",
            "探望了芙兰吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "是啊，已经回来了，\x01",
            "刚到家没多久。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……呼……\x01",
            "芙兰能醒过来，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "真该好好感谢\x01",
            "那位舍身保护她的\x01",
            "二科警督啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10103F嗯……\x01",
            "我们会专程\x01",
            "去探望他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "嗯，那就拜托大家了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_15FD")

    label("loc_15AD")


    #C0036
    ChrTalk(
        0xFE,
        (
            "你们准备去医院吗？\x01",
            "我稍后也要再去一趟。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "得给芙兰送些\x01",
            "换洗衣服之类的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FD")

    Jump("loc_238A")

    label("loc_1602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D2")

    #C0038
    ChrTalk(
        0xFE,
        (
            "玛因兹居然被占领了……\x01",
            "通商会议时也曾出现过恐怖分子，\x01",
            "重大事件真是连续不断啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "听说警备队已经\x01",
            "出动了，\x01",
            "但我还是十分不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "你们几个如果打算过去，\x01",
            "一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1724")

    label("loc_16D2")


    #C0041
    ChrTalk(
        0xFE,
        (
            "占领事件\x01",
            "让我感到十分不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "你们几个如果打算过去，\x01",
            "一定要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1724")

    Jump("loc_238A")

    label("loc_1729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1821")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CC")

    #C0043
    ChrTalk(
        0xFE,
        "今天又下雨啊……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "实在是懒得出去买东西了，\x01",
            "晚饭干脆就热些剩菜，\x01",
            "随便凑和过去算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        (
            "#10106F（妈妈也有懒散的\x01",
            "  一面呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_181C")

    label("loc_17CC")


    #C0046
    ChrTalk(
        0xFE,
        (
            "今天的晚饭就热些剩菜，\x01",
            "随便凑和过去算了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "下雨天出门\x01",
            "实在是太麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181C")

    Jump("loc_238A")

    label("loc_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18A0")

    #C0048
    ChrTalk(
        0xFE,
        (
            "我正在指导尤格特\x01",
            "做主日学校布置的作业呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "唔……看着这些题目，\x01",
            "就会想起过去指导\x01",
            "诺艾尔和芙兰的时候……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238A")

    label("loc_18A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1909")

    #C0050
    ChrTalk(
        0xFE,
        (
            "听说对面的尤格特\x01",
            "最近已经可以\x01",
            "一个人看家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "呵呵，总觉得很欣慰呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_194E")

    label("loc_1909")


    #C0052
    ChrTalk(
        0xFE,
        (
            "莎丽娜拜托我\x01",
            "定时去看看他的\x01",
            "情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "待会给他送些\x01",
            "零食好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194E")

    Jump("loc_238A")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FA")

    #C0054
    ChrTalk(
        0xFE,
        (
            "对面的莎丽娜今天要\x01",
            "工作到很晚才能回家，\x01",
            "所以请我替她照看尤格特。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "莎丽娜到家以后，\x01",
            "肚子肯定也该饿了……\x01",
            "给她准备一顿丰盛的晚餐吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A52")

    label("loc_19FA")


    #C0056
    ChrTalk(
        0xFE,
        "我很喜欢照顾小孩子。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "呵呵，机会难得，\x01",
            "就让我大展身手，\x01",
            "给他们做一顿好吃的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A52")

    Jump("loc_238A")

    label("loc_1A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE6")

    #C0058
    ChrTalk(
        0xFE,
        (
            "芙兰今天说，\x01",
            "她的联络工作\x01",
            "也繁忙了起来。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "毕竟通商会议的正式会议\x01",
            "就要开始了。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "希望会议能\x01",
            "平安闭幕……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B35")

    label("loc_1AE6")


    #C0061
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "芙兰那孩子，\x01",
            "又忘记带午饭了……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "真没办法，\x01",
            "待会给她送过去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B35")

    Jump("loc_238A")

    label("loc_1B3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B48")
    Jump("loc_238A")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D2B")

    #C0063
    ChrTalk(
        0xFE,
        (
            "奇怪，我在百货店\x01",
            "买的高级曲奇饼\x01",
            "放到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#10105F妈、妈妈……\x01",
            "莫非你……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 0)

    #C0065
    ChrTalk(
        0xFE,
        (
            "嗯，我打算给芙兰送去，\x01",
            "慰劳她一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "通商会议临近，\x01",
            "警察肯定也相当忙碌吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x109,
        (
            "#10106F我、我说啊，妈妈……\x01",
            "上班时间吃零食\x01",
            "可不太好……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "哎呀，这有什么的，\x01",
            "只要芙兰高兴不就好了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "啊，对了，不然也给\x01",
            "特别任务支援科送去一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#10106F不用不用！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00009F（芙兰那种我行我素的作风……\x01",
            "  看来是遗传自\x01",
            "  克拉莉丝女士的啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_1D94")

    label("loc_1D2B")


    #C0072
    ChrTalk(
        0xFE,
        (
            "通商会议临近，\x01",
            "警察肯定也相当忙碌吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "我得给芙兰\x01",
            "送点慰劳品。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        "#10106F（这样真的好吗……）\x02",
    )

    CloseMessageWindow()

    label("loc_1D94")

    Jump("loc_238A")

    label("loc_1D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F18")

    #C0075
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "听说你们几个\x01",
            "得到导力车了？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "诺艾尔有没有大呼小叫的？\x01",
            "这孩子啊，只要一见到车……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        (
            "#10112F完、完全没有的事。\x01",
            "……对吧，各位？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00012F这个嘛，也不能说\x01",
            "完全没有……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00104F诺艾尔小姐很激动地给我们\x01",
            "讲了不少性能方面的知识呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x109,
        "#10106F咦咦！有、有这种事吗！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，你自己竟然\x01",
            "完全没有意识到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "真是的……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FD4")

    label("loc_1F18")


    #C0083
    ChrTalk(
        0xFE,
        (
            "只要遇到有关导力车的事情，\x01",
            "这孩子就会兴奋得喋喋不休。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "第一次在警备队坐上装甲车的时候也是，\x01",
            "一个劲地说速度如何，耐久性如何……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x109,
        (
            "#10106F我、我知道啦，\x01",
            "妈妈你就别再说下去了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD4")

    Jump("loc_238A")

    label("loc_1FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_238A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2284")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x109, 0)

    #C0086
    ChrTalk(
        0xFE,
        (
            "诺艾尔，\x01",
            "听说你加入了传说中的\x01",
            "特别任务支援科啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x109,
        (
            "#10100F这个嘛，严格来说，\x01",
            "只是一次『外派』，\x01",
            "所以并不算加入……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "真是的，你这孩子\x01",
            "总是这么爱较真。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "芙兰高兴得手舞足蹈，\x01",
            "说总算可以和你一起工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#00102F呵呵，我能想象到那副画面。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x109,
        (
            "#10106F唉，芙兰真是的……\x01",
            "总像个长不大的\x01",
            "小孩子一样。\x02\x03",

            "#10109F但、但话说回来，\x01",
            "我其实也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，你们姐妹之间的\x01",
            "感情可真好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "但我这个当妈妈的\x01",
            "却有点担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "她们两个的条件都不错，\x01",
            "可姐妹俩的感情太好了，\x01",
            "再这么下去，就越来越难嫁出去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        "#10106F妈、妈妈你可真是的……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00000F（哈哈……\x01",
            "  不光是姐妹间，\x01",
            "  母女间的感情也很好呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 3)
    Jump("loc_238A")

    label("loc_2284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234A")

    #C0097
    ChrTalk(
        0xFE,
        (
            "诺艾尔，记得要偶尔回家\x01",
            "看看哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x109,
        (
            "#10105F咦，可我最近不是\x01",
            "经常回来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "难得调到了离家这么近的工作岗位，\x01",
            "尽量再多回来看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x109,
        (
            "#10106F真是的，\x01",
            "不要这么粘着我啦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_238A")

    label("loc_234A")


    #C0101
    ChrTalk(
        0xFE,
        (
            "诺艾尔，记得偶尔\x01",
            "回家看看哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "妈妈会一直\x01",
            "在家等你的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238A")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE9 end

    def Function_9_238E(): pass

    label("Function_9_238E")

    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    #C0103
    ChrTalk(
        0xB,
        "哎呀……这不是诺艾尔吗！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#10102F妈妈……太好了。\x01",
            "你好像很有精神呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "你也是啊。这段时间一直\x01",
            "没回来看我，我还挺担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        (
            "你不是说国防军的工作繁忙，\x01",
            "暂时回不了家吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x109,
        "#10108F这、这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xB,
        (
            "……哈哈，我就不问了。\x01",
            "你肯定有自己的原因吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "听说芙兰已经出院了，\x01",
            "她正在和你们一起行动吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#00000F是的，她在非常\x01",
            "努力地协助我们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "呵呵，既然如此，\x01",
            "我也就不再多说什么了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        (
            "今后就继续在你们\x01",
            "选择的道路上前进吧，\x01",
            "直到达成想要的结果为止。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "一定要选择一条不会令自己后悔的道路，\x01",
            "别让你们身在天国的\x01",
            "爸爸感到丢脸哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        "#10101F……嗯，我知道了！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_260A")
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_2611")

    label("loc_260A")

    OP_93(0xB, 0x10E, 0x0)

    label("loc_2611")

    SetScenarioFlags(0x1BA, 3)
    Return()

    # Function_9_238E end

    def Function_10_2615(): pass

    label("Function_10_2615")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D3")

    #C0115
    ChrTalk(
        0xFE,
        (
            "亚泽尔今天\x01",
            "到旧城区去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "如果是过去的我，\x01",
            "一定会对他发怒，抱怨他怎么\x01",
            "可以在这种时候丢下家人……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "但现在，我却希望他为了\x01",
            "自己的朋友和大家而努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2736")

    label("loc_26D3")


    #C0118
    ChrTalk(
        0xFE,
        (
            "亚泽尔已经长大了，\x01",
            "我不会再对他\x01",
            "过多干涉。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "我现在希望亚泽尔为了\x01",
            "自己的朋友和大家而努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_347A")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2846")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2812")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0120
    ChrTalk(
        0xFE,
        (
            "亚泽尔急匆匆地\x01",
            "从旧城区回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "多亏如此，因为害怕而不停哭泣的\x01",
            "尤格特总算平静下来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        "我、我才没哭呢！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #C0123
    ChrTalk(
        0xFE,
        (
            "呵呵，没哭没哭。\x01",
            "尤格特是个坚强的孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2841")

    label("loc_2812")


    #C0124
    ChrTalk(
        0xFE,
        (
            "……总之，亚泽尔回来了，\x01",
            "我也就安下心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2841")

    Jump("loc_347A")

    label("loc_2846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_296E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2906")

    #C0125
    ChrTalk(
        0xFE,
        (
            "迪塔总统所说的\x01",
            "『原因不明的事故』……\x01",
            "我也曾听说过。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "但真没想到，那居然是由于\x01",
            "两大国的暗斗而引起的……\x01",
            "老实说，真是太可怕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "独立果然还是\x01",
            "有必要的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2969")

    label("loc_2906")


    #C0128
    ChrTalk(
        0xFE,
        (
            "一想到尤格特和亚泽尔\x01",
            "也有可能被卷入到那些\x01",
            "『原因不明的事故』……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "独立果然还是\x01",
            "有必要的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2969")

    Jump("loc_347A")

    label("loc_296E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2AA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A3E")

    #C0130
    ChrTalk(
        0xFE,
        (
            "亚泽尔和圣书会的\x01",
            "同伴们正在一起参与旧城区的\x01",
            "重建工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "居然能为了他人而行动……\x01",
            "如果是过去的他，\x01",
            "根本不可能做出这样的举动。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "呵呵，身为他的姐姐，\x01",
            "也不禁为他感到骄傲。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A9E")

    label("loc_2A3E")


    #C0133
    ChrTalk(
        0xFE,
        (
            "弟弟以前很叛逆，\x01",
            "一向不听人劝……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "但他现在真的改变了。\x01",
            "身为他的姐姐，也替他感到骄傲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9E")

    Jump("loc_347A")

    label("loc_2AA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B0C")

    #C0135
    ChrTalk(
        0xFE,
        "竟然发生了占领事件，真可怕啊……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "虽说今天应该去上班，\x01",
            "但安全起见，还是请个假吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_347A")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2B6B")

    #C0137
    ChrTalk(
        0xFE,
        (
            "听说昨天有人在脱轨事故现场的附近\x01",
            "目击到了一只巨大的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "太可怕了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_347A")

    label("loc_2B6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B79")
    Jump("loc_347A")

    label("loc_2B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B8A")
    Call(0, 11)
    Jump("loc_347A")

    label("loc_2B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C10")

    #C0139
    ChrTalk(
        0xFE,
        (
            "尤格特今天去\x01",
            "主日学校上课了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "亚泽尔以前总是\x01",
            "逃课……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "希望尤格特好好学习，\x01",
            "别像他哥哥一样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C36")

    label("loc_2C10")


    #C0142
    ChrTalk(
        0xFE,
        (
            "啊，糟了……\x01",
            "得赶快去上班\x01",
            "才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C36")

    Jump("loc_347A")

    label("loc_2C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E35")

    #C0143
    ChrTalk(
        0xFE,
        (
            "听说昨天有一位奇怪的客人\x01",
            "出现在了亚泽尔工作的酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "那个人一头金发，\x01",
            "穿着白色大衣，\x01",
            "带着一把鲁特琴……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "自作主张就开始演奏，\x01",
            "和来店的女客人调笑，\x01",
            "总之就是为所欲为。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_2DC8")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0x101,
        "#00006F（这……大概就是皇子殿下吧。）\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        "#00306F（不用加上大概，肯定是他啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E2D")

    label("loc_2DC8")


    #C0148
    ChrTalk(
        0x101,
        (
            "#00005F（金发、鲁特琴……\x01",
            "  最近好像在哪里见过这样的人……？）\x02\x03",

            "#00004F（不、不可能是他吧……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2D")

    SetScenarioFlags(0x0, 1)
    Jump("loc_2EAD")

    label("loc_2E35")


    #C0149
    ChrTalk(
        0xFE,
        (
            "亚泽尔回家以后，一向都很少\x01",
            "和我说店里的事，但这次却\x01",
            "忍不住和我说个不停……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "那位客人\x01",
            "肯定是个\x01",
            "相当奇怪的人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAD")

    Jump("loc_347A")

    label("loc_2EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F5A")

    #C0151
    ChrTalk(
        0xFE,
        (
            "住在对面的克拉莉丝女士\x01",
            "今天出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "克拉莉丝女士总是替我\x01",
            "照看尤格特，真是受到她\x01",
            "不少照顾……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "我得找个机会，好好向她道谢才行。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FBE")

    label("loc_2F5A")


    #C0154
    ChrTalk(
        0xFE,
        (
            "克拉莉丝女士总是替我\x01",
            "照看尤格特，真是受到她\x01",
            "不少照顾……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "我得找个机会，好好向她道谢才行。\x02",
    )

    CloseMessageWindow()

    label("loc_2FBE")

    Jump("loc_347A")

    label("loc_2FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_30BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3071")

    #C0156
    ChrTalk(
        0xFE,
        (
            "我事先没有告知弟弟，\x01",
            "直接去他打工的那家酒吧看了看。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "他一开始很不好意思，\x01",
            "但还是认真接待我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "能怀有职业操守而工作，\x01",
            "真是值得表扬。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30B9")

    label("loc_3071")


    #C0159
    ChrTalk(
        0xFE,
        "（咕嘟咕嘟）……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "亚泽尔调制的\x01",
            "无酒精鸡尾酒……\x01",
            "味道相当不错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    Jump("loc_347A")

    label("loc_30BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_317D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3130")

    #C0161
    ChrTalk(
        0xFE,
        (
            "今天我休假，\x01",
            "所以就在家陪弟弟。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "不过，唔……\x01",
            "再怎么说，游击士游戏\x01",
            "也有些……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3178")

    label("loc_3130")


    #C0163
    ChrTalk(
        0xFE,
        (
            "游击士游戏\x01",
            "应该怎么玩呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "在这种时候，\x01",
            "亚泽尔却偏偏不在家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3178")

    Jump("loc_347A")

    label("loc_317D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_347A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337C")
    TurnDirection(0xFE, 0x105, 0)

    #C0165
    ChrTalk(
        0xFE,
        "哎呀，你是……？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x105,
        (
            "#10300F哦，你是……\x01",
            "亚泽尔的姐姐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00005F咦……\x01",
            "你们认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，她弟弟亚泽尔是\x01",
            "圣书会的成员。\x02\x03",

            "#10300F我记得在很久之前，\x01",
            "她为了让弟弟离开圣书会，\x01",
            "还曾闯进『崔尼蒂』呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        "#00105F闯、闯进……？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "那、那次真是\x01",
            "给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "当时我实在很想\x01",
            "让亚泽尔脱离你们，\x01",
            "所以才……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        (
            "#10304F那气势汹汹的样子，\x01",
            "让圣书会的各位都\x01",
            "大吃一惊呢。\x02\x03",

            "#10309F呵呵，那也正是\x01",
            "姐弟情的体现吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        "#00006F（说、说得好像事不关己一样……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 4)
    Jump("loc_347A")

    label("loc_337C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341B")

    #C0174
    ChrTalk(
        0xFE,
        (
            "我弟弟亚泽尔在\x01",
            "『崔尼蒂』打工。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "那里的治安状况比较差，\x01",
            "所以我一开始很担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "不过看他一直好好做到现在，\x01",
            "我也总算安心了一些。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_347A")

    label("loc_341B")


    #C0177
    ChrTalk(
        0xFE,
        (
            "唉，亚泽尔真是的，\x01",
            "几乎从不跟我说\x01",
            "组织里发生的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "真希望他不要老是\x01",
            "让我这么担心……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_347A")

    TalkEnd(0xFE)
    Return()

    # Function_10_2615 end

    def Function_11_347E(): pass

    label("Function_11_347E")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E4")

    #C0179
    ChrTalk(
        0x9,
        (
            "姐姐这就去\x01",
            "上班了。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "尤格特，\x01",
            "你可要锁好门哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        "嗯，交给我吧～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3534")

    label("loc_34E4")


    #C0182
    ChrTalk(
        0x9,
        (
            "对了，\x01",
            "就算姐姐不在身边，\x01",
            "你也要乖乖把作业做完哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        "真是的～我知道啦～\x02",
    )

    CloseMessageWindow()

    label("loc_3534")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_347E end

    def Function_12_353D(): pass

    label("Function_12_353D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_36A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3626")

    #C0184
    ChrTalk(
        0xFE,
        (
            "看着外面那棵蓝白色的大树，\x01",
            "我真的很害怕……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "但哥哥安慰了我，\x01",
            "说不要紧，\x01",
            "他一定会想办法的。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "其实我知道，发生了这种事情，\x01",
            "就算是哥哥也无能为力……\x01",
            "嘿嘿，但听了哥哥的安慰，我还是打起精神了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36A1")

    label("loc_3626")


    #C0187
    ChrTalk(
        0xFE,
        (
            "哥哥看到我害怕那棵蓝白色的大树，\x01",
            "耐心地安慰了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "哥哥果然是最帅的。\x01",
            "听了哥哥的安慰后，我已经打起精神了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A1")

    Jump("loc_3AFA")

    label("loc_36A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_36E3")

    #C0189
    ChrTalk(
        0xFE,
        (
            "只要有哥哥在身边，\x01",
            "我们就一定不会有事的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_36E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3751")

    #C0190
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔独立……？\x01",
            "那到底是怎么一回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "我不大理解呢。\x01",
            "玛布尔老师会不会明白呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_3751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_37A9")

    #C0192
    ChrTalk(
        0xFE,
        (
            "有没有什么\x01",
            "我也能帮上忙的事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "干脆到哥哥所在的\x01",
            "旧城区看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_37A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_37F5")

    #C0194
    ChrTalk(
        0xFE,
        (
            "好像发生了\x01",
            "很严重的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "亚泽尔哥哥\x01",
            "还不回来吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_37F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3854")

    #C0196
    ChrTalk(
        0xFE,
        (
            "听说昨天有一辆列车\x01",
            "翻倒在地上了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "真可怕……\x01",
            "为什么会发生\x01",
            "那种事呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_393B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F3")
    OP_4B(0xB, 0xFF)

    #C0198
    ChrTalk(
        0xFE,
        "唉……作业真讨厌啊。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        "再加把劲吧，尤格特。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "阿姨还准备了零食\x01",
            "来奖励你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "真的吗～！？\x01",
            "那我就再加把劲吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3936")

    label("loc_38F3")


    #C0202
    ChrTalk(
        0xFE,
        "我想想……１４×２３等于……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "唔……两位数的乘法\x01",
            "好难啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3936")

    Jump("loc_3AFA")

    label("loc_393B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_394C")
    Call(0, 11)
    Jump("loc_3AFA")

    label("loc_394C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_395A")
    Jump("loc_3AFA")

    label("loc_395A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_39B8")

    #C0204
    ChrTalk(
        0xFE,
        (
            "哥哥最近大概每过三天\x01",
            "就会回来一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "他还会把店里没卖完的\x01",
            "小菜带回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_39B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A26")

    #C0206
    ChrTalk(
        0xFE,
        (
            "克拉莉丝阿姨告诉我，\x01",
            "她今天要去大圣堂。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "说起来，她上个月好像也是\x01",
            "在同一天去大圣堂的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_3A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A34")
    Jump("loc_3AFA")

    label("loc_3A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A90")

    #C0208
    ChrTalk(
        0xFE,
        (
            "姐姐说她不知道\x01",
            "游击士游戏的玩法。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "唉～真没办法，\x01",
            "那就玩过家家算了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AFA")

    label("loc_3A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3AFA")

    #C0210
    ChrTalk(
        0xFE,
        (
            "亚泽尔哥哥\x01",
            "在旧城区的店里\x01",
            "做调酒师哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "嘿嘿，是不是很帅气？\x01",
            "那可是我引以为傲的哥哥呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AFA")

    TalkEnd(0xFE)
    Return()

    # Function_12_353D end

    def Function_13_3AFE(): pass

    label("Function_13_3AFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D01")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 500)

    #C0212
    ChrTalk(
        0xFE,
        (
            "咦……瓦、瓦吉！？\x01",
            "你回到克洛斯贝尔了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x105,
        "#10400F呵呵，好久不见了，亚泽尔。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "你那身打扮是怎么回事……\x01",
            "还有，阿巴斯在哪里！？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x105,
        (
            "#10404F看来你有不少问题\x01",
            "想问我啊，可惜的是，\x01",
            "现在实在是没时间慢慢说。\x02\x03",

            "#10400F等事情过去之后，我会慢慢向你解释的，\x01",
            "你现在就在这里保护好\x01",
            "自己的姐姐和弟弟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "我、我知道了……\x01",
            "说的也是，现在可不是\x01",
            "闲聊天的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "不过，瓦吉你没事，真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x105,
        (
            "#10402F呵呵，彼此彼此。\x01",
            "……那就这样了，下次再见吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 4)
    Jump("loc_3E1B")

    label("loc_3D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA6")

    #C0219
    ChrTalk(
        0xFE,
        (
            "那些在外面四处徘徊的怪物\x01",
            "好像并不会进入建筑物内。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "……但仍然不能放松警惕，\x01",
            "必须得全力戒备它们……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "我一定要保护好\x01",
            "姐姐和尤格特……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E1B")

    label("loc_3DA6")


    #C0222
    ChrTalk(
        0xFE,
        (
            "那些在外面四处徘徊的怪物\x01",
            "好像并不会进入建筑物内……\x01",
            "但仍然不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "我一定要保护好\x01",
            "姐姐和尤格特……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E1B")

    TalkEnd(0xFE)
    Return()

    # Function_13_3AFE end

    def Function_14_3E1F(): pass

    label("Function_14_3E1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E30")
    Jump("loc_49E0")

    label("loc_3E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3E3E")
    Jump("loc_49E0")

    label("loc_3E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_402B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F0E")

    #C0224
    ChrTalk(
        0xFE,
        (
            "我今天就要\x01",
            "离开克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "已经火速打包好了行李……\x01",
            "但这本书不方便携带。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "干脆送给你们好了。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0227
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝11卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝11卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 2)
    Jump("loc_4026")

    label("loc_3F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9F")

    #C0228
    ChrTalk(
        0xFE,
        (
            "帝国政府向我们\x01",
            "下达了撤离命令。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "我打算乘坐今天的列车\x01",
            "离开克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "车站那边似乎相当混乱，\x01",
            "我也得赶快过去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4026")

    label("loc_3F9F")


    #C0231
    ChrTalk(
        0xFE,
        (
            "真没想到我居然会以\x01",
            "这种形式离开克洛斯贝尔……\x01",
            "但对我来说，家人始终是最重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "车站那边似乎相当混乱，\x01",
            "我得尽早乘上列车才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4026")

    Jump("loc_49E0")

    label("loc_402B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CE")

    #C0233
    ChrTalk(
        0xFE,
        (
            "身在帝国的家人很担心我，\x01",
            "还给我寄了信。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "毕竟发生了那种事件，\x01",
            "我也想早日\x01",
            "回到故乡。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "看来有必要和总公司\x01",
            "好好谈谈这个问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4112")

    label("loc_40CE")


    #C0236
    ChrTalk(
        0xFE,
        (
            "虽然我的家人\x01",
            "都很担心……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "但还是要逐步办好\x01",
            "回帝国的手续。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4112")

    Jump("loc_49E0")

    label("loc_4117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_419E")

    #C0238
    ChrTalk(
        0xFE,
        (
            "武装集团竟然\x01",
            "占领了玛因兹……\x01",
            "这种事情真是闻所未闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "总之，现在也只能向女神祈祷，\x01",
            "希望这起事件能尽早解决了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E0")

    label("loc_419E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_42A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4234")

    #C0240
    ChrTalk(
        0xFE,
        (
            "来这里游玩的妻子和女儿\x01",
            "今天已经回帝国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "昨天的脱轨事故\x01",
            "真是让我胆战心惊……\x01",
            "不过，铁路能马上修复，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_429F")

    label("loc_4234")


    #C0242
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "我已经好久没有与\x01",
            "妻子和女儿团聚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "哈哈，久别重逢一次，\x01",
            "反而让我的思乡病发作了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_429F")

    Jump("loc_49E0")

    label("loc_42A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_42B2")
    Jump("loc_49E0")

    label("loc_42B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4323")

    #C0244
    ChrTalk(
        0xFE,
        (
            "是吗……\x01",
            "你们要回去了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "短时间之内，我还无法回到\x01",
            "你们母女的身边……\x01",
            "孩子就靠你照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E0")

    label("loc_4323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B9")

    #C0246
    ChrTalk(
        0xFE,
        (
            "身在帝国的妻子和女儿\x01",
            "来这里玩了……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "她们来之前都没有联系我，\x01",
            "让我大吃了一惊……\x01",
            "但、但我还是很高兴。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x10)
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_442D")

    label("loc_43B9")


    #C0248
    ChrTalk(
        0xFE,
        (
            "原来如此，坐的是昨天的列车……\x01",
            "你们应该提前联络我一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "没能提前做好迎接你们的准备，\x01",
            "真是太不好意思了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_442D")

    Jump("loc_49E0")

    label("loc_4432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44A4")

    #C0250
    ChrTalk(
        0xFE,
        (
            "通商会议的商谈情况，\x01",
            "应该也会影响到股价。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "作为一名证券经理，\x01",
            "我必须要密切关注会议的动向。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E0")

    label("loc_44A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_46A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4536")

    #C0252
    ChrTalk(
        0xFE,
        (
            "住在对面的本德先生\x01",
            "一家养的小猫\x01",
            "在昨天走失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "我也帮他们找了一阵子，\x01",
            "但最后还是没能找到……\x01",
            "到底跑到哪里了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_469D")

    label("loc_4536")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D6")

    #C0254
    ChrTalk(
        0xFE,
        (
            "哎呀，你们要去寻找\x01",
            "本德先生家的猫吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "那个女孩从昨天一直哭到现在，\x01",
            "实在是太可怜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "请你们一定要把\x01",
            "那只猫找回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_463D")

    label("loc_45D6")


    #C0257
    ChrTalk(
        0xFE,
        (
            "因为小猫走失了，\x01",
            "那个女孩从昨天一直哭到现在，\x01",
            "实在是太可怜了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "请你们一定要把\x01",
            "那只猫找回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463D")

    Jump("loc_469D")

    label("loc_4642")


    #C0259
    ChrTalk(
        0xFE,
        (
            "我听到对面那个女孩\x01",
            "欢快的声音了。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "看来总算把猫\x01",
            "找回来了啊。\x01",
            "可喜可贺，可喜可贺。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_469D")

    Jump("loc_49E0")

    label("loc_46A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_47E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4760")

    #C0261
    ChrTalk(
        0xFE,
        (
            "听说对面的本德先生\x01",
            "一家原本住在\x01",
            "住宅街。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "似乎经历了很多事情，\x01",
            "最后搬到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "话虽如此，\x01",
            "但他们一家人的气氛却温暖乐观，\x01",
            "我真该好好向他们学学啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_47DB")

    label("loc_4760")


    #C0264
    ChrTalk(
        0xFE,
        (
            "对面那家人是从\x01",
            "住宅街的黄金地段\x01",
            "搬到这里来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "他们似乎经历了很多事情，却能那么乐观开朗……\x01",
            "我真应该好好学学啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47DB")

    Jump("loc_49E0")

    label("loc_47E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_48F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4805")
    Call(0, 15)
    Jump("loc_489B")

    label("loc_4805")

    OP_4B(0xC, 0xFF)

    #C0266
    ChrTalk(
        0xC,
        (
            "非常感谢\x01",
            "您的关心。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "今后也许会给您添不少麻烦，\x01",
            "还请您多加关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "不不不，哪里的话。\x01",
            "以后要是有什么困难，\x01",
            "请不要客气，尽管说哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_489B")

    Jump("loc_48F2")

    label("loc_48A0")


    #C0269
    ChrTalk(
        0xFE,
        (
            "听说本德先生和我一样，\x01",
            "是个证券经理。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "呵呵，大概会是个不错的\x01",
            "交流对象。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48F2")

    Jump("loc_49E0")

    label("loc_48F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_49E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4996")

    #C0271
    ChrTalk(
        0xFE,
        (
            "对面原本住着\x01",
            "两名年轻游击士……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "但他们在几个月前回故乡了，\x01",
            "这层楼一下子就变得冷冷清清的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "真希望\x01",
            "早日搬进\x01",
            "新住户……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_49E0")

    label("loc_4996")


    #C0274
    ChrTalk(
        0xFE,
        (
            "单身赴任真是\x01",
            "让我感到十分寂寞。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "对面能不能快点\x01",
            "搬进新住户呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E0")

    TalkEnd(0xFE)
    Return()

    # Function_14_3E1F end

    def Function_15_49E4(): pass

    label("Function_15_49E4")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0276
    ChrTalk(
        0xC,
        "就是这样……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "今后说不定会给您\x01",
            "添不少麻烦，\x01",
            "但还是请您多加关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xD,
        "请多关照。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xE,
        "来，玛丽也要打声招呼哦。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xF,
        "喵～\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "呵呵，你们一家人的\x01",
            "感情可真好。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "以后要是有什么困难，\x01",
            "随时都可以过来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        "好的，真是太谢谢您了。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_15_49E4 end

    def Function_16_4B15(): pass

    label("Function_16_4B15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B3E")
    Call(0, 22)
    Return()

    label("loc_4B3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B72")
    Call(0, 23)
    Return()

    label("loc_4B72")

    Call(0, 25)
    Return()

    label("loc_4B76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C54")

    #C0284
    ChrTalk(
        0xFE,
        (
            "我们公司原本在ＩＢＣ内，\x01",
            "现在租了个小房子当事务所，\x01",
            "已经重新开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "这段时间，我一直没有工作，\x01",
            "要好好准备一下才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "为了能支撑起这个由三人一猫\x01",
            "组成的家庭，我可得好好努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CDF")

    label("loc_4C54")


    #C0287
    ChrTalk(
        0xFE,
        (
            "我们公司原本在ＩＢＣ内，\x01",
            "现在租了个小房子当事务所，\x01",
            "已经重新开始营业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "为了能支撑起这个由三人一猫\x01",
            "组成的家庭，我可得好好努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDF")

    Jump("loc_552E")

    label("loc_4CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D5E")

    #C0289
    ChrTalk(
        0xFE,
        (
            "不管怎么说，既然已经颁布了戒严令，\x01",
            "那还是待在家里比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "没关系的，这种状况\x01",
            "不可能持续太久……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_552E")

    label("loc_4D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E06")

    #C0291
    ChrTalk(
        0xFE,
        (
            "那种宣言肯定会对帝国和共和国\x01",
            "造成强烈的刺激。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "说不定会使克洛斯贝尔\x01",
            "陷入危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "但不管发生什么事，\x01",
            "我都一定会保护好我的家人。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E74")

    label("loc_4E06")


    #C0294
    ChrTalk(
        0xFE,
        (
            "总之……\x01",
            "现在重要的就是把握现状，\x01",
            "并做出冷静的判断。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "不管发生什么事，\x01",
            "我都一定会保护好\x01",
            "我的家人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E74")

    Jump("loc_552E")

    label("loc_4E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F59")

    #C0296
    ChrTalk(
        0xFE,
        (
            "我就职的那家公司\x01",
            "原本在ＩＢＣ大楼……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "但如你们所知，\x01",
            "那里现在已经化为一堆瓦砾了，\x01",
            "所以被迫停业。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "虽然无人遇难，\x01",
            "但要想恢复业务，\x01",
            "恐怕得花费不少时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "唉……这可真让人头疼啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FC6")

    label("loc_4F59")


    #C0300
    ChrTalk(
        0xFE,
        (
            "袭击者破坏了ＩＢＣ大楼，\x01",
            "我们公司也被迫停业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "……不幸中的万幸是，\x01",
            "我家周边地区并没有\x01",
            "遭到袭击。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC6")

    Jump("loc_552E")

    label("loc_4FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5025")

    #C0302
    ChrTalk(
        0xFE,
        (
            "说起来，事态好像\x01",
            "变得很严重啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "那个武装集团究竟\x01",
            "有什么目的呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_552E")

    label("loc_5025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5090")

    #C0304
    ChrTalk(
        0xFE,
        (
            "久违地\x01",
            "拿到了一天休假。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "反正外面也正下着雨，\x01",
            "今天就和家人一起\x01",
            "悠闲度过吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_5090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_509E")
    Jump("loc_552E")

    label("loc_509E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_50AC")
    Jump("loc_552E")

    label("loc_50AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50BA")
    Jump("loc_552E")

    label("loc_50BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5166")

    #C0306
    ChrTalk(
        0xFE,
        (
            "我的工作和玛西先生\x01",
            "很相似。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "所以我偶尔会到对面\x01",
            "房间，和他一起推测\x01",
            "股价的走向。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "帝国的证券经理\x01",
            "有着相当独特的眼光，\x01",
            "真是很有意思。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51D3")

    label("loc_5166")


    #C0309
    ChrTalk(
        0xFE,
        (
            "好了……我差不多\x01",
            "也该去公司了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "虽然有点在意通商会议……\x01",
            "但也只能等待\x01",
            "克洛斯贝尔时代周刊的报道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D3")

    Jump("loc_552E")

    label("loc_51D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_52BE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5281")

    #C0311
    ChrTalk(
        0xFE,
        (
            "哎呀，没想到\x01",
            "你们肯来帮忙，\x01",
            "我真是很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "我稍后也会\x01",
            "去中央广场\x01",
            "继续找的。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "如果有什么发现，\x01",
            "请各位随时联系我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52B9")

    label("loc_5281")


    #C0314
    ChrTalk(
        0xFE,
        "今天真的太感谢你们了。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "我绝不会忘记这份恩情。\x02",
    )

    CloseMessageWindow()

    label("loc_52B9")

    Jump("loc_552E")

    label("loc_52BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5397")

    #C0316
    ChrTalk(
        0xFE,
        (
            "我以前拥有可以\x01",
            "在家中工作的设备……\x01",
            "但现在可就今非昔比了。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "只好和其他职员一样，\x01",
            "每天去ＩＢＣ大楼内的\x01",
            "公司上班。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "搬到这里之后，\x01",
            "已经基本安顿了下来，\x01",
            "接下来就要开始努力工作了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5400")

    label("loc_5397")


    #C0319
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "上班其实也不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "筋疲力尽地回到家之后，\x01",
            "能听到一声『你回来啦』，\x01",
            "实在是一种幸福。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5400")

    Jump("loc_552E")

    label("loc_5405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5525")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542A")
    Call(0, 15)
    Jump("loc_54C6")

    label("loc_542A")

    OP_4B(0x8, 0xFF)

    #C0321
    ChrTalk(
        0xC,
        (
            "非常感谢您的\x01",
            "关心。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xC,
        (
            "也许我们会给您添不少麻烦，\x01",
            "但还是请您多加关照了。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "哪里的话，彼此彼此。\x01",
            "以后如果有什么事，\x01",
            "请不要客气，尽管说哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_54C6")

    Jump("loc_5520")

    label("loc_54CB")


    #C0324
    ChrTalk(
        0xFE,
        "我真是个幸福的人。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "这也是多亏了家人的支持……\x01",
            "今后我也得好好珍惜她们才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5520")

    Jump("loc_552E")

    label("loc_5525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_552E")

    label("loc_552E")

    TalkEnd(0xFE)
    Return()

    # Function_16_4B15 end

    def Function_17_5532(): pass

    label("Function_17_5532")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5560")
    Call(0, 22)
    Return()

    label("loc_5560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5598")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5594")
    Call(0, 23)
    Return()

    label("loc_5594")

    Call(0, 25)
    Return()

    label("loc_5598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5620")

    #C0326
    ChrTalk(
        0xFE,
        (
            "听说住宅街的索菲亚夫人\x01",
            "和辛迪小姐她们\x01",
            "全都平安无事，我总算松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "总之，现在就努力恢复\x01",
            "过去的悠闲生活吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1F")

    label("loc_5620")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5682")

    #C0328
    ChrTalk(
        0xFE,
        (
            "我很担心住宅街的\x01",
            "那些老邻居……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "索菲亚小姐和辛迪小姐\x01",
            "是否都平安无事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1F")

    label("loc_5682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_56F7")

    #C0330
    ChrTalk(
        0xFE,
        (
            "我也不奢望什么，\x01",
            "只希望克洛斯贝尔市\x01",
            "能恢复得像过去一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "只要家人能幸福生活，\x01",
            "我就很满足了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1F")

    label("loc_56F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_57E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5796")

    #C0332
    ChrTalk(
        0xFE,
        (
            "我……\x01",
            "我看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "那个在旧城区大肆破坏的\x01",
            "巨大怪物……\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "啊啊，太可怕了……\x01",
            "克洛斯贝尔什么时候\x01",
            "变成这么可怕的地方了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_57E1")

    label("loc_5796")


    #C0335
    ChrTalk(
        0xFE,
        (
            "一想到那个巨大的怪物\x01",
            "说不定还会再次出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "呜呜，我就浑身发抖。\x02",
    )

    CloseMessageWindow()

    label("loc_57E1")

    Jump("loc_5E1F")

    label("loc_57E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5836")

    #C0337
    ChrTalk(
        0xFE,
        (
            "我真的很害怕\x01",
            "血腥和暴力……\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "但愿事件能\x01",
            "平安无事地结束。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1F")

    label("loc_5836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_590E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58BA")

    #C0339
    ChrTalk(
        0xFE,
        (
            "（浇水）……\x01",
            "只要给植物浇水，\x01",
            "我就感到身心舒畅。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "下雨的声音也很美妙……\x01",
            "这个休息日真是宁静啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5909")

    label("loc_58BA")


    #C0341
    ChrTalk(
        0xFE,
        (
            "（浇水）……\x01",
            "再过一会，\x01",
            "就是下午茶时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "啊，还得给玛丽\x01",
            "装些猫粮。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5909")

    Jump("loc_5E1F")

    label("loc_590E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5989")

    #C0343
    ChrTalk(
        0xFE,
        (
            "一会得出门买点东西。\x01",
            "玛尔缇小姐那里的东西\x01",
            "今天会比较便宜吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "呵呵，我已经认得\x01",
            "市场里的所有人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1F")

    label("loc_5989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A3C")

    #C0345
    ChrTalk(
        0xFE,
        (
            "据说今天有个重要的会议，\x01",
            "我老公一大早就出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "自从搬到这里之后，\x01",
            "老公对工作更加\x01",
            "热忱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "而且他非常关心我和女儿……\x01",
            "呵呵，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A83")

    label("loc_5A3C")


    #C0348
    ChrTalk(
        0xFE,
        (
            "自从搬到这里之后，\x01",
            "老公对工作更加热忱了。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        "呵呵，真是太好了。\x02",
    )

    CloseMessageWindow()

    label("loc_5A83")

    Jump("loc_5E1F")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5A96")
    Jump("loc_5E1F")

    label("loc_5A96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B33")

    #C0350
    ChrTalk(
        0xFE,
        (
            "住在对面那个人\x01",
            "经常会送东西给我们，\x01",
            "是个十分和善的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "不过，他似乎\x01",
            "有些寂寞呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "单身赴任，\x01",
            "平时肯定会很寂寞吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B94")

    label("loc_5B33")


    #C0353
    ChrTalk(
        0xFE,
        (
            "单身赴任，\x01",
            "平时肯定会很寂寞吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "如此看来，\x01",
            "我们一家人能团聚在一起，\x01",
            "就已经十分幸福了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B94")

    Jump("loc_5E1F")

    label("loc_5B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5C5E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C01")

    #C0355
    ChrTalk(
        0xFE,
        (
            "那就请各位替我们\x01",
            "寻找玛丽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "那孩子一定\x01",
            "很想回家。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C59")

    label("loc_5C01")


    #C0357
    ChrTalk(
        0xFE,
        (
            "呵呵呵，萨妮塔可真是的，\x01",
            "竟然抱得那么紧。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "不过，玛丽好像\x01",
            "很喜欢被她这样抱呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C59")

    Jump("loc_5E1F")

    label("loc_5C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CE8")

    #C0359
    ChrTalk(
        0xFE,
        (
            "虽然这间房子\x01",
            "做饭时地方有些狭窄。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "但可以在外面的花盆种植花卉，\x01",
            "继续我的园艺爱好，\x01",
            "所以我还挺满意的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5D47")

    label("loc_5CE8")


    #C0361
    ChrTalk(
        0xFE,
        (
            "我本以为\x01",
            "萨妮塔需要一些时间\x01",
            "才能习惯这里的生活……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "呵呵呵，看来已经\x01",
            "不需要担心了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D47")

    Jump("loc_5E1F")

    label("loc_5D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D71")
    Call(0, 15)
    Jump("loc_5DA7")

    label("loc_5D71")


    #C0363
    ChrTalk(
        0xFE,
        (
            "呵呵呵，邻居看起来\x01",
            "是个很和善的人，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA7")

    Jump("loc_5E11")

    label("loc_5DAC")


    #C0364
    ChrTalk(
        0xFE,
        (
            "今后不管发生什么事，\x01",
            "我们一家人\x01",
            "也一定能撑过去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "呵呵呵，这让我想起了\x01",
            "新婚那时的心情呢⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E11")

    Jump("loc_5E1F")

    label("loc_5E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5E1F")

    label("loc_5E1F")

    TalkEnd(0xFE)
    Return()

    # Function_17_5532 end

    def Function_18_5E23(): pass

    label("Function_18_5E23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E57")
    Call(0, 23)
    Return()

    label("loc_5E57")

    Call(0, 25)
    Return()

    label("loc_5E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EEB")

    #C0366
    ChrTalk(
        0xFE,
        (
            "能够重新投入到工作中，\x01",
            "爸爸显得很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "呵呵，萨妮塔也很为他高兴。\x01",
            "玛丽，你也这么觉得吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xF,
        "喵～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5F3B")

    label("loc_5EEB")


    #C0369
    ChrTalk(
        0xFE,
        (
            "能够重新投入到工作中，\x01",
            "爸爸显得很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "呵呵，萨妮塔也\x01",
            "很为他高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F3B")

    Jump("loc_6823")

    label("loc_5F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5F87")

    #C0371
    ChrTalk(
        0xFE,
        "玛丽，你别担心。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "萨妮塔一定会\x01",
            "保护好你的……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6823")

    label("loc_5F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FDF")

    #C0373
    ChrTalk(
        0xFE,
        (
            "听说住在对面的叔叔\x01",
            "今天就要离开\x01",
            "克洛斯贝尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "真有些不舍啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6823")

    label("loc_5FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_603E")

    #C0375
    ChrTalk(
        0xFE,
        (
            "要不要带玛丽\x01",
            "一起去慈善活动\x01",
            "会场看看呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "听说那里聚集了\x01",
            "很多漂亮的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6823")

    label("loc_603E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_60F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60AA")

    #C0377
    ChrTalk(
        0xFE,
        (
            "爸爸妈妈叫我\x01",
            "今天不要到太远的\x01",
            "地方去。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "只好在这里和玛丽玩了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_60EC")

    label("loc_60AA")


    #C0379
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "今天本该全家一起\x01",
            "到百货店去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "真无聊啊……\x02",
    )

    CloseMessageWindow()

    label("loc_60EC")

    Jump("loc_6823")

    label("loc_60F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6154")

    #C0381
    ChrTalk(
        0xFE,
        (
            "玛丽它昨天\x01",
            "洗脸了哟。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "听说猫一洗脸，天就会下雨，\x01",
            "看来是真的呢。\x01",
            "太吃惊了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6823")

    label("loc_6154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E7")

    #C0383
    ChrTalk(
        0xFE,
        (
            "玛丽它在\x01",
            "很认真地给自己\x01",
            "洗脸呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "摆摊的阿姨说过，\x01",
            "猫一洗脸，\x01",
            "天就会下雨……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "……也就是说，明天会下雨吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6220")

    label("loc_61E7")


    #C0386
    ChrTalk(
        0xFE,
        (
            "玛丽在给自己\x01",
            "洗脸呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        "……所以明天会下雨吗？\x02",
    )

    CloseMessageWindow()

    label("loc_6220")

    Jump("loc_6823")

    label("loc_6225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62C4")
    OP_4B(0xF, 0xFF)

    #C0388
    ChrTalk(
        0xFE,
        (
            "玛丽，今天我用这个\x01",
            "跟你玩哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        "（晃晃晃）……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    #C0390
    ChrTalk(
        0xF,
        "呜喵喵……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "哇……\x01",
            "它真的喜欢呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_630B")

    label("loc_62C4")


    #C0392
    ChrTalk(
        0xFE,
        (
            "这是摆摊的哥哥\x01",
            "送我的\x01",
            "『逗猫棒』。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "呵呵，玛丽\x01",
            "好像很喜欢呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_630B")

    Jump("loc_6823")

    label("loc_6310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_631E")
    Jump("loc_6823")

    label("loc_631E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_63FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6390")

    #C0394
    ChrTalk(
        0xFE,
        (
            "那是爸爸的床，\x01",
            "这是妈妈和\x01",
            "萨妮塔的床。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "玛丽，你记住了吗？\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xF,
        "喵呜……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_63F9")

    label("loc_6390")


    #C0397
    ChrTalk(
        0xFE,
        (
            "为了不让玛丽\x01",
            "再次跑丢，\x01",
            "我正在教它记住家里的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "只要让它记住这些，\x01",
            "应该就不会再出问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63F9")

    Jump("loc_6823")

    label("loc_63FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_65FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64E2")
    OP_4B(0xD, 0xFF)

    #C0399
    ChrTalk(
        0xE,
        (
            "呜呜，玛丽……\x01",
            "对不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "是、是我不好……\x01",
            "都是我不好……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xD,
        "萨妮塔……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        "#00100F（……得赶快把猫找回来啊。）\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#00000F（是啊……\x01",
            "  尽全力去找吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_6524")

    label("loc_64E2")


    #C0404
    ChrTalk(
        0xFE,
        (
            "呜呜，玛丽……\x01",
            "对不起。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "是、是我不好……\x01",
            "都是我不好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6524")

    Jump("loc_65F7")

    label("loc_6529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65A0")
    OP_4B(0xF, 0xFF)

    #C0406
    ChrTalk(
        0xE,
        "真是太好了，玛丽……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xE,
        (
            "真是的……作为处罚，\x01",
            "今天我会一直抱着你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xF,
        "喵、喵呜～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    Jump("loc_65F7")

    label("loc_65A0")

    OP_4B(0xF, 0xFF)

    #C0409
    ChrTalk(
        0xE,
        (
            "好了，玛丽，\x01",
            "做好心理准备吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xE,
        "（紧抱）～～～～～～\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xF,
        "喵、喵呜～⊥\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_65F7")

    Jump("loc_6823")

    label("loc_65FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_66ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669B")

    #C0412
    ChrTalk(
        0xFE,
        (
            "我很喜欢\x01",
            "我们现在的\x01",
            "新家。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "不过，自从搬到这里之后，\x01",
            "玛丽的样子\x01",
            "就有点怪怪的。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "说不定是因为\x01",
            "突然搬家，\x01",
            "让它受惊了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_66E8")

    label("loc_669B")


    #C0415
    ChrTalk(
        0xFE,
        (
            "总觉得玛丽\x01",
            "好像一直在发抖……\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "大概是因为\x01",
            "突然搬家，\x01",
            "让它受惊了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E8")

    Jump("loc_6823")

    label("loc_66ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_681A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6712")
    Call(0, 15)
    Jump("loc_676B")

    label("loc_6712")


    #C0417
    ChrTalk(
        0xFE,
        (
            "嘿嘿，幸好我早有准备，\x01",
            "让玛丽学会了怎么\x01",
            "跟人打招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "多亏如此，\x01",
            "才没有出丑呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_676B")

    Jump("loc_6815")

    label("loc_6770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C9")

    #C0419
    ChrTalk(
        0xFE,
        (
            "呵呵，玛丽真是个\x01",
            "聪明懂事的好孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "我来给你抓抓痒\x01",
            "作为奖励吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6815")

    label("loc_67C9")


    #C0421
    ChrTalk(
        0xFE,
        (
            "爸爸和妈妈的感情\x01",
            "比以前更好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "看到他们这样，萨妮塔\x01",
            "真的好高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6815")

    Jump("loc_6823")

    label("loc_681A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6823")

    label("loc_6823")

    TalkEnd(0xFE)
    Return()

    # Function_18_5E23 end

    def Function_19_6827(): pass

    label("Function_19_6827")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_684A")

    #C0423
    ChrTalk(
        0xFE,
        "……喵呜……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_684A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6864")

    #C0424
    ChrTalk(
        0xFE,
        "喵呜？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_6864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_687E")

    #C0425
    ChrTalk(
        0xFE,
        "喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_687E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6898")

    #C0426
    ChrTalk(
        0xFE,
        "喵呜。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_6898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_68B2")

    #C0427
    ChrTalk(
        0xFE,
        "喵呜～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_68B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_68CC")

    #C0428
    ChrTalk(
        0xFE,
        "喵呜～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_68CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6901")
    TurnDirection(0xF, 0xE, 500)
    Sleep(500)

    #C0429
    ChrTalk(
        0xFE,
        (
            "喵喵……\x01",
            "（擦脸、擦脸）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_6901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_691F")

    #C0430
    ChrTalk(
        0xFE,
        "唔喵喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_691F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_692D")
    Jump("loc_6A9A")

    label("loc_692D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6949")

    #C0431
    ChrTalk(
        0xFE,
        "喵～唔。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_6949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6A23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C7")
    OP_4B(0xE, 0xFF)

    #C0432
    ChrTalk(
        0xE,
        "真是太好了，玛丽……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        (
            "真是的……作为处罚，\x01",
            "今天我会一直抱着你哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xF,
        "喵、喵～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xE, 0xFF)
    Jump("loc_6A1E")

    label("loc_69C7")

    OP_4B(0xE, 0xFF)

    #C0435
    ChrTalk(
        0xE,
        (
            "好了，玛丽，\x01",
            "做好心理准备吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        "（紧抱）～～～～～～\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xF,
        "喵、喵呜～⊥\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)

    label("loc_6A1E")

    Jump("loc_6A9A")

    label("loc_6A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6A3D")

    #C0438
    ChrTalk(
        0xFE,
        "喵……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A9A")

    label("loc_6A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A61")

    #C0439
    ChrTalk(
        0xFE,
        "喵呜～\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A8C")

    label("loc_6A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A80")

    #C0440
    ChrTalk(
        0xFE,
        "喵喵呜～⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A8C")

    label("loc_6A80")


    #C0441
    ChrTalk(
        0xFE,
        "喵喵¤\x02",
    )

    CloseMessageWindow()

    label("loc_6A8C")

    Jump("loc_6A9A")

    label("loc_6A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6A9A")

    label("loc_6A9A")

    TalkEnd(0xFE)
    Return()

    # Function_19_6827 end

    def Function_20_6A9E(): pass

    label("Function_20_6A9E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6B1F")
    OP_4B(0x8, 0xFF)

    #C0442
    ChrTalk(
        0xFE,
        (
            "因为我们也不能\x01",
            "妨碍你的工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        (
            "在工作结束之前，\x01",
            "你可要好好注意身体。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x8,
        "嗯……我会注意的。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_6B9F")

    label("loc_6B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6B9F")
    OP_4B(0x8, 0xFF)

    #C0445
    ChrTalk(
        0xFE,
        (
            "说起来，老公你\x01",
            "是不是瘦了？\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "可不能因为现在是独居，\x01",
            "就随便吃些东西\x01",
            "凑和哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        "哈哈……要求真严啊。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_6B9F")

    TalkEnd(0xFE)
    Return()

    # Function_20_6A9E end

    def Function_21_6BA3(): pass

    label("Function_21_6BA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6BEB")

    #C0448
    ChrTalk(
        0xFE,
        (
            "啧～必须要\x01",
            "回去了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        "我好想再来看爸爸啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C44")

    label("loc_6BEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6C44")

    #C0450
    ChrTalk(
        0xFE,
        (
            "爸爸～\x01",
            "你前不久寄的那些花车\x01",
            "游行的照片真的好漂亮！\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        "就是拍得有点模糊～\x02",
    )

    CloseMessageWindow()

    label("loc_6C44")

    TalkEnd(0xFE)
    Return()

    # Function_21_6BA3 end

    def Function_22_6C48(): pass

    label("Function_22_6C48")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50090, 1430, 52450, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 49700, 30, 51700, 360)
    SetChrPos(0x102, 50700, 30, 51700, 360)
    SetChrPos(0x109, 49600, 30, 50700, 360)
    SetChrPos(0x105, 50800, 30, 50700, 360)
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)
    FadeToBright(1000, 0)
    OP_0D()

    #C0452
    ChrTalk(
        0xD,
        "哎呀，有客人呢。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        "哦？你们是……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        (
            "#12P#00000F我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的人。\x02\x03",

            "您是本德先生吧？\x01",
            "上次和您见面，\x01",
            "还是在教团事件的时候了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E41")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0455
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K前作「寻找迷路小猫的主主」？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【完成】\x01",          # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E2D")
    OP_29(0x8, 0x4, 0x10)
    Jump("loc_6E41")

    label("loc_6E2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E41")
    OP_29(0x8, 0x3, 0x10)

    label("loc_6E41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6F34")

    #C0456
    ChrTalk(
        0xC,
        "啊，我当然记得你们。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xC,
        (
            "再怎么说，把我们从那个\x01",
            "『堡垒』的牢房里救出来的人\x01",
            "就是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xC,
        (
            "说起来，我们刚开始饲养\x01",
            "玛丽的时候，也受到你们\x01",
            "不少关照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xC,
        (
            "哎呀，我早就想郑重\x01",
            "向你们道声谢了。\x01",
            "那个时候真是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FD6")

    label("loc_6F34")


    #C0460
    ChrTalk(
        0xC,
        "啊，我当然记得你们。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xC,
        (
            "再怎么说，把我们从那个\x01",
            "『堡垒』的牢房里救出来的人\x01",
            "就是你们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "哎呀，我早就想郑重\x01",
            "向你们道声谢了。\x01",
            "那个时候真是太感谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FD6")


    #C0463
    ChrTalk(
        0xD,
        (
            "我也要向各位\x01",
            "道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xD,
        (
            "当时多亏各位\x01",
            "帮助了我丈夫。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#12P#00004F哪里，不必客气。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#12P#00100F是啊，\x01",
            "看到您这么精神，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xC,
        "哈哈，这也是托了你们的福。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "对了，各位今天来这里，\x01",
            "是有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#12P#00000F其实是这样……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0470
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将调查一事向本德做了说明之后，\x01",
            "向其询问了迁居的缘由。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0471
    ChrTalk(
        0xC,
        (
            "原来如此，\x01",
            "可疑的住户变更表吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        (
            "所以，你们是想问我\x01",
            "为何会卖掉那栋房子？\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#12P#00103F是的，我们知道这很失礼，\x01",
            "但还是希望能确认一下\x01",
            "手续中是否存在违法之处……\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xC,
        (
            "不，这个要求很合理，\x01",
            "并没有什么失礼的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xC,
        (
            "简要而言，\x01",
            "我是为了清还债务，\x01",
            "才会将房屋出售。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xC,
        (
            "卖出与购入都经由同一所房产公司，\x01",
            "手续也是正规的……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xC,
        (
            "所以这宗交易应该没有\x01",
            "任何违法之处。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        "#12P#00005F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#12P#00103F嗯……如果方便，\x01",
            "我想问个问题……\x02\x03",

            "#00101F请问您为何会\x01",
            "背上那么沉重的债务呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        (
            "哦，\x01",
            "其实原因很简单……\x01",
            "完全是我自作自受。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xC,
        (
            "有关当时的记忆，\x01",
            "如今已经不是很清晰了……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xC,
        (
            "总之，我在服用那种蓝色药片的时期，\x01",
            "曾经大量买入过\x01",
            "风险性极高的股票。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xC,
        (
            "教团事件结束的时候，\x01",
            "那些股票的市值瞬间暴跌……\x01",
            "使我背上了巨额债务。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x109,
        "#12P#10105F居、居然发生了那种事……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xC,
        (
            "是啊。\x01",
            "不过，我还算运气好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xC,
        (
            "变卖掉包括那栋房子在内的全部财产后，\x01",
            "就把债务还得差不多了……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xC,
        (
            "损害最终控制在了我个人能承担的范围内，\x01",
            "总算没有被公司炒鱿鱼。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    #C0488
    ChrTalk(
        0xC,
        (
            "另外，最重要的是……\x01",
            "妻子和女儿都没有离弃\x01",
            "如此无可救药的我。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    #C0489
    ChrTalk(
        0xD,
        (
            "#11P老公……\x01",
            "我们说好了不说这个的。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xD,
        (
            "#11P毕竟我们彼此是\x01",
            "最重要的家人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xD,
        "#11P同甘共苦是理所当然的呀。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        "库雷优……真是太谢谢你了。\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xC,
        (
            "我打从心底感谢\x01",
            "你和萨妮塔。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    #C0494
    ChrTalk(
        0xD,
        (
            "#11P老、老公……\x01",
            "大家都在看着呢，\x01",
            "多不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#12P#10109F呵呵，你们之间有着\x01",
            "坚固的羁绊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x105,
        (
            "#12P#10304F嗯，在家人间的羁绊面前，\x01",
            "住所这种小问题根本就不值一提吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)

    #C0497
    ChrTalk(
        0xC,
        (
            "哈哈，其实也没有\x01",
            "你们说的那么伟大……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xC,
        (
            "总之，我会振奋精神，\x01",
            "拼命努力工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        (
            "这也是为了把剩下的债务全部还清，\x01",
            "好好回报妻子和女儿。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    #C0500
    ChrTalk(
        0xD,
        "老公……\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        (
            "#12P#00104F真是个很好的目标呢。\x02\x03",

            "#00100F如果今后有什么事，\x01",
            "请不要客气，\x01",
            "尽管委托我们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)

    #C0502
    ChrTalk(
        0x101,
        (
            "#12P#00000F没错，我们到时\x01",
            "一定会马上赶来。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        (
            "哈哈，你们能\x01",
            "这么说，\x01",
            "我实在非常感激。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xC,
        (
            "嗯，如果发生了什么事，\x01",
            "就拜托你们帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xC,
        (
            "对了，你们来这里\x01",
            "就只是为了这件事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "如果还有什么其它问题，\x01",
            "我都会回答你们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#12P#00000F我们已经得到了\x01",
            "需要的情报，这就足够了。\x02\x03",

            "#00004F十分感谢您积极\x01",
            "配合我们的调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x105,
        "#12P#10300F那我们就到下一个地方去吧？\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        (
            "#12P#00100F嗯，说的也是。\x02\x03",

            "#00104F那么……本德先生，\x01",
            "我们就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x109,
        (
            "#12P#10109F希望您一家人永远\x01",
            "都像现在这样融洽。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xC,
        "嗯嗯，一定！\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xD,
        "呵呵呵，当然。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49250, 1400, 2740, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17020, 0)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 52000, 0, 6750, 180)
    SetChrPos(0x109, 52000, 0, 6750, 180)
    SetChrPos(0x102, 52000, 0, 6750, 180)
    SetChrPos(0x105, 52000, 0, 6750, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)

    def lambda_7A91():
        OP_95(0xFE, 51400, 0, 2650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A91)

    def lambda_7AAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7AAB)
    Sleep(900)

    def lambda_7ABF():
        OP_95(0xFE, 52300, 0, 2750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7ABF)

    def lambda_7AD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7AD9)
    Sleep(900)

    def lambda_7AED():
        OP_95(0xFE, 51400, 0, 3650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AED)

    def lambda_7B07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7B07)
    Sleep(900)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_7B2D():
        OP_95(0xFE, 52300, 0, 3750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B2D)

    def lambda_7B47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7B47)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(200)

    def lambda_7B73():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7B73)
    Sleep(50)

    def lambda_7B83():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_7B83)
    Sleep(1000)

    #C0513
    ChrTalk(
        0xE,
        "#6P哎呀，大哥哥……\x02",
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

    def lambda_7C00():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C00)
    Sleep(50)

    def lambda_7C10():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C10)
    Sleep(50)

    def lambda_7C20():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C20)
    Sleep(50)

    def lambda_7C30():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C30)
    Sleep(50)

    def lambda_7C40():
        OP_95(0x101, 50250, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C40)
    Sleep(50)

    def lambda_7C5D():
        OP_95(0x102, 50500, 0, 3650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C5D)
    Sleep(50)

    def lambda_7C7A():
        OP_95(0x109, 51500, 0, 2550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C7A)
    Sleep(50)

    def lambda_7C97():
        OP_95(0x105, 51750, 0, 3750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C97)
    SetMapObjFlags(0x1, 0x0)
    WaitChrThread(0x101, 1)

    #C0514
    ChrTalk(
        0xE,
        (
            "#6P找爸爸和妈妈\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        (
            "#00000F是啊，跟他们\x01",
            "稍微聊了聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#11P#00100F你是叫萨妮塔吧？\x01",
            "你的父母都很好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0517
    ChrTalk(
        0xE,
        "#6P你、你也这么觉得吗？\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xE,
        (
            "#6P呵呵，\x01",
            "在搬家之后，\x01",
            "他们的感情比以前更好了……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xE,
        (
            "#6P嘿嘿，\x01",
            "是我引以为傲的双亲哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0520
    ChrTalk(
        0xE,
        "#12P玛丽，你也这么觉得吧？\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    #C0521
    ChrTalk(
        0xF,
        "#6P喵呜～⊥\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x109,
        "#10102F呵呵，他们能这么乐观，真好。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        "#00000F是啊，真是太好了。\x02",
    )

    CloseMessageWindow()

    def lambda_7E4D():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E4D)
    Sleep(50)

    def lambda_7E5D():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E5D)
    Sleep(50)

    def lambda_7E6D():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E6D)
    Sleep(50)

    def lambda_7E7D():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E7D)

    #C0524
    ChrTalk(
        0x101,
        (
            "#12P#00003F好了，这样就确认过\x01",
            "本德先生的情况了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA0")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0525
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆「调查状况？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【未变更】\x01",                  # 0
            "【还有其它】\x01",                # 1
            "【六处地点已调查完毕】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7F73"),
        (1, "loc_7F78"),
        (2, "loc_7F8C"),
        (SWITCH_DEFAULT, "loc_7FA0"),
    )


    label("loc_7F73")

    Jump("loc_7FA0")

    label("loc_7F78")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_7FA0")

    label("loc_7F8C")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_7FA0")

    label("loc_7FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FF2")

    #C0526
    ChrTalk(
        0x101,
        (
            "#12P#00000F那么，我们继续去\x01",
            "调查剩下的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8039")

    label("loc_7FF2")


    #C0527
    ChrTalk(
        0x101,
        (
            "#12P#00000F好，已经全部调查完毕了。\x02\x03",

            "去市民会馆汇报结果吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_8039")

    OP_93(0xE, 0x5A, 0x0)
    OP_93(0xF, 0x5A, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xE, 0x0, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    SetScenarioFlags(0x131, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51000, 0, 3400, 225)
    EventEnd(0x5)
    Return()

    # Function_22_6C48 end

    def Function_23_809F(): pass

    label("Function_23_809F")

    EventBegin(0x0)
    Fade(500)
    OP_68(51550, 1420, 51330, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 51730, 0, 52230, 90)
    SetChrPos(0x102, 51730, 0, 51030, 90)
    SetChrPos(0x109, 50530, 0, 52230, 90)
    SetChrPos(0x105, 50530, 0, 51030, 90)
    SetChrPos(0x104, 49330, 0, 51530, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_0D()

    #C0528
    ChrTalk(
        0xE,
        (
            "呜呜、呜呜呜……\x01",
            "是萨妮塔不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xE,
        (
            "都怪萨妮塔没有好好\x01",
            "照看着玛丽……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xD,
        (
            "萨妮塔……\x01",
            "你别太自责了。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "#5P是啊，而且一定能把\x01",
            "玛丽找回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xC,
        (
            "#5P所以，萨妮塔，\x01",
            "打起精神来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x10E, 0x1F4)

    #C0533
    ChrTalk(
        0xC,
        "#11P啊！几位是……！\x02",
    )

    CloseMessageWindow()

    def lambda_8236():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8236)
    Sleep(50)

    def lambda_8246():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8246)
    WaitChrThread(0xD, 1)

    #C0534
    ChrTalk(
        0xD,
        "哎呀……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#6P#00000F你们好，\x01",
            "我们看到支援请求，所以就赶过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xC,
        (
            "#11P你们真的来了啊……\x01",
            "太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xC,
        (
            "#11P老实说，相比找警察，\x01",
            "这件事情还是委托给\x01",
            "游击士更加合适……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xC,
        (
            "#11P但我一下就想到了你们，\x01",
            "所以就发出请求了。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x102,
        (
            "#6P#00100F原来如此，您能这么说，\x01",
            "我们也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x109,
        (
            "#6P#10103F听说小猫玛丽\x01",
            "失踪了……？\x02\x03",

            "#10100F具体是从何时开始\x01",
            "不见踪影的？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xC,
        (
            "#11P这个嘛，虽然不能确定\x01",
            "具体时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xC,
        "#11P但肯定是昨天傍晚的事。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xD,
        (
            "我们一家人在东街\x01",
            "逛露天摊的时候，\x01",
            "萨妮塔突然发现它不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xD,
        (
            "只是一时不注意，\x01",
            "它就突然不见了踪影……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xD,
        (
            "在那之后，露天店街的各位\x01",
            "也帮忙在附近\x01",
            "搜寻了许久……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xC,
        (
            "#11P嗯，天黑之前，\x01",
            "大家都在帮忙寻找，\x01",
            "可直到最后都没能找到。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 500)

    #C0547
    ChrTalk(
        0xE,
        (
            "呜呜、呜呜呜……\x01",
            "爸爸骗人！\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xE,
        (
            "你不是说玛丽今天早上\x01",
            "就会回来的吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    #C0549
    ChrTalk(
        0xC,
        "#5P对不起，萨妮塔……\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x102,
        "#6P#00108F萨妮塔……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#6P#00001F那么……\x01",
            "有没有什么目击情报？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85B2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_85B2)
    Sleep(50)

    def lambda_85C2():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_85C2)
    WaitChrThread(0xE, 2)

    #C0552
    ChrTalk(
        0xC,
        (
            "#11P嗯，不过都是\x01",
            "昨天的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xC,
        (
            "#11P根据大家提供的消息，\x01",
            "我想它应该没有\x01",
            "离开市内。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xC,
        (
            "#11P因为有人看到玛丽\x01",
            "往中央广场走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xC,
        (
            "#11P但当时天色已晚，\x01",
            "没法继续追寻下去，\x01",
            "所以只能放弃……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        (
            "#6P#00301F……然后它就音讯全无，\x01",
            "直到今天早上吗？\x02\x03",

            "#00303F这样一来，不管它跑到\x01",
            "市内的什么地方，\x01",
            "也都不足为奇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x105,
        (
            "#6P#10300F也就是说，搜索范围是\x01",
            "整个市内吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        (
            "#6P#00006F唔……线索要是\x01",
            "再多一点就好了……\x02\x03",

            "#00001F对了……\x01",
            "请问玛丽以前有没有\x01",
            "像这次这样跑丢过？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xC,
        "#11P不，从来没有。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xC,
        (
            "#11P因为萨妮塔总和\x01",
            "玛丽待在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xC,
        (
            "#11P而且它十分胆小，\x01",
            "很难想象它会独自离开，\x01",
            "跑到其它地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xC,
        (
            "#11P所以我认为它肯定是\x01",
            "因为什么原因而迷路的……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x101,
        "#6P#00003F是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x102,
        (
            "#6P#00100F总之，我们也只能先到大街上\x01",
            "找找看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#6P#00000F是啊，就先从\x01",
            "这一步开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xC,
        (
            "#11P等萨妮塔平静一点之后，\x01",
            "我也会出去继续找的……\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xC,
        (
            "#11P这大概会是一场持久战，\x01",
            "如果你们还有其它要事，\x01",
            "不妨把这件事情留到后面处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        "#6P#00000F这个嘛……\x02",
    )

    CloseMessageWindow()
    OP_29(0x74, 0x1, 0x0)
    Call(0, 24)
    EventEnd(0x5)
    Return()

    # Function_23_809F end

    def Function_24_8982(): pass

    label("Function_24_8982")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【马上开始搜寻】\x01",        # 0
            "【请对方稍等一阵】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A38")

    #C0569
    ChrTalk(
        0x101,
        (
            "#6P#00000F不，并没有其它要事，\x01",
            "我们马上就开始搜寻。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xC,
        "#11P是吗，那真是帮大忙了。\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_8AA6")

    label("loc_8A38")

    OP_29(0x74, 0x1, 0x1)

    #C0571
    ChrTalk(
        0x101,
        (
            "#6P#00000F既然如此，实在不好意思……\x01",
            "您可以再等我们\x01",
            "一段时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xC,
        "#11P没问题，那就稍后再见吧。\x02",
    )

    CloseMessageWindow()

    label("loc_8AA6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x155, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51730, 0, 52230, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_24_8982 end

    def Function_25_8AF7(): pass

    label("Function_25_8AF7")

    EventBegin(0x0)
    Fade(500)
    OP_68(51550, 1420, 51330, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 51730, 0, 52230, 90)
    SetChrPos(0x102, 51730, 0, 51030, 90)
    SetChrPos(0x109, 50530, 0, 52230, 90)
    SetChrPos(0x105, 50530, 0, 51030, 90)
    SetChrPos(0x104, 49330, 0, 51530, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0xD, 0x10E, 0x0)
    OP_93(0xE, 0x10E, 0x0)
    OP_0D()

    #C0573
    ChrTalk(
        0xC,
        "#11P哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xC,
        (
            "#11P可以开始搜寻\x01",
            "玛丽了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【开始搜寻小猫】\x01",        # 0
            "【请对方稍等一阵】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8C")

    #C0575
    ChrTalk(
        0x101,
        (
            "#6P#00000F没问题，\x01",
            "我们这就开始搜寻。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xC,
        "#11P谢谢，真是帮大忙了。\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_8CFB")

    label("loc_8C8C")


    #C0577
    ChrTalk(
        0x101,
        (
            "#6P#00006F不好意思，\x01",
            "我们还要再准备一下……\x02\x03",

            "#00000F您可以再等我们\x01",
            "一段时间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xC,
        "#11P好的，我明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_8CFB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51730, 0, 52230, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_8AF7 end

    def Function_26_8D49(): pass

    label("Function_26_8D49")

    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0579
    ChrTalk(
        0x102,
        (
            "#6P#00100F那么……罗伊德，\x01",
            "先从哪里开始调查？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0580
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯……这或许只是在重复调查\x01",
            "他们昨天找过的地方……\x02\x03",

            "#00000F但我们还是先从玛丽失去踪影的地方，\x01",
            "也就是东街开始调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x104,
        "#6P#00300F也对，这样最妥当。\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x105,
        "#6P#10304F呵呵，这就是调查的基本原则吧？\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x109,
        (
            "#6P#10100F对了，玛丽有可能会到\x01",
            "东街的什么地方呢，\x01",
            "各位有没有头绪？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8EB0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EB0)
    Sleep(50)

    def lambda_8EC0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8EC0)
    Sleep(300)

    #C0584
    ChrTalk(
        0xD,
        (
            "啊，那应该就是\x01",
            "路边摊一条街中的鱼摊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xD,
        (
            "在东街，\x01",
            "它最喜欢那里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xC,
        (
            "#11P是啊，今天早上还没有\x01",
            "去调查过，说不定\x01",
            "它会突然出现在那附近呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xC,
        (
            "#11P摊主玛尔缇女士昨天也曾\x01",
            "帮我们一起搜寻过玛丽，\x01",
            "要是它过去了，她肯定会注意到。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xC,
        (
            "#11P如果可以，\x01",
            "请各位找她打听一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x101,
        "#6P#00000F原来如此，我明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xC, 500)
    Sleep(300)

    #C0590
    ChrTalk(
        0x102,
        (
            "#6P#00100F对了，本德先生，\x01",
            "您接下来有何打算？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)
    Sleep(300)

    #C0591
    ChrTalk(
        0xC,
        "#11P正好我今天休假。\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xC,
        (
            "#11P稍后\x01",
            "就会出去\x01",
            "继续搜寻玛丽……\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xC,
        (
            "#11P因为昨天已经在东街\x01",
            "打听过一圈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xC,
        (
            "#11P所以我今天打算\x01",
            "去中央广场\x01",
            "收集信息。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xC,
        (
            "#11P如果有什么发现，\x01",
            "请各位随时联系我。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x104,
        "#6P#00300F明白了。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x105,
        (
            "#12P#10300F那么，我们先去路边摊的\x01",
            "鱼摊问问情况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        "#6P#00000F嗯，这就出发吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0599
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找小猫的委托】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x154, 7)
    OP_29(0x74, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51730, 0, 52230, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_26_8D49 end

    def Function_27_9232(): pass

    label("Function_27_9232")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(50170, 1420, 530, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 51040, 30, 1350, 0)
    SetChrPos(0xC, 49720, 0, 3350, 180)
    SetChrPos(0xD, 52360, 0, 3350, 180)
    SetChrPos(0xE, 51040, 0, 3350, 180)
    SetChrPos(0x101, 52320, 20, 0, 0)
    SetChrPos(0x1A3, 50960, 20, 0, 0)
    SetChrPos(0x102, 51680, 20, -980, 0)
    SetChrPos(0x104, 51340, 0, -3020, 0)
    SetChrPos(0x109, 50390, 30, -1740, 0)
    SetChrPos(0x105, 52250, 30, -1900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    SetCameraDistance(21000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0600
    ChrTalk(
        0xE,
        "#5P玛丽……！\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xE,
        "#5P真是的……你到底去了哪里啊！\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xE,
        (
            "#5P呜呜、呜呜……\x01",
            "我真的、真的……\x01",
            "……很担心……你啊………\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xF,
        "#12P喵，喵呜～\x02",
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(300)

    #C0604
    ChrTalk(
        0xE,
        (
            "#5P对……对不起，\x01",
            "都是我不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xE,
        (
            "#5P谢谢你……\x01",
            "谢谢你回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xE,
        (
            "#5P今后可不能再擅自\x01",
            "乱跑了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    Sound(953, 0, 100, 0)

    #C0607
    ChrTalk(
        0xF,
        "#12P喵呜～⊥\x02",
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x102,
        "#12P#00109F呵呵，真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x109,
        "#12P#10100F这件事情顺利解决了呢。\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xC,
        (
            "我该如何\x01",
            "感谢你们才好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xC,
        (
            "多谢各位帮我们找回了\x01",
            "重要的家庭成员玛丽。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xD,
        "是啊，实在是感激不尽。\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xD,
        (
            "你们以前救过我老公，\x01",
            "这次又找回了玛丽……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xD,
        (
            "各位真是我们一家的\x01",
            "最大恩人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        (
            "#12P#00002F哪、哪里，言重了……\x02\x03",

            "#00000F而且在这次的事件中，\x01",
            "这个女孩才是\x01",
            "功劳最大的人。\x02\x03",

            "她还让恐慌不安的\x01",
            "玛丽平静了下来……\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xF, 0xB4, 0xC8, 0x3E8, 0x0)
    TurnDirection(0xF, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    #C0616
    ChrTalk(
        0xF,
        "#5P喵呜～⊥\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xE,
        "#5P……玛丽！？\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xE,
        (
            "#5P你该不会是想\x01",
            "和那个姐姐\x01",
            "在一起吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0xE, 500)
    OP_63(0xF, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0619
    ChrTalk(
        0xF,
        "#12P喵、喵呜……？\x02",
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x1A3,
        (
            "#12P#04602F啊哈哈，你不用担心。\x02\x03",

            "#04604F我和玛丽聊过了，\x01",
            "它说它最喜欢萨妮塔～\x02\x03",

            "#04609F而且还给我讲了好多关于你的事情，\x01",
            "真是服了它。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0621
    ChrTalk(
        0xE,
        "#5P真、真的吗，玛丽？\x02",
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    #C0622
    ChrTalk(
        0xF,
        "#12P喵呜～⊥\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x1A3,
        (
            "#12P#04609F呵呵，好啦，\x01",
            "我差不多也该回去了。\x02\x03",

            "#04604F今天和几位小哥玩得很开心，\x01",
            "还认识了玛丽。\x02\x03",

            "#04611F更重要的是，\x01",
            "发现了最棒的目标呢⊥\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9838():

        label("loc_9838")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_9838")

    QueueWorkItem2(0x101, 2, lambda_9838)
    Sleep(300)

    #C0624
    ChrTalk(
        0x101,
        "#11P#00005F咦……\x02",
    )

    CloseMessageWindow()

    def lambda_9864():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_9864)
    Sleep(50)

    def lambda_9881():

        label("loc_9881")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_9881")

    QueueWorkItem2(0x102, 2, lambda_9881)
    Sleep(50)

    def lambda_9896():

        label("loc_9896")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_9896")

    QueueWorkItem2(0x104, 2, lambda_9896)
    Sleep(50)

    def lambda_98AB():

        label("loc_98AB")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_98AB")

    QueueWorkItem2(0x109, 2, lambda_98AB)
    Sleep(50)

    def lambda_98C0():

        label("loc_98C0")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_98C0")

    QueueWorkItem2(0x105, 2, lambda_98C0)
    Sleep(50)

    def lambda_98D5():

        label("loc_98D5")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_98D5")

    QueueWorkItem2(0xC, 2, lambda_98D5)
    Sleep(50)

    def lambda_98EA():

        label("loc_98EA")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_98EA")

    QueueWorkItem2(0xD, 2, lambda_98EA)
    Sleep(50)

    def lambda_98FF():

        label("loc_98FF")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_98FF")

    QueueWorkItem2(0xE, 2, lambda_98FF)
    Sleep(50)

    def lambda_9914():

        label("loc_9914")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_9914")

    QueueWorkItem2(0xF, 2, lambda_9914)
    WaitChrThread(0x1A3, 1)

    #C0625
    ChrTalk(
        0x104,
        "#00305F喂、喂……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A3, 0x87, 0x1F4)
    Sleep(300)

    #C0626
    ChrTalk(
        0x1A3,
        (
            "#6P#04602F啊哈哈，再见啦～！\x02\x03",

            "#04609F也许过不了多久\x01",
            "就会再次见面了哟！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_999B():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_999B)
    Sleep(300)

    def lambda_99B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_99B8)
    WaitChrThread(0x1A3, 1)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0627
    ChrTalk(
        0x102,
        "#00106F……这……\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x109,
        (
            "#10106F那、那孩子简直\x01",
            "就像一股台风啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，与其说是台风，\x01",
            "还是用龙卷风来形容更合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x104,
        (
            "#00306F真是的，叔叔应该\x01",
            "多管管她啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x101,
        (
            "#00012F不、不过，这次真是\x01",
            "多亏有她帮助呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xC,
        (
            "唔……如果可以，\x01",
            "真想向那个女孩郑重道声谢……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(300)

    #C0633
    ChrTalk(
        0xC,
        (
            "总之，诸位……\x01",
            "再次感谢你们的帮助。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B9E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B9E)
    Sleep(50)

    def lambda_9BAE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_9BAE)

    def lambda_9BBB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9BBB)
    Sleep(50)

    def lambda_9BCB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9BCB)

    def lambda_9BD8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9BD8)
    Sleep(50)

    def lambda_9BE8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_9BE8)

    def lambda_9BF5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9BF5)
    Sleep(50)

    def lambda_9C05():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9C05)
    WaitChrThread(0x105, 2)

    #C0634
    ChrTalk(
        0xD,
        "我一辈子都不会忘记你们的大恩。\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xE,
        (
            "对了，萨妮塔也要\x01",
            "向大家道谢！\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xF,
        "喵呜⊥\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        "#12P#00009F哈哈，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x102,
        (
            "#12P#00100F今后如果发生了什么事情，\x01",
            "请不要客气，尽管联络我们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0639
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【寻找小猫的委托】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x74, 0x1, 0x8)
    OP_29(0x74, 0x4, 0x10)
    OP_C9(0x1, 0x1000)
    OP_29(0xA3, 0x1, 0xE)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetChrPos(0xC, 53730, 0, 52730, 180)
    SetChrPos(0xD, 53730, 0, 50730, 0)
    SetChrPos(0xE, 53730, 0, 51730, 270)
    SetChrPos(0xF, 52730, 0, 51730, 90)
    BeginChrThread(0xF, 0, 0, 0)
    RemoveParty(0xA2, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 50960, 20, 0, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_9232 end

    def Function_28_9DAA(): pass

    label("Function_28_9DAA")

    EventBegin(0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0640
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x01",
            "看来住户已经离去了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 51800, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_28_9DAA end

    def Function_29_9DF5(): pass

    label("Function_29_9DF5")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0641
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
    EventEnd(0x3)
    Return()

    # Function_29_9DF5 end

    SaveToFile()

Try(main)
