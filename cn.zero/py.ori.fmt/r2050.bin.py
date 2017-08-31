from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r2050.bin",                # FileName
        "r2050",                    # MapName
        "r2050",                    # Location
        0x0063,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2050", "r0000_1", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 99, 0, 2, 0, 3],
    )

    BuildStringList((
        "r2050",                  # 0
        "巴士",                   # 1
        "车１",                   # 2
        "致命毒蜘蛛",             # 3
        "SE控制",                 # 4
        "br2040",                 # 5
        "br2050",                 # 6
        "br2050",                 # 7
        "br2050",                 # 8
        "br2040",                 # 9
        "br2040",                 # 10
        "br2040",                 # 11
        "br2050",                 # 12
        "克洛斯贝尔市方向",       # 13
        "矿山镇玛因兹方向",       # 14
        "月之僧院方向",           # 15
    ))

    ATBonus("ATBonus_604", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3B2F", 0,   9,   2,   0,   5,   4,   5)
    Sepith("Sepith_3B1F", 7,   4,   0,   1,   4,   6,   3)
    Sepith("Sepith_3B27", 9,   0,   4,   0,   4,   2,   6)
    Sepith("Sepith_3B17", 0,   0,   0,   6,   6,   6,   6)
    Sepith("Sepith_3B0F", 14,  4,   9,   5,   7,   12,  9)

    MonsterBattlePostion("MonsterBattlePostion_664", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_66C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_674", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_644", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 0, 0, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_95C", 0x0000, 14, 6, 60, 10, 1, 40, 0, "br2050", "Sepith_3B2F", 30, 40, 20, 10,
        (
            ("ms69100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
        )
    )

    BattleInfo(
        "BattleInfo_7CC", 0x0000, 14, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_3B1F", 30, 40, 20, 10,
        (
            ("ms68100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms68100.dat", "ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
        )
    )

    BattleInfo(
        "BattleInfo_894", 0x0000, 14, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_3B27", 30, 40, 20, 10,
        (
            ("ms72800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms72800.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
        )
    )

    BattleInfo(
        "BattleInfo_704", 0x0000, 14, 6, 60, 10, 1, 30, 0, "br2040", "Sepith_3B17", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms71700.dat", "ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms71700.dat", "ms71700.dat", "ms65500.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
        )
    )

    BattleInfo(
        "BattleInfo_B48", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2050", "Sepith_3B0F", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7400", "ed7403", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A68", 0x0C10, 255, 6, 0, 0, 0, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76000.dat", "ms77700.dat", "ms77700.dat", "ms77700.dat", "ms77700.dat", 0, "ms77700.dat", 0, "MonsterBattlePostion_6E4", "MonsterBattlePostion_6C4", "ed7401", "ed7403", "ATBonus_604"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_A24", 0x0000, 14, 6, 60, 0, 1, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72800.dat", "ms68100.dat", "ms72800.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7401", "ed7403", "ATBonus_604"),
            (),
            (),
            (),
        )
    )

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
        "monster/ch71750.itc",               # 10
        "monster/ch71751.itc",               # 11
        "monster/ch68150.itc",               # 12
        "monster/ch68151.itc",               # 13
        "monster/ch72850.itc",               # 14
        "monster/ch72851.itc",               # 15
        "monster/ch69150.itc",               # 16
        "monster/ch69151.itc",               # 17
        "monster/ch76050.itc",               # 18
        "monster/ch76051.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-12930,  8500,    127330,  0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-11790,  32470,   0,       0x1010000,    "BattleInfo_95C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-48260,  51700,   0,       0x1010000,    "BattleInfo_7CC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-58330,  102750,  0,       0x1010000,    "BattleInfo_894", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-103440, 89080,   -14000,  0x1010000,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-57310,  146680,  0,       0x1010000,    "BattleInfo_95C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-25730,  141040,  8000,    0x1010000,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-83270,  179260,  0,       0x1010000,    "BattleInfo_7CC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-33350,  41540,   0,       0x1010000,    "BattleInfo_B48", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-62470,  119400,  0,       0x1010000,    "BattleInfo_B48", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-82940,  170350,  0,       0x1010000,    "BattleInfo_B48", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-74490,  81330,   -5980,   0x1010000,    "BattleInfo_B48", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-26820,  143860,  7990,    0x185010E,    "BattleInfo_A68", 0,   24,  0xFFFF, 8,  9)

    DeclEvent(0x0000, 0, 16,  -67.5,                 101.0,                 -1.0,                  324.0,                 [0.05892555043101311,  0.23570235073566437,   -0.0,                  0.0,                   -0.05892558768391609,  0.23570220172405243,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.928958892822266,     -7.8960137367248535,   0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 17,  -67.5,                 101.0,                 -1.0,                  324.0,                 [0.05892555043101311,  0.23570235073566437,   -0.0,                  0.0,                   -0.05892558768391609,  0.23570220172405243,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   9.928958892822266,     -7.8960137367248535,   0.20000000298023224,   1.0])
    DeclEvent(0x0040, 0, 8,   -26.81999969482422,    143.86000061035156,    6.989999771118164,     16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   3.3524999618530273,    -17.982500076293945,   -1.747499942779541,    1.0])
    DeclEvent(0x0000, 0, 20,  -55.97999954223633,    98.30000305175781,     -0.5,                  729.0,                 [0.23570217192173004,  0.03928372263908386,   -0.0,                  0.0,                   -0.23570233583450317,  0.039283692836761475,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   36.3641471862793,      -1.6624844074249268,   0.09999999403953552,   1.0])
    DeclEvent(0x0000, 0, 21,  -62.279998779296875,   123.3499984741211,     -0.5,                  729.0,                 [-2.132526049081207e-07, 0.0555555559694767,    0.0,                   0.0,                   -0.3333333134651184,   -3.554210081802012e-08, 0.0,                   0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   41.11664962768555,     3.4600043296813965,    0.10000000149011612,   1.0])

    DeclActor(-21100,  8000,    145620,  1200,    -21100,  9000,    145620,  0x007C, 0,  4,  0x0000)
    DeclActor(-12930,  8000,    127330,  1200,    -12930,  9000,    127330,  0x007C, 0,  5,  0x0000)
    DeclActor(-54270,  0,       137790,  1200,    -54270,  1000,    137790,  0x007C, 0,  13, 0x0000)
    DeclActor(-56750,  0,       105830,  1200,    -56750,  2000,    105830,  0x007C, 0,  12, 0x0000)
    DeclActor(-51520,  0,       60360,   1200,    -51520,  0,       60360,   0x007C, 0,  6,  0x0000)
    DeclActor(-80100,  0,       181140,  1200,    -80100,  0,       181140,  0x007C, 0,  7,  0x0000)

    PlaceName(-6.0, 0.0, -16.989999771118164, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-86.0, 0.0, 229.97999572753906, 0x0000, 0x0000, "矿山镇玛因兹方向")
    PlaceName(-151.4199981689453, 0.0, 100.58000183105469, 0x0000, 0x0000, "月之僧院方向")
    PlaceName(-55.5, 0.0, 107.0, 0x0000, 0x0056, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3])                         # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9

    ScpFunction((
        "Function_0_CB8",          # 00, 0
        "Function_1_CD7",          # 01, 1
        "Function_2_CF6",          # 02, 2
        "Function_3_D3E",          # 03, 3
        "Function_4_139B",         # 04, 4
        "Function_5_149F",         # 05, 5
        "Function_6_1699",         # 06, 6
        "Function_7_16AD",         # 07, 7
        "Function_8_16C1",         # 08, 8
        "Function_9_18E3",         # 09, 9
        "Function_10_1906",        # 0A, 10
        "Function_11_1E8A",        # 0B, 11
        "Function_12_1F77",        # 0C, 12
        "Function_13_1F9B",        # 0D, 13
        "Function_14_1F9C",        # 0E, 14
        "Function_15_2656",        # 0F, 15
        "Function_16_2699",        # 10, 16
        "Function_17_2B83",        # 11, 17
        "Function_18_3766",        # 12, 18
        "Function_19_37F4",        # 13, 19
        "Function_20_392D",        # 14, 20
        "Function_21_3949",        # 15, 21
        "Function_22_3965",        # 16, 22
    ))


    def Function_0_CB8(): pass

    label("Function_0_CB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CD6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_CB8")

    label("loc_CD6")

    Return()

    # Function_0_CB8 end

    def Function_1_CD7(): pass

    label("Function_1_CD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF5")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_CD7")

    label("loc_CF5")

    Return()

    # Function_1_CD7 end

    def Function_2_CF6(): pass

    label("Function_2_CF6")

    OP_16(0x2, 2000, 0, 0, 386, 452, 557974784)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D22")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_D3A")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_D3A")

    Call(0, 9)
    Return()

    # Function_2_CF6 end

    def Function_3_D3E(): pass

    label("Function_3_D3E")

    OP_65(0x2, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D69")
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D86")
    ModifyEventFlags(1, 1, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)

    label("loc_D86")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E00")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -55910, 0, 107440, 315)
    OP_D3(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    OP_66(0x3, 0x1)

    label("loc_E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E84")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -55910, 0, 107440, 315)
    OP_D3(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    OP_66(0x3, 0x1)
    Jump("loc_E89")

    label("loc_E84")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_E89")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11B8")
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jump("loc_11CC")

    label("loc_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CC")
    ClearChrFlags(0x17, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_11CC")

    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128F")
    OP_70(0x0, 0x0)
    Jump("loc_1293")

    label("loc_128F")

    OP_70(0x0, 0x1E)

    label("loc_1293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A6")
    OP_70(0x1, 0x0)
    Jump("loc_12AA")

    label("loc_12A6")

    OP_70(0x1, 0x1E)

    label("loc_12AA")

    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_1310")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -51520, 0, 60360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)
    Jump("loc_1369")

    label("loc_1310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 2)), scpexpr(EXPR_END)), "loc_1369")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -80100, 0, 181140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_1369")

    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_138B")
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)

    label("loc_138B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139A")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_139A")

    Return()

    # Function_3_D3E end

    def Function_4_139B(): pass

    label("Function_4_139B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1470")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 50)
    AddSepith(0x1, 50)
    AddSepith(0x2, 50)
    AddSepith(0x3, 50)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×５０\x01\x07\x02",

            "#57I水之耀晶片×５０\x01\x07\x02",

            "#58I火之耀晶片×５０\x01\x07\x02",

            "#59I风之耀晶片×５０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x104, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_148D")

    label("loc_1470")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_148D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_139B end

    def Function_5_149F(): pass

    label("Function_5_149F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165B")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x74, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1598")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_14F8():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14F8)

    def lambda_1512():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1512)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_A24", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1579"),
        (2, "loc_1588"),
        (1, "loc_1595"),
        (SWITCH_DEFAULT, "loc_1598"),
    )


    label("loc_1579")

    SetScenarioFlags(0x74, 3)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1598")

    label("loc_1588")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1595")

    OP_B7(0x0)
    Return()

    label("loc_1598")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('军用靴', 1)"), scpexpr(EXPR_END)), "loc_15EF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '军用靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1656")

    label("loc_15EF")

    FadeToDark(300, 0, 100)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '军用靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '军用靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1656")

    Jump("loc_168D")

    label("loc_165B")

    FadeToDark(300, 0, 100)

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

    label("loc_168D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_149F end

    def Function_6_1699(): pass

    label("Function_6_1699")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1699 end

    def Function_7_16AD(): pass

    label("Function_7_16AD")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 2)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_16AD end

    def Function_8_16C1(): pass

    label("Function_8_16C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 7)), scpexpr(EXPR_END)), "loc_16CB")
    Return()

    label("loc_16CB")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_1797"),
        (SWITCH_DEFAULT, "loc_17AE"),
    )


    label("loc_1797")

    Sleep(500)
    OP_90(0x0, -35110, 7990, 143660, 89)
    EventEnd(0x5)
    Return()

    label("loc_17AE")

    Battle("BattleInfo_A68", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-35110, 8990, 143660, 0)
    OP_90(0x0, -35110, 7990, 143660, 89)
    OP_90(0x1, -35110, 7990, 143660, 89)
    OP_90(0x2, -35110, 7990, 143660, 89)
    OP_90(0x3, -35110, 7990, 143660, 89)
    OP_90(0x4, -35110, 7990, 143660, 89)
    OP_90(0x5, -35110, 7990, 143660, 89)
    OP_90(0x6, -35110, 7990, 143660, 89)
    OP_90(0x7, -35110, 7990, 143660, 89)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1870"),
        (1, "loc_1873"),
        (SWITCH_DEFAULT, "loc_1876"),
    )


    label("loc_1870")

    EventEnd(0x5)
    Return()

    label("loc_1873")

    OP_B7(0x0)
    Return()

    label("loc_1876")

    EventBegin(0x1)
    SetChrFlags(0x17, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 7)
    OP_29(0x23, 0x4, 0x10)
    OP_29(0x23, 0x4, 0x2)
    OP_29(0x23, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_8_16C1 end

    def Function_9_18E3(): pass

    label("Function_9_18E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1905")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_1905")

    Return()

    # Function_9_18E3 end

    def Function_10_1906(): pass

    label("Function_10_1906")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1920")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E82")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1F")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AC")
    MenuCmd(1, 1, "★克洛斯贝尔·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_19C6")

    label("loc_19AC")

    MenuCmd(1, 1, "　克洛斯贝尔·中央广场")

    label("loc_19C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F6")
    MenuCmd(1, 1, "★克洛斯贝尔·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1A0E")

    label("loc_19F6")

    MenuCmd(1, 1, "　克洛斯贝尔·东出口")

    label("loc_1A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A3E")
    MenuCmd(1, 1, "★克洛斯贝尔·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1A56")

    label("loc_1A3E")

    MenuCmd(1, 1, "　克洛斯贝尔·西出口")

    label("loc_1A56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A86")
    MenuCmd(1, 1, "★克洛斯贝尔·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1A9E")

    label("loc_1A86")

    MenuCmd(1, 1, "　克洛斯贝尔·南出口")

    label("loc_1A9E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACE")
    MenuCmd(1, 1, "★克洛斯贝尔·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_1AE6")

    label("loc_1ACE")

    MenuCmd(1, 1, "　克洛斯贝尔·北出口")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0E")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_1B1E")

    label("loc_1B0E")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B46")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1B56")

    label("loc_1B46")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_1B56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B84")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1B9A")

    label("loc_1B84")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_1B9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC4")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1BD6")

    label("loc_1BC4")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C00")
    MenuCmd(1, 1, "★玛因兹矿山镇")
    MenuCmd(3, 1, 0x9)
    Jump("loc_1C12")

    label("loc_1C00")

    MenuCmd(1, 1, "　玛因兹矿山镇")

    label("loc_1C12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C42")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1C5A")

    label("loc_1C42")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_1C5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C80")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1C8E")

    label("loc_1C80")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_1C8E")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E10")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x3)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D63"),
        (1, "loc_1D71"),
        (2, "loc_1D7F"),
        (3, "loc_1D8D"),
        (4, "loc_1D9B"),
        (5, "loc_1DA9"),
        (6, "loc_1DB7"),
        (7, "loc_1DC5"),
        (8, "loc_1DD3"),
        (9, "loc_1DE1"),
        (10, "loc_1DEF"),
        (11, "loc_1DFD"),
        (SWITCH_DEFAULT, "loc_1E0B"),
    )


    label("loc_1D63")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1D71")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1D7F")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1D8D")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1D9B")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DA9")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DB7")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DC5")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DD3")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DE1")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DEF")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1DFD")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1E0B")

    label("loc_1E0B")

    Jump("loc_1E1A")

    label("loc_1E10")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E1A")

    Jump("loc_1E7D")

    label("loc_1E1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6A")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_1E7D")

    label("loc_1E6A")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E7D")

    Jump("loc_1920")

    label("loc_1E82")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1906 end

    def Function_11_1E8A(): pass

    label("Function_11_1E8A")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -57660, 0, 105090, 225)
    SetChrPos(0x1, -57660, 0, 105090, 225)
    SetChrPos(0x2, -57660, 0, 105090, 225)
    SetChrPos(0x3, -57660, 0, 105090, 225)
    SetChrPos(0x4, -57660, 0, 105090, 225)
    SetChrPos(0x5, -57660, 0, 105090, 225)
    Sleep(1)
    OP_68(-57660, 2500, 105090, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F5C")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_1F62")

    label("loc_1F5C")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_1F62")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1E8A end

    def Function_12_1F77(): pass

    label("Function_12_1F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F8D")
    Call(0, 18)
    Jump("loc_1F9A")

    label("loc_1F8D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 10)

    label("loc_1F9A")

    Return()

    # Function_12_1F77 end

    def Function_13_1F9B(): pass

    label("Function_13_1F9B")

    Return()

    # Function_13_1F9B end

    def Function_14_1F9C(): pass

    label("Function_14_1F9C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x3)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(840)
    OP_68(-3690, 2500, 9580, 0)
    MoveCamera(31, 12, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(17280, 0)
    OP_68(-3690, 2500, 580, 6000)
    SetChrPos(0x101, -1740, 0, -2640, 0)
    SetChrPos(0x102, -620, 0, -3750, 0)
    SetChrPos(0x103, -2390, 0, -4560, 0)
    SetChrPos(0x104, -1370, 0, -5530, 0)
    FadeToBright(1000, 0)
    Sleep(2000)

    def lambda_2077():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2077)

    def lambda_208C():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_208C)

    def lambda_20A1():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_20A1)

    def lambda_20B6():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20B6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_6F(0x1)

    #C0009
    ChrTalk(
        0x104,
        (
            "#0300F隧道吗……\x01",
            "建造得还真牢固啊。\x02\x03",

            "既然建造在这深山里，\x01",
            "显然是为了搬运七耀石吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0010
    ChrTalk(
        0x101,
        (
            "#0004F#5P嗯，应该是吧。\x02\x03",

            "#0000F记得是在克洛斯贝尔\x01",
            "自治州成立前后\x01",
            "建造的吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)
    Sleep(300)

    #C0011
    ChrTalk(
        0x103,
        (
            "#0203F#6P#N这样的话……\x01",
            "那就是七十年以前的建筑啊。\x02\x03",

            "#0200F说到克洛斯贝尔，\x01",
            "好像曾经是以七耀石产地\x01",
            "而闻名的吧……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0012
    ChrTalk(
        0x102,
        (
            "#0103F嗯，帝国和共和国以前\x01",
            "还曾因为它而产生纷争呢。\x02\x03",

            "#0100F虽然现在的开采量没有减少，\x01",
            "仍是非常重要的资源……\x02\x03",

            "但因为开采技术的不断进步，\x01",
            "在其它国家也发现了有潜力的矿脉，\x01",
            "因此就没有以前那么受瞩目了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0003F#5P是啊……\x02\x03",

            "现在提起克洛斯贝尔的话，\x01",
            "最受关注的应该是贸易与金融吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(842, 0, 100, 0)
    Sleep(1000)
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
    Sleep(1000)

    def lambda_23AB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23AB)

    def lambda_23B8():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23B8)

    def lambda_23C5():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23C5)

    def lambda_23D2():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23D2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0014
    ChrTalk(
        0x101,
        "#0001F#5P难不成……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0301F嘁……\x01",
            "有回声啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2429():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2429)
    Sleep(50)

    def lambda_2439():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2439)
    Sleep(50)

    def lambda_2449():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2449)
    WaitChrThread(0x104, 1)

    #C0016
    ChrTalk(
        0x102,
        "#0101F缇欧，能找到吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x103,
        "#0201F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1203, 255, 100, 0)    #voice#Tio
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0xB, 1, 0, 15)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    #C0018
    ChrTalk(
        0x103,
        (
            "#0203F#5P……确定了。\x02\x03",

            "#0201F是从隧道的外面，\x01",
            "前方出口位置传来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#0001F#5P明白了，去看看吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    SetChrPos(0x0, -1200, 0, -1100, 0)
    SetScenarioFlags(0x64, 6)
    OP_29(0x40, 0x1, 0x5)
    OP_E0(0x2)
    Call(0, 9)
    EndChrThread(0xB, 0x1)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_1F9C end

    def Function_15_2656(): pass

    label("Function_15_2656")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_15_2656 end

    def Function_16_2699(): pass

    label("Function_16_2699")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-69470, 1100, 96030, 0)
    MoveCamera(30, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(19500, 2500)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -67560, 0, 98480, 180)
    SetChrPos(0x102, -68860, 0, 97180, 180)
    SetChrPos(0x103, -66110, 0, 98530, 180)
    SetChrPos(0x104, -69340, 0, 98740, 180)
    SetChrPos(0x109, -67000, 0, 100640, 180)

    def lambda_273D():
        OP_95(0xFE, -69630, 0, 96020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_273D)

    def lambda_2757():
        OP_95(0xFE, -71190, 0, 94710, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2757)

    def lambda_2771():
        OP_95(0xFE, -68070, 0, 96430, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2771)

    def lambda_278B():
        OP_95(0xFE, -70710, 0, 97390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_278B)

    def lambda_27A5():
        OP_95(0xFE, -68650, 0, 99180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_27A5)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0xB4, 0x12C)
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0xB4, 0x1F4)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0xB4, 0x12C)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0xB4, 0x1F4)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0xB4, 0x12C)
    OP_0D()
    OP_6F(0x10)
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2926")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_2867")

    #C0020
    ChrTalk(
        0x101,
        (
            "#0003F#5P呼……\x01",
            "一下就到了啊。\x02\x03",

            "#0001F记得这里就是通往\x01",
            "山道尽头那个遗迹的岔路吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_2867")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_28CB")

    #C0021
    ChrTalk(
        0x101,
        (
            "#0003F#5P呼……\x01",
            "一下就到了啊。\x02\x03",

            "#0001F这边果然就是\x01",
            "通往山道尽头那个\x01",
            "遗迹的路吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2921")

    label("loc_28CB")


    #C0022
    ChrTalk(
        0x101,
        (
            "#0003F#5P呼……\x01",
            "一下子就到了。\x02\x03",

            "#0001F莫非这边就是\x01",
            "通往山道尽头那个\x01",
            "遗迹的路吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2921")

    Jump("loc_2A5B")

    label("loc_2926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_2991")

    #C0023
    ChrTalk(
        0x101,
        (
            "#0006F#5P不知不觉\x01",
            "就走到这里来了……\x02\x03",

            "#0001F记得这里就是通往\x01",
            "山道尽头那个遗迹的岔路吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 7)), scpexpr(EXPR_END)), "loc_29FF")

    #C0024
    ChrTalk(
        0x101,
        (
            "#0006F#5P不知不觉\x01",
            "就走到这里来了……\x02\x03",

            "#0001F这边果然就是\x01",
            "就是通往山道尽头那个\x01",
            "遗迹的路吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A5B")

    label("loc_29FF")


    #C0025
    ChrTalk(
        0x101,
        (
            "#0006F#5P不知不觉\x01",
            "就走到这里来了……\x02\x03",

            "#0001F莫非这边就是\x01",
            "通往山道尽头那个\x01",
            "遗迹的路吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A5B")


    #C0026
    ChrTalk(
        0x109,
        (
            "#0503F#5P嗯，是啊。\x02\x03",

            "#0500F我想，接下来的道路\x01",
            "还是徒步行进比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0300F#5P嗯，如果准备好了，\x01",
            "就马上过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        "#0204F#5P是呀。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0108F#5P（……唉………\x01",
            "  有幽灵出没的遗迹……）\x02\x03",

            "#0113F（不、不……！\x01",
            "  那种东西是不存在的……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -70200, 0, 98000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xC0, 2)
    OP_E0(0x2)
    Call(0, 9)
    EventEnd(0x5)
    Return()

    # Function_16_2699 end

    def Function_17_2B83(): pass

    label("Function_17_2B83")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    LoadChrToIndex("apl/ch50109.itc", 0x1F)
    SoundLoad(806)
    OP_68(-61260, 2300, 105970, 0)
    MoveCamera(76, 9, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17150, 0)
    SetChrPos(0x101, -64190, 0, 101320, 45)
    SetChrPos(0x102, -65650, 0, 102220, 45)
    SetChrPos(0x103, -66810, 0, 100330, 45)
    SetChrPos(0x104, -64840, 0, 100030, 45)
    SetChrPos(0x109, -62860, 0, 103720, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_2C46():
        OP_95(0xFE, -61100, 0, 104820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C46)

    def lambda_2C60():
        OP_95(0xFE, -62740, 0, 105360, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C60)

    def lambda_2C7A():
        OP_95(0xFE, -63850, 0, 103990, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C7A)

    def lambda_2C94():
        OP_95(0xFE, -62330, 0, 103250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C94)

    def lambda_2CAE():
        OP_95(0xFE, -59960, 0, 107020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CAE)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -55910, 0, 107440, 315)
    OP_D3(0x9, 0x0, 0x4CE78, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    FadeToBright(1000, 0)
    OP_68(-61260, 1300, 105970, 3000)
    OP_6F(0x79)
    OP_0D()
    WaitChrThread(0x109, 1)
    OP_93(0x109, 0xE1, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0030
    ChrTalk(
        0x109,
        (
            "#0502F#5P好了……\x01",
            "接下来要怎么办？\x02\x03",

            "反正还有时间，\x01",
            "不管想去哪里，都可以送你们过去哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0002F#12P嗯～这个嘛。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0032
    ChrTalk(
        0x102,
        (
            "#0109F#6P呵呵，机会难得，\x01",
            "就恭敬不如从命了吧。\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        "#0005F#11P哦……有通讯。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0034
    ChrTalk(
        0x104,
        (
            "#0300F#12P哈哈，打来的\x01",
            "时机还真巧啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x190)
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(400)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    #Sound(1084, 255, 90, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0035
    AnonymousTalk(
        0x101,
        (
            "#0000F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2083, 255, 100, 0)    #voice#Fran
    #Sleep(1000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德警官。\x02\x03"      #line#50
            "那个……请问各位\x01",
            "现在在哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 4)), scpexpr(EXPR_END)), "loc_30A4")
    SetMessageWindowPos(90, 130, -1, -1)

    #A0037
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F哦，在玛因兹山道\x01",
            "途中的隧道里……\x02\x03",

            "#0002F刚刚才和你姐姐把\x01",
            "那个遗迹调查完毕呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，辛苦了。\x02\x03",

            "调查已经顺利结束了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_316D")

    label("loc_30A4")

    SetMessageWindowPos(90, 130, -1, -1)

    #A0039
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F嗯，在玛因兹山道\x01",
            "途中的隧道里哦。\x02\x03",

            "#0000F其实，刚和你姐姐一起\x01",
            "调查过这里的某个遗迹……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，了解。\x01",
            "我之前也听姐姐说过的。\x02\x03",

            "调查已经顺利结束了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_316D")

    SetMessageWindowPos(90, 130, -1, -1)

    #A0041
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F嗯，已经告一段落啦。\x02\x03",

            "#0000F找你姐姐有事吗？\x01",
            "我可以叫她来接……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊哈哈，不是啦～\x02\x03",

            "那样的话，我就会直接\x01",
            "拨打姐姐的艾尼格玛了嘛。\x02\x03",

            "其实，是接到了联络，\x01",
            "有人想找罗伊德警官与大家咨询一些情况。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0043
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F咨询……是市民吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不，是玛因兹\x01",
            "的镇长先生……\x02\x03",

            "说是有事想与\x01",
            "罗伊德警官和各位商量。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0045
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000F哦……\x01",
            "这还真少见啊。\x02\x03",

            "要商量什么事情呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，好像是说矿山镇的某个镇民\x01",
            "在来到克洛斯贝尔市以后，\x01",
            "过了好几天都没有回去……\x02\x03",

            "大致内容就是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0047
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F原来如此……\x01",
            "确实是有点令人在意啊。\x02\x03",

            "#0000F──明白了。\x01",
            "这里离玛因兹也很近，\x01",
            "我们立刻就去拜访镇长吧。\x02\x03",

            "正好你姐姐\x01",
            "说可以送我们。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，不用客气，\x01",
            "尽管使唤她吧。\x02\x03",

            "那么，我就这样\x01",
            "转告对方啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0049
    ChrTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0500F#5P是芙兰吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0012F#11P嗯，不过说的只是\x01",
            "有关支援科工作的事情。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3554():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3554)
    Sleep(50)
    TurnDirection(0x101, 0x103, 500)
    WaitChrThread(0x103, 1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将芙兰的联络内容简单说明了一下。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    #C0052
    ChrTalk(
        0x102,
        (
            "#0105F#6P原来如此……\x01",
            "是玛因兹的比克森镇长的委托啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0203F#12P前往市里之后，\x01",
            "好几天都没回去的镇民吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#0300F#12P这里离矿山镇很近，\x01",
            "我们还是过去直接听他说比较快吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#0000F#5P嗯，我也这么想。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0056
    ChrTalk(
        0x101,
        (
            "#0002F#11P那么，上士，\x01",
            "能送我们去矿山镇吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0057
    ChrTalk(
        0x109,
        "#0502F#5P嗯，小事一桩！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_37()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrPos(0x0, -64000, 0, 105500, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_E0(0x2)
    OP_66(0x3, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0xC1, 0)
    OP_29(0x49, 0x4, 0x10)
    OP_29(0x4A, 0x4, 0x2)
    OP_29(0x4A, 0x1, 0x0)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 4, 0x80)
    Sleep(500)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_17_2B83 end

    def Function_18_3766(): pass

    label("Function_18_3766")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要乘坐警备队的车辆移动吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "矿山镇玛因兹·巴士站\x01",      # 0
            "放弃\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37EC")
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 19)
    ClearMapFlags(0x8000000)
    SetScenarioFlags(0x5C, 2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()

    label("loc_37EC")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_18_3766 end

    def Function_19_37F4(): pass

    label("Function_19_37F4")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-63070, 1200, 112420, 0)
    MoveCamera(28, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16140, 0)
    OP_68(-63070, 3800, 112420, 4000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x3, 0x400)
    SetChrFlags(0x9, 0x8000)
    OP_78(0x3, 0x9)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetChrPos(0x9, -61970, 0, 110190, 0)
    OP_D3(0x9, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x3, 0x1E)
    OP_70(0x3, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_E0(0x1)
    FadeToBright(1000, 0)
    Sound(469, 0, 100, 0)
    Sound(488, 0, 70, 0)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)

    def lambda_3901():
        OP_9B(0x0, 0xFE, 0x0, 0x9C40, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3901)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    EndChrThread(0x9, 0x1)
    OP_6F(0x1)
    Return()

    # Function_19_37F4 end

    def Function_20_392D(): pass

    label("Function_20_392D")

    EventBegin(0x1)
    Call(0, 22)
    Sleep(50)
    SetChrPos(0x0, -58910, 0, 103870, 316)
    EventEnd(0x4)
    Return()

    # Function_20_392D end

    def Function_21_3949(): pass

    label("Function_21_3949")

    EventBegin(0x1)
    Call(0, 22)
    Sleep(50)
    SetChrPos(0x0, -62130, 0, 119470, 181)
    EventEnd(0x4)
    Return()

    # Function_21_3949 end

    def Function_22_3965(): pass

    label("Function_22_3965")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C2")

    #C0059
    ChrTalk(
        0x101,
        (
            "#0005F哦……\x02\x03",

            "#0000F这次还是坐警备队\x01",
            "的车辆过去吧。\x01",
            "那样应该比较快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9E")

    label("loc_39C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A50")

    #C0060
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x02\x03",

            "#0000F诺艾尔上士，能麻烦你\x01",
            "用警备队的车辆送我们过去吗。\x01",
            "那样应该比较快。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        (
            "#0500F啊，是哦。\x01",
            "明白了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A9E")

    label("loc_3A50")


    #C0062
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x02\x03",

            "#0000F这次不坐警备队\x01",
            "的车辆过去吗？\x01",
            "那样的话应该会比较快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A9E")

    Return()

    # Function_22_3965 end

    SaveToFile()

Try(main)
