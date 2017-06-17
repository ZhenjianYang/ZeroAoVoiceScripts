from ScenarioHelper import *

def main():
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
        "巴士",                   # 1
        "莉丝修女",               # 2
        "车",                     # 3
        "钢铁土龙",               # 4
        "SE控制",                 # 5
        "br2000",                 # 6
        "克洛斯贝尔市方向",       # 7
        "克洛斯贝尔大圣堂方向",   # 8
        "矿山镇玛因兹方向",       # 9
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

    PlaceName(-1.7999999523162842, 0.0, -15.550000190734863, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(45.0, 0.0, 37.0, 0x0000, 0x0000, "克洛斯贝尔大圣堂方向")
    PlaceName(-23.0, 0.0, 75.30000305175781, 0x0000, 0x0000, "矿山镇玛因兹方向")
    PlaceName(11.25, 0.0, 16.450000762939453, 0x0000, 0x0055, "")

    ChipFrameInfo(1096, 0)                                       # 0

    ScpFunction((
        "Function_0_448",          # 00, 0
        "Function_1_467",          # 01, 1
        "Function_2_F9D",          # 02, 2
        "Function_3_126B",         # 03, 3
        "Function_4_126F",         # 04, 4
        "Function_5_1442",         # 05, 5
        "Function_6_1576",         # 06, 6
        "Function_7_15C7",         # 07, 7
        "Function_8_165B",         # 08, 8
        "Function_9_19F0",         # 09, 9
        "Function_10_1BA4",        # 0A, 10
        "Function_11_1CC6",        # 0B, 11
        "Function_12_300E",        # 0C, 12
        "Function_13_309E",        # 0D, 13
        "Function_14_30CF",        # 0E, 14
        "Function_15_3100",        # 0F, 15
        "Function_16_3131",        # 10, 16
        "Function_17_3162",        # 11, 17
        "Function_18_3192",        # 12, 18
        "Function_19_31B7",        # 13, 19
        "Function_20_399D",        # 14, 20
        "Function_21_3A52",        # 15, 21
        "Function_22_3D86",        # 16, 22
        "Function_23_3FE1",        # 17, 23
        "Function_24_45BC",        # 18, 24
        "Function_25_4884",        # 19, 25
        "Function_26_48CC",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1330")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "调查停靠站的告示牌后，\x01",
            "就能乘坐导力巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与驾驶导力车一样，乘坐巴士\x01",
            "也可移动至各地，请多加利用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 6)

    label("loc_1330")


    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "矿山镇玛因兹\x01",                # 0
            "停靠站（人偶工房附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E9")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DB")
    SetScenarioFlags(0x22, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_13E4")

    label("loc_13DB")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_13E4")

    Jump("loc_143A")

    label("loc_13E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_143A")
    Call(0, 5)
    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1431")
    SetScenarioFlags(0x22, 1)
    SetScenarioFlags(0x25, 1)
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_143A")

    label("loc_1431")

    NewScene("r2030", 0, 0, 0)
    IdleLoop()

    label("loc_143A")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_4_126F end

    def Function_5_1442(): pass

    label("Function_5_1442")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1572")
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

    def lambda_1528():
        OP_9E(0xFE, 0x3174, 0x82A0, 0xFFFF15A0, 0xFA0, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1528)
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

    label("loc_1572")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_5_1442 end

    def Function_6_1576(): pass

    label("Function_6_1576")

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

    # Function_6_1576 end

    def Function_7_15C7(): pass

    label("Function_7_15C7")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1622")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1617")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_161D")

    label("loc_1617")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_161D")

    Jump("loc_1646")

    label("loc_1622")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1640")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_1646")

    label("loc_1640")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_1646")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_15C7 end

    def Function_8_165B(): pass

    label("Function_8_165B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16C3")
    TalkBegin(0xFF)

    #C0004
    ChrTalk(
        0x101,
        (
            "#00000F琪雅要是看到这辆车，\x01",
            "一定会很吃惊吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#00100F呵呵，赶快去接她吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_16C3")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16F5")
    SetScenarioFlags(0x31, 2)

    label("loc_16F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_173B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1735")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_172A")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_1730")

    label("loc_172A")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_1730")

    Jump("loc_173B")

    label("loc_1735")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_173B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_17AC")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_178C"),
        (SWITCH_DEFAULT, "loc_179D"),
    )


    label("loc_178C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_17A7")

    label("loc_179D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17A7")

    Jump("loc_19DD")

    label("loc_17AC")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_17DC")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_17DC")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1806"),
        (1, "loc_190A"),
        (2, "loc_199B"),
        (SWITCH_DEFAULT, "loc_19D3"),
    )


    label("loc_1806")

    SetMapObjFrame(0x1, "light", 0x0, 0x1)
    OP_74(0x1, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1837")
    OP_70(0x1, 0x12C)
    OP_71(0x1, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_1847")

    label("loc_1837")

    OP_70(0x1, 0xF0)
    OP_71(0x1, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_1847")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_189D")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C0")
    Sound(461, 0, 100, 0)

    label("loc_18C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18E0")
    OP_70(0x1, 0x14A)
    OP_71(0x1, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_18F0")

    label("loc_18E0")

    OP_70(0x1, 0x10E)
    OP_71(0x1, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_18F0")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x1, "light", 0x1, 0x1)
    OP_70(0x1, 0x0)
    Jump("loc_173B")

    label("loc_190A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_197C")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_193F")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1957")

    label("loc_193F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1952")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1957")

    label("loc_1952")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1957")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1996")

    label("loc_197C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_198C")
    OP_AF(0xFB)
    Jump("loc_1996")

    label("loc_198C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1996")

    Jump("loc_19DD")

    label("loc_199B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19CE")

    label("loc_19B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_19C4")
    OP_AF(0xFB)
    Jump("loc_19CE")

    label("loc_19C4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19CE")

    Jump("loc_19DD")

    label("loc_19D3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19DD")

    Jump("loc_173B")

    label("loc_19E2")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_8_165B end

    def Function_9_19F0(): pass

    label("Function_9_19F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A02")
    Call(0, 10)
    Return()

    label("loc_1A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A39")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A4B")
    Call(0, 10)
    Return()

    label("loc_1A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ABD")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00000F我们现在还是集中精神，\x01",
            "专心调查事故的状况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF8")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0009
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

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B6A")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0011
    ChrTalk(
        0x101,
        (
            "#00001F我们不需要去玛因兹地区，\x01",
            "没必要在这里等巴士。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_1B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1BA0")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0012
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

    label("loc_1BA0")

    Call(0, 4)
    Return()

    # Function_9_19F0 end

    def Function_10_1BA4(): pass

    label("Function_10_1BA4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000F我们不需要去玛因兹地区，\x01",
            "没必要在这里等巴士。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC3")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随着剧情的进展，\x01",
            "即可在各地的停靠站\x01",
            "乘坐巴士。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "乘坐巴士往来于市外各地十分便利，\x01",
            "届时请多加利用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_1CC3")

    EventEnd(0x3)
    Return()

    # Function_10_1BA4 end

    def Function_11_1CC6(): pass

    label("Function_11_1CC6")

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
            "#00000F#11P嗯……\x01",
            "琪雅应该还在里面吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00102F#12P我们先去主日学校\x01",
            "的教室看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x105,
        (
            "#10306F#5P哎呀呀，我竟然\x01",
            "也会来教会这种地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#10106F#6P瓦吉，你好像从来都\x01",
            "不去教会做礼拜吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x109, 500)

    #C0021
    ChrTalk(
        0x105,
        (
            "#10304F#5P我并不是讨厌女神，\x01",
            "只是一直都不太习惯教会内的气氛。\x02\x03",

            "#10302F你们不会觉得来这里有种芒刺在背的感觉吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00001F#11P率领着模仿宗教集团的不良团伙，\x01",
            "竟然还能说出这样的话……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)

    #C0023
    ChrTalk(
        0x102,
        (
            "#00111F#12P你们在打架的时候，\x01",
            "不是总喊什么『圣战』吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    #C0024
    ChrTalk(
        0x105,
        (
            "#10304F#5P呵呵，那只是阿巴斯\x01",
            "的个人兴趣而已。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 2200, 0, 11250, 0)

    #N0025
    NpcTalk(
        0x9,
        "女孩的声音",
        "#1P……打扰一下。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xDAC)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_21D3():
        OP_93(0x101, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21D3)
    Sleep(50)

    def lambda_21E3():
        OP_93(0x102, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_21E3)
    Sleep(50)

    def lambda_21F3():
        OP_93(0x109, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_21F3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0026
    ChrTalk(
        0x101,
        "#00005F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#00105F#5P啊……？\x02",
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

    def lambda_22CD():
        OP_95(0xFE, 3800, 0, 16050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22CD)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    #N0028
    NpcTalk(
        0x9,
        "穿修女服的少女",
        (
            "#13803F#11P冒昧打扰，真是不好意思。\x02\x03",

            "#13800F请问克洛斯贝尔大圣堂\x01",
            "是在这边吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00002F#6P啊……是、是的。\x01",
            "（好大的手提箱啊……）\x02",
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
        "#00105F#6P莉、莉丝小姐！？\x02",
    )

    CloseMessageWindow()

    #N0031
    NpcTalk(
        0x9,
        "穿修女服的少女",
        (
            "#13805F#11P艾莉小姐……\x01",
            "真是好久不见了。\x02\x03",

            "#13802F说起来，你当时的确说过，\x01",
            "自己是出身于克洛斯贝尔呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00102F#6P嗯……！\x02\x03",

            "#00109F呵呵，真没想到能在这种地方\x01",
            "和莉丝小姐再会啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00005F#6P那个……\x01",
            "这位是艾莉的朋友吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0034
    ChrTalk(
        0x102,
        (
            "#00104F#11P嗯，以前和大家说过，\x01",
            "我曾经去各地留学……\x02\x03",

            "#00102F两年前，我在亚尔特利亚法典国\x01",
            "留学时，曾受到莉丝小姐很多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        "#10105F#6P亚尔特利亚法典国……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10302F#6P嘿，那好像是七耀教会\x01",
            "的总根据地吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0037
    NpcTalk(
        0x9,
        "穿修女服的少女",
        "#13804F#11P嗯，正是。\x02",
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
            "初次见面，\x01",
            "我的名字是莉丝·亚尔珍特。\x02\x03",

            "此次前来，是要前往\x01",
            "克洛斯贝尔大圣堂赴任。\x02\x03",

            "还请各位多多关照。\x02",
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
        "#00000F#6P彼、彼此彼此。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        "#10104F#6P请多关照。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0041
    ChrTalk(
        0x102,
        (
            "#00102F#6P这样啊……\x01",
            "莉丝小姐要去克洛斯贝尔大圣堂赴任。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x102,
        (
            "#00105F#6P哎……？\x01",
            "但莉丝小姐不是……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3540, 1400, 18670, 750)

    def lambda_2799():
        OP_96(0xFE, 0x109A, 0x0, 0x4010, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2799)

    def lambda_27B3():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_27B3)
    Sleep(100)

    def lambda_27C3():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_27C3)
    Sleep(100)

    def lambda_27D3():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_27D3)
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
            "#13806F#11P（……艾莉小姐，\x01",
            "  拜托你一件事情。）\x02\x03",

            "#13808F（不要将我的身份\x01",
            "  告诉其他人，可以吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00105F#6P（……啊……\x01",
            "  果、果然如此啊。）\x02\x03",

            "#00108F（那个……\x01",
            "  你来此赴任，是出于某些缘由吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#13803F#11P（嗯，以后有机会时，\x01",
            "  会向你详细说明的。）\x02\x03",

            "#13802F（关于克洛斯贝尔的状况，\x01",
            "  我也有不少事情需要请教。）\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#00100F#6P（明、明白了。）\x02",
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
        "#00005F#6P那个……艾莉？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0048
    ChrTalk(
        0x102,
        "#00109F#11P啊哈哈，没什么。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#13803F#11P我还要去大圣堂报到，\x01",
            "就此失陪了。\x02\x03",

            "#13800F……对了，\x01",
            "各位也有事要去大圣堂吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    #C0050
    ChrTalk(
        0x102,
        (
            "#00104F#6P嗯，我们要去\x01",
            "接一个孩子。\x02\x03",

            "#00100F她现在应该在\x01",
            "主日学校的教室……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "#13804F#11P这样啊。\x01",
            "……那我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3620, 1400, 19740, 5000)

    def lambda_2AE7():

        label("loc_2AE7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2AE7")

    QueueWorkItem2(0x101, 2, lambda_2AE7)

    def lambda_2AF9():

        label("loc_2AF9")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2AF9")

    QueueWorkItem2(0x102, 2, lambda_2AF9)

    def lambda_2B0B():

        label("loc_2B0B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2B0B")

    QueueWorkItem2(0x109, 2, lambda_2B0B)

    def lambda_2B1D():

        label("loc_2B1D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2B1D")

    QueueWorkItem2(0x105, 2, lambda_2B1D)
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
            "#00002F#11P真是一位气质\x01",
            "独特的修女啊……\x02\x03",

            "她的举止虽然相当稳重，\x01",
            "但年纪好像和我们差不多吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0053
    ChrTalk(
        0x102,
        (
            "#00104F#11P嗯，比我大一岁，\x01",
            "现在是十九岁。\x02\x03",

            "#00100F我在亚尔特利亚留学时，\x01",
            "在一次偶然的机会下结识了她……\x02\x03",

            "#00109F呵呵，她当时带我去了\x01",
            "很多不错的美食店呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0054
    ChrTalk(
        0x109,
        "#10105F#12P美食店吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0055
    ChrTalk(
        0x102,
        (
            "#00104F#5P嗯，从外表也许看不出，\x01",
            "其实她非常喜欢美食。\x02\x03",

            "#00102F既然她来克洛斯贝尔了，\x01",
            "到时一定要给她介绍几家美食店。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x109,
        (
            "#10109F#12P呵呵，有不少店\x01",
            "都值得介绍呢。\x02",
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
            "#00005F#5P瓦吉，你怎么了？\x01",
            "一直目不转睛地凝视……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D7E():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D7E)
    Sleep(100)

    def lambda_2D8E():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D8E)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0058
    ChrTalk(
        0x105,
        (
            "#10303F#12P……没什么。\x02\x03",

            "#10300F我只是觉得那位姐姐\x01",
            "散发着一股很有趣的气息。\x02",
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
        "#00001F#5P很有趣的气息……？\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        (
            "#10105F#11P确实，可以感觉到\x01",
            "修女独有的那种清澈气质……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    #C0062
    ChrTalk(
        0x105,
        (
            "#10304F#6P不，我的意思是，\x01",
            "可以感觉到她不是寻常之辈。\x02\x03",

            "#10302F……而且某人\x01",
            "似乎了解一些内情。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0063
    ChrTalk(
        0x102,
        "#00109F#11P你、你在说什么呢？\x02",
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
            "#00006F#5P嗯、嗯……算啦。\x02\x03",

            "#00000F天快要黑了，\x01",
            "我们赶快去接琪雅吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0066
    ChrTalk(
        0x102,
        (
            "#00106F#11P是、是啊。\x01",
            "（瓦吉真是太敏锐了……）\x02",
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

    # Function_11_1CC6 end

    def Function_12_300E(): pass

    label("Function_12_300E")

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

    # Function_12_300E end

    def Function_13_309E(): pass

    label("Function_13_309E")


    def lambda_30A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30A3)
    OP_95(0xFE, 5600, 0, 20200, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_309E end

    def Function_14_30CF(): pass

    label("Function_14_30CF")


    def lambda_30D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30D4)
    OP_95(0xFE, 4550, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_14_30CF end

    def Function_15_3100(): pass

    label("Function_15_3100")


    def lambda_3105():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3105)
    OP_95(0xFE, 4050, 0, 20250, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_15_3100 end

    def Function_16_3131(): pass

    label("Function_16_3131")


    def lambda_3136():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3136)
    OP_95(0xFE, 3050, 0, 18350, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_3131 end

    def Function_17_3162(): pass

    label("Function_17_3162")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 6000, 0, 17000, 2000, 0x1)
    OP_95(0xFE, 8500, 0, 25900, 2000, 0x0)
    Return()

    # Function_17_3162 end

    def Function_18_3192(): pass

    label("Function_18_3192")

    Sound(468, 2, 100, 0)
    Sound(494, 0, 70, 0)
    Sleep(1500)
    Sound(459, 0, 100, 0)
    Sleep(5000)
    Sound(492, 0, 80, 0)
    StopSound(468, 1000, 100)
    Return()

    # Function_18_3192 end

    def Function_19_31B7(): pass

    label("Function_19_31B7")

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

    def lambda_327C():
        OP_95(0xFE, 10200, 0, 25750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_327C)

    def lambda_3296():
        OP_95(0xFE, 9950, 150, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3296)

    def lambda_32B0():
        OP_95(0xFE, 11300, 250, 27300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32B0)

    def lambda_32CA():
        OP_95(0xFE, 12450, 250, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32CA)

    def lambda_32E4():
        OP_95(0xFE, 7500, 0, 23800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_32E4)
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
        "#01109F#3599V#5P#40W哇，有辆车！\x02",
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

    def lambda_33F6():
        OP_95(0xFE, 2650, 0, 21050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_33F6)
    WaitChrThread(0x153, 1)
    OP_6F(0x79)
    OP_0D()

    #C0068
    ChrTalk(
        0x153,
        (
            "#01110F#11P好漂亮啊！\x01",
            "是谁开来的～？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 20)
    Sleep(1500)
    OP_68(2950, 1000, 21250, 6000)
    MoveCamera(27, 24, 0, 6000)
    SetCameraDistance(18000, 6000)

    def lambda_346F():
        OP_96(0xFE, 0xE74, 0x0, 0x5366, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_346F)
    Sleep(150)

    def lambda_348C():
        OP_96(0xFE, 0x122A, 0x0, 0x5140, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_348C)
    Sleep(150)

    def lambda_34A9():
        OP_96(0xFE, 0x12C0, 0x0, 0x5686, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34A9)
    Sleep(150)

    def lambda_34C6():
        OP_96(0xFE, 0x1644, 0x0, 0x5334, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_34C6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0069
    ChrTalk(
        0x109,
        "#10112F#11P啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        (
            "#10304F#11P呵呵，看来她\x01",
            "的确很开心。\x02",
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
        "#01100F#6P嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00004F#11P琪雅，听了可别吃惊啊。\x02\x03",

            "#00000F告诉你哦，这辆车\x01",
            "是我们开来的。\x02",
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
            "#01105F#6P真、真的吗！？\x02\x03",

            "#01107F你们买彩票中奖了吗！？\x01",
            "还是炒股赚大钱了！？\x02",
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
            "#00006F#11P琪雅……\x01",
            "你是什么时候学到这些的……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00109F#11P呼，住在克洛斯贝尔，\x01",
            "肯定会经常听到这些……\x02\x03",

            "#00100F琪雅，这辆车是配发给\x01",
            "我们用于工作的。\x02\x03",

            "所以，准确来说，\x01",
            "它并不是属于我们的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x153,
        (
            "#01102F#6P哎，这样啊。\x02\x03",

            "#01109F不过这辆车好漂亮！\x01",
            "真是太帅了！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00002F#11P是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        (
            "#10109F#11P呵呵，琪雅好像\x01",
            "理解了呢～\x02\x03",

            "#10102F要不要现在就坐坐看？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x153,
        "#01110F#6P嗯！要坐！\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#00012F#11P哈哈，她很高兴啊。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10302F#11P嗯，机会难得，\x01",
            "我们换条路线回去如何？\x02\x03",

            "#10304F我建议先绕行到港湾区，\x01",
            "之后经由东街回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#00102F#11P哦，这主意不错呢。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#00004F#11P好，那就走这条路线\x01",
            "回支援科吧。\x02\x03",

            "#00000F诺艾尔，驾驶工作就拜托你啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x109,
        "#10100F#11P嗯，没问题。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0085
    ChrTalk(
        0x153,
        "#01109F#6P#4S那就出发吧！\x02",
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

    # Function_19_31B7 end

    def Function_20_399D(): pass

    label("Function_20_399D")


    def lambda_39A2():

        label("loc_39A2")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_39A2")

    QueueWorkItem2(0xFE, 2, lambda_39A2)
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

    # Function_20_399D end

    def Function_21_3A52(): pass

    label("Function_21_3A52")

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

    def lambda_3B27():
        OP_9B(0x0, 0x101, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3B27)
    Sleep(50)

    def lambda_3B3F():
        OP_9B(0x0, 0x102, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B3F)
    Sleep(50)

    def lambda_3B57():
        OP_9B(0x0, 0x103, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3B57)
    Sleep(50)

    def lambda_3B6F():
        OP_9B(0x0, 0x109, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B6F)
    Sleep(50)

    def lambda_3B87():
        OP_9B(0x0, 0x105, 0xA, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3B87)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()

    def lambda_3BB4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BB4)

    def lambda_3BC1():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3BC1)
    Sleep(50)

    def lambda_3BD1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3BD1)
    Sleep(50)

    def lambda_3BE1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3BE1)
    Sleep(50)

    def lambda_3BF1():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3BF1)
    Sleep(50)

    def lambda_3C01():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C01)
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
            "#00008F#5P瀑布前的高台……\x01",
            "也就是小吊桥那里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#00201F#6P嗯，从位置来看，\x01",
            "应该就是那个地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x105,
        (
            "#10303F#11P警备队的人好像驻守在那一带，\x01",
            "我们还是悄悄行动为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#00108F#11P是啊……\x01",
            "没时间和他们说明事情经过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        (
            "#10106F#12P……确实如此。\x02\x03",

            "#10101F总之，我们就向\x01",
            "吊桥所在的地方前进吧。\x02",
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

    # Function_21_3A52 end

    def Function_22_3D86(): pass

    label("Function_22_3D86")

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
            "#00008F#11P瀑布前的高台……\x01",
            "也就是小吊桥那里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#00201F#5P嗯，从位置来看，\x01",
            "应该就是那个地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10303F#5P警备队的人好像驻守在那一带，\x01",
            "我们还是悄悄行动为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#00108F#12P是啊……\x01",
            "没时间和他们说明事情经过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        (
            "#10106F#6P……确实如此。\x02\x03",

            "#10101F总之，我们就向\x01",
            "吊桥所在的地方前进吧。\x02",
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

    # Function_22_3D86 end

    def Function_23_3FE1(): pass

    label("Function_23_3FE1")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_41A3")
    SetChrName("")

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人\x01",
            "驾驶导力车，将莉丝修女\x01",
            "送到了克洛斯贝尔大圣堂前。\x07\x00\x02",
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
            "#11P#04404F多谢大家特意\x01",
            "把我送到这里。\x02\x03",

            "#04402F你们的导力车……\x01",
            "坐起来相当舒服呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x109,
        (
            "#6P#10109F呵呵，能让你满意，\x01",
            "我也很开心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42C7")

    label("loc_41A3")

    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人\x01",
            "和莉丝修女一起乘坐巴士，\x01",
            "回到了克洛斯贝尔大圣堂前。\x07\x00\x02",
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
            "#11P#04404F多谢大家特意\x01",
            "把我送到这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        (
            "#6P#10102F哪里，这没什么大不了的……\x02\x03",

            "#10106F原本想开我们的导力车\x01",
            "送你回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x18D,
        (
            "#11P#04402F呵呵，下次要是有机会，\x01",
            "请一定让我坐坐看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C7")


    #C0103
    ChrTalk(
        0x101,
        (
            "#6P#00001F话说回来……\x01",
            "关于你的『星杯骑士』身份，\x01",
            "大圣堂的各位都……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x18D,
        (
            "#11P#04403F嗯，我没有对任何人说过。\x02\x03",

            "#04408F艾拉尔达大主教\x01",
            "似乎已经隐隐察觉到了……\x02\x03",

            "#04404F不过，只要别做出多余的举动，\x01",
            "应该也不会有什么问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#6P#00306F唔……看来教会中\x01",
            "的情况也很复杂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        (
            "#6P#00100F莉丝小姐，请一定不要\x01",
            "太勉强自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，精神也不要\x01",
            "崩得太紧。\x02\x03",

            "#10302F那样是不利于美容的。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x18D,
        (
            "#11P#04404F嗯……不必担心。\x02\x03",

            "#04400F那么，如果以后再有什么事情，\x01",
            "还要请各位多多帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#6P#00000F嗯，彼此彼此。\x02",
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
            "#11P#00000F好……\x01",
            "那我们\x01",
            "也走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        "#6P#00200F嗯，知道了。\x02",
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
            "任务【调查月之僧院】\x07\x00",
            "完成！\x02",
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

    # Function_23_3FE1 end

    def Function_24_45BC(): pass

    label("Function_24_45BC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462C")

    #C0113
    ChrTalk(
        0x101,
        (
            "#00000F这边是玛因兹山道……\x02\x03",

            "现在没什么特别的事情，\x01",
            "还是不要继续前进了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4668")

    label("loc_462C")


    #C0114
    ChrTalk(
        0x101,
        (
            "#00000F现在不需要前往玛因兹地区，\x01",
            "还是不要继续前进了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46AA")

    #C0115
    ChrTalk(
        0x101,
        (
            "#00000F哦，不是这个方向，\x01",
            "还是赶快去接琪雅吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4718")

    #C0116
    ChrTalk(
        0x101,
        (
            "#00000F这边是玛因兹山道……\x02\x03",

            "现在没什么特别的事情，\x01",
            "还是不要继续前进了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4754")

    label("loc_4718")


    #C0117
    ChrTalk(
        0x101,
        (
            "#00000F现在不需要前往玛因兹地区，\x01",
            "还是不要继续前进了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47BB")

    #C0118
    ChrTalk(
        0x101,
        (
            "#00001F前方正在进行着战斗……\x02\x03",

            "但我们现在必须要\x01",
            "尽快调查出兰迪的行踪，\x01",
            "先回市里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47FB")

    #C0119
    ChrTalk(
        0x101,
        (
            "#00001F现在并不需要去山道地区，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4870")

    #C0120
    ChrTalk(
        0x101,
        (
            "#00001F都已经走到了这一步，\x01",
            "现在没理由离开市区。\x02\x03",

            "突入兰花塔的作战行动……\x01",
            "无论如何也要取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4870")

    SetChrPos(0x0, -27230, -2000, 65230, 135)
    EventEnd(0x4)
    Return()

    # Function_24_45BC end

    def Function_25_4884(): pass

    label("Function_25_4884")

    EventBegin(0x1)

    #C0121
    ChrTalk(
        0x101,
        (
            "#00000F赶快去接琪雅吧，\x01",
            "接到她以后再回市里。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -200, -500, 1530, 0)
    EventEnd(0x4)
    Return()

    # Function_25_4884 end

    def Function_26_48CC(): pass

    label("Function_26_48CC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　南·克洛斯贝尔市\x01",
            "　东·克洛斯贝尔大圣堂\x01",
            "西北·矿山镇玛因兹　３１１赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_48CC end

    SaveToFile()

Try(main)
