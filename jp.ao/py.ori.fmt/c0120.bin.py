from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0120.bin",                # FileName
        "c0120",                    # MapName
        "c0120",                    # Location
        0x0009,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 9, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0120",                  # 0
        "セルゲイ課長",           # 1
        "キーア",                 # 2
        "手紙",                   # 3
        "エニグマ",               # 4
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch02502.itc",                   # 01
        "chr/ch08200.itc",                   # 02
    ))

    DeclNpc(100089,  29,      65750,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   1.0,                   -0.5,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.5,                  0.25,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  -3.299999952316284,    68.0,                  -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.649999976158142,     -34.0,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  1.0,                   71.5,                  0.0,                   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.5,                  -23.83333396911621,    -0.0,                  1.0])

    DeclActor(13960,   0,       63640,   1500,    13960,   1500,    63640,   0x007C, 0,  8,  0x0000)
    DeclActor(170000,  0,       63560,   1500,    170000,  1500,    63560,   0x007C, 0,  7,  0x0000)
    DeclActor(-860,    0,       128259,  1200,    -860,    3000,    128259,  0x007C, 0,  24, 0x0000)
    DeclActor(-2790,   0,       127470,  1200,    -2790,   2000,    127470,  0x007C, 0,  25, 0x0000)
    DeclActor(49300,   30,      129770,  1200,    49300,   3500,    129770,  0x007C, 0,  26, 0x0000)
    DeclActor(53410,   0,       123840,  1200,    53410,   2000,    123840,  0x007C, 0,  27, 0x0000)
    DeclActor(100740,  30,      129180,  1200,    100740,  1500,    129180,  0x007C, 0,  28, 0x0000)
    DeclActor(102940,  30,      125380,  1200,    102940,  2000,    125380,  0x007C, 0,  29, 0x0000)
    DeclActor(2750,    0,       125420,  1200,    2750,    1500,    125420,  0x007C, 0,  21, 0x0000)
    DeclActor(48000,   0,       127860,  1200,    47560,   1500,    128630,  0x007C, 0,  22, 0x0000)
    DeclActor(102450,  0,       127940,  1200,    102450,  1500,    127940,  0x007C, 0,  23, 0x0000)

    ChipFrameInfo(1132, 0)                                       # 0

    ScpFunction((
        "Function_0_46C",          # 00, 0
        "Function_1_51C",          # 01, 1
        "Function_2_724",          # 02, 2
        "Function_3_976",          # 03, 3
        "Function_4_C66",          # 04, 4
        "Function_5_CDB",          # 05, 5
        "Function_6_1260",         # 06, 6
        "Function_7_1569",         # 07, 7
        "Function_8_15BC",         # 08, 8
        "Function_9_1611",         # 09, 9
        "Function_10_16CE",        # 0A, 10
        "Function_11_178B",        # 0B, 11
        "Function_12_17E2",        # 0C, 12
        "Function_13_1A9E",        # 0D, 13
        "Function_14_1D7A",        # 0E, 14
        "Function_15_1F96",        # 0F, 15
        "Function_16_21BE",        # 10, 16
        "Function_17_221B",        # 11, 17
        "Function_18_2428",        # 12, 18
        "Function_19_263B",        # 13, 19
        "Function_20_284D",        # 14, 20
        "Function_21_2A5F",        # 15, 21
        "Function_22_2B04",        # 16, 22
        "Function_23_2BA9",        # 17, 23
        "Function_24_2C4E",        # 18, 24
        "Function_25_2D03",        # 19, 25
        "Function_26_2DBC",        # 1A, 26
        "Function_27_2E71",        # 1B, 27
        "Function_28_2F37",        # 1C, 28
        "Function_29_2FF2",        # 1D, 29
        "Function_30_30AD",        # 1E, 30
        "Function_31_3122",        # 1F, 31
        "Function_32_3151",        # 20, 32
        "Function_33_3180",        # 21, 33
        "Function_34_31AF",        # 22, 34
        "Function_35_31DE",        # 23, 35
        "Function_36_3D2F",        # 24, 36
        "Function_37_47C7",        # 25, 37
        "Function_38_48D4",        # 26, 38
        "Function_39_5945",        # 27, 39
        "Function_40_5980",        # 28, 40
        "Function_41_59BB",        # 29, 41
        "Function_42_611A",        # 2A, 42
        "Function_43_6B8E",        # 2B, 43
    ))


    def Function_0_46C(): pass

    label("Function_0_46C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_4A4"),
        (1, "loc_4B0"),
        (2, "loc_4BC"),
        (3, "loc_4C8"),
        (4, "loc_4D4"),
        (5, "loc_4E0"),
        (6, "loc_4EC"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_51B")

    Return()

    # Function_0_46C end

    def Function_1_51C(): pass

    label("Function_1_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_670")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x349, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    Event(0, 14)

    label("loc_551")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x348, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_578")
    Event(0, 15)

    label("loc_578")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    Event(0, 37)

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34F, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E0")
    Event(0, 18)

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34E, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    Event(0, 17)

    label("loc_607")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x353, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    Event(0, 20)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x352, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
    Event(0, 19)

    label("loc_655")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_670")
    Event(0, 6)

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_67E")
    Jump("loc_6FA")

    label("loc_67E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_68C")
    Jump("loc_6FA")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_6B6")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 49960, 30, 123630, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_6FA")

    label("loc_6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6C4")
    Jump("loc_6FA")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 3)), scpexpr(EXPR_END)), "loc_6EC")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 99500, 30, 65530, 180)

    label("loc_6EC")

    Jump("loc_6FA")

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6FA")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_711")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 41)
    Jump("loc_723")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_723")
    ClearScenarioFlags(0x23, 2)
    SetScenarioFlags(0x0, 1)
    Event(0, 43)

    label("loc_723")

    Return()

    # Function_1_51C end

    def Function_2_724(): pass

    label("Function_2_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_739")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_783")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_783")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7D7")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FE")
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    Jump("loc_812")

    label("loc_7FE")

    SetMapObjFrame(0xFF, "01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02", 0x0, 0x1)

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_82F")
    SetMapObjFrame(0xFF, "asihuki", 0x0, 0x1)
    Jump("loc_83E")

    label("loc_82F")

    SetMapObjFrame(0xFF, "asihuki", 0x1, 0x1)

    label("loc_83E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_851")
    OP_1B(0x2, 0x0, 0x2A)

    label("loc_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86B")
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x2)
    OP_65(0x2, 0x1)

    label("loc_86B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A")
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x2)
    OP_65(0x3, 0x1)
    Jump("loc_896")

    label("loc_88A")

    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x2)

    label("loc_896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B0")
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x2)
    OP_65(0x4, 0x1)

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x2)
    OP_65(0x5, 0x1)
    Jump("loc_8D5")

    label("loc_8CF")

    SetMapObjFlags(0xF, 0x4)

    label("loc_8D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8EF")
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x2)
    OP_65(0x6, 0x1)

    label("loc_8EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_909")
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x2)
    OP_65(0x7, 0x1)

    label("loc_909")

    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_928")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_93B")
    SetMapObjFlags(0x4, 0x10)
    OP_65(0x1, 0x1)

    label("loc_93B")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95D")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_95D")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_975")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_975")

    Return()

    # Function_2_724 end

    def Function_3_976(): pass

    label("Function_3_976")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_B11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01000F国家独立の住民投票の件で、\x01",
            "色々と書類が回ってきていてな。\x02\x03",

            "気になる案件は入ってるが……\x01",
            "まあ、こっちは他の課に任せておけ。\x02\x03",

            "ひとまず、今は危機管理が先決だ。\x01",
            "人形工房の聞き込みだけじゃなく、\x01",
            "支援要請もカバーしておくといい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B0C")

    label("loc_A7F")


    #C0002
    ChrTalk(
        0x8,
        (
            "#01000Fああ、キーアならついさっき\x01",
            "夕食の買い物に出かけたようだ。\x02\x03",

            "少し図書館に寄るっつってたが……\x01",
            "まあ、心配なら様子を見に行ってやれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C")

    Jump("loc_C62")

    label("loc_B11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE2")

    #C0003
    ChrTalk(
        0x8,
        (
            "#01000Fよう、俺もついさっき\x01",
            "病院から戻ってきた所だ。\x02\x03",

            "#01003Fお前らの方は引き続き、\x01",
            "《幻獣》の調査を進めとけ。\x02\x03",

            "#01002F《風の剣聖》が動けないうちに\x01",
            "せいぜい実績を上げるといい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C62")

    label("loc_BE2")


    #C0004
    ChrTalk(
        0x8,
        (
            "#01003Fお前らの方は引き続き、\x01",
            "《幻獣》の調査を進めとけ。\x02\x03",

            "#01002F《風の剣聖》が動けないうちに\x01",
            "せいぜい実績を上げるといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62")

    TalkEnd(0xFE)
    Return()

    # Function_3_976 end

    def Function_4_C66(): pass

    label("Function_4_C66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_CD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C84")
    Call(0, 5)
    Jump("loc_CD7")

    label("loc_C84")


    #C0005
    ChrTalk(
        0x9,
        (
            "#01100Fがんばってね、みんな。\x02\x03",

            "#01109Fキーア、ここで\x01",
            "みんなを待ってるからー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD7")

    TalkEnd(0xFE)
    Return()

    # Function_4_C66 end

    def Function_5_CDB(): pass

    label("Function_5_CDB")

    EventBegin(0x0)
    Fade(500)
    OP_68(49470, 1300, 122080, 0)
    MoveCamera(49, 30, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22450, 0)
    SetChrPos(0x101, 49340, 0, 122340, 0)
    SetChrPos(0x102, 50640, 0, 122340, 0)
    SetChrPos(0x103, 49970, 0, 121240, 0)
    SetChrPos(0x109, 48730, 0, 121240, 0)
    SetChrPos(0x105, 51310, 0, 121240, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    OP_0D()

    #C0006
    ChrTalk(
        0x102,
        "#00100Fキーアちゃん……ここにいたのね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x12C)

    #C0007
    ChrTalk(
        0x9,
        "#5P#01100Fあ、うんー……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0008
    ChrTalk(
        0x9,
        (
            "#5P#01108F……ランディ、\x01",
            "あのテガミを書いたとき\x01",
            "どんな気持ちだったのかな。\x02\x03",

            "#01103Fもうキーアたちに会わない……\x01",
            "つもりだったのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#12P#00205Fキーア……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10300F……ランディが戦おうとしている相手は\x01",
            "あまりにも強大みたいだからね。\x02\x03",

            "#10303F全てを手放す覚悟で挑んでいても\x01",
            "なにも不思議じゃないのかもしれない。\x02\x03",

            "#10308F居場所、仲間……自分の命さえもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#11P#00003F……そんな身勝手な覚悟で\x01",
            "支援課を抜けさせてやるもんか。\x02\x03",

            "エリィ、ティオ、ランディ……\x01",
            "ノエル、ワジ、セルゲイ課長に\x01",
            "キーアにツァイト……\x02\x03",

            "#00001Fこの中の誰かが一人でも欠けたら、\x01",
            "俺たちは『支援課』じゃないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#00104Fロイド……そうね。\x02\x03",

            "#00108Fそんな事も分かろうとしないで、\x01",
            "勝手に自分の命を懸けたりして……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        "#12P#00203Fええ、厳罰ものかと。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        "#5P#01108F………………………………\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        (
            "#12P#10100F心配しないでね、キーアちゃん。\x01",
            "先輩は絶対連れて帰るから！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、ようやく有力な手がかりが\x01",
            "得られたところだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#5P#01110Fそうなんだ……\x02\x03",

            "#01104F……がんばってね、みんな。\x02\x03",

            "#01109Fキーア、ここで\x01",
            "みんなを待ってるからー。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#11P#00000Fああ、必ずランディと一緒に\x01",
            "ここに戻ってくるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x16B, 6)
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, 49970, 0, 121240, 0)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    EventEnd(0x5)
    Return()

    # Function_5_CDB end

    def Function_6_1260(): pass

    label("Function_6_1260")

    EventBegin(0x0)
    Fade(500)
    OP_68(100360, 630, 124300, 0)
    MoveCamera(36, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 98820, 0, 123690, 315)
    SetChrPos(0x1, 100820, 0, 123690, 45)
    SetChrPos(0x2, 100680, 30, 121540, 0)
    SetChrPos(0x3, 99070, 30, 121530, 0)
    SetChrPos(0x4, 100020, 0, 124500, 0)
    OP_0D()

    #C0019
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、わが城にようこそ。\x01",
            "……なんてね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_135E")

    #C0020
    ChrTalk(
        0x1A5,
        "#5P#01105Fわー、綺麗なお部屋ー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1397")

    label("loc_135E")


    #C0021
    ChrTalk(
        0x101,
        (
            "#5P#00005Fこりゃまた……\x01",
            "さすがにお洒落な部屋だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1397")


    #C0022
    ChrTalk(
        0x109,
        (
            "#12P#10105Fほ、ほんと……\x01",
            "この部屋だけなんだか\x01",
            "モデルルームみたいっていうか。\x02\x03",

            "#10106Fなんというか、\x01",
            "馴染むのが早すぎない？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#11P#00100Fええ、しかも\x01",
            "かなり高価そうな家具が\x01",
            "揃ってるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、知り合いに頼んで\x01",
            "調達してもらったのさ。\x02\x03",

            "#10300Fまあ、疲れたらいつでも\x01",
            "寛ぎにきてくれて構わない。\x02\x03",

            "せっかくだし入居祝いに\x01",
            "そこのボトルを開けてみるのも\x01",
            "いいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#5P#00006Fいや、流石にダメだから……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100020, 30, 121290, 0)
    SetScenarioFlags(0x13B, 5)
    EventEnd(0x5)
    Return()

    # Function_6_1260 end

    def Function_7_1569(): pass

    label("Function_7_1569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157B")
    Call(0, 12)
    Jump("loc_15BB")

    label("loc_157B")

    TalkBegin(0xFF)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00000Fここはティオの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_15BB")

    Return()

    # Function_7_1569 end

    def Function_8_15BC(): pass

    label("Function_8_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CE")
    Call(0, 13)
    Jump("loc_1610")

    label("loc_15CE")

    TalkBegin(0xFF)

    #C0027
    ChrTalk(
        0x101,
        (
            "#00000Fここはランディの部屋だ。\x01",
            "入るのはやめておこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1610")

    Return()

    # Function_8_15BC end

    def Function_9_1611(): pass

    label("Function_9_1611")

    EventBegin(0x1)

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#00100Fそうね、声を掛けましょう。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1611 end

    def Function_10_16CE(): pass

    label("Function_10_16CE")

    EventBegin(0x1)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00000F……そういえば、キーアが\x01",
            "日曜学校に行くって言ってたな。\x02\x03",

            "課長も出かけた事だし、\x01",
            "一緒に出た方がいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00100Fそうね、声を掛けましょう。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_16CE end

    def Function_11_178B(): pass

    label("Function_11_178B")

    EventBegin(0x1)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00000Fキーアはこれから日曜学校だ。\x01",
            "裏口の方が近道だな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_178B end

    def Function_12_17E2(): pass

    label("Function_12_17E2")

    EventBegin(0x0)
    Fade(500)
    OP_68(169990, 1000, 63110, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23860, 0)
    SetChrPos(0x101, 170800, 0, 62310, 315)
    SetChrPos(0x102, 168790, 0, 62190, 45)
    SetChrPos(0x109, 171240, 0, 63400, 270)
    SetChrPos(0x105, 168190, 0, 63200, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_187C")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_187C")

    OP_0D()

    #C0033
    ChrTalk(
        0x102,
        "#6P#00100Fここはティオちゃんの部屋ね。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        (
            "#6P#10300F確か今は、レマン自治州に\x01",
            "出張しているんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ヨナと一緒に\x01",
            "エプスタイン財団の\x01",
            "研究所に行っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#6P#00100F自治州法の改正で導力ネットも\x01",
            "普及が進められているし、\x01",
            "その関係の手伝いなんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#11P#10103F難しいことはわかりませんけど……\x01",
            "そっちもかなり大変そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A50")

    #C0038
    ChrTalk(
        0x1A5,
        "#12P#01100Fティオ、早く帰ってこれるといいねー。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00000Fああ、本当にな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A86")

    label("loc_1A50")


    #C0040
    ChrTalk(
        0x101,
        (
            "#00000Fああ、早く帰ってこれると\x01",
            "いいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A86")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_12_17E2 end

    def Function_13_1A9E(): pass

    label("Function_13_1A9E")

    EventBegin(0x0)
    Fade(500)
    OP_68(14040, 800, 63300, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23800, 0)
    SetChrPos(0x101, 12730, 0, 61720, 45)
    SetChrPos(0x102, 14330, 0, 61720, 315)
    SetChrPos(0x109, 11530, 0, 62750, 90)
    SetChrPos(0x105, 15130, 0, 62750, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B38")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_1B38")

    OP_0D()

    #C0041
    ChrTalk(
        0x101,
        "#12P#00000Fこっちはランディの部屋だな。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#00100Fランディは今、\x01",
            "ベルガード門の部隊と\x01",
            "リハビリ訓練の真っ最中なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10305Fああ、確か教団事件で\x01",
            "例のクスリを盛られてたんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x109,
        (
            "#6P#10103Fうん……\x01",
            "後遺症というほど酷いものが\x01",
            "残ったわけじゃないけど。\x02\x03",

            "#10108F体力とカンを取り戻すのに\x01",
            "しばらく時間がかかるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそうか……\x01",
            "警備隊も早く立ち直ってほしいな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D24")

    #C0046
    ChrTalk(
        0x1A5,
        "#12P#01100Fランディも早く帰ってこないかなー。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#00100Fふふ、本当にね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D62")

    label("loc_1D24")


    #C0048
    ChrTalk(
        0x102,
        (
            "#00100Fそうね、ランディにも\x01",
            "早く帰ってきてもらいたいし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D62")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_13_1A9E end

    def Function_14_1D7A(): pass

    label("Function_14_1D7A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    OP_68(-460, 1300, 127470, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD4")
    SetChrFlags(0x0, 0x8)

    label("loc_1DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DE7")
    SetChrFlags(0x1, 0x8)

    label("loc_1DE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DFA")
    SetChrFlags(0x2, 0x8)

    label("loc_1DFA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E0D")
    SetChrFlags(0x3, 0x8)

    label("loc_1E0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E20")
    SetChrFlags(0x4, 0x8)

    label("loc_1E20")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E33")
    SetChrFlags(0x5, 0x8)

    label("loc_1E33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1E4C")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_1E4C")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -460, 0, 127470, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0049
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x349, 1)
    SetScenarioFlags(0x13C, 0)
    OP_66(0x2, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")
    Call(0, 38)

    label("loc_1EF7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0A")
    ClearChrFlags(0x0, 0x8)

    label("loc_1F0A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1D")
    ClearChrFlags(0x1, 0x8)

    label("loc_1F1D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F30")
    ClearChrFlags(0x2, 0x8)

    label("loc_1F30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F43")
    ClearChrFlags(0x3, 0x8)

    label("loc_1F43")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F56")
    ClearChrFlags(0x4, 0x8)

    label("loc_1F56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F69")
    ClearChrFlags(0x5, 0x8)

    label("loc_1F69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F82")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_1F82")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_14_1D7A end

    def Function_15_1F96(): pass

    label("Function_15_1F96")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x2)
    OP_68(-2420, 1330, 126860, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFC")
    SetChrFlags(0x0, 0x8)

    label("loc_1FFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200F")
    SetChrFlags(0x1, 0x8)

    label("loc_200F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2022")
    SetChrFlags(0x2, 0x8)

    label("loc_2022")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2035")
    SetChrFlags(0x3, 0x8)

    label("loc_2035")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2048")
    SetChrFlags(0x4, 0x8)

    label("loc_2048")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_205B")
    SetChrFlags(0x5, 0x8)

    label("loc_205B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2074")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_2074")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -2420, 30, 126860, 315)
    FadeToBright(500, 0)
    OP_0D()

    #C0051
    ChrTalk(
        0x101,
        "#0000Fここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x348, 1)
    SetScenarioFlags(0x13C, 1)
    OP_66(0x3, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211F")
    Call(0, 38)

    label("loc_211F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2132")
    ClearChrFlags(0x0, 0x8)

    label("loc_2132")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2145")
    ClearChrFlags(0x1, 0x8)

    label("loc_2145")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2158")
    ClearChrFlags(0x2, 0x8)

    label("loc_2158")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_216B")
    ClearChrFlags(0x3, 0x8)

    label("loc_216B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_217E")
    ClearChrFlags(0x4, 0x8)

    label("loc_217E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2191")
    ClearChrFlags(0x5, 0x8)

    label("loc_2191")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21AA")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_21AA")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_15_1F96 end

    def Function_16_21BE(): pass

    label("Function_16_21BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221A")
    SetChrName("")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "家具アイテムを入手すると\x01",
            "支援課メンバーの部屋に置く事ができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_221A")

    Return()

    # Function_16_21BE end

    def Function_17_221B(): pass

    label("Function_17_221B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(49580, 1330, 129410, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2275")
    SetChrFlags(0x0, 0x8)

    label("loc_2275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2288")
    SetChrFlags(0x1, 0x8)

    label("loc_2288")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229B")
    SetChrFlags(0x2, 0x8)

    label("loc_229B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22AE")
    SetChrFlags(0x3, 0x8)

    label("loc_22AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C1")
    SetChrFlags(0x4, 0x8)

    label("loc_22C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D4")
    SetChrFlags(0x5, 0x8)

    label("loc_22D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22ED")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_22ED")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 49580, 30, 129410, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0054
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34E, 1)
    SetScenarioFlags(0x13C, 2)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239C")
    ClearChrFlags(0x0, 0x8)

    label("loc_239C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AF")
    ClearChrFlags(0x1, 0x8)

    label("loc_23AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23C2")
    ClearChrFlags(0x2, 0x8)

    label("loc_23C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D5")
    ClearChrFlags(0x3, 0x8)

    label("loc_23D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E8")
    ClearChrFlags(0x4, 0x8)

    label("loc_23E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23FB")
    ClearChrFlags(0x5, 0x8)

    label("loc_23FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2414")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2414")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_17_221B end

    def Function_18_2428(): pass

    label("Function_18_2428")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x2)
    SetMapObjFlags(0xF, 0x4)
    OP_68(52070, 1330, 123440, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2488")
    SetChrFlags(0x0, 0x8)

    label("loc_2488")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_249B")
    SetChrFlags(0x1, 0x8)

    label("loc_249B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AE")
    SetChrFlags(0x2, 0x8)

    label("loc_24AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C1")
    SetChrFlags(0x3, 0x8)

    label("loc_24C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D4")
    SetChrFlags(0x4, 0x8)

    label("loc_24D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24E7")
    SetChrFlags(0x5, 0x8)

    label("loc_24E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2500")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_2500")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52070, 30, 123440, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0056
    ChrTalk(
        0x104,
        "#0300Fここでいいか。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x34F, 1)
    SetScenarioFlags(0x13C, 3)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AF")
    ClearChrFlags(0x0, 0x8)

    label("loc_25AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C2")
    ClearChrFlags(0x1, 0x8)

    label("loc_25C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D5")
    ClearChrFlags(0x2, 0x8)

    label("loc_25D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E8")
    ClearChrFlags(0x3, 0x8)

    label("loc_25E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25FB")
    ClearChrFlags(0x4, 0x8)

    label("loc_25FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_260E")
    ClearChrFlags(0x5, 0x8)

    label("loc_260E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2627")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2627")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_18_2428 end

    def Function_19_263B(): pass

    label("Function_19_263B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(100680, 1330, 127820, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2695")
    SetChrFlags(0x0, 0x8)

    label("loc_2695")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26A8")
    SetChrFlags(0x1, 0x8)

    label("loc_26A8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26BB")
    SetChrFlags(0x2, 0x8)

    label("loc_26BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26CE")
    SetChrFlags(0x3, 0x8)

    label("loc_26CE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E1")
    SetChrFlags(0x4, 0x8)

    label("loc_26E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F4")
    SetChrFlags(0x5, 0x8)

    label("loc_26F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_270D")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_270D")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 100680, 30, 127820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0058
    ChrTalk(
        0x105,
        "#10300Fフフ、ここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x352, 1)
    SetScenarioFlags(0x13C, 4)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C1")
    ClearChrFlags(0x0, 0x8)

    label("loc_27C1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D4")
    ClearChrFlags(0x1, 0x8)

    label("loc_27D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27E7")
    ClearChrFlags(0x2, 0x8)

    label("loc_27E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27FA")
    ClearChrFlags(0x3, 0x8)

    label("loc_27FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280D")
    ClearChrFlags(0x4, 0x8)

    label("loc_280D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2820")
    ClearChrFlags(0x5, 0x8)

    label("loc_2820")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2839")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2839")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_19_263B end

    def Function_20_284D(): pass

    label("Function_20_284D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_68(101940, 1330, 125580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A7")
    SetChrFlags(0x0, 0x8)

    label("loc_28A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28BA")
    SetChrFlags(0x1, 0x8)

    label("loc_28BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28CD")
    SetChrFlags(0x2, 0x8)

    label("loc_28CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E0")
    SetChrFlags(0x3, 0x8)

    label("loc_28E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28F3")
    SetChrFlags(0x4, 0x8)

    label("loc_28F3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2906")
    SetChrFlags(0x5, 0x8)

    label("loc_2906")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_291F")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_291F")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 101940, 30, 125580, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0060
    ChrTalk(
        0x105,
        "#10300Fフフ、ここでいいかな。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジの部屋に\x01",
            "新しい家具が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber(0x353, 1)
    SetScenarioFlags(0x13C, 5)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29D3")
    ClearChrFlags(0x0, 0x8)

    label("loc_29D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29E6")
    ClearChrFlags(0x1, 0x8)

    label("loc_29E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F9")
    ClearChrFlags(0x2, 0x8)

    label("loc_29F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0C")
    ClearChrFlags(0x3, 0x8)

    label("loc_2A0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A1F")
    ClearChrFlags(0x4, 0x8)

    label("loc_2A1F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A32")
    ClearChrFlags(0x5, 0x8)

    label("loc_2A32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2A4B")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_2A4B")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_20_284D end

    def Function_21_2A5F(): pass

    label("Function_21_2A5F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE6")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2AE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B02")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2B02")

    Return()

    # Function_21_2A5F end

    def Function_22_2B04(): pass

    label("Function_22_2B04")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8B")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2B8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA7")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2BA7")

    Return()

    # Function_22_2B04 end

    def Function_23_2BA9(): pass

    label("Function_23_2BA9")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C30")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2C30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2C4C")

    Return()

    # Function_23_2BA9 end

    def Function_24_2C4E(): pass

    label("Function_24_2C4E")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis361.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "トリスタン号がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_24_2C4E end

    def Function_25_2D03(): pass

    label("Function_25_2D03")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis360.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ミニサンドバッグがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_25_2D03 end

    def Function_26_2DBC(): pass

    label("Function_26_2DBC")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis366.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "サーフボードがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_26_2DBC end

    def Function_27_2E71(): pass

    label("Function_27_2E71")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis367.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ジュークボックスがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7592", 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_27_2E71 end

    def Function_28_2F37(): pass

    label("Function_28_2F37")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis368.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "コンフォートチェアがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_28_2F37 end

    def Function_29_2FF2(): pass

    label("Function_29_2FF2")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis369.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ミニ・アクアリウムがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_29_2FF2 end

    def Function_30_30AD(): pass

    label("Function_30_30AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3121")
    OP_E0(0x16, 0x0)

    label("loc_3121")

    Return()

    # Function_30_30AD end

    def Function_31_3122(): pass

    label("Function_31_3122")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_31_3122 end

    def Function_32_3151(): pass

    label("Function_32_3151")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_32_3151 end

    def Function_33_3180(): pass

    label("Function_33_3180")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_33_3180 end

    def Function_34_31AF(): pass

    label("Function_34_31AF")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_34_31AF end

    def Function_35_31DE(): pass

    label("Function_35_31DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2E")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis366.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis367.itp")
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 51750, 130, 125650, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3290")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3290")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32A9")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_32A9")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その日、ロイドたちは\x01",
            "支援業務の合間に支援課に戻り──\x02",
        )
    )

    CloseMessageWindow()

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本部との定時連絡を取りがてら\x01",
            "各自休憩を入れることにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(51630, 1830, 125550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(51630, 1330, 125550, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 49870, 0, 119410, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    #N0070
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1Pランディ、いいか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    #C0071
    ChrTalk(
        0x104,
        "#00300Fおお、いいぜ。\x02",
    )

    CloseMessageWindow()
    OP_68(49870, 1300, 123830, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_3438():
        OP_9B(0x0, 0xFE, 0xA, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3438)

    def lambda_344D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_344D)
    OP_68(50750, 1300, 124710, 2000)
    MoveCamera(45, 21, 0, 2000)
    SetCameraDistance(21500, 2000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    TurnDirection(0x101, 0x104, 500)
    OP_6F(0x79)
    Sleep(500)

    #C0072
    ChrTalk(
        0x104,
        "#00300Fなんだ、そろそろ行くか？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#00004Fああ、本部からの業務連絡も\x01",
            "今日は特に無かったからね。\x02\x03",

            "#00001F……まさかとは思うけど\x01",
            "一杯やったりとかしてないよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00309Fギクッ……\x01",
            "イヤア、ソンナコトハ。\x02\x03",

            "#00300Fうっし、そんじゃあ\x01",
            "とっとと出かけるとすっか！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x104, 0x40)
    SetChrPos(0x104, 51300, 30, 125650, 270)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x4)
    OP_0D()
    TurnDirection(0x104, 0x101, 500)
    Sleep(500)
    TurnDirection(0x101, 0x104, 500)

    #C0075
    ChrTalk(
        0x101,
        (
            "#00006Fまったく……\x02\x03",

            "#00000F（とか言いつつ結構真面目だから\x01",
            "  あんまり心配はしてないけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(750)

    #C0076
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば……\x01",
            "なんか、色々と増えてるな？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(50440, 2200, 131009, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(21000, 3000)

    def lambda_36C6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36C6)
    Sleep(200)

    def lambda_36D6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36D6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 31)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    #A0077
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000Fこれは……\x01",
            "たしかサーフボードだったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0078
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00303Fああ、本来は海沿いでしか\x01",
            "使われねぇシロモンだが……\x02\x03",

            "#00300Fエルム湖にも波は立つから\x01",
            "一応、遊べなくもないんだぜ？\x02\x03",

            "#00309Fレイクサーフィンってやつだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0079
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002Fなるほど、ランディはそういうの\x01",
            "結構好きそうだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_68(50390, 2200, 122310, 4000)
    MoveCamera(60, 25, 0, 4000)
    Sleep(1500)

    def lambda_3855():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3855)
    Sleep(200)

    def lambda_3865():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3865)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 33)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    #A0080
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fそれは……\x01",
            "えっと、何だったっけ？\x02\x03",

            "#00003F雑誌か何かで\x01",
            "見たことがあるような。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0081
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300Fジュークボックスだ。\x02\x03",

            "#00303F１０ミラコインを入れたら\x01",
            "好きな曲を演奏してくれる……\x02\x03",

            "#00302Fま、場末の酒場なんかに\x01",
            "たまに置いてあるマシンだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    Sleep(500)
    SetCameraDistance(18000, 5000)
    Sleep(500)
    OP_95(0x104, 51250, 30, 123870, 2000, 0x1)
    OP_95(0x104, 52210, 30, 123640, 2000, 0x0)
    Sleep(1000)
    StopBGM(0xBB8)
    Sound(99, 0, 100, 0)
    OP_6F(0x79)
    Sound(853, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x1, 0xA, 0x0, 0x8)
    Sleep(1500)
    OP_71(0xC, 0xA, 0x45, 0x0, 0x20)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7592", 0)
    Sleep(1500)
    OP_93(0x104, 0xB4, 0x1F4)
    OP_95(0x104, 52190, 0, 122140, 1000, 0x0)
    TurnDirection(0x104, 0x101, 500)
    Sleep(1500)

    #C0082
    ChrTalk(
        0x101,
        (
            "#00004F……いいな、これ。\x02\x03",

            "#00003F何ていうか……\x01",
            "すごく懐かしい気分になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#00304Fはは、クロスベルあたりじゃ\x01",
            "あんまり見かけねぇが……\x02\x03",

            "#00302F他に娯楽もない、\x01",
            "片田舎の酒場なんかだと\x01",
            "わりと定番のマシンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00005Fそうなのか……\x02\x03",

            "#00000Fランディが前に使っていた\x01",
            "酒場なんかにもあったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#00300Fああ、まあな。\x02\x03",

            "#00303F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)
    Sleep(500)

    #C0086
    ChrTalk(
        0x101,
        "#00005Fランディ？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#00304F……はは、何でもねぇ。\x02\x03",

            "#00300Fそろそろ行くか。\x01",
            "お嬢たちが待ってんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00000Fああ、行こうか。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ランディの家具を全て揃えた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x104, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3CEF")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_3CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3D08")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_3D08")

    OP_49()
    OP_D7(0x1E)
    OP_CC(0x1, 0xFF, 0x0)
    OP_74(0xC, 0x1E)
    OP_70(0xC, 0x0)
    SetScenarioFlags(0x12D, 0)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 105, 0, 0)
    IdleLoop()

    label("loc_3D2E")

    Return()

    # Function_35_31DE end

    def Function_36_3D2F(): pass

    label("Function_36_3D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C6")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis368.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis369.itp")
    LoadChrToIndex("chr/ch03002.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, 100630, 200, 129169, 225)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3DE7")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3DE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3E00")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_3E00")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その日、ロイドたちは\x01",
            "支援業務の合間に支援課に戻り──\x02",
        )
    )

    CloseMessageWindow()

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本部との定時連絡を取りがてら\x01",
            "各自休憩を入れることにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(100220, 1830, 128539, 0)
    MoveCamera(33, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(100250, 1330, 128590, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x101, 99800, 0, 119340, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x8)

    #N0092
    NpcTalk(
        0x101,
        "ロイドの声",
        "#1Pワジ、いるか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x105,
        "#10300Fああ、遠慮なく入りなよ。\x02",
    )

    CloseMessageWindow()
    OP_68(98850, 1330, 122760, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_3F8E():
        OP_9B(0x0, 0xFE, 0x2, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F8E)

    def lambda_3FA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FA3)
    OP_68(99510, 1330, 125860, 3000)
    MoveCamera(33, 20, 0, 3000)
    SetCameraDistance(21500, 3000)
    Sleep(1000)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    OP_6F(0x79)
    Sleep(500)

    #C0094
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ。\x01",
            "そろそろ出発かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00004F#6Pああ、本部からの業務連絡も\x01",
            "今日は特に無かったからね。\x02\x03",

            "#00005Fっていうか、ワジ……\x01",
            "良さそうな椅子に座ってるな？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(99910, 1330, 128039, 2000)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 31)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0096
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10302Fああ、レミフェリア製の\x01",
            "コンフォートチェアでね。\x02\x03",

            "#10304F人間工学に基づいて\x01",
            "デザインされているから\x01",
            "すごく気持ちいいんだ。\x02\x03",

            "#10300F試しに座ってみるかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0097
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fえ、いいのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0098
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10309Fフフ、どうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    Sleep(500)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x105, 0x40)
    SetChrPos(0x105, 100240, 30, 128600, 192)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x105, 0x4)
    OP_0D()
    OP_93(0x105, 0xE1, 0x1F4)
    OP_95(0x105, 98960, 30, 128789, 1000, 0x0)

    def lambda_4200():

        label("loc_4200")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4200")

    QueueWorkItem2(0x105, 1, lambda_4200)
    Sleep(500)

    #C0099
    ChrTalk(
        0x101,
        "#00000Fえっと、それじゃあ──\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    SetCameraDistance(20500, 2500)
    OP_95(0x101, 100460, 30, 126150, 2000, 0x1)
    OP_95(0x101, 100420, 30, 128020, 2000, 0x0)
    EndChrThread(0x105, 0x1)
    OP_93(0x105, 0x3C, 0x0)
    Sleep(500)
    OP_6F(0x79)
    Fade(500)
    Sound(898, 0, 100, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 100590, 200, 129080, 225)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(1000)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x101,
        (
            "#00005Fあ……\x02\x03",

            "#00003F…………………………\x01",
            "………すごいな、これは。\x02\x03",

            "#00004F何ていうか、まるで身体が\x01",
            "包み込まれてるみたいだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#10302Fふふ、だろう？\x02\x03",

            "#10304Fま、こういうので\x01",
            "ストレスを解消するのも\x01",
            "必要な工夫ってわけさ。\x02\x03",

            "#10309F店のナンバーワンとしてはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00006Fそこはホストじゃなくて\x01",
            "支援課のハードな任務の疲れを\x01",
            "癒すためとか言ってくれよ……\x02\x03",

            "#00002Fあー……でもその水槽といい、\x01",
            "確かにリラックスできるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(100920, 1330, 128039, 2500)
    MoveCamera(45, 20, 0, 2500)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)
    OP_93(0x105, 0x78, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 33)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    #A0103
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fそういえば……\x01",
            "その水槽もワジの趣味なのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0104
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10305Fああ……\x02\x03",

            "#10304Fそれはどちらかというと\x01",
            "昔が懐かしかったから、かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)

    #C0105
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10305F……フフ、こちらの話さ。\x02\x03",

            "#10300Fそれよりここで\x01",
            "寛#2Rくつろ#いじゃっててもいいのかい？\x02\x03",

            "#10309F僕としては一向に構わないけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x40)
    SetChrPos(0x101, 100240, 30, 128600, 270)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    TurnDirection(0x101, 0x105, 0)
    OP_68(100140, 1330, 128180, 500)
    MoveCamera(45, 20, 0, 500)
    SetCameraDistance(21000, 500)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_64(0x101)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00011Fそ、そうだった！\x02\x03",

            "#00001Fみんな待ってるだろうし、\x01",
            "急いで行くぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        "#10304FＯＫ、リーダー。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジの家具を全て揃えた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrChipByIndex(0x105, 0xFF)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_478D")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_478D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_47A6")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_47A6")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 2)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 114, 0, 0)
    IdleLoop()

    label("loc_47C6")

    Return()

    # Function_36_3D2F end

    def Function_37_47C7(): pass

    label("Function_37_47C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E7")
    SetChrFlags(0x0, 0x8)

    label("loc_47E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47FA")
    SetChrFlags(0x1, 0x8)

    label("loc_47FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_480D")
    SetChrFlags(0x2, 0x8)

    label("loc_480D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4820")
    SetChrFlags(0x3, 0x8)

    label("loc_4820")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4833")
    SetChrFlags(0x4, 0x8)

    label("loc_4833")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4846")
    SetChrFlags(0x5, 0x8)

    label("loc_4846")

    ClearChrFlags(0x101, 0x8)
    Call(0, 38)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4861")
    ClearChrFlags(0x0, 0x8)

    label("loc_4861")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4874")
    ClearChrFlags(0x1, 0x8)

    label("loc_4874")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4887")
    ClearChrFlags(0x2, 0x8)

    label("loc_4887")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_489A")
    ClearChrFlags(0x3, 0x8)

    label("loc_489A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48AD")
    ClearChrFlags(0x4, 0x8)

    label("loc_48AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48C0")
    ClearChrFlags(0x5, 0x8)

    label("loc_48C0")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_37_47C7 end

    def Function_38_48D4(): pass

    label("Function_38_48D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5944")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis361.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis360.itp")
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    SoundLoad(3666)
    SoundLoad(3667)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_497A")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_497A")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x1)
    SetChrPos(0x101, 2400, 900, 125400, 180)
    SetMapObjFlags(0x8, 0x4)
    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その日、ロイドたちは\x01",
            "支援業務の合間に支援課に戻り──\x02",
        )
    )

    CloseMessageWindow()

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本部との定時連絡を取りがてら\x01",
            "各自休憩を入れることにした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(1820, 1830, 125210, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7102", 0)
    FadeToBright(1000, 0)
    OP_68(1820, 1330, 125210, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)

    #C0112
    ChrTalk(
        0x101,
        (
            "#05203Fふう……定時連絡も終わったし。\x02\x03",

            "#05209Fこのまま昼寝できたらいいんだけど\x01",
            "そういう訳にもいかないか……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(808, 0, 100, 0)
    Sleep(500)
    SetChrPos(0x9, -100, 0, 119480, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x1000)
    OP_C9(0x0, 0x80000000)

    #N0113
    NpcTalk(
        0x9,
        "キーアの声",
        (
            "#1P#3666Vねえねえ。\x01",
            "ロイド、いるー？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE52)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0x101, 0x3)
    Sleep(250)
    SetChrSubChip(0x101, 0x4)
    Sleep(150)
    SetChrSubChip(0x101, 0x5)
    Sleep(500)
    SetChrSubChip(0x101, 0x6)
    Sleep(1000)

    #C0114
    ChrTalk(
        0x101,
        "#05202Fああ、いるぞ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1)
    SetChrPos(0x101, 1280, 30, 125030, 225)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    OP_68(-420, 1330, 122210, 2500)
    OP_0D()
    OP_95(0x101, 400, 30, 123890, 2000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)
    OP_68(-170, 1330, 122810, 2000)

    def lambda_4C6A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4C6A)

    def lambda_4C7F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4C7F)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D67")

    #C0115
    ChrTalk(
        0x101,
        (
            "#05205F#1Pあれ、キーア、\x01",
            "出かけてたんだよな？\x02\x03",

            "#05203Fいったん戻ってきたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "#01100F#2Pあ、うん。\x01",
            "忘れ物があったからー。\x02\x03",

            "#01109Fそれでロイドの気配がしたから\x01",
            "いるのかなって思って。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D67")

    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0117
    ChrTalk(
        0x9,
        (
            "#01110F#2P#3667Vあ……！\x01",
            "なんか増えてる！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE53)
    OP_C9(0x1, 0x80000000)
    OP_68(-170, 1330, 125490, 4000)
    MoveCamera(45, 22, 0, 4000)

    def lambda_4DDC():

        label("loc_4DDC")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_4DDC")

    QueueWorkItem2(0x101, 1, lambda_4DDC)
    OP_95(0x9, -2180, 30, 126470, 2000, 0x0)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x2D, 0x1F4)
    OP_95(0x9, 10, 30, 127370, 2000, 0x0)
    SetChrSubChip(0x9, 0x0)
    Sleep(300)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_95(0x9, 400, 30, 125890, 2000, 0x0)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x101, 0x1)
    Sleep(500)

    #C0118
    ChrTalk(
        0x101,
        (
            "#05202Fはは……\x01",
            "さすがにちょっと珍しいか。\x02\x03",

            "#05204F普通に見かけることが\x01",
            "無いものだろうからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        "#01109Fうんっ！\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    OP_68(360, 1330, 128889, 2500)
    SetCameraDistance(21500, 2500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_4F18():
        OP_95(0xFE, 710, 0, 127430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4F18)
    Sleep(250)

    def lambda_4F35():
        OP_95(0xFE, -130, 30, 126060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F35)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x0)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 31)
    Sleep(1000)
    SetMessageWindowPos(16, 150, -1, -1)

    #A0120
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01105F？？？\x02\x03",

            "#01100Fこれって、そこにある\x01",
            "クルマと同じモケイだよね？\x02\x03",

            "#01103Fどーりょく飛行船とは\x01",
            "形が違うみたいだけどー。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0121
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05200Fああ、これは劇画に出てくる\x01",
            "架空の乗り物さ。\x02\x03",

            "#05203F『飛行機』って言って\x01",
            "導力を使わなくても\x01",
            "鳥みたいに空が飛べるんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0122
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01102Fへー……\x01",
            "ちょっと乗ってみたいかも。\x02\x03",

            "#01105Fあ、でもカクウっていうことは\x01",
            "本当は飛んでいないのー？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0123
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05205Fう、うーん、そうだと思うけど。\x02\x03",

            "#05203F導力を使わずに空を飛ぶなんて\x01",
            "普通は無理だと思うし……\x02\x03",

            "#05208F（いや……意外とどこかで\x01",
            "  開発されていたりするのか？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_63(0x9, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_93(0x9, 0x10E, 0x1F4)

    #C0124
    ChrTalk(
        0x9,
        "#01110Fねーねー、それじゃあアレは！？\x02",
    )

    CloseMessageWindow()
    OP_68(-1580, 1330, 126880, 2000)
    OP_93(0x101, 0x10E, 0x1F4)
    OP_6F(0x79)
    Sleep(500)
    Call(0, 33)
    Sleep(1000)
    SetMessageWindowPos(280, 150, -1, -1)

    #A0125
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05200Fああ、あれはサンドバッグさ。\x02\x03",

            "#05204F中に砂が入っていて\x01",
            "殴ったり蹴ったりできるんだ。\x02\x03",

            "#05202Fまあ、本格的な拳闘用じゃなくて\x01",
            "軽いトレーニング用のものだけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(16, 150, -1, -1)

    #A0126
    AnonymousTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#01103Fなるほどー。\x02\x03",

            "#01111Fそれじゃあ、叩いてもそんなに\x01",
            "痛くないように作ってあるんだね？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(280, 150, -1, -1)

    #A0127
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#05202Fそういうこと。\x02\x03",

            "#05204F（しかしホント、聡明というか\x01",
            "  どんどん賢くなってるなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    Sleep(500)

    #C0128
    ChrTalk(
        0x9,
        "#01101F#3Pよーし……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-830, 1330, 126920, 2000)
    SetCameraDistance(20500, 2000)
    TurnDirection(0x101, 0x9, 500)
    Sleep(500)
    OP_6F(0x79)

    #C0129
    ChrTalk(
        0x101,
        "#05205Fキーア？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0130
    ChrTalk(
        0x9,
        "#01107F#1Pロイド～～～っ！\x02",
    )

    CloseMessageWindow()
    OP_68(-1760, 1330, 126770, 500)
    SetCameraDistance(19500, 500)

    def lambda_5468():
        OP_95(0xFE, -2600, 0, 127600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5468)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_549D():

        label("loc_549D")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_549D")

    QueueWorkItem2(0x101, 1, lambda_549D)
    WaitChrThread(0x9, 1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x1, 0x50, 0x0, 0x8)
    Sound(811, 0, 100, 0)
    Sound(815, 0, 30, 0)
    Sound(114, 0, 40, 0)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    OP_9C(0x9, 0x1F4, 0x0, 0x0, 0xC8, 0xBB8)
    Sleep(1000)
    EndChrThread(0x101, 0x1)
    SetCameraDistance(20500, 2000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5527():
        OP_95(0xFE, -1770, 30, 126630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5527)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x9, 500)
    OP_64(0xFFFF)
    Sleep(1000)
    OP_6F(0x79)

    #C0131
    ChrTalk(
        0x101,
        (
            "#05211F#2Pお、おいおい。\x01",
            "キーア、大丈夫か？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    Sleep(500)
    SetChrChipByIndex(0x9, 0x2)
    OP_98(0x9, 0xC8, 0x0, 0x0, 0x3E8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_63(0x9, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    #C0132
    ChrTalk(
        0x9,
        (
            "#01109F#1Pあはははっ！\x01",
            "たのしーね、コレ！\x02\x03",

            "#01110Fキーア、けっこうスキかも！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#05209F#2Pはは、そっか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0134
    ChrTalk(
        0x101,
        (
            "#05204F#2P（そういえば……\x01",
            "  兄貴の部屋にもあったっけ。）\x02\x03",

            "（もっとデカくて重いやつで\x01",
            "  試しに殴ったら結構痛くて……）\x02\x03",

            "#05200F（うーん、せっかくだから\x01",
            "  本格的なものの方がいいかな？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(200)
    OP_63(0x9, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x9,
        (
            "#01102F#1Pねえねえ、ロイドがいない時に\x01",
            "遊ばせてもらってもいーい？\x02\x03",

            "#01109Fタックルする練習に\x01",
            "ちょーどよさそう！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x101,
        (
            "#05212F#2Pいいけど……\x01",
            "身体を痛めない程度にな？\x02\x03",

            "#05204F（はは……しばらくは\x01",
            "  これを使っておくか。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21500, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドの家具を全て揃えた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    OP_1F()
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x0, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_58B9")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_58B9")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58DA")
    ClearChrFlags(0x0, 0x8)

    label("loc_58DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58ED")
    ClearChrFlags(0x1, 0x8)

    label("loc_58ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5900")
    ClearChrFlags(0x2, 0x8)

    label("loc_5900")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5913")
    ClearChrFlags(0x3, 0x8)

    label("loc_5913")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5926")
    ClearChrFlags(0x4, 0x8)

    label("loc_5926")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5939")
    ClearChrFlags(0x5, 0x8)

    label("loc_5939")

    EventEnd(0x6)
    NewScene("c0120", 103, 0, 0)
    IdleLoop()

    label("loc_5944")

    Return()

    # Function_38_48D4 end

    def Function_39_5945(): pass

    label("Function_39_5945")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_597F")
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x9)
    Sleep(200)
    SetChrSubChip(0xFE, 0xA)
    Sleep(200)
    SetChrSubChip(0xFE, 0xB)
    Sleep(200)
    SetChrSubChip(0xFE, 0xA)
    Sleep(200)
    SetChrSubChip(0xFE, 0x9)
    Sleep(200)
    Jump("Function_39_5945")

    label("loc_597F")

    Return()

    # Function_39_5945 end

    def Function_40_5980(): pass

    label("Function_40_5980")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_59BA")
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    SetChrSubChip(0xFE, 0x6)
    Sleep(200)
    SetChrSubChip(0xFE, 0x7)
    Sleep(200)
    SetChrSubChip(0xFE, 0x6)
    Sleep(200)
    SetChrSubChip(0xFE, 0x5)
    Sleep(200)
    Jump("Function_40_5980")

    label("loc_59BA")

    Return()

    # Function_40_5980 end

    def Function_41_59BB(): pass

    label("Function_41_59BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51108.itc", 0x1E)
    LoadChrToIndex("apl/ch51109.itc", 0x1F)
    SoundLoad(128)
    SoundLoad(3600)
    SoundLoad(3601)
    SoundLoad(3602)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x3)
    SetChrPos(0x9, 2550, -100, 125550, 180)
    BeginChrThread(0x9, 3, 0, 39)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 3000, 150, 125900, 180)
    OP_7D(0xDC, 0xDC, 0xDC, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0xFF, "rhuton", 0x0, 0x1)
    OP_68(0, 1100, 131000, 0)
    MoveCamera(43, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18000, 0)
    Sound(883, 0, 70, 0)
    Sleep(2300)
    Sound(128, 2, 10, 0)
    Sleep(150)
    OP_25(0x80, 0x14)
    Sleep(150)
    OP_25(0x80, 0x1E)
    Sleep(150)
    OP_25(0x80, 0x28)
    Sleep(150)
    OP_25(0x80, 0x32)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0138
    AnonymousTalk(
        0x101,
        "#05206F#50W……んん……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(2800, 1100, 125650, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrSubChip(0x101, 0x0)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)

    #C0139
    ChrTalk(
        0x101,
        (
            "#05205F#5P#40W……今日は雨か……\x02\x03",

            "#05206Fそういえば雑誌の週間予報に\x01",
            "書いてあったような……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    #Sound(3026, 255, 80, 0)    #voice#KeA

    #N0140
    NpcTalk(
        0x9,
        "声",
        "#6P#60W#2S………んん～…………\x02",
    )

    CloseMessageWindow()
    OP_24(0xBD2)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0xFFFFFE0C, 1500, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x3)
    Sleep(100)
    SetChrSubChip(0x101, 0x4)
    Sleep(500)

    #C0141
    ChrTalk(
        0x101,
        "#05205F#5P#30Wもしかして……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16630, 700)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x0)

    def lambda_5C6C():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EA3C, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5C6C)
    SetChrSubChip(0x101, 0x5)
    Sleep(150)
    SetChrSubChip(0x101, 0x6)
    Sleep(150)
    SetChrSubChip(0x101, 0x7)
    WaitChrThread(0x9, 1)
    OP_79(0x8)
    OP_6F(0x79)
    Sleep(500)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0142
    ChrTalk(
        0x101,
        (
            "#05206F#11P#30Wキーア……\x01",
            "また入り込んできたのか。\x02\x03",

            "#05208F最近あんまり無かったけど\x01",
            "どうしたのかな……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x9, 0x3)
    SetChrSubChip(0x9, 0x3)
    Sleep(150)
    SetChrSubChip(0x9, 0x2)
    Sleep(150)
    SetChrSubChip(0x9, 0x1)
    Sleep(150)
    SetChrSubChip(0x9, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0143
    ChrTalk(
        0x9,
        "#05813F#3600V#6P#60W……んん～…………\x02",
    )

    CloseMessageWindow()
    OP_24(0xE10)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x9,
        (
            "#05809F#3601V#6P#60W……えへへ……\x01",
            "シズクー……こっちだよ～……\x02\x03",

            "#05813F#3602V#2S……ん……むにゃむにゃ…………\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE12)
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x9, 3, 0, 40)
    Sleep(800)

    #C0145
    ChrTalk(
        0x101,
        (
            "#05212F#11P#30Wはは……シズクちゃんと\x01",
            "遊んでる夢みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetChrSubChip(0x101, 0x8)
    Sleep(150)
    SetChrSubChip(0x101, 0x9)
    Sleep(500)

    #C0146
    ChrTalk(
        0x101,
        (
            "#05200F#11P#30Wまだ明け方だし……\x01",
            "もう少し俺も眠るか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetChrSubChip(0x101, 0x8)
    Sleep(150)
    SetChrSubChip(0x101, 0x7)
    Sleep(500)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0147
    ChrTalk(
        0x101,
        (
            "#05206F#11P#30W（Ｄ∴Ｇ教団の御子……\x01",
            "  ５００年前の時代の出身か。）\x02\x03",

            "#05208F（教団の残党が居なくなって\x01",
            "  危険が及ぶことも無くなった……）\x02\x03",

            "#05201F（もう家族も残っていない以上、\x01",
            "  下手に記憶を取り戻さない方が\x01",
            "  いいかもしれないけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x14, 0x0, 0x0, 0x0)

    def lambda_5FEF():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5FEF)

    def lambda_6009():
        OP_96(0xFE, 0xBB8, 0x96, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6009)
    SetChrSubChip(0x101, 0x7)
    Sleep(150)
    SetChrSubChip(0x101, 0x6)
    Sleep(150)
    SetChrSubChip(0x101, 0x5)
    Sleep(150)
    SetChrSubChip(0x101, 0x4)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    OP_79(0x8)
    Sleep(1800)

    #C0148
    ChrTalk(
        0x101,
        (
            "#05203F#11P#30W（……今はクロスベルの治安を\x01",
            "  守ることに専念しよう……）\x02\x03",

            "#05201F（この子たちが安心して暮らせる\x01",
            "  毎日を守るためにも……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x101, 0x3)
    SetCameraDistance(17630, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    ReplaceBGM("ed7150", "ed7000")
    Sleep(1000)
    SetScenarioFlags(0x22, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_59BB end

    def Function_42_611A(): pass

    label("Function_42_611A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51275.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
    OP_68(-2250, 1100, 67800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -2000, 10, 69500, 180)
    SetChrPos(0x102, -2000, 10, 68300, 270)
    SetChrPos(0x104, -1000, 0, 68300, 270)
    SetChrPos(0x109, -2500, 10, 67300, 270)
    SetChrPos(0x105, -1500, 10, 67300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_61FD():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_61FD)
    Sleep(200)

    def lambda_621A():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_621A)
    Sleep(200)

    def lambda_6237():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6237)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_6272():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6272)
    Sleep(400)

    def lambda_6286():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6286)
    Sleep(400)

    def lambda_629A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_629A)

    def lambda_62AB():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62AB)
    Sleep(300)

    def lambda_62C8():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62C8)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    #C0149
    ChrTalk(
        0x101,
        "#00003F#11P──なあ、ランディ。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x104, 0x101, 500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0150
    AnonymousTalk(
        0x104,
        "ん？　なんだロイド。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0151
    ChrTalk(
        0x101,
        (
            "#00008F#11Pその……\x01",
            "お父さんのことだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x104,
        (
            "#6P#00306Fああ、それか……\x02\x03",

            "#00300F別に気にすることはねぇぜ？\x01",
            "あの世界じゃ珍しくもねぇ話だ。\x02\x03",

            "それに、団を抜けた時に\x01",
            "俺と親父は縁を切っている。\x02\x03",

            "#00304F何も感じないわけじゃねぇが……\x01",
            "ま、サバサバしたもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00006F#11P……そっか。\x02\x03",

            "#00001Fでも、気が向いたら\x01",
            "色々と聞かせてくれよな？\x02\x03",

            "一応、リーダーとして\x01",
            "相談に乗れることがあるかも\x01",
            "しれないしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        "#6P#00305F………………………………\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        (
            "#00011F#11Pあ、ゴメン。\x01",
            "ちょっと生意気だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            "#6P#00304Fハハ、違う違う。\x02\x03",

            "#00302F何だかんだ言って\x01",
            "お前も成長してると思ってな。\x02\x03",

            "#00309Fうーん、お兄さん感慨深いぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6828")

    #C0157
    ChrTalk(
        0x101,
        "#00006F#11Pあのな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0158
    ChrTalk(
        0x101,
        (
            "#00008F#11P……その、こういう時は\x01",
            "何とか力にならせて欲しいんだ。\x02\x03",

            "#00000F頼りないかもしれないけど\x01",
            "それが“相棒”ってもんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#6P#00305Fロイド……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_6747():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6747)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x2)
    SetChrFlags(0x104, 0x10)
    SetChrFlags(0x104, 0x2)
    SetChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    Sleep(100)
    SetChrSubChip(0x104, 0x3)
    SetChrSubChip(0x101, 0x7)
    Sound(811, 0, 30, 0)
    Sleep(300)

    #C0160
    ChrTalk(
        0x104,
        (
            "#6P#00302F……分かった、いずれ話を\x01",
            "聞いてもらうかもしれねぇ。\x02\x03",

            "#00309Fそん時は頼むぜ──相棒。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#00002F#11Pああ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_68BA")

    label("loc_6828")


    #C0162
    ChrTalk(
        0x101,
        "#00006F#11Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#6P#00304F……ま、気が向いたら\x01",
            "相談するかもしれねぇ。\x02\x03",

            "#00300Fそん時はよろしく頼むぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#00000F#11Pああ……！\x02",
    )

    CloseMessageWindow()

    label("loc_68BA")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    #N0165
    NpcTalk(
        0x105,
        "ワジの声",
        "#2P#2Sあれ、何してるの？\x02",
    )

    CloseMessageWindow()

    #N0166
    NpcTalk(
        0x102,
        "エリィの声",
        "#2P#2S２人とも、忘れ物？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_69B1")
    SetCameraDistance(22500, 700)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x10)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)

    def lambda_6998():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6998)
    WaitChrThread(0x104, 1)

    label("loc_69B1")


    def lambda_69B6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_69B6)

    #C0167
    ChrTalk(
        0x101,
        "#00011F#11Pゴメン、すぐ行く！\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        (
            "#11P#00304Fそんじゃあボチボチ、\x01",
            "お仕事を始めるとすっか。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_6A2A():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A2A)
    Sleep(100)

    def lambda_6A47():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A47)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_6A6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6A6E)
    Sleep(400)

    def lambda_6A82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A82)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力車で、クロスベル全土に\x01",
            "移動することが可能になりました。\x02\x03",

            "西通りに出る特務支援課の裏口に\x01",
            "停めてあるので活用してみてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x140, 1)
    OP_C9(0x1, 0x1000)
    EventEnd(0x5)
    NewScene("c0200", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_42_611A end

    def Function_43_6B8E(): pass

    label("Function_43_6B8E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50005.itc", 0x1E)
    LoadChrToIndex("apl/ch50091.itc", 0x1F)
    LoadChrToIndex("apl/ch50092.itc", 0x20)
    LoadChrToIndex("apl/ch50011.itc", 0x21)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis030.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis226.itp")
    OP_68(50000, 1030, 127600, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 48600, 30, 125100, 90)
    SetChrPos(0x102, 51050, 30, 125000, 270)
    SetChrPos(0x103, 51050, 30, 126500, 225)
    SetChrPos(0x109, 50000, 0, 119000, 0)
    SetChrPos(0x105, 50000, 0, 119300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, 50000, 0, 119000, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 47300, 30, 126200, 135)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x1E)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 49700, 300, 125500, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x12)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 49800, 350, 125100, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetMapObjFrame(0xFF, "01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02", 0x1, 0x1)
    Sleep(500)
    Sound(886, 0, 80, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0170
    AnonymousTalk(
        0x101,
        "#00007F……くそっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7567", 0)
    OP_68(50000, 1030, 125100, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Sound(18, 0, 60, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ケリを付けて来る。\x01",
            "じゃあな。　　　　ランディ\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0172
    AnonymousTalk(
        0x103,
        "#00206F……そんな………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0173
    AnonymousTalk(
        0x102,
        (
            "#00106Fこ、こんな\x01",
            "書き置きだけ残して……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0174
    AnonymousTalk(
        0x101,
        (
            "#00008F……すっかり……\x01",
            "昨日の言葉に騙されたな……\x02\x03",

            "#00010Fクソッ……エニグマまで\x01",
            "置いて行くなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0175
    AnonymousTalk(
        0x9,
        "#01108F………ランディ…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sound(103, 0, 100, 0)

    def lambda_6F6F():
        OP_96(0xFE, 0xBEA0, 0x0, 0x1E1A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F6F)

    def lambda_6F89():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F89)
    Sleep(300)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_6FA5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6FA5)
    Sleep(100)

    def lambda_6FB5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FB5)

    def lambda_6FC2():
        OP_96(0xFE, 0xC2EC, 0x0, 0x1E078, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6FC2)

    def lambda_6FDC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6FDC)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)

    #C0176
    ChrTalk(
        0x109,
        (
            "#12P#10106Fダメです、周辺の人たちも\x01",
            "全然見かけていないみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#12P#10301F多分、人通りのない深夜に\x01",
            "出て行っちゃったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#00108F#5Pで、でも一体どこに……？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#5P#00201Fケリを付けてくるという事は\x01",
            "マインツ方面でしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ……\x01",
            "その可能性が高いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#12P#10107Fそれなら山道に展開している\x01",
            "警備隊からも連絡が……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    #N0182
    NpcTalk(
        0x8,
        "セルゲイの声",
        "#5P──そいつは望み薄だな。\x02",
    )

    CloseMessageWindow()
    OP_68(50280, 1130, 123880, 1500)

    def lambda_71AF():
        OP_96(0xFE, 0xC350, 0x0, 0x1DA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_71AF)

    def lambda_71C9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_71C9)
    Sleep(100)

    def lambda_71DD():

        label("loc_71DD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_71DD")

    QueueWorkItem2(0x109, 2, lambda_71DD)

    def lambda_71EF():

        label("loc_71EF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_71EF")

    QueueWorkItem2(0x101, 2, lambda_71EF)
    Sleep(100)

    def lambda_7204():

        label("loc_7204")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7204")

    QueueWorkItem2(0x105, 2, lambda_7204)

    def lambda_7216():

        label("loc_7216")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7216")

    QueueWorkItem2(0x102, 2, lambda_7216)

    def lambda_7228():

        label("loc_7228")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_7228")

    QueueWorkItem2(0x103, 2, lambda_7228)

    def lambda_723A():

        label("loc_723A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_723A")

    QueueWorkItem2(0x9, 2, lambda_723A)
    WaitChrThread(0x8, 1)

    #C0183
    ChrTalk(
        0x101,
        "#00011F#5P課長……\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x1F4)
    Sleep(500)
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(300)

    #C0184
    ChrTalk(
        0x8,
        (
            "#12P#01006Fったく、いつも散らかしてるクセに\x01",
            "妙に小奇麗にして行きやがって。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(49000, 1330, 125100, 3000)
    MoveCamera(48, 23, 0, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_72F4():
        OP_95(0xFE, 48000, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72F4)
    WaitChrThread(0x8, 1)

    def lambda_7312():
        OP_95(0xFE, 46900, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7312)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x9, 0x2)

    #C0185
    ChrTalk(
        0x8,
        (
            "#6P#01001F……警備隊にも問い合わせたが\x01",
            "ヤツの姿は確認されてないそうだ。\x02\x03",

            "多分、マインツに向かうにしても\x01",
            "真っ当なルートは使わねぇだろ。\x02\x03",

            "#01003Fあれでも百戦錬磨の元猟兵……\x01",
            "正規軍の目をくらますことは\x01",
            "幾らでもできるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x109,
        "#11P#10108Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00106F#11P……少しは私たちのことを\x01",
            "頼ってくれていると思ったのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        "#5P#00208F#5P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0189
    ChrTalk(
        0x105,
        (
            "#12P#10306F……ま、しばらく様子を\x01",
            "見るしかないかもしれないね。\x02\x03",

            "#10308F山岳地での軍事行動ほど\x01",
            "猟兵の得意分野は無いだろうし。\x02\x03",

            "#10301F追いかけようにも手がかりすら\x01",
            "見つからないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#00003F#11P──いや。\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_75C1():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_75C1)
    Sleep(50)

    def lambda_75D1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_75D1)
    Sleep(50)

    def lambda_75E1():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_75E1)
    Sleep(50)

    def lambda_75F1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75F1)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    Sleep(500)

    #C0191
    ChrTalk(
        0x105,
        "#12P#10305Fえ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00006F#5P多分、ランディも夜のうちには\x01",
            "マインツ方面には行ってないと思う。\x02\x03",

            "#00001Fひょっとしたら……\x01",
            "まだクロスベル市にいる\x01",
            "可能性すらあるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0193
    ChrTalk(
        0x102,
        "#00105F#11Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        "#12P#10105Fどうして分かるんですか！？\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#00003F#5P……簡単なことさ。\x02\x03",

            "#00008Fもしランディが本気で\x01",
            "《赤い星座》の武装活動を\x01",
            "何とかしようとしているなら……\x02\x03",

            "#00013F今のあいつの得物……\x01",
            "スタンハルバードだけで\x01",
            "何とかなると思うか？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        "#12P#10111Fあ……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x103,
        (
            "#5P#00206F……確かに。\x01",
            "どう考えても無理がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#6P#01003Fって事は、ヤツが猟兵時代に\x01",
            "使っていた何らかの武装……\x02\x03",

            "#01001Fそれを調達するのが先ってワケか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_7A82")

    #C0199
    ChrTalk(
        0x101,
        "#00001F#11Pはい……\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(50, 50, -1, -1)
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "……ったく、こんな事なら\x01",
            "アレを持ってくるんだったな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    VolumeBGM(0x64, 0x3E8)

    #C0201
    ChrTalk(
        0x101,
        (
            "#00003F#11P……ランディは昔、\x01",
            "かなりの火力の導力ライフルを\x01",
            "使っていたと言ってました。\x02\x03",

            "#00001Fそれをクロスベルのどこかに\x01",
            "保管しているみたいなんです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B65")

    label("loc_7A82")


    #C0202
    ChrTalk(
        0x101,
        (
            "#00003F#11Pはい……経歴から考えて\x01",
            "かなりの火力の重火器あたりに\x01",
            "通じていてもおかしくありません。\x02\x03",

            "#00008Fそれらを市内で調達するのは\x01",
            "決して不可能ではありませんし……\x02\x03",

            "#00001F昔の得物をどこかに\x01",
            "保管していた可能性もあります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B65")


    #C0203
    ChrTalk(
        0x8,
        "#6P#01003Fなるほどな……\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        (
            "#00102F#11Pそ、それじゃあ市内で\x01",
            "彼が立ち寄りそうな場所を\x01",
            "回ってみれば……！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#5P#00202Fランディさんの行方を\x01",
            "突き止められるかもしれない？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x109,
        (
            "#12P#10102F確かに……！\x01",
            "調べる価値はありそうです！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0207
    ChrTalk(
        0x101,
        "#00000F#5Pああ、そう思ってさ。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x105,
        "#12P#10300F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x105, 500)

    #C0209
    ChrTalk(
        0x101,
        (
            "#00001F#5Pワジ……\x01",
            "見当外れだと思うか？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#12P#10302Fいや、フフ……\x01",
            "さすがに予想外だと思ってさ。\x02\x03",

            "#10304F──いいんじゃない？\x01",
            "聞いてて成程と思ったよ。\x02\x03",

            "#10300Fそれで、彼が立ち寄るとしたら\x01",
            "市内のどこが怪しいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00008F#5Pそうだな……\x02\x03",

            "#00003F──やはり旧市街周辺が\x01",
            "一番怪しいかもしれない。\x02\x03",

            "#00001F交換屋のアシュリーさんは\x01",
            "裏で武器も扱ってるし……\x02\x03",

            "ギヨーム親方なんかも\x01",
            "重火器の扱いには詳しそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#5P#00203Fカジノのドレイク・オーナーも\x01",
            "何か知ってるかもしれませんね。\x02\x03",

            "#00201Fランディさん、しょっちゅう\x01",
            "遊びに行ってたみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x102,
        (
            "#00103F#11Pそうね……\x02\x03",

            "#00101Fそれに確か、ランディが\x01",
            "クロスベルに来た時以来の\x01",
            "知り合いじゃなかったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#6P#01004Fクク……ヤツも災難なこった。\x02\x03",

            "#01002F上手く撒#2Rま#いたつもりが\x01",
            "お前らにかかりゃ、あっという間に\x01",
            "尻尾を掴まれちまうんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x109,
        "#12P#10112Fふふっ、確かに。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#00006F#5P……当然です。\x02\x03",

            "#00013Fこんな勝手、リーダーとしても\x01",
            "許すわけにはいきません。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x4)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(500)

    #C0217
    ChrTalk(
        0x101,
        (
            "#00007F#6P何とか行き先を掴んで\x01",
            "絶対に連れ戻さないと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#5P#00203Fあたりきしゃりきです。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#00107F#11Pええ、首に縄をかけても\x01",
            "連れて帰りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        "#6P#01108F……ランディ、大丈夫なのー？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_81E5():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_81E5)
    Sleep(50)

    def lambda_81F5():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_81F5)
    Sleep(50)

    def lambda_8205():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8205)
    Sleep(50)

    def lambda_8215():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8215)
    Sleep(50)

    def lambda_8225():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8225)
    Sleep(50)

    def lambda_8235():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8235)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x8, 0)

    #C0221
    ChrTalk(
        0x101,
        (
            "#00002F#11Pああ……\x01",
            "絶対に連れて帰ってくるから！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#00109F#11Pええ、何も心配いらないわ。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x103,
        (
            "#11P#00202Fキーアはツァイトと一緒に\x01",
            "お留守番をしていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        (
            "#6P#01122F……うんっ。\x02\x03",

            "#01121Fロイドたちも……\x01",
            "くれぐれも気をつけてね！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7150", "ed7151")
    ReplaceBGM("ed7101", "ed7151")
    SetScenarioFlags(0x165, 5)
    SetScenarioFlags(0x23, 2)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_6B8E end

    SaveToFile()

Try(main)
