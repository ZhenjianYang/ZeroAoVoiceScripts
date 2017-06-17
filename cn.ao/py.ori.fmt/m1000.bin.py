from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1000.bin",                # FileName
        "m1000",                    # MapName
        "m1000",                    # Location
        0x006B,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 107, 0, 2, 0, 3],
    )

    BuildStringList((
        "m1000",                  # 0
        "先驱者",                 # 1
        "先驱者",                 # 2
        "『刚毅』艾奈丝",         # 3
        "SE控制",                 # 4
        "bm1080",                 # 5
        "乌尔斯拉间道方向",       # 6
    ))

    ATBonus("ATBonus_34C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_40C", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_400", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_404", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_42C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm1080", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_40C", "MonsterBattlePostion_3EC", "ed7451", "ed7453", "ATBonus_34C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "monster/ch80050.itc",               # 00
        "chr/ch43200.itc",                   # 01
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

    DeclNpc(29950,   -13199,  97660,   180,  453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(39959,   -13199,  97639,   180,  453,  0x0, 0,   0,   0,   0,   1,   255, 255, 255,  0)
    DeclNpc(34990,   -13199,  99489,   180,  453,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 13,  35.0,                  94.5,                  -13.199999809265137,   10920.25,              [0.09090908616781235,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.05263157933950424,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.1818180084228516,   -4.973684310913086,    2.640000104904175,     1.0])
    DeclEvent(0x0000, 0, 14,  34.5,                  72.0,                  -14.199999809265137,   225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.450000047683716,    -24.0,                 2.8399999141693115,    1.0])
    DeclEvent(0x0000, 0, 6,   6.940000057220459,     26.5,                  -3.880000114440918,    182.25,                [0.1111111119389534,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.7711111307144165,   -8.833333015441895,    0.7760000228881836,    1.0])

    DeclActor(43800,   -13200,  94690,   1200,    43800,   -11200,  94690,   0x007C, 0,  4,  0x0000)
    DeclActor(45150,   -13240,  95200,   1200,    45150,   -11240,  95200,   0x007C, 0,  4,  0x0000)
    DeclActor(34360,   -13200,  99420,   1200,    34360,   -11200,  99420,   0x007C, 0,  21, 0x0000)

    PlaceName(-1.100000023841858, 0.0, -30.0, 0x0000, 0x0000, "乌尔斯拉间道方向")

    ChipFrameInfo(1224, 0)                                       # 0

    ScpFunction((
        "Function_0_4C8",          # 00, 0
        "Function_1_580",          # 01, 1
        "Function_2_630",          # 02, 2
        "Function_3_B7C",          # 03, 3
        "Function_4_D8F",          # 04, 4
        "Function_5_10BC",         # 05, 5
        "Function_6_1150",         # 06, 6
        "Function_7_1185",         # 07, 7
        "Function_8_1989",         # 08, 8
        "Function_9_1CB6",         # 09, 9
        "Function_10_1D1D",        # 0A, 10
        "Function_11_20B6",        # 0B, 11
        "Function_12_2174",        # 0C, 12
        "Function_13_21A9",        # 0D, 13
        "Function_14_267A",        # 0E, 14
        "Function_15_3221",        # 0F, 15
        "Function_16_323C",        # 10, 16
        "Function_17_3278",        # 11, 17
        "Function_18_32C5",        # 12, 18
        "Function_19_4009",        # 13, 19
        "Function_20_404D",        # 14, 20
        "Function_21_4066",        # 15, 21
    ))


    def Function_0_4C8(): pass

    label("Function_0_4C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_508"),
        (1, "loc_514"),
        (2, "loc_520"),
        (3, "loc_52C"),
        (4, "loc_538"),
        (5, "loc_544"),
        (6, "loc_550"),
        (SWITCH_DEFAULT, "loc_55C"),
    )


    label("loc_508")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_514")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_520")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_52C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_538")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_544")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_550")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_55C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_568")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_568")

    label("loc_57F")

    Return()

    # Function_0_4C8 end

    def Function_1_580(): pass

    label("Function_1_580")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5B8"),
        (1, "loc_5C4"),
        (2, "loc_5D0"),
        (3, "loc_5DC"),
        (4, "loc_5E8"),
        (5, "loc_5F4"),
        (6, "loc_600"),
        (SWITCH_DEFAULT, "loc_60C"),
    )


    label("loc_5B8")

    OP_A0(0xFE, 1450, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5C4")

    OP_A0(0xFE, 1550, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5D0")

    OP_A0(0xFE, 1600, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5DC")

    OP_A0(0xFE, 1400, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5E8")

    OP_A0(0xFE, 1650, 0x0, 0x5)
    Jump("loc_618")

    label("loc_5F4")

    OP_A0(0xFE, 1350, 0x0, 0x5)
    Jump("loc_618")

    label("loc_600")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_618")

    label("loc_60C")

    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_618")

    label("loc_618")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62F")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_618")

    label("loc_62F")

    Return()

    # Function_1_580 end

    def Function_2_630(): pass

    label("Function_2_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)

    label("loc_65C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E9")
    SetScenarioFlags(0x38, 0)

    label("loc_6E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF")
    SetScenarioFlags(0x38, 1)

    label("loc_6FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    SetScenarioFlags(0x38, 2)

    label("loc_715")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72B")
    SetScenarioFlags(0x38, 3)

    label("loc_72B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_741")
    SetScenarioFlags(0x38, 4)

    label("loc_741")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_757")
    SetScenarioFlags(0x38, 5)

    label("loc_757")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76D")
    SetScenarioFlags(0x38, 6)

    label("loc_76D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783")
    SetScenarioFlags(0x38, 7)

    label("loc_783")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_799")
    SetScenarioFlags(0x39, 0)

    label("loc_799")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AF")
    SetScenarioFlags(0x39, 1)

    label("loc_7AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C5")
    SetScenarioFlags(0x39, 2)

    label("loc_7C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DB")
    SetScenarioFlags(0x39, 3)

    label("loc_7DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    SetScenarioFlags(0x39, 4)

    label("loc_7F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_807")
    SetScenarioFlags(0x39, 5)

    label("loc_807")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81D")
    SetScenarioFlags(0x39, 6)

    label("loc_81D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    SetScenarioFlags(0x39, 7)

    label("loc_833")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849")
    SetScenarioFlags(0x3A, 0)

    label("loc_849")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_85F")
    SetScenarioFlags(0x3A, 1)

    label("loc_85F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_875")
    SetScenarioFlags(0x3A, 2)

    label("loc_875")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88B")
    SetScenarioFlags(0x3A, 3)

    label("loc_88B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A1")
    SetScenarioFlags(0x3A, 4)

    label("loc_8A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B7")
    SetScenarioFlags(0x3A, 5)

    label("loc_8B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD")
    SetScenarioFlags(0x3A, 6)

    label("loc_8CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E3")
    SetScenarioFlags(0x3A, 7)

    label("loc_8E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F9")
    SetScenarioFlags(0x3B, 0)

    label("loc_8F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90F")
    SetScenarioFlags(0x3B, 1)

    label("loc_90F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    SetScenarioFlags(0x3B, 2)

    label("loc_925")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93B")
    SetScenarioFlags(0x3B, 3)

    label("loc_93B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_951")
    SetScenarioFlags(0x3B, 4)

    label("loc_951")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_967")
    SetScenarioFlags(0x3B, 5)

    label("loc_967")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97D")
    SetScenarioFlags(0x3B, 6)

    label("loc_97D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")
    SetScenarioFlags(0x3B, 7)

    label("loc_993")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    SetScenarioFlags(0x3D, 5)

    label("loc_9A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BF")
    SetScenarioFlags(0x3D, 6)

    label("loc_9BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D5")
    SetScenarioFlags(0x3D, 7)

    label("loc_9D5")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A10")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_B00")

    label("loc_A10")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A33")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_B00")

    label("loc_A33")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A56")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_B00")

    label("loc_A56")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A79")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_B00")

    label("loc_A79")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9C")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_B00")

    label("loc_A9C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABF")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_B00")

    label("loc_ABF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE2")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_B00")

    label("loc_AE2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B00")
    SetScenarioFlags(0x3C, 7)

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B16")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B48")
    SetChrPos(0x0, 42960, -13200, 94790, 260)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 5)

    label("loc_B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_B7B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")
    SetChrPos(0x0, 45150, -13240, 95200, 260)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_B7B")

    Return()

    # Function_2_630 end

    def Function_3_B7C(): pass

    label("Function_3_B7C")

    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BBA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3E")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_C3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C75")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x12C, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "gray")

    label("loc_C75")

    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CAB")
    SetMapObjFlags(0x7, 0x4)
    OP_65(0x2, 0x1)

    label("loc_CAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD5")
    SetMapObjFlags(0x7, 0x4)
    OP_65(0x2, 0x1)

    label("loc_CD5")

    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CEF")
    ClearMapObjFlags(0xB, 0x4)

    label("loc_CEF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D0D")
    ClearMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0xA, 0x4)

    label("loc_D0D")

    MiniGame(0x2F, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_D5E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D76")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_D76")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8E")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_D8E")

    Return()

    # Function_3_B7C end

    def Function_4_D8F(): pass

    label("Function_4_D8F")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC1")
    SetScenarioFlags(0x31, 2)

    label("loc_DC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DF6")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_DFC")

    label("loc_DF6")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_DFC")

    Jump("loc_E07")

    label("loc_E01")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_E07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_E78")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E58"),
        (SWITCH_DEFAULT, "loc_E69"),
    )


    label("loc_E58")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_E73")

    label("loc_E69")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E73")

    Jump("loc_10A9")

    label("loc_E78")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_EA8")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_EA8")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_ED2"),
        (1, "loc_FD6"),
        (2, "loc_1067"),
        (SWITCH_DEFAULT, "loc_109F"),
    )


    label("loc_ED2")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F03")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F13")

    label("loc_F03")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F13")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F69")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F69")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8C")
    Sound(461, 0, 100, 0)

    label("loc_F8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_FAC")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_FBC")

    label("loc_FAC")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_FBC")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_E07")

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1048")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_100B")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1023")

    label("loc_100B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_101E")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1023")

    label("loc_101E")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1023")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1062")

    label("loc_1048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1058")
    OP_AF(0xFB)
    Jump("loc_1062")

    label("loc_1058")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1062")

    Jump("loc_10A9")

    label("loc_1067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1080")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_109A")

    label("loc_1080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1090")
    OP_AF(0xFB)
    Jump("loc_109A")

    label("loc_1090")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_109A")

    Jump("loc_10A9")

    label("loc_109F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10A9")

    Jump("loc_E07")

    label("loc_10AE")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_4_D8F end

    def Function_5_10BC(): pass

    label("Function_5_10BC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1117")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_110C")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_1112")

    label("loc_110C")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_1112")

    Jump("loc_113B")

    label("loc_1117")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1135")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_113B")

    label("loc_1135")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_113B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_5_10BC end

    def Function_6_1150(): pass

    label("Function_6_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_1161")
    Call(0, 9)
    Jump("loc_1175")

    label("loc_1161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_1172")
    Call(0, 8)
    Jump("loc_1175")

    label("loc_1172")

    Call(0, 7)

    label("loc_1175")

    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    Return()

    # Function_6_1150 end

    def Function_7_1185(): pass

    label("Function_7_1185")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1763")

    #A0001
    AnonymousTalk(
        0x105,
        (
            "#10401F『噬身之蛇』守在这里吗……\x02\x03",

            "#10403F那个身穿铠甲，守着大门的女孩，\x01",
            "是『钢之圣女』的部下之一呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0x101,
        (
            "#00013F她两旁的智能兵器很大啊……\x01",
            "以前从没见过那种类型。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12E8")

    #A0003
    AnonymousTalk(
        0x103,
        (
            "#00208F和我在数据库中见过的，\x01",
            "利贝尔发生异变时，\x01",
            "结社所使用的那种类型很相似……\x02",
        )
    )

    CloseMessageWindow()

    #A0004
    AnonymousTalk(
        0x105,
        (
            "#10401F是『先驱者』吧？\x01",
            "好像是高性能的白刃战类型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1360")

    label("loc_12E8")


    #A0005
    AnonymousTalk(
        0x105,
        (
            "#10403F据说在利贝尔异变的时候，\x01",
            "结社也使用过那种智能兵器，\x01",
            "好像是高性能的白刃战类型。\x02\x03",

            "#10400F记得是叫『先驱者』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1360")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13F1")

    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F#6P……总之，\x01",
            "现在还是不要接近为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00301F#6P话说回来，瓦吉，\x01",
            "你对『结社』的了解\x01",
            "好像相当详细啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145F")

    label("loc_13F1")


    #C0008
    ChrTalk(
        0x101,
        (
            "#00003F#6P……总之，\x01",
            "现在还是不要接近为好。\x02\x03",

            "#00005F话说回来，瓦吉，\x01",
            "你对『结社』的了解\x01",
            "好像相当详细啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_150A")

    #C0009
    ChrTalk(
        0x105,
        (
            "#10404F#12P呵呵……\x01",
            "还算比较详细吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x107,
        (
            "#01200F#6P#3C在历史长河中，\x01",
            "『骑士团』与『结社』\x01",
            "曾在暗中展开过多次交锋。\x02\x03",

            "因此知己知彼\x01",
            "是最为重要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B7")

    label("loc_150A")


    #C0011
    ChrTalk(
        0x105,
        (
            "#10404F#6P呵呵……\x01",
            "还算比较详细吧。\x02\x03",

            "#10400F在历史长河中，\x01",
            "『骑士团』与『结社』\x01",
            "曾在暗中展开过多次交锋。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00003F#6P原来如此……也就是说，\x01",
            "知己知彼是非常重要的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B7")


    #C0013
    ChrTalk(
        0x105,
        (
            "#10406F#12P不过，『骑士团』和『结社』的\x01",
            "情况都会时常发生变化，\x01",
            "最后也只是没完没了地互相试探而已。\x02\x03",

            "#10402F哦，随便谈论这种事情，\x01",
            "也许会惹阿巴斯发火呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A5")

    #C0014
    ChrTalk(
        0x109,
        "#10106F#6P瓦、瓦吉，你真是的……\x02",
    )

    CloseMessageWindow()

    label("loc_16A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1717")

    #C0015
    ChrTalk(
        0x106,
        (
            "#10709F#6P啊、啊哈哈……\x01",
            "阿巴斯先生好像也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00001F#6P……暂且离开此地吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_175E")

    label("loc_1717")


    #C0017
    ChrTalk(
        0x101,
        (
            "#00006F#6P阿巴斯好像也很辛苦呢。\x02\x03",

            "#00000F……我们暂且离开此地吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_175E")

    Jump("loc_193F")

    label("loc_1763")


    #A0018
    AnonymousTalk(
        0x101,
        "#00003F#6P『噬身之蛇』守在这里吗…………\x02",
    )

    CloseMessageWindow()

    #A0019
    AnonymousTalk(
        0x102,
        (
            "#00103F#6P站在那里的女孩，\x01",
            "好像是『钢之圣女』\x01",
            "的部下之一呢。\x02\x03",

            "#00101F另外，那种白色的智能兵器是……\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0x103,
        (
            "#00208F#6P和结社在利贝尔异变中\x01",
            "所使用的那种类型很相似，\x01",
            "我之前查阅数据库时见到过……\x02",
        )
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0x109,
        (
            "#10101F#6P从其武装来推测，\x01",
            "应该是白刃战类型……\x02",
        )
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0x104,
        (
            "#00303F#6P……虽然未必无法与其抗衡，\x01",
            "但如果大摇大摆地接近，\x01",
            "根本就是自杀行为。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Sleep(500)

    #C0023
    ChrTalk(
        0x101,
        (
            "#00001F#6P……总之，我们现在\x01",
            "还是不要接近为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x106,
        "#10700F#6P是啊，暂且离开这里吧。\x02",
    )

    CloseMessageWindow()

    label("loc_193F")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1959")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1959")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1972")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1972")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_7_1185 end

    def Function_8_1989(): pass

    label("Function_8_1989")

    EventBegin(0x0)
    Call(0, 11)
    Call(0, 10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A17")

    #A0025
    AnonymousTalk(
        0x105,
        (
            "#10401F这里也被『噬身之蛇』控制了吗……\x02\x03",

            "#10403F那个身穿铠甲，守着大门的女孩，\x01",
            "是『钢之圣女』的部下之一呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A88")

    label("loc_1A17")


    #A0026
    AnonymousTalk(
        0x106,
        (
            "#10701F这里也被『噬身之蛇』控制了吗……\x02\x03",

            "#10703F那个身穿铠甲，守着大门的女孩，\x01",
            "是『钢之圣女』的部下之一呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A88")


    #A0027
    AnonymousTalk(
        0x104,
        (
            "#00301F她两边的智能兵器\x01",
            "相当大啊……\x02",
        )
    )

    CloseMessageWindow()

    #A0028
    AnonymousTalk(
        0x103,
        (
            "#00208F和我在数据库中见过的，\x01",
            "利贝尔发生异变时，\x01",
            "结社所使用的那种类型很相似……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B54")

    #A0029
    AnonymousTalk(
        0x105,
        (
            "#10401F是『先驱者』吧？\x01",
            "好像是高性能的白刃战类型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B86")

    label("loc_1B54")


    #A0030
    AnonymousTalk(
        0x109,
        (
            "#10101F从其武装来推测，\x01",
            "应该是白刃战类型……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B86")

    OP_5A()
    Call(0, 12)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BF6")

    #C0031
    ChrTalk(
        0x107,
        (
            "#01200F#6P#3C贸然出手\x01",
            "恐怕并非良策。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#00000F#6P是啊，我们暂且离开这里吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C42")

    label("loc_1BF6")


    #C0033
    ChrTalk(
        0x101,
        (
            "#00003F#6P……看来还是\x01",
            "不要贸然出手为好。\x02\x03",

            "#00000F我们暂且离开这里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C42")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C6C")

    #C0034
    ChrTalk(
        0x106,
        "#10701F#6P嗯，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_1C6C")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C86")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1C86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C9F")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_1C9F")

    SetChrPos(0x0, 6370, -3700, 23670, 19)
    SetScenarioFlags(0x1AF, 4)
    EventEnd(0x5)
    Return()

    # Function_8_1989 end

    def Function_9_1CB6(): pass

    label("Function_9_1CB6")

    EventBegin(0x1)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F『结社』的势力\x01",
            "看守在前方。\x02\x03",

            "#00001F……现在还是\x01",
            "不要贸然接近为好。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 6370, -3700, 23670, 19)
    EventEnd(0x4)
    Return()

    # Function_9_1CB6 end

    def Function_10_1D1D(): pass

    label("Function_10_1D1D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D5F")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1D54():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D54)
    Sleep(50)

    label("loc_1D5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DA1")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1D96():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D96)
    Sleep(50)

    label("loc_1DA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE3")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1DD8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DD8)
    Sleep(50)

    label("loc_1DE3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E2C")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0xA, 500)

    def lambda_1E21():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1E21)
    Sleep(50)

    label("loc_1E2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E75")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0xA, 500)

    def lambda_1E6A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1E6A)
    Sleep(50)

    label("loc_1E75")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EBE")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0xA, 500)

    def lambda_1EB3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1EB3)
    Sleep(50)

    label("loc_1EBE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F07")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0xA, 500)

    def lambda_1EFC():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1EFC)
    Sleep(50)

    label("loc_1F07")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F50")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0xA, 500)

    def lambda_1F45():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1F45)
    Sleep(50)

    label("loc_1F50")

    Sleep(1000)

    #C0036
    ChrTalk(
        0x101,
        "#00005F那是……\x02",
    )

    CloseMessageWindow()
    OP_68(12350, 300, 39810, 4000)
    Sleep(4000)
    Fade(500)
    OP_68(28680, -8700, 77510, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21940, 0)
    OP_68(29090, -8700, 89190, 7000)
    MoveCamera(30, 19, 0, 7000)
    OP_6E(510, 7000)
    SetCameraDistance(17870, 7000)
    Sleep(8000)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2001")
    SetChrPos(0x0, 6840, -3700, 25000, 20)

    label("loc_2001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2021")
    SetChrPos(0x1, 5580, -3700, 24600, 20)

    label("loc_2021")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2041")
    SetChrPos(0x2, 8390, -3700, 25230, 20)

    label("loc_2041")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2061")
    SetChrPos(0x3, 6770, -3700, 22930, 20)

    label("loc_2061")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_208B")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, 8320, -3700, 23330, 20)

    label("loc_208B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20B5")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, 5820, -3700, 23330, 20)

    label("loc_20B5")

    Return()

    # Function_10_1D1D end

    def Function_11_20B6(): pass

    label("Function_11_20B6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20D6")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20EB")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_20EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2100")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2100")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2115")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2115")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_212A")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_212A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_213F")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_213F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2154")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2154")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2169")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2169")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_11_20B6 end

    def Function_12_2174(): pass

    label("Function_12_2174")

    Fade(500)
    OP_68(9400, -4400, 31020, 0)
    MoveCamera(20, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26500, 0)
    OP_0D()
    Return()

    # Function_12_2174 end

    def Function_13_21A9(): pass

    label("Function_13_21A9")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(32640, -8500, 94450, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(14430, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2273")
    SetChrPos(0x101, 34720, -13200, 91570, 0)
    SetChrPos(0x102, 33350, -13200, 91570, 0)
    SetChrPos(0x103, 36070, -13200, 91570, 0)
    SetChrPos(0x104, 34720, -13200, 89800, 0)
    SetChrPos(0x109, 33350, -13200, 90300, 0)
    SetChrPos(0x105, 36070, -13200, 90300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_22D2")

    label("loc_2273")

    SetChrPos(0x101, 33980, -13200, 91570, 0)
    SetChrPos(0x102, 35370, -13200, 91570, 0)
    SetChrPos(0x104, 34720, -13200, 89800, 0)
    SetChrPos(0x109, 33350, -13200, 90300, 0)
    SetChrPos(0x105, 36070, -13200, 90300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_22D2")

    OP_68(32640, -9700, 94450, 3000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23A3")

    def lambda_22F8():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22F8)
    Sleep(50)

    def lambda_2315():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2315)
    Sleep(50)

    def lambda_2332():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2332)
    Sleep(50)

    def lambda_234F():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_234F)
    Sleep(50)

    def lambda_236C():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_236C)
    Sleep(50)

    def lambda_2389():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2389)
    Jump("loc_2431")

    label("loc_23A3")


    def lambda_23A8():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23A8)
    Sleep(50)

    def lambda_23C5():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23C5)
    Sleep(50)

    def lambda_23E2():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23E2)
    Sleep(50)

    def lambda_23FF():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23FF)
    Sleep(50)

    def lambda_241C():
        OP_97(0xFE, 0x0, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_241C)

    label("loc_2431")

    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_6F(0x1)

    #C0037
    ChrTalk(
        0x101,
        "#00000F到达『星见之塔』了啊。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00100F是啊，好久没来过了。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x105,
        (
            "#10305F哦？走近一看，\x01",
            "真是相当高呢。\x02\x03",

            "#10304F似乎很有探索一下的价值。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        (
            "#10100F路障已经撤除了，\x01",
            "我们可以马上开始。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25CB")

    #C0041
    ChrTalk(
        0x104,
        "#00304F嗯，立刻出发吧──\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        (
            "#00203F但在前进途中\x01",
            "也不要太过大意。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306F唔……\x01",
            "你还是老样子啊，阿缇。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，缇欧说的没错。\x02\x03",

            "#00000F好，我们赶快\x01",
            "进去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2621")

    label("loc_25CB")


    #C0045
    ChrTalk(
        0x104,
        "#00304F嗯，立刻出发吧。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00004F说的没错。\x02\x03",

            "#00000F好，我们赶快\x01",
            "进去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2621")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_264A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_2654")

    label("loc_264A")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2654")

    SetChrPos(0x0, 34460, -13200, 96070, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x2)
    SetScenarioFlags(0x153, 1)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_21A9 end

    def Function_14_267A(): pass

    label("Function_14_267A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26CA")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_26CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26E2")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_26E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26FA")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_26FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2712")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_2712")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_272A")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_272A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2742")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_2742")

    LoadChrToIndex("monster/ch80051.itc", 0x24)
    LoadChrToIndex("monster/ch80052.itc", 0x25)
    SoundLoad(3895)
    SoundLoad(3896)
    SoundLoad(3897)
    SoundLoad(3898)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 35000, -13200, 81000, 0)
    SetChrPos(0x102, 35820, -13200, 80140, 0)
    SetChrPos(0x103, 34740, -13200, 79630, 0)
    SetChrPos(0x104, 35070, -13200, 78450, 0)
    SetChrPos(0xF4, 36480, -13200, 79110, 0)
    SetChrPos(0xF5, 33750, -13200, 79310, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x8, 32950, -13200, 100650, 180)
    SetChrPos(0x9, 36950, -13200, 100650, 180)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(30780, 25100, 100030, 0)
    MoveCamera(23, 0, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17090, 0)
    OP_68(32119, -10100, 99250, 10000)
    MoveCamera(33, 5, 0, 10000)
    OP_6E(600, 10000)
    SetCameraDistance(17090, 10000)
    PlaceName2(340, 40, "c_plac28", 0x0, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0xB, 1, 0, 17)
    OP_6F(0x79)
    Fade(500)
    OP_68(35000, -11500, 104000, 0)
    OP_68(35000, -11500, 94000, 6000)
    MoveCamera(40, 25, 0, 0)
    MoveCamera(40, 20, 0, 6000)
    OP_6E(600, 0)
    SetCameraDistance(24500, 0)
    Sleep(1500)

    def lambda_2921():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2921)
    Sleep(50)

    def lambda_2939():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2939)
    Sleep(50)

    def lambda_2951():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2951)
    Sleep(50)

    def lambda_2969():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2969)
    Sleep(50)

    def lambda_2981():
        OP_9B(0x0, 0xF4, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2981)
    Sleep(50)

    def lambda_2999():
        OP_9B(0x0, 0xF5, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_2999)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(34510, -12000, 90890, 0)
    MoveCamera(32, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    Sleep(300)

    #C0047
    ChrTalk(
        0x102,
        "#00108F#12P白色的智能兵器……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3F")

    #C0048
    ChrTalk(
        0x101,
        (
            "#00013F#12P真大啊……\x01",
            "以前从没见过这种类型。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#00208F#12P和我在数据库中见过的，\x01",
            "利贝尔发生异变时，\x01",
            "结社所使用的那种类型很相似……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B04")

    #C0050
    ChrTalk(
        0x105,
        (
            "#10401F#12P是『先驱者』吧？\x01",
            "好像是高性能的白刃战类型。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B3A")

    label("loc_2B04")


    #C0051
    ChrTalk(
        0x109,
        (
            "#10101F#12P从其武装来推测，\x01",
            "应该是白刃战类型……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3A")

    Jump("loc_2C28")

    label("loc_2B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B8C")

    #C0052
    ChrTalk(
        0x105,
        (
            "#10401F#12P似乎是结社操控的\x01",
            "智能兵器『先驱者』呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC4")

    label("loc_2B8C")


    #C0053
    ChrTalk(
        0x109,
        (
            "#10101F#12P接近一看，压迫感和\x01",
            "远观时真是完全不同。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC4")


    #C0054
    ChrTalk(
        0x101,
        (
            "#00013F#12P那是白刃战类型\x01",
            "的智能兵器……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00208F#12P要想进入塔内，\x01",
            "似乎得花费一番工夫了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C28")

    Sleep(300)
    StopBGM(0x1388)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("女性的声音")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3895V#34A#30W先驱者Ｆ３『铁马』……\x02\x03",

            "#3896V#55A#30W是我们『铁机队』所使用的机体，\x01",
            "已经做过了特殊调整。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(1000)
    OP_68(34950, -10750, 104850, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(15500, 20000)
    OP_0D()

    #C0057
    ChrTalk(
        0x101,
        "#00007F#3P#N#15A你是……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E04")

    #C0058
    ChrTalk(
        0x106,
        "#10701F#6P#N#15A『钢之圣女』……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Jump("loc_2E2C")

    label("loc_2E04")


    #C0059
    ChrTalk(
        0x109,
        "#10101F#6P#N#15A『钢之圣女』……！\x02",
    )
    #Auto

    CloseMessageWindow()

    label("loc_2E2C")

    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("阿瑞安赫德的声音")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3897V#43A#30W看来你们顺利突破了\x01",
            "肯帕雷拉的防线呢。\x02\x03",

            "#3898V#55A#30W在这座因缘之塔，\x01",
            "就由我们铁机队来做你们的对手好了。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_68(35000, -12000, 96500, 2000)
    MoveCamera(0, 23, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15500, 2000)
    Sleep(1300)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    OP_82(0x0, 0x64, 0xBB8, 0x3E8)
    Sound(905, 0, 100, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x8, 0x24)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 15)
    BeginChrThread(0x9, 0, 0, 15)

    def lambda_2F7E():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F7E)

    def lambda_2F93():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2F93)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 1)
    OP_6F(0x79)
    Sleep(700)
    Fade(500)
    OP_68(35000, -12000, 92000, 0)
    MoveCamera(45, 15, 0, 0)
    MoveCamera(30, 15, 0, 10000)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x101,
        "#00010F#12P唔……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3064")
    Sound(540, 0, 50, 0)

    label("loc_3064")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("阿瑞安赫德的声音")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W你们就先尝试\x01",
            "突破它们的防守吧。\x02\x03",

            "剩下的话之后再谈。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #C0063
    ChrTalk(
        0x104,
        "#00307F#12P#N哈……求之不得！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0064
    ChrTalk(
        0x101,
        "#00007F#12P全力迎战吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x0)
    Sound(905, 0, 100, 0)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 16)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    OP_0D()
    Sleep(300)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10500, 500)
    Sound(951, 0, 100, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    OP_68(35000, -12000, 87000, 1500)

    def lambda_31C0():
        OP_9B(0x1, 0xFE, 0xFFFB, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31C0)

    def lambda_31D5():
        OP_9B(0x1, 0xFE, 0x5, 0x2710, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_31D5)
    SetChrSubChip(0x8, 0x2)
    SetChrSubChip(0x9, 0x2)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    SetChrSubChip(0x9, 0x3)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Battle("BattleInfo_42C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 18)
    Return()

    # Function_14_267A end

    def Function_15_3221(): pass

    label("Function_15_3221")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_323B")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_15_3221")

    label("loc_323B")

    Return()

    # Function_15_3221 end

    def Function_16_323C(): pass

    label("Function_16_323C")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3254():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3254)
    Sleep(100)
    OP_A1(0xFE, 0x5DC, 0x2, 0x0, 0x1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_16_323C end

    def Function_17_3278(): pass

    label("Function_17_3278")

    Sound(828, 2, 10, 0)
    Sound(132, 2, 40, 0)
    Sleep(100)
    OP_25(0x33C, 0xF)
    Sleep(100)
    OP_25(0x33C, 0x14)
    OP_25(0x84, 0x32)
    Sleep(100)
    OP_25(0x33C, 0x19)
    Sleep(100)
    OP_25(0x33C, 0x1E)
    OP_25(0x84, 0x3C)
    Sleep(100)
    OP_25(0x84, 0x46)
    Sound(1011, 0, 100, 0)
    Sleep(5000)
    StopSound(828, 2000, 20)
    StopSound(132, 2000, 60)
    Return()

    # Function_17_3278 end

    def Function_18_32C5(): pass

    label("Function_18_32C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3304")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_3304")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_331C")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_331C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3334")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_3334")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_334C")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_334C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3364")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_3364")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_337C")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_337C")

    LoadEffect(0x0, "event/ev17029.eff")
    LoadEffect(0x1, "event\\ev14002.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 35000, -13200, 90000, 0)
    SetChrPos(0x102, 35820, -13200, 89140, 0)
    SetChrPos(0x103, 34740, -13200, 88630, 0)
    SetChrPos(0x104, 35070, -13200, 87450, 0)
    SetChrPos(0xF4, 36480, -13200, 88110, 0)
    SetChrPos(0xF5, 33750, -13200, 88310, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 32950, -13200, 95150, 180)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 36950, -13200, 95150, 180)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 1, 0, 20)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_352B():

        label("loc_352B")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_352B")

    QueueWorkItem2(0x8, 3, lambda_352B)

    def lambda_3549():

        label("loc_3549")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_3549")

    QueueWorkItem2(0x9, 3, lambda_3549)
    OP_68(34950, -11700, 95150, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11650, 0)
    FadeToBright(1000, 0)
    MoveCamera(50, 30, 0, 3000)
    SetCameraDistance(13650, 3000)
    OP_6F(0x79)
    OP_0D()
    SetCameraDistance(22000, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0x1388, 0x7D0)

    def lambda_35DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_35DB)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x1, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_3635():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3635)
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    CancelBlur(2500)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    OP_6F(0x79)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Sleep(1800)
    Fade(1000)
    OP_68(34950, -10750, 104850, 0)
    MoveCamera(0, 21, 0, 0)
    MoveCamera(0, 12, 0, 3000)
    OP_6E(600, 0)
    SetCameraDistance(22650, 0)
    SetCameraDistance(16650, 3000)
    OP_6F(0x79)
    OP_0D()
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0xA, 0x1, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 19)
    WaitChrThread(0x101, 3)
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("阿瑞安赫德的声音")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "看来你们确实\x01",
            "有挑战的资格呢。\x02\x03",

            "塔内的各处要地均有\x01",
            "『铁机队』的队员把守。\x02\x03",

            "做好心理准备之后，\x01",
            "就去挑战她们吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(34950, -12250, 91600, 0)
    OP_68(34950, -12250, 89600, 2500)
    MoveCamera(40, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3818")
    Sound(540, 0, 50, 0)

    label("loc_3818")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    #C0066
    ChrTalk(
        0x101,
        (
            "#00008F#11P『铁机队』……\x01",
            "就是那些穿铠甲的女孩吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3999")

    #C0067
    ChrTalk(
        0x105,
        (
            "#10406F#12P据说她们在『结社』\x01",
            "之中也称得上是最强的战斗部队。\x02\x03",

            "#10401F我们最好把她们每一个人都视为\x01",
            "拥有接近执行者实力的对手。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A01")

    label("loc_3999")


    #C0068
    ChrTalk(
        0x106,
        (
            "#10703F#12P……我在地下世界中\x01",
            "也听说过那个部队。\x02\x03",

            "#10701F据说她们每个人都拥有\x01",
            "达人级别的兵器造诣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A01")


    #C0069
    ChrTalk(
        0x104,
        (
            "#00306F#12P……看来那些女孩\x01",
            "相当难对付啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3AB4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AB4)
    Sleep(50)

    def lambda_3AC4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3AC4)
    Sleep(50)

    def lambda_3AD4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3AD4)
    Sleep(50)

    def lambda_3AE4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3AE4)
    Sleep(50)

    def lambda_3AF4():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_3AF4)
    Sleep(50)

    def lambda_3B04():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_3B04)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0xF4, 2)
    WaitChrThread(0xF5, 2)

    #C0070
    ChrTalk(
        0x103,
        "#00205F#6P……艾莉前辈？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00001F#5P有什么心事吗？\x02",
    )

    CloseMessageWindow()
    OP_64(0x102)
    Sleep(500)
    OP_93(0x102, 0xE1, 0x1F4)

    #C0072
    ChrTalk(
        0x102,
        (
            "#00106F#11P啊，嗯……\x01",
            "也不是什么大事啦。\x02\x03",

            "#00101F『钢之圣女』……\x01",
            "她用头盔遮住了脸，\x01",
            "我在想她到底是什么人。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        "#00305F#12P这个……的确很令人在意啊。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x103,
        (
            "#00203F#6P特意将脸遮住，\x01",
            "是不是有什么内情……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CBB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C66")
    OP_FC(0xB)
    Jump("loc_3C7B")

    label("loc_3C66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C7B")
    OP_FC(0x6)

    label("loc_3C7B")


    #C0075
    ChrTalk(
        0x105,
        (
            "#10406F#13P唔……连星杯骑士团\x01",
            "都没能查明她的真面目和来历。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D32")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CE5")
    OP_FC(0xB)
    Jump("loc_3CFA")

    label("loc_3CE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CFA")
    OP_FC(0x6)

    label("loc_3CFA")


    #C0076
    ChrTalk(
        0x106,
        (
            "#10708F#13P……她和我不同，\x01",
            "并没有隐瞒自己的性别。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3DB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D5C")
    OP_FC(0xB)
    Jump("loc_3D71")

    label("loc_3D5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D71")
    OP_FC(0x6)

    label("loc_3D71")


    #C0077
    ChrTalk(
        0x109,
        (
            "#10108F#13P看样子，似乎也不是出于\x01",
            "有犯罪前科之类的单纯理由。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DB3")


    #C0078
    ChrTalk(
        0x101,
        (
            "#00003F#5P……是啊。\x02\x03",

            "#00008F关于这些疑问，或许可以在\x01",
            "与她们对决的时候得到答案。\x02\x03",

            "#00013F正如钢之圣女刚才所说，\x01",
            "我们一定要拿出坚定的决心！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        "#00107F#11P嗯……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E86")
    OP_FC(0xB)
    Jump("loc_3E9B")

    label("loc_3E86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E9B")
    OP_FC(0x6)

    label("loc_3E9B")


    #C0080
    ChrTalk(
        0x109,
        "#10107F#13P是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EFF")

    label("loc_3EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ECF")
    OP_FC(0xB)
    Jump("loc_3EE4")

    label("loc_3ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EE4")
    OP_FC(0x6)

    label("loc_3EE4")


    #C0081
    ChrTalk(
        0x106,
        "#10707F#13P是的……！\x02",
    )

    CloseMessageWindow()

    label("loc_3EFF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一旦完成『星见之塔』的剧情，\x01",
            "在一段时间之内，将无法自由\x01",
            "往来于克洛斯贝尔的各个地区。\x02\x03",

            "届时也无法使用终端等设备，\x01",
            "还请多加注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearMapObjFlags(0xA, 0x2)
    SetMapObjFlags(0xA, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, 34740, -13200, 89500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 6)
    OP_29(0xB0, 0x1, 0x4)
    ModifyEventFlags(0, 1, 0x80)
    OP_24(0x9B)
    EventEnd(0x5)
    Return()

    # Function_18_32C5 end

    def Function_19_4009(): pass

    label("Function_19_4009")

    Sound(116, 0, 100, 0)
    Sound(155, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xBB8)
    ClearMapObjFlags(0x1, 0x10)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x0, 0xF, 0x0, 0x8)
    OP_79(0x1)
    OP_24(0x9B)
    Sound(149, 0, 80, 0)
    OP_74(0x1, 0x1E)
    Return()

    # Function_19_4009 end

    def Function_20_404D(): pass

    label("Function_20_404D")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_20_404D end

    def Function_21_4066(): pass

    label("Function_21_4066")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　未经许可，禁止入内　※\x01",
            "※　 克洛斯贝尔警备队　 ※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_21_4066 end

    SaveToFile()

Try(main)
