from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1410.bin",                # FileName
        "c1410",                    # MapName
        "c1410",                    # Location
        0x0075,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 117, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1410",                  # 0
        "ワジ",                   # 1
        "アッバス",               # 2
        "キーンツ",               # 3
        "ベッセ",                 # 4
        "リャン",                 # 5
        "アゼル",                 # 6
        "ワジ",                   # 7
        "アシュリー",             # 8
        "サリナ",                 # 9
        "ガイトナー",             # 10
        "見物客",                 # 11
        "見物客",                 # 12
        "見物客",                 # 13
        "見物客",                 # 14
        "見物客",                 # 15
        "見物客",                 # 16
        "グラス",                 # 17
        "グラス",                 # 18
    ))

    AddCharChip((
        "chr/ch00400.itc",                   # 00
        "chr/ch06700.itc",                   # 01
        "chr/ch30900.itc",                   # 02
        "chr/ch31800.itc",                   # 03
        "apl/ch50016.itc",                   # 04
        "chr/ch24500.itc",                   # 05
        "chr/ch21300.itc",                   # 06
        "chr/ch09202.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch21000.itc",                   # 09
        "chr/ch24502.itc",                   # 0A
        "chr/ch21302.itc",                   # 0B
        "chr/ch23702.itc",                   # 0C
        "chr/ch23602.itc",                   # 0D
        "apl/ch50375.itc",                   # 0E
        "apl/ch50091.itc",                   # 0F
    ))

    DeclNpc(0,       0,       11220,   135,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2980,    0,       14779,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2950,    29,      6579,    180,  261,  0x0, 0,   3,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(10229,   0,       4409,    90,   261,  0x0, 0,   2,   0,   0,   2,   0,   25,  255,  0)
    DeclNpc(14069,   0,       13409,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(12770,   0,       15310,   180,  261,  0x0, 0,   14,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-2599,   50,      12600,   0,    261,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-479,    150,     12600,   0,    389,  0x0, 0,   7,   0,   255, 255, 0,   38,  255,  0)
    DeclNpc(0,       0,       5789,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-1269,   0,       12640,   45,   389,  0x0, 0,   9,   0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-1240,   0,       4139,    0,    405,  0x0, 0,   5,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(-170,    0,       4019,    315,  389,  0x0, 0,   6,   0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-2900,   150,     3500,    0,    405,  0x0, 0,   10,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(-4300,   150,     3500,    0,    405,  0x0, 0,   11,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(3730,    150,     12600,   0,    405,  0x0, 0,   12,  0,   255, 255, 0,   47,  255,  0)
    DeclNpc(1559,    150,     12600,   0,    405,  0x0, 0,   13,  0,   255, 255, 0,   50,  255,  0)
    DeclNpc(-2599,   519,     13449,   0,    374,  0x0, 0,   15,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-479,    540,     13449,   0,    502,  0x0, 4,   15,  0,   255, 255, 255, 255, 255,  0)

    DeclActor(2590,    0,       13420,   1500,    2980,    1500,    14780,   0x007E, 0,  16, 0x0000)
    DeclActor(750,     0,       13420,   1500,    750,     1500,    14770,   0x007E, 0,  29, 0x0000)
    DeclActor(750,     0,       13420,   1500,    750,     1500,    14770,   0x007E, 0,  35, 0x0000)

    ScpFunction((
        "Function_0_42C",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_559",          # 02, 2
        "Function_3_632",          # 03, 3
        "Function_4_B58",          # 04, 4
        "Function_5_C17",          # 05, 5
        "Function_6_DB3",          # 06, 6
        "Function_7_311B",         # 07, 7
        "Function_8_354D",         # 08, 8
        "Function_9_3D20",         # 09, 9
        "Function_10_43FF",        # 0A, 10
        "Function_11_4A32",        # 0B, 11
        "Function_12_4C0A",        # 0C, 12
        "Function_13_4F0B",        # 0D, 13
        "Function_14_5154",        # 0E, 14
        "Function_15_52AF",        # 0F, 15
        "Function_16_5FDD",        # 10, 16
        "Function_17_5FE1",        # 11, 17
        "Function_18_60EA",        # 12, 18
        "Function_19_6177",        # 13, 19
        "Function_20_61B2",        # 14, 20
        "Function_21_7354",        # 15, 21
        "Function_22_73FC",        # 16, 22
        "Function_23_7485",        # 17, 23
        "Function_24_7538",        # 18, 24
        "Function_25_7BB9",        # 19, 25
        "Function_26_8D0F",        # 1A, 26
        "Function_27_8DD4",        # 1B, 27
        "Function_28_8F07",        # 1C, 28
        "Function_29_9D61",        # 1D, 29
        "Function_30_9D65",        # 1E, 30
        "Function_31_9E38",        # 1F, 31
        "Function_32_9EF5",        # 20, 32
        "Function_33_9FF0",        # 21, 33
        "Function_34_A101",        # 22, 34
        "Function_35_AC86",        # 23, 35
        "Function_36_AC8A",        # 24, 36
        "Function_37_AD34",        # 25, 37
        "Function_38_ADAC",        # 26, 38
        "Function_39_B1C5",        # 27, 39
        "Function_40_B272",        # 28, 40
        "Function_41_B4FD",        # 29, 41
        "Function_42_B616",        # 2A, 42
        "Function_43_B69F",        # 2B, 43
        "Function_44_B7AD",        # 2C, 44
        "Function_45_B844",        # 2D, 45
        "Function_46_B905",        # 2E, 46
        "Function_47_BA13",        # 2F, 47
        "Function_48_BAF0",        # 30, 48
        "Function_49_BBA1",        # 31, 49
        "Function_50_BC4B",        # 32, 50
        "Function_51_BD71",        # 33, 51
        "Function_52_E601",        # 34, 52
        "Function_53_E674",        # 35, 53
        "Function_54_E6E7",        # 36, 54
        "Function_55_E75A",        # 37, 55
        "Function_56_F49E",        # 38, 56
        "Function_57_F7F3",        # 39, 57
        "Function_58_F823",        # 3A, 58
        "Function_59_F853",        # 3B, 59
        "Function_60_F897",        # 3C, 60
    ))


    def Function_0_42C(): pass

    label("Function_0_42C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_46C"),
        (1, "loc_478"),
        (2, "loc_484"),
        (3, "loc_490"),
        (4, "loc_49C"),
        (5, "loc_4A8"),
        (6, "loc_4B4"),
        (SWITCH_DEFAULT, "loc_4C0"),
    )


    label("loc_46C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_478")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_484")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_490")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_49C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4CC")

    label("loc_4E3")

    Return()

    # Function_0_42C end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_558")
    OP_95(0xFE, 2970, 30, 4200, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(5500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    OP_95(0xFE, 6630, 30, 6580, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Sleep(8500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    Jump("Function_1_4E4")

    label("loc_558")

    Return()

    # Function_1_4E4 end

    def Function_2_559(): pass

    label("Function_2_559")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_631")
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 6340, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 5070, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    Jump("Function_2_559")

    label("loc_631")

    Return()

    # Function_2_559 end

    def Function_3_632(): pass

    label("Function_3_632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_648")
    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_667")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_675")
    Jump("loc_B57")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6CD")
    SetChrPos(0xC, 1070, 0, 15400, 270)
    SetChrPos(0xD, -300, 0, 15400, 90)
    SetChrFlags(0xC, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4")
    SetChrFlags(0xD, 0x10)

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_6C8")

    Jump("loc_B57")

    label("loc_6CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6E0")
    SetChrFlags(0xD, 0x80)
    Jump("loc_B57")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6FF")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_6FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_735")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0xF, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7AB")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0xC, 10230, 0, 4410, 90)
    SetChrPos(0x11, 2950, 30, 6580, 180)
    BeginChrThread(0xC, 0, 0, 2)
    BeginChrThread(0x11, 0, 0, 1)
    Jump("loc_B57")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_85E")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)
    SetChrPos(0xA, -1730, 0, 6920, 0)
    SetChrPos(0xC, 750, 0, 14770, 180)
    SetChrPos(0x11, 2950, 30, 6580, 180)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0x12, -2600, 0, 10330, 0)
    SetChrPos(0x13, -1200, 0, 10360, 315)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0x11, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859")
    SetChrFlags(0x11, 0x10)

    label("loc_859")

    Jump("loc_B57")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_91D")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xA, 0, 0, 7400, 180)
    SetChrPos(0xB, 1000, 0, 7720, 225)
    SetChrPos(0xC, 750, 0, 14770, 180)
    SetChrPos(0x12, 0, 0, 5790, 0)
    SetChrPos(0x13, 680, 0, 5200, 0)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_909")
    SetChrFlags(0xA, 0x10)

    label("loc_909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_918")
    SetChrFlags(0x11, 0x10)

    label("loc_918")

    Jump("loc_B57")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_955")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x10)
    SetChrPos(0xD, 750, 0, 14770, 180)
    Jump("loc_B57")

    label("loc_955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_986")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x18, 0x80)
    Jump("loc_B57")

    label("loc_986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A26")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 1160, 0, 10170, 315)
    SetChrPos(0xA, 2840, 30, 8000, 270)
    SetChrPos(0xB, 1350, 0, 8000, 90)
    SetChrPos(0xC, -750, 0, 7000, 0)
    SetChrPos(0xD, -750, 0, 8500, 180)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A0D")
    SetChrFlags(0x8, 0x10)

    label("loc_A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_A21")

    Jump("loc_B57")

    label("loc_A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A45")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AB3")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0xF, 0x1)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_AAE")
    SetChrPos(0x9, -4000, 0, 16690, 0)
    SetChrPos(0xD, -350, 0, 14760, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE")
    SetChrFlags(0xD, 0x10)

    label("loc_AAE")

    Jump("loc_B57")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_AD2")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AF1")
    SetChrPos(0xD, -4000, 0, 16690, 0)
    Jump("loc_B57")

    label("loc_AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B1E")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0xD, 0, 0, 7400, 180)
    SetChrChipByIndex(0xD, 0x2)
    Jump("loc_B57")

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_B30")
    SetChrChipByIndex(0xD, 0x2)
    Jump("loc_B57")

    label("loc_B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_B52")
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4D")
    SetChrFlags(0xA, 0x10)

    label("loc_B4D")

    Jump("loc_B57")

    label("loc_B52")

    SetChrFlags(0xD, 0x80)

    label("loc_B57")

    Return()

    # Function_3_632 end

    def Function_4_B58(): pass

    label("Function_4_B58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B71")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_B77")

    label("loc_B71")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_B77")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B8D")
    Jump("loc_C16")

    label("loc_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_BA3")
    OP_65(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_C16")

    label("loc_BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BB9")
    OP_65(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_C16")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_BCB")
    OP_66(0x2, 0x1)
    Jump("loc_C16")

    label("loc_BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_BDD")
    OP_65(0x0, 0x1)
    Jump("loc_C16")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BEF")
    OP_65(0x0, 0x1)
    Jump("loc_C16")

    label("loc_BEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_BFD")
    Jump("loc_C16")

    label("loc_BFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C16")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C16")
    OP_65(0x0, 0x1)

    label("loc_C16")

    Return()

    # Function_4_B58 end

    def Function_5_C17(): pass

    label("Function_5_C17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CA2")
    OP_4B(0x9, 0xFF)

    #C0001
    ChrTalk(
        0x8,
        (
            "#0404Fアッバス、折角だから\x01",
            "乾杯してから行こうか。\x02\x03",

            "#0400Fウフフ、一応クロスベルを\x01",
            "讃えるお祭りなワケだしさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_DAF")

    label("loc_CA2")


    #C0002
    ChrTalk(
        0x8,
        (
            "#0404F今日はみんなで記念祭に\x01",
            "繰り出そうって話をしていてね。\x02\x03",

            "#0400F……そうだ、君たちもどう？\x01",
            "結構楽しいと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0003Fいや、悪いが職務中だからさ。\x02\x03",

            "#0001Fっていうかワジ、\x01",
            "分かってて誘ってるだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#0409Fあはは！\x01",
            "君ってホント頭固いなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_DAF")

    TalkEnd(0xFE)
    Return()

    # Function_5_C17 end

    def Function_6_DB3(): pass

    label("Function_6_DB3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E47")
    Jump("loc_E91")

    label("loc_E47")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E67")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E91")

    label("loc_E67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E87")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E91")

    label("loc_E87")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E91")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_F69")

    #C0005
    ChrTalk(
        0xE,
        (
            "#0400F（アッバスに関しては\x01",
            "  僕も詳しいわけじゃないけど。）\x02\x03",

            "（ゼムリア大陸の\x01",
            "  中東部あたりの出身らしいよ。）\x02\x03",

            "（ふふ……\x01",
            "  かなりの物好きなのは確かだよね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3113")

    label("loc_F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_1113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FDD")

    #C0006
    ChrTalk(
        0xE,
        (
            "#0400Fじきに日も落ちるだろう。\x02\x03",

            "どこに行くか知らないけど\x01",
            "早く行った方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_110E")

    label("loc_FDD")


    #C0007
    ChrTalk(
        0xE,
        "#0404F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#0005Fワジ、どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xE,
        (
            "#0400F……いや、そう言えば\x01",
            "今夜は満月だと思ってね。\x02\x03",

            "#0402F今日は晴れているし\x01",
            "綺麗なお月様が見えるんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#0100Fそう……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0200F月は不吉の\x01",
            "象徴でもありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0303F……今の状況だと\x01",
            "洒落になってねぇな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_110E")

    Jump("loc_3113")

    label("loc_1113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_12D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_118C")

    #C0013
    ChrTalk(
        0xE,
        (
            "#0400Fまあ、バイパーの方は\x01",
            "僕の方でも気に掛けておくよ。\x02\x03",

            "君らは君らの\x01",
            "仕事をしてくるといい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12CE")

    label("loc_118C")


    #C0014
    ChrTalk(
        0xE,
        (
            "#0403Fヴァルドもさすがに\x01",
            "焦れてきたみたいだね。\x02\x03",

            "#0400F……あの意地っ張りさえ直せば\x01",
            "楽になれるのにさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0000Fワジって結構、\x01",
            "ヴァルドのこと気に掛けてるよな。\x02\x03",

            "#0005F実はバイパーの事だって\x01",
            "最初から心配してたんじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xE,
        (
            "#0404Fクス……どうかな。\x02\x03",

            "#0402Fただヴァルドってさ、\x01",
            "放っておけない所があるんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12CE")

    Jump("loc_3113")

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_135C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 6)), scpexpr(EXPR_END)), "loc_1354")

    #C0017
    ChrTalk(
        0xE,
        (
            "#0400Fフフ、一課きっての\x01",
            "エースと一緒にいるとはね。\x02\x03",

            "何をしているのか……\x01",
            "まあ、聞かぬが華だろうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1357")

    label("loc_1354")

    Call(0, 7)

    label("loc_1357")

    Jump("loc_3113")

    label("loc_135C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1555")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_1421")

    #C0018
    ChrTalk(
        0xE,
        (
            "#0400F旧市街じゃ今のところ\x01",
            "そのディーノって子以外に\x01",
            "クスリを使ってるのはいなさそうだ。\x02\x03",

            "ただ、誰がクスリを\x01",
            "さばいてるのかも分からないしね。\x01",
            "僕の方でも気をつけておくよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1550")

    label("loc_1421")


    #C0019
    ChrTalk(
        0xE,
        "#0402F……来たね。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0001Fワジ、早速だけど\x01",
            "話を聞かせてくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "#0404F情報料、って言いたい所だけど\x01",
            "今回はタダにしておくよ。\x02\x03",

            "#0406F僕らも無関係じゃないし……\x01",
            "そこそこヤバイ話だからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Call(0, 8)

    label("loc_1550")

    Jump("loc_3113")

    label("loc_1555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1808")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1692")

    #C0022
    ChrTalk(
        0xE,
        (
            "#0404Fそれにしても……襲うだけ襲って\x01",
            "首を取れなかったなんて不手際だね。\x02\x03",

            "#0402F僕がルバーチェなら\x01",
            "確実に仕留める方法を考えるけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x102,
        (
            "#0106F（やっぱりワジ君って\x01",
            "  危険人物なのよねぇ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1803")

    label("loc_1692")


    #C0024
    ChrTalk(
        0xE,
        (
            "#0400Fそういえば、黒月の事務所が\x01",
            "襲われたみたいだけど……\x02\x03",

            "#0403Fルバーチェも無茶するよね。\x01",
            "これじゃ報復してくれと\x01",
            "言わんばかりじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0025
    ChrTalk(
        0x101,
        "#0003Fワジが言うと説得力があるな……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        (
            "#0400Fふふ、当然の事じゃない。\x01",
            "僕が黒月の立場なら\x01",
            "間違いなくお礼するけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1803")

    Jump("loc_3113")

    label("loc_1808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1891")

    #C0027
    ChrTalk(
        0xE,
        (
            "#0403Fどうやら街の方でも\x01",
            "騒ぎがあったみたいだし……\x02\x03",

            "#0402Fフフ、明日は満月だから\x01",
            "みんな血が騒いでるのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1942")

    label("loc_1891")


    #C0028
    ChrTalk(
        0xE,
        "#0403F………………………………\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0000Fワジ？　どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xE,
        (
            "#0402Fいや、別に……\x02\x03",

            "ちょっとバイパーの様子が\x01",
            "気になっただけだよ。\x01",
            "昨夜は揉めていたみたいだしね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1942")

    Jump("loc_3113")

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 4)), scpexpr(EXPR_END)), "loc_1B11")
    SetChrSubChip(0xE, 0x0)
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x109, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19F1")
    Jump("loc_1A3B")

    label("loc_19F1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A11")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A3B")

    label("loc_1A11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A31")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A3B")

    label("loc_1A31")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A3B")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0031
    ChrTalk(
        0x109,
        (
            "#0501Fだ、だいたい未成年のくせに\x01",
            "昼間っからお酒を飲んでるなんて\x01",
            "良くないんじゃないかな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xE,
        "#0402Fあ、これただのジュースだから。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0006F（また適当な事を……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B14")

    label("loc_1B11")

    Call(0, 9)

    label("loc_1B14")

    Jump("loc_3113")

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_1B89")

    #C0034
    ChrTalk(
        0xE,
        (
            "#0400Fまあ、ゆっくりして行きなよ。\x02\x03",

            "よかったら３人で\x01",
            "ミルクセーキでも飲んでいけば？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8C")

    label("loc_1B89")

    Call(0, 10)

    label("loc_1B8C")

    TalkEnd(0xFE)
    SetChrSubChip(0xE, 0x2)
    Return()

    label("loc_1B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C22")

    #C0035
    ChrTalk(
        0xE,
        (
            "#0406F僕、こう見えても\x01",
            "記念祭の間は忙しいんだよね。\x02\x03",

            "#0400Fフフ、残念だけど\x01",
            "適当に相手して帰しちゃおうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C25")

    label("loc_1C22")

    Call(0, 11)

    label("loc_1C25")

    Jump("loc_3113")

    label("loc_1C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_1CD7")

    #C0036
    ChrTalk(
        0xE,
        (
            "#0400Fま、今日は君たちも\x01",
            "ゆっくりして行きなよ。\x02\x03",

            "アッバスはあれで\x01",
            "カクテルの腕は良くてね。\x02\x03",

            "フフ、今日のレシピは\x01",
            "中々イケてるよ。\x01",
            "君たちもどう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EBE")

    label("loc_1CD7")


    #C0037
    ChrTalk(
        0xE,
        (
            "#0404Fフフ、昨日はどうも。\x02\x03",

            "#0400F話題の遊撃士コンビにも会えたし\x01",
            "なかなか楽しませてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0005Fワジは……\x01",
            "特に疲れとか無いのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0039
    ChrTalk(
        0xE,
        (
            "#0405Fえ、疲れ？\x01",
            "もしかして昨日のレースの事？\x02\x03",

            "#0402Fあはは、あんなの普通じゃない。\x02\x03",

            "ヴァルドとの喧嘩なんて\x01",
            "いつもあの調子だよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0040
    ChrTalk(
        0x101,
        "#0003F（不良の体力は侮れないな……）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        "#0306F（つーか俺は歳を感じるぜ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 0)

    label("loc_1EBE")

    Jump("loc_3113")

    label("loc_1EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1EF9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 7)), scpexpr(EXPR_END)), "loc_1EE9")
    Call(0, 13)
    Jump("loc_1EEC")

    label("loc_1EE9")

    Call(0, 12)

    label("loc_1EEC")

    Jump("loc_1EF4")

    label("loc_1EF1")

    Call(0, 13)

    label("loc_1EF4")

    Jump("loc_3113")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1F37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 7)), scpexpr(EXPR_END)), "loc_1F1F")
    Call(0, 14)
    Jump("loc_1F22")

    label("loc_1F1F")

    Call(0, 12)

    label("loc_1F22")

    Jump("loc_1F2A")

    label("loc_1F27")

    Call(0, 14)

    label("loc_1F2A")

    TalkEnd(0xFE)
    SetChrSubChip(0xE, 0x2)
    Return()

    label("loc_1F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_22B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 5)), scpexpr(EXPR_END)), "loc_201B")

    #C0042
    ChrTalk(
        0xE,
        (
            "#0400F最近クロスベルの裏社会に\x01",
            "《黒月》ってのが\x01",
            "入ってきてるらしいね。\x02\x03",

            "#0400F最近は密輸ルートなんかを巡って\x01",
            "小競り合いをしてるらしいよ。\x02\x03",

            "#0406Fやれやれ……\x01",
            "こっちにまで飛び火しなきゃ\x01",
            "いいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22B2")

    label("loc_201B")


    #C0043
    ChrTalk(
        0xE,
        (
            "#0400F最近クロスベルの裏社会に\x01",
            "《黒月》ってのが\x01",
            "入ってきてるらしいね。\x02\x03",

            "東方系の組織らしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0000Fああ、カルバードの\x01",
            "東方人街を締めてる\x01",
            "巨大マフィアらしい……\x02\x03",

            "#0001Fワジ、何か知ってるのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0045
    ChrTalk(
        0xE,
        (
            "#0405F……え？\x01",
            "知ってるって程じゃないけど……\x02\x03",

            "#0400F最近は密輸ルートなんかを巡って\x01",
            "小競り合いをしてるらしいよ。\x02\x03",

            "ルバーチェが押されてきてるらしいけど、\x01",
            "兵力を増強したって噂もあるしさ。\x02\x03",

            "#0406Fこっちにまで飛び火するかも\x01",
            "しれないから警戒してるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0001Fそうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0301Fにしても、そんな情報\x01",
            "どこから聞いてきたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xE,
        (
            "#0404Fフッ、確かに\x01",
            "僕の専門外だけどさ。\x02\x03",

            "#0402Fこう見えて僕って\x01",
            "付き合い広いからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 5)

    label("loc_22B2")

    Jump("loc_3113")

    label("loc_22B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2629")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 4)), scpexpr(EXPR_END)), "loc_245D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2360")

    #C0049
    ChrTalk(
        0xE,
        (
            "#0400Fフフ、最近じゃ\x01",
            "《特務支援課》の名前も\x01",
            "売れてきたみたいじゃない。\x02\x03",

            "#0404Fま、その調子で頑張りなよ。\x01",
            "僕も楽しみにしてるからさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2458")

    label("loc_2360")


    #C0050
    ChrTalk(
        0xE,
        (
            "#0400Fフフ、最近じゃ\x01",
            "《特務支援課》の名前も\x01",
            "売れてきたみたいじゃない。\x02\x03",

            "#0409Fどっちかというと\x01",
            "お笑いの対象としてだけどさ。\x01",
            "あはははは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0303F……クロスベルタイムズのせいで\x01",
            "イヤな売れ方しちまってるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#0106Fそうねぇ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2458")

    Jump("loc_2624")

    label("loc_245D")


    #C0053
    ChrTalk(
        0xE,
        (
            "#0400Fやあ、ロイド達じゃない。\x02\x03",

            "最近見なかったけど\x01",
            "また何か捜査でもしてるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0000Fいや、今日は\x01",
            "細かい支援要請だよ。\x02\x03",

            "#0006F最近は本部の応援とかも多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xE,
        (
            "#0404Fフフ、記念祭前の\x01",
            "賑わいってわけだね。\x02\x03",

            "#0400Fまあその調子で頑張りなよ。\x02\x03",

            "最近のクロスベルタイムズにも\x01",
            "前よりはマシな取り上げられ方を\x01",
            "されてたみたいだしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0003Fあ、ああ、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0305F（つーか何故不良グループのヘッドに\x01",
            "  こんな事を言われてんだろうなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 4)

    label("loc_2624")

    Jump("loc_3113")

    label("loc_2629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_267B")

    #C0058
    ChrTalk(
        0xE,
        (
            "#0400Fやれやれ……今日は\x01",
            "適当に切り上げちゃおうかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2711")

    label("loc_267B")


    #C0059
    ChrTalk(
        0xE,
        (
            "#0406Fやれやれ……\x01",
            "僕、これから\x01",
            "仕事があるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0000F仕事……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xE,
        (
            "#0402Fフフ、ヒ・ミ・ツ。\x02\x03",

            "これ以上は\x01",
            "情報料を貰わなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2711")

    Jump("loc_3113")

    label("loc_2716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_27DA")

    #C0062
    ChrTalk(
        0xE,
        (
            "#0403F白きたてがみを持つ狼、\x01",
            "鐘響く宿業の地を見守らん──\x01",
            "……だったかな？\x02\x03",

            "#0400F七耀教会の聖典あたりに\x01",
            "そんな話があった気がするよ。\x02\x03",

            "#0404Fまあ、まさかとは思うけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A0C")

    label("loc_27DA")


    #C0063
    ChrTalk(
        0xE,
        (
            "#0400Fクロスベルの警備隊が\x01",
            "狼型魔獣ってのを\x01",
            "山狩りしてるんだって？\x02\x03",

            "#0404Fフーン……狼型って所が\x01",
            "少し気になるよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0001F山狩りっていうか\x01",
            "警備巡回らしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0301Fつーかどこから\x01",
            "仕入れたんだよ、そんな情報をよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xE,
        (
            "#0404Fフフ……\x01",
            "どうやら本当の話っぽいね。\x02\x03",

            "#0400F……いやさ、確か教会の聖典に\x01",
            "そんな話があった気がしたからさ。\x02\x03",

            "#0403F白きたてがみを持つ狼、\x01",
            "鐘響く宿業の地を見守らん──\x01",
            "……だったかな？\x02\x03",

            "#0400Fまあ、まさかとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#0005Fそ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0100F村長さんの話……\x01",
            "意外とはっきりした形で\x01",
            "伝えられているみたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2A0C")

    Jump("loc_3113")

    label("loc_2A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2CCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2ABF")

    #C0069
    ChrTalk(
        0xE,
        (
            "#0403Fあの夜は、君たち支援課の\x01",
            "お世話になっちゃったね。\x02\x03",

            "#0402Fフフ、また何かあったらおいでよ。\x01",
            "僕の気が向いたら\x01",
            "力になってあげるかもしれないよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CC8")

    label("loc_2ABF")


    #C0070
    ChrTalk(
        0xE,
        (
            "#0405Fやあ、ロイドじゃないか。\x02\x03",

            "#0402F嬉しいね……\x01",
            "僕に会いに来てくれたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#0013Fえっ！？　えっとその……\x02\x03",

            "#0013F別に普通の意味で\x01",
            "礼を言いにきただけというか……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0072
    ChrTalk(
        0x103,
        (
            "#0211Fロイドさんが\x01",
            "不自然に慌てています。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        (
            "#0403Fフフ……冗談はさておき。\x02\x03",

            "#0400Fあの夜は、君たち支援課の\x01",
            "お世話になっちゃったね。\x02\x03",

            "#0402Fまた何かあったらおいでよ。\x01",
            "僕の気が向いたら\x01",
            "力になってあげるかもしれないよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0003Fあ、ああ、その時はよろしく。\x01",
            "（何か苦手なんだよな、こいつ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2CC8")

    Jump("loc_3113")

    label("loc_2CCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2D9A")

    #C0075
    ChrTalk(
        0xE,
        (
            "#0404Fメンバーには改めて\x01",
            "勝手な真似はしないように\x01",
            "言っておいたよ。\x02\x03",

            "#0400F少なくとも今日一日は\x01",
            "猶予があるんじゃないかな。\x02\x03",

            "#0402Fフフ……捜査するなら\x01",
            "急いだ方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FD7")

    label("loc_2D9A")


    #C0076
    ChrTalk(
        0xE,
        (
            "#0404Fメンバーには改めて\x01",
            "勝手な真似はしないように\x01",
            "言っておいたよ。\x02\x03",

            "#0400F少なくとも今日一日は\x01",
            "猶予があるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#0001Fそうか……助かるよ。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xE,
        (
            "#0402Fそんな……やだなぁ。\x01",
            "別に君達のために\x01",
            "言ったわけじゃないし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0xE,
        (
            "#0402F今のうちに戦力を蓄えて\x01",
            "バイパーを血祭りに上げるために\x01",
            "決まってるじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0080
    ChrTalk(
        0x104,
        (
            "#0306F（可愛い顔してても\x01",
            "  不良は不良……だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2FD7")

    Jump("loc_3113")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_304C")

    #C0081
    ChrTalk(
        0xE,
        (
            "#0400Fフフ……\x01",
            "ぜひ面白い話を持ってきてよ。\x02\x03",

            "僕も少しの間なら\x01",
            "待っててあげるかもしれないよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3113")

    label("loc_304C")


    #C0082
    ChrTalk(
        0xE,
        (
            "#0400Fロイドって言ったっけ？\x01",
            "君、とっても面白いじゃない。\x02\x03",

            "#0402Fフフ……ここには\x01",
            "いつでも来ちゃっていいからさ。\x01",
            "ぜひ面白い話を持ってきてよ。\x02\x03",

            "僕も少しの間なら\x01",
            "待っててあげるかもしれないよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_3113")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_DB3 end

    def Function_7_311B(): pass

    label("Function_7_311B")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(-1760, 1100, 11760, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -890, 0, 11490, 315)
    SetChrPos(0x102, -780, 0, 10570, 315)
    SetChrPos(0x103, -2780, 0, 10550, 0)
    SetChrPos(0x104, -3990, 0, 10450, 45)
    SetChrPos(0x10A, -1990, 0, 10100, 0)
    SetChrPos(0xE, -2500, 50, 12400, 135)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    SetChrSubChip(0xE, 0x2)
    Sleep(1000)

    #C0083
    ChrTalk(
        0xE,
        (
            "#0402Fこれはこれは……\x01",
            "珍しい人を連れているね？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x10A,
        (
            "#0603F久しぶりだな、\x01",
            "ワジ・ヘミスフィア。\x02\x03",

            "#0601Fいいかげん下らん不良ゴッコを\x01",
            "止めるつもりにはならんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xE,
        (
            "#0404Fフフ、何度も言ってるように\x01",
            "僕はどっちでもいいんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_32D3():
        TurnDirection(0x101, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32D3)

    def lambda_32E0():
        TurnDirection(0x102, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32E0)

    def lambda_32ED():
        TurnDirection(0x103, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_32ED)

    def lambda_32FA():
        TurnDirection(0x104, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_32FA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0086
    ChrTalk(
        0x101,
        (
            "#0011Fダドリー捜査官……\x01",
            "彼と知り合いだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x10A,
        (
            "#0601F２年前、こいつが旧市街に来て\x01",
            "チームを作った時からな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xE,
        (
            "#0404Fフフ、彼は捜査一課でも\x01",
            "唯一定期的に旧市街に\x01",
            "足を運んでるみたいだからね。\x02\x03",

            "#0402F何でも僕の知らない\x01",
            "誰かさんの影響みたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        "#0005F誰かさん……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x10A,
        "#0603F下らんお喋りはそこまでだ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x9, 350)

    #C0091
    ChrTalk(
        0x10A,
        (
            "#0601F#6Pアッバス。\x01",
            "こいつが無用にヴァルドを\x01",
            "挑発しないよう気をつけておけ。\x02\x03",

            "我々一課を本気で出張らせるなよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 350)

    #C0092
    ChrTalk(
        0x9,
        "……承知した。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    #C0093
    ChrTalk(
        0xE,
        "#0404Fやれやれ。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 0, 11490, 315)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xD0, 6)
    OP_4C(0x9, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_7_311B end

    def Function_8_354D(): pass

    label("Function_8_354D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    OP_68(-2940, 1100, 11130, 0)
    MoveCamera(51, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, -2690, 0, 10450, 360)
    SetChrPos(0x102, -1410, 0, 10430, 315)
    SetChrPos(0x103, -4080, 0, 10220, 45)
    SetChrPos(0x104, -4600, 0, 11800, 90)
    SetChrPos(0xE, -2690, 50, 12150, 180)
    SetChrSubChip(0xE, 0x0)
    SetCameraDistance(19950, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0094
    ChrTalk(
        0xE,
        (
            "#0403F#5Pバイパーのパシリの子は\x01",
            "ディーノっていったっけ。\x02\x03",

            "#0401F最近、様子が変だったみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_36FC")

    #C0095
    ChrTalk(
        0x104,
        (
            "#0303F#6Pああ、噂には聞いてたな。\x01",
            "確か幹部とタイマンしたとか何とか……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        (
            "#0402F#5Pそれがさ、昨日はついに\x01",
            "ヴァルドに喧嘩を挑んだらしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37E0")

    label("loc_36FC")


    #C0097
    ChrTalk(
        0x101,
        "#0008F#12Pやっぱりそうか……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xE,
        (
            "#0406F#5Pああ、とても新人とは思えない\x01",
            "横柄で乱暴な態度になったらしくてさ。\x02\x03",

            "#0401Fうちのメンバーにも\x01",
            "頻繁に絡んできてたみたいだけど……\x02\x03",

            "#0402F昨日はついに\x01",
            "ヴァルドに喧嘩を挑んだらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37E0")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0099
    ChrTalk(
        0x101,
        "#0007F#12Pあ、あのヴァルドに……！？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        (
            "#0402F#5Pそういうこと。\x02\x03",

            "#0404F聞いた話だけど、\x01",
            "もの凄いスピードと力で\x01",
            "ヴァルドと良い勝負をしたらしいよ。\x02\x03",

            "最終的にはヴァルドが全力を出して\x01",
            "何とか勝ったらしいんだけど……\x02\x03",

            "#0400Fディーノの方は\x01",
            "そのまま飛び出て行った挙句に\x01",
            "今朝、誰も姿を見てないらしいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#0306F#6Pヤバイじゃねえか……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0108F#12Pさすがにそれは……\x01",
            "ただ事じゃないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xE)

    #C0103
    ChrTalk(
        0xE,
        (
            "#0404F#5Pそれで……\x02\x03",

            "#0402Fやっぱり何かのクスリなわけ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0104
    ChrTalk(
        0x101,
        "#0011F#12Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#0105F#12Pどこでそれを……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xE,
        (
            "#0405F#5Pあ、やっぱりそうなんだ。\x02\x03",

            "#0404F最近『願いが叶う薬』とかいう\x01",
            "都市伝説みたいな噂が流れてるからさ。\x01",
            "もしかしてと思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        "#0211F#6Pカマかけですか……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#0301F#6Pおい、あんまり\x01",
            "周りに広めるんじゃねえぞ？\x02\x03",

            "事が事だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        (
            "#0409F#5Pフフ、その辺は弁えてるよ。\x02\x03",

            "#0400F#5Pま、旧市街じゃ今のところ\x01",
            "そのディーノって子以外に\x01",
            "クスリを使ってるのはいなさそうだ。\x02\x03",

            "#0404Fただ、誰がクスリを\x01",
            "さばいてるのかも分からないしね。\x01",
            "僕の方でも気をつけておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#0000F#12P……助かるよ、ワジ。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#0100F#12P頼りにしてるわね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -2690, 0, 10250, 360)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetScenarioFlags(0xC8, 1)
    OP_29(0x4C, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_8_354D end

    def Function_9_3D20(): pass

    label("Function_9_3D20")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-1760, 1100, 11760, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -890, 0, 11490, 315)
    SetChrPos(0x102, -780, 0, 10570, 315)
    SetChrPos(0x103, -2780, 0, 10550, 0)
    SetChrPos(0x104, -3990, 0, 10450, 45)
    SetChrPos(0x109, -1990, 0, 10100, 0)
    SetChrPos(0xE, -2500, 50, 12400, 135)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0112
    ChrTalk(
        0xE,
        (
            "#0402Fやあロイド達じゃない。\x01",
            "今日もお仕事？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0003Fああ、色々と仕事が入っててさ。\x02\x03",

            "#0000F旧市街の方は変わりないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xE,
        (
            "#0403F………………………………\x02\x03",

            "#0400Fまあね、テスタメンツは\x01",
            "いつも通りだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0115
    ChrTalk(
        0xE,
        (
            "#0400Fフフ、それはそうと……\x02\x03",

            "#0402F珍しい人を連れてるじゃない。\x01",
            "警備隊の人かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#0000Fああ、ちょうど手伝いで\x01",
            "同行してもらってるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x109,
        (
            "#0500F初めまして、\x01",
            "ノエル・シーカーです。\x02\x03",

            "ロイドさんたちの\x01",
            "お知り合いみたいですね？\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    #C0118
    ChrTalk(
        0xE,
        (
            "#0402Fへえ……\x02\x03",

            "#0404Fフフ、生真面目っていうか\x01",
            "中々からかい甲斐のありそうな\x01",
            "お姉さんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x109,
        "#0505Fなっ……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#0011Fおい、ワジ……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        (
            "#0403Fあのさ、僕みたいな悪ガキにまで\x01",
            "わざわざ敬語を使わないでもいいよ。\x02\x03",

            "#0402Fどちらかっていうと\x01",
            "お姉さんみたいなタイプには\x01",
            "小うるさく言われたいんだよね。\x02\x03",

            "#0405Fあ、別にＭってわけじゃないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        (
            "#0503Fき、君ねぇ……\x02\x03",

            "#0501F人が真面目に挨拶してるのに\x01",
            "そんな馬鹿にした態度は\x01",
            "ないんじゃないかな？\x02\x03",

            "大体その格好はなに？\x01",
            "もっと若者らしい格好をしないと！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xE,
        "#0409Fそうそう、そんな感じでさ㈱\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x109,
        "#0505Fむぐっ……\x02",
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
    Sleep(1000)

    #C0125
    ChrTalk(
        0x101,
        (
            "#0003F（生真面目な曹長を\x01",
            "  ここに連れてきたのは\x01",
            "  ちょっと失敗だったかな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#0300F（はは、これはこれで\x01",
            "  意外と気が合ってそうだけどな。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -890, 0, 11490, 315)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xD0, 4)
    EventEnd(0x5)
    Return()

    # Function_9_3D20 end

    def Function_10_43FF(): pass

    label("Function_10_43FF")

    SetChrSubChip(0xE, 0x2)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-2840, 1100, 11440, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -2660, 0, 10470, 0)
    SetChrPos(0xEF, -1570, 0, 10560, 315)
    SetChrPos(0x153, -3700, 0, 10800, 45)
    SetChrPos(0xE, -2710, 0, 12150, 180)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)

    #C0127
    ChrTalk(
        0x153,
        "#1110Fあっ、ワジだー。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    #C0128
    ChrTalk(
        0xE,
        (
            "#0402Fやあ、久し振り。\x01",
            "君の方は元気にしてたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x153,
        (
            "#1109Fうん、キーア元気だよ。\x01",
            "朝ゴハンもちゃんと食べてきたモン！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xE,
        "#0402Fフフ、それは何よりだ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    #C0131
    ChrTalk(
        0xE,
        (
            "#0404F……どうやら\x01",
            "何とか乗り切ったみたいだね？\x02\x03",

            "#0400Fルバーチェの方も\x01",
            "手打ちになったって聞いたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#0000Fああ、今朝ようやくね。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_467F")

    #C0133
    ChrTalk(
        0x102,
        (
            "#0100Fそれでキーアちゃんに\x01",
            "街を案内してるところなの。\x02\x03",

            "#0101F……ワジ君。\x01",
            "キーアちゃんに変なことを\x01",
            "吹き込まないでちょうだいね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4797")

    label("loc_467F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4717")

    #C0134
    ChrTalk(
        0x103,
        (
            "#0200Fそれでキーアに\x01",
            "街を案内しているというわけです。\x02\x03",

            "#0203F……ワジさん。\x01",
            "キーアに変なことを\x01",
            "吹き込まないようお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4797")

    label("loc_4717")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4797")

    #C0135
    ChrTalk(
        0x104,
        (
            "#0300Fそれでキー坊に\x01",
            "街を案内してるって訳だ。\x02\x03",

            "#0301F……おいワジ、あんまキー坊に\x01",
            "変なことを吹き込むなよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4797")


    #C0136
    ChrTalk(
        0x101,
        (
            "#0003Fそうだった……\x02\x03",

            "#0001Fワジ、くれぐれも\x01",
            "言葉に気をつけてくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xE,
        (
            "#0404Fフフ、心外だなぁ。\x02\x03",

            "#0400Fしかし２人とも\x01",
            "完全に保護者の顔をしてるねぇ。\x02\x03",

            "さしずめ彼女の\x01",
            "パパとママってところかな？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48DC")

    #C0138
    ChrTalk(
        0x102,
        "#0105Fそ、そうかしら……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0000Fはは、まあ家族が見つかるまでの\x01",
            "保護者であるのは確かだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A13")

    label("loc_48DC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4979")

    #C0140
    ChrTalk(
        0x103,
        (
            "#0211Fわたしがママというのは\x01",
            "さすがに無理があるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000Fはは、まあ家族が見つかるまでの\x01",
            "保護者であるのは確かだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A13")

    label("loc_4979")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A13")

    #C0142
    ChrTalk(
        0x104,
        (
            "#0309Fお、その場合、\x01",
            "俺がパパでロイドがママか？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0003Fあのな……\x02\x03",

            "#0000Fま、家族が見つかるまでの\x01",
            "保護者であるのは確かだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A13")

    SetScenarioFlags(0xB0, 1)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x1)
    EventEnd(0x5)
    Return()

    # Function_10_43FF end

    def Function_11_4A32(): pass

    label("Function_11_4A32")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0xE, 0x2)

    #C0144
    ChrTalk(
        0x12,
        "お隣、いいですかぁ～？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x12,
        (
            "えっと、わたし達ぃ、\x01",
            "道に迷っちゃったんですけど～。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x13,
        (
            "この辺って悪い人が多くってぇ、\x01",
            "心細いっていうかぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x13,
        (
            "でもワジさんに会えて超ラッキー㈱\x01",
            "みたいな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xE,
        (
            "#0403F………………………………\x02\x03",

            "#0400Fへえ、そうなんだ。\x01",
            "……でも残念だなぁ。\x02\x03",

            "#0402F僕が一番\x01",
            "悪いヒトだったりするんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0149
    ChrTalk(
        0x101,
        "#0001F（ワジ……なんて奴だ………）\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#0306F（手馴れてんなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_11_4A32 end

    def Function_12_4C0A(): pass

    label("Function_12_4C0A")


    #C0151
    ChrTalk(
        0xE,
        (
            "#0402Fフフ、ご苦労様。\x02\x03",

            "ウチのメンバーだけじゃなく、\x01",
            "バイパーの下っ端たちにも\x01",
            "稽古を付けてくれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0003Fああ……\x01",
            "それはいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CAA():
        TurnDirection(0x0, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4CAA)

    def lambda_4CB7():
        TurnDirection(0x1, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4CB7)

    def lambda_4CC4():
        TurnDirection(0x2, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4CC4)

    def lambda_4CD1():
        TurnDirection(0x3, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4CD1)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    def lambda_4D45():
        TurnDirection(0x0, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D45)

    def lambda_4D52():
        TurnDirection(0x1, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4D52)

    def lambda_4D5F():
        TurnDirection(0x2, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4D5F)

    def lambda_4D6C():
        TurnDirection(0x3, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4D6C)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)

    #C0153
    ChrTalk(
        0x102,
        (
            "#0101F（あのアッバスって、\x01",
            "  一体どういう人なのかしら？）\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#0306F（なんか上手い具合に\x01",
            "  乗せられちまったんだが。）\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xE,
        (
            "#0404F（フフ、さてね。）\x02\x03",

            "#0400F（ゼムリア大陸の中東部あたりの\x01",
            "  出身らしいけど……）\x02\x03",

            "（まあ、僕みたいな変人を\x01",
            "  御輿に担いでいるくらいだから\x01",
            "  かなりの物好きなのは確かだよね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xE, 500)
    Sleep(300)

    #C0156
    ChrTalk(
        0x9,
        "聞こえているぞ、ワジ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4EF9")
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_4F00")

    label("loc_4EF9")

    OP_93(0x9, 0x0, 0x0)

    label("loc_4F00")

    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x8F, 7)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_12_4C0A end

    def Function_13_4F0B(): pass

    label("Function_13_4F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4FF7")

    #C0157
    ChrTalk(
        0xE,
        (
            "#0404Fそういえば、旧市街に住んでる\x01",
            "東方系のグラマーな子がいるよね。\x02\x03",

            "#0400Fほら、アルカンシェルの新作の\x01",
            "準主役に大抜擢されたっていう。\x02\x03",

            "#0402Fどう考えてもあの胸、\x01",
            "演技の邪魔になりそうなんだけど\x01",
            "フフ、大丈夫なのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5153")

    label("loc_4FF7")


    #C0158
    ChrTalk(
        0xE,
        (
            "#0405Fあれ……\x01",
            "切羽詰った顔をしてるね？\x02\x03",

            "#0400Fフフ、また何かの\x01",
            "トラブルに巻き込まれてるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0001F……まあ、色々とね。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xE,
        (
            "#0402Fどんな事件か知らないけど\x01",
            "まあ、精々頑張りなよ。\x02\x03",

            "アルカンシェルの新作は\x01",
            "僕も楽しみにしてるんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        "#0301F（結局知ってんじゃねえか。）\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        (
            "#0200F（カマをかけてる\x01",
            "  だけかもしれませんが……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_5153")

    Return()

    # Function_13_4F0B end

    def Function_14_5154(): pass

    label("Function_14_5154")

    SetChrSubChip(0xE, 0x2)

    #C0163
    ChrTalk(
        0xE,
        (
            "#0402Fへェ、その仕入れって\x01",
            "実は結構ヤバイんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xF,
        "ヤバくはないさ。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xF,
        (
            "アタシは捌ける品しか\x01",
            "取り扱わないんでねェ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_END)), "loc_527F")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#0001F（話が合ってるみたいだな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_52AB")

    label("loc_527F")


    #C0167
    ChrTalk(
        0x101,
        "#0006F（な、何の話をしてるんだ……？）\x02",
    )

    CloseMessageWindow()

    label("loc_52AB")

    SetScenarioFlags(0x0, 0)

    label("loc_52AE")

    Return()

    # Function_14_5154 end

    def Function_15_52AF(): pass

    label("Function_15_52AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52D8")
    Call(0, 55)
    Return()

    label("loc_52D8")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551C")

    #C0168
    ChrTalk(
        0x9,
        (
            "テスタメンツメンバーに\x01",
            "護身術を学ばせたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "警察流の制圧術とやら、\x01",
            "見せてやってはくれぬか？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【受ける】\x01",          # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54A3")
    TalkEnd(0x9)
    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    Fade(800)
    OP_68(1290, 1000, 9450, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0x9, 3060, 0, 8960, 270)
    SetChrPos(0x101, 700, 0, 9600, 90)
    SetChrPos(0x102, 560, 0, 8000, 90)
    SetChrPos(0x103, -990, 0, 8000, 90)
    SetChrPos(0x104, -990, 0, 9600, 90)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, 14390, 0, 7400, 178)
    SetChrPos(0xC, 14000, 0, 7400, 268)
    SetChrPos(0xA, 9250, 0, 4150, 225)
    SetChrPos(0xB, 5000, 0, 2000, 90)
    OP_0D()
    Call(0, 56)
    Return()

    label("loc_54A3")


    #C0170
    ChrTalk(
        0x101,
        (
            "#0001F……少し待ってくれ。\x01",
            "こちらも準備を整えたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "本日中は時間が空いている。\x01",
            "十分に準備を整えるがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_551C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_556F")

    #C0172
    ChrTalk(
        0x9,
        "こちらに異常は無い。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        (
            "お前たちは\x01",
            "調査とやらを続けるがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_556F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_561A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_55D7")

    #C0174
    ChrTalk(
        0x9,
        "……こちらのことはワジに任せろ。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "お前たちは\x01",
            "調査とやらを続けるがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5615")

    label("loc_55D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_END)), "loc_55F9")

    #C0176
    ChrTalk(
        0x9,
        "……何か用か？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5615")

    label("loc_55F9")


    #C0177
    ChrTalk(
        0x9,
        "ワジなら出かけている。\x02",
    )

    CloseMessageWindow()

    label("loc_5615")

    Jump("loc_5FD9")

    label("loc_561A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_563E")

    #C0178
    ChrTalk(
        0x9,
        "ワジに何か用か？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_563E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_569F")

    #C0179
    ChrTalk(
        0x9,
        (
            "先週からバイパーの様子が\x01",
            "おかしいようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_569F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_571C")

    #C0181
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        "注文があるなら言うがいい。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#0006F（この人も\x01",
            "  相変わらず無愛想だ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_571C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_58E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_57A1")

    #C0184
    ChrTalk(
        0x9,
        (
            "……ワジの判断なら問題ない。\x01",
            "全てワジの判断に任せろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_58E3")

    label("loc_57A1")


    #C0185
    ChrTalk(
        0x9,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "ワジを警察の揉め事に\x01",
            "巻き込まないで欲しいものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#0006Fミシュラムでのあれは\x01",
            "ワジから入ってきたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "……ワジの判断か…………\x01",
            "………………ならばいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0x101,
        (
            "#0006F（そういう割り切りされるのも\x01",
            "  微妙なんだが……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_58E3")

    Jump("loc_5FD9")

    label("loc_58E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5A17")

    #C0190
    ChrTalk(
        0x9,
        "ワジなら仕事で出かけている。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "用があるなら\x01",
            "別の機会にして貰おう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A12")

    #C0192
    ChrTalk(
        0x101,
        "#0005F仕事って……？\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        "お前たちに答える義理は無い。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x101,
        "#0006F（相変わらず無愛想だなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5A12")

    Jump("loc_5FD9")

    label("loc_5A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5A76")

    #C0195
    ChrTalk(
        0x9,
        (
            "記念祭の間は\x01",
            "スペシャルカクテルを出している。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        "良ければ注文するといい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_5A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5AC9")

    #C0197
    ChrTalk(
        0x9,
        "……本日は臨時休業だ。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "飲みたいのなら\x01",
            "また後日来るといい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_5AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5AFF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 1)), scpexpr(EXPR_END)), "loc_5AEF")
    Call(0, 18)
    Jump("loc_5AF2")

    label("loc_5AEF")

    Call(0, 17)

    label("loc_5AF2")

    Jump("loc_5AFA")

    label("loc_5AF7")

    Call(0, 18)

    label("loc_5AFA")

    Jump("loc_5FD9")

    label("loc_5AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5B35")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 1)), scpexpr(EXPR_END)), "loc_5B25")
    Call(0, 19)
    Jump("loc_5B28")

    label("loc_5B25")

    Call(0, 17)

    label("loc_5B28")

    Jump("loc_5B30")

    label("loc_5B2D")

    Call(0, 19)

    label("loc_5B30")

    Jump("loc_5FD9")

    label("loc_5B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5C60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5BC0")

    #C0199
    ChrTalk(
        0x9,
        (
            "マフィアどもを入り込ませぬため\x01",
            "旧市街の巡回を始める予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "我らとしても\x01",
            "以前のような事態は御免だからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C5B")

    label("loc_5BC0")


    #C0201
    ChrTalk(
        0x9,
        (
            "マフィア同士の抗争が激しくなれば\x01",
            "こちらにも影響があるかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        "……我らとしても手を打たねばな。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "手始めに旧市街の\x01",
            "巡回を始める予定だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5C5B")

    Jump("loc_5FD9")

    label("loc_5C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5D45")

    #C0204
    ChrTalk(
        0x9,
        (
            "近頃、不穏な事件が\x01",
            "増えているそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D40")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0206
    ChrTalk(
        0x9,
        "……いや、何でもない。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5D40")

    Jump("loc_5FD9")

    label("loc_5D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5DB9")

    #C0207
    ChrTalk(
        0x9,
        (
            "メンバーの事情に\x01",
            "立ち入るつもりは無い。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "テスタメンツへの参加は\x01",
            "おのおのの判断に任せている。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_5DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5E5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5E0C")

    #C0209
    ChrTalk(
        0x9,
        "アゼルの面倒は我々で見る。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        "余計な気遣いは無用だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E58")

    label("loc_5E0C")


    #C0211
    ChrTalk(
        0x9,
        (
            "アゼルはまだ\x01",
            "病院通いが必要だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        "長く意識が無かったのだからな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5E58")

    Jump("loc_5FD9")

    label("loc_5E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5F1A")

    #C0213
    ChrTalk(
        0x9,
        "……一応開業している。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "食事を取りたければ\x01",
            "そう言うがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F15")

    #C0215
    ChrTalk(
        0x101,
        "#0003Fど、どうも……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#0301F（つーかやっぱこの店は\x01",
            "  このデカイのが開いてんのか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5F15")

    Jump("loc_5FD9")

    label("loc_5F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5F77")

    #C0217
    ChrTalk(
        0x9,
        (
            "何か情報が判ったのなら\x01",
            "ワジに声を掛けろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        "我らに話をする必要はない。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FD9")

    label("loc_5F77")


    #C0219
    ChrTalk(
        0x9,
        (
            "……我らは病院からの\x01",
            "連絡を待っているところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "話が終わったのなら\x01",
            "さっさと行くがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FD9")

    TalkEnd(0x9)
    Return()

    # Function_15_52AF end

    def Function_16_5FDD(): pass

    label("Function_16_5FDD")

    Call(0, 15)
    Return()

    # Function_16_5FDD end

    def Function_17_5FE1(): pass

    label("Function_17_5FE1")


    #C0221
    ChrTalk(
        0x9,
        "これを持って行くがいい。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1D5, 1)

    #C0223
    ChrTalk(
        0x101,
        "#0005Fど、どうも……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x103,
        (
            "#0203F（さっきの仕事の報酬でしょうか。\x01",
            "  無愛想すぎてよく判りませんが。）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        "#0100F（まあ、受け取っておきましょうか。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 1)
    Return()

    # Function_17_5FE1 end

    def Function_18_60EA(): pass

    label("Function_18_60EA")


    #C0226
    ChrTalk(
        0x9,
        (
            "……さて。\x01",
            "記念祭に向けて\x01",
            "我らも準備を始めるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#0005F（……………………？\x01",
            "  このバーで\x01",
            "  セールでもやるつもりなのかな。）\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_60EA end

    def Function_19_6177(): pass

    label("Function_19_6177")


    #C0228
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        "ワジの時間を妨げるな。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_19_6177 end

    def Function_20_61B2(): pass

    label("Function_20_61B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_62D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_623F")

    #C0230
    ChrTalk(
        0xA,
        (
            "正々堂々と戦って勝つ。\x01",
            "テスタメンツは卑怯な真似は\x01",
            "しないものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "コホン……君達も\x01",
            "よく覚えておきたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62CC")

    label("loc_623F")


    #C0232
    ChrTalk(
        0xA,
        (
            "バイパーが弱っている今は\x01",
            "連中を叩き潰すチャンスだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        (
            "……だがまあ、ワジは\x01",
            "そんな事はしないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        "それでこそワジだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_62CC")

    Jump("loc_7350")

    label("loc_62D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6356")

    #C0235
    ChrTalk(
        0xA,
        (
            "ワジが朝から\x01",
            "真剣な顔をしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xA,
        (
            "……あんなワジを見るのは\x01",
            "僕としても初めてだよ。\x01",
            "何かあるんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_6356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_647A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_63A8")

    #C0237
    ChrTalk(
        0xA,
        (
            "ワジの許可さえあれば\x01",
            "あんな新米、伸してやるんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6475")

    label("loc_63A8")


    #C0238
    ChrTalk(
        0xA,
        (
            "コホン……バイパーの下っ端が\x01",
            "妙に粋がってるそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        (
            "あの少年なら僕らも知っている。\x01",
            "毎日のように絡んでくるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "……でもワジは\x01",
            "手を出すなと言うんだ。\x01",
            "くそっ、もどかしいな……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6475")

    Jump("loc_7350")

    label("loc_647A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6589")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_64CC")

    #C0241
    ChrTalk(
        0xA,
        (
            "さすがに今回ばかりは\x01",
            "警察も動かざるを得ないだろうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6584")

    label("loc_64CC")


    #C0242
    ChrTalk(
        0xA,
        (
            "マフィアどもが抗争したお陰で\x01",
            "親父が勤めてるウルスラ大にも\x01",
            "何人も運び込まれてきたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        "……デマじゃなさそうだな。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xA,
        (
            "フン、市街地のど真ん中で\x01",
            "大胆な事をするものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6584")

    Jump("loc_7350")

    label("loc_6589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_667F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_65E2")

    #C0245
    ChrTalk(
        0xA,
        (
            "バイパーの連中め……\x01",
            "最近また調子に\x01",
            "乗ってるんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_667A")

    label("loc_65E2")


    #C0246
    ChrTalk(
        0xA,
        (
            "昨日表の通りで\x01",
            "バイパーの連中に絡まれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xA,
        (
            "フン……相変わらず\x01",
            "品性の欠片も感じない連中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "さっさと叩き出して\x01",
            "しまいたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_667A")

    Jump("loc_7350")

    label("loc_667F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_6798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_671B")

    #C0249
    ChrTalk(
        0xA,
        (
            "全てはワジの意志だ。\x01",
            "ここはワジに任せるしかない。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "……ワ、ワジ、すまない。\x01",
            "ワジが帰ってくる前に\x01",
            "追い返そうとしたんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6793")

    label("loc_671B")


    #C0251
    ChrTalk(
        0xA,
        (
            "コ、コホン……\x01",
            "君たち、ワジの邪魔はするなよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "『全てはワジの意志だ』。\x01",
            "アッバスなら\x01",
            "きっとそう言うだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6793")

    Jump("loc_7350")

    label("loc_6798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6813")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_680B")

    #C0253
    ChrTalk(
        0xA,
        (
            "ワジもアッバスも\x01",
            "出かけてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xA,
        (
            "な、何とか僕らだけで\x01",
            "店を持たせないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680E")

    label("loc_680B")

    Call(0, 21)

    label("loc_680E")

    Jump("loc_7350")

    label("loc_6813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6951")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_68A5")

    #C0255
    ChrTalk(
        0xA,
        (
            "バイパーの連中とは\x01",
            "しばらく緊張関係が\x01",
            "続いていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xA,
        (
            "……まあ、記念祭だからな。\x01",
            "決着はしばらくお預けだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694C")

    label("loc_68A5")


    #C0257
    ChrTalk(
        0xA,
        (
            "マフィアの連中も\x01",
            "記念祭が近づくと\x01",
            "大人しくなったらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        (
            "バイパーとの緊張関係も\x01",
            "一旦はお開きだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        (
            "やれやれ、連中との決着は\x01",
            "しばらくお預けだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_694C")

    Jump("loc_7350")

    label("loc_6951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6987")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_697F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 2)), scpexpr(EXPR_END)), "loc_6977")
    Call(0, 23)
    Jump("loc_697A")

    label("loc_6977")

    Call(0, 22)

    label("loc_697A")

    Jump("loc_6982")

    label("loc_697F")

    Call(0, 23)

    label("loc_6982")

    Jump("loc_7350")

    label("loc_6987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6B27")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 2)), scpexpr(EXPR_END)), "loc_6A37")

    #C0260
    ChrTalk(
        0xA,
        (
            "近頃ルバーチェの連中が\x01",
            "コソコソしてるらしいからね。\x01",
            "僕たちも見回りを強化しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xA,
        (
            "フン……今度見かけたら\x01",
            "ただじゃ置かないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A3A")

    label("loc_6A37")

    Call(0, 22)

    label("loc_6A3A")

    Jump("loc_6B22")

    label("loc_6A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6A99")

    #C0262
    ChrTalk(
        0xA,
        (
            "ワジはただでさえ\x01",
            "夜の仕事が多いんだ。\x01",
            "体には気を付けて欲しいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B22")

    label("loc_6A99")


    #C0263
    ChrTalk(
        0xA,
        (
            "ワジはまた徹夜で\x01",
            "飲んでいたみたいだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xA,
        (
            "その、勿論ワジに\x01",
            "意見するつもりは無いんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xA,
        "体には気を付けて欲しいものだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6B22")

    Jump("loc_7350")

    label("loc_6B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6BA9")

    #C0266
    ChrTalk(
        0xA,
        (
            "歓楽街や裏通りの辺りでも\x01",
            "事件が頻発しているそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "フン……これは\x01",
            "君たち警察の怠慢じゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_6BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6C31")

    #C0268
    ChrTalk(
        0xA,
        (
            "バイパーの連中とは\x01",
            "いずれ片を付ける。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "だが記念祭前は休戦だな。\x01",
            "警察や役人がいては\x01",
            "興がそがれてしまう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CD3")

    label("loc_6C31")


    #C0270
    ChrTalk(
        0xA,
        (
            "ここの所、バイパーとは\x01",
            "まともな喧嘩一つしていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "記念祭前で警察や役人が\x01",
            "ウロウロしているせいだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xA,
        (
            "あれじゃ興をそがれてしまう。\x01",
            "まったく……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6CD3")

    Jump("loc_7350")

    label("loc_6CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6D3C")

    #C0273
    ChrTalk(
        0xA,
        "それはそうと……\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "アゼル、まさか\x01",
            "辞めてしまうんじゃないだろうな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DC0")

    label("loc_6D3C")


    #C0275
    ChrTalk(
        0xA,
        (
            "さっき広場の方に\x01",
            "バイパーの連中が来ていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "連中、また調子に\x01",
            "乗り出したんじゃないだろうな。\x01",
            "まったく目障りな連中だ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6DC0")

    Jump("loc_7350")

    label("loc_6DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6F3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6E44")

    #C0277
    ChrTalk(
        0xA,
        (
            "僕は武術をたしなんでいてね、\x01",
            "素手の格闘にも自信がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xA,
        (
            "……もっとも\x01",
            "ワジほどじゃないけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F36")

    label("loc_6E44")


    #C0279
    ChrTalk(
        0xA,
        (
            "最近バイパーの連中と\x01",
            "やり合うことも無くなったな。\x01",
            "退屈を覚えるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xA,
        (
            "腕がなまってもいけない、\x01",
            "スリングショットの練習でも\x01",
            "しておくとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xA,
        (
            "ちなみに僕は幼少の頃から\x01",
            "武術をたしなんでいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xA,
        "素手の格闘にも自信があるよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6F36")

    Jump("loc_7350")

    label("loc_6F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_709E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6FCC")

    #C0283
    ChrTalk(
        0xA,
        (
            "ようやくアゼルが退院した。\x01",
            "最後の胸の支えが取れた気分だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xA,
        (
            "あとはバイパーの連中と\x01",
            "白黒付けられればいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7099")

    label("loc_6FCC")


    #C0285
    ChrTalk(
        0xA,
        (
            "ようやくアゼルが退院してね。\x01",
            "僕らも胸を撫で下ろしている所さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xA,
        (
            "……一応礼は言っておくが\x01",
            "思い上がらないでくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xA,
        (
            "我らテスタメンツはワジの手足。\x01",
            "命令できるのは\x01",
            "ワジだけなんだからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_7099")

    Jump("loc_7350")

    label("loc_709E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_711C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 3)), scpexpr(EXPR_END)), "loc_7114")

    #C0288
    ChrTalk(
        0xA,
        "病院にいるアゼルが心配だな。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xA,
        (
            "親父のコネもあるし、明日\x01",
            "直接様子を見に行ってみるか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7117")

    label("loc_7114")

    Call(0, 24)

    label("loc_7117")

    Jump("loc_7350")

    label("loc_711C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_719F")

    #C0290
    ChrTalk(
        0xA,
        (
            "倒れていたアゼルは\x01",
            "打撲と細かい裂傷だらけだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xA,
        (
            "あれはバイパーの\x01",
            "釘付き棍棒に間違いない！\x01",
            "……くそっ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7350")

    label("loc_719F")


    #C0292
    ChrTalk(
        0xA,
        (
            "君たちは知らないだろうが\x01",
            "僕らはあまり単独行動をとらない。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xA,
        (
            "だがあの日、アゼルは\x01",
            "久々に家に帰る所でね……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xA,
        (
            "……僕たちが駆けつけたとき\x01",
            "倒れていたアゼルは\x01",
            "打撲と細かい裂傷だらけだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xA,
        (
            "あれはあの低脳連中の\x01",
            "釘付き棍棒に間違いない！\x01",
            "……くそっ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_734D")

    #C0296
    ChrTalk(
        0x101,
        (
            "#0003Fそうか……\x01",
            "話をしてくれて助かる。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xA,
        (
            "フ、フン……ワジの許しが\x01",
            "あったから話したまでだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xA,
        (
            "能無しの警察が、いい気に\x01",
            "ならないでくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 2)

    label("loc_734D")

    SetScenarioFlags(0x0, 2)

    label("loc_7350")

    TalkEnd(0xFE)
    Return()

    # Function_20_61B2 end

    def Function_21_7354(): pass

    label("Function_21_7354")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0299
    ChrTalk(
        0xB,
        "オ、オレは、接客は、苦手だ。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        "ここはキーンツに任せる。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xA,
        (
            "ぼ、僕も\x01",
            "得意というわけじゃないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xA,
        "分かった、ここは引き受けよう。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_21_7354 end

    def Function_22_73FC(): pass

    label("Function_22_73FC")


    #C0303
    ChrTalk(
        0xA,
        (
            "実は僕も秘密の特訓をしていてね。\x01",
            "今日の実戦は参考になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xA,
        (
            "……感謝はしないが、\x01",
            "礼は言っておく。\x01",
            "そ、その、サンキュー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 2)
    Return()

    # Function_22_73FC end

    def Function_23_7485(): pass

    label("Function_23_7485")


    #C0305
    ChrTalk(
        0xA,
        (
            "まさかバイパーの連中も\x01",
            "巡回を始めていたなんてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        (
            "フン、道理で\x01",
            "近頃よく見かけるわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xA,
        (
            "ワジも今すぐ\x01",
            "抗争ってつもりは無いみたいだが\x01",
            "正直、向こうの出方次第だな。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_23_7485 end

    def Function_24_7538(): pass

    label("Function_24_7538")


    #C0308
    ChrTalk(
        0xA,
        (
            "……こんな事なら……\x01",
            "親父の医学書でも\x01",
            "読んでおくべきだったな……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x103,
        "#0205F……医学書、ですか？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xA, 0x0, 500)

    #C0310
    ChrTalk(
        0xA,
        "な、なんだ、また君たちか。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xA,
        (
            "フン……悪いかい？\x01",
            "人には色々と事情があるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xA)

    #C0312
    ChrTalk(
        0xA,
        (
            "闇討ちにあったアゼルの奴は\x01",
            "ここに運び込んで介抱したんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xA,
        (
            "意識が戻らなくてね、\x01",
            "明け方を待ってから\x01",
            "救急車を呼んだというわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xA,
        (
            "……親父のことは大嫌いだが、\x01",
            "応急手当くらいは\x01",
            "身に付けておくべきだったかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#0003Fそうだったのか……\x01",
            "確かにそれは心配だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xA,
        (
            "ああ、だが\x01",
            "アゼルを乗せた救急車は\x01",
            "何故か発車しなくてね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_792E")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0317
    ChrTalk(
        0x101,
        (
            "#0005Fああ、そうか。\x01",
            "サーベルバイパーの子と\x01",
            "同じ救急車になったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#0203F良かったですね。\x01",
            "救急車が二度手間に\x01",
            "ならずに済んで……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0319
    ChrTalk(
        0xA,
        (
            "#4Sよ、良かったわけがないだろう！？\x01",
            "バイパーの連中と一緒なんだぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B31")

    label("loc_792E")

    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0320
    ChrTalk(
        0x102,
        "#0105Fそれは……どういうこと？\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xA,
        (
            "旧市街の方から\x01",
            "もう一人怪我人が来たのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xA,
        (
            "フン、あのバイパーの連中だよ。\x01",
            "大怪我の仲間だとか言っていたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xA,
        (
            "２人は同じ救急車で\x01",
            "運ばれていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#0003Fそ、そうか。\x01",
            "両方とも同じ夜に襲われて……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#0301Fなんともまあ、\x01",
            "タイミングのいいことだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0326
    ChrTalk(
        0xA,
        (
            "#4Sタイミングは\x01",
            "悪かったに決まっているだろう！？\x01",
            "バイパーの連中と一緒なんだぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 5)

    label("loc_7B31")


    #C0327
    ChrTalk(
        0xA,
        "#2S……コ、コホン、やれやれ……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xA,
        (
            "病院にいるアゼルが心配だな。\x01",
            "親父のコネもあるし、明日\x01",
            "直接様子を見に行ってみるか……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x4E, 3)
    Return()

    # Function_24_7538 end

    def Function_25_7BB9(): pass

    label("Function_25_7BB9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7CB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7C35")

    #C0329
    ChrTalk(
        0xB,
        (
            "バイパーに奇襲をかける作戦は\x01",
            "ワジに却下されたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xB,
        (
            "赤マムシども……\x01",
            "い、命拾いしたな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CB1")

    label("loc_7C35")


    #C0331
    ChrTalk(
        0xB,
        (
            "バ、バイパーの連中には\x01",
            "恨みつらみもあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        "ワ、ワジがそう言うなら仕方ない。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        "今回は、か、勘弁してやる。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_7CB1")

    Jump("loc_8D0B")

    label("loc_7CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7D08")

    #C0334
    ChrTalk(
        0xB,
        "ワジは最近、が、外出が多い。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xB,
        "な、何か調べているみたいだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D0B")

    label("loc_7D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_7E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7D91")

    #C0336
    ChrTalk(
        0xB,
        (
            "バ、バイパーが、はでに\x01",
            "内輪もめしているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xB,
        (
            "フン……赤マムシどもなど、\x01",
            "心配してやる事は、ないがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E35")

    label("loc_7D91")


    #C0338
    ChrTalk(
        0xB,
        (
            "さ、さっき様子を見てきたが、\x01",
            "本当らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xB,
        (
            "バイパーの幹部がやられて、\x01",
            "病院に、行っているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xB,
        (
            "い、意味が判らないな。\x01",
            "さすが、低脳なバイパーだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_7E35")

    Jump("loc_8D0B")

    label("loc_7E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7E8E")

    #C0341
    ChrTalk(
        0xB,
        (
            "マ、マフィアども……\x01",
            "旧市街に顔を出したら、許さないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F05")

    label("loc_7E8E")


    #C0342
    ChrTalk(
        0xB,
        (
            "マ、マフィアども……\x01",
            "またうろうろしているのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xB,
        (
            "連中には前に世話になった。\x01",
            "見かけたら、つ、捕まえてやる。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_7F05")

    Jump("loc_8D0B")

    label("loc_7F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7F95")

    #C0344
    ChrTalk(
        0xB,
        (
            "あ、あの青髪の赤マムシ……\x01",
            "最近よく絡んでくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xB,
        (
            "しかも、よ、様子が変だ。\x01",
            "前はもっとおどおどした奴だった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8012")

    label("loc_7F95")


    #C0346
    ChrTalk(
        0xB,
        (
            "あ、あの青い髪の赤マムシは\x01",
            "普通じゃないものを、感じる。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xB,
        (
            "そ、そもそもあいつ、\x01",
            "たしか見張りをしていた下っ端だぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_8012")

    Jump("loc_8D0B")

    label("loc_8017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_80B5")

    #C0348
    ChrTalk(
        0xB,
        (
            "キーンツのやつは、\x01",
            "お、親父さんに会いに行っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xB,
        (
            "あ、あいつの親父さんは\x01",
            "ウルスラ大の医者だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xB,
        "そりは、あ、合わないらしいがな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D0B")

    label("loc_80B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_81F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8134")

    #C0351
    ChrTalk(
        0xB,
        (
            "リャンのお陰で、\x01",
            "店もなんとか持ちそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xB,
        (
            "へ、変な客が、ワジに\x01",
            "たかっているのが気になるがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81EF")

    label("loc_8134")


    #C0353
    ChrTalk(
        0xB,
        (
            "リャンに、カクテル作りの\x01",
            "才能があるとは、知らなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xB,
        (
            "ア、アッバスのカクテルも美味いが、\x01",
            "リャンも、すごい。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        (
            "そういえば、\x01",
            "リャンは目立たないが\x01",
            "手先が器用だったからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_81EF")

    Jump("loc_8D0B")

    label("loc_81F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_825E")
    OP_4B(0x12, 0xFF)

    #C0356
    ChrTalk(
        0xB,
        (
            "ビリヤードをやりたいなら、\x01",
            "オ、オレに言え。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xB,
        "ルールを教えてやる。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_8261")

    label("loc_825E")

    Call(0, 21)

    label("loc_8261")

    Jump("loc_8D0B")

    label("loc_8266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_82D1")

    #C0358
    ChrTalk(
        0xB,
        "き、今日は、みんなで出かける。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xB,
        (
            "ワジは忙しいから、\x01",
            "昨日は、時間が取れなかったんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D0B")

    label("loc_82D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8307")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_82FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 4)), scpexpr(EXPR_END)), "loc_82F7")
    Call(0, 27)
    Jump("loc_82FA")

    label("loc_82F7")

    Call(0, 26)

    label("loc_82FA")

    Jump("loc_8302")

    label("loc_82FF")

    Call(0, 27)

    label("loc_8302")

    Jump("loc_8D0B")

    label("loc_8307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_844E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_83DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 4)), scpexpr(EXPR_END)), "loc_83D6")

    #C0360
    ChrTalk(
        0xB,
        (
            "ご、護身術さえ身につければ、\x01",
            "マフィアも怖くない。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xB,
        (
            "見つけたら、この旧市街から\x01",
            "た、叩き出してやる。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83CE")

    #C0362
    ChrTalk(
        0x101,
        (
            "#0006Fあまり無茶な真似は\x01",
            "しないでくれよ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83CE")

    SetScenarioFlags(0x0, 3)
    Jump("loc_83D9")

    label("loc_83D6")

    Call(0, 26)

    label("loc_83D9")

    Jump("loc_8449")

    label("loc_83DE")


    #C0363
    ChrTalk(
        0xB,
        (
            "あ、あの客は、\x01",
            "週に一度ほど、必ずくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xB,
        "ワジと、話が合うらしい。\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xB,
        "や、やはりワジは大人だな。\x02",
    )

    CloseMessageWindow()

    label("loc_8449")

    Jump("loc_8D0B")

    label("loc_844E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_86DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 3)), scpexpr(EXPR_END)), "loc_84F2")

    #C0366
    ChrTalk(
        0xB,
        (
            "旧市街の近くには、\x01",
            "そ、倉庫街や廃墟も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xB,
        (
            "マ、マフィアの連中、\x01",
            "最近その辺りで\x01",
            "抗争をやっているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xB,
        "は、はた迷惑な話だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_86D5")

    label("loc_84F2")


    #C0369
    ChrTalk(
        0xB,
        (
            "旧市街の近くには、\x01",
            "そ、倉庫街や廃墟も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xB,
        (
            "マ、マフィアの連中、\x01",
            "最近その辺りで\x01",
            "抗争をやっているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xB,
        "は、はた迷惑な話だ。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#0003Fなるほどな……\x02\x03",

            "#0001Fルバーチェと黒月の抗争、\x01",
            "こっちにも影響があるって事か。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x104,
        (
            "#0306Fつーか、お前らの抗争だって\x01",
            "はた迷惑なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xB,
        (
            "オレたちの抗争は、\x01",
            "れ、連中とは違う。\x01",
            "必要なものだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0375
    ChrTalk(
        0x102,
        "#0106Fそうは思えないけど……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 3)

    label("loc_86D5")

    Jump("loc_8D0B")

    label("loc_86DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8749")

    #C0376
    ChrTalk(
        0xB,
        (
            "き、旧市街に来る役人は、\x01",
            "偽善者ばかりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xB,
        (
            "ああいう手合いは\x01",
            "し、信用ならない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8851")

    label("loc_8749")


    #C0378
    ChrTalk(
        0xB,
        (
            "記念祭が近づくと、\x01",
            "ま、毎年、役人がやってくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xB,
        (
            "営業許可を確認したり、\x01",
            "観光客への注意をしたり、する。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xB,
        (
            "だが役人は、い、いつも適当だ。\x01",
            "実際には確認してなくても、\x01",
            "確認したことにしている。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xB,
        (
            "フ、フン……偽善者め。\x01",
            "ああいう手合いは、気に入らない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_8851")

    Jump("loc_8D0B")

    label("loc_8856")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_88E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_888F")

    #C0382
    ChrTalk(
        0xB,
        "アゼル、どうするんだろうな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_88E4")

    label("loc_888F")


    #C0383
    ChrTalk(
        0xB,
        (
            "ま、まさか\x01",
            "乗り込んでくるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xB,
        (
            "お、驚いた。\x01",
            "アゼルの姉は、大胆だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_88E4")

    Jump("loc_8D0B")

    label("loc_88E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C9")

    #C0385
    ChrTalk(
        0xFE,
        (
            "さっき東通りを歩いていたら、\x01",
            "お、女の人に呼び止められたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "なんでもアゼルの姉だとかで、\x01",
            "アゼルの様子を、色々聞かれた。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "アゼルは入院していたからな……\x01",
            "ず、随分心配そうにしていた。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8A4C")

    label("loc_89C9")


    #C0388
    ChrTalk(
        0xFE,
        (
            "東通りで、アゼルの姉に\x01",
            "話を聞かれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "そ、そういえば去り際に\x01",
            "きつい目で睨まれた気がするが……\x01",
            "……き、気のせいか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A4C")

    Jump("loc_8D0B")

    label("loc_8A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8AD4")

    #C0390
    ChrTalk(
        0xB,
        (
            "け、警察の犬なんて、\x01",
            "まだまだ信用できないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xB,
        (
            "ここに来るのはいいが、\x01",
            "か、勝手な真似は許さないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B97")

    label("loc_8AD4")


    #C0392
    ChrTalk(
        0xB,
        (
            "け、警察の犬……\x01",
            "また、き、来ていたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xB,
        (
            "た、確かにお前たちには\x01",
            "世話になったが、\x01",
            "このトリニティはワジの聖域だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xB,
        (
            "ここじゃワジに従うのがルールだ。\x01",
            "わ、分かってるんだろうな！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_8B97")

    Jump("loc_8D0B")

    label("loc_8B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8C35")

    #C0395
    ChrTalk(
        0xB,
        (
            "バ、バイパーの連中……\x01",
            "この前の抗争で押され気味だったのを\x01",
            "根に持っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xB,
        (
            "ひ、卑怯な奴らめ。\x01",
            "犯人は連中以外に考えられない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D0B")

    label("loc_8C35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8C9C")

    #C0397
    ChrTalk(
        0xB,
        (
            "け、警察の犬なんかに\x01",
            "協力する気はさらさら、ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xB,
        "さ、さっさと消えたらどうだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D0B")

    label("loc_8C9C")


    #C0399
    ChrTalk(
        0xB,
        (
            "い、いいか。\x01",
            "このトリニティはワジの聖域だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xB,
        (
            "余計な真似をしたら、\x01",
            "そ、それこそただじゃ置かないぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_8D0B")

    TalkEnd(0xFE)
    Return()

    # Function_25_7BB9 end

    def Function_26_8D0F(): pass

    label("Function_26_8D0F")


    #C0401
    ChrTalk(
        0xB,
        (
            "今日稽古をすることは、\x01",
            "じ、事前に決めていたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xB,
        (
            "だ、だが直前まで\x01",
            "そんな素振りはなかっただろう。\x01",
            "ふふ、お、驚いたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x103,
        "#0200Fええ、まあ……\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x104,
        "#0306F驚いたっつーかなんつーか。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 4)
    Return()

    # Function_26_8D0F end

    def Function_27_8DD4(): pass

    label("Function_27_8DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8E52")

    #C0405
    ChrTalk(
        0xB,
        (
            "マフィアも嫌いだが、\x01",
            "れ、連中も目障りだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xB,
        (
            "ち、近頃大目に見ていたら\x01",
            "調子に乗ったんじゃないだろうな！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F06")

    label("loc_8E52")


    #C0407
    ChrTalk(
        0xB,
        (
            "さ、最近、赤マムシどもは\x01",
            "旧市街の巡回をしているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xB,
        (
            "め、目障りなやつだだ。\x01",
            "昨日は、い、一日巡回をしただけで\x01",
            "３回も出くわした。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xB,
        "……さ、さすがに目障りすぎだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_8F06")

    Return()

    # Function_27_8DD4 end

    def Function_28_8F07(): pass

    label("Function_28_8F07")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_8F89")

    #C0410
    ChrTalk(
        0xC,
        "喧嘩なんてない方がいいんだ。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xC,
        (
            "でも仲間のためなら\x01",
            "どんな事だってできる……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xC,
        "僕たち似た者同士だもの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D5D")

    label("loc_8F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8FEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8FE2")
    OP_4B(0xC, 0xFF)

    #C0413
    ChrTalk(
        0xC,
        "アゼルも練習すれば上手くなるよ。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xC,
        "……頑張って。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_8FE5")

    label("loc_8FE2")

    Call(0, 30)

    label("loc_8FE5")

    Jump("loc_9D5D")

    label("loc_8FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_90C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9040")

    #C0415
    ChrTalk(
        0xC,
        (
            "バイパーは嫌いだけど……\x01",
            "すさんだ噂なんて聞きたくないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90BF")

    label("loc_9040")


    #C0416
    ChrTalk(
        0xC,
        (
            "さっき噂を聞いたんだ……\x01",
            "バイパーが仲間内でもめてるって。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xC,
        (
            "バイパーの連中は嫌いだけど、\x01",
            "何だか気になるんだよね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_90BF")

    Jump("loc_9D5D")

    label("loc_90C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_91AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9137")

    #C0418
    ChrTalk(
        0xC,
        (
            "アゼルは家族が心配で\x01",
            "家に戻ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xC,
        (
            "……アゼル、すっかり\x01",
            "素直になれたんだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91A9")

    label("loc_9137")


    #C0420
    ChrTalk(
        0xC,
        (
            "港湾公園で事件があったらしいんだ。\x01",
            "アゼルは家族の所に戻ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xC,
        "……アゼルの家、港湾区に近いもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_91A9")

    Jump("loc_9D5D")

    label("loc_91AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_928E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9207")

    #C0422
    ChrTalk(
        0xC,
        "旧市街は何も変わらないよね。\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xC,
        "……だから好きなんだけど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9289")

    label("loc_9207")


    #C0424
    ChrTalk(
        0xC,
        (
            "最近街の方は\x01",
            "景気がいいみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xC,
        (
            "会社が進出とか\x01",
            "そんな噂ばかり聞くよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xC,
        (
            "旧市街の貧しさは\x01",
            "相変わらずだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9289")

    Jump("loc_9D5D")

    label("loc_928E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_92F6")

    #C0427
    ChrTalk(
        0xC,
        (
            "今日は街も\x01",
            "のんびりしてるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xC,
        (
            "こんな日は散歩するのも\x01",
            "いいかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D5D")

    label("loc_92F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_93E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9362")

    #C0429
    ChrTalk(
        0xC,
        "今日も店を手伝ってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xC,
        (
            "いらっしゃいませ。\x01",
            "注文ならアッバスに言ってね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93E1")

    label("loc_9362")


    #C0431
    ChrTalk(
        0xC,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xC,
        (
            "……今日もみんな\x01",
            "出かけちゃったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "仕方がないから\x01",
            "僕がお客さんの相手をしてるんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_93E1")

    Jump("loc_9D5D")

    label("loc_93E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_94A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_945A")

    #C0434
    ChrTalk(
        0xC,
        "ちなみにワジは怒ると怖いんだ。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xC,
        (
            "……大抵はベタベタしてくる\x01",
            "女の人に対してだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94A2")

    label("loc_945A")


    #C0436
    ChrTalk(
        0xC,
        "２人とも可哀相に……\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xC,
        (
            "きっと後で\x01",
            "こっぴどく振られちゃうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_94A2")

    Jump("loc_9D5D")

    label("loc_94A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_94FC")

    #C0438
    ChrTalk(
        0xC,
        "アッバスは出かけちゃってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xC,
        "注文は僕がとるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9542")

    label("loc_94FC")


    #C0440
    ChrTalk(
        0xC,
        "注文は何？\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xC,
        (
            "アッバスがいないから\x01",
            "今日は僕が注文をとるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9542")

    Jump("loc_9D5D")

    label("loc_9547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_95C7")

    #C0442
    ChrTalk(
        0xC,
        (
            "家に帰るより\x01",
            "仲間と居る方がずっと楽なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xC,
        (
            "……世の中には\x01",
            "僕みたいな人も\x01",
            "いると思うんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9663")

    label("loc_95C7")


    #C0444
    ChrTalk(
        0xC,
        (
            "記念祭は家族で\x01",
            "回る人が多いみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xC,
        "でも僕、両親はいないんだ。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xC,
        (
            "家には意地悪な\x01",
            "叔父さんと叔母さんがいるし……\x01",
            "２度と帰りたくないんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9663")

    Jump("loc_9D5D")

    label("loc_9668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_96D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_96C8")

    #C0447
    ChrTalk(
        0xC,
        "あ……警察の人。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xC,
        (
            "お仕事ご苦労さま。\x01",
            "人が多いから気を付けてね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96CB")

    label("loc_96C8")

    Call(0, 31)

    label("loc_96CB")

    Jump("loc_9D5D")

    label("loc_96D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9706")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 5)), scpexpr(EXPR_END)), "loc_96F6")
    Call(0, 33)
    Jump("loc_96F9")

    label("loc_96F6")

    Call(0, 32)

    label("loc_96F9")

    Jump("loc_9701")

    label("loc_96FE")

    Call(0, 33)

    label("loc_9701")

    Jump("loc_9D5D")

    label("loc_9706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_97C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9778")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 5)), scpexpr(EXPR_END)), "loc_9770")

    #C0449
    ChrTalk(
        0xC,
        (
            "アゼルがカウンターに入ると\x01",
            "ビリヤードの相手がいなくて寂しいな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9773")

    label("loc_9770")

    Call(0, 32)

    label("loc_9773")

    Jump("loc_97BC")

    label("loc_9778")


    #C0450
    ChrTalk(
        0xC,
        "君たちって、今日は時間あるの？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xC,
        "……いや、何でもないんだ。\x02",
    )

    CloseMessageWindow()

    label("loc_97BC")

    Jump("loc_9D5D")

    label("loc_97C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_98C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9840")

    #C0452
    ChrTalk(
        0xC,
        (
            "僕たちも旧市街の\x01",
            "見回りを始めるつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        (
            "……安心して。\x01",
            "もう絶対あんな事にはしないから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98BB")

    label("loc_9840")


    #C0454
    ChrTalk(
        0xC,
        (
            "僕も最近、裏路地の方で\x01",
            "マフィアを見かけたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xC,
        (
            "……前にアゼルを闇討ちした連中だ、\x01",
            "ついカチンと来ちゃったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_98BB")

    Jump("loc_9D5D")

    label("loc_98C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9979")

    #C0456
    ChrTalk(
        0xFE,
        (
            "アゼルが働きだして\x01",
            "そろそろ一週間だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "僕も手伝いたいけど、手を出して\x01",
            "ほしくないって言われてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        (
            "……アゼル、何だかちょっと\x01",
            "大人になった気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D5D")

    label("loc_9979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_99F7")

    #C0459
    ChrTalk(
        0xC,
        (
            "アゼル、本当は\x01",
            "お姉さんのことも好きなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xC,
        (
            "でも……日頃苦労を掛けてるから\x01",
            "きっと居心地が悪いんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D5D")

    label("loc_99F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9A68")

    #C0461
    ChrTalk(
        0xC,
        (
            "僕らは困ったときは\x01",
            "みんなで助け合うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "……それが\x01",
            "テスタメンツのいい所だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9ACF")

    label("loc_9A68")


    #C0463
    ChrTalk(
        0xC,
        (
            "アゼルはもうしばらく\x01",
            "病院通いが必要なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xC,
        (
            "……心配しないで。\x01",
            "診療代はみんなで出すから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9ACF")

    Jump("loc_9D5D")

    label("loc_9AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9C37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9B67")

    #C0465
    ChrTalk(
        0xC,
        (
            "アゼルは打ち所が悪かったら\x01",
            "死んでいたかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xC,
        (
            "マフィアの連中は許せないな。\x01",
            "僕らも今後は気を付けておくよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C32")

    label("loc_9B67")


    #C0467
    ChrTalk(
        0xC,
        "アゼルが無事に退院したんだ。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "その……\x01",
            "遅くなったけどありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xC,
        (
            "アゼルは打ち所が悪かったら\x01",
            "死んでいたかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xC,
        (
            "……そう考えると\x01",
            "仇を取ってくれた君たちには\x01",
            "感謝しなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9C32")

    Jump("loc_9D5D")

    label("loc_9C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_9C98")

    #C0471
    ChrTalk(
        0xC,
        "アゼル……具合はどうなのかな。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        (
            "そろそろ意識が\x01",
            "戻ってるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D5D")

    label("loc_9C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9CDC")

    #C0473
    ChrTalk(
        0xC,
        "仲間の仇は僕らの手で討つ。\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xC,
        "邪魔しないでよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D5D")

    label("loc_9CDC")


    #C0475
    ChrTalk(
        0xC,
        (
            "襲われたのは\x01",
            "アゼルって奴だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xC,
        "……仲間の仇は僕らの手で討つ。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xC,
        (
            "ワジには勝手に動くなって\x01",
            "止められていたけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9D5D")

    TalkEnd(0xC)
    Return()

    # Function_28_8F07 end

    def Function_29_9D61(): pass

    label("Function_29_9D61")

    Call(0, 28)
    Return()

    # Function_29_9D61 end

    def Function_30_9D65(): pass

    label("Function_30_9D65")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0478
    ChrTalk(
        0xD,
        (
            "……リャンって、\x01",
            "カクテル作り上手いんだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xD,
        (
            "そういえば手先が器用で、\x01",
            "ビリヤードも一番強かったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        "アゼルも練習すれば上手くなるよ。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xC,
        "……頑張って。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xD,
        "う、うん。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_30_9D65 end

    def Function_31_9E38(): pass

    label("Function_31_9E38")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0483
    ChrTalk(
        0xC,
        "アゼル、家族の方はいいの？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xC,
        "別に遠慮しなくてもいいんだよ？\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xD,
        (
            "ああ、記念祭の後半は\x01",
            "姉さんと過ごす予定だからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xD,
        "今日はみんなと楽しみたいんだ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_31_9E38 end

    def Function_32_9EF5(): pass

    label("Function_32_9EF5")


    #C0487
    ChrTalk(
        0xC,
        (
            "さっきはありがとう。\x01",
            "戦い方の参考になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xC,
        (
            "バイパーとの喧嘩にも\x01",
            "応用できるといいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0489
    ChrTalk(
        0x101,
        "#0006Fお願いだから応用しないでくれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 5)
    Return()

    # Function_32_9EF5 end

    def Function_33_9FF0(): pass

    label("Function_33_9FF0")


    #C0490
    ChrTalk(
        0xC,
        (
            "サーベルバイパーのヴァルドは\x01",
            "ずっと旧市街を仕切ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xC,
        (
            "でも２年前にワジが現れてね、\x01",
            "いちゃもんをつけたヴァルドは\x01",
            "あっという間に倒されちゃったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        (
            "それ以来、ヴァルドに従わない\x01",
            "『テスタメンツ』が出来たってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xC,
        "……ワジはとっても強いんだよね。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_33_9FF0 end

    def Function_34_A101(): pass

    label("Function_34_A101")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A1EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A18F")

    #C0494
    ChrTalk(
        0xD,
        (
            "仕事にも慣れてきたし、\x01",
            "喧嘩に興味なくなってきたんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xD,
        (
            "……ワジが抗争を止めてくれて\x01",
            "正直ほっとしたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1E9")

    label("loc_A18F")


    #C0496
    ChrTalk(
        0xD,
        (
            "バイパーのヴァルドが\x01",
            "弱ってるって本当なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xD,
        "な、何だか想像できないなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_A1E9")

    Jump("loc_AC82")

    label("loc_A1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A25C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A254")

    #C0498
    ChrTalk(
        0xD,
        (
            "リャンって器用だし\x01",
            "何でもこなせるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xD,
        "いい友達がいて助かるぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A257")

    label("loc_A254")

    Call(0, 30)

    label("loc_A257")

    Jump("loc_AC82")

    label("loc_A25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A32A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A2C0")

    #C0500
    ChrTalk(
        0xD,
        (
            "ワジは夜の仕事で\x01",
            "かなり稼いでるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xD,
        "何ていうか、ワジだもんな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A325")

    label("loc_A2C0")


    #C0502
    ChrTalk(
        0xD,
        (
            "ワジは週に２、３日は\x01",
            "夜の仕事が入ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xD,
        (
            "……ああ見えて\x01",
            "かなり稼いでるみたいだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_A325")

    Jump("loc_AC82")

    label("loc_A32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A3A2")

    #C0504
    ChrTalk(
        0xD,
        "店の仕事にも大分慣れたよ。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xD,
        (
            "……やっぱ働いて\x01",
            "稼ぐって気持ちいいよな。\x01",
            "みんなにも感謝しなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC82")

    label("loc_A3A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A400")

    #C0506
    ChrTalk(
        0xD,
        (
            "これってきっと\x01",
            "ワジ目当ての客だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xD,
        "ワジは目立つからなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A46C")

    label("loc_A400")


    #C0508
    ChrTalk(
        0xD,
        "客が増えてきたな……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xD,
        "やっぱり昨日のあれのせいかな。\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xD,
        (
            "結構観客やらなんやらも\x01",
            "いたもんなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_A46C")

    Jump("loc_AC82")

    label("loc_A471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A4FC")

    #C0511
    ChrTalk(
        0xD,
        (
            "記念祭の後半は\x01",
            "家族で過ごす予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xD,
        (
            "テスタメンツはその辺は自由だし、\x01",
            "姉さんも喜んでくれると思うんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4FF")

    label("loc_A4FC")

    Call(0, 31)

    label("loc_A4FF")

    Jump("loc_AC82")

    label("loc_A504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_A53A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A532")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 6)), scpexpr(EXPR_END)), "loc_A52A")
    Call(0, 37)
    Jump("loc_A52D")

    label("loc_A52A")

    Call(0, 36)

    label("loc_A52D")

    Jump("loc_A535")

    label("loc_A532")

    Call(0, 37)

    label("loc_A535")

    Jump("loc_AC82")

    label("loc_A53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A6B4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 6)), scpexpr(EXPR_END)), "loc_A63E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A5CC")

    #C0513
    ChrTalk(
        0xD,
        (
            "（この女の人、ちょっと\x01",
            "  おっかないんだよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xD,
        (
            "（ワジとは気が合う\x01",
            "  みたいなんだけどさ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A639")

    label("loc_A5CC")


    #C0515
    ChrTalk(
        0xD,
        "あの、ご注文のカクテルです。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xF,
        "おう、付けといてくんな。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xD,
        (
            "わ、分かりました。\x01",
            "ツケですね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_A639")

    Jump("loc_A64F")

    label("loc_A63E")

    TurnDirection(0xD, 0x0, 0)
    Call(0, 36)
    OP_93(0xD, 0xB4, 0x0)

    label("loc_A64F")

    Jump("loc_A6AF")

    label("loc_A654")


    #C0518
    ChrTalk(
        0xD,
        (
            "こほん、今日は少し\x01",
            "大切な用事があるんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xD,
        "そろそろ準備をしておかないとな。\x02",
    )

    CloseMessageWindow()

    label("loc_A6AF")

    Jump("loc_AC82")

    label("loc_A6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_A80B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7A6")
    OP_93(0xFE, 0x0, 0x0)

    #C0520
    ChrTalk(
        0xFE,
        (
            "ええと、グラスは拭いたし\x01",
            "次は仕入れの確認を、と……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0521
    ChrTalk(
        0xFE,
        (
            "……アッバスって結構厳しいんだよな。\x01",
            "失敗するとビシッと注意されるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "つるんでた時は気付かなかったけど\x01",
            "体もでかいし、迫力あるよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A806")

    label("loc_A7A6")


    #C0523
    ChrTalk(
        0xFE,
        (
            "仕事で失敗すると\x01",
            "アッバスに注意されるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xFE,
        (
            "……ううっ、バイトも\x01",
            "楽じゃないんだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A806")

    Jump("loc_AC82")

    label("loc_A80B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A915")

    #C0525
    ChrTalk(
        0xFE,
        "ここのバーでバイトを始めたんだ。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "……自分で働いたミラで\x01",
            "姉さんに治療費を返そうと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "姉さんには心配掛けちゃったし、\x01",
            "本当はテスタメンツを辞めて働いた方が\x01",
            "いいのかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        "しばらくはここで頑張ってみるよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_A99A")

    label("loc_A915")


    #C0529
    ChrTalk(
        0xFE,
        (
            "色々考えたけど\x01",
            "やっぱりテスタメンツは\x01",
            "辞めたくないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        (
            "働いたミラで治療費を返すってことで\x01",
            "姉さんには納得してもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A99A")

    Jump("loc_AC82")

    label("loc_A99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A9EB")

    #C0531
    ChrTalk(
        0xD,
        "姉さんが訪ねてきちゃったよ！\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xD,
        "ど、ど、どうしよう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC82")

    label("loc_A9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_AB1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_AA76")

    #C0533
    ChrTalk(
        0xD,
        (
            "姉さんに謝ったら\x01",
            "テスタメンツをやめろって\x01",
            "言われちゃいそうなんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xD,
        "はあ、タイミングがつかめないよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB16")

    label("loc_AA76")


    #C0535
    ChrTalk(
        0xD,
        (
            "姉さんに謝るタイミングが\x01",
            "つかめないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xD,
        (
            "心配掛けたし、\x01",
            "一言くらいって思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xD,
        (
            "うーん、検査通院が終わって、\x01",
            "完治したら謝ろうかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_AB16")

    Jump("loc_AC82")

    label("loc_AB1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_AB98")

    #C0538
    ChrTalk(
        0xD,
        "姉さんには心配掛けちゃったな。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        (
            "オレも悪いとは思ってるんだけど……\x01",
            "はあ、余計に顔を合わせづらいよ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC82")

    label("loc_AB98")


    #C0540
    ChrTalk(
        0xD,
        (
            "怪我もほとんど治って、\x01",
            "ようやく退院できたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xD,
        (
            "姉さんには\x01",
            "随分心配掛けちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xD,
        (
            "姉さん、テスタメンツのこと\x01",
            "良く思ってないし……\x01",
            "無断外泊のまま入院しちゃったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xD,
        (
            "……はあ、いまさら\x01",
            "顔を合わせづらいよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_AC82")

    TalkEnd(0xD)
    Return()

    # Function_34_A101 end

    def Function_35_AC86(): pass

    label("Function_35_AC86")

    Call(0, 34)
    Return()

    # Function_35_AC86 end

    def Function_36_AC8A(): pass

    label("Function_36_AC8A")


    #C0544
    ChrTalk(
        0xD,
        "さ、さっきは世話になったな。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xD,
        (
            "オレ、一度マフィアに\x01",
            "やられちまったし\x01",
            "今度から護身術の練習しておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        "#0100Fそう……頑張ってね。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xD,
        "ああ、もちろんさ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 6)
    Return()

    # Function_36_AC8A end

    def Function_37_AD34(): pass

    label("Function_37_AD34")


    #C0548
    ChrTalk(
        0xD,
        (
            "姉さん、記念祭は\x01",
            "休みを取るみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "……オレも休みが取れたら\x01",
            "付き合おうかな。\x01",
            "普段心配掛けてるもんな。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_37_AD34 end

    def Function_38_ADAC(): pass

    label("Function_38_ADAC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AE40")
    Jump("loc_AE8A")

    label("loc_AE40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AE60")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE8A")

    label("loc_AE60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE80")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AE8A")

    label("loc_AE80")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AE8A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_B0C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_B00F")
    SetChrSubChip(0xF, 0x1)

    #C0550
    ChrTalk(
        0xF,
        "クク、手打ちとは滑稽な幕引きだねェ。\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xF,
        (
            "あたしはもう少し楽しませてくれるのかと\x01",
            "思ってたんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xE,
        (
            "#0402Fあはは、お姉さんも性格悪いなぁ。\x01",
            "かれこれ１週間……\x01",
            "あちらさんもよく持った方じゃない。\x02\x03",

            "#0404Fま、僕としては\x01",
            "限界まで耐えちゃったその後が\x01",
            "ちょっと気がかりなんだけどさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x101,
        "#0005F（何の話をしてるんだろ……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0BE")

    label("loc_B00F")


    #C0554
    ChrTalk(
        0xF,
        (
            "ん……？\x01",
            "なんだい、可愛らしい子だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xF,
        (
            "うちのジンゴと\x01",
            "同い年くらいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xF,
        (
            "うちの店はそこを出た所の\x01",
            "ナインヴァリって店だ。\x01",
            "ま、会ったら遊んでやっとくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 5)

    label("loc_B0BE")

    Jump("loc_B1BD")

    label("loc_B0C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B145")

    #C0557
    ChrTalk(
        0xF,
        "……おや、もう朝か。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xF,
        (
            "やれやれ、また\x01",
            "徹夜で飲んじまったねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xF,
        (
            "ジンゴはちゃんと\x01",
            "店を開けてるかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B1BD")

    label("loc_B145")


    #C0560
    ChrTalk(
        0xF,
        (
            "クク、仕切ってるのはダサい連中だが\x01",
            "ここのカクテルは中々だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xF,
        (
            "あんたらもどうだい？\x01",
            "良けりゃ一杯奢ってやるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1BD")

    TalkEnd(0xFE)
    SetChrSubChip(0xF, 0x1)
    Return()

    # Function_38_ADAC end

    def Function_39_B1C5(): pass

    label("Function_39_B1C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_B26E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B24E")

    #C0562
    ChrTalk(
        0xFE,
        (
            "アゼル……\x01",
            "どういうつもりなのっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "姉さんやユゴットが\x01",
            "どれだけ心配してると\x01",
            "思っているの……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_B26E")

    label("loc_B24E")


    #C0564
    ChrTalk(
        0xFE,
        "聞いているの、アゼル……！\x02",
    )

    CloseMessageWindow()

    label("loc_B26E")

    TalkEnd(0xFE)
    Return()

    # Function_39_B1C5 end

    def Function_40_B272(): pass

    label("Function_40_B272")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B34B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_B2EA")

    #C0565
    ChrTalk(
        0x11,
        (
            "恥ずかしながら\x01",
            "偏見を持っていたみたいだよ。\x02\x03",

            "不良といっても\x01",
            "悪い連中でもないみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B346")

    label("loc_B2EA")


    #C0566
    ChrTalk(
        0x11,
        (
            "いやはや、祭りは楽しいな！\x02\x03",

            "旧市街の不良といっても\x01",
            "そう悪い連中でもないじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_B346")

    Jump("loc_B4F9")

    label("loc_B34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_B3C0")

    #C0567
    ChrTalk(
        0x11,
        (
            "はっはっは、こう見えて私は\x01",
            "ビリヤードは得意なんだ！\x02\x03",

            "それそれ、\x01",
            "もう１本取ってしまうぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B422")

    label("loc_B3C0")

    TurnDirection(0x11, 0xB, 0)

    #C0568
    ChrTalk(
        0x11,
        (
            "……よし、私の番だな。\x02\x03",

            "はっは、見ていたまえ。\x01",
            "ビリヤードは得意中の得意だぞ！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_B422")

    Jump("loc_B4F9")

    label("loc_B427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_B472")

    #C0569
    ChrTalk(
        0x11,
        (
            "いやあ、中々いいバーだな。\x01",
            "今日はゆっくり飲めそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4F9")

    label("loc_B472")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0570
    ChrTalk(
        0x11,
        (
            "あ、あのー、スコッチを１つ……\x02\x03",

            "ダブルでお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xC,
        (
            "スコッチ１つ、ダブルだね。\x01",
            "すぐに用意するよ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_B4F9")

    TalkEnd(0xFE)
    Return()

    # Function_40_B272 end

    def Function_41_B4FD(): pass

    label("Function_41_B4FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B54A")

    #C0572
    ChrTalk(
        0x12,
        (
            "そ、そんな……\x01",
            "……わたしワジさんだったら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B54D")

    label("loc_B54A")

    Call(0, 11)

    label("loc_B54D")

    Jump("loc_B612")

    label("loc_B552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B60F")
    OP_4B(0xA, 0xFF)

    #C0573
    ChrTalk(
        0x12,
        (
            "今日、ワジさん\x01",
            "いないんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xA,
        "わ、悪いがその通りだよ。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xA,
        (
            "ワジは留守にしている、\x01",
            "というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        (
            "さっきから何度も同じ事を\x01",
            "聞かないでくれたまえ……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_B612")

    label("loc_B60F")

    Call(0, 42)

    label("loc_B612")

    TalkEnd(0xFE)
    Return()

    # Function_41_B4FD end

    def Function_42_B616(): pass

    label("Function_42_B616")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0577
    ChrTalk(
        0x12,
        "ねえねえ、あの人じゃな～い？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x12,
        "昨日のクールな美少年！\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x13,
        "きゃっ、カクテル飲んでる～。\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x13,
        "カ・ワ・イ・イ～㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_42_B616 end

    def Function_43_B69F(): pass

    label("Function_43_B69F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B733")
    Jump("loc_B77D")

    label("loc_B733")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B753")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B77D")

    label("loc_B753")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B773")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B77D")

    label("loc_B773")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B77D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 44)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_B69F end

    def Function_44_B7AD(): pass

    label("Function_44_B7AD")

    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)

    #C0581
    ChrTalk(
        0x14,
        "ワジさん、今日もいないわね……\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x15,
        (
            "はあ、あの涼しげな瞳……\x01",
            "……不思議な色彩を放つ髪……\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x15,
        (
            "ワジさん、どこに\x01",
            "行っちゃったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_44_B7AD end

    def Function_45_B844(): pass

    label("Function_45_B844")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B891")

    #C0584
    ChrTalk(
        0x13,
        (
            "ポワンポワン……\x01",
            "な、何だか胸が苦しいかも……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B894")

    label("loc_B891")

    Call(0, 11)

    label("loc_B894")

    Jump("loc_B901")

    label("loc_B899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_B8FE")

    #C0585
    ChrTalk(
        0x13,
        "今日も来ちゃった……\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x13,
        (
            "ワジさん、どうして今日は\x01",
            "姿を見せてくれないのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B901")

    label("loc_B8FE")

    Call(0, 42)

    label("loc_B901")

    TalkEnd(0xFE)
    Return()

    # Function_45_B844 end

    def Function_46_B905(): pass

    label("Function_46_B905")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B999")
    Jump("loc_B9E3")

    label("loc_B999")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B9B9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9E3")

    label("loc_B9B9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9D9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9E3")

    label("loc_B9D9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B9E3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 44)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_B905 end

    def Function_47_BA13(): pass

    label("Function_47_BA13")

    TalkBegin(0xFE)
    SetChrSubChip(0x16, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BA97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_BA8F")
    SetChrSubChip(0x16, 0x1)

    #C0587
    ChrTalk(
        0x16,
        (
            "あー、そっかー。\x01",
            "確かにそうだよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x16,
        (
            "旧市街の人って\x01",
            "みんな貧乏らしいもんねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA92")

    label("loc_BA8F")

    Call(0, 48)

    label("loc_BA92")

    Jump("loc_BAEC")

    label("loc_BA97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_BAE9")
    SetChrSubChip(0x16, 0x1)

    #C0589
    ChrTalk(
        0x16,
        "いいじゃん、スリルあってさ。\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x16,
        "あたし結構楽しかったよ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BAEC")

    label("loc_BAE9")

    Call(0, 49)

    label("loc_BAEC")

    TalkEnd(0xFE)
    Return()

    # Function_47_BA13 end

    def Function_48_BAF0(): pass

    label("Function_48_BAF0")

    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)

    #C0591
    ChrTalk(
        0x16,
        (
            "ここのバーテンさん、\x01",
            "超ごついねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x16,
        (
            "もしかしてヤクザだったり\x01",
            "するのかなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x17,
        (
            "ばーか、ヤクザが\x01",
            "いるのは街の方だろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x17,
        "ヤクザが貧乏なワケねえじゃん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_48_BAF0 end

    def Function_49_BBA1(): pass

    label("Function_49_BBA1")

    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)

    #C0595
    ChrTalk(
        0x16,
        "結構いいとこじゃん。\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x16,
        "やっぱ来てよかったでしょ？\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x17,
        (
            "おまえ、１人で先に\x01",
            "行きすぎなんだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x17,
        (
            "言っとくけど旧市街の不良って\x01",
            "超怖い連中らしいぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_49_BBA1 end

    def Function_50_BC4B(): pass

    label("Function_50_BC4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BCD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_BCCD")
    SetChrSubChip(0x17, 0x2)

    #C0599
    ChrTalk(
        0x17,
        (
            "ヤクザっていやあ\x01",
            "ルバーチェとかだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x17,
        (
            "あいつら超金持ちじゃん。\x01",
            "旧市街にいるわけねえって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCD0")

    label("loc_BCCD")

    Call(0, 48)

    label("loc_BCD0")

    Jump("loc_BD6D")

    label("loc_BCD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_BD6A")
    SetChrSubChip(0x17, 0x2)

    #C0601
    ChrTalk(
        0x17,
        (
            "旧市街の不良って、\x01",
            "前にヤクザと抗争してたんだろ？\x01",
            "絶対に超凶暴な連中バッカだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x17,
        (
            "……ま、オレも\x01",
            "見た事はないけどさー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD6D")

    label("loc_BD6A")

    Call(0, 49)

    label("loc_BD6D")

    TalkEnd(0xFE)
    Return()

    # Function_50_BC4B end

    def Function_51_BD71(): pass

    label("Function_51_BD71")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30950.itc", 0x1E)
    LoadChrToIndex("chr/ch31850.itc", 0x1F)
    OP_68(12000, 1000, 12000, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -300, 0, -500, 0)
    SetChrPos(0x102, 500, 0, -500, 0)
    SetChrPos(0x103, -300, 0, -500, 0)
    SetChrPos(0x104, 500, 0, -500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2600, 50, 12600, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x40)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    OP_68(4000, 1000, 7000, 8000)
    MoveCamera(25, 17, 0, 8000)
    SetCameraDistance(23500, 8000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1000, 1700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetCameraDistance(24500, 2000)

    def lambda_BF6D():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF6D)

    def lambda_BF87():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BF87)
    Sleep(400)

    def lambda_BF9B():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF9B)

    def lambda_BFB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BFB5)
    Sleep(400)

    def lambda_BFC9():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BFC9)

    def lambda_BFE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BFE3)
    Sleep(400)

    def lambda_BFF7():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BFF7)

    def lambda_C011():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C011)
    WaitChrThread(0x101, 1)

    def lambda_C026():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C026)
    WaitChrThread(0x102, 1)

    def lambda_C037():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C037)
    WaitChrThread(0x103, 1)

    def lambda_C048():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C048)
    WaitChrThread(0x104, 1)

    def lambda_C059():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C059)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)

    #C0603
    ChrTalk(
        0x102,
        "#0105F#6Pビリヤード台……？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x104,
        (
            "#12P#0300Fプールバーってやつか。\x01",
            "なかなかいい趣味してるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x103,
        (
            "#6P#0200F『トリニティ』……\x01",
            "一応、認可を受けた店ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x101,
        (
            "#6P#0001Fなるほど、ここが\x01",
            "『テスタメンツ』の溜まり場か……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 7200, 0, 9500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)

    #N0607
    NpcTalk(
        0x9,
        "男の声",
        "──何用だ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0xA, 7200, 0, 9500, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, 7200, 0, 9500, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_68(0, 1000, 3600, 3000)
    MoveCamera(45, 23, 0, 3000)
    SetCameraDistance(22500, 3000)
    BeginChrThread(0x9, 3, 0, 52)
    Sleep(700)
    BeginChrThread(0xA, 3, 0, 53)
    Sleep(700)
    BeginChrThread(0xB, 3, 0, 54)
    Sleep(1200)

    def lambda_C273():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C273)
    Sleep(300)

    def lambda_C283():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C283)

    def lambda_C290():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C290)
    Sleep(300)

    def lambda_C2A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C2A0)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)

    #N0608
    NpcTalk(
        0xA,
        "青装束の青年",
        "君たちは……！？\x02",
    )

    CloseMessageWindow()

    #N0609
    NpcTalk(
        0xB,
        "青装束の青年",
        "#5Pけ、警察……？\x02",
    )

    CloseMessageWindow()

    #N0610
    NpcTalk(
        0x9,
        "禿の大男",
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        (
            "#12P#0003F先ほどはどうも。\x02\x03",

            "#0000F一応、営業してるみたいだね。\x01",
            "邪魔させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0612
    NpcTalk(
        0xA,
        "青装束の青年",
        "くっ、ぬけぬけと……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #N0613
    NpcTalk(
        0xA,
        "青装束の青年",
        (
            "#1P……何の用だ！？\x01",
            "返答次第ではタダでは帰さん！\x02",
        )
    )

    CloseMessageWindow()

    #N0614
    NpcTalk(
        0xB,
        "青装束の青年",
        (
            "#5Pさ、先ほどの借りも\x01",
            "まとめて返させてもらう……！\x02",
        )
    )

    CloseMessageWindow()

    #N0615
    NpcTalk(
        0x9,
        "禿の大男",
        "#5P──待て。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    OP_0D()

    #N0616
    NpcTalk(
        0xA,
        "青装束の青年",
        "#1Pアッバス……\x02",
    )

    CloseMessageWindow()

    #N0617
    NpcTalk(
        0xB,
        "青装束の青年",
        "#5Pな、なぜ止める……？\x02",
    )

    CloseMessageWindow()

    #N0618
    NpcTalk(
        0x9,
        "禿の大男",
        (
            "#5Pここは聖域──\x01",
            "余計な雑音を立てるな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x190)

    #N0619
    NpcTalk(
        0x9,
        "禿の大男",
        "#11Pワジ、どうする？\x02",
    )

    CloseMessageWindow()

    #N0620
    NpcTalk(
        0x8,
        "声",
        "……んー、そうだね。\x02",
    )

    CloseMessageWindow()
    OP_68(-2600, 1000, 12600, 2000)
    MoveCamera(35, 23, 0, 2000)
    SetCameraDistance(22000, 2000)
    OP_6F(0x79)

    #C0621
    ChrTalk(
        0x8,
        (
            "#0404Fいいんじゃない？\x01",
            "ここに通しちゃっても。\x02",
        )
    )

    CloseMessageWindow()

    #N0622
    NpcTalk(
        0x9,
        "禿の大男",
        "……わかった。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1000, 3600, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    OP_0D()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_C63C():

        label("loc_C63C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_C63C")

    QueueWorkItem2(0x101, 2, lambda_C63C)

    def lambda_C64E():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C64E)
    Sleep(50)

    def lambda_C66B():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C66B)
    Sleep(50)

    def lambda_C688():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C688)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    TurnDirection(0x9, 0x101, 500)

    #N0623
    NpcTalk(
        0x9,
        "禿の大男",
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x101,
        "#12P#0005Fど、どうも。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x104,
        "#4P#0305F（なんだ、このノリは……）\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        "#0106F#6P（何かの儀式みたいね……）\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_C756():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C756)
    Sleep(50)

    def lambda_C773():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C773)
    Sleep(50)

    def lambda_C790():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C790)
    Sleep(50)

    def lambda_C7AD():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C7AD)
    Sleep(1500)
    Fade(500)
    OP_68(-2500, 1100, 10700, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrPos(0x101, -1600, 0, 6700, 0)
    SetChrPos(0x102, -600, 0, 6700, 0)
    SetChrPos(0x103, -1500, 0, 5500, 0)
    SetChrPos(0x104, -500, 0, 5500, 0)
    SetChrPos(0x9, 1000, 0, 2400, 0)
    SetChrPos(0xA, 1900, 0, 1700, 0)
    SetChrPos(0xB, 1900, 0, 500, 0)

    def lambda_C884():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x25E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C884)

    def lambda_C89E():
        OP_96(0xFE, 0xFFFFF9C0, 0x0, 0x25E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C89E)
    Sleep(50)

    def lambda_C8BB():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C8BB)

    def lambda_C8D5():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C8D5)

    def lambda_C8EF():
        OP_96(0xFE, 0x0, 0x0, 0x2C88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C8EF)
    Sleep(50)

    def lambda_C90C():
        OP_96(0xFE, 0x384, 0x0, 0x29CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C90C)

    def lambda_C926():
        OP_96(0xFE, 0x384, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C926)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x9, 1)

    def lambda_C954():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C954)
    WaitChrThread(0xA, 1)

    def lambda_C965():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C965)
    WaitChrThread(0xB, 1)

    def lambda_C976():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_C976)
    SetChrFlags(0x8, 0x20)

    def lambda_C988():
        OP_96(0xFE, 0xFFFFF63C, 0x32, 0x3070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C988)

    def lambda_C9A2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C9A2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(1432, 255, 90, 0)    #voice#Lazy

    #A0627
    AnonymousTalk(
        0x8,
        (
            "──で、なに？\x02\x03",

            "警察はお呼びじゃないって\x01",
            "言ったはずだけど？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0628
    ChrTalk(
        0x101,
        (
            "#12P#0003Fそちらに用がなくても\x01",
            "こちらにはあってね。\x02\x03",

            "#0000F君たちに、少しばかり\x01",
            "捜査に協力して欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x8,
        (
            "#5P#0403Fふーん、捜査ねぇ。\x02\x03",

            "#0402F言っておくけど、\x01",
            "バイパーと決着を付けるのを\x01",
            "止めるつもりはないよ？\x02\x03",

            "#0404F近所の住民には迷惑だろうけど\x01",
            "ま、我慢してもらうしかないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x101,
        (
            "#12P#0003F別に君たちの争いを\x01",
            "止めにきたわけじゃない。\x02\x03",

            "#0001F──君たちが本気で\x01",
            "潰し合おうとしている理由……\x02\x03",

            "それを聞かせてもらいに来た。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0631
    ChrTalk(
        0x8,
        "#5P#0400Fへぇ……\x02",
    )

    CloseMessageWindow()

    #N0632
    NpcTalk(
        0xA,
        "青装束の青年",
        "#2Pそ、それは……！\x02",
    )

    CloseMessageWindow()

    #N0633
    NpcTalk(
        0x9,
        "禿の大男",
        (
            "#5P──口を出すな。\x01",
            "全てワジに任せろ。\x02",
        )
    )

    CloseMessageWindow()

    #N0634
    NpcTalk(
        0xA,
        "青装束の青年",
        "#2Pあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        (
            "#12P#0001F……その様子だと\x01",
            "本当に何かあるみたいだな。\x02\x03",

            "どうか聞かせてくれないか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrPos(0x8, -2600, 0, 11500, 180)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(1433, 255, 90, 0)    #voice#Lazy
    Sleep(800)

    def lambda_CDA7():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x2A94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CDA7)
    WaitChrThread(0x8, 1)

    #C0636
    ChrTalk(
        0x8,
        (
            "#0400Fそれを知ってどうするの？\x02\x03",

            "遊撃士ならまだしも……\x01",
            "警察が何かしてくれるワケ？\x02\x03",

            "僕たち旧市街#6Rダウンタウン#に住む、\x01",
            "厄介者の悪ガキ共#8Rバッドボーイズ#にさ？\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        (
            "#12P#0006F……警察の対応が\x01",
            "不十分なのは認めるよ。\x02\x03",

            "理由を知ったからといって\x01",
            "君たちに協力できるとも限らない。\x02\x03",

            "#0000F人を守るのが仕事だっていう\x01",
            "遊撃士と同じ訳じゃないからね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CF1E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CF1E)
    Sleep(50)

    def lambda_CF2E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF2E)
    WaitChrThread(0x104, 2)

    #C0638
    ChrTalk(
        0x104,
        "#0301Fお、おい……\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        "#0101F#11Pちょっと、ロイド……\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "#0404Fやれやれ、お話にならないな。\x02\x03",

            "#0402Fギブ・アンド・テイクなしに\x01",
            "情報だけを引き出すつもりかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        "#12P#0004F──いや、ギブならあるさ。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x8,
        "#0405Fえ……\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#12P#0001F捜査官の仕事は\x01",
            "闇に埋もれた真実を明らかにして\x01",
            "人と社会に光をもたらすこと……\x02\x03",

            "少なくとも俺は\x01",
            "そんな風に教えられてきた。\x02\x03",

            "#0004Fもし君たちが、ほんの少しでも\x01",
            "疑念という闇を抱えてるのなら……\x02\x03",

            "それを晴らす手伝いはできると思う。\x02\x03",

            "#0000Fそれが……\x01",
            "俺たちの提供できるギブさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x102,
        "#0105F#11P……あ…………\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x104,
        "#0302Fこりゃまた……\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x103,
        "#12P#0202F………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    #Sound(1434, 255, 100, 0)    #voice#Lazy

    #C0647
    ChrTalk(
        0x8,
        "#0404F…………くくっ……………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    #Sound(1431, 255, 100, 0)    #voice#Lazy

    #C0648
    ChrTalk(
        0x8,
        "#0409F#4Sあはははははははッ！！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0649
    ChrTalk(
        0x8,
        (
            "#0402Fいいね！　すごくいいよ！\x02\x03",

            "そんなクサイ台詞、\x01",
            "そうそう聞けるもんじゃない！\x02\x03",

            "#0409Fロイドって言ったっけ！？\x01",
            "いや～、気に入っちゃったよ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D29E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D29E)

    def lambda_D2AB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D2AB)

    #C0650
    ChrTalk(
        0x101,
        (
            "#12P#0006F……別にウケを取るために\x01",
            "言ったんじゃないけどな。\x02\x03",

            "#0001Fそれで、どうなんだ？\x02\x03",

            "『本気で潰し合う理由』……\x01",
            "教えてくれる気はあるのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D34C():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x2CEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D34C)
    WaitChrThread(0x8, 1)
    Fade(250)
    SetChrPos(0x8, -2500, 50, 12400, 135)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x2)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0651
    ChrTalk(
        0x8,
        (
            "#5P#0404F#5P……フフ、まあいいか。\x02\x03",

            "あんな決め台詞まで聞かされて\x01",
            "おひねりを出さないほどケチじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x0)
    Sleep(200)

    #C0652
    ChrTalk(
        0x8,
        (
            "#5P#0402F──アッバス。\x01",
            "教えちゃっていいよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    #N0653
    NpcTalk(
        0x9,
        "禿の大男",
        "#11P……分かった。\x02",
    )

    CloseMessageWindow()
    OP_68(-2140, 1100, 10430, 1000)

    def lambda_D472():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D472)
    Sleep(150)

    def lambda_D482():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D482)
    Sleep(50)

    def lambda_D492():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D492)
    Sleep(50)

    def lambda_D4A2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D4A2)
    Sleep(50)

    def lambda_D4B2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D4B2)
    WaitChrThread(0x104, 2)
    Sleep(1000)

    #N0654
    NpcTalk(
        0x9,
        "禿の大男",
        "#5P名乗っていなかったな。\x02",
    )

    CloseMessageWindow()

    #N0655
    NpcTalk(
        0x9,
        "禿の大男",
        (
            "#5P俺はアッバス。\x01",
            "テスタメンツの一員だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ、ああ……よろしく。\x02\x01",

            "#0001F（でかいな……何かやってるのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x9,
        "#5P事の発端は５日前の夜だ。\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x9,
        (
            "#5Pうちのメンバーの一人が\x01",
            "この近くの裏路地で\x01",
            "バイパーどもの闇討ちにあった。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0659
    ChrTalk(
        0x101,
        "#6P#0007F闇討ち……！？\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x102,
        (
            "#6P#0101Fその……\x01",
            "ただの喧嘩ではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #N0661
    NpcTalk(
        0xA,
        "青装束の青年",
        "#11Pフン、喧嘩なものか……！\x02",
    )

    CloseMessageWindow()

    #N0662
    NpcTalk(
        0xA,
        "青装束の青年",
        (
            "#11P後頭部に一撃くらって\x01",
            "倒れた所をメッタ打ちだぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #N0663
    NpcTalk(
        0xB,
        "青装束の青年",
        "い、一方的な襲撃だ……\x02",
    )

    CloseMessageWindow()

    #N0664
    NpcTalk(
        0xB,
        "青装束の青年",
        (
            "やられたヤツは……\x01",
            "びょ、病院に運ばれている……\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x104,
        "#12P#0306Fそいつはエグいな……\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x101,
        (
            "#6P#0001Fその……\x01",
            "容態の方はどうなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x9,
        (
            "#5P病院からの連絡では\x01",
            "まだ意識が戻らないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x9,
        (
            "#5P手当ては済んだようだが\x01",
            "頭を打ったらしいからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x9,
        "#5P今、連絡を待っているところだ。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#6P#0003Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x102,
        (
            "#6P#0101F……あの、やっぱり\x01",
            "警察には届け出なかったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x9,
        (
            "#5P伝えたところで我々のために\x01",
            "動くとはとても思えんからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x9,
        (
            "#5Pそれに犯人は明確だ。\x01",
            "報復の邪魔をされては困る。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x102,
        "#6P#0108F……そう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0675
    ChrTalk(
        0x103,
        (
            "#6P#0205F──待ってください。\x02\x03",

            "#0200F襲われた人は、まだ意識が\x01",
            "戻ってないそうですけど……\x02\x03",

            "なら、どうしてその人が\x01",
            "『サーベルバイパー』に\x01",
            "襲われたと分かったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0676
    ChrTalk(
        0x101,
        (
            "#6P#0005Fそういえば……\x02\x03",

            "ひょっとして\x01",
            "状況証拠だけなのか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sleep(200)

    #C0677
    ChrTalk(
        0x8,
        (
            "#5P#0404F……ま、そこまで\x01",
            "僕たちも短絡的じゃないよ。\x02\x03",

            "#0402Fなにせウチは、連中と違って\x01",
            "知性派で売ってるらしいからね。\x02\x03",

            "#0409Fハハ、たかが不良に\x01",
            "知性派ってのもどうかと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #N0678
    NpcTalk(
        0xA,
        "青装束の青年",
        "#11Pワジ……！\x02",
    )

    CloseMessageWindow()

    def lambda_DB49():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DB49)
    Sleep(50)

    def lambda_DB59():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DB59)
    Sleep(50)

    def lambda_DB69():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DB69)
    Sleep(50)

    def lambda_DB79():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DB79)

    #C0679
    ChrTalk(
        0x8,
        (
            "#5P#0404Fフフ、僕たちが\x01",
            "彼らの仕業と断定した理由……\x02\x03",

            "#0400F捜査官の君なら\x01",
            "見当がつくんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        "#12P#0003F………そうだな…………\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【襲われた場所の位置】\x01",          # 0
            "【襲われたメンバーの傷跡】\x01",      # 1
            "【現場に残されていた足跡】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DC9D"),
        (1, "loc_DE58"),
        (2, "loc_DF6B"),
        (SWITCH_DEFAULT, "loc_E17E"),
    )


    label("loc_DC9D")


    #C0681
    ChrTalk(
        0x101,
        (
            "#12P#0001Fそのメンバーが襲われた場所……\x01",
            "それが決め手になったんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x8,
        (
            "#5P#0406Fうーん、さっきも言ったけど\x01",
            "襲われた場所は近くの裏路地だ。\x02\x03",

            "#0400Fバイパーの連中が通る事もあるけど\x01",
            "ちょっと決め手にはならないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x101,
        "#12P#0005Fそ、そうか……\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x9,
        (
            "#5P──決め手となったのは\x01",
            "襲われたメンバーの傷跡だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x9,
        (
            "#5P主に打撃によるものだったが\x01",
            "同時に裂傷も目立っていてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x9,
        (
            "#5Pまるで硬く尖ったもので\x01",
            "引き裂いたような感じだった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E17E")

    label("loc_DE58")

    OP_2C(0x3E, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0687
    ChrTalk(
        0x101,
        (
            "#12P#0008F……そうか、分かった。\x02\x03",

            "#0001F襲われたメンバーの\x01",
            "傷跡が決め手になったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x8,
        "#5P#0409Fビンゴ、流石だね。\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x9,
        (
            "#5P傷は、主に打撃によるものだったが\x01",
            "同時に裂傷も目立っていてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x9,
        (
            "#5Pまるで硬く尖ったもので\x01",
            "引き裂いたような感じだった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E17E")

    label("loc_DF6B")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0691
    ChrTalk(
        0x101,
        (
            "#12P#0008F君たちも彼らも、\x01",
            "特徴的な靴を履いている……\x02\x03",

            "#0001Fひょっとして、現場に残っていた\x01",
            "足跡が決め手になったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x8,
        (
            "#5P#0405Fへえ、面白い意見だね。\x02\x03",

            "#0406Fただまあ、\x01",
            "旧市街の路面は古い石畳だから\x01",
            "それほど足跡は付かないんだ。\x02\x03",

            "#0400F連中も日頃から行き来してるし\x01",
            "決め手にはならなかったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        "#12P#0005Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x9,
        (
            "#5P──決め手となったのは\x01",
            "襲われたメンバーの傷跡だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x9,
        (
            "#5P主に打撃によるものだったが\x01",
            "同時に裂傷も目立っていてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x9,
        (
            "#5Pまるで硬く尖ったもので\x01",
            "引き裂いたような感じだった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E17E")

    label("loc_E17E")


    #C0697
    ChrTalk(
        0x102,
        (
            "#0105F#12P打撃による傷跡と\x01",
            "硬く尖ったものによる裂傷……\x02\x03",

            "#0101F……あ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x104,
        (
            "#0301F#12P……なるほど。\x01",
            "連中が持ってた釘付きの棍棒か。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x103,
        (
            "#6P#0204F確かに犯人の目星としては\x01",
            "決定的かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0700
    ChrTalk(
        0x101,
        (
            "#12P#0003F──話は大体判った。\x02\x03",

            "#0000Fありがとう、参考になったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        (
            "#5P#0405Fそれはいいけど……\x01",
            "何、その情報だけでいいの？\x02\x03",

            "報復は止めろとか、\x01",
            "改めて言ったりしないわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#12P#0006F個人的にはもちろん\x01",
            "止めたいところだけど……\x02\x03",

            "#0001F今はまだ、判断材料が少なすぎる。\x02\x03",

            "サーベルバイパーの話も聞いて\x01",
            "何か判ったら連絡させてもらうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x8,
        (
            "#5P#0404Fフフ、なるほど。\x01",
            "あくまで“捜査”に拘りたいのか。\x02\x03",

            "#0402Fなら、面白い話が聞けるのを\x01",
            "楽しみにさせてもらおうかな。\x02\x03",

            "#0409F──まあ、そうならなかったら\x01",
            "血の雨が降るだけの話だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x101,
        (
            "#12P#0003F………分かった。\x02\x03",

            "#0000Fせいぜいご期待に沿えるよう、\x01",
            "面白い話を持ってくるさ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -2600, 50, 12600, 0)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    OP_4C(0x9, 0xFF)
    SetChrPos(0xA, 2950, 30, 6580, 180)
    OP_4C(0xA, 0xFF)
    SetChrPos(0xB, 10230, 0, 4410, 90)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_68(0, 1100, 9500, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 0, 0, 9500, 180)
    SetChrPos(0x1, 0, 0, 9500, 180)
    SetChrPos(0x2, 0, 0, 9500, 180)
    SetChrPos(0x3, 0, 0, 9500, 180)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x42, 1)
    OP_29(0x3E, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_51_BD71 end

    def Function_52_E601(): pass

    label("Function_52_E601")


    def lambda_E606():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E606)

    def lambda_E617():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E617)
    WaitChrThread(0xFE, 1)

    def lambda_E635():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E635)
    WaitChrThread(0xFE, 1)

    def lambda_E653():
        OP_95(0xFE, 0, 0, 4800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_E653)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)
    Return()

    # Function_52_E601 end

    def Function_53_E674(): pass

    label("Function_53_E674")


    def lambda_E679():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E679)

    def lambda_E68A():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E68A)
    WaitChrThread(0xFE, 1)

    def lambda_E6A8():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6A8)
    WaitChrThread(0xFE, 1)

    def lambda_E6C6():
        OP_95(0xFE, -600, 0, 6100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_E6C6)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x1F4)
    Return()

    # Function_53_E674 end

    def Function_54_E6E7(): pass

    label("Function_54_E6E7")


    def lambda_E6EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E6EC)

    def lambda_E6FD():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6FD)
    WaitChrThread(0xFE, 1)

    def lambda_E71B():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E71B)
    WaitChrThread(0xFE, 1)

    def lambda_E739():
        OP_95(0xFE, 700, 0, 6700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_E739)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xB4, 0x1F4)
    Return()

    # Function_54_E6E7 end

    def Function_55_E75A(): pass

    label("Function_55_E75A")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x0, 0x9, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(2960, 1100, 12800, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(25980, 0)
    SetChrPos(0x101, 2740, 0, 11700, 0)
    SetChrPos(0x102, 1500, 0, 10260, 0)
    SetChrPos(0x103, 1500, 0, 11700, 0)
    SetChrPos(0x104, 2740, 0, 10260, 0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0705
    ChrTalk(
        0x9,
        "#5P……来たか。\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x101,
        (
            "#0003F#11P……来たか、じゃないんだが。\x02\x03",

            "#0001F『テスタメンツを稽古』って……\x01",
            "何を物騒な依頼を出してるんだ。\x02\x03",

            "警察が不良を\x01",
            "訓練できるわけないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x102,
        (
            "#12P#0105Fワジ君じゃなくて\x01",
            "貴方の名前だったけど……\x01",
            "これは貴方が考えたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x9,
        (
            "#5Pふむ、どうやら\x01",
            "勘違いをしているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x9,
        (
            "#5P説明してやろう。\x01",
            "こちらに来るがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_E95D():

        label("loc_E95D")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_E95D")

    QueueWorkItem2(0x0, 1, lambda_E95D)

    def lambda_E96F():

        label("loc_E96F")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_E96F")

    QueueWorkItem2(0x1, 1, lambda_E96F)

    def lambda_E981():

        label("loc_E981")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_E981")

    QueueWorkItem2(0x2, 1, lambda_E981)

    def lambda_E993():

        label("loc_E993")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_E993")

    QueueWorkItem2(0x3, 1, lambda_E993)

    def lambda_E9A5():
        OP_95(0xFE, 7550, 0, 14780, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_E9A5)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x9, 0x0)
    OP_68(1290, 1000, 9450, 0)
    MoveCamera(52, 17, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0x9, 3060, 0, 8960, 270)
    SetChrPos(0x101, 700, 0, 9600, 90)
    SetChrPos(0x102, 560, 0, 8000, 90)
    SetChrPos(0x103, -990, 0, 8000, 90)
    SetChrPos(0x104, -990, 0, 9600, 90)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xD, 14390, 0, 7400, 178)
    SetChrPos(0xC, 14000, 0, 7400, 268)
    SetChrPos(0xA, 9250, 0, 4150, 225)
    SetChrPos(0xB, 5000, 0, 2000, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0710
    ChrTalk(
        0x9,
        "#11Pそう難しい話ではない。\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x9,
        (
            "#11P──依頼したいのは\x01",
            "メンバーへの護身術のレクチャーだ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0712
    ChrTalk(
        0x101,
        "#6P#0005F……へ…………！？\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x104,
        (
            "#6P#0305F護身術……？\x02\x03",

            "#0301Fおいおい、そんなモンを\x01",
            "あんたらの喧嘩に使おうってのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x9,
        "#11P勘違いをするなと言っている。\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x9,
        "#11P想定される相手はマフィアだ。\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x103,
        (
            "#6P#0200Fマフィア……\x01",
            "ルバーチェもしくは黒月ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそういえば最近\x01",
            "マフィア同士の抗争が\x01",
            "始まったそうね……\x02\x03",

            "#0103F散発的だけど\x01",
            "撃ち合いなんかも\x01",
            "やっているそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x9,
        "#11Pその通りだ。\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x9,
        (
            "#11Pそしてここ旧市街は\x01",
            "往々にしてその最前線となる。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x9,
        (
            "#11P近くには倉庫街や廃屋、空き地……\x01",
            "連中にとっても都合がいいのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x9,
        (
            "#11P我らにとって\x01",
            "好ましい状況とは言えん。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそれで護身術を学びたい……と。\x02\x03",

            "#0200F……そういえば、例の旧市街の一件で\x01",
            "１週間も意識混濁になった\x01",
            "メンバーさんもいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x101,
        (
            "#6P#0001F……なるほど…………\x01",
            "そういう事だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x9,
        "#11Pさすがに理解は早いようだな。\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x9,
        (
            "#11P本来ならばワジの格闘術を\x01",
            "メンバーに身に付けさせるという\x01",
            "方法を採るべきだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x9,
        (
            "#11Pあれは少々特殊で、\x01",
            "柔軟な体格や、体質的な素質が無ければ\x01",
            "使いこなせん。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x9,
        (
            "#11Pその点、ロイド・バニングスの見せた\x01",
            "警察流の護身術は注目に値する。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x9,
        (
            "#11P見事な防御力に加え\x01",
            "万人が身に付けられる汎用性……\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x9,
        (
            "#11P……その戦いぶり、\x01",
            "メンバーとの実戦の中で\x01",
            "もう一度見せてもらえぬか？\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x9,
        (
            "#11P無論一朝一夕で身に付く物では\x01",
            "なかろうが、その心構えだけでも\x01",
            "良い刺激となるだろう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)

    def lambda_F103():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F103)
    Sleep(10)

    def lambda_F113():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F113)

    def lambda_F120():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F120)

    def lambda_F12D():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F12D)
    Sleep(400)

    #C0731
    ChrTalk(
        0x102,
        (
            "#12P#0100Fどうやら真っ当な\x01",
            "依頼だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x103,
        (
            "#6P#0203Fええ、受けても問題ないかと。\x02\x03",

            "#0200Fロイドさん、どうしますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        (
            "#5P#0003F実戦形式でのレクチャー、か。\x01",
            "そうだな……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F1F7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F1F7)
    Sleep(50)

    def lambda_F207():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F207)

    def lambda_F214():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F214)

    def lambda_F221():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F221)
    Sleep(300)

    #C0734
    ChrTalk(
        0x101,
        (
            "#6P#0001Fあれは護身術じゃなくて\x01",
            "警察学校で学んだ\x01",
            "制圧術の一種だけど……\x02\x03",

            "……それでも構わないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x9,
        "#11P無論だ。\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x9,
        (
            "#11Pあくまで稽古、\x01",
            "そちらの３名の参加も認めよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x101,
        "#6P#0003Fそうか……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【受ける】\x01",          # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F35A")
    OP_29(0x12, 0x1, 0x1)
    Call(0, 56)
    Return()

    label("loc_F35A")


    #C0738
    ChrTalk(
        0x101,
        (
            "#6P#0001F……少し待ってくれ。\x01",
            "こちらも準備を整えたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x9,
        "#11Pそうか。\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x9,
        (
            "#11P本日中は時間が空いている。\x01",
            "十分に準備を整えるがいい。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetChrPos(0xD, 12470, 0, 16210, 180)
    SetChrPos(0xC, 14030, 30, 11040, 270)
    SetChrPos(0xA, 2950, 30, 6580, 180)
    SetChrPos(0xB, 10230, 0, 4410, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_F460")
    SetChrPos(0xD, -4000, 0, 16690, 0)

    label("loc_F460")

    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0x0, 600, 0, 8000, 90)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    OP_4C(0x9, 0xFF)
    BeginChrThread(0x9, 0, 0, 0)
    OP_29(0x12, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_55_E75A end

    def Function_56_F49E(): pass

    label("Function_56_F49E")

    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xD, 0x2)

    #C0741
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそういった事情が\x01",
            "あるなら断る理由はない。\x02\x03",

            "#0000Fむしろ君達が更正する\x01",
            "手助けもできそうだしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x104,
        (
            "#6P#0306Fふう……そう言うと思ってたぜ。\x02\x03",

            "#0300Fロイド、いくらお前でも\x01",
            "メンバー全員相手はキツイだろ。\x01",
            "遠慮なく俺たちも使っていけよ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F5B1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F5B1)

    def lambda_F5BE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F5BE)

    def lambda_F5CB():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F5CB)
    Sleep(200)

    #C0743
    ChrTalk(
        0x101,
        (
            "#11P#0000Fああ、分かってる。\x01",
            "手を借りるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x9,
        "#11P話は纏まったようだな。\x02",
    )

    CloseMessageWindow()

    def lambda_F62C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F62C)

    def lambda_F639():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F639)

    def lambda_F646():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F646)
    Sleep(300)
    OP_93(0x9, 0xB4, 0x190)
    Sleep(500)

    #C0745
    ChrTalk(
        0x9,
        "#5P#4S──総員、集合！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(2240, 1100, 7350, 4200)
    MoveCamera(79, 30, 0, 4200)
    OP_6E(260, 4200)
    SetCameraDistance(32250, 4200)
    BeginChrThread(0xA, 0, 0, 59)
    Sleep(200)
    BeginChrThread(0xC, 0, 0, 58)
    Sleep(400)
    BeginChrThread(0xD, 0, 0, 57)
    Sleep(300)
    BeginChrThread(0xB, 0, 0, 60)

    def lambda_F6CC():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F6CC)
    Sleep(10)

    def lambda_F6DC():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F6DC)

    def lambda_F6E9():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F6E9)
    Sleep(8)

    def lambda_F6F9():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F6F9)
    WaitChrThread(0xD, 0)
    Sleep(700)

    #C0746
    ChrTalk(
        0x9,
        (
            "#5P我らテスタメンツは\x01",
            "これより模擬戦闘に突入する！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 60, -1, -1)
    SetChrName("メンバーたち")

    #A0747
    AnonymousTalk(
        0xFF,
        "#5S  ヤーッ！  \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0748
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【テスタメンツの稽古依頼】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_F49E end

    def Function_57_F7F3(): pass

    label("Function_57_F7F3")

    OP_95(0xD, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xD, 2880, 30, 6910, 2000, 0x0)
    OP_93(0xD, 0x13B, 0x190)
    Return()

    # Function_57_F7F3 end

    def Function_58_F823(): pass

    label("Function_58_F823")

    OP_95(0xC, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xC, 2180, 0, 6080, 2000, 0x0)
    OP_93(0xC, 0x13B, 0x190)
    Return()

    # Function_58_F823 end

    def Function_59_F853(): pass

    label("Function_59_F853")

    OP_95(0xA, 9250, 0, 7400, 2000, 0x0)
    OP_95(0xA, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xA, 1330, 0, 5310, 2000, 0x0)
    OP_93(0xA, 0x13B, 0x190)
    Return()

    # Function_59_F853 end

    def Function_60_F897(): pass

    label("Function_60_F897")

    OP_95(0xB, 2460, 20, 2000, 2000, 0x0)
    OP_95(0xB, 2460, 20, 4550, 2000, 0x0)
    OP_95(0xB, 490, 0, 4550, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x190)
    Return()

    # Function_60_F897 end

    SaveToFile()

Try(main)
