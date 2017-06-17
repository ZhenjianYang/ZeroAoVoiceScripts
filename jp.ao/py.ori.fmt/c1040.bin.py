from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "マーシー",               # 1
        "サリナ",                 # 2
        "ユゴット",               # 3
        "クラリス",               # 4
        "ボンド",                 # 5
        "クレイユ",               # 6
        "サニータ",               # 7
        "マリー",                 # 8
        "セピア",                 # 9
        "ウーナ",                 # 10
        "アゼル",                 # 11
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
        "Function_9_27DE",         # 09, 9
        "Function_10_2ACD",        # 0A, 10
        "Function_11_3BF6",        # 0B, 11
        "Function_12_3CF7",        # 0C, 12
        "Function_13_4402",        # 0D, 13
        "Function_14_474B",        # 0E, 14
        "Function_15_5512",        # 0F, 15
        "Function_16_5695",        # 10, 16
        "Function_17_6282",        # 11, 17
        "Function_18_6D53",        # 12, 18
        "Function_19_7A2F",        # 13, 19
        "Function_20_7D10",        # 14, 20
        "Function_21_7E4F",        # 15, 21
        "Function_22_7F32",        # 16, 22
        "Function_23_9703",        # 17, 23
        "Function_24_A218",        # 18, 24
        "Function_25_A3AD",        # 19, 25
        "Function_26_A645",        # 1A, 26
        "Function_27_AC2A",        # 1B, 27
        "Function_28_B938",        # 1C, 28
        "Function_29_B995",        # 1D, 29
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
    SetChrPos(0xC, 46190, 380, 52360, 0)
    ClearChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 45240, 380, 52380, 0)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1130")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E17")
    Call(0, 9)
    Jump("loc_FB0")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F36")

    #C0001
    ChrTalk(
        0xFE,
        "もしお父さんが生きてたら……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "やっぱり警備隊として、\x01",
            "諦めずに最後まで戦うことを\x01",
            "選んだでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……特務支援課の皆さん、\x01",
            "ノエルとフランをよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "この事態を解決するために、\x01",
            "存分にこき使ってやってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x109,
        "#10109Fもう……母さんったら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_FB0")

    label("loc_F36")


    #C0006
    ChrTalk(
        0xFE,
        (
            "特務支援課の皆さん、\x01",
            "ノエルとフランをよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "この事態を解決するために、\x01",
            "存分にこき使ってやってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB0")

    Jump("loc_112B")

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B1")

    #C0008
    ChrTalk(
        0xFE,
        "もしお父さんが生きてたら……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "やっぱり警備隊として、\x01",
            "諦めずに最後まで戦うことを\x01",
            "選んだでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……特務支援課の皆さん、\x01",
            "ノエルとフランをよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "この事態を解決するために、\x01",
            "存分にこき使ってやってちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_112B")

    label("loc_10B1")


    #C0012
    ChrTalk(
        0xFE,
        (
            "特務支援課の皆さん、\x01",
            "ノエルとフランをよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "この事態を解決するために、\x01",
            "存分にこき使ってやってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112B")

    Jump("loc_27DA")

    label("loc_1130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12F4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115B")
    Call(0, 9)
    Jump("loc_1253")

    label("loc_115B")


    #C0014
    ChrTalk(
        0xFE,
        (
            "アゼル君も手伝いに来てくれてるし、\x01",
            "ここは大丈夫よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "もしあの化物が入ってきても、\x01",
            "ユゴット君やサニータちゃんには\x01",
            "指一本触れさせないんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1253")

    #C0016
    ChrTalk(
        0x109,
        "#10101F母さん、気をつけてね。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ふふっ、ノエルたちの方こそ\x01",
            "気をつけるのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1253")

    Jump("loc_12EF")

    label("loc_1258")


    #C0018
    ChrTalk(
        0xFE,
        (
            "アゼル君も手伝いに来てくれてるし、\x01",
            "ここは大丈夫よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "もしあの化物が入ってきても、\x01",
            "ユゴット君やサニータちゃんには\x01",
            "指一本触れさせないんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EF")

    Jump("loc_27DA")

    label("loc_12F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1436")

    #C0020
    ChrTalk(
        0xFE,
        (
            "ディーターさん……\x01",
            "彼も今まで、納得できて\x01",
            "いなかったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "このクロスベルで起こってきた、\x01",
            "無理にでも納得していくしかない\x01",
            "数々の理不尽な出来事に……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "…………………………………\x01",
            "……うちの人も………………\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00005Fえ…………？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……ふふ、ごめんなさい。\x01",
            "何でもないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1512")

    label("loc_1436")


    #C0025
    ChrTalk(
        0xFE,
        (
            "……それにしても国防軍って、\x01",
            "警備隊だった頃より\x01",
            "どうにも近寄りがたい雰囲気ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "あの白い制服が、なんだか\x01",
            "キッチリしすぎてるっていうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "私はお父さんの生きていた頃の、\x01",
            "警備隊の制服が好きだったんだけどねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1512")

    Jump("loc_27DA")

    label("loc_1517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1719")

    #C0028
    ChrTalk(
        0xFE,
        (
            "ええと……\x01",
            "フランの着替えは\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "そうだわ、ちょっとした\x01",
            "果物とかを持ってこうかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10100F母さん……\x01",
            "帰ってきてたんだ。\x02\x03",

            "確か午前はウルスラ病院に\x01",
            "行ってくるって言ってたよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "ええ、ついさっき\x01",
            "お見舞いから戻ったところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "……ふう、それにしても\x01",
            "フランの意識が戻ってよかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "庇#2Rかば#ってくださった\x01",
            "二課の警部さんには\x01",
            "本当に感謝しないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10103Fそうだね……\x01",
            "そちらにも改めて\x01",
            "お見舞いしてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "うん、よろしく頼んだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1793")

    label("loc_1719")


    #C0036
    ChrTalk(
        0xFE,
        (
            "あなたたち、病院に行くみたいね？\x01",
            "私もあとでまた行くつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "フランに着替えやらなにやらを\x01",
            "届けに行かないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1793")

    Jump("loc_27DA")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")

    #C0038
    ChrTalk(
        0xFE,
        (
            "マインツの占拠だなんて……\x01",
            "通商会議に現れたテロリストといい、\x01",
            "大きな事件が続くわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "警備隊が解決にあたってると\x01",
            "いう話だったけど、\x01",
            "なんだか胸騒ぎがするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "あなたたち、向かうなら\x01",
            "充分に注意したほうがいいわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1900")

    label("loc_1896")


    #C0041
    ChrTalk(
        0xFE,
        (
            "例の占拠事件、\x01",
            "なんだか胸騒ぎがするわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "あなたたち、向かうなら\x01",
            "充分に注意したほうがいいわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1900")

    Jump("loc_27DA")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BA")

    #C0043
    ChrTalk(
        0xFE,
        "今日も雨、か……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "買い物に行くのも億劫だし、\x01",
            "今日の夕飯は適当に残り物で\x01",
            "済ませちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x109,
        (
            "#10106F（割とズボラなのよね、\x01",
            "  母さん……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A1A")

    label("loc_19BA")


    #C0046
    ChrTalk(
        0xFE,
        (
            "今日の夕飯は適当な残り物で\x01",
            "済ませちゃいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "雨の中でかけるなんて\x01",
            "面倒だものね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1A")

    Jump("loc_27DA")

    label("loc_1A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AC2")

    #C0048
    ChrTalk(
        0xFE,
        (
            "ユゴット君に日曜学校の宿題を\x01",
            "教えてあげているところなのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "うーん、問題を見ていると\x01",
            "ノエルとフランに勉強を教えてた\x01",
            "思い出が蘇るわねえ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4D")

    #C0050
    ChrTalk(
        0xFE,
        (
            "お向かいのユゴット君、\x01",
            "最近一人でお留守番が\x01",
            "できるようになったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "ふふ、なんだか微笑ましいわね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1BC0")

    label("loc_1B4D")


    #C0052
    ChrTalk(
        0xFE,
        (
            "サリナちゃんには\x01",
            "定期的に様子を見るように\x01",
            "頼まれているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "あとでおやつでも\x01",
            "持っていってあげようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC0")

    Jump("loc_27DA")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9C")

    #C0054
    ChrTalk(
        0xFE,
        (
            "今日は向かいのサリナちゃんが\x01",
            "仕事でおそくなるらしくて、\x01",
            "ユゴットくんの世話を頼まれてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "サリナちゃんも帰ってきたら\x01",
            "おなかがすくでしょうし……\x01",
            "夕飯を沢山用意してあげなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D12")

    label("loc_1C9C")


    #C0056
    ChrTalk(
        0xFE,
        "私、子供の世話って大好きなのよね。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "ふふ、せっかくだから\x01",
            "腕によりをかけて美味しいものを\x01",
            "つくっちゃおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D12")

    Jump("loc_27DA")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD0")

    #C0058
    ChrTalk(
        0xFE,
        (
            "今日はフランも\x01",
            "オペレーターの仕事が\x01",
            "忙しくなるって言ってたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "なんてったって、\x01",
            "通商会議も本番ですものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "何事もなく終われば\x01",
            "いいのだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E33")

    label("loc_1DD0")


    #C0061
    ChrTalk(
        0xFE,
        (
            "あ……\x01",
            "フランったら、また\x01",
            "お弁当を忘れて……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "仕方ない、あとで\x01",
            "届けてあげるとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E33")

    Jump("loc_27DA")

    label("loc_1E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E46")
    Jump("loc_27DA")

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207D")

    #C0063
    ChrTalk(
        0xFE,
        (
            "えっと、百貨店で買った\x01",
            "高級なクッキーが\x01",
            "どこかにあったはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#10105Fか、母さん？\x01",
            "もしかして……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 0)

    #C0065
    ChrTalk(
        0xFE,
        (
            "ええ、フランに\x01",
            "差し入れでもしようかと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "警察も、通商会議が近づいて\x01",
            "随分忙しくしてるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x109,
        (
            "#10106Fあ、あのね、母さん。\x01",
            "仕事中なんだから\x01",
            "そういうのはあまり……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "あら、フランは喜んでくれるし\x01",
            "別にいいじゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "あ、そうだ、せっかくだから\x01",
            "今度特務支援課にも……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#10106F来なくていいから！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#00009F（このマイペースぶり……\x01",
            "  フランはクラリスさんに\x01",
            "  似たのかもな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_210E")

    label("loc_207D")


    #C0072
    ChrTalk(
        0xFE,
        (
            "警察も、通商会議が近づいて\x01",
            "忙しくしてるんでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "フランに差し入れを\x01",
            "持っていってあげないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        "#10106F（いいのかなあ……）\x02",
    )

    CloseMessageWindow()

    label("loc_210E")

    Jump("loc_27DA")

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_239D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DA")

    #C0075
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "あなたたち、導力車を\x01",
            "手に入れたんですってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "ノエルがうるさくなかったかしら？\x01",
            "この子、車のことになると……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x109,
        (
            "#10112Fそ、そんなことないってば。\x01",
            "……ねえ、皆さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00012Fえっと、ないことも\x01",
            "ないような気がするんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00104F夢中になって性能の話とかを\x01",
            "色々と教えてくれたわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x109,
        "#10106Fええ！　そ、そうですか！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、意外と\x01",
            "自覚してなかったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        "やれやれ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2398")

    label("loc_22DA")


    #C0083
    ChrTalk(
        0xFE,
        (
            "この子、導力車のことになると\x01",
            "本当にうるさいんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "警備隊で初めて装甲車に乗れたときも、\x01",
            "速度がどうだの耐久力がこうだの……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x109,
        (
            "#10106Fわ、分かったから\x01",
            "もう止めてよ母さん～っ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2398")

    Jump("loc_27DA")

    label("loc_239D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_27DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x109, 0)

    #C0086
    ChrTalk(
        0xFE,
        (
            "ノエル、\x01",
            "噂の特務支援課に\x01",
            "入ったそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x109,
        (
            "#10100Fええっと、厳密には\x01",
            "“出向”の名目だから\x01",
            "ちょっと違うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "もう、あんたって\x01",
            "結構細かい性格してるわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "あんたと一緒に仕事ができるって、\x01",
            "フランが小躍りしながら喜んでたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#00102Fふふ、光景が目に浮かびますね。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x109,
        (
            "#10106Fはあ、フランったら……\x01",
            "いつまでたっても\x01",
            "子供みたいなんだから。\x02\x03",

            "#10109Fま、まあ、もちろん\x01",
            "あたしも嬉しいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、君たち姉妹って\x01",
            "ほんと、仲いいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "親としてはある意味、\x01",
            "心配なところなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "２人とも器量がいいのに、\x01",
            "これじゃ嫁の貰い手に\x01",
            "困りそうだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        "#10106Fか、母さんってば……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00000F（はは……\x01",
            "  姉妹仲だけじゃなくて\x01",
            "  親子仲もいいんだよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 3)
    Jump("loc_27DA")

    label("loc_2692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2786")

    #C0097
    ChrTalk(
        0xFE,
        (
            "ノエル、たまにはうちに\x01",
            "顔を出しなさいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x109,
        (
            "#10105Fえ、でもここ最近は\x01",
            "よく顔を出してたじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "せっかく職場が近くなったんだから、\x01",
            "もっと来なさいって言ってるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x109,
        (
            "#10106Fもう、そんなに\x01",
            "甘えられないってば……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27DA")

    label("loc_2786")


    #C0101
    ChrTalk(
        0xFE,
        (
            "ノエル、たまには\x01",
            "顔を出しなさいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "母さん、いつでも\x01",
            "ここで待ってるから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DA")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE9 end

    def Function_9_27DE(): pass

    label("Function_9_27DE")

    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    #C0103
    ChrTalk(
        0xB,
        "あら……ノエルじゃない！\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#10102F母さん……良かった。\x01",
            "元気にしてるみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "あんたこそ、しばらく\x01",
            "顔を見せないから心配してたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xB,
        (
            "しばらくは国防軍で仕事してるから\x01",
            "帰れないんじゃなかったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x109,
        "#10108Fえ、えっとそれは……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xB,
        (
            "……あはは、まあいいわ。\x01",
            "あんたにも色々あったんでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "フランも退院したって聞いたけど、\x01",
            "あなたたちと行動してるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#00000Fええ、俺たちに同行して\x01",
            "とても頑張ってくれてます。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "ふふ、だったら私には\x01",
            "何も口を出す権利はないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xB,
        (
            "ノエル、あとは\x01",
            "あんたたちの気が済むように、\x01",
            "好きな道を進んでいきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "女神様の元にいる\x01",
            "お父さんに恥ずかしくないように、\x01",
            "自分に後悔しない道をね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        "#10101F……うん、分かった！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2AC2")
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_2AC9")

    label("loc_2AC2")

    OP_93(0xB, 0x10E, 0x0)

    label("loc_2AC9")

    SetScenarioFlags(0x1BA, 3)
    Return()

    # Function_9_27DE end

    def Function_10_2ACD(): pass

    label("Function_10_2ACD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAB")

    #C0115
    ChrTalk(
        0xFE,
        (
            "アゼルは今日は\x01",
            "旧市街に行っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "以前の私なら、\x01",
            "こんな時に家族を放っておいてと\x01",
            "怒るところかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "今は友達やみんなのために、\x01",
            "ただ一所懸命働いてほしいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C38")

    label("loc_2BAB")


    #C0118
    ChrTalk(
        0xFE,
        (
            "アゼルも一人前ですし、\x01",
            "私からとやかく言うのは\x01",
            "もうやめることにしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "今は友達やみんなのために、\x01",
            "ただ一所懸命働いてほしいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C38")

    Jump("loc_3BF2")

    label("loc_2C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D36")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0120
    ChrTalk(
        0xFE,
        (
            "アゼルが大急ぎで旧市街から\x01",
            "帰ってきてくれたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "おかげで怖がって泣いていた\x01",
            "ユゴットも落ち着いてくれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        "な、泣いてなんかないもん！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #C0123
    ChrTalk(
        0xFE,
        (
            "ふふ、そうね。\x01",
            "ユゴットは強い子だもんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D71")

    label("loc_2D36")


    #C0124
    ChrTalk(
        0xFE,
        (
            "……とにかく、アゼルが\x01",
            "帰ってきてくれて安心しました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D71")

    Jump("loc_3BF2")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2EEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E64")

    #C0125
    ChrTalk(
        0xFE,
        (
            "ディーター大統領の言っていた\x01",
            "『不可解な事故』……\x01",
            "私も話には聞いていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "でもそれが、２大国の暗躍に\x01",
            "よるものだったなんて……\x01",
            "正直、恐ろしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "やっぱり、独立は\x01",
            "必要なことなんだと思います。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EE7")

    label("loc_2E64")


    #C0128
    ChrTalk(
        0xFE,
        (
            "もし、ユゴットやアゼルが\x01",
            "『不可解な事故』に\x01",
            "巻き込まれていたらと思うと……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "やっぱり、独立は\x01",
            "必要なことなんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE7")

    Jump("loc_3BF2")

    label("loc_2EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC4")

    #C0130
    ChrTalk(
        0xFE,
        (
            "アゼル、チームの仲間と一緒に\x01",
            "旧市街の復興を\x01",
            "手伝っているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "他人の為に働こう、なんて\x01",
            "昔のあの子じゃ考えられない\x01",
            "行動なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "ふふ、姉として\x01",
            "なんだか誇らしいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3040")

    label("loc_2FC4")


    #C0133
    ChrTalk(
        0xFE,
        (
            "前はとにかくツンケンして、\x01",
            "やんちゃもする子だったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "弟は本当に変わりました。\x01",
            "姉としてなんだか誇らしいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3040")

    Jump("loc_3BF2")

    label("loc_3045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_30B6")

    #C0135
    ChrTalk(
        0xFE,
        "怖いですよね、占領事件だなんて……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "今日は仕事なんですけど、\x01",
            "念のため休みをとろうかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BF2")

    label("loc_30B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3125")

    #C0137
    ChrTalk(
        0xFE,
        (
            "昨日、脱線事故があったあたりで\x01",
            "大きな怪物が目撃されたそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "なんだか怖いです……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BF2")

    label("loc_3125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3133")
    Jump("loc_3BF2")

    label("loc_3133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3144")
    Call(0, 11)
    Jump("loc_3BF2")

    label("loc_3144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FC")

    #C0139
    ChrTalk(
        0xFE,
        (
            "今日は、ユゴットは\x01",
            "日曜学校に行ってるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "アゼルは日曜学校を\x01",
            "サボりがちな子でしたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "せめてユゴットには\x01",
            "しっかり勉強して欲しいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_323C")

    label("loc_31FC")


    #C0142
    ChrTalk(
        0xFE,
        (
            "あっ、いけない……\x01",
            "そろそろ仕事にいかないと\x01",
            "いけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    Jump("loc_3BF2")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346D")

    #C0143
    ChrTalk(
        0xFE,
        (
            "昨日、アゼルの働いているバーに\x01",
            "変なお客さんが来たそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "金髪に白いコートで、\x01",
            "リュートを携えていた方だった\x01",
            "そうなんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "頼んでもないのに演奏を始めたり、\x01",
            "来ていた女性客を口説いたりと\x01",
            "やりたい放題だったとか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_3400")
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
        "#00006F（皇子殿下の話だな、多分。）\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        "#00306F（多分っつーか、確実だろ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_3400")


    #C0148
    ChrTalk(
        0x101,
        (
            "#00005F（金髪にリュートって……\x01",
            "  最近どこかで見たような……？）\x02\x03",

            "#00004F（……ま、まさかな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3465")

    SetScenarioFlags(0x0, 1)
    Jump("loc_34F9")

    label("loc_346D")


    #C0149
    ChrTalk(
        0xFE,
        (
            "普段、家ではお店でのことを\x01",
            "あまり報告しないアゼルが\x01",
            "言ったくらいですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "そのお客さん、\x01",
            "よっぽどヘンな人\x01",
            "だったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F9")

    Jump("loc_3BF2")

    label("loc_34FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CE")

    #C0151
    ChrTalk(
        0xFE,
        (
            "今日は、向かいのクラリスさんは\x01",
            "お出かけしてるみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "クラリスさんには\x01",
            "いつもユゴットを見てもらって\x01",
            "お世話になっていますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        "今度、お礼をしないといけませんね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3644")

    label("loc_35CE")


    #C0154
    ChrTalk(
        0xFE,
        (
            "クラリスさんには\x01",
            "いつもユゴットを見てもらって\x01",
            "お世話になっていますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "今度、お礼をしないといけませんね。\x02",
    )

    CloseMessageWindow()

    label("loc_3644")

    Jump("loc_3BF2")

    label("loc_3649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370B")

    #C0156
    ChrTalk(
        0xFE,
        (
            "弟の働いているバーに\x01",
            "内緒で訪ねてみたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "最初は恥ずかしがってたけど\x01",
            "ちゃんともてなしてくれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "プロ意識をもって働いてるのは\x01",
            "いいことですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3763")

    label("loc_370B")


    #C0159
    ChrTalk(
        0xFE,
        "こくこく……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "アゼルの作った\x01",
            "ノンアルコールカクテル……\x01",
            "なかなか美味しいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3763")

    Jump("loc_3BF2")

    label("loc_3768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EE")

    #C0161
    ChrTalk(
        0xFE,
        (
            "今日はお仕事が休みなので、\x01",
            "弟と過ごすんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "でも、うーん……\x01",
            "流石に遊撃士ごっこは\x01",
            "ちょっと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3852")

    label("loc_37EE")


    #C0163
    ChrTalk(
        0xFE,
        (
            "遊撃士ごっこなんて\x01",
            "どうしたらいいのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "こういうときに限って\x01",
            "アゼルはいないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3852")

    Jump("loc_3BF2")

    label("loc_3857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC2")
    TurnDirection(0xFE, 0x105, 0)

    #C0165
    ChrTalk(
        0xFE,
        "あら、あなたは……？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x105,
        (
            "#10300Fおや、確か……\x01",
            "アゼルの姉上だったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00005Fえっと……\x01",
            "知り合いなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、彼女の弟のアゼルは\x01",
            "テスタメンツのメンバーでね。\x02\x03",

            "#10300F確か大分前に、彼を辞めさせに\x01",
            "《トリニティ》まで\x01",
            "乗り込んできてなかったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        "#00105Fの、乗り込んだって……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "えっと、その節は\x01",
            "ご迷惑をおかけしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "あのときはどうしても、\x01",
            "アゼルをチームから\x01",
            "抜けさせたくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x105,
        (
            "#10304Fあの剣幕には\x01",
            "テスタメンツの皆も\x01",
            "さぞ驚いてたみたいだ。\x02\x03",

            "#10309Fフフ、あれこそが姉弟愛の\x01",
            "なせるワザってヤツだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        "#00006F（な、何で他人事なんだよ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 4)
    Jump("loc_3BF2")

    label("loc_3AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7D")

    #C0174
    ChrTalk(
        0xFE,
        (
            "弟のアゼルは《トリニティ》で\x01",
            "アルバイトをしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "治安の悪い場所ですから\x01",
            "最初は心配したんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "ちゃんと続いているので\x01",
            "少し安心しています。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BF2")

    label("loc_3B7D")


    #C0177
    ChrTalk(
        0xFE,
        (
            "ふう、アゼルったら\x01",
            "チームのことはほとんど\x01",
            "話してくれないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "あまり心配させないで\x01",
            "ほしいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF2")

    TalkEnd(0xFE)
    Return()

    # Function_10_2ACD end

    def Function_11_3BF6(): pass

    label("Function_11_3BF6")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C86")

    #C0179
    ChrTalk(
        0x9,
        (
            "それじゃあお姉ちゃん、\x01",
            "お仕事に行ってくるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "ユゴット、\x01",
            "ちゃんと戸締りお願いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xA,
        "うん、まかせて～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CEE")

    label("loc_3C86")


    #C0182
    ChrTalk(
        0x9,
        (
            "そうそう、\x01",
            "お姉ちゃんが見てなくても、\x01",
            "ちゃんと宿題しないとだめよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        "もー、分かってるってば～。\x02",
    )

    CloseMessageWindow()

    label("loc_3CEE")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_3BF6 end

    def Function_12_3CF7(): pass

    label("Function_12_3CF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFC")

    #C0184
    ChrTalk(
        0xFE,
        (
            "外にでてきた青白い木をみて\x01",
            "僕はすっごく怖かったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんが\x01",
            "大丈夫だ、なんとかしてやるって\x01",
            "励ましてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "いくらお兄ちゃんでもそこまでは\x01",
            "できないとは思うけど……\x01",
            "えへへ、おかげで元気がでてきたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E87")

    label("loc_3DFC")


    #C0187
    ChrTalk(
        0xFE,
        (
            "青白い木をみて怖がる僕を\x01",
            "お兄ちゃんが励ましてくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "えへへ、やっぱり\x01",
            "お兄ちゃんはかっこいいや。\x01",
            "おかげで元気がでてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E87")

    Jump("loc_43FE")

    label("loc_3E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3ECD")

    #C0189
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんがいてくれたら\x01",
            "きっと大丈夫だよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_3ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F5B")

    #C0190
    ChrTalk(
        0xFE,
        (
            "クロスベルがドクリツするって……\x01",
            "結局、どういうことなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "僕にはよく分かんないよ。\x01",
            "マーブル先生なら分かるのかなあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_3F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FC9")

    #C0192
    ChrTalk(
        0xFE,
        (
            "僕も、何か\x01",
            "手伝えることはないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "旧市街にいる兄ちゃんのところに\x01",
            "行ってみようかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_3FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4031")

    #C0194
    ChrTalk(
        0xFE,
        (
            "なんだか大変な事に\x01",
            "なってるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "アゼル兄ちゃん、\x01",
            "帰ってこないかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_4031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40A4")

    #C0196
    ChrTalk(
        0xFE,
        (
            "昨日、列車が\x01",
            "転んじゃったんだってね？\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "怖いよね……\x01",
            "なんでそんなことに\x01",
            "なっちゃったのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_40A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4163")
    OP_4B(0xB, 0xFF)

    #C0198
    ChrTalk(
        0xFE,
        "あ～あ、宿題なんていやだなぁ。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        "がんばって、ユゴット君。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xB,
        (
            "おばさんがご褒美に\x01",
            "おやつを用意してるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "ほんと～！？\x01",
            "じゃあ、がんばるよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_41AC")

    label("loc_4163")


    #C0202
    ChrTalk(
        0xFE,
        "えっと、１４×２３は……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "うーん、２ケタの掛け算は\x01",
            "難しいなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41AC")

    Jump("loc_43FE")

    label("loc_41B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41C2")
    Call(0, 11)
    Jump("loc_43FE")

    label("loc_41C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41D0")
    Jump("loc_43FE")

    label("loc_41D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_425C")

    #C0204
    ChrTalk(
        0xFE,
        (
            "最近は、３日に１回くらいは\x01",
            "お兄ちゃんが帰ってくるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "お店であまったおつまみとかを\x01",
            "持って帰ってきてくれるんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_425C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42E4")

    #C0206
    ChrTalk(
        0xFE,
        (
            "クラリスおばちゃん、\x01",
            "今日は大聖堂に行くって言ってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "そういえば、先月も同じ日に\x01",
            "行ってたような気がするなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_42E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_42F2")
    Jump("loc_43FE")

    label("loc_42F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4376")

    #C0208
    ChrTalk(
        0xFE,
        (
            "お姉ちゃん、遊撃士ごっこの\x01",
            "やりかた分かんないんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "もー、しょうがないなあ。\x01",
            "おままごとでもいいかなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_4376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_43FE")

    #C0210
    ChrTalk(
        0xFE,
        (
            "アゼル兄ちゃん、\x01",
            "旧市街でバーテンダーを\x01",
            "やってるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "えへへ、かっこいいでしょ。\x01",
            "ぼくの自慢のお兄ちゃんなんだ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43FE")

    TalkEnd(0xFE)
    Return()

    # Function_12_3CF7 end

    def Function_13_4402(): pass

    label("Function_13_4402")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4609")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 500)

    #C0212
    ChrTalk(
        0xFE,
        (
            "あれ……ワ、ワジ！？\x01",
            "クロスベルに戻ってたのか！\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x105,
        "#10400Fフフ、久しぶりアゼル。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "その格好は一体……それに\x01",
            "アッバスはどこにいるんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x105,
        (
            "#10404F聞きたいことは\x01",
            "色々あるだろうけど、\x01",
            "悪いが今は時間がないんだ。\x02\x03",

            "#10400F後でゆっくり説明するから、\x01",
            "今はお姉さんと弟くんを\x01",
            "しっかりと守ってやるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "あ、ああ……\x01",
            "確かに今はそんな場合じゃ\x01",
            "ないかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        "でもワジ、無事でよかったよ。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x105,
        (
            "#10402Fフフ、君もね。\x01",
            "……それじゃ、また後で。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 4)
    Jump("loc_4747")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C8")

    #C0219
    ChrTalk(
        0xFE,
        (
            "外をうろついてる化物は\x01",
            "別段中に入ってくる様子はないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "……だけど、油断は禁物だ。\x01",
            "しっかり警戒しとかないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "姉さんとユゴットは\x01",
            "俺が絶対に守ってやる……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4747")

    label("loc_46C8")


    #C0222
    ChrTalk(
        0xFE,
        (
            "外をうろついてる化物が\x01",
            "中に入ってくる様子はないけど……\x01",
            "油断は禁物だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "姉さんとユゴットは\x01",
            "俺が絶対に守ってやる……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4747")

    TalkEnd(0xFE)
    Return()

    # Function_13_4402 end

    def Function_14_474B(): pass

    label("Function_14_474B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_475C")
    Jump("loc_550E")

    label("loc_475C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_476A")
    Jump("loc_550E")

    label("loc_476A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_499D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4860")

    #C0224
    ChrTalk(
        0xFE,
        (
            "今日、クロスベルを\x01",
            "離れることになってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "急いで荷造りをしたんだが……\x01",
            "この本はかさばりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        "よかったら君たちにあげよう。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F8, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 2)
    Jump("loc_4998")

    label("loc_4860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4903")

    #C0228
    ChrTalk(
        0xFE,
        (
            "帝国政府の方から\x01",
            "退去命令が下ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "今日鉄道でクロスベルを\x01",
            "離れるつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "駅は相当混雑しているようだし、\x01",
            "私も急がないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4998")

    label("loc_4903")


    #C0231
    ChrTalk(
        0xFE,
        (
            "こんな形でクロスベルを\x01",
            "離れるとは思いも寄らなかったが……\x01",
            "私にとっては家族が第一だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "混雑しているようだし、\x01",
            "一刻も早く列車に乗らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4998")

    Jump("loc_550E")

    label("loc_499D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A64")

    #C0233
    ChrTalk(
        0xFE,
        (
            "帝国にいる家族が\x01",
            "心配して手紙をくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "あんな事件があったんだ、\x01",
            "私も早いところ\x01",
            "故郷に戻りたいところだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "これは一度本社に\x01",
            "相談してみる必要があるかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4ABE")

    label("loc_4A64")


    #C0236
    ChrTalk(
        0xFE,
        (
            "家族には心配を\x01",
            "かけてしまったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "なんとか帝国に戻る\x01",
            "段取りをつけないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ABE")

    Jump("loc_550E")

    label("loc_4AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4B54")

    #C0238
    ChrTalk(
        0xFE,
        (
            "武装集団がマインツに\x01",
            "立てこもるだなんて……\x01",
            "前代未聞だよ、これは。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "とにかく、早く解決することを\x01",
            "女神に願うしかないな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550E")

    label("loc_4B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF0")

    #C0240
    ChrTalk(
        0xFE,
        (
            "遊びに来ていた妻と娘が、\x01",
            "今日帝国に帰ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "昨日の脱線事故は\x01",
            "本当に肝が冷えたけど……\x01",
            "すぐに復旧してよかったなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C67")

    label("loc_4BF0")


    #C0242
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "久しぶりに妻と娘と一緒に\x01",
            "過ごす事ができたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "はは、なんだか逆に\x01",
            "里心がついてしまったがね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C67")

    Jump("loc_550E")

    label("loc_4C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C7A")
    Jump("loc_550E")

    label("loc_4C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D03")

    #C0244
    ChrTalk(
        0xFE,
        (
            "そうか……\x01",
            "もう帰ってしまうんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "まだしばらく寂しい思いを\x01",
            "させてしまうけど……\x01",
            "子供のことはよろしく頼んだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550E")

    label("loc_4D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA7")

    #C0246
    ChrTalk(
        0xFE,
        (
            "妻と娘が帝国の実家から\x01",
            "遊びに来てくれたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "連絡もなしに来るから\x01",
            "びっくりしちゃったけど……\x01",
            "う、うれしいなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x10)
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_4E29")

    label("loc_4DA7")


    #C0248
    ChrTalk(
        0xFE,
        (
            "へえ、じゃあ昨日の列車で……\x01",
            "連絡くらいくれたらよかったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "なんの家族サービスもできないんじゃ\x01",
            "申し訳ないじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E29")

    Jump("loc_550E")

    label("loc_4E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EA6")

    #C0250
    ChrTalk(
        0xFE,
        (
            "通商会議の展開によっては\x01",
            "株価にも影響がでるだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "証券マンの私としては\x01",
            "動向は見逃せないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550E")

    label("loc_4EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F50")

    #C0252
    ChrTalk(
        0xFE,
        (
            "昨日辺りから、\x01",
            "向かいのボンドさん一家の\x01",
            "飼い猫がいなくなったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "私も協力して探したけど、\x01",
            "結局見つからなくてね……\x01",
            "どうしたものか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_510F")

    label("loc_4F50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500A")

    #C0254
    ChrTalk(
        0xFE,
        (
            "おや、ボンドさん一家の猫を\x01",
            "探しにいくのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xFE,
        (
            "娘さんが昨日から泣き通しでね。\x01",
            "どうにもかわいそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "なんとか見つけ出して\x01",
            "やってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_508B")

    label("loc_500A")


    #C0257
    ChrTalk(
        0xFE,
        (
            "猫がいなくなったことで、\x01",
            "娘さんが昨日から泣き通しでね。\x01",
            "どうにもかわいそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "なんとか見つけ出して\x01",
            "やってくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_508B")

    Jump("loc_510F")

    label("loc_5090")


    #C0259
    ChrTalk(
        0xFE,
        (
            "お向かいさんの娘さんの\x01",
            "うれしそうな声が聞こえてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "どうやらネコは\x01",
            "無事にみつかったようだね。\x01",
            "よかったよかった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_510F")

    Jump("loc_550E")

    label("loc_5114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5278")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F4")

    #C0261
    ChrTalk(
        0xFE,
        (
            "お向かいのボンドさん一家は、\x01",
            "もともと住宅街に\x01",
            "住んでいたそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xFE,
        (
            "だが色々と事情があって\x01",
            "こちらに越してきたそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "だというのに、\x01",
            "あの家族は暖かくて明るい。\x01",
            "見習いたいくらいだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5273")

    label("loc_51F4")


    #C0264
    ChrTalk(
        0xFE,
        (
            "お向かいさんは\x01",
            "住宅街の一等地から\x01",
            "こちらに越してきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "色々と事情があるようだが……\x01",
            "彼らの明るさは見習いたいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5273")

    Jump("loc_550E")

    label("loc_5278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529D")
    Call(0, 15)
    Jump("loc_5355")

    label("loc_529D")

    OP_4B(0xC, 0xFF)

    #C0266
    ChrTalk(
        0xC,
        (
            "色々とお気遣い\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "ご迷惑をかけるでしょうが、\x01",
            "何卒よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "いやいや、こちらこそ。\x01",
            "困った事があったら\x01",
            "なんでも言ってくださいよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_5355")

    Jump("loc_53CE")

    label("loc_535A")


    #C0269
    ChrTalk(
        0xFE,
        (
            "何でも、ボンドさんは\x01",
            "私と同じ証券マンらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "ふふ、これはいい話し相手に\x01",
            "なってくれるかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53CE")

    Jump("loc_550E")

    label("loc_53D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_550E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54AC")

    #C0271
    ChrTalk(
        0xFE,
        (
            "向かいに遊撃士の子たちが\x01",
            "住んでいたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "数ヶ月前に故郷に帰ってしまって、\x01",
            "すっかり寂しくなってしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "早いところ、\x01",
            "だれか新しい人たちが\x01",
            "引っ越してこないだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_550E")

    label("loc_54AC")


    #C0274
    ChrTalk(
        0xFE,
        (
            "やはり単身赴任だと、\x01",
            "どうしても寂しいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "向かいにだれか\x01",
            "引っ越してこないかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550E")

    TalkEnd(0xFE)
    Return()

    # Function_14_474B end

    def Function_15_5512(): pass

    label("Function_15_5512")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0276
    ChrTalk(
        0xC,
        "と、いうわけでして……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        (
            "これからご迷惑をかけることも\x01",
            "あるかと思いますが、\x01",
            "どうか宜しくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xD,
        "よろしくお願いいたしますわ。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xE,
        "ほら、マリーも挨拶するのよ。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xF,
        "にゃ～ん。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "ふふ、皆さん\x01",
            "仲がよさそうで結構ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "何か困ったことがあれば、\x01",
            "いつでも頼ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xC,
        "ええ、ありがとうございます。\x02",
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

    # Function_15_5512 end

    def Function_16_5695(): pass

    label("Function_16_5695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56BE")
    Call(0, 22)
    Return()

    label("loc_56BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F2")
    Call(0, 23)
    Return()

    label("loc_56F2")

    Call(0, 25)
    Return()

    label("loc_56F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57EC")

    #C0284
    ChrTalk(
        0xFE,
        (
            "ＩＢＣに入っていた会社が、\x01",
            "小さな貸物件を事務所に\x01",
            "再開されることになってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "しばらく仕事からはなれてたから\x01",
            "ちゃんと準備しておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "３人と１匹の家族を支えるためにも\x01",
            "頑張っていきたいところだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5881")

    label("loc_57EC")


    #C0287
    ChrTalk(
        0xFE,
        (
            "ＩＢＣに入っていた会社が、\x01",
            "小さな貸物件を事務所に\x01",
            "再開されることになってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "３人と１匹の家族を支えるためにも\x01",
            "頑張っていきたいところだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5881")

    Jump("loc_627E")

    label("loc_5886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5912")

    #C0289
    ChrTalk(
        0xFE,
        (
            "とにかく、戒厳令も出ていることだし\x01",
            "家の中にいたほうがいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "大丈夫、こんな状況が\x01",
            "そうそう続くわけがないさ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_627E")

    label("loc_5912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E8")

    #C0291
    ChrTalk(
        0xFE,
        (
            "あの宣言は、帝国と共和国を\x01",
            "強く刺激してしまっただろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "もしかしたら、クロスベルが\x01",
            "危険な状態に陥るかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "だが、どんなことがあろうと\x01",
            "家族は絶対に守ってみせるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A60")

    label("loc_59E8")


    #C0294
    ChrTalk(
        0xFE,
        (
            "とにかく……\x01",
            "今は状況の把握と\x01",
            "冷静な判断が必要だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "家族は絶対に\x01",
            "私が守ってみせる……\x01",
            "どんなことがあろうとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A60")

    Jump("loc_627E")

    label("loc_5A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B69")

    #C0296
    ChrTalk(
        0xFE,
        (
            "私の勤める会社は、\x01",
            "ＩＢＣビルに入っていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "知っての通り、\x01",
            "今や瓦礫と化してしまってね。\x01",
            "事実上、休業状態なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "人的被害はなかったものの、\x01",
            "業務再開までには\x01",
            "時間がかかるというし……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        "ふう、困ったものだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BFA")

    label("loc_5B69")


    #C0300
    ChrTalk(
        0xFE,
        (
            "襲撃犯がＩＢＣビルを破壊したことで\x01",
            "私の会社も休業状態だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "……うちの周辺が襲撃に\x01",
            "あわなかっただけでも、\x01",
            "よしとすべきかもしれないな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BFA")

    Jump("loc_627E")

    label("loc_5BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C61")

    #C0302
    ChrTalk(
        0xFE,
        (
            "しかし、\x01",
            "大変なことになったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "武装集団とやらの狙いは\x01",
            "何なのだろうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_627E")

    label("loc_5C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CEA")

    #C0304
    ChrTalk(
        0xFE,
        (
            "久しぶりに、\x01",
            "一日休みがもらえてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "雨も降ってることだし、\x01",
            "今日は家族と一緒に\x01",
            "のんびり過ごすつもりだよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_5CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CF8")
    Jump("loc_627E")

    label("loc_5CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D06")
    Jump("loc_627E")

    label("loc_5D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D14")
    Jump("loc_627E")

    label("loc_5D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF0")

    #C0306
    ChrTalk(
        0xFE,
        (
            "マーシーさんとは\x01",
            "仕事の分野がよく似ていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "ときどきあちらの部屋で、\x01",
            "一緒に株の動きなどを\x01",
            "予想したりするんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "帝国の証券マンも\x01",
            "独特な目を持っている。\x01",
            "なかなか面白いものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E69")

    label("loc_5DF0")


    #C0309
    ChrTalk(
        0xFE,
        (
            "さて……そろそろ\x01",
            "会社に行かなければね。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xFE,
        (
            "通商会議も気になるが……\x01",
            "クロスベルタイムズの\x01",
            "報道を待つしかないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E69")

    Jump("loc_627E")

    label("loc_5E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5FAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F5F")

    #C0311
    ChrTalk(
        0xFE,
        (
            "いや、しかし君たちに\x01",
            "手伝ってもらえるなんて\x01",
            "本当に嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "とりあえず、しばらくしたら\x01",
            "私も中央広場に出向いて\x01",
            "捜索の続きを行うつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "何かあったら、\x01",
            "いつでも声を掛けて欲しい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA9")

    label("loc_5F5F")


    #C0314
    ChrTalk(
        0xFE,
        "君たち、今日は本当にありがとう。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "この恩は決して忘れないからね。\x02",
    )

    CloseMessageWindow()

    label("loc_5FA9")

    Jump("loc_627E")

    label("loc_5FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B3")

    #C0316
    ChrTalk(
        0xFE,
        (
            "以前は自宅で仕事ができる\x01",
            "設備があったんだが……\x01",
            "ここではそうもいかなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "他の社員と同じく、\x01",
            "ＩＢＣに入っている会社に\x01",
            "通勤することになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xFE,
        (
            "引っ越してからある程度\x01",
            "落ち着いてきたし、\x01",
            "仕事にも本腰を入れないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6122")

    label("loc_60B3")


    #C0319
    ChrTalk(
        0xFE,
        (
            "でも……\x01",
            "通勤も悪くないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xFE,
        (
            "疲れて帰ってきたときに\x01",
            "『お帰り』と言ってもらえるのは\x01",
            "なかなか幸せだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6122")

    Jump("loc_627E")

    label("loc_6127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_614C")
    Call(0, 15)
    Jump("loc_6204")

    label("loc_614C")

    OP_4B(0x8, 0xFF)

    #C0321
    ChrTalk(
        0xC,
        (
            "色々とお気遣い\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xC,
        (
            "ご迷惑をかけるでしょうが、\x01",
            "何卒よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x8,
        (
            "いやいや、こちらこそ。\x01",
            "困った事があったら\x01",
            "なんでも言ってくださいよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_6204")

    Jump("loc_6270")

    label("loc_6209")


    #C0324
    ChrTalk(
        0xFE,
        "本当に私はつくづく幸せ者だよ。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "これも全て家族のおかげ……\x01",
            "これからも目一杯大切にしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6270")

    Jump("loc_627E")

    label("loc_6275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_627E")

    label("loc_627E")

    TalkEnd(0xFE)
    Return()

    # Function_16_5695 end

    def Function_17_6282(): pass

    label("Function_17_6282")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62B0")
    Call(0, 22)
    Return()

    label("loc_62B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E4")
    Call(0, 23)
    Return()

    label("loc_62E4")

    Call(0, 25)
    Return()

    label("loc_62E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_638A")

    #C0326
    ChrTalk(
        0xFE,
        (
            "住宅街のソフィアさんや\x01",
            "シンディさんのお宅も\x01",
            "無事だったそうで安心しましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "今はとにかく、のんびりとした\x01",
            "日常を取り戻したいですわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_638A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6404")

    #C0328
    ChrTalk(
        0xFE,
        (
            "住宅街に住んでた頃の\x01",
            "ご近所さんも心配ですわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "ソフィアさん、シンディさん、\x01",
            "ご無事でしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_6404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_649D")

    #C0330
    ChrTalk(
        0xFE,
        (
            "多くは望みませんから、\x01",
            "今までどおりのクロスベル市では\x01",
            "いられないのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "私は家族が幸せであれば\x01",
            "それだけでいいんですもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_649D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654A")

    #C0332
    ChrTalk(
        0xFE,
        (
            "私……\x01",
            "見てしまったんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "旧市街で暴れる、\x01",
            "巨大な化け物……\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "ああ、恐ろしい……\x01",
            "クロスベルはいつから\x01",
            "こんな恐ろしいところに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_659D")

    label("loc_654A")


    #C0335
    ChrTalk(
        0xFE,
        (
            "またあの巨大な化け物が\x01",
            "現れたらと思うと……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        "うう、震えが止まりませんわ。\x02",
    )

    CloseMessageWindow()

    label("loc_659D")

    Jump("loc_6D4F")

    label("loc_65A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6608")

    #C0337
    ChrTalk(
        0xFE,
        (
            "私、血なまぐさい事は\x01",
            "本当に苦手ですの……\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "事件が無事に終われば\x01",
            "いいのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_6608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6690")

    #C0339
    ChrTalk(
        0xFE,
        (
            "しゃわわ……\x01",
            "植物に水をあげると、\x01",
            "心が癒されますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "雨の音も心地いいし……\x01",
            "和やかな休日ですわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66F5")

    label("loc_6690")


    #C0341
    ChrTalk(
        0xFE,
        (
            "しゃわわ……\x01",
            "もう少ししたら\x01",
            "ティータイムにしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "あっ、マリーにも\x01",
            "エサをあげないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_6D4F")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_678F")

    #C0343
    ChrTalk(
        0xFE,
        (
            "あとで御買い物にいかないと。\x01",
            "今日はマルテさんのところが\x01",
            "安かったかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "ふふ、市場の人たちも\x01",
            "もうみんな顔見知りですのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_678F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_68E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6872")

    #C0345
    ChrTalk(
        0xFE,
        (
            "今日は大事な会議があるらしく、\x01",
            "主人は朝早くに出かけましたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "こっちに引っ越してから、\x01",
            "仕事にも俄然やる気が\x01",
            "出たようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "主人は家族も大事にしますし……\x01",
            "ふふ、とてもいいことですわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_68DD")

    label("loc_6872")


    #C0348
    ChrTalk(
        0xFE,
        (
            "主人はこっちに引っ越してから、\x01",
            "仕事にも俄然やる気が出たようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        "ふふ、とてもいいことですわね。\x02",
    )

    CloseMessageWindow()

    label("loc_68DD")

    Jump("loc_6D4F")

    label("loc_68E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_68F0")
    Jump("loc_6D4F")

    label("loc_68F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69BD")

    #C0350
    ChrTalk(
        0xFE,
        (
            "お向かいの方は\x01",
            "よくお裾分けをしてくださったり、\x01",
            "とてもお優しい方ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xFE,
        (
            "でも、やっぱりどこか\x01",
            "寂しそうにしてらして……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "単身赴任というのも、\x01",
            "寂しいものでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A30")

    label("loc_69BD")


    #C0353
    ChrTalk(
        0xFE,
        (
            "単身赴任というのも\x01",
            "なかなか寂しいものでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xFE,
        (
            "うちは家族が\x01",
            "揃っているだけでも\x01",
            "充分幸せと言えますわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A30")

    Jump("loc_6D4F")

    label("loc_6A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ADB")

    #C0355
    ChrTalk(
        0xFE,
        (
            "皆さん、どうかマリーのことを\x01",
            "よろしくお願いいたししますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "あの子もきっと、この家に\x01",
            "帰りたがっているはずですの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B41")

    label("loc_6ADB")


    #C0357
    ChrTalk(
        0xFE,
        (
            "うふふ、サニータったら\x01",
            "あんなに強く抱きしめて。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "でも、マリーも\x01",
            "まんざらではなさそうですの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B41")

    Jump("loc_6D4F")

    label("loc_6B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE6")

    #C0359
    ChrTalk(
        0xFE,
        (
            "こっちのお部屋は\x01",
            "台所が多少狭いですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "趣味のガーデニングも\x01",
            "表の植木鉢でできそうですし、\x01",
            "なかなか気に入りましたのよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C55")

    label("loc_6BE6")


    #C0361
    ChrTalk(
        0xFE,
        (
            "サニータが慣れるのに\x01",
            "時間がかかるかと\x01",
            "思っていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "うふふ、その心配は\x01",
            "なかったようですわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C55")

    Jump("loc_6D4F")

    label("loc_6C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7F")
    Call(0, 15)
    Jump("loc_6CBF")

    label("loc_6C7F")


    #C0363
    ChrTalk(
        0xFE,
        (
            "うふふ、お隣さんが\x01",
            "お優しそうな方で\x01",
            "本当に良かったですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CBF")

    Jump("loc_6D41")

    label("loc_6CC4")


    #C0364
    ChrTalk(
        0xFE,
        (
            "これからも、家族みんなで\x01",
            "どんなことだって\x01",
            "乗り越えていきますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "うふふ、何だか新婚の頃の\x01",
            "気持ちを思い出しますの㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D41")

    Jump("loc_6D4F")

    label("loc_6D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6D4F")

    label("loc_6D4F")

    TalkEnd(0xFE)
    Return()

    # Function_17_6282 end

    def Function_18_6D53(): pass

    label("Function_18_6D53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D87")
    Call(0, 23)
    Return()

    label("loc_6D87")

    Call(0, 25)
    Return()

    label("loc_6D8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E35")

    #C0366
    ChrTalk(
        0xFE,
        (
            "お父様、お仕事に復帰できて\x01",
            "とっても嬉しそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xFE,
        (
            "ふふ、サニータもとっても嬉しいっ。\x01",
            "マリーもそう思うでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xF,
        "にゃ～ん？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6E9B")

    label("loc_6E35")


    #C0369
    ChrTalk(
        0xFE,
        (
            "お父様、お仕事に復帰できて\x01",
            "とっても嬉しそうですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "ふふ、サニータも\x01",
            "とっても嬉しいですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E9B")

    Jump("loc_7A2B")

    label("loc_6EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6F03")

    #C0371
    ChrTalk(
        0xFE,
        "マリー、心配しないでね。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "マリーはサニータが\x01",
            "絶対に守ってあげますからっ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_6F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6F71")

    #C0373
    ChrTalk(
        0xFE,
        (
            "お向かいさん、今日にも\x01",
            "クロスベルを出て行って\x01",
            "しまうそうですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        "寂しくなりますの……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_6F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7000")

    #C0375
    ChrTalk(
        0xFE,
        (
            "マリーといっしょに、\x01",
            "チャリティイベントへ\x01",
            "遊びに行こうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "噂じゃ、キレーな人たちが\x01",
            "いっぱい集まるらしいんですの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_7000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_70F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7094")

    #C0377
    ChrTalk(
        0xFE,
        (
            "今日はあまり遠くに\x01",
            "いかないようにって\x01",
            "言われてしまいましたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        (
            "仕方ないですから、\x01",
            "ここでマリーと遊んでますの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_70EC")

    label("loc_7094")


    #C0379
    ChrTalk(
        0xFE,
        (
            "もう……\x01",
            "今日は家族みんなで\x01",
            "百貨店にいくはずでしたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xFE,
        "つまらないですの……\x02",
    )

    CloseMessageWindow()

    label("loc_70EC")

    Jump("loc_7A2B")

    label("loc_70F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7182")

    #C0381
    ChrTalk(
        0xFE,
        (
            "マリー、きのう\x01",
            "お顔を洗っていましたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "猫が顔を洗うと雨が降るって、\x01",
            "本当のことでしたのね。\x01",
            "サニータ、びっくりですの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_7182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7239")

    #C0383
    ChrTalk(
        0xFE,
        (
            "マリーったら\x01",
            "なんだか顔をごしごし\x01",
            "洗っていますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xFE,
        (
            "猫が顔を洗うと雨が降るって、\x01",
            "露店のおばさまが\x01",
            "言ってましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        "……明日は、雨ですの？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7282")

    label("loc_7239")


    #C0386
    ChrTalk(
        0xFE,
        (
            "マリーが顔を洗っている\x01",
            "ということは……\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        "……明日は、雨ですの？\x02",
    )

    CloseMessageWindow()

    label("loc_7282")

    Jump("loc_7A2B")

    label("loc_7287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_73C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7348")
    OP_4B(0xF, 0xFF)

    #C0388
    ChrTalk(
        0xFE,
        (
            "マリー、今日はこれで\x01",
            "あそんであげますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        "ふさふさふさ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    #C0390
    ChrTalk(
        0xF,
        "ふにゃああ……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "わあ……\x01",
            "本当に効くんですのね、これ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_73BB")

    label("loc_7348")


    #C0392
    ChrTalk(
        0xFE,
        (
            "露店のお兄さんに\x01",
            "おしえてもらった、\x01",
            "『ねこじゃらし』ですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xFE,
        (
            "ふふ、マリーったら\x01",
            "気に入っちゃったみたい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BB")

    Jump("loc_7A2B")

    label("loc_73C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_73CE")
    Jump("loc_7A2B")

    label("loc_73CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_74E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7462")

    #C0394
    ChrTalk(
        0xFE,
        (
            "それがお父様のベッド。\x01",
            "こっちがお母様と\x01",
            "サニータのベッドですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "マリー、覚えたかしら？\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xF,
        "にゃおん……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_74DF")

    label("loc_7462")


    #C0397
    ChrTalk(
        0xFE,
        (
            "マリーがまたどこかに\x01",
            "行ってしまわないように、\x01",
            "家にある物を覚えさせてますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xFE,
        (
            "これを続ければ、\x01",
            "きっと大丈夫ですわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74DF")

    Jump("loc_7A2B")

    label("loc_74E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_774C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F4")
    OP_4B(0xD, 0xFF)

    #C0399
    ChrTalk(
        0xE,
        (
            "うう、マリー……\x01",
            "ごめんなさいですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xE,
        (
            "わたしが、わたしが\x01",
            "いけなかったから……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xD,
        "サニータ……\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        "#00100F（……早く見つけてあげないとね。）\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#00000F（そうだな……\x01",
            "  とにかく全力を尽くそう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_764C")

    label("loc_75F4")


    #C0404
    ChrTalk(
        0xFE,
        (
            "うう、マリー……\x01",
            "ごめんなさいですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "わたしが、わたしが\x01",
            "いけなかったから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_764C")

    Jump("loc_7747")

    label("loc_7651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76DE")
    OP_4B(0xF, 0xFF)

    #C0406
    ChrTalk(
        0xE,
        "本当によかった、マリー……\x02",
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xE,
        (
            "もう……バツとして今日は\x01",
            "ず～っと抱きしめるんですのっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xF,
        "にゃ、にゃ～ん？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    Jump("loc_7747")

    label("loc_76DE")

    OP_4B(0xF, 0xFF)

    #C0409
    ChrTalk(
        0xE,
        (
            "さあ、マリー。\x01",
            "覚悟を決めるんですのよっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xE,
        "ぎゅ～～～～～～っ。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xF,
        "にゃ、にゃあ～ん㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_7747")

    Jump("loc_7A2B")

    label("loc_774C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7827")

    #C0412
    ChrTalk(
        0xFE,
        (
            "新しいおうち、\x01",
            "サニータは結構\x01",
            "気に入ってるんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "でもマリーは、なんだか\x01",
            "こっちの部屋にきてから\x01",
            "様子が変なんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xFE,
        (
            "急なおひっこしで\x01",
            "びっくりしちゃったのかも\x01",
            "しれませんわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7894")

    label("loc_7827")


    #C0415
    ChrTalk(
        0xFE,
        (
            "マリー、なんだか\x01",
            "びくびくしてるみたい……\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "急なおひっこしで\x01",
            "びっくりしちゃったのかも\x01",
            "しれませんわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7894")

    Jump("loc_7A2B")

    label("loc_7899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78BE")
    Call(0, 15)
    Jump("loc_793D")

    label("loc_78BE")


    #C0417
    ChrTalk(
        0xFE,
        (
            "ふふん、こんな時のために\x01",
            "マリーにあいさつをおしえて\x01",
            "おいてよかったですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "おかげで、ハジを\x01",
            "かかなくて済みましたの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_793D")

    Jump("loc_7A1D")

    label("loc_7942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79AB")

    #C0419
    ChrTalk(
        0xFE,
        (
            "ふふ、マリーはほんとうに\x01",
            "おりこうさんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "ごほうびに、\x01",
            "スリスリしてあげますの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A1D")

    label("loc_79AB")


    #C0421
    ChrTalk(
        0xFE,
        (
            "お父さまとお母さまは前よりも\x01",
            "すごく仲がよくなったんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xFE,
        (
            "サニータは、それがとっても\x01",
            "嬉しいんですの。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A1D")

    Jump("loc_7A2B")

    label("loc_7A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7A2B")

    label("loc_7A2B")

    TalkEnd(0xFE)
    Return()

    # Function_18_6D53 end

    def Function_19_7A2F(): pass

    label("Function_19_7A2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7A56")

    #C0423
    ChrTalk(
        0xFE,
        "……にゃおん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7A72")

    #C0424
    ChrTalk(
        0xFE,
        "にゃお？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7A90")

    #C0425
    ChrTalk(
        0xFE,
        "にゃー……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7AAE")

    #C0426
    ChrTalk(
        0xFE,
        "みゃおん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7ACE")

    #C0427
    ChrTalk(
        0xFE,
        "ふにゃーん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AEE")

    #C0428
    ChrTalk(
        0xFE,
        "にゃーん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7B2F")
    TurnDirection(0xF, 0xE, 500)
    Sleep(500)

    #C0429
    ChrTalk(
        0xFE,
        (
            "にゃにゃ……\x01",
            "（ごしごし、ごしごし）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7B51")

    #C0430
    ChrTalk(
        0xFE,
        "ふみゃああ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7B5F")
    Jump("loc_7D0C")

    label("loc_7B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B7D")

    #C0431
    ChrTalk(
        0xFE,
        "にゃーご。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C13")
    OP_4B(0xE, 0xFF)

    #C0432
    ChrTalk(
        0xE,
        "本当によかった、マリー……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xE,
        (
            "もう……バツとして今日は\x01",
            "ず～っと抱きしめるんですのっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xF,
        "にゃ、にゃ～ん？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xE, 0xFF)
    Jump("loc_7C7C")

    label("loc_7C13")

    OP_4B(0xE, 0xFF)

    #C0435
    ChrTalk(
        0xE,
        (
            "さあ、マリー。\x01",
            "覚悟を決めるんですのよっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xE,
        "ぎゅ～～～～～～っ。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xF,
        "にゃ、にゃあ～ん㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)

    label("loc_7C7C")

    Jump("loc_7D0C")

    label("loc_7C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7C9F")

    #C0438
    ChrTalk(
        0xFE,
        "にゃー……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CC7")

    #C0439
    ChrTalk(
        0xFE,
        "にゃ～ん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CFE")

    label("loc_7CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CEA")

    #C0440
    ChrTalk(
        0xFE,
        "ごろにゃ～ん㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CFE")

    label("loc_7CEA")


    #C0441
    ChrTalk(
        0xFE,
        "にゃんにゃん♪\x02",
    )

    CloseMessageWindow()

    label("loc_7CFE")

    Jump("loc_7D0C")

    label("loc_7D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7D0C")

    label("loc_7D0C")

    TalkEnd(0xFE)
    Return()

    # Function_19_7A2F end

    def Function_20_7D10(): pass

    label("Function_20_7D10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7DAD")
    OP_4B(0x8, 0xFF)

    #C0442
    ChrTalk(
        0xFE,
        (
            "お仕事の邪魔になっても\x01",
            "いけませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        (
            "あなたも、仕事がおわるまで\x01",
            "体調を崩さないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x8,
        "うむ……気をつけるよ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_7E4B")

    label("loc_7DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7E4B")
    OP_4B(0x8, 0xFF)

    #C0445
    ChrTalk(
        0xFE,
        (
            "それにしてもあなた、\x01",
            "やせたんじゃなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "一人暮らしだからって、\x01",
            "適当なものばかり\x01",
            "食べていてはだめよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x8,
        "はは……手厳しいなあ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_7E4B")

    TalkEnd(0xFE)
    Return()

    # Function_20_7D10 end

    def Function_21_7E4F(): pass

    label("Function_21_7E4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7EB3")

    #C0448
    ChrTalk(
        0xFE,
        (
            "ちぇー、もう帰らなきゃ\x01",
            "いけないんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        "またパパに会いにきたいなあ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F2E")

    label("loc_7EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7F2E")

    #C0450
    ChrTalk(
        0xFE,
        (
            "あのねー、パパ。\x01",
            "こないだのパレードの写真、\x01",
            "とっても楽しそうだったよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        "ちょっとぴんぼけしてたけどね～。\x02",
    )

    CloseMessageWindow()

    label("loc_7F2E")

    TalkEnd(0xFE)
    Return()

    # Function_21_7E4F end

    def Function_22_7F32(): pass

    label("Function_22_7F32")

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
        "あら、お客さんですわね。\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        "おや、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x101,
        (
            "#12P#00000F自分たちはクロスベル警察・\x01",
            "特務支援課の者です。\x02\x03",

            "ボンドさんですね？\x01",
            "教団事件の際にお会いして\x01",
            "以来だと思いますが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_815D")
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
            "#1K前編「迷い猫の飼い主探し」クエストを？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",        # 0
            "【やっている】\x01",        # 1
            "【やっていない】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8149")
    OP_29(0x8, 0x4, 0x10)
    Jump("loc_815D")

    label("loc_8149")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_815D")
    OP_29(0x8, 0x3, 0x10)

    label("loc_815D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_829E")

    #C0456
    ChrTalk(
        0xC,
        "ああ、もちろん覚えているとも。\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xC,
        (
            "何と言っても、あの《砦》で\x01",
            "我々を牢屋から解放してくれたのは\x01",
            "他ならぬ君たちだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xC,
        (
            "そういえば、君たちには\x01",
            "マリーを飼うことになった時にも\x01",
            "お世話になっていたんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0xC,
        (
            "いや、君たちには改めて\x01",
            "お礼を言わなきゃと思ってたんだ。\x01",
            "あの時は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8374")

    label("loc_829E")


    #C0460
    ChrTalk(
        0xC,
        "ああ、もちろん覚えているとも。\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0xC,
        (
            "何と言っても、あの《砦》で\x01",
            "我々を牢屋から解放してくれたのは\x01",
            "他ならぬ君たちだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "いや、君たちには改めて\x01",
            "お礼を言わなきゃと思ってたんだ。\x01",
            "あの時は本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8374")


    #C0463
    ChrTalk(
        0xD,
        (
            "私からもお礼を\x01",
            "言わせていただきますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xD,
        (
            "その節は主人が\x01",
            "大変お世話になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#12P#00004Fいえ、とんでもありません。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#12P#00100Fええ、とにかく\x01",
            "お元気そうで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0xC,
        "はは、おかげさまでね。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "ところで、今日は\x01",
            "何か用事でもあったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#12P#00000Fはい、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0470
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ボンドに調査の説明をした上で、\x01",
            "転居した経緯を尋ねた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0471
    ChrTalk(
        0xC,
        (
            "なるほど、\x01",
            "不審な居住者変更届けか……\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        (
            "それで、あの家を手放した\x01",
            "経緯が聞きたいんだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#12P#00103Fはい、失礼は承知なのですが、\x01",
            "手続きなどに違法性がなかったか\x01",
            "どうかを確認したいので……\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xC,
        (
            "いや、失礼だなんてとんでもない。\x01",
            "言ってることはもっともだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0xC,
        (
            "ま、ありていに言うと、\x01",
            "家は自身の借金返済のために\x01",
            "売り払ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xC,
        (
            "売却先は購入先と同じ不動産会社で\x01",
            "手続きも正規のものだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xC,
        (
            "そういう意味で違法な所は\x01",
            "全くないと言えるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        "#12P#00005Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x102,
        (
            "#12P#00103Fあの、これは差し支えなければで\x01",
            "構わないのですが……\x02\x03",

            "#00101F借金そのものの原因について\x01",
            "伺っても宜しいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        (
            "ああ、構わないよ。\x01",
            "単純な話……\x01",
            "これも身から出たサビでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xC,
        (
            "当時の記憶は\x01",
            "あまり定かではないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xC,
        (
            "あの蒼い薬を服用していた時期に\x01",
            "どうやらリスクの高い危険な相場に\x01",
            "手を出していたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0xC,
        (
            "教団事件が終わった頃に\x01",
            "それが一気に大暴落……\x01",
            "多額の借金をしてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x109,
        "#12P#10105Fそ、そんなことが……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xC,
        (
            "ああ。\x01",
            "ただまあ、私は恵まれているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xC,
        (
            "家を含め全ての資産を売り払うことで\x01",
            "借金の多くを返せたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0xC,
        (
            "損害が個人の範囲だったこともあって、\x01",
            "何とか会社もクビにならずに済んだんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    #C0488
    ChrTalk(
        0xC,
        (
            "それに何と言っても……\x01",
            "こんなどうしようもない私を\x01",
            "妻と娘は見放さなかったんだからね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    #C0489
    ChrTalk(
        0xD,
        (
            "#11Pあなた……\x01",
            "それは言わない約束ですわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0xD,
        (
            "#11P大体、私たちは世界に\x01",
            "たった１つの家族なんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xD,
        "#11P苦労を共にするのは当然ですわ。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        "クレイユ……本当にありがとう。\x02",
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xC,
        (
            "君とサニータには\x01",
            "心の底から感謝しているよ。\x02",
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
            "#11Pあ、あなた……\x01",
            "皆さんの見ている前で\x01",
            "恥ずかしいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x109,
        (
            "#12P#10109Fふふ、とても固い絆で\x01",
            "結ばれていらっしゃるんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0x105,
        (
            "#12P#10304Fまあ、家族の絆の前には\x01",
            "住む場所は関係ないという事かな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)

    #C0497
    ChrTalk(
        0xC,
        (
            "はは、そんな大層な話でも\x01",
            "ないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xC,
        (
            "いずれにせよ、心機一転して\x01",
            "ここから頑張るつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        (
            "残りの借金を全て返し終えて、\x01",
            "妻と娘に恩返しをするためにね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    #C0500
    ChrTalk(
        0xD,
        "あなた……\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        (
            "#12P#00104Fご立派な心がけだと思います。\x02\x03",

            "#00100Fあの、今後もし何か\x01",
            "お困りのことがあったら\x01",
            "遠慮なく私たちに依頼してくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)

    #C0502
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、その時は\x01",
            "すぐに駆けつけますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xC,
        (
            "はは、君たちにまで\x01",
            "そんな風に言ってもらえるとは\x01",
            "つくづく有難い話だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xC,
        (
            "うん、それじゃ何かあった時は\x01",
            "頼らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xC,
        (
            "ところで、話の方は\x01",
            "これで大丈夫だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "他にもあったら\x01",
            "何でも答えさせてもらうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、必要な情報は\x01",
            "得られたので十分です。\x02\x03",

            "#00004F調査にご協力いただき、\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x105,
        "#12P#10300Fじゃあ、そろそろ次へ行こうか？\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x102,
        (
            "#12P#00100Fええ、そうね。\x02\x03",

            "#00104Fでは、ボンドさん。\x01",
            "私たちはこれで失礼しますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x109,
        (
            "#12P#10109Fこれからも家族みんなで\x01",
            "仲良くしてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xC,
        "ああ、もちろんだとも！\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xD,
        "うふふ、了解ですわ。\x02",
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

    def lambda_903F():
        OP_95(0xFE, 51400, 0, 2650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_903F)

    def lambda_9059():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9059)
    Sleep(900)

    def lambda_906D():
        OP_95(0xFE, 52300, 0, 2750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_906D)

    def lambda_9087():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9087)
    Sleep(900)

    def lambda_909B():
        OP_95(0xFE, 51400, 0, 3650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_909B)

    def lambda_90B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_90B5)
    Sleep(900)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_90DB():
        OP_95(0xFE, 52300, 0, 3750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90DB)

    def lambda_90F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_90F5)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(200)

    def lambda_9121():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9121)
    Sleep(50)

    def lambda_9131():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9131)
    Sleep(1000)

    #C0513
    ChrTalk(
        0xE,
        "#6Pあら、お兄さんたち……\x02",
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

    def lambda_91B4():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91B4)
    Sleep(50)

    def lambda_91C4():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91C4)
    Sleep(50)

    def lambda_91D4():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_91D4)
    Sleep(50)

    def lambda_91E4():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_91E4)
    Sleep(50)

    def lambda_91F4():
        OP_95(0x101, 50250, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91F4)
    Sleep(50)

    def lambda_9211():
        OP_95(0x102, 50500, 0, 3650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9211)
    Sleep(50)

    def lambda_922E():
        OP_95(0x109, 51500, 0, 2550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_922E)
    Sleep(50)

    def lambda_924B():
        OP_95(0x105, 51750, 0, 3750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_924B)
    SetMapObjFlags(0x1, 0x0)
    WaitChrThread(0x101, 1)

    #C0514
    ChrTalk(
        0xE,
        (
            "#6Pお父さまとお母さまに\x01",
            "何か用事でもありましたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ちょっとだけ\x01",
            "お話をさせてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x102,
        (
            "#11P#00100Fサニータちゃんと言ったかしら。\x01",
            "いいご両親を持っているわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0517
    ChrTalk(
        0xE,
        "#6Pわ、分かりますの？\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0xE,
        (
            "#6Pそうですわ、\x01",
            "とくにお引越しをしてからは\x01",
            "２人ともすごく仲がよくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xE,
        (
            "#6Pえへへ、とっても\x01",
            "じまんのりょーしんですのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0520
    ChrTalk(
        0xE,
        "#12Pね、マリーもそう思うでしょう？\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    #C0521
    ChrTalk(
        0xF,
        "#6Pにゃ～ん㈱\x02",
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x109,
        "#10102Fふふ、前向きで救われますね。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        "#00000Fああ、何よりなことだ。\x02",
    )

    CloseMessageWindow()

    def lambda_9475():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9475)
    Sleep(50)

    def lambda_9485():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9485)
    Sleep(50)

    def lambda_9495():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9495)
    Sleep(50)

    def lambda_94A5():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_94A5)

    #C0524
    ChrTalk(
        0x101,
        (
            "#12P#00003Fさてと、これでボンドさんの\x01",
            "状況は確認できたわけだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95EE")
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
            "◆「調査状況は？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",                  # 0
            "【まだ残りがある】\x01",              # 1
            "【６箇所の確認が終わった】\x01",      # 2
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
        (0, "loc_95C1"),
        (1, "loc_95C6"),
        (2, "loc_95DA"),
        (SWITCH_DEFAULT, "loc_95EE"),
    )


    label("loc_95C1")

    Jump("loc_95EE")

    label("loc_95C6")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_95EE")

    label("loc_95DA")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_95EE")

    label("loc_95EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_964A")

    #C0526
    ChrTalk(
        0x101,
        (
            "#12P#00000Fよし、それじゃ引き続き\x01",
            "残りの調査にあたろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_969D")

    label("loc_964A")


    #C0527
    ChrTalk(
        0x101,
        (
            "#12P#00000Fよし、これで一通り調査は済んだな。\x02\x03",

            "市民会館へ報告に戻ろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_969D")

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

    # Function_22_7F32 end

    def Function_23_9703(): pass

    label("Function_23_9703")

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
            "ひぐっ、ひぐっ……\x01",
            "サニータがいけないんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0xE,
        (
            "サニータがマリーを\x01",
            "ちゃんと見ていなかったから……\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xD,
        (
            "サニータ……そんなに\x01",
            "自分を責めてはいけませんわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0xC,
        (
            "#5Pああ、それに\x01",
            "マリーは必ず見つかるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xC,
        (
            "#5Pだから、サニータ。\x01",
            "元気をお出し。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x10E, 0x1F4)

    #C0533
    ChrTalk(
        0xC,
        "#11Pああ、君たちは……！\x02",
    )

    CloseMessageWindow()

    def lambda_98DE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_98DE)
    Sleep(50)

    def lambda_98EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_98EE)
    WaitChrThread(0xD, 1)

    #C0534
    ChrTalk(
        0xD,
        "まあ……\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#6P#00000Fどうも、こんにちは。\x01",
            "依頼を拝見して伺いました。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xC,
        (
            "#11Pちゃんと見てくれたんだね、\x01",
            "……ありがたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xC,
        (
            "#11P正直な所、警察というより\x01",
            "ギルドに頼むような\x01",
            "内容かとも思ったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xC,
        (
            "#11P君たちのことが頭に浮んだから\x01",
            "頼らせてもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x102,
        (
            "#6P#00100Fええ、そう言って頂けると\x01",
            "こちらもありがたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x109,
        (
            "#6P#10103F何でも仔猫のマリーちゃんが\x01",
            "行方不明ということですが……\x02\x03",

            "#10100F一体、いつから\x01",
            "居なくなったか分かりますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xC,
        (
            "#11Pああ、はっきりした時間は\x01",
            "分からないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xC,
        "#11P昨日の夕方過ぎからなんだ。\x02",
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xD,
        (
            "家族みんなで東通りの\x01",
            "露店を見ている時に\x01",
            "サニータが気付いたんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xD,
        (
            "目を離している隙に突然いなく\x01",
            "なってしまったみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xD,
        (
            "その後、商店街の皆さんにも\x01",
            "手伝っていただいて\x01",
            "付近を捜したのですけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xC,
        (
            "#11Pああ、それで夜になるまで\x01",
            "みんなで捜したんだけど、\x01",
            "結局見つからなかったんだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 500)

    #C0547
    ChrTalk(
        0xE,
        (
            "うぐ、うぐっ……\x01",
            "お父様は嘘つきですわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xE,
        (
            "今朝になれば\x01",
            "帰って来るって言ったのに！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    #C0549
    ChrTalk(
        0xC,
        "#5Pすまない、サニータ……\x02",
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0x102,
        "#6P#00108Fサニータちゃん……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x101,
        (
            "#6P#00001Fちなみに……\x01",
            "何か目撃情報はあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D36():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9D36)
    Sleep(50)

    def lambda_9D46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9D46)
    WaitChrThread(0xE, 2)

    #C0552
    ChrTalk(
        0xC,
        (
            "#11Pああ──といっても全て\x01",
            "昨日の段階のものだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0xC,
        (
            "#11Pそれらの情報によると、\x01",
            "さすがに街道には\x01",
            "出ていないようなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0xC,
        (
            "#11P中央広場方面へ向かう\x01",
            "マリーを見たという人がいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xC,
        (
            "#11P昨日はもう夜も遅かったから\x01",
            "それ以上は追いきれず、\x01",
            "捜索を切り上げたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        (
            "#6P#00301F……で、音沙汰なく\x01",
            "今朝に至るってわけか。\x02\x03",

            "#00303Fとなると市内であれば\x01",
            "どこへ行ってても\x01",
            "不思議じゃねえかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x105,
        (
            "#6P#10300Fつまり、捜索範囲は\x01",
            "市内全域ってことかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x101,
        (
            "#6P#00006Fう～ん、もう少し何か\x01",
            "手がかりが欲しい所だけど……\x02\x03",

            "#00001F失礼ですが……\x01",
            "これまでにマリーちゃんが\x01",
            "出て行ったことは？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xC,
        "#11Pいや、それが一度もないんだ。\x02",
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xC,
        (
            "#11P何しろ、マリーは\x01",
            "サニータによく懐いていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xC,
        (
            "#11Pそれに臆病な子だから\x01",
            "自分から離れてどこかに行くのは\x01",
            "どうにも考えづらいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xC,
        (
            "#11Pだから何かの拍子で僕たちを見失って\x01",
            "迷子になったんだと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x101,
        "#6P#00003Fなるほど、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0x102,
        (
            "#6P#00100Fとにかく、まずは街に出て\x01",
            "捜してみるしかないのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、とりあえずは\x01",
            "そこから始めるしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xC,
        (
            "#11P僕も落ち着いたら\x01",
            "また捜しに行くつもりだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0xC,
        (
            "#11P長丁場になりそうだし、\x01",
            "もし他に用事があれば先に\x01",
            "片付けてくれて構わないからね？\x02",
        )
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x101,
        "#6P#00000Fそうですね……\x02",
    )

    CloseMessageWindow()
    OP_29(0x74, 0x1, 0x0)
    Call(0, 24)
    EventEnd(0x5)
    Return()

    # Function_23_9703 end

    def Function_24_A218(): pass

    label("Function_24_A218")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【すぐに捜索を開始する】\x01",      # 0
            "【少し待ってもらう】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E2")

    #C0569
    ChrTalk(
        0x101,
        (
            "#6P#00000Fいえ、他は大丈夫なので\x01",
            "すぐに捜索を始めたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xC,
        "#11Pそうか、助かるよ。\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_A35C")

    label("loc_A2E2")

    OP_29(0x74, 0x1, 0x1)

    #C0571
    ChrTalk(
        0x101,
        (
            "#6P#00000Fでは申し訳ありませんが……\x01",
            "少しだけ待っていて\x01",
            "もらっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xC,
        "#11P了解だ、じゃあまた後で。\x02",
    )

    CloseMessageWindow()

    label("loc_A35C")

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

    # Function_24_A218 end

    def Function_25_A3AD(): pass

    label("Function_25_A3AD")

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
        "#11Pああ、君たちか。\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xC,
        (
            "#11Pマリーの捜索を\x01",
            "始めてもらえるんだね？\x02",
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
            "【仔猫の捜索を開始する】\x01",      # 0
            "【少し待ってもらう】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A568")

    #C0575
    ChrTalk(
        0x101,
        (
            "#6P#00000Fはい、これから\x01",
            "捜索を行いたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xC,
        "#11Pそうか、助かるよ。\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_A5F7")

    label("loc_A568")


    #C0577
    ChrTalk(
        0x101,
        (
            "#6P#00006Fすみません、ちょっと\x01",
            "準備したいことがありまして……\x02\x03",

            "#00000Fもう少しだけ\x01",
            "待ってもらっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xC,
        "#11Pああ、了解したよ。\x02",
    )

    CloseMessageWindow()

    label("loc_A5F7")

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

    # Function_25_A3AD end

    def Function_26_A645(): pass

    label("Function_26_A645")

    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0579
    ChrTalk(
        0x102,
        (
            "#6P#00100Fじゃあ、ロイド。\x01",
            "まずはどこから調べるの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0580
    ChrTalk(
        0x101,
        (
            "#6P#00003Fそうだな、昨日の繰り返しに\x01",
            "なるかもしれないけど……\x02\x03",

            "#00000Fまずは足取りを追う意味でも\x01",
            "東通りから調査すべきだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x104,
        "#6P#00300Fまあ、妥当っちゃあ妥当か。\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x105,
        "#6P#10304Fフフ、捜査の基本ってヤツだね。\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x109,
        (
            "#6P#10100Fちなみに、この東通りで\x01",
            "マリーちゃんが行きそうな場所に\x01",
            "心当たりはありますか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A7D0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7D0)
    Sleep(50)

    def lambda_A7E0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7E0)
    Sleep(300)

    #C0584
    ChrTalk(
        0xD,
        (
            "ええ、それなら\x01",
            "露店にある魚屋さんですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xD,
        (
            "この辺りでは一番の\x01",
            "お気に入りの場所なんですの。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xC,
        (
            "#11Pああ、今朝は確認してないけど\x01",
            "もしかしたら、ひょっこり\x01",
            "姿を見せているかも知れないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xC,
        (
            "#11P店主のマルテさんには\x01",
            "昨日捜索を手伝ってもらったから\x01",
            "来ていれば分かるはずなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xC,
        (
            "#11Pよければ、そちらの方で\x01",
            "話を聞いて来てもらえるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x101,
        "#6P#00000Fなるほど、わかりました。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xC, 500)
    Sleep(300)

    #C0590
    ChrTalk(
        0x102,
        (
            "#6P#00100Fところで、ボンドさんの方は\x01",
            "これからどうされるんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)
    Sleep(300)

    #C0591
    ChrTalk(
        0xC,
        "#11P幸い、今日は仕事も休みでね。\x02",
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0xC,
        (
            "#11Pもう少ししたら\x01",
            "昨日の続きで捜索を\x01",
            "始めるつもりだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0xC,
        (
            "#11P東通りの人たちには昨日の内に\x01",
            "大体声を掛けて回ったからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xC,
        (
            "#11P今度は中央広場の方を\x01",
            "地道に回って情報を\x01",
            "集めようと思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xC,
        (
            "#11P何かあったら\x01",
            "いつでも声を掛けて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x104,
        "#6P#00300F了解ッス。\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそれじゃあ、まずは露店の\x01",
            "魚屋で聞き込みかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x101,
        "#6P#00000Fああ、さっそく向かおう。\x02",
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
            "クエスト【仔猫の捜索依頼】\x07\x00",
            "を開始した！\x02",
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

    # Function_26_A645 end

    def Function_27_AC2A(): pass

    label("Function_27_AC2A")

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
        "#5Pマリー……！\x02",
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xE,
        "#5Pもう……どこに行ってたんですの！\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0xE,
        (
            "#5Pひぐっ、ひぐっ……\x01",
            "ほんとうに心配……\x01",
            "……したん……だから………\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xF,
        "#12Pにゃ、にゃ～ん。\x02",
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(300)

    #C0604
    ChrTalk(
        0xE,
        (
            "#5Pううん……ごめんなさい。\x01",
            "わるいのはサニータだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xE,
        (
            "#5Pでもありがとう……\x01",
            "こうして帰ってきてくれて……\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xE,
        (
            "#5Pこれからは勝手にひとりで\x01",
            "どこかへ行っちゃダメだからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    Sound(953, 0, 100, 0)

    #C0607
    ChrTalk(
        0xF,
        "#12Pにゃ～ん㈱\x02",
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x102,
        "#12P#00109Fふふ、よかったわね。\x02",
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x109,
        "#12P#10100Fこれで一件落着ですね。\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xC,
        (
            "君たちには\x01",
            "何とお礼を言っていいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xC,
        (
            "我が家の大切なマリーを\x01",
            "本当にどうもありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xD,
        "ええ、感謝の言葉もありませんわ。\x02",
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xD,
        (
            "以前は主人を、\x01",
            "そして今度はマリーを……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xD,
        (
            "皆さんは私たち家族の\x01",
            "大大大恩人ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0x101,
        (
            "#12P#00002Fいえ、そんな……\x02\x03",

            "#00000Fそれに今回は俺たちよりも\x01",
            "ここにいる彼女が\x01",
            "一番貢献してくれたんです。\x02\x03",

            "すっかり怯えてしまっていた\x01",
            "マリーを落ち着かせてくれて……\x02",
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
        "#5Pにゃ～ん㈱\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xE,
        "#5P……マリー！？\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xE,
        (
            "#5Pあなた、もしかして\x01",
            "そのお姉さんといっしょに\x01",
            "いたいっていうんじゃ……\x02",
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
        "#12Pにゃ、にゃうん……？\x02",
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x1A3,
        (
            "#12P#04602Fあはは、心配しなくていいよ。\x02\x03",

            "#04604Fマリーからサニータのことは\x01",
            "大好きだって聞いてるからさー。\x02\x03",

            "#04609Fノロケ話をさんざん聞かされて\x01",
            "参っちゃうくらいにね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0621
    ChrTalk(
        0xE,
        "#5Pそ、そうなの、マリー？\x02",
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    #C0622
    ChrTalk(
        0xF,
        "#12Pにゃ～ん㈱\x02",
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x1A3,
        (
            "#12P#04609Fふふっ、それじゃあ\x01",
            "そろそろシャーリィも帰ろっかな？\x02\x03",

            "#04604Fお兄さんたちとも遊べたし、\x01",
            "マリーとも知り合いになれたし。\x02\x03",

            "#04611F──なんと言っても\x01",
            "とっておきを見つけちゃったしね㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B35C():

        label("loc_B35C")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B35C")

    QueueWorkItem2(0x101, 2, lambda_B35C)
    Sleep(300)

    #C0624
    ChrTalk(
        0x101,
        "#11P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    def lambda_B388():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B388)
    Sleep(50)

    def lambda_B3A5():

        label("loc_B3A5")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3A5")

    QueueWorkItem2(0x102, 2, lambda_B3A5)
    Sleep(50)

    def lambda_B3BA():

        label("loc_B3BA")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3BA")

    QueueWorkItem2(0x104, 2, lambda_B3BA)
    Sleep(50)

    def lambda_B3CF():

        label("loc_B3CF")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3CF")

    QueueWorkItem2(0x109, 2, lambda_B3CF)
    Sleep(50)

    def lambda_B3E4():

        label("loc_B3E4")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3E4")

    QueueWorkItem2(0x105, 2, lambda_B3E4)
    Sleep(50)

    def lambda_B3F9():

        label("loc_B3F9")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3F9")

    QueueWorkItem2(0xC, 2, lambda_B3F9)
    Sleep(50)

    def lambda_B40E():

        label("loc_B40E")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B40E")

    QueueWorkItem2(0xD, 2, lambda_B40E)
    Sleep(50)

    def lambda_B423():

        label("loc_B423")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B423")

    QueueWorkItem2(0xE, 2, lambda_B423)
    Sleep(50)

    def lambda_B438():

        label("loc_B438")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B438")

    QueueWorkItem2(0xF, 2, lambda_B438)
    WaitChrThread(0x1A3, 1)

    #C0625
    ChrTalk(
        0x104,
        "#00305Fお、おい……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A3, 0x87, 0x1F4)
    Sleep(300)

    #C0626
    ChrTalk(
        0x1A3,
        (
            "#6P#04602Fあはは、まったねー！\x02\x03",

            "#04609Fまた近いうちに、\x01",
            "会えるかもしれないけどサ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B4CD():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B4CD)
    Sleep(300)

    def lambda_B4EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_B4EA)
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
        "#00106F……えっと……\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x109,
        (
            "#10106Fな、何だか\x01",
            "台風みたいな子でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、台風というより、\x01",
            "竜巻って感じだったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x104,
        (
            "#00306Fったく、叔父貴も\x01",
            "もう少し躾けとけっての……\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x101,
        (
            "#00012Fま、まあ今回に関しては\x01",
            "色々と助けてもらったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xC,
        (
            "うーん、できれば彼女にも\x01",
            "お礼を言いたかったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(300)

    #C0633
    ChrTalk(
        0xC,
        (
            "──とにかく君たち。\x01",
            "改めてお礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B706():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B706)
    Sleep(50)

    def lambda_B716():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_B716)

    def lambda_B723():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B723)
    Sleep(50)

    def lambda_B733():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B733)

    def lambda_B740():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B740)
    Sleep(50)

    def lambda_B750():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_B750)

    def lambda_B75D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B75D)
    Sleep(50)

    def lambda_B76D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B76D)
    WaitChrThread(0x105, 2)

    #C0634
    ChrTalk(
        0xD,
        "このご恩は一生忘れませんわ。\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xE,
        (
            "えとえと、サニータからも\x01",
            "お礼をいわせてくださいまし！\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xF,
        "にゃん㈱\x02",
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        "#12P#00009Fはは、どういたしまして。\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x102,
        (
            "#12P#00100Fまた何かありましたら\x01",
            "遠慮なく連絡なさって下さい。\x02",
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
            "クエスト【仔猫の捜索依頼】\x07\x00",
            "を達成した！\x02",
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

    # Function_27_AC2A end

    def Function_28_B938(): pass

    label("Function_28_B938")

    EventBegin(0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0640
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵がかかっている。\x01",
            "住人はすでに退去したようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 51800, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_28_B938 end

    def Function_29_B995(): pass

    label("Function_29_B995")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0641
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_29_B995 end

    SaveToFile()

Try(main)
