from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アミー",                 # 1
        "カルロス",               # 2
        "アレク",                 # 3
        "鉱員ロージー",           # 4
        "鉱山長ホフマン",         # 5
        "鉱員ガンツ",             # 6
        "鉱員マルロ",             # 7
        "鉱員マックス",           # 8
        "観光客",                 # 9
        "観光客ルナリィ",         # 10
        "観光客コビー",           # 11
        "車",                     # 12
        "鉱員マルロ",             # 13
        "マフィア",               # 14
        "マフィア",               # 15
        "ソーニャ副司令",         # 16
        "ノエル曹長",             # 17
        "バス",                   # 18
        "警備隊員",               # 19
        "警備隊員",               # 20
        "警備隊員",               # 21
        "警備隊員",               # 22
        "SE制御",                 # 23
        "マインツ山道",           # 24
        "マインツ鉱山",           # 25
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

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "マインツ鉱山")
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
        "Function_6_D85",          # 06, 6
        "Function_7_F08",          # 07, 7
        "Function_8_F9D",          # 08, 8
        "Function_9_154F",         # 09, 9
        "Function_10_163E",        # 0A, 10
        "Function_11_164C",        # 0B, 11
        "Function_12_22EE",        # 0C, 12
        "Function_13_23F2",        # 0D, 13
        "Function_14_3014",        # 0E, 14
        "Function_15_3BA5",        # 0F, 15
        "Function_16_4218",        # 10, 16
        "Function_17_42E4",        # 11, 17
        "Function_18_44CA",        # 12, 18
        "Function_19_4674",        # 13, 19
        "Function_20_495F",        # 14, 20
        "Function_21_5007",        # 15, 21
        "Function_22_5073",        # 16, 22
        "Function_23_510E",        # 17, 23
        "Function_24_51F7",        # 18, 24
        "Function_25_52F8",        # 19, 25
        "Function_26_5554",        # 1A, 26
        "Function_27_5598",        # 1B, 27
        "Function_28_5688",        # 1C, 28
        "Function_29_56B4",        # 1D, 29
        "Function_30_5719",        # 1E, 30
        "Function_31_5D27",        # 1F, 31
        "Function_32_5D4D",        # 20, 32
        "Function_33_5D73",        # 21, 33
        "Function_34_5D99",        # 22, 34
        "Function_35_5DBF",        # 23, 35
        "Function_36_64BB",        # 24, 36
        "Function_37_64C2",        # 25, 37
        "Function_38_64C9",        # 26, 38
        "Function_39_70C1",        # 27, 39
        "Function_40_7105",        # 28, 40
        "Function_41_7149",        # 29, 41
        "Function_42_7184",        # 2A, 42
        "Function_43_781C",        # 2B, 43
        "Function_44_787F",        # 2C, 44
        "Function_45_78E2",        # 2D, 45
        "Function_46_7945",        # 2E, 46
        "Function_47_7997",        # 2F, 47
        "Function_48_8919",        # 30, 48
        "Function_49_896B",        # 31, 49
        "Function_50_89DB",        # 32, 50
        "Function_51_89EF",        # 33, 51
        "Function_52_8A03",        # 34, 52
        "Function_53_8E00",        # 35, 53
        "Function_54_8E0A",        # 36, 54
        "Function_55_90F8",        # 37, 55
        "Function_56_914A",        # 38, 56
        "Function_57_919C",        # 39, 57
        "Function_58_91EE",        # 3A, 58
        "Function_59_9240",        # 3B, 59
        "Function_60_92A3",        # 3C, 60
        "Function_61_9342",        # 3D, 61
        "Function_62_947D",        # 3E, 62
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
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市北口\x01",            # 0
            "停留所（人形工房付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5D")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_D7D")

    label("loc_D5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7D")
    Call(0, 6)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_D7D")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_CC6 end

    def Function_6_D85(): pass

    label("Function_6_D85")

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

    def lambda_E60():
        OP_95(0xFE, 450, -2000, 6620, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_E60)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x19, 1)
    Fade(1000)
    OP_68(-3860, -550, 26120, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x19, -6320, -2000, 18640, 0)

    def lambda_ECE():
        OP_95(0xFE, -6320, -2000, 21130, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_ECE)
    WaitChrThread(0x19, 1)
    OP_71(0xA, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0xA)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_6_D85 end

    def Function_7_F08(): pass

    label("Function_7_F08")

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

    # Function_7_F08 end

    def Function_8_F9D(): pass

    label("Function_8_F9D")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1547")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E4")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104D")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_1069")

    label("loc_104D")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_1069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109B")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_10B5")

    label("loc_109B")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_10B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E7")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1101")

    label("loc_10E7")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_1101")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1133")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_114D")

    label("loc_1133")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_114D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117F")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1199")

    label("loc_117F")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_1199")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C3")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_11D5")

    label("loc_11C3")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_11D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FF")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1211")

    label("loc_11FF")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1211")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123F")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1255")

    label("loc_123F")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_1255")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127F")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1291")

    label("loc_127F")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_1291")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BD")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_12D1")

    label("loc_12BD")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_12D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1303")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_131D")

    label("loc_1303")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_131D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1343")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1351")

    label("loc_1343")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_1351")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D5")
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
        (0, "loc_1428"),
        (1, "loc_1436"),
        (2, "loc_1444"),
        (3, "loc_1452"),
        (4, "loc_1460"),
        (5, "loc_146E"),
        (6, "loc_147C"),
        (7, "loc_148A"),
        (8, "loc_1498"),
        (9, "loc_14A6"),
        (10, "loc_14B4"),
        (11, "loc_14C2"),
        (SWITCH_DEFAULT, "loc_14D0"),
    )


    label("loc_1428")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_1436")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_1444")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_1452")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_1460")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_146E")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_147C")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_148A")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_1498")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_14A6")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_14B4")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_14C2")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D0")

    label("loc_14D0")

    Jump("loc_14DF")

    label("loc_14D5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14DF")

    Jump("loc_1542")

    label("loc_14E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152F")
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
    Jump("loc_1542")

    label("loc_152F")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1542")

    Jump("loc_FB7")

    label("loc_1547")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_F9D end

    def Function_9_154F(): pass

    label("Function_9_154F")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1623")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1629")

    label("loc_1623")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1629")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_154F end

    def Function_10_163E(): pass

    label("Function_10_163E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)
    Return()

    # Function_10_163E end

    def Function_11_164C(): pass

    label("Function_11_164C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16BE")

    #C0002
    ChrTalk(
        0xFE,
        (
            "町長とガンツさん、\x01",
            "昨日のうちに戻ってこなかったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "うーん、何かあったのかしら……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1731")

    #C0004
    ChrTalk(
        0xFE,
        (
            "ガンツさん、結局クロスベル市で\x01",
            "豪遊生活を送ってたんですって？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "まったく人騒がせなんだから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_1731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_17E6")

    #C0006
    ChrTalk(
        0xFE,
        (
            "カルロスさん、ガンツさんが\x01",
            "行方不明になったのを\x01",
            "結構気に病んでるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "カルロスさんに責任は\x01",
            "無いと思うんだけどねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "まったく、真面目クンなんだから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_17E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1872")

    #C0009
    ChrTalk(
        0xFE,
        "あ、そろそろ日が落ちる時間ね。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "ロージー兄さんは今日は\x01",
            "真面目に働かされてたみたいだし\x01",
            "疲れて帰ってくるんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_1872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_198C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1938")
    TurnDirection(0xFE, 0x109, 0)

    #C0011
    ChrTalk(
        0xFE,
        (
            "ふぅん……\x01",
            "なかなか凛々しくて\x01",
            "カッコイイと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "惜しむらくは女の人だってことね。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        "#0505Fへ？　えっと……？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "あぁ、気にしないでちょうだい。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1987")

    label("loc_1938")


    #C0015
    ChrTalk(
        0xFE,
        (
            "カッコイイ人がやっと来たと思ったら\x01",
            "女の人かぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "まぁ、仕方ないか。\x02",
    )

    CloseMessageWindow()

    label("loc_1987")

    Jump("loc_22EA")

    label("loc_198C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A1B")

    #C0017
    ChrTalk(
        0xFE,
        (
            "結局今年の記念祭も\x01",
            "ロクな出会いはなし……か。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "ううん、きっと来年こそは……！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "……って、去年も言ってた気がする……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_1A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFD")

    #C0020
    ChrTalk(
        0xFE,
        "はぁ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "昨日、この町に\x01",
            "かっこいい観光客が\x01",
            "来てたんだけどね……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "見晴らしのいい所を眺めたら\x01",
            "さっさとクロスベル市に\x01",
            "戻っちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……きーっくやしい！\x01",
            "なんだか馬鹿にされた気分！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B97")

    label("loc_1AFD")


    #C0024
    ChrTalk(
        0xFE,
        (
            "見晴らしのいい場所を見て\x01",
            "さっさとクロスベル市に\x01",
            "戻っちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "やっぱりまずは\x01",
            "《赤レンガ亭》の美味しいお酒で\x01",
            "酔い潰すべきだったかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B97")

    Jump("loc_22EA")

    label("loc_1B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB7")
    Call(0, 12)
    Jump("loc_1C0F")

    label("loc_1BB7")


    #C0026
    ChrTalk(
        0xFE,
        (
            "さ、さ。\x01",
            "お兄さん、遠慮しちゃだめ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "私が眺めのいいところを\x01",
            "案内してあげるわ㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C0F")

    Jump("loc_22EA")

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CB2")

    #C0028
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》の初日公演は\x01",
            "むちゃくちゃ混んでたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "それだけの人間を動かすなんて、\x01",
            "さすが大スター、イリア・プラティエね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_1CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DAA")

    #C0030
    ChrTalk(
        0xFE,
        (
            "こないだ、\x01",
            "カッコイイ男の人を探しに\x01",
            "バスでクロスベル市に行ったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "そしたらトンネルを抜けた先で\x01",
            "お人形みたいな\x01",
            "可愛い女の子を見かけたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "この辺の子じゃ無いみたいだけど……\x01",
            "あんな所で何してたのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E1F")

    label("loc_1DAA")


    #C0033
    ChrTalk(
        0xFE,
        (
            "あの辺は確か、\x01",
            "なんとかベルク工房ってのが\x01",
            "あったと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "あの子、\x01",
            "あんな所で何してたのかしらね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1F")

    Jump("loc_22EA")

    label("loc_1E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5D")

    #C0035
    ChrTalk(
        0xFE,
        (
            "はぁ……なんでこの町って\x01",
            "いい男がいないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "鉱員のお兄ちゃんは\x01",
            "サボリ魔で付き合い悪いし。\x01",
            "そもそも鉱員なんて泥臭いし……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "カルロスさんは及第点だけど、\x01",
            "なんだか優男すぎて\x01",
            "趣味じゃないのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "やっぱり、クロスベル市まで行って\x01",
            "漁る……もとい、探すしかないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FCB")

    label("loc_1F5D")


    #C0039
    ChrTalk(
        0xFE,
        (
            "いい男を探すには\x01",
            "やっぱり、クロスベル市まで\x01",
            "進出するしかないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "あとでバス使って行ってみよっと。\x02",
    )

    CloseMessageWindow()

    label("loc_1FCB")

    Jump("loc_22EA")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1FDE")
    Jump("loc_22EA")

    label("loc_1FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C0")

    #C0041
    ChrTalk(
        0xFE,
        (
            "……ぶるぶるっ。\x01",
            "冷え込んできたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "……おっと、暗くならないうちに\x01",
            "家に帰るように\x01",
            "町長から言われてるんだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "夜道で魔獣に襲われるなんて\x01",
            "御免こうむるしね。\x01",
            "さっさと帰るとしましょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2102")

    label("loc_20C0")


    #C0044
    ChrTalk(
        0xFE,
        (
            "山の夜は寒いのよねー。\x01",
            "晩御飯は、\x01",
            "シチューでも作ろうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2102")

    Jump("loc_22EA")

    label("loc_2107")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_22EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212C")
    SetScenarioFlags(0x66, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2217")

    #C0045
    ChrTalk(
        0xFE,
        (
            "（あら……\x01",
            "  結構かっこいい男が２人も！）\x02",
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
        "#0005Fあの……？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "うふ、なんでもないわお兄さん。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ここは鉱山町マインツという町よ。\x01",
            "ゆっくり滞在してって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6F, 6)
    Jump("loc_22EA")

    label("loc_2217")


    #C0049
    ChrTalk(
        0xFE,
        (
            "（こっちのジャケットのお兄さんは\x01",
            "  可愛い顔してるし、\x01",
            "  背の高いお兄さんもかっこいい㈱）\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0006F（さっきからなんなんだ……？）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0304F（ん～、女の子に見つめられるのは\x01",
            "  やっぱ悪い気はしねぇなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EA")

    TalkEnd(0xFE)
    Return()

    # Function_11_164C end

    def Function_12_22EE(): pass

    label("Function_12_22EE")

    OP_4B(0x8, 0xFF)
    OP_4B(0x10, 0xFF)
    TurnDirection(0x8, 0x10, 0)
    TurnDirection(0x10, 0x8, 0)

    #C0052
    ChrTalk(
        0x10,
        (
            "ここはアルモリカ村……\x01",
            "じゃないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x10,
        (
            "うーん、乗るバスを\x01",
            "間違えてしまったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "お兄さん、この鉱山町マインツも\x01",
            "眺めがよくていいところよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "良かったら\x01",
            "案内して差し上げましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x10,
        "え、ええっと……\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x10, 0xFF)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_12_22EE end

    def Function_13_23F2(): pass

    label("Function_13_23F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D1")

    #C0057
    ChrTalk(
        0xFE,
        (
            "昨晩は町長たちを\x01",
            "車で迎えに行くつもり\x01",
            "だったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "少し滞在するかもしれないって\x01",
            "断られてしまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "通信で聞いた町長の声、\x01",
            "なんだか元気がなさげだったのが\x01",
            "気になるな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_253B")

    label("loc_24D1")


    #C0060
    ChrTalk(
        0xFE,
        (
            "少しクロスベル市に\x01",
            "滞在するかもしれないって\x01",
            "言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "町長の元気のない声が気になるなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_253B")

    Jump("loc_3010")

    label("loc_2540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_25C3")

    #C0062
    ChrTalk(
        0xFE,
        (
            "町長ならガンツさんを迎えに\x01",
            "クロスベル市へ向かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "はぁ、とにかく\x01",
            "居場所が分かっただけでも\x01",
            "一安心だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_25C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_275D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CF")

    #C0064
    ChrTalk(
        0xFE,
        (
            "実は、あの日ガンツさんを\x01",
            "クロスベル市に送ったのは僕なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "鉱石の運搬があったから\x01",
            "そのついでにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "……だけどガンツさんは\x01",
            "約束の時間になっても\x01",
            "戻ってこなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "どうかお願いだ……\x01",
            "なんとかガンツさんを見つけ出してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2758")

    label("loc_26CF")


    #C0068
    ChrTalk(
        0xFE,
        (
            "ガンツさんをクロスベル市に\x01",
            "連れて行った僕にも\x01",
            "責任があると思うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "どうかお願いだ……\x01",
            "なんとかガンツさんを見つけ出してくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2758")

    Jump("loc_3010")

    label("loc_275D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F5")

    #C0070
    ChrTalk(
        0xFE,
        (
            "あ……キミたちは\x01",
            "町長の連絡を受けた\x01",
            "特務支援課の人達だね？\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "来てくれてありがとう。\x01",
            "町長がお待ちだ、奥の家にどうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_281B")

    label("loc_27F5")


    #C0072
    ChrTalk(
        0xFE,
        "町長がお待ちだ、奥の家にどうぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_281B")

    Jump("loc_3010")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_28F0")

    #C0073
    ChrTalk(
        0xFE,
        (
            "この町へ来るトンネルの途中に\x01",
            "分かれ道があるだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "最近、あの先にある遺跡から\x01",
            "鐘のようなおかしな音が\x01",
            "聞こえることがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "あの辺りには人気がないから\x01",
            "妙に不気味なんだよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_29A7")

    #C0076
    ChrTalk(
        0xFE,
        (
            "さて、今日は夜になったら\x01",
            "鉱員さんたちを迎えにいかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "ガンツさんは、今年こそ\x01",
            "儲けることができたかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……ま、ありえないかな。\x01",
            "ガンツさんだし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_29A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A71")

    #C0079
    ChrTalk(
        0xFE,
        (
            "記念祭を見に行く機会があったから\x01",
            "少し見てきたけど……\x01",
            "やぁ、今年はすごい人だかりだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "《アルカンシェル》の新作と\x01",
            "被った影響だって言われてるけど……\x01",
            "まさにその通りだと思ったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_2A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2B04")

    #C0081
    ChrTalk(
        0xFE,
        (
            "今日は鉱石の運搬ついでに\x01",
            "記念祭を見てくる予定なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "うーん、楽しみだな。\x01",
            "《龍老飯店》で食べてくるのも\x01",
            "いいかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_2B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B8C")

    #C0083
    ChrTalk(
        0xFE,
        (
            "若い鉱員たちが\x01",
            "記念祭で町に出てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "普段から仕事を大変そうにしてるし、\x01",
            "この機会にストレス発散してほしいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_2B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C6E")

    #C0085
    ChrTalk(
        0xFE,
        (
            "この鉱山で採れる七耀石は\x01",
            "様々な形で使われてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "細かい欠片#4Rセピス#は結晶回路の材料に、\x01",
            "大粒の結晶は宝石細工なんかに使用されるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "僕が運んだ七耀石が\x01",
            "何かの役に立っていると思うと\x01",
            "感慨深いよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_2C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2D36")

    #C0088
    ChrTalk(
        0xFE,
        (
            "僕は採掘された七耀石を\x01",
            "運搬車で運んでるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "いつ七耀石が発掘できなくなるか\x01",
            "不安でならないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "鉱山に埋まってる七耀石が\x01",
            "無限じゃないのは\x01",
            "自分でも分かってるからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3010")

    label("loc_2D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_2D44")
    Jump("loc_3010")

    label("loc_2D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_2F83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E95")

    #C0091
    ChrTalk(
        0xFE,
        (
            "山から見る夕焼けは綺麗だねぇ。\x01",
            "心が洗われるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "そういえば……ちょっと前に、\x01",
            "この空をすごく大きなものが\x01",
            "飛んでいるのを見たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "この辺の鳥や魔獣なんて\x01",
            "目じゃないほどの大きさでね。\x01",
            "あれは一体なんだったのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F（うーん、気になる話だけど……\x01",
            "  今回の事件には関係なさそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 0)
    Jump("loc_2F7E")

    label("loc_2E95")


    #C0095
    ChrTalk(
        0xFE,
        (
            "ちょっと前に、\x01",
            "この空をすごく大きなものが\x01",
            "飛んでいるのを見たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "この辺の鳥や魔獣なんて\x01",
            "目じゃないほどの大きさでね。\x01",
            "あれは一体なんだったのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "ま、夜だった上に雨も降ってたし、\x01",
            "単なる見間違いかもしれないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F7E")

    Jump("loc_3010")

    label("loc_2F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3010")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA8")
    SetScenarioFlags(0x66, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_2FA8")


    #C0098
    ChrTalk(
        0xFE,
        "村の入り口に停めてある運搬車……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "さっきの人達、\x01",
            "あんな良い車を持ってるなんて\x01",
            "何者なんだろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3010")

    TalkEnd(0xFE)
    Return()

    # Function_13_23F2 end

    def Function_14_3014(): pass

    label("Function_14_3014")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_319A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3117")

    #C0100
    ChrTalk(
        0xFE,
        (
            "鉱員さんたち、\x01",
            "ガンツさんの分の仕事も\x01",
            "手分けして進めてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "いやな顔ひとつしないで\x01",
            "みんな、もくもくと仕事してるよ。\x01",
            "面倒くさがりのロージーさんまで……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……鉱員さんって仲間想いだよね。\x01",
            "やっぱり憧れちゃうなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3195")

    label("loc_3117")


    #C0103
    ChrTalk(
        0xFE,
        (
            "お母さんは危ない仕事だから\x01",
            "やめておきなさいって言うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "僕もみんなみたいに、仲間想いの\x01",
            "立派な鉱員になりたいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3195")

    Jump("loc_3BA1")

    label("loc_319A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3317")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C6")

    #C0105
    ChrTalk(
        0xFE,
        (
            "ガンツさん、みつかったんだよね。\x01",
            "よかったぁ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "ねぇ、ガンツさん元気にしてた？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 7)), scpexpr(EXPR_END)), "loc_3271")

    #C0107
    ChrTalk(
        0x101,
        (
            "#0008F…………………………\x02\x03",

            "（言えないな、あんな薬を\x01",
            "  使ってたかもしれないなんて……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32BE")

    label("loc_3271")


    #C0108
    ChrTalk(
        0x101,
        (
            "#0000Fあぁ、安心していいと思うよ。\x01",
            "（微妙に様子はおかしかったけど……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32BE")

    SetScenarioFlags(0x0, 5)
    Jump("loc_3312")

    label("loc_32C6")


    #C0109
    ChrTalk(
        0xFE,
        (
            "ガンツさんが帰ってきたら\x01",
            "またクロスベル市のことを\x01",
            "教えてもらおうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3312")

    Jump("loc_3BA1")

    label("loc_3317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3399")

    #C0110
    ChrTalk(
        0xFE,
        (
            "ガンツさん、どこに\x01",
            "行っちゃったのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "いつもはどんなに長くても\x01",
            "３日くらいでこっちに戻ってきてたのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_3399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3415")

    #C0112
    ChrTalk(
        0xFE,
        (
            "マルロさんに聞いたら\x01",
            "ガンツさん、行方が分からなく\x01",
            "なってるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "一体どうしちゃったんだろう……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_3415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_347C")

    #C0114
    ChrTalk(
        0xFE,
        (
            "そういえば……\x01",
            "最近ガンツさん見ないなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "街の話とか色々聞いてみたかったのに。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_347C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_35E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3574")

    #C0116
    ChrTalk(
        0xFE,
        (
            "昨日、ロージーさんが\x01",
            "仕事が面白くないって言ったのを聞いて、\x01",
            "なんか色々考えちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "鉱員ってみんな、\x01",
            "イヤイヤやってるのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "仕事終わりの飲み会とか\x01",
            "カジノの話をしてる時は\x01",
            "すっごい楽しそうなのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_35DC")

    label("loc_3574")


    #C0119
    ChrTalk(
        0xFE,
        (
            "鉱員ってみんな、\x01",
            "イヤイヤやってるのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "鉱員を目指してる僕としては、\x01",
            "なんかショックかも。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35DC")

    Jump("loc_3BA1")

    label("loc_35E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_366C")

    #C0121
    ChrTalk(
        0xFE,
        (
            "僕、鉱員にあこがれてるから\x01",
            "ロージーさんに良い所を\x01",
            "聞いてみたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "ロージーさん……\x01",
            "仕事、楽しくないのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_366C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36FD")

    #C0123
    ChrTalk(
        0xFE,
        (
            "うちのお父さん、\x01",
            "鉱山長やってるんだけど\x01",
            "すごく男らしくてかっこいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "だから僕、将来は鉱員になる。\x01",
            "へへ、いいでしょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_36FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3776")

    #C0125
    ChrTalk(
        0xFE,
        (
            "昨日は珍しくお父さんも\x01",
            "宴会に行ってたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "いーなー……\x01",
            "僕も連れてってくれれば\x01",
            "よかったのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_3776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_38BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3842")

    #C0127
    ChrTalk(
        0xFE,
        (
            "昨日、その辺で走り回ってたら\x01",
            "思いっきり転んじゃってさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "体中すりむいて帰ったら、\x01",
            "お母さんに滅茶苦茶怒られちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "とほほ……\x01",
            "次からは足元を良く見ないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_38BA")

    label("loc_3842")


    #C0130
    ChrTalk(
        0xFE,
        (
            "昨日、そこのタラップに足を引っ掛けて\x01",
            "思いっきり転んじゃってさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "あれは痛かったなぁ。\x01",
            "次からは気をつけよ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BA")

    Jump("loc_3BA1")

    label("loc_38BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_39D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3956")

    #C0132
    ChrTalk(
        0xFE,
        (
            "山道の分かれ道の先に\x01",
            "変な遺跡があるの見たことある？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "ああいうの見るとワクワクするよね。\x01",
            "いつか探検してみたいな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_39D0")

    label("loc_3956")


    #C0134
    ChrTalk(
        0xFE,
        (
            "山道の分かれ道の先に\x01",
            "変な遺跡があるの見たことある？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "中はどういう風になってんだろ……\x01",
            "いつか探検してみたいな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D0")

    Jump("loc_3BA1")

    label("loc_39D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_39E3")
    Jump("loc_3BA1")

    label("loc_39E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_3A77")

    #C0136
    ChrTalk(
        0xFE,
        (
            "僕のお父さんは、\x01",
            "鉱山で一番偉い鉱山長なんだ。\x01",
            "すごいでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "今日の鉱山の仕事も\x01",
            "終わったみたいだし……\x01",
            "迎えに行こうかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_3A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9C")
    SetScenarioFlags(0x66, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_3A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B53")

    #C0138
    ChrTalk(
        0xFE,
        (
            "町の外に、閉じた坑道の\x01",
            "入り口があったでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "あれは昔の廃坑なんだってさ。\x01",
            "探検してみたいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "まぁ、近づこうとすると\x01",
            "町長さんに怒られるんだけどさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3BA1")

    label("loc_3B53")


    #C0141
    ChrTalk(
        0xFE,
        (
            "ああいう廃坑って、\x01",
            "まだ何かお宝が眠ってそうだよね。\x01",
            "探検してみたいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA1")

    TalkEnd(0xFE)
    Return()

    # Function_14_3014 end

    def Function_15_3BA5(): pass

    label("Function_15_3BA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3BB6")
    Jump("loc_4214")

    label("loc_3BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3BC4")
    Jump("loc_4214")

    label("loc_3BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_3C28")

    #C0142
    ChrTalk(
        0xFE,
        (
            "くぅ……\x01",
            "やっと仕事がおわったぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "疲れたし、さっさと家に\x01",
            "帰るとするかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4214")

    label("loc_3C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_3C36")
    Jump("loc_4214")

    label("loc_3C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3C44")
    Jump("loc_4214")

    label("loc_3C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3CD4")

    #C0144
    ChrTalk(
        0xFE,
        (
            "鉱山長の息子、\x01",
            "今日も元気無かったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        "やっぱ、俺のせいなのかね。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "はぁ、子供に愚痴るなんて\x01",
            "ダメなヤツだな俺は……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4214")

    label("loc_3CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D7B")

    #C0147
    ChrTalk(
        0xFE,
        (
            "鉱山長の息子に\x01",
            "鉱員について聞かれたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "『キツいし疲れる仕事だ』\x01",
            "なんて、身も蓋もないことを\x01",
            "つい言っちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "悪いことしたかな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4214")

    label("loc_3D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E01")

    #C0150
    ChrTalk(
        0xFE,
        (
            "はぁーだるい……\x01",
            "飲み会してから全くやる気が起きねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "……ま、いつもやる気ないけど。\x01",
            "記念祭中だし、いいよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4214")

    label("loc_3E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E0F")
    Jump("loc_4214")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EDD")

    #C0152
    ChrTalk(
        0xFE,
        (
            "鉱員の給料なんてのは\x01",
            "大したことないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "この町で暮らす分はいいけど、\x01",
            "クロスベル市の歓楽街に行きゃ\x01",
            "あっという間にすっからかんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "ったく、割に合わないっての。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3F2E")

    label("loc_3EDD")


    #C0155
    ChrTalk(
        0xFE,
        (
            "働けど、働けど、\x01",
            "我が生活は楽にならず……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "……ま、サボってんだけどな。\x02",
    )

    CloseMessageWindow()

    label("loc_3F2E")

    Jump("loc_4214")

    label("loc_3F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_400E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FB3")

    #C0157
    ChrTalk(
        0xFE,
        "ん……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "……サボってんだよ、悪い？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "ちょっとだけだから\x01",
            "他の鉱員にバラさないでくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4009")

    label("loc_3FB3")


    #C0160
    ChrTalk(
        0xFE,
        (
            "ちょっと疲れたから\x01",
            "サボってたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……他の鉱員に\x01",
            "バラさないでくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4009")

    Jump("loc_4214")

    label("loc_400E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_401C")
    Jump("loc_4214")

    label("loc_401C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_40E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4037")
    Call(0, 16)
    Jump("loc_40E2")

    label("loc_4037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B7")

    #C0162
    ChrTalk(
        0xFE,
        (
            "ふぁ～あ……\x01",
            "俺はさっさと帰るとするかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "（適当にサボってたおかげで\x01",
            "  そんなに疲れてないしな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_40E2")

    label("loc_40B7")


    #C0164
    ChrTalk(
        0xFE,
        (
            "ふぁ～あ……\x01",
            "さっさと帰って寝るかぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40E2")

    Jump("loc_4214")

    label("loc_40E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4214")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410C")
    SetScenarioFlags(0x66, 3)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)

    label("loc_410C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41CE")

    #C0165
    ChrTalk(
        0xFE,
        (
            "ここに住んでる鉱員が\x01",
            "こないだ魔獣に襲われてよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "ケガ自体は\x01",
            "大したことなかったんだが\x01",
            "大事をとって休養だとさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "……はぁ、俺も休みてぇ～。\x01",
            "ていうかサボりてぇ～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4214")

    label("loc_41CE")


    #C0168
    ChrTalk(
        0xFE,
        (
            "あのくらいの怪我で\x01",
            "休めるなんていいよなぁ。\x01",
            "俺もサボリてぇ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4214")

    TalkEnd(0xFE)
    Return()

    # Function_15_3BA5 end

    def Function_16_4218(): pass

    label("Function_16_4218")


    #C0169
    ChrTalk(
        0xFE,
        (
            "（……実は鉱山の中で\x01",
            "  サボって本を読んでたんだ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "（お前ら、鉱山長にバレる前に\x01",
            "  この本、もらってくんない？）\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2C8, 1)
    SetScenarioFlags(0x9C, 2)
    Return()

    # Function_16_4218 end

    def Function_17_42E4(): pass

    label("Function_17_42E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_42F5")
    Jump("loc_44C6")

    label("loc_42F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4303")
    Jump("loc_44C6")

    label("loc_4303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_43A7")

    #C0172
    ChrTalk(
        0xFE,
        "今日の分もようやく終わったか。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "ガンツのヤツがいねぇと\x01",
            "やっぱり効率が悪いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "あいつは良くも悪くも\x01",
            "ムードメーカーなところがあるからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44C6")

    label("loc_43A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_43B5")
    Jump("loc_44C6")

    label("loc_43B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_43C3")
    Jump("loc_44C6")

    label("loc_43C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_43D1")
    Jump("loc_44C6")

    label("loc_43D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_43DF")
    Jump("loc_44C6")

    label("loc_43DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_43ED")
    Jump("loc_44C6")

    label("loc_43ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_43FB")
    Jump("loc_44C6")

    label("loc_43FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4409")
    Jump("loc_44C6")

    label("loc_4409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4417")
    Jump("loc_44C6")

    label("loc_4417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4425")
    Jump("loc_44C6")

    label("loc_4425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_44BD")
    OP_93(0xFE, 0x5A, 0x0)

    #C0175
    ChrTalk(
        0xFE,
        (
            "お前ら、飲みにいくのは構わんが\x01",
            "出来るだけ早く帰れよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "マックスの奴が戻るまで、\x01",
            "これから一人でも欠けるのは\x01",
            "許さんからな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44C6")

    label("loc_44BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_44C6")

    label("loc_44C6")

    TalkEnd(0xFE)
    Return()

    # Function_17_42E4 end

    def Function_18_44CA(): pass

    label("Function_18_44CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_44DB")
    Jump("loc_4670")

    label("loc_44DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_44E9")
    Jump("loc_4670")

    label("loc_44E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_44F7")
    Jump("loc_4670")

    label("loc_44F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4505")
    Jump("loc_4670")

    label("loc_4505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4513")
    Jump("loc_4670")

    label("loc_4513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4521")
    Jump("loc_4670")

    label("loc_4521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_452F")
    Jump("loc_4670")

    label("loc_452F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_453D")
    Jump("loc_4670")

    label("loc_453D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4558")
    Call(0, 19)
    Jump("loc_45C8")

    label("loc_4558")


    #C0177
    ChrTalk(
        0xFE,
        (
            "う～……まだ頭がいてぇ。\x01",
            "完全に二日酔いだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "チッ、完全に潰れてるロージーが\x01",
            "うらやましいくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45C8")

    Jump("loc_4670")

    label("loc_45CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_45DB")
    Jump("loc_4670")

    label("loc_45DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45E9")
    Jump("loc_4670")

    label("loc_45E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_45F7")
    Jump("loc_4670")

    label("loc_45F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4667")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4612")
    Call(0, 19)
    Jump("loc_4662")

    label("loc_4612")


    #C0179
    ChrTalk(
        0xFE,
        (
            "朝から晩まで薄暗い穴倉で\x01",
            "働いてやってんだ。\x01",
            "これくらいのご褒美がねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4662")

    Jump("loc_4670")

    label("loc_4667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4670")

    label("loc_4670")

    TalkEnd(0xFE)
    Return()

    # Function_18_44CA end

    def Function_19_4674(): pass

    label("Function_19_4674")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xD, 0xE, 0)
    TurnDirection(0xE, 0xD, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4698")
    Jump("loc_4950")

    label("loc_4698")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_46A6")
    Jump("loc_4950")

    label("loc_46A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_46B4")
    Jump("loc_4950")

    label("loc_46B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_46C2")
    Jump("loc_4950")

    label("loc_46C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_46D0")
    Jump("loc_4950")

    label("loc_46D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_46DE")
    Jump("loc_4950")

    label("loc_46DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_46EC")
    Jump("loc_4950")

    label("loc_46EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_46FA")
    Jump("loc_4950")

    label("loc_46FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4812")

    #C0180
    ChrTalk(
        0xD,
        (
            "う～……\x01",
            "頭がまだガンガンするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        "どう考えても飲みすぎだな。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xE,
        (
            "……でも町長もいい人だよな。\x01",
            "記念祭だからって鉱員全員に\x01",
            "酒を振舞うなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xD,
        (
            "お陰でロージーのヤツは\x01",
            "いまだに赤レンガ亭で\x01",
            "寝てやがるけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xD,
        (
            "……ま、昨日は楽しかったし\x01",
            "よしとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4950")

    label("loc_4812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4820")
    Jump("loc_4950")

    label("loc_4820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_482E")
    Jump("loc_4950")

    label("loc_482E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_483C")
    Jump("loc_4950")

    label("loc_483C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4947")

    #C0185
    ChrTalk(
        0xE,
        "ふー、今日の仕事も終わりだな。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xD,
        (
            "おい、この後《赤レンガ亭》で\x01",
            "飲んでいこうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "おいおい、町長に言われたろ？\x01",
            "早く家に帰れって……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xD,
        (
            "つれないこというなって。\x01",
            "夜更けにゃまだ早いし、\x01",
            "いいじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xE,
        (
            "……仕方ねぇな。\x01",
            "付き合ってやるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4950")

    label("loc_4947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4950")

    label("loc_4950")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_19_4674 end

    def Function_20_495F(): pass

    label("Function_20_495F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A5B")

    #C0190
    ChrTalk(
        0xFE,
        (
            "最近は人数が足りないから\x01",
            "いつもより早くから仕事を始めてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "ノルマは待っちゃくれない。\x01",
            "ガンツがいない間は\x01",
            "皆でその穴を埋めるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "へへ……ガンツのヤツが帰ってきたら\x01",
            "せいぜい借りを返してもらわなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4AD8")

    label("loc_4A5B")


    #C0193
    ChrTalk(
        0xFE,
        (
            "ノルマは待っちゃくれない。\x01",
            "ガンツがいない間は\x01",
            "皆でその穴を埋めるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "さぁて……俺もそろそろ\x01",
            "仕事に戻らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AD8")

    Jump("loc_5003")

    label("loc_4ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C17")

    #C0195
    ChrTalk(
        0xFE,
        (
            "昨日はガンツのやつを\x01",
            "見つけてくれたそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "……あいつは昔から\x01",
            "鉱員の仕事をキツく思ってて\x01",
            "よく愚痴ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "ストレスのはけ口として\x01",
            "ギャンブルに手を出してたみたいだが\x01",
            "まさか行方不明にまでなるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "面倒かけて悪かったな。\x01",
            "あいつの代わりに\x01",
            "俺が謝らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4CE6")

    label("loc_4C17")


    #C0199
    ChrTalk(
        0xFE,
        (
            "鉱員の仕事は体力的にキツいし、\x01",
            "給料も大したこと無い。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "不満を持ってるやつは\x01",
            "結構いると思うけど、\x01",
            "皆は口に出さないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "今回のガンツの件も、\x01",
            "溜まってたストレスが\x01",
            "爆発したせいだと俺は思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE6")

    Jump("loc_5003")

    label("loc_4CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_4D6D")

    #C0202
    ChrTalk(
        0xFE,
        (
            "ガンツと俺は幼馴染でね、\x01",
            "昔からよくつるんでたもんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "だからあいつがいないと、\x01",
            "どうも調子が狂っちまうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5003")

    label("loc_4D6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4D7B")
    Jump("loc_5003")

    label("loc_4D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4DC6")

    #C0204
    ChrTalk(
        0xFE,
        (
            "…………………………\x01",
            "あいつ、どこ行っちまったのかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5003")

    label("loc_4DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4EC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E39")

    #C0205
    ChrTalk(
        0xFE,
        "……ふぅ……\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "記念祭って言っても\x01",
            "俺たちにとっちゃは何事もなく\x01",
            "過ぎていくな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4EBB")

    label("loc_4E39")


    #C0207
    ChrTalk(
        0xFE,
        (
            "ん……別にサボってるわけじゃないぞ。\x01",
            "ロージーの奴と一緒にしないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "ちゃんと鉱山長に許可を貰って\x01",
            "一服しにきたのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EBB")

    Jump("loc_5003")

    label("loc_4EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4ECE")
    Jump("loc_5003")

    label("loc_4ECE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4EDC")
    Jump("loc_5003")

    label("loc_4EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4F77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF7")
    Call(0, 19)
    Jump("loc_4F72")

    label("loc_4EF7")


    #C0209
    ChrTalk(
        0xFE,
        (
            "昨晩は楽しかったよ。\x01",
            "町長が鉱員全員に\x01",
            "酒を振る舞ってくれてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "お陰で英気が養えた。\x01",
            "……さ、仕事に行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F72")

    Jump("loc_5003")

    label("loc_4F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F85")
    Jump("loc_5003")

    label("loc_4F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4F93")
    Jump("loc_5003")

    label("loc_4F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_4FA1")
    Jump("loc_5003")

    label("loc_4FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_4FFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FBC")
    Call(0, 19)
    Jump("loc_4FF5")

    label("loc_4FBC")


    #C0211
    ChrTalk(
        0xFE,
        (
            "ま、これも付き合いだ。\x01",
            "ちょっとくらいならいいだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF5")

    Jump("loc_5003")

    label("loc_4FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5003")

    label("loc_5003")

    TalkEnd(0xFE)
    Return()

    # Function_20_495F end

    def Function_21_5007(): pass

    label("Function_21_5007")

    TalkBegin(0xFE)

    #C0212
    ChrTalk(
        0xFE,
        "ここ２週間は宴会もやってねぇんだ。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "仲間が行方不明だってのに\x01",
            "宴会ってのも不謹慎だからな……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_5007 end

    def Function_22_5073(): pass

    label("Function_22_5073")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5088")
    Call(0, 12)
    Jump("loc_510A")

    label("loc_5088")


    #C0214
    ChrTalk(
        0xFE,
        (
            "ま、参ったな……\x01",
            "アルモリカ村に行くつもりだったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "……折角だから観光していくかな。\x01",
            "高所だから眺めはよさそうだし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_510A")

    TalkEnd(0xFE)
    Return()

    # Function_22_5073 end

    def Function_23_510E(): pass

    label("Function_23_510E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A0")

    #C0216
    ChrTalk(
        0xFE,
        (
            "鉱山の町ってあまりなじみが\x01",
            "なかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "なかなか景色もいいし、\x01",
            "珍しいものも結構見かけるし……\x01",
            "来てよかったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_51F3")

    label("loc_51A0")


    #C0218
    ChrTalk(
        0xFE,
        (
            "それにしてもこの機械……\x01",
            "一体何に使うんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        "シロートには分かんないわ。\x02",
    )

    CloseMessageWindow()

    label("loc_51F3")

    TalkEnd(0xFE)
    Return()

    # Function_23_510E end

    def Function_24_51F7(): pass

    label("Function_24_51F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529B")
    OP_93(0xFE, 0x0, 0x0)

    #C0220
    ChrTalk(
        0xFE,
        "──やっ、ほぉー！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("こだまする声")

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2S（……やっ……ほー……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0222
    ChrTalk(
        0xFE,
        "はは、聞こえてきた聞こえてきた。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_52F4")

    label("loc_529B")


    #C0223
    ChrTalk(
        0xFE,
        (
            "やはり山を登ったら、\x01",
            "一度はこれをやらないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "……ちょっと恥ずかしいけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_52F4")

    TalkEnd(0xFE)
    Return()

    # Function_24_51F7 end

    def Function_25_52F8(): pass

    label("Function_25_52F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5482")
    TalkBegin(0xFF)
    SetChrName("")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_536A")

    #C0226
    ChrTalk(
        0x101,
        (
            "#0000F今回は使う必要は\x01",
            "なさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547A")

    label("loc_536A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53A6")

    #C0227
    ChrTalk(
        0x102,
        (
            "#0100F今回は使う必要は\x01",
            "なさそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547A")

    label("loc_53A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E6")

    #C0228
    ChrTalk(
        0x103,
        (
            "#0200F今回は使う必要は\x01",
            "なさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547A")

    label("loc_53E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542A")

    #C0229
    ChrTalk(
        0x104,
        (
            "#0300Fハハ、今回は使う必要は\x01",
            "なさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547A")

    label("loc_542A")


    #C0230
    ChrTalk(
        0x109,
        (
            "#0500Fええと……使う必要は\x01",
            "なさそうですね。\x01",
            "警備隊の車両があるわけですし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_547A")

    TalkEnd(0xFF)
    Jump("loc_5553")

    label("loc_5482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54BE")
    TalkBegin(0xFF)
    SetChrName("")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_5553")

    label("loc_54BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_54CF")
    Call(0, 5)
    Jump("loc_5553")

    label("loc_54CF")

    TalkBegin(0xFF)
    SetChrName("")

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0233
    ChrTalk(
        0x101,
        (
            "#0000F今日はバスは使わないでおこう。\x02\x03",

            "調査の為には、街道も\x01",
            "足で歩いた方が良さそうだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_5553")

    Return()

    # Function_25_52F8 end

    def Function_26_5554(): pass

    label("Function_26_5554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5566")
    Call(0, 35)
    Jump("loc_5597")

    label("loc_5566")

    TalkBegin(0xFF)
    SetChrName("")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉の中から話し声が聞こえる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_5597")

    Return()

    # Function_26_5554 end

    def Function_27_5598(): pass

    label("Function_27_5598")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_563B")
    Sound(810, 0, 100, 0)

    #C0235
    ChrTalk(
        0x101,
        (
            "#0005Fここは……\x01",
            "マインツ鉱山の\x01",
            "入り口みたいだな。\x02\x03",

            "#0003F……鍵がかかってる。\x01",
            "狼魔獣事件があったから\x01",
            "警戒してるのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5684")

    label("loc_563B")

    Sound(810, 0, 100, 0)

    #C0236
    ChrTalk(
        0x101,
        (
            "#0001F……鍵がかかってる。\x01",
            "ここは後回しにした方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5684")

    TalkEnd(0xFF)
    Return()

    # Function_27_5598 end

    def Function_28_5688(): pass

    label("Function_28_5688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56B3")
    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B3")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_56B3")

    Return()

    # Function_28_5688 end

    def Function_29_56B4(): pass

    label("Function_29_56B4")

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

    # Function_29_56B4 end

    def Function_30_5719(): pass

    label("Function_30_5719")

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

    def lambda_5837():
        OP_95(0xFE, 1200, -2000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5837)

    def lambda_5851():
        OP_95(0xFE, -100, -2000, 18700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5851)

    def lambda_586B():
        OP_95(0xFE, 1200, -2000, 18700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_586B)

    def lambda_5885():
        OP_95(0xFE, -100, -2000, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5885)
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
            "#0000F#6Pここが七耀石の産地……\x01",
            "《鉱山町マインツ》か。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x103,
        (
            "#0205F#6Pずいぶん険しい場所に\x01",
            "あるんですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        (
            "#0300F#6Pなんつーか……\x02\x03",

            "#0300Fアルモリカ村もそうだったが\x01",
            "街とのギャップが凄ぇよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#0103F#6Pそうね……\x02\x03",

            "#0100F採掘のための導力化は\x01",
            "一応されているみたいだけど。\x02",
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
            "#0105F#12Pあら……？\x01",
            "そちらの黒い車は……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A70():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A70)

    def lambda_5A7D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A7D)
    Sleep(50)

    def lambda_5A8D():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A8D)
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
            "#0005F#12Pこれは……\x01",
            "鉱石を運ぶ運搬車なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#0301F#2Pんー、それにしちゃあ、\x01",
            "妙にゴツイ造りをしてねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x103,
        (
            "#0203F#12P帝国・ラインフォルト社製の\x01",
            "特殊運搬車みたいですね。\x02\x03",

            "#0200Fどうやら最新型のようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x102,
        (
            "#0105F#6P最新型ともなると……\x01",
            "相当、高価なはずだけど。\x02\x03",

            "#0100F町長さんあたりが\x01",
            "所有しているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0003F#12Pそうかもしれないな。\x02\x03",

            "#0000F……いずれにせよ、\x01",
            "まずは町長を訪ねてみよう。\x02\x03",

            "魔獣の被害状況について\x01",
            "改めて話を聞いてみないとな。\x02",
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

    # Function_30_5719 end

    def Function_31_5D27(): pass

    label("Function_31_5D27")


    def lambda_5D2C():
        OP_95(0xFE, -1850, -2000, 22150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D2C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_31_5D27 end

    def Function_32_5D4D(): pass

    label("Function_32_5D4D")


    def lambda_5D52():
        OP_95(0xFE, -3100, -2000, 20750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D52)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_32_5D4D end

    def Function_33_5D73(): pass

    label("Function_33_5D73")


    def lambda_5D78():
        OP_95(0xFE, -1850, -2000, 20650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D78)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_33_5D73 end

    def Function_34_5D99(): pass

    label("Function_34_5D99")


    def lambda_5D9E():
        OP_95(0xFE, -3100, -2000, 22250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5D9E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_34_5D99 end

    def Function_35_5DBF(): pass

    label("Function_35_5DBF")

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
        "#0005F#5Pあれ……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉の中から話し声が聞こえる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0249
    ChrTalk(
        0x102,
        "#0105F#6Pどうしたの？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x101,
        (
            "#0003F#5Pいや……\x01",
            "何だか取り込み中みたいだ。\x02\x03",

            "#0000F来客中なのかな？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 22250, -1420, 63410, 270)

    #N0251
    NpcTalk(
        0x14,
        "青年の声",
        (
            "あれ……\x01",
            "あんたたち、町長に用？\x02",
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

    def lambda_5F95():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F95)

    def lambda_5FA2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FA2)

    def lambda_5FAF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FAF)
    Sleep(50)

    def lambda_5FBF():
        OP_93(0xFE, 0x87, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FBF)

    def lambda_5FCC():
        OP_95(0xFE, 17000, 0, 63700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5FCC)
    WaitChrThread(0x14, 1)
    TurnDirection(0x14, 0x101, 500)
    OP_6F(0x41)

    #C0252
    ChrTalk(
        0x101,
        (
            "#0000F#5Pあ……\x01",
            "ええ、そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#0100F#5Pそれでは、こちらが\x01",
            "町長さんのお宅ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        "ああ、そうだけど……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x14,
        (
            "今は入らない方がいいよ。\x01",
            "なんか真面目な話をしている\x01",
            "みたいだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        "#0005F#5P真面目な話……？\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x14,
        (
            "ああ、ちょうど今朝、\x01",
            "警備隊が引き上げただろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x14,
        (
            "魔獣も退治されてないのに\x01",
            "どうしようかと困ってたところに\x01",
            "街から助っ人が来てらしくてさ。\x02",
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
        "#0001F#5Pそれってまさか……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        "#0301F#5P遊撃士の連中かよ？\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x14,
        (
            "そこまでは知らないけど\x01",
            "魔獣対策の話をしてるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x14,
        (
            "町長に何の用か知らないけど\x01",
            "後で訪ねた方がいいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xE1, 0x1F4)
    OP_68(13760, 1650, 65630, 3000)

    def lambda_62A7():
        OP_95(0xFE, 8330, 0, 61360, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_62A7)

    def lambda_62C1():

        label("loc_62C1")

        TurnDirection(0x101, 0x14, 500)
        Yield()
        Jump("loc_62C1")

    QueueWorkItem2(0x101, 1, lambda_62C1)

    def lambda_62D3():

        label("loc_62D3")

        TurnDirection(0x102, 0x14, 500)
        Yield()
        Jump("loc_62D3")

    QueueWorkItem2(0x102, 1, lambda_62D3)

    def lambda_62E5():

        label("loc_62E5")

        TurnDirection(0x103, 0x14, 500)
        Yield()
        Jump("loc_62E5")

    QueueWorkItem2(0x103, 1, lambda_62E5)

    def lambda_62F7():

        label("loc_62F7")

        TurnDirection(0x104, 0x14, 500)
        Yield()
        Jump("loc_62F7")

    QueueWorkItem2(0x104, 1, lambda_62F7)
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
        "#0200F#6P……どうしますか？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#0006F#11Pうーん……\x01",
            "取り込み中なら仕方ない。\x02\x03",

            "#0001F一通り聞き込みをしてから\x01",
            "もう一度こちらを訪ねてみよう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_641B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_641B)
    Sleep(100)

    def lambda_642B():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_642B)
    Sleep(300)

    #C0265
    ChrTalk(
        0x102,
        (
            "#0106F#6Pふう……\x01",
            "そうするしかないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x104,
        (
            "#0303F#6Pやれやれ……\x01",
            "妙な展開になりそうだな。\x02",
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

    # Function_35_5DBF end

    def Function_36_64BB(): pass

    label("Function_36_64BB")

    SetScenarioFlags(0x0, 0)
    Call(0, 38)
    Return()

    # Function_36_64BB end

    def Function_37_64C2(): pass

    label("Function_37_64C2")

    SetScenarioFlags(0x0, 1)
    Call(0, 38)
    Return()

    # Function_37_64C2 end

    def Function_38_64C9(): pass

    label("Function_38_64C9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6575")
    OP_68(21240, 1450, 62400, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_90(0x101, 21200, -600, 62700, 270)
    OP_90(0x102, 21200, -600, 63800, 270)
    OP_90(0x104, 22200, -1300, 63800, 270)
    OP_90(0x103, 22200, -1300, 62700, 270)
    Jump("loc_65E7")

    label("loc_6575")

    OP_68(6800, 1450, 57800, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 7200, 0, 58500, 0)
    SetChrPos(0x102, 5800, 0, 58500, 0)
    SetChrPos(0x103, 7200, 0, 57100, 0)
    SetChrPos(0x104, 5800, 0, 57100, 0)

    label("loc_65E7")

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
        "男の声",
        (
            "#2S#1Pそれじゃあ町長！\x01",
            "よろしくご検討くださいよ！\x02",
        )
    )

    CloseMessageWindow()

    #N0268
    NpcTalk(
        0x16,
        "男の声",
        (
            "#2S#11Pまた明日、\x01",
            "お伺いに参りますからねぇ！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_68(11750, 1450, 66200, 4000)

    def lambda_6787():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6787)

    def lambda_6798():
        OP_95(0xFE, 12000, 0, 65000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6798)
    Sleep(1000)

    def lambda_67B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_67B5)

    def lambda_67C6():
        OP_95(0xFE, 12000, 0, 66800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_67C6)
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
            "#6Pクク……\x01",
            "あと一押しってところだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x16,
        (
            "#11Pああ、これで何とか\x01",
            "ボーナスが手に入りそうだ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 39)
    Sleep(300)
    BeginChrThread(0x16, 3, 0, 40)
    Sleep(2000)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A01")
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

    def lambda_693A():
        OP_97(0xFE, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_693A)
    Sleep(200)

    def lambda_6957():
        OP_97(0xFE, 0xFFFFEA84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6957)
    Sleep(250)

    def lambda_6974():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6974)
    Sleep(200)

    def lambda_6991():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6991)
    WaitChrThread(0x101, 1)

    def lambda_69AF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_69AF)
    WaitChrThread(0x102, 1)

    def lambda_69C0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_69C0)
    WaitChrThread(0x103, 1)

    def lambda_69D1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_69D1)
    WaitChrThread(0x104, 1)

    def lambda_69E2():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_69E2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    Jump("loc_6B29")

    label("loc_6A01")

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

    label("loc_6B29")

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
            "#0101F#11P《ルバーチェ》の手下……\x01",
            "こんな場所に現れるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x104,
        (
            "#0301F#11Pおいおい……\x01",
            "何であいつらが来てんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x103,
        (
            "#0206F#11P遊撃士以上に\x01",
            "面倒そうな相手ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#0006F#11Pああ、そうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x101,
        "#0005F#11Pえ……？\x02",
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

    def lambda_6CB3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6CB3)
    OP_71(0x8, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x8)
    Sleep(300)
    SetChrFlags(0x15, 0x4)

    def lambda_6CEA():
        OP_95(0xFE, -3100, -1400, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6CEA)

    def lambda_6D04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6D04)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0x10E, 0x1F4)
    Sleep(300)
    SetChrFlags(0x16, 0x4)

    def lambda_6D30():
        OP_95(0xFE, -3100, -1400, 20200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_6D30)

    def lambda_6D4A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6D4A)
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

    def lambda_6D9A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6D9A)
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

    def lambda_6E46():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E46)
    Sleep(200)

    def lambda_6E63():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E63)
    Sleep(250)

    def lambda_6E80():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6E80)
    Sleep(200)

    def lambda_6E9D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E9D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0277
    ChrTalk(
        0x101,
        (
            "#0001F#11Pあの運搬車……\x01",
            "連中のものだったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x102,
        (
            "#0106F#5P道理で帝国製の最新車両を\x01",
            "持っているはずだわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        (
            "#0201F#11Pですが……\x02\x03",

            "マフィアが鉱山町に\x01",
            "一体、どういう用事が？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#0306F#11Pそうだな……あんまり街の外で\x01",
            "活動してるイメージじゃなかったが。\x02",
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
            "#0003F#11P……とりあえず町長から\x01",
            "話を聞かせてもらおう。\x02\x03",

            "#0001Fマフィアが何をしに来たのか\x01",
            "ついでに判るかもしれない。\x02",
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

    # Function_38_64C9 end

    def Function_39_70C1(): pass

    label("Function_39_70C1")

    OP_93(0x15, 0xE1, 0x1F4)

    def lambda_70CD():
        OP_95(0xFE, 7000, 0, 60000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_70CD)
    WaitChrThread(0x15, 1)

    def lambda_70EB():
        OP_95(0xFE, 7000, 0, 40000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_70EB)
    WaitChrThread(0x15, 1)
    Return()

    # Function_39_70C1 end

    def Function_40_7105(): pass

    label("Function_40_7105")

    OP_93(0x16, 0xE1, 0x1F4)

    def lambda_7111():
        OP_95(0xFE, 7000, 0, 61800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_7111)
    WaitChrThread(0x16, 1)

    def lambda_712F():
        OP_95(0xFE, 7000, 0, 41800, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_712F)
    WaitChrThread(0x16, 1)
    Return()

    # Function_40_7105 end

    def Function_41_7149(): pass

    label("Function_41_7149")


    def lambda_714E():
        OP_97(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_714E)

    def lambda_7168():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7168)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_41_7149 end

    def Function_42_7184(): pass

    label("Function_42_7184")

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
            "#0101F#5Pロイド、大丈夫なの？\x01",
            "あんな安請け合いをして……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x104,
        (
            "#0306F#11P狼型の魔獣が２種類、\x01",
            "いるらしい事までは判ったが……\x02\x03",

            "#0301F今日明日で、俺たちだけで\x01",
            "黒い方を退治しきれるのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#0004F#6P……いや。\x01",
            "必ずしも退治する必要はないさ。\x02\x03",

            "#0000Fそもそも俺たちの役目は、\x01",
            "警備隊の調書で不可解な箇所を\x01",
            "明らかにすることだっただろう？\x02",
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
        "#0105F#5Pそういえば……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x103,
        (
            "#0206F#11Pいつの間にか、魔獣そのものを\x01",
            "何とかする話に変わってましたね……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#0003F#6Pそこで提案なんだけど……\x02\x03",

            "#0000Fあの白い狼が伝えたように、\x01",
            "これで全ての手がかりが揃ったと思う。\x02\x03",

            "一度、今回の件について\x01",
            "ミーティングをしてみないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        (
            "#0106F#5Pそうね……\x01",
            "情報の整理は必要かも。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        (
            "#0300F#11Pそんじゃ、もう夕方だし\x01",
            "バスでクロスベル市まで戻るか？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0004F#6Pいや……\x01",
            "今日はこの町に泊まって行こう。\x02\x03",

            "#0000Fミーティングは客室ですればいい。\x02",
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
        "#0101F#5Pそれって……\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x103,
        "#0205F#11Pロイドさん、もしかして……\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x104,
        (
            "#0302F#11Pどうやら旧市街の時と同じく、\x01",
            "何か気付いたみたいだな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#0004F#6Pああ、まだ確信までには\x01",
            "至ってないけどね。\x02\x03",

            "#0000Fよかったらミーティングで\x01",
            "推理の検証に付き合って欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x102,
        "#0100F#5Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#0204F#11P……それでは早速、\x01",
            "宿で部屋を取りましょう。\x02",
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

    # Function_42_7184 end

    def Function_43_781C(): pass

    label("Function_43_781C")


    def lambda_7821():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7821)

    def lambda_783B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_783B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_7854():
        OP_95(0xFE, 11990, 0, 64780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7854)
    WaitChrThread(0x101, 1)

    def lambda_7872():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7872)
    WaitChrThread(0x101, 1)
    Return()

    # Function_43_781C end

    def Function_44_787F(): pass

    label("Function_44_787F")


    def lambda_7884():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7884)

    def lambda_789E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_789E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_78B7():
        OP_95(0xFE, 10890, 0, 65950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78B7)
    WaitChrThread(0xFE, 1)

    def lambda_78D5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78D5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_787F end

    def Function_45_78E2(): pass

    label("Function_45_78E2")


    def lambda_78E7():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78E7)

    def lambda_7901():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7901)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_791A():
        OP_95(0xFE, 12960, 0, 65970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_791A)
    WaitChrThread(0xFE, 1)

    def lambda_7938():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7938)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_78E2 end

    def Function_46_7945(): pass

    label("Function_46_7945")


    def lambda_794A():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_794A)

    def lambda_7964():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7964)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_797D():
        OP_95(0xFE, 11900, 0, 66840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_797D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_46_7945 end

    def Function_47_7997(): pass

    label("Function_47_7997")

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
            "#0509F#11P──皆さん、凄いです！\x02\x03",

            "#0502Fまさか事件の真相を見抜いて\x01",
            "そのまま解決するなんて！\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x17,
        (
            "#2004F#5Pええ……正直、驚かされたわ。\x02\x03",

            "#2001Fできれば大立ち回りをする前に\x01",
            "私たちを呼んで欲しかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0006F#6Pその、すみません。\x02\x03",

            "#0008F……警備隊の司令殿から\x01",
            "マフィアに情報が流れる可能性を\x01",
            "つい考えてしまいまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x17,
        (
            "#2006F#5Pふう……\x01",
            "それを言われると辛いけどね。\x02\x03",

            "#2001Fでも貴方たち、その白い狼たちに\x01",
            "助けられなかったらどうしたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#0011F#6Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x104,
        "#0306F#6P正直、危なかったッスね。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        (
            "#2001F#5Pそういう時はセルゲイに相談して\x01",
            "私に直接話が行くようにするとか、\x01",
            "色々とやり方があるでしょう。\x02\x03",

            "確かに、クロスベルの現状には\x01",
            "色々と難しい問題があるけれど……\x02\x03",

            "それでも自分たちだけで\x01",
            "何でも解決しようとするのは\x01",
            "ただの思い上がりに過ぎないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x101,
        "#0006F#6P……はい……\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x102,
        "#0106F#6P……返す言葉もありません。\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x17,
        (
            "#2004F#5Pふふ……まあ、\x01",
            "お小言はここまでにしましょう。\x02\x03",

            "#2002F本当によく無事でいてくれたわ。\x02\x03",

            "それと、私たちの代わりに\x01",
            "事件を解決してくれて感謝します。\x02",
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
            "#0309F#6Pはは……\x01",
            "改めて言われるとムズ痒いっスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x18,
        (
            "#0504F#11Pふふ……ところで、副司令。\x02\x03",

            "#0500Fロイドさんたちを助けたという、\x01",
            "白い狼たちの方はどうしましょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x17,
        (
            "#2003F#5Pそうね……\x01",
            "完全に濡れ衣だったみたいだし。\x02\x03",

            "#2000F様子見してもいいと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        (
            "#0204F#6P……大丈夫かと思います。\x02\x03",

            "#0202F無用なトラブルを起こすほど\x01",
            "愚かではなさそうでしたから……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x17,
        (
            "#2002F#5Pふふ、そうみたいね。\x02\x03",

            "#2006F……しかし、そういう意味では\x01",
            "愚かなのは人間の方だったわね。\x02\x03",

            "まさか軍用犬の実戦テストをするために\x01",
            "各地で騒ぎを起こしていたなんて……\x02\x03",

            "#2001Fいくら後ろ盾があるからといって\x01",
            "舐めたことをしてくれたものだわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        "#0108F#6P……はい。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0000F#6Pでも、これだけの騒ぎを\x01",
            "起こしたわけですし……\x02\x03",

            "さすがに今回ばかりは\x01",
            "言い逃れはできないですよね？\x02",
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
        "#0011F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        (
            "#0101F#6Pやはり……\x01",
            "保釈されてしまう可能性が？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x17,
        "#2003F#5P……ええ、高いわね。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x18,
        (
            "#0506F#11P──今までにも、\x01",
            "国境付近でのマフィアの密輸を\x01",
            "摘発したことがあったんですが……\x02\x03",

            "その都度、圧力がかけられて\x01",
            "保釈されてしまっているんです。\x02\x03",

            "#0508Fそれどころか適当な名目で\x01",
            "密輸品も返還する事になって……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        "#0007F#6Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x103,
        "#0206F#6Pグダグダですね……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#0301F#6Pそういや、ベルガード門でも\x01",
            "同じようなことがあったな……\x02",
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
            "#2003F#5Pでも……\x01",
            "腐ってばかりもいられないわ。\x02\x03",

            "#2001Fこの状況で、みんなが諦めたら\x01",
            "クロスベルは本当に駄目になる……\x02\x03",

            "そう考えて、自分に出来ることを\x01",
            "している人たちは少なくないはずよ。\x02\x03",

            "#2000F貴方たちみたいにね。\x02",
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
            "#0002F#6Pあ……\x02\x03",

            "#0004F──はい。\x01",
            "そうでありたいと思っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x17,
        (
            "#2002F#5Pふふ……\x01",
            "これからも支援課#6Rあなたたち#の働きに\x01",
            "期待させてもらうわね。\x02\x03",

            "#2004F──さ、クロスベル市まで\x01",
            "うちの車両で送って行くわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 500)
    Sleep(300)

    #C0326
    ChrTalk(
        0x17,
        "#2000F#5Pノエル、出発の準備を。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)
    #Sound(1479, 255, 100, 0)    #voice#Noel
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0327
    ChrTalk(
        0x18,
        "#0502F#2P了解しました#12Rイ エ ス ・ マ ム#！\x02",
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

    # Function_47_7997 end

    def Function_48_8919(): pass

    label("Function_48_8919")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    SetChrFlags(0xFE, 0x4)

    def lambda_8939():
        OP_97(0xFE, 0xFFFFFA24, 0x190, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8939)
    Sleep(650)

    def lambda_8956():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8956)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_48_8919 end

    def Function_49_896B(): pass

    label("Function_49_896B")

    OP_9B(0x0, 0xFE, 0x0, 0x1AC2, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x12C)
    SetChrFlags(0xFE, 0x4)

    def lambda_898B():
        OP_97(0xFE, 0xFFFFFB78, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_898B)
    WaitChrThread(0xFE, 1)

    def lambda_89A9():
        OP_97(0xFE, 0xFFFFFA24, 0x190, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_89A9)
    Sleep(650)

    def lambda_89C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_89C6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_49_896B end

    def Function_50_89DB(): pass

    label("Function_50_89DB")

    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_89DB end

    def Function_51_89EF(): pass

    label("Function_51_89EF")

    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x3E8, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_89EF end

    def Function_52_8A03(): pass

    label("Function_52_8A03")

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
        "#0502F#5Pはい、到着しました。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0002F#12Pはは、さすがに\x01",
            "あっという間に着いたな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0330
    ChrTalk(
        0x101,
        (
            "#0000F#5P早速、町長さんに\x01",
            "詳しい話を聞きに行こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x104,
        "#0304F#12Pだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0332
    ChrTalk(
        0x102,
        (
            "#0100F#11P確か、まっすぐ進んで\x01",
            "突き当たりにある家だったわね。\x02",
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

    # Function_52_8A03 end

    def Function_53_8E00(): pass

    label("Function_53_8E00")

    Sleep(1000)
    Sound(485, 0, 90, 0)
    Return()

    # Function_53_8E00 end

    def Function_54_8E0A(): pass

    label("Function_54_8E0A")

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
            "#0005F#11Pもう夕方か……\x02\x03",

            "#0000Fそろそろクロスベル市に\x01",
            "戻った方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x102,
        (
            "#0103F#11Pそうね……\x01",
            "今日中に聞き込みくらいは\x01",
            "しておきたいところだし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0335
    ChrTalk(
        0x102,
        "#0100F#6Pノエルさん、お願いできる？\x02",
    )

    CloseMessageWindow()

    def lambda_904D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_904D)
    Sleep(50)

    def lambda_905D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_905D)
    Sleep(50)

    def lambda_906D():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_906D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0336
    ChrTalk(
        0x109,
        (
            "#0509F#11Pええ、お安い御用です。\x02\x03",

            "#0502Fそれでは\x01",
            "車両の所に戻りましょう。\x02",
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

    # Function_54_8E0A end

    def Function_55_90F8(): pass

    label("Function_55_90F8")


    def lambda_90FD():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_90FD)

    def lambda_9117():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9117)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_9130():
        OP_95(0xFE, 12200, 0, 64769, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9130)
    WaitChrThread(0x101, 1)
    Return()

    # Function_55_90F8 end

    def Function_56_914A(): pass

    label("Function_56_914A")


    def lambda_914F():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_914F)

    def lambda_9169():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9169)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_9182():
        OP_95(0xFE, 10890, 0, 65950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9182)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_56_914A end

    def Function_57_919C(): pass

    label("Function_57_919C")


    def lambda_91A1():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91A1)

    def lambda_91BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_91BB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_91D4():
        OP_95(0xFE, 12960, 0, 65970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91D4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_57_919C end

    def Function_58_91EE(): pass

    label("Function_58_91EE")


    def lambda_91F3():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91F3)

    def lambda_920D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_920D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_9226():
        OP_95(0xFE, 12550, 0, 67610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9226)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_58_91EE end

    def Function_59_9240(): pass

    label("Function_59_9240")


    def lambda_9245():
        OP_95(0xFE, 11920, 0, 68420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9245)

    def lambda_925F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_925F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_9278():
        OP_95(0xFE, 11220, 0, 67760, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9278)
    WaitChrThread(0xFE, 1)

    def lambda_9296():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9296)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_59_9240 end

    def Function_60_92A3(): pass

    label("Function_60_92A3")

    EventBegin(0x1)
    Sound(1499, 255, 100, 0)    #voice#Noel

    #A0337
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警備隊車両で移動しますか？\x02",
        )
    )

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9332")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市\x01",      # 0
            "やめる\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_932D")
    Call(0, 61)
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_932D")

    Jump("loc_933F")

    label("loc_9332")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 8)

    label("loc_933F")

    EventEnd(0x5)
    Return()

    # Function_60_92A3 end

    def Function_61_9342(): pass

    label("Function_61_9342")

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

    def lambda_9457():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_9457)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x13, 0x1)
    OP_6F(0x1)
    Return()

    # Function_61_9342 end

    def Function_62_947D(): pass

    label("Function_62_947D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94FB")

    #C0338
    ChrTalk(
        0x101,
        (
            "#0003Fもう日が暮れたし\x01",
            "街道に出るのはやめておこう。\x02\x03",

            "#0001F宿酒場で推理の検証も\x01",
            "しなくちゃいけないしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9558")

    #C0339
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街道方面だな。\x02\x03",

            "#0003F帰る前に町長さんの話を\x01",
            "聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95B9")

    #C0340
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街道方面だな。\x02\x03",

            "#0004Fせっかくだし\x01",
            "ノエル曹長に送ってもらおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95B9")

    Sleep(50)
    SetChrPos(0x0, 650, -2000, -4920, 0)
    EventEnd(0x4)
    Return()

    # Function_62_947D end

    SaveToFile()

Try(main)
