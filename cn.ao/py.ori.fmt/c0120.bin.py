from ScenarioHelper import *

def main():
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
        "赛尔盖科长",             # 1
        "琪雅",                   # 2
        "信",                     # 3
        "艾尼格玛",               # 4
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
        "Function_4_BEA",          # 04, 4
        "Function_5_C4F",          # 05, 5
        "Function_6_1116",         # 06, 6
        "Function_7_13C1",         # 07, 7
        "Function_8_140C",         # 08, 8
        "Function_9_1457",         # 09, 9
        "Function_10_14F8",        # 0A, 10
        "Function_11_1599",        # 0B, 11
        "Function_12_15E8",        # 0C, 12
        "Function_13_1840",        # 0D, 13
        "Function_14_1ABE",        # 0E, 14
        "Function_15_1CD0",        # 0F, 15
        "Function_16_1EEE",        # 10, 16
        "Function_17_1F41",        # 11, 17
        "Function_18_213C",        # 12, 18
        "Function_19_233D",        # 13, 19
        "Function_20_253F",        # 14, 20
        "Function_21_2741",        # 15, 21
        "Function_22_27E0",        # 16, 22
        "Function_23_287F",        # 17, 23
        "Function_24_291E",        # 18, 24
        "Function_25_29D1",        # 19, 25
        "Function_26_2A82",        # 1A, 26
        "Function_27_2B2F",        # 1B, 27
        "Function_28_2BEB",        # 1C, 28
        "Function_29_2C9A",        # 1D, 29
        "Function_30_2D4D",        # 1E, 30
        "Function_31_2DC2",        # 1F, 31
        "Function_32_2DF1",        # 20, 32
        "Function_33_2E20",        # 21, 33
        "Function_34_2E4F",        # 22, 34
        "Function_35_2E7E",        # 23, 35
        "Function_36_38DD",        # 24, 36
        "Function_37_42A7",        # 25, 37
        "Function_38_43B4",        # 26, 38
        "Function_39_52D7",        # 27, 39
        "Function_40_5312",        # 28, 40
        "Function_41_534D",        # 29, 41
        "Function_42_5A3C",        # 2A, 42
        "Function_43_6460",        # 2B, 43
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('特里斯坦号', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_551")
    Event(0, 14)

    label("loc_551")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你沙袋', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_578")
    Event(0, 15)

    label("loc_578")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    Event(0, 37)

    label("loc_5B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('点唱机', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E0")
    Event(0, 18)

    label("loc_5E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('冲浪板', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_607")
    Event(0, 17)

    label("loc_607")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('迷你水族馆', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E")
    Event(0, 20)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('安乐椅', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_655")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A79")

    #C0001
    ChrTalk(
        0x8,
        (
            "#01000F调查独立意向的居民投票活动逐渐临近，\x01",
            "送来了各种各样的文件。\x02\x03",

            "其中有些事项实在是令人在意……\x01",
            "算了，这些事情就交给其它科吧。\x02\x03",

            "总之，目前最重要的是危机管理。\x01",
            "除了去人偶工房探听消息之外，\x01",
            "你们也可以顺便处理一些支援请求。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_ADC")

    label("loc_A79")


    #C0002
    ChrTalk(
        0x8,
        (
            "#01000F哦，琪雅刚刚出去\x01",
            "买晚饭的材料了。\x02\x03",

            "还说要去图书馆看看……\x01",
            "你们要是担心，就去看看她吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADC")

    Jump("loc_BE6")

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_BE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B82")

    #C0003
    ChrTalk(
        0x8,
        (
            "#01000F哦，我刚刚才从\x01",
            "医院回来。\x02\x03",

            "#01003F你们就继续调查\x01",
            "『幻兽』吧。\x02\x03",

            "#01002F趁着『风之剑圣』无暇分身之机，\x01",
            "不妨多累积一些成绩。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BE6")

    label("loc_B82")


    #C0004
    ChrTalk(
        0x8,
        (
            "#01003F你们就继续调查\x01",
            "『幻兽』吧。\x02\x03",

            "#01002F趁着『风之剑圣』无暇分身之机，\x01",
            "不妨多累积一些成绩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE6")

    TalkEnd(0xFE)
    Return()

    # Function_3_976 end

    def Function_4_BEA(): pass

    label("Function_4_BEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_END)), "loc_C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C08")
    Call(0, 5)
    Jump("loc_C4B")

    label("loc_C08")


    #C0005
    ChrTalk(
        0x9,
        (
            "#01100F大家都要加油哦。\x02\x03",

            "#01109F琪雅会在这里\x01",
            "等着大家回来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4B")

    TalkEnd(0xFE)
    Return()

    # Function_4_BEA end

    def Function_5_C4F(): pass

    label("Function_5_C4F")

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
        "#00100F小琪雅……你在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x12C)

    #C0007
    ChrTalk(
        0x9,
        "#5P#01100F啊，嗯……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0008
    ChrTalk(
        0x9,
        (
            "#5P#01108F……兰迪在写\x01",
            "那封信的时候，\x01",
            "究竟怀着什么样的心情呢……\x02\x03",

            "#01103F他是不是打算……\x01",
            "以后再也不和我们见面了？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        "#12P#00205F琪雅……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10300F……兰迪要面对的敌人\x01",
            "非常强大。\x02\x03",

            "#10303F他恐怕已经下定决心，\x01",
            "抱着豁尽一切的觉悟去挑战了。\x02\x03",

            "#10308F哪怕要舍弃容身之处、同伴……\x01",
            "甚至自己的性命也在所不惜。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#11P#00003F……怎能允许他出于这种决心\x01",
            "而脱离支援科。\x02\x03",

            "艾莉、缇欧、兰迪……\x01",
            "诺艾尔、瓦吉、赛尔盖科长，\x01",
            "还有琪雅和蔡特……\x02\x03",

            "#00001F无论少了谁，\x01",
            "我们都不能称为『支援科』啊 。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#00104F罗伊德……你说的没错。\x02\x03",

            "#00108F但兰迪却完全不考虑这些，\x01",
            "自作主张地拿自己的生命去冒险……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        "#12P#00203F是啊，绝对应该严惩。\x02",
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
            "#12P#10100F别担心，小琪雅，\x01",
            "我们一定会把兰迪前辈带回来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，而且我们还\x01",
            "得到了有力的线索。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#5P#01110F嗯……\x02\x03",

            "#01104F……大家要加油啊。\x02\x03",

            "#01109F琪雅会在这里\x01",
            "等着大家回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#11P#00000F嗯，我们一定会和兰迪\x01",
            "一起回来的。\x02",
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

    # Function_5_C4F end

    def Function_6_1116(): pass

    label("Function_6_1116")

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
            "#12P#10302F欢迎来到我的城堡。\x01",
            "呵呵……请放松吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_120E")

    #C0020
    ChrTalk(
        0x1A5,
        "#5P#01105F哇，好漂亮的房间。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1239")

    label("loc_120E")


    #C0021
    ChrTalk(
        0x101,
        (
            "#5P#00005F这……\x01",
            "真是个雅致的房间啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1239")


    #C0022
    ChrTalk(
        0x109,
        (
            "#12P#10105F确、确实……\x01",
            "这个房间\x01",
            "看起来像样品间一样。\x02\x03",

            "#10106F该怎么说呢，\x01",
            "你适应环境的速度未免也太快了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#11P#00100F是啊，而且\x01",
            "这里的家具好像都是\x01",
            "价格昂贵的高档品……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，是托熟人\x01",
            "替我置办的。\x02\x03",

            "#10300F你们以后要是累了，\x01",
            "随时都可以来这里放松一下。\x02\x03",

            "机会难得，\x01",
            "我们把那瓶酒打开尝尝，\x01",
            "就当作是庆祝乔迁之喜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#5P#00006F那当然不行……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 100020, 30, 121290, 0)
    SetScenarioFlags(0x13B, 5)
    EventEnd(0x5)
    Return()

    # Function_6_1116 end

    def Function_7_13C1(): pass

    label("Function_7_13C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D3")
    Call(0, 12)
    Jump("loc_140B")

    label("loc_13D3")

    TalkBegin(0xFF)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00000F这是缇欧的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_140B")

    Return()

    # Function_7_13C1 end

    def Function_8_140C(): pass

    label("Function_8_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141E")
    Call(0, 13)
    Jump("loc_1456")

    label("loc_141E")

    TalkBegin(0xFF)

    #C0027
    ChrTalk(
        0x101,
        (
            "#00000F这是兰迪的房间，\x01",
            "还是不要随便进去了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_1456")

    Return()

    # Function_8_140C end

    def Function_9_1457(): pass

    label("Function_9_1457")

    EventBegin(0x1)

    #C0028
    ChrTalk(
        0x101,
        (
            "#00000F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",

            "科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#00100F说的也是，我们去叫她吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 800, 0, 1890, 0)
    EventEnd(0x4)
    Return()

    # Function_9_1457 end

    def Function_10_14F8(): pass

    label("Function_10_14F8")

    EventBegin(0x1)

    #C0030
    ChrTalk(
        0x101,
        (
            "#00000F……对了，琪雅今天\x01",
            "好像要去主日学校吧？\x02\x03",

            "科长已经出去了，\x01",
            "我们还是和她一起出门比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00100F说的也是，我们去叫她吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -2190, 0, 68010, 90)
    EventEnd(0x4)
    Return()

    # Function_10_14F8 end

    def Function_11_1599(): pass

    label("Function_11_1599")

    EventBegin(0x1)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00000F琪雅要去主日学校上课，\x01",
            "从后门出去比较近。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -1330, 0, 71380, 268)
    EventEnd(0x4)
    Return()

    # Function_11_1599 end

    def Function_12_15E8(): pass

    label("Function_12_15E8")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1682")
    SetChrPos(0x1A5, 169520, 0, 61730, 0)

    label("loc_1682")

    OP_0D()

    #C0033
    ChrTalk(
        0x102,
        "#6P#00100F这是缇欧的房间呢。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        (
            "#6P#10300F她现在正在\x01",
            "列曼自治州出差吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00000F嗯，她和约纳\x01",
            "一起去了爱普斯泰恩\x01",
            "财团的研究所。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#6P#00100F由于自治州法的修正，\x01",
            "导力网络在今后将会进一步普及，\x01",
            "他们好像正在准备那方面的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#11P#10103F听起来真是复杂……\x01",
            "看来他们那边的工作也很辛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1800")

    #C0038
    ChrTalk(
        0x1A5,
        "#12P#01100F真希望缇欧早点回来～\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1828")

    label("loc_1800")


    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F嗯，真希望她能\x01",
            "早日回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1828")

    OP_5A()
    SetChrPos(0x0, 169990, 0, 63110, 180)
    SetScenarioFlags(0x13B, 3)
    EventEnd(0x5)
    Return()

    # Function_12_15E8 end

    def Function_13_1840(): pass

    label("Function_13_1840")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18DA")
    SetChrPos(0x1A5, 13500, 0, 61420, 0)

    label("loc_18DA")

    OP_0D()

    #C0041
    ChrTalk(
        0x101,
        "#12P#00000F这是兰迪的房间。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#00100F兰迪现在正带领着\x01",
            "贝尔加德门的部队\x01",
            "进行复健训练吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10305F哦，据说是因为士兵们\x01",
            "在教团事件中被骗服了那种药物？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x109,
        (
            "#6P#10103F嗯……\x01",
            "虽然还没有严重到\x01",
            "会留下后遗症的程度……\x02\x03",

            "#10108F但想恢复原有的体力与手感，\x01",
            "似乎还需要花费一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#12P#00003F是吗……\x01",
            "希望警备队能尽快重振雄风啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A7E")

    #C0046
    ChrTalk(
        0x1A5,
        "#12P#01100F也希望兰迪早点回来。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#00100F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA6")

    label("loc_1A7E")


    #C0048
    ChrTalk(
        0x102,
        (
            "#00100F是啊，也希望兰迪\x01",
            "早日回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA6")

    OP_5A()
    SetChrPos(0x0, 14040, 0, 63300, 180)
    SetScenarioFlags(0x13B, 4)
    EventEnd(0x5)
    Return()

    # Function_13_1840 end

    def Function_14_1ABE(): pass

    label("Function_14_1ABE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x2)
    OP_68(-460, 1300, 127470, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B18")
    SetChrFlags(0x0, 0x8)

    label("loc_1B18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B2B")
    SetChrFlags(0x1, 0x8)

    label("loc_1B2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3E")
    SetChrFlags(0x2, 0x8)

    label("loc_1B3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B51")
    SetChrFlags(0x3, 0x8)

    label("loc_1B51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B64")
    SetChrFlags(0x4, 0x8)

    label("loc_1B64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B77")
    SetChrFlags(0x5, 0x8)

    label("loc_1B77")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B90")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_1B90")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -460, 0, 127470, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0049
    ChrTalk(
        0x101,
        "#0000F放在这里就可以了吧。\x02",
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
            "罗伊德的房间里\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('特里斯坦号', 1)
    SetScenarioFlags(0x13C, 0)
    OP_66(0x2, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C31")
    Call(0, 38)

    label("loc_1C31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C44")
    ClearChrFlags(0x0, 0x8)

    label("loc_1C44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C57")
    ClearChrFlags(0x1, 0x8)

    label("loc_1C57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6A")
    ClearChrFlags(0x2, 0x8)

    label("loc_1C6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C7D")
    ClearChrFlags(0x3, 0x8)

    label("loc_1C7D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C90")
    ClearChrFlags(0x4, 0x8)

    label("loc_1C90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CA3")
    ClearChrFlags(0x5, 0x8)

    label("loc_1CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1CBC")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_1CBC")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_14_1ABE end

    def Function_15_1CD0(): pass

    label("Function_15_1CD0")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D36")
    SetChrFlags(0x0, 0x8)

    label("loc_1D36")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D49")
    SetChrFlags(0x1, 0x8)

    label("loc_1D49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5C")
    SetChrFlags(0x2, 0x8)

    label("loc_1D5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D6F")
    SetChrFlags(0x3, 0x8)

    label("loc_1D6F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D82")
    SetChrFlags(0x4, 0x8)

    label("loc_1D82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D95")
    SetChrFlags(0x5, 0x8)

    label("loc_1D95")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DAE")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_1DAE")

    ClearChrFlags(0x101, 0x8)
    SetChrPos(0x101, -2420, 30, 126860, 315)
    FadeToBright(500, 0)
    OP_0D()

    #C0051
    ChrTalk(
        0x101,
        "#0000F放在这里就可以了吧。\x02",
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
            "罗伊德的房间里\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('迷你沙袋', 1)
    SetScenarioFlags(0x13C, 1)
    OP_66(0x3, 0x1)
    Call(0, 16)
    Call(0, 30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4F")
    Call(0, 38)

    label("loc_1E4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E62")
    ClearChrFlags(0x0, 0x8)

    label("loc_1E62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E75")
    ClearChrFlags(0x1, 0x8)

    label("loc_1E75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E88")
    ClearChrFlags(0x2, 0x8)

    label("loc_1E88")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E9B")
    ClearChrFlags(0x3, 0x8)

    label("loc_1E9B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EAE")
    ClearChrFlags(0x4, 0x8)

    label("loc_1EAE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EC1")
    ClearChrFlags(0x5, 0x8)

    label("loc_1EC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EDA")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_1EDA")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_15_1CD0 end

    def Function_16_1EEE(): pass

    label("Function_16_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F40")
    SetChrName("")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果得到了家具类道具，\x01",
            "可以放置在支援科各成员的房间中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x13B, 7)

    label("loc_1F40")

    Return()

    # Function_16_1EEE end

    def Function_17_1F41(): pass

    label("Function_17_1F41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x2)
    OP_68(49580, 1330, 129410, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F9B")
    SetChrFlags(0x0, 0x8)

    label("loc_1F9B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAE")
    SetChrFlags(0x1, 0x8)

    label("loc_1FAE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FC1")
    SetChrFlags(0x2, 0x8)

    label("loc_1FC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD4")
    SetChrFlags(0x3, 0x8)

    label("loc_1FD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE7")
    SetChrFlags(0x4, 0x8)

    label("loc_1FE7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FFA")
    SetChrFlags(0x5, 0x8)

    label("loc_1FFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2013")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_2013")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 49580, 30, 129410, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0054
    ChrTalk(
        0x104,
        "#0300F放在这里好了。\x02",
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
            "兰迪的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('冲浪板', 1)
    SetScenarioFlags(0x13C, 2)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x4, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B0")
    ClearChrFlags(0x0, 0x8)

    label("loc_20B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20C3")
    ClearChrFlags(0x1, 0x8)

    label("loc_20C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D6")
    ClearChrFlags(0x2, 0x8)

    label("loc_20D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E9")
    ClearChrFlags(0x3, 0x8)

    label("loc_20E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20FC")
    ClearChrFlags(0x4, 0x8)

    label("loc_20FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")
    ClearChrFlags(0x5, 0x8)

    label("loc_210F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2128")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2128")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_17_1F41 end

    def Function_18_213C(): pass

    label("Function_18_213C")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_219C")
    SetChrFlags(0x0, 0x8)

    label("loc_219C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21AF")
    SetChrFlags(0x1, 0x8)

    label("loc_21AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C2")
    SetChrFlags(0x2, 0x8)

    label("loc_21C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D5")
    SetChrFlags(0x3, 0x8)

    label("loc_21D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21E8")
    SetChrFlags(0x4, 0x8)

    label("loc_21E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21FB")
    SetChrFlags(0x5, 0x8)

    label("loc_21FB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2214")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_2214")

    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 52070, 30, 123440, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0056
    ChrTalk(
        0x104,
        "#0300F放在这里好了。\x02",
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
            "兰迪的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('点唱机', 1)
    SetScenarioFlags(0x13C, 3)
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x5, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22B1")
    ClearChrFlags(0x0, 0x8)

    label("loc_22B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22C4")
    ClearChrFlags(0x1, 0x8)

    label("loc_22C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22D7")
    ClearChrFlags(0x2, 0x8)

    label("loc_22D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22EA")
    ClearChrFlags(0x3, 0x8)

    label("loc_22EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22FD")
    ClearChrFlags(0x4, 0x8)

    label("loc_22FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2310")
    ClearChrFlags(0x5, 0x8)

    label("loc_2310")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2329")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_2329")

    SetChrPos(0x0, 49930, 0, 121070, 0)
    EventEnd(0x5)
    Return()

    # Function_18_213C end

    def Function_19_233D(): pass

    label("Function_19_233D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x2)
    OP_68(100680, 1330, 127820, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2397")
    SetChrFlags(0x0, 0x8)

    label("loc_2397")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23AA")
    SetChrFlags(0x1, 0x8)

    label("loc_23AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23BD")
    SetChrFlags(0x2, 0x8)

    label("loc_23BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D0")
    SetChrFlags(0x3, 0x8)

    label("loc_23D0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23E3")
    SetChrFlags(0x4, 0x8)

    label("loc_23E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23F6")
    SetChrFlags(0x5, 0x8)

    label("loc_23F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_240F")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_240F")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 100680, 30, 127820, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0058
    ChrTalk(
        0x105,
        "#10300F呵呵，就放在这里吧。\x02",
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
            "瓦吉的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('安乐椅', 1)
    SetScenarioFlags(0x13C, 4)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x6, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B3")
    ClearChrFlags(0x0, 0x8)

    label("loc_24B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C6")
    ClearChrFlags(0x1, 0x8)

    label("loc_24C6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24D9")
    ClearChrFlags(0x2, 0x8)

    label("loc_24D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24EC")
    ClearChrFlags(0x3, 0x8)

    label("loc_24EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FF")
    ClearChrFlags(0x4, 0x8)

    label("loc_24FF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2512")
    ClearChrFlags(0x5, 0x8)

    label("loc_2512")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_252B")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_252B")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_19_233D end

    def Function_20_253F(): pass

    label("Function_20_253F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x2)
    OP_68(101940, 1330, 125580, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2599")
    SetChrFlags(0x0, 0x8)

    label("loc_2599")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25AC")
    SetChrFlags(0x1, 0x8)

    label("loc_25AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25BF")
    SetChrFlags(0x2, 0x8)

    label("loc_25BF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D2")
    SetChrFlags(0x3, 0x8)

    label("loc_25D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E5")
    SetChrFlags(0x4, 0x8)

    label("loc_25E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F8")
    SetChrFlags(0x5, 0x8)

    label("loc_25F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2611")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_2611")

    ClearChrFlags(0x105, 0x8)
    SetChrPos(0x105, 101940, 30, 125580, 90)
    FadeToBright(500, 0)
    OP_0D()

    #C0060
    ChrTalk(
        0x105,
        "#10300F呵呵，就放在这里吧。\x02",
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
            "瓦吉的房间中\x01",
            "增添了新家具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SubItemNumber('迷你水族馆', 1)
    SetScenarioFlags(0x13C, 5)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_66(0x7, 0x1)
    Call(0, 16)
    Call(0, 30)
    Call(0, 36)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B5")
    ClearChrFlags(0x0, 0x8)

    label("loc_26B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C8")
    ClearChrFlags(0x1, 0x8)

    label("loc_26C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26DB")
    ClearChrFlags(0x2, 0x8)

    label("loc_26DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26EE")
    ClearChrFlags(0x3, 0x8)

    label("loc_26EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2701")
    ClearChrFlags(0x4, 0x8)

    label("loc_2701")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2714")
    ClearChrFlags(0x5, 0x8)

    label("loc_2714")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_272D")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_272D")

    SetChrPos(0x0, 100020, 30, 121290, 0)
    EventEnd(0x5)
    Return()

    # Function_20_253F end

    def Function_21_2741(): pass

    label("Function_21_2741")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C2")
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

    label("loc_27C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27DE")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_27DE")

    Return()

    # Function_21_2741 end

    def Function_22_27E0(): pass

    label("Function_22_27E0")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2861")
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

    label("loc_2861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_287D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_287D")

    Return()

    # Function_22_27E0 end

    def Function_23_287F(): pass

    label("Function_23_287F")

    OP_F4(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2900")
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

    label("loc_2900")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_291C")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_291C")

    Return()

    # Function_23_287F end

    def Function_24_291E(): pass

    label("Function_24_291E")

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
            "悬挂着特里斯坦号。\x02",
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

    # Function_24_291E end

    def Function_25_29D1(): pass

    label("Function_25_29D1")

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
            "摆放着迷你沙袋。\x02",
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

    # Function_25_29D1 end

    def Function_26_2A82(): pass

    label("Function_26_2A82")

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
            "挂着冲浪板。\x02",
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

    # Function_26_2A82 end

    def Function_27_2B2F(): pass

    label("Function_27_2B2F")

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
            "摆放着点唱机。\x02",
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

    # Function_27_2B2F end

    def Function_28_2BEB(): pass

    label("Function_28_2BEB")

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
            "摆放着安乐椅。\x02",
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

    # Function_28_2BEB end

    def Function_29_2C9A(): pass

    label("Function_29_2C9A")

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
            "摆放着迷你水族馆。\x02",
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

    # Function_29_2C9A end

    def Function_30_2D4D(): pass

    label("Function_30_2D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13D, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC1")
    OP_E0(0x16, 0x0)

    label("loc_2DC1")

    Return()

    # Function_30_2D4D end

    def Function_31_2DC2(): pass

    label("Function_31_2DC2")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_31_2DC2 end

    def Function_32_2DF1(): pass

    label("Function_32_2DF1")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Return()

    # Function_32_2DF1 end

    def Function_33_2E20(): pass

    label("Function_33_2E20")

    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_33_2E20 end

    def Function_34_2E4F(): pass

    label("Function_34_2E4F")

    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Return()

    # Function_34_2E4F end

    def Function_35_2E7E(): pass

    label("Function_35_2E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38DC")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis366.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis367.itp")
    LoadChrToIndex("chr/ch00302.itc", 0x1E)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x104, 51750, 130, 125650, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F30")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_2F30")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F49")
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)

    label("loc_2F49")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "某日，罗伊德一行人趁着\x01",
            "支援工作的余暇回到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与总部进行过定时联络后，\x01",
            "众人各自休息片刻。\x02",
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
        "罗伊德的声音",
        "#1P兰迪，我可以进来吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x104, 0x1)
    Sleep(500)

    #C0071
    ChrTalk(
        0x104,
        "#00300F哦，可以啊。\x02",
    )

    CloseMessageWindow()
    OP_68(49870, 1300, 123830, 1500)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_30CA():
        OP_9B(0x0, 0xFE, 0xA, 0x1130, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30CA)

    def lambda_30DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30DF)
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
        "#00300F怎么，这就要出发了吗？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#00004F是啊，今天总部\x01",
            "也没什么特别的工作联络。\x02\x03",

            "#00001F……那个，你应该没有\x01",
            "趁机喝酒吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#00309F呃……\x01",
            "哎呀，才没有那种事啦。\x02\x03",

            "#00300F好，那我们\x01",
            "赶紧出发吧！\x02",
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
            "#00006F真是的……\x02\x03",

            "#00000F（话虽如此，但他在工作时其实相当认真，\x01",
            "  所以并不用很担心。）\x02",
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
            "#00005F说起来……\x01",
            "好像多了不少东西啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(50440, 2200, 131009, 3000)
    MoveCamera(30, 25, 0, 3000)
    SetCameraDistance(21000, 3000)

    def lambda_330C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_330C)
    Sleep(200)

    def lambda_331C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_331C)
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
            "#00000F那个是……\x01",
            "冲浪板吧？\x02",
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
            "#00303F是啊，那东西原本\x01",
            "只能在海边使用……\x02\x03",

            "#00300F但艾鲁姆湖的浪也挺大，\x01",
            "应该还是可以玩玩的。\x02\x03",

            "#00309F可以去试试所谓的湖上冲浪。\x02",
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
            "#00002F原来如此，你好像\x01",
            "很喜欢这类娱乐。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 32)
    OP_68(50390, 2200, 122310, 4000)
    MoveCamera(60, 25, 0, 4000)
    Sleep(1500)

    def lambda_3459():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3459)
    Sleep(200)

    def lambda_3469():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3469)
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
            "#00005F这个……\x01",
            "又是什么呢？\x02\x03",

            "#00003F好像在杂志上\x01",
            "见到过类似的东西。\x02",
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
            "#00300F这是投币式点唱机。\x02\x03",

            "#00303F只要投进一枚十米拉的硬币，\x01",
            "就可以播放你喜欢的曲子……\x02\x03",

            "#00302F有些偏僻的小酒馆里\x01",
            "会摆放这种设备。\x02",
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
            "#00004F……这东西真不错啊。\x02\x03",

            "#00003F该怎么说呢……\x01",
            "让人有一种非常怀旧的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#00304F哈哈，虽然在克洛斯贝尔地区\x01",
            "不是很常见……\x02\x03",

            "#00302F但在没有其它娱乐方式的\x01",
            "乡下小酒馆，\x01",
            "这可以算是必备的设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00005F这样啊……\x02\x03",

            "#00000F兰迪以前常去的\x01",
            "酒馆里也有这个吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#00300F嗯，是啊。\x02\x03",

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
        "#00005F兰迪？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#00304F……哈哈，没什么。\x02\x03",

            "#00300F差不多也该出发啦，\x01",
            "大小姐她们还在等我们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00000F是啊，我们走吧。\x02",
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
            "兰迪的家具全部集齐了！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_389D")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_389D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_38B6")
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)

    label("loc_38B6")

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

    label("loc_38DC")

    Return()

    # Function_35_2E7E end

    def Function_36_38DD(): pass

    label("Function_36_38DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42A6")
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3995")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_3995")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_39AE")
    ClearChrFlags(0x105, 0x80)
    ClearChrBattleFlags(0x105, 0x8000)

    label("loc_39AE")

    StopBGM(0xBB8)
    SetChrName("")
    SetMessageWindowPos(14, 280, 60, 3)

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "某日，罗伊德一行人趁着\x01",
            "支援工作的余暇回到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与总部进行过定时联络后，\x01",
            "众人各自休息片刻。\x02",
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
        "罗伊德的声音",
        "#1P瓦吉，在吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x105,
        "#10300F嗯，不用客气，进来吧。\x02",
    )

    CloseMessageWindow()
    OP_68(98850, 1330, 122760, 2000)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_3B2A():
        OP_9B(0x0, 0xFE, 0x2, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B2A)

    def lambda_3B3F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B3F)
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
            "#10306F哎呀呀，\x01",
            "要出发了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#00004F#6P是啊，今天总部\x01",
            "也没什么特别的工作联络。\x02\x03",

            "#00005F话说回来，瓦吉……\x01",
            "你坐的椅子好像挺不错啊。\x02",
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
            "#10302F嗯，这可是雷米菲利亚制造的\x01",
            "安乐椅哦。\x02\x03",

            "#10304F它是基于人体工学\x01",
            "设计的，\x01",
            "所以坐起来很舒服。\x02\x03",

            "#10300F要不要坐坐看？\x02",
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
            "#00005F哎，可以吗？\x02",
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
            "#10309F呵呵，请吧。\x02",
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

    def lambda_3D56():

        label("loc_3D56")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3D56")

    QueueWorkItem2(0x105, 1, lambda_3D56)
    Sleep(500)

    #C0099
    ChrTalk(
        0x101,
        "#00000F嗯，那我就……\x02",
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
            "#00005F啊……\x02\x03",

            "#00003F…………………………\x01",
            "………好舒服啊。\x02\x03",

            "#00004F该怎么说呢，感觉整个身体\x01",
            "都被包裹住了……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，感觉不错吧？\x02\x03",

            "#10304F为了有效\x01",
            "缓解压力，\x01",
            "这可是很必要的。\x02\x03",

            "#10309F毕竟我是店里的头牌嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00006F在这种时候就别再提男公关的工作了，\x01",
            "至少说是为了缓解支援科的\x01",
            "辛苦工作造成的疲劳吧……\x02\x03",

            "#00002F啊……那个鱼缸\x01",
            "也让人觉得很放松呢。\x02",
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
            "#00005F说起来……\x01",
            "养鱼也是瓦吉的兴趣吗？\x02",
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
            "#10305F是啊……\x02\x03",

            "#10304F硬要说的话，\x01",
            "其实是为了缅怀过去吧。\x02",
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
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10305F……呵呵，没什么，只是我自己的事情。\x02\x03",

            "#10300F不说这些了，倒是你，\x01",
            "一直在这里休息，没问题吗？\x02\x03",

            "#10309F虽然我完全都不介意。\x02",
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
            "#00011F对、对啊！\x02\x03",

            "#00001F大家应该已经在等我们了，\x01",
            "赶快走吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x105,
        "#10304F是，队长。\x02",
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
            "瓦吉的家具全部集齐了！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_426D")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_426D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4286")
    SetChrFlags(0x105, 0x80)
    SetChrBattleFlags(0x105, 0x8000)

    label("loc_4286")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 2)
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    EventEnd(0x6)
    NewScene("c0120", 114, 0, 0)
    IdleLoop()

    label("loc_42A6")

    Return()

    # Function_36_38DD end

    def Function_37_42A7(): pass

    label("Function_37_42A7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42C7")
    SetChrFlags(0x0, 0x8)

    label("loc_42C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42DA")
    SetChrFlags(0x1, 0x8)

    label("loc_42DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42ED")
    SetChrFlags(0x2, 0x8)

    label("loc_42ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4300")
    SetChrFlags(0x3, 0x8)

    label("loc_4300")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4313")
    SetChrFlags(0x4, 0x8)

    label("loc_4313")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4326")
    SetChrFlags(0x5, 0x8)

    label("loc_4326")

    ClearChrFlags(0x101, 0x8)
    Call(0, 38)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4341")
    ClearChrFlags(0x0, 0x8)

    label("loc_4341")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4354")
    ClearChrFlags(0x1, 0x8)

    label("loc_4354")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4367")
    ClearChrFlags(0x2, 0x8)

    label("loc_4367")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_437A")
    ClearChrFlags(0x3, 0x8)

    label("loc_437A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_438D")
    ClearChrFlags(0x4, 0x8)

    label("loc_438D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43A0")
    ClearChrFlags(0x5, 0x8)

    label("loc_43A0")

    SetChrPos(0x0, 20, 30, 121010, 0)
    EventEnd(0x5)
    Return()

    # Function_37_42A7 end

    def Function_38_43B4(): pass

    label("Function_38_43B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13C, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52D6")
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis361.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis360.itp")
    LoadChrToIndex("apl/ch50106.itc", 0x1E)
    LoadChrToIndex("apl/ch50107.itc", 0x1F)
    LoadChrToIndex("apl/ch50380.itc", 0x20)
    SoundLoad(3666)
    SoundLoad(3667)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_445A")
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)

    label("loc_445A")

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
            "某日，罗伊德一行人趁着\x01",
            "支援工作的余暇回到了支援科。\x02",
        )
    )

    CloseMessageWindow()

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与总部进行过定时联络后，\x01",
            "众人各自休息片刻。\x02",
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
            "#05203F呼……定时联络已经结束。\x02\x03",

            "#05209F真想就这样睡个午觉，\x01",
            "但终究还是不行吧……\x02",
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
        "琪雅的声音",
        (
            "#1P#3666V罗伊德，\x01",
            "在吗在吗？\x02",
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
        "#05202F哦，在啊。\x02",
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

    def lambda_4714():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4714)

    def lambda_4729():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4729)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F7")

    #C0115
    ChrTalk(
        0x101,
        (
            "#05205F#1P哎，琪雅，\x01",
            "你不是出去了吗？\x02\x03",

            "#05203F怎么又回来了？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "#01100F#2P啊……嗯，\x01",
            "因为我忘了带东西。\x02\x03",

            "#01109F然后，感觉罗伊德好像回来了，\x01",
            "就来看看你在不在。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47F7")

    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0117
    ChrTalk(
        0x9,
        (
            "#01110F#2P#3667V啊……！\x01",
            "多了一些东西呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0xE53)
    OP_C9(0x1, 0x80000000)
    OP_68(-170, 1330, 125490, 4000)
    MoveCamera(45, 22, 0, 4000)

    def lambda_486C():

        label("loc_486C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_486C")

    QueueWorkItem2(0x101, 1, lambda_486C)
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
            "#05202F哈哈……\x01",
            "很新鲜吧？\x02\x03",

            "#05204F这些都是比较\x01",
            "少见的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        "#01109F嗯！\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    OP_68(360, 1330, 128889, 2500)
    SetCameraDistance(21500, 2500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_4982():
        OP_95(0xFE, 710, 0, 127430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4982)
    Sleep(250)

    def lambda_499F():
        OP_95(0xFE, -130, 30, 126060, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_499F)
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

            "#01100F这个……跟那边的车一样，\x01",
            "都是模型吧？\x02\x03",

            "#01103F但外形和飞艇\x01",
            "好像不太一样。\x02",
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
            "#05200F嗯，这是出现在漫画中的\x01",
            "虚构交通工具。\x02\x03",

            "#05203F它叫做『飞机』，\x01",
            "就算不使用导力，\x01",
            "也可以像鸟一样在天上飞。\x02",
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
            "#01102F这样啊……\x01",
            "真想坐坐看呢。\x02\x03",

            "#01105F啊，不过……既然是虚构的，\x01",
            "那就说明它并不能飞吧？\x02",
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
            "#05205F唔……应该不能。\x02\x03",

            "#05203F在不使用导力的情况下飞上天，\x01",
            "一般来说，自然是不可能的……\x02\x03",

            "#05208F（但也不一定……说不定在某些地方\x01",
            "  已经发明出来了。）\x02",
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
        "#01110F啊，那个又是什么？！\x02",
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
            "#05200F哦，那是沙袋。\x02\x03",

            "#05204F里面装满了沙子，\x01",
            "可以用来拳打脚踢。\x02\x03",

            "#05202F不过，那并不是用于正式拳击训练的，\x01",
            "主要还是轻度锻炼使用。\x02",
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
            "#01103F原来如此。\x02\x03",

            "#01111F也就是说，就算打上去，\x01",
            "手也不会很疼吧？\x02",
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
            "#05202F没错。\x02\x03",

            "#05204F（话说回来，她的理解力好强啊，\x01",
            "  真是越来越聪明了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 34)
    Sleep(500)

    #C0128
    ChrTalk(
        0x9,
        "#01101F#3P好……\x02",
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
        "#05205F琪雅？\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0130
    ChrTalk(
        0x9,
        "#01107F#1P罗伊德～～～！\x02",
    )

    CloseMessageWindow()
    OP_68(-1760, 1330, 126770, 500)
    SetCameraDistance(19500, 500)

    def lambda_4E34():
        OP_95(0xFE, -2600, 0, 127600, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E34)
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4E69():

        label("loc_4E69")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_4E69")

    QueueWorkItem2(0x101, 1, lambda_4E69)
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

    def lambda_4EF3():
        OP_95(0xFE, -1770, 30, 126630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4EF3)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x9, 500)
    OP_64(0xFFFF)
    Sleep(1000)
    OP_6F(0x79)

    #C0131
    ChrTalk(
        0x101,
        (
            "#05211F#2P喂、喂喂，\x01",
            "琪雅，你没事吧？\x02",
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
            "#01109F#1P啊哈哈哈！\x01",
            "这个真好玩啊！\x02\x03",

            "#01110F琪雅也很喜欢呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#05209F#2P哈哈，是吗。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0134
    ChrTalk(
        0x101,
        (
            "#05204F#2P（说起来……\x01",
            "  大哥当年的房间里也有这个。）\x02\x03",

            "（那个更大更重，\x01",
            "  我曾试着打过，结果把手弄得很疼……）\x02\x03",

            "#05200F（唔……难得购置一件训练器具，\x01",
            "  也许还是买个正式些的更好吧？）\x02",
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
            "#01102F#1P罗伊德不在的时候，\x01",
            "我可以来玩这个吗？\x02\x03",

            "#01109F好像很适合\x01",
            "用来练习飞扑！\x02",
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
            "#05212F#2P可以是可以……\x01",
            "但可不要把自己弄痛哦。\x02\x03",

            "#05204F（哈哈……看来短时间内\x01",
            "  是不能把它换掉了。）\x02",
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
            "罗伊德的家具全部集齐了！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_524B")
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)

    label("loc_524B")

    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x12D, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_526C")
    ClearChrFlags(0x0, 0x8)

    label("loc_526C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_527F")
    ClearChrFlags(0x1, 0x8)

    label("loc_527F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5292")
    ClearChrFlags(0x2, 0x8)

    label("loc_5292")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52A5")
    ClearChrFlags(0x3, 0x8)

    label("loc_52A5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52B8")
    ClearChrFlags(0x4, 0x8)

    label("loc_52B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52CB")
    ClearChrFlags(0x5, 0x8)

    label("loc_52CB")

    EventEnd(0x6)
    NewScene("c0120", 103, 0, 0)
    IdleLoop()

    label("loc_52D6")

    Return()

    # Function_38_43B4 end

    def Function_39_52D7(): pass

    label("Function_39_52D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5311")
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
    Jump("Function_39_52D7")

    label("loc_5311")

    Return()

    # Function_39_52D7 end

    def Function_40_5312(): pass

    label("Function_40_5312")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_534C")
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
    Jump("Function_40_5312")

    label("loc_534C")

    Return()

    # Function_40_5312 end

    def Function_41_534D(): pass

    label("Function_41_534D")

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
        "#05206F#50W……嗯嗯……？\x02",
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
            "#05205F#5P#40W……今天下雨啊……\x02\x03",

            "#05206F说起来，杂志的天气周报中\x01",
            "好像写过……\x02",
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
        "声音",
        "#6P#60W#2S………嗯嗯…………\x02",
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
        "#05205F#5P#30W难道……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16630, 700)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x0)

    def lambda_55EC():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EA3C, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55EC)
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
            "#05206F#11P#30W琪雅……\x01",
            "你又钻进来了啊。\x02\x03",

            "#05208F最近已经很少这样了，\x01",
            "这是怎么了……？\x02",
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
        "#05813F#3600V#6P#60W……嗯嗯…………\x02",
    )

    CloseMessageWindow()
    OP_24(0xE10)
    OP_63(0x101, 0xFFFFFF38, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x9,
        (
            "#05809F#3601V#6P#60W……嘿嘿嘿……\x01",
            "滴……我在这边哦……\x02\x03",

            "#05813F#3602V#2S……嗯……呼呼…………\x02",
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
            "#05212F#11P#30W哈哈……好像正在做\x01",
            "和小滴一起玩的梦呢。\x02",
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
            "#05200F#11P#30W天刚蒙蒙亮……\x01",
            "我也再睡一会吧……\x02",
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
            "#05206F#11P#30W（Ｄ∴Ｇ教团的圣子……\x01",
            "  出生在五百年前的时代吗……）\x02\x03",

            "#05208F（教团的余党已经一个不剩，\x01",
            "  她也不会再遇到危险了……）\x02\x03",

            "#05201F（既然她已经没有任何家人，\x01",
            "  可能还是不要贸然让她\x01",
            "  恢复记忆为好……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x14, 0x0, 0x0, 0x0)

    def lambda_5923():
        OP_96(0xFE, 0x9F6, 0x64, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5923)

    def lambda_593D():
        OP_96(0xFE, 0xBB8, 0x96, 0x1EC30, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_593D)
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
            "#05203F#11P#30W（……现在就专心\x01",
            "  维护克洛斯贝尔的治安吧……）\x02\x03",

            "#05201F（这也是为了让这些孩子\x01",
            "　能够过上安心的生活……）\x02",
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

    # Function_41_534D end

    def Function_42_5A3C(): pass

    label("Function_42_5A3C")

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

    def lambda_5B1F():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B1F)
    Sleep(200)

    def lambda_5B3C():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5B3C)
    Sleep(200)

    def lambda_5B59():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5B59)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    VolumeBGM(0x50, 0x3E8)
    Sound(103, 0, 100, 0)
    Sleep(600)

    def lambda_5B94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5B94)
    Sleep(400)

    def lambda_5BA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5BA8)
    Sleep(400)

    def lambda_5BBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5BBC)

    def lambda_5BCD():
        OP_96(0xFE, 0xFFFFF448, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BCD)
    Sleep(300)

    def lambda_5BEA():
        OP_96(0xFE, 0xFFFFFA24, 0xA, 0x108D8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5BEA)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x104, 500)

    #C0149
    ChrTalk(
        0x101,
        "#00003F#11P那个……兰迪。\x02",
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
        "怎么了，罗伊德？\x02",
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
            "#00008F#11P该怎么说呢……\x01",
            "关于你的父亲……\x02",
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
            "#6P#00306F哦，那件事啊……\x02\x03",

            "#00300F其实我并不是很在意啦。\x01",
            "在那个世界里，这并不算什么稀罕事。\x02\x03",

            "而且，在离开猎兵团的时候，\x01",
            "我和父亲之间就已经没什么关系了。\x02\x03",

            "#00304F当然，肯定不会毫无感觉……\x01",
            "但却也觉得好像松了口气。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#00006F#11P……是吗。\x02\x03",

            "#00001F等你有心情的时候，\x01",
            "给我讲讲过去的事吧？\x02\x03",

            "说不定我能\x01",
            "以队长的角度\x01",
            "提出一些想法。\x02",
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
            "#00011F#11P啊，抱歉，\x01",
            "我是不是有些自以为是了？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            "#6P#00304F哈哈，没有没有。\x02\x03",

            "#00302F我只是在想，\x01",
            "你也成长了不少呢。\x02\x03",

            "#00309F嗯～哥哥我感慨颇深啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6104")

    #C0157
    ChrTalk(
        0x101,
        "#00006F#11P你可真是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0158
    ChrTalk(
        0x101,
        (
            "#00008F#11P……总之，在这种时候，\x01",
            "我很想为你做点什么。\x02\x03",

            "#00000F也许我现在还不够可靠，\x01",
            "但所谓的『搭档』，就是要互相依赖吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        "#6P#00305F罗伊德……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    SetCameraDistance(22000, 1000)

    def lambda_602D():
        OP_96(0xFE, 0xFFFFF736, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_602D)
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
            "#6P#00302F……明白了，我以后\x01",
            "或许会和你好好聊聊。\x02\x03",

            "#00309F到时就要麻烦你了哦──搭档。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        "#00002F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_6198")

    label("loc_6104")


    #C0162
    ChrTalk(
        0x101,
        "#00006F#11P你可真是……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x104,
        (
            "#6P#00304F……好啦，如果我以后有心情，\x01",
            "说不定会和你聊一聊。\x02\x03",

            "#00300F到时就要麻烦你了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        "#00000F#11P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_6198")

    SetChrPos(0x102, -7000, -2000, 68300, 270)
    SetChrPos(0x105, -7000, -2000, 67300, 270)

    #N0165
    NpcTalk(
        0x105,
        "瓦吉的声音",
        "#2P#2S哎？你们在干什么？\x02",
    )

    CloseMessageWindow()

    #N0166
    NpcTalk(
        0x102,
        "艾莉的声音",
        "#2P#2S你们两个忘带东西了吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6295")
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

    def lambda_627C():
        OP_96(0xFE, 0xFFFFF542, 0xA, 0x108D8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_627C)
    WaitChrThread(0x104, 1)

    label("loc_6295")


    def lambda_629A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_629A)

    #C0167
    ChrTalk(
        0x101,
        "#00011F#11P抱歉，马上就出发！\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        (
            "#11P#00304F好，不要着急，\x01",
            "慢慢处理工作吧。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x3E8)

    def lambda_6300():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6300)
    Sleep(100)

    def lambda_631D():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_631D)
    FadeToDark(1000, 0, -1)
    Sleep(400)

    def lambda_6344():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6344)
    Sleep(400)

    def lambda_6358():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6358)
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
            "从现在开始，可以驾驶导力车，快速驶往\x01",
            "克洛斯贝尔自治州内的各个地区了。\x02\x03",

            "导力车停在位于西街的特别任务支援科后门，\x01",
            "请多加利用。\x07\x00\x02",
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

    # Function_42_5A3C end

    def Function_43_6460(): pass

    label("Function_43_6460")

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
        "#00007F……可恶……！\x02",
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
            "我要去做个了断。\x01",
            "就这样，再见。　　　　兰迪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0172
    AnonymousTalk(
        0x103,
        "#00206F……怎么会这样………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0173
    AnonymousTalk(
        0x102,
        (
            "#00106F只、只留下\x01",
            "这种字条……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0174
    AnonymousTalk(
        0x101,
        (
            "#00008F……完全……\x01",
            "被他昨天的话骗了啊……\x02\x03",

            "#00010F可恶……他竟然连艾尼格玛\x01",
            "都留下了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0175
    AnonymousTalk(
        0x9,
        "#01108F………兰迪…………\x02",
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

    def lambda_6825():
        OP_96(0xFE, 0xBEA0, 0x0, 0x1E1A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6825)

    def lambda_683F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_683F)
    Sleep(300)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_685B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_685B)
    Sleep(100)

    def lambda_686B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_686B)

    def lambda_6878():
        OP_96(0xFE, 0xC2EC, 0x0, 0x1E078, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6878)

    def lambda_6892():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6892)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)

    #C0176
    ChrTalk(
        0x109,
        (
            "#12P#10106F我已经问过附近的人了，\x01",
            "谁都没有见过他……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#12P#10301F大概是在没有行人的深夜\x01",
            "离开的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#00108F#5P他、他到底去哪里了……？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#5P#00201F既然说是要去做个了断，\x01",
            "那应该是玛因兹那边吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00006F#5P是啊……\x01",
            "很有可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#12P#10107F既然如此，驻扎在山道的\x01",
            "警备队或许会有消息……！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    #N0182
    NpcTalk(
        0x8,
        "赛尔盖的声音",
        "#5P恐怕没什么希望。\x02",
    )

    CloseMessageWindow()
    OP_68(50280, 1130, 123880, 1500)

    def lambda_6A23():
        OP_96(0xFE, 0xC350, 0x0, 0x1DA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6A23)

    def lambda_6A3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6A3D)
    Sleep(100)

    def lambda_6A51():

        label("loc_6A51")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6A51")

    QueueWorkItem2(0x109, 2, lambda_6A51)

    def lambda_6A63():

        label("loc_6A63")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6A63")

    QueueWorkItem2(0x101, 2, lambda_6A63)
    Sleep(100)

    def lambda_6A78():

        label("loc_6A78")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6A78")

    QueueWorkItem2(0x105, 2, lambda_6A78)

    def lambda_6A8A():

        label("loc_6A8A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6A8A")

    QueueWorkItem2(0x102, 2, lambda_6A8A)

    def lambda_6A9C():

        label("loc_6A9C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6A9C")

    QueueWorkItem2(0x103, 2, lambda_6A9C)

    def lambda_6AAE():

        label("loc_6AAE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6AAE")

    QueueWorkItem2(0x9, 2, lambda_6AAE)
    WaitChrThread(0x8, 1)

    #C0183
    ChrTalk(
        0x101,
        "#00011F#5P科长……\x02",
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
            "#12P#01006F真是的，平时总是把这里搞得乱七八糟，\x01",
            "走之前却特意收拾得这么整洁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(49000, 1330, 125100, 3000)
    MoveCamera(48, 23, 0, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_6B6A():
        OP_95(0xFE, 48000, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6B6A)
    WaitChrThread(0x8, 1)

    def lambda_6B88():
        OP_95(0xFE, 46900, 0, 124800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6B88)
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
            "#6P#01001F……我已经问过警备队了，\x01",
            "他们也没有见过那家伙。\x02\x03",

            "就算他真的去了玛因兹，\x01",
            "大概也不会从大道走吧。\x02\x03",

            "#01003F他毕竟是身经百战的前猎兵……\x01",
            "要想瞒过正规军队的耳目，\x01",
            "应该是轻而易举的。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x109,
        "#11P#10108F这、这……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#00106F#11P……原本还以为他\x01",
            "多少已经在依靠我们了……\x02",
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
            "#12P#10306F……算啦，暂时也只能\x01",
            "观望一下情况了。\x02\x03",

            "#10308F在山岳地带展开军事行动\x01",
            "是猎兵最擅长的事情。\x02\x03",

            "#10301F就算要追，\x01",
            "我们恐怕也毫无头绪吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#00003F#11P不。\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_6DC9():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6DC9)
    Sleep(50)

    def lambda_6DD9():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6DD9)
    Sleep(50)

    def lambda_6DE9():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6DE9)
    Sleep(50)

    def lambda_6DF9():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6DF9)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    Sleep(500)

    #C0191
    ChrTalk(
        0x105,
        "#12P#10305F哎……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00006F#5P我觉得兰迪并没有\x01",
            "连夜赶往玛因兹地区。\x02\x03",

            "#00001F说不定……\x01",
            "他现在仍然身处\x01",
            "克洛斯贝尔市内。\x02",
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
        "#00105F#11P哎！？\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        "#12P#10105F你是怎么知道的？！\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#00003F#5P……很简单。\x02\x03",

            "#00008F如果兰迪真的\x01",
            "决心与『赤色星座』\x01",
            "对抗……\x02\x03",

            "#00013F光凭他现在的武器……\x01",
            "也就是那把冲击斧枪，\x01",
            "又能有什么收效呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        "#12P#10111F啊……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x103,
        (
            "#5P#00206F……确实如此。\x01",
            "无论怎么想，也太过勉强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#6P#01003F也就是说，\x01",
            "他在出发之前……\x02\x03",

            "#01001F要先去取回在猎兵时代曾使用过的某些武器装备。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_71F8")

    #C0199
    ChrTalk(
        0x101,
        "#00001F#11P是的……\x02",
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
            "……真是的，如果早知道会遇到这种事，\x01",
            "我就把那个东西给带来了。\x02",
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
            "#00003F#11P……兰迪说过，\x01",
            "他曾经用过一把火力相当\x01",
            "强大的导力来复枪。\x02\x03",

            "#00001F他似乎将那把枪保管在了\x01",
            "克洛斯贝尔的某个地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B3")

    label("loc_71F8")


    #C0202
    ChrTalk(
        0x101,
        (
            "#00003F#11P是的……从他过去的经历来考虑，\x01",
            "就算精通火力强大的重型武器\x01",
            "也不足为奇。\x02\x03",

            "#00008F虽然在市内购置那种东西\x01",
            "也不是不可能……\x02\x03",

            "#00001F但他或许把自己\x01",
            "过去的武器保管在了某个地方。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B3")


    #C0203
    ChrTalk(
        0x8,
        "#6P#01003F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        (
            "#00102F#11P既、既然如此，\x01",
            "我们只要以市内为搜索范围，\x01",
            "到他有可能会去的地方找一找……！\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#5P#00202F也许就可以查到\x01",
            "兰迪前辈的行踪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x109,
        (
            "#12P#10102F看来……\x01",
            "确实有调查的价值呢！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0207
    ChrTalk(
        0x101,
        "#00000F#5P嗯，我就是这么想的。\x02",
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
            "#00001F#5P瓦吉……\x01",
            "你认为我的猜测有误吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x105,
        (
            "#12P#10302F不，呵呵……\x01",
            "只是出乎我的预料而已。\x02\x03",

            "#10304F你推测得很好，\x01",
            "我听了之后恍然大悟。\x02\x03",

            "#10300F那么，说到他会去的场所，\x01",
            "市内哪些地方最有可能呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        (
            "#00008F#5P这个嘛……\x02\x03",

            "#00003F可能性最高的\x01",
            "显然还是旧城区一带吧。\x02\x03",

            "#00001F交换店的亚修莉女士\x01",
            "一直在暗地里买卖武器……\x02\x03",

            "而基约姆师傅好像也对\x01",
            "重型武器很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x103,
        (
            "#5P#00203F巴鲁卡的多雷克老板\x01",
            "说不定也知道些什么呢。\x02\x03",

            "#00201F毕竟兰迪前辈平时\x01",
            "总是去那里玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x102,
        (
            "#00103F#11P是啊……\x02\x03",

            "#00101F而且，在兰迪刚来\x01",
            "克洛斯贝尔的时候，\x01",
            "他们两个好像就认识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#6P#01004F呵呵……那家伙也真是不走运。\x02\x03",

            "#01002F本以为可以远走高飞，\x01",
            "可惜碰上了你们，\x01",
            "这么快就被揪住了尾巴。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x109,
        "#12P#10112F呵呵，确实如此。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#00006F#5P……当然。\x02\x03",

            "#00013F身为队长，我绝不允许\x01",
            "他这样擅自行动。\x02",
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
            "#00007F#6P我们一定要设法查到他的去向，\x01",
            "把他带回来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#5P#00203F那是当然的。\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x102,
        (
            "#00107F#11P嗯，就算在他的脖子上套根绳子，\x01",
            "也要把他给带回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        "#6P#01108F……兰迪不要紧吧？\x02",
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

    def lambda_786B():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_786B)
    Sleep(50)

    def lambda_787B():
        TurnDirection(0x103, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_787B)
    Sleep(50)

    def lambda_788B():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_788B)
    Sleep(50)

    def lambda_789B():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_789B)
    Sleep(50)

    def lambda_78AB():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_78AB)
    Sleep(50)

    def lambda_78BB():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_78BB)
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
            "#00002F#11P嗯……\x01",
            "我们一定会把他带回来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        "#00109F#11P嗯，不用担心。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x103,
        (
            "#11P#00202F琪雅就和蔡特一起\x01",
            "好好看家吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x9,
        (
            "#6P#01122F……嗯。\x02\x03",

            "#01121F罗伊德……\x01",
            "你们要多加小心啊！\x02",
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

    # Function_43_6460 end

    SaveToFile()

Try(main)
