from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1600.bin",                # FileName
        "t1600",                    # MapName
        "t1600",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1600",                  # 0
        "マーサ師長",             # 1
        "看護師シロン",           # 2
        "ヨアヒム准教授",         # 3
        "研修医リットン",         # 4
        "ダイソン用務員",         # 5
        "看護師メイファ",         # 6
        "観光客トッティ",         # 7
        "ウルスラ間道",           # 8
    ))

    AddCharChip((
        "chr/ch29600.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "chr/ch07100.itc",                   # 02
        "chr/ch29400.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch34200.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
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

    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4039,    7000,    2160,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(4019,    7000,    3849,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(3430,    7000,    -9159,   178,  389,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-25850,  6000,    14149,   270,  389,  0x0, 0,   5,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(13619,   7000,    280,     135,  385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 20,  -4.5,                  19.5,                  6.0,                   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.5,                   -3.9000000953674316,   -1.2000000476837158,   1.0])
    DeclEvent(0x0000, 0, 23,  15.0,                  -14.300000190734863,   6.0,                   729.0,                 [0.23570217192173004,  0.03928372263908386,   -0.0,                  0.0,                   -0.23570233583450317,  0.039283692836761475,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -6.906075954437256,    -0.02749902382493019,  -1.1999999284744263,   1.0])
    DeclEvent(0x0000, 0, 24,  -13.5,                 20.0,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -10.0,                 -1.100000023841858,    1.0])
    DeclEvent(0x0000, 0, 25,  -1.5,                  23.5,                  6.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.75,                  -11.75,                -1.3000000715255737,   1.0])
    DeclEvent(0x0000, 0, 26,  -22.5,                 23.5,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   11.25,                 -11.75,                -1.100000023841858,    1.0])

    DeclActor(28100,   7000,    -16700,  2000,    28100,   8000,    -16700,  0x007C, 0,  15, 0x0000)
    DeclActor(3300,    7000,    0,       2000,    3300,    8000,    0,       0x007C, 0,  16, 0x0000)
    DeclActor(22500,   7000,    13500,   2000,    22500,   8000,    13500,   0x007C, 0,  17, 0x0000)
    DeclActor(-9300,   7000,    18100,   2000,    -9300,   8000,    18100,   0x007C, 0,  18, 0x0000)
    DeclActor(-30000,  6000,    17000,   2000,    -30000,  7000,    17000,   0x007C, 0,  19, 0x0000)
    DeclActor(17500,   7000,    -3000,   2000,    18000,   8000,    -3000,   0x007C, 0,  14, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_5EC",          # 01, 1
        "Function_2_617",          # 02, 2
        "Function_3_642",          # 03, 3
        "Function_4_818",          # 04, 4
        "Function_5_9C2",          # 05, 5
        "Function_6_B6E",          # 06, 6
        "Function_7_1478",         # 07, 7
        "Function_8_1613",         # 08, 8
        "Function_9_17C5",         # 09, 9
        "Function_10_1EFA",        # 0A, 10
        "Function_11_2022",        # 0B, 11
        "Function_12_242F",        # 0C, 12
        "Function_13_24B6",        # 0D, 13
        "Function_14_25C5",        # 0E, 14
        "Function_15_2B03",        # 0F, 15
        "Function_16_2CB4",        # 10, 16
        "Function_17_2E5F",        # 11, 17
        "Function_18_3014",        # 12, 18
        "Function_19_315F",        # 13, 19
        "Function_20_32FC",        # 14, 20
        "Function_21_358B",        # 15, 21
        "Function_22_35FB",        # 16, 22
        "Function_23_3650",        # 17, 23
        "Function_24_3E07",        # 18, 24
        "Function_25_40AC",        # 19, 25
        "Function_26_40C8",        # 1A, 26
        "Function_27_40E4",        # 1B, 27
    ))


    def Function_0_534(): pass

    label("Function_0_534")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_574"),
        (1, "loc_580"),
        (2, "loc_58C"),
        (3, "loc_598"),
        (4, "loc_5A4"),
        (5, "loc_5B0"),
        (6, "loc_5BC"),
        (SWITCH_DEFAULT, "loc_5C8"),
    )


    label("loc_574")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_580")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_58C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_598")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D4")

    label("loc_5EB")

    Return()

    # Function_0_534 end

    def Function_1_5EC(): pass

    label("Function_1_5EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_616")
    OP_94(0xFE, 0xFFFFF4A2, 0x49DE, 0xFFFFFD58, 0x5172, 0x3E8)
    Sleep(500)
    Jump("Function_1_5EC")

    label("loc_616")

    Return()

    # Function_1_5EC end

    def Function_2_617(): pass

    label("Function_2_617")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_641")
    OP_94(0xFE, 0x1FF4, 0xFFFFEB2E, 0x2EEA, 0xFFFFFE84, 0x3E8)
    Sleep(500)
    Jump("Function_2_617")

    label("loc_641")

    Return()

    # Function_2_617 end

    def Function_3_642(): pass

    label("Function_3_642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_650")
    Jump("loc_804")

    label("loc_650")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_679")
    SetChrPos(0x9, -27540, 6000, 14130, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_804")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_691")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6A9")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_804")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6D3")
    SetChrPos(0x9, -1790, 7000, 19910, 180)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_804")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6FC")
    SetChrPos(0x9, -27200, 6000, 20220, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_6FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_714")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_722")
    Jump("loc_804")

    label("loc_722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_73A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_73A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_79C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_76F")
    SetChrPos(0xA, 4040, 7000, 2160, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_797")

    label("loc_76F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_797")
    SetChrPos(0xB, 10930, 7000, -2350, 180)
    BeginChrThread(0xB, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)

    label("loc_797")

    Jump("loc_804")

    label("loc_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7AF")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_7AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7C2")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_804")

    label("loc_7C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_7DA")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_804")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_7E8")
    Jump("loc_804")

    label("loc_7E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7F6")
    Jump("loc_804")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_804")
    ClearChrFlags(0x8, 0x80)

    label("loc_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_817")
    ClearChrFlags(0xE, 0x80)

    label("loc_817")

    Return()

    # Function_3_642 end

    def Function_4_818(): pass

    label("Function_4_818")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_835")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_848")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_848")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_87E")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_87E")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B0")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    Jump("loc_903")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8DC")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    Jump("loc_903")

    label("loc_8DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_903")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_945")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    Jump("loc_979")

    label("loc_945")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_979")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_991")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_991")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9A9")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_9A9")

    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9C1")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_9C1")

    Return()

    # Function_4_818 end

    def Function_5_9C2(): pass

    label("Function_5_9C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B33")
    OP_93(0xFE, 0x0, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0001
    ChrTalk(
        0xFE,
        (
            "おや……\x01",
            "あんたたち、誰か探してるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0005Fえっと、病院に勤めている\x01",
            "知り合いを呼び出そうと、\x01",
            "受付に向かっているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "おやまぁ、\x01",
            "随分と見当違いな所を\x01",
            "歩いているじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "受付は病棟の１階ロビーさ。\x01",
            "ほれ、戻った戻った。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000Fああ、そうでしたか。\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B6A")

    label("loc_B33")


    #C0006
    ChrTalk(
        0xFE,
        (
            "受付なら病棟の１階ロビーさ。\x01",
            "ほれ、戻った戻った。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6A")

    TalkEnd(0xFE)
    Return()

    # Function_5_9C2 end

    def Function_6_B6E(): pass

    label("Function_6_B6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B7F")
    Jump("loc_1474")

    label("loc_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9A")
    Call(0, 7)
    Jump("loc_C12")

    label("loc_B9A")


    #C0007
    ChrTalk(
        0xFE,
        (
            "メイファちゃんって、\x01",
            "なんだかんだ言って私のミスを\x01",
            "フォローしてくれるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "うふふ、いい友達を持ってよかった。\x02",
    )

    CloseMessageWindow()

    label("loc_C12")

    Jump("loc_1474")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D24")

    #C0009
    ChrTalk(
        0xFE,
        (
            "シーツの発注書を書き間違えてるって、\x01",
            "またメイファちゃんに怒られちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "５０枚じゃ少ないと思って\x01",
            "０をひとつ足しただけだったのにー。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "でも、いいの。\x01",
            "間違いはいちいち\x01",
            "気に病まないことにしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "どんまいどんまい、わたし！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DAF")

    label("loc_D24")


    #C0013
    ChrTalk(
        0xFE,
        (
            "またメイファちゃんに\x01",
            "怒られちゃったけど……\x01",
            "気にしないことにしたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "間違いはいちいち気に病まないの。\x01",
            "どんまいどんまい、わたし！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAF")

    Jump("loc_1474")

    label("loc_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E59")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")
    Call(0, 8)
    Jump("loc_E54")

    label("loc_DD0")


    #C0015
    ChrTalk(
        0xFE,
        (
            "メイファちゃんったら、\x01",
            "また私を叱りつけたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "配達物をキチンと保存してただけなのに……\x01",
            "何で怒られなきゃなんないのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E54")

    Jump("loc_1474")

    label("loc_E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4D")

    #C0017
    ChrTalk(
        0xFE,
        (
            "うーん、走ってた子供に\x01",
            "ぶつかっちゃってふらふらです……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0006Fす、すみませんでした。\x01",
            "たぶん、うちで預かってる子です。\x02\x03",

            "#0005Fえっと、大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "だ、大丈夫ですよ？\x01",
            "ちょっと眼が回っているだけですし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FB9")

    label("loc_F4D")


    #C0020
    ChrTalk(
        0xFE,
        (
            "ううん、もうしばらく\x01",
            "フラフラしそうです……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "あ、さっきの女の子なら\x01",
            "病院の中に入っていきましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB9")

    Jump("loc_1474")

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1084")

    #C0022
    ChrTalk(
        0xFE,
        (
            "同僚のメイファちゃんは\x01",
            "看護師なのにけっこう短気なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "私なんて怒られてばっかりで……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "今日はゲバルさんの病室に\x01",
            "行くって言ってたけど\x01",
            "大丈夫でしょうかね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_111D")

    label("loc_1084")


    #C0025
    ChrTalk(
        0xFE,
        (
            "同僚のメイファちゃんは\x01",
            "看護師なのにけっこう短気なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ゲバルさんってワガママなところ\x01",
            "ありますからねぇ。\x01",
            "ちゃんと我慢できてるでしょうかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111D")

    Jump("loc_1474")

    label("loc_1122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_125B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D8")

    #C0027
    ChrTalk(
        0xFE,
        (
            "うふふ～いい天気。\x01",
            "シーツもすぐに乾きそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "……あっ、そうだ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "こないだうっかり汚しちゃった\x01",
            "メイファちゃんの服も\x01",
            "一緒に干しちゃおうかな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1256")

    label("loc_11D8")


    #C0030
    ChrTalk(
        0xFE,
        (
            "こないだ、メイファちゃんの私服に\x01",
            "薬棚の変な薬品をこぼしちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "天気もいいし、\x01",
            "こっそり一緒に干しちゃおうっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1256")

    Jump("loc_1474")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1269")
    Jump("loc_1474")

    label("loc_1269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12E5")

    #C0032
    ChrTalk(
        0xFE,
        (
            "昨日はセシル先輩たちと\x01",
            "入れ替わりで休暇だったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "メイファちゃんと街を回れて\x01",
            "とっても楽しかったわ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1474")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_12F3")
    Jump("loc_1474")

    label("loc_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1301")
    Jump("loc_1474")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_130F")
    Jump("loc_1474")

    label("loc_130F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_144F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D6")

    #C0034
    ChrTalk(
        0xFE,
        (
            "ふふ、いい夕焼け。\x01",
            "涼しくていい感じ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "……はっくしょん！！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "……あー、シーツに鼻水ついちゃった！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "やだ、どーしよ～！\x01",
            "またメイファちゃんに叱られちゃう～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_144A")

    label("loc_13D6")


    #C0038
    ChrTalk(
        0xFE,
        (
            "ど、どうしよ～！\x01",
            "またメイファちゃんに叱られちゃう！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "ダイソンさんに頼んだら\x01",
            "こっそり洗ってくれるかなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144A")

    Jump("loc_1474")

    label("loc_144F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_145D")
    Jump("loc_1474")

    label("loc_145D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_146B")
    Jump("loc_1474")

    label("loc_146B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1474")

    label("loc_1474")

    TalkEnd(0xFE)
    Return()

    # Function_6_B6E end

    def Function_7_1478(): pass

    label("Function_7_1478")

    TurnDirection(0x9, 0xD, 0)
    TurnDirection(0xD, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0040
    ChrTalk(
        0xD,
        (
            "シロン、あんたねぇ……\x01",
            "シーツ干すだけで\x01",
            "どんだけ時間掛かってんの！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "あ、メイファちゃん。\x01",
            "待ってて、あと少しで理想の角度に\x01",
            "干すことができそうなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xD,
        "り、理想の角度って……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xD,
        (
            "そんなもん追求してる間に\x01",
            "あんたの手持ちの仕事が\x01",
            "私に回ってきたじゃないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "あ、私の仕事しててくれたの？\x01",
            "うわぁ、ありがと～！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "……ハァ……もういいわ、\x01",
            "怒る気力も失せちゃった。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_7_1478 end

    def Function_8_1613(): pass

    label("Function_8_1613")


    #C0046
    ChrTalk(
        0xFE,
        (
            "また叱られちゃった。\x01",
            "はーぁ、メイファちゃんったら\x01",
            "怒りっぽいんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "きっと、いつも決まった時間に\x01",
            "お昼をとれないから\x01",
            "イライラしてるんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "この間記念祭の出店で見かけた\x01",
            "ハンバーガー、作ってみたら\x01",
            "簡単だったし教えてあげようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "あ、よかったら\x01",
            "あなた達にも教えてあげる。\x01",
            "ほんと、簡単だから！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xB)
    Return()

    # Function_8_1613 end

    def Function_9_17C5(): pass

    label("Function_9_17C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_17D6")
    Jump("loc_1EF6")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_17E4")
    Jump("loc_1EF6")

    label("loc_17E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_17F2")
    Jump("loc_1EF6")

    label("loc_17F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19ED")

    #C0052
    ChrTalk(
        0xA,
        (
            "#2401Fキーア君の症例について\x01",
            "いろいろと調べているのだが……\x02\x03",

            "#2406Fやはりピタリ当てはまるものはないね。\x01",
            "新種の症状という可能性もあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0006Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        (
            "#2400Fまぁ、今のところ\x01",
            "重大な異常はないようだし……\x01",
            "しばらく様子見かな。\x02\x03",

            "#2406F無理に病院なんかに\x01",
            "閉じ込めようとするほど\x01",
            "僕はサディストじゃないんでね。\x02\x03",

            "#2409Fどちらかというとモチロン、Ｍで……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#0211F……………………\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#0106Fな、なんの話をしてるんですか……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#0306Fったく、読めねぇお人だぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B25")

    label("loc_19ED")


    #C0058
    ChrTalk(
        0xA,
        (
            "#2400Fまぁ、キーア君については\x01",
            "今すぐどうこうってわけじゃないし、\x01",
            "気長に構えてればいいだろうさ。\x02\x03",

            "#2409F……それはそうと聞いてくれよ。\x01",
            "気分転換の為に朝釣りに出かけたら\x01",
            "なかなかの大物に出くわしてね。\x02\x03",

            "いやぁ、釣公師団の\x01",
            "セルダン支部長の驚いた顔が\x01",
            "今でも忘れられないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#0006Fマイペースですねホント……\x02",
    )

    CloseMessageWindow()

    label("loc_1B25")

    Jump("loc_1EF6")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1B38")
    Jump("loc_1EF6")

    label("loc_1B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1B46")
    Jump("loc_1EF6")

    label("loc_1B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1B54")
    Jump("loc_1EF6")

    label("loc_1B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B62")
    Jump("loc_1EF6")

    label("loc_1B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B70")
    Jump("loc_1EF6")

    label("loc_1B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C75")

    #C0060
    ChrTalk(
        0xA,
        (
            "#2406F今日ばかりは分からないように\x01",
            "抜け出してきたつもりなんだけどねぇ。\x02\x03",

            "あんなに早く君たちが来なければ、\x01",
            "僕は存分に記念祭を楽しめたのに……\x02\x03",

            "#2400Fまぁ、楽しみにしてた\x01",
            "釣り大会に参加出来たんだ。\x01",
            "それだけでも良しとしなければね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D1A")

    label("loc_1C75")


    #C0061
    ChrTalk(
        0xA,
        (
            "#2406F今日ばかりは分からないように\x01",
            "抜け出してきたつもりなんだけどねぇ。\x02\x03",

            "#2400Fまぁ、楽しみにしてた\x01",
            "釣り大会に参加出来たんだ。\x01",
            "それだけでも良しとしなければね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1A")

    Jump("loc_1EF6")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D2D")
    Jump("loc_1EF6")

    label("loc_1D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D3B")
    Jump("loc_1EF6")

    label("loc_1D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1ED1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E45")

    #C0062
    ChrTalk(
        0xA,
        (
            "#2404Fどれ、時間もあることだし\x01",
            "釣りにでも……\x02\x03",

            "#2405F……１階にいる\x01",
            "ラゴー教授に見つかったら\x01",
            "大目玉を食らってしまうな。\x02\x03",

            "#2406Fはぁ、仕方ない。\x01",
            "今日はあきらめて\x01",
            "ひきこもっているとするかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0012F（つくづく、ヘンな先生だな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1ECC")

    label("loc_1E45")


    #C0064
    ChrTalk(
        0xA,
        (
            "#2403F釣りはなかなか良いものだよ。\x01",
            "気分転換にもなるしね。\x02\x03",

            "#2400F時間があれば\x01",
            "クロスベル釣り場探訪……\x01",
            "なんてのもやってみたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECC")

    Jump("loc_1EF6")

    label("loc_1ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1EDF")
    Jump("loc_1EF6")

    label("loc_1EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1EED")
    Jump("loc_1EF6")

    label("loc_1EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1EF6")

    label("loc_1EF6")

    TalkEnd(0xFE)
    Return()

    # Function_9_17C5 end

    def Function_10_1EFA(): pass

    label("Function_10_1EFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F96")

    #C0065
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "ヨアヒム先生が見つかって\x01",
            "本当に良かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生なら\x01",
            "仕事なんてすぐ終わるんだから、\x01",
            "押し付けないでほしいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201E")

    label("loc_1F96")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_201E")

    #C0067
    ChrTalk(
        0xFE,
        (
            "ああ～もう！　ヨアヒム先生は\x01",
            "どこ行っちゃったんだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "こんな仕事量、研修医の僕に\x01",
            "さばききれるわけないじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1EFA end

    def Function_11_2022(): pass

    label("Function_11_2022")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2033")
    Jump("loc_242B")

    label("loc_2033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2041")
    Jump("loc_242B")

    label("loc_2041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_20B8")

    #C0069
    ChrTalk(
        0xFE,
        "ヨアヒム先生たちがさっき戻られたよ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "なんでも大怪我した人が\x01",
            "運びこまれて大忙しだったらしいぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_20B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_20C6")
    Jump("loc_242B")

    label("loc_20C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2112")

    #C0071
    ChrTalk(
        0xFE,
        (
            "はて……\x01",
            "女の子がすごい速さで\x01",
            "駆けて行ってしまったが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_2112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2179")

    #C0072
    ChrTalk(
        0xFE,
        (
            "君たち、病気をしてるようには\x01",
            "あまり見えないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "もしかして、研究棟に用事かい？\x02",
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_2179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_221D")

    #C0074
    ChrTalk(
        0xFE,
        (
            "お偉方は教授会だか何だかで\x01",
            "出払っているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "人の上に立つってのは\x01",
            "気苦労が多くて大変そうだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "私は気ままな用務員で満足してるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_221D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_222B")
    Jump("loc_242B")

    label("loc_222B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2298")

    #C0077
    ChrTalk(
        0xFE,
        (
            "先生方も看護師たちも、\x01",
            "仕事に精を出しているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        "私も手抜きのないようにせんとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_2298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_22A6")
    Jump("loc_242B")

    label("loc_22A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2335")

    #C0079
    ChrTalk(
        0xFE,
        (
            "緑色には人の心を\x01",
            "安らげる効果があるという。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "患者に少しでも\x01",
            "安心してもらえるように、\x01",
            "病院には沢山の植物を置いてるのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_2335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_23F8")

    #C0081
    ChrTalk(
        0xFE,
        (
            "この間、寮のテラスに設置した\x01",
            "魔獣よけのフェンスだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "用心のためにも、このまま\x01",
            "設置しておくことになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "また魔獣が侵入して\x01",
            "誰かが怪我したら元も子もないしね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_242B")

    label("loc_23F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2406")
    Jump("loc_242B")

    label("loc_2406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2414")
    Jump("loc_242B")

    label("loc_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2422")
    Jump("loc_242B")

    label("loc_2422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_242B")

    label("loc_242B")

    TalkEnd(0xFE)
    Return()

    # Function_11_2022 end

    def Function_12_242F(): pass

    label("Function_12_242F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2444")
    Call(0, 7)
    Jump("loc_24B2")

    label("loc_2444")


    #C0084
    ChrTalk(
        0xFE,
        (
            "もしかして私……\x01",
            "シロンを甘やかしすぎかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "何も自分が代わりにやってあげること\x01",
            "なかったわよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B2")

    TalkEnd(0xFE)
    Return()

    # Function_12_242F end

    def Function_13_24B6(): pass

    label("Function_13_24B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255A")

    #C0086
    ChrTalk(
        0xFE,
        (
            "屋上がこんなに広くて、\x01",
            "さらに建物まで建ってるなんて\x01",
            "びっくりしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "この建物の一番上までのぼったら、\x01",
            "クロスベル市まで見えるかなー？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_25C1")

    label("loc_255A")


    #C0088
    ChrTalk(
        0xFE,
        (
            "この建物の一番上までのぼったら、\x01",
            "すごく眺めがよさそうだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "勝手に入ったら怒られるかなー？\x02",
    )

    CloseMessageWindow()

    label("loc_25C1")

    TalkEnd(0xFE)
    Return()

    # Function_13_24B6 end

    def Function_14_25C5(): pass

    label("Function_14_25C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_263F")
    TalkBegin(0xFF)

    #C0090
    ChrTalk(
        0x101,
        (
            "#0006F（結局、研究棟には\x01",
            "  キーアはいなかったな……）\x02\x03",

            "#0008F（一体どこに行ったんだろう？）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_2B02")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_275C")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270B")

    #C0091
    ChrTalk(
        0x101,
        "#0005Fここは研究棟だな……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#0101Fどうする？\x01",
            "聞き込みに行ってみる？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0003Fいや……\x01",
            "今は現場検証が先決だろう。\x02\x03",

            "#0001F屋上を中心に\x01",
            "一通り調査をしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2754")

    label("loc_270B")


    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F今は屋上の現場検証をやろう。\x01",
            "魔獣の手がかりを見つけないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2754")

    TalkEnd(0xFF)
    Jump("loc_2B02")

    label("loc_275C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2AC2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27B6")
    MenuCmd(1, 0, "【４Ｆ 薬学・神経科研究室】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27ED")
    MenuCmd(1, 0, "【１Ｆ 資料室】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A7D")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(1, 0, "やめる")
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kどこに行きますか？\x07\x00\x02",
        )
    )

    MenuCmd(2, 0, 132, -1, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_DB()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_287E"),
        (1, "loc_28C4"),
        (2, "loc_290A"),
        (SWITCH_DEFAULT, "loc_2919"),
    )


    label("loc_287E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28A6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28BF")

    label("loc_28A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28BF")

    Jump("loc_2919")

    label("loc_28C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28EC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2905")

    label("loc_28EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2905")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2905")

    Jump("loc_2919")

    label("loc_290A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2919")

    label("loc_2919")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2935"),
        (1, "loc_2A41"),
        (2, "loc_2A71"),
        (SWITCH_DEFAULT, "loc_2A78"),
    )


    label("loc_2935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29D3")

    #C0096
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……ヨアヒム先生が\x01",
            "いるかどうか判らないし、\x01",
            "一応受付で確認してみよう。\x02\x03",

            "#0003F部外者が無断で\x01",
            "入っていい所でもないしな。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x5)
    Jump("loc_2A3C")

    label("loc_29D3")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A12")
    SetScenarioFlags(0x5C, 0)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_2A3C")

    label("loc_2A12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A31")
    SetScenarioFlags(0x5C, 1)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_2A3C")

    label("loc_2A31")

    EventEnd(0x5)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_2A3C")

    Jump("loc_2A78")

    label("loc_2A41")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1620", 114, 0, 0)
    IdleLoop()
    Jump("loc_2A78")

    label("loc_2A71")

    EventEnd(0x3)
    Jump("loc_2A78")

    label("loc_2A78")

    Jump("loc_2ABD")

    label("loc_2A7D")

    TalkBegin(0xFF)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウルスラ病院の研究棟だ。\x01",
            "今は特に用事はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2ABD")

    Jump("loc_2B02")

    label("loc_2AC2")

    TalkBegin(0xFF)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウルスラ病院の研究棟だ。\x01",
            "今は特に用事はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2B02")

    Return()

    # Function_14_25C5 end

    def Function_15_2B03(): pass

    label("Function_15_2B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C67")
    EventBegin(0x0)
    Fade(1000)
    OP_68(22460, 8000, -25140, 0)
    MoveCamera(53, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25970, 0)
    SetChrPos(0x101, 26480, 7000, -16960, 180)
    SetChrPos(0x102, 27690, 7000, -14290, 180)
    SetChrPos(0x103, 26160, 7000, -15280, 180)
    SetChrPos(0x104, 28420, 7000, -15270, 180)
    OP_0D()
    Sleep(500)

    #C0099
    ChrTalk(
        0x104,
        (
            "#3P#0306Fさすがにここから\x01",
            "入ってきたってのはナシか。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#0001Fああ……下は水面だしね。\x02\x03",

            "狼型の魔獣だったら\x01",
            "よじ登るのも無理だろうな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 26480, 7000, -16960, 0)
    OP_68(26480, 8000, -16960, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetScenarioFlags(0x62, 4)
    OP_29(0x3F, 0x1, 0xB)
    EventEnd(0x5)
    Jump("loc_2CB3")

    label("loc_2C67")

    TalkBegin(0xFF)

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手すりの下はかなりの高さがあり\x01",
            "さらに水面が広がっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2CB3")

    Return()

    # Function_15_2B03 end

    def Function_16_2CB4(): pass

    label("Function_16_2CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E16")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-2220, 8000, -4870, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16280, 0)
    SetChrPos(0x101, 3970, 7000, 110, 270)
    SetChrPos(0x102, 5190, 7000, -250, 270)
    SetChrPos(0x103, 4160, 7000, 1920, 270)
    SetChrPos(0x104, 5500, 7000, 1650, 270)
    OP_0D()
    Sleep(500)

    #C0102
    ChrTalk(
        0x103,
        (
            "#0200F#6Pかなりの高さですけど……\x01",
            "途中に一段、屋根がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#0006F#4Pうーん、と言っても\x01",
            "１階分の高さが２段か……\x02\x03",

            "#0001F魔獣が入ってくるのは\x01",
            "かなり厳しいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 3970, 7000, 110, 90)
    SetScenarioFlags(0x62, 5)
    OP_29(0x3F, 0x1, 0xC)
    EventEnd(0x5)
    Jump("loc_2E5E")

    label("loc_2E16")

    TalkBegin(0xFF)

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "玄関部分の屋根が見える。\x01",
            "高さはそれなりにありそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2E5E")

    Return()

    # Function_16_2CB4 end

    def Function_17_2E5F(): pass

    label("Function_17_2E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB5")
    EventBegin(0x0)
    Fade(1000)
    OP_68(23090, 8000, 14140, 0)
    MoveCamera(45, 41, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 21870, 7000, 12850, 45)
    SetChrPos(0x102, 21970, 7000, 11830, 45)
    SetChrPos(0x103, 20710, 7000, 11420, 45)
    SetChrPos(0x104, 20470, 7000, 13080, 45)
    OP_0D()
    Sleep(500)

    #C0105
    ChrTalk(
        0x102,
        (
            "#0101F#12P#Nねえ、ここから\x01",
            "入ってきたというのは？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0106
    ChrTalk(
        0x101,
        (
            "#0003F#6Pうーん、いかにも魔獣が\x01",
            "入ってきそうな地形だけど……\x02\x03",

            "#0001Fそれでもやっぱり\x01",
            "高さがネックになりそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 21200, 7000, 12090, 225)
    SetScenarioFlags(0x62, 6)
    OP_29(0x3F, 0x1, 0xD)
    EventEnd(0x5)
    Jump("loc_3013")

    label("loc_2FB5")

    TalkBegin(0xFF)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いかにも魔獣が現れそうな\x01",
            "地形が広がっている。\x02\x03",

            "高さはそれなりにありそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3013")

    Return()

    # Function_17_2E5F end

    def Function_18_3014(): pass

    label("Function_18_3014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3122")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-8530, 8000, 17450, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24400, 0)
    SetChrPos(0x101, -8770, 7000, 18960, 180)
    SetChrPos(0x102, -10030, 7000, 19500, 180)
    SetChrPos(0x103, -6950, 7000, 19010, 180)
    SetChrPos(0x104, -7950, 7000, 20200, 180)
    OP_0D()
    Sleep(500)

    #C0108
    ChrTalk(
        0x101,
        (
            "#0006F#5Pさすがにここから\x01",
            "侵入したってのはないか。\x02\x03",

            "#0001F飛行型魔獣なら\x01",
            "説明は付くんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8770, 7000, 18960, 270)
    SetScenarioFlags(0x62, 7)
    OP_29(0x3F, 0x1, 0xE)
    EventEnd(0x5)
    Jump("loc_315E")

    label("loc_3122")

    TalkBegin(0xFF)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "渡り廊下の下は\x01",
            "かなりの高さがありそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_315E")

    Return()

    # Function_18_3014 end

    def Function_19_315F(): pass

    label("Function_19_315F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B7")
    EventBegin(0x0)
    Fade(1000)
    OP_68(-30100, 7000, 16720, 0)
    MoveCamera(37, 43, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22550, 0)
    SetChrPos(0x101, -29060, 6000, 17010, 270)
    SetChrPos(0x102, -28050, 6000, 16180, 270)
    SetChrPos(0x103, -28460, 6000, 14890, 270)
    SetChrPos(0x104, -28620, 6000, 19420, 270)
    OP_0D()
    Sleep(500)

    #C0110
    ChrTalk(
        0x101,
        "#0005F#11Pここは……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#0100F#11Pねえ、ここからだったら\x01",
            "入って来られそうじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0000F#11P確かに、飛び移って\x01",
            "来れない高さじゃないな。\x02\x03",

            "#0008Fとなると……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -29060, 6000, 17010, 0)
    SetScenarioFlags(0x63, 0)
    OP_29(0x3F, 0x1, 0xF)
    ModifyEventFlags(0, 4, 0x80)
    EventEnd(0x5)
    Jump("loc_32FB")

    label("loc_32B7")

    TalkBegin(0xFF)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手すりのすぐ下まで\x01",
            "木箱やコンテナが積まれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_32FB")

    Return()

    # Function_19_315F end

    def Function_20_32FC(): pass

    label("Function_20_32FC")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-4500, 8000, 19000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25250, 0)
    SetChrPos(0x101, -3800, 7000, 18900, 90)
    SetChrPos(0x102, -3800, 7000, 20100, 90)
    SetChrPos(0x103, -4900, 7000, 18900, 90)
    SetChrPos(0x104, -4900, 7000, 20100, 90)
    SetChrPos(0x136, -1600, 7000, 19500, 270)
    OP_68(-3000, 8000, 19000, 2500)
    OP_6F(0x1)
    OP_0D()
    OP_93(0x101, 0xB4, 0x12C)
    Sleep(1000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0114
    ChrTalk(
        0x101,
        (
            "#0001F#6Pひょっとして……\x01",
            "ここが被害者が襲われた？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x136,
        (
            "#1303F#11Pええ……\x01",
            "病棟の屋上になるわね。\x02\x03",

            "#1300Fどうする？\x01",
            "先にこちらを調べてしまう？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#0000F#6Pいや……その前に\x01",
            "被害者の話を聞いておきたい。\x02\x03",

            "後で案内してくれるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x136,
        (
            "#1300F#11P分かったわ。\x02\x03",

            "被害にあった研修医の人は\x01",
            "２階の病室にいるから案内するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#0000F#6Pうん、よろしく。\x02",
    )

    CloseMessageWindow()
    OP_93(0x136, 0x0, 0x1F4)
    BeginChrThread(0x136, 3, 0, 21)
    Sleep(1300)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(1200)
    BeginChrThread(0x102, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 22)
    Sleep(1200)
    BeginChrThread(0x104, 3, 0, 22)
    WaitChrThread(0x136, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    Sound(106, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x65, 7)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_32FC end

    def Function_21_358B(): pass

    label("Function_21_358B")


    def lambda_3590():
        OP_95(0xFE, -1680, 7000, 22860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3590)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x4)

    def lambda_35C9():
        OP_95(0xFE, -1550, 7000, 25460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35C9)
    Sleep(500)

    def lambda_35E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35E6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_358B end

    def Function_22_35FB(): pass

    label("Function_22_35FB")


    def lambda_3600():
        OP_95(0xFE, -1680, 7000, 22860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3600)
    WaitChrThread(0xFE, 1)

    def lambda_361E():
        OP_95(0xFE, -1550, 7000, 25460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_361E)
    Sleep(500)

    def lambda_363B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_363B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_35FB end

    def Function_23_3650(): pass

    label("Function_23_3650")

    EventBegin(0x0)
    Fade(1000)
    OP_68(15000, 8000, -13430, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_68(15000, 8000, -15500, 3000)
    SetChrPos(0x101, 15700, 7000, -14680, 180)
    SetChrPos(0x102, 14280, 7000, -14560, 180)
    SetChrPos(0x103, 14260, 7000, -13000, 180)
    SetChrPos(0x104, 15640, 7000, -13120, 180)
    SetChrPos(0x136, 15040, 7000, -16780, 0)
    OP_0D()
    OP_6F(0x1)

    #C0119
    ChrTalk(
        0x101,
        (
            "#0005F#5P話を聞いた限りだと……\x01",
            "このあたりが現場になるのかな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3737():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3737)
    WaitChrThread(0x136, 1)
    Sleep(300)

    #C0120
    ChrTalk(
        0x136,
        (
            "#1301F#5Pええ、リットンさんは\x01",
            "そこのベンチの前あたりで\x01",
            "倒れていたらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#0001F#5Pそうか……\x02",
    )

    CloseMessageWindow()

    def lambda_37B7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37B7)
    WaitChrThread(0x101, 1)
    Sleep(500)

    def lambda_37CB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_37CB)
    Sleep(100)

    def lambda_37DB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37DB)
    Sleep(100)

    def lambda_37EB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_37EB)
    Sleep(400)

    def lambda_37FB():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37FB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    MoveCamera(45, 13, 0, 2000)
    OP_68(15000, 8500, -15500, 2000)
    OP_6F(0x51)

    #C0122
    ChrTalk(
        0x101,
        (
            "#6P#0005Fその建物は……\x01",
            "確か《研究棟》だったっけ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_387F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_387F)
    Sleep(50)

    def lambda_388F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_388F)
    Sleep(50)

    def lambda_389F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_389F)
    Sleep(50)

    def lambda_38AF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_38AF)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)

    #C0123
    ChrTalk(
        0x136,
        (
            "#12P#1300Fええ、先生方と\x01",
            "研修医の人が詰めている場所よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#0200F#6P実験用に、何か危険な魔獣を\x01",
            "飼っているような事は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x136,
        (
            "#12P#1304Fふふ、それはさすがに無いわね。\x02\x03",

            "#1300F研究用の植物を育てている\x01",
            "温室みたいな場所はあるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#6P#0100Fなるほど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(15000, 8000, -15500, 1200)
    MoveCamera(45, 18, 0, 1200)

    def lambda_3A09():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A09)
    Sleep(50)

    def lambda_3A19():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3A19)
    Sleep(50)

    def lambda_3A29():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A29)
    Sleep(50)

    def lambda_3A39():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A39)
    Sleep(50)

    def lambda_3A49():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A49)
    OP_6F(0x51)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0127
    ChrTalk(
        0x101,
        (
            "#0004F#5Pセシル姉、案内ありがとう。\x02\x03",

            "#0000Fとりあえず何か分かるまで\x01",
            "一通り調べてみるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x136,
        (
            "#1300F#12Pうん、分かったわ。\x02\x03",

            "#1309Fそれじゃあ、みんな。\x01",
            "調査の方、頑張ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#0102F#5Pはい。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        "#0202F#5P……お疲れさまです。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#0309F#5Pどうか朗報、\x01",
            "期待しててくださいッス！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B83():

        label("loc_3B83")

        TurnDirection(0x101, 0x136, 500)
        Yield()
        Jump("loc_3B83")

    QueueWorkItem2(0x101, 1, lambda_3B83)

    def lambda_3B95():

        label("loc_3B95")

        TurnDirection(0x102, 0x136, 500)
        Yield()
        Jump("loc_3B95")

    QueueWorkItem2(0x102, 1, lambda_3B95)

    def lambda_3BA7():

        label("loc_3BA7")

        TurnDirection(0x103, 0x136, 500)
        Yield()
        Jump("loc_3BA7")

    QueueWorkItem2(0x103, 1, lambda_3BA7)

    def lambda_3BB9():

        label("loc_3BB9")

        TurnDirection(0x104, 0x136, 500)
        Yield()
        Jump("loc_3BB9")

    QueueWorkItem2(0x104, 1, lambda_3BB9)
    OP_93(0x136, 0x13B, 0x1F4)
    OP_68(13760, 8000, -12780, 3000)

    def lambda_3BE3():
        OP_95(0xFE, 11170, 7000, -14900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3BE3)
    WaitChrThread(0x136, 1)

    def lambda_3C01():
        OP_95(0xFE, 10070, 7000, -2850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3C01)
    Sleep(3000)
    StopBGM(0xBB8)
    WaitChrThread(0x136, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(15390, 8000, -13910, 1500)

    def lambda_3C48():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C48)
    WaitChrThread(0x101, 1)

    def lambda_3C59():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C59)
    Sleep(100)

    def lambda_3C69():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3C69)

    def lambda_3C76():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3C76)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0132
    ChrTalk(
        0x101,
        (
            "#11P#0003Fとりあえず、屋上を中心に\x01",
            "一通り調査をしてみよう。\x02\x03",

            "#0001F狼型魔獣たちが\x01",
            "本当に屋上に現れた──\x02\x03",

            "その前提で、侵入ポイントを\x01",
            "何とか突き止めてみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        "#6P#0100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#0202F#1Pロイドさんお得意の\x01",
            "可能性を絞り込む方法ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        "#5P#0300Fんじゃま、調べてみるか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x35, 0x0)
    SetChrPos(0x0, 15500, 7000, -13700, 180)
    ModifyEventFlags(0, 1, 0x80)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    SetScenarioFlags(0x62, 3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    EventEnd(0x5)
    Return()

    # Function_23_3650 end

    def Function_24_3E07(): pass

    label("Function_24_3E07")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-20770, 7000, 15490, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FFB")
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    #C0136
    ChrTalk(
        0x8,
        (
            "……あら、あんたたち\x01",
            "道に迷ったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "ここは外来の人が来る所じゃないよ。\x01",
            "ちゃんと病院の受付で\x01",
            "話をして来なさいな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3EF1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3EF1)
    Sleep(50)

    def lambda_3F01():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3F01)
    Sleep(50)

    def lambda_3F11():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3F11)
    Sleep(50)

    def lambda_3F21():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3F21)
    WaitChrThread(0x0, 1)

    #C0138
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……すみません。\x02\x03",

            "#0006F（やっぱり病院内を歩くのは\x01",
            "   セシル姉と会ってからの方が\x01",
            "   良さそうだな……）\x02\x03",

            "（受付は病棟の\x01",
            "  １階ロビーにあったはずだし、\x01",
            "  そこで呼び出してもらおう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_408A")

    label("loc_3FFB")

    TurnDirection(0x8, 0x0, 500)

    #C0139
    ChrTalk(
        0x8,
        (
            "ここは外来の人が来る所じゃないよ。\x01",
            "ちゃんと受付で話をして来なさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "受付は病棟の１階ロビーさ。\x01",
            "ほれ、そっちに回んなさいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_408A")

    Sleep(50)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -16660, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_24_3E07 end

    def Function_25_40AC(): pass

    label("Function_25_40AC")

    EventBegin(0x1)
    Call(0, 27)
    Sleep(50)
    SetChrPos(0x0, -1500, 6500, 21500, 180)
    EventEnd(0x4)
    Return()

    # Function_25_40AC end

    def Function_26_40C8(): pass

    label("Function_26_40C8")

    EventBegin(0x1)
    Call(0, 27)
    Sleep(50)
    SetChrPos(0x0, -22500, 6000, 21500, 182)
    EventEnd(0x4)
    Return()

    # Function_26_40C8 end

    def Function_27_40E4(): pass

    label("Function_27_40E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41AA")

    #C0141
    ChrTalk(
        0x104,
        (
            "#0305Fおっと……\x01",
            "こっちだと建物の中に\x01",
            "戻っちまうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#0001Fまだ何も見つかってないんだ、\x01",
            "もう少し調査しよう。\x02\x03",

            "この屋上に狼型魔獣が現れた……\x01",
            "それを裏付ける証拠を探そう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_41FE")

    label("loc_41AA")


    #C0143
    ChrTalk(
        0x101,
        (
            "#0001Fまだ何も見つかってないんだ、\x01",
            "屋上に狼型魔獣が現れたという\x01",
            "証拠を探そう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41FE")

    Return()

    # Function_27_40E4 end

    SaveToFile()

Try(main)
