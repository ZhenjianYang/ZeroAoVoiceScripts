from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2000.bin",                # FileName
        "r2000",                    # MapName
        "r2000",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2000", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x11,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 1, 0, 2],
    )

    BuildStringList((
        "r2000",                  # 0
        "バス",                   # 1
        "シスター・リース",       # 2
        "車",                     # 3
        "鉄鋼ドリュー",           # 4
        "SE制御",                 # 5
        "br2000",                 # 6
        "クロスベル市方面",       # 7
        "クロスベル大聖堂方面",   # 8
        "鉱山町マインツ方面",     # 9
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch76050.itc",               # 10
        "monster/ch76051.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-22079,  -2000,   42080,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 19,  14.149999618530273,    30.399999618530273,    -1.0,                  729.0,                 [0.288675457239151,    -0.027777668088674545, 0.0,                   0.0,                   0.16666600108146667,   0.04811257869005203,   -0.0,                  0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   0.0,                   -9.15140438079834,     -1.069568395614624,    0.19999998807907104,   1.0])

    DeclActor(11200,   0,       16200,   1500,    11200,   1500,    16200,   0x007C, 0,  9,  0x0000)
    DeclActor(870,     0,       19400,   1500,    -90,     2000,    19400,   0x007C, 0,  8,  0x0000)
    DeclActor(-1120,   0,       19360,   1500,    -1120,   2000,    19360,   0x007C, 0,  8,  0x0000)
    DeclActor(4200,    0,       36290,   2500,    4200,    1700,    36290,   0x007C, 0,  26, 0x0000)

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "クロスベル大聖堂方面")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "鉱山町マインツ方面")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")

    ChipFrameInfo(1096, 0)                                       # 0

    ScpFunction((
        "Function_0_448",          # 00, 0
        "Function_1_467",          # 01, 1
        "Function_2_F9D",          # 02, 2
        "Function_3_126B",         # 03, 3
        "Function_4_126F",         # 04, 4
        "Function_5_1450",         # 05, 5
        "Function_6_1584",         # 06, 6
        "Function_7_15D5",         # 07, 7
        "Function_8_1669",         # 08, 8
        "Function_9_1A1E",         # 09, 9
        "Function_10_1BF4",        # 0A, 10
        "Function_11_1D40",        # 0B, 11
        "Function_12_322E",        # 0C, 12
        "Function_13_32BE",        # 0D, 13
        "Function_14_32EF",        # 0E, 14
        "Function_15_3320",        # 0F, 15
        "Function_16_3351",        # 10, 16
        "Function_17_3382",        # 11, 17
        "Function_18_33B2",        # 12, 18
        "Function_19_33D7",        # 13, 19
        "Function_20_3C8D",        # 14, 20
        "Function_21_3D42",        # 15, 21
        "Function_22_40C2",        # 16, 22
        "Function_23_4369",        # 17, 23
        "Function_24_4A3C",        # 18, 24
        "Function_25_4D64",        # 19, 25
        "Function_26_4DBA",        # 1A, 26
    ))


    def Function_0_448(): pass

    label("Function_0_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_466")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_448")

    label("loc_466")

    Return()

    # Function_0_448 end

    def Function_1_467(): pass

    label("Function_1_467")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_4A5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A5")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x0, 2)

    label("loc_4A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_949")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_532")
    SetScenarioFlags(0x38, 0)

    label("loc_532")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548")
    SetScenarioFlags(0x38, 1)

    label("loc_548")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E")
    SetScenarioFlags(0x38, 2)

    label("loc_55E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_574")
    SetScenarioFlags(0x38, 3)

    label("loc_574")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    SetScenarioFlags(0x38, 4)

    label("loc_58A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A0")
    SetScenarioFlags(0x38, 5)

    label("loc_5A0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B6")
    SetScenarioFlags(0x38, 6)

    label("loc_5B6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    SetScenarioFlags(0x38, 7)

    label("loc_5CC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E2")
    SetScenarioFlags(0x39, 0)

    label("loc_5E2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F8")
    SetScenarioFlags(0x39, 1)

    label("loc_5F8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60E")
    SetScenarioFlags(0x39, 2)

    label("loc_60E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624")
    SetScenarioFlags(0x39, 3)

    label("loc_624")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63A")
    SetScenarioFlags(0x39, 4)

    label("loc_63A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_650")
    SetScenarioFlags(0x39, 5)

    label("loc_650")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_666")
    SetScenarioFlags(0x39, 6)

    label("loc_666")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C")
    SetScenarioFlags(0x39, 7)

    label("loc_67C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_692")
    SetScenarioFlags(0x3A, 0)

    label("loc_692")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8")
    SetScenarioFlags(0x3A, 1)

    label("loc_6A8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    SetScenarioFlags(0x3A, 2)

    label("loc_6BE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D4")
    SetScenarioFlags(0x3A, 3)

    label("loc_6D4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA")
    SetScenarioFlags(0x3A, 4)

    label("loc_6EA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_700")
    SetScenarioFlags(0x3A, 5)

    label("loc_700")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_716")
    SetScenarioFlags(0x3A, 6)

    label("loc_716")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72C")
    SetScenarioFlags(0x3A, 7)

    label("loc_72C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_742")
    SetScenarioFlags(0x3B, 0)

    label("loc_742")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_758")
    SetScenarioFlags(0x3B, 1)

    label("loc_758")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76E")
    SetScenarioFlags(0x3B, 2)

    label("loc_76E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_784")
    SetScenarioFlags(0x3B, 3)

    label("loc_784")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A")
    SetScenarioFlags(0x3B, 4)

    label("loc_79A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B0")
    SetScenarioFlags(0x3B, 5)

    label("loc_7B0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C6")
    SetScenarioFlags(0x3B, 6)

    label("loc_7C6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DC")
    SetScenarioFlags(0x3B, 7)

    label("loc_7DC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F2")
    SetScenarioFlags(0x3D, 5)

    label("loc_7F2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_808")
    SetScenarioFlags(0x3D, 6)

    label("loc_808")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81E")
    SetScenarioFlags(0x3D, 7)

    label("loc_81E")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_859")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_949")

    label("loc_859")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_949")

    label("loc_87C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_949")

    label("loc_89F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_949")

    label("loc_8C2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_949")

    label("loc_8E5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_949")

    label("loc_908")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_949")

    label("loc_92B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_949")
    SetScenarioFlags(0x3C, 7)

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95F")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_991")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    SetChrPos(0x0, 1950, 0, 20570, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 7)

    label("loc_991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_9C4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C4")
    SetChrPos(0x0, -1120, 0, 19360, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_9C4")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_A83")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 6)

    label("loc_A83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F39")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B22")
    SetScenarioFlags(0x38, 0)

    label("loc_B22")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B38")
    SetScenarioFlags(0x38, 1)

    label("loc_B38")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4E")
    SetScenarioFlags(0x38, 2)

    label("loc_B4E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B64")
    SetScenarioFlags(0x38, 3)

    label("loc_B64")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7A")
    SetScenarioFlags(0x38, 4)

    label("loc_B7A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B90")
    SetScenarioFlags(0x38, 5)

    label("loc_B90")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA6")
    SetScenarioFlags(0x38, 6)

    label("loc_BA6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBC")
    SetScenarioFlags(0x38, 7)

    label("loc_BBC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD2")
    SetScenarioFlags(0x39, 0)

    label("loc_BD2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE8")
    SetScenarioFlags(0x39, 1)

    label("loc_BE8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFE")
    SetScenarioFlags(0x39, 2)

    label("loc_BFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C14")
    SetScenarioFlags(0x39, 3)

    label("loc_C14")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2A")
    SetScenarioFlags(0x39, 4)

    label("loc_C2A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C40")
    SetScenarioFlags(0x39, 5)

    label("loc_C40")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C56")
    SetScenarioFlags(0x39, 6)

    label("loc_C56")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6C")
    SetScenarioFlags(0x39, 7)

    label("loc_C6C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C82")
    SetScenarioFlags(0x3A, 0)

    label("loc_C82")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C98")
    SetScenarioFlags(0x3A, 1)

    label("loc_C98")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAE")
    SetScenarioFlags(0x3A, 2)

    label("loc_CAE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC4")
    SetScenarioFlags(0x3A, 3)

    label("loc_CC4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA")
    SetScenarioFlags(0x3A, 4)

    label("loc_CDA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF0")
    SetScenarioFlags(0x3A, 5)

    label("loc_CF0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D06")
    SetScenarioFlags(0x3A, 6)

    label("loc_D06")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1C")
    SetScenarioFlags(0x3A, 7)

    label("loc_D1C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")
    SetScenarioFlags(0x3B, 0)

    label("loc_D32")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D48")
    SetScenarioFlags(0x3B, 1)

    label("loc_D48")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5E")
    SetScenarioFlags(0x3B, 2)

    label("loc_D5E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D74")
    SetScenarioFlags(0x3B, 3)

    label("loc_D74")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8A")
    SetScenarioFlags(0x3B, 4)

    label("loc_D8A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA0")
    SetScenarioFlags(0x3B, 5)

    label("loc_DA0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB6")
    SetScenarioFlags(0x3B, 6)

    label("loc_DB6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCC")
    SetScenarioFlags(0x3B, 7)

    label("loc_DCC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE2")
    SetScenarioFlags(0x3D, 5)

    label("loc_DE2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF8")
    SetScenarioFlags(0x3D, 6)

    label("loc_DF8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0E")
    SetScenarioFlags(0x3D, 7)

    label("loc_E0E")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E49")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_F39")

    label("loc_E49")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E6C")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_F39")

    label("loc_E6C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8F")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_F39")

    label("loc_E8F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB2")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_F39")

    label("loc_EB2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED5")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_F39")

    label("loc_ED5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF8")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_F39")

    label("loc_EF8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1B")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_F39")

    label("loc_F1B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F39")
    SetScenarioFlags(0x3C, 7)

    label("loc_F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F4D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 11)
    Jump("loc_F70")

    label("loc_F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F5E")
    ClearScenarioFlags(0x22, 1)
    Jump("loc_F70")

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F70")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 23)

    label("loc_F70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9C")
    SetMapFlags(0x10000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")
    Event(0, 22)
    Jump("loc_F9C")

    label("loc_F99")

    Event(0, 21)

    label("loc_F9C")

    Return()

    # Function_1_467 end

    def Function_2_F9D(): pass

    label("Function_2_F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FB7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_FC9")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_FC9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FE8")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)

    label("loc_FE8")

    MiniGame(0x2F, 0x1, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1096")
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    SetChrPos(0xA, -1090, 0, 19490, 350)
    OP_D5(0xA, 0x0, 0x55730, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)

    label("loc_1096")

    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B9")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_10B9")

    OP_10(0x4, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D3")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x1)

    label("loc_10D3")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EB")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_10EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10FE")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_10FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1111")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1124")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_1124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1137")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_1137")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_114A")
    OP_1B(0x2, 0x0, 0x18)

    label("loc_114A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_115D")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_115D")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0x3, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1216")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_125E")
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    Jump("loc_126A")

    label("loc_125E")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)

    label("loc_126A")

    Return()

    # Function_2_F9D end

    def Function_3_126B(): pass

    label("Function_3_126B")

    Call(1, 6)
    Return()

    # Function_3_126B end

    def Function_4_126F(): pass

    label("Function_4_126F")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
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

    label("loc_1336")


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
            "鉱山町マインツ\x01",              # 0
            "停留所（人形工房付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E9")
    SetScenarioFlags(0x22, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_13F2")

    label("loc_13E9")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_13F2")

    Jump("loc_1448")

    label("loc_13F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1448")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_143F")
    SetScenarioFlags(0x22, 1)
    SetScenarioFlags(0x25, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1448")

    label("loc_143F")

    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_1448")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_4_126F end

    def Function_5_1450(): pass

    label("Function_5_1450")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1580")
    Fade(500)
    OP_68(10010, 600, 21560, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(23500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, 10190, 0, 16230, 0)
    SetChrPos(0x1, 9210, 0, 16200, 0)
    SetChrPos(0x2, 8170, 0, 16290, 0)
    SetChrPos(0x3, 7240, 0, 16350, 0)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x8)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -40, 0, 30670, 105)
    OP_D5(0x8, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_1536():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1536)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_1580")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_5_1450 end

    def Function_6_1584(): pass

    label("Function_6_1584")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, 10030, 0, 16580, 0)
    OP_31(0x1)
    OP_68(10030, 600, 16580, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    EventEnd(0x5)
    Return()

    # Function_6_1584 end

    def Function_7_15D5(): pass

    label("Function_7_15D5")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1630")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1625")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_162B")

    label("loc_1625")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_162B")

    Jump("loc_1654")

    label("loc_1630")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_164E")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1654")

    label("loc_164E")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1654")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_15D5 end

    def Function_8_1669(): pass

    label("Function_8_1669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16DB")
    TalkBegin(0xFF)

    #C0004
    ChrTalk(
        0x101,
        (
            "#00000Fキーア、こいつを見たら\x01",
            "驚くだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#00100Fふふ、早く迎えに行きましょう。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_16DB")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_170D")
    SetScenarioFlags(0x31, 2)

    label("loc_170D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_174D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1742")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_1748")

    label("loc_1742")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_1748")

    Jump("loc_1753")

    label("loc_174D")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_1753")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_17CC")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_17AC"),
        (SWITCH_DEFAULT, "loc_17BD"),
    )


    label("loc_17AC")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_17C7")

    label("loc_17BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C7")

    Jump("loc_1A0B")

    label("loc_17CC")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1800")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_1800")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1834"),
        (1, "loc_1938"),
        (2, "loc_19C9"),
        (SWITCH_DEFAULT, "loc_1A01"),
    )


    label("loc_1834")

    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1865")
    OP_70(0x1, 0x12C)
    OP_71(0x1, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_1875")

    label("loc_1865")

    OP_70(0x1, 0xF0)
    OP_71(0x1, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_1875")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18CB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18CB")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18EE")
    Sound(461, 0, 100, 0)

    label("loc_18EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_190E")
    OP_70(0x1, 0x14A)
    OP_71(0x1, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_191E")

    label("loc_190E")

    OP_70(0x1, 0x10E)
    OP_71(0x1, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_191E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x1, "light", 0x1, 0x1)
    OP_70(0x1, 0x0)
    Jump("loc_1753")

    label("loc_1938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_19AA")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_196D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1985")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1980")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1985")

    label("loc_1980")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1985")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19C4")

    label("loc_19AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19BA")
    OP_AF(0xFB)
    Jump("loc_19C4")

    label("loc_19BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19C4")

    Jump("loc_1A0B")

    label("loc_19C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19FC")

    label("loc_19E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19F2")
    OP_AF(0xFB)
    Jump("loc_19FC")

    label("loc_19F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19FC")

    Jump("loc_1A0B")

    label("loc_1A01")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A0B")

    Jump("loc_1753")

    label("loc_1A10")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_8_1669 end

    def Function_9_1A1E(): pass

    label("Function_9_1A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A30")
    Call(0, 10)
    Return()

    label("loc_1A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A65")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A77")
    Call(0, 10)
    Return()

    label("loc_1A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AE5")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00000F今はとにかく、\x01",
            "事故関連の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B32")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0009
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

    label("loc_1B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BA8")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x101,
        (
            "#00001Fマインツ方面に用事はない。\x01",
            "バスを待つ必要はないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1BF0")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0012
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

    label("loc_1BF0")

    Call(0, 4)
    Return()

    # Function_9_1A1E end

    def Function_10_1BF4(): pass

    label("Function_10_1BF4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000Fマインツ方面に用事はない。\x01",
            "バスを待つ必要はないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3D")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ストーリーが進行すると、\x01",
            "各地の停留所からバスを\x01",
            "利用できるようになります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道の行き来に便利ですので、\x01",
            "時期が来た後にご活用ください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_1D3D")

    EventEnd(0x3)
    Return()

    # Function_10_1BF4 end

    def Function_11_1D40(): pass

    label("Function_11_1D40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51107.itc", 0x1E)
    SoundLoad(468)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x1, 0xA)
    OP_49()
    SetChrPos(0xA, 0, -2900, -7900, 0)
    OP_D5(0xA, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x2)
    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDC, 0xB4, 0xA0, 0x1E, 0x64, 0x0)
    SetMapObjFrame(0xFF, "model06_shade", 0x0, 0x1)
    FadeToBright(1000, 0)
    BeginChrThread(0xA, 3, 0, 12)
    BeginChrThread(0xC, 1, 0, 18)
    OP_68(-3400, 2700, 4900, 0)
    MoveCamera(39, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19150, 0)
    OP_68(-4150, 4300, 8400, 7500)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0xA, 3)
    Sleep(1500)
    Fade(500)
    OP_68(1000, 1200, 18900, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12500, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x101, 750, 0, 19850, 45)
    SetChrPos(0x102, 750, 0, 19850, 45)
    SetChrPos(0x109, 750, 0, 19850, 45)
    SetChrPos(0x105, 750, 0, 19850, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    Sleep(1000)
    OP_68(4300, 1200, 19250, 6000)
    MoveCamera(45, 16, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14650, 6000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 15)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 16)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    OP_0D()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F#11Pさてと……\x01",
            "キーアはまだいるのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00102F#12Pとにかく日曜学校の\x01",
            "教室に行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x105,
        (
            "#10306F#5Pやれやれ、まさか教会に\x01",
            "僕が来ることになるなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#10106F#6Pワジ君って礼拝とか\x01",
            "全然行ってなさそうだもんね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    #C0021
    ChrTalk(
        0x105,
        (
            "#10304F#5P別に女神は嫌いじゃないけど\x01",
            "昔から教会の空気は苦手でね。\x02\x03",

            "#10302Fこう、ムズ痒#2Rがゆ#くなってこないかい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00001F#11P宗教がかった不良グループを\x01",
            "率いてたくせによく言うなぁ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    #C0023
    ChrTalk(
        0x102,
        (
            "#00111F#12Pよくケンカで『聖戦』とか\x01",
            "言ってなかったかしら？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    #C0024
    ChrTalk(
        0x105,
        (
            "#10304F#5Pフフ、あれはどちらかというと\x01",
            "アッバスの趣味なんだけど。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2200, 0, 11250, 0)

    #N0025
    NpcTalk(
        0x9,
        "娘の声",
        "#1P……あの。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xDAC)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2291():
        OP_93(0x101, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2291)
    Sleep(50)

    def lambda_22A1():
        OP_93(0x102, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_22A1)
    Sleep(50)

    def lambda_22B1():
        OP_93(0x109, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_22B1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0026
    ChrTalk(
        0x101,
        "#00005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#00105F#5Pあら……？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7202", 0)
    Fade(500)
    SetChrPos(0x101, 4650, 0, 19500, 180)
    SetChrPos(0x102, 4400, 0, 18200, 180)
    SetChrPos(0x109, 2900, 0, 18500, 180)
    SetChrPos(0x105, 3150, 0, 19800, 180)
    OP_68(3350, 1400, 17650, 0)
    MoveCamera(135, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14350, 0)
    OP_68(3400, 1400, 18600, 3000)

    def lambda_238D():
        OP_95(0xFE, 3800, 0, 16050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_238D)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    #N0028
    NpcTalk(
        0x9,
        "シスター服の娘",
        (
            "#13803F#11P突然、すみません。\x02\x03",

            "#13800Fクロスベル大聖堂というのは\x01",
            "こちらで宜しいのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00002F#6Pあ、はい、そうですけど。\x01",
            "（大きなトランクだな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_9B(0x0, 0x102, 0x0, 0x28A, 0x7D0, 0x0)

    #C0030
    ChrTalk(
        0x102,
        "#00105F#6Pリ、リースさん！？\x02",
    )

    CloseMessageWindow()

    #N0031
    NpcTalk(
        0x9,
        "シスター服の娘",
        (
            "#13805F#11Pエリィさん……\x01",
            "どうもお久しぶりです。\x02\x03",

            "#13802Fそういえばクロスベルの出身と\x01",
            "仰っていましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00102F#6Pええ……！\x02\x03",

            "#00109Fふふっ、まさかリースさんと\x01",
            "こんな場所で再会できるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00005F#6Pえっと……\x01",
            "エリィの知り合いなのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0034
    ChrTalk(
        0x102,
        (
            "#00104F#11Pええ、私が各地に留学していたのは\x01",
            "話したと思うけど……\x02\x03",

            "#00102F２年前、アルテリア法国に\x01",
            "留学した時にお世話になったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        "#10105F#6Pアルテリア法国……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10302F#6Pへえ、たしか七耀教会の\x01",
            "本拠地がある場所だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0037
    NpcTalk(
        0x9,
        "シスター服の娘",
        "#13804F#11Pええ、その通りです。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0038
    AnonymousTalk(
        0x9,
        (
            "──初めまして。\x01",
            "リース・アルジェントです。\x02\x03",

            "この度、クロスベル大聖堂に\x01",
            "赴任することになりました。\x02\x03",

            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0039
    ChrTalk(
        0x101,
        "#00000F#6Pこ、こちらこそ。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        "#10104F#6Pよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0041
    ChrTalk(
        0x102,
        (
            "#00102F#6Pそうですか……\x01",
            "リースさんがクロスベル大聖堂へ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x102,
        (
            "#00105F#6Pあら……？\x01",
            "でも確かリースさんって……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3540, 1400, 18670, 750)

    def lambda_28DD():
        OP_96(0xFE, 0x109A, 0x0, 0x4010, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28DD)

    def lambda_28F7():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_28F7)
    Sleep(100)

    def lambda_2907():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2907)
    Sleep(100)

    def lambda_2917():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2917)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)

    #C0043
    ChrTalk(
        0x9,
        (
            "#13806F#11P（……エリィさん。\x01",
            "  一つお願いがあります。）\x02\x03",

            "#13808F（私の身分は他言無用に\x01",
            "  していただけませんか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00105F#6P（……あ……\x01",
            "  や、やっぱりそうですよね。）\x02\x03",

            "#00108F（その……\x01",
            "  何か事情があって赴任を？）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#13803F#11P（ええ、いずれエリィさんには\x01",
            "  詳しいことをお話します。）\x02\x03",

            "#13802F（クロスベルの状況について\x01",
            "  お聞きしたい事もありますし。）\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#00100F#6P（わ、分かりました。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        "#00005F#6Pえっと、エリィ？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0048
    ChrTalk(
        0x102,
        "#00109F#11Pあはは、何でもないの。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#13803F#11P着任の挨拶があるので\x01",
            "私はこれで失礼します。\x02\x03",

            "#13800F……そういえば\x01",
            "皆さんも大聖堂へ用事が？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0050
    ChrTalk(
        0x102,
        (
            "#00104F#6Pえっと、知り合いの子を\x01",
            "迎えにきたんです。\x02\x03",

            "#00100F多分、日曜学校の教室に\x01",
            "いると思うんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#13804F#11Pそうですか。\x01",
            "……それではまた。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3620, 1400, 19740, 5000)

    def lambda_2C91():

        label("loc_2C91")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2C91")

    QueueWorkItem2(0x101, 2, lambda_2C91)

    def lambda_2CA3():

        label("loc_2CA3")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2CA3")

    QueueWorkItem2(0x102, 2, lambda_2CA3)

    def lambda_2CB5():

        label("loc_2CB5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2CB5")

    QueueWorkItem2(0x109, 2, lambda_2CB5)

    def lambda_2CC7():

        label("loc_2CC7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2CC7")

    QueueWorkItem2(0x105, 2, lambda_2CC7)
    BeginChrThread(0x9, 3, 0, 17)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00002F#11P何か独特の雰囲気を持った\x01",
            "シスターさんだったな……\x02\x03",

            "すごく落ち着いていたけど\x01",
            "俺たちよりも年上なのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0053
    ChrTalk(
        0x102,
        (
            "#00104F#11P私の１つ上だったから\x01",
            "１９歳のはずよ。\x02\x03",

            "#00100Fアルテリアに滞在していた時に\x01",
            "たまたま知り合って……\x02\x03",

            "#00109Fふふ、色々と美味しいお店に\x01",
            "連れて行ってくれたわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0054
    ChrTalk(
        0x109,
        "#10105F#12P美味しいお店、ですか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0055
    ChrTalk(
        0x102,
        (
            "#00104F#5Pええ、ああ見えて\x01",
            "食べる事が大好きな人なの。\x02\x03",

            "#00102Fクロスベルに来たんだったら\x01",
            "良い店を紹介しなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x109,
        (
            "#10109F#12Pふふっ、さぞかし\x01",
            "紹介しがいがありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00005F#5Pワジ、どうした？\x01",
            "じっと見つめたりして……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F64():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F64)
    Sleep(100)

    def lambda_2F74():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F74)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0058
    ChrTalk(
        0x105,
        (
            "#10303F#12P……いや。\x02\x03",

            "#10300F面白い気配をまとった\x01",
            "お姉さんだと思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        "#00105F#11P！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#00001F#5P面白い気配……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        (
            "#10105F#11P確かにシスターだけあって\x01",
            "清らかな感じはしたけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    #C0062
    ChrTalk(
        0x105,
        (
            "#10304F#6Pいや、どちらかというと\x01",
            "タダ者じゃない雰囲気かな。\x02\x03",

            "#10302F……どうやら誰かさんは\x01",
            "何か知っているみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0063
    ChrTalk(
        0x102,
        "#00109F#11Pな、何のことかしら？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 350)

    #C0064
    ChrTalk(
        0x109,
        "#10100F#12P？？？\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00006F#5Pう、うーん、まあいいや。\x02\x03",

            "#00000Fそろそろ日が暮れる。\x01",
            "早くキーアを迎えに行こう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0066
    ChrTalk(
        0x102,
        (
            "#00106F#11Pそ、そうね。\x01",
            "（ワジ君、鋭すぎるわ……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(14850, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 6300, 0, 24000, 45)
    SetScenarioFlags(0x127, 7)
    OP_29(0xA1, 0x1, 0xA)
    OP_1B(0x2, 0x0, 0x18)
    OP_1B(0x0, 0x0, 0x19)
    OP_66(0x1, 0x1)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM("ed7150", "ed7102")
    OP_24(0x1D4)
    EventEnd(0x5)
    Return()

    # Function_11_1D40 end

    def Function_12_322E(): pass

    label("Function_12_322E")

    SetChrPos(0xFE, 0, -2900, -7900, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 0, -550, 0)
    OP_9F(0x1, 0, 350, 8800)
    OP_9F(0x1, -50, 0, 13200)
    OP_9F(0x1, -350, 0, 15050)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    OP_71(0x1, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_12_322E end

    def Function_13_32BE(): pass

    label("Function_13_32BE")


    def lambda_32C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32C3)
    OP_95(0xFE, 5600, 0, 20200, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_32BE end

    def Function_14_32EF(): pass

    label("Function_14_32EF")


    def lambda_32F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_32F4)
    OP_95(0xFE, 4550, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_32EF end

    def Function_15_3320(): pass

    label("Function_15_3320")


    def lambda_3325():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3325)
    OP_95(0xFE, 4050, 0, 20250, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_3320 end

    def Function_16_3351(): pass

    label("Function_16_3351")


    def lambda_3356():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3356)
    OP_95(0xFE, 3050, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_3351 end

    def Function_17_3382(): pass

    label("Function_17_3382")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 6000, 0, 17000, 2000, 0x1)
    OP_95(0xFE, 8500, 0, 25900, 2000, 0x0)
    Return()

    # Function_17_3382 end

    def Function_18_33B2(): pass

    label("Function_18_33B2")

    Sound(468, 2, 100, 0)
    Sound(494, 0, 70, 0)
    Sleep(1500)
    Sound(459, 0, 100, 0)
    Sleep(5000)
    Sound(492, 0, 80, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_33B2 end

    def Function_19_33D7(): pass

    label("Function_19_33D7")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SoundLoad(3599)
    OP_68(4650, 800, 21900, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16350, 0)
    SetChrPos(0x101, 13080, 0, 28350, 225)
    SetChrPos(0x102, 13200, 250, 30000, 225)
    SetChrPos(0x109, 14500, 250, 30050, 225)
    SetChrPos(0x105, 15650, 0, 29950, 225)
    SetChrPos(0x153, 11400, 250, 26600, 225)
    FadeToBright(1000, 0)
    OP_68(7500, 800, 23800, 3500)

    def lambda_349C():
        OP_95(0xFE, 10200, 0, 25750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_349C)

    def lambda_34B6():
        OP_95(0xFE, 9950, 150, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34B6)

    def lambda_34D0():
        OP_95(0xFE, 11300, 250, 27300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34D0)

    def lambda_34EA():
        OP_95(0xFE, 12450, 250, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_34EA)

    def lambda_3504():
        OP_95(0xFE, 7500, 0, 23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3504)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x153, 1)
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0067
    ChrTalk(
        0x153,
        "#01109F#3599V#5P#40Wわあ、クルマだぁ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE0F)
    OP_C9(0x1, 0x80000000)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x101, 12700, 0, 26550, 270)
    SetChrPos(0x102, 13650, 0, 26000, 270)
    SetChrPos(0x109, 13800, 0, 27350, 270)
    SetChrPos(0x105, 14700, 0, 26500, 270)
    SetChrPos(0x153, 9750, 0, 24200, 270)
    OP_68(1050, 800, 21000, 0)
    MoveCamera(27, 31, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17350, 0)
    SetCameraDistance(16350, 2500)

    def lambda_361C():
        OP_95(0xFE, 2650, 0, 21050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_361C)
    WaitChrThread(0x153, 1)
    OP_6F(0x79)
    OP_0D()

    #C0068
    ChrTalk(
        0x153,
        (
            "#01110F#11Pすごくキレイだねー！\x01",
            "誰が乗ってきたんだろ～？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 20)
    Sleep(1500)
    OP_68(2950, 1000, 21250, 6000)
    MoveCamera(27, 24, 0, 6000)
    SetCameraDistance(18000, 6000)

    def lambda_36A9():
        OP_96(0xFE, 0xE74, 0x0, 0x5366, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A9)
    Sleep(150)

    def lambda_36C6():
        OP_96(0xFE, 0x122A, 0x0, 0x5140, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36C6)
    Sleep(150)

    def lambda_36E3():
        OP_96(0xFE, 0x12C0, 0x0, 0x5686, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36E3)
    Sleep(150)

    def lambda_3700():
        OP_96(0xFE, 0x1644, 0x0, 0x5334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3700)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0069
    ChrTalk(
        0x109,
        "#10112F#11Pあはは……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        (
            "#10304F#11Pフフ、これは確かに\x01",
            "喜んでもらえそうだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_93(0x153, 0x5A, 0x1F4)

    #C0071
    ChrTalk(
        0x153,
        "#01100F#6Pんー、どうしたのー？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00004F#11Pキーア、聞いて驚け。\x02\x03",

            "#00000F何を隠そう、この車は\x01",
            "俺たちが乗ってきたんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x153,
        (
            "#01105F#6Pホ、ホントー！？\x02\x03",

            "#01107F宝クジが当たったのー！？\x01",
            "それともカブでもうけたとか！？\x02",
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

    #C0074
    ChrTalk(
        0x101,
        (
            "#00006F#11Pキーア……\x01",
            "いつの間にそんな知識を。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00109F#11Pまあ、クロスベルにいれば\x01",
            "聞くことも多いでしょうし……\x02\x03",

            "#00100Fキーアちゃん、この車は\x01",
            "お仕事用に支給されたものなの。\x02\x03",

            "だから正確には\x01",
            "私たちのものじゃないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x153,
        (
            "#01102F#6Pへー、そうなんだー。\x02\x03",

            "#01109Fでも、いいカオしてる！\x01",
            "すごくカッコイイね！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00002F#11Pそ、そうか？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        (
            "#10109F#11Pふふ、キーアちゃん、\x01",
            "分かってるみたいだね～。\x02\x03",

            "#10102Fさっそく乗ってみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x153,
        "#01110F#6Pうんっ、乗りたいー！\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00012F#11Pはは、大喜びだな。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10302F#11Pああ、せっかくだから\x01",
            "別のルートで帰らないか？\x02\x03",

            "#10304F僕としては港湾区を通って\x01",
            "東通りに抜けてみたいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#00102F#11Pあら、いいかもしれないわね。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00004F#11Pよし、そのコースで\x01",
            "支援課に帰ろうか。\x02\x03",

            "#00000Fノエル、お願いできるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x109,
        "#10100F#11Pええ、お安い御用です。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0085
    ChrTalk(
        0x153,
        "#01109F#6P#4Sそれじゃあ、レッツ・ゴー！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_33D7 end

    def Function_20_3C8D(): pass

    label("Function_20_3C8D")


    def lambda_3C92():

        label("loc_3C92")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3C92")

    QueueWorkItem2(0xFE, 2, lambda_3C92)
    OP_96(0xFE, 0x4B0, 0x0, 0x5AD2, 0x7D0, 0x0)
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(800)
    OP_64(0x153)
    OP_96(0xFE, 0x8CA, 0x0, 0x5208, 0x7D0, 0x0)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(600)
    EndChrThread(0xFE, 0x2)
    OP_96(0xFE, 0x866, 0x0, 0x477C, 0x7D0, 0x0)
    OP_63(0xFE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(400)
    OP_96(0xFE, 0x8CA, 0x0, 0x5208, 0x7D0, 0x0)
    Return()

    # Function_20_3C8D end

    def Function_21_3D42(): pass

    label("Function_21_3D42")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 0, 10000, 0)
    SetChrPos(0x102, 1000, 0, 9500, 0)
    SetChrPos(0x103, -750, 0, 8500, 0)
    SetChrPos(0x109, 0, 0, 7750, 0)
    SetChrPos(0x105, 1500, 0, 8000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(0, 800, 10000, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(850, 800, 12900, 3000)
    MoveCamera(50, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(23500, 3000)
    FadeToBright(1000, 0)

    def lambda_3E17():
        OP_9B(0x0, 0x101, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E17)
    Sleep(50)

    def lambda_3E2F():
        OP_9B(0x0, 0x102, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E2F)
    Sleep(50)

    def lambda_3E47():
        OP_9B(0x0, 0x103, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E47)
    Sleep(50)

    def lambda_3E5F():
        OP_9B(0x0, 0x109, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E5F)
    Sleep(50)

    def lambda_3E77():
        OP_9B(0x0, 0x105, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E77)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    def lambda_3EA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EA4)

    def lambda_3EB1():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3EB1)
    Sleep(50)

    def lambda_3EC1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3EC1)
    Sleep(50)

    def lambda_3ED1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3ED1)
    Sleep(50)

    def lambda_3EE1():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3EE1)
    Sleep(50)

    def lambda_3EF1():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3EF1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)

    #C0086
    ChrTalk(
        0x101,
        (
            "#00008F#5P滝の手前の高台ということは……\x01",
            "小さな吊橋がかかっていた場所か？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00201F#6Pええ、位置的には\x01",
            "ちょうどそこになるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x105,
        (
            "#10303F#11P警備隊が近くにいるらしいけど\x01",
            "こっそり行った方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#00108F#11Pそうね……\x01",
            "事情を説明している暇も無いし。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10106F#12P……確かにそうかもしれません。\x02\x03",

            "#10101Fとにかくこのまま\x01",
            "吊橋の手前まで行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 700, 0, 13950, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x166, 3)
    EventEnd(0x5)
    Return()

    # Function_21_3D42 end

    def Function_22_40C2(): pass

    label("Function_22_40C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 5100, 0, 19400, 270)
    SetChrPos(0x102, 3400, 0, 18350, 45)
    SetChrPos(0x103, 4700, 0, 20450, 180)
    SetChrPos(0x109, 1250, 0, 19500, 270)
    SetChrPos(0x105, 3500, 0, 20950, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-1250, 600, 18950, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    OP_68(4150, 600, 19600, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(23500, 3000)
    Sound(461, 0, 100, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x109, 0xB4, 0x1F4)
    OP_95(0x109, 3000, 0, 19500, 2000, 0x0)
    OP_6F(0x79)

    #C0091
    ChrTalk(
        0x101,
        (
            "#00008F#11P滝の手前の高台ということは……\x01",
            "小さな吊橋がかかっていた場所か？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#00201F#5Pええ、位置的には\x01",
            "ちょうどそこになるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10303F#5P警備隊が近くにいるらしいけど\x01",
            "こっそり行った方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#00108F#12Pそうね……\x01",
            "事情を説明している暇も無いし。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        (
            "#10106F#6P……確かにそうかもしれません。\x02\x03",

            "#10101Fとにかくこのまま\x01",
            "吊橋の手前まで行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 5100, 0, 19400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x166, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_22_40C2 end

    def Function_23_4369(): pass

    label("Function_23_4369")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(24150, 130, 33310, 0)
    MoveCamera(54, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21160, 0)
    SetChrPos(0x18D, 24890, 120, 31720, 270)
    SetChrPos(0x101, 23000, 130, 32259, 90)
    SetChrPos(0x102, 22060, 120, 31350, 90)
    SetChrPos(0x103, 22160, 130, 33020, 90)
    SetChrPos(0x104, 20520, 120, 31760, 90)
    SetChrPos(0x109, 20700, 130, 33000, 90)
    SetChrPos(0x105, 20830, 130, 30480, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4571")
    SetChrName("")

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "シスター・リースを導力車で\x01",
            "クロスベル大聖堂へと送り届けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7202", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0097
    ChrTalk(
        0x18D,
        (
            "#11P#04404F皆さん、わざわざ送っていただいて\x01",
            "ありがとうございました。\x02\x03",

            "#04402F皆さんの導力車……\x01",
            "大変乗り心地がよかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x109,
        (
            "#6P#10109Fふふっ、喜んでいただけて\x01",
            "あたしも嬉しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46EB")

    label("loc_4571")

    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "シスター・リースと一緒にバスに乗り、\x01",
            "クロスベル大聖堂へと送り届けた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7202", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0100
    ChrTalk(
        0x18D,
        (
            "#11P#04404F皆さん、わざわざ送っていただいて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        (
            "#6P#10102Fいえ、大したことは……\x02\x03",

            "#10106F本当ならあたしたちの導力車に\x01",
            "乗せて差し上げたかった所ですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x18D,
        (
            "#11P#04402Fふふ、それは是非\x01",
            "次の機会によろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46EB")


    #C0103
    ChrTalk(
        0x101,
        (
            "#6P#00001Fところで……\x01",
            "《星杯騎士》のことは、\x01",
            "大聖堂の人には？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x18D,
        (
            "#11P#04403Fええ、誰にも言っていません。\x02\x03",

            "#04408Fさすがにエラルダ大司教は\x01",
            "薄々感づいている様子ですが……\x02\x03",

            "#04404Fまあ、下手を打たなければ\x01",
            "問題ないかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#6P#00306Fうーむ、教会の中も\x01",
            "色々と大変そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        (
            "#6P#00100Fリースさん、くれぐれも\x01",
            "無茶はしないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、それとあまり神経を\x01",
            "すり減らさないように。\x02\x03",

            "#10302F美容にも悪そうだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x18D,
        (
            "#11P#04404Fええ……ご心配なく。\x02\x03",

            "#04400Fでは、また何かあったら\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#6P#00000Fええ、こちらこそ。\x02",
    )

    CloseMessageWindow()
    OP_97(0x18D, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0x18D, 0x80)
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        (
            "#11P#00000Fよし……\x01",
            "それじゃあ俺たちも\x01",
            "行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#6P#00200Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【月の僧院の調査】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7C, 0x1, 0x4)
    OP_29(0x7C, 0x1, 0x5)
    OP_29(0x7C, 0x4, 0x10)
    RemoveParty(0x8C, 0x0)
    SetChrPos(0x0, 5530, 0, 23110, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_23_4369 end

    def Function_24_4A3C(): pass

    label("Function_24_4A3C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AB8")

    #C0113
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはマインツ山道か……\x02\x03",

            "特に用事はないし、\x01",
            "これ以上進むのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4AFE")

    label("loc_4AB8")


    #C0114
    ChrTalk(
        0x101,
        (
            "#00000Fマインツ方面に用事はない。\x01",
            "これ以上進むのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B50")

    #C0115
    ChrTalk(
        0x101,
        (
            "#00000Fおっと、こっちは逆方向だな。\x01",
            "早くキーアを迎えに行こう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCA")

    #C0116
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはマインツ山道か……\x02\x03",

            "特に用事はないし、\x01",
            "これ以上進むのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C10")

    label("loc_4BCA")


    #C0117
    ChrTalk(
        0x101,
        (
            "#00000Fマインツ方面に用事はない。\x01",
            "これ以上進むのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C8B")

    #C0118
    ChrTalk(
        0x101,
        (
            "#00001Fこの先で戦闘が……\x02\x03",

            "だが、今はとにかく\x01",
            "ランディの足跡を追わないと。\x01",
            "――いったん街の方に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CD1")

    #C0119
    ChrTalk(
        0x101,
        (
            "#00001F山道方面に用事はない。\x01",
            "大人しく引き返そう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D50")

    #C0120
    ChrTalk(
        0x101,
        (
            "#00001Fここまで来て市内を\x01",
            "離れるわけにはいかない。\x02\x03",

            "オルキスタワー突入作戦――\x01",
            "何としても成功させなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D50")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_24_4A3C end

    def Function_25_4D64(): pass

    label("Function_25_4D64")

    EventBegin(0x1)

    #C0121
    ChrTalk(
        0x101,
        (
            "#00000F早くキーアを迎えに行こう。\x01",
            "街に戻るのはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -200, -500, 1530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_4D64 end

    def Function_26_4DBA(): pass

    label("Function_26_4DBA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　南・クロスベル市\x01",
            "　東・クロスベル大聖堂\x01",
            "北西・鉱山町マインツ　３１１セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_4DBA end

    SaveToFile()

Try(main)
