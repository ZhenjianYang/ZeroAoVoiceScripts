from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "レオールガンイージ",     # 1
        "レオールガンイージ",     # 2
        "アビスワーム",           # 3
        "アビスワーム",           # 4
        "鉄鋼ドリュー",           # 5
        "鉄鋼ドリュー",           # 6
        "シスター・リース",       # 7
        "SE制御",                 # 8
        "br2070",                 # 9
        "br2070",                 # 10
        "br2070",                 # 11
        "br2070",                 # 12
        "br2080",                 # 13
        "マインツ山道方面",       # 14
    ))

    ATBonus("ATBonus_640", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_660", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_6540", 10,  0,   7,   0,   4,   2,   4)
    Sepith("Sepith_6548", 0,   4,   2,   9,   6,   4,   2)

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
        "BattleInfo_740", 0x0000, 64, 6, 60, 6, 1, 25, 0, "br2070", "Sepith_6540", 30, 30, 25, 15,
        (
            ("ms76100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6A0", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
            ("ms76100.dat", "ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, "MonsterBattlePostion_680", "MonsterBattlePostion_700", "ed7450", "ed7453", "ATBonus_640"),
        )
    )

    BattleInfo(
        "BattleInfo_808", 0x0000, 64, 6, 60, 6, 1, 40, 0, "br2070", "Sepith_6548", 30, 30, 25, 15,
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

    PlaceName(16.25, 0.0, 5.0, 0x0000, 0x0000, "マインツ山道方面")

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
        "Function_7_16A0",         # 07, 7
        "Function_8_17F1",         # 08, 8
        "Function_9_1942",         # 09, 9
        "Function_10_1A93",        # 0A, 10
        "Function_11_1DF1",        # 0B, 11
        "Function_12_214F",        # 0C, 12
        "Function_13_2153",        # 0D, 13
        "Function_14_2496",        # 0E, 14
        "Function_15_252A",        # 0F, 15
        "Function_16_2576",        # 10, 16
        "Function_17_25A2",        # 11, 17
        "Function_18_25EE",        # 12, 18
        "Function_19_2B65",        # 13, 19
        "Function_20_2EE7",        # 14, 20
        "Function_21_2F5E",        # 15, 21
        "Function_22_32D4",        # 16, 22
        "Function_23_3392",        # 17, 23
        "Function_24_33C7",        # 18, 24
        "Function_25_41AA",        # 19, 25
        "Function_26_4A3B",        # 1A, 26
        "Function_27_4A7F",        # 1B, 27
        "Function_28_4A98",        # 1C, 28
        "Function_29_5E06",        # 1D, 29
        "Function_30_6297",        # 1E, 30
        "Function_31_63E8",        # 1F, 31
        "Function_32_6474",        # 20, 32
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164F")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_15D8")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_164A")

    label("loc_15D8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_164A")

    Jump("loc_1694")

    label("loc_164F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1694")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_154F end

    def Function_7_16A0(): pass

    label("Function_7_16A0")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A0")
    Sound(14, 0, 100, 0)
    OP_74(0x8, 0x1E)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x16, 1)"), scpexpr(EXPR_END)), "loc_1729")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_179B")

    label("loc_1729")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x16),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x16),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_179B")

    Jump("loc_17E5")

    label("loc_17A0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_17E5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_16A0 end

    def Function_8_17F1(): pass

    label("Function_8_17F1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F1")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x442, 1)"), scpexpr(EXPR_END)), "loc_187A")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_18EC")

    label("loc_187A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x442),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x442),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18EC")

    Jump("loc_1936")

    label("loc_18F1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1936")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_17F1 end

    def Function_9_1942(): pass

    label("Function_9_1942")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A42")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x456, 1)"), scpexpr(EXPR_END)), "loc_19CB")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1A3D")

    label("loc_19CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x456),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x456),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A3D")

    Jump("loc_1A87")

    label("loc_1A42")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1A87")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1942 end

    def Function_10_1A93(): pass

    label("Function_10_1A93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C4B")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1C2C")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C27")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1C24")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1B4D)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C06")
    Call(1, 5)
    Jump("loc_1C1F")

    label("loc_1C06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1C1C")
    Call(1, 4)
    Jump("loc_1C1F")

    label("loc_1C1C")

    Call(1, 3)

    label("loc_1C1F")

    Jump("loc_1C27")

    label("loc_1C24")

    Call(1, 1)

    label("loc_1C27")

    Jump("loc_1C42")

    label("loc_1C2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1C42")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1C42")

    TalkEnd(0xFF)
    Return()

    label("loc_1C4B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 5)), scpexpr(EXPR_END)), "loc_1DD6")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD1")
    ClearScenarioFlags(0x3B, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1DCE")
    ClearScenarioFlags(0x39, 5)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1CF7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1CF7)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC9")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DB0")
    Call(1, 5)
    Jump("loc_1DC9")

    label("loc_1DB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DC6")
    Call(1, 4)
    Jump("loc_1DC9")

    label("loc_1DC6")

    Call(1, 3)

    label("loc_1DC9")

    Jump("loc_1DD1")

    label("loc_1DCE")

    Call(1, 1)

    label("loc_1DD1")

    Jump("loc_1DEC")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 5)), scpexpr(EXPR_END)), "loc_1DEC")
    ClearScenarioFlags(0x39, 5)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1DEC")

    TalkEnd(0xFF)
    Return()

    # Function_10_1A93 end

    def Function_11_1DF1(): pass

    label("Function_11_1DF1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FA9")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_END)), "loc_1F8A")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F85")
    ClearScenarioFlags(0x3B, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_1F82")
    ClearScenarioFlags(0x39, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1EAB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1EAB)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F7D")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F64")
    Call(1, 5)
    Jump("loc_1F7D")

    label("loc_1F64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F7A")
    Call(1, 4)
    Jump("loc_1F7D")

    label("loc_1F7A")

    Call(1, 3)

    label("loc_1F7D")

    Jump("loc_1F85")

    label("loc_1F82")

    Call(1, 1)

    label("loc_1F85")

    Jump("loc_1FA0")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_1FA0")
    ClearScenarioFlags(0x39, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_1FA0")

    TalkEnd(0xFF)
    Return()

    label("loc_1FA9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 6)), scpexpr(EXPR_END)), "loc_2134")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_212F")
    ClearScenarioFlags(0x3B, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_212C")
    ClearScenarioFlags(0x39, 6)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2055():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2055)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2127")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_210E")
    Call(1, 5)
    Jump("loc_2127")

    label("loc_210E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2124")
    Call(1, 4)
    Jump("loc_2127")

    label("loc_2124")

    Call(1, 3)

    label("loc_2127")

    Jump("loc_212F")

    label("loc_212C")

    Call(1, 1)

    label("loc_212F")

    Jump("loc_214A")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 6)), scpexpr(EXPR_END)), "loc_214A")
    ClearScenarioFlags(0x39, 6)
    OP_65(0x7, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_214A")

    TalkEnd(0xFF)
    Return()

    # Function_11_1DF1 end

    def Function_12_214F(): pass

    label("Function_12_214F")

    Call(1, 6)
    Return()

    # Function_12_214F end

    def Function_13_2153(): pass

    label("Function_13_2153")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2185")
    SetScenarioFlags(0x31, 2)

    label("loc_2185")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_21C5")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_21BA")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_21C0")

    label("loc_21BA")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_21C0")

    Jump("loc_21CB")

    label("loc_21C5")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_21CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2488")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2244")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2224"),
        (SWITCH_DEFAULT, "loc_2235"),
    )


    label("loc_2224")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_223F")

    label("loc_2235")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_223F")

    Jump("loc_2483")

    label("loc_2244")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2278")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_2278")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22AC"),
        (1, "loc_23B0"),
        (2, "loc_2441"),
        (SWITCH_DEFAULT, "loc_2479"),
    )


    label("loc_22AC")

    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    OP_74(0xD, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22DD")
    OP_70(0xD, 0x12C)
    OP_71(0xD, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_22ED")

    label("loc_22DD")

    OP_70(0xD, 0xF0)
    OP_71(0xD, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_22ED")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2343")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2343")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2366")
    Sound(461, 0, 100, 0)

    label("loc_2366")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2386")
    OP_70(0xD, 0x14A)
    OP_71(0xD, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2396")

    label("loc_2386")

    OP_70(0xD, 0x10E)
    OP_71(0xD, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2396")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xD, "light", 0x1, 0x1)
    OP_70(0xD, 0x0)
    Jump("loc_21CB")

    label("loc_23B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2422")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_23E5")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_23FD")

    label("loc_23E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_23F8")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_23FD")

    label("loc_23F8")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_23FD")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_243C")

    label("loc_2422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2432")
    OP_AF(0xFB)
    Jump("loc_243C")

    label("loc_2432")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_243C")

    Jump("loc_2483")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2474")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_246A")
    OP_AF(0xFB)
    Jump("loc_2474")

    label("loc_246A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2474")

    Jump("loc_2483")

    label("loc_2479")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2483")

    Jump("loc_21CB")

    label("loc_2488")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_13_2153 end

    def Function_14_2496(): pass

    label("Function_14_2496")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_24F1")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_24E6")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_24EC")

    label("loc_24E6")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_24EC")

    Jump("loc_2515")

    label("loc_24F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_250F")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_2515")

    label("loc_250F")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_2515")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2496 end

    def Function_15_252A(): pass

    label("Function_15_252A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_254A")
    Call(0, 31)
    Return()

    label("loc_254A")

    TalkBegin(0xFF)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_15_252A end

    def Function_16_2576(): pass

    label("Function_16_2576")

    TalkBegin(0xFF)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_16_2576 end

    def Function_17_25A2(): pass

    label("Function_17_25A2")

    OP_E2(0x3)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_25C1")
    Call(0, 20)
    Jump("loc_25D5")

    label("loc_25C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 4)), scpexpr(EXPR_END)), "loc_25D2")
    Call(0, 19)
    Jump("loc_25D5")

    label("loc_25D2")

    Call(0, 18)

    label("loc_25D5")

    OP_E2(0x2)
    ClearMapObjFlags(0x17, 0x1000)
    ClearMapObjFlags(0xC, 0x1000)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    Return()

    # Function_17_25A2 end

    def Function_18_25EE(): pass

    label("Function_18_25EE")

    EventBegin(0x0)
    Call(0, 22)
    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B1B")

    #A0023
    AnonymousTalk(
        0x105,
        (
            "#10403F《身喰らう蛇#10Rウ ロ ボ ロ ス#》……\x01",
            "ここは彼らが守っているみたいだね。\x02\x03",

            "#10401F扉の前に立っているのは、\x01",
            "結社の拠点防衛用の重人形兵器\x01",
            "《レオールガンイージ》だ。\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0x103,
        (
            "#00203Fかなりの武装を\x01",
            "積んでいるみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2734")

    #A0025
    AnonymousTalk(
        0x109,
        (
            "#10101Fええ、おそらく拠点防衛用の\x01",
            "大火力タイプかと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2734")


    #A0026
    AnonymousTalk(
        0x104,
        (
            "#00301Fノコノコ近づいていくのは\x01",
            "自殺行為だろうな。\x02",
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
            "#00003F#6P……とにかく、今は\x01",
            "引いたほうがよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#6Pそれにしてもワジ、\x01",
            "やっぱり《結社》については\x01",
            "随分と詳しいみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28D9")

    #C0029
    ChrTalk(
        0x105,
        (
            "#10404F#12Pフフ……\x01",
            "まあ、そこそこは詳しいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x107,
        (
            "#01200F#6P#3C《騎士団》と《結社》は\x01",
            "歴史の影で幾度となく\x01",
            "対立してきた経緯がある。\x02\x03",

            "その中で、相手を知る事は\x01",
            "最も重要な事だろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29A9")

    label("loc_28D9")


    #C0031
    ChrTalk(
        0x105,
        (
            "#10404F#12Pフフ……\x01",
            "まあ、そこそこは詳しいかな？\x02\x03",

            "#10400F《騎士団》と《結社》は\x01",
            "歴史の影で幾度となく\x01",
            "対立した経緯があるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00003F#6Pなるほど……そういう事情なら\x01",
            "相手を知る事は重要だろうしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A9")


    #C0033
    ChrTalk(
        0x105,
        (
            "#10406F#12Pま、《騎士団》も《結社》も\x01",
            "常に状況は変わっていくから、\x01",
            "正直イタチゴッコなんだけどね。\x02\x03",

            "#10402Fおっと、こんな事を軽々しく言うと\x01",
            "アッバスに怒られちゃうかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AA9")

    #C0034
    ChrTalk(
        0x109,
        "#10106F#6Pも、もうワジ君ったら……\x02",
    )

    CloseMessageWindow()

    label("loc_2AA9")


    #C0035
    ChrTalk(
        0x106,
        (
            "#10709F#6Pあ、あはは……\x01",
            "アッバスさんも苦労してそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00001F#6P……ひとまずここを離れよう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2B1B")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B35")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B4E")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2B4E")

    SetChrPos(0x0, -135390, 20000, 123030, 180)
    SetScenarioFlags(0x1AF, 5)
    EventEnd(0x5)
    Return()

    # Function_18_25EE end

    def Function_19_2B65(): pass

    label("Function_19_2B65")

    EventBegin(0x0)
    Call(0, 22)
    Call(0, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C4D")

    #A0037
    AnonymousTalk(
        0x105,
        (
            "#10403Fここにも《身喰らう蛇#10Rウ ロ ボ ロ ス#》か……\x02\x03",

            "#10401F扉の前に立っているのは、\x01",
            "結社の拠点防衛用の重人形兵器\x01",
            "《レオールガンイージ》だ。\x02",
        )
    )

    CloseMessageWindow()

    #A0038
    AnonymousTalk(
        0x103,
        (
            "#00203Fかなりの武装を\x01",
            "積んでいるみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CDE")

    label("loc_2C4D")


    #A0039
    AnonymousTalk(
        0x106,
        "#10701Fここにも《身喰らう蛇#10Rウ ロ ボ ロ ス#》が……\x02",
    )

    CloseMessageWindow()

    #A0040
    AnonymousTalk(
        0x103,
        (
            "#00203F扉の前に立っている人形兵器は、\x01",
            "かなりの武装を\x01",
            "積んでいるみたいですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D28")

    #A0041
    AnonymousTalk(
        0x109,
        (
            "#10101Fええ、おそらく拠点防衛用の\x01",
            "大火力タイプかと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D28")


    #A0042
    AnonymousTalk(
        0x104,
        (
            "#00301F#6Pノコノコ近づいていくのは\x01",
            "自殺行為だろうな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 23)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DF8")

    #C0043
    ChrTalk(
        0x101,
        (
            "#00003F#6P……やっぱり、迂闊に手を出すのは\x01",
            "やめておいた方がよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x106,
        "#10701F#6Pはい、ひとまず離れましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E66")

    label("loc_2DF8")


    #C0045
    ChrTalk(
        0x101,
        (
            "#00003F#6P……やっぱり、迂闊に手を出すのは\x01",
            "やめておいた方がよさそうだ。\x02\x03",

            "#00001Fひとまずここを離れよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E9D")

    #C0046
    ChrTalk(
        0x107,
        "#01200F#6P#3Cうむ、行くとしよう。\x02",
    )

    CloseMessageWindow()

    label("loc_2E9D")

    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2EB7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2EB7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2ED0")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2ED0")

    SetChrPos(0x0, -135390, 20000, 123030, 180)
    SetScenarioFlags(0x1AF, 5)
    EventEnd(0x5)
    Return()

    # Function_19_2B65 end

    def Function_20_2EE7(): pass

    label("Function_20_2EE7")

    EventBegin(0x1)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00001Fこの先は《結社》が\x01",
            "守っているみたいだ。\x02\x03",

            "#00003F……今は引いたほうが\x01",
            "よさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -135390, 20000, 123030, 180)
    EventEnd(0x4)
    Return()

    # Function_20_2EE7 end

    def Function_21_2F5E(): pass

    label("Function_21_2F5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FA0")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2F95():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F95)
    Sleep(50)

    label("loc_2FA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FE2")
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2FD7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FD7)
    Sleep(50)

    label("loc_2FE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3024")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_3019():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3019)
    Sleep(50)

    label("loc_3024")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_306D")
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x104, 0x8, 500)

    def lambda_3062():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3062)
    Sleep(50)

    label("loc_306D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30B6")
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x105, 0x8, 500)

    def lambda_30AB():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_30AB)
    Sleep(50)

    label("loc_30B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30FF")
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x106, 0x8, 500)

    def lambda_30F4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_30F4)
    Sleep(50)

    label("loc_30FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3148")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x109, 0x8, 500)

    def lambda_313D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_313D)
    Sleep(50)

    label("loc_3148")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3191")
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0x107, 0x8, 500)

    def lambda_3186():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3186)
    Sleep(50)

    label("loc_3191")

    Sleep(1000)

    #C0048
    ChrTalk(
        0x101,
        "#00005Fあれは……\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_321F")
    SetChrPos(0x0, -133380, 20000, 124530, 39)

    label("loc_321F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_323F")
    SetChrPos(0x1, -134310, 20000, 125180, 39)

    label("loc_323F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_325F")
    SetChrPos(0x2, -132840, 20000, 123600, 39)

    label("loc_325F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_327F")
    SetChrPos(0x3, -132290, 20000, 122620, 39)

    label("loc_327F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32A9")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x4, -134600, 20000, 123840, 39)

    label("loc_32A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32D3")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x5, -134300, 20000, 122570, 39)

    label("loc_32D3")

    Return()

    # Function_21_2F5E end

    def Function_22_32D4(): pass

    label("Function_22_32D4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32F4")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3309")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3309")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_331E")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_331E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3333")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3348")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_335D")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_335D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3372")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3372")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3387")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3387")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_22_32D4 end

    def Function_23_3392(): pass

    label("Function_23_3392")

    Fade(500)
    OP_68(-134300, 21620, 122570, 0)
    MoveCamera(39, 6, 0, 0)
    OP_6E(530, 0)
    SetCameraDistance(17870, 0)
    OP_0D()
    Return()

    # Function_23_3392 end

    def Function_24_33C7(): pass

    label("Function_24_33C7")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_343A")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch0295F.itc", 0x27)

    label("loc_343A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3458")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch0315F.itc", 0x27)

    label("loc_3458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3476")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch0325A.itc", 0x27)

    label("loc_3476")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3494")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch0295F.itc", 0x29)

    label("loc_3494")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34B2")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch0315F.itc", 0x29)

    label("loc_34B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34D0")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch0325A.itc", 0x29)

    label("loc_34D0")

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

    def lambda_3663():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3663)
    Sleep(50)

    def lambda_367B():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_367B)
    Sleep(50)

    def lambda_3693():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3693)
    Sleep(50)

    def lambda_36AB():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_36AB)
    Sleep(50)

    def lambda_36C3():
        OP_9B(0x0, 0xF4, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_36C3)
    Sleep(50)

    def lambda_36DB():
        OP_9B(0x0, 0xF5, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_36DB)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_378C")

    #C0049
    ChrTalk(
        0x105,
        "#10401F#6P《身喰らう蛇#10Rウ ロ ボ ロ ス#》の紋章か……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37C7")

    label("loc_378C")


    #C0050
    ChrTalk(
        0x106,
        "#10701F#6P《身喰らう蛇#10Rウ ロ ボ ロ ス#》の紋章……\x02",
    )

    CloseMessageWindow()

    label("loc_37C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_3852")

    #C0051
    ChrTalk(
        0x103,
        (
            "#00201F#6Pどうやら何らかの力で\x01",
            "封鎖されているようですが……\x02\x03",

            "#00203Fそういえば、ここを守っていた\x01",
            "人形兵器はどこに……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3893")

    label("loc_3852")


    #C0052
    ChrTalk(
        0x103,
        (
            "#00201F#6Pどうやら何らかの力で\x01",
            "封鎖されているようですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3893")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38E5")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x109,
        "#10107F#6P皆さん、あれ……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_391C")

    label("loc_38E5")

    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x106,
        "#10707F#6Pあれを……！\x02",
    )

    CloseMessageWindow()

    label("loc_391C")

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
        "#00101Fあの大鐘が……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#00301Fとにかくあれの共鳴を\x01",
            "止めりゃあいいってわけだな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("少年の声")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3720V#30W#28Aウフフ、その通りさ。\x07\x00\x02",
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
    SetChrName("少年の声")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "やれやれ、ここに来たって事は\x01",
            "マイスターから聞いたみたいだね。\x02\x03",

            "ゴルディアス級最終型や\x01",
            "アルカンシェル襲撃の件で\x01",
            "怒らせちゃったかな？\x07\x00\x02",
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
        "#00304F#6Pああ、ご立腹だったぜ。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        "#00211F#6Pまあ、自業自得かと。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("少年の声")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "うーん、博士や猟兵たちの\x01",
            "とばっちりを喰らった気もするけど……\x02\x03",

            "フフ、まあいいか。\x07\x00\x02",
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

    def lambda_3D8B():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_3D8B)
    Sleep(50)
    SetChrChipByIndex(0xF4, 0x27)
    SetChrSubChip(0xF4, 0x0)

    def lambda_3DB3():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_3DB3)
    Sleep(50)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)

    def lambda_3DDB():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3DDB)
    Sleep(50)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_3E03():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3E03)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x2)

    def lambda_3E2B():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E2B)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x2)

    def lambda_3E53():
        OP_9C(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E53)
    Sleep(50)
    WaitChrThread(0xF5, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E88")
    Sound(540, 0, 50, 0)

    label("loc_3E88")

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

    def lambda_3F0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3F0F)

    def lambda_3F20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3F20)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    CancelBlur(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    SetMessageWindowPos(280, 20, -1, -1)
    SetChrName("少年の声")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "──ここに来たってことは\x01",
            "それなりの覚悟があるんだよね？\x02\x03",

            "ウフフ、愉しませてもらうよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 5)), scpexpr(EXPR_END)), "loc_3FF6")

    #C0064
    ChrTalk(
        0x101,
        (
            "#00007F#6Pくっ……\x01",
            "前に見たやつか！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D4")

    label("loc_3FF6")


    #C0065
    ChrTalk(
        0x101,
        "#00007F#6Pくっ……人形兵器か！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4087")

    #C0066
    ChrTalk(
        0x105,
        (
            "#10410F#6P《レオールガンイージ》！\x02\x03",

            "#10407F結社の拠点防衛用の\x01",
            "重人形兵器だ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D4")

    label("loc_4087")


    #C0067
    ChrTalk(
        0x109,
        (
            "#10107F#6P武装を多数確認！\x02\x03",

            "おそらく拠点防衛用の\x01",
            "大火力タイプかと……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D4")


    #C0068
    ChrTalk(
        0x104,
        "#00307F#6Pとにかくブチ倒すぞ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4125")

    #C0069
    ChrTalk(
        0x106,
        "#10707F#6Pはいっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_413F")

    label("loc_4125")


    #C0070
    ChrTalk(
        0x109,
        "#10107F#6P了解です！\x02",
    )

    CloseMessageWindow()

    label("loc_413F")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(10650, 500)

    def lambda_4159():
        OP_9B(0x1, 0xFE, 0xFFE2, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4159)

    def lambda_416E():
        OP_9B(0x1, 0xFE, 0x1E, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_416E)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    OP_24(0x3BF)
    Battle("BattleInfo_958", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 25)
    Return()

    # Function_24_33C7 end

    def Function_25_41AA(): pass

    label("Function_25_41AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    SoundLoad(155)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_41EB")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_41EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4203")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_4203")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_421B")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_421B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4233")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_4233")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_424B")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_424B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4263")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_4263")

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

    def lambda_4405():

        label("loc_4405")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_4405")

    QueueWorkItem2(0x8, 3, lambda_4405)

    def lambda_4423():

        label("loc_4423")

        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        Yield()
        Jump("loc_4423")

    QueueWorkItem2(0x9, 3, lambda_4423)
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

    def lambda_44C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_44C6)
    Sound(200, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)
    Sleep(100)
    Sound(833, 0, 50, 0)

    def lambda_4520():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4520)
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
    SetChrName("少年の声")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3721V#30W#25Aウフフ、お見事。\x02\x03",

            "#3722V#30W#40Aそれじゃあ遠慮なく\x01",
            "中に入っておいでよ。\x02\x03",

            "#3723V#30W#27A鐘の前で待ってるからさ㈱\x07\x00\x02",
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
        "#00108F#5P……どう思う？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        (
            "#00006F#5Pどう考えても何か仕掛けを\x01",
            "用意していそうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48A6")

    #C0074
    ChrTalk(
        0x105,
        (
            "#10403F#5Pそれもタチの悪そうな\x01",
            "仕掛けの可能性が高そうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48E9")

    label("loc_48A6")


    #C0075
    ChrTalk(
        0x106,
        (
            "#10703F#5Pええ、それもタチの悪い\x01",
            "仕掛けの可能性が高そうです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4937")

    #C0076
    ChrTalk(
        0x109,
        (
            "#10101F#5Pそれでも踏み込むしか\x01",
            "ないと思います……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_496A")

    label("loc_4937")


    #C0077
    ChrTalk(
        0x106,
        (
            "#10701F#5Pそれでも踏み込むしか\x01",
            "ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_496A")


    #C0078
    ChrTalk(
        0x104,
        (
            "#00307F#11Pおお。\x01",
            "腹を括るとしようぜ。\x02",
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

    # Function_25_41AA end

    def Function_26_4A3B(): pass

    label("Function_26_4A3B")

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

    # Function_26_4A3B end

    def Function_27_4A7F(): pass

    label("Function_27_4A7F")

    Sound(203, 0, 60, 0)
    Sleep(900)
    Sound(203, 0, 70, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Return()

    # Function_27_4A7F end

    def Function_28_4A98(): pass

    label("Function_28_4A98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4AA8")
    Call(0, 30)
    Return()

    label("loc_4AA8")

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
        "シスター服の女性",
        (
            "#04400F『──かの罪人によって\x01",
            "  それは打ち鳴らされた。』\x02\x03",

            "『響き渡る禍々しい音が\x01",
            "  混沌の時代の始まりを告げた……』\x02\x03",

            "#04403F──ラダー記序節、\x01",
            "『目覚めの響音』より……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(160, 140, -1, -1)

    #A0080
    AnonymousTalk(
        0x101,
        "#00005F（あれ、あの人は……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #A0081
    AnonymousTalk(
        0x102,
        "#00105F……リ、リースさん！？\x02",
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
            "あなた方は……\x01",
            "確か、特務支援課の。\x02",
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
        "#12P#10302Fフフ、ご無沙汰してるね。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        "#12P#00205Fええと、この方は……？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#6P#00000Fあ、ああ……\x01",
            "ついこの間出会ったばかりの\x01",
            "教会のシスターだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xE,
        (
            "#11P#04404Fリース・アルジェントです。\x01",
            "どうぞよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#6P#00300Fしかしまあ、教会のシスターが\x01",
            "こんなところで何をしてたんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x109,
        (
            "#6P#10105Fそ、そうですよ！\x02\x03",

            "#10106Fここは警備隊によって\x01",
            "封鎖されてるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xE,
        (
            "#11P#04403Fええ、今日は鉱山町の方へ\x01",
            "出張していたのですが……\x02\x03",

            "#04401F実は先ほど、こちらの方から\x01",
            "『音』が聞こえたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        "#6P#00005F音……？\x02",
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
        "#6P#00301Fおいロイド、こいつは……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ……\x01",
            "《鐘》が鳴っているみたいだ。\x02\x03",

            "#00001Fティオ、中から例の気配は感じるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#12P#00203F……微かにですが……\x02\x03",

            "#00201F以前の“上位三属性”の気配が\x01",
            "復活してしまっているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#6P#00105Fそ、そんな……\x02\x03",

            "#00101F誰かがまた、\x01",
            "あの鐘を動かしたっていうの？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x105,
        (
            "#12P#10303Fふむ……\x02\x03",

            "#10302F察するに、ここが例の\x01",
            "“幽霊騒動”の現場なんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        (
            "#11P#04405F幽霊……？\x02\x03",

            "#04400Fあの、できれば詳しく\x01",
            "話を聞かせていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#6P#00006Fえ、ええ、実は……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは以前、この場所を\x01",
            "探索した時のことを説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0099
    ChrTalk(
        0xE,
        (
            "#11P#04403F……なるほど。\x01",
            "そういうことですか。\x02\x03",

            "#04408F上位三属性が働く\x01",
            "摩訶不思議な遺跡……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)

    #C0100
    ChrTalk(
        0x102,
        "#6P#00105F……リースさん？\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xE,
        (
            "#11P#04403F……いえ、何でもありません。\x02\x03",

            "#04400Fだとしたら、早急に\x01",
            "その《鐘》とやらを止める\x01",
            "必要がありそうですね。\x02\x03",

            "#04403Fそれでは皆さん、またどこかで。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5452():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_5452)
    OP_68(-134870, 22200, 129860, 3500)
    MoveCamera(6, 13, 0, 3500)
    OP_6E(510, 3500)
    SetCameraDistance(14600, 3500)
    OP_6F(0x79)

    #C0102
    ChrTalk(
        0x101,
        "#6P#00005Fへっ……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xE,
        "#5P#04403F……よいしょ。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrPos(0xE, -131490, 20000, 137100, 55)
    OP_0D()
    Sound(30, 0, 100, 0)

    def lambda_54E8():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_54E8)
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
            "#6P#10111Fちょ、ちょっとリースさん！？\x01",
            "一体何を……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0xE1, 0x1F4)

    #C0105
    ChrTalk(
        0xE,
        (
            "#11P#04400Fいえ、その鐘とやらを\x01",
            "止めにいこうかと。\x02\x03",

            "#04403F……成仏できない魂を鎮めるのも、\x01",
            "聖職者としての役目ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#00306Fつってもなあ……\x02\x03",

            "#00301F……おい、ロイド。\x01",
            "ここは俺たちが引き受けたほうが\x01",
            "いいんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        (
            "#12P#00203Fそうですね。\x02\x03",

            "#00200F上位三属性が働いているとしたら、\x01",
            "例の“魔物”たちが徘徊している\x01",
            "可能性は高いでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、確かに……\x01",
            "民間人を歩かせるには危険すぎる。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#6P#00105Fえ、えっとでも、彼女なら……\x02",
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

    def lambda_586C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_586C)
    Sleep(50)

    def lambda_587C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_587C)
    Sleep(50)

    def lambda_588C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_588C)
    Sleep(50)

    def lambda_589C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_589C)
    Sleep(50)

    def lambda_58AC():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_58AC)
    Sleep(300)

    #C0110
    ChrTalk(
        0x101,
        "#11P#00005F……どうしたエリィ？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0111
    ChrTalk(
        0x102,
        (
            "#6P#00103F……い、いえ。\x01",
            "そうね、確かに危険だわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xE, 500)
    Sleep(300)

    #C0112
    ChrTalk(
        0x102,
        (
            "#6P#00100Fリースさん、どうかここは\x01",
            "任せてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_596B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_596B)
    Sleep(50)

    def lambda_597B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_597B)
    Sleep(50)

    def lambda_598B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_598B)
    Sleep(50)

    def lambda_599B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_599B)
    Sleep(50)

    def lambda_59AB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59AB)
    Sleep(300)

    #C0113
    ChrTalk(
        0xE,
        (
            "#11P#04403F……それなら……\x02\x03",

            "#04401F是非、この私を同行させて\x01",
            "くださいませんか。\x02\x03",

            "私にも法術の心得が\x01",
            "多少あるので、お邪魔には\x01",
            "ならないかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x105,
        (
            "#6P#N#10309Fフフ、なかなか頑固なお姉さんだね。\x02\x03",

            "#10300Fどうするんだい？\x01",
            "彼女、まったく折れる気は\x01",
            "ないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0115
    ChrTalk(
        0x101,
        (
            "#6P#00003F……仕方ない。\x01",
            "そういうことなら\x01",
            "同行してもらおう。\x02\x03",

            "#00000Fこの遺跡は前に探索しているし、\x01",
            "多分、何とかなるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)
    Sleep(300)

    #C0116
    ChrTalk(
        0x101,
        (
            "#11P#00000Fってことだけど……\x01",
            "エリィ、大丈夫かな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0117
    ChrTalk(
        0x102,
        (
            "#6P#00113Fも、もう。\x01",
            "心配はいらないわ。\x02\x03",

            "#00111F一度入った事のある場所だし、\x01",
            "しっかりと心の準備を整えれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#11P#00012F（それってあまり\x01",
            "  大丈夫じゃないんじゃ……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(300)

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#00004Fと、とにかく。\x01",
            "リースさんもそれでいいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xE,
        (
            "#11P#04400F……ええ、分かりました。\x01",
            "どうかよろしくお願いします。\x02",
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
            "クエスト【月の僧院の調査】\x07\x00",
            "を開始した！\x02",
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
            "シスター・リースが護衛対象に加わりました。\x01",
            "ＨＰが０になるとゲームオーバーになります。\x07\x00\x02",
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

    # Function_28_4A98 end

    def Function_29_5E06(): pass

    label("Function_29_5E06")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6151")

    #C0123
    ChrTalk(
        0xE,
        "#6P#04405F《僧院》の探索をやめるのですか？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#11P#00000Fいえ、少し別の場所で\x01",
            "準備をしようかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xE,
        (
            "#6P#04403Fでしたら、私はここで\x01",
            "人が入らないよう見張っておきます。\x02\x03",

            "#04400Fしっかり準備をなさってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#11P#00005Fええと、できれば\x01",
            "リースさんも一緒に\x01",
            "来ていただけると……\x02\x03",

            "#00003Fさすがに１人で残して\x01",
            "行くわけにはいきませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "#6P#04403F……いえ。\x01",
            "これは私の仕事ですから。\x02\x03",

            "#04400F何でしたらやはり、\x01",
            "私１人で探索しても……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        (
            "#11P#00006F……それはやめてください。\x02\x03",

            "#00001F後で戻ってきますから、\x01",
            "決して１人で入らないように\x01",
            "してくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xE,
        (
            "#6P#04403F……分かりました。\x01",
            "お待ちしています。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x157, 5)
    Jump("loc_6219")

    label("loc_6151")


    #C0130
    ChrTalk(
        0xE,
        "#6P#04400F《僧院》の探索をやめるのですか？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#11P#00000F少しの間、準備をしてきます。\x02\x03",

            "リースさん、すみませんが\x01",
            "ここで待っていてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#6P#04403F……分かりました。\x01",
            "お待ちしています。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6219")

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

    # Function_29_5E06 end

    def Function_30_6297(): pass

    label("Function_30_6297")

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
            "#11P#04400Fお待ちしてました。\x02\x03",

            "#04403Fそれでは探索を再開しましょう。\x02",
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

    # Function_30_6297 end

    def Function_31_63E8(): pass

    label("Function_31_63E8")

    TalkBegin(0xFF)
    SetChrName("")

    #A0134
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0135
    ChrTalk(
        0x101,
        "#00005F……閉まっているみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x18D,
        "#04400F別の入口を探した方がよさそうですね。\x02",
    )

    CloseMessageWindow()
    OP_29(0x7C, 0x1, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_31_63E8 end

    def Function_32_6474(): pass

    label("Function_32_6474")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※　この先、許可なく立ち入り禁止　※\x01",
            "※　　　　クロスベル警備隊　　　　※\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_32_6474 end

    SaveToFile()

Try(main)
