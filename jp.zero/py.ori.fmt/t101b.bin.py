from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t101b.bin",                # FileName
        "t101b",                    # MapName
        "t101b",                    # Location
        0x0042,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 5],
    )

    BuildStringList((
        "t101b",                  # 0
        "エミー",                 # 1
        "ゼル",                   # 2
        "カビラン",               # 3
        "ルーグマン",             # 4
        "招待客",                 # 5
        "犬１",                   # 6
        "犬２",                   # 7
        "犬３",                   # 8
        "犬４",                   # 9
        "レクター",               # 10
        "黒い仔猫",               # 11
        "キリカ",                 # 12
        "マフィアその１",         # 13
        "マフィアその２",         # 14
        "ドーベンカイザーその１", # 15
        "SE制御",                 # 16
        "bt101b",                 # 17
        "bt101b",                 # 18
        "bt101b",                 # 19
        "BT101b",                 # 20
        "議長邸方面",             # 21
        "ホテル・デルフィニア方面",# 22
    ))

    ATBonus("ATBonus_384", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_364", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_428", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_430", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_434", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_438", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_43C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_444", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 0, 0, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_530", 0x000A, 27, 6, 0, 0, 0, 0, 0, "BT101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67100.dat", "ms67100.dat", "ms67100.dat", "ms67100.dat", 0, 0, 0, 0, "MonsterBattlePostion_3A4", "MonsterBattlePostion_424", "ed7509", "ed7000", "ATBonus_384"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_464", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31102.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_424", "ed7509", "ed7000", "ATBonus_364"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4A8", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31002.dat", "ms31900.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_424", "ed7509", "ed7000", "ATBonus_364"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4EC", 0x000A, 27, 6, 0, 0, 0, 0, 0, "bt101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31102.dat", "ms31900.dat", "ms67100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_424", "ed7509", "ed7000", "ATBonus_364"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch22302.itc",                   # 00
        "chr/ch22202.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch27600.itc",                   # 04
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
        "monster/ch67151.itc",               # 1A
        "chr/ch31051.itc",                   # 1B
        "chr/ch31151.itc",                   # 1C
        "chr/ch31951.itc",                   # 1D
    ))

    DeclNpc(2279,    -3700,   -12430,  180,  469,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(3660,    -3700,   -12430,  180,  469,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  385,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-1970,   -2000,   34720,   180,  385,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2400,    -1799,   55840,   0,    385,  0x0, 0,   4,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   26,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  0.0,                   6.0,                   -2.799999952316284,    225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -2.0,                  0.5600000023841858,    1.0])

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "議長邸方面")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

    ScpFunction((
        "Function_0_5D4",          # 00, 0
        "Function_1_68C",          # 01, 1
        "Function_2_6ED",          # 02, 2
        "Function_3_74E",          # 03, 3
        "Function_4_76A",          # 04, 4
        "Function_5_7FE",          # 05, 5
        "Function_6_826",          # 06, 6
        "Function_7_A27",          # 07, 7
        "Function_8_BEF",          # 08, 8
        "Function_9_F0B",          # 09, 9
        "Function_10_1032",        # 0A, 10
        "Function_11_111E",        # 0B, 11
        "Function_12_1179",        # 0C, 12
        "Function_13_17E6",        # 0D, 13
        "Function_14_1828",        # 0E, 14
        "Function_15_186A",        # 0F, 15
        "Function_16_18AC",        # 10, 16
        "Function_17_18EE",        # 11, 17
        "Function_18_190A",        # 12, 18
        "Function_19_1929",        # 13, 19
        "Function_20_194E",        # 14, 20
        "Function_21_1968",        # 15, 21
        "Function_22_1D0C",        # 16, 22
        "Function_23_252E",        # 17, 23
    ))


    def Function_0_5D4(): pass

    label("Function_0_5D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_614"),
        (1, "loc_620"),
        (2, "loc_62C"),
        (3, "loc_638"),
        (4, "loc_644"),
        (5, "loc_650"),
        (6, "loc_65C"),
        (SWITCH_DEFAULT, "loc_668"),
    )


    label("loc_614")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_620")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_62C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_638")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_644")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_650")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_65C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_668")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_674")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_674")

    label("loc_68B")

    Return()

    # Function_0_5D4 end

    def Function_1_68C(): pass

    label("Function_1_68C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EC")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_68C")

    label("loc_6EC")

    Return()

    # Function_1_68C end

    def Function_2_6ED(): pass

    label("Function_2_6ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74D")
    OP_95(0xFE, -1970, -2000, 34720, 2000, 0x0)
    OP_95(0xFE, -1970, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 8940, 2000, 0x0)
    OP_95(0xFE, 2029, -2000, 34720, 2000, 0x0)
    Jump("Function_2_6ED")

    label("loc_74D")

    Return()

    # Function_2_6ED end

    def Function_3_74E(): pass

    label("Function_3_74E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_769")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_3_74E")

    label("loc_769")

    Return()

    # Function_3_74E end

    def Function_4_76A(): pass

    label("Function_4_76A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_779")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 22)

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_787")
    Jump("loc_7B4")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_END)), "loc_7B4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B4")
    Event(0, 23)

    label("loc_7B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_7D8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2450, -3800, -10800, 90)
    Jump("loc_7FD")

    label("loc_7D8")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    BeginChrThread(0xA, 0, 0, 1)
    BeginChrThread(0xB, 0, 0, 2)

    label("loc_7FD")

    Return()

    # Function_4_76A end

    def Function_5_7FE(): pass

    label("Function_5_7FE")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_816")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_816")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_81F")

    label("loc_81F")

    Sound(126, 1, 80, 0)
    Return()

    # Function_5_7FE end

    def Function_6_826(): pass

    label("Function_6_826")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BA")
    Jump("loc_904")

    label("loc_8BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_904")

    label("loc_8DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_904")

    label("loc_8FA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_904")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_937")
    Jump("loc_A1F")

    label("loc_937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_945")
    Jump("loc_A1F")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_953")
    Jump("loc_A1F")

    label("loc_953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_961")
    Jump("loc_A1F")

    label("loc_961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_9FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97C")
    Call(0, 8)
    Jump("loc_9F5")

    label("loc_97C")


    #C0001
    ChrTalk(
        0xFE,
        (
            "ゼルったら……\x01",
            "紳士的振る舞いだけは合格ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "あとはもっと、\x01",
            "あたしに相応しい\x01",
            "かっこいい人になってもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F5")

    Jump("loc_A1F")

    label("loc_9FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_A08")
    Jump("loc_A1F")

    label("loc_A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_A16")
    Jump("loc_A1F")

    label("loc_A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A1F")

    label("loc_A1F")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_826 end

    def Function_7_A27(): pass

    label("Function_7_A27")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ABB")
    Jump("loc_B05")

    label("loc_ABB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ADB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B05")

    label("loc_ADB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AFB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B05")

    label("loc_AFB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B05")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_B38")
    Jump("loc_BE7")

    label("loc_B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_B46")
    Jump("loc_BE7")

    label("loc_B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_B54")
    Jump("loc_BE7")

    label("loc_B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_B62")
    Jump("loc_BE7")

    label("loc_B62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7D")
    Call(0, 8)
    Jump("loc_BBD")

    label("loc_B7D")


    #C0003
    ChrTalk(
        0xFE,
        (
            "……？\x01",
            "エミー、何か顔が赤いよ？\x01",
            "風邪でもひいたんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBD")

    Jump("loc_BE7")

    label("loc_BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_BD0")
    Jump("loc_BE7")

    label("loc_BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_BDE")
    Jump("loc_BE7")

    label("loc_BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BE7")

    label("loc_BE7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_A27 end

    def Function_8_BEF(): pass

    label("Function_8_BEF")

    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x9, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C83")
    Jump("loc_CCD")

    label("loc_C83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CA3")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCD")

    label("loc_CA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CC3")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCD")

    label("loc_CC3")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCD")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x8, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D86")
    Jump("loc_DD0")

    label("loc_D86")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DA6")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD0")

    label("loc_DA6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DC6")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DD0")

    label("loc_DC6")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DD0")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0004
    ChrTalk(
        0x8,
        (
            "いいこと、ゼル？\x01",
            "あなたはあたしの許婚なんだから\x01",
            "あたしの体を気遣わなきゃいけないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "……へくちっ。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "エミー、寒いんじゃない？\x01",
            "一日中こんな水辺で\x01",
            "しゃべってるから……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "お家に帰って\x01",
            "暖かいスープでも飲もうよ。\x01",
            "屋敷まで送るからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "…………ぽっ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_8_BEF end

    def Function_9_F0B(): pass

    label("Function_9_F0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_F55")

    #C0009
    ChrTalk(
        0xFE,
        (
            "あ、あわわ……！\x01",
            "なんでこんなところに魔獣が……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102E")

    label("loc_F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_F63")
    Jump("loc_102E")

    label("loc_F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_F71")
    Jump("loc_102E")

    label("loc_F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_F7F")
    Jump("loc_102E")

    label("loc_F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_1009")

    #C0010
    ChrTalk(
        0xFE,
        (
            "……ふぅん。\x01",
            "なかなか上品な格好を\x01",
            "しているじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "もしかして君たちも\x01",
            "ハルトマン議長邸に\x01",
            "招待されたクチかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102E")

    label("loc_1009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1017")
    Jump("loc_102E")

    label("loc_1017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_1025")
    Jump("loc_102E")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_102E")

    label("loc_102E")

    TalkEnd(0xFE)
    Return()

    # Function_9_F0B end

    def Function_10_1032(): pass

    label("Function_10_1032")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_1043")
    Jump("loc_111A")

    label("loc_1043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 2)), scpexpr(EXPR_END)), "loc_1051")
    Jump("loc_111A")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 1)), scpexpr(EXPR_END)), "loc_105F")
    Jump("loc_111A")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_106D")
    Jump("loc_111A")

    label("loc_106D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 7)), scpexpr(EXPR_END)), "loc_10F5")

    #C0012
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長の邸宅前に\x01",
            "黒服が立っているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "流石、クロスベルの実質トップともなれば\x01",
            "その警備も万全らしい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111A")

    label("loc_10F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_END)), "loc_1103")
    Jump("loc_111A")

    label("loc_1103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_END)), "loc_1111")
    Jump("loc_111A")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_111A")

    label("loc_111A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1032 end

    def Function_11_111E(): pass

    label("Function_11_111E")

    TalkBegin(0xFE)

    #C0014
    ChrTalk(
        0xFE,
        (
            "さて……急がなければ。\x01",
            "招待を受けておいて遅れましたじゃ\x01",
            "示しがつかないからな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_111E end

    def Function_12_1179(): pass

    label("Function_12_1179")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("monster/ch67150.itc", 0x23)
    LoadChrToIndex("monster/ch67151.itc", 0x24)
    LoadChrToIndex("monster/ch67152.itc", 0x25)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(420, -500, 6130, 0)
    MoveCamera(309, 18, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19430, 0)
    SetChrPos(0x101, 390, -1800, 11210, 180)
    SetChrPos(0x102, 1320, -1800, 11960, 180)
    SetChrPos(0x103, -1280, -1800, 13280, 180)
    SetChrPos(0x104, -280, -2000, 14780, 180)
    SetChrPos(0x105, -2040, -2000, 15280, 180)
    SetChrPos(0x133, -1620, -1800, 6940, 135)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x4)
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0xD, 27210, -2000, 1000, 270)
    SetChrPos(0xE, 25090, -2000, 250, 270)
    SetChrPos(0xF, 28070, -2000, -1440, 270)
    SetChrPos(0x10, 29870, -2000, -300, 270)
    BeginChrThread(0xD, 0, 0, 17)
    Sleep(10)
    BeginChrThread(0xE, 0, 0, 17)
    Sleep(10)
    BeginChrThread(0xF, 0, 0, 17)
    Sleep(10)
    BeginChrThread(0x10, 0, 0, 17)
    ModifyEventFlags(0, 0, 0x80)
    FadeToBright(1000, 0)
    SetCameraDistance(16930, 1500)

    def lambda_1435():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1435)

    def lambda_144A():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_144A)

    def lambda_145F():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_145F)

    def lambda_1474():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1474)

    def lambda_1489():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1489)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Sound(836, 0, 100, 0)
    OP_6F(0x10)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_1536():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1536)
    Sleep(50)

    def lambda_1546():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1546)
    Sleep(50)

    def lambda_1556():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1556)
    Sleep(50)

    def lambda_1566():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1566)
    Sleep(50)

    def lambda_1576():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1576)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Fade(1000)
    OP_68(19350, -500, -880, 0)
    MoveCamera(300, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(32759, 0)
    OP_68(14350, -500, -880, 3000)
    SetCameraDistance(16680, 3000)
    MoveCamera(318, 15, 0, 3000)
    BeginChrThread(0xD, 3, 0, 13)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0x10, 3, 0, 16)
    BeginChrThread(0x17, 1, 0, 20)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(1780, -500, 5030, 0)
    MoveCamera(318, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(20680, 0)
    OP_68(2740, -500, 3670, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18660, 0)
    OP_68(1900, -500, 4600, 2000)
    OP_93(0x101, 0x87, 0x0)
    OP_93(0x102, 0x87, 0x0)
    OP_93(0x103, 0x87, 0x0)
    OP_93(0x104, 0x87, 0x0)
    OP_93(0x105, 0x87, 0x0)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 3)
    EndChrThread(0x17, 0x1)
    OP_6F(0x1)
    OP_0D()

    #C0015
    ChrTalk(
        0x101,
        "#0007F#11Pまさか……街区に犬を！？\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x101,
        "キーア",
        "#5805F#5Pなんかいっぱいいるね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0017
    ChrTalk(
        0x104,
        "#0307F#5P#N来るぞ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 3, 0, 19)
    BeginChrThread(0xF, 3, 0, 19)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 19)
    BeginChrThread(0x10, 3, 0, 19)
    Sleep(200)
    Sound(814, 0, 100, 0)
    SetCameraDistance(14660, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x10, 0x3)
    Battle("BattleInfo_530", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 21)
    Return()

    # Function_12_1179 end

    def Function_13_17E6(): pass

    label("Function_13_17E6")


    def lambda_17EB():
        OP_95(0xFE, 3400, -1800, 2640, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17EB)
    WaitChrThread(0xFE, 1)

    def lambda_1809():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1809)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_13_17E6 end

    def Function_14_1828(): pass

    label("Function_14_1828")


    def lambda_182D():
        OP_95(0xFE, 4100, -1800, -110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_182D)
    WaitChrThread(0xFE, 1)

    def lambda_184B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_184B)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_14_1828 end

    def Function_15_186A(): pass

    label("Function_15_186A")


    def lambda_186F():
        OP_95(0xFE, 6240, -1800, -410, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_186F)
    WaitChrThread(0xFE, 1)

    def lambda_188D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_188D)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_15_186A end

    def Function_16_18AC(): pass

    label("Function_16_18AC")


    def lambda_18B1():
        OP_95(0xFE, 5390, -1800, 2470, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18B1)
    WaitChrThread(0xFE, 1)

    def lambda_18CF():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18CF)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 18)
    Return()

    # Function_16_18AC end

    def Function_17_18EE(): pass

    label("Function_17_18EE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1909")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_17_18EE")

    label("loc_1909")

    Return()

    # Function_17_18EE end

    def Function_18_190A(): pass

    label("Function_18_190A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1928")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_18_190A")

    label("loc_1928")

    Return()

    # Function_18_190A end

    def Function_19_1929(): pass

    label("Function_19_1929")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x25)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    SetChrSubChip(0xFE, 0x3)
    OP_9B(0x1, 0xFE, 0x0, 0x2BC, 0x1770, 0x0)
    Return()

    # Function_19_1929 end

    def Function_20_194E(): pass

    label("Function_20_194E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1967")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_20_194E")

    label("loc_1967")

    Return()

    # Function_20_194E end

    def Function_21_1968(): pass

    label("Function_21_1968")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    LoadChrToIndex("chr/ch00000.itc", 0x25)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    OP_68(780, -500, 4500, 0)
    MoveCamera(312, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19960, 0)
    SetChrPos(0x101, 1870, -1800, 3670, 90)
    SetChrPos(0x102, -430, -1800, 3700, 90)
    SetChrPos(0x103, -1240, -1800, 5800, 90)
    SetChrPos(0x104, -440, -1800, 8090, 90)
    SetChrPos(0x105, 610, -1800, 5940, 90)
    SetChrPos(0x133, 1770, -1800, 2390, 90)
    ClearChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(18460, 2000)
    OP_6F(0x10)
    OP_0D()

    #C0018
    ChrTalk(
        0x102,
        (
            "#0108F#5Pし、信じられない……\x02\x03",

            "#0110F他の観光客だっているのに\x01",
            "軍用犬を放つなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0211F#5Pなりふり構わなく\x01",
            "なってきましたね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x13B, 0x1F4)

    #C0020
    ChrTalk(
        0x101,
        (
            "#0003F#6P……とにかくアーケードを\x01",
            "突破して波止場に向かおう。\x02\x03",

            "#0013F一般市民が巻き込まれたら\x01",
            "そっちも何とかカバーするぞ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C11():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1C11)

    def lambda_1C1E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1C1E)
    Sleep(100)

    def lambda_1C2E():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C2E)

    def lambda_1C3B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C3B)

    def lambda_1C48():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x133, 1, lambda_1C48)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x133, 1)

    #C0021
    ChrTalk(
        0x104,
        "#0306F#11Pおーおー、無茶言いやがる！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        "#0402F#5Pフフ、君たちも苦労してるね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x25)
    SetChrPos(0x0, 500, -1800, 1800, 90)
    SetScenarioFlags(0xA7, 4)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_21_1968 end

    def Function_22_1D0C(): pass

    label("Function_22_1D0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch07400.itc", 0x1E)
    LoadChrToIndex("chr/ch39100.itc", 0x1F)
    LoadChrToIndex("chr/ch07300.itc", 0x20)
    OP_68(0, -2700, -18800, 0)
    MoveCamera(315, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19700, 0)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrPos(0x11, 0, -3800, -14800, 180)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 1000, -3800, -14500, 180)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x13, 4850, -1800, -1450, 270)
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    OP_90(0x0, 25500, -2000, -3000, 270)
    OP_90(0x1, 25500, -2000, -3000, 270)
    OP_90(0x2, 25500, -2000, -3000, 270)
    OP_90(0x3, 25500, -2000, -3000, 270)
    OP_90(0x4, 25500, -2000, -3000, 270)
    OP_90(0x5, 25500, -2000, -3000, 270)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    FadeToBright(1000, 0)
    OP_68(0, -2700, -14800, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    #C0023
    ChrTalk(
        0x11,
        (
            "#3504F#11P……行っちまったなァ。\x02\x03",

            "#3500Fんー、できればもうちょい、\x01",
            "本格的に遊びたかったが……\x02\x03",

            "#3509Fま、あの辺りで我慢しておくか。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)

    #N0024
    NpcTalk(
        0x13,
        "女性の声",
        (
            "#3P……我慢も何も、好き放題に\x01",
            "やっていたのではなくて？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1F7F():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1F7F)
    OP_93(0x11, 0x0, 0x1F4)
    WaitChrThread(0x12, 1)
    Fade(1000)
    OP_68(0, -700, -6800, 0)
    OP_68(0, -2700, -13800, 9000)

    def lambda_1FBE():
        OP_95(0xFE, 0, -1800, -1190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FBE)
    WaitChrThread(0x13, 1)

    def lambda_1FDC():
        OP_95(0xFE, 0, -3800, -12250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1FDC)
    WaitChrThread(0x13, 1)
    OP_6F(0x79)
    OP_0D()

    #C0025
    ChrTalk(
        0x13,
        (
            "#3404F#11P鉄血宰相とハルトマン議長の\x01",
            "間に作られたパイプ……\x02\x03",

            "#3400Fその繋ぎ役としては\x01",
            "いささか不適切な言動が\x01",
            "多かったように見受けられるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x11,
        (
            "#3510F#6Pん～、何のことかな？\x02\x03",

            "別にオレは、誰かさんみたいに\x01",
            "直接助けたワケじゃないからなァ。\x02\x03",

            "#3502Fいいのか、アレ？\x01",
            "完璧に内政干渉だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x13,
        (
            "#3405F#11Pああ、あの偃月輪#6Rえんげつりん#は\x01",
            "なかなか見事だったわね。\x02\x03",

            "#3404F《銀#2Rイン#》とかいう、\x01",
            "噂の凶手でも現れたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x11,
        (
            "#3501F#6P……そう来たか。\x02\x03",

            "#3504Fま、今回のオレの主要任務は\x01",
            "アンタに会うことだったしな。\x02\x03",

            "#3500F《ロックスミス機関》……\x01",
            "キリカ・ロウラン室長どの。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x13,
        (
            "#3400F#11Pフフ、さすがに耳が早いわね。\x02\x03",

            "#3404F帝国政府付き、二等書記官……\x02\x03",

            "#3402Fいえ、帝国軍情報局所属、\x01",
            "レクター・アランドール大尉と\x01",
            "呼んだ方がいいかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x11,
        (
            "#3502F#6Pま、お互いカードは\x01",
            "ある程度見えてるってことか。\x02\x03",

            "#3504F──そんじゃ、ホテルの\x01",
            "ラウンジあたりで話すとするか。\x02\x03",

            "#3500Fクロスベルでの諜報戦に関する\x01",
            "今後の取り決め……\x02\x03",

            "不戦条約と導力ネットを視野に入れた\x01",
            "新時代のルール作りってやつをな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x13,
        (
            "#3402F#11Pええ、始めましょう。\x02\x03",

            "#3404F──破壊工作とテロリズムで\x01",
            "状況を動かす時代は終わったわ。\x02\x03",

            "かつてのような“不幸な事故”を\x01",
            "クロスベルで起こさないためにも……\x02\x03",

            "#3401F私たちは仮初#4Rかりそめ#とはいえ、\x01",
            "新たな秩序を構築する必要がある。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(18700, 3000)
    OP_0D()
    StopBGM(0xFA0)
    OP_25(0x7E, 0x3C)
    Sleep(100)
    OP_25(0x7E, 0x32)
    Sleep(100)
    OP_25(0x7E, 0x28)
    Sleep(100)
    OP_25(0x7E, 0x1E)
    Sleep(100)
    OP_25(0x7E, 0x14)
    Sleep(100)
    OP_25(0x7E, 0xA)
    Sleep(100)
    OP_25(0x7E, 0x0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    SetScenarioFlags(0x5C, 0)
    NewScene("e3010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_1D0C end

    def Function_23_252E(): pass

    label("Function_23_252E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00450.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2578")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)

    label("loc_2578")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2590")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)

    label("loc_2590")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25A8")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_25A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25C0")
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)

    label("loc_25C0")

    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_25F2"),
        (1, "loc_25FF"),
        (2, "loc_260C"),
        (SWITCH_DEFAULT, "loc_2619"),
    )


    label("loc_25F2")

    SetChrChipByIndex(0x14, 0x1B)
    SetChrChipByIndex(0x15, 0x1C)
    Jump("loc_2619")

    label("loc_25FF")

    SetChrChipByIndex(0x14, 0x1B)
    SetChrChipByIndex(0x15, 0x1D)
    Jump("loc_2619")

    label("loc_260C")

    SetChrChipByIndex(0x14, 0x1C)
    SetChrChipByIndex(0x15, 0x1D)
    Jump("loc_2619")

    label("loc_2619")

    SetChrSubChip(0x14, 0x0)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    OP_52(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x16, 1, 0, 3)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    OP_68(32650, -200, -50, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 32650, -2000, 700, 270)
    SetChrPos(0x1, 32900, -2000, -800, 270)
    SetChrPos(0x2, 34150, -2000, 700, 270)
    SetChrPos(0x3, 34400, -2000, -800, 270)
    SetChrPos(0x133, 35900, -2000, -50, 270)
    SetChrPos(0x14, 26150, -2000, -50, 90)
    SetChrPos(0x15, 24150, -2000, -800, 90)
    SetChrPos(0x16, 25150, -2000, 700, 90)

    def lambda_2725():
        OP_98(0x14, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2725)
    Sleep(50)

    def lambda_2742():
        OP_98(0x15, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2742)
    Sleep(50)

    def lambda_275F():
        OP_98(0x16, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_275F)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0x14, 1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_279E"),
        (1, "loc_27BD"),
        (2, "loc_27DC"),
        (SWITCH_DEFAULT, "loc_27FB"),
    )


    label("loc_279E")

    Battle("BattleInfo_464", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Jump("loc_27FB")

    label("loc_27BD")

    Battle("BattleInfo_4A8", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Jump("loc_27FB")

    label("loc_27DC")

    Battle("BattleInfo_4EC", 0x0, 0x0, 0x0, 0xF, 0xFF)
    FadeToDark(0, 0, -1)
    Jump("loc_27FB")

    label("loc_27FB")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_281D")
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    label("loc_281D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2835")
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    label("loc_2835")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_284D")
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    label("loc_284D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2865")
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    label("loc_2865")

    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x16, 0x2)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    OP_68(33150, -200, -50, 0)
    MoveCamera(315, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(37000, 0)
    SetChrPos(0x0, 33150, -2000, -50, 270)
    SetChrPos(0x1, 33150, -2000, -50, 270)
    SetChrPos(0x2, 33150, -2000, -50, 270)
    SetChrPos(0x3, 33150, -2000, -50, 270)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_252E end

    SaveToFile()

Try(main)
