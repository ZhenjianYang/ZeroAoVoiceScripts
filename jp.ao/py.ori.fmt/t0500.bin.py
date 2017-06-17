from ScenarioHelper import *

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
        0x05,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 60, 0, 4, 0, 5],
    )

    BuildStringList((
        "t0500",                  # 0
        "アミー",                 # 1
        "カルロス",               # 2
        "アレク",                 # 3
        "鉱員ロージー",           # 4
        "キミィ",                 # 5
        "鉱員ガンツ",             # 6
        "鉱員マルロ",             # 7
        "遊撃士ヴェンツェル",     # 8
        "チルル",                 # 9
        "バス",                   # 10
        "警備隊員",               # 11
        "警備隊員",               # 12
        "警備隊員",               # 13
        "警備隊員",               # 14
        "警備隊員",               # 15
        "ミレイユ三尉",           # 16
        "車",                     # 17
        "ツァイト",               # 18
        "ビクセン町長",           # 19
        "アンナ夫人",             # 20
        "鉱員マックス",           # 21
        "鉱山長ホフマン",         # 22
        "SE制御",                 # 23
        "マインツ山道",           # 24
        "マインツ鉱山",           # 25
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

    PlaceName(11.0, 0.0, -23.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-32.0, 0.0, 62.0, 0x0000, 0x0000, "マインツ鉱山")
    PlaceName(-19.75, 0.0, 45.75, 0x0000, 0x0053, "")
    PlaceName(-3.0, 0.0, 49.0, 0x0000, 0x0052, "")
    PlaceName(-4.5, 0.0, 28.600000381469727, 0x0000, 0x0055, "")

    ChipFrameInfo(1344, 0)                                       # 0

    ScpFunction((
        "Function_0_540",          # 00, 0
        "Function_1_5F8",          # 01, 1
        "Function_2_623",          # 02, 2
        "Function_3_64E",          # 03, 3
        "Function_4_681",          # 04, 4
        "Function_5_E0A",          # 05, 5
        "Function_6_1027",         # 06, 6
        "Function_7_11AB",         # 07, 7
        "Function_8_12DE",         # 08, 8
        "Function_9_132F",         # 09, 9
        "Function_10_13C3",        # 0A, 10
        "Function_11_215C",        # 0B, 11
        "Function_12_2EAB",        # 0C, 12
        "Function_13_37F7",        # 0D, 13
        "Function_14_38CB",        # 0E, 14
        "Function_15_3CFA",        # 0F, 15
        "Function_16_3F03",        # 10, 16
        "Function_17_4011",        # 11, 17
        "Function_18_415D",        # 12, 18
        "Function_19_4483",        # 13, 19
        "Function_20_457F",        # 14, 20
        "Function_21_48C2",        # 15, 21
        "Function_22_490E",        # 16, 22
        "Function_23_4EAA",        # 17, 23
        "Function_24_4EBA",        # 18, 24
        "Function_25_4F55",        # 19, 25
        "Function_26_4F56",        # 1A, 26
        "Function_27_4F57",        # 1B, 27
        "Function_28_4F58",        # 1C, 28
        "Function_29_4F96",        # 1D, 29
        "Function_30_5019",        # 1E, 30
        "Function_31_50A3",        # 1F, 31
        "Function_32_512E",        # 20, 32
        "Function_33_51B1",        # 21, 33
        "Function_34_52A9",        # 22, 34
        "Function_35_534D",        # 23, 35
        "Function_36_538A",        # 24, 36
        "Function_37_53EC",        # 25, 37
        "Function_38_54CD",        # 26, 38
        "Function_39_58A2",        # 27, 39
        "Function_40_5902",        # 28, 40
        "Function_41_5912",        # 29, 41
        "Function_42_5925",        # 2A, 42
        "Function_43_5938",        # 2B, 43
        "Function_44_594B",        # 2C, 44
        "Function_45_607F",        # 2D, 45
        "Function_46_6099",        # 2E, 46
        "Function_47_6108",        # 2F, 47
        "Function_48_6171",        # 30, 48
        "Function_49_61AF",        # 31, 49
        "Function_50_61F0",        # 32, 50
        "Function_51_6231",        # 33, 51
        "Function_52_62A4",        # 34, 52
        "Function_53_62BD",        # 35, 53
        "Function_54_6A6C",        # 36, 54
        "Function_55_6AA4",        # 37, 55
        "Function_56_6B4B",        # 38, 56
        "Function_57_6BDA",        # 39, 57
        "Function_58_8355",        # 3A, 58
        "Function_59_8385",        # 3B, 59
        "Function_60_83DB",        # 3C, 60
        "Function_61_842E",        # 3D, 61
        "Function_62_8498",        # 3E, 62
        "Function_63_84F8",        # 3F, 63
        "Function_64_8558",        # 40, 64
        "Function_65_8766",        # 41, 65
        "Function_66_87B3",        # 42, 66
        "Function_67_8800",        # 43, 67
        "Function_68_8825",        # 44, 68
    ))


    def Function_0_540(): pass

    label("Function_0_540")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_580"),
        (1, "loc_58C"),
        (2, "loc_598"),
        (3, "loc_5A4"),
        (4, "loc_5B0"),
        (5, "loc_5BC"),
        (6, "loc_5C8"),
        (SWITCH_DEFAULT, "loc_5D4"),
    )


    label("loc_580")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_58C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_598")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5A4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5B0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5BC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5E0")

    label("loc_5F7")

    Return()

    # Function_0_540 end

    def Function_1_5F8(): pass

    label("Function_1_5F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_622")
    OP_94(0xFE, 0x648C, 0xEA38, 0x727E, 0xF488, 0x3E8)
    Sleep(300)
    Jump("Function_1_5F8")

    label("loc_622")

    Return()

    # Function_1_5F8 end

    def Function_2_623(): pass

    label("Function_2_623")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64D")
    OP_94(0xFE, 0x1C98, 0x8EDA, 0x1F40, 0xB72A, 0x3E8)
    Sleep(300)
    Jump("Function_2_623")

    label("loc_64D")

    Return()

    # Function_2_623 end

    def Function_3_64E(): pass

    label("Function_3_64E")

    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_680")
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)

    label("loc_680")

    Return()

    # Function_3_64E end

    def Function_4_681(): pass

    label("Function_4_681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_694")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_81E")

    label("loc_694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6C2")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18450, -8990, 41770, 270)
    Jump("loc_81E")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6E6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 18450, -8990, 41770, 270)
    Jump("loc_81E")

    label("loc_6E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6F4")
    Jump("loc_81E")

    label("loc_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_702")
    Jump("loc_81E")

    label("loc_702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_71F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_81E")

    label("loc_71F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_72D")
    Jump("loc_81E")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_772")
    SetChrPos(0xA, 1400, 6000, 77780, 0)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 400, 6000, 77780, 0)
    SetChrFlags(0xC, 0x10)
    Jump("loc_81E")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_785")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_81E")

    label("loc_785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C0")
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, 1850, 0, 69850, 270)
    SetChrPos(0xC, 850, 0, 69850, 90)
    Jump("loc_81E")

    label("loc_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_7CE")
    Jump("loc_81E")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7E1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_81E")

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F4")
    SetChrFlags(0xA, 0x80)
    Jump("loc_81E")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_807")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_81E")

    label("loc_807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_815")
    Jump("loc_81E")

    label("loc_815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_81E")

    label("loc_81E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_842")
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_879")

    label("loc_842")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_861")
    Event(0, 44)
    Jump("loc_879")

    label("loc_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_879")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 53)

    label("loc_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_890")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 22)
    Jump("loc_8DB")

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_8A4")
    ClearScenarioFlags(0x22, 1)
    Event(0, 44)
    Jump("loc_8DB")

    label("loc_8A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_8B8")
    ClearScenarioFlags(0x22, 2)
    Event(0, 53)
    Jump("loc_8DB")

    label("loc_8B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_8CC")
    ClearScenarioFlags(0x22, 3)
    Event(0, 57)
    Jump("loc_8DB")

    label("loc_8CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_8DB")
    ClearScenarioFlags(0x22, 4)
    Event(0, 64)

    label("loc_8DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    SetScenarioFlags(0x38, 0)

    label("loc_968")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    SetScenarioFlags(0x38, 1)

    label("loc_97E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    SetScenarioFlags(0x38, 2)

    label("loc_994")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA")
    SetScenarioFlags(0x38, 3)

    label("loc_9AA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C0")
    SetScenarioFlags(0x38, 4)

    label("loc_9C0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D6")
    SetScenarioFlags(0x38, 5)

    label("loc_9D6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9EC")
    SetScenarioFlags(0x38, 6)

    label("loc_9EC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A02")
    SetScenarioFlags(0x38, 7)

    label("loc_A02")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18")
    SetScenarioFlags(0x39, 0)

    label("loc_A18")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")
    SetScenarioFlags(0x39, 1)

    label("loc_A2E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A44")
    SetScenarioFlags(0x39, 2)

    label("loc_A44")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5A")
    SetScenarioFlags(0x39, 3)

    label("loc_A5A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    SetScenarioFlags(0x39, 4)

    label("loc_A70")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A86")
    SetScenarioFlags(0x39, 5)

    label("loc_A86")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9C")
    SetScenarioFlags(0x39, 6)

    label("loc_A9C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB2")
    SetScenarioFlags(0x39, 7)

    label("loc_AB2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC8")
    SetScenarioFlags(0x3A, 0)

    label("loc_AC8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADE")
    SetScenarioFlags(0x3A, 1)

    label("loc_ADE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    SetScenarioFlags(0x3A, 2)

    label("loc_AF4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0A")
    SetScenarioFlags(0x3A, 3)

    label("loc_B0A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B20")
    SetScenarioFlags(0x3A, 4)

    label("loc_B20")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B36")
    SetScenarioFlags(0x3A, 5)

    label("loc_B36")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4C")
    SetScenarioFlags(0x3A, 6)

    label("loc_B4C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B62")
    SetScenarioFlags(0x3A, 7)

    label("loc_B62")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")
    SetScenarioFlags(0x3B, 0)

    label("loc_B78")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8E")
    SetScenarioFlags(0x3B, 1)

    label("loc_B8E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA4")
    SetScenarioFlags(0x3B, 2)

    label("loc_BA4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBA")
    SetScenarioFlags(0x3B, 3)

    label("loc_BBA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD0")
    SetScenarioFlags(0x3B, 4)

    label("loc_BD0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE6")
    SetScenarioFlags(0x3B, 5)

    label("loc_BE6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFC")
    SetScenarioFlags(0x3B, 6)

    label("loc_BFC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12")
    SetScenarioFlags(0x3B, 7)

    label("loc_C12")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C28")
    SetScenarioFlags(0x3D, 5)

    label("loc_C28")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C3E")
    SetScenarioFlags(0x3D, 6)

    label("loc_C3E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C54")
    SetScenarioFlags(0x3D, 7)

    label("loc_C54")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_D7F")

    label("loc_C8F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB2")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_D7F")

    label("loc_CB2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD5")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_D7F")

    label("loc_CD5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF8")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_D7F")

    label("loc_CF8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1B")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_D7F")

    label("loc_D1B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3E")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_D7F")

    label("loc_D3E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D61")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_D7F")

    label("loc_D61")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7F")
    SetScenarioFlags(0x3C, 7)

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D95")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC7")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC7")
    SetChrPos(0x0, 2750, -2000, 25500, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_DFA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFA")
    SetChrPos(0x0, 2750, -2000, 25500, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_E09")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 8)

    label("loc_E09")

    Return()

    # Function_4_681 end

    def Function_5_E0A(): pass

    label("Function_5_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E24")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_E50")

    label("loc_E24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 0)), scpexpr(EXPR_END)), "loc_E3E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x25, 0)
    Jump("loc_E50")

    label("loc_E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_E50")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E50")

    SoundDistance(0x84, 0xFFFFF678, 0x1B4E, 0x15766, 0x2710, 0xC350, 0x64, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE3")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xC8, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_EE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_EFA")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_EFA")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F08")
    Jump("loc_FDF")

    label("loc_F08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_F29")
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jump("loc_FDF")

    label("loc_F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F37")
    Jump("loc_FDF")

    label("loc_F37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F45")
    Jump("loc_FDF")

    label("loc_F45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F53")
    Jump("loc_FDF")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F61")
    Jump("loc_FDF")

    label("loc_F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F6F")
    Jump("loc_FDF")

    label("loc_F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F7D")
    Jump("loc_FDF")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_F8B")
    Jump("loc_FDF")

    label("loc_F8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FAC")
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    Jump("loc_FDF")

    label("loc_FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_FBA")
    Jump("loc_FDF")

    label("loc_FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_FC8")
    Jump("loc_FDF")

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FD6")
    Jump("loc_FDF")

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FDF")

    label("loc_FDF")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1013")
    Jump("loc_1026")

    label("loc_1013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1026")
    ClearMapObjFlags(0x6, 0x10)
    OP_66(0x3, 0x1)

    label("loc_1026")

    Return()

    # Function_5_E0A end

    def Function_6_1027(): pass

    label("Function_6_1027")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EE")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停留所の看板を調べると、\x01",
            "導力バスに乗ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車と同様に、\x01",
            "各地への移動にご活用ください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_10EE")


    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kバス停がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1183")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_11A3")

    label("loc_1183")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_11A3")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1027 end

    def Function_7_11AB(): pass

    label("Function_7_11AB")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_12DA")
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

    def lambda_1291():
        OP_96(0xFE, 0xFFFFE750, 0xFFFFF830, 0x528A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1291)
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

    label("loc_12DA")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_11AB end

    def Function_8_12DE(): pass

    label("Function_8_12DE")

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

    # Function_8_12DE end

    def Function_9_132F(): pass

    label("Function_9_132F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_138A")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_137F")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1385")

    label("loc_137F")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1385")

    Jump("loc_13AE")

    label("loc_138A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13A8")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_13AE")

    label("loc_13A8")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_13AE")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_132F end

    def Function_10_13C3(): pass

    label("Function_10_13C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_154B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B5")

    #C0004
    ChrTalk(
        0x8,
        (
            "な、なんなのかしら。\x01",
            "あの青白く光ってる樹……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "高所にあるマインツから見ても\x01",
            "すっごく大きいのが分かるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "歴史に詳しいおばあちゃんでも\x01",
            "見たことないものだって言うし、\x01",
            "なんだか不安になってきちゃった。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1546")

    label("loc_14B5")


    #C0007
    ChrTalk(
        0x8,
        (
            "あの青白く光ってる樹……\x01",
            "なんなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "歴史に詳しいおばあちゃんでも\x01",
            "見たことないものだって言うし、\x01",
            "なんだか不安になってきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1546")

    Jump("loc_2158")

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_169E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1618")

    #C0009
    ChrTalk(
        0x8,
        (
            "クロスベルの独立が\x01",
            "無効になったってホント？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "レジスタンスの人たちを\x01",
            "捜索に来ていた国防軍が、\x01",
            "すっごい焦って帰ってったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "フフン、いい気味ね。\x01",
            "正義は必ず勝つのよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1699")

    label("loc_1618")


    #C0012
    ChrTalk(
        0x8,
        (
            "レジスタンスの人たちを\x01",
            "捜索に来ていた国防軍が、\x01",
            "すっごい焦って帰ってったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "フフン、いい気味ね。\x01",
            "正義は必ず勝つのよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1699")

    Jump("loc_2158")

    label("loc_169E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A9")

    #C0014
    ChrTalk(
        0x8,
        (
            "マインツでは町全体で\x01",
            "警備隊員たちのレジスタンス活動を\x01",
            "手伝っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "マインツを占領した\x01",
            "猟兵を使ってる大統領なんか、\x01",
            "信用できるわけないわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "……それに、お上に逆らって\x01",
            "自分達の正義を貫き通すなんて、\x01",
            "かっこいいもんね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_184D")

    label("loc_17A9")


    #C0017
    ChrTalk(
        0x8,
        (
            "マインツでは町全体で\x01",
            "警備隊員たちのレジスタンス活動を\x01",
            "手伝っているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "大統領なんか信用できないし……\x01",
            "それに逆らうレジスタンスなんて\x01",
            "かっこいいもんね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184D")

    Jump("loc_2158")

    label("loc_1852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_196E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193A")

    #C0019
    ChrTalk(
        0x8,
        (
            "この間、猟兵たちが\x01",
            "町に現れたときは、\x01",
            "もうダメかと思ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "助けに来てくれた警備隊も\x01",
            "次々とやられちゃって……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "でも、町の人やモノには\x01",
            "ほとんど手を出さなかったの。\x01",
            "何がしたかったのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1969")

    label("loc_193A")


    #C0022
    ChrTalk(
        0x8,
        (
            "あの猟兵たち、\x01",
            "何がしたかったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1969")

    Jump("loc_2158")

    label("loc_196E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_197C")
    Jump("loc_2158")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8F")

    #C0023
    ChrTalk(
        0x8,
        (
            "明後日はクロスベル市で\x01",
            "アルカンシェルの\x01",
            "リニューアル公演よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "私も一回でいいから、\x01",
            "舞台ってものをみてみたいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "それで、観劇が趣味のオジサマと\x01",
            "偶然、席が隣り合って、\x01",
            "話が弾んじゃったりしてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#00000F（動機が不純だなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B07")

    label("loc_1A8F")


    #C0027
    ChrTalk(
        0x8,
        (
            "私も一回でいいから、\x01",
            "舞台ってものをみてみたいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "それで、観劇が趣味のオジサマと\x01",
            "素敵な出会いをしちゃうのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B07")

    Jump("loc_2158")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C19")

    #C0029
    ChrTalk(
        0x8,
        (
            "こないだ、遊撃士さんたちが\x01",
            "北の山岳地帯に出たっていう\x01",
            "魔獣を退治しに来てたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "退治はできたみたいだけど、\x01",
            "なんだかフツーじゃない\x01",
            "おかしな魔獣だったんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "最近そういう魔獣の話を\x01",
            "よく聞くけど……\x01",
            "何か原因があるのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C8A")

    label("loc_1C19")


    #C0032
    ChrTalk(
        0x8,
        (
            "でも、そんな\x01",
            "得体のしれない魔獣を\x01",
            "やっつけちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "遊撃士さんってやっぱり\x01",
            "かっこいいわよねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8A")

    Jump("loc_2158")

    label("loc_1C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEF")

    #C0034
    ChrTalk(
        0x8,
        (
            "町には定期的に、\x01",
            "シスターが来て日曜学校の\x01",
            "授業をしていくんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "たまには若い神父様が\x01",
            "来てくれてもいいと思わない？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "それでね、それでね！\x01",
            "修道服とかも派手にアレンジした\x01",
            "オシャレさんだったりしてね！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#00000Fも、妄想とはいえ\x01",
            "随分な不良神父だなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、案外本当に\x01",
            "そんな神父がいたりしてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E7E")

    label("loc_1DEF")


    #C0039
    ChrTalk(
        0x8,
        (
            "たまには若い神父様が\x01",
            "来てくれてもいいわよねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "修道服とかも派手にアレンジした\x01",
            "オシャレさんだったりしたら、\x01",
            "あたし惚れちゃうかも～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7E")

    Jump("loc_2158")

    label("loc_1E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E91")
    Jump("loc_2158")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1FC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4C")

    #C0041
    ChrTalk(
        0x8,
        (
            "ウチのお兄ちゃん、\x01",
            "鉱山で鉱員として働いてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "前はサボってばっかりだったけど、\x01",
            "なんだか最近は頑張ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        "ふふ、お婆ちゃんも喜んでたわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FC4")

    label("loc_1F4C")


    #C0044
    ChrTalk(
        0x8,
        (
            "ウチのお兄ちゃん、\x01",
            "サボってばっかりだったけど\x01",
            "最近はちゃんと仕事してるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "ふふ、お婆ちゃんも喜んでたわ。\x02",
    )

    CloseMessageWindow()

    label("loc_1FC4")

    Jump("loc_2158")

    label("loc_1FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2158")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20DA")
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0046
    ChrTalk(
        0x8,
        "#5Sひょわっ！？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、僕に何か用かい？\x01",
            "可愛いお嬢さん#8Rフロイライン#。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "（ななななな、なにこのヒト！\x01",
            "  超ドストライクなんですけど！）\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#00000F（うーん、さすがワジ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2158")

    label("loc_20DA")

    TurnDirection(0x8, 0x105, 0)

    #C0050
    ChrTalk(
        0x8,
        (
            "はあ、それにしても\x01",
            "綺麗な顔……㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "（……ってあれ？\x01",
            "  男の子？　女の子？）\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x105,
        "#10300Fフフ、おかしな子だね。\x02",
    )

    CloseMessageWindow()

    label("loc_2158")

    TalkEnd(0xFE)
    Return()

    # Function_10_13C3 end

    def Function_11_215C(): pass

    label("Function_11_215C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_226D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2218")

    #C0053
    ChrTalk(
        0x9,
        "まさかあんな物が現れるなんて……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        "……いや、弱気になってちゃダメだ。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "せっかく鉱山が再開して\x01",
            "皆がやる気になってるんだし、\x01",
            "前向きにいかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2268")

    label("loc_2218")


    #C0056
    ChrTalk(
        0x9,
        (
            "せっかく鉱山が再開して\x01",
            "皆がやる気になってるんだし、\x01",
            "前向きにいかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2268")

    Jump("loc_2EA7")

    label("loc_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_23B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2342")

    #C0057
    ChrTalk(
        0x9,
        (
            "前にあった猟兵たちの\x01",
            "レジスタンス狩り以来、\x01",
            "大規模な作戦は行われてない。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x9,
        (
            "無効宣言が出た以上、\x01",
            "奴らがどう出るかが心配だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "レジスタンスの皆には\x01",
            "気をつけてほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23B2")

    label("loc_2342")


    #C0060
    ChrTalk(
        0x9,
        (
            "無効宣言が出た以上、\x01",
            "猟兵たちがどう出るかが心配だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "レジスタンスの皆には\x01",
            "気をつけてほしいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B2")

    Jump("loc_2EA7")

    label("loc_23B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248A")

    #C0062
    ChrTalk(
        0x9,
        (
            "ミレイユさんたちが\x01",
            "最初にここを訪れたときは、\x01",
            "僕達も警戒したけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "マインツのみんなも、\x01",
            "大統領や国防軍の方針には\x01",
            "疑問を感じていたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        "ここが意地の張りどころだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2502")

    label("loc_248A")


    #C0065
    ChrTalk(
        0x9,
        (
            "ミレイユさんたちと同じく、\x01",
            "マインツのみんなも大統領には\x01",
            "疑問を感じていたからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "ここが意地の張りどころだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_2502")

    Jump("loc_2EA7")

    label("loc_2507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2693")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2608")

    #C0067
    ChrTalk(
        0x9,
        (
            "マインツの占領と街の襲撃は、\x01",
            "独立提唱を撤回させるための\x01",
            "帝国の工作だったという噂だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "何の罪もない僕たちを巻き込んで、\x01",
            "警備隊にも大きな被害を出して……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "……政治の為に人を犠牲にするなんて、\x01",
            "絶対に許しちゃいけないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_268E")

    label("loc_2608")


    #C0070
    ChrTalk(
        0x9,
        (
            "マインツの占領と街の襲撃は、\x01",
            "帝国の工作だったという噂だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "政治の為に人を犠牲にするなんて、\x01",
            "絶対に許しちゃいけないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268E")

    Jump("loc_2EA7")

    label("loc_2693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_26A1")
    Jump("loc_2EA7")

    label("loc_26A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277A")

    #C0072
    ChrTalk(
        0x9,
        (
            "マインツに住んでる僕も、\x01",
            "山道の途中にある工房のことは\x01",
            "よく知らないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "なにせ、あの工房の主は\x01",
            "人里にまったく現れないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "多分、相当偏屈な人が\x01",
            "住んでいるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_27E8")

    label("loc_277A")


    #C0075
    ChrTalk(
        0x9,
        (
            "山道の途中にある工房の主は\x01",
            "人里にまったく現れない。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "多分、相当偏屈な人が\x01",
            "住んでいるんじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E8")

    Jump("loc_2EA7")

    label("loc_27ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_290F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2894")

    #C0077
    ChrTalk(
        0x9,
        (
            "この間、\x01",
            "北の山岳地帯に現れた魔獣……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "少し前に旧鉱山に現れた魔獣と\x01",
            "同じ姿形をしていたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "ふむ……何か関係があるのかな？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_290A")

    label("loc_2894")


    #C0080
    ChrTalk(
        0x9,
        (
            "北の山岳地帯の魔獣と、\x01",
            "少し前に旧鉱山に出た魔獣は\x01",
            "同じ姿形をしていたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        "ふむ……何か関係があるのかな？\x02",
    )

    CloseMessageWindow()

    label("loc_290A")

    Jump("loc_2EA7")

    label("loc_290F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D1")

    #C0082
    ChrTalk(
        0x9,
        (
            "ガンツさん、昨日は\x01",
            "またカジノでスッたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "気晴らしに、鉱員みんなで\x01",
            "大盛り上がりしてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "僕も途中から参加してね。\x01",
            "いや、なかなか楽しかったな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A39")

    label("loc_29D1")


    #C0085
    ChrTalk(
        0x9,
        (
            "昨日は鉱員たちが\x01",
            "大盛り上がりしてたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "僕も途中から参加してね。\x01",
            "いや、なかなか楽しかったな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A39")

    Jump("loc_2EA7")

    label("loc_2A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4B")

    #C0087
    ChrTalk(
        0x9,
        (
            "今朝は街へ七耀石を\x01",
            "運びに行っていてね。\x01",
            "ついでに除幕式も見てきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "オルキスタワーのお披露目には、\x01",
            "みんな、なかなかの盛り上がりを\x01",
            "見せていたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "あれほどの高さからなら、\x01",
            "街を見渡せるだろう。\x01",
            "一度上ってみたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BF3")

    label("loc_2B4B")


    #C0090
    ChrTalk(
        0x9,
        (
            "オルキスタワーのお披露目には、\x01",
            "みんな、なかなかの盛り上がりを\x01",
            "見せていたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "あれほどの高さからなら、\x01",
            "街を見渡せるだろう。\x01",
            "一度上ってみたいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF3")

    Jump("loc_2EA7")

    label("loc_2BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CDA")

    #C0092
    ChrTalk(
        0x9,
        (
            "僕は、この鉱山で\x01",
            "採掘された七耀石を\x01",
            "街へ運んでいるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "山道はカーブが多くて、\x01",
            "積荷を載せた運搬車を\x01",
            "運転するのは大変なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "崖も多いから、なによりも\x01",
            "慎重さが要求されるのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D5B")

    label("loc_2CDA")


    #C0095
    ChrTalk(
        0x9,
        (
            "山道はカーブが多くて、\x01",
            "積荷を載せた運搬車は\x01",
            "左右にふられやすいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "崖も多いから、なによりも\x01",
            "慎重さが要求されるのさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5B")

    Jump("loc_2EA7")

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2F")

    #C0097
    ChrTalk(
        0x9,
        (
            "ガンツさん、最近はとても\x01",
            "楽しそうに仕事をしているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "どうやらあの\x01",
            "教団事件をきっかけに\x01",
            "色々と吹っ切れたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "みんな心配してたけど……\x01",
            "とにかく、よかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EA7")

    label("loc_2E2F")


    #C0100
    ChrTalk(
        0x9,
        (
            "ガンツさん、教団事件をきっかけに\x01",
            "色々と吹っ切れたみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "みんな心配してたけど……\x01",
            "とにかく、よかったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA7")

    TalkEnd(0xFE)
    Return()

    # Function_11_215C end

    def Function_12_2EAB(): pass

    label("Function_12_2EAB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2FA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F37")

    #C0102
    ChrTalk(
        0xA,
        (
            "お父さんや鉱員の皆は、\x01",
            "今日は鉱山に入ってったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "みんな嬉しそうだったな……\x01",
            "えへへ、僕も嬉しいや。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FA3")

    label("loc_2F37")


    #C0104
    ChrTalk(
        0xA,
        (
            "あのでっかい樹が\x01",
            "出てきたのは不安だけど、\x01",
            "鉱山が再開して嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "お父さん達、頑張ってほしいな。\x02",
    )

    CloseMessageWindow()

    label("loc_2FA3")

    Jump("loc_37F3")

    label("loc_2FA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_302B")

    #C0106
    ChrTalk(
        0xA,
        (
            "最近は、たくさんの狼が\x01",
            "レジスタンスの皆を\x01",
            "助けているんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "とっても賢い狼なんだね。\x01",
            "頼りになるな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F3")

    label("loc_302B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C9")

    #C0108
    ChrTalk(
        0xA,
        (
            "こんな状況だから\x01",
            "鉱山も休みになってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "お父さんがお家に居るのは\x01",
            "嬉しいけど……やっぱり、\x01",
            "なんだかつまらなそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3154")

    label("loc_30C9")


    #C0110
    ChrTalk(
        0xA,
        (
            "鉱山が休みになってて、\x01",
            "お父さんはつまらなそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "僕も、お父さんが鉱員として\x01",
            "働いてるのが好きだし……\x01",
            "早く再開するといいなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    Jump("loc_37F3")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3251")

    #C0112
    ChrTalk(
        0xA,
        (
            "あの悪い奴らが来たとき、\x01",
            "鉱員さんたちが町を守るために\x01",
            "立ち向かっていったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "でも、結局かなわなくて……\x01",
            "お父さんが突き飛ばされて、\x01",
            "怪我しちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "大した怪我じゃなかったけど、\x01",
            "すっごく心配したよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32E0")

    label("loc_3251")


    #C0115
    ChrTalk(
        0xA,
        (
            "お父さんたちは、町を守るために\x01",
            "悪い奴と戦ったんだけど……\x01",
            "結局かなわなかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "大した怪我はしなかったけど、\x01",
            "すっごく心配したよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E0")

    Jump("loc_37F3")

    label("loc_32E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32F3")
    Jump("loc_37F3")

    label("loc_32F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3358")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330E")
    Call(0, 13)
    Jump("loc_3353")

    label("loc_330E")


    #C0117
    ChrTalk(
        0xA,
        (
            "あはは、やまびこって\x01",
            "おもしろいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "次はなんて叫ぼうかな。\x02",
    )

    CloseMessageWindow()

    label("loc_3353")

    Jump("loc_37F3")

    label("loc_3358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3447")

    #C0119
    ChrTalk(
        0xA,
        (
            "ロージーさん、最近は全然\x01",
            "お仕事をサボらなくなったんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xA,
        (
            "イヤイヤやってるだけだって\x01",
            "口では言ってたけど……\x01",
            "顔はすっごく楽しそうだったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "僕も、仕事を楽しみながらやれる\x01",
            "立派な鉱員になりたいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3484")

    label("loc_3447")


    #C0122
    ChrTalk(
        0xA,
        (
            "僕も、仕事を楽しみながらやれる\x01",
            "立派な鉱員になりたいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3484")

    Jump("loc_37F3")

    label("loc_3489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354F")

    #C0123
    ChrTalk(
        0xA,
        (
            "今日はここで\x01",
            "日曜学校の授業があったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "いつも来てくれるシスターじゃ\x01",
            "なかったけど、とっても優しくて\x01",
            "丁寧に勉強を教えてくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        "えへへ、また会いたいな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_35D1")

    label("loc_354F")


    #C0126
    ChrTalk(
        0xA,
        (
            "今日はいつも来てくれるシスターじゃ\x01",
            "なかったけど、とっても優しくて\x01",
            "丁寧に勉強を教えてくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xA,
        "えへへ、また会いたいな。\x02",
    )

    CloseMessageWindow()

    label("loc_35D1")

    Jump("loc_37F3")

    label("loc_35D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3677")

    #C0128
    ChrTalk(
        0xA,
        "しゅん……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "昨日、お父さんとお母さんに\x01",
            "すっごく叱られちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xA,
        (
            "鉱山の奥に入ったの、\x01",
            "そんなにいけなかったのかなあ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36C0")

    label("loc_3677")


    #C0131
    ChrTalk(
        0xA,
        (
            "鉱山の奥に入ったの、\x01",
            "そんなにいけなかったのかなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        "しゅん……\x02",
    )

    CloseMessageWindow()

    label("loc_36C0")

    Jump("loc_37F3")

    label("loc_36C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36D3")
    Jump("loc_37F3")

    label("loc_36D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_37F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379A")

    #C0133
    ChrTalk(
        0xA,
        (
            "今日の朝見たら、\x01",
            "町の外にある旧鉱山の\x01",
            "トビラが開いてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "コッソリ入ろうとしたら、\x01",
            "すぐガンツさんに見つかって\x01",
            "怒られちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xA,
        "ちぇ、探検したかったなあ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37F3")

    label("loc_379A")


    #C0136
    ChrTalk(
        0xA,
        (
            "旧鉱山、前から探検して\x01",
            "みたかったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        "怒られちゃったし、仕方ないかな。\x02",
    )

    CloseMessageWindow()

    label("loc_37F3")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EAB end

    def Function_13_37F7(): pass

    label("Function_13_37F7")

    OP_4B(0xA, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0138
    ChrTalk(
        0xA,
        "#4Sやっ、ほー！！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("やまびこ")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……っ……ほー……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0140
    ChrTalk(
        0xC,
        "#4Sおとーちゃんだいすきー！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 30, -1, -1)
    SetChrName("やまびこ")

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……いすきー……すきー……\x07\x00\x02",
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

    # Function_13_37F7 end

    def Function_14_38CB(): pass

    label("Function_14_38CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38DC")
    Jump("loc_3CF6")

    label("loc_38DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3920")

    #C0142
    ChrTalk(
        0xB,
        "はあ………………\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xB,
        "鉱山、再開しねえかなあ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF6")

    label("loc_3920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")

    #C0144
    ChrTalk(
        0xB,
        (
            "独立国ってやつになってから、\x01",
            "前みたいなだらけた生活に\x01",
            "戻っちまった気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "はあああ……鉱員の仕事にも\x01",
            "せっかくやる気出てたのにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3A30")

    label("loc_39CA")


    #C0146
    ChrTalk(
        0xB,
        (
            "鉱員の仕事にも\x01",
            "せっかくやる気出てたのにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "このままだらけた生活に\x01",
            "逆戻りしちまうのかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A30")

    Jump("loc_3CF6")

    label("loc_3A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3A43")
    Jump("loc_3CF6")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A51")
    Jump("loc_3CF6")

    label("loc_3A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A5F")
    Jump("loc_3CF6")

    label("loc_3A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3A6D")
    Jump("loc_3CF6")

    label("loc_3A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3A7B")
    Jump("loc_3CF6")

    label("loc_3A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A89")
    Jump("loc_3CF6")

    label("loc_3A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A97")
    Jump("loc_3CF6")

    label("loc_3A97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3CF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB0")

    #C0148
    ChrTalk(
        0xB,
        (
            "俺、前は時々サボリながら\x01",
            "ダラダラ仕事してたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xB,
        (
            "最近はそうもいかなくて、\x01",
            "本を読む暇もないんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xB,
        (
            "この本……持ってても仕方ないし、\x01",
            "あんたたちにやるよ。\x02",
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2EF, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 1)
    Jump("loc_3CF6")

    label("loc_3BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CAB")

    #C0152
    ChrTalk(
        0xB,
        (
            "オレとしては前みたいに\x01",
            "時々サボりながら\x01",
            "ダラダラやってきたいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "最近、他のみんながハリキってるから\x01",
            "なんだかサボりにくいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xB,
        (
            "そろそろやる気を出さなきゃ\x01",
            "いけない時期なのかもしんねー。\x01",
            "はあ、めんどいぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CF6")

    label("loc_3CAB")


    #C0155
    ChrTalk(
        0xB,
        (
            "……今は別にサボってんじゃないぜ。\x01",
            "ちゃんと休憩もらってダラけてんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF6")

    TalkEnd(0xFE)
    Return()

    # Function_14_38CB end

    def Function_15_3CFA(): pass

    label("Function_15_3CFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3D0B")
    Jump("loc_3EFF")

    label("loc_3D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3D19")
    Jump("loc_3EFF")

    label("loc_3D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D34")
    Call(0, 13)
    Jump("loc_3DA0")

    label("loc_3D34")


    #C0156
    ChrTalk(
        0xC,
        (
            "すごいすごーい、\x01",
            "ちゃんとお声がかえってきた！\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        (
            "あの山のむこうにも、\x01",
            "キミィみたいな子がいるのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA0")

    Jump("loc_3EFF")

    label("loc_3DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DB3")
    Jump("loc_3EFF")

    label("loc_3DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3EDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6B")

    #C0158
    ChrTalk(
        0xC,
        (
            "シスターさんなら、\x01",
            "もう教会に帰っちゃったよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xC,
        (
            "そういえば、帰るときに\x01",
            "向こうの方の空を\x01",
            "気にしてたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xC,
        "うーん、何かあるのかな～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3ED5")

    label("loc_3E6B")


    #C0161
    ChrTalk(
        0xC,
        (
            "シスターさん、\x01",
            "帰るときに向こうの方の空を\x01",
            "気にしてたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xC,
        "うーん、何かあるのかな～。\x02",
    )

    CloseMessageWindow()

    label("loc_3ED5")

    Jump("loc_3EFF")

    label("loc_3EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3EE8")
    Jump("loc_3EFF")

    label("loc_3EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3EF6")
    Jump("loc_3EFF")

    label("loc_3EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3EFF")

    label("loc_3EFF")

    TalkEnd(0xFE)
    Return()

    # Function_15_3CFA end

    def Function_16_3F03(): pass

    label("Function_16_3F03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3F14")
    Jump("loc_400D")

    label("loc_3F14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC4")

    #C0163
    ChrTalk(
        0xD,
        (
            "俺たちも何かしたいけど……\x01",
            "レジスタンスの姉ちゃんたちを\x01",
            "手伝えるわけでもないしなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xD,
        (
            "……やっぱり、鉱員に出来るのは\x01",
            "穴掘りしかねえよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3FFF")

    label("loc_3FC4")


    #C0165
    ChrTalk(
        0xD,
        (
            "……やっぱり、鉱員に出来るのは\x01",
            "穴掘りしかねえよな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FFF")

    Jump("loc_400D")

    label("loc_4004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_400D")

    label("loc_400D")

    TalkEnd(0xFE)
    Return()

    # Function_16_3F03 end

    def Function_17_4011(): pass

    label("Function_17_4011")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4022")
    Jump("loc_4159")

    label("loc_4022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4150")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CC")

    #C0166
    ChrTalk(
        0xE,
        (
            "リュッカちゃんに\x01",
            "酒場を追い出されちゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "レジスタンスのリーダーさんが\x01",
            "ゆっくり休めるようにって事だし、\x01",
            "まあ仕方ないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_414B")

    label("loc_40CC")


    #C0168
    ChrTalk(
        0xE,
        (
            "……それにしても、\x01",
            "こんなに長く鉱山の仕事から\x01",
            "離れたのは初めてだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xE,
        (
            "ここまで物足りないなんて\x01",
            "思ってもみなかったな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_414B")

    Jump("loc_4159")

    label("loc_4150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4159")

    label("loc_4159")

    TalkEnd(0xFE)
    Return()

    # Function_17_4011 end

    def Function_18_415D(): pass

    label("Function_18_415D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43AF")

    #C0170
    ChrTalk(
        0xFE,
        (
            "マインツ鉱山の再開に当たって、\x01",
            "湧いていた危険度の高い魔獣を\x01",
            "退治していてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "《魔導兵》や《幻獣》に比べれば\x01",
            "大したことはなかったが、\x01",
            "１人での魔獣退治は骨が折れた。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#00000Fはは……すごいですね。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00304Fさすが帝国ギルド出身の\x01",
            "腕利き遊撃士ってとこか。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        "フ、俺などまだまだだがな。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "……帝国では内戦の最中だが、\x01",
            "古巣ではどうしているやら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    #C0176
    ChrTalk(
        0xFE,
        "……いや、やめておこう。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "目の前のことを最優先に処理する……\x01",
            "それが出来ない者に、過去を振り返り\x01",
            "未来を望む資格などないのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#00000F（はは、相変わらず厳しい人だな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BC, 3)
    Jump("loc_447F")

    label("loc_43AF")


    #C0179
    ChrTalk(
        0xFE,
        (
            "大統領を拘束したとはいえ、\x01",
            "クロスベルも抜き差しならぬ状況だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "……宿屋で休んでいる彼らも、\x01",
            "体力が戻ったら色々と\x01",
            "手伝ってもらう事になるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "苦しい時かもしれんが……\x01",
            "今こそが踏ん張り所だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447F")

    TalkEnd(0xFE)
    Return()

    # Function_18_415D end

    def Function_19_4483(): pass

    label("Function_19_4483")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4524")

    #C0182
    ChrTalk(
        0xFE,
        (
            "マインツ連峰、\x01",
            "少し前の挑戦は失敗したけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "足腰を鍛えて、何年かかっても\x01",
            "絶対に踏破してみせる。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        "……とりあえず、決意表明。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_457B")

    label("loc_4524")


    #C0185
    ChrTalk(
        0xFE,
        (
            "決意表明も済んだし……\x01",
            "そろそろ家に帰ろうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "久しぶりに、友達に会いたい。\x02",
    )

    CloseMessageWindow()

    label("loc_457B")

    TalkEnd(0xFE)
    Return()

    # Function_19_4483 end

    def Function_20_457F(): pass

    label("Function_20_457F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45B1")
    SetScenarioFlags(0x31, 2)

    label("loc_45B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_45F1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45E6")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_45EC")

    label("loc_45E6")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_45EC")

    Jump("loc_45F7")

    label("loc_45F1")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_45F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_4670")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4650"),
        (SWITCH_DEFAULT, "loc_4661"),
    )


    label("loc_4650")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_466B")

    label("loc_4661")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_466B")

    Jump("loc_48AF")

    label("loc_4670")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_46A4")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_46A4")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_46D8"),
        (1, "loc_47DC"),
        (2, "loc_486D"),
        (SWITCH_DEFAULT, "loc_48A5"),
    )


    label("loc_46D8")

    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_74(0x9, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4709")
    OP_70(0x9, 0x12C)
    OP_71(0x9, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4719")

    label("loc_4709")

    OP_70(0x9, 0xF0)
    OP_71(0x9, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4719")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_476F")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4792")
    Sound(461, 0, 100, 0)

    label("loc_4792")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_47B2")
    OP_70(0x9, 0x14A)
    OP_71(0x9, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_47C2")

    label("loc_47B2")

    OP_70(0x9, 0x10E)
    OP_71(0x9, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_47C2")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x9, "light", 0x1, 0x1)
    OP_70(0x9, 0x0)
    Jump("loc_45F7")

    label("loc_47DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_484E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_4811")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4829")

    label("loc_4811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4824")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4829")

    label("loc_4824")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4829")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4868")

    label("loc_484E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_485E")
    OP_AF(0xFB)
    Jump("loc_4868")

    label("loc_485E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4868")

    Jump("loc_48AF")

    label("loc_486D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4886")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48A0")

    label("loc_4886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4896")
    OP_AF(0xFB)
    Jump("loc_48A0")

    label("loc_4896")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48A0")

    Jump("loc_48AF")

    label("loc_48A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48AF")

    Jump("loc_45F7")

    label("loc_48B4")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_20_457F end

    def Function_21_48C2(): pass

    label("Function_21_48C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_490A")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0187
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力バスは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_490A")

    Call(0, 6)
    Return()

    # Function_21_48C2 end

    def Function_22_490E(): pass

    label("Function_22_490E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A69")
    SetChrName("")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──マインツに戻ったロイドたちは\x01",
            "町長たちに一通りの事情を説明した。\x02\x03",

            "しかし旧鉱山入口の扉を破壊し、\x01",
            "爆薬を仕掛けた犯人は明らかにならず、\x01",
            "坑道内の異常も説明が付かなかった。\x02\x03",

            "その後、もう一度付近を調べて\x01",
            "不審な人物がいないか確認した後……\x02\x03",

            "ロイドたちは警備隊に巡回を要請して\x01",
            "クロスベル市に戻ることにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4A69")

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

    # Function_22_490E end

    def Function_23_4EAA(): pass

    label("Function_23_4EAA")

    OP_79(0x9)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    Return()

    # Function_23_4EAA end

    def Function_24_4EBA(): pass

    label("Function_24_4EBA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4ED5")
    Sleep(300)
    Jump("loc_4F29")

    label("loc_4ED5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EF0")
    Sleep(600)
    Jump("loc_4F29")

    label("loc_4EF0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F0B")
    Sleep(900)
    Jump("loc_4F29")

    label("loc_4F0B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F26")
    Sleep(1200)
    Jump("loc_4F29")

    label("loc_4F26")

    Sleep(1500)

    label("loc_4F29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F54")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_4F29")

    label("loc_4F54")

    Return()

    # Function_24_4EBA end

    def Function_25_4F55(): pass

    label("Function_25_4F55")

    Return()

    # Function_25_4F55 end

    def Function_26_4F56(): pass

    label("Function_26_4F56")

    Return()

    # Function_26_4F56 end

    def Function_27_4F57(): pass

    label("Function_27_4F57")

    Return()

    # Function_27_4F57 end

    def Function_28_4F58(): pass

    label("Function_28_4F58")

    OP_9B(0x0, 0xFE, 0x1, 0x2328, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x50, 0xFA0, 0x7D0, 0x0)
    OP_93(0xFE, 0xB4, 0x0)
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Return()

    # Function_28_4F58 end

    def Function_29_4F96(): pass

    label("Function_29_4F96")

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

    def lambda_4FF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FF5)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_4F96 end

    def Function_30_5019(): pass

    label("Function_30_5019")

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

    def lambda_507F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_507F)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_5019 end

    def Function_31_50A3(): pass

    label("Function_31_50A3")

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

    def lambda_510A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_510A)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_50A3 end

    def Function_32_512E(): pass

    label("Function_32_512E")

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

    def lambda_518D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_518D)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_512E end

    def Function_33_51B1(): pass

    label("Function_33_51B1")

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

    def lambda_5285():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5285)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    Sleep(500)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_51B1 end

    def Function_34_52A9(): pass

    label("Function_34_52A9")

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

    # Function_34_52A9 end

    def Function_35_534D(): pass

    label("Function_35_534D")

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

    # Function_35_534D end

    def Function_36_538A(): pass

    label("Function_36_538A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -4500, -2000, 18000)
    OP_9F(0x1, -4500, -2000, 16000)
    OP_9F(0x1, -4000, -2000, 12000)
    OP_9F(0x1, -1500, -2000, 6000)
    OP_9F(0x1, 500, -2000, 0)
    OP_9F(0x1, 500, -2000, -12000)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_36_538A end

    def Function_37_53EC(): pass

    label("Function_37_53EC")

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

    # Function_37_53EC end

    def Function_38_54CD(): pass

    label("Function_38_54CD")

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
            "#00006F#5Pふう……\x01",
            "結局ここまで歩いて来たか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    #C0190
    ChrTalk(
        0x102,
        "#00100F#11Pノエルさん、ワジ君、大丈夫？\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x2D, 0x1F4)

    #C0191
    ChrTalk(
        0x109,
        "#10102F#6Pええ、心配ご無用です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(150)

    #C0192
    ChrTalk(
        0x105,
        (
            "#10306F#6P僕も大丈夫だけど……\x01",
            "支援課ってホント酔狂だねぇ。\x02\x03",

            "#10301F素直に車とか\x01",
            "バスを使えばいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00002F#5Pはは、トレーニングにもなるし\x01",
            "一石二鳥でいいだろ？\x02\x03",

            "#00004Fそれにしても……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0194
    ChrTalk(
        0x101,
        (
            "#00012F#5Pエリィは本当に体力付いたよな。\x02\x03",

            "#00000F最初は、街道を少し歩いただけで\x01",
            "青息吐息だったのに。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(100)

    #C0195
    ChrTalk(
        0x102,
        (
            "#00109F#12Pふふっ、誰かさんたちのおかげで\x01",
            "鍛えられましたから。\x02\x03",

            "#00100Fそれで、どうするの？\x01",
            "さっそく町長さんを訪ねてみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00004F#5Pああ、そうしよう。\x02\x03",

            "#00000F町長の家は、町に入って\x01",
            "まっすぐ行った突き当りになるな。\x02",
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

    # Function_38_54CD end

    def Function_39_58A2(): pass

    label("Function_39_58A2")

    Sleep(5500)

    def lambda_58AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_58AA)

    def lambda_58BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_58BB)

    def lambda_58CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_58CC)

    def lambda_58DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_58DD)
    BeginChrThread(0x101, 0, 0, 40)
    BeginChrThread(0x102, 0, 0, 41)
    BeginChrThread(0x109, 0, 0, 42)
    BeginChrThread(0x105, 0, 0, 43)
    Return()

    # Function_39_58A2 end

    def Function_40_5902(): pass

    label("Function_40_5902")

    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
    Return()

    # Function_40_5902 end

    def Function_41_5912(): pass

    label("Function_41_5912")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x3714, 0x7D0, 0x0)
    Return()

    # Function_41_5912 end

    def Function_42_5925(): pass

    label("Function_42_5925")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x37DC, 0x7D0, 0x0)
    Return()

    # Function_42_5925 end

    def Function_43_5938(): pass

    label("Function_43_5938")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x38A4, 0x7D0, 0x0)
    Return()

    # Function_43_5938 end

    def Function_44_594B(): pass

    label("Function_44_594B")

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

    def lambda_5ABD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5ABD)
    Sleep(50)

    def lambda_5ACD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5ACD)
    Sleep(50)

    def lambda_5ADD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5ADD)
    Sleep(50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D9D")

    #C0197
    ChrTalk(
        0x102,
        (
            "#00104F#5Pふふ……\x01",
            "あっという間だったわね。\x02\x03",

            "#00100F聞いていた通り、\x01",
            "山道方面は晴れてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#00002F#11Pああ、雨上がりの景色が\x01",
            "綺麗だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x109,
        (
            "#10109F#12Pうーん、でもこの車、\x01",
            "ホント大したものですよ。\x02\x03",

            "#10102F山道みたいな場所でも\x01",
            "あんまり揺れませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#10304F#6PさすがはＺＣＦ。\x01",
            "発売されたら売れそうだね。\x02\x03",

            "#10300Fそれで、この鉱山町の\x01",
            "町長さんが話があるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        (
            "#00102F#5Pええ、ビクセン町長という方よ。\x02\x03",

            "町に入って、まっすぐ行った\x01",
            "突き当たりの家だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、行ってみよう。\x02\x03",

            "#00003F（……そういえば、山道の途中に\x01",
            "  人形工房への道があったか。）\x02\x03",

            "#00008F（もうレンはいないけど……\x01",
            "  ちょっと様子を見に行きたかったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6046")

    label("loc_5D9D")


    #C0203
    ChrTalk(
        0x105,
        (
            "#10305F#6Pへえ、ここがマインツか。\x02\x03",

            "#10302F名前だけは知ってたけど\x01",
            "来るのは初めてかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00006F#11Pまあ、用事でもない限り、\x01",
            "来る機会も無いだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00100F#5Pそういえば、ノエルさんは\x01",
            "結構マインツには来てるのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x109,
        (
            "#10104F#12Pええ、定期パトロールの\x01",
            "コースにもなっていますから。\x02\x03",

            "#10102Fそういえば、特務支援課とは\x01",
            "マインツ方面で縁がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#00002F#5Pはは、そういえばそうだな。\x02\x03",

            "#00000F軍用犬の事件や\x01",
            "僧院の探索で一緒だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00106F#5Pそ、そうね……\x01",
            "（イヤな事を思い出しちゃった。）\x02\x03",

            "#00100Fそれで、どうするの？\x01",
            "さっそく町長さんを訪ねてみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00004F#11Pああ、そうしよう。\x02\x03",

            "#00000F町長の家は、町に入って\x01",
            "まっすぐ行った突き当りになるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6046")

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

    # Function_44_594B end

    def Function_45_607F(): pass

    label("Function_45_607F")

    Sleep(5500)
    BeginChrThread(0x18, 0, 0, 46)
    WaitChrThread(0x18, 0)
    BeginChrThread(0x18, 0, 0, 47)
    BeginChrThread(0x1E, 1, 0, 52)
    Return()

    # Function_45_607F end

    def Function_46_6099(): pass

    label("Function_46_6099")

    SetChrPos(0xFE, 0, -1950, -500, 0)
    OP_9B(0x1, 0xFE, 0x0, 0x2CEC, 0xFA0, 0x0)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFEB7E0, 0xBB8, 0x1)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF060, 0x7D0, 0x1)
    OP_71(0x9, 0x5B, 0x78, 0x1, 0x8)
    OP_9E(0xFE, 0xFFFFEC78, 0x2AF8, 0xFFFFF830, 0x3E8, 0x1)
    Sleep(300)
    Return()

    # Function_46_6099 end

    def Function_47_6108(): pass

    label("Function_47_6108")

    OP_74(0x9, 0xA)
    OP_71(0x9, 0xB4, 0x79, 0x0, 0x20)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF448, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFEC398, 0xBB8, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF060, 0x7D0, 0x4)
    OP_9E(0xFE, 0xFFFFEC78, 0x6590, 0xFFFFF830, 0x3E8, 0x4)
    OP_70(0x9, 0x78)
    Return()

    # Function_47_6108 end

    def Function_48_6171(): pass

    label("Function_48_6171")


    def lambda_6176():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6176)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x145, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_48_6171 end

    def Function_49_61AF(): pass

    label("Function_49_61AF")

    Sleep(1300)

    def lambda_61B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61B7)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x6D6, 0x7D0, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_49_61AF end

    def Function_50_61F0(): pass

    label("Function_50_61F0")

    Sleep(2600)

    def lambda_61F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_61F8)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    OP_93(0xFE, 0xD7, 0x1F4)
    OP_9B(0x1, 0xFE, 0x0, 0x546, 0x7D0, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_50_61F0 end

    def Function_51_6231(): pass

    label("Function_51_6231")

    Sleep(3900)

    def lambda_6239():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6239)
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

    # Function_51_6231 end

    def Function_52_62A4(): pass

    label("Function_52_62A4")

    Sound(494, 0, 50, 0)
    Sleep(2000)
    Sound(459, 0, 100, 0)
    Sleep(2300)
    Sound(492, 0, 60, 0)
    Return()

    # Function_52_62A4 end

    def Function_53_62BD(): pass

    label("Function_53_62BD")

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

    def lambda_63BB():

        label("loc_63BB")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63BB")

    QueueWorkItem2(0x101, 2, lambda_63BB)

    def lambda_63CD():

        label("loc_63CD")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63CD")

    QueueWorkItem2(0x102, 2, lambda_63CD)

    def lambda_63DF():

        label("loc_63DF")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63DF")

    QueueWorkItem2(0x109, 2, lambda_63DF)

    def lambda_63F1():

        label("loc_63F1")

        TurnDirection(0xFE, 0x11, 500)
        Yield()
        Jump("loc_63F1")

    QueueWorkItem2(0x105, 2, lambda_63F1)
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

    def lambda_645D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_645D)
    Sleep(50)

    def lambda_646D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_646D)
    Sleep(50)

    def lambda_647D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_647D)
    Sleep(50)

    def lambda_648D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_648D)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6782")

    #C0210
    ChrTalk(
        0x102,
        (
            "#00104F#12Pふふ……\x01",
            "あっという間だったわね。\x02\x03",

            "#00100F聞いていた通り、\x01",
            "山道方面は晴れてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00002F#11Pああ、雨上がりの景色が\x01",
            "綺麗だったな。\x02\x03",

            "#00006Fしかし、せっかく車があるのに\x01",
            "ついバスに乗っちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x109,
        (
            "#10109F#5Pふふっ。\x01",
            "あたしはバスも好きですよ。\x02\x03",

            "#10102Fのんびりとした感じが\x01",
            "いいんですよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x105,
        (
            "#10304F#6P僕も滅多に乗らないから\x01",
            "わりと新鮮だったかな。\x02\x03",

            "#10300Fそれで、この鉱山町の\x01",
            "町長さんが話があるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#00102F#12Pええ、ビクセン町長という方よ。\x02\x03",

            "町に入って、まっすぐ行った\x01",
            "突き当たりの家だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ、行ってみよう。\x02\x03",

            "#00003F（……そういえば、山道の途中に\x01",
            "  人形工房への道があったか。）\x02\x03",

            "#00008F（もうレンはいないけど……\x01",
            "  ちょっと様子を見に行きたかったな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A2D")

    label("loc_6782")


    #C0216
    ChrTalk(
        0x105,
        (
            "#10305F#6Pへえ、ここがマインツか。\x02\x03",

            "#10302F名前だけは知ってたけど\x01",
            "来るのは初めてかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00006F#11Pまあ、用事でもない限り、\x01",
            "来る機会も無いだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x102,
        (
            "#00100F#12Pそういえば、ノエルさんは\x01",
            "結構マインツには来てるのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x109,
        (
            "#10104F#5Pええ、定期パトロールの\x01",
            "コースにもなっていますから。\x02\x03",

            "#10102Fそういえば、特務支援課とは\x01",
            "マインツ方面で縁がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#00002F#11Pはは、そういえばそうだな。\x02\x03",

            "#00000F軍用犬の事件や\x01",
            "僧院の探索で一緒だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        (
            "#00106F#12Pそ、そうね……\x01",
            "（イヤな事を思い出しちゃった。）\x02\x03",

            "#00100Fそれで、どうするの？\x01",
            "さっそく町長さんを訪ねてみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#00004F#11Pああ、そうしよう。\x02\x03",

            "#00000F町長の家は、町に入って\x01",
            "まっすぐ行った突き当りになるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A2D")

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

    # Function_53_62BD end

    def Function_54_6A6C(): pass

    label("Function_54_6A6C")

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

    # Function_54_6A6C end

    def Function_55_6AA4(): pass

    label("Function_55_6AA4")

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

    # Function_55_6AA4 end

    def Function_56_6B4B(): pass

    label("Function_56_6B4B")

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

    # Function_56_6B4B end

    def Function_57_6BDA(): pass

    label("Function_57_6BDA")

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

    def lambda_70E1():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_70E1)
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
            "#07904F#5Pどうやら《赤い星座》も\x01",
            "一通り撤退したみたいね。\x02\x03",

            "#07902F略奪をした形跡も\x01",
            "特にないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        "#00004F#12Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#00102F#12Pよかった……\x01",
            "不幸中の幸いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x104,
        (
            "#00303F#11P元々、必要がなければ\x01",
            "無用な略奪はしない連中だ。\x02\x03",

            "#00308F逆に必要だったらどんな事でも\x01",
            "やってのけるだろうが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    def lambda_7360():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7360)
    Sleep(50)

    def lambda_7370():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7370)
    Sleep(50)

    def lambda_7380():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7380)
    Sleep(50)

    def lambda_7390():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7390)
    Sleep(50)

    def lambda_73A0():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_73A0)
    Sleep(50)

    def lambda_73B0():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_73B0)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0227
    ChrTalk(
        0x109,
        "#10105F#12Pランディ先輩？\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x17,
        (
            "#07908F#5P大丈夫？\x01",
            "ずいぶん無茶をしたって\x01",
            "聞いたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x104,
        (
            "#00300F#11Pいや、どうってことねぇさ。\x02\x03",

            "#00306Fせっかく封印を解いたライフルは\x01",
            "しばらく使い物にならねぇが。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x105,
        (
            "#10302F#12Pあの凄いチェーンソーに\x01",
            "ガリガリやられちゃってたしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x103,
        (
            "#00206F#6Pしかし、シャーリィさんの\x01",
            "チェーンソーライフルといい……\x02\x03",

            "#00201F《赤い星座》の猟兵というのは\x01",
            "とんでもない装備を持っていますね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)
    Sleep(100)

    #C0232
    ChrTalk(
        0x104,
        (
            "#00303F#5Pああ、専門の武器工房に\x01",
            "わざわざ依頼してるんだが……\x02\x03",

            "#00302Fま、ギヨームの親方だったら\x01",
            "何とか修理できんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        "#00002F#6Pああ、そうするといい。\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#00109F#12Pふふ、街に戻ったら\x01",
            "早速寄ってみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x17,
        (
            "#07904F#5P……でも良かった。\x02\x03",

            "#07902Fまたライフルを\x01",
            "使えるようになったのね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xB4, 0x1F4)
    Sleep(100)

    #C0236
    ChrTalk(
        0x104,
        (
            "#00300F#11Pはは……遅まきながらだがな。\x02\x03",

            "#00309Fいや～、お前さんにも\x01",
            "随分心配をかけちまったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x17,
        (
            "#07906F#5Pそ、そうよ……\x01",
            "最初からライフルを使えていれば\x01",
            "今も警備隊に在籍したままで……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_7797():
        TurnDirection(0x101, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7797)
    Sleep(50)

    def lambda_77A7():
        TurnDirection(0x102, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_77A7)
    Sleep(50)

    def lambda_77B7():
        TurnDirection(0x103, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_77B7)
    Sleep(50)

    def lambda_77C7():
        TurnDirection(0x109, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_77C7)
    Sleep(50)

    def lambda_77D7():
        TurnDirection(0x105, 0x17, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_77D7)
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
            "#07911F#5Pち、違うんですからね！？\x02\x03",

            "その、このチャランポランな男が\x01",
            "他でちゃんとやれるのかなって！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#00012F#12P（はは……）\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        "#00102F#12P（何だか微笑ましいわね。）\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x103,
        (
            "#00204F#6P（ランディさんも気付いては\x01",
            "  いるんでしょうけど……）\x02",
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
            "#07903F#11Pコホン……\x01",
            "０１方面隊、ミレイユです。\x02\x03",

            "#07902Fああ、ご苦労様。\x01",
            "それで連中の足取りは……\x02\x03",

            "#07905F#30W……………………………………\x02\x03",

            "#07908F……何ですって？\x02",
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
        "#00005F#12Pど、どうしたんですか？\x02",
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
            "#07906F#5P……撤退した猟兵たちが\x01",
            "突如消えてしまったらしいわ。\x02\x03",

            "#07901Fトンネル道の分かれ道から\x01",
            "遺跡方面へ抜けたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        "#00201F#6P《月の僧院》……\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#00108F#12Pその……\x01",
            "遺跡に逃げ込んだのではなく？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x17,
        (
            "#07903F#5Pいえ、遺跡前の封鎖を\x01",
            "突破した形跡はなかったそうよ。\x02\x03",

            "#07908F一体どこに……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x109,
        (
            "#10106F#11P……あの辺りは\x01",
            "切り立った崖ばかりですし……\x02\x03",

            "#10101F他に撤退できる場所なんて\x01",
            "どこにも無いはずなのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x105,
        (
            "#10303F#12Pフム、あのシャーリィって子に\x01",
            "常識は通用しなさそうだけど……\x02",
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
            "#00306F#11P──おかしいとは思ったんだ。\x02\x03",

            "#00301Fマインツ方面にいた連中だが……\x01",
            "どう考えても数が少なすぎる。\x02",
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

    def lambda_7E13():
        TurnDirection(0x17, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_7E13)
    Sleep(50)

    def lambda_7E23():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E23)
    Sleep(50)

    def lambda_7E33():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7E33)
    Sleep(50)

    def lambda_7E43():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_7E43)
    Sleep(50)

    def lambda_7E53():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7E53)
    Sleep(50)

    def lambda_7E63():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7E63)
    WaitChrThread(0x17, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0251
    ChrTalk(
        0x101,
        "#00011F#6Pなに……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    #C0252
    ChrTalk(
        0x104,
        (
            "#00303F#5Pクロスベルに来ていたのは\x01",
            "１００人前後の大所帯……\x02\x03",

            "だが、マインツ方面にいたのは\x01",
            "せいぜい２０人くらいだ。\x02\x03",

            "#00308F……何よりも\x01",
            "シグムント・オルランド──\x02\x03",

            "#00311Fシャーリィ以上のあの化物は\x01",
            "どこに行きやがったんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00013F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x17,
        "#07907F#5Pそ、それって……\x02",
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
            "#00205F#5Pあ……\x02\x03",

            "#00207F#4S──皆さん、あれを！\x02",
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

    def lambda_80D8():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80D8)
    Sleep(20)

    def lambda_80E8():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80E8)
    Sleep(20)

    def lambda_80F8():
        OP_93(0x104, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_80F8)
    Sleep(20)

    def lambda_8108():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8108)
    Sleep(20)

    def lambda_8118():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8118)
    Sleep(20)

    def lambda_8128():
        OP_93(0x17, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_8128)
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
        "#00107Fあ、あれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(280, 280, -1, -1)

    #A0257
    AnonymousTalk(
        0x109,
        "#10110Fま、まさか……！\x02",
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
            "#00007Fクロスベル市が──\x01",
            "燃えているのか！？\x02",
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

    # Function_57_6BDA end

    def Function_58_8355(): pass

    label("Function_58_8355")

    OP_96(0xFE, 0x28A, 0x0, 0xD41C, 0x3E8, 0x0)
    OP_95(0xFE, 650, 0, 55950, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_58_8355 end

    def Function_59_8385(): pass

    label("Function_59_8385")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8394():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8394)
    OP_95(0xFE, 3000, 0, 54800, 3000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_59_8385 end

    def Function_60_83DB(): pass

    label("Function_60_83DB")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_83EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_83EA)
    OP_95(0xFE, 3000, 0, 53800, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_60_83DB end

    def Function_61_842E(): pass

    label("Function_61_842E")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_843D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_843D)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 650, 0, 54950, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_61_842E end

    def Function_62_8498(): pass

    label("Function_62_8498")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_84A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_84A7)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 1150, 0, 51250, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_62_8498 end

    def Function_63_84F8(): pass

    label("Function_63_84F8")

    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x40)

    def lambda_8507():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_8507)
    OP_95(0xFE, 650, 0, 54300, 2000, 0x0)
    OP_95(0xFE, 2400, 0, 52100, 2000, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_63_84F8 end

    def Function_64_8558(): pass

    label("Function_64_8558")

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

    # Function_64_8558 end

    def Function_65_8766(): pass

    label("Function_65_8766")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87B2")
    OP_95(0xFE, 4450, -2000, 1050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, 6000, -2000, 3050, 2000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1500)
    Jump("Function_65_8766")

    label("loc_87B2")

    Return()

    # Function_65_8766 end

    def Function_66_87B3(): pass

    label("Function_66_87B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87FF")
    OP_95(0xFE, -1850, -2000, 2250, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    OP_95(0xFE, -2350, -2000, 9550, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1500)
    Jump("Function_66_87B3")

    label("loc_87FF")

    Return()

    # Function_66_87B3 end

    def Function_67_8800(): pass

    label("Function_67_8800")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8824")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(2000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    Jump("Function_67_8800")

    label("loc_8824")

    Return()

    # Function_67_8800 end

    def Function_68_8825(): pass

    label("Function_68_8825")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_68_8825 end

    SaveToFile()

Try(main)
