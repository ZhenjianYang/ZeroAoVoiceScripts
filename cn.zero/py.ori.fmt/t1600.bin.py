from ZeroScenarioHelper import *

def main():
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
        "玛萨护士长",             # 1
        "希伦护士",               # 2
        "约亚西姆副教授",         # 3
        "实习医生利顿",           # 4
        "勤杂工戴森",             # 5
        "梅菲尔护士",             # 6
        "游客托迪",               # 7
        "乌尔斯拉间道",           # 8
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

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_5EC",          # 01, 1
        "Function_2_617",          # 02, 2
        "Function_3_642",          # 03, 3
        "Function_4_818",          # 04, 4
        "Function_5_9C2",          # 05, 5
        "Function_6_B14",          # 06, 6
        "Function_7_1200",         # 07, 7
        "Function_8_1361",         # 08, 8
        "Function_9_14BD",         # 09, 9
        "Function_10_1AF6",        # 0A, 10
        "Function_11_1BEE",        # 0B, 11
        "Function_12_1F29",        # 0C, 12
        "Function_13_1F98",        # 0D, 13
        "Function_14_2089",        # 0E, 14
        "Function_15_2588",        # 0F, 15
        "Function_16_2715",        # 10, 16
        "Function_17_289C",        # 11, 17
        "Function_18_2A1B",        # 12, 18
        "Function_19_2B58",        # 13, 19
        "Function_20_2CC9",        # 14, 20
        "Function_21_2F22",        # 15, 21
        "Function_22_2F92",        # 16, 22
        "Function_23_2FE7",        # 17, 23
        "Function_24_36EA",        # 18, 24
        "Function_25_3955",        # 19, 25
        "Function_26_3971",        # 1A, 26
        "Function_27_398D",        # 1B, 27
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ADD")
    OP_93(0xFE, 0x0, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0001
    ChrTalk(
        0xFE,
        (
            "哎呀……\x01",
            "你们是在找人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0005F嗯，我们想找\x01",
            "在医院工作的朋友，\x01",
            "正打算去接待处……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "哎呀，\x01",
            "那你们还真是\x01",
            "走错地方了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "接待处在病房楼一层的大厅哦。\x01",
            "好啦，回去回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000F啊，是这样吗……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B10")

    label("loc_ADD")


    #C0006
    ChrTalk(
        0xFE,
        (
            "接待处在病房楼一层的大厅啦。\x01",
            "好啦，回去回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B10")

    TalkEnd(0xFE)
    Return()

    # Function_5_9C2 end

    def Function_6_B14(): pass

    label("Function_6_B14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B25")
    Jump("loc_11FC")

    label("loc_B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")
    Call(0, 7)
    Jump("loc_BA0")

    label("loc_B40")


    #C0007
    ChrTalk(
        0xFE,
        (
            "梅菲尔虽然有\x01",
            "诸多抱怨，但还是会\x01",
            "帮我补救失误呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "呵呵，有个这么善良的朋友真是太好了。\x02",
    )

    CloseMessageWindow()

    label("loc_BA0")

    Jump("loc_11FC")

    label("loc_BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6E")

    #C0009
    ChrTalk(
        0xFE,
        (
            "我把床单的订货单写错了，\x01",
            "梅菲尔又发火了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "我只是觉得五十张太少了，\x01",
            "所以就加了个零而已啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "不过，算啦。\x01",
            "不能总是为\x01",
            "失败而烦恼。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "没什么，没什么，我不介意！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CD3")

    label("loc_C6E")


    #C0013
    ChrTalk(
        0xFE,
        (
            "虽然又被梅菲尔\x01",
            "骂了……\x01",
            "不过我并不介意。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "不能总是为失败而烦恼。\x01",
            "没什么，没什么，我不介意！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD3")

    Jump("loc_11FC")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF4")
    Call(0, 8)
    Jump("loc_D56")

    label("loc_CF4")


    #C0015
    ChrTalk(
        0xFE,
        (
            "梅菲尔真是的，\x01",
            "又训斥我了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "我只是把收到的货物好好保管起来而已……\x01",
            "为什么一定要被骂呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D56")

    Jump("loc_11FC")

    label("loc_D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_E64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E15")

    #C0017
    ChrTalk(
        0xFE,
        (
            "嗯～我被跑过去的\x01",
            "小孩子撞到了，晕乎乎的……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0006F对、对不起，\x01",
            "那应该是我们监护的孩子。\x02\x03",

            "#0005F那个，你没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "没、没事哦，\x01",
            "只是头有点晕而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E5F")

    label("loc_E15")


    #C0020
    ChrTalk(
        0xFE,
        (
            "不行，可能还要\x01",
            "再晕一会……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "啊，刚才的女孩子\x01",
            "跑进医院里面去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5F")

    Jump("loc_11FC")

    label("loc_E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_F54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF4")

    #C0022
    ChrTalk(
        0xFE,
        (
            "我的同事梅菲尔\x01",
            "虽然是护士，却是个急性子。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "我总是被她骂……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "今天她说要去\x01",
            "盖巴尔先生的病房，\x01",
            "没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_F4F")

    label("loc_EF4")


    #C0025
    ChrTalk(
        0xFE,
        (
            "我的同事梅菲尔\x01",
            "虽然是护士，却是个急性子。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "盖巴尔先生\x01",
            "很任性呢，\x01",
            "她能忍得下来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4F")

    Jump("loc_11FC")

    label("loc_F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1043")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE4")

    #C0027
    ChrTalk(
        0xFE,
        (
            "呵呵～天气真好，\x01",
            "床单似乎也能很快晾干。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "……啊，对了。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "把之前不小心弄脏的\x01",
            "梅菲尔的衣服\x01",
            "也一起晾了吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_103E")

    label("loc_FE4")


    #C0030
    ChrTalk(
        0xFE,
        (
            "之前我把药架上的奇怪药品\x01",
            "撒到梅菲尔的便服上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "反正天气不错，\x01",
            "偷偷一起晾了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103E")

    Jump("loc_11FC")

    label("loc_1043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1051")
    Jump("loc_11FC")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_10A9")

    #C0032
    ChrTalk(
        0xFE,
        (
            "昨天和塞茜尔前辈她们\x01",
            "换班去休假了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "和梅菲尔一起逛街\x01",
            "好开心哦⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FC")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_10B7")
    Jump("loc_11FC")

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_10C5")
    Jump("loc_11FC")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_10D3")
    Jump("loc_11FC")

    label("loc_10D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1174")

    #C0034
    ChrTalk(
        0xFE,
        (
            "呵呵，好漂亮的晚霞。\x01",
            "感觉好凉爽。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "……啊嚏！！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "……啊～鼻涕沾到床单上了！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "讨厌，怎么办呀～！\x01",
            "又要被梅菲尔骂了～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11D2")

    label("loc_1174")


    #C0038
    ChrTalk(
        0xFE,
        (
            "怎、怎么办呀～！\x01",
            "又要被梅菲尔骂了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "拜托戴森先生的话，\x01",
            "他会不会私下帮我洗了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D2")

    Jump("loc_11FC")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_11E5")
    Jump("loc_11FC")

    label("loc_11E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_11F3")
    Jump("loc_11FC")

    label("loc_11F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_11FC")

    label("loc_11FC")

    TalkEnd(0xFE)
    Return()

    # Function_6_B14 end

    def Function_7_1200(): pass

    label("Function_7_1200")

    TurnDirection(0x9, 0xD, 0)
    TurnDirection(0xD, 0x9, 0)
    OP_4B(0x9, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0040
    ChrTalk(
        0xD,
        (
            "希伦，你这个人啊……\x01",
            "只是晾个床单而已，\x01",
            "要花多长时间啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "啊，梅菲尔。\x01",
            "你再等等，好像只差一点\x01",
            "就可以调整到理想的晾晒角度了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xD,
        "理、理想的角度……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xD,
        (
            "在你追求这种东西的时候，\x01",
            "本该由你做的工作\x01",
            "全都转给我了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "啊，你帮我做完了工作吗？\x01",
            "哇，谢谢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "……唉……算了，\x01",
            "我已经连生气的力气都没有了。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_7_1200 end

    def Function_8_1361(): pass

    label("Function_8_1361")


    #C0046
    ChrTalk(
        0xFE,
        (
            "我又被骂了。\x01",
            "唉～梅菲尔\x01",
            "就是爱生气。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "一定是因为总是不能\x01",
            "按时吃午饭，\x01",
            "所以才那么暴躁呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "我试着做了一下之前在纪念庆典\x01",
            "的露天店看到的汉堡包，\x01",
            "还挺简单的，要不要教给她呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "啊，有兴趣的话，\x01",
            "不妨也教给你们吧。\x01",
            "真的很简单的！\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '午餐汉堡'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '午餐汉堡'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0xB)
    Return()

    # Function_8_1361 end

    def Function_9_14BD(): pass

    label("Function_9_14BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14CE")
    Jump("loc_1AF2")

    label("loc_14CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_14DC")
    Jump("loc_1AF2")

    label("loc_14DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_14EA")
    Jump("loc_1AF2")

    label("loc_14EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_17AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1687")

    #C0052
    ChrTalk(
        0xA,
        (
            "#2401F关于琪雅的病症，\x01",
            "我查了不少资料……\x02\x03",

            "#2406F但还是没有发现相符的病例呢，\x01",
            "也有可能是新的症状……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0006F是吗……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        (
            "#2400F算了，反正现在\x01",
            "好像也没有重大异常……\x01",
            "暂时先观察一下情况吧。\x02\x03",

            "#2406F我还没那么Ｓ，\x01",
            "不会把她强行关在\x01",
            "医院里检查的。\x02\x03",

            "#2409F硬要说的话，当然是Ｍ……\x02",
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
        "#0106F您、您在说什么呢……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#0306F唉，真是个让人捉摸不透的人啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17A5")

    label("loc_1687")


    #C0058
    ChrTalk(
        0xA,
        (
            "#2400F总之，琪雅的情况并不严重，\x01",
            "也不是必须要立刻采取什么治疗对策，\x01",
            "耐心观察一阵子就好啦。\x02\x03",

            "#2409F……对了，你们听我说哦。\x01",
            "我为了转换心情，早上出去钓鱼，\x01",
            "结果钓到了相当大的鱼呢。\x02\x03",

            "哈哈，钓公师团的\x01",
            "赛尔丹分部长那惊讶的表情，\x01",
            "我直到现在还记忆犹新呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#0006F还真是我行我素啊……\x02",
    )

    CloseMessageWindow()

    label("loc_17A5")

    Jump("loc_1AF2")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_17B8")
    Jump("loc_1AF2")

    label("loc_17B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_17C6")
    Jump("loc_1AF2")

    label("loc_17C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17D4")
    Jump("loc_1AF2")

    label("loc_17D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_17E2")
    Jump("loc_1AF2")

    label("loc_17E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_17F0")
    Jump("loc_1AF2")

    label("loc_17F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1941")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18BF")

    #C0060
    ChrTalk(
        0xA,
        (
            "#2406F本以为今天终于成功在\x01",
            "不被发现的情况下顺利溜走了呢。\x02\x03",

            "要不是你们来得那么快，\x01",
            "我就可以尽情享受纪念庆典了……\x02\x03",

            "#2400F算啦，反正参加了\x01",
            "期待已久的钓鱼大赛。\x01",
            "这样就足够了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_193C")

    label("loc_18BF")


    #C0061
    ChrTalk(
        0xA,
        (
            "#2406F本以为今天终于成功在\x01",
            "不被发现的情况下顺利溜走了呢。\x02\x03",

            "#2400F算啦，反正参加了\x01",
            "期待已久的钓鱼大赛。\x01",
            "这样就足够了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_193C")

    Jump("loc_1AF2")

    label("loc_1941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_194F")
    Jump("loc_1AF2")

    label("loc_194F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_195D")
    Jump("loc_1AF2")

    label("loc_195D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4B")

    #C0062
    ChrTalk(
        0xA,
        (
            "#2404F嗯，反正还有时间，\x01",
            "不如去钓鱼……\x02\x03",

            "#2405F……但要是被一楼的\x01",
            "拉格教授发现，\x01",
            "一定会被大骂一通的吧。\x02\x03",

            "#2406F唉，没办法。\x01",
            "今天还是放弃吧，\x01",
            "就窝在医院里好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0012F（越来越觉得这位医生很奇怪了……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1AC8")

    label("loc_1A4B")


    #C0064
    ChrTalk(
        0xA,
        (
            "#2403F钓鱼可是很不错的哦，\x01",
            "还可以转换心情。\x02\x03",

            "#2400F有时间的话，\x01",
            "一定要去探访克洛斯贝尔的各大钓鱼点……\x01",
            "真想赶快行动呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC8")

    Jump("loc_1AF2")

    label("loc_1ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1ADB")
    Jump("loc_1AF2")

    label("loc_1ADB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1AE9")
    Jump("loc_1AF2")

    label("loc_1AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1AF2")

    label("loc_1AF2")

    TalkEnd(0xFE)
    Return()

    # Function_9_14BD end

    def Function_10_1AF6(): pass

    label("Function_10_1AF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B7A")

    #C0065
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "能找到约亚西姆医生\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生的话，\x01",
            "很快就能把工作做完了，\x01",
            "所以请不要推给我啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BEA")

    label("loc_1B7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1BEA")

    #C0067
    ChrTalk(
        0xFE,
        (
            "啊啊～真是的！约亚西姆医生\x01",
            "到底去哪里了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "这种工作量，我这个实习医生\x01",
            "根本不可能完成啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BEA")

    TalkEnd(0xFE)
    Return()

    # Function_10_1AF6 end

    def Function_11_1BEE(): pass

    label("Function_11_1BEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1BFF")
    Jump("loc_1F25")

    label("loc_1BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1C0D")
    Jump("loc_1F25")

    label("loc_1C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1C70")

    #C0069
    ChrTalk(
        0xFE,
        "约亚西姆医生他们刚才回来了。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "好像有人受了重伤要被\x01",
            "抬进来，忙得不可开交呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1C7E")
    Jump("loc_1F25")

    label("loc_1C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1CBE")

    #C0071
    ChrTalk(
        0xFE,
        (
            "话说……\x01",
            "有个女孩子以超快的速度\x01",
            "跑过去了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1D09")

    #C0072
    ChrTalk(
        0xFE,
        (
            "你们看起来\x01",
            "不像是生病了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "莫非是来研究楼有事吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D91")

    #C0074
    ChrTalk(
        0xFE,
        (
            "上级领导们好像出去\x01",
            "开什么教授会议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "当领导也要操心劳神，\x01",
            "真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "我只要当个轻松的勤杂工就很满足了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D9F")
    Jump("loc_1F25")

    label("loc_1D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DE8")

    #C0077
    ChrTalk(
        0xFE,
        (
            "医生和护士们\x01",
            "都对工作尽心尽力。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        "我也不能偷懒啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DF6")
    Jump("loc_1F25")

    label("loc_1DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1E61")

    #C0079
    ChrTalk(
        0xFE,
        (
            "听说绿色有\x01",
            "安抚人心的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "为了让病人们\x01",
            "多少能安心一点，\x01",
            "医院里摆放了很多盆植物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EF2")

    #C0081
    ChrTalk(
        0xFE,
        (
            "之前在宿舍天台上设置的\x01",
            "防魔兽护栏……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "保险起见，就一直\x01",
            "留在那里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "因为要是再有魔兽侵入\x01",
            "伤人的话，那不就糟糕了嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F25")

    label("loc_1EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1F00")
    Jump("loc_1F25")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1F0E")
    Jump("loc_1F25")

    label("loc_1F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1F1C")
    Jump("loc_1F25")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F25")

    label("loc_1F25")

    TalkEnd(0xFE)
    Return()

    # Function_11_1BEE end

    def Function_12_1F29(): pass

    label("Function_12_1F29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F3E")
    Call(0, 7)
    Jump("loc_1F94")

    label("loc_1F3E")


    #C0084
    ChrTalk(
        0xFE,
        (
            "我是不是……\x01",
            "太娇纵希伦了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "无论是什么事情，我都\x01",
            "替她完成，这可不行啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F94")

    TalkEnd(0xFE)
    Return()

    # Function_12_1F29 end

    def Function_13_1F98(): pass

    label("Function_13_1F98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2030")

    #C0086
    ChrTalk(
        0xFE,
        (
            "楼顶上竟然这么宽敞，\x01",
            "甚至还建了建筑物，\x01",
            "真叫人大吃一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "要是能爬到这栋建筑物的顶部，\x01",
            "大概连克洛斯贝尔市都能望得到吧～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2085")

    label("loc_2030")


    #C0088
    ChrTalk(
        0xFE,
        (
            "要是能爬到这栋建筑物的顶部，\x01",
            "视野一定非常好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "但擅自进去的话会被骂吧～？\x02",
    )

    CloseMessageWindow()

    label("loc_2085")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F98 end

    def Function_14_2089(): pass

    label("Function_14_2089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20ED")
    TalkBegin(0xFF)

    #C0090
    ChrTalk(
        0x101,
        (
            "#0006F（结果琪雅\x01",
            "  并不在研究楼里啊……）\x02\x03",

            "#0008F（到底去哪里了呢？）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_2587")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21F4")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A7")

    #C0091
    ChrTalk(
        0x101,
        "#0005F这里是研究楼吧……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x102,
        (
            "#0101F怎么办？\x01",
            "要去探听一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0003F不……\x01",
            "现在最重要的是现场取证吧。\x02\x03",

            "#0001F以楼顶为中心，\x01",
            "仔细调查一遍吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_21EC")

    label("loc_21A7")


    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F现在还是在楼顶进行现场取证吧，\x01",
            "要找到有关魔兽的线索才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EC")

    TalkEnd(0xFF)
    Jump("loc_2587")

    label("loc_21F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2545")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2250")
    MenuCmd(1, 0, "【４Ｆ 药物学·神经科研究室】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2250")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2287")
    MenuCmd(1, 0, "【１Ｆ 资料室】")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2287")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FE")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    MenuCmd(1, 0, "放弃")
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K 要去哪里？\x07\x00\x02",
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
        (0, "loc_230F"),
        (1, "loc_2355"),
        (2, "loc_239B"),
        (SWITCH_DEFAULT, "loc_23AA"),
    )


    label("loc_230F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2337")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2350")

    label("loc_2337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2350")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2350")

    Jump("loc_23AA")

    label("loc_2355")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_237D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2396")

    label("loc_237D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2396")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2396")

    Jump("loc_23AA")

    label("loc_239B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_23AA")

    label("loc_23AA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_23C6"),
        (1, "loc_24C2"),
        (2, "loc_24F2"),
        (SWITCH_DEFAULT, "loc_24F9"),
    )


    label("loc_23C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2454")

    #C0096
    ChrTalk(
        0x101,
        (
            "#0005F哦……也不知道\x01",
            "约亚西姆医生在不在，\x01",
            "还是先到接待处确认一下吧。\x02\x03",

            "#0003F这里也不是外部人员\x01",
            "可以随便进去的地方。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x5)
    Jump("loc_24BD")

    label("loc_2454")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2493")
    SetScenarioFlags(0x5C, 0)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_24BD")

    label("loc_2493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24B2")
    SetScenarioFlags(0x5C, 1)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()
    Jump("loc_24BD")

    label("loc_24B2")

    EventEnd(0x5)
    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_24BD")

    Jump("loc_24F9")

    label("loc_24C2")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    EventEnd(0x5)
    NewScene("t1620", 114, 0, 0)
    IdleLoop()
    Jump("loc_24F9")

    label("loc_24F2")

    EventEnd(0x3)
    Jump("loc_24F9")

    label("loc_24F9")

    Jump("loc_2540")

    label("loc_24FE")

    TalkBegin(0xFF)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是乌尔斯拉医院的研究楼。\x01",
            "现在没有什么要事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2540")

    Jump("loc_2587")

    label("loc_2545")

    TalkBegin(0xFF)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里是乌尔斯拉医院的研究楼。\x01",
            "现在没有什么要事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2587")

    Return()

    # Function_14_2089 end

    def Function_15_2588(): pass

    label("Function_15_2588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D0")
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
            "#3P#0306F再怎么说，也不可能\x01",
            "是从这里进来的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        (
            "#0001F嗯……下面是水面呢。\x02\x03",

            "狼形魔兽根本就\x01",
            "爬不上来吧。\x02",
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
    Jump("loc_2714")

    label("loc_26D0")

    TalkBegin(0xFF)

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "此处栏杆距离地面相当高，\x01",
            "而且底下还有广阔的水面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2714")

    Return()

    # Function_15_2588 end

    def Function_16_2715(): pass

    label("Function_16_2715")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2855")
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
            "#0200F#6P高度相当高……\x01",
            "但中途有一段屋檐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#0006F#4P嗯～原来如此，\x01",
            "一层的高度被分为两段吗……\x02\x03",

            "#0001F但魔兽要进来的话，\x01",
            "应该还是很困难吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 3970, 7000, 110, 90)
    SetScenarioFlags(0x62, 5)
    OP_29(0x3F, 0x1, 0xC)
    EventEnd(0x5)
    Jump("loc_289B")

    label("loc_2855")

    TalkBegin(0xFF)

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "可以看到正门部分的屋檐，\x01",
            "距离地面似乎有一定的高度。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_289B")

    Return()

    # Function_16_2715 end

    def Function_17_289C(): pass

    label("Function_17_289C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")
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
            "#0101F#12P#N嗯，会不会\x01",
            "是从这里进来的？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0106
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯～魔兽的确很有可能\x01",
            "从这种地形侵入……\x02\x03",

            "#0001F可是，这种高度\x01",
            "仍然是个问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 21200, 7000, 12090, 225)
    SetScenarioFlags(0x62, 6)
    OP_29(0x3F, 0x1, 0xD)
    EventEnd(0x5)
    Jump("loc_2A1A")

    label("loc_29D0")

    TalkBegin(0xFF)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是一片很有可能\x01",
            "会出现魔兽的地形。\x02\x03",

            "但似乎有一定的高度。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2A1A")

    Return()

    # Function_17_289C end

    def Function_18_2A1B(): pass

    label("Function_18_2A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B21")
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
            "#0006F#5P再怎么说，也不会是从\x01",
            "这里侵入的吧。\x02\x03",

            "#0001F如果是会飞行的魔兽，\x01",
            "倒还能理解……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -8770, 7000, 18960, 270)
    SetScenarioFlags(0x62, 7)
    OP_29(0x3F, 0x1, 0xE)
    EventEnd(0x5)
    Jump("loc_2B57")

    label("loc_2B21")

    TalkBegin(0xFF)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "空中走廊距离地面\x01",
            "似乎有相当的高度。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2B57")

    Return()

    # Function_18_2A1B end

    def Function_19_2B58(): pass

    label("Function_19_2B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C94")
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
        "#0005F#11P这里是……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#0100F#11P嗯，从这里的话，\x01",
            "似乎进得来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#0000F#11P的确，这种高度\x01",
            "也不是跳不上来呢。\x02\x03",

            "#0008F这样的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -29060, 6000, 17010, 0)
    SetScenarioFlags(0x63, 0)
    OP_29(0x3F, 0x1, 0xF)
    ModifyEventFlags(0, 4, 0x80)
    EventEnd(0x5)
    Jump("loc_2CC8")

    label("loc_2C94")

    TalkBegin(0xFF)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "栏杆的正下方\x01",
            "堆放着木箱和集装箱。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_2CC8")

    Return()

    # Function_19_2B58 end

    def Function_20_2CC9(): pass

    label("Function_20_2CC9")

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
            "#0001F#6P莫非……\x01",
            "这里就是受害者被袭击的地方？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x136,
        (
            "#1303F#11P嗯……\x01",
            "是病房楼的楼顶。\x02\x03",

            "#1300F怎么办？\x01",
            "先调查这里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        (
            "#0000F#6P不……在此之前，\x01",
            "还是想先听听受害者怎么说。\x02\x03",

            "稍后再带我们来好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x136,
        (
            "#1300F#11P明白了。\x02\x03",

            "遇袭的实习医生\x01",
            "在二楼的病房里，我带你们去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#0000F#6P嗯，拜托了。\x02",
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

    # Function_20_2CC9 end

    def Function_21_2F22(): pass

    label("Function_21_2F22")


    def lambda_2F27():
        OP_95(0xFE, -1680, 7000, 22860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F27)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    Sound(105, 0, 100, 0)
    OP_79(0x4)

    def lambda_2F60():
        OP_95(0xFE, -1550, 7000, 25460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F60)
    Sleep(500)

    def lambda_2F7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F7D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_2F22 end

    def Function_22_2F92(): pass

    label("Function_22_2F92")


    def lambda_2F97():
        OP_95(0xFE, -1680, 7000, 22860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F97)
    WaitChrThread(0xFE, 1)

    def lambda_2FB5():
        OP_95(0xFE, -1550, 7000, 25460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FB5)
    Sleep(500)

    def lambda_2FD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FD2)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_2F92 end

    def Function_23_2FE7(): pass

    label("Function_23_2FE7")

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
            "#0005F#5P从听到的情况看来……\x01",
            "这一带就是现场吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30C0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_30C0)
    WaitChrThread(0x136, 1)
    Sleep(300)

    #C0120
    ChrTalk(
        0x136,
        (
            "#1301F#5P嗯嗯，利顿医生\x01",
            "就是在那条长椅附近\x01",
            "晕倒的。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#0001F#5P是吗……\x02",
    )

    CloseMessageWindow()

    def lambda_3124():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3124)
    WaitChrThread(0x101, 1)
    Sleep(500)

    def lambda_3138():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3138)
    Sleep(100)

    def lambda_3148():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3148)
    Sleep(100)

    def lambda_3158():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3158)
    Sleep(400)

    def lambda_3168():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3168)
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
            "#6P#0005F这栋建筑物……\x01",
            "好像是『研究楼』吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31E6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31E6)
    Sleep(50)

    def lambda_31F6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_31F6)
    Sleep(50)

    def lambda_3206():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3206)
    Sleep(50)

    def lambda_3216():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3216)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x136, 1)

    #C0123
    ChrTalk(
        0x136,
        (
            "#12P#1300F嗯，医生和实习医生们\x01",
            "都在里面工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#0200F#6P有没有为了做实验\x01",
            "而饲养什么危险的魔兽……？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x136,
        (
            "#12P#1304F呵呵，才不会啦。\x02\x03",

            "#1300F不过倒是有用来培育研究用的植物，\x01",
            "类似温室一样的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#6P#0100F原来如此……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(15000, 8000, -15500, 1200)
    MoveCamera(45, 18, 0, 1200)

    def lambda_334E():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_334E)
    Sleep(50)

    def lambda_335E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_335E)
    Sleep(50)

    def lambda_336E():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_336E)
    Sleep(50)

    def lambda_337E():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_337E)
    Sleep(50)

    def lambda_338E():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_338E)
    OP_6F(0x51)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0127
    ChrTalk(
        0x101,
        (
            "#0004F#5P塞茜尔姐姐，谢谢你给我们带路。\x02\x03",

            "#0000F总之，我们先调查一遍，\x01",
            "看能不能发现什么吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x136,
        (
            "#1300F#12P嗯，好的。\x02\x03",

            "#1309F那么，各位，\x01",
            "要加油调查哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#0102F#5P好的。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        "#0202F#5P……辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#0309F#5P敬请期待\x01",
            "我们的好消息吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_349E():

        label("loc_349E")

        TurnDirection(0x101, 0x136, 500)
        Yield()
        Jump("loc_349E")

    QueueWorkItem2(0x101, 1, lambda_349E)

    def lambda_34B0():

        label("loc_34B0")

        TurnDirection(0x102, 0x136, 500)
        Yield()
        Jump("loc_34B0")

    QueueWorkItem2(0x102, 1, lambda_34B0)

    def lambda_34C2():

        label("loc_34C2")

        TurnDirection(0x103, 0x136, 500)
        Yield()
        Jump("loc_34C2")

    QueueWorkItem2(0x103, 1, lambda_34C2)

    def lambda_34D4():

        label("loc_34D4")

        TurnDirection(0x104, 0x136, 500)
        Yield()
        Jump("loc_34D4")

    QueueWorkItem2(0x104, 1, lambda_34D4)
    OP_93(0x136, 0x13B, 0x1F4)
    OP_68(13760, 8000, -12780, 3000)

    def lambda_34FE():
        OP_95(0xFE, 11170, 7000, -14900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_34FE)
    WaitChrThread(0x136, 1)

    def lambda_351C():
        OP_95(0xFE, 10070, 7000, -2850, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_351C)
    Sleep(3000)
    StopBGM(0xBB8)
    WaitChrThread(0x136, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_68(15390, 8000, -13910, 1500)

    def lambda_3563():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3563)
    WaitChrThread(0x101, 1)

    def lambda_3574():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3574)
    Sleep(100)

    def lambda_3584():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3584)

    def lambda_3591():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3591)
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
            "#11P#0003F总之，先以楼顶为中心，\x01",
            "全部调查一遍吧。\x02\x03",

            "#0001F狼形魔兽\x01",
            "确实出现在了楼顶上──\x02\x03",

            "以此为前提，要尽量\x01",
            "找到侵入地点。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        "#6P#0100F嗯嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#0202F#1P是要用罗伊德前辈擅长的\x01",
            "排除法吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        "#5P#0300F那么，就调查看看吧。\x02",
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

    # Function_23_2FE7 end

    def Function_24_36EA(): pass

    label("Function_24_36EA")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-20770, 7000, 15490, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38B0")
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    #C0136
    ChrTalk(
        0x8,
        (
            "……哎呀，你们\x01",
            "迷路了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "这里可不是外部人员可以进来的地方哦。\x01",
            "先去医院接待处\x01",
            "通告一声再来吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37BE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37BE)
    Sleep(50)

    def lambda_37CE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_37CE)
    Sleep(50)

    def lambda_37DE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_37DE)
    Sleep(50)

    def lambda_37EE():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_37EE)
    WaitChrThread(0x0, 1)

    #C0138
    ChrTalk(
        0x101,
        (
            "#0005F哦……对不起。\x02\x03",

            "#0006F（在医院里闲逛之前，\x01",
            "　果然还是应该先去和塞茜尔姐姐\x01",
            "　见个面为好啊……）\x02\x03",

            "（接待处应该在\x01",
            "  病房楼一层的大厅，\x01",
            "  在那里让人帮忙传一下话吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3933")

    label("loc_38B0")

    TurnDirection(0x8, 0x0, 500)

    #C0139
    ChrTalk(
        0x8,
        (
            "这里可不是外部人员可以进入的地方哦。\x01",
            "先去医院接待处通告一声再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "接待处就在病房楼一层的大厅。\x01",
            "喏，快去那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3933")

    Sleep(50)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -16660, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_24_36EA end

    def Function_25_3955(): pass

    label("Function_25_3955")

    EventBegin(0x1)
    Call(0, 27)
    Sleep(50)
    SetChrPos(0x0, -1500, 6500, 21500, 180)
    EventEnd(0x4)
    Return()

    # Function_25_3955 end

    def Function_26_3971(): pass

    label("Function_26_3971")

    EventBegin(0x1)
    Call(0, 27)
    Sleep(50)
    SetChrPos(0x0, -22500, 6000, 21500, 182)
    EventEnd(0x4)
    Return()

    # Function_26_3971 end

    def Function_27_398D(): pass

    label("Function_27_398D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A47")

    #C0141
    ChrTalk(
        0x104,
        (
            "#0305F哦……\x01",
            "往这边走的话，就回到\x01",
            "建筑物里面去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#0001F还什么都没发现呢，\x01",
            "再调查一下吧。\x02\x03",

            "这个楼顶上出现了狼形魔兽……\x01",
            "我们就来寻找可以证明这一点的证据吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3A91")

    label("loc_3A47")


    #C0143
    ChrTalk(
        0x101,
        (
            "#0001F还什么都没发现呢，\x01",
            "继续在楼顶上寻找\x01",
            "狼形魔兽曾经出现的证据吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A91")

    Return()

    # Function_27_398D end

    SaveToFile()

Try(main)
