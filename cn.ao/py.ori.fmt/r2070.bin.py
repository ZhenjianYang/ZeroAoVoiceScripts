from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r2070.bin",                # FileName
        "r2070",                    # MapName
        "r2070",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2070", "r0000_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 202, 0, 4, 0, 5],
    )

    BuildStringList((
        "r2070",                  # 0
        "合金狮子",               # 1
        "合金狮子",               # 2
        "深渊蠕虫",               # 3
        "深渊蠕虫",               # 4
        "钢铁土龙",               # 5
        "钢铁土龙",               # 6
        "莉丝修女",               # 7
        "SE控制",                 # 8
        "br2070",                 # 9
        "br2070",                 # 10
        "br2070",                 # 11
        "br2070",                 # 12
        "br2080",                 # 13
        "玛因兹山道方向",         # 14
    ))

    ATBonus("ATBonus_640", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_660", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5ED7", 10,  0,   7,   0,   4,   2,   4)
    Sepith("Sepith_5EDF", 0,   4,   2,   9,   6,   4,   2)

    MonsterBattlePostion("MonsterBattlePostion_6A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_704", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_708", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_70C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_710", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_714", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_718", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_680", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_690", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_694", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_698", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_69C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 0, 0, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_740", 0x0000, 64, 6, 60, 6, 1, 25, 0, "br2070", "Sepith_5ED7", 30, 30, 25, 15,
        (
            ("ms76100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
        )
    )

    BattleInfo(
        "BattleInfo_808", 0x0000, 64, 6, 60, 6, 1, 40, 0, "br2070", "Sepith_5EDF", 30, 30, 25, 15,
        (
            ("ms64300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms64300.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms64300.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms64300.dat", "ms66300.dat", "ms66300.dat", "ms66300.dat", 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
        )
    )

    # event battle count: 5

    BattleInfo(
        "BattleInfo_8D0", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "ms76100.dat", "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7453", "ed7453", "ATBonus_640"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_914", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7453", "ed7453", "ATBonus_640"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_958", 0x0042, 255, 6, 45, 3, 3, 30, 0, "br2080", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80300.dat", "ms80300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_720", "MonsterBattlePostion_700", "ed7451", "ed7453", "ATBonus_660"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch14000.itc",                   # 00
        "monster/ch80350.itc",               # 01
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
        "monster/ch76150.itc",               # 10
        "monster/ch76150.itc",               # 11
        "monster/ch64350.itc",               # 12
        "monster/ch64350.itc",               # 13
        "monster/ch76050.itc",               # 14
        "monster/ch76051.itc",               # 15
    ))

    DeclNpc(-91300,  19750,   183369,  225,  453,  0x0, 0,   1,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(-86699,  19750,   178770,  225,  453,  0x0, 0,   1,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(-101089, 6000,    56509,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-131500, 20000,   73660,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-101089, 7000,    56509,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-131500, 21000,   73660,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-133419, 20000,   135100,  55,   385,  0x0, 0,   0,   0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-27230,  5960,    0,       0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-68500,  36190,   10000,   0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-107980, 55130,   6000,    0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-111460, 28450,   2000,    0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-108740, 75420,   20000,   0x1010000,    "BattleInfo_740", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-137070, 87090,   20000,   0x1010000,    "BattleInfo_808", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 24,  -96.0,                 174.0,                 19.0,                  441.0,                 [-0.2357024997472763,  0.05050758272409439,   0.0,                   0.0,                   -0.2357020527124405,   -0.05050767958164215,  0.0,                   0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   18.38471794128418,     13.637063980102539,    -3.8000004291534424,   1.0])
    DeclEvent(0x0000, 0, 28,  -134.30999755859375,   133.35000610351562,    18.5,                  626.0004272460938,     [-0.07552560418844223, -0.10134761780500412,  0.0,                   0.0,                   0.03521830216050148,   -0.21733985841274261,  -0.0,                  0.0,                   0.0,                   0.0,                   0.25,                  0.0,                   -14.840204238891602,   15.37027359008789,     -4.625,                1.0])
    DeclEvent(0x0000, 0, 29,  -128.0,                142.0,                 18.5,                  626.0004272460938,     [-0.05892546847462654, -0.1695702224969864,   0.0,                   0.0,                   0.05892566218972206,   -0.1695697009563446,   -0.0,                  0.0,                   0.0,                   0.0,                   0.2499999850988388,    0.0,                   -15.909903526306152,   2.3739089965820312,    -4.624999523162842,    1.0])
    DeclEvent(0x0000, 0, 17,  -135.17999267578125,   126.5999984741211,     20.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   22.529998779296875,    -42.20000076293945,    -4.0,                  1.0])
    DeclEvent(0x0000, 0, 28,  -135.17999267578125,   126.5999984741211,     20.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   22.529998779296875,    -42.20000076293945,    -4.0,                  1.0])

    DeclActor(-108720, 2000,    22560,   1200,    -108720, 3000,    22560,   0x007C, 0,  6,  0x0000)
    DeclActor(-116200, 2000,    29390,   1200,    -116200, 3000,    29390,   0x007C, 0,  7,  0x0000)
    DeclActor(-77840,  3750,    170050,  1200,    -77840,  4750,    170050,  0x007C, 0,  8,  0x0000)
    DeclActor(-99540,  7750,    191810,  1200,    -99540,  8750,    191810,  0x007C, 0,  9,  0x0000)
    DeclActor(-80750,  19750,   189250,  1200,    -80750,  20750,   189250,  0x007C, 0,  15, 0x0000)
    DeclActor(-62380,  11750,   159630,  1200,    -62380,  12750,   159630,  0x007C, 0,  16, 0x0000)
    DeclActor(-101090, 6000,    56510,   1200,    -101090, 6000,    56510,   0x007C, 0,  10, 0x0000)
    DeclActor(-131500, 20000,   73660,   1200,    -131500, 20000,   73660,   0x007C, 0,  11, 0x0000)
    DeclActor(-95700,  19750,   184720,  1200,    -95700,  21750,   184720,  0x007C, 0,  13, 0x0000)
    DeclActor(-96240,  20000,   185900,  1200,    -96240,  22000,   185900,  0x007C, 0,  13, 0x0000)
    DeclActor(-62380,  -250,    159630,  1200,    -62380,  750,     159630,  0x007C, 0,  16, 0x0000)
    DeclActor(-132250, 20000,   134700,  1200,    -132250, 21500,   134700,  0x007C, 0,  32, 0x0000)

    PlaceName(16.25, 0.0, 5.0, 0x0000, 0x0000, "玛因兹山道方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_A50",          # 00, 0
        "Function_1_A6D",          # 01, 1
        "Function_2_A8C",          # 02, 2
        "Function_3_B44",          # 03, 3
        "Function_4_BF4",          # 04, 4
        "Function_5_CE3",          # 05, 5
        "Function_6_154F",         # 06, 6
        "Function_7_168A",         # 07, 7
        "Function_8_17C5",         # 08, 8
        "Function_9_1900",         # 09, 9
        "Function_10_1A3B",        # 0A, 10
        "Function_11_1D65",        # 0B, 11
        "Function_12_208F",        # 0C, 12
        "Function_13_2093",        # 0D, 13
        "Function_14_23C0",        # 0E, 14
        "Function_15_2454",        # 0F, 15
        "Function_16_2498",        # 10, 16
        "Function_17_24BC",        # 11, 17
        "Function_18_2508",        # 12, 18
        "Function_19_29A8",        # 13, 19
        "Function_20_2C76",        # 14, 20
        "Function_21_2CDD",        # 15, 21
        "Function_22_3051",        # 16, 22
        "Function_23_310F",        # 17, 23
        "Function_24_3144",        # 18, 24
        "Function_25_3E8D",        # 19, 25
        "Function_26_46DC",        # 1A, 26
        "Function_27_4720",        # 1B, 27
        "Function_28_4739",        # 1C, 28
        "Function_29_5863",        # 1D, 29
        "Function_30_5C68",        # 1E, 30
        "Function_31_5DAB",        # 1F, 31
        "Function_32_5E17",        # 20, 32
    ))


    def Function_0_A50(): pass

    label("Function_0_A50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6C")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_0_A50")

    label("loc_A6C")

    Return()

    # Function_0_A50 end

    def Function_1_A6D(): pass

    label("Function_1_A6D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_A6D")

    label("loc_A8B")

    Return()

    # Function_1_A6D end

    def Function_2_A8C(): pass

    label("Function_2_A8C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_ACC"),
        (1, "loc_AD8"),
        (2, "loc_AE4"),
        (3, "loc_AF0"),
        (4, "loc_AFC"),
        (5, "loc_B08"),
        (6, "loc_B14"),
        (SWITCH_DEFAULT, "loc_B20"),
    )


    label("loc_ACC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AD8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AE4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AF0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_AFC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B08")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B20")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B43")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B2C")

    label("loc_B43")

    Return()

    # Function_2_A8C end

    def Function_3_B44(): pass

    label("Function_3_B44")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_B7C"),
        (1, "loc_B88"),
        (2, "loc_B94"),
        (3, "loc_BA0"),
        (4, "loc_BAC"),
        (5, "loc_BB8"),
        (6, "loc_BC4"),
        (SWITCH_DEFAULT, "loc_BD0"),
    )


    label("loc_B7C")

    OP_A0(0xFE, 950, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_B88")

    OP_A0(0xFE, 1050, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_B94")

    OP_A0(0xFE, 1100, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BA0")

    OP_A0(0xFE, 900, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BAC")

    OP_A0(0xFE, 1150, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BB8")

    OP_A0(0xFE, 850, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BC4")

    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BD0")

    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF3")
    OP_A0(0xFE, 1000, 0x0, 0x3)
    Jump("loc_BDC")

    label("loc_BF3")

    Return()

    # Function_3_B44 end

    def Function_4_BF4(): pass

    label("Function_4_BF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0A")
    SetScenarioFlags(0x150, 6)
    Jump("loc_C0D")

    label("loc_C0A")

    SetScenarioFlags(0x150, 7)

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2F")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C67")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8C)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)

    label("loc_C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x37, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7D")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF")
    SetChrPos(0x0, -95100, 19750, 184090, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 14)

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_CE2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE2")
    SetChrPos(0x0, -96240, 20000, 185900, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_CE2")

    Return()

    # Function_4_BF4 end

    def Function_5_CE3(): pass

    label("Function_5_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_D5A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D23")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D55")

    label("loc_D23")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D55")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D55")

    Jump("loc_D71")

    label("loc_D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D71")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D71")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11D3")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_11D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_122A")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x12C, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    Jump("loc_125A")

    label("loc_122A")

    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)

    label("loc_125A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -81250, 19750, 189000, 6000, 3000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1290")
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_1298")

    label("loc_1290")

    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_1298")

    SetBarrier(0x0, 0x1, 0x1, 0x0, -62550, 11750, 159550, 5000, 3000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CE")
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    Jump("loc_12D6")

    label("loc_12CE")

    SetBarrier(0x2, 0x1, 0x1)
    OP_65(0x5, 0x1)

    label("loc_12D6")

    SetBarrier(0x0, 0x2, 0x1, 0x0, -62550, -250, 159550, 6000, 3000, 45000)
    ClearMapObjFlags(0x5, 0x10)
    MiniGame(0x2F, 0x8, 0x9, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132E")
    OP_70(0x7, 0x0)
    Jump("loc_1332")

    label("loc_132E")

    OP_70(0x7, 0x1E)

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1345")
    OP_70(0x8, 0x0)
    Jump("loc_1349")

    label("loc_1345")

    OP_70(0x8, 0x1E)

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135C")
    OP_70(0x9, 0x0)
    Jump("loc_1360")

    label("loc_135C")

    OP_70(0x9, 0x1E)

    label("loc_1360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1373")
    OP_70(0xA, 0x0)
    Jump("loc_1377")

    label("loc_1373")

    OP_70(0xA, 0x1E)

    label("loc_1377")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13D8")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -101090, 6000, 56510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_13D8")

    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1424")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -131500, 20000, 73660, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x7, 0x1)

    label("loc_1424")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1447")
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x2)
    OP_65(0xB, 0x1)
    Jump("loc_1453")

    label("loc_1447")

    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x2)

    label("loc_1453")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1471")
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFlags(0xF, 0x4)

    label("loc_1471")

    SetMapObjFlags(0x1B, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_148B")
    ClearMapObjFlags(0x1B, 0x4)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AF")
    ClearMapObjFlags(0x1B, 0x4)

    label("loc_14AF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_14C7")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DF")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_14DF")

    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_152D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150E")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_150E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_152D")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_152D")

    OP_1C(0x0, 0x18, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x19, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0x1A, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_CE3 end

    def Function_6_154F(): pass

    label("Function_6_154F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1641")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_15D2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_163C")

    label("loc_15D2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_163C")

    Jump("loc_167E")

    label("loc_1641")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_167E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_154F end

    def Function_7_168A(): pass

    label("Function_7_168A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177C")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x16, 1)"), scpexpr(EXPR_END)), "loc_170D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x16),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1777")

    label("loc_170D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x16),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x16),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1777")

    Jump("loc_17B9")

    label("loc_177C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_17B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_168A end

    def Function_8_17C5(): pass

    label("Function_8_17C5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18B7")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x442, 1)"), scpexpr(EXPR_END)), "loc_1848")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x442),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_18B2")

    label("loc_1848")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x442),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x442),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18B2")

    Jump("loc_18F4")

    label("loc_18B7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_18F4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_17C5 end

    def Function_9_1900(): pass

    label("Function_9_1900")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F2")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x456, 1)"), scpexpr(EXPR_END)), "loc_1983")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x456),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_19ED")

    label("loc_1983")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x456),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x456),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_19ED")

    Jump("loc_1A2F")

    label("loc_19F2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1A2F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1900 end

    def Function_10_1A3B(): pass

    label("Function_10_1A3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BD9")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1BBA")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB5")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1BB2")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1ADD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1ADD)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1B94")
    Call(1, 5)
    Jump("loc_1BAD")

    label("loc_1B94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BAA")
    Call(1, 4)
    Jump("loc_1BAD")

    label("loc_1BAA")

    Call(1, 3)

    label("loc_1BAD")

    Jump("loc_1BB5")

    label("loc_1BB2")

    Call(1, 1)

    label("loc_1BB5")

    Jump("loc_1BD0")

    label("loc_1BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1BD0")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1BD0")

    TalkEnd(0xFF)
    Return()

    label("loc_1BD9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1D4A")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D45")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1D42")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1C6D)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D24")
    Call(1, 5)
    Jump("loc_1D3D")

    label("loc_1D24")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D3A")
    Call(1, 4)
    Jump("loc_1D3D")

    label("loc_1D3A")

    Call(1, 3)

    label("loc_1D3D")

    Jump("loc_1D45")

    label("loc_1D42")

    Call(1, 1)

    label("loc_1D45")

    Jump("loc_1D60")

    label("loc_1D4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1D60")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1D60")

    TalkEnd(0xFF)
    Return()

    # Function_10_1A3B end

    def Function_11_1D65(): pass

    label("Function_11_1D65")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F03")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_END)), "loc_1EE4")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDF")
    ClearScenarioFlags(0x3B, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_1EDC")
    ClearScenarioFlags(0x39, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1E07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E07)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED7")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EBE")
    Call(1, 5)
    Jump("loc_1ED7")

    label("loc_1EBE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1ED4")
    Call(1, 4)
    Jump("loc_1ED7")

    label("loc_1ED4")

    Call(1, 3)

    label("loc_1ED7")

    Jump("loc_1EDF")

    label("loc_1EDC")

    Call(1, 1)

    label("loc_1EDF")

    Jump("loc_1EFA")

    label("loc_1EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_1EFA")
    ClearScenarioFlags(0x39, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1EFA")

    TalkEnd(0xFF)
    Return()

    label("loc_1F03")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_END)), "loc_2074")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206F")
    ClearScenarioFlags(0x3B, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_206C")
    ClearScenarioFlags(0x39, 6)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1F97)
    TurnDirection(0xD, 0x0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    PlayEffect(0x7, 0x1, 0xD, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2067")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_204E")
    Call(1, 5)
    Jump("loc_2067")

    label("loc_204E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2064")
    Call(1, 4)
    Jump("loc_2067")

    label("loc_2064")

    Call(1, 3)

    label("loc_2067")

    Jump("loc_206F")

    label("loc_206C")

    Call(1, 1)

    label("loc_206F")

    Jump("loc_208A")

    label("loc_2074")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_208A")
    ClearScenarioFlags(0x39, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_208A")

    TalkEnd(0xFF)
    Return()

    # Function_11_1D65 end

    def Function_12_208F(): pass

    label("Function_12_208F")

    Call(1, 6)
    Return()

    # Function_12_208F end

    def Function_13_2093(): pass

    label("Function_13_2093")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20C5")
    SetScenarioFlags(0x31, 2)

    label("loc_20C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_210B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2105")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20FA")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2100")

    label("loc_20FA")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2100")

    Jump("loc_210B")

    label("loc_2105")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_210B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_217C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_215C"),
        (SWITCH_DEFAULT, "loc_216D"),
    )


    label("loc_215C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2177")

    label("loc_216D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2177")

    Jump("loc_23AD")

    label("loc_217C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_21AC")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_21AC")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21D6"),
        (1, "loc_22DA"),
        (2, "loc_236B"),
        (SWITCH_DEFAULT, "loc_23A3"),
    )


    label("loc_21D6")

    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    OP_74(0xD, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2207")
    OP_70(0xD, 0x12C)
    OP_71(0xD, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2217")

    label("loc_2207")

    OP_70(0xD, 0xF0)
    OP_71(0xD, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2217")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_226D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_226D")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2290")
    Sound(461, 0, 100, 0)

    label("loc_2290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22B0")
    OP_70(0xD, 0x14A)
    OP_71(0xD, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_22C0")

    label("loc_22B0")

    OP_70(0xD, 0x10E)
    OP_71(0xD, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_22C0")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xD, "light", 0x1, 0x1)
    OP_70(0xD, 0x0)
    Jump("loc_210B")

    label("loc_22DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_234C")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_230F")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2327")

    label("loc_230F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2322")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2327")

    label("loc_2322")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2327")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2366")

    label("loc_234C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_235C")
    OP_AF(0xFB)
    Jump("loc_2366")

    label("loc_235C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2366")

    Jump("loc_23AD")

    label("loc_236B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2384")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_239E")

    label("loc_2384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2394")
    OP_AF(0xFB)
    Jump("loc_239E")

    label("loc_2394")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_239E")

    Jump("loc_23AD")

    label("loc_23A3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23AD")

    Jump("loc_210B")

    label("loc_23B2")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2093 end

    def Function_14_23C0(): pass

    label("Function_14_23C0")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_241B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2410")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_2416")

    label("loc_2410")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_2416")

    Jump("loc_243F")

    label("loc_241B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2439")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_243F")

    label("loc_2439")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_243F")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_23C0 end

    def Function_15_2454(): pass

    label("Function_15_2454")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2474")
    Call(0, 31)
    Return()

    label("loc_2474")

    TalkBegin(0xFF)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧紧关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_15_2454 end

    def Function_16_2498(): pass

    label("Function_16_2498")

    TalkBegin(0xFF)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧紧关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_2498 end

    def Function_17_24BC(): pass

    label("Function_17_24BC")

    OP_E2(0x3)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_24DB")
    Call(0, 20)
    Jump("loc_24EF")

    label("loc_24DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_24EC")
    Call(0, 19)
    Jump("loc_24EF")

    label("loc_24EC")

    Call(0, 18)

    label("loc_24EF")

    OP_E2(0x2)
    ClearMapObjFlags(0x17, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    Return()

    # Function_17_24BC end

    def Function_18_2508(): pass

    label("Function_18_2508")

    EventBegin(0x0)
    Call(0, 22)
    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_295E")

    #A0023
    AnonymousTalk(
        0x105,
        (
            "#10403F『噬身之蛇』……\x01",
            "他们似乎看守在这里呢。\x02\x03",

            "#10401F守卫在门前的\x01",
            "是结社用于据点防卫的\x01",
            "重型智能兵器『合金狮子』。\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0x103,
        (
            "#00203F好像具有相当强\x01",
            "的武装火力……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2603")

    #A0025
    AnonymousTalk(
        0x109,
        (
            "#10101F嗯，恐怕是防卫据点\x01",
            "专用的重火力型。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2603")


    #A0026
    AnonymousTalk(
        0x104,
        (
            "#00301F如果大摇大摆地接近，\x01",
            "根本就是自杀行为。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 23)
    Sleep(500)

    #C0027
    ChrTalk(
        0x101,
        (
            "#00003F#6P……总之，我们现在\x01",
            "还是暂时撤退为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#6P话说回来，瓦吉，\x01",
            "你对『结社』的了解\x01",
            "好像相当详细啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2762")

    #C0029
    ChrTalk(
        0x105,
        (
            "#10404F#12P呵呵……\x01",
            "还算比较详细吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
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
    Jump("loc_2810")

    label("loc_2762")


    #C0031
    ChrTalk(
        0x105,
        (
            "#10404F#12P呵呵……\x01",
            "还算比较详细吧。\x02\x03",

            "#10400F在历史长河中，\x01",
            "『骑士团』与『结社』\x01",
            "曾在暗中展开过多次交锋。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00003F#6P原来如此……也就是说，\x01",
            "知己知彼是非常重要的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2810")


    #C0033
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28FE")

    #C0034
    ChrTalk(
        0x109,
        "#10106F#6P瓦、瓦吉，你真是的……\x02",
    )

    CloseMessageWindow()

    label("loc_28FE")


    #C0035
    ChrTalk(
        0x106,
        (
            "#10709F#6P啊、啊哈哈……\x01",
            "阿巴斯先生好像也很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00001F#6P……暂且离开此地吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_295E")

    label("loc_295E")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2978")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2978")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2991")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2991")

    SetChrPos(0x0, -135390, 20000, 123030, 180)
    SetScenarioFlags(0x1AF, 5)
    EventEnd(0x5)
    Return()

    # Function_18_2508 end

    def Function_19_29A8(): pass

    label("Function_19_29A8")

    EventBegin(0x0)
    Call(0, 22)
    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A61")

    #A0037
    AnonymousTalk(
        0x105,
        (
            "#10403F这里也被『噬身之蛇』控制了吗……\x02\x03",

            "#10401F守卫在门前的\x01",
            "是结社用于据点防卫的\x01",
            "重型智能兵器『合金狮子』。\x02",
        )
    )

    CloseMessageWindow()

    #A0038
    AnonymousTalk(
        0x103,
        (
            "#00203F好像具有相当强\x01",
            "的武装火力……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACD")

    label("loc_2A61")


    #A0039
    AnonymousTalk(
        0x106,
        "#10701F这里也被『噬身之蛇』控制了吗……\x02",
    )

    CloseMessageWindow()

    #A0040
    AnonymousTalk(
        0x103,
        (
            "#00203F守卫在门前的智能兵器\x01",
            "好像具有相当强\x01",
            "的武装火力……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B0D")

    #A0041
    AnonymousTalk(
        0x109,
        (
            "#10101F嗯，恐怕是防卫据点\x01",
            "专用的重火力型。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0D")


    #A0042
    AnonymousTalk(
        0x104,
        (
            "#00301F#6P如果大摇大摆地接近，\x01",
            "根本就是自杀行为。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 23)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BB9")

    #C0043
    ChrTalk(
        0x101,
        (
            "#00003F#6P……总之，我们现在\x01",
            "还是暂时撤退为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x106,
        "#10701F#6P是的，还是先离开吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_2BB9")


    #C0045
    ChrTalk(
        0x101,
        (
            "#00003F#6P……我们还是不要\x01",
            "贸然接近为好。\x02\x03",

            "#00001F先离开这里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C2C")

    #C0046
    ChrTalk(
        0x107,
        "#01200F#6P#3C嗯，走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2C2C")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C46")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2C46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2C5F")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2C5F")

    SetChrPos(0x0, -135390, 20000, 123030, 180)
    SetScenarioFlags(0x1AF, 5)
    EventEnd(0x5)
    Return()

    # Function_19_29A8 end

    def Function_20_2C76(): pass

    label("Function_20_2C76")

    EventBegin(0x1)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00001F『结社』的智能兵器\x01",
            "守卫在前方。\x02\x03",

            "#00003F……我们还是\x01",
            "暂时撤退为好。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -135390, 20000, 123030, 180)
    EventEnd(0x4)
    Return()

    # Function_20_2C76 end

    def Function_21_2CDD(): pass

    label("Function_21_2CDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1F")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2D14():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D14)
    Sleep(50)

    label("loc_2D1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D61")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2D56():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D56)
    Sleep(50)

    label("loc_2D61")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DA3")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2D98():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D98)
    Sleep(50)

    label("loc_2DA3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DEC")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0x8, 500)

    def lambda_2DE1():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2DE1)
    Sleep(50)

    label("loc_2DEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E35")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0x8, 500)

    def lambda_2E2A():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E2A)
    Sleep(50)

    label("loc_2E35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E7E")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0x8, 500)

    def lambda_2E73():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2E73)
    Sleep(50)

    label("loc_2E7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EC7")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0x8, 500)

    def lambda_2EBC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2EBC)
    Sleep(50)

    label("loc_2EC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F10")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0x8, 500)

    def lambda_2F05():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2F05)
    Sleep(50)

    label("loc_2F10")

    Sleep(1000)

    #C0048
    ChrTalk(
        0x101,
        "#00005F那是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-115530, 21850, 135930, 0)
    MoveCamera(358, 22, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(25000, 0)
    OP_68(-88910, 21850, 177310, 7000)
    MoveCamera(6, 14, 0, 7000)
    Sleep(8000)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F9C")
    SetChrPos(0x0, -133380, 20000, 124530, 39)

    label("loc_2F9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FBC")
    SetChrPos(0x1, -134310, 20000, 125180, 39)

    label("loc_2FBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FDC")
    SetChrPos(0x2, -132840, 20000, 123600, 39)

    label("loc_2FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2FFC")
    SetChrPos(0x3, -132290, 20000, 122620, 39)

    label("loc_2FFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3026")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, -134600, 20000, 123840, 39)

    label("loc_3026")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3050")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, -134300, 20000, 122570, 39)

    label("loc_3050")

    Return()

    # Function_21_2CDD end

    def Function_22_3051(): pass

    label("Function_22_3051")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3071")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3071")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3086")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3086")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_309B")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_309B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B0")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30C5")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30DA")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30EF")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3104")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3104")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_22_3051 end

    def Function_23_310F(): pass

    label("Function_23_310F")

    Fade(500)
    OP_68(-134300, 21620, 122570, 0)
    MoveCamera(39, 6, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17870, 0)
    OP_0D()
    Return()

    # Function_23_310F end

    def Function_24_3144(): pass

    label("Function_24_3144")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00056.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00156.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00256.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00356.itc", 0x25)
    SoundLoad(959)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31B7")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("loc_31B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D5")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("loc_31D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31F3")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("loc_31F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3211")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_3211")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_322F")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("loc_322F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_324D")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("loc_324D")

    LoadEffect(0x0, "event\\ev10002.eff")
    SoundLoad(3720)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -91820, 19750, 178310, 45)
    SetChrPos(0x102, -92990, 19750, 178120, 45)
    SetChrPos(0x103, -92650, 19750, 176650, 45)
    SetChrPos(0x104, -91640, 19750, 176190, 45)
    SetChrPos(0xF4, -94120, 19750, 177940, 45)
    SetChrPos(0xF5, -93700, 19750, 176110, 45)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -88300, 19750, 186370, 235)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -83700, 19750, 181770, 235)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-82750, 22750, 187250, 0)
    OP_68(-87750, 22550, 182250, 6000)
    MoveCamera(9, 21, 0, 0)
    MoveCamera(9, 15, 0, 6000)
    OP_6E(700, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(24000, 6000)
    FadeToBright(1000, 0)
    Sleep(2500)

    def lambda_33E0():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33E0)
    Sleep(50)

    def lambda_33F8():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_33F8)
    Sleep(50)

    def lambda_3410():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3410)
    Sleep(50)

    def lambda_3428():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3428)
    Sleep(50)

    def lambda_3440():
        OP_9B(0x0, 0xF4, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3440)
    Sleep(50)

    def lambda_3458():
        OP_9B(0x0, 0xF5, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_3458)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-87750, 21000, 182250, 0)
    MoveCamera(9, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14650, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34F4")

    #C0049
    ChrTalk(
        0x105,
        "#10401F#6P『噬身之蛇』的徽章啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_351A")

    label("loc_34F4")


    #C0050
    ChrTalk(
        0x106,
        "#10701F#6P『噬身之蛇』的徽章……\x02",
    )

    CloseMessageWindow()

    label("loc_351A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_358D")

    #C0051
    ChrTalk(
        0x103,
        (
            "#00201F#6P入口似乎被\x01",
            "某种力量封锁了……\x02\x03",

            "#00203F说起来，之前守卫在这里的\x01",
            "智能兵器去哪里了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35BA")

    label("loc_358D")


    #C0052
    ChrTalk(
        0x103,
        (
            "#00201F#6P入口似乎被\x01",
            "某种力量封锁了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35BA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_360A")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x109,
        "#10107F#6P各位，那是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_363F")

    label("loc_360A")

    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x106,
        "#10707F#6P那是……！\x02",
    )

    CloseMessageWindow()

    label("loc_363F")

    OP_68(-87750, 30600, 182250, 4000)
    MoveCamera(45, -10, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(9350, 4000)
    Sleep(2000)
    Sound(944, 0, 100, 0)
    OP_6F(0x79)

    #C0055
    ChrTalk(
        0x102,
        "#00101F那口大钟……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#00301F总之，只要能把大钟的\x01",
            "共鸣停止就行了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("少年的声音")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3720V#30W#28A呵呵，正是如此。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0058
    ChrTalk(
        0x101,
        "#00013F！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-80750, 22750, 189250, 0)
    MoveCamera(45, 39, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(19000, 10000)
    OP_0D()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("少年的声音")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "哎呀呀，你们会来到这里，\x01",
            "想必是得到了约鲁古大师的助言呢。\x02\x03",

            "极限级智能兵器最终型的事情，\x01",
            "还有袭击彩虹剧团的事情，\x01",
            "似乎把大师惹火了吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-87750, 21000, 182250, 0)
    MoveCamera(18, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14650, 0)
    OP_0D()

    #C0060
    ChrTalk(
        0x104,
        "#00304F#6P嗯，他非常生气。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#00211F#6P所以，你们也算是自食恶果吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("少年的声音")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "唔……我好像是被博士\x01",
            "和那些猎兵连累了呢……\x02\x03",

            "呵呵，不过算啦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x64, 0xC8, 0xBB8, 0x2EE)
    SetCameraDistance(15650, 500)
    Sound(959, 2, 100, 0)
    Sound(817, 0, 100, 0)
    Sound(202, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 0, 100, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    OP_0D()
    CancelBlur(500)
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
    Fade(350)
    OP_68(-88250, 21000, 181750, 500)
    SetChrChipByIndex(0xF5, 0x29)
    SetChrSubChip(0xF5, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_3A94():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3A94)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x27)
    SetChrSubChip(0xF4, 0x0)

    def lambda_3ABC():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_3ABC)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)

    def lambda_3AE4():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AE4)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_3B0C():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B0C)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x2)

    def lambda_3B34():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B34)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)

    def lambda_3B5C():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B5C)
    Sleep(50)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B91")
    Sound(540, 0, 50, 0)

    label("loc_3B91")

    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    WaitChrThread(0xF4, 1)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    WaitChrThread(0x103, 1)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_6F(0x79)
    OP_0D()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x64, 0xC8, 0xBB8, 0x2EE)
    StopSound(959, 1000, 100)
    Sound(902, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)

    def lambda_3C18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3C18)

    def lambda_3C29():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3C29)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    CancelBlur(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("少年的声音")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "既然你们来到此地，\x01",
            "自然已有相应的觉悟了吧？\x02\x03",

            "呵呵，要让我玩得开心一点哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_3CFB")

    #C0064
    ChrTalk(
        0x101,
        (
            "#00007F#6P唔……\x01",
            "是之前见到过的那种东西！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC5")

    label("loc_3CFB")


    #C0065
    ChrTalk(
        0x101,
        "#00007F#6P唔……智能兵器吗！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D82")

    #C0066
    ChrTalk(
        0x105,
        (
            "#10410F#6P『合金狮子』！\x02\x03",

            "#10407F是结社用于防卫据点的\x01",
            "重型智能兵器……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DC5")

    label("loc_3D82")


    #C0067
    ChrTalk(
        0x109,
        (
            "#10107F#6P发现武装兵器！\x02\x03",

            "恐怕是用于防卫据点\x01",
            "的重火力型……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DC5")


    #C0068
    ChrTalk(
        0x104,
        "#00307F#6P赶快干掉它们！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E0C")

    #C0069
    ChrTalk(
        0x106,
        "#10707F#6P是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E22")

    label("loc_3E0C")


    #C0070
    ChrTalk(
        0x109,
        "#10107F#6P明白！\x02",
    )

    CloseMessageWindow()

    label("loc_3E22")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10650, 500)

    def lambda_3E3C():
        OP_9B(0x1, 0xFE, 0xFFE2, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E3C)

    def lambda_3E51():
        OP_9B(0x1, 0xFE, 0x1E, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E51)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    OP_24(0x3BF)
    Battle("BattleInfo_958", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 25)
    Return()

    # Function_24_3144 end

    def Function_25_3E8D(): pass

    label("Function_25_3E8D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3ECE")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_3ECE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EE6")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_3EE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EFE")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_3EFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F16")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_3F16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2E")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_3F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F46")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_3F46")

    LoadEffect(0x0, "event/ev17029.eff")
    LoadEffect(0x1, "event\\ev14002.eff")
    SoundLoad(3721)
    SoundLoad(3722)
    SoundLoad(3723)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -89280, 19750, 180850, 45)
    SetChrPos(0x102, -90450, 19750, 180660, 45)
    SetChrPos(0x103, -90110, 19750, 179190, 45)
    SetChrPos(0x104, -89100, 19750, 178730, 45)
    SetChrPos(0xF4, -91580, 19750, 180480, 45)
    SetChrPos(0xF5, -91160, 19750, 178650, 45)
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
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -88300, 19750, 186370, 235)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -83700, 19750, 181770, 235)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    BeginChrThread(0xF, 1, 0, 27)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_40E8():

        label("loc_40E8")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_40E8")

    QueueWorkItem2(0x8, 3, lambda_40E8)

    def lambda_4106():

        label("loc_4106")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_4106")

    QueueWorkItem2(0x9, 3, lambda_4106)
    OP_68(-86250, 21000, 183750, 0)
    MoveCamera(6, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_68(-86250, 21000, 183750, 3000)
    MoveCamera(0, 30, 0, 3000)
    SetCameraDistance(14000, 3000)
    OP_6F(0x79)
    OP_0D()
    SetCameraDistance(22000, 500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0x1388, 0x7D0)

    def lambda_41A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_41A9)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_4203():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4203)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x1, 0x2)
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
    OP_68(-81300, 23000, 188600, 0)
    MoveCamera(45, 18, 0, 0)
    MoveCamera(45, 15, 0, 3000)
    OP_6E(700, 0)
    SetCameraDistance(19650, 0)
    SetCameraDistance(17650, 3000)
    OP_6F(0x79)
    OP_0D()
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    OP_75(0xF, 0x1, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 26)
    Sleep(400)
    OP_68(-89300, 22000, 180600, 3000)
    MoveCamera(45, 8, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(13550, 3000)
    Sleep(2000)
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
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("少年的声音")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3721V#30W#25A呵呵，干得漂亮。\x02\x03",

            "#3722V#30W#40A那就不必客气了，\x01",
            "尽管进来吧。\x02\x03",

            "#3723V#30W#27A我在大钟前等着你们哦⊥\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    #C0072
    ChrTalk(
        0x102,
        "#00108F#5P……你们觉得前面会有什么？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#00006F#5P对方显然设置了\x01",
            "一些机关……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4569")

    #C0074
    ChrTalk(
        0x105,
        (
            "#10403F#5P而且很可能是\x01",
            "相当低级趣味的机关呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A0")

    label("loc_4569")


    #C0075
    ChrTalk(
        0x106,
        (
            "#10703F#5P嗯，而且很可能是\x01",
            "相当低级趣味的机关呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45E8")

    #C0076
    ChrTalk(
        0x109,
        (
            "#10101F#5P但即使如此，\x01",
            "我们也只能硬闯了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4615")

    label("loc_45E8")


    #C0077
    ChrTalk(
        0x106,
        (
            "#10701F#5P即使如此，\x01",
            "我们也只能硬闯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4615")


    #C0078
    ChrTalk(
        0x104,
        (
            "#00307F#11P嗯！\x01",
            "拿出干劲来！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0xF, 0x2)
    SetMapObjFlags(0xF, 0x4)
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
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_37()
    SetChrPos(0x0, -89300, 19750, 180600, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 3)
    OP_29(0xB0, 0x1, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ClearScenarioFlags(0x150, 7)
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    OP_66(0x5, 0x1)
    OP_24(0x9B)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_25_3E8D end

    def Function_26_46DC(): pass

    label("Function_26_46DC")

    Sound(116, 0, 100, 0)
    Sound(155, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xBB8)
    ClearMapObjFlags(0x1, 0x10)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)
    OP_24(0x9B)
    Sound(149, 0, 80, 0)
    OP_74(0x1, 0x1E)
    Return()

    # Function_26_46DC end

    def Function_27_4720(): pass

    label("Function_27_4720")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_27_4720 end

    def Function_28_4739(): pass

    label("Function_28_4739")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4749")
    Call(0, 30)
    Return()

    label("loc_4749")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_E2(0x3)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04400.itp")
    SetChrPos(0x101, -136050, 20000, 132320, 45)
    SetChrPos(0x102, -137070, 20000, 133060, 45)
    SetChrPos(0x103, -135790, 20000, 131260, 45)
    SetChrPos(0x104, -137600, 20000, 131410, 45)
    SetChrPos(0x109, -138640, 20000, 131920, 45)
    SetChrPos(0x105, -137150, 20000, 130120, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    OP_68(-62530, 30850, 175200, 0)
    MoveCamera(31, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(81900, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-83430, 30850, 189890, 10000)
    PlaceName2(340, 40, "c_plac29", 0x0, 6000)
    OP_6F(0x1)
    OP_68(-126570, 23100, 136030, 5000)
    MoveCamera(28, -1, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(24080, 5000)
    OP_6F(0x79)

    #N0079
    NpcTalk(
        0xE,
        "穿修女服的女性",
        (
            "#04400F『那名罪人\x01",
            "  将钟敲响。』\x02\x03",

            "『响彻世界的不祥之音\x01",
            "  宣告着混沌时代的开始……』\x02\x03",

            "#04403F──选自《拉达记》序节，\x01",
            "『觉醒之音』……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 140, -1, -1)

    #A0080
    AnonymousTalk(
        0x101,
        "#00005F（哎，那个人是……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #A0081
    AnonymousTalk(
        0x102,
        "#00105F……莉、莉丝小姐！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(-136960, 22000, 130690, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15660, 0)
    OP_0D()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xE, 0xE1, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0082
    AnonymousTalk(
        0xE,
        (
            "你们是……\x01",
            "特别任务支援科的……\x02",
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

    #C0083
    ChrTalk(
        0x105,
        "#12P#10302F呵呵，好久不见了啊。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#12P#00205F这位是……？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#6P#00000F哦……\x01",
            "是我们在不久之前\x01",
            "刚刚认识的教会修女。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xE,
        (
            "#11P#04404F我是莉丝·亚尔珍特，\x01",
            "请多多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#6P#00300F话说回来，教会的修女\x01",
            "在这种地方做什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x109,
        (
            "#6P#10105F是、是啊！\x02\x03",

            "#10106F这里已经被警备队\x01",
            "封锁了……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xE,
        (
            "#11P#04403F哦，我今天是来\x01",
            "矿山镇外出授课的……\x02\x03",

            "#04401F刚才突然听到\x01",
            "有声音从这边传出。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#6P#00005F声音……？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(827, 0, 60, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x104,
        "#6P#00301F喂，罗伊德，这是……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯……\x01",
            "好像是『钟』在鸣响。\x02\x03",

            "#00001F缇欧，能从里面感应到那种气息吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#12P#00203F……虽然很微弱……\x02\x03",

            "#00201F但当时那种『上级三属性』\x01",
            "的气息似乎已经恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#6P#00105F怎、怎么会……\x02\x03",

            "#00101F也就是说，有人再次\x01",
            "敲响了那口钟吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#12P#10303F唔……\x02\x03",

            "#10302F看来这里就是当初那起\x01",
            "『幽灵骚乱』事件的现场吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        (
            "#11P#04405F幽灵……？\x02\x03",

            "#04400F那个……如果可以，\x01",
            "能否将详情告诉我？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#6P#00006F嗯，其实是这样的……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将以前来此地探索\x01",
            "的事情做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0099
    ChrTalk(
        0xE,
        (
            "#11P#04403F……原来如此，\x01",
            "是这样啊。\x02\x03",

            "#04408F上级三属性产生影响\x01",
            "的奇异遗迹……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0100
    ChrTalk(
        0x102,
        "#6P#00105F……莉丝小姐？\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xE,
        (
            "#11P#04403F……没什么。\x02\x03",

            "#04400F既然如此，\x01",
            "看来有必要尽快\x01",
            "让那口钟停止鸣响啊。\x02\x03",

            "#04403F那么，我们以后有机会再见了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FCD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4FCD)
    OP_68(-134870, 22200, 129860, 3500)
    MoveCamera(6, 13, 0, 3500)
    OP_6E(510, 3500)
    SetCameraDistance(14600, 3500)
    OP_6F(0x79)

    #C0102
    ChrTalk(
        0x101,
        "#6P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xE,
        "#5P#04403F……嘿。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrPos(0xE, -131490, 20000, 137100, 55)
    OP_0D()
    Sound(30, 0, 100, 0)

    def lambda_505B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_505B)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0104
    ChrTalk(
        0x109,
        (
            "#6P#10111F等、等一下，莉丝小姐！？\x01",
            "你到底想……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0xE1, 0x1F4)

    #C0105
    ChrTalk(
        0xE,
        (
            "#11P#04400F没什么，只是去把\x01",
            "那口钟停住而已。\x02\x03",

            "#04403F……安抚无法升天的灵魂\x01",
            "也是神职人员的职责。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#00306F话虽如此，可是……\x02\x03",

            "#00301F……喂，罗伊德，\x01",
            "这里还是由我们\x01",
            "来接手为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        (
            "#12P#00203F是啊。\x02\x03",

            "#00200F既然上级三属性已经开始运转，\x01",
            "遗迹内很可能徘徊着\x01",
            "那种魔物……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，确实如此……\x01",
            "如果让民间人士入内探索，未免太过危险了。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#6P#00105F哎，那、那个，可是她……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_64(0xE)

    def lambda_538F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_538F)
    Sleep(50)

    def lambda_539F():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_539F)
    Sleep(50)

    def lambda_53AF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_53AF)
    Sleep(50)

    def lambda_53BF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_53BF)
    Sleep(50)

    def lambda_53CF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_53CF)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        "#11P#00005F……怎么了？艾莉。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0111
    ChrTalk(
        0x102,
        (
            "#6P#00103F……没、没什么，\x01",
            "你说的对，确实很危险呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 500)
    Sleep(300)

    #C0112
    ChrTalk(
        0x102,
        (
            "#6P#00100F莉丝小姐，这里的事情\x01",
            "就交给我们来处理吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5488():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5488)
    Sleep(50)

    def lambda_5498():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5498)
    Sleep(50)

    def lambda_54A8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54A8)
    Sleep(50)

    def lambda_54B8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_54B8)
    Sleep(50)

    def lambda_54C8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_54C8)
    Sleep(300)

    #C0113
    ChrTalk(
        0xE,
        (
            "#11P#04403F……既然如此……\x02\x03",

            "#04401F请务必让\x01",
            "我与各位同行。\x02\x03",

            "我多少懂得一些法术，\x01",
            "应该不会成为\x01",
            "大家的累赘。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x105,
        (
            "#6P#N#10309F呵呵，真是个固执的姐姐。\x02\x03",

            "#10300F你意下如何？\x01",
            "反正我看她是绝对\x01",
            "不会让步的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0115
    ChrTalk(
        0x101,
        (
            "#6P#00003F……没办法。\x01",
            "既然如此，\x01",
            "那我们就一起行动吧。\x02\x03",

            "#00000F我们以前曾调查过这个遗迹，\x01",
            "这次应该可以顺利解决。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0116
    ChrTalk(
        0x101,
        (
            "#11P#00000F不过……\x01",
            "艾莉，你不要紧吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0117
    ChrTalk(
        0x102,
        (
            "#6P#00113F真、真是的，\x01",
            "不用担心我啦。\x02\x03",

            "#00111F毕竟以前进去过一次，\x01",
            "只要充分做好心理准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#11P#00012F（看来还是\x01",
            "  很害怕啊……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(300)

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#00004F总、总之，\x01",
            "莉丝小姐也没有异议吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xE,
        (
            "#11P#04400F……嗯，是的，\x01",
            "请大家多多关照。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查月之僧院】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "莉丝修女以保护对象的身份加入队伍。\x01",
            "当其ＨＰ降为０时，游戏就会结束。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddParty(0x8C, 0xFF, 0xFF)
    SetChrFlags(0xE, 0x80)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, -124480, 19000, 147110, 55)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7C, 0x4, 0x2)
    OP_29(0x7C, 0x1, 0x0)
    ClearScenarioFlags(0x150, 4)
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x4, 0x1)
    ModifyEventFlags(0, 4, 0x80)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_28_4739 end

    def Function_29_5863(): pass

    label("Function_29_5863")

    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-130080, 21250, 139610, 0)
    MoveCamera(19, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18810, 0)
    SetChrPos(0x101, -129729, 19750, 140230, 223)
    SetChrPos(0x102, -128590, 19750, 139960, 223)
    SetChrPos(0x103, -129550, 19710, 141680, 223)
    SetChrPos(0x104, -128229, 19590, 141260, 223)
    SetChrPos(0x109, -127000, 19450, 141150, 223)
    SetChrPos(0x105, -128440, 19430, 142730, 223)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -131050, 20000, 138750, 55)
    RemoveParty(0x8C, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3E")

    #C0123
    ChrTalk(
        0xE,
        "#6P#04405F要放弃探索『僧院』吗？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#11P#00000F不，只是去其它地方\x01",
            "稍微准备一下而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xE,
        (
            "#6P#04403F那我就留在这里看守好了，\x01",
            "以免其他人入内。\x02\x03",

            "#04400F请大家慢慢准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#11P#00005F那个……如果可以，\x01",
            "希望莉丝小姐\x01",
            "也和我们一起走……\x02\x03",

            "#00003F把你一个人留在这里\x01",
            "总不太好。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "#6P#04403F……哪里，\x01",
            "这是我的工作。\x02\x03",

            "#04400F如果各位有什么难处，\x01",
            "我一个人进去探索也……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#11P#00006F……请不要这样。\x02\x03",

            "#00001F我们稍后还会回来的，\x01",
            "请你千万不要\x01",
            "一个人进去啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xE,
        (
            "#6P#04403F……明白了，\x01",
            "我会等大家的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x157, 5)
    Jump("loc_5BEA")

    label("loc_5B3E")


    #C0130
    ChrTalk(
        0xE,
        "#6P#04400F要放弃探索『僧院』吗？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#11P#00000F我们要去做一些准备工作。\x02\x03",

            "莉丝小姐，不好意思，\x01",
            "你可以在这里稍等一阵子吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#6P#04403F……明白了，\x01",
            "我会等大家的。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_5BEA")

    Fade(500)
    SetChrPos(0xE, -133420, 20000, 135100, 55)
    OP_4C(0xE, 0xFF)
    OP_37()
    SetChrPos(0x0, -135420, 20000, 126370, 190)
    OP_68(-135420, 23500, 126370, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    OP_0D()
    OP_29(0x7C, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_29_5863 end

    def Function_30_5C68(): pass

    label("Function_30_5C68")

    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-136960, 22000, 130690, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15660, 0)
    SetChrPos(0x101, -136050, 20000, 132320, 45)
    SetChrPos(0x102, -137070, 20000, 133060, 45)
    SetChrPos(0x103, -135790, 20000, 131260, 45)
    SetChrPos(0x104, -137600, 20000, 131410, 45)
    SetChrPos(0x109, -138640, 20000, 131920, 45)
    SetChrPos(0x105, -137150, 20000, 130120, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xE, 0xFF)
    OP_93(0xE, 0xE1, 0x0)
    OP_0D()

    #C0133
    ChrTalk(
        0xE,
        (
            "#11P#04400F我一直在等着大家。\x02\x03",

            "#04403F我们继续探索吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x8C, 0xFF, 0xFF)
    SetChrFlags(0xE, 0x80)
    OP_37()
    SetChrPos(0x0, -124480, 19000, 147110, 55)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    OP_29(0x7C, 0x2, 0x1)
    EventEnd(0x5)
    Return()

    # Function_30_5C68 end

    def Function_31_5DAB(): pass

    label("Function_31_5DAB")

    TalkBegin(0xFF)
    SetChrName("")

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门牢固地关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0135
    ChrTalk(
        0x101,
        "#00005F……门好像锁着呢。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x18D,
        "#04400F去找找其它的入口吧。\x02",
    )

    CloseMessageWindow()
    OP_29(0x7C, 0x1, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_31_5DAB end

    def Function_32_5E17(): pass

    label("Function_32_5E17")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　未经许可，禁止继续前进　※\x01",
            "※　　克洛斯贝尔警备队　　　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_32_5E17 end

    SaveToFile()

Try(main)
