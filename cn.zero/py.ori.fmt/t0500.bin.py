from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0500.bin",                # FileName
        "t0500",                    # MapName
        "t0500",                    # Location
        0x003C,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x06,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 3, 0, 4],
    )

    BuildStringList((
        "t0500",                  # 0
        "亚米",                   # 1
        "卡洛斯",                 # 2
        "亚雷库",                 # 3
        "矿工罗基",               # 4
        "霍夫曼矿山长",           # 5
        "矿工冈兹",               # 6
        "矿工玛尔罗",             # 7
        "矿工马库斯",             # 8
        "游客",                   # 9
        "游客露娜莉",             # 10
        "游客科比",               # 11
        "车",                     # 12
        "矿工玛尔罗",             # 13
        "黑手党",                 # 14
        "黑手党",                 # 15
        "索妮亚副司令",           # 16
        "诺艾尔上士",             # 17
        "巴士",                   # 18
        "警备队员",               # 19
        "警备队员",               # 20
        "警备队员",               # 21
        "警备队员",               # 22
        "SE控制",                 # 23
        "玛因兹山道",             # 24
        "玛因兹矿山",             # 25
    ))

    AddCharChip((
        "chr/ch23700.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch26300.itc",                   # 04
        "chr/ch22000.itc",                   # 05
        "chr/ch32200.itc",                   # 06
        "chr/ch30700.itc",                   # 07
        "chr/ch22100.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
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

    DeclNpc(6739,    0,       42729,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(10399,   0,       55259,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(28329,   -3000,   62000,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(15710,   -9000,   39830,   225,  385,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-24540,  11439,   55959,   90,   385,  0x0, 0,   4,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-21579,  11439,   57630,   180,  385,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    385,  0x0, 0,   3,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(850,     6000,    77519,   0,    385,  0x0, 0,   3,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4519,    -2000,   25190,   0,    385,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-610,    0,       67440,   270,  385,  0x0, 0,   8,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(870,     6000,    77220,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  19.399999618530273,    63.29999923706055,     -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.4666666984558105,   -12.65999984741211,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 37,  5.199999809265137,     58.400001525878906,    -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.3466666638851166,   -19.46666717529297,    0.20000000298023224,   1.0])

    DeclActor(-4600,   -2000,   28700,   1500,    -4600,   -500,    28700,   0x007C, 0,  25, 0x0000)
    DeclActor(12000,   400,     70000,   1500,    12000,   1400,    70000,   0x007C, 0,  26, 0x0000)
    DeclActor(-13210,  -2000,   25680,   1200,    -13210,  0,       25680,   0x007C, 0,  60, 0x0000)
    DeclActor(-25900,  11440,   56000,   1500,    -25900,  12940,   56000,   0x007C, 0,  27, 0x0000)

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "玛因兹矿山")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")
    PlaceName(-14.5, 0.0, 24.75, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_654",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_737",          # 02, 2
        "Function_3_762",          # 03, 3
        "Function_4_A14",          # 04, 4
        "Function_5_CC6",          # 05, 5
        "Function_6_D7F",          # 06, 6
        "Function_7_F02",          # 07, 7
        "Function_8_F97",          # 08, 8
        "Function_9_151B",         # 09, 9
        "Function_10_160A",        # 0A, 10
        "Function_11_1618",        # 0B, 11
        "Function_12_2032",        # 0C, 12
        "Function_13_2100",        # 0D, 13
        "Function_14_2AFC",        # 0E, 14
        "Function_15_346F",        # 0F, 15
        "Function_16_3A0C",        # 10, 16
        "Function_17_3ABB",        # 11, 17
        "Function_18_3C5D",        # 12, 18
        "Function_19_3DCF",        # 13, 19
        "Function_20_4060",        # 14, 20
        "Function_21_460E",        # 15, 21
        "Function_22_465C",        # 16, 22
        "Function_23_46EB",        # 17, 23
        "Function_24_47BA",        # 18, 24
        "Function_25_489D",        # 19, 25
        "Function_26_4AA9",        # 1A, 26
        "Function_27_4AE3",        # 1B, 27
        "Function_28_4BA7",        # 1C, 28
        "Function_29_4BD3",        # 1D, 29
        "Function_30_4C38",        # 1E, 30
        "Function_31_51F0",        # 1F, 31
        "Function_32_5216",        # 20, 32
        "Function_33_523C",        # 21, 33
        "Function_34_5262",        # 22, 34
        "Function_35_5288",        # 23, 35
        "Function_36_58F4",        # 24, 36
        "Function_37_58FB",        # 25, 37
        "Function_38_5902",        # 26, 38
        "Function_39_648C",        # 27, 39
        "Function_40_64D0",        # 28, 40
        "Function_41_6514",        # 29, 41
        "Function_42_654F",        # 2A, 42
        "Function_43_6B43",        # 2B, 43
        "Function_44_6BA6",        # 2C, 44
        "Function_45_6C09",        # 2D, 45
        "Function_46_6C6C",        # 2E, 46
        "Function_47_6CBE",        # 2F, 47
        "Function_48_7AE4",        # 30, 48
        "Function_49_7B36",        # 31, 49
        "Function_50_7BA6",        # 32, 50
        "Function_51_7BBA",        # 33, 51
        "Function_52_7BCE",        # 34, 52
        "Function_53_7F99",        # 35, 53
        "Function_54_7FA3",        # 36, 54
        "Function_55_826D",        # 37, 55
        "Function_56_82BF",        # 38, 56
        "Function_57_8311",        # 39, 57
        "Function_58_8363",        # 3A, 58
        "Function_59_83B5",        # 3B, 59
        "Function_60_8418",        # 3C, 60
        "Function_61_84B5",        # 3D, 61
        "Function_62_85F0",        # 3E, 62
    ))


    def Function_0_654(): pass

    label("Function_0_654")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_694"),
        (1, "loc_6A0"),
        (2, "loc_6AC"),
        (3, "loc_6B8"),
        (4, "loc_6C4"),
        (5, "loc_6D0"),
        (6, "loc_6DC"),
        (SWITCH_DEFAULT, "loc_6E8"),
    )


    label("loc_694")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_70B")

    Return()

    # Function_0_654 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_736")
    OP_94(0xFE, 0x1C98, 0x8EDA, 0x1F40, 0xB72A, 0x3E8)
    Sleep(300)
    Jump("Function_1_70C")

    label("loc_736")

    Return()

    # Function_1_70C end

    def Function_2_737(): pass

    label("Function_2_737")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_761")
    OP_94(0xFE, 0x648C, 0xEA38, 0x727E, 0xF488, 0x3E8)
    Sleep(300)
    Jump("Function_2_737")

    label("loc_761")

    Return()

    # Function_2_737 end

    def Function_3_762(): pass

    label("Function_3_762")

    BeginChrThread(0xA, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_792")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 900, 6000, 77780, 0)
    Jump("loc_971")

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7BC")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 900, 6000, 77780, 0)
    Jump("loc_971")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_817")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 910, 0, 50450, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -22550, 11440, 56120, 90)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -20140, 11440, 57900, 45)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_971")

    label("loc_817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_82B")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_971")

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_855")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 900, 6000, 77780, 0)
    Jump("loc_971")

    label("loc_855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_86E")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_887")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x8, 4520, -2000, 26540, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_971")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8C4")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_971")

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8DD")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_8DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F6")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_971")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_913")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_971")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_95D")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -21670, 11440, 55170, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -21580, 11440, 56390, 0)
    Jump("loc_971")

    label("loc_95D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_971")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xB, 0x80)

    label("loc_971")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98C")
    SetMapFlags(0x10000000)
    Event(0, 30)
    Jump("loc_99D")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_99D")
    Event(0, 54)

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_9B1")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 42)
    Jump("loc_9D4")

    label("loc_9B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_9C5")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 47)
    Jump("loc_9D4")

    label("loc_9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_9D4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 52)

    label("loc_9D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EC")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_9FB")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 7)

    label("loc_9FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_A13")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)

    label("loc_A13")

    Return()

    # Function_3_762 end

    def Function_4_A14(): pass

    label("Function_4_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A2B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2B")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A80")
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x13)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)

    label("loc_A80")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9C")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)

    label("loc_A9C")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB0")
    ClearMapObjFlags(0x6, 0x10)

    label("loc_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABE")
    OP_66(0x3, 0x1)

    label("loc_ABE")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Call(0, 28)
    SetMapObjFlags(0x9, 0x4)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B54")
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_B54")
    OP_66(0x2, 0x1)

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B65")
    Call(0, 29)

    label("loc_B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BDF")
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_66(0x2, 0x1)

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_END)), "loc_BF2")
    OP_16(0x3, 0x5, 0x1, 0x0)
    Jump("loc_C18")

    label("loc_BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_C13")
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0E")
    OP_16(0x3, 0x5, 0x1, 0x0)

    label("loc_C0E")

    Jump("loc_C18")

    label("loc_C13")

    OP_16(0x3, 0x5, 0x1, 0x0)

    label("loc_C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C44")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    Jump("loc_C6B")

    label("loc_C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C6B")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)

    label("loc_C6B")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C83")
    OP_1B(0x0, 0x0, 0x3E)

    label("loc_C83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C96")
    OP_1B(0x0, 0x0, 0x3E)

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA9")
    OP_1B(0x0, 0x0, 0x3E)

    label("loc_CA9")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Return()

    # Function_4_A14 end

    def Function_5_CC6(): pass

    label("Function_5_CC6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔北出口\x01",            # 0
            "停靠站（人偶工房附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D57")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D77")

    label("loc_D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D77")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_D77")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_CC6 end

    def Function_6_D7F(): pass

    label("Function_6_D7F")

    Fade(1000)
    OP_68(1060, -550, -2890, 0)
    MoveCamera(308, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    SetChrPos(0x1, -5300, -2000, 27570, 180)
    SetChrPos(0x2, -6100, -2000, 27430, 180)
    SetChrPos(0x3, -6860, -2000, 27250, 180)
    ClearChrFlags(0x19, 0x80)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x2)
    OP_78(0xA, 0x19)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x19, 0, -2000, -8290, 0)
    OP_D3(0x19, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)

    def lambda_E5A():
        OP_95(0xFE, 450, -2000, 6620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E5A)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x19, 1)
    Fade(1000)
    OP_68(-3860, -550, 26120, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x19, -6320, -2000, 18640, 0)

    def lambda_EC8():
        OP_95(0xFE, -6320, -2000, 21130, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_EC8)
    WaitChrThread(0x19, 1)
    OP_71(0xA, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0xA)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_6_D7F end

    def Function_7_F02(): pass

    label("Function_7_F02")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    SetChrPos(0x1, -4540, -2000, 27710, 180)
    SetChrPos(0x2, -4540, -2000, 27710, 180)
    SetChrPos(0x3, -4540, -2000, 27710, 180)
    OP_68(-4540, -550, 27710, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_F02 end

    def Function_8_F97(): pass

    label("Function_8_F97")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1513")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B0")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_103D")
    MenuCmd(1, 1, "★克洛斯贝尔·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1057")

    label("loc_103D")

    MenuCmd(1, 1, "　克洛斯贝尔·中央广场")

    label("loc_1057")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1087")
    MenuCmd(1, 1, "★克洛斯贝尔·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_109F")

    label("loc_1087")

    MenuCmd(1, 1, "　克洛斯贝尔·东出口")

    label("loc_109F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CF")
    MenuCmd(1, 1, "★克洛斯贝尔·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_10E7")

    label("loc_10CF")

    MenuCmd(1, 1, "　克洛斯贝尔·西出口")

    label("loc_10E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1117")
    MenuCmd(1, 1, "★克洛斯贝尔·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_112F")

    label("loc_1117")

    MenuCmd(1, 1, "　克洛斯贝尔·南出口")

    label("loc_112F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115F")
    MenuCmd(1, 1, "★克洛斯贝尔·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1177")

    label("loc_115F")

    MenuCmd(1, 1, "　克洛斯贝尔·北出口")

    label("loc_1177")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119F")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_11AF")

    label("loc_119F")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_11AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D7")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_11E7")

    label("loc_11D7")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_11E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1215")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_122B")

    label("loc_1215")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_122B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1267")

    label("loc_1255")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_1267")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1291")
    MenuCmd(1, 1, "★玛因兹矿山镇")
    MenuCmd(3, 1, 0x9)
    Jump("loc_12A3")

    label("loc_1291")

    MenuCmd(1, 1, "　玛因兹矿山镇")

    label("loc_12A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D3")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_12EB")

    label("loc_12D3")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_12EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1311")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_131F")

    label("loc_1311")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_131F")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A1")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x9)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13F4"),
        (1, "loc_1402"),
        (2, "loc_1410"),
        (3, "loc_141E"),
        (4, "loc_142C"),
        (5, "loc_143A"),
        (6, "loc_1448"),
        (7, "loc_1456"),
        (8, "loc_1464"),
        (9, "loc_1472"),
        (10, "loc_1480"),
        (11, "loc_148E"),
        (SWITCH_DEFAULT, "loc_149C"),
    )


    label("loc_13F4")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1402")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1410")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_141E")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_142C")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_143A")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1448")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1456")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1464")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1472")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_1480")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_148E")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_149C")

    label("loc_149C")

    Jump("loc_14AB")

    label("loc_14A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14AB")

    Jump("loc_150E")

    label("loc_14B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FB")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_150E")

    label("loc_14FB")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_150E")

    Jump("loc_FB1")

    label("loc_1513")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_F97 end

    def Function_9_151B(): pass

    label("Function_9_151B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -11920, -2000, 26400, 45)
    SetChrPos(0x1, -11920, -2000, 26400, 45)
    SetChrPos(0x2, -11920, -2000, 26400, 45)
    SetChrPos(0x3, -11920, -2000, 26400, 45)
    SetChrPos(0x4, -11920, -2000, 26400, 45)
    SetChrPos(0x5, -11920, -2000, 26400, 45)
    Sleep(1)
    OP_68(-11920, -550, 26400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15EF")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_15F5")

    label("loc_15EF")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_15F5")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_151B end

    def Function_10_160A(): pass

    label("Function_10_160A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    Return()

    # Function_10_160A end

    def Function_11_1618(): pass

    label("Function_11_1618")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_166E")

    #C0002
    ChrTalk(
        0xFE,
        (
            "镇长和冈兹先生\x01",
            "昨天都没回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "嗯～到底出了什么事呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_16D5")

    #C0004
    ChrTalk(
        0xFE,
        (
            "听说冈兹先生其实是在克洛斯贝尔市\x01",
            "挥金如土，过着奢华的生活？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "真会给人添麻烦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_16D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_176E")

    #C0006
    ChrTalk(
        0xFE,
        (
            "因为冈兹先生行踪不明，\x01",
            "卡洛斯先生好像\x01",
            "一直很自责。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "但我觉得这根本就不是\x01",
            "卡洛斯先生的责任呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "真是的，他就是一本正经过头了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_176E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_17D8")

    #C0009
    ChrTalk(
        0xFE,
        "啊，差不多该到日落的时候了。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "罗基哥哥今天\x01",
            "似乎工作得很认真，\x01",
            "回来时应该会很累吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1866")
    TurnDirection(0xFE, 0x109, 0)

    #C0011
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "真是威风凛凛，\x01",
            "又很帅气……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "可惜是个女人呢。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        "#0505F哎？那个……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "啊，请不必介意。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_18AD")

    label("loc_1866")


    #C0015
    ChrTalk(
        0xFE,
        (
            "本以为好不容易来了个帅哥，\x01",
            "结果竟然是女人吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "哎，没办法。\x02",
    )

    CloseMessageWindow()

    label("loc_18AD")

    Jump("loc_202E")

    label("loc_18B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1939")

    #C0017
    ChrTalk(
        0xFE,
        (
            "结果，在今年的纪念庆典\x01",
            "也没有什么像样的邂逅吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "不行，明年一定要……！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "……不过，去年好像也这么说过……\x02",
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FF")

    #C0020
    ChrTalk(
        0xFE,
        "唉……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "昨天，我们镇上\x01",
            "来了个很帅的\x01",
            "游客呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "但他就在风景好的地方\x01",
            "眺望了一下，\x01",
            "然后就立刻返回克洛斯贝尔市了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……呜～好不甘心！\x01",
            "感觉就像被耍了一样！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A6D")

    label("loc_19FF")


    #C0024
    ChrTalk(
        0xFE,
        (
            "观赏了风景之后，\x01",
            "竟然马上就\x01",
            "返回克洛斯贝尔市……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "真应该把他拉去\x01",
            "『红砖亭』喝点好酒，\x01",
            "然后灌醉啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6D")

    Jump("loc_202E")

    label("loc_1A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8D")
    Call(0, 12)
    Jump("loc_1AD1")

    label("loc_1A8D")


    #C0026
    ChrTalk(
        0xFE,
        (
            "来，来。\x01",
            "这位小哥，不要客气。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "我带你去\x01",
            "风景优美的地方吧⊥\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD1")

    Jump("loc_202E")

    label("loc_1AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B4A")

    #C0028
    ChrTalk(
        0xFE,
        (
            "『彩虹剧团』的首日公演\x01",
            "好像去了超多人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "能够动员那么多人，\x01",
            "不愧是大明星伊莉娅·普拉提耶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_1B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C04")

    #C0030
    ChrTalk(
        0xFE,
        (
            "前一阵子，我坐巴士\x01",
            "去克洛斯贝尔市\x01",
            "看帅哥。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "穿过隧道的时候，\x01",
            "看到了一个像人偶一样\x01",
            "可爱的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "好像不是这附近的孩子……\x01",
            "她在那种地方干什么呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C57")

    label("loc_1C04")


    #C0033
    ChrTalk(
        0xFE,
        (
            "我记得那附近好像\x01",
            "有个叫什么贝尔克的\x01",
            "工房……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "那孩子\x01",
            "在那种地方干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C57")

    Jump("loc_202E")

    label("loc_1C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5D")

    #C0035
    ChrTalk(
        0xFE,
        (
            "唉……我们镇上\x01",
            "为什么没有好男人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "当矿工的哥哥\x01",
            "经常偷懒，又不好相处。\x01",
            "其他的矿工也都很土气……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "卡洛斯先生还算及格，\x01",
            "但是文弱过头了，\x01",
            "不是我喜欢的类型呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "果然还是只能去克洛斯贝尔市\x01",
            "狩猎……不，是找帅哥了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1DAD")

    label("loc_1D5D")


    #C0039
    ChrTalk(
        0xFE,
        (
            "要找好男人，\x01",
            "果然还是只能\x01",
            "去克洛斯贝尔市了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "稍后就坐巴士去看看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1DAD")

    Jump("loc_202E")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1DC0")
    Jump("loc_202E")

    label("loc_1DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")

    #C0041
    ChrTalk(
        0xFE,
        (
            "……（发抖）。\x01",
            "天气冷起来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "……哦，镇长叫我\x01",
            "在天黑之前\x01",
            "赶紧回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "我可不想在夜路上\x01",
            "被魔兽袭击啊。\x01",
            "赶紧回家吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E8C")

    label("loc_1E5E")


    #C0044
    ChrTalk(
        0xFE,
        (
            "山里的夜晚很冷呢～\x01",
            "晚饭不然\x01",
            "就做炖菜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8C")

    Jump("loc_202E")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_202E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EB6")
    SetScenarioFlags(0x66, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_1EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7F")

    #C0045
    ChrTalk(
        0xFE,
        (
            "（哎呀……\x01",
            "  竟然有两个帅哥！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x101,
        "#0005F那个……？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "呵呵，我什么都没说哦，小哥。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "这里是矿山镇玛因兹。\x01",
            "请慢慢逛吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6F, 6)
    Jump("loc_202E")

    label("loc_1F7F")


    #C0049
    ChrTalk(
        0xFE,
        (
            "（这个穿夹克衫的小哥\x01",
            "  长得很可爱，\x01",
            "  那个高个子的大哥也很帅⊥）\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0006F（从刚才起就一直这样，怎么回事……？）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0304F（嗯～被女孩子盯着看，\x01",
            "  感觉果然不坏啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1618 end

    def Function_12_2032(): pass

    label("Function_12_2032")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    TurnDirection(0x8, 0x10, 0)
    TurnDirection(0x10, 0x8, 0)

    #C0052
    ChrTalk(
        0x10,
        (
            "这里好像……\x01",
            "不是阿尔摩利卡村啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x10,
        (
            "嗯～坐错\x01",
            "巴士了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "小哥，我们矿山镇玛因兹\x01",
            "也是风景优美的好地方哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "不介意的话，\x01",
            "我来给你带路吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10,
        "嗯，那个……\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_12_2032 end

    def Function_13_2100(): pass

    label("Function_13_2100")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21B1")

    #C0057
    ChrTalk(
        0xFE,
        (
            "昨晚我本来\x01",
            "打算开车去接\x01",
            "镇长他们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "但是镇长说可能\x01",
            "还要再待一阵子，就拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "在通讯的时候，\x01",
            "镇长的声音听起来\x01",
            "好像没什么精神……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_220F")

    label("loc_21B1")


    #C0060
    ChrTalk(
        0xFE,
        (
            "说是可能要在\x01",
            "克洛斯贝尔市\x01",
            "再待上一阵子……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "镇长的声音好像没什么精神，很令人担心呢。\x02",
    )

    CloseMessageWindow()

    label("loc_220F")

    Jump("loc_2AF8")

    label("loc_2214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_227F")

    #C0062
    ChrTalk(
        0xFE,
        (
            "镇长去克洛斯贝尔市\x01",
            "接冈兹先生了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "唉，总而言之，\x01",
            "只要知道他在哪里\x01",
            "也就暂时放心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_227F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_23B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2351")

    #C0064
    ChrTalk(
        0xFE,
        (
            "其实，那天是我把冈兹先生\x01",
            "送到克洛斯贝尔市的。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "反正要搬运矿石，\x01",
            "就顺便送他去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "……可是，过了\x01",
            "约定的时间，\x01",
            "冈兹先生也没有回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "拜托了……\x01",
            "请务必要找到冈兹先生。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_23B2")

    label("loc_2351")


    #C0068
    ChrTalk(
        0xFE,
        (
            "是我把冈兹先生送到\x01",
            "克洛斯贝尔市的，\x01",
            "所以我也有责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "拜托了……\x01",
            "请务必要找到冈兹先生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B2")

    Jump("loc_2AF8")

    label("loc_23B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_247E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_244B")

    #C0070
    ChrTalk(
        0xFE,
        (
            "啊……你们是\x01",
            "接到镇长联络而来的\x01",
            "特别任务支援科成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "谢谢你们过来。\x01",
            "镇长正在等着呢，请去里面那座房子找他吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2479")

    label("loc_244B")


    #C0072
    ChrTalk(
        0xFE,
        "镇长正在等着呢，请去里面那座房子找他吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2479")

    Jump("loc_2AF8")

    label("loc_247E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2530")

    #C0073
    ChrTalk(
        0xFE,
        (
            "来我们镇子的隧道途中，\x01",
            "不是有条分岔路吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "那条路的尽头有处遗迹，\x01",
            "最近从那里有时会传来\x01",
            "类似钟声一样的奇怪声音。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "那一带明明没有人迹的，\x01",
            "真是诡异啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25B5")

    #C0076
    ChrTalk(
        0xFE,
        (
            "好，今天晚上\x01",
            "还得去接矿工们呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "冈兹先生今年\x01",
            "能不能赚到钱呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……嗯，应该没戏吧。\x01",
            "毕竟是冈兹先生……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_25B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2651")

    #C0079
    ChrTalk(
        0xFE,
        (
            "因为有机会去看纪念庆典，\x01",
            "所以就稍微转了转……\x01",
            "呀，今年也是人山人海呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "据说那也是『彩虹剧团』的\x01",
            "新剧的影响……\x01",
            "我觉得一点也没错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_26C0")

    #C0081
    ChrTalk(
        0xFE,
        (
            "今天准备搬运矿石，\x01",
            "顺便看看纪念庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "嗯～真期待啊。\x01",
            "去『龙老饭店』\x01",
            "吃顿饭似乎也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_26C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2730")

    #C0083
    ChrTalk(
        0xFE,
        (
            "年轻的矿工们\x01",
            "都出镇去看纪念庆典了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "平时工作都很辛苦，\x01",
            "希望他们趁此机会释放一下压力呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_2730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27F0")

    #C0085
    ChrTalk(
        0xFE,
        (
            "我们矿山开采出的七耀石\x01",
            "会用于多种领域。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "细小的碎片用作结晶回路的材料，\x01",
            "大颗的结晶用来加工成宝石等等。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "一想到由我运送的\x01",
            "七耀石能派上某些用场，\x01",
            "就不由得感慨良多啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_27F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_28A2")

    #C0088
    ChrTalk(
        0xFE,
        (
            "我负责用搬运车来运送\x01",
            "开采出来的七耀石……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "但真担心以后有那么一天，\x01",
            "再也没有七耀石可以开采了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "埋在矿山里的七耀石\x01",
            "可不是无限的，\x01",
            "连我也明白这一点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF8")

    label("loc_28A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_28B0")
    Jump("loc_2AF8")

    label("loc_28B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2A73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C3")

    #C0091
    ChrTalk(
        0xFE,
        (
            "从山上看晚霞可真美啊。\x01",
            "仿佛连心灵都被净化了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "说起来……就在前一阵子，\x01",
            "我见到有个很大的东西\x01",
            "飞过这片天空。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "要比这附近的\x01",
            "鸟或魔兽大得太多了。\x01",
            "那到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F（嗯～这话令人有点在意……\x01",
            "  但应该和这次事件没什么关系吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 0)
    Jump("loc_2A6E")

    label("loc_29C3")


    #C0095
    ChrTalk(
        0xFE,
        (
            "前一阵子，\x01",
            "我见到有个很大的东西\x01",
            "飞过这片天空。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "要比这附近的\x01",
            "鸟或魔兽大得太多了。\x01",
            "那到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "不过，那时是晚上，而且又下着雨，\x01",
            "说不定只是我看错了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6E")

    Jump("loc_2AF8")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2AF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A98")
    SetScenarioFlags(0x66, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_2A98")


    #C0098
    ChrTalk(
        0xFE,
        "停在村子入口的搬运车好高级……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "刚才那些人竟然\x01",
            "拥有那么高级的好车，\x01",
            "到底是什么来头呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF8")

    TalkEnd(0xFE)
    Return()

    # Function_13_2100 end

    def Function_14_2AFC(): pass

    label("Function_14_2AFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD9")

    #C0100
    ChrTalk(
        0xFE,
        (
            "矿工叔叔们\x01",
            "似乎把冈兹叔叔的工作\x01",
            "也平摊做好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "大家都毫无怨言，\x01",
            "默默担起了工作。\x01",
            "就连最怕麻烦的罗基叔叔也是……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……矿工叔叔们真会为同伴着想啊，\x01",
            "矿工果然是个令人憧憬的职业呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2C45")

    label("loc_2BD9")


    #C0103
    ChrTalk(
        0xFE,
        (
            "虽然妈妈说那是危险的工作，\x01",
            "不让我去做……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "但是我也想成为像叔叔们一样，\x01",
            "会为同伴着想的出色矿工呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C45")

    Jump("loc_346B")

    label("loc_2C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D40")

    #C0105
    ChrTalk(
        0xFE,
        (
            "冈兹叔叔似乎被找到了。\x01",
            "太好了～\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "那个，冈兹叔叔还好吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_2D01")

    #C0107
    ChrTalk(
        0x101,
        (
            "#0008F…………………………\x02\x03",

            "（他可能服用了那种药物的事，\x01",
            "  实在说不出口啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D38")

    label("loc_2D01")


    #C0108
    ChrTalk(
        0x101,
        (
            "#0000F嗯，你就放心吧。\x01",
            "（虽然情况有点不对劲……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D38")

    SetScenarioFlags(0x0, 5)
    Jump("loc_2D7E")

    label("loc_2D40")


    #C0109
    ChrTalk(
        0xFE,
        (
            "等冈兹叔叔回来以后，\x01",
            "要让他再给我讲讲\x01",
            "克洛斯贝尔市的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7E")

    Jump("loc_346B")

    label("loc_2D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_2DD7")

    #C0110
    ChrTalk(
        0xFE,
        (
            "冈兹叔叔，到底\x01",
            "去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "平时最久也是\x01",
            "去三天就回来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_2DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2E2B")

    #C0112
    ChrTalk(
        0xFE,
        (
            "听玛尔罗叔叔说，\x01",
            "冈兹叔叔好像\x01",
            "失踪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "到底出了什么事呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E86")

    #C0114
    ChrTalk(
        0xFE,
        (
            "说起来……\x01",
            "最近好像都没看到冈兹叔叔啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "还想听他讲讲市里的事情呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_2E86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2FAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F52")

    #C0116
    ChrTalk(
        0xFE,
        (
            "昨天我听罗基叔叔\x01",
            "说工作没意思，\x01",
            "让我深有感触。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "矿工叔叔们都是\x01",
            "很不情愿地工作着吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "但在收工之后的饮酒会时，\x01",
            "还有谈起『巴鲁卡』的时候，\x01",
            "他们看上去都那么开心……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FAA")

    label("loc_2F52")


    #C0119
    ChrTalk(
        0xFE,
        (
            "矿工叔叔们都是\x01",
            "很不情愿地工作着吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "对于想当矿工的我来说，\x01",
            "还真有点受打击。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FAA")

    Jump("loc_346B")

    label("loc_2FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3026")

    #C0121
    ChrTalk(
        0xFE,
        (
            "我很憧憬矿工这个职业，\x01",
            "所以向罗基叔叔询问\x01",
            "这工作有什么优点……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "罗基叔叔……\x01",
            "不喜欢这工作吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_3026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3089")

    #C0123
    ChrTalk(
        0xFE,
        (
            "我爸爸\x01",
            "是矿山长，\x01",
            "非常有男子汉气概。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "所以我将来也要当矿工。\x01",
            "嘿嘿，不错吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_3089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_30F0")

    #C0125
    ChrTalk(
        0xFE,
        (
            "昨天爸爸好像也去\x01",
            "参加了宴会，真是少见。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "真羡慕啊～……\x01",
            "要是也能带我去\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_30F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_31EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3196")

    #C0127
    ChrTalk(
        0xFE,
        (
            "昨天我在外边跑来跑去时，\x01",
            "狠狠摔了一跤……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "身上擦伤了好多处，\x01",
            "回家之后被妈妈大骂了一顿呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "呜呜……\x01",
            "以后可得小心脚下才行啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_31E6")

    label("loc_3196")


    #C0130
    ChrTalk(
        0xFE,
        (
            "昨天我被那边的梯子绊到，\x01",
            "狠狠摔了一跤……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "真够痛的。\x01",
            "以后小心点吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E6")

    Jump("loc_346B")

    label("loc_31EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327E")

    #C0132
    ChrTalk(
        0xFE,
        (
            "在山道的岔路深处\x01",
            "有座奇怪的遗迹，你们见过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "看到那种东西，我就觉得很兴奋呢。\x01",
            "以后有机会的话，真想去探险啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_32EC")

    label("loc_327E")


    #C0134
    ChrTalk(
        0xFE,
        (
            "在山道的岔路深处\x01",
            "有座奇怪的遗迹，你们见过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "里面会是什么样子呢……\x01",
            "以后有机会的话，真想去探险啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EC")

    Jump("loc_346B")

    label("loc_32F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_32FF")
    Jump("loc_346B")

    label("loc_32FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_337B")

    #C0136
    ChrTalk(
        0xFE,
        (
            "我爸爸是\x01",
            "管理整个矿山的矿山长。\x01",
            "很厉害吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "今天爸爸在矿山中的工作\x01",
            "好像也结束了……\x01",
            "要不要去接他呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_346B")

    label("loc_337B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_346B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A0")
    SetScenarioFlags(0x66, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_33A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342F")

    #C0138
    ChrTalk(
        0xFE,
        (
            "镇子外面有个\x01",
            "封闭的坑道入口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "听说那里是以前的废矿，\x01",
            "真想去探险呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "不过，要是靠近的话，\x01",
            "会被镇长叔叔骂的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_346B")

    label("loc_342F")


    #C0141
    ChrTalk(
        0xFE,
        (
            "总觉得那种废矿里\x01",
            "好像沉眠着什么宝物呢，\x01",
            "真想去探险啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_346B")

    TalkEnd(0xFE)
    Return()

    # Function_14_2AFC end

    def Function_15_346F(): pass

    label("Function_15_346F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3480")
    Jump("loc_3A08")

    label("loc_3480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_348E")
    Jump("loc_3A08")

    label("loc_348E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_34D2")

    #C0142
    ChrTalk(
        0xFE,
        (
            "呜……\x01",
            "总算干完活了……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "好累，赶紧\x01",
            "回家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A08")

    label("loc_34D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_34E0")
    Jump("loc_3A08")

    label("loc_34E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_34EE")
    Jump("loc_3A08")

    label("loc_34EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_356E")

    #C0144
    ChrTalk(
        0xFE,
        (
            "矿山长的儿子\x01",
            "今天也没什么精神啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "果然是我的错吗……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "唉，竟然对小孩子发牢骚，\x01",
            "我可真是没用啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A08")

    label("loc_356E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_35F7")

    #C0147
    ChrTalk(
        0xFE,
        (
            "矿山长的儿子\x01",
            "向我询问矿工的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "我一不经意就说出了\x01",
            "『这工作又烦又累』\x01",
            "这种直白露骨的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "打击到他了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A08")

    label("loc_35F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3687")

    #C0150
    ChrTalk(
        0xFE,
        (
            "呼～好累……\x01",
            "喝酒之后，就会完全没有干劲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "……哈，不过我平时也没什么干劲。\x01",
            "不管怎么说，反正现在是纪念庆典，没关系吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A08")

    label("loc_3687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3695")
    Jump("loc_3A08")

    label("loc_3695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3795")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373B")

    #C0152
    ChrTalk(
        0xFE,
        (
            "矿工的薪水\x01",
            "可没有多少啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "虽然在这个镇上生活还好，\x01",
            "但要是去克洛斯贝尔市的欢乐街，\x01",
            "一转眼就会花个精光。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "真是的，太不平衡了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3790")

    label("loc_373B")


    #C0155
    ChrTalk(
        0xFE,
        (
            "虽然不停工作，\x01",
            "但我的生活还是没见好转……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "……不过，事实上我也经常偷懒啦。\x02",
    )

    CloseMessageWindow()

    label("loc_3790")

    Jump("loc_3A08")

    label("loc_3795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37FB")

    #C0157
    ChrTalk(
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "……我在偷懒，不行吗？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "就一小会，\x01",
            "别告诉其他矿工哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_383B")

    label("loc_37FB")


    #C0160
    ChrTalk(
        0xFE,
        (
            "我有点累了，\x01",
            "所以正在偷懒。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……不要告诉\x01",
            "其他矿工哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_383B")

    Jump("loc_3A08")

    label("loc_3840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_384E")
    Jump("loc_3A08")

    label("loc_384E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_38FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3869")
    Call(0, 16)
    Jump("loc_38F8")

    label("loc_3869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D5")

    #C0162
    ChrTalk(
        0xFE,
        (
            "呼啊～啊……\x01",
            "我还是早点回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "（因为适当偷了会懒，\x01",
            "  所以也没有那么累呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_38F8")

    label("loc_38D5")


    #C0164
    ChrTalk(
        0xFE,
        (
            "呼啊～啊……\x01",
            "早点回去睡觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F8")

    Jump("loc_3A08")

    label("loc_38FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3A08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3922")
    SetScenarioFlags(0x66, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_3922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39D0")

    #C0165
    ChrTalk(
        0xFE,
        (
            "前一阵子，有魔兽\x01",
            "袭击了住在这里的矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "虽然伤势\x01",
            "并不是非常重，\x01",
            "但为了保险起见，还是让他在家静养。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "……唉，我也想休息啊～\x01",
            "或者说想偷懒～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3A08")

    label("loc_39D0")


    #C0168
    ChrTalk(
        0xFE,
        (
            "受那点伤\x01",
            "就可以休息，真羡慕啊。\x01",
            "我也想偷懒啊～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A08")

    TalkEnd(0xFE)
    Return()

    # Function_15_346F end

    def Function_16_3A0C(): pass

    label("Function_16_3A0C")


    #C0169
    ChrTalk(
        0xFE,
        (
            "（……其实我在矿山里\x01",
            "  偷懒看书呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "（在被矿山长发现之前，\x01",
            "  你们能不能收下这本书？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了 。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('黑市医生格伦　３卷', 1)
    SetScenarioFlags(0x9C, 2)
    Return()

    # Function_16_3A0C end

    def Function_17_3ABB(): pass

    label("Function_17_3ABB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3ACC")
    Jump("loc_3C59")

    label("loc_3ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3ADA")
    Jump("loc_3C59")

    label("loc_3ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3B58")

    #C0172
    ChrTalk(
        0xFE,
        "总算把今天的工作干完了。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "冈兹那家伙不在，\x01",
            "效率果然很低啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "不管怎么说，那家伙\x01",
            "很擅长活跃气氛呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C59")

    label("loc_3B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3B66")
    Jump("loc_3C59")

    label("loc_3B66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3B74")
    Jump("loc_3C59")

    label("loc_3B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B82")
    Jump("loc_3C59")

    label("loc_3B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3B90")
    Jump("loc_3C59")

    label("loc_3B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B9E")
    Jump("loc_3C59")

    label("loc_3B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3BAC")
    Jump("loc_3C59")

    label("loc_3BAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BBA")
    Jump("loc_3C59")

    label("loc_3BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3BC8")
    Jump("loc_3C59")

    label("loc_3BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3BD6")
    Jump("loc_3C59")

    label("loc_3BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3C50")
    OP_93(0xFE, 0x5A, 0x0)

    #C0175
    ChrTalk(
        0xFE,
        (
            "你们去喝酒是可以，\x01",
            "但是尽量早点回来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "在马库斯那家伙回来之前，\x01",
            "今后一个人\x01",
            "也不许缺席啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C59")

    label("loc_3C50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C59")

    label("loc_3C59")

    TalkEnd(0xFE)
    Return()

    # Function_17_3ABB end

    def Function_18_3C5D(): pass

    label("Function_18_3C5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C6E")
    Jump("loc_3DCB")

    label("loc_3C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3C7C")
    Jump("loc_3DCB")

    label("loc_3C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3C8A")
    Jump("loc_3DCB")

    label("loc_3C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C98")
    Jump("loc_3DCB")

    label("loc_3C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3CA6")
    Jump("loc_3DCB")

    label("loc_3CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3CB4")
    Jump("loc_3DCB")

    label("loc_3CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3CC2")
    Jump("loc_3DCB")

    label("loc_3CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3CD0")
    Jump("loc_3DCB")

    label("loc_3CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3D3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CEB")
    Call(0, 19)
    Jump("loc_3D35")

    label("loc_3CEB")


    #C0177
    ChrTalk(
        0xFE,
        (
            "呜～……头还在痛。\x01",
            "完全宿醉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "嘁，还真羡慕\x01",
            "完全醉倒的罗基啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D35")

    Jump("loc_3DCB")

    label("loc_3D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3D48")
    Jump("loc_3DCB")

    label("loc_3D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D56")
    Jump("loc_3DCB")

    label("loc_3D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3D64")
    Jump("loc_3DCB")

    label("loc_3D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7F")
    Call(0, 19)
    Jump("loc_3DBD")

    label("loc_3D7F")


    #C0179
    ChrTalk(
        0xFE,
        (
            "我们从早到晚都在\x01",
            "阴暗的洞穴里干活。\x01",
            "这点奖励是应得的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBD")

    Jump("loc_3DCB")

    label("loc_3DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3DCB")

    label("loc_3DCB")

    TalkEnd(0xFE)
    Return()

    # Function_18_3C5D end

    def Function_19_3DCF(): pass

    label("Function_19_3DCF")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3DF3")
    Jump("loc_4051")

    label("loc_3DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3E01")
    Jump("loc_4051")

    label("loc_3E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3E0F")
    Jump("loc_4051")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3E1D")
    Jump("loc_4051")

    label("loc_3E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3E2B")
    Jump("loc_4051")

    label("loc_3E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3E39")
    Jump("loc_4051")

    label("loc_3E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3E47")
    Jump("loc_4051")

    label("loc_3E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E55")
    Jump("loc_4051")

    label("loc_3E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3F47")

    #C0180
    ChrTalk(
        0xD,
        (
            "呜～……\x01",
            "头还是疼得厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        "不管怎么想，都是喝多了啊。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xE,
        (
            "……不过，镇长真是好人啊。\x01",
            "因为是纪念庆典，就请\x01",
            "所有矿工喝酒。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xD,
        (
            "拜其所赐，罗基那家伙\x01",
            "直到现在还睡在\x01",
            "红砖亭呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xD,
        (
            "……嗯，反正昨天挺开心的，\x01",
            "就算了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4051")

    label("loc_3F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3F55")
    Jump("loc_4051")

    label("loc_3F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3F63")
    Jump("loc_4051")

    label("loc_3F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_3F71")
    Jump("loc_4051")

    label("loc_3F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4048")

    #C0185
    ChrTalk(
        0xE,
        "呼～今天的工作也终于结束了啊。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        (
            "喂，等下去『红砖亭』\x01",
            "喝酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "喂喂，镇长不是说了吗？\x01",
            "要我们早点回家……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xD,
        (
            "别扫兴嘛。\x01",
            "离深夜还早呢，\x01",
            "有什么关系嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xE,
        (
            "……真没办法啊。\x01",
            "我就陪你去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4051")

    label("loc_4048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4051")

    label("loc_4051")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_3DCF end

    def Function_20_4060(): pass

    label("Function_20_4060")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_419A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4128")

    #C0190
    ChrTalk(
        0xFE,
        (
            "最近人手不足，\x01",
            "我们开工都比平时早。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "指标可不等人啊。\x01",
            "冈兹不在的时候，\x01",
            "他的工作就要由大家来分担。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "嘿嘿……等冈兹那家伙回来以后，\x01",
            "可要让他好好报答我们才是。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4195")

    label("loc_4128")


    #C0193
    ChrTalk(
        0xFE,
        (
            "指标可不等人啊。\x01",
            "冈兹不在的时候，\x01",
            "他的工作就要由大家来分担。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "好啦……我差不多也\x01",
            "必须要回去干活了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4195")

    Jump("loc_460A")

    label("loc_419A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_433A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4290")

    #C0195
    ChrTalk(
        0xFE,
        (
            "听说你们昨天找到\x01",
            "冈兹那家伙了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "……那家伙从以前开始\x01",
            "就一直嫌矿工的工作太累，\x01",
            "经常发牢骚。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "为了发泄压力，\x01",
            "才会染上玩牌的嗜好，\x01",
            "但没想到竟然会失踪啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "给你们添麻烦了，真抱歉。\x01",
            "我代替他\x01",
            "向你们道歉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4335")

    label("loc_4290")


    #C0199
    ChrTalk(
        0xFE,
        (
            "矿工这个工作是辛苦的体力活，\x01",
            "薪水也没多少。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "我想，心怀不满\x01",
            "的人应该有不少吧，\x01",
            "可大家都不会说出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "冈兹这次的事情，\x01",
            "我觉得也是因为\x01",
            "积累的压力爆发了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4335")

    Jump("loc_460A")

    label("loc_433A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_43B6")

    #C0202
    ChrTalk(
        0xFE,
        (
            "冈兹是我从小玩到大的伙伴，\x01",
            "从以前开始就经常在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "所以，没有他在的时候，\x01",
            "就总觉得少了点什么似的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_460A")

    label("loc_43B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_43C4")
    Jump("loc_460A")

    label("loc_43C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4409")

    #C0204
    ChrTalk(
        0xFE,
        (
            "…………………………\x01",
            "那家伙，到底跑到哪里去了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_460A")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_44DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446E")

    #C0205
    ChrTalk(
        0xFE,
        "……呼……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "虽说是纪念庆典，\x01",
            "但对我们来说，\x01",
            "日子还是一如往常……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_44DA")

    label("loc_446E")


    #C0207
    ChrTalk(
        0xFE,
        (
            "嗯……我可不是在偷懒哦。\x01",
            "别把我跟罗基那家伙混为一谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "我是得到了矿山长的许可，\x01",
            "才过来休息一下的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44DA")

    Jump("loc_460A")

    label("loc_44DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_44ED")
    Jump("loc_460A")

    label("loc_44ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_44FB")
    Jump("loc_460A")

    label("loc_44FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4584")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4516")
    Call(0, 19)
    Jump("loc_457F")

    label("loc_4516")


    #C0209
    ChrTalk(
        0xFE,
        (
            "昨晚可真开心啊。\x01",
            "镇长请我们所有矿工\x01",
            "喝了酒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "托他的福，这下可养足精神了。\x01",
            "……好，去干活吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_457F")

    Jump("loc_460A")

    label("loc_4584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4592")
    Jump("loc_460A")

    label("loc_4592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45A0")
    Jump("loc_460A")

    label("loc_45A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_45AE")
    Jump("loc_460A")

    label("loc_45AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4601")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45C9")
    Call(0, 19)
    Jump("loc_45FC")

    label("loc_45C9")


    #C0211
    ChrTalk(
        0xFE,
        (
            "嗯，这也是人际交往嘛。\x01",
            "一点点的话也没关系吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45FC")

    Jump("loc_460A")

    label("loc_4601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_460A")

    label("loc_460A")

    TalkEnd(0xFE)
    Return()

    # Function_20_4060 end

    def Function_21_460E(): pass

    label("Function_21_460E")

    TalkBegin(0xFE)

    #C0212
    ChrTalk(
        0xFE,
        "这两周都没开过宴会呢。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "因为有同伴失踪，\x01",
            "开宴会太不妥当了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_460E end

    def Function_22_465C(): pass

    label("Function_22_465C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4671")
    Call(0, 12)
    Jump("loc_46E7")

    label("loc_4671")


    #C0214
    ChrTalk(
        0xFE,
        (
            "伤、伤脑筋啊……\x01",
            "本来是打算去阿尔摩利卡村的。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "……但难得来了，还是观光一下吧。\x01",
            "这里地势高，风景似乎不错……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E7")

    TalkEnd(0xFE)
    Return()

    # Function_22_465C end

    def Function_23_46EB(): pass

    label("Function_23_46EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476D")

    #C0216
    ChrTalk(
        0xFE,
        (
            "我本来对矿山镇的情况\x01",
            "不是很熟悉……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "不过这里风景挺不错，\x01",
            "还能看到许多稀奇的东西……\x01",
            "倒是来对了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_47B6")

    label("loc_476D")


    #C0218
    ChrTalk(
        0xFE,
        (
            "话说回来，这机械……\x01",
            "到底是干什么用的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "外行人真是搞不懂啊。\x02",
    )

    CloseMessageWindow()

    label("loc_47B6")

    TalkEnd(0xFE)
    Return()

    # Function_23_46EB end

    def Function_24_47BA(): pass

    label("Function_24_47BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4848")
    OP_93(0xFE, 0x0, 0x0)

    #C0220
    ChrTalk(
        0xFE,
        "……呀……喝～！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("回声")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S（……呀……喝～……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0222
    ChrTalk(
        0xFE,
        "哈哈，听见了，听见了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_4899")

    label("loc_4848")


    #C0223
    ChrTalk(
        0xFE,
        (
            "身处群山之中时，\x01",
            "果然还是要这样喊一次才行啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "……虽然稍微有点难为情。\x02",
    )

    CloseMessageWindow()

    label("loc_4899")

    TalkEnd(0xFE)
    Return()

    # Function_24_47BA end

    def Function_25_489D(): pass

    label("Function_25_489D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49EB")
    TalkBegin(0xFF)
    SetChrName("")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4905")

    #C0226
    ChrTalk(
        0x101,
        (
            "#0000F这次似乎\x01",
            "没必要乘坐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E3")

    label("loc_4905")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493B")

    #C0227
    ChrTalk(
        0x102,
        (
            "#0100F这次似乎\x01",
            "没必要乘坐呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E3")

    label("loc_493B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496F")

    #C0228
    ChrTalk(
        0x103,
        (
            "#0200F这次似乎\x01",
            "没必要乘坐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E3")

    label("loc_496F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49AB")

    #C0229
    ChrTalk(
        0x104,
        (
            "#0300F哈哈，这次似乎\x01",
            "没必要乘坐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E3")

    label("loc_49AB")


    #C0230
    ChrTalk(
        0x109,
        (
            "#0500F嗯……似乎\x01",
            "没必要乘坐呢。\x01",
            "反正有警备队的车。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E3")

    TalkEnd(0xFF)
    Jump("loc_4AA8")

    label("loc_49EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A25")
    TalkBegin(0xFF)
    SetChrName("")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_4AA8")

    label("loc_4A25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A36")
    Call(0, 5)
    Jump("loc_4AA8")

    label("loc_4A36")

    TalkBegin(0xFF)
    SetChrName("")

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0233
    ChrTalk(
        0x101,
        (
            "#0000F今天还是不要坐巴士了吧。\x02\x03",

            "为了进行调查，\x01",
            "还是徒步走一走比较好。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_4AA8")

    Return()

    # Function_25_489D end

    def Function_26_4AA9(): pass

    label("Function_26_4AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ABB")
    Call(0, 35)
    Jump("loc_4AE2")

    label("loc_4ABB")

    TalkBegin(0xFF)
    SetChrName("")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门后传来了谈话声。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_4AE2")

    Return()

    # Function_26_4AA9 end

    def Function_27_4AE3(): pass

    label("Function_27_4AE3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B70")
    Sound(810, 0, 100, 0)

    #C0235
    ChrTalk(
        0x101,
        (
            "#0005F这里……\x01",
            "似乎是玛因兹矿山的\x01",
            "入口啊。\x02\x03",

            "#0003F……上锁了。\x01",
            "说不定是针对狼形魔兽事件\x01",
            "而采取的警戒措施啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_4BA3")

    label("loc_4B70")

    Sound(810, 0, 100, 0)

    #C0236
    ChrTalk(
        0x101,
        (
            "#0001F……上锁了，\x01",
            "还是以后再来这边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA3")

    TalkEnd(0xFF)
    Return()

    # Function_27_4AE3 end

    def Function_28_4BA7(): pass

    label("Function_28_4BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BD2")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BD2")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_4BD2")

    Return()

    # Function_28_4BA7 end

    def Function_29_4BD3(): pass

    label("Function_29_4BD3")

    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    SetMapObjFlags(0x8, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x8, 0x13)
    SetMapObjFlags(0x8, 0x1000)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetChrPos(0x13, -5500, -2000, 20700, 180)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x0)
    Return()

    # Function_29_4BD3 end

    def Function_30_4C38(): pass

    label("Function_30_4C38")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x101, 1130, -2000, 15860, 0)
    SetChrPos(0x102, -160, -2000, 13680, 0)
    SetChrPos(0x103, 940, -2000, 13950, 0)
    SetChrPos(0x104, -70, -2000, 15410, 0)
    Call(0, 29)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0x118, 0x0)
    FadeToBright(1000, 0)
    OP_68(34130, -500, 46430, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(49940, 0)
    OP_68(1670, -500, 43690, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(1190, 5500, 41450, 0)
    MoveCamera(309, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(45590, 0)
    OP_68(1190, -500, 41450, 10000)
    SetCameraDistance(72340, 10000)
    Sleep(5000)
    PlaceName2(340, 200, "c_plac17", 0x0, 0)

    def lambda_4D56():
        OP_95(0xFE, 1200, -2000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D56)

    def lambda_4D70():
        OP_95(0xFE, -100, -2000, 18700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D70)

    def lambda_4D8A():
        OP_95(0xFE, 1200, -2000, 18700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D8A)

    def lambda_4DA4():
        OP_95(0xFE, -100, -2000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4DA4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)
    OP_0D()
    Fade(1000)
    OP_68(440, 350, 19370, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0xE6, 0x0)
    OP_68(440, -850, 19370, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0237
    ChrTalk(
        0x101,
        (
            "#0000F#6P这里就是七耀石的产地……\x01",
            "『矿山镇玛因兹』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        (
            "#0205F#6P竟然建在地势这么险峻\x01",
            "的地方呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#0300F#6P怎么说～呢……\x02\x03",

            "#0300F和阿尔摩利卡村一样，\x01",
            "跟市里的反差可真大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#0103F#6P是呀……\x02\x03",

            "#0100F不过，为了开采矿石，\x01",
            "导力倒是有一定程度的普及。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x102, 0x10E, 0x1F4)

    #C0241
    ChrTalk(
        0x102,
        (
            "#0105F#12P哎呀……？\x01",
            "那边的黑色车辆是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F7D():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F7D)

    def lambda_4F8A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F8A)
    Sleep(50)

    def lambda_4F9A():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F9A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_68(-3300, -800, 21380, 2500)
    MoveCamera(310, 19, 0, 2500)
    SetCameraDistance(17800, 2500)
    BeginChrThread(0x102, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(80)
    BeginChrThread(0x101, 3, 0, 31)
    Sleep(120)
    BeginChrThread(0x103, 3, 0, 33)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(300)

    #C0242
    ChrTalk(
        0x101,
        (
            "#0005F#12P这个……\x01",
            "是运送矿石的搬运车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#0301F#2P嗯～以搬运车来说，\x01",
            "造型莫名地粗犷呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x103,
        (
            "#0203F#12P看起来，好像是帝国莱恩福尔特公司\x01",
            "制造的特殊搬运车呢。\x02\x03",

            "#0200F而且似乎是最新型。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x102,
        (
            "#0105F#6P如果是最新型的话……\x01",
            "价格应该相当昂贵。\x02\x03",

            "#0100F会是镇长先生他们\x01",
            "的车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0003F#12P说不定吧。\x02\x03",

            "#0000F……不管怎么说，\x01",
            "先去拜访镇长吧。\x02\x03",

            "关于魔兽事件的受灾情况，\x01",
            "还要听听他怎么说才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -280, -2000, 19780, 0)
    ClearChrFlags(0x13, 0x8000)
    ClearMapObjFlags(0x8, 0x1000)
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x65, 1)
    OP_29(0x40, 0x1, 0x7)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_30_4C38 end

    def Function_31_51F0(): pass

    label("Function_31_51F0")


    def lambda_51F5():
        OP_95(0xFE, -1850, -2000, 22150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51F5)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_31_51F0 end

    def Function_32_5216(): pass

    label("Function_32_5216")


    def lambda_521B():
        OP_95(0xFE, -3100, -2000, 20750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_521B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_5216 end

    def Function_33_523C(): pass

    label("Function_33_523C")


    def lambda_5241():
        OP_95(0xFE, -1850, -2000, 20650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5241)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_33_523C end

    def Function_34_5262(): pass

    label("Function_34_5262")


    def lambda_5267():
        OP_95(0xFE, -3100, -2000, 22250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5267)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_34_5262 end

    def Function_35_5288(): pass

    label("Function_35_5288")

    EventBegin(0x0)
    Fade(1000)
    OP_68(12530, 1450, 68850, 0)
    MoveCamera(325, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18140, 0)
    SetChrPos(0x101, 12000, 250, 69500, 0)
    SetChrPos(0x102, 11700, 0, 67400, 0)
    SetChrPos(0x103, 13480, 0, 66130, 0)
    SetChrPos(0x104, 11700, 0, 66100, 0)
    OP_0D()

    #C0247
    ChrTalk(
        0x101,
        "#0005F#5P咦……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门后传来了谈话声。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0249
    ChrTalk(
        0x102,
        "#0105F#6P怎么了？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯……\x01",
            "好像正忙着呢。\x02\x03",

            "#0000F是在接待客人吗？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 22250, -1420, 63410, 270)

    #N0251
    NpcTalk(
        0x14,
        "青年的声音",
        (
            "咦……\x01",
            "你们找镇长有事？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(14640, 1650, 65760, 2000)
    MoveCamera(325, 14, 0, 2000)

    def lambda_543A():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_543A)

    def lambda_5447():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5447)

    def lambda_5454():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5454)
    Sleep(50)

    def lambda_5464():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5464)

    def lambda_5471():
        OP_95(0xFE, 17000, 0, 63700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5471)
    WaitChrThread(0x14, 1)
    TurnDirection(0x14, 0x101, 500)
    OP_6F(0x41)

    #C0252
    ChrTalk(
        0x101,
        (
            "#0000F#5P啊……\x01",
            "嗯，是的。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#0100F#5P请问，这里\x01",
            "是镇长先生的家吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        "嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x14,
        (
            "不过现在最好还是别进去哦，\x01",
            "因为他们好像在谈什么\x01",
            "正事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#0005F#5P正事……？\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            "嗯，警备队不是在\x01",
            "今天早上撤退了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x14,
        (
            "魔兽都还没消灭，\x01",
            "就在烦恼不知道该怎么办时，\x01",
            "市里似乎就正好有人来帮忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0259
    ChrTalk(
        0x101,
        "#0001F#5P难道是……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        "#0301F#5P游击士协会的家伙们吗？\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x14,
        (
            "那我就不知道了，\x01",
            "反正好像是在谈魔兽方面的对策。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x14,
        (
            "不知道你们找镇长有什么事，\x01",
            "总之，还是待会再去拜访比较好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xE1, 0x1F4)
    OP_68(13760, 1650, 65630, 3000)

    def lambda_56FC():
        OP_95(0xFE, 8330, 0, 61360, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_56FC)

    def lambda_5716():

        label("loc_5716")

        TurnDirection(0x101, 0x14, 500)
        Yield()
        Jump("loc_5716")

    QueueWorkItem2(0x101, 1, lambda_5716)

    def lambda_5728():

        label("loc_5728")

        TurnDirection(0x102, 0x14, 500)
        Yield()
        Jump("loc_5728")

    QueueWorkItem2(0x102, 1, lambda_5728)

    def lambda_573A():

        label("loc_573A")

        TurnDirection(0x103, 0x14, 500)
        Yield()
        Jump("loc_573A")

    QueueWorkItem2(0x103, 1, lambda_573A)

    def lambda_574C():

        label("loc_574C")

        TurnDirection(0x104, 0x14, 500)
        Yield()
        Jump("loc_574C")

    QueueWorkItem2(0x104, 1, lambda_574C)
    WaitChrThread(0x14, 1)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0263
    ChrTalk(
        0x103,
        "#0200F#6P……该怎么办呢？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#0006F#11P嗯～……\x01",
            "既然有客人，那就没办法了。\x02\x03",

            "#0001F先在镇上四处探听一遍，\x01",
            "再过来拜访吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_585C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_585C)
    Sleep(100)

    def lambda_586C():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_586C)
    Sleep(300)

    #C0265
    ChrTalk(
        0x102,
        (
            "#0106F#6P呼……\x01",
            "也只好这样了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        (
            "#0303F#6P哎呀呀……\x01",
            "事情的发展好像有点古怪啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 12000, 0, 67500, 180)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x65, 2)
    OP_29(0x40, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_35_5288 end

    def Function_36_58F4(): pass

    label("Function_36_58F4")

    SetScenarioFlags(0x0, 0)
    Call(0, 38)
    Return()

    # Function_36_58F4 end

    def Function_37_58FB(): pass

    label("Function_37_58FB")

    SetScenarioFlags(0x0, 1)
    Call(0, 38)
    Return()

    # Function_37_58FB end

    def Function_38_5902(): pass

    label("Function_38_5902")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_59AE")
    OP_68(21240, 1450, 62400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_90(0x101, 21200, -600, 62700, 270)
    OP_90(0x102, 21200, -600, 63800, 270)
    OP_90(0x104, 22200, -1300, 63800, 270)
    OP_90(0x103, 22200, -1300, 62700, 270)
    Jump("loc_5A20")

    label("loc_59AE")

    OP_68(6800, 1450, 57800, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7200, 0, 58500, 0)
    SetChrPos(0x102, 5800, 0, 58500, 0)
    SetChrPos(0x103, 7200, 0, 57100, 0)
    SetChrPos(0x104, 5800, 0, 57100, 0)

    label("loc_5A20")

    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 12000, 380, 71000, 180)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 12000, 380, 71000, 180)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, -4000, -2000, 20700, 180)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    OP_68(12000, 1450, 68500, 2300)
    OP_6F(0x1)
    Sleep(300)

    #N0267
    NpcTalk(
        0x15,
        "男性的声音",
        (
            "#2S#1P那么，镇长！\x01",
            "就请你们好好商量一下吧！\x02",
        )
    )

    CloseMessageWindow()

    #N0268
    NpcTalk(
        0x16,
        "男性的声音",
        (
            "#2S#11P我们明天\x01",
            "还会再来拜访的！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(11750, 1450, 66200, 4000)

    def lambda_5BB6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_5BB6)

    def lambda_5BC7():
        OP_95(0xFE, 12000, 0, 65000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5BC7)
    Sleep(1000)

    def lambda_5BE4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_5BE4)

    def lambda_5BF5():
        OP_95(0xFE, 12000, 0, 66800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_5BF5)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    OP_93(0x15, 0x0, 0x1F4)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    OP_6F(0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    ReplaceBGM("ed7121", "ed7302")

    #C0269
    ChrTalk(
        0x15,
        (
            "#6P呵呵……\x01",
            "就差最后一把劲了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x16,
        (
            "#11P嗯，看样子，这下总算\x01",
            "能立下功劳，拿到奖赏了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 39)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 40)
    Sleep(2000)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E2A")
    OP_68(20240, 1450, 62400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(21240, 1450, 62400, 3000)
    OP_90(0x101, 21200, -600, 62700, 270)
    OP_90(0x102, 21200, -600, 63800, 270)
    OP_90(0x104, 22200, -1300, 63800, 270)
    OP_90(0x103, 22200, -1300, 62700, 270)
    OP_6F(0x1)
    Sleep(1500)
    OP_68(17240, 1450, 62400, 4000)

    def lambda_5D63():
        OP_97(0xFE, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D63)
    Sleep(200)

    def lambda_5D80():
        OP_97(0xFE, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D80)
    Sleep(250)

    def lambda_5D9D():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D9D)
    Sleep(200)

    def lambda_5DBA():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5DBA)
    WaitChrThread(0x101, 1)

    def lambda_5DD8():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5DD8)
    WaitChrThread(0x102, 1)

    def lambda_5DE9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5DE9)
    WaitChrThread(0x103, 1)

    def lambda_5DFA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5DFA)
    WaitChrThread(0x104, 1)

    def lambda_5E0B():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5E0B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Jump("loc_5F52")

    label("loc_5E2A")

    OP_68(6070, 1450, 54600, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -1800, 250, 53800, 90)
    SetChrPos(0x102, -3200, 250, 53800, 90)
    SetChrPos(0x103, -1800, 250, 54840, 90)
    SetChrPos(0x104, -3200, 250, 54840, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(7000)
    OP_68(2070, 1450, 54600, 3000)
    OP_6F(0x1)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x0)
    Sleep(1000)
    OP_68(3070, 1450, 53600, 4000)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 41)
    Sleep(150)
    BeginChrThread(0x104, 3, 0, 41)
    Sleep(3000)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    label("loc_5F52")

    OP_0D()

    #C0271
    ChrTalk(
        0x101,
        "#0001F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#0101F#11P『鲁巴彻』的手下……\x01",
            "竟然会出现在这种地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x104,
        (
            "#0301F#11P喂喂……\x01",
            "那些家伙怎么会来这里啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x103,
        (
            "#0206F#11P看来是比游击士\x01",
            "更加麻烦的对手呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#0006F#11P嗯，是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x101,
        "#0005F#11P哎……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    Fade(500)
    OP_68(-700, -550, 21400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x15, -2100, -2000, 20200, 270)
    SetChrPos(0x16, -2100, -2000, 25200, 180)

    def lambda_60C8():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_60C8)
    OP_71(0x8, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x8)
    Sleep(300)
    SetChrFlags(0x15, 0x4)

    def lambda_60FF():
        OP_95(0xFE, -3100, -1400, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_60FF)

    def lambda_6119():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6119)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x10E, 0x1F4)
    Sleep(300)
    SetChrFlags(0x16, 0x4)

    def lambda_6145():
        OP_95(0xFE, -3100, -1400, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6145)

    def lambda_615F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_615F)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    OP_0D()
    OP_71(0x8, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x8)
    OP_71(0x8, 0x3C, 0x5A, 0x0, 0x0)
    Sound(465, 0, 100, 0)
    OP_79(0x8)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_61AF():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_61AF)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x4)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearMapObjFlags(0x8, 0x1000)
    SetMapObjFlags(0x8, 0x4)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_68(610, -550, 25820, 5000)
    SetChrPos(0x101, 1070, 0, 37010, 180)
    SetChrPos(0x102, -310, 0, 37020, 180)
    SetChrPos(0x103, 1050, 0, 38460, 180)
    SetChrPos(0x104, -300, 0, 38460, 180)

    def lambda_625B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_625B)
    Sleep(200)

    def lambda_6278():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6278)
    Sleep(250)

    def lambda_6295():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6295)
    Sleep(200)

    def lambda_62B2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62B2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0277
    ChrTalk(
        0x101,
        (
            "#0001F#11P那辆搬运车……\x01",
            "原来是他们的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#0106F#5P难怪拥有帝国制造的\x01",
            "最新型车辆……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#0201F#11P可是……\x02\x03",

            "黑手党的人到矿山镇来，\x01",
            "到底有什么事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#0306F#11P是啊……印象中，\x01",
            "他们似乎不太到市外活动。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0281
    ChrTalk(
        0x101,
        (
            "#0003F#11P……总之，先听听\x01",
            "镇长怎么说吧。\x02\x03",

            "#0001F说不定还能顺便了解到\x01",
            "黑手党来此的目的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetChrPos(0x0, 310, -2000, 26720, 180)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x1, 0x1)
    SetMapObjFlags(0x4, 0x10)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0x65, 3)
    OP_29(0x40, 0x1, 0x9)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_38_5902 end

    def Function_39_648C(): pass

    label("Function_39_648C")

    OP_93(0x15, 0xE1, 0x1F4)

    def lambda_6498():
        OP_95(0xFE, 7000, 0, 60000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6498)
    WaitChrThread(0x15, 1)

    def lambda_64B6():
        OP_95(0xFE, 7000, 0, 40000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_64B6)
    WaitChrThread(0x15, 1)
    Return()

    # Function_39_648C end

    def Function_40_64D0(): pass

    label("Function_40_64D0")

    OP_93(0x16, 0xE1, 0x1F4)

    def lambda_64DC():
        OP_95(0xFE, 7000, 0, 61800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_64DC)
    WaitChrThread(0x16, 1)

    def lambda_64FA():
        OP_95(0xFE, 7000, 0, 41800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_64FA)
    WaitChrThread(0x16, 1)
    Return()

    # Function_40_64D0 end

    def Function_41_6514(): pass

    label("Function_41_6514")


    def lambda_6519():
        OP_97(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6519)

    def lambda_6533():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6533)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_41_6514 end

    def Function_42_654F(): pass

    label("Function_42_654F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(12030, 1250, 67730, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14310, 0)
    SetChrPos(0x101, 11820, 400, 71040, 270)
    SetChrPos(0x102, 11820, 400, 71040, 270)
    SetChrPos(0x103, 11820, 400, 71040, 270)
    SetChrPos(0x104, 11820, 400, 71040, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    OP_68(12030, 1250, 65730, 4000)
    BeginChrThread(0x101, 3, 0, 43)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 44)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 45)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 46)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x1)

    #C0282
    ChrTalk(
        0x102,
        (
            "#0101F#5P罗伊德，没问题吗？\x01",
            "这样轻易许诺……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#0306F#11P狼形魔兽似乎有两种，\x01",
            "这点已经弄清了……\x02\x03",

            "#0301F就在今明两天，光凭我们几个，\x01",
            "能消灭黑色的那种吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#0004F#6P……不，\x01",
            "我们不一定非要消灭它们。\x02\x03",

            "#0000F我们本来的任务，\x01",
            "只是将警备队调查书上的\x01",
            "那些不明了的部分查清吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    #C0285
    ChrTalk(
        0x102,
        "#0105F#5P这么一说的话……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        (
            "#0206F#11P好像在不知不觉间，就变成\x01",
            "要对付魔兽本身了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#0003F#6P所以，我有个提议……\x02\x03",

            "#0000F正像那头白狼所说，\x01",
            "如此一来，所有的线索都已经凑全了。\x02\x03",

            "要不要针对这次事件，\x01",
            "开个会讨论一下？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        (
            "#0106F#5P是啊……\x01",
            "或许有必要整理一下情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        (
            "#0300F#11P那么，都已经到傍晚了，\x01",
            "要坐巴士回克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0004F#6P不……\x01",
            "今天就住在这个镇上吧。\x02\x03",

            "#0000F在酒馆的客房里开会就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x102,
        "#0101F#5P这……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#0205F#11P罗伊德前辈，莫非……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x104,
        (
            "#0302F#11P看样子，和旧城区那次一样，\x01",
            "你已经察觉到了什么吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#0004F#6P嗯，虽然目前还\x01",
            "无法断言。\x02\x03",

            "#0000F可以的话，希望大家\x01",
            "在开会时一起验证我的推理。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        "#0100F#5P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#0204F#11P……那么，我们赶快去\x01",
            "旅店订个房间吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15310, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x65, 4)
    OP_29(0x40, 0x1, 0xA)
    OP_1B(0x0, 0x0, 0x3E)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 0)
    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_42_654F end

    def Function_43_6B43(): pass

    label("Function_43_6B43")


    def lambda_6B48():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B48)

    def lambda_6B62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B62)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6B7B():
        OP_95(0xFE, 11990, 0, 64780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B7B)
    WaitChrThread(0x101, 1)

    def lambda_6B99():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B99)
    WaitChrThread(0x101, 1)
    Return()

    # Function_43_6B43 end

    def Function_44_6BA6(): pass

    label("Function_44_6BA6")


    def lambda_6BAB():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BAB)

    def lambda_6BC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6BC5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6BDE():
        OP_95(0xFE, 10890, 0, 65950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BDE)
    WaitChrThread(0xFE, 1)

    def lambda_6BFC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BFC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_6BA6 end

    def Function_45_6C09(): pass

    label("Function_45_6C09")


    def lambda_6C0E():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C0E)

    def lambda_6C28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C28)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6C41():
        OP_95(0xFE, 12960, 0, 65970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C41)
    WaitChrThread(0xFE, 1)

    def lambda_6C5F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C5F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_6C09 end

    def Function_46_6C6C(): pass

    label("Function_46_6C6C")


    def lambda_6C71():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C71)

    def lambda_6C8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6C8B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_6CA4():
        OP_95(0xFE, 11900, 0, 66840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CA4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_6C6C end

    def Function_47_6CBE(): pass

    label("Function_47_6CBE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("chr/ch31000.itc", 0x20)
    LoadChrToIndex("chr/ch31100.itc", 0x21)
    LoadChrToIndex("apl/ch50157.itc", 0x23)
    LoadChrToIndex("apl/ch50158.itc", 0x25)
    SetChrPos(0x101, 550, -2000, 18000, 0)
    SetChrPos(0x102, -350, -2000, 17300, 0)
    SetChrPos(0x103, 1450, -2000, 16700, 0)
    SetChrPos(0x104, 550, -2000, 16000, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x17, 50, -2000, 20000, 180)
    SetChrPos(0x18, 1160, -2000, 20000, 180)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x15, 12000, 380, 71000, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 12000, 380, 71000, 180)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1A, -4940, -2000, 23820, 180)
    SetChrPos(0x1B, -3780, -2000, 23800, 180)
    SetChrPos(0x1C, -4940, -2000, 14000, 0)
    SetChrPos(0x1D, -3780, -2000, 14000, 0)
    SetChrPos(0x15, -4940, -2000, 15300, 0)
    SetChrPos(0x16, -3780, -2000, 15300, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, -7240, -2000, 22350, 180)
    OP_D3(0x13, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x10E, 0x10E, 0x0, 0x0)
    OP_79(0x9)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0x118, 0x0)
    Sound(829, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7126", 0)
    FadeToBright(1000, 0)
    OP_68(6920, 2550, 28230, 0)
    MoveCamera(318, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(36300, 0)
    OP_68(1420, 2550, 18280, 8000)
    BeginChrThread(0x15, 0, 0, 48)
    BeginChrThread(0x16, 0, 0, 49)
    BeginChrThread(0x1C, 0, 0, 50)
    BeginChrThread(0x1D, 0, 0, 51)
    OP_6F(0x1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(510, -800, 18460, 0)
    MoveCamera(317, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17880, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0xE6, 0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    #C0297
    ChrTalk(
        0x18,
        (
            "#0509F#11P──各位真的好厉害啊！\x02\x03",

            "#0502F没想到一下就看穿了事件的真相，\x01",
            "还顺势将其解决了！\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x17,
        (
            "#2004F#5P嗯……说实话，真是令人吃惊。\x02\x03",

            "#2001F不过，在事态扩大之前，\x01",
            "还是应该先通知我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0006F#6P那个，对不起。\x02\x03",

            "#0008F……因为考虑到\x01",
            "警备队的司令阁下\x01",
            "有可能将情报泄露给黑手党……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x17,
        (
            "#2006F#5P呼……\x01",
            "被你这么一说，还真是难受呢。\x02\x03",

            "#2001F不过，要是那些白狼\x01",
            "没来相救的话，你们要怎么办？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#0011F#6P这个……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        "#0306F#6P老实说，那可就真是很危险了。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        (
            "#2001F#5P在这种时候，应该和赛尔盖商量，\x01",
            "或者直接跟我说，\x01",
            "类似的方法还有很多种吧。\x02\x03",

            "的确，从克洛斯贝尔的现状来看，\x01",
            "还存在着各种复杂的难题……\x02\x03",

            "但即使如此，光凭自己\x01",
            "就想解决所有事情的话，\x01",
            "也只是狂妄自大而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#0006F#6P……是……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#0106F#6P……我们无言以对。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x17,
        (
            "#2004F#5P呵呵……算啦，\x01",
            "责备就到此为止吧。\x02\x03",

            "#2002F你们能平安无事，真是太好了。\x02\x03",

            "还有，感谢各位\x01",
            "代替我们解决了此事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        "#0000F#6P副司令……\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#0309F#6P哈哈……\x01",
            "您说得这么郑重，反倒叫人不好意思了。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x18,
        (
            "#0504F#11P呵呵……对了，副司令。\x02\x03",

            "#0500F救了罗伊德警官他们的\x01",
            "那些白狼要怎么办呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x17,
        (
            "#2003F#5P这个嘛……\x01",
            "它们似乎完全被冤枉了。\x02\x03",

            "#2000F我想，可以先放着它们不管，静观其变……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        (
            "#0204F#6P……我觉得这样做应该没问题。\x02\x03",

            "#0202F它们看起来并不会愚蠢到\x01",
            "去惹些没意义的麻烦……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x17,
        (
            "#2002F#5P呵呵，似乎是呢。\x02\x03",

            "#2006F……不过，从这层意义上来说，\x01",
            "愚蠢的反倒是人类呢。\x02\x03",

            "没想到，居然会为了进行军犬的实战测试，\x01",
            "而在各地引起骚乱……\x02\x03",

            "#2001F虽说有后盾撑腰，\x01",
            "但未免也太瞧不起我们了……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#0108F#6P……是呀。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0000F#6P可是，都引起\x01",
            "这么大的骚动了……\x02\x03",

            "他们这次终究是\x01",
            "没法再抵赖了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x17)
    OP_64(0x18)

    #C0315
    ChrTalk(
        0x101,
        "#0011F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        (
            "#0101F#6P他们果然……\x01",
            "还是有可能被保释吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x17,
        "#2003F#5P……嗯，很可能。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x18,
        (
            "#0506F#11P──我们以前\x01",
            "也曾揭发过黑手党在国境附近的\x01",
            "走私行为……\x02\x03",

            "但上层每次都会向我们施压，\x01",
            "使他们得到保释。\x02\x03",

            "#0508F不仅如此，还随便找了个名头，\x01",
            "将走私品原封不动地返还回去……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#0007F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#0206F#6P真是太不负责任了……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#0301F#6P这么一说的话，贝尔加德门\x01",
            "也发生过同样的事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        "#0108F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x17,
        (
            "#2003F#5P可是……\x01",
            "我们也不能一味消沉下去啊。\x02\x03",

            "#2001F在这种状况下，如果大家都放弃的话，\x01",
            "克洛斯贝尔也就真的没救了……\x02\x03",

            "抱着这样的想法，为了不让克洛斯贝尔彻底堕入黑暗而\x01",
            "努力做着力所能及之事的人，应该也不在少数呢。\x02\x03",

            "#2000F就像你们一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0324
    ChrTalk(
        0x101,
        (
            "#0002F#6P啊……\x02\x03",

            "#0004F──是。\x01",
            "我们正是以此为目标的。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x17,
        (
            "#2002F#5P呵呵……\x01",
            "我今后也会期待你们支援科的\x01",
            "活跃表现。\x02\x03",

            "#2004F──走吧，用我们的车\x01",
            "送你们回克洛斯贝尔市。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 500)
    Sleep(300)

    #C0326
    ChrTalk(
        0x17,
        "#2000F#5P诺艾尔，准备出发。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)
    #Sound(1479, 255, 100, 0)    #voice#Noel
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0327
    ChrTalk(
        0x18,
        "#0502F#2P是，长官！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7100", "ed7000")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x23)
    OP_D5(0x25)
    SetScenarioFlags(0x5C, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_6CBE end

    def Function_48_7AE4(): pass

    label("Function_48_7AE4")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    SetChrFlags(0xFE, 0x4)

    def lambda_7B04():
        OP_97(0xFE, 0xFFFFFA24, 0x190, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B04)
    Sleep(650)

    def lambda_7B21():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B21)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_48_7AE4 end

    def Function_49_7B36(): pass

    label("Function_49_7B36")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    SetChrFlags(0xFE, 0x4)

    def lambda_7B56():
        OP_97(0xFE, 0xFFFFFB78, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B56)
    WaitChrThread(0xFE, 1)

    def lambda_7B74():
        OP_97(0xFE, 0xFFFFFA24, 0x190, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B74)
    Sleep(650)

    def lambda_7B91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7B91)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_49_7B36 end

    def Function_50_7BA6(): pass

    label("Function_50_7BA6")

    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_7BA6 end

    def Function_51_7BBA(): pass

    label("Function_51_7BBA")

    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_7BBA end

    def Function_52_7BCE(): pass

    label("Function_52_7BCE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3840, 4950, 31680, 0)
    MoveCamera(329, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(54120, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0x118, 0x0)
    OP_68(3840, -250, 31680, 8000)
    SetChrPos(0x101, -940, -2000, 21970, 270)
    SetChrPos(0x102, 150, -2000, 22750, 270)
    SetChrPos(0x103, 890, -2000, 21090, 270)
    SetChrPos(0x104, 1790, -2000, 21770, 270)
    SetChrPos(0x109, -2690, -2000, 22000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, -1260, -2000, -800, 0)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    FadeToBright(1000, 0)
    BeginChrThread(0x1E, 1, 0, 53)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -1150, -2000, 6310)
    OP_9F(0x1, -5650, -2000, 15640)
    OP_9F(0x1, -5760, -2000, 21610)
    OP_9F(0x2, 0x13, 4000, 0x6)
    OP_0D()
    OP_6F(0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0x13, 0xB4, 0x0)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_65(0x2, 0x1)
    SetChrPos(0x13, -14260, -2000, 24500, 0)
    OP_D3(0x13, 0x0, 0x23668, 0x0, 0x0)
    OP_68(-3410, -1050, 22410, 0)
    MoveCamera(309, 13, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19530, 0)
    OP_11(0x6A, 0xA3, 0xCC, 0x0, 0xE6, 0x0)
    FadeToBright(1000, 0)
    OP_68(-1410, -1050, 22410, 3000)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    #Sound(1503, 255, 100, 0)    #voice#Noel
    Sleep(300)

    #C0328
    ChrTalk(
        0x109,
        "#0502F#5P好，到了。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0002F#12P哈哈，真是\x01",
            "一眨眼就到了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0330
    ChrTalk(
        0x101,
        (
            "#0000F#5P快点去找镇长先生\x01",
            "询问一下详情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x104,
        "#0304F#12P是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0332
    ChrTalk(
        0x102,
        (
            "#0100F#11P我记得是直走到\x01",
            "尽头的那间房子吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, -2000, 18000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0xC1, 1)
    OP_29(0x4A, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_52_7BCE end

    def Function_53_7F99(): pass

    label("Function_53_7F99")

    Sleep(1000)
    Sound(485, 0, 90, 0)
    Return()

    # Function_53_7F99 end

    def Function_54_7FA3(): pass

    label("Function_54_7FA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(10950, 850, 69530, 0)
    MoveCamera(330, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15780, 0)
    SetChrPos(0x101, 11820, 400, 71040, 270)
    SetChrPos(0x102, 11820, 400, 71040, 270)
    SetChrPos(0x103, 11820, 400, 71040, 270)
    SetChrPos(0x104, 11820, 400, 71040, 270)
    SetChrPos(0x109, 11820, 400, 71040, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x4)
    OP_68(10950, 850, 67290, 4000)
    BeginChrThread(0x101, 3, 0, 55)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 56)
    Sleep(1000)
    BeginChrThread(0x103, 3, 0, 57)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 58)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 59)
    Sleep(1000)
    OP_71(0x4, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x4)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x1)

    #C0333
    ChrTalk(
        0x101,
        (
            "#0005F#11P都已经到傍晚了吗……\x02\x03",

            "#0000F差不多也该回\x01",
            "克洛斯贝尔市了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#0103F#11P是呀……\x01",
            "最好在今天之内\x01",
            "将情报探听完。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0335
    ChrTalk(
        0x102,
        "#0100F#6P诺艾尔上士，能麻烦你再送我们一程吗？\x02",
    )

    CloseMessageWindow()

    def lambda_81D0():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81D0)
    Sleep(50)

    def lambda_81E0():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_81E0)
    Sleep(50)

    def lambda_81F0():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_81F0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0336
    ChrTalk(
        0x109,
        (
            "#0509F#11P嗯，小事一桩。\x02\x03",

            "#0502F那么，\x01",
            "我们就回车子那边吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 13210, 0, 65069, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x2, 0x1)
    SetScenarioFlags(0xC1, 3)
    EventEnd(0x5)
    Return()

    # Function_54_7FA3 end

    def Function_55_826D(): pass

    label("Function_55_826D")


    def lambda_8272():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8272)

    def lambda_828C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_828C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_82A5():
        OP_95(0xFE, 12200, 0, 64769, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82A5)
    WaitChrThread(0x101, 1)
    Return()

    # Function_55_826D end

    def Function_56_82BF(): pass

    label("Function_56_82BF")


    def lambda_82C4():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82C4)

    def lambda_82DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_82DE)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_82F7():
        OP_95(0xFE, 10890, 0, 65950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_82F7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_82BF end

    def Function_57_8311(): pass

    label("Function_57_8311")


    def lambda_8316():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8316)

    def lambda_8330():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8330)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_8349():
        OP_95(0xFE, 12960, 0, 65970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8349)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_8311 end

    def Function_58_8363(): pass

    label("Function_58_8363")


    def lambda_8368():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8368)

    def lambda_8382():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8382)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_839B():
        OP_95(0xFE, 12550, 0, 67610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_839B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_8363 end

    def Function_59_83B5(): pass

    label("Function_59_83B5")


    def lambda_83BA():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83BA)

    def lambda_83D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_83D4)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_83ED():
        OP_95(0xFE, 11220, 0, 67760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_83ED)
    WaitChrThread(0xFE, 1)

    def lambda_840B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_840B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_59_83B5 end

    def Function_60_8418(): pass

    label("Function_60_8418")

    EventBegin(0x1)
    Sound(1499, 255, 100, 0)    #voice#Noel

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要乘坐警备队的车辆移动吗？\x02",
        )
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84A5")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A0")
    Call(0, 61)
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_84A0")

    Jump("loc_84B2")

    label("loc_84A5")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_84B2")

    EventEnd(0x5)
    Return()

    # Function_60_8418 end

    def Function_61_84B5(): pass

    label("Function_61_84B5")

    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(470, 0, 70, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(-290, -2150, 10870, 0)
    MoveCamera(341, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20940, 0)
    OP_68(-290, 750, 10870, 4000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    SetMapObjFlags(0x9, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x9, 0x13)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetChrPos(0x13, 180, -2000, 16790, 180)
    OP_D3(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sound(486, 0, 100, 0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)

    def lambda_85CA():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_85CA)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x13, 0x1)
    OP_6F(0x1)
    Return()

    # Function_61_84B5 end

    def Function_62_85F0(): pass

    label("Function_62_85F0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8656")

    #C0338
    ChrTalk(
        0x101,
        (
            "#0003F天都快黑了，\x01",
            "还是不要去郊外了吧。\x02\x03",

            "#0001F还得在酒馆\x01",
            "对推理进行验证才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86B1")

    #C0339
    ChrTalk(
        0x101,
        (
            "#0000F这边是郊外方向啊。\x02\x03",

            "#0003F回去之前，还是先听听\x01",
            "镇长先生怎么说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_870E")

    #C0340
    ChrTalk(
        0x101,
        (
            "#0000F这边是郊外方向啊。\x02\x03",

            "#0004F机会难得，\x01",
            "还是让诺艾尔上士送我们一程吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_870E")

    Sleep(50)
    SetChrPos(0x0, 650, -2000, -4920, 0)
    EventEnd(0x4)
    Return()

    # Function_62_85F0 end

    SaveToFile()

Try(main)
