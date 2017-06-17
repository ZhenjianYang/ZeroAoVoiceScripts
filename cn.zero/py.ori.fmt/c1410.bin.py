from ZeroScenarioHelper import *

def main():
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
        "瓦吉",                   # 1
        "阿巴斯",                 # 2
        "琴兹",                   # 3
        "贝赛",                   # 4
        "良",                     # 5
        "亚泽尔",                 # 6
        "瓦吉",                   # 7
        "亚修莉",                 # 8
        "莎丽娜",                 # 9
        "盖特纳",                 # 10
        "游客",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客",                   # 15
        "游客",                   # 16
        "古拉斯",                 # 17
        "古拉斯",                 # 18
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
    DeclNpc(-479,    100,     12600,   0,    389,  0x0, 0,   7,   0,   255, 255, 0,   38,  255,  0)
    DeclNpc(0,       0,       5789,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-1269,   0,       12640,   45,   389,  0x0, 0,   9,   0,   0,   0,   0,   40,  255,  0)
    DeclNpc(-1240,   0,       4139,    0,    405,  0x0, 0,   5,   0,   0,   0,   0,   41,  255,  0)
    DeclNpc(-170,    0,       4019,    315,  389,  0x0, 0,   6,   0,   0,   0,   0,   45,  255,  0)
    DeclNpc(-2900,   150,     3500,    0,    405,  0x0, 0,   10,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(-4300,   150,     3500,    0,    405,  0x0, 0,   11,  0,   255, 255, 0,   46,  255,  0)
    DeclNpc(3730,    119,     12600,   0,    405,  0x0, 0,   12,  0,   255, 255, 0,   47,  255,  0)
    DeclNpc(1559,    100,     12600,   0,    405,  0x0, 0,   13,  0,   255, 255, 0,   50,  255,  0)
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
        "Function_6_DA7",          # 06, 6
        "Function_7_2FBD",         # 07, 7
        "Function_8_33C3",         # 08, 8
        "Function_9_3B22",         # 09, 9
        "Function_10_41B9",        # 0A, 10
        "Function_11_4772",        # 0B, 11
        "Function_12_490E",        # 0C, 12
        "Function_13_4BE9",        # 0D, 13
        "Function_14_4DF2",        # 0E, 14
        "Function_15_4F17",        # 0F, 15
        "Function_16_5B41",        # 10, 16
        "Function_17_5B45",        # 11, 17
        "Function_18_5C30",        # 12, 18
        "Function_19_5CB7",        # 13, 19
        "Function_20_5CF0",        # 14, 20
        "Function_21_6D2E",        # 15, 21
        "Function_22_6DCA",        # 16, 22
        "Function_23_6E55",        # 17, 23
        "Function_24_6EF8",        # 18, 24
        "Function_25_7511",        # 19, 25
        "Function_26_854D",        # 1A, 26
        "Function_27_8608",        # 1B, 27
        "Function_28_874B",        # 1C, 28
        "Function_29_948B",        # 1D, 29
        "Function_30_948F",        # 1E, 30
        "Function_31_9568",        # 1F, 31
        "Function_32_961F",        # 20, 32
        "Function_33_9718",        # 21, 33
        "Function_34_97F9",        # 22, 34
        "Function_35_A2AA",        # 23, 35
        "Function_36_A2AE",        # 24, 36
        "Function_37_A348",        # 25, 37
        "Function_38_A3B4",        # 26, 38
        "Function_39_A76B",        # 27, 39
        "Function_40_A804",        # 28, 40
        "Function_41_AA57",        # 29, 41
        "Function_42_AB54",        # 2A, 42
        "Function_43_ABD3",        # 2B, 43
        "Function_44_ACE1",        # 2C, 44
        "Function_45_AD68",        # 2D, 45
        "Function_46_AE19",        # 2E, 46
        "Function_47_AF27",        # 2F, 47
        "Function_48_AFD2",        # 30, 48
        "Function_49_B06B",        # 31, 49
        "Function_50_B105",        # 32, 50
        "Function_51_B227",        # 33, 51
        "Function_52_D9FF",        # 34, 52
        "Function_53_DA72",        # 35, 53
        "Function_54_DAE5",        # 36, 54
        "Function_55_DB58",        # 37, 55
        "Function_56_E852",        # 38, 56
        "Function_57_EB87",        # 39, 57
        "Function_58_EBB7",        # 3A, 58
        "Function_59_EBE7",        # 3B, 59
        "Function_60_EC2B",        # 3C, 60
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C96")
    OP_4B(0x9, 0xFF)

    #C0001
    ChrTalk(
        0x8,
        (
            "#0404F阿巴斯，难得的好日子，\x01",
            "我们就来干一杯吧。\x02\x03",

            "#0400F呵呵，毕竟是歌颂\x01",
            "克洛斯贝尔的重要节日啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    Jump("loc_DA3")

    label("loc_C96")


    #C0002
    ChrTalk(
        0x8,
        (
            "#0404F我们正在商量今天要不要\x01",
            "一起去参观纪念庆典呢。\x02\x03",

            "#0400F……对了，你们也一起来如何？\x01",
            "肯定会很开心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0003F还是免了，不好意思，因为我们正在执勤。\x02\x03",

            "#0001F对了，瓦吉，你是明知如此，\x01",
            "还故意邀请我们的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#0409F啊哈哈！\x01",
            "你可真够死脑筋的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)
    SetChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_DA3")

    TalkEnd(0xFE)
    Return()

    # Function_5_C17 end

    def Function_6_DA7(): pass

    label("Function_6_DA7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E3B")
    Jump("loc_E85")

    label("loc_E3B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E5B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E85")

    label("loc_E5B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E7B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E85")

    label("loc_E7B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E85")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_F61")

    #C0005
    ChrTalk(
        0xE,
        (
            "#0400F（关于阿巴斯这个人，\x01",
            "  其实我也了解得不是很详细。）\x02\x03",

            "（据说，他好像出身于\x01",
            "  塞姆里亚大陆中东部。）\x02\x03",

            "（呵呵……\x01",
            "  总之他很喜欢给自己找事，这倒是不用怀疑的。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB5")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_10EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FC7")

    #C0006
    ChrTalk(
        0xE,
        (
            "#0400F太阳都快下山了啊。\x02\x03",

            "虽然不知道你们要去哪，\x01",
            "但还是早点出发比较好吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10E6")

    label("loc_FC7")


    #C0007
    ChrTalk(
        0xE,
        "#0404F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#0005F瓦吉，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xE,
        (
            "#0400F……没什么，说起来，\x01",
            "今晚好像是满月呢。\x02\x03",

            "#0402F今天的天空很晴朗，\x01",
            "应该能看到美丽的月亮吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#0100F是啊……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0200F但月亮不是\x01",
            "不吉利的象征么……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0303F……在如今这种状况下，\x01",
            "实在是开心不起来呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10E6")

    Jump("loc_2FB5")

    label("loc_10EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1299")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1158")

    #C0013
    ChrTalk(
        0xE,
        (
            "#0400F算了，至于剑蛇帮那边，\x01",
            "我们也会留意的。\x02\x03",

            "你们只要做好\x01",
            "自己的工作就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1294")

    label("loc_1158")


    #C0014
    ChrTalk(
        0xE,
        (
            "#0403F瓦鲁多好像也\x01",
            "开始焦虑起来了呢。\x02\x03",

            "#0400F……他要是能把那种固执要强的性格稍微改改，\x01",
            "这种时候也就能轻松一些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0000F瓦吉，你好像相当\x01",
            "关心瓦鲁多啊。\x02\x03",

            "#0005F其实，你从一开始就一直\x01",
            "很担心剑蛇帮那边的情况吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xE,
        (
            "#0404F呵呵……怎么说呢。\x02\x03",

            "#0402F只是，瓦鲁多那个人嘛，\x01",
            "有些方面确实是让人放不下心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1294")

    Jump("loc_2FB5")

    label("loc_1299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_131C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 6)), scpexpr(EXPR_END)), "loc_1314")

    #C0017
    ChrTalk(
        0xE,
        (
            "#0400F呵呵，你们竟然在和\x01",
            "一科的精英一起行动啊。\x02\x03",

            "正在做什么呢……\x01",
            "算了，有些事情还是不问为好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1317")

    label("loc_1314")

    Call(0, 7)

    label("loc_1317")

    Jump("loc_2FB5")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_13D5")

    #C0018
    ChrTalk(
        0xE,
        (
            "#0400F如今，除了那个叫迪诺\x01",
            "的少年之外，旧城区中似乎\x01",
            "就没有其他服用过那种药物的人了。\x02\x03",

            "只是，那药物究竟是谁散发出去的，\x01",
            "现在还不清楚呢。\x01",
            "我们这边也会留意的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1504")

    label("loc_13D5")


    #C0019
    ChrTalk(
        0xE,
        "#0402F……来了啊。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0001F瓦吉，能拜托你尽快……\x01",
            "将情况告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "#0404F我本来是想先要情报费的，\x01",
            "不过这次就算了吧。\x02\x03",

            "#0406F毕竟，这件事和我们也不是完全无关……\x01",
            "而且情况似乎相当严峻呢。\x02",
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

    label("loc_1504")

    Jump("loc_2FB5")

    label("loc_1509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_17C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_164A")

    #C0022
    ChrTalk(
        0xE,
        (
            "#0404F话说回来……仅仅只是袭击，却没有把\x01",
            "对方的首领干掉，手法实在是不太干净利落呢。\x02\x03",

            "#0402F如果我是鲁巴彻的人，肯定会想出一些\x01",
            "把对方彻底做掉的计划。\x02",
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
            "#0106F（瓦吉果然是个\x01",
            "  危险人物呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C1")

    label("loc_164A")


    #C0024
    ChrTalk(
        0xE,
        (
            "#0400F说起来，听说黑月的事务所\x01",
            "遭到了袭击呢……\x02\x03",

            "#0403F鲁巴彻也真是够乱来的啊。\x01",
            "这种行为不就是在明目张胆地\x01",
            "邀请对方前来复仇吗。\x02",
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
        "#0003F瓦吉都这么说，确实是很有信服力呢……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xE,
        (
            "#0400F呵呵，这不是理所当然的嘛。\x01",
            "我如果站在黑月的立场上，\x01",
            "肯定也会回赠对方一份大礼的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17C1")

    Jump("loc_2FB5")

    label("loc_17C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_18F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_184F")

    #C0027
    ChrTalk(
        0xE,
        (
            "#0403F看起来，市区那边似乎\x01",
            "也陷入骚乱了呢……\x02\x03",

            "#0402F呵呵，难道因为明天是满月，\x01",
            "所以大家的热血全都沸腾了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_184F")


    #C0028
    ChrTalk(
        0xE,
        "#0403F………………………………\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0000F瓦吉？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xE,
        (
            "#0402F不，没什么……\x02\x03",

            "只是有些在意剑蛇帮\x01",
            "那边的情况而已。\x01",
            "他们昨天晚上好像闹得很凶呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18EC")

    Jump("loc_2FB5")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 4)), scpexpr(EXPR_END)), "loc_1AA1")
    SetChrSubChip(0xE, 0x0)
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x109, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_199B")
    Jump("loc_19E5")

    label("loc_199B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BB")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19E5")

    label("loc_19BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19DB")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19E5")

    label("loc_19DB")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19E5")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    #C0031
    ChrTalk(
        0x109,
        (
            "#0501F明、明明是个未成年人，\x01",
            "竟然在大白天公然喝酒，\x01",
            "这可不好吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xE,
        "#0402F啊，这只是普通的果汁而已。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0006F（又面不改色地说谎……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA4")

    label("loc_1AA1")

    Call(0, 9)

    label("loc_1AA4")

    Jump("loc_2FB5")

    label("loc_1AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1B19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 1)), scpexpr(EXPR_END)), "loc_1B09")

    #C0034
    ChrTalk(
        0xE,
        (
            "#0400F总之，请各位慢慢享受吧。\x02\x03",

            "如果有空，三个人\x01",
            "一起喝点奶昔如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0C")

    label("loc_1B09")

    Call(0, 10)

    label("loc_1B0C")

    TalkEnd(0xFE)
    SetChrSubChip(0xE, 0x2)
    Return()

    label("loc_1B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BB0")

    #C0035
    ChrTalk(
        0xE,
        (
            "#0406F别看我现在这样，其实在纪念\x01",
            "庆典期间，我也是很忙的哦。\x02\x03",

            "#0400F呵呵，虽然很遗憾，但今天就\x01",
            "随便敷衍一下，放她们回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB3")

    label("loc_1BB0")

    Call(0, 11)

    label("loc_1BB3")

    Jump("loc_2FB5")

    label("loc_1BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 0)), scpexpr(EXPR_END)), "loc_1C5B")

    #C0036
    ChrTalk(
        0xE,
        (
            "#0400F总之，你们今天也\x01",
            "好好放松一下吧。\x02\x03",

            "阿巴斯的调酒技术\x01",
            "可是十分高超的哦。\x02\x03",

            "呵呵，今天的酒单里\x01",
            "都是些上乘之品哦。\x01",
            "你们也来一杯如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E5A")

    label("loc_1C5B")


    #C0037
    ChrTalk(
        0xE,
        (
            "#0404F呵呵，昨天多谢你们了。\x02\x03",

            "#0400F能跟那对很有名气的游击士二人组同场竞技，\x01",
            "而且比赛本身也非常有趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#0005F瓦吉你……\x01",
            "难道没有疲惫不堪吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0039
    ChrTalk(
        0xE,
        (
            "#0405F哎，疲惫？为什么？\x01",
            "难道你是指昨天的竞赛吗？\x02\x03",

            "#0402F啊哈哈，那不是很平常的娱乐活动嘛。\x02\x03",

            "平时和瓦鲁多打架，\x01",
            "每次也都会那么激烈的。\x02",
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
        "#0003F（真是不可小看不良少年的体力啊……）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x104,
        "#0306F（呼～让我感觉自己已经上了年纪呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 0)

    label("loc_1E5A")

    Jump("loc_2FB5")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1E95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 7)), scpexpr(EXPR_END)), "loc_1E85")
    Call(0, 13)
    Jump("loc_1E88")

    label("loc_1E85")

    Call(0, 12)

    label("loc_1E88")

    Jump("loc_1E90")

    label("loc_1E8D")

    Call(0, 13)

    label("loc_1E90")

    Jump("loc_2FB5")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1ED3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 7)), scpexpr(EXPR_END)), "loc_1EBB")
    Call(0, 14)
    Jump("loc_1EBE")

    label("loc_1EBB")

    Call(0, 12)

    label("loc_1EBE")

    Jump("loc_1EC6")

    label("loc_1EC3")

    Call(0, 14)

    label("loc_1EC6")

    TalkEnd(0xFE)
    SetChrSubChip(0xE, 0x2)
    Return()

    label("loc_1ED3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 5)), scpexpr(EXPR_END)), "loc_1FAB")

    #C0042
    ChrTalk(
        0xE,
        (
            "#0400F最近，克洛斯贝尔的黑道势力中\x01",
            "好像新加入了一个\x01",
            "名叫『黑月』的组织呢。\x02\x03",

            "#0400F近来他们好像在走私渠道方面和鲁巴彻\x01",
            "一直有些小摩擦。\x02\x03",

            "#0406F哎呀哎呀……\x01",
            "只要不要把战火烧到\x01",
            "我们这边就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21FC")

    label("loc_1FAB")


    #C0043
    ChrTalk(
        0xE,
        (
            "#0400F克洛斯贝尔的黑道势力中\x01",
            "最近好像新加入了一个\x01",
            "名叫『黑月』的组织。\x02\x03",

            "似乎是来自东方国家呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0000F嗯，据说是控制着\x01",
            "卡尔瓦德东方人街\x01",
            "的巨大黑手党组织……\x02\x03",

            "#0001F瓦吉，你了解什么内情吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0045
    ChrTalk(
        0xE,
        (
            "#0405F……哎？\x01",
            "虽然还谈不上了解……\x02\x03",

            "#0400F不过，他们近来好像在走私渠道方面和鲁巴彻\x01",
            "一直有些小摩擦。\x02\x03",

            "虽然鲁巴彻好像暂时落了下风，\x01",
            "但也有传闻说，他们已经增强了战斗力。\x02\x03",

            "#0406F战火也许会波及到我们这里，\x01",
            "所以要提高警惕。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0001F是吗……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0301F不过，你这些情报\x01",
            "是从哪里听来的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xE,
        (
            "#0404F呵，探听情报虽然\x01",
            "不是我的专长。\x02\x03",

            "#0402F但我的交际面\x01",
            "毕竟也算很广呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 5)

    label("loc_21FC")

    Jump("loc_2FB5")

    label("loc_2201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2589")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 4)), scpexpr(EXPR_END)), "loc_23B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22B6")

    #C0049
    ChrTalk(
        0xE,
        (
            "#0400F呵呵，最近这段时间，\x01",
            "『特别任务支援科』这个名字\x01",
            "似乎也变得广为人知了呢。\x02\x03",

            "#0404F哈，就保持这种势头，继续加油吧。\x01",
            "我也很期待你们的表现呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23AE")

    label("loc_22B6")


    #C0050
    ChrTalk(
        0xE,
        (
            "#0400F呵呵，最近这段时间，\x01",
            "『特别任务支援科』这个名字\x01",
            "似乎也变得广为人知了呢。\x02\x03",

            "#0409F不过，真要说的话，其实只是\x01",
            "被人当作嘲笑的对象而已呢。\x01",
            "啊哈哈哈哈……！\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0303F……都怪克洛斯贝尔时代周刊，\x01",
            "宣传方式太让人不爽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#0106F是啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_23AE")

    Jump("loc_2584")

    label("loc_23B3")


    #C0053
    ChrTalk(
        0xE,
        (
            "#0400F哎呀，这不是罗伊德和各位嘛。\x02\x03",

            "最近一直都没见到你们，\x01",
            "又在调查些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#0000F不，今天只是在处理一些\x01",
            "琐碎的支援请求而已。\x02\x03",

            "#0006F最近也经常跑去总部帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xE,
        (
            "#0404F呵呵，大概是因为临近纪念庆典，\x01",
            "到处都很热闹，所以警察局也很忙吧。\x02\x03",

            "#0400F总之，就保持这种势头，继续加油吧。\x02\x03",

            "最近这段时间，克洛斯贝尔时代周刊\x01",
            "对你们的评价好像也比以前\x01",
            "强了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0003F嗯，是啊。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0305F（话说～这种鼓励的话，为什么是\x01",
            "  不良团伙的首领对我们说的啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 4)

    label("loc_2584")

    Jump("loc_2FB5")

    label("loc_2589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_25CF")

    #C0058
    ChrTalk(
        0xE,
        (
            "#0400F哎呀呀……今天差不多\x01",
            "也该关门了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2661")

    label("loc_25CF")


    #C0059
    ChrTalk(
        0xE,
        (
            "#0406F哎呀呀……\x01",
            "我接下来还有\x01",
            "工作哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#0000F工作……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xE,
        (
            "#0402F呵呵，秘·密·哦。\x02\x03",

            "如果想得到更多的情报，\x01",
            "可就必须要付情报费了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2661")

    Jump("loc_2FB5")

    label("loc_2666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2720")

    #C0062
    ChrTalk(
        0xE,
        (
            "#0403F白色鬃毛的神狼，守护着\x01",
            "钟声响起的宿命之地──\x01",
            "……大概是这么说的吧？\x02\x03",

            "#0400F七耀教会的圣典中\x01",
            "好像有过这样的记载呢。\x02\x03",

            "#0404F不过，以前从没当真过就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2920")

    label("loc_2720")


    #C0063
    ChrTalk(
        0xE,
        (
            "#0400F听说克洛斯贝尔的\x01",
            "警备队正在山中猎捕\x01",
            "狼形的魔兽？\x02\x03",

            "#0404F哼……狼形吗……\x01",
            "稍微有些让人在意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0001F与其说是在山中猎捕，\x01",
            "其实也只是警备巡逻而已吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0301F话说～这些奇怪的情报，\x01",
            "你到底是从哪里打探来的啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xE,
        (
            "#0404F呵呵……\x01",
            "看来确有其事呢。\x02\x03",

            "#0400F……其实，我只是记得在教会的圣典中\x01",
            "有过那样的记载。\x02\x03",

            "#0403F白色鬃毛的神狼，守护着\x01",
            "钟声响起的宿命之地──\x01",
            "……大概是这么说的吧？\x02\x03",

            "#0400F不过，以前从没当真过就是了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        "#0005F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0100F村长先生的话……\x01",
            "还真是意外的\x01",
            "准确呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2920")

    Jump("loc_2FB5")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_29C7")

    #C0069
    ChrTalk(
        0xE,
        (
            "#0403F那天晚上，确实是承蒙\x01",
            "你们支援科关照了。\x02\x03",

            "#0402F呵呵，以后要是有什么事，尽管来找我。\x01",
            "只要我有兴致，\x01",
            "说不定可以助你们一臂之力哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B9E")

    label("loc_29C7")


    #C0070
    ChrTalk(
        0xE,
        (
            "#0405F哎呀，这不是罗伊德嘛。\x02\x03",

            "#0402F真开心呢……\x01",
            "你是来找我的吗？\x02",
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
            "#0013F哎！？那个……\x02\x03",

            "#0013F没有什么特别的意思，\x01",
            "只是过来道个谢而已……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0072
    ChrTalk(
        0x103,
        (
            "#0211F罗伊德前辈的反应很不自然，\x01",
            "明显心慌了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        (
            "#0403F呵呵……不开玩笑了。\x02\x03",

            "#0400F那天晚上，真是承蒙\x01",
            "你们支援科的关照了。\x02\x03",

            "#0402F以后要是有什么事，尽管来找我。\x01",
            "只要我有兴致，\x01",
            "说不定可以助你们一臂之力哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0003F啊，那到时候就拜托了。\x01",
            "（总觉和他说话很累呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2B9E")

    Jump("loc_2FB5")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2C6E")

    #C0075
    ChrTalk(
        0xE,
        (
            "#0404F我已经向成员们交代过了，\x01",
            "让他们不要再擅自\x01",
            "做出一些不妥的行动。\x02\x03",

            "#0400F至少在今天一天，\x01",
            "应该不会再有什么麻烦了。\x02\x03",

            "#0402F呵呵……要进行调查的话，\x01",
            "最好还是应该赶快行动吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9B")

    label("loc_2C6E")


    #C0076
    ChrTalk(
        0xE,
        (
            "#0404F我已经向成员们交代过了，\x01",
            "让他们不要再擅自\x01",
            "做出一些不妥的行动。\x02\x03",

            "#0400F至少在今天一天，\x01",
            "应该不会再有什么麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#0001F是吗……那可真是多谢了。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xE,
        (
            "#0402F哈哈……真讨厌啊。\x01",
            "我又不是为了你们\x01",
            "才约束大家的。\x02",
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
            "#0402F只是趁现在积蓄一下战斗力，\x01",
            "到时候才能去血洗\x01",
            "剑蛇帮而已啊。\x02",
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
            "#0306F（虽然外表很可爱，\x01",
            "  但不良少年终究是不良少年呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2E9B")

    Jump("loc_2FB5")

    label("loc_2EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2F08")

    #C0081
    ChrTalk(
        0xE,
        (
            "#0400F呵呵……\x01",
            "一定要带些有趣的消息回来啊。\x02\x03",

            "短时间之内，\x01",
            "我倒是可以在这里等等你们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FB5")

    label("loc_2F08")


    #C0082
    ChrTalk(
        0xE,
        (
            "#0400F你是叫罗伊德吧？\x01",
            "还真是个很有意思的人。\x02\x03",

            "#0402F呵呵……以后也可以\x01",
            "随时来这里玩哦。\x01",
            "还有，一定要带些有趣的消息回来啊。\x02\x03",

            "短时间之内，\x01",
            "我倒是可以在这里等等你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2FB5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_DA7 end

    def Function_7_2FBD(): pass

    label("Function_7_2FBD")

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
            "#0402F哎呀，这不是……\x01",
            "你们这次带了稀客过来啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x10A,
        (
            "#0603F好久不见了啊，\x01",
            "瓦吉·赫米斯菲亚。\x02\x03",

            "#0601F你还没打算停止这种\x01",
            "无聊的不良少年游戏吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xE,
        (
            "#0404F呵呵，同样的话都回答过很多次了，\x01",
            "对我来说，其实怎样都无所谓。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3165():
        TurnDirection(0x101, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3165)

    def lambda_3172():
        TurnDirection(0x102, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3172)

    def lambda_317F():
        TurnDirection(0x103, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_317F)

    def lambda_318C():
        TurnDirection(0x104, 0x10A, 350)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_318C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0086
    ChrTalk(
        0x101,
        (
            "#0011F达德利搜查官……\x01",
            "你们原来就认识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x10A,
        (
            "#0601F两年前就认识了，那时这小子刚来到旧城区，\x01",
            "并建立起这个组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xE,
        (
            "#0404F呵呵，即使在搜查一科中，\x01",
            "他也是唯一一位会定期\x01",
            "来旧城区视察的人哦。\x02\x03",

            "#0402F不过，这好像也是受\x01",
            "我不认识的某人所影响呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        "#0005F某人……？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x10A,
        "#0603F无聊的闲话就到此为止吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x9, 350)

    #C0091
    ChrTalk(
        0x10A,
        (
            "#0601F#6P阿巴斯，\x01",
            "看好这小子，不要让他对瓦鲁多\x01",
            "做出一些无意义的挑衅行为。\x02\x03",

            "可不要逼迫我们一科正式介入啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 350)

    #C0092
    ChrTalk(
        0x9,
        "……明白了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    #C0093
    ChrTalk(
        0xE,
        "#0404F哎呀呀。\x02",
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

    # Function_7_2FBD end

    def Function_8_33C3(): pass

    label("Function_8_33C3")

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
            "#0403F#5P剑蛇帮新收的那个小跑腿，\x01",
            "好像是叫迪诺吧。\x02\x03",

            "#0401F他最近的样子好像很奇怪呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_355E")

    #C0095
    ChrTalk(
        0x104,
        (
            "#0303F#6P嗯，我们也有所耳闻。\x01",
            "好像是提出和干部单挑，然后把对方给怎么样了……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        (
            "#0402F#5P然后，听说他昨天\x01",
            "终于向瓦鲁多发出了挑战。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360C")

    label("loc_355E")


    #C0097
    ChrTalk(
        0x101,
        "#0008F#12P果然如此吗……\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xE,
        (
            "#0406F#5P嗯，完全不像是个新人，\x01",
            "态度相当傲慢狂暴。\x02\x03",

            "#0401F平时也经常会向我们的人\x01",
            "挑衅，然后……\x02\x03",

            "#0402F昨天他终于主动向\x01",
            "瓦鲁多提出单挑了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360C")

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
        "#0007F#12P啊，和那个瓦鲁多……！？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        (
            "#0402F#5P正是。\x02\x03",

            "#0404F我也只是听说而已，\x01",
            "据说他的速度和力量都相当厉害，\x01",
            "和瓦鲁多不相上下，打得很精彩呢。\x02\x03",

            "据说，瓦鲁多最后拼尽了全力，\x01",
            "总算是勉强取胜了……\x02\x03",

            "#0400F而迪诺在战败之后，\x01",
            "就直接飞奔离去了。\x01",
            "今天早上，好像谁都没有见到他。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#0306F#6P这真是很危险啊……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#0108F#12P这样的话……\x01",
            "事态确实不一般呢。\x02",
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
            "#0404F#5P那么……\x02\x03",

            "#0402F果然是某种药物的影响吧？\x02",
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
        "#0011F#12P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#0105F#12P你是从哪里知道的……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xE,
        (
            "#0405F#5P啊，果然是真的吗？\x02\x03",

            "#0404F最近这段时间，克洛斯贝尔流传着一个都市传说，\x01",
            "叫做『可以实现愿望的药』。\x01",
            "我就在想，会不会和那个有关。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        "#0211F#6P原来是在套我们的话吗……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#0301F#6P喂，这些事情无论如何\x01",
            "也不要到处说啊！\x02\x03",

            "毕竟事态有些特殊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        (
            "#0409F#5P呵呵，我当然明白这些。\x02\x03",

            "#0400F#5P还好，在这旧城区，\x01",
            "除了那个叫迪诺的少年之外，\x01",
            "似乎还没有其他人服用过那种药物呢。\x02\x03",

            "#0404F只是，目前还不知道是什么人\x01",
            "将这种药流出来的。\x01",
            "关于这方面，我也会多加留意的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        "#0000F#12P……真是多谢了，瓦吉。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#0100F#12P我们很期待你的消息。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -2690, 0, 10250, 360)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetScenarioFlags(0xC8, 1)
    OP_29(0x4C, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_8_33C3 end

    def Function_9_3B22(): pass

    label("Function_9_3B22")

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
            "#0402F哎呀，这不是罗伊德和各位嘛，\x01",
            "今天也在努力工作吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0003F嗯，各种各样的工作都堆积成山了。\x02\x03",

            "#0000F旧城区这边没什么特别情况吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xE,
        (
            "#0403F………………………………\x02\x03",

            "#0400F算是吧，圣书会还是和\x01",
            "平时一样。\x02",
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
            "#0400F呵呵，不过……\x02\x03",

            "#0402F这次还带了位稀客过来啊，\x01",
            "好像是警备队的人？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#0000F嗯，正好有些事情要帮忙，\x01",
            "所以暂时和我们同行……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x109,
        (
            "#0500F初次见面，\x01",
            "我是诺艾尔·希卡。\x02\x03",

            "您是罗伊德警官\x01",
            "他们的朋友吧？\x01",
            "请多多指教。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    #C0118
    ChrTalk(
        0xE,
        (
            "#0402F嘿……\x02\x03",

            "#0404F呵呵，这位姐姐，\x01",
            "该说你太过一本正经，\x01",
            "还是该说非常有捉弄的价值呢？\x02",
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
        "#0505F什么……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        "#0011F喂，瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        (
            "#0403F我说，对我这种不良团伙的小鬼，\x01",
            "没必要特意使用礼貌用语吧。\x02\x03",

            "#0402F相比之下，\x01",
            "面对你这样严肃认真的姐姐，我宁愿\x01",
            "被居高临下地唠叨教训一番呢。\x02\x03",

            "#0405F啊，但这并不代表我是个Ｍ哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        (
            "#0503F你、你可真是……\x02\x03",

            "#0501F别人认真地和你打招呼，\x01",
            "你却用那种嘲弄的态度回应，\x01",
            "这样是不是不太好呢？\x02\x03",

            "而且你那是什么打扮啊？\x01",
            "请穿得正经一点，有个年轻人的样子！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xE,
        "#0409F没错没错！要的就是这种感觉⊥\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x109,
        "#0505F呜……\x02",
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
            "#0003F（把一丝不苟的上士\x01",
            "  带到这种地方来，\x01",
            "  不得不说，真是有点失策呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#0300F（哈哈，不过他们两个\x01",
            "  倒是意外地投缘呢。）\x02",
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

    # Function_9_3B22 end

    def Function_10_41B9(): pass

    label("Function_10_41B9")

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
        "#1110F啊，是瓦吉～\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x2)

    #C0128
    ChrTalk(
        0xE,
        (
            "#0402F哎呀，好久不见。\x01",
            "你最近还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x153,
        (
            "#1109F嗯，琪雅很好哦。\x01",
            "每天早上都有好好吃饭！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xE,
        "#0402F呵呵，那就好。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)

    #C0131
    ChrTalk(
        0xE,
        (
            "#0404F……看样子，\x01",
            "总算是避过风头了吗？\x02\x03",

            "#0400F听说鲁巴彻那边\x01",
            "也打算不再深究了。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#0000F嗯，事情终于在今天早上平息了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43E5")

    #C0133
    ChrTalk(
        0x102,
        (
            "#0100F所以我们就带小琪雅\x01",
            "到街上熟悉一下。\x02\x03",

            "#0101F……瓦吉，\x01",
            "请不要对小琪雅灌输一些\x01",
            "奇怪的东西哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E7")

    label("loc_43E5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4465")

    #C0134
    ChrTalk(
        0x103,
        (
            "#0200F所以我们就带琪雅\x01",
            "到市里熟悉一下。\x02\x03",

            "#0203F……瓦吉先生，\x01",
            "拜托你不要对小琪雅灌输一些\x01",
            "奇怪的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44E7")

    label("loc_4465")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44E7")

    #C0135
    ChrTalk(
        0x104,
        (
            "#0300F于是我们就带着阿琪，\x01",
            "来街上熟悉一下环境。\x02\x03",

            "#0301F……喂，瓦吉，你可别对阿琪\x01",
            "灌输一些莫名其妙的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44E7")


    #C0136
    ChrTalk(
        0x101,
        (
            "#0003F是啊……\x02\x03",

            "#0001F瓦吉，请一定要\x01",
            "注意措辞哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xE,
        (
            "#0404F呵呵，说得我真伤心啊。\x02\x03",

            "#0400F话说回来，看你们两个的样子，\x01",
            "完全就像是监护人嘛。\x02\x03",

            "是想做她临时的\x01",
            "爸爸妈妈吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4618")

    #C0138
    ChrTalk(
        0x102,
        "#0105F大、大概算是吧……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，不管怎么说，在找到她的家人之前，\x01",
            "我们确实就算是她的监护人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4753")

    label("loc_4618")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46AF")

    #C0140
    ChrTalk(
        0x103,
        (
            "#0211F让我来当妈妈的话，\x01",
            "实在是有些勉强吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，不管怎么说，在找到她的家人之前，\x01",
            "我们确实就算是她的监护人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4753")

    label("loc_46AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4753")

    #C0142
    ChrTalk(
        0x104,
        (
            "#0309F哦，这样的话，\x01",
            "我是爸爸，罗伊德是妈妈吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0003F那个……\x02\x03",

            "#0000F算了，不管怎么说，在找到她的家人之前，\x01",
            "我们确实就算是她的监护人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4753")

    SetScenarioFlags(0xB0, 1)
    SetChrPos(0xE, -2600, 50, 12600, 0)
    SetChrSubChip(0xE, 0x2)
    SetChrSubChip(0xF, 0x1)
    EventEnd(0x5)
    Return()

    # Function_10_41B9 end

    def Function_11_4772(): pass

    label("Function_11_4772")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)
    SetChrSubChip(0xE, 0x2)

    #C0144
    ChrTalk(
        0x12,
        "可以坐在你旁边吗～？\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x12,
        (
            "那个，我们不小心\x01",
            "迷了路呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x13,
        (
            "这一带的坏人可真多啊。\x01",
            "真是很不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x13,
        (
            "不过，能遇到瓦吉先生，可真是超级幸运⊥\x01",
            "哈哈～\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xE,
        (
            "#0403F………………………………\x02\x03",

            "#0400F呵，是吗？\x01",
            "……不过，真遗憾啊。\x02\x03",

            "#0402F其实我才是这里\x01",
            "最大的恶人呢。\x02",
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
        "#0001F（瓦吉……这家伙………）\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#0306F（应对还真是熟练啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_11_4772 end

    def Function_12_490E(): pass

    label("Function_12_490E")


    #C0151
    ChrTalk(
        0xE,
        (
            "#0402F呵呵，各位辛苦了。\x02\x03",

            "听说，不仅是我们的成员，\x01",
            "连剑蛇帮的低级成员\x01",
            "也接受了你们的训练呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0003F嗯……\x01",
            "结果还算不错吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4998():
        TurnDirection(0x0, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4998)

    def lambda_49A5():
        TurnDirection(0x1, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_49A5)

    def lambda_49B2():
        TurnDirection(0x2, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_49B2)

    def lambda_49BF():
        TurnDirection(0x3, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_49BF)
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

    def lambda_4A33():
        TurnDirection(0x0, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4A33)

    def lambda_4A40():
        TurnDirection(0x1, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4A40)

    def lambda_4A4D():
        TurnDirection(0x2, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4A4D)

    def lambda_4A5A():
        TurnDirection(0x3, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4A5A)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)

    #C0153
    ChrTalk(
        0x102,
        (
            "#0101F（但那个叫阿巴斯的人，\x01",
            "  究竟是何方神圣呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#0306F（他的能力好像很强，\x01",
            "  游刃自若地掌控着状况呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xE,
        (
            "#0404F（呵呵，这个嘛。）\x02\x03",

            "#0400F（据说他是出身于塞姆里亚\x01",
            "  大陆中东部的……）\x02\x03",

            "（哈，总而言之，他自愿给我\x01",
            "  这样的怪人担当帮手，\x01",
            "  显然很喜欢给自己找事，这倒是不用怀疑的。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xE, 500)
    Sleep(300)

    #C0156
    ChrTalk(
        0x9,
        "我听到了哦，瓦吉。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4BD7")
    OP_93(0x9, 0xB4, 0x0)
    Jump("loc_4BDE")

    label("loc_4BD7")

    OP_93(0x9, 0x0, 0x0)

    label("loc_4BDE")

    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x8F, 7)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_12_490E end

    def Function_13_4BE9(): pass

    label("Function_13_4BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4CC5")

    #C0157
    ChrTalk(
        0xE,
        (
            "#0404F说起来，这个旧城区里住着\x01",
            "一个充满魅力的东方女孩。\x02\x03",

            "#0400F呵呵，据说她就是那个被破格提拔为\x01",
            "彩虹剧团新剧目女二号的团员呢。\x02\x03",

            "#0402F但是不管怎么想，她那么丰满，\x01",
            "肯定会影响到表演吧。\x01",
            "呵呵，不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DF1")

    label("loc_4CC5")


    #C0158
    ChrTalk(
        0xE,
        (
            "#0405F咦……\x01",
            "你们怎么都皱着眉头呢？\x02\x03",

            "#0400F呵呵，莫非又被卷进\x01",
            "什么麻烦事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#0001F……嗯，说来话长。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xE,
        (
            "#0402F虽然不知道发生了什么，\x01",
            "总之，请继续加油吧。\x02\x03",

            "我也很期待彩虹剧团\x01",
            "的新剧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        "#0301F（明明什么都知道嘛。）\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        (
            "#0200F（也没准只是故意这么说，\x01",
            "  想借此套出我们的话……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_4DF1")

    Return()

    # Function_13_4BE9 end

    def Function_14_4DF2(): pass

    label("Function_14_4DF2")

    SetChrSubChip(0xE, 0x2)

    #C0163
    ChrTalk(
        0xE,
        (
            "#0402F嘿，这些货好像\x01",
            "很危险吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xF,
        "并不危险。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xF,
        (
            "我可不会订购\x01",
            "自己处理不了的货。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_END)), "loc_4EED")
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
        "#0001F（好像正在谈话呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F13")

    label("loc_4EED")


    #C0167
    ChrTalk(
        0x101,
        "#0006F（在、在说些什么呢……？）\x02",
    )

    CloseMessageWindow()

    label("loc_4F13")

    SetScenarioFlags(0x0, 0)

    label("loc_4F16")

    Return()

    # Function_14_4DF2 end

    def Function_15_4F17(): pass

    label("Function_15_4F17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F40")
    Call(0, 55)
    Return()

    label("loc_4F40")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_516E")

    #C0168
    ChrTalk(
        0x9,
        (
            "希望你们能指导圣书会的成员\x01",
            "学习防身术。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "让他们见识一下警察特有的压制格斗技，\x01",
            "可以吗？\x02",
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
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50FD")
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

    label("loc_50FD")


    #C0170
    ChrTalk(
        0x101,
        (
            "#0001F……请再稍等一下。\x01",
            "我们也需要准备准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x9,
        (
            "我们今天一整天都有空。\x01",
            "你们做好充足准备之后再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_516E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_51AB")

    #C0172
    ChrTalk(
        0x9,
        "这边没有异常。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        (
            "请你们继续\x01",
            "进行调查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_51AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_523A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_END)), "loc_51FF")

    #C0174
    ChrTalk(
        0x9,
        "……这边的事情就交给瓦吉吧。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x9,
        (
            "请你们继续\x01",
            "进行调查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5235")

    label("loc_51FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_END)), "loc_5223")

    #C0176
    ChrTalk(
        0x9,
        "……有什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5235")

    label("loc_5223")


    #C0177
    ChrTalk(
        0x9,
        "瓦吉出门了。\x02",
    )

    CloseMessageWindow()

    label("loc_5235")

    Jump("loc_5B3D")

    label("loc_523A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5260")

    #C0178
    ChrTalk(
        0x9,
        "找瓦吉有什么事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_5260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_52BF")

    #C0179
    ChrTalk(
        0x9,
        (
            "从上周开始，剑蛇帮的情况\x01",
            "好像就有些奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_52BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_533C")

    #C0181
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        "想点单的话和我说就好。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#0006F（这个人的态度还是\x01",
            "  这么冷淡生硬呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_533C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_54E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_53BB")

    #C0184
    ChrTalk(
        0x9,
        (
            "……瓦吉的判断不会出问题，\x01",
            "全都交给他来判断吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jump("loc_54DF")

    label("loc_53BB")


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
            "希望你们不要把瓦吉卷进\x01",
            "警察的纠纷里。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x101,
        (
            "#0006F米修拉姆的事件\x01",
            "是瓦吉自己决定要插手的……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "……是瓦吉的判断吗…………\x01",
            "………………那就没问题了。\x02",
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
            "#0006F（态度的变化好像\x01",
            "  莫名地果断呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_54DF")

    Jump("loc_5B3D")

    label("loc_54E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5607")

    #C0190
    ChrTalk(
        0x9,
        "瓦吉出门工作了。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "如果找他有什么事，\x01",
            "等以后有机会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5602")

    #C0192
    ChrTalk(
        0x101,
        "#0005F工作……？\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        "我没有义务回答你们。\x02",
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
        "#0006F（一点都没变，还是这么冷淡生硬啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5602")

    Jump("loc_5B3D")

    label("loc_5607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5662")

    #C0195
    ChrTalk(
        0x9,
        (
            "在纪念庆典期间，\x01",
            "我们推出了特别鸡尾酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        "有兴趣的话就点一杯尝尝吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_5662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56AD")

    #C0197
    ChrTalk(
        0x9,
        "……今天临时休业。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "想喝东西的话，\x01",
            "就请改日再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_56AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_56E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_56DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 1)), scpexpr(EXPR_END)), "loc_56D3")
    Call(0, 18)
    Jump("loc_56D6")

    label("loc_56D3")

    Call(0, 17)

    label("loc_56D6")

    Jump("loc_56DE")

    label("loc_56DB")

    Call(0, 18)

    label("loc_56DE")

    Jump("loc_5B3D")

    label("loc_56E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5719")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 1)), scpexpr(EXPR_END)), "loc_5709")
    Call(0, 19)
    Jump("loc_570C")

    label("loc_5709")

    Call(0, 17)

    label("loc_570C")

    Jump("loc_5714")

    label("loc_5711")

    Call(0, 19)

    label("loc_5714")

    Jump("loc_5B3D")

    label("loc_5719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_582E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_579E")

    #C0199
    ChrTalk(
        0x9,
        (
            "为了防止那群黑手党潜入旧城区，\x01",
            "我们准备开始在这里巡逻。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "因为我们自己也不想让\x01",
            "之前那种事件再度发生。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5829")

    label("loc_579E")


    #C0201
    ChrTalk(
        0x9,
        (
            "如果黑手党之间的斗争不断升级，\x01",
            "说不定也会影响到我们这边。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        "……我们也必须采取些措施了。\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "首先要做的就是\x01",
            "在旧城区定期巡逻。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5829")

    Jump("loc_5B3D")

    label("loc_582E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5911")

    #C0204
    ChrTalk(
        0x9,
        (
            "听说最近这段时间，危险事件\x01",
            "好像有所增多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_590C")
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
        "……不，没什么。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_590C")

    Jump("loc_5B3D")

    label("loc_5911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_596B")

    #C0207
    ChrTalk(
        0x9,
        (
            "我没打算要干预\x01",
            "成员的私事。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "是否要加入圣书会就交给\x01",
            "大家自行判断。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_596B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_59FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_59B8")

    #C0209
    ChrTalk(
        0x9,
        "亚泽尔由我们来照顾就好。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        "不需要多余的担心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_59F6")

    label("loc_59B8")


    #C0211
    ChrTalk(
        0x9,
        (
            "亚泽尔还需要\x01",
            "去医院复查。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        "因为他之前昏迷了很久。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_59F6")

    Jump("loc_5B3D")

    label("loc_59FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5AA0")

    #C0213
    ChrTalk(
        0x9,
        "……本店已经开业了。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        (
            "如果想吃东西，\x01",
            "就和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A9B")

    #C0215
    ChrTalk(
        0x101,
        "#0003F谢、谢谢……\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#0301F（话说，这家店果然是\x01",
            "  这个大块头开的啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_5A9B")

    Jump("loc_5B3D")

    label("loc_5AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5AF3")

    #C0217
    ChrTalk(
        0x9,
        (
            "如果探听到什么情报的话，\x01",
            "就去告诉瓦吉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        "没必要和我们说。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B3D")

    label("loc_5AF3")


    #C0219
    ChrTalk(
        0x9,
        (
            "……我们正在等待\x01",
            "医院那边的联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "如果话说完了，\x01",
            "就赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B3D")

    TalkEnd(0x9)
    Return()

    # Function_15_4F17 end

    def Function_16_5B41(): pass

    label("Function_16_5B41")

    Call(0, 15)
    Return()

    # Function_16_5B41 end

    def Function_17_5B45(): pass

    label("Function_17_5B45")


    #C0221
    ChrTalk(
        0x9,
        "把这个拿去吧。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '秘水『桃源乡』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('秘水『桃源乡』', 1)

    #C0223
    ChrTalk(
        0x101,
        "#0005F谢、谢谢……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x103,
        (
            "#0203F（是刚才的工作报酬吧。但他的态度\x01",
            "  太过生硬，让人难以判断呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        "#0100F（算了，我们就先收下吧。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 1)
    Return()

    # Function_17_5B45 end

    def Function_18_5C30(): pass

    label("Function_18_5C30")


    #C0226
    ChrTalk(
        0x9,
        (
            "……那么。\x01",
            "为了应对纪念庆典，\x01",
            "我们也该开始做准备了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#0005F（……………………？\x01",
            "  这家酒吧难道也打算\x01",
            "  展开优惠活动吗。）\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_18_5C30 end

    def Function_19_5CB7(): pass

    label("Function_19_5CB7")


    #C0228
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        "不要耽误瓦吉的时间。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_19_5CB7 end

    def Function_20_5CF0(): pass

    label("Function_20_5CF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5DFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5D71")

    #C0230
    ChrTalk(
        0xA,
        (
            "堂堂正正地战斗，然后战胜对手。\x01",
            "圣书会绝对不会使用\x01",
            "卑鄙的手段。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xA,
        (
            "咳……你们也给我\x01",
            "好好记住吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFA")

    label("loc_5D71")


    #C0232
    ChrTalk(
        0xA,
        (
            "剑蛇帮的战斗力已经削弱了，\x01",
            "现在正是击溃他们的大好时机……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xA,
        (
            "不过……还是算了，瓦吉绝对\x01",
            "不会那么做的。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        "他就是那样的人啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5DFA")

    Jump("loc_6D2A")

    label("loc_5DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5E80")

    #C0235
    ChrTalk(
        0xA,
        (
            "瓦吉从今天早上开始，\x01",
            "就一直是一脸严肃的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xA,
        (
            "……我还是第一次见到\x01",
            "那种样子的瓦吉呢，\x01",
            "发生什么事了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D2A")

    label("loc_5E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_5F9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5ED8")

    #C0237
    ChrTalk(
        0xA,
        (
            "要是能得到瓦吉的许可，\x01",
            "像那种新人，轻轻松松就能收拾掉了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F99")

    label("loc_5ED8")


    #C0238
    ChrTalk(
        0xA,
        (
            "咳……剑蛇帮的底层成员竟会如此嚣张，\x01",
            "确实是很蹊跷啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xA,
        (
            "那个少年我们也是认识的。\x01",
            "因为他几乎每天都会来找我们麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xA,
        (
            "……不过，瓦吉却说\x01",
            "不要对他出手。\x01",
            "可恶，真是咽不下这口气……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5F99")

    Jump("loc_6D2A")

    label("loc_5F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_608D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_5FE8")

    #C0241
    ChrTalk(
        0xA,
        (
            "这次出了这么大的事情，\x01",
            "警察也不得不出动了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6088")

    label("loc_5FE8")


    #C0242
    ChrTalk(
        0xA,
        (
            "由于黑手党之间争斗不断，\x01",
            "我老爸工作的乌尔斯拉医院\x01",
            "好像也运进了很多伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        "……看起来还真不是谣传呢。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xA,
        (
            "哼，在市区中心，\x01",
            "竟然干出了那么大胆的事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6088")

    Jump("loc_6D2A")

    label("loc_608D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6157")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_60D8")

    #C0245
    ChrTalk(
        0xA,
        (
            "剑蛇帮的那群混蛋……\x01",
            "最近又开始\x01",
            "嚣张起来了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6152")

    label("loc_60D8")


    #C0246
    ChrTalk(
        0xA,
        (
            "我昨天在大街上\x01",
            "被剑蛇帮的人缠住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xA,
        (
            "哼……一点都没变，\x01",
            "还是一群品行低劣的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xA,
        (
            "真想赶快把他们\x01",
            "都干掉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6152")

    Jump("loc_6D2A")

    label("loc_6157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_626A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_61EF")

    #C0249
    ChrTalk(
        0xA,
        (
            "一切都要听从瓦吉的意思，\x01",
            "现在也只能交给瓦吉来处理了。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "……瓦、瓦吉，对不起。\x01",
            "本想趁瓦吉回来之前\x01",
            "把她们打发走，可是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6265")

    label("loc_61EF")


    #C0251
    ChrTalk(
        0xA,
        (
            "咳、咳咳……\x01",
            "你们几个，不要打扰到瓦吉哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        (
            "『全都要听从瓦吉的意思』。\x01",
            "如果是阿巴斯的话，\x01",
            "肯定会这么说吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6265")

    Jump("loc_6D2A")

    label("loc_626A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_62C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_62C1")

    #C0253
    ChrTalk(
        0xA,
        (
            "瓦吉和阿巴斯\x01",
            "都出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xA,
        (
            "我、我们必须加油\x01",
            "把店看好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C4")

    label("loc_62C1")

    Call(0, 21)

    label("loc_62C4")

    Jump("loc_6D2A")

    label("loc_62C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_63F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_635B")

    #C0255
    ChrTalk(
        0xA,
        (
            "和剑蛇帮之间的紧张关系，\x01",
            "在短时间内仍然会持续。\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xA,
        (
            "……算了，毕竟到了纪念庆典。\x01",
            "决斗什么的，就暂时延后吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63F0")

    label("loc_635B")


    #C0257
    ChrTalk(
        0xA,
        (
            "临近纪念庆典，\x01",
            "黑手党的那些家伙\x01",
            "好像也变老实了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xA,
        (
            "和剑蛇帮之间的紧张关系\x01",
            "也暂时停止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        (
            "哎呀呀，和他们的决斗\x01",
            "就暂时推延一阵子吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_63F0")

    Jump("loc_6D2A")

    label("loc_63F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_642B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 2)), scpexpr(EXPR_END)), "loc_641B")
    Call(0, 23)
    Jump("loc_641E")

    label("loc_641B")

    Call(0, 22)

    label("loc_641E")

    Jump("loc_6426")

    label("loc_6423")

    Call(0, 23)

    label("loc_6426")

    Jump("loc_6D2A")

    label("loc_642B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_658F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_64D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 2)), scpexpr(EXPR_END)), "loc_64CB")

    #C0260
    ChrTalk(
        0xA,
        (
            "最近这段时间，鲁巴彻的家伙\x01",
            "好像一直鬼鬼祟祟的。\x01",
            "我们也要增加巡逻的力度。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xA,
        (
            "哼……下次要是再发现他们，\x01",
            "绝对不会轻饶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64CE")

    label("loc_64CB")

    Call(0, 22)

    label("loc_64CE")

    Jump("loc_658A")

    label("loc_64D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_651F")

    #C0262
    ChrTalk(
        0xA,
        (
            "瓦吉的夜间工作\x01",
            "本来就很多了，\x01",
            "希望他能注意自己的身体啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658A")

    label("loc_651F")


    #C0263
    ChrTalk(
        0xA,
        (
            "瓦吉好像又\x01",
            "通宵喝酒了……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xA,
        (
            "当然，我不是对瓦吉\x01",
            "有什么不满。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xA,
        "但希望他能好好注意自己的身体。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_658A")

    Jump("loc_6D2A")

    label("loc_658F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6601")

    #C0266
    ChrTalk(
        0xA,
        (
            "欢乐街和后巷那一带好像也是\x01",
            "事件的多发之地。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "哼……这都是因为你们警察\x01",
            "玩忽职守所造成的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D2A")

    label("loc_6601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_6728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_668B")

    #C0268
    ChrTalk(
        0xA,
        (
            "早晚要和剑蛇帮的那些家伙\x01",
            "做个彻底了结。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "但在纪念庆典之前，暂时休战。\x01",
            "警察和官员在场的话，\x01",
            "就非常扫兴了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6723")

    label("loc_668B")


    #C0270
    ChrTalk(
        0xA,
        (
            "最近这段时间，和剑蛇帮\x01",
            "连一次像样的架都没打成。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "都是因为临近纪念庆典，警察和官员们\x01",
            "一批接一批的不断跑来。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xA,
        (
            "真是让人败兴啊。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6723")

    Jump("loc_6D2A")

    label("loc_6728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_67EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_677C")

    #C0273
    ChrTalk(
        0xA,
        "先不提这个……\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "亚泽尔他不会真的打算\x01",
            "离开组织吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67EA")

    label("loc_677C")


    #C0275
    ChrTalk(
        0xA,
        (
            "刚才，剑蛇帮的人从广场那边\x01",
            "过来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "那些家伙该不会是\x01",
            "又开始得意忘形了吧，\x01",
            "真是一群碍眼的家伙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_67EA")

    Jump("loc_6D2A")

    label("loc_67EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_692B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_685E")

    #C0277
    ChrTalk(
        0xA,
        (
            "我也学习过武术哦，\x01",
            "对徒手格斗还是很有自信的。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xA,
        (
            "……当然，还远远比不上\x01",
            "瓦吉啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6926")

    label("loc_685E")


    #C0279
    ChrTalk(
        0xA,
        (
            "最近都没再和剑蛇帮的人\x01",
            "打过架了。\x01",
            "真是好无聊啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xA,
        (
            "但也不能放任自己的身手退步。\x01",
            "看来也只能在平时多练习一下\x01",
            "弹弓射击了。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xA,
        (
            "顺便一说，我从小就\x01",
            "开始习武呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xA,
        "对徒手格斗还是很有自信的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6926")

    Jump("loc_6D2A")

    label("loc_692B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_6A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_69B6")

    #C0283
    ChrTalk(
        0xA,
        (
            "亚泽尔总算是出院了。\x01",
            "感觉心中最后的一块石头也落了地啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xA,
        (
            "接下来，只要去和剑蛇帮的家伙们\x01",
            "做个了结就可以了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A7B")

    label("loc_69B6")


    #C0285
    ChrTalk(
        0xA,
        (
            "亚泽尔总算出院了啊，\x01",
            "我们也终于可以放下心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xA,
        (
            "……老实说，不得不向你们表示感谢。\x01",
            "不过，可不要太得意忘形啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xA,
        (
            "我们圣书会的成员就相当于瓦吉的手足。\x01",
            "可以下达命令的人，\x01",
            "只有首领瓦吉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_6A7B")

    Jump("loc_6D2A")

    label("loc_6A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6AFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 3)), scpexpr(EXPR_END)), "loc_6AF2")

    #C0288
    ChrTalk(
        0xA,
        "真担心正在住院的亚泽尔啊。\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xA,
        (
            "反正我老爸也在医院工作，\x01",
            "不然明天直接去看看他好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AF5")

    label("loc_6AF2")

    Call(0, 24)

    label("loc_6AF5")

    Jump("loc_6D2A")

    label("loc_6AFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6B8D")

    #C0290
    ChrTalk(
        0xA,
        (
            "被打倒的亚泽尔，\x01",
            "伤口是被钝器击打造成的，同时还有轻微的撕裂。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xA,
        (
            "那明显是被剑蛇帮的钉棍所造成的，\x01",
            "绝对不会有错！\x01",
            "……可恶……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D2A")

    label("loc_6B8D")


    #C0292
    ChrTalk(
        0xA,
        (
            "你们也许不清楚，\x01",
            "其实我们是很少单独行动的。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xA,
        (
            "但亚泽尔已经很久没回家了，\x01",
            "那天正好回家……\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xA,
        (
            "……等到我们赶到的时候，\x01",
            "亚泽尔已经倒在地上了，\x01",
            "伤口是被钝器击打造成的，同时还有轻微的撕裂。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xA,
        (
            "显然是被那群无脑混蛋们\x01",
            "用钉棍打的，不会有错！\x01",
            "……可恶……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D27")

    #C0296
    ChrTalk(
        0x101,
        (
            "#0003F是吗……\x01",
            "多谢你告诉我们这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xA,
        (
            "哼、哼……因为有瓦吉的许可，\x01",
            "我才会和你们说这些的。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xA,
        (
            "无能的警察，可不要太\x01",
            "得意忘形啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 2)

    label("loc_6D27")

    SetScenarioFlags(0x0, 2)

    label("loc_6D2A")

    TalkEnd(0xFE)
    Return()

    # Function_20_5CF0 end

    def Function_21_6D2E(): pass

    label("Function_21_6D2E")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0299
    ChrTalk(
        0xB,
        "我、我很不擅、擅长接待客人的。\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        "这里就交给琴兹吧。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xA,
        (
            "其、其实我也\x01",
            "不是很擅长啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xA,
        "不过，明白了，这里就交给我吧。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_21_6D2E end

    def Function_22_6DCA(): pass

    label("Function_22_6DCA")


    #C0303
    ChrTalk(
        0xA,
        (
            "其实我正在进行秘密特训呢，\x01",
            "今天的实战确实很有参考价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xA,
        (
            "……虽然并不想向你们道谢，\x01",
            "但确实是对我有所帮助呢。\x01",
            "那、那个，谢啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 2)
    Return()

    # Function_22_6DCA end

    def Function_23_6E55(): pass

    label("Function_23_6E55")


    #C0305
    ChrTalk(
        0xA,
        (
            "真没想到，竟然连剑蛇帮的家伙\x01",
            "也开始巡逻了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        (
            "哼，难怪最近这段时间\x01",
            "经常看到他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xA,
        (
            "瓦吉好像并不打算\x01",
            "要立刻开战呢。\x01",
            "但关键还是要看对方的态度如何。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_23_6E55 end

    def Function_24_6EF8(): pass

    label("Function_24_6EF8")


    #C0308
    ChrTalk(
        0xA,
        (
            "……早知会有这种事情发生的话……\x01",
            "我以前是不是也应该\x01",
            "多看看老爸的医书呢……\x02",
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
        "#0205F……医书吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xA, 0x0, 500)

    #C0310
    ChrTalk(
        0xA,
        "什、什么啊，又是你们吗？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xA,
        (
            "哼……有意见吗？\x01",
            "每个人都有自己的隐情。\x02",
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
            "遭到暗算的亚泽尔被抬到了这里，\x01",
            "并接受了简单的护理，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xA,
        (
            "他一直都没有恢复意识，\x01",
            "最后还是等到了天亮，\x01",
            "然后叫来了急救车。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xA,
        (
            "……我虽然很讨厌老爸，\x01",
            "但以前真应该多向他学习一些\x01",
            "基本的急救知识啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#0003F是吗……\x01",
            "确实是很让人担心呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xA,
        (
            "嗯，可是，不知为何，\x01",
            "亚泽尔乘坐的那辆\x01",
            "急救车没有立刻发车……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 5)), scpexpr(EXPR_END)), "loc_72B4")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0317
    ChrTalk(
        0x101,
        (
            "#0005F啊，是吗。\x01",
            "因为那辆急救车也要等\x01",
            "剑蛇帮的那个受害者吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#0203F这样也挺好的。\x01",
            "至少不用耽误时间，\x01",
            "让急救车跑两趟……\x02",
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
            "#4S好、好什么好啊！？\x01",
            "我们可是跟剑蛇帮的家伙上了一辆车哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7491")

    label("loc_72B4")

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
        "#0105F那是……怎么回事呢？\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xA,
        (
            "从旧城区那边又送来了\x01",
            "另一个受伤者。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xA,
        (
            "哼，就是剑蛇帮的那个家伙。\x01",
            "他的同伴说他受了重伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xA,
        (
            "最后把两个伤员用同一辆\x01",
            "急救车送走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#0003F是吗，\x01",
            "两方人员都在同一个夜晚遭到袭击……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x104,
        (
            "#0301F该怎么说呢，\x01",
            "这时机未免也太巧了吧。\x02",
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
            "#4S应该说时机实在是\x01",
            "太糟了才对吧！\x01",
            "我们可是跟剑蛇帮的家伙上了一辆车哦！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4D, 5)

    label("loc_7491")


    #C0327
    ChrTalk(
        0xA,
        "#2S……咳、咳咳，哎呀呀……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xA,
        (
            "真担心正在住院的亚泽尔啊。\x01",
            "反正我老爸也在医院工作，\x01",
            "不然明天直接去看看他好了……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x4E, 3)
    Return()

    # Function_24_6EF8 end

    def Function_25_7511(): pass

    label("Function_25_7511")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_760A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7589")

    #C0329
    ChrTalk(
        0xB,
        (
            "向剑蛇帮发动奇袭作战的提议\x01",
            "被瓦吉否决了\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xB,
        (
            "可恶的红衣爬虫们……\x01",
            "算、算你们捡了条命啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7605")

    label("loc_7589")


    #C0331
    ChrTalk(
        0xB,
        (
            "虽、虽然我很憎恨\x01",
            "剑蛇帮的那群家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        "但、但既然瓦吉都那么说了，也就没办法了。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        "这次就先饶、饶他们一命吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_7605")

    Jump("loc_8549")

    label("loc_760A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7652")

    #C0334
    ChrTalk(
        0xB,
        "瓦吉最近经、经常外出。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xB,
        "好、好像是在调查些什么。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8549")

    label("loc_7652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_7762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_76BD")

    #C0336
    ChrTalk(
        0xB,
        (
            "剑、剑蛇帮好像出现了\x01",
            "很严重的内斗呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xB,
        (
            "哼……我才没有担心那些\x01",
            "红衣爬虫呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_775D")

    label("loc_76BD")


    #C0338
    ChrTalk(
        0xB,
        (
            "我刚、刚才过去看了一下，\x01",
            "好像是真的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xB,
        (
            "剑蛇帮的干部被打伤了，\x01",
            "好像已经送去医院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xB,
        (
            "这、这事发生得还真够没头没脑，\x01",
            "真有白痴蛇帮成员的风格呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_775D")

    Jump("loc_8549")

    label("loc_7762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_77BC")

    #C0341
    ChrTalk(
        0xB,
        (
            "那、那些混蛋黑手党们……\x01",
            "再敢来旧城区的话，我绝对饶不了他们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_784D")

    label("loc_77BC")


    #C0342
    ChrTalk(
        0xB,
        (
            "那、那些混蛋黑手党们……\x01",
            "又开始做什么鬼祟勾当了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xB,
        (
            "之前可真是承蒙他们的『关照』啊。\x01",
            "要、要是让我看见他们的话，一、一定把他们捉到。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_784D")

    Jump("loc_8549")

    label("loc_7852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_794B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_78D7")

    #C0344
    ChrTalk(
        0xB,
        (
            "那、那个蓝头发的红衣爬虫……\x01",
            "最近经常来闹事。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xB,
        (
            "而且他、他的样子也变了，\x01",
            "以前明明是个胆小懦弱的家伙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7946")

    label("loc_78D7")


    #C0346
    ChrTalk(
        0xB,
        (
            "我、我能感觉得到，\x01",
            "那个蓝头发的红衣爬虫似乎不太寻常。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xB,
        (
            "那、那个家伙原本只是\x01",
            "负责看门的最底层成员。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_7946")

    Jump("loc_8549")

    label("loc_794B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_79D1")

    #C0348
    ChrTalk(
        0xB,
        (
            "琴兹那家伙，\x01",
            "去、去找他的父亲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xB,
        (
            "那、那家伙的父亲\x01",
            "是乌尔斯拉医院的医生。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xB,
        "他、他和他父亲好像很合不来呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8549")

    label("loc_79D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7AF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7A42")

    #C0351
    ChrTalk(
        0xB,
        (
            "多亏了良，\x01",
            "店铺可以维持营业了。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xB,
        (
            "奇、奇怪的客人凑到了瓦吉身边，\x01",
            "真是让人在意啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AF1")

    label("loc_7A42")


    #C0353
    ChrTalk(
        0xB,
        (
            "良竟然还有调制鸡尾酒的才能，\x01",
            "我以前都不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xB,
        (
            "阿、阿巴斯调制的鸡尾酒很好喝，\x01",
            "不过良也很厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        (
            "说起来，\x01",
            "阿良那家伙虽然平时不起眼，\x01",
            "但双手真的非常灵巧呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_7AF1")

    Jump("loc_8549")

    label("loc_7AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7B60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7B58")
    OP_4B(0x12, 0xFF)

    #C0356
    ChrTalk(
        0xB,
        (
            "要是想打台球的话，\x01",
            "就、就来和我说。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xB,
        "我可以把规则教给你。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_7B5B")

    label("loc_7B58")

    Call(0, 21)

    label("loc_7B5B")

    Jump("loc_8549")

    label("loc_7B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7BB7")

    #C0358
    ChrTalk(
        0xB,
        "大、大家今、今天要一起出门。\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xB,
        (
            "瓦吉很忙的，\x01",
            "昨天都没能挤出时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8549")

    label("loc_7BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_7BED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7BE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 4)), scpexpr(EXPR_END)), "loc_7BDD")
    Call(0, 27)
    Jump("loc_7BE0")

    label("loc_7BDD")

    Call(0, 26)

    label("loc_7BE0")

    Jump("loc_7BE8")

    label("loc_7BE5")

    Call(0, 27)

    label("loc_7BE8")

    Jump("loc_8549")

    label("loc_7BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7D0E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7CAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 4)), scpexpr(EXPR_END)), "loc_7CA6")

    #C0360
    ChrTalk(
        0xB,
        (
            "要、要是能学好防身术，\x01",
            "就不用再怕那些黑手党了。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xB,
        (
            "发现他们之后，就把他们\x01",
            "赶、赶出这旧城区。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C9E")

    #C0362
    ChrTalk(
        0x101,
        (
            "#0006F不过还是不要\x01",
            "太乱来哦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C9E")

    SetScenarioFlags(0x0, 3)
    Jump("loc_7CA9")

    label("loc_7CA6")

    Call(0, 26)

    label("loc_7CA9")

    Jump("loc_7D09")

    label("loc_7CAE")


    #C0363
    ChrTalk(
        0xB,
        (
            "那、那位客人每个星期\x01",
            "必来一次。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xB,
        "好像和瓦吉有话说呢。\x02",
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xB,
        "瓦、瓦吉果然很成熟啊。\x02",
    )

    CloseMessageWindow()

    label("loc_7D09")

    Jump("loc_8549")

    label("loc_7D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 3)), scpexpr(EXPR_END)), "loc_7D9A")

    #C0366
    ChrTalk(
        0xB,
        (
            "旧城区这一带有很多的\x01",
            "仓、仓库和废墟。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0xB,
        (
            "据、据说那些黑手党\x01",
            "就是在这\x01",
            "附近开战的。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xB,
        "真、真会给人添麻烦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F57")

    label("loc_7D9A")


    #C0369
    ChrTalk(
        0xB,
        (
            "旧城区这一带有很多的\x01",
            "仓、仓库和废墟。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xB,
        (
            "据、据说那些黑手党\x01",
            "就是在这\x01",
            "附近开战的。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xB,
        "真、真会给人添麻烦啊。\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#0003F原来如此啊……\x02\x03",

            "#0001F鲁巴彻和黑月的斗争，\x01",
            "也影响到这里的了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x104,
        (
            "#0306F呼～其实你们之间的\x01",
            "斗争也挺让人头疼的……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xB,
        (
            "我们之间的斗争\x01",
            "和、和那些家伙可不一样。\x01",
            "全都是必要的行动啊。\x02",
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
        "#0106F我想不能这么说吧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 3)

    label("loc_7F57")

    Jump("loc_8549")

    label("loc_7F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_80CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7FC9")

    #C0376
    ChrTalk(
        0xB,
        (
            "来、来旧城区的那些官员\x01",
            "全都是一群伪善者。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xB,
        (
            "那种家伙实在是\x01",
            "无、无法让人信任。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80C9")

    label("loc_7FC9")


    #C0378
    ChrTalk(
        0xB,
        (
            "每年只要一到了临近纪念庆典的时候，\x01",
            "就、就会有很多官员过来找麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xB,
        (
            "不是检查营业许可证，\x01",
            "就是提醒游客小心注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0xB,
        (
            "但那些官员总、总是敷衍了事，\x01",
            "实际上根本就没有检查过，\x01",
            "最后却说已经确认好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xB,
        (
            "哼、哼……一群伪善者。\x01",
            "那种家伙实在令人讨厌。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_80C9")

    Jump("loc_8549")

    label("loc_80CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_815F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_8103")

    #C0382
    ChrTalk(
        0xB,
        "亚泽尔到底会怎么决定呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_815A")

    label("loc_8103")


    #C0383
    ChrTalk(
        0xB,
        (
            "竟、竟然会被\x01",
            "找到这种地方来……\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0xB,
        (
            "真、真是吃惊。\x01",
            "亚泽尔的姐姐可真是大胆啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_815A")

    Jump("loc_8549")

    label("loc_815F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_82A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_821D")

    #C0385
    ChrTalk(
        0xFE,
        (
            "刚才我走在东街上，\x01",
            "就、就被一个女人给叫住了。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "好像是亚泽尔的姐姐，\x01",
            "问了我很多关于亚泽尔的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "大概是因为亚泽尔住院了吧……\x01",
            "她、她好像非常担心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_829C")

    label("loc_821D")


    #C0388
    ChrTalk(
        0xFE,
        (
            "我在东街被亚泽尔的姐姐\x01",
            "问了话。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "说、说起来，在我离开的时候，\x01",
            "她好像在用很锐利的目光瞪着我呢……\x01",
            "……是、是错觉吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_829C")

    Jump("loc_8549")

    label("loc_82A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_83EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_831C")

    #C0390
    ChrTalk(
        0xB,
        (
            "警、警察局的走狗，\x01",
            "我仍然无法信任。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xB,
        (
            "虽然来这里倒是可以，\x01",
            "但、但不许干出一些太过分的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E9")

    label("loc_831C")


    #C0392
    ChrTalk(
        0xB,
        (
            "警、警察局的走狗……\x01",
            "你们又、又来、来了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0xB,
        (
            "虽、虽然之前确实是\x01",
            "得到了你们的帮助。\x01",
            "但这间酒吧——崔尼蒂可是瓦吉的圣域哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xB,
        (
            "这里的规矩就是，一切都要遵从瓦吉的指示。\x01",
            "听、听明白了没有啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_83E9")

    Jump("loc_8549")

    label("loc_83EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8487")

    #C0395
    ChrTalk(
        0xB,
        (
            "剑、剑蛇帮的家伙……\x01",
            "他们在上次的争斗中落了下风，\x01",
            "所以就一直怀恨在心。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xB,
        (
            "这、这群卑鄙无耻的家伙。\x01",
            "犯人除了他们之外，不做其它考虑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8549")

    label("loc_8487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_84DE")

    #C0397
    ChrTalk(
        0xB,
        (
            "我、我丝毫不打算\x01",
            "为警、警察提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xB,
        "赶、赶快从我眼前消失吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8549")

    label("loc_84DE")


    #C0399
    ChrTalk(
        0xB,
        (
            "听、听好啊，\x01",
            "这间酒吧——崔尼蒂可是瓦吉的圣域。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xB,
        (
            "如果敢在这里乱来，\x01",
            "可、可是不会被轻易放过的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_8549")

    TalkEnd(0xFE)
    Return()

    # Function_25_7511 end

    def Function_26_854D(): pass

    label("Function_26_854D")


    #C0401
    ChrTalk(
        0xB,
        (
            "今天的训练是在\x01",
            "事、事前就决定好的。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xB,
        (
            "但、但在正式进行之前，\x01",
            "完全都没有透露出丝毫口风。\x01",
            "呵呵，是、是不是很吃惊啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x103,
        "#0200F嗯，算是吧……\x02",
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x104,
        "#0306F真是的，吃惊又如何啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 4)
    Return()

    # Function_26_854D end

    def Function_27_8608(): pass

    label("Function_27_8608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_86A2")

    #C0405
    ChrTalk(
        0xB,
        (
            "虽然很讨厌那些黑手党，\x01",
            "但剑、剑蛇帮的那些家伙也很碍眼。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xB,
        (
            "我们最、最近宽宏大量，不和他们计较，\x01",
            "结果他们反倒得意忘形，嚣张起来了！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_874A")

    label("loc_86A2")


    #C0407
    ChrTalk(
        0xB,
        (
            "最、最近这段时间，红衣爬虫们\x01",
            "好像也开始在旧城区巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xB,
        (
            "真、真是群碍眼的家伙。\x01",
            "光、光是昨、昨天巡逻一天，\x01",
            "就见到了他们三次。\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xB,
        "……实、实在是太碍眼了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_874A")

    Return()

    # Function_27_8608 end

    def Function_28_874B(): pass

    label("Function_28_874B")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_87CB")

    #C0410
    ChrTalk(
        0xC,
        "不打架虽然挺好。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xC,
        (
            "不过，只要是为了同伴，\x01",
            "不管是什么事情我都愿意做……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xC,
        "我们都是志趣相投的好兄弟。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_87CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_882A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8822")
    OP_4B(0xC, 0xFF)

    #C0413
    ChrTalk(
        0xC,
        "只要多练习，亚泽尔也能越来越厉害。\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0xC,
        "……加油。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_8825")

    label("loc_8822")

    Call(0, 30)

    label("loc_8825")

    Jump("loc_9487")

    label("loc_882A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_8902")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_887C")

    #C0415
    ChrTalk(
        0xC,
        (
            "虽然很讨厌剑蛇帮……\x01",
            "但还是不希望听到那种不好的传闻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88FD")

    label("loc_887C")


    #C0416
    ChrTalk(
        0xC,
        (
            "我刚才听到了传闻……\x01",
            "剑蛇帮好像发生了同伴之间的内斗。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xC,
        (
            "虽然我很讨厌剑蛇帮的那些家伙，\x01",
            "但不知为何，还是有点担心呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_88FD")

    Jump("loc_9487")

    label("loc_8902")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_89CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8969")

    #C0418
    ChrTalk(
        0xC,
        (
            "亚泽尔很担心他的家人，\x01",
            "所以就回家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xC,
        (
            "……亚泽尔还真是\x01",
            "彻底学乖了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C9")

    label("loc_8969")


    #C0420
    ChrTalk(
        0xC,
        (
            "港湾公园好像发生了事件呢，\x01",
            "亚泽尔回去和家人团聚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xC,
        "……因为他家就在港湾区附近啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_89C9")

    Jump("loc_9487")

    label("loc_89CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8AAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8A27")

    #C0422
    ChrTalk(
        0xC,
        "旧城区还是一点都没变啊。\x02",
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xC,
        "……但正因如此，我才喜欢这里。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8AA9")

    label("loc_8A27")


    #C0424
    ChrTalk(
        0xC,
        (
            "最近这段时间，市里\x01",
            "的经济好像很景气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xC,
        (
            "总能听到一些有公司\x01",
            "入驻之类的传闻。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xC,
        (
            "不过，旧城区的贫困\x01",
            "还是一如既往呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8AA9")

    Jump("loc_9487")

    label("loc_8AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8B08")

    #C0427
    ChrTalk(
        0xC,
        (
            "今天街上也很\x01",
            "宁静悠闲啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xC,
        (
            "在这种日子散散步，\x01",
            "似乎也是不错的选择。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_8B08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8B64")

    #C0429
    ChrTalk(
        0xC,
        "今天也要在店里帮忙。\x02",
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xC,
        (
            "欢迎光临，\x01",
            "想点餐的话就和阿巴斯说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BBF")

    label("loc_8B64")


    #C0431
    ChrTalk(
        0xC,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xC,
        (
            "……大家今天也都\x01",
            "出门了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xC,
        (
            "没办法了，\x01",
            "只有由我来接待客人了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8BBF")

    Jump("loc_9487")

    label("loc_8BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8C36")

    #C0434
    ChrTalk(
        0xC,
        "其实瓦吉生气时很恐怖呢。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xC,
        (
            "……但一般来说，他也只对缠着自己不放\x01",
            "的女人才会发脾气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C80")

    label("loc_8C36")


    #C0436
    ChrTalk(
        0xC,
        "那两个人都很可怜呢……\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xC,
        (
            "肯定过不了多久，\x01",
            "就会被无情地抛弃呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8C80")

    Jump("loc_9487")

    label("loc_8C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8CCC")

    #C0438
    ChrTalk(
        0xC,
        "阿巴斯出门了，\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xC,
        "想点餐的话就和我说吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D12")

    label("loc_8CCC")


    #C0440
    ChrTalk(
        0xC,
        "想点些什么呢？\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xC,
        (
            "阿巴斯现在不在，\x01",
            "今天要点单的话就来找我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8D12")

    Jump("loc_9487")

    label("loc_8D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8D8F")

    #C0442
    ChrTalk(
        0xC,
        (
            "比起回家待着，\x01",
            "还是跟同伴们在一起更加开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xC,
        (
            "……像我这么想的人，\x01",
            "在世上应该\x01",
            "有不少呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E13")

    label("loc_8D8F")


    #C0444
    ChrTalk(
        0xC,
        (
            "在纪念庆典时，全家一起\x01",
            "出游的人好像很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xC,
        "可是我没有父母。\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xC,
        (
            "家里面只有对我很凶的\x01",
            "叔叔和婶婶……\x01",
            "再也不想回去了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_8E13")

    Jump("loc_9487")

    label("loc_8E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8E6E")

    #C0447
    ChrTalk(
        0xC,
        "啊……是警察。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0xC,
        (
            "工作辛苦了。\x01",
            "现在人很多，请小心点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E71")

    label("loc_8E6E")

    Call(0, 31)

    label("loc_8E71")

    Jump("loc_9487")

    label("loc_8E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8EAC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8EA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 5)), scpexpr(EXPR_END)), "loc_8E9C")
    Call(0, 33)
    Jump("loc_8E9F")

    label("loc_8E9C")

    Call(0, 32)

    label("loc_8E9F")

    Jump("loc_8EA7")

    label("loc_8EA4")

    Call(0, 33)

    label("loc_8EA7")

    Jump("loc_9487")

    label("loc_8EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8F45")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8F14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 5)), scpexpr(EXPR_END)), "loc_8F0C")

    #C0449
    ChrTalk(
        0xC,
        (
            "亚泽尔去柜台接待客人后，\x01",
            "都没人和我打台球了，真寂寞……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F0F")

    label("loc_8F0C")

    Call(0, 32)

    label("loc_8F0F")

    Jump("loc_8F40")

    label("loc_8F14")


    #C0450
    ChrTalk(
        0xC,
        "你们今天有空吗？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xC,
        "……不，没什么。\x02",
    )

    CloseMessageWindow()

    label("loc_8F40")

    Jump("loc_9487")

    label("loc_8F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_8FB0")

    #C0452
    ChrTalk(
        0xC,
        (
            "我们也准备开始\x01",
            "在旧城区巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0xC,
        (
            "……放心吧，\x01",
            "绝对不会再让那种事情发生了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9021")

    label("loc_8FB0")


    #C0454
    ChrTalk(
        0xC,
        (
            "我最近也在偏僻的小巷中\x01",
            "见到过黑手党的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0xC,
        (
            "……就是之前暗算亚泽尔的家伙，\x01",
            "见到他们，我当然非常火大。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9021")

    Jump("loc_9487")

    label("loc_9026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_90C9")

    #C0456
    ChrTalk(
        0xFE,
        (
            "亚泽尔可以重新活动，\x01",
            "差不多已经有一个星期了……\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0xFE,
        (
            "我想多帮帮他，\x01",
            "但他却不希望让我帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xFE,
        (
            "……不知为何，总觉得\x01",
            "亚泽尔稍微变得成熟些了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_90C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_9139")

    #C0459
    ChrTalk(
        0xC,
        (
            "亚泽尔其实很喜欢\x01",
            "他的姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0xC,
        (
            "不过……他总是给姐姐惹麻烦，\x01",
            "所以心里肯定会有些不自在吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_9139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_91FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_919A")

    #C0461
    ChrTalk(
        0xC,
        (
            "在遇到困难的时候，\x01",
            "我们都会互相帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xC,
        (
            "……这正是圣书会\x01",
            "的优点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91F5")

    label("loc_919A")


    #C0463
    ChrTalk(
        0xC,
        (
            "亚泽尔还要再去医院\x01",
            "复查几次。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0xC,
        (
            "……不用担心钱的问题，\x01",
            "医疗费已经由大家分摊了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_91F5")

    Jump("loc_9487")

    label("loc_91FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_9361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9285")

    #C0465
    ChrTalk(
        0xC,
        (
            "如果亚泽尔当时被打中要害的话，\x01",
            "说不定就会死掉了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xC,
        (
            "绝对不能原谅那些黑手党，\x01",
            "我们今后也要多加留意才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_935C")

    label("loc_9285")


    #C0467
    ChrTalk(
        0xC,
        "亚泽尔平安无事地出院了。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0xC,
        (
            "那个……虽然这句话说得有些晚，\x01",
            "不过，真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0xC,
        (
            "如果亚泽尔当时被打中要害，\x01",
            "现在说不定就已经死掉了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0xC,
        (
            "……这么一想的话，\x01",
            "实在是不能不感谢\x01",
            "为我们报仇的各位啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_935C")

    Jump("loc_9487")

    label("loc_9361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_93C0")

    #C0471
    ChrTalk(
        0xC,
        "亚泽尔……现在怎么样了呢？\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0xC,
        (
            "意识差不多也该恢复了吧，\x01",
            "希望他平安无事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_93C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9406")

    #C0473
    ChrTalk(
        0xC,
        "同伴的仇，就由我们亲手来报。\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xC,
        "你们不要多事哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9487")

    label("loc_9406")


    #C0475
    ChrTalk(
        0xC,
        (
            "遭到袭击的人是一个\x01",
            "名叫亚泽尔的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xC,
        "……我们本想亲手为同伴报仇。\x02",
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0xC,
        (
            "但瓦吉却阻止我们出手，\x01",
            "让我们不要擅自行动。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9487")

    TalkEnd(0xC)
    Return()

    # Function_28_874B end

    def Function_29_948B(): pass

    label("Function_29_948B")

    Call(0, 28)
    Return()

    # Function_29_948B end

    def Function_30_948F(): pass

    label("Function_30_948F")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0478
    ChrTalk(
        0xD,
        (
            "……良，你这家伙还真是\x01",
            "很擅长调制鸡尾酒啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xD,
        (
            "说起来，你的手一直都很巧，\x01",
            "打台球的技术也是我们这里最厉害的。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0xC,
        "只要多练习，亚泽尔也能越来越厉害的。\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xC,
        "……加油吧。\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xD,
        "嗯、嗯。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_30_948F end

    def Function_31_9568(): pass

    label("Function_31_9568")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0483
    ChrTalk(
        0xC,
        "亚泽尔，你的家人如何了？\x02",
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xC,
        "有需要就回去，用不着在意我们哦。\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0xD,
        (
            "嗯，纪念庆典的后半段时间，\x01",
            "准备和姐姐一起过。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xD,
        "今天就和大家一起开心一下吧。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 4)
    Return()

    # Function_31_9568 end

    def Function_32_961F(): pass

    label("Function_32_961F")


    #C0487
    ChrTalk(
        0xC,
        (
            "刚才真是多谢了。\x01",
            "你们的战斗方式很值得参考。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0xC,
        (
            "以后和剑蛇帮的人打架时，\x01",
            "应该也能派上用场……\x02",
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
        "#0006F拜托你，不要在那种场合派上用场啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 5)
    Return()

    # Function_32_961F end

    def Function_33_9718(): pass

    label("Function_33_9718")


    #C0490
    ChrTalk(
        0xC,
        (
            "剑蛇帮的瓦鲁多一直在旧城区\x01",
            "占山为王，以老大自居。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0xC,
        (
            "但在两年前的时候，瓦吉出现了，\x01",
            "前来滋事找碴的瓦鲁多，\x01",
            "在一瞬间便被他打倒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        (
            "自那之后，不服从瓦鲁多\x01",
            "的组织『圣书会』就建立起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0xC,
        "……瓦吉可是非常强的。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_33_9718 end

    def Function_34_97F9(): pass

    label("Function_34_97F9")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_98E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9889")

    #C0494
    ChrTalk(
        0xD,
        (
            "我已经习惯了如今的工作，\x01",
            "对打架越来越没有兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0xD,
        (
            "……听到瓦吉让我们停止争斗时，\x01",
            "老实说，还真是松了口气呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98DF")

    label("loc_9889")


    #C0496
    ChrTalk(
        0xD,
        (
            "听说剑蛇帮的瓦鲁多\x01",
            "现在非常消沉沮丧，是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0xD,
        "实、实在是难以想象啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_98DF")

    Jump("loc_A2A6")

    label("loc_98E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_994E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9946")

    #C0498
    ChrTalk(
        0xD,
        (
            "良很有天赋，\x01",
            "不管学什么都能很快掌握。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xD,
        "有这样的好朋友真是很不错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9949")

    label("loc_9946")

    Call(0, 30)

    label("loc_9949")

    Jump("loc_A2A6")

    label("loc_994E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_9A12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_99B0")

    #C0500
    ChrTalk(
        0xD,
        (
            "瓦吉在夜间工作中\x01",
            "赚到了很多钱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0xD,
        "该怎么说呢，真不愧是瓦吉啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9A0D")

    label("loc_99B0")


    #C0502
    ChrTalk(
        0xD,
        (
            "瓦吉每周都有两三天左右\x01",
            "的时间要去做夜间工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xD,
        (
            "……看样子，他好像\x01",
            "赚了不少钱呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_9A0D")

    Jump("loc_A2A6")

    label("loc_9A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_9A80")

    #C0504
    ChrTalk(
        0xD,
        "我已经很习惯店里的工作了。\x02",
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xD,
        (
            "……凭劳动赚钱的感觉\x01",
            "果然很不错呢，\x01",
            "必须要感谢大家才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2A6")

    label("loc_9A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9AE2")

    #C0506
    ChrTalk(
        0xD,
        (
            "这肯定是以瓦吉\x01",
            "为目标而光顾的客人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xD,
        "因为瓦吉他实在是太惹眼了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B3C")

    label("loc_9AE2")


    #C0508
    ChrTalk(
        0xD,
        "客人开始增多了呢……\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0xD,
        "果然是因为昨天那件事吧。\x02",
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xD,
        (
            "游客源源不断地\x01",
            "光顾这里。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_9B3C")

    Jump("loc_A2A6")

    label("loc_9B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_9BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9BC4")

    #C0511
    ChrTalk(
        0xD,
        (
            "在纪念庆典的后半段时间，\x01",
            "我准备和家人一起度过。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xD,
        (
            "圣书会在这方面是很自由的，\x01",
            "姐姐一定也会很高兴吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BC7")

    label("loc_9BC4")

    Call(0, 31)

    label("loc_9BC7")

    Jump("loc_A2A6")

    label("loc_9BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_9C02")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 6)), scpexpr(EXPR_END)), "loc_9BF2")
    Call(0, 37)
    Jump("loc_9BF5")

    label("loc_9BF2")

    Call(0, 36)

    label("loc_9BF5")

    Jump("loc_9BFD")

    label("loc_9BFA")

    Call(0, 37)

    label("loc_9BFD")

    Jump("loc_A2A6")

    label("loc_9C02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_9D3E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_9CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 6)), scpexpr(EXPR_END)), "loc_9CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9C78")

    #C0513
    ChrTalk(
        0xD,
        (
            "（这女人稍微有些\x01",
            "  可怕呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xD,
        (
            "（不过和瓦吉好像\x01",
            "  还挺投缘的。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CDB")

    label("loc_9C78")


    #C0515
    ChrTalk(
        0xD,
        "那个，这是您点的鸡尾酒。\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xF,
        "哦，帮我记在账上吧。\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xD,
        (
            "明、明白了，\x01",
            "先记在账上是吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_9CDB")

    Jump("loc_9CF1")

    label("loc_9CE0")

    TurnDirection(0xD, 0x0, 0)
    Call(0, 36)
    OP_93(0xD, 0xB4, 0x0)

    label("loc_9CF1")

    Jump("loc_9D39")

    label("loc_9CF6")


    #C0518
    ChrTalk(
        0xD,
        (
            "咳，今天稍微有些\x01",
            "重要的工作呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xD,
        "差不多也该开始准备了。\x02",
    )

    CloseMessageWindow()

    label("loc_9D39")

    Jump("loc_A2A6")

    label("loc_9D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_9E8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E28")
    OP_93(0xFE, 0x0, 0x0)

    #C0520
    ChrTalk(
        0xFE,
        (
            "嗯，杯子已经擦过了，\x01",
            "然后是进货单的检查……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0521
    ChrTalk(
        0xFE,
        (
            "……阿巴斯还真是相当严厉呢。\x01",
            "一旦做错什么，就会受到他的严肃警告。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "虽然平时在一起的时候没发现过，\x01",
            "但那副魁梧的身材实在是威严感十足呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9E8A")

    label("loc_9E28")


    #C0523
    ChrTalk(
        0xFE,
        (
            "如果工作中犯了错误，\x01",
            "就会被阿巴斯警告呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xFE,
        (
            "……呜呜，看来打工也不是\x01",
            "一件很轻松的事啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E8A")

    Jump("loc_A2A6")

    label("loc_9E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F77")

    #C0525
    ChrTalk(
        0xFE,
        "我开始在这家酒吧里打工了。\x02",
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xFE,
        (
            "……我想通过自己的劳动赚钱，\x01",
            "把治疗费还给姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0xFE,
        (
            "我总是让姐姐为我担心，\x01",
            "是不是应该退出圣书会，\x01",
            "好好工作才对呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        "不过，我暂时还是先试着在这里工作一段时间吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_9FF2")

    label("loc_9F77")


    #C0529
    ChrTalk(
        0xFE,
        (
            "虽然我也想过很多，\x01",
            "但果然还是不愿意\x01",
            "退出圣书会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        (
            "我通过劳动赚钱，把治疗费还给姐姐的举动，\x01",
            "得到了姐姐的认可呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF2")

    Jump("loc_A2A6")

    label("loc_9FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A03F")

    #C0531
    ChrTalk(
        0xD,
        "姐姐跑到这里来找我了！\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0xD,
        "这、这、这该怎么办啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2A6")

    label("loc_A03F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_A151")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A0B2")

    #C0533
    ChrTalk(
        0xD,
        (
            "如果向姐姐道歉的话，\x01",
            "她肯定会要求我\x01",
            "退出圣书会的……\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0xD,
        "唉，找不到合适的时机道歉啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A14C")

    label("loc_A0B2")


    #C0535
    ChrTalk(
        0xD,
        (
            "我找不到合适的时机\x01",
            "向姐姐道歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0xD,
        (
            "我总是让她担心，\x01",
            "所以至少也要道个歉……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xD,
        (
            "嗯～检查期已经结束了，\x01",
            "彻底痊愈之后，是不是该向姐姐道个歉呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_A14C")

    Jump("loc_A2A6")

    label("loc_A151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A1BA")

    #C0538
    ChrTalk(
        0xD,
        "确实是让姐姐担心了呢。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        (
            "我也觉得很对不起她……\x01",
            "唉，但见面的话，实在是很别扭呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A2A6")

    label("loc_A1BA")


    #C0540
    ChrTalk(
        0xD,
        (
            "我的伤势已经基本痊愈了，\x01",
            "总算是出院了……\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0xD,
        (
            "但姐姐这段时间\x01",
            "好像相当为我担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xD,
        (
            "在姐姐的心里，圣书会\x01",
            "实在不是一个好地方……\x01",
            "因为加入这里，我才彻夜不回，最后受伤住院……\x02",
        )
    )

    CloseMessageWindow()

    #C0543
    ChrTalk(
        0xD,
        (
            "……唉，事到如今，\x01",
            "实在是没脸再面对她了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_A2A6")

    TalkEnd(0xD)
    Return()

    # Function_34_97F9 end

    def Function_35_A2AA(): pass

    label("Function_35_A2AA")

    Call(0, 34)
    Return()

    # Function_35_A2AA end

    def Function_36_A2AE(): pass

    label("Function_36_A2AE")


    #C0544
    ChrTalk(
        0xD,
        "刚、刚才真是承蒙关照了啊。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0xD,
        (
            "我之前曾被黑手党\x01",
            "的人暗算得手，\x01",
            "从今以后一定要好好练习防身术。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        "#0100F是吗……那就加油吧。\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0xD,
        "嗯，那当然。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 6)
    Return()

    # Function_36_A2AE end

    def Function_37_A348(): pass

    label("Function_37_A348")


    #C0548
    ChrTalk(
        0xD,
        (
            "姐姐好像要在纪念庆典时\x01",
            "申请休假呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xD,
        (
            "……如果我也能放假，\x01",
            "就去陪陪她好了。\x01",
            "平时总是让她为我担心。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_37_A348 end

    def Function_38_A3B4(): pass

    label("Function_38_A3B4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A448")
    Jump("loc_A492")

    label("loc_A448")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A468")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A492")

    label("loc_A468")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A488")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A492")

    label("loc_A488")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A492")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_A66F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 5)), scpexpr(EXPR_END)), "loc_A5D9")
    SetChrSubChip(0xF, 0x1)

    #C0550
    ChrTalk(
        0xF,
        "呵呵，和解休战还真是个滑稽的谢幕方式啊。\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0xF,
        (
            "本来还希望能让我\x01",
            "玩得再开心一些呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0xE,
        (
            "#0402F啊哈哈，这位姐姐好坏啊。\x01",
            "都已经一周了……\x01",
            "那位先生也算是很能忍了。\x02\x03",

            "#0404F不过，我倒是有些\x01",
            "担心，当忍耐到极限\x01",
            "之后会怎么收场……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x101,
        "#0005F（究竟在说些什么呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_A66A")

    label("loc_A5D9")


    #C0554
    ChrTalk(
        0xF,
        (
            "嗯……？\x01",
            "啊，真是个可爱的孩子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xF,
        (
            "和我家的金格\x01",
            "好像差不多同岁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xF,
        (
            "我的店叫纳因瓦利，\x01",
            "离这里很近的。\x01",
            "哈，见到金格就陪她玩玩吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 5)

    label("loc_A66A")

    Jump("loc_A763")

    label("loc_A66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A6E1")

    #C0557
    ChrTalk(
        0xF,
        "……哎呀，都已经是早上了啊。\x02",
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xF,
        (
            "哎呀呀，又喝了\x01",
            "一个通宵呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0xF,
        (
            "金格应该\x01",
            "按时开店了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A763")

    label("loc_A6E1")


    #C0560
    ChrTalk(
        0xF,
        (
            "呵呵，虽然看店的都是一些讨厌的臭小子，\x01",
            "但这里的鸡尾酒还真是很地道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0xF,
        (
            "怎么样，如果有兴趣的话，\x01",
            "我也可以请你们喝一杯哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A763")

    TalkEnd(0xFE)
    SetChrSubChip(0xF, 0x1)
    Return()

    # Function_38_A3B4 end

    def Function_39_A76B(): pass

    label("Function_39_A76B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7DE")

    #C0562
    ChrTalk(
        0xFE,
        (
            "亚泽尔……\x01",
            "你到底打算干什么啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0xFE,
        (
            "你知道姐姐和\x01",
            "尤格特有多\x01",
            "担心你吗……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_A800")

    label("loc_A7DE")


    #C0564
    ChrTalk(
        0xFE,
        "你在听我说话吗，亚泽尔……！\x02",
    )

    CloseMessageWindow()

    label("loc_A800")

    TalkEnd(0xFE)
    Return()

    # Function_39_A76B end

    def Function_40_A804(): pass

    label("Function_40_A804")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A8D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_A87E")

    #C0565
    ChrTalk(
        0x11,
        (
            "真是有些不好意思，\x01",
            "我之前确实是对他们有些偏见呢。\x02\x03",

            "虽然是不良成员，\x01",
            "但好像并不是什么坏人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D2")

    label("loc_A87E")


    #C0566
    ChrTalk(
        0x11,
        (
            "哎呀，庆典真是开心啊！\x02\x03",

            "虽说是旧城区的不良组织，\x01",
            "但成员却并不是一些坏人呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_A8D2")

    Jump("loc_AA53")

    label("loc_A8D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_A991")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_A932")

    #C0567
    ChrTalk(
        0x11,
        (
            "哈哈哈，其实我也\x01",
            "很擅长打台球的！\x02\x03",

            "嘿嘿，\x01",
            "马上还要再进一球哦！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A98C")

    label("loc_A932")

    TurnDirection(0x11, 0xB, 0)

    #C0568
    ChrTalk(
        0x11,
        (
            "……好，轮到我击球啦。\x02\x03",

            "哈哈，好好看着吧。\x01",
            "台球可是我长项中的长项啊！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)

    label("loc_A98C")

    Jump("loc_AA53")

    label("loc_A991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_A9E2")

    #C0569
    ChrTalk(
        0x11,
        (
            "哎呀，这里还真是间很不错的酒吧呢，\x01",
            "今天应该能好好品尝一番了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA53")

    label("loc_A9E2")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0570
    ChrTalk(
        0x11,
        (
            "啊，那个，一杯威士忌……\x02\x03",

            "要大杯的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xC,
        (
            "一杯大杯的威士忌吗，\x01",
            "马上就给您调制好。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)

    label("loc_AA53")

    TalkEnd(0xFE)
    Return()

    # Function_40_A804 end

    def Function_41_AA57(): pass

    label("Function_41_AA57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_AAA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AAA0")

    #C0572
    ChrTalk(
        0x12,
        (
            "怎、怎么会……\x01",
            "……如果是瓦吉先生，我……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAA3")

    label("loc_AAA0")

    Call(0, 11)

    label("loc_AAA3")

    Jump("loc_AB50")

    label("loc_AAA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AB4D")
    OP_4B(0xA, 0xFF)

    #C0573
    ChrTalk(
        0x12,
        (
            "瓦吉先生今天\x01",
            "不在吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xA,
        "不、不好意思，是的。\x02",
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xA,
        (
            "瓦吉他今天不在。\x01",
            "我说……\x02",
        )
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        (
            "从刚才开始，同样的问题\x01",
            "你已经问过我无数次了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_AB50")

    label("loc_AB4D")

    Call(0, 42)

    label("loc_AB50")

    TalkEnd(0xFE)
    Return()

    # Function_41_AA57 end

    def Function_42_AB54(): pass

    label("Function_42_AB54")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0577
    ChrTalk(
        0x12,
        "喂喂，那不就是那个人吗～？\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x12,
        "昨天那个冷峻的美少年！\x02",
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x13,
        "哎呀，他在喝鸡尾酒～\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x13,
        "好·可·爱·呀～⊥\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_42_AB54 end

    def Function_43_ABD3(): pass

    label("Function_43_ABD3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AC67")
    Jump("loc_ACB1")

    label("loc_AC67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AC87")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACB1")

    label("loc_AC87")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACA7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ACB1")

    label("loc_ACA7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ACB1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 44)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_ABD3 end

    def Function_44_ACE1(): pass

    label("Function_44_ACE1")

    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)

    #C0581
    ChrTalk(
        0x14,
        "瓦吉先生今天也不在啊……\x02",
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x15,
        (
            "唉，那冷峻的眼神……\x01",
            "……清爽飘逸，有着神秘色泽的秀发……\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x15,
        (
            "瓦吉先生到底\x01",
            "去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_44_ACE1 end

    def Function_45_AD68(): pass

    label("Function_45_AD68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_ADBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_ADB5")

    #C0584
    ChrTalk(
        0x13,
        (
            "（梳理头发）……\x01",
            "不、不知为何，心中很苦闷……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ADB8")

    label("loc_ADB5")

    Call(0, 11)

    label("loc_ADB8")

    Jump("loc_AE15")

    label("loc_ADBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AE12")

    #C0585
    ChrTalk(
        0x13,
        "今天也到这里来了……\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x13,
        (
            "瓦吉先生，为什么今天\x01",
            "不让我见到你呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE15")

    label("loc_AE12")

    Call(0, 42)

    label("loc_AE15")

    TalkEnd(0xFE)
    Return()

    # Function_45_AD68 end

    def Function_46_AE19(): pass

    label("Function_46_AE19")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AEAD")
    Jump("loc_AEF7")

    label("loc_AEAD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AECD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AEF7")

    label("loc_AECD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AEF7")

    label("loc_AEED")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AEF7")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Call(0, 44)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_AE19 end

    def Function_47_AF27(): pass

    label("Function_47_AF27")

    TalkBegin(0xFE)
    SetChrSubChip(0x16, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AF8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_AF87")
    SetChrSubChip(0x16, 0x1)

    #C0587
    ChrTalk(
        0x16,
        (
            "啊～是吗～\x01",
            "确实如此呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0x16,
        (
            "旧城区的人\x01",
            "应该都很贫穷呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF8A")

    label("loc_AF87")

    Call(0, 48)

    label("loc_AF8A")

    Jump("loc_AFCE")

    label("loc_AF8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_AFCB")
    SetChrSubChip(0x16, 0x1)

    #C0589
    ChrTalk(
        0x16,
        "不错啊，真刺激。\x02",
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x16,
        "我相当开心呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AFCE")

    label("loc_AFCB")

    Call(0, 49)

    label("loc_AFCE")

    TalkEnd(0xFE)
    Return()

    # Function_47_AF27 end

    def Function_48_AFD2(): pass

    label("Function_48_AFD2")

    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)

    #C0591
    ChrTalk(
        0x16,
        (
            "这里的酒保先生\x01",
            "超级魁梧呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x16,
        (
            "莫非他是个\x01",
            "黑道人士吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x17,
        (
            "笨蛋～只有市区里\x01",
            "才会有什么黑道吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x17,
        "而且黑道成员怎么可能会这么穷呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_48_AFD2 end

    def Function_49_B06B(): pass

    label("Function_49_B06B")

    SetChrSubChip(0x16, 0x1)
    SetChrSubChip(0x17, 0x2)

    #C0595
    ChrTalk(
        0x16,
        "这里还真是个好地方啊，\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x16,
        "果然来对了，是吧？\x02",
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x17,
        (
            "明明是你一直走，\x01",
            "最后走过头了……\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0x17,
        (
            "听说旧城区的不良团伙\x01",
            "都是一群超恐怖的家伙呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_49_B06B end

    def Function_50_B105(): pass

    label("Function_50_B105")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B195")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B18D")
    SetChrSubChip(0x17, 0x2)

    #C0599
    ChrTalk(
        0x17,
        (
            "要说黑道什么的，\x01",
            "应该是像鲁巴彻那样的组织吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x17,
        (
            "他们可是超级有钱的，\x01",
            "旧城区里可不会有那种组织啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B190")

    label("loc_B18D")

    Call(0, 48)

    label("loc_B190")

    Jump("loc_B223")

    label("loc_B195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B220")
    SetChrSubChip(0x17, 0x2)

    #C0601
    ChrTalk(
        0x17,
        (
            "旧城区的不良团伙\x01",
            "之前好像和黑道组织斗争过吧？\x01",
            "那绝对都是一群超级凶残的家伙。\x02",
        )
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x17,
        (
            "……哈，其实我也没有\x01",
            "亲眼看到啦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B223")

    label("loc_B220")

    Call(0, 49)

    label("loc_B223")

    TalkEnd(0xFE)
    Return()

    # Function_50_B105 end

    def Function_51_B227(): pass

    label("Function_51_B227")

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

    def lambda_B423():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B423)

    def lambda_B43D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B43D)
    Sleep(400)

    def lambda_B451():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B451)

    def lambda_B46B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B46B)
    Sleep(400)

    def lambda_B47F():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B47F)

    def lambda_B499():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B499)
    Sleep(400)

    def lambda_B4AD():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B4AD)

    def lambda_B4C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B4C7)
    WaitChrThread(0x101, 1)

    def lambda_B4DC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B4DC)
    WaitChrThread(0x102, 1)

    def lambda_B4ED():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B4ED)
    WaitChrThread(0x103, 1)

    def lambda_B4FE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B4FE)
    WaitChrThread(0x104, 1)

    def lambda_B50F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B50F)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)

    #C0603
    ChrTalk(
        0x102,
        "#0105F#6P台球桌……？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x104,
        (
            "#12P#0300F设有台球桌的酒吧，这就是所谓的撞球吧了。\x01",
            "还真是挺有情趣的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x103,
        (
            "#6P#0200F『崔尼蒂』……\x01",
            "也是一家有经营许可的正规店面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x101,
        (
            "#6P#0001F原来如此，这里就是\x01",
            "『圣书会』的集会所吗……\x02",
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
        "男人的声音",
        "──有什么事？\x02",
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

    def lambda_B72F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B72F)
    Sleep(300)

    def lambda_B73F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B73F)

    def lambda_B74C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B74C)
    Sleep(300)

    def lambda_B75C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B75C)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)

    #N0608
    NpcTalk(
        0xA,
        "蓝衣青年",
        "你们是……！？\x02",
    )

    CloseMessageWindow()

    #N0609
    NpcTalk(
        0xB,
        "蓝衣青年",
        "#5P警、警察局的走狗……？\x02",
    )

    CloseMessageWindow()

    #N0610
    NpcTalk(
        0x9,
        "高大的光头男子",
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        (
            "#12P#0003F之前真是多谢配合了。\x02\x03",

            "#0000F这里好像正在营业吧，\x01",
            "那我们就打扰一下了。\x02",
        )
    )

    CloseMessageWindow()

    #N0612
    NpcTalk(
        0xA,
        "蓝衣青年",
        "真、真够厚颜无耻的……\x02",
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
        "蓝衣青年",
        (
            "#1P……你们来干什么！？\x01",
            "如果没有一个像样的回答，可别想就这么回去了！\x02",
        )
    )

    CloseMessageWindow()

    #N0614
    NpcTalk(
        0xB,
        "蓝衣青年",
        (
            "#5P刚、刚才的账，\x01",
            "就连本带利和你们算清楚……！\x02",
        )
    )

    CloseMessageWindow()

    #N0615
    NpcTalk(
        0x9,
        "高大的光头男子",
        "#5P──慢着。\x02",
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
        "蓝衣青年",
        "#1P阿巴斯……\x02",
    )

    CloseMessageWindow()

    #N0617
    NpcTalk(
        0xB,
        "蓝衣青年",
        "#5P为、为什么阻止我们……？\x02",
    )

    CloseMessageWindow()

    #N0618
    NpcTalk(
        0x9,
        "高大的光头男子",
        (
            "#5P这里是圣域──\x01",
            "不要引发不必要的骚乱。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x190)

    #N0619
    NpcTalk(
        0x9,
        "高大的光头男子",
        "#11P瓦吉，怎么办？\x02",
    )

    CloseMessageWindow()

    #N0620
    NpcTalk(
        0x8,
        "声音",
        "……嗯～这个嘛。\x02",
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
            "#0404F只是进来也无所谓吧？\x01",
            "让他们过来好了。\x02",
        )
    )

    CloseMessageWindow()

    #N0622
    NpcTalk(
        0x9,
        "高大的光头男子",
        "……明白了。\x02",
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

    def lambda_BB04():

        label("loc_BB04")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_BB04")

    QueueWorkItem2(0x101, 2, lambda_BB04)

    def lambda_BB16():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BB16)
    Sleep(50)

    def lambda_BB33():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BB33)
    Sleep(50)

    def lambda_BB50():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BB50)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x101, 0x2)
    TurnDirection(0x9, 0x101, 500)

    #N0623
    NpcTalk(
        0x9,
        "高大的光头男子",
        "#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x101,
        "#12P#0005F多、多谢。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x104,
        "#4P#0305F（怎么回事，这种举动……）\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        "#0106F#6P（看起来简直像是在举行某种仪式呢……）\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_BC2E():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BC2E)
    Sleep(50)

    def lambda_BC4B():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BC4B)
    Sleep(50)

    def lambda_BC68():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BC68)
    Sleep(50)

    def lambda_BC85():
        OP_98(0xFE, 0xFFFFFC18, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BC85)
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

    def lambda_BD5C():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x25E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BD5C)

    def lambda_BD76():
        OP_96(0xFE, 0xFFFFF9C0, 0x0, 0x25E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BD76)
    Sleep(50)

    def lambda_BD93():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BD93)

    def lambda_BDAD():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0x2134, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BDAD)

    def lambda_BDC7():
        OP_96(0xFE, 0x0, 0x0, 0x2C88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BDC7)
    Sleep(50)

    def lambda_BDE4():
        OP_96(0xFE, 0x384, 0x0, 0x29CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BDE4)

    def lambda_BDFE():
        OP_96(0xFE, 0x384, 0x0, 0x251C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BDFE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x9, 1)

    def lambda_BE2C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_BE2C)
    WaitChrThread(0xA, 1)

    def lambda_BE3D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BE3D)
    WaitChrThread(0xB, 1)

    def lambda_BE4E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BE4E)
    SetChrFlags(0x8, 0x20)

    def lambda_BE60():
        OP_96(0xFE, 0xFFFFF63C, 0x32, 0x3070, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BE60)

    def lambda_BE7A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE7A)
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
            "──那么，有何贵干？\x02\x03",

            "我不是已经说过了吗？\x01",
            "和警察局的走狗没什么好说的。\x02",
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
            "#12P#0003F虽然你没什么可说的，\x01",
            "但我却有些事想问。\x02\x03",

            "#0000F希望你们能稍微配合一下，\x01",
            "协助我们的调查工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0x8,
        (
            "#5P#0403F哼～调查啊。\x02\x03",

            "#0402F我先把话说在前面，\x01",
            "我们和剑蛇帮的决战是势在必行的，\x01",
            "不要妄图去阻止。\x02\x03",

            "#0404F也许确实会给附近的居民造成不便，\x01",
            "不过也没办法，只能让他们稍微忍耐一下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x101,
        (
            "#12P#0003F我们并不是来\x01",
            "阻止你们进行争斗的。\x02\x03",

            "#0001F只是想来问一问──\x01",
            "你们决心要彻底击溃对方的理由……\x02\x03",

            "究竟是什么呢？\x02",
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
        "#5P#0400F喔……？\x02",
    )

    CloseMessageWindow()

    #N0632
    NpcTalk(
        0xA,
        "蓝衣青年",
        "#2P那、那是因为……！\x02",
    )

    CloseMessageWindow()

    #N0633
    NpcTalk(
        0x9,
        "高大的光头男子",
        (
            "#5P──不要多嘴，\x01",
            "一切都交给瓦吉吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0634
    NpcTalk(
        0xA,
        "蓝衣青年",
        "#2P啊，好的……\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0x101,
        (
            "#12P#0001F……看他这种反应，\x01",
            "好像确实是有什么内情吧。\x02\x03",

            "可不可以告诉我们呢？\x02",
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

    def lambda_C26F():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x2A94, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C26F)
    WaitChrThread(0x8, 1)

    #C0636
    ChrTalk(
        0x8,
        (
            "#0400F就算知道了，你们又能怎样？\x02\x03",

            "如果是游击士，也倒罢了……\x01",
            "警察又能起到什么作用呢？\x02\x03",

            "难道还会帮助我们这些居住在\x01",
            "旧城区的危险分子？\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        (
            "#12P#0006F……我承认，警察局在这方面\x01",
            "的应对措施确实是不够充分。\x02\x03",

            "而且就算知道了理由，\x01",
            "我们也不一定能帮助你们。\x02\x03",

            "#0000F毕竟我们的工作性质，和以保卫市民\x01",
            "为首要目的的游击士并不相同。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C3D0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C3D0)
    Sleep(50)

    def lambda_C3E0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C3E0)
    WaitChrThread(0x104, 2)

    #C0638
    ChrTalk(
        0x104,
        "#0301F喂、喂……\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x102,
        "#0101F#11P等一下，罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x8,
        (
            "#0404F哎呀呀，和你真是很难沟通。\x02\x03",

            "#0402F连最基本的互利关系都不存在，\x01",
            "就想套出我的情报吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        "#12P#0004F──不，互利关系是存在的。\x02",
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x8,
        "#0405F哎……\x02",
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0x101,
        (
            "#12P#0001F搜查官的工作，就是将\x01",
            "埋藏在黑暗深处的真相查明，\x01",
            "为市民与社会带来光明……\x02\x03",

            "至少，我就是在这样的\x01",
            "教育下成长的。\x02\x03",

            "#0004F哪怕只是一点点也好，\x01",
            "如果你们对此次事件的内幕还抱有疑问……\x02\x03",

            "我们就一定会帮忙将其中的真相彻底查明。\x02\x03",

            "#0000F这就是……\x01",
            "我们可以提供的『利』。\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x102,
        "#0105F#11P……啊…………\x02",
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x104,
        "#0302F还真是会说呢……\x02",
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
        "#0404F…………哼哼……………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    #Sound(1431, 255, 100, 0)    #voice#Lazy

    #C0648
    ChrTalk(
        0x8,
        "#0409F#4S啊哈哈哈哈哈哈哈！！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0649
    ChrTalk(
        0x8,
        (
            "#0402F好！很好很好！\x02\x03",

            "这种一本正经的台词\x01",
            "还真是难得听到一回啊！\x02\x03",

            "#0409F你是叫罗伊德吧！？\x01",
            "哈哈～我很欣赏你！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C714():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C714)

    def lambda_C721():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C721)

    #C0650
    ChrTalk(
        0x101,
        (
            "#12P#0006F……我并不是为了\x01",
            "讨好你才说这些的啊。\x02\x03",

            "#0001F那么，究竟是为什么呢？\x02\x03",

            "『你们非要将对方彻底击溃的理由』……\x01",
            "可以告诉我们了吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C7BA():
        OP_96(0xFE, 0xFFFFF5D8, 0x0, 0x2CEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C7BA)
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
            "#5P#0404F#5P……呵呵，好吧。\x02\x03",

            "你都已经说出那么搞笑的台词了，\x01",
            "我再不表示一下，岂不是显得很小气。\x02",
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
            "#5P#0402F──阿巴斯，\x01",
            "告诉他们吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    #N0653
    NpcTalk(
        0x9,
        "高大的光头男子",
        "#11P……明白了。\x02",
    )

    CloseMessageWindow()
    OP_68(-2140, 1100, 10430, 1000)

    def lambda_C8D4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C8D4)
    Sleep(150)

    def lambda_C8E4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C8E4)
    Sleep(50)

    def lambda_C8F4():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C8F4)
    Sleep(50)

    def lambda_C904():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C904)
    Sleep(50)

    def lambda_C914():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C914)
    WaitChrThread(0x104, 2)
    Sleep(1000)

    #N0654
    NpcTalk(
        0x9,
        "高大的光头男子",
        "#5P我还没有自报家门。\x02",
    )

    CloseMessageWindow()

    #N0655
    NpcTalk(
        0x9,
        "高大的光头男子",
        (
            "#5P我叫阿巴斯。\x01",
            "是圣书会的一员。\x02",
        )
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊……请多指教。\x02\x01",

            "#0001F（好魁梧啊……他到底是做什么的？）\x02",
        )
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x9,
        "#5P事件的开端，是五天前的夜晚。\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x9,
        (
            "#5P我们的一名成员\x01",
            "在附近的偏僻小巷中\x01",
            "被剑蛇帮的人暗算了。\x02",
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
        "#6P#0007F暗算……！？\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x102,
        (
            "#6P#0101F那个……\x01",
            "并不是普通的打架吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0661
    NpcTalk(
        0xA,
        "蓝衣青年",
        "#11P哼，怎么会是普通的打架……！？\x02",
    )

    CloseMessageWindow()

    #N0662
    NpcTalk(
        0xA,
        "蓝衣青年",
        (
            "#11P后脑部位挨了重重的一击，\x01",
            "倒下之后又被围殴了一顿呢！！\x02",
        )
    )

    CloseMessageWindow()

    #N0663
    NpcTalk(
        0xB,
        "蓝衣青年",
        "完、完全是单方面的袭击……\x02",
    )

    CloseMessageWindow()

    #N0664
    NpcTalk(
        0xB,
        "蓝衣青年",
        (
            "被暗算的那个同伴……\x01",
            "已、已经被送到医院了……\x02",
        )
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x104,
        "#12P#0306F下手还真是挺重的啊……\x02",
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x101,
        (
            "#6P#0001F那个……\x01",
            "受害者目前的伤势如何了？\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x9,
        (
            "#5P据医院那边的人说，\x01",
            "现在好像还没有恢复意识。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x9,
        (
            "#5P医疗救治工作虽然已经完成了，\x01",
            "但毕竟是头部受到了重击……\x02",
        )
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x9,
        "#5P目前还在等待联络呢。\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#6P#0003F是吗……\x02",
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x102,
        (
            "#6P#0101F……那个，你们一直都\x01",
            "没有报警吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x9,
        (
            "#5P就算报警，那些家伙也不会\x01",
            "为了我们而出动的。\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x9,
        (
            "#5P而且，犯人是谁，已经一目了然了。\x01",
            "如果通报警察，反而会影响我们的复仇计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x102,
        "#6P#0108F……是吗。\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0675
    ChrTalk(
        0x103,
        (
            "#6P#0205F──请等一下。\x02\x03",

            "#0200F被袭击的人好像\x01",
            "还没有恢复意识吧……\x02\x03",

            "既然如此，各位为什么\x01",
            "就能肯定犯人是\x01",
            "『剑蛇帮』的人呢？\x02",
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
            "#6P#0005F这么一说……\x02\x03",

            "该不会是……\x01",
            "单靠臆测而得出的结论吧？\x02",
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
            "#5P#0404F……哈，再怎么说，\x01",
            "我们也不会武断到那种程度啊。\x02\x03",

            "#0402F再怎么说，我们也和那些家伙不同，\x01",
            "算是知性派的组织呢。\x02\x03",

            "#0409F哈哈，不过，仔细想想的话，\x01",
            "一个不良团伙，说什么知性派也很可笑呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0678
    NpcTalk(
        0xA,
        "蓝色装束的青年",
        "#11P瓦吉……！\x02",
    )

    CloseMessageWindow()

    def lambda_CF75():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CF75)
    Sleep(50)

    def lambda_CF85():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CF85)
    Sleep(50)

    def lambda_CF95():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CF95)
    Sleep(50)

    def lambda_CFA5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_CFA5)

    #C0679
    ChrTalk(
        0x8,
        (
            "#5P#0404F呵呵，我们之所以断定\x01",
            "犯人是他们，理由就是……\x02\x03",

            "#0400F你既然是个搜查官，\x01",
            "想必已经有头绪了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x101,
        "#12P#0003F………这个嘛…………\x02",
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
            "【遭到袭击的场所】\x01",      # 0
            "【受袭成员的伤口】\x01",      # 1
            "【留在现场的脚印】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D0B5"),
        (1, "loc_D25A"),
        (2, "loc_D365"),
        (SWITCH_DEFAULT, "loc_D558"),
    )


    label("loc_D0B5")


    #C0681
    ChrTalk(
        0x101,
        (
            "#12P#0001F那名成员受到袭击的场所……\x01",
            "应该就是决定性的证据吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x8,
        (
            "#5P#0406F嗯～刚才都已经说过了，\x01",
            "他们发动袭击的场所就是附近的偏僻小巷。\x02\x03",

            "#0400F剑蛇帮的人虽然也会从那里经过，\x01",
            "但这显然不能算是什么决定性的证据。\x02",
        )
    )

    CloseMessageWindow()

    #C0683
    ChrTalk(
        0x101,
        "#12P#0005F是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x9,
        (
            "#5P──决定性的证据，\x01",
            "就是受袭成员的伤口。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x9,
        (
            "#5P虽然主要是由钝器击打而造成的，\x01",
            "但同时还有一些很明显的裂口……\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x9,
        (
            "#5P感觉就像是某种坚硬的\x01",
            "尖锐物体造成的撕裂伤口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D558")

    label("loc_D25A")

    OP_2C(0x3E, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0687
    ChrTalk(
        0x101,
        (
            "#12P#0008F……是吗，我明白了。\x02\x03",

            "#0001F决定性的证据应该\x01",
            "就是受袭成员的伤口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0x8,
        "#5P#0409F答对啦，果然有一套嘛。\x02",
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x9,
        (
            "#5P伤口虽然主要是由钝器击打而造成的，\x01",
            "但同时还有一些很明显的裂口……\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x9,
        (
            "#5P感觉就像是某种坚硬的\x01",
            "尖锐物体造成的撕裂伤口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D558")

    label("loc_D365")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0691
    ChrTalk(
        0x101,
        (
            "#12P#0008F你们和他们都穿着\x01",
            "很独特的鞋子……\x02\x03",

            "#0001F决定性的证据，莫非就是\x01",
            "残留在现场的脚印吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x8,
        (
            "#5P#0405F嘿，很有趣的观点啊。\x02\x03",

            "#0406F不过呢，旧城区的路面\x01",
            "都是用陈旧的石板铺设而成的，\x01",
            "基本留不下什么脚印。\x02\x03",

            "#0400F而且他们平时也经常会路过那里，\x01",
            "所以并不能算是什么决定性的证据。\x02",
        )
    )

    CloseMessageWindow()

    #C0693
    ChrTalk(
        0x101,
        "#12P#0005F是吗……\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x9,
        (
            "#5P──决定性的证据，\x01",
            "就是受袭成员的伤口。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x9,
        (
            "#5P虽然主要是由钝器击打而造成的，\x01",
            "但同时还有一些很明显的裂口……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x9,
        (
            "#5P感觉就像是某种坚硬的\x01",
            "尖锐物体造成的撕裂伤口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D558")

    label("loc_D558")


    #C0697
    ChrTalk(
        0x102,
        (
            "#0105F#12P由钝器击打造成的伤口，\x01",
            "还有坚硬的尖锐物体造成的裂伤……\x02\x03",

            "#0101F……啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x104,
        (
            "#0301F#12P……原来如此，\x01",
            "就是那些家伙用的钉棍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x103,
        (
            "#6P#0204F这种明显的特征，也许确实\x01",
            "可以算是决定性的证据呢。\x02",
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
            "#12P#0003F──事情的经过，我已经大致了解了。\x02\x03",

            "#0000F谢谢，这些情报很有参考价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        (
            "#5P#0405F有用就好，不过……\x01",
            "只要这点情报就够了吗？\x02\x03",

            "难道不想说些『请停止报复行为』\x01",
            "之类的劝言吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x101,
        (
            "#12P#0006F以我个人的立场来说，\x01",
            "当然是很想阻止你们……\x02\x03",

            "#0001F但目前掌握到的判断材料实在是太少了。\x02\x03",

            "我们还要去剑蛇帮那边了解一下情况，\x01",
            "如果有什么新发现，会再来和你们联络的。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x8,
        (
            "#5P#0404F呵呵，原来如此。\x01",
            "无论如何也要执着于所谓的『调查』啊。\x02\x03",

            "#0402F既然如此，我就期待着\x01",
            "你们给我带来一些有趣的消息了。\x02\x03",

            "#0409F──呵呵，不过，如果没有什么进展，\x01",
            "旧城区可就要迎来一场腥风血雨了。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x101,
        (
            "#12P#0003F………明白了。\x02\x03",

            "#0000F我们不会辜负你的期待，\x01",
            "一定能带回你所谓的有趣的消息。\x02",
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

    # Function_51_B227 end

    def Function_52_D9FF(): pass

    label("Function_52_D9FF")


    def lambda_DA04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DA04)

    def lambda_DA15():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA15)
    WaitChrThread(0xFE, 1)

    def lambda_DA33():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA33)
    WaitChrThread(0xFE, 1)

    def lambda_DA51():
        OP_95(0xFE, 0, 0, 4800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DA51)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xB4, 0x1F4)
    Return()

    # Function_52_D9FF end

    def Function_53_DA72(): pass

    label("Function_53_DA72")


    def lambda_DA77():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DA77)

    def lambda_DA88():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA88)
    WaitChrThread(0xFE, 1)

    def lambda_DAA6():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DAA6)
    WaitChrThread(0xFE, 1)

    def lambda_DAC4():
        OP_95(0xFE, -600, 0, 6100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_DAC4)
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x1F4)
    Return()

    # Function_53_DA72 end

    def Function_54_DAE5(): pass

    label("Function_54_DAE5")


    def lambda_DAEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DAEA)

    def lambda_DAFB():
        OP_95(0xFE, 7200, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DAFB)
    WaitChrThread(0xFE, 1)

    def lambda_DB19():
        OP_95(0xFE, 2000, 0, 7000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DB19)
    WaitChrThread(0xFE, 1)

    def lambda_DB37():
        OP_95(0xFE, 700, 0, 6700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_DB37)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xB4, 0x1F4)
    Return()

    # Function_54_DAE5 end

    def Function_55_DB58(): pass

    label("Function_55_DB58")

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
        "#5P……来了吗。\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x101,
        (
            "#0003F#11P……来是来了，但这不是重点。\x02\x03",

            "#0001F所谓的『训练圣书会成员』……\x01",
            "这种委托内容也太乱来了吧。\x02\x03",

            "警察怎么可能\x01",
            "训练不良少年啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0707
    ChrTalk(
        0x102,
        (
            "#12P#0105F委托人的姓名并不是瓦吉，\x01",
            "而是您，也就是说……\x01",
            "这是您的主意吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0708
    ChrTalk(
        0x9,
        (
            "#5P嗯，看起来，\x01",
            "你们好像是有些误会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x9,
        (
            "#5P我先来说明一下吧，\x01",
            "请到这边来。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_DD3D():

        label("loc_DD3D")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_DD3D")

    QueueWorkItem2(0x0, 1, lambda_DD3D)

    def lambda_DD4F():

        label("loc_DD4F")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_DD4F")

    QueueWorkItem2(0x1, 1, lambda_DD4F)

    def lambda_DD61():

        label("loc_DD61")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_DD61")

    QueueWorkItem2(0x2, 1, lambda_DD61)

    def lambda_DD73():

        label("loc_DD73")

        TurnDirection(0xFE, 0x9, 300)
        Yield()
        Jump("loc_DD73")

    QueueWorkItem2(0x3, 1, lambda_DD73)

    def lambda_DD85():
        OP_95(0xFE, 7550, 0, 14780, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_DD85)
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
        "#11P其实这件委托并没有那么复杂。\x02",
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x9,
        (
            "#11P──想委托你们的，\x01",
            "只是指导我们的成员学习防身术而已。\x02",
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
        "#6P#0005F……哎…………！？\x02",
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x104,
        (
            "#6P#0305F防身术……？\x02\x03",

            "#0301F喂喂，让他们学习那种东西，\x01",
            "难道是想用来打架吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x9,
        "#11P我刚才说过，你们误会了。\x02",
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x9,
        "#11P我们要警惕的敌人是黑手党。\x02",
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x103,
        (
            "#6P#0200F黑手党……\x01",
            "鲁巴彻或是黑月吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x102,
        (
            "#6P#0101F说起来，\x01",
            "这些黑手党组织最近\x01",
            "好像开始互相争斗了呢……\x02\x03",

            "#0103F虽然都是些零星的活动，\x01",
            "但听说有时也会出现\x01",
            "枪击行为呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x9,
        "#11P正是如此。\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x9,
        (
            "#11P而且，旧城区往往\x01",
            "处于风口浪尖的位置。\x02",
        )
    )

    CloseMessageWindow()

    #C0720
    ChrTalk(
        0x9,
        (
            "#11P因为附近尽是一些仓库、废屋、空地……\x01",
            "对他们来说，都是些开战的好地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0721
    ChrTalk(
        0x9,
        (
            "#11P对我们而言，\x01",
            "这种状况实在是不容乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x103,
        (
            "#6P#0203F所以才想学习防身术……您是这个意思吧。\x02\x03",

            "#0200F……话说起来，\x01",
            "在旧城区之前的那起事件中，圣书会就有\x01",
            "一名成员遭到暗算，昏迷了整整一周呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0723
    ChrTalk(
        0x101,
        (
            "#6P#0001F……原来如此…………\x01",
            "是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x9,
        "#11P你们理解得很快。\x02",
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x9,
        (
            "#11P按照我们原本的方案，\x01",
            "本来是想让大家学习\x01",
            "瓦吉的格斗技……\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x9,
        (
            "#11P但他的战斗技术比较特殊，\x01",
            "需要肢体有先天的柔软度。\x01",
            "若缺乏合适的体质，便无法顺利掌握。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x9,
        (
            "#11P而罗伊德·班宁斯曾经使用过的\x01",
            "警察特有的防身术很值得借鉴。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0x9,
        (
            "#11P不仅拥有出色的防御效果，\x01",
            "而且技巧比较主流，人人皆可学习……\x02",
        )
    )

    CloseMessageWindow()

    #C0729
    ChrTalk(
        0x9,
        (
            "#11P……那种战斗方式，\x01",
            "能否通过实战练习，\x01",
            "让我们的成员再见识一次呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x9,
        (
            "#11P当然了，这种技术肯定也不是一朝一夕\x01",
            "就能掌握的。但只需在他们的心中留下印象，\x01",
            "就能产生很好的刺激与督促效果了。\x02",
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

    def lambda_E4D1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4D1)
    Sleep(10)

    def lambda_E4E1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E4E1)

    def lambda_E4EE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E4EE)

    def lambda_E4FB():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4FB)
    Sleep(400)

    #C0731
    ChrTalk(
        0x102,
        (
            "#12P#0100F看起来，好像确实是\x01",
            "很正当的委托请求呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x103,
        (
            "#6P#0203F嗯，既然如此，应该可以接受吧。\x02\x03",

            "#0200F罗伊德前辈，要怎么做？\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x101,
        (
            "#5P#0003F实战形式的训练指导吗，\x01",
            "这个嘛……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E5BD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E5BD)
    Sleep(50)

    def lambda_E5CD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E5CD)

    def lambda_E5DA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E5DA)

    def lambda_E5E7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E5E7)
    Sleep(300)

    #C0734
    ChrTalk(
        0x101,
        (
            "#6P#0001F其实我用的并不是防身术，\x01",
            "而是在警察学校中学习的\x01",
            "一种压制格斗技……\x02\x03",

            "……这样也可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0x9,
        "#11P当然。\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x9,
        (
            "#11P为了训练得彻底一些，\x01",
            "你们那边的另外三位也可以参加。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x101,
        "#6P#0003F是吗……\x02",
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
            "【接受】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E718")
    OP_29(0x12, 0x1, 0x1)
    Call(0, 56)
    Return()

    label("loc_E718")


    #C0738
    ChrTalk(
        0x101,
        (
            "#6P#0001F……请再稍等一下。\x01",
            "我们也需要准备准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x9,
        "#11P是吗。\x02",
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x9,
        (
            "#11P我们今天一整天都有空。\x01",
            "你们做好充分准备之后再来吧。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_E814")
    SetChrPos(0xD, -4000, 0, 16690, 0)

    label("loc_E814")

    BeginChrThread(0xA, 0, 0, 1)
    SetChrPos(0x0, 600, 0, 8000, 90)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    OP_4C(0x9, 0xFF)
    BeginChrThread(0x9, 0, 0, 0)
    OP_29(0x12, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_55_DB58 end

    def Function_56_E852(): pass

    label("Function_56_E852")

    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xD, 0x2)

    #C0741
    ChrTalk(
        0x101,
        (
            "#6P#0003F既然情况如此，\x01",
            "我们自然没有拒绝的理由。\x02\x03",

            "#0000F不如说，这也许还能\x01",
            "帮助他们改过自新呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x104,
        (
            "#6P#0306F呼……我就知道你会这么说啊。\x02\x03",

            "#0300F罗伊德，即使是你，如果同时应付\x01",
            "他们全体成员，恐怕也会吃不消吧。\x01",
            "这种时候就不要客气了，让我们也加入吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E96D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E96D)

    def lambda_E97A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E97A)

    def lambda_E987():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E987)
    Sleep(200)

    #C0743
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，明白了。\x01",
            "大家都来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x9,
        "#11P那么，双方都已经达成一致了。\x02",
    )

    CloseMessageWindow()

    def lambda_E9EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E9EA)

    def lambda_E9F7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E9F7)

    def lambda_EA04():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EA04)
    Sleep(300)
    OP_93(0x9, 0xB4, 0x190)
    Sleep(500)

    #C0745
    ChrTalk(
        0x9,
        "#5P#4S──全员集合！\x02",
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

    def lambda_EA88():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EA88)
    Sleep(10)

    def lambda_EA98():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EA98)

    def lambda_EAA5():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EAA5)
    Sleep(8)

    def lambda_EAB5():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_EAB5)
    WaitChrThread(0xD, 0)
    Sleep(700)

    #C0746
    ChrTalk(
        0x9,
        (
            "#5P我们圣书会现在就要\x01",
            "展开模拟战斗了！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 60, -1, -1)
    SetChrName("众成员")

    #A0747
    AnonymousTalk(
        0xFF,
        "#5S明白！\x02",
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
            "任务【圣书会的训练委托】\x07\x00",
            "开始！\x02",
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

    # Function_56_E852 end

    def Function_57_EB87(): pass

    label("Function_57_EB87")

    OP_95(0xD, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xD, 2880, 30, 6910, 2000, 0x0)
    OP_93(0xD, 0x13B, 0x190)
    Return()

    # Function_57_EB87 end

    def Function_58_EBB7(): pass

    label("Function_58_EBB7")

    OP_95(0xC, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xC, 2180, 0, 6080, 2000, 0x0)
    OP_93(0xC, 0x13B, 0x190)
    Return()

    # Function_58_EBB7 end

    def Function_59_EBE7(): pass

    label("Function_59_EBE7")

    OP_95(0xA, 9250, 0, 7400, 2000, 0x0)
    OP_95(0xA, 3340, 0, 7400, 2000, 0x0)
    OP_95(0xA, 1330, 0, 5310, 2000, 0x0)
    OP_93(0xA, 0x13B, 0x190)
    Return()

    # Function_59_EBE7 end

    def Function_60_EC2B(): pass

    label("Function_60_EC2B")

    OP_95(0xB, 2460, 20, 2000, 2000, 0x0)
    OP_95(0xB, 2460, 20, 4550, 2000, 0x0)
    OP_95(0xB, 490, 0, 4550, 2000, 0x0)
    OP_93(0xB, 0x13B, 0x190)
    Return()

    # Function_60_EC2B end

    SaveToFile()

Try(main)
