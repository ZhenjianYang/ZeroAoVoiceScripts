from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0500.bin",                # FileName
        "t0500",                    # MapName
        "t0500",                    # Location
        0x003C,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0500",                  # 0
        "亚米",                   # 1
        "卡洛斯",                 # 2
        "亚雷库",                 # 3
        "矿工罗基",               # 4
        "奇米",                   # 5
        "矿工冈兹",               # 6
        "矿工玛尔罗",             # 7
        "游击士温蔡尔",           # 8
        "琪露露",                 # 9
        "巴士",                   # 10
        "警备队员",               # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "警备队员",               # 14
        "警备队员",               # 15
        "米蕾优三尉",             # 16
        "车",                     # 17
        "蔡特",                   # 18
        "比克森镇长",             # 19
        "安娜夫人",               # 20
        "矿工马库斯",             # 21
        "霍夫曼矿山长",           # 22
        "SE控制",                 # 23
        "玛因兹山道",             # 24
        "玛因兹矿山",             # 25
    ))

    AddCharChip((
        "chr/ch23700.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch26200.itc",                   # 03
        "chr/ch23900.itc",                   # 04
        "chr/ch20500.itc",                   # 05
        "chr/ch30700.itc",                   # 06
        "chr/ch27300.itc",                   # 07
    ))

    DeclNpc(6739,    0,       42729,   0,    261,  0x0, 0,   0,   0,   0,   2,   0,   10,  255,  0)
    DeclNpc(10399,   0,       55259,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(28329,   -3000,   62000,   180,  261,  0x0, 0,   2,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(899,     6000,    77779,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(400,     6000,    77779,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1980,    6000,    77930,   45,   389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(19,      6000,    77889,   0,    389,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(1980,    6000,    77930,   45,   389,  0x0, 0,   7,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(1980,    6000,    77930,   45,   389,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-4600,   -2000,   28700,   1500,    -4600,   -500,    28700,   0x007C, 0,  21, 0x0000)
    DeclActor(4850,    -2000,   26210,   1500,    4850,    0,       26210,   0x007C, 0,  20, 0x0000)
    DeclActor(5390,    -2000,   26160,   1500,    5390,    0,       26160,   0x007C, 0,  20, 0x0000)
    DeclActor(-25900,  11440,   56000,   1500,    -25900,  12940,   56000,   0x007C, 0,  68, 0x0000)

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "玛因兹矿山")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")

    ChipFrameInfo(1344, 0)                                       # 0

    ScpFunction((
        "Function_0_54C",          # 00, 0
        "Function_1_604",          # 01, 1
        "Function_2_62F",          # 02, 2
        "Function_3_65A",          # 03, 3
        "Function_4_68D",          # 04, 4
        "Function_5_E16",          # 05, 5
        "Function_6_1033",         # 06, 6
        "Function_7_11AD",         # 07, 7
        "Function_8_12E0",         # 08, 8
        "Function_9_1331",         # 09, 9
        "Function_10_13C5",        # 0A, 10
        "Function_11_1F06",        # 0B, 11
        "Function_12_2A8F",        # 0C, 12
        "Function_13_323D",        # 0D, 13
        "Function_14_32FB",        # 0E, 14
        "Function_15_36A2",        # 0F, 15
        "Function_16_3857",        # 10, 16
        "Function_17_3937",        # 11, 17
        "Function_18_3A35",        # 12, 18
        "Function_19_3D15",        # 13, 19
        "Function_20_3E01",        # 14, 20
        "Function_21_412E",        # 15, 21
        "Function_22_4168",        # 16, 22
        "Function_23_46D8",        # 17, 23
        "Function_24_46E8",        # 18, 24
        "Function_25_4783",        # 19, 25
        "Function_26_4784",        # 1A, 26
        "Function_27_4785",        # 1B, 27
        "Function_28_4786",        # 1C, 28
        "Function_29_47C4",        # 1D, 29
        "Function_30_4847",        # 1E, 30
        "Function_31_48D1",        # 1F, 31
        "Function_32_495C",        # 20, 32
        "Function_33_49DF",        # 21, 33
        "Function_34_4AD7",        # 22, 34
        "Function_35_4B7B",        # 23, 35
        "Function_36_4BB8",        # 24, 36
        "Function_37_4C1A",        # 25, 37
        "Function_38_4CFB",        # 26, 38
        "Function_39_5095",        # 27, 39
        "Function_40_50F5",        # 28, 40
        "Function_41_5105",        # 29, 41
        "Function_42_5118",        # 2A, 42
        "Function_43_512B",        # 2B, 43
        "Function_44_513E",        # 2C, 44
        "Function_45_57F5",        # 2D, 45
        "Function_46_580F",        # 2E, 46
        "Function_47_587E",        # 2F, 47
        "Function_48_58E7",        # 30, 48
        "Function_49_5925",        # 31, 49
        "Function_50_5966",        # 32, 50
        "Function_51_59A7",        # 33, 51
        "Function_52_5A1A",        # 34, 52
        "Function_53_5A33",        # 35, 53
        "Function_54_6141",        # 36, 54
        "Function_55_6179",        # 37, 55
        "Function_56_6220",        # 38, 56
        "Function_57_62AF",        # 39, 57
        "Function_58_78E2",        # 3A, 58
        "Function_59_7912",        # 3B, 59
        "Function_60_7968",        # 3C, 60
        "Function_61_79BB",        # 3D, 61
        "Function_62_7A25",        # 3E, 62
        "Function_63_7A85",        # 3F, 63
        "Function_64_7AE5",        # 40, 64
        "Function_65_7CF3",        # 41, 65
        "Function_66_7D40",        # 42, 66
        "Function_67_7D8D",        # 43, 67
        "Function_68_7DB2",        # 44, 68
    ))


    def Function_0_54C(): pass

    label("Function_0_54C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_58C"),
        (1, "loc_598"),
        (2, "loc_5A4"),
        (3, "loc_5B0"),
        (4, "loc_5BC"),
        (5, "loc_5C8"),
        (6, "loc_5D4"),
        (SWITCH_DEFAULT, "loc_5E0"),
    )


    label("loc_58C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_598")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_603")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5EC")

    label("loc_603")

    Return()

    # Function_0_54C end

    def Function_1_604(): pass

    label("Function_1_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62E")
    OP_94(0xFE, 0x648C, 0xEA38, 0x727E, 0xF488, 0x3E8)
    Sleep(300)
    Jump("Function_1_604")

    label("loc_62E")

    Return()

    # Function_1_604 end

    def Function_2_62F(): pass

    label("Function_2_62F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_659")
    OP_94(0xFE, 0x1C98, 0x8EDA, 0x1F40, 0xB72A, 0x3E8)
    Sleep(300)
    Jump("Function_2_62F")

    label("loc_659")

    Return()

    # Function_2_62F end

    def Function_3_65A(): pass

    label("Function_3_65A")

    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)

    label("loc_68C")

    Return()

    # Function_3_65A end

    def Function_4_68D(): pass

    label("Function_4_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6A0")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_82A")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6CE")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18450, -8990, 41770, 270)
    Jump("loc_82A")

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6F2")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18450, -8990, 41770, 270)
    Jump("loc_82A")

    label("loc_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_700")
    Jump("loc_82A")

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_70E")
    Jump("loc_82A")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_72B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_82A")

    label("loc_72B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_739")
    Jump("loc_82A")

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_77E")
    SetChrPos(0xA, 1400, 6000, 77780, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 400, 6000, 77780, 0)
    SetChrFlags(0xC, 0x10)
    Jump("loc_82A")

    label("loc_77E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_791")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_82A")

    label("loc_791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7CC")
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 1850, 0, 69850, 270)
    SetChrPos(0xC, 850, 0, 69850, 90)
    Jump("loc_82A")

    label("loc_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7DA")
    Jump("loc_82A")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7ED")
    SetChrFlags(0x8, 0x80)
    Jump("loc_82A")

    label("loc_7ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_800")
    SetChrFlags(0xA, 0x80)
    Jump("loc_82A")

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_813")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_82A")

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_821")
    Jump("loc_82A")

    label("loc_821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_82A")

    label("loc_82A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84E")
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_885")

    label("loc_84E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86D")
    Event(0, 44)
    Jump("loc_885")

    label("loc_86D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_885")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 53)

    label("loc_885")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_89C")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 22)
    Jump("loc_8E7")

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_8B0")
    ClearScenarioFlags(0x22, 1)
    Event(0, 44)
    Jump("loc_8E7")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_8C4")
    ClearScenarioFlags(0x22, 2)
    Event(0, 53)
    Jump("loc_8E7")

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_8D8")
    ClearScenarioFlags(0x22, 3)
    Event(0, 57)
    Jump("loc_8E7")

    label("loc_8D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_8E7")
    ClearScenarioFlags(0x22, 4)
    Event(0, 64)

    label("loc_8E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8B")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974")
    SetScenarioFlags(0x38, 0)

    label("loc_974")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98A")
    SetScenarioFlags(0x38, 1)

    label("loc_98A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A0")
    SetScenarioFlags(0x38, 2)

    label("loc_9A0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B6")
    SetScenarioFlags(0x38, 3)

    label("loc_9B6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CC")
    SetScenarioFlags(0x38, 4)

    label("loc_9CC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E2")
    SetScenarioFlags(0x38, 5)

    label("loc_9E2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F8")
    SetScenarioFlags(0x38, 6)

    label("loc_9F8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E")
    SetScenarioFlags(0x38, 7)

    label("loc_A0E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A24")
    SetScenarioFlags(0x39, 0)

    label("loc_A24")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3A")
    SetScenarioFlags(0x39, 1)

    label("loc_A3A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A50")
    SetScenarioFlags(0x39, 2)

    label("loc_A50")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A66")
    SetScenarioFlags(0x39, 3)

    label("loc_A66")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7C")
    SetScenarioFlags(0x39, 4)

    label("loc_A7C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A92")
    SetScenarioFlags(0x39, 5)

    label("loc_A92")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA8")
    SetScenarioFlags(0x39, 6)

    label("loc_AA8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABE")
    SetScenarioFlags(0x39, 7)

    label("loc_ABE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4")
    SetScenarioFlags(0x3A, 0)

    label("loc_AD4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEA")
    SetScenarioFlags(0x3A, 1)

    label("loc_AEA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00")
    SetScenarioFlags(0x3A, 2)

    label("loc_B00")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B16")
    SetScenarioFlags(0x3A, 3)

    label("loc_B16")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2C")
    SetScenarioFlags(0x3A, 4)

    label("loc_B2C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B42")
    SetScenarioFlags(0x3A, 5)

    label("loc_B42")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B58")
    SetScenarioFlags(0x3A, 6)

    label("loc_B58")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6E")
    SetScenarioFlags(0x3A, 7)

    label("loc_B6E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    SetScenarioFlags(0x3B, 0)

    label("loc_B84")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9A")
    SetScenarioFlags(0x3B, 1)

    label("loc_B9A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB0")
    SetScenarioFlags(0x3B, 2)

    label("loc_BB0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC6")
    SetScenarioFlags(0x3B, 3)

    label("loc_BC6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDC")
    SetScenarioFlags(0x3B, 4)

    label("loc_BDC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    SetScenarioFlags(0x3B, 5)

    label("loc_BF2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C08")
    SetScenarioFlags(0x3B, 6)

    label("loc_C08")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1E")
    SetScenarioFlags(0x3B, 7)

    label("loc_C1E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    SetScenarioFlags(0x3D, 5)

    label("loc_C34")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4A")
    SetScenarioFlags(0x3D, 6)

    label("loc_C4A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C60")
    SetScenarioFlags(0x3D, 7)

    label("loc_C60")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9B")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_D8B")

    label("loc_C9B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBE")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_D8B")

    label("loc_CBE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE1")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_D8B")

    label("loc_CE1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D04")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_D8B")

    label("loc_D04")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D27")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_D8B")

    label("loc_D27")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4A")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_D8B")

    label("loc_D4A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6D")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_D8B")

    label("loc_D6D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8B")
    SetScenarioFlags(0x3C, 7)

    label("loc_D8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA1")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD3")
    SetChrPos(0x0, 2750, -2000, 25500, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_E06")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E06")
    SetChrPos(0x0, 2750, -2000, 25500, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_E15")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 8)

    label("loc_E15")

    Return()

    # Function_4_68D end

    def Function_5_E16(): pass

    label("Function_5_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E30")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_E5C")

    label("loc_E30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_E4A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)
    Jump("loc_E5C")

    label("loc_E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E5C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E5C")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEF")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_F06")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_F06")

    label("loc_F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F14")
    Jump("loc_FEB")

    label("loc_F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F35")
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jump("loc_FEB")

    label("loc_F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F43")
    Jump("loc_FEB")

    label("loc_F43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F51")
    Jump("loc_FEB")

    label("loc_F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F5F")
    Jump("loc_FEB")

    label("loc_F5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F6D")
    Jump("loc_FEB")

    label("loc_F6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F7B")
    Jump("loc_FEB")

    label("loc_F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F89")
    Jump("loc_FEB")

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_F97")
    Jump("loc_FEB")

    label("loc_F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FB8")
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jump("loc_FEB")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FC6")
    Jump("loc_FEB")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_FD4")
    Jump("loc_FEB")

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FE2")
    Jump("loc_FEB")

    label("loc_FE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FEB")

    label("loc_FEB")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_101F")
    Jump("loc_1032")

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1032")
    ClearMapObjFlags(0x6, 0x10)
    OP_66(0x3, 0x1)

    label("loc_1032")

    Return()

    # Function_5_E16 end

    def Function_6_1033(): pass

    label("Function_6_1033")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F4")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查停靠站的告示牌，\x01",
            "即可乘坐导力巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与驾驶导力车相同，乘坐巴士\x01",
            "也可以来往于各地，请多加活用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_10F4")


    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K这里是巴士车站。\x01",
            "要搭乘巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市北出口\x01",          # 0
            "停靠站（人偶工房附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1185")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A5")

    label("loc_1185")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A5")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_11A5")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1033 end

    def Function_7_11AD(): pass

    label("Function_7_11AD")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_12DC")
    Fade(500)
    OP_68(-3860, -550, 26120, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    SetChrPos(0x1, -5300, -2000, 27570, 180)
    SetChrPos(0x2, -6100, -2000, 27430, 180)
    SetChrPos(0x3, -6860, -2000, 27250, 180)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x2)
    OP_78(0x8, 0x11)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -6320, -2000, 11640, 0)
    OP_D5(0x11, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1293():
        OP_96(0xFE, 0xFFFFE750, 0xFFFFF830, 0x528A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1293)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x8, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x8)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_12DC")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_11AD end

    def Function_8_12E0(): pass

    label("Function_8_12E0")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -4540, -2000, 27710, 180)
    OP_31(0x1)
    OP_68(-4540, -550, 27710, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    EventEnd(0x5)
    Return()

    # Function_8_12E0 end

    def Function_9_1331(): pass

    label("Function_9_1331")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_138C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1381")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1387")

    label("loc_1381")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1387")

    Jump("loc_13B0")

    label("loc_138C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13AA")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_13B0")

    label("loc_13AA")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_13B0")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_1331 end

    def Function_10_13C5(): pass

    label("Function_10_13C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1493")

    #C0004
    ChrTalk(
        0x8,
        (
            "那、那究竟是什么？\x01",
            "那棵散发着蓝白色光芒的树……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "就算站在玛因兹这种高地来眺望，\x01",
            "也能看出它相当巨大啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "就连熟知历史的奶奶\x01",
            "也说从没听说过那种树，\x01",
            "真是让人不安啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1504")

    label("loc_1493")


    #C0007
    ChrTalk(
        0x8,
        (
            "那棵散发着蓝白色光芒的树……\x01",
            "究竟是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "就连熟知历史的奶奶\x01",
            "也说从没听说过那种树，\x01",
            "真是让人不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1504")

    Jump("loc_1F02")

    label("loc_1509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AE")

    #C0009
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔的独立无效，\x01",
            "这是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "那些前来搜索反抗军\x01",
            "成员的国防军士兵\x01",
            "已经焦躁万分地回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "嘿嘿，真开心啊。\x01",
            "正义必胜！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_160F")

    label("loc_15AE")


    #C0012
    ChrTalk(
        0x8,
        (
            "那些前来搜索反抗军\x01",
            "成员的国防军士兵\x01",
            "已经焦躁万分地回去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "嘿嘿，真开心啊。\x01",
            "正义必胜！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160F")

    Jump("loc_1F02")

    label("loc_1614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    #C0014
    ChrTalk(
        0x8,
        (
            "玛因兹矿山镇的全体居民\x01",
            "都在支持警备队员们的\x01",
            "反抗行动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "居然雇佣了侵占过\x01",
            "玛因兹的猎兵，\x01",
            "我们可无法信任那种总统。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "……而且，向统治者发起反抗，\x01",
            "贯彻自己相信的正义……\x01",
            "反抗军真是很帅呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_177D")

    label("loc_16F7")


    #C0017
    ChrTalk(
        0x8,
        (
            "玛因兹矿山镇的全体居民\x01",
            "都在支持警备队员们的\x01",
            "反抗行动哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "我们无法信任那种总统……\x01",
            "而且向统治者发起抵抗的\x01",
            "反抗军实在是很帅！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177D")

    Jump("loc_1F02")

    label("loc_1782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1878")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1852")

    #C0019
    ChrTalk(
        0x8,
        (
            "当时，那些猎兵出现在\x01",
            "镇上的时候，\x01",
            "我真的以为彻底完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "前来援救我们的警备队\x01",
            "陆续被猎兵击溃……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "不过，那些猎兵对镇上的人与物\x01",
            "几乎没有任何侵害。\x01",
            "他们到底有何企图啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1873")

    label("loc_1852")


    #C0022
    ChrTalk(
        0x8,
        (
            "那些猎兵到底\x01",
            "有何企图呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1873")

    Jump("loc_1F02")

    label("loc_1878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1886")
    Jump("loc_1F02")

    label("loc_1886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_19E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1979")

    #C0023
    ChrTalk(
        0x8,
        (
            "彩虹剧团的新版舞剧\x01",
            "后天就要在克洛斯贝尔市\x01",
            "公演了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "哪怕只有一次也好，\x01",
            "我真想去现场看看舞台表演啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "说不定还能碰巧坐在\x01",
            "喜爱舞剧的大叔的旁边，\x01",
            "然后趁机攀谈起来呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#00000F（动机真是不纯啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19E1")

    label("loc_1979")


    #C0027
    ChrTalk(
        0x8,
        (
            "哪怕只有一次也好，\x01",
            "我真想去现场看看舞台表演啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "说不定还会与喜爱舞剧的大叔\x01",
            "有个美妙的邂逅呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E1")

    Jump("loc_1F02")

    label("loc_19E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACD")

    #C0029
    ChrTalk(
        0x8,
        (
            "不久之前，有两位游击士\x01",
            "前来驱逐了出现在\x01",
            "北部山岳地带的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "虽然将魔兽顺利击退了，\x01",
            "但据说那只魔兽并不普通，\x01",
            "是一种很奇怪的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "最近经常能听到\x01",
            "有关那种魔兽的传言……\x01",
            "或许存在某些原因吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B1C")

    label("loc_1ACD")


    #C0032
    ChrTalk(
        0x8,
        (
            "话说回来，\x01",
            "竟然连那种来历不明的\x01",
            "魔兽都能击退……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "游击士果然\x01",
            "很帅啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1C")

    Jump("loc_1F02")

    label("loc_1B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3D")

    #C0034
    ChrTalk(
        0x8,
        (
            "主日学校的修女\x01",
            "会定期来镇上\x01",
            "授课……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "要是偶尔也派个\x01",
            "年轻的神父来讲课就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "嗯嗯！\x01",
            "最好是那种把修道服改制成\x01",
            "帅气式样的时髦神父！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#00000F虽、虽说只是妄想，\x01",
            "但听上去真是相当夸张的不良神父啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，不过还\x01",
            "真有那样的神父呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CB2")

    label("loc_1C3D")


    #C0039
    ChrTalk(
        0x8,
        (
            "要是偶尔也派个\x01",
            "年轻的神父来讲课就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "如果有那种把修道服改制成\x01",
            "帅气式样的时髦神父，\x01",
            "我说不定会被迷住呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB2")

    Jump("loc_1F02")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1CC5")
    Jump("loc_1F02")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D50")

    #C0041
    ChrTalk(
        0x8,
        (
            "我哥哥是在矿山\x01",
            "工作的矿工。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "他以前总爱偷懒，\x01",
            "但不知为何，最近好像很努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        "呵呵，奶奶也很高兴呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DA0")

    label("loc_1D50")


    #C0044
    ChrTalk(
        0x8,
        (
            "我哥哥原来\x01",
            "总是爱偷懒，\x01",
            "但最近开始认真工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "呵呵，奶奶也很高兴呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1DA0")

    Jump("loc_1F02")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1F02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E86")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0046
    ChrTalk(
        0x8,
        "#5S哇哇！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，找我有什么事吗？\x01",
            "可爱的小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "（这这这这这、这个人……！\x01",
            "  好英俊啊！）\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00000F（唔，不愧是瓦吉……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F02")

    label("loc_1E86")

    TurnDirection(0x8, 0x105, 0)

    #C0050
    ChrTalk(
        0x8,
        (
            "呼，这张脸实在是\x01",
            "太漂亮了……⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "（……哎？\x01",
            "  不过，到底是男孩还是女孩呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x105,
        "#10300F呵呵，奇怪的孩子。\x02",
    )

    CloseMessageWindow()

    label("loc_1F02")

    TalkEnd(0xFE)
    Return()

    # Function_10_13C5 end

    def Function_11_1F06(): pass

    label("Function_11_1F06")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA4")

    #C0053
    ChrTalk(
        0x9,
        "竟然会出现那种东西……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        "……不行，我可不能胆怯。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "矿山好不容易重新开放了，\x01",
            "大家现在干劲十足，\x01",
            "必须要积极向前看啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FEA")

    label("loc_1FA4")


    #C0056
    ChrTalk(
        0x9,
        (
            "矿山好不容易重新开放了，\x01",
            "大家现在干劲十足，\x01",
            "必须要积极向前看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FEA")

    Jump("loc_2A8B")

    label("loc_1FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_210D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AA")

    #C0057
    ChrTalk(
        0x9,
        (
            "自从那些猎兵上次\x01",
            "展开围剿行动之后，\x01",
            "就没有再发生过大规模作战了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "如今发表了独立无效宣言，\x01",
            "真担心他们会有什么行动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "希望反抗军的各位\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2108")

    label("loc_20AA")


    #C0060
    ChrTalk(
        0x9,
        (
            "如今发表了独立无效宣言，\x01",
            "真担心那些猎兵会有什么行动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "希望反抗军的各位\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2108")

    Jump("loc_2A8B")

    label("loc_210D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21CC")

    #C0062
    ChrTalk(
        0x9,
        (
            "米蕾优小姐他们\x01",
            "刚刚来到这里的时候，\x01",
            "我们还有些警戒……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "不过，玛因兹的各位\x01",
            "也都对总统与国防军的方针\x01",
            "抱有很大疑问。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        "在这种时候，就得鼓起勇气支持他们。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2234")

    label("loc_21CC")


    #C0065
    ChrTalk(
        0x9,
        (
            "玛因兹的各位和\x01",
            "米蕾优小姐他们一样，\x01",
            "也对总统抱有很大疑问。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "在这种时候，就得鼓起勇气支持他们。\x02",
    )

    CloseMessageWindow()

    label("loc_2234")

    Jump("loc_2A8B")

    label("loc_2239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_238B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2318")

    #C0067
    ChrTalk(
        0x9,
        (
            "据说占领玛因兹与袭击城市\x01",
            "都是帝国为了让我们撤回\x01",
            "独立提案而发起的行动。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "竟然把我们这些无辜的居民卷入，\x01",
            "还给警备队造成巨大损害……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "……这种为了政治而牺牲他人的做法，\x01",
            "我绝对无法原谅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2386")

    label("loc_2318")


    #C0070
    ChrTalk(
        0x9,
        (
            "据说占领玛因兹与袭击城市\x01",
            "都是帝国发起的行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "……这种为了政治而牺牲他人的做法，\x01",
            "我绝对无法原谅。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2386")

    Jump("loc_2A8B")

    label("loc_238B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2399")
    Jump("loc_2A8B")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2448")

    #C0072
    ChrTalk(
        0x9,
        (
            "即使是我这样的玛因兹居民，\x01",
            "也不了解位于山道途中\x01",
            "的那家工房。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "因为那家工房的主人\x01",
            "从来都不会出现在镇上。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "多半是个相当\x01",
            "乖张古怪的人吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_249E")

    label("loc_2448")


    #C0075
    ChrTalk(
        0x9,
        (
            "山道途中那家工房的主人\x01",
            "从来都不会出现在镇上。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "多半是个相当\x01",
            "乖张古怪的人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249E")

    Jump("loc_2A8B")

    label("loc_24A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_25AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2542")

    #C0077
    ChrTalk(
        0x9,
        (
            "不久前，\x01",
            "北部山岳地带出现了魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "听说那只魔兽的样子与\x01",
            "当时出现在旧矿山的魔兽相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "唔……二者是不是有什么关系呢？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_25A6")

    label("loc_2542")


    #C0080
    ChrTalk(
        0x9,
        (
            "听说北部山岳地带的魔兽\x01",
            "与当时出现在旧矿山\x01",
            "的魔兽外貌相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        "唔……二者是不是有什么关系呢？\x02",
    )

    CloseMessageWindow()

    label("loc_25A6")

    Jump("loc_2A8B")

    label("loc_25AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2649")

    #C0082
    ChrTalk(
        0x9,
        (
            "冈兹先生昨天\x01",
            "又在巴鲁卡输了好多。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "为了散心，矿工们一起\x01",
            "尽情喝酒玩乐。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "我也在中途加入了。\x01",
            "哎呀呀，玩得真是很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_269F")

    label("loc_2649")


    #C0085
    ChrTalk(
        0x9,
        (
            "矿工们昨天\x01",
            "一起尽情喝酒玩乐。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "我也在中途加入了。\x01",
            "哎呀呀，玩得真是很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269F")

    Jump("loc_2A8B")

    label("loc_26A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2779")

    #C0087
    ChrTalk(
        0x9,
        (
            "今天早上我\x01",
            "去市里运送七耀石，\x01",
            "顺便还去观看了揭幕式。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "去观看兰花塔揭幕式的\x01",
            "人们心情似乎都\x01",
            "非常激动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "站在那么高的建筑物上，\x01",
            "恐怕能将整个城市一览无余吧。\x01",
            "真想上去看看啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27FB")

    label("loc_2779")


    #C0090
    ChrTalk(
        0x9,
        (
            "在观看兰花塔的揭幕式时，\x01",
            "大家的心情都\x01",
            "非常激动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "站在那么高的建筑物上，\x01",
            "恐怕能将整个城市一览无余吧。\x01",
            "真想上去看看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27FB")

    Jump("loc_2A8B")

    label("loc_2800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_295A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D4")

    #C0092
    ChrTalk(
        0x9,
        (
            "我负责把从这座矿山中\x01",
            "采掘到的七耀石\x01",
            "运送到城市……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "山道上有很多弯路，\x01",
            "驾驶这种满载货物的\x01",
            "运输车实在是很不容易。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "再加上山道的一侧都是悬崖，\x01",
            "在开车时，必须要特别小心慎重。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2955")

    label("loc_28D4")


    #C0095
    ChrTalk(
        0x9,
        (
            "山道上有很多弯路，\x01",
            "驾驶这种满载货物的\x01",
            "运输车实在是很不容易。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "再加上山道的一侧都是悬崖，\x01",
            "在开车时，必须要特别小心慎重。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2955")

    Jump("loc_2A8B")

    label("loc_295A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A13")

    #C0097
    ChrTalk(
        0x9,
        (
            "冈兹最近似乎\x01",
            "工作得很开心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "看样子，\x01",
            "在经历了那起教团事件之后，\x01",
            "他已经彻底改头换面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "虽然当时让大家担心不已……\x01",
            "但现在这结果真是很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A8B")

    label("loc_2A13")


    #C0100
    ChrTalk(
        0x9,
        (
            "冈兹在经历了那起教团事件之后，\x01",
            "似乎已经彻底改头换面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "虽然当时让大家担心不已……\x01",
            "但现在这结果真是很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8B")

    TalkEnd(0xFE)
    Return()

    # Function_11_1F06 end

    def Function_12_2A8F(): pass

    label("Function_12_2A8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B05")

    #C0102
    ChrTalk(
        0xA,
        (
            "我爸爸和各位矿工\x01",
            "今天进入矿山了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "大家好像都很高兴……\x01",
            "嘿嘿嘿，我也很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B69")

    label("loc_2B05")


    #C0104
    ChrTalk(
        0xA,
        (
            "虽然那棵突然出现\x01",
            "的巨树让人很不安，\x01",
            "但矿山能重新开放，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "希望爸爸他们继续加油。\x02",
    )

    CloseMessageWindow()

    label("loc_2B69")

    Jump("loc_3239")

    label("loc_2B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2BCD")

    #C0106
    ChrTalk(
        0xA,
        (
            "听说最近有很多狼\x01",
            "在帮助反抗军\x01",
            "的各位呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "真是很聪明的狼啊，\x01",
            "太可靠了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3239")

    label("loc_2BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C51")

    #C0108
    ChrTalk(
        0xA,
        (
            "在这种状况下，\x01",
            "矿山也只能暂时关闭了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "爸爸在家里，我当然\x01",
            "很开心……\x01",
            "但总觉得他好像感到很无聊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CBE")

    label("loc_2C51")


    #C0110
    ChrTalk(
        0xA,
        (
            "矿山封闭之后，\x01",
            "爸爸好像感到很无聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "我还是更喜欢在矿山中\x01",
            "努力工作的爸爸……\x01",
            "希望矿山能早日重开啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CBE")

    Jump("loc_3239")

    label("loc_2CC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D85")

    #C0112
    ChrTalk(
        0xA,
        (
            "那些坏蛋来侵略的时候，\x01",
            "矿工叔叔们为保卫矿山镇\x01",
            "奋起反抗。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "但最后还是敌不过他们……\x01",
            "爸爸也拼命战斗，\x01",
            "结果受了伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "虽然伤得并不严重，\x01",
            "不过还是好担心他……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2E00")

    label("loc_2D85")


    #C0115
    ChrTalk(
        0xA,
        (
            "爸爸他们为了保卫矿山镇，\x01",
            "拼命和那些坏蛋战斗……\x01",
            "但最后还是敌不过他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "虽然爸爸伤得并不严重，\x01",
            "不过还是好担心他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E00")

    Jump("loc_3239")

    label("loc_2E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E13")
    Jump("loc_3239")

    label("loc_2E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2E")
    Call(0, 13)
    Jump("loc_2E71")

    label("loc_2E2E")


    #C0117
    ChrTalk(
        0xA,
        (
            "啊哈哈，山里的回音\x01",
            "真有意思啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "接下来该喊点什么好呢……\x02",
    )

    CloseMessageWindow()

    label("loc_2E71")

    Jump("loc_3239")

    label("loc_2E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F1F")

    #C0119
    ChrTalk(
        0xA,
        (
            "听说罗基叔叔最近\x01",
            "完全没有在工作时偷过懒。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "虽然他嘴上\x01",
            "抱怨不断……\x01",
            "但脸上的表情却非常开心。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "我也想成为懂得\x01",
            "享受工作的优秀矿工。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2F48")

    label("loc_2F1F")


    #C0122
    ChrTalk(
        0xA,
        (
            "我也想成为懂得\x01",
            "享受工作的优秀矿工。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F48")

    Jump("loc_3239")

    label("loc_2F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF1")

    #C0123
    ChrTalk(
        0xA,
        (
            "主日学校的修女\x01",
            "今天来这里讲了课。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "虽然并不是以前常来的\x01",
            "那位修女，不过她非常温柔，\x01",
            "教得很耐心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        "嘿嘿嘿，真想再次见到她。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_305B")

    label("loc_2FF1")


    #C0126
    ChrTalk(
        0xA,
        (
            "今天来的老师虽然不是\x01",
            "以前常来的那位修女，\x01",
            "不过非常温柔，教得很耐心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        "嘿嘿嘿，真想再次见到她。\x02",
    )

    CloseMessageWindow()

    label("loc_305B")

    Jump("loc_3239")

    label("loc_3060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_311B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30DB")

    #C0128
    ChrTalk(
        0xA,
        "（一脸沮丧）……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "我昨天被爸爸妈妈\x01",
            "狠狠骂了一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "进入矿山里面\x01",
            "真的有那么严重吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3116")

    label("loc_30DB")


    #C0131
    ChrTalk(
        0xA,
        (
            "进入矿山里面\x01",
            "真的有那么严重吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        "（一脸沮丧）……\x02",
    )

    CloseMessageWindow()

    label("loc_3116")

    Jump("loc_3239")

    label("loc_311B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3129")
    Jump("loc_3239")

    label("loc_3129")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E8")

    #C0133
    ChrTalk(
        0xA,
        (
            "我今天早上出去玩，\x01",
            "发现镇外那个旧矿山\x01",
            "的大门开着。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "我偷偷摸摸地进去之后，\x01",
            "立刻就被冈兹叔叔发现了，\x01",
            "他狠狠地训斥了我一顿。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        "哼，我只是想去探险而已嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3239")

    label("loc_31E8")


    #C0136
    ChrTalk(
        0xA,
        (
            "我早就想去\x01",
            "旧矿山探险了……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "但刚进去就被冈兹叔叔训了一顿，真是没办法。\x02",
    )

    CloseMessageWindow()

    label("loc_3239")

    TalkEnd(0xFE)
    Return()

    # Function_12_2A8F end

    def Function_13_323D(): pass

    label("Function_13_323D")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0138
    ChrTalk(
        0xA,
        "#4S呀哈！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("山谷回音")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……呀……哈……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0140
    ChrTalk(
        0xC,
        "#4S我最喜欢爸爸啦！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("山谷回音")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……喜欢……爸爸……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 1)
    OP_4C(0xA, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_13_323D end

    def Function_14_32FB(): pass

    label("Function_14_32FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_330C")
    Jump("loc_369E")

    label("loc_330C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3346")

    #C0142
    ChrTalk(
        0xB,
        "呼………………\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        "矿山还不重开吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_369E")

    label("loc_3346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_346B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EC")

    #C0144
    ChrTalk(
        0xB,
        (
            "自从成为独立国家以后，\x01",
            "我的生活好像又要恢复到\x01",
            "以前那种散漫的状态了。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "唉……好不容易有了干劲，\x01",
            "想努力工作一番，结果却遇到这种事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3466")

    label("loc_33EC")


    #C0146
    ChrTalk(
        0xB,
        (
            "我难得有了干劲，想在矿山里\x01",
            "努力工作，结果却遇到这种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "这样下去，大概又要恢复到\x01",
            "以前那种散漫的生活状态了吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3466")

    Jump("loc_369E")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3479")
    Jump("loc_369E")

    label("loc_3479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3487")
    Jump("loc_369E")

    label("loc_3487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3495")
    Jump("loc_369E")

    label("loc_3495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34A3")
    Jump("loc_369E")

    label("loc_34A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34B1")
    Jump("loc_369E")

    label("loc_34B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34BF")
    Jump("loc_369E")

    label("loc_34BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34CD")
    Jump("loc_369E")

    label("loc_34CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_369E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AA")

    #C0148
    ChrTalk(
        0xB,
        (
            "我以前经常\x01",
            "偷懒怠工……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "最近不再那样之后，\x01",
            "连读书的时间都没有了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "这本书……我留着也没用，\x01",
            "不如送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0151
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2EF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2EF, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 1)
    Jump("loc_369E")

    label("loc_35AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3665")

    #C0152
    ChrTalk(
        0xB,
        (
            "其实我很想\x01",
            "和从前一样，\x01",
            "继续偷懒怠工……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "但最近这段时间，大家全都干劲十足，\x01",
            "我也不好意思再偷懒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "说不定一段时间之内\x01",
            "都得努力工作才行。\x01",
            "唉，真是累人……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_369E")

    label("loc_3665")


    #C0155
    ChrTalk(
        0xB,
        (
            "……我现在并不是在偷懒哦，\x01",
            "只是在休息时间放松一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369E")

    TalkEnd(0xFE)
    Return()

    # Function_14_32FB end

    def Function_15_36A2(): pass

    label("Function_15_36A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36B3")
    Jump("loc_3853")

    label("loc_36B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36C1")
    Jump("loc_3853")

    label("loc_36C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3737")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36DC")
    Call(0, 13)
    Jump("loc_3732")

    label("loc_36DC")


    #C0156
    ChrTalk(
        0xC,
        (
            "好棒啊！\x01",
            "声音清清楚楚地传回来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "那座山的对面是不是\x01",
            "有个像我一样的小孩呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3732")

    Jump("loc_3853")

    label("loc_3737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3745")
    Jump("loc_3853")

    label("loc_3745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_382E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D5")

    #C0158
    ChrTalk(
        0xC,
        (
            "修女已经\x01",
            "回教会了哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "说起来，她回去的时候，\x01",
            "好像一直在\x01",
            "盯着远方的天空……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        "唔……是不是发生什么事了～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3829")

    label("loc_37D5")


    #C0161
    ChrTalk(
        0xC,
        (
            "修女回去的时候，\x01",
            "好像一直在\x01",
            "盯着远方的天空……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        "唔……是不是发生什么事了～\x02",
    )

    CloseMessageWindow()

    label("loc_3829")

    Jump("loc_3853")

    label("loc_382E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_383C")
    Jump("loc_3853")

    label("loc_383C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_384A")
    Jump("loc_3853")

    label("loc_384A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3853")

    label("loc_3853")

    TalkEnd(0xFE)
    Return()

    # Function_15_36A2 end

    def Function_16_3857(): pass

    label("Function_16_3857")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3868")
    Jump("loc_3933")

    label("loc_3868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_392A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F8")

    #C0163
    ChrTalk(
        0xD,
        (
            "虽然我们也想帮些忙……\x01",
            "但终究没能力和反抗军的\x01",
            "那位小姐并肩作战啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xD,
        (
            "……我们矿工能做的事情\x01",
            "也只有挖矿了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3925")

    label("loc_38F8")


    #C0165
    ChrTalk(
        0xD,
        (
            "……我们矿工能做的事情\x01",
            "也只有挖矿了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3925")

    Jump("loc_3933")

    label("loc_392A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3933")

    label("loc_3933")

    TalkEnd(0xFE)
    Return()

    # Function_16_3857 end

    def Function_17_3937(): pass

    label("Function_17_3937")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3948")
    Jump("loc_3A31")

    label("loc_3948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3A28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")

    #C0166
    ChrTalk(
        0xE,
        (
            "琉卡小姐把我从酒馆里\x01",
            "轰出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "说是要让反抗军的领袖小姐\x01",
            "好好休息一下……\x01",
            "算啦，这也没办法。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3A23")

    label("loc_39CA")


    #C0168
    ChrTalk(
        0xE,
        (
            "……话说回来，\x01",
            "我还是第一次这么久\x01",
            "不做挖矿工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        (
            "没想到感觉会\x01",
            "如此空虚啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A23")

    Jump("loc_3A31")

    label("loc_3A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A31")

    label("loc_3A31")

    TalkEnd(0xFE)
    Return()

    # Function_17_3937 end

    def Function_18_3A35(): pass

    label("Function_18_3A35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C51")

    #C0170
    ChrTalk(
        0xFE,
        (
            "玛因兹矿山重开之后，\x01",
            "一些危险度很高的魔兽汹涌而来，\x01",
            "我好不容易才将它们击退。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "与『魔导兵』或『幻兽』相比，\x01",
            "自然没什么大不了的，\x01",
            "但独自一人驱赶魔兽实在是很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#00000F哈哈……好厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00304F不愧是出身于帝国协会\x01",
            "的精英游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "呵，我还差得远呢。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "……帝国的内战还在持续，\x01",
            "不知道协会的情况如何。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    #C0176
    ChrTalk(
        0xFE,
        "……算了，不想那些了。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "现在还是要把眼前的事情摆在首位……\x01",
            "如果连这都做不到，便没有资格\x01",
            "回首过去或展望未来。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#00000F（哈哈，还是和以前一样严于律己呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 3)
    Jump("loc_3D11")

    label("loc_3C51")


    #C0179
    ChrTalk(
        0xFE,
        (
            "虽说总统已经被拘捕，\x01",
            "但克洛斯贝尔目前的状况仍然十分严峻。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……在旅店休息的那两人\x01",
            "恢复体力之后，\x01",
            "应该也会来帮些忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "这段时期也许会很艰苦……\x01",
            "但越是在这种时候，就越要咬牙坚持。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D11")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A35 end

    def Function_19_3D15(): pass

    label("Function_19_3D15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB4")

    #C0182
    ChrTalk(
        0xFE,
        (
            "不久之前，我尝试翻越\x01",
            "玛因兹连峰，最后以失败告终……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "不过我会继续锻炼腰腿，\x01",
            "无论花费多少年也要将它征服。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "……在此表明决心。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3DFD")

    label("loc_3DB4")


    #C0185
    ChrTalk(
        0xFE,
        (
            "决心已经表过了……\x01",
            "差不多也该回家啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "好想见到久别多时的朋友。\x02",
    )

    CloseMessageWindow()

    label("loc_3DFD")

    TalkEnd(0xFE)
    Return()

    # Function_19_3D15 end

    def Function_20_3E01(): pass

    label("Function_20_3E01")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E33")
    SetScenarioFlags(0x31, 2)

    label("loc_3E33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3E73")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E68")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_3E6E")

    label("loc_3E68")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_3E6E")

    Jump("loc_3E79")

    label("loc_3E73")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_3E79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4120")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3EEA")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3ECA"),
        (SWITCH_DEFAULT, "loc_3EDB"),
    )


    label("loc_3ECA")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3EE5")

    label("loc_3EDB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EE5")

    Jump("loc_411B")

    label("loc_3EEA")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3F1A")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_3F1A")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F44"),
        (1, "loc_4048"),
        (2, "loc_40D9"),
        (SWITCH_DEFAULT, "loc_4111"),
    )


    label("loc_3F44")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3F75")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3F85")

    label("loc_3F75")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3F85")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FDB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FDB")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFE")
    Sound(461, 0, 100, 0)

    label("loc_3FFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_401E")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_402E")

    label("loc_401E")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_402E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_3E79")

    label("loc_4048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_40BA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_407D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4095")

    label("loc_407D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4090")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4095")

    label("loc_4090")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4095")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40D4")

    label("loc_40BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_40CA")
    OP_AF(0xFB)
    Jump("loc_40D4")

    label("loc_40CA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40D4")

    Jump("loc_411B")

    label("loc_40D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40F2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_410C")

    label("loc_40F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4102")
    OP_AF(0xFB)
    Jump("loc_410C")

    label("loc_4102")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_410C")

    Jump("loc_411B")

    label("loc_4111")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_411B")

    Jump("loc_3E79")

    label("loc_4120")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_3E01 end

    def Function_21_412E(): pass

    label("Function_21_412E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4164")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4164")

    Call(0, 6)
    Return()

    # Function_21_412E end

    def Function_22_4168(): pass

    label("Function_22_4168")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4297")
    SetChrName("")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "返回玛因兹的罗伊德一行\x01",
            "向镇长等人说明了事情经过。\x02\x03",

            "不过，未能查明安置炸药、\x01",
            "破坏旧矿山入口大门的犯人，\x01",
            "坑道内的异常情况也无法解释。\x02\x03",

            "之后，众人再次调查了旧矿山大门一带，\x01",
            "确认附近并无可疑人物……\x02\x03",

            "于是，罗伊德等人请求警备队前来巡逻，\x01",
            "随后准备返回克洛斯贝尔市。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4297")

    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("chr/ch23200.itc", 0x1F)
    LoadChrToIndex("chr/ch20100.itc", 0x20)
    LoadChrToIndex("chr/ch30700.itc", 0x21)
    LoadChrToIndex("chr/ch26300.itc", 0x22)
    LoadChrToIndex("chr/ch26200.itc", 0x23)
    LoadChrToIndex("chr/ch23700.itc", 0x24)
    LoadChrToIndex("chr/ch02750.itc", 0x25)
    LoadChrToIndex("chr/ch02751.itc", 0x26)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x9, 0x18)
    OP_49()
    SetChrPos(0x18, -4500, -2000, 18000, 180)
    OP_D5(0x18, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    OP_93(0x18, 0xB4, 0x0)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x1C, 0x23)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0xD, -1200, -2000, 26750, 180)
    SetChrPos(0x1A, 0, -2000, 26400, 180)
    SetChrPos(0x1B, 1200, -2000, 26750, 180)
    SetChrPos(0x8, 1900, 0, 37500, 180)
    SetChrPos(0x1D, -600, -1710, 30570, 180)
    SetChrPos(0xE, -1600, -1370, 31750, 180)
    SetChrPos(0x1C, -300, -1370, 31750, 180)
    SetChrPos(0xB, 600, -1370, 31750, 180)
    SetChrPos(0x19, -2800, -2000, 23750, 30)
    OP_4B(0xD, 0xFF)
    OP_4B(0x1A, 0xFF)
    OP_4B(0x1B, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0x1D, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x1C, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_52(0x19, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 900, -2000, 24000, 0)
    SetChrPos(0x102, -900, -2000, 24000, 0)
    SetChrPos(0x109, -1100, -2000, 22600, 0)
    SetChrPos(0x105, 1100, -2000, 22600, 0)
    SetChrPos(0x104, 0, -2000, 23200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, -550, 25080, 0)
    MoveCamera(306, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0xD, 2, 0, 24)
    BeginChrThread(0x1A, 2, 0, 24)
    BeginChrThread(0x1B, 2, 0, 24)
    PlayBGM("ed7102", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xD, 3, 0, 27)
    BeginChrThread(0x1A, 3, 0, 25)
    BeginChrThread(0x1B, 3, 0, 26)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 29)
    BeginChrThread(0x102, 3, 0, 30)
    BeginChrThread(0x109, 3, 0, 31)
    BeginChrThread(0x105, 3, 0, 32)
    BeginChrThread(0x104, 3, 0, 33)
    BeginChrThread(0x19, 3, 0, 34)
    Sleep(300)
    OP_68(-4540, -350, 17850, 3500)
    Sleep(5000)
    MoveCamera(341, 18, 0, 3500)
    OP_6E(600, 3500)
    SetCameraDistance(16400, 3500)
    OP_6F(0x79)
    Sleep(500)
    Sleep(1000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    BeginChrThread(0x8, 3, 0, 28)
    OP_68(-4540, -350, 17850, 2000)
    MoveCamera(341, 22, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(21360, 2000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x19, 3)
    Sound(461, 0, 100, 0)
    OP_71(0x9, 0x1F, 0x3C, 0x0, 0x0)
    OP_79(0x9)
    Sleep(1500)
    OP_68(-140, -350, 5080, 4000)
    MoveCamera(333, 15, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(21360, 4000)
    Sound(457, 0, 100, 0)
    Sound(494, 0, 60, 0)
    BeginChrThread(0x18, 3, 0, 36)
    OP_71(0x9, 0x3C, 0x5A, 0x0, 0x0)
    BeginChrThread(0x18, 2, 0, 23)
    WaitChrThread(0x18, 2)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    StopSound(457, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_4168 end

    def Function_23_46D8(): pass

    label("Function_23_46D8")

    OP_79(0x9)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    Return()

    # Function_23_46D8 end

    def Function_24_46E8(): pass

    label("Function_24_46E8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4703")
    Sleep(300)
    Jump("loc_4757")

    label("loc_4703")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_471E")
    Sleep(600)
    Jump("loc_4757")

    label("loc_471E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4739")
    Sleep(900)
    Jump("loc_4757")

    label("loc_4739")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4754")
    Sleep(1200)
    Jump("loc_4757")

    label("loc_4754")

    Sleep(1500)

    label("loc_4757")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4782")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_4757")

    label("loc_4782")

    Return()

    # Function_24_46E8 end

    def Function_25_4783(): pass

    label("Function_25_4783")

    Return()

    # Function_25_4783 end

    def Function_26_4784(): pass

    label("Function_26_4784")

    Return()

    # Function_26_4784 end

    def Function_27_4785(): pass

    label("Function_27_4785")

    Return()

    # Function_27_4785 end

    def Function_28_4786(): pass

    label("Function_28_4786")

    OP_9B(0x0, 0xFE, 0x1, 0x2328, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x50, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Return()

    # Function_28_4786 end

    def Function_29_47C4(): pass

    label("Function_29_47C4")

    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x11F8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x384, 0x3E8, 0x0)
    Sleep(600)
    OP_9B(0x0, 0xFE, 0x0, 0x514, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x1A, 500)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_4823():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4823)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_47C4 end

    def Function_30_4847(): pass

    label("Function_30_4847")

    Sleep(2500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x1194, 0x7D0, 0x1)
    TurnDirection(0xFE, 0x1A, 500)
    Sleep(1000)
    OP_93(0xFE, 0xFF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x1130, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(200)

    def lambda_48AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_48AD)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_4847 end

    def Function_31_48D1(): pass

    label("Function_31_48D1")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0xE10, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(200)
    Sound(462, 0, 100, 0)
    OP_71(0x9, 0x1, 0x1E, 0x0, 0x0)
    Sleep(700)

    def lambda_4938():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4938)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_48D1 end

    def Function_32_495C(): pass

    label("Function_32_495C")

    Sleep(800)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x1F4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x3E8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x1A, 500)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(700)

    def lambda_49BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_49BB)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_495C end

    def Function_33_49DF(): pass

    label("Function_33_49DF")

    Sleep(1200)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x9C4, 0xBB8, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_9B(0x1, 0xFE, 0x5A, 0x1F4, 0x3E8, 0x0)
    Sleep(500)
    OP_9B(0x1, 0xFE, 0x10E, 0x6A4, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x13B, 0x4B0, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x1450, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x3E8, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x320, 0xBB8, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x2D, 0x5DC, 0xBB8, 0x0)
    OP_9B(0x0, 0xFE, 0x13B, 0x898, 0xBB8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_4AB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4AB3)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_49DF end

    def Function_34_4AD7(): pass

    label("Function_34_4AD7")

    Sleep(1600)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x19, 0x25)
    OP_93(0xFE, 0x10E, 0x1F4)
    BeginChrThread(0x1E, 1, 0, 35)
    SetChrChipByIndex(0x19, 0x26)
    OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x1388, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x5DC, 0x1388, 0x1)
    SetChrChipByIndex(0x19, 0x25)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0x19, 0x1E)
    Sleep(1700)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    SetChrChipByIndex(0x19, 0x26)
    OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x1770, 0x1)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x19, 0x32, 0x2EE)
    Sound(844, 0, 60, 0)
    OP_9C(0xFE, 0x0, 0x1770, 0xFFFFD8F0, 0x1770, 0x5DC)
    Return()

    # Function_34_4AD7 end

    def Function_35_4B7B(): pass

    label("Function_35_4B7B")

    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Sleep(3700)
    Sound(845, 0, 40, 0)
    Sleep(400)
    Sound(845, 0, 40, 0)
    Return()

    # Function_35_4B7B end

    def Function_36_4BB8(): pass

    label("Function_36_4BB8")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4500, -2000, 18000)
    OP_9F(0x1, -4500, -2000, 16000)
    OP_9F(0x1, -4000, -2000, 12000)
    OP_9F(0x1, -1500, -2000, 6000)
    OP_9F(0x1, 500, -2000, 0)
    OP_9F(0x1, 500, -2000, -12000)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_36_4BB8 end

    def Function_37_4C1A(): pass

    label("Function_37_4C1A")

    OP_68(-43420, -550, 73000, 0)
    MoveCamera(316, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(71020, 0)
    Fade(500)
    OP_68(-10650, -4950, 66450, 7500)
    MoveCamera(305, 21, 0, 7500)
    OP_6E(600, 7500)
    SetCameraDistance(63120, 7500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-14770, -4950, 77970, 0)
    MoveCamera(324, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(69590, 0)
    Fade(500)
    OP_68(-6010, -4950, 47080, 7000)
    MoveCamera(332, 15, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(69590, 7000)
    Sleep(1000)
    PlaceName2(340, 200, "c_plac17", 0x0, 0)
    OP_6F(0x79)
    Return()

    # Function_37_4C1A end

    def Function_38_4CFB(): pass

    label("Function_38_4CFB")

    ClearChrFlags(0xB, 0x80)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -100, -2000, 6950, 0)
    SetChrPos(0x102, 1140, -2000, 6260, 0)
    SetChrPos(0x109, -500, -2000, 5130, 0)
    SetChrPos(0x105, 770, -2000, 4350, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    BeginChrThread(0x101, 3, 0, 39)
    Call(0, 37)
    Fade(500)
    OP_68(490, -550, 19950, 0)
    MoveCamera(335, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15430, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(300)
    OP_93(0x101, 0x87, 0x1F4)
    #Sound(2092, 255, 80, 0)    #voice#Lloyd

    #C0189
    ChrTalk(
        0x101,
        (
            "#00006F#5P呼……\x01",
            "一直步行到了这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    #C0190
    ChrTalk(
        0x102,
        "#00100F#11P诺艾尔小姐、瓦吉先生，你们没事吧？\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    #C0191
    ChrTalk(
        0x109,
        "#10102F#6P嗯，不用担心。\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(150)

    #C0192
    ChrTalk(
        0x105,
        (
            "#10306F#6P我也没问题……\x01",
            "不过支援科还真是特立独行啊。\x02\x03",

            "#10301F老老实实地开车\x01",
            "或乘坐巴士不好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00002F#5P哈哈，步行的话，在巡视同时还能锻炼身体，\x01",
            "这不是一举两得嘛。\x02\x03",

            "#00004F话说回来……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0194
    ChrTalk(
        0x101,
        (
            "#00012F#5P艾莉的体能还真是大有长进啊。\x02\x03",

            "#00000F在最开始的时候，\x01",
            "你走不了几步就会气喘吁吁了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0195
    ChrTalk(
        0x102,
        (
            "#00109F#12P呵呵，多亏某些人\x01",
            "让我得到了锻炼啊。\x02\x03",

            "#00100F那么，接下来要做什么呢？\x01",
            "先去拜访镇长先生如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00004F#5P嗯，赞成。\x02\x03",

            "#00000F从这里一直往前走，\x01",
            "走到头就是镇长家了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 900, -2000, 20280, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x129, 5)
    SetScenarioFlags(0x12A, 5)
    OP_29(0xA1, 0x1, 0x13)
    ClearMapFlags(0x10000000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_38_4CFB end

    def Function_39_5095(): pass

    label("Function_39_5095")

    Sleep(5500)

    def lambda_509D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_509D)

    def lambda_50AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_50AE)

    def lambda_50BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_50BF)

    def lambda_50D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_50D0)
    BeginChrThread(0x101, 0, 0, 40)
    BeginChrThread(0x102, 0, 0, 41)
    BeginChrThread(0x109, 0, 0, 42)
    BeginChrThread(0x105, 0, 0, 43)
    Return()

    # Function_39_5095 end

    def Function_40_50F5(): pass

    label("Function_40_50F5")

    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_40_50F5 end

    def Function_41_5105(): pass

    label("Function_41_5105")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x3714, 0x7D0, 0x0)
    Return()

    # Function_41_5105 end

    def Function_42_5118(): pass

    label("Function_42_5118")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x37DC, 0x7D0, 0x0)
    Return()

    # Function_42_5118 end

    def Function_43_512B(): pass

    label("Function_43_512B")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
    Return()

    # Function_43_512B end

    def Function_44_513E(): pass

    label("Function_44_513E")

    ClearChrFlags(0xB, 0x80)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 3750, -2000, 26000, 270)
    SetChrPos(0x102, 3750, -2000, 26000, 270)
    SetChrPos(0x109, 3750, -2000, 26000, 270)
    SetChrPos(0x105, 3750, -2000, 26000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x18)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x18, 0, -2000, -500, 0)
    OP_D5(0x18, 0x0, 0x1B58, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x101, 3, 0, 45)
    Call(0, 37)
    OP_0D()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    SetCameraDistance(55590, 5500)
    WaitChrThread(0x18, 0)
    OP_6F(0x79)
    OP_68(2740, -550, 25130, 0)
    MoveCamera(335, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14100, 0)
    Fade(500)
    OP_0D()
    Sound(462, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0xF1, 0x10E, 0x1, 0x8)
    OP_79(0x9)
    BeginChrThread(0x101, 0, 0, 48)
    BeginChrThread(0x102, 0, 0, 49)
    BeginChrThread(0x105, 0, 0, 50)
    BeginChrThread(0x109, 0, 0, 51)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_52B5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_52B5)
    Sleep(50)

    def lambda_52C5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_52C5)
    Sleep(50)

    def lambda_52D5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_52D5)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5559")

    #C0197
    ChrTalk(
        0x102,
        (
            "#00104F#5P呵呵……\x01",
            "转眼之间就到了啊。\x02\x03",

            "#00100F和芙兰说的一样，\x01",
            "山道一带的天气已经放晴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#00002F#11P嗯，雨后的景色\x01",
            "真是美丽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x109,
        (
            "#10109F#12P唔……话说回来，\x01",
            "这辆车实在是很棒呢。\x02\x03",

            "#10102F行驶在这种崎岖难行的山道上，\x01",
            "也基本不会摇晃。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#10304F#6P不愧是蔡斯中央工房，\x01",
            "正式销售之后，肯定会大受欢迎的。\x02\x03",

            "#10300F对了，这座矿山镇的镇长\x01",
            "有事情要和我们谈吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        (
            "#00102F#5P嗯，是比克森镇长。\x02\x03",

            "进镇之后一直走，\x01",
            "走到头就是镇长家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，我们走吧。\x02\x03",

            "#00003F（……说起来，在山道途中，\x01",
            "  还有一条通往人偶工房的小路。）\x02\x03",

            "#00008F（虽然玲已经不在工房了……\x01",
            "  但还是想去看看那里的情况呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57BC")

    label("loc_5559")


    #C0203
    ChrTalk(
        0x105,
        (
            "#10305F#6P嘿，这里就是玛因兹啊。\x02\x03",

            "#10302F名字倒是知道，\x01",
            "但我还是第一次来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00006F#11P嗯，如果没有什么特别的事情，\x01",
            "一般也不会来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00100F#5P对了，诺艾尔小姐\x01",
            "应该经常来玛因兹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x109,
        (
            "#10104F#12P嗯，警备队在定期巡逻时\x01",
            "会经过这里。\x02\x03",

            "#10102F说起来，我和特别任务支援科的缘分\x01",
            "总是和玛因兹有关呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#00002F#5P哈哈，听你这么一说，好像确实如此。\x02\x03",

            "#00000F在军犬事件和探索僧院的任务中，\x01",
            "我们都曾联手行动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00106F#5P是、是啊……\x01",
            "（又想起了很糟糕的回忆。）\x02\x03",

            "#00100F那么，接下来要做什么呢？\x01",
            "先去拜访镇长先生如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00004F#11P嗯，赞成。\x02\x03",

            "#00000F从这里一直往前走，\x01",
            "走到头就是镇长家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57BC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 2400, -2000, 25800, 270)
    ClearMapObjFlags(0x9, 0x1000)
    SetScenarioFlags(0x129, 6)
    SetScenarioFlags(0x12A, 5)
    OP_29(0xA1, 0x1, 0x13)
    ClearMapFlags(0x8000000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_44_513E end

    def Function_45_57F5(): pass

    label("Function_45_57F5")

    Sleep(5500)
    BeginChrThread(0x18, 0, 0, 46)
    WaitChrThread(0x18, 0)
    BeginChrThread(0x18, 0, 0, 47)
    BeginChrThread(0x1E, 1, 0, 52)
    Return()

    # Function_45_57F5 end

    def Function_46_580F(): pass

    label("Function_46_580F")

    SetChrPos(0xFE, 0, -1950, -500, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2CEC, 0xFA0, 0x0)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFEB7E0, 0xBB8, 0x1)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF060, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x8)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF830, 0x3E8, 0x1)
    Sleep(300)
    Return()

    # Function_46_580F end

    def Function_47_587E(): pass

    label("Function_47_587E")

    OP_74(0x9, 0xA)
    OP_71(0x9, 0xB4, 0x79, 0x0, 0x20)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF448, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFEC398, 0xBB8, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF060, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF830, 0x3E8, 0x4)
    OP_70(0x9, 0x78)
    Return()

    # Function_47_587E end

    def Function_48_58E7(): pass

    label("Function_48_58E7")


    def lambda_58EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_58EC)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_48_58E7 end

    def Function_49_5925(): pass

    label("Function_49_5925")

    Sleep(1300)

    def lambda_592D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_592D)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_5925 end

    def Function_50_5966(): pass

    label("Function_50_5966")

    Sleep(2600)

    def lambda_596E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_596E)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_50_5966 end

    def Function_51_59A7(): pass

    label("Function_51_59A7")

    Sleep(3900)

    def lambda_59AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_59AF)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0x9, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(600)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x1C)
    Sleep(300)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_51_59A7 end

    def Function_52_5A1A(): pass

    label("Function_52_5A1A")

    Sound(494, 0, 50, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    Sleep(2300)
    Sound(492, 0, 60, 0)
    Return()

    # Function_52_5A1A end

    def Function_53_5A33(): pass

    label("Function_53_5A33")

    ClearChrFlags(0xB, 0x80)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -1870, -2000, 27300, 180)
    SetChrPos(0x102, -1010, -2000, 26220, 270)
    SetChrPos(0x109, -2770, -2000, 26360, 90)
    SetChrPos(0x105, -2130, -2000, 25230, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x11, 0x80)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x2)
    OP_78(0x8, 0x11)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, 0, -1950, -2000, 0)
    OP_D5(0x11, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    BeginChrThread(0x101, 3, 0, 54)
    Call(0, 37)
    WaitChrThread(0x101, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x11, -6320, -1950, 21130, 180)
    OP_93(0x11, 0xB4, 0x0)

    def lambda_5B36():
        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x101, 2, lambda_5B36)

    def lambda_5B48():
        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x102, 2, lambda_5B48)

    def lambda_5B5A():
        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x109, 2, lambda_5B5A)

    def lambda_5B6C():
        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_FFFFABCD")

    QueueWorkItem2(0x105, 2, lambda_5B6C)
    OP_68(-1750, -550, 26120, 0)
    MoveCamera(335, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15940, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x11, 0, 0, 56)
    OP_0D()
    Sleep(1500)
    Sleep(1500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x109, 0x2)

    def lambda_5BD8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5BD8)
    Sleep(50)

    def lambda_5BE8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5BE8)
    Sleep(50)

    def lambda_5BF8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5BF8)
    Sleep(50)

    def lambda_5C08():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5C08)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E9D")

    #C0210
    ChrTalk(
        0x102,
        (
            "#00104F#12P呵呵……\x01",
            "转眼之间就到了啊。\x02\x03",

            "#00100F和芙兰说的一样，\x01",
            "山道一带的天气已经放晴了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00002F#11P嗯，雨后的景色\x01",
            "真是美丽啊。\x02\x03",

            "#00006F话说回来，我们明明有车，\x01",
            "结果却还是习惯性地坐了巴士啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x109,
        (
            "#10109F#5P呵呵，\x01",
            "我很喜欢巴士。\x02\x03",

            "#10102F这种悠哉悠哉的感觉\x01",
            "实在是不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x105,
        (
            "#10304F#6P我平时很少坐巴士，\x01",
            "感觉很新鲜呢。\x02\x03",

            "#10300F对了，这座矿山镇的镇长\x01",
            "有事情要和我们谈吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#00102F#12P嗯，是比克森镇长。\x02\x03",

            "进镇之后一直走，\x01",
            "走到头就是镇长家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00000F#11P嗯，我们走吧。\x02\x03",

            "#00003F（……说起来，在山道途中，\x01",
            "  还有一条通往人偶工房的小路。）\x02\x03",

            "#00008F（虽然玲已经不在工房了……\x01",
            "  但还是想去看看那里的情况呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6102")

    label("loc_5E9D")


    #C0216
    ChrTalk(
        0x105,
        (
            "#10305F#6P嘿，这里就是玛因兹啊。\x02\x03",

            "#10302F名字倒是知道，\x01",
            "但我还是第一次来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00006F#11P嗯，如果没有什么特别的事情，\x01",
            "一般也不会来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00100F#12P对了，诺艾尔小姐\x01",
            "应该经常来玛因兹吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x109,
        (
            "#10104F#5P嗯，警备队在定期巡逻时\x01",
            "会经过这里。\x02\x03",

            "#10102F说起来，我和特别任务支援科的缘分\x01",
            "总是和玛因兹有关呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#00002F#11P哈哈，听你这么一说，好像确实如此。\x02\x03",

            "#00000F在军犬事件和探索僧院的任务中，\x01",
            "我们都曾联手行动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        (
            "#00106F#12P是、是啊……\x01",
            "（又想起了很糟糕的回忆。）\x02\x03",

            "#00100F那么，接下来要做什么呢？\x01",
            "先去拜访镇长先生如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00004F#11P嗯，赞成。\x02\x03",

            "#00000F从这里一直往前走，\x01",
            "走到头就是镇长家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6102")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x2)
    SetChrPos(0x0, 590, -2000, 26270, 0)
    SetScenarioFlags(0x129, 7)
    SetScenarioFlags(0x12A, 5)
    OP_29(0xA1, 0x1, 0x13)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_53_5A33 end

    def Function_54_6141(): pass

    label("Function_54_6141")

    Sleep(5500)
    Sleep(2200)
    Sound(473, 0, 100, 0)
    Sleep(300)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    BeginChrThread(0x11, 0, 0, 55)
    Sleep(2200)
    Sound(467, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 0)
    OP_79(0x8)
    Sleep(300)
    Return()

    # Function_54_6141 end

    def Function_55_6179(): pass

    label("Function_55_6179")

    OP_74(0x8, 0xF)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -850, -1950, 2000, 0)
    OP_9F(0x0, 0xFE)
    OP_93(0xFE, 0x0, 0x0)
    OP_9F(0x1, -3200, -1950, 8000)
    OP_9F(0x1, -5300, -1950, 13000)
    OP_9F(0x1, -6320, -1950, 17000)
    OP_9F(0x1, -6320, -1950, 19630)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x7D0, 0x1)
    OP_71(0x8, 0x5B, 0x78, 0x0, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    Return()

    # Function_55_6179 end

    def Function_56_6220(): pass

    label("Function_56_6220")

    Sound(471, 0, 100, 0)
    OP_74(0x8, 0xF)
    OP_71(0x8, 0x79, 0xB4, 0x0, 0x20)
    SetChrPos(0xFE, -6320, -1950, 21130, 180)
    OP_93(0xFE, 0xB4, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x3E8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0x7D0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xBB8, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x15E, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x1)
    OP_9B(0x1, 0xFE, 0x13B, 0x1770, 0x1388, 0x1)
    ClearMapObjFlags(0x8, 0x1000)
    Return()

    # Function_56_6220 end

    def Function_57_62AF(): pass

    label("Function_57_62AF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31200.itc", 0x1E)
    LoadChrToIndex("chr/ch31300.itc", 0x1F)
    LoadChrToIndex("chr/ch32600.itc", 0x20)
    LoadChrToIndex("apl/ch51441.itc", 0x21)
    SoundLoad(803)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis409.itp")
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetMapObjFrame(0xC, "mark01", 0x0, 0x1)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark01", 0x0, 0x1)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    OP_71(0xE, 0x0, 0x258, 0x0, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    SetChrPos(0x102, -5000000, 0, 0, 0)
    SetChrPos(0x103, -5000000, 0, 0, 0)
    SetChrPos(0x104, -5000000, 0, 0, 0)
    SetChrPos(0x109, -5000000, 0, 0, 0)
    SetChrPos(0x105, -5000000, 0, 0, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x17, -5000000, 0, 0, 0)
    SetChrPos(0x12, -5000000, 0, 0, 0)
    SetChrPos(0x13, -5000000, 0, 0, 0)
    SetChrPos(0x14, -5000000, 0, 0, 0)
    SetChrPos(0x8, -5000000, 0, 0, 0)
    SetChrPos(0x9, -5000000, 0, 0, 0)
    SetChrPos(0xA, -5000000, 0, 0, 0)
    SetChrPos(0xB, -5000000, 0, 0, 0)
    SetChrPos(0xC, -5000000, 0, 0, 0)
    OP_68(-12300, -550, 22120, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(200, -550, 23600, 10000)
    MoveCamera(305, 15, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(20000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x12, -950, 300, 54300, 270)
    SetChrPos(0xA, -2150, 450, 54300, 90)
    SetChrPos(0xC, -2150, 450, 54300, 90)
    SetChrPos(0x8, -2150, 450, 54300, 90)
    SetChrPos(0xB, -2150, 450, 54300, 90)
    SetChrPos(0x9, -2150, 450, 54300, 90)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-1500, 900, 54300, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(650, 600, 54300, 8000)
    SetCameraDistance(20000, 8000)
    OP_0D()
    BeginChrThread(0x12, 1, 0, 58)
    Sleep(1000)
    Sound(105, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    BeginChrThread(0xA, 1, 0, 59)
    Sleep(500)
    BeginChrThread(0xC, 1, 0, 60)
    Sleep(500)
    BeginChrThread(0xB, 1, 0, 62)
    Sleep(750)
    BeginChrThread(0x9, 1, 0, 63)
    Sleep(750)
    BeginChrThread(0x8, 1, 0, 61)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Fade(500)
    OP_64(0xA)
    OP_64(0xC)
    OP_64(0x8)
    OP_64(0xB)
    OP_64(0x9)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x12, -8230, 7110, 64050, 270)
    SetChrPos(0x13, -14750, 7000, 37800, 30)
    SetChrPos(0x14, -5650, 7000, 71150, 180)
    OP_68(-5650, 8000, 71150, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(-15500, 8100, 42800, 7000)
    MoveCamera(300, 20, 0, 7000)
    SetCameraDistance(22000, 7000)

    def lambda_67B6():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_67B6)
    Sleep(3000)
    OP_95(0x13, -13050, 7000, 41450, 2000, 0x0)
    OP_95(0x13, -15450, 7250, 42850, 2000, 0x0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x101, 5750, -2000, 6500, 270)
    SetChrPos(0x102, 5400, -2000, 7700, 225)
    SetChrPos(0x103, 5500, -2000, 5350, 270)
    SetChrPos(0x104, 3700, -2000, 7550, 180)
    SetChrPos(0x109, 5050, -2000, 9000, 225)
    SetChrPos(0x105, 6850, -2000, 7550, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x17, 2900, -2000, 5800, 90)
    OP_68(4370, -900, 6610, 0)
    MoveCamera(301, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 1500)
    OP_0D()
    OP_6F(0x79)

    #C0223
    ChrTalk(
        0x17,
        (
            "#07904F#5P看样子，『赤色星座』\x01",
            "已经撤退了呢。\x02\x03",

            "#07902F这里好像没有什么\x01",
            "遭受掠夺的形迹。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#00004F#12P是吗……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#00102F#12P太好了……\x01",
            "真是不幸中的大幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x104,
        (
            "#00303F#11P在没有必要时，那些家伙\x01",
            "原本便不会发动无用的掠夺。\x02\x03",

            "#00308F但反过来说，一旦情势需要，\x01",
            "他们恐怕什么事情都做得出来……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    def lambda_6A23():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_6A23)
    Sleep(50)

    def lambda_6A33():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A33)
    Sleep(50)

    def lambda_6A43():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6A43)
    Sleep(50)

    def lambda_6A53():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6A53)
    Sleep(50)

    def lambda_6A63():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A63)
    Sleep(50)

    def lambda_6A73():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6A73)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0227
    ChrTalk(
        0x109,
        "#10105F#12P兰迪前辈……？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x17,
        (
            "#07908F#5P你没事吧？\x01",
            "听说你之前\x01",
            "非常乱来。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#00300F#11P哪里，没什么大不了的。\x02\x03",

            "#00306F不过，好不容易才解封的来复枪，\x01",
            "在短时间内又不能用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x105,
        (
            "#10302F#12P被那把威力惊人的\x01",
            "链锯枪损毁了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        (
            "#00206F#6P说起来，谢莉小姐的那把\x01",
            "链锯枪自不必说……\x02\x03",

            "#00201F『赤色星座』的其他猎兵\x01",
            "也都有相当惊人的武装呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(100)

    #C0232
    ChrTalk(
        0x104,
        (
            "#00303F#5P嗯，那都是特意找\x01",
            "专业武器工房打造的……\x02\x03",

            "#00302F算啦，反正只要有基约姆师傅在，\x01",
            "总能想办法把它修理好。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        "#00002F#6P嗯，但愿如此。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#00109F#12P呵呵，回市里以后，\x01",
            "我们就赶快去找他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x17,
        (
            "#07904F#5P……真是太好了。\x02\x03",

            "#07902F你终于可以再次\x01",
            "举起来复枪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(100)

    #C0236
    ChrTalk(
        0x104,
        (
            "#00300F#11P哈哈……虽然稍微晚了一些。\x02\x03",

            "#00309F说起来～我以前还真是\x01",
            "害你很担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x17,
        (
            "#07906F#5P是、是啊……\x01",
            "如果你从一开始就使用来复枪，\x01",
            "现在恐怕仍然是警备队的在籍成员……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_6DE4():
        TurnDirection(0x101, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6DE4)
    Sleep(50)

    def lambda_6DF4():
        TurnDirection(0x102, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6DF4)
    Sleep(50)

    def lambda_6E04():
        TurnDirection(0x103, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6E04)
    Sleep(50)

    def lambda_6E14():
        TurnDirection(0x109, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E14)
    Sleep(50)

    def lambda_6E24():
        TurnDirection(0x105, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E24)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x17, 0x103, 500)
    Sleep(500)
    TurnDirection(0x17, 0x104, 500)
    Sleep(500)
    TurnDirection(0x17, 0x101, 500)

    #C0238
    ChrTalk(
        0x17,
        (
            "#07911F#5P你、你们不要误会啊！\x02\x03",

            "我、我只是在担心……这种散漫随便\x01",
            "的男人是否能在其它岗位上认真尽责！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#00012F#12P（哈哈……）\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        "#00102F#12P（忍不住想笑呢。）\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        (
            "#00204F#6P（兰迪前辈应该也\x01",
            "  察觉到了对方的心意吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_64(0x17)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x17, 0xB4, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x17, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)

    #C0242
    ChrTalk(
        0x17,
        (
            "#07903F#11P咳咳……\x01",
            "我是一分队的米蕾优。\x02\x03",

            "#07902F嗯，辛苦了。\x01",
            "那些家伙现在的行踪……\x02\x03",

            "#07905F#30W……………………………………\x02\x03",

            "#07908F……你说什么？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0243
    ChrTalk(
        0x101,
        "#00005F#12P怎、怎么了？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    Sound(804, 0, 100, 0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x17, 0x101, 500)
    Sleep(150)

    #C0244
    ChrTalk(
        0x17,
        (
            "#07906F#5P……据报告说，\x01",
            "撤退的猎兵们突然消失了。\x02\x03",

            "#07901F只知道他们先从隧道的岔路口\x01",
            "去往遗迹方向了……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        "#00201F#6P『月之僧院』……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#00108F#12P那个……\x01",
            "难道不是逃入遗迹了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x17,
        (
            "#07903F#5P遗迹前的封锁\x01",
            "并没有遭受突破的痕迹。\x02\x03",

            "#07908F他们究竟去了什么地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x109,
        (
            "#10106F#11P……那一带全都是\x01",
            "陡峭的悬崖……\x02\x03",

            "#10101F完全没有其它的\x01",
            "撤离场所……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x105,
        (
            "#10303F#12P唔，那个叫谢莉的孩子\x01",
            "恐怕不能用常识来衡量……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)

    #C0250
    ChrTalk(
        0x104,
        (
            "#00306F#11P我之前就觉得很奇怪。\x02\x03",

            "#00301F那些家伙在玛因兹地区安排的人数……\x01",
            "无论怎么想也都太少了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_73D8():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_73D8)
    Sleep(50)

    def lambda_73E8():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_73E8)
    Sleep(50)

    def lambda_73F8():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_73F8)
    Sleep(50)

    def lambda_7408():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7408)
    Sleep(50)

    def lambda_7418():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7418)
    Sleep(50)

    def lambda_7428():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7428)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0251
    ChrTalk(
        0x101,
        "#00011F#6P什么……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    #C0252
    ChrTalk(
        0x104,
        (
            "#00303F#5P来到克洛斯贝尔的赤色星座成员\x01",
            "多达一百人左右……\x02\x03",

            "但在玛因兹地区的\x01",
            "却只有二十人左右。\x02\x03",

            "#00308F……最重要的是，\x01",
            "西格蒙德·奥兰多……\x02\x03",

            "#00311F那个比谢莉更加可怕的怪物\x01",
            "究竟去了何处……？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00013F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x17,
        "#07907F#5P这、这个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x87, 0x1F4)

    #C0255
    ChrTalk(
        0x103,
        (
            "#00205F#5P啊……\x02\x03",

            "#00207F#4S大家快看那里！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(13800, -900, 940, 2500)

    def lambda_7671():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7671)
    Sleep(20)

    def lambda_7681():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7681)
    Sleep(20)

    def lambda_7691():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_7691)
    Sleep(20)

    def lambda_76A1():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_76A1)
    Sleep(20)

    def lambda_76B1():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_76B1)
    Sleep(20)

    def lambda_76C1():
        OP_93(0x17, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_76C1)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x17, 0)
    Sleep(2000)
    Fade(500)
    CancelBlur(3000)
    OP_68(68650, 0, 20750, 0)
    MoveCamera(90, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(52000, 0)
    MoveCamera(90, 20, 0, 5000)
    SetCameraDistance(50000, 5000)
    OP_7D(0xB4, 0x96, 0x96, 0x0, 0x0)
    OP_11(0x16, 0x0, 0xA, 0x15, 0x34, 0x0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(-1, 280, -1, -1)

    #A0256
    AnonymousTalk(
        0x102,
        "#00107F那、那是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 280, -1, -1)

    #A0257
    AnonymousTalk(
        0x109,
        "#10110F难、难道……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(0, 280, -1, -1)

    #A0258
    AnonymousTalk(
        0x101,
        (
            "#00007F克洛斯贝尔市……\x01",
            "正在燃烧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(52000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_29(0xAA, 0x1, 0x7)
    OP_29(0xAA, 0x4, 0x10)
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E5(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_E0(0x20, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C9(0x0, 0x10)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x25, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x25, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_C9(0x1, 0x10)
    OP_E5(0xB)
    ReplaceBGM("ed7301", -1)
    ReplaceBGM("ed7351", -1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_57_62AF end

    def Function_58_78E2(): pass

    label("Function_58_78E2")

    OP_96(0xFE, 0x28A, 0x0, 0xD41C, 0x3E8, 0x0)
    OP_95(0xFE, 650, 0, 55950, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_58_78E2 end

    def Function_59_7912(): pass

    label("Function_59_7912")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_7921():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7921)
    OP_95(0xFE, 3000, 0, 54800, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_59_7912 end

    def Function_60_7968(): pass

    label("Function_60_7968")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_7977():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7977)
    OP_95(0xFE, 3000, 0, 53800, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_60_7968 end

    def Function_61_79BB(): pass

    label("Function_61_79BB")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_79CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_79CA)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 650, 0, 54950, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_61_79BB end

    def Function_62_7A25(): pass

    label("Function_62_7A25")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_7A34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7A34)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 1150, 0, 51250, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_62_7A25 end

    def Function_63_7A85(): pass

    label("Function_63_7A85")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_7A94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_7A94)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 2400, 0, 52100, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_63_7A85 end

    def Function_64_7AE5(): pass

    label("Function_64_7AE5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50123.itc", 0x1E)
    LoadChrToIndex("apl/ch50124.itc", 0x1F)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x0, 5000000, 0, 0, 0)
    SetChrPos(0x1, 5000000, 0, 0, 0)
    SetChrPos(0x2, 5000000, 0, 0, 0)
    SetChrPos(0x3, 5000000, 0, 0, 0)
    SetChrPos(0x12, -500, -2000, -1500, 180)
    SetChrPos(0x13, 1250, -2000, -1300, 180)
    SetChrPos(0x14, 4450, -2000, 1050, 135)
    SetChrPos(0x15, -2350, -2000, 9550, 270)
    SetChrPos(0x16, 850, -2000, 5500, 180)
    BeginChrThread(0x14, 1, 0, 65)
    BeginChrThread(0x15, 1, 0, 66)
    BeginChrThread(0x16, 1, 0, 67)
    OP_68(1600, 200, -4600, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12000, 0)
    OP_68(3250, 200, 950, 6000)
    MoveCamera(315, 20, 0, 6000)
    SetCameraDistance(15000, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Fade(500)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    SetChrPos(0x14, 400, 0, 52700, 90)
    SetChrPos(0x15, 400, 0, 55350, 90)
    OP_68(-1700, 2150, 54300, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(22000, 0)
    MoveCamera(305, 25, 0, 4000)
    SetCameraDistance(19000, 4000)
    OP_0D()
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t0520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_64_7AE5 end

    def Function_65_7CF3(): pass

    label("Function_65_7CF3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D3F")
    OP_95(0xFE, 4450, -2000, 1050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 6000, -2000, 3050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    Jump("Function_65_7CF3")

    label("loc_7D3F")

    Return()

    # Function_65_7CF3 end

    def Function_66_7D40(): pass

    label("Function_66_7D40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D8C")
    OP_95(0xFE, -1850, -2000, 2250, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, -2350, -2000, 9550, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    Jump("Function_66_7D40")

    label("loc_7D8C")

    Return()

    # Function_66_7D40 end

    def Function_67_7D8D(): pass

    label("Function_67_7D8D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DB1")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(2000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    Jump("Function_67_7D8D")

    label("loc_7DB1")

    Return()

    # Function_67_7D8D end

    def Function_68_7DB2(): pass

    label("Function_68_7DB2")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门牢牢关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_68_7DB2 end

    SaveToFile()

Try(main)
