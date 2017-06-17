from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c020c.bin",                # FileName
        "c020c",                    # MapName
        "c020c",                    # Location
        0x000A,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 10, 0, 2, 0, 3],
    )

    BuildStringList((
        "c020c",                  # 0
        "庞斯",                   # 1
        "布利克",                 # 2
        "贝奈特",                 # 3
        "爱尔莎",                 # 4
        "小桃",                   # 5
        "卢威克老人",             # 6
        "奥丽加夫人",             # 7
        "卡缇莉娜",               # 8
        "琪露露",                 # 9
        "游客",                   # 10
        "游客",                   # 11
        "游客",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "雷兹老人",               # 15
        "柯林",                   # 16
        "哈罗德",                 # 17
        "索菲亚",                 # 18
        "修利",                   # 19
        "SE控制",                 # 20
        "中央广场",               # 21
        "西街",                   # 22
        "行政区",                 # 23
        "住宅街",                 # 24
        "欢乐街",                 # 25
        "东街",                   # 26
        "旧城区",                 # 27
        "港湾区",                 # 28
        "ＩＢＣ",                 # 29
        "站前街道",               # 30
        "后巷",                   # 31
        "乌尔斯拉间道",           # 32
        "东克洛斯贝尔街道",       # 33
        "西克洛斯贝尔街道",       # 34
        "玛因兹山道",             # 35
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch20402.itc",                   # 01
        "chr/ch34300.itc",                   # 02
        "chr/ch10400.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch21600.itc",                   # 05
        "chr/ch20100.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch21800.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch21602.itc",                   # 0C
        "chr/ch21100.itc",                   # 0D
        "chr/ch21602.itc",                   # 0E
        "chr/ch24400.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-25120,  0,       4139,    180,  261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(6570,    -150,    5119,    90,   341,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(4869,    0,       629,     225,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4820,    3000,    17420,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(6309,    3000,    17329,   180,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6579,   0,       7170,    90,   261,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-5219,   0,       7170,    270,  261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-15020,  -2599,   -8350,   180,  405,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-13739,  -2599,   -8350,   180,  405,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(3349,    0,       -9760,   270,  261,  0x0, 0,   15,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(2089,    0,       -9760,   90,   261,  0x0, 0,   11,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1629,    3000,    13079,   180,  261,  0x0, 0,   9,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8039,    -150,    6960,    180,  469,  0x0, 0,   12,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(6980,    -300,    7619,    180,  389,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5500,    -200,    8000,    270,  469,  0x0, 0,   14,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 39,  39.5,                  -19.0,                 -4.5,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -19.75,                9.5,                   0.9000000357627869,    1.0])

    DeclActor(14410,   -6500,   -13590,  1200,    14410,   -5500,   -13590,  0x007C, 0,  4,  0x0000)
    DeclActor(-32070,  -1000,   11050,   1200,    -32070,  0,       11050,   0x007C, 0,  5,  0x0000)
    DeclActor(4050,    0,       -190,    1000,    4870,    1500,    630,     0x007E, 0,  8,  0x0000)
    DeclActor(-31040,  -1000,   9420,    1500,    -29950,  1000,    8850,    0x007C, 0,  30, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央广场")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西街")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "东街")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧城区")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "站前街道")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "后巷")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_7C8",          # 01, 1
        "Function_2_7F3",          # 02, 2
        "Function_3_A97",          # 03, 3
        "Function_4_C3E",          # 04, 4
        "Function_5_D93",          # 05, 5
        "Function_6_EE2",          # 06, 6
        "Function_7_1168",         # 07, 7
        "Function_8_14CF",         # 08, 8
        "Function_9_14D3",         # 09, 9
        "Function_10_1972",        # 0A, 10
        "Function_11_1A94",        # 0B, 11
        "Function_12_1AE4",        # 0C, 12
        "Function_13_1CBA",        # 0D, 13
        "Function_14_1DEB",        # 0E, 14
        "Function_15_2011",        # 0F, 15
        "Function_16_206C",        # 10, 16
        "Function_17_20D6",        # 11, 17
        "Function_18_2260",        # 12, 18
        "Function_19_23B6",        # 13, 19
        "Function_20_2607",        # 14, 20
        "Function_21_2760",        # 15, 21
        "Function_22_280C",        # 16, 22
        "Function_23_29F7",        # 17, 23
        "Function_24_2A9C",        # 18, 24
        "Function_25_37B8",        # 19, 25
        "Function_26_3820",        # 1A, 26
        "Function_27_3888",        # 1B, 27
        "Function_28_3BCB",        # 1C, 28
        "Function_29_3CFD",        # 1D, 29
        "Function_30_41A0",        # 1E, 30
        "Function_31_4214",        # 1F, 31
        "Function_32_4B59",        # 20, 32
        "Function_33_4B96",        # 21, 33
        "Function_34_4BB2",        # 22, 34
        "Function_35_4BCE",        # 23, 35
        "Function_36_4BEA",        # 24, 36
        "Function_37_4C06",        # 25, 37
        "Function_38_4DA7",        # 26, 38
        "Function_39_4E16",        # 27, 39
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_750"),
        (1, "loc_75C"),
        (2, "loc_768"),
        (3, "loc_774"),
        (4, "loc_780"),
        (5, "loc_78C"),
        (6, "loc_798"),
        (SWITCH_DEFAULT, "loc_7A4"),
    )


    label("loc_750")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_75C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_768")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_774")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_780")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_78C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_798")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7B0")

    label("loc_7C7")

    Return()

    # Function_0_710 end

    def Function_1_7C8(): pass

    label("Function_1_7C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F2")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_1_7C8")

    label("loc_7F2")

    Return()

    # Function_1_7C8 end

    def Function_2_7F3(): pass

    label("Function_2_7F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BE")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_891")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_8B0")

    label("loc_891")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_8B0")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_95F")

    label("loc_8BE")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_937")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_956")

    label("loc_937")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_956")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_956")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95F")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_98C")
    SetChrPos(0x13, 21980, 0, -10790, 135)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_A4E")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9D3")
    SetChrPos(0x13, -2410, 0, -1730, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_9CE")
    LoadEffect(0x0, "event\\eva02_00.eff")

    label("loc_9CE")

    Jump("loc_A4E")

    label("loc_9D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A3B")
    ClearChrFlags(0xB, 0x80)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    SetChrPos(0x13, -6580, 0, 5810, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A36")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x13, 0x80)

    label("loc_A36")

    Jump("loc_A4E")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A4E")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A5F")
    Event(0, 24)

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_A73")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 27)
    Jump("loc_A96")

    label("loc_A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_A87")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 28)
    Jump("loc_A96")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_A96")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 31)

    label("loc_A96")

    Return()

    # Function_2_7F3 end

    def Function_3_A97(): pass

    label("Function_3_A97")

    ClearMapObjFlags(0x9, 0x10)
    OP_70(0x9, 0x1E)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x8, 0xFF, 0xFFFF)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACD")
    OP_1B(0x1, 0x0, 0x25)
    OP_1B(0x8, 0x0, 0x26)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE0")
    OP_1B(0x1, 0x0, 0x25)

    label("loc_AE0")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFD")
    OP_66(0x3, 0x1)

    label("loc_AFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B1E")
    OP_65(0x1, 0x1)
    OP_66(0x3, 0x1)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")
    OP_70(0x7, 0x0)
    Jump("loc_B35")

    label("loc_B31")

    OP_70(0x7, 0x1E)

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")
    OP_70(0x8, 0x0)
    Jump("loc_B4C")

    label("loc_B48")

    OP_70(0x8, 0x1E)

    label("loc_B4C")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -25000, -4000, 4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, -4000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 24000, -4000, -8000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 4000, -1000, 18000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_A97 end

    def Function_4_C3E(): pass

    label("Function_4_C3E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D64")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x7, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×８０\x01\x07\x02",

            "#57I水之耀晶片×８０\x01\x07\x02",

            "#58I火之耀晶片×８０\x01\x07\x02",

            "#59I风之耀晶片×８０\x01\x07\x02",

            "#60I时之耀晶片×８０\x01\x07\x02",

            "#61I空之耀晶片×８０\x01\x07\x02",

            "#62I幻之耀晶片×８０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x110, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_D81")

    label("loc_D64")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_D81")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C3E end

    def Function_5_D93(): pass

    label("Function_5_D93")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E80")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('焰星铃', 1)"), scpexpr(EXPR_END)), "loc_E12")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '焰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_E7B")

    label("loc_E12")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '焰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '焰星铃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E7B")

    Jump("loc_EBD")

    label("loc_E80")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_EBD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE1")
    Call(0, 29)

    label("loc_EE1")

    Return()

    # Function_5_D93 end

    def Function_6_EE2(): pass

    label("Function_6_EE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F45")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今天日落之后，\x01",
            "将会有压轴的烟花哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "这可不能错过呢。\x01",
            "要占个好位置才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1164")

    label("loc_F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1089")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1032")

    #C0008
    ChrTalk(
        0xFE,
        "七十周年纪念日快乐！\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "庞斯架好了导力相机。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)

    #C0010
    ChrTalk(
        0xFE,
        (
            "你们怎么样？\x01",
            "开心吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1084")

    label("loc_1032")


    #C0011
    ChrTalk(
        0xFE,
        (
            "今天拍到的照片\x01",
            "都很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "呵呵，克洛斯贝尔万岁～！\x01",
            "七十周年纪念日快乐！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1084")

    Jump("loc_1164")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_10D0")

    #C0013
    ChrTalk(
        0xFE,
        (
            "嗯～大家的笑容\x01",
            "都很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "真期待显像结果啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1164")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_111F")

    #C0015
    ChrTalk(
        0xFE,
        "哦哦，连飞船也出来了啊……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "来来，再拍一张\x01",
            "留作纪念吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1164")

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1164")

    #C0017
    ChrTalk(
        0xFE,
        "嗯～不愧是创立纪念庆典啊！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "不愁找不到摄影题材呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1164")

    TalkEnd(0xFE)
    Return()

    # Function_6_EE2 end

    def Function_7_1168(): pass

    label("Function_7_1168")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11FC")
    Jump("loc_1246")

    label("loc_11FC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_121C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1246")

    label("loc_121C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_123C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1246")

    label("loc_123C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1246")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_12CB")

    #C0019
    ChrTalk(
        0xFE,
        (
            "今天下午将要\x01",
            "在市政厅召开闭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长也会出席，\x01",
            "我也去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C7")

    label("loc_12CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1344")

    #C0021
    ChrTalk(
        0xFE,
        (
            "像这样和外国人\x01",
            "悠闲聊着天，\x01",
            "还真有纪念庆典的气氛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "可以的话，希望他们\x01",
            "明年也能来克洛斯贝尔呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C7")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1386")
    SetChrSubChip(0xFE, 0x1)

    #C0023
    ChrTalk(
        0xFE,
        "哈哈，不要拘束啊。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        "来吧，一起干杯～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_14C7")

    label("loc_1386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_13F0")

    #C0025
    ChrTalk(
        0xFE,
        (
            "观光巴士加上飞行船啊……\x01",
            "今年可真是大手笔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "都没法安心看书了，\x01",
            "我也去转一圈吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C7")

    label("loc_13F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_14C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148A")

    #C0027
    ChrTalk(
        0xFE,
        (
            "我昨天去听了\x01",
            "市长的开幕演讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长\x01",
            "都已经年过七十了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "明明刚发生过那种事件，\x01",
            "却感觉不到他有丝毫衰弱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C7")

    label("loc_148A")


    #C0030
    ChrTalk(
        0xFE,
        "麦克道尔市长果然厉害呀。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "距离引退应该\x01",
            "还早得很吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1168 end

    def Function_8_14CF(): pass

    label("Function_8_14CF")

    Call(0, 9)
    Return()

    # Function_8_14CF end

    def Function_9_14D3(): pass

    label("Function_9_14D3")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196E")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1530")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1550")
    OP_AF(0xCF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1969")

    label("loc_1550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1564")
    Jump("loc_1969")

    label("loc_1564")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1969")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15D7")

    #C0032
    ChrTalk(
        0xA,
        (
            "呵呵……\x01",
            "奥斯卡，你就玩去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        (
            "趁此机会，我会好好\x01",
            "研究新品面包的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1969")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_162E")

    #C0034
    ChrTalk(
        0xA,
        "呵呵，人这么多，真是求之不得啊。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xA,
        (
            "要将我烤的面包\x01",
            "宣传给所有人！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1969")

    label("loc_162E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_17B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1754")

    #C0036
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0038
    ChrTalk(
        0xA,
        (
            "…………？\x01",
            "这孩子好像在哪里见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xA,
        (
            "……不过今天没看见呢。\x01",
            "小孩子孤身一个人的话，应该是很显眼的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 23)
    Jump("loc_17AC")

    label("loc_1754")


    #C0041
    ChrTalk(
        0xA,
        (
            "至少可以确定，\x01",
            "他没来试吃过新品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xA,
        (
            "……如果来的话，我一定会\x01",
            "给他推荐面包的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17AC")

    Jump("loc_1969")

    label("loc_17B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1808")

    #C0043
    ChrTalk(
        0xA,
        "呼呼，人这么多，真是求之不得啊。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "要将我烤的面包\x01",
            "宣传给所有人！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1969")

    label("loc_1808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_184B")

    #C0045
    ChrTalk(
        0xA,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        (
            "呵呵，不要客气，\x01",
            "尽量多买哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1969")

    label("loc_184B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18D2")

    #C0047
    ChrTalk(
        0xA,
        (
            "呵呵……这个月的新品面包\x01",
            "是由我负责的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xA,
        (
            "纪念庆典的人这么多，\x01",
            "一定会卖得很好！\x01",
            "趁此机会，给奥斯卡个下马威吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1969")

    label("loc_18D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1969")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192B")

    #C0049
    ChrTalk(
        0xA,
        "……请、请品尝一下吧。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xA,
        "如果觉得好吃，就请买一点吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1969")

    label("loc_192B")


    #C0051
    ChrTalk(
        0xA,
        "今天的面包是我烤的。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        "不、不嫌弃的话，就请买一点吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1969")

    Jump("loc_14E0")

    label("loc_196E")

    TalkEnd(0xA)
    Return()

    # Function_9_14D3 end

    def Function_10_1972(): pass

    label("Function_10_1972")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BE")

    #C0053
    ChrTalk(
        0xFE,
        "欢迎光临塔利兹商店～\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "请进来看看～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A21")

    label("loc_19BE")


    #C0055
    ChrTalk(
        0xFE,
        (
            "小桃真是的，\x01",
            "又缩在家里不出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "嗯～人这么多，\x01",
            "对那个内向的孩子来说，\x01",
            "也许很不自在吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A21")

    Jump("loc_1A90")

    label("loc_1A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A90")

    #C0057
    ChrTalk(
        0xFE,
        "欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "我那老公，还是和平时一样\x01",
            "悠然自得，什么都不做。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "我可得努力推销才行呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1A90")

    TalkEnd(0xFE)
    Return()

    # Function_10_1972 end

    def Function_11_1A94(): pass

    label("Function_11_1A94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACA")

    #C0060
    ChrTalk(
        0xFE,
        (
            "庆典……\x01",
            "来了好多客人啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AE0")

    label("loc_1ACA")


    #C0061
    ChrTalk(
        0xFE,
        "欢、欢迎光临……\x02",
    )

    CloseMessageWindow()

    label("loc_1AE0")

    TalkEnd(0xFE)
    Return()

    # Function_11_1A94 end

    def Function_12_1AE4(): pass

    label("Function_12_1AE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1B41")

    #C0062
    ChrTalk(
        0xFE,
        (
            "今天去中央广场一带\x01",
            "逛逛看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "说不定能买到\x01",
            "适合我们家的日用品呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB6")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1B96")
    OP_93(0xFE, 0x5A, 0x0)

    #C0064
    ChrTalk(
        0xFE,
        (
            "唔唔，今晚我受邀\x01",
            "参加晚餐会。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "你该不会\x01",
            "完全忘记了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB6")

    label("loc_1B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1BF7")

    #C0066
    ChrTalk(
        0xFE,
        "哎呀呀，已经走了啊。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "虽说每年都是这样，\x01",
            "但一旦结束，还是感觉有些寂寥呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB6")

    label("loc_1BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1C4D")
    OP_93(0xFE, 0x5A, 0x0)

    #C0068
    ChrTalk(
        0xFE,
        (
            "去高一点的地方，\x01",
            "会比较容易看到吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "你还真是不机灵啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CB6")

    label("loc_1C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C5E")
    Call(0, 13)
    Jump("loc_1CB6")

    label("loc_1C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CB6")

    #C0070
    ChrTalk(
        0xFE,
        (
            "这是难得的庆典，\x01",
            "大家一起开开心心地度过吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "庆典期间可以不拘小节啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1CB6")

    TalkEnd(0xFE)
    Return()

    # Function_12_1AE4 end

    def Function_13_1CBA(): pass

    label("Function_13_1CBA")

    OP_4B(0xD, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xD, 0x13, 0)
    TurnDirection(0x13, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D71")

    #C0072
    ChrTalk(
        0x13,
        "哎呀，这不是议员嘛。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x13,
        (
            "哦，已经引退了，\x01",
            "所以现在是前议员了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xD,
        (
            "记得你是\x01",
            "委员会的官员……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "呵呵，别来无恙吧？\x01",
            "那就再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1DE2")

    label("loc_1D71")


    #C0076
    ChrTalk(
        0xD,
        (
            "呵呵，我已经\x01",
            "不过问政治了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        (
            "话说，不如来我家坐坐，\x01",
            "一起喝一杯吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x13,
        (
            "哈哈哈，那我就\x01",
            "恭敬不如从命了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE2")

    OP_4C(0xD, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_13_1CBA end

    def Function_14_1DEB(): pass

    label("Function_14_1DEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E5D")
    OP_93(0xFE, 0x10E, 0x0)

    #C0079
    ChrTalk(
        0xFE,
        (
            "哎呀，今天不是要去\x01",
            "彩虹剧团看演出吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "要是去别处闲逛的话，\x01",
            "公演可就要结束了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1E5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_1EC2")
    OP_93(0xFE, 0x10E, 0x0)

    #C0081
    ChrTalk(
        0xFE,
        (
            "哎呀，先去那边的面包摊子\x01",
            "试吃一点也没关系嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "顺便买点\x01",
            "回去也不错吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F30")

    #C0083
    ChrTalk(
        0xFE,
        (
            "虽然每年都有，\x01",
            "不过看着游行真是令人心情愉快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "平日积累的怨气\x01",
            "也都抛到九霄云外去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F8B")
    OP_93(0xFE, 0x10E, 0x0)

    #C0085
    ChrTalk(
        0xFE,
        (
            "哎呀，游行队伍\x01",
            "要从那边过来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "在这里等待\x01",
            "当然是最好的了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1FCF")

    #C0087
    ChrTalk(
        0xFE,
        "我老伴曾经当过议员。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "所以还是有一定人脉的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_200D")

    label("loc_1FCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_200D")

    #C0089
    ChrTalk(
        0xFE,
        (
            "至少在纪念庆典期间，\x01",
            "就夫妇两人一起好好享受吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200D")

    TalkEnd(0xFE)
    Return()

    # Function_14_1DEB end

    def Function_15_2011(): pass

    label("Function_15_2011")

    TalkBegin(0xFE)

    #C0090
    ChrTalk(
        0xFE,
        "啊，快看快看，是飞行船哦！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "呜哇～……\x01",
            "装饰得好华丽。\x01",
            "不愧是纪念庆典呢～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2011 end

    def Function_16_206C(): pass

    label("Function_16_206C")

    TalkBegin(0xFE)
    OP_4B(0xF, 0xFF)

    #C0092
    ChrTalk(
        0xFE,
        (
            "呜～我还想\x01",
            "在家睡觉呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xFE, 500)

    #C0093
    ChrTalk(
        0xF,
        "哎～那多可惜啊～\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xF,
        "琪露露，一起逛吧！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x0)
    OP_4C(0xF, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_16_206C end

    def Function_17_20D6(): pass

    label("Function_17_20D6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_212C")

    #C0095
    ChrTalk(
        0xFE,
        "呼，已经到最终日了啊……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "城市太广阔，\x01",
            "我连一半都没逛到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225C")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2186")

    #C0097
    ChrTalk(
        0xFE,
        (
            "（嚼嚼）……\x01",
            "那边的面包店\x01",
            "正在举办试吃活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "你们也去吃点如何？\x02",
    )

    CloseMessageWindow()
    Jump("loc_225C")

    label("loc_2186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2205")

    #C0099
    ChrTalk(
        0xFE,
        (
            "你们知道吗？\x01",
            "在那个漂亮的喷泉前面，\x01",
            "有个什么村的人在开露天店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "超级推荐哦！\x01",
            "那个蛋包饭真是太美味了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_225C")

    label("loc_2205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_225C")

    #C0101
    ChrTalk(
        0xFE,
        (
            "我从帝国过来，\x01",
            "在铁道上摇晃了三个小时……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "终于到达\x01",
            "克洛斯贝尔了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225C")

    TalkEnd(0xFE)
    Return()

    # Function_17_20D6 end

    def Function_18_2260(): pass

    label("Function_18_2260")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_22C2")
    OP_93(0xFE, 0x5A, 0x0)

    #C0103
    ChrTalk(
        0xFE,
        "好，去欢乐街那边看看吧。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "难得从家里\x01",
            "溜出来嘛。\x01",
            "一定要玩个痛快！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B2")

    label("loc_22C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2300")
    OP_93(0xFE, 0x5A, 0x0)

    #C0105
    ChrTalk(
        0xFE,
        "喂，花心鬼！\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "不要转移\x01",
            "话题！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B2")

    label("loc_2300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2351")

    #C0107
    ChrTalk(
        0xFE,
        (
            "我觉得中央广场的\x01",
            "甜品店不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        "那里的东西超～美味的呀！\x02",
    )

    CloseMessageWindow()
    Jump("loc_23B2")

    label("loc_2351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23B2")

    #C0109
    ChrTalk(
        0xFE,
        (
            "因为妈妈一直不准我出来，\x01",
            "所以这么迟才能逛庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "既然如此，就更要\x01",
            "玩个痛快呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B2")

    TalkEnd(0xFE)
    Return()

    # Function_18_2260 end

    def Function_19_23B6(): pass

    label("Function_19_23B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244F")

    #C0111
    ChrTalk(
        0xFE,
        (
            "我记得那栋建筑物\x01",
            "以前是克洛斯贝尔时代周刊社……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "不过，周刊社应该\x01",
            "搬到商业街去了，\x01",
            "不知那栋建筑物现在是做什么的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_24A3")

    label("loc_244F")


    #C0113
    ChrTalk(
        0xFE,
        (
            "在街上随便逛逛，\x01",
            "就会有许多新发现呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "那栋建筑物，\x01",
            "现在的主人究竟是谁呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A3")

    Jump("loc_2603")

    label("loc_24A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_24DF")

    #C0115
    ChrTalk(
        0xFE,
        (
            "呼，今年的游行\x01",
            "真是华丽又热闹啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2603")

    label("loc_24DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2543")

    #C0116
    ChrTalk(
        0xFE,
        (
            "好吧，就在这边占个位置\x01",
            "来看游行吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "这是纪念庆典的焦点活动，\x01",
            "可不能错过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2603")

    label("loc_2543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2554")
    Call(0, 13)
    Jump("loc_2603")

    label("loc_2554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B9")

    #C0118
    ChrTalk(
        0xFE,
        (
            "纪念庆典还是\x01",
            "随意乱逛比较有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "城市会显得\x01",
            "和平时大不相同呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2603")

    label("loc_25B9")


    #C0120
    ChrTalk(
        0xFE,
        (
            "到处都有店主\x01",
            "在开露天店啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "唔唔，城市会显得\x01",
            "和平时大不相同呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2603")

    TalkEnd(0xFE)
    Return()

    # Function_19_23B6 end

    def Function_20_2607(): pass

    label("Function_20_2607")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_269B")
    Jump("loc_26E5")

    label("loc_269B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_26BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26E5")

    label("loc_26BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26DB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26E5")

    label("loc_26DB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26E5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0122
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔人会\x01",
            "热情地迎接外地人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "看来这是个\x01",
            "很适合居住的城市嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_2607 end

    def Function_21_2760(): pass

    label("Function_21_2760")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_27A5")

    #C0124
    ChrTalk(
        0xFE,
        (
            "真是精彩的\x01",
            "游行呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "嗯～果然是\x01",
            "来对了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2808")

    label("loc_27A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2808")

    #C0126
    ChrTalk(
        0xFE,
        (
            "说到克洛斯贝尔的庆典，\x01",
            "就一定少不了游行！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "我就是为了看这个，\x01",
            "才会远道而来的～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2808")

    TalkEnd(0xFE)
    Return()

    # Function_21_2760 end

    def Function_22_280C(): pass

    label("Function_22_280C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28A0")
    Jump("loc_28EA")

    label("loc_28A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28C0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28EA")

    label("loc_28C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28E0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28EA")

    label("loc_28E0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28EA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2945")

    #C0128
    ChrTalk(
        0x16,
        (
            "今天就在西街\x01",
            "悠闲地度过吧，\x01",
            "呵呵。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EF")

    label("loc_2945")


    #C0129
    ChrTalk(
        0x16,
        (
            "虽然我平时\x01",
            "都是在住宅街悠闲度日的。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x16,
        (
            "但我喜欢的那个长椅，今天却被一个\x01",
            "一脸疲惫的穿西装男子给占了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x16,
        (
            "呵呵，看他一副没精打采的样子，\x01",
            "我就把那座位让给他了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_29EF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_22_280C end

    def Function_23_29F7(): pass

    label("Function_23_29F7")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A9B")
    OP_29(0x46, 0x1, 0xB)

    #C0132
    ChrTalk(
        0x101,
        (
            "#0000F（这样一来，西街\x01",
            "  也基本转过一遍了……）\x02\x03",

            "（……不知道大家的\x01",
            "  搜索情况怎么样了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_2A9B")

    Return()

    # Function_23_29F7 end

    def Function_24_2A9C(): pass

    label("Function_24_2A9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(13500, 1000, -8500, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 12700, 0, -8500, 90)
    SetChrPos(0x160, 14300, 0, -8500, 270)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(40, 19, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x5)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0134
    AnonymousTalk(
        0x101,
        "#0001F喂，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2BED():
        OP_9A(0xFE, 0x101, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_2BED)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我是艾莉，\x01",
            "查到一点令人担心的事，\x01",
            "所以向你报告哦。\x02\x03",

            "我现在刚好\x01",
            "跟缇欧在一起……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是我，罗伊德前辈。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0137
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F嗯，你们会合了啊。\x02\x03",

            "那么，怎么样了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "关于柯林，他好像曾经在栈桥这里\x01",
            "眺望过水上巴士。\x02\x03",

            "但不清楚他之后\x01",
            "又去了哪里……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "于是我就拜托蔡特\x01",
            "探寻了一下气味。\x02\x03",

            "然后……\x01",
            "气味似乎是在栈桥到阶梯\x01",
            "的位置就突然中断了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0140
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F气味中断了……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，是在港湾区的东南端……\x02\x03",

            "这到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0142
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F……莫非是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x160, 1)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【进入车辆里面了】\x01",      # 0
            "【掉进河里去了】\x01",        # 1
            "【被谁抱走了】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EC4"),
        (1, "loc_2FFF"),
        (2, "loc_324B"),
        (SWITCH_DEFAULT, "loc_3430"),
    )


    label("loc_2EC4")

    OP_2C(0x46, 0x2)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0143
    AnonymousTalk(
        0x101,
        (
            "#0003F具有一定程度的密闭性，\x01",
            "气味不易外泄的地方……\x02\x03",

            "#0001F有可能是\x01",
            "乘上某辆车了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "原来如此……\x01",
            "这样就可以理解了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0146
    AnonymousTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F嗯，玲也同意哦。\x02\x03",

            "#3301F这样一来，接下来的问题就是，\x01",
            "他究竟上了什么车呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3430")

    label("loc_2FFF")

    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0147
    AnonymousTalk(
        0x101,
        (
            "#0011F该不会……\x01",
            "是掉进河里了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0148
    AnonymousTalk(
        0x160,
        (
            "#3306F真是的，大哥哥。\x01",
            "你是怎么听的啊。\x02\x03",

            "#3301F狼先生说的是\x01",
            "栈桥到阶梯的位置吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0149
    AnonymousTalk(
        0x101,
        "#0006F啊，是哦……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0150
    AnonymousTalk(
        0x160,
        (
            "#3303F即使是被人抱走了，\x01",
            "应该也会留下些许气味的。\x02\x03",

            "#3300F不过，如果是进入了\x01",
            "具有一定程度的密闭性的地方……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0151
    AnonymousTalk(
        0x101,
        "#0005F对了……是车辆吗！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "原来如此……\x01",
            "这样就可以理解了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0154
    AnonymousTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F嗯，就是这样。\x02\x03",

            "#3301F这样一来，接下来的问题就是，\x01",
            "他究竟上了什么车呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3430")

    label("loc_324B")

    OP_2C(0x46, 0x1)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0155
    AnonymousTalk(
        0x101,
        (
            "#0013F他被人抱着\x01",
            "离开了那里……\x02\x03",

            "#0008F不……应该不是。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0156
    AnonymousTalk(
        0x160,
        (
            "#3303F嗯，即使是被人抱走了，\x01",
            "应该也会留下些许气味的。\x02\x03",

            "#3300F可是，如果是进入了\x01",
            "具有一定程度的密闭性的地方……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0157
    AnonymousTalk(
        0x101,
        "#0005F对了……是车辆吗！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "原来如此……\x01",
            "这样就可以理解了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0160
    AnonymousTalk(
        0x160,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F嗯，就是这样。\x02\x03",

            "#3301F这样的话，接下来的问题就是，\x01",
            "他究竟上了什么车呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3430")

    label("loc_3430")

    OP_63(0x160, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x160)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "对了……\x01",
            "你旁边还有什么人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个女孩子的声音好像\x01",
            "在哪里听过呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0163
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F嗯，说来话长啦。\x02\x03",

            "#0001F总之，大家暂时先集合，\x01",
            "整理一下情报比较──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_352C():
        OP_96(0xFE, 0x37DC, 0x0, 0xFFFFDECC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_352C)
    WaitChrThread(0x160, 1)
    SetMessageWindowPos(50, 30, -1, -1)

    #A0164
    AnonymousTalk(
        0x160,
        (
            "#3304F──喂，大哥哥。\x02\x03",

            "#3300F支援科的终端，借我用一下哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0165
    AnonymousTalk(
        0x101,
        "#0005F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x160, 3, 0, 25)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0166
    ChrTalk(
        0x101,
        "#5P#0011F等、等一下！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x5)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0167
    AnonymousTalk(
        0x101,
        (
            "#0013F──艾莉、缇欧！\x01",
            "你们联络兰迪，\x01",
            "暂时先回支援科吧！\x02\x03",

            "到时候我再一起说明！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("艾莉的声音")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯、嗯……我明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("缇欧的声音")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不太清楚状况，不过好吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x4)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    SetCameraDistance(18500, 3000)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x160, 0xFF)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 3)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_2A9C end

    def Function_25_37B8(): pass

    label("Function_25_37B8")

    OP_92(0x160, 0x4650, 0xFFFFD440, 0x1F4)

    def lambda_37CA():
        OP_95(0xFE, 18000, 0, -11200, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_37CA)
    WaitChrThread(0x160, 1)

    def lambda_37E8():
        OP_95(0xFE, 18000, -2000, -19600, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_37E8)
    WaitChrThread(0x160, 1)

    def lambda_3806():
        OP_95(0xFE, 27000, -4000, -19600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_3806)
    WaitChrThread(0x160, 1)
    Return()

    # Function_25_37B8 end

    def Function_26_3820(): pass

    label("Function_26_3820")

    OP_92(0x101, 0x4650, 0xFFFFD440, 0x1F4)

    def lambda_3832():
        OP_95(0xFE, 18000, 0, -11200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3832)
    WaitChrThread(0x101, 1)

    def lambda_3850():
        OP_95(0xFE, 18000, -2000, -19600, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3850)
    WaitChrThread(0x101, 1)

    def lambda_386E():
        OP_95(0xFE, 27000, -4000, -19600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_386E)
    WaitChrThread(0x101, 1)
    Return()

    # Function_26_3820 end

    def Function_27_3888(): pass

    label("Function_27_3888")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07200.itc", 0x1E)
    LoadChrToIndex("chr/ch09300.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    OP_68(32800, -3000, -19000, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 35000, -4000, -19500, 270)
    SetChrPos(0x102, 35000, -4000, -18500, 270)
    SetChrPos(0x103, 36300, -4000, -19500, 270)
    SetChrPos(0x104, 36300, -4000, -18500, 270)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 31300, -4000, -19000, 90)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 30300, -4000, -18300, 90)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x20)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 30300, -4000, -19700, 90)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    MoveCamera(43, 23, 0, 11000)
    SetCameraDistance(21500, 11000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9C(0x17, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(100)
    OP_9C(0x17, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_63(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_93(0x17, 0x10E, 0x1F4)

    def lambda_3AAB():

        label("loc_3AAB")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_3AAB")

    QueueWorkItem2(0x18, 2, lambda_3AAB)

    def lambda_3ABD():

        label("loc_3ABD")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_3ABD")

    QueueWorkItem2(0x19, 2, lambda_3ABD)

    def lambda_3ACF():
        OP_96(0xFE, 0x75F8, 0xFFFFF060, 0xFFFFB5C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3ACF)
    WaitChrThread(0x17, 1)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    OP_63(0x17, 0x0, 1600, 0x8, 0x9, 0xFA, 0x0)

    def lambda_3B07():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B07)

    def lambda_3B21():
        OP_97(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3B21)

    def lambda_3B3B():
        OP_98(0xFE, 0xFFFFF060, 0x0, 0xFFFFFBB4, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3B3B)
    WaitChrThread(0x18, 1)

    def lambda_3B59():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B59)

    def lambda_3B73():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3B73)

    def lambda_3B8D():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x3E8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3B8D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x17)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x17, 0x1)
    OP_6F(0x79)
    SetScenarioFlags(0x5C, 5)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_3888 end

    def Function_28_3BCB(): pass

    label("Function_28_3BCB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(160, 5000, 20460, 0)
    MoveCamera(23, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -1000, 3000, 22200, 180)
    SetChrPos(0x102, 400, 3000, 22700, 180)
    SetChrPos(0x103, 400, 3000, 24260, 180)
    SetChrPos(0x104, -1000, 3000, 23860, 180)
    Sleep(50)

    def lambda_3C52():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C52)
    Sleep(100)

    def lambda_3C6A():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C6A)
    Sleep(100)

    def lambda_3C82():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C82)
    Sleep(100)

    def lambda_3C9A():
        OP_9B(0x0, 0xFE, 0x5, 0x2134, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C9A)
    OP_68(-2940, 5000, 12880, 4800)
    MoveCamera(41, 28, 0, 4800)
    OP_6E(600, 4800)
    SetCameraDistance(16500, 4800)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("c0240", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_3BCB end

    def Function_29_3CFD(): pass

    label("Function_29_3CFD")

    EventBegin(0x0)
    Fade(800)
    OP_68(-29840, 700, 9950, 0)
    MoveCamera(301, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetChrPos(0x101, -31110, -1000, 11250, 270)
    SetChrPos(0x102, -28840, -1000, 11440, 270)
    SetChrPos(0x103, -29910, -1000, 11720, 270)
    SetChrPos(0x104, -27680, -1000, 11600, 270)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_0D()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_93(0x101, 0xB4, 0x190)
    Sleep(600)

    #C0170
    ChrTalk(
        0x101,
        "#5P#0005F咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_3DBF():

        label("loc_3DBF")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_3DBF")

    QueueWorkItem2(0x104, 1, lambda_3DBF)

    def lambda_3DD1():

        label("loc_3DD1")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_3DD1")

    QueueWorkItem2(0x102, 1, lambda_3DD1)

    def lambda_3DE3():

        label("loc_3DE3")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_3DE3")

    QueueWorkItem2(0x103, 1, lambda_3DE3)
    OP_95(0x101, -31250, -1000, 9570, 700, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "栏杆上有很新的刮痕。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0172
    ChrTalk(
        0x104,
        "#12P#0305F罗伊德，发现什么了？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#5P#0001F嗯……好像有\x01",
            "一些刮痕。\x02\x03",

            "#0003F而且还是在靠里侧……\x01",
            "应该不会是过路的人\x01",
            "造成的……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#11P#0200F说起来，这个后门\x01",
            "最适合侵入公寓呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    TurnDirection(0x101, 0x103, 500)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_3F4D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3F4D)
    Sleep(10)

    def lambda_3F5D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F5D)

    def lambda_3F6A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F6A)
    Sleep(12)

    def lambda_3F7A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3F7A)
    Sleep(200)
    OP_68(-19620, 700, 13840, 4000)
    MoveCamera(16, 20, 0, 4000)
    Sleep(5200)
    Fade(500)
    OP_68(-29840, 700, 9950, 0)
    MoveCamera(301, 36, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    OP_0D()

    #C0175
    ChrTalk(
        0x104,
        (
            "#12P#0305F的确，走这里的话，就可以\x01",
            "避开大道，轻松溜进来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#12P#0103F目击情报很少，\x01",
            "就是这个原因吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_410A")

    #C0177
    ChrTalk(
        0x101,
        (
            "#5P#0000F好，预先调查就到此为止吧。\x02\x03",

            "先回伊莉娅小姐的房间，\x01",
            "整理一下情报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x104,
        "#12P#0300F明白，差不多也该考虑作战计划了吧！\x02",
    )

    CloseMessageWindow()
    OP_29(0x1D, 0x1, 0x9)
    Jump("loc_417E")

    label("loc_410A")


    #C0179
    ChrTalk(
        0x101,
        (
            "#5P#0003F…………………………\x02\x03",

            "#0001F现在就下判断还很危险，\x01",
            "再探听一下情报吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        "#12P#0300F明白，这就去吧。\x02",
    )

    CloseMessageWindow()

    label("loc_417E")

    SetChrPos(0x0, -30970, -1000, 11070, 270)
    OP_66(0x3, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_3CFD end

    def Function_30_41A0(): pass

    label("Function_30_41A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41BA")
    Call(0, 29)
    Return()

    label("loc_41BA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "栏杆上有\x01",
            "刮擦过的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    #A0182
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎是最近才有的……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_30_41A0 end

    def Function_31_4214(): pass

    label("Function_31_4214")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10100.itc", 0x1E)
    OP_68(-19540, 660, 12830, 0)
    MoveCamera(53, 41, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(31000, 0)
    SetChrPos(0x101, -29500, -1000, 11640, 56)
    SetChrPos(0x102, -8400, 0, 6880, 0)
    SetChrPos(0x103, -8400, 0, 6880, 0)
    SetChrPos(0x104, -10300, 0, 13950, 0)
    SetChrPos(0x1A, -19560, -1000, 14750, 180)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    OP_52(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0xA)
    MoveCamera(37, 31, 0, 3900)

    def lambda_42F4():
        OP_95(0xFE, -19560, -1000, 12750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_42F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1200)
    OP_95(0x104, -10300, 0, 7880, 4000, 0x0)
    Sleep(900)

    #N0183
    NpcTalk(
        0x104,
        "声音",
        "#5C#1P找到了吗……！？\x02",
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x102,
        "声音",
        (
            "#5C#1P已经不见踪影了，\x01",
            "大街上似乎也没人看见过。\x02",
        )
    )

    CloseMessageWindow()

    #N0185
    NpcTalk(
        0x103,
        "声音",
        "#5C#3P真奇怪呢……\x02",
    )

    CloseMessageWindow()

    #N0186
    NpcTalk(
        0x1A,
        "少年",
        (
            "#5P哼……\x01",
            "……以为那么简单\x01",
            "就可以抓到我吗？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-19540, 660, 12830, 0)
    MoveCamera(40, 36, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(27430, 0)
    OP_0D()
    Sleep(200)
    OP_93(0x1A, 0x10E, 0x190)
    Sleep(300)

    #N0187
    NpcTalk(
        0x1A,
        "少年",
        (
            "#5P这种城市里的\x01",
            "窝囊废……\x02",
        )
    )

    CloseMessageWindow()

    #N0188
    NpcTalk(
        0x1A,
        "少年",
        (
            "#5P哼，看着吧。\x01",
            "之后我再好好整你们……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-22720, 660, 11450, 1200)
    MoveCamera(56, 36, 0, 1200)
    OP_95(0x1A, -19900, -1000, 11430, 6000, 0x1)
    OP_95(0x1A, -22720, -1000, 11450, 6000, 0x0)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_9C(0x1A, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)

    #N0189
    NpcTalk(
        0x1A,
        "少年",
        "#11P啊……！？\x02",
    )

    CloseMessageWindow()

    #N0190
    NpcTalk(
        0x101,
        "声音",
        "#2P事情可没那么简单哦。\x02",
    )

    CloseMessageWindow()
    OP_68(-24890, 660, 11580, 2000)
    SetCameraDistance(31610, 2000)
    OP_95(0x101, -26250, -1000, 12160, 1800, 0x0)

    #C0191
    ChrTalk(
        0x101,
        (
            "#6P#0001F我们知道你走的是这条路线，\x01",
            "这次是我们的作战胜利了。\x02",
        )
    )

    CloseMessageWindow()

    #N0192
    NpcTalk(
        0x1A,
        "少年",
        "#11P可恶……！\x02",
    )

    CloseMessageWindow()

    def lambda_45B4():
        OP_95(0xFE, -21200, -1000, 11420, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_45B4)
    Sleep(50)

    #C0193
    ChrTalk(
        0x101,
        "#5P#0007F你还是放弃挣扎吧！\x02",
    )

    OP_68(-20560, 660, 11200, 2000)
    MoveCamera(306, 36, 0, 2000)
    OP_95(0x101, -21850, -1000, 11450, 6000, 0x0)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    CloseMessageWindow()

    #N0194
    NpcTalk(
        0x1A,
        "少年",
        (
            "#12P哇……可恶……！！\x01",
            "你这混账……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x1A, 2, 0, 32)
    Sleep(100)
    BeginChrThread(0x101, 2, 0, 32)

    #N0195
    NpcTalk(
        0x1A,
        "少年",
        "#12P放、放手……放开我……！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#5P#0001F那可不行。\x01",
            "你的行为是犯罪……\x02\x03",

            "#0006F……我说你，\x01",
            "老实一点啦……！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    BeginChrThread(0x1B, 1, 0, 36)

    #N0197
    NpcTalk(
        0x1A,
        "少年",
        "#12P可恶……混账！！\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#5P#0010F好痛……\x01",
            "喂，不要乱甩胳膊啊！！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x104, -11580, 0, 6930, 261)
    SetChrPos(0x102, -10570, 0, 6180, 261)
    SetChrPos(0x103, -10050, 0, 7210, 261)

    #C0199
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，这家伙真是\x01",
            "很有活力嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1A)
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    EndChrThread(0x1A, 0x2)

    def lambda_47C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_47C6)

    def lambda_47D3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47D3)
    OP_68(-18900, 860, 8630, 2000)
    MoveCamera(309, 24, 0, 2000)
    BeginChrThread(0x104, 1, 0, 35)
    Sleep(200)
    BeginChrThread(0x102, 1, 0, 33)
    Sleep(200)
    BeginChrThread(0x103, 1, 0, 34)
    Sleep(1200)

    #N0200
    NpcTalk(
        0x1A,
        "少年",
        "#11P你、你们是刚才的……\x02",
    )

    CloseMessageWindow()

    #N0201
    NpcTalk(
        0x1A,
        "少年",
        "#11P你、你们竟敢骗我……！？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        (
            "#0202F#12P嘻……\x01",
            "要演戏还真是累人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#6P#0100F虽然被你的敏捷身手\x01",
            "吓了一跳，\x01",
            "不过总算是抓到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        "#5P#0000F嗯，不过……\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1B58)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x1A, 0x5A, 0x1F4)
    OP_93(0x101, 0x5A, 0x1F4)
    BeginChrThread(0x1A, 2, 0, 32)
    Sleep(800)
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

    #C0205
    ChrTalk(
        0x104,
        (
            "#6P#0303F好像跟想象中的不太一样啊。\x02\x03",

            "#0300F听说是个朴素的家伙，\x01",
            "实际一看，倒不如说是不修边幅，\x01",
            "或者是有点脏兮兮吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#6P#0105F而且好像不是\x01",
            "克洛斯贝尔的孩子……\x02\x03",

            "是出身于某处边境地区吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#12P#0200F从犯罪行为来看，\x01",
            "与其说是狂热的崇拜者，\x01",
            "反而更像是偷闯空门的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#5P#0001F嗯，具体的事由，\x01",
            "还要请你一五一十交待清楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0209
    ChrTalk(
        0x101,
        (
            "#5P#0006F话说……\x01",
            "你差不多快给我老实点吧！\x02",
        )
    )

    CloseMessageWindow()

    #N0210
    NpcTalk(
        0x1A,
        "少年",
        (
            "#11P住手，放开我……！\x01",
            "……放手啊，你这个混账！！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(35190, 1800)
    OP_0D()
    EndChrThread(0x1B, 0x1)
    SetScenarioFlags(0x5C, 1)
    NewScene("c0240", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_31_4214 end

    def Function_32_4B59(): pass

    label("Function_32_4B59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B95")
    OP_A6(0xFE, 0x0, 0x14, 0x258, 0xBB8)
    Sleep(800)
    OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
    Sleep(1200)
    Jump("Function_32_4B59")

    label("loc_4B95")

    Return()

    # Function_32_4B59 end

    def Function_33_4B96(): pass

    label("Function_33_4B96")

    OP_95(0x102, -17370, 0, 6510, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_33_4B96 end

    def Function_34_4BB2(): pass

    label("Function_34_4BB2")

    OP_95(0x103, -16239, 0, 7090, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_34_4BB2 end

    def Function_35_4BCE(): pass

    label("Function_35_4BCE")

    OP_95(0x104, -17830, 0, 7480, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_35_4BCE end

    def Function_36_4BEA(): pass

    label("Function_36_4BEA")

    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Sleep(500)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 100, 0)
    Return()

    # Function_36_4BEA end

    def Function_37_4C06(): pass

    label("Function_37_4C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D39")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB9")

    #C0211
    ChrTalk(
        0x101,
        (
            "#0003F住宅街那边应该由\x01",
            "哈罗德先生在负责寻找……\x02\x03",

            "如果找到的话，\x01",
            "肯定会马上联络我的吧。\x02\x03",

            "#0001F还是按照原定计划，\x01",
            "继续在我负责的街区探听吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4D23")

    label("loc_4CB9")


    #C0212
    ChrTalk(
        0x101,
        (
            "#0003F住宅街那边应该由\x01",
            "哈罗德先生在负责寻找……\x02\x03",

            "#0001F还是按照原定计划，\x01",
            "继续在我负责的街区探听吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D23")

    Sleep(50)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)

    label("loc_4D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DA6")
    EventBegin(0x1)

    #C0213
    ChrTalk(
        0x101,
        (
            "#0001F现在可不是绕道的时候……\x02\x03",

            "还是尽快\x01",
            "前往西克洛斯贝尔街道吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 110, 3000, 22760, 180)
    EventEnd(0x4)

    label("loc_4DA6")

    Return()

    # Function_37_4C06 end

    def Function_38_4DA7(): pass

    label("Function_38_4DA7")

    EventBegin(0x1)

    #C0214
    ChrTalk(
        0x101,
        (
            "#0000F现在就算离开市区，\x01",
            "也打听不到情报的。\x02\x03",

            "……还是在这一带\x01",
            "再仔细探听一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    # Function_38_4DA7 end

    def Function_39_4E16(): pass

    label("Function_39_4E16")

    EventBegin(0x1)

    #C0215
    ChrTalk(
        0x101,
        (
            "#0000F现在没有什么要事……\x01",
            "还是专心寻找柯林吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 36500, -4000, -19000, 270)
    EventEnd(0x4)
    Return()

    # Function_39_4E16 end

    SaveToFile()

Try(main)
