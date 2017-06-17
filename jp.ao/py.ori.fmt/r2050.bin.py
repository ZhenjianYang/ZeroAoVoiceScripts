from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2050.bin",                # FileName
        "r2050",                    # MapName
        "r2050",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2050", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x15,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 5, 0, 6],
    )

    BuildStringList((
        "r2050",                  # 0
        "マダラマーダー",         # 1
        "マダラマーダー",         # 2
        "鉄鋼ドリュー",           # 3
        "鉄鋼ドリュー",           # 4
        "アカマダラマーダー",     # 5
        " ",                      # 6
        "警備隊員",               # 7
        "警備隊員",               # 8
        "猟兵",                   # 9
        "猟兵",                   # 10
        "猟兵",                   # 11
        "猟兵",                   # 12
        "猟兵",                   # 13
        "シャーリィ",             # 14
        "装甲車",                 # 15
        "装甲車",                 # 16
        "装甲車",                 # 17
        "br2040",                 # 18
        "br2050",                 # 19
        "br2050",                 # 20
        "br2050",                 # 21
        "br2040",                 # 22
        "br2050",                 # 23
        "br2040",                 # 24
        "br2040",                 # 25
        "br2040",                 # 26
        "br2040",                 # 27
        "クロスベル市方面",       # 28
        "鉱山町マインツ方面",     # 29
        "月の僧院方面",           # 30
    ))

    ATBonus("ATBonus_668", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_688", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4C49", 0,   4,   0,   4,   2,   2,   2)
    Sepith("Sepith_4C39", 5,   2,   0,   1,   2,   3,   2)
    Sepith("Sepith_4C41", 4,   0,   4,   0,   4,   1,   3)
    Sepith("Sepith_4C31", 0,   0,   0,   5,   5,   5,   3)
    Sepith("Sepith_4C29", 11,  3,   6,   4,   6,   10,  8)

    MonsterBattlePostion("MonsterBattlePostion_6C8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_72C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_730", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_734", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_738", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_73C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_740", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_744", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 2, 13, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_9A0", 0x0000, 53, 6, 60, 10, 1, 40, 0, "br2050", "Sepith_4C49", 30, 40, 20, 10,
        (
            ("ms69100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms69100.dat", "ms69100.dat", "ms69100.dat", "ms69100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_810", 0x0000, 53, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_4C39", 30, 40, 20, 10,
        (
            ("ms68100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms68100.dat", "ms68100.dat", "ms71700.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x0000, 53, 6, 60, 10, 1, 50, 0, "br2050", "Sepith_4C41", 30, 40, 20, 10,
        (
            ("ms72800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms72800.dat", "ms68100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms72800.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_748", 0x0000, 53, 6, 60, 10, 1, 30, 0, "br2040", "Sepith_4C31", 30, 40, 20, 10,
        (
            ("ms71700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms71700.dat", "ms71700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms71700.dat", "ms71700.dat", "ms65900.dat", "ms71700.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
        )
    )

    BattleInfo(
        "BattleInfo_B04", 0x0000, 82, 6, 45, 6, 1, 30, 0, "br2050", "Sepith_4C29", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C8", "MonsterBattlePostion_728", "ed7450", "ed7453", "ATBonus_668"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C28", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms79501.dat", "ms79501.dat", "ms79501.dat", "ms79501.dat", "ms79501.dat", "ms79501.dat", 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7451", "ed7453", "ATBonus_688"),
            (),
            (),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_C6C", 0x0000, 50, 6, 45, 0, 1, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "ms72800.dat", "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7451", "ed7453", "ATBonus_668"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BA0", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "ms68100.dat", "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7453", "ed7453", "ATBonus_668"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BE4", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, "MonsterBattlePostion_6A8", "MonsterBattlePostion_728", "ed7453", "ed7453", "ATBonus_668"),
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
        "monster/ch79550.itc",               # 1A
        "monster/ch79551.itc",               # 1B
    ))

    DeclNpc(-21340,  0,       45409,   270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-24100,  8000,    147860,  270,  484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-21340,  0,       45409,   270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-24100,  8000,    147860,  270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-12930,  8500,    127330,  0,    484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    192,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-11790,  32470,   0,       0x1010000,    "BattleInfo_9A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-48260,  51700,   0,       0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-58330,  102750,  0,       0x1010000,    "BattleInfo_8D8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-103440, 89080,   -14000,  0x1010000,    "BattleInfo_748", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-57310,  146680,  0,       0x1010000,    "BattleInfo_9A0", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-25730,  141040,  8000,    0x1010000,    "BattleInfo_748", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-83270,  179260,  0,       0x1010000,    "BattleInfo_810", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-33350,  41540,   0,       0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-62470,  119400,  0,       0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-82940,  170350,  0,       0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-74490,  81330,   -5980,   0x1010000,    "BattleInfo_B04", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-22720,  140300,  7990,    0x185010E,    "BattleInfo_C28", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0040, 0, 16,  -22.719999313354492,   140.3000030517578,     7.989999771118164,     16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   2.8399999141693115,    -17.537500381469727,   -1.997499942779541,    1.0])
    DeclEvent(0x0000, 0, 22,  -70.0,                 94.33999633789062,     -1.0800000429153442,   506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.6666669845581055,    -31.446666717529297,   0.2160000056028366,    1.0])

    DeclActor(-21100,  8000,    145620,  1200,    -21100,  9000,    145620,  0x007C, 0,  7,  0x0000)
    DeclActor(-12930,  8000,    127330,  1200,    -12930,  9000,    127330,  0x007C, 0,  8,  0x0000)
    DeclActor(-118840, -9000,   105750,  1200,    -118840, -8000,   105750,  0x007C, 0,  9,  0x0000)
    DeclActor(-21340,  0,       45410,   1200,    -21340,  0,       45410,   0x007C, 0,  10, 0x0000)
    DeclActor(-24100,  8000,    147860,  1200,    -24100,  8000,    147860,  0x007C, 0,  11, 0x0000)
    DeclActor(-55280,  0,       138630,  1200,    -55280,  2000,    138630,  0x007C, 0,  14, 0x0000)
    DeclActor(-54000,  0,       138000,  1200,    -54000,  2000,    138000,  0x007C, 0,  14, 0x0000)

    PlaceName(-6.0, 0.0, -16.989999771118164, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-86.0, 0.0, 229.97999572753906, 0x0000, 0x0000, "鉱山町マインツ方面")
    PlaceName(-151.4199981689453, 0.0, 100.58000183105469, 0x0000, 0x0000, "月の僧院方面")

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
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 10
    ChipFrameInfo(899, 0, [0, 1, 2, 3, 4])                       # 11

    ScpFunction((
        "Function_0_D9C",          # 00, 0
        "Function_1_DBB",          # 01, 1
        "Function_2_DDA",          # 02, 2
        "Function_3_DF9",          # 03, 3
        "Function_4_E16",          # 04, 4
        "Function_5_135B",         # 05, 5
        "Function_6_18B1",         # 06, 6
        "Function_7_1FD8",         # 07, 7
        "Function_8_2129",         # 08, 8
        "Function_9_2340",         # 09, 9
        "Function_10_24A7",        # 0A, 10
        "Function_11_2805",        # 0B, 11
        "Function_12_2B63",        # 0C, 12
        "Function_13_2B86",        # 0D, 13
        "Function_14_2B8A",        # 0E, 14
        "Function_15_2ECD",        # 0F, 15
        "Function_16_2F61",        # 10, 16
        "Function_17_31CD",        # 11, 17
        "Function_18_361A",        # 12, 18
        "Function_19_3A1C",        # 13, 19
        "Function_20_3F23",        # 14, 20
        "Function_21_4887",        # 15, 21
        "Function_22_48C9",        # 16, 22
    ))


    def Function_0_D9C(): pass

    label("Function_0_D9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBA")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_D9C")

    label("loc_DBA")

    Return()

    # Function_0_D9C end

    def Function_1_DBB(): pass

    label("Function_1_DBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DBB")

    label("loc_DD9")

    Return()

    # Function_1_DBB end

    def Function_2_DDA(): pass

    label("Function_2_DDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF8")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_DDA")

    label("loc_DF8")

    Return()

    # Function_2_DDA end

    def Function_3_DF9(): pass

    label("Function_3_DF9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E15")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_3_DF9")

    label("loc_E15")

    Return()

    # Function_3_DF9 end

    def Function_4_E16(): pass

    label("Function_4_E16")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_135A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E77")
    SetScenarioFlags(0x0, 1)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -88800, -1000, 192450, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_E77")

    SetScenarioFlags(0x0, 1)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x5, 0x800000)
    OP_C4(0x0, 0x1, 0x1, 0x0)

    label("loc_E8D")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EE6")
    SetScenarioFlags(0x0, 2)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -90600, -1000, 184350, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_EE6")

    SetScenarioFlags(0x0, 2)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x6, 0x800000)
    OP_C4(0x1, 0x1, 0x1, 0x0)

    label("loc_EFC")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F55")
    SetScenarioFlags(0x0, 3)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -85120, -1000, 181010, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_F55")

    SetScenarioFlags(0x0, 3)
    SetMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x7, 0x800000)
    OP_C4(0x2, 0x1, 0x1, 0x0)

    label("loc_F6B")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_FDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FC4")
    SetScenarioFlags(0x0, 4)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -79990, -1000, 163480, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_FC4")

    SetScenarioFlags(0x0, 4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x800000)
    OP_C4(0x3, 0x1, 0x1, 0x0)

    label("loc_FDA")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1049")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1033")
    SetScenarioFlags(0x0, 5)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -66570, -1000, 155940, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_1033")

    SetScenarioFlags(0x0, 5)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x800000)
    OP_C4(0x4, 0x1, 0x1, 0x0)

    label("loc_1049")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10A2")
    SetScenarioFlags(0x0, 6)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -70370, -1000, 145190, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_10A2")

    SetScenarioFlags(0x0, 6)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xA, 0x800000)
    OP_C4(0x5, 0x1, 0x1, 0x0)

    label("loc_10B8")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1111")
    SetScenarioFlags(0x0, 7)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -62710, -1000, 124440, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_1111")

    SetScenarioFlags(0x0, 7)
    SetMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xB, 0x800000)
    OP_C4(0x6, 0x1, 0x1, 0x0)

    label("loc_1127")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1180")
    SetScenarioFlags(0x1, 0)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -61700, -1000, 106350, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_1180")

    SetScenarioFlags(0x1, 0)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x800000)
    OP_C4(0x7, 0x1, 0x1, 0x0)

    label("loc_1196")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11EF")
    SetScenarioFlags(0x1, 1)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -54430, -1000, 89830, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_11EF")

    SetScenarioFlags(0x1, 1)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xD, 0x800000)
    OP_C4(0x8, 0x1, 0x1, 0x0)

    label("loc_1205")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1274")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125E")
    SetScenarioFlags(0x1, 2)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -54220, -1000, 58200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_125E")

    SetScenarioFlags(0x1, 2)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xE, 0x800000)
    OP_C4(0x9, 0x1, 0x1, 0x0)

    label("loc_1274")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CD")
    SetScenarioFlags(0x1, 3)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -32170, -1000, 41830, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_12CD")

    SetScenarioFlags(0x1, 3)
    SetMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0xF, 0x800000)
    OP_C4(0xA, 0x1, 0x1, 0x0)

    label("loc_12E3")

    Sleep(15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1352")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_133C")
    SetScenarioFlags(0x1, 4)
    PlayEffect(0xA, 0xFF, 0xFF, 0x20, -5660, -1000, 24900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)

    label("loc_133C")

    SetScenarioFlags(0x1, 4)
    SetMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x10, 0x800000)
    OP_C4(0xB, 0x1, 0x1, 0x0)

    label("loc_1352")

    Sleep(15)
    Jump("Function_4_E16")

    label("loc_135A")

    Return()

    # Function_4_E16 end

    def Function_5_135B(): pass

    label("Function_5_135B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_136F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)
    Jump("loc_137E")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_137E")
    ClearScenarioFlags(0x22, 1)
    Event(0, 18)

    label("loc_137E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1394")
    SetMapFlags(0x10000000)
    Event(0, 20)

    label("loc_1394")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1838")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1421")
    SetScenarioFlags(0x38, 0)

    label("loc_1421")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1437")
    SetScenarioFlags(0x38, 1)

    label("loc_1437")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144D")
    SetScenarioFlags(0x38, 2)

    label("loc_144D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1463")
    SetScenarioFlags(0x38, 3)

    label("loc_1463")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1479")
    SetScenarioFlags(0x38, 4)

    label("loc_1479")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148F")
    SetScenarioFlags(0x38, 5)

    label("loc_148F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A5")
    SetScenarioFlags(0x38, 6)

    label("loc_14A5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BB")
    SetScenarioFlags(0x38, 7)

    label("loc_14BB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D1")
    SetScenarioFlags(0x39, 0)

    label("loc_14D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E7")
    SetScenarioFlags(0x39, 1)

    label("loc_14E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FD")
    SetScenarioFlags(0x39, 2)

    label("loc_14FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1513")
    SetScenarioFlags(0x39, 3)

    label("loc_1513")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1529")
    SetScenarioFlags(0x39, 4)

    label("loc_1529")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153F")
    SetScenarioFlags(0x39, 5)

    label("loc_153F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1555")
    SetScenarioFlags(0x39, 6)

    label("loc_1555")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156B")
    SetScenarioFlags(0x39, 7)

    label("loc_156B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1581")
    SetScenarioFlags(0x3A, 0)

    label("loc_1581")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1597")
    SetScenarioFlags(0x3A, 1)

    label("loc_1597")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AD")
    SetScenarioFlags(0x3A, 2)

    label("loc_15AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C3")
    SetScenarioFlags(0x3A, 3)

    label("loc_15C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D9")
    SetScenarioFlags(0x3A, 4)

    label("loc_15D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EF")
    SetScenarioFlags(0x3A, 5)

    label("loc_15EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1605")
    SetScenarioFlags(0x3A, 6)

    label("loc_1605")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161B")
    SetScenarioFlags(0x3A, 7)

    label("loc_161B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1631")
    SetScenarioFlags(0x3B, 0)

    label("loc_1631")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1647")
    SetScenarioFlags(0x3B, 1)

    label("loc_1647")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165D")
    SetScenarioFlags(0x3B, 2)

    label("loc_165D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1673")
    SetScenarioFlags(0x3B, 3)

    label("loc_1673")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1689")
    SetScenarioFlags(0x3B, 4)

    label("loc_1689")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169F")
    SetScenarioFlags(0x3B, 5)

    label("loc_169F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16B5")
    SetScenarioFlags(0x3B, 6)

    label("loc_16B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CB")
    SetScenarioFlags(0x3B, 7)

    label("loc_16CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E1")
    SetScenarioFlags(0x3D, 5)

    label("loc_16E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F7")
    SetScenarioFlags(0x3D, 6)

    label("loc_16F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170D")
    SetScenarioFlags(0x3D, 7)

    label("loc_170D")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1748")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1838")

    label("loc_1748")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_176B")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1838")

    label("loc_176B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178E")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1838")

    label("loc_178E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B1")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1838")

    label("loc_17B1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D4")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1838")

    label("loc_17D4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1838")

    label("loc_17F7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181A")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1838")

    label("loc_181A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1838")
    SetScenarioFlags(0x3C, 7)

    label("loc_1838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186A")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_186A")
    SetChrPos(0x0, -56050, 0, 138420, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 15)

    label("loc_186A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_189D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189D")
    SetChrPos(0x0, -54000, 0, 138000, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_189D")

    Call(0, 12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18B0")
    OP_E2(0x1)

    label("loc_18B0")

    Return()

    # Function_5_135B end

    def Function_6_18B1(): pass

    label("Function_6_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_18C3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_18EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E5")
    ClearChrFlags(0x24, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x24, 0x8000)

    label("loc_18E5")

    ClearChrBattleFlags(0x24, 0x8000)
    Jump("loc_18F9")

    label("loc_18EF")

    SetChrFlags(0x24, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_18F9")

    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MiniGame(0x2F, 0x5, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8D")
    OP_70(0x0, 0x0)
    Jump("loc_1E91")

    label("loc_1E8D")

    OP_70(0x0, 0x1E)

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA4")
    OP_70(0x1, 0x0)
    Jump("loc_1EA8")

    label("loc_1EA4")

    OP_70(0x1, 0x1E)

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBB")
    OP_70(0x2, 0x0)
    Jump("loc_1EBF")

    label("loc_1EBB")

    OP_70(0x2, 0x1E)

    label("loc_1EBF")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F20")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -21340, 0, 45410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1F20")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F6C")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -24100, 8000, 147860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA1")
    LoadEffect(0xA, "map/mpr2050.eff")
    LoadEffect(0x9, "map/mpcave2.eff")
    Call(0, 19)

    label("loc_1FA1")

    OP_1C(0x0, 0x15, 0x0, 0x32, 0x0, 0xD, 0x0, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FC4")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FD7")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1FD7")

    Return()

    # Function_6_18B1 end

    def Function_7_1FD8(): pass

    label("Function_7_1FD8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D8")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x46, 1)"), scpexpr(EXPR_END)), "loc_2061")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_20D3")

    label("loc_2061")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_20D3")

    Jump("loc_211D")

    label("loc_20D8")

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

    label("loc_211D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1FD8 end

    def Function_8_2129(): pass

    label("Function_8_2129")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22FA")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2228")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_2186():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2186)

    def lambda_21A0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_21A0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_C6C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_2209"),
        (2, "loc_2218"),
        (1, "loc_2225"),
        (SWITCH_DEFAULT, "loc_2228"),
    )


    label("loc_2209")

    SetScenarioFlags(0x216, 2)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_2228")

    label("loc_2218")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2225")

    OP_B9(0x0)
    Return()

    label("loc_2228")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8C, 1)"), scpexpr(EXPR_END)), "loc_2285")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E7, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_22F5")

    label("loc_2285")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_22F5")

    Jump("loc_2334")

    label("loc_22FA")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_2334")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_2129 end

    def Function_9_2340(): pass

    label("Function_9_2340")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 60)
    AddSepith(0x1, 60)
    AddSepith(0x2, 60)
    AddSepith(0x3, 60)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×６０\x01\x07\x02",

            "#57I水のセピス×６０\x01\x07\x02",

            "#58I火のセピス×６０\x01\x07\x02",

            "#59I風のセピス×６０\x01\x07\x02",

            "#60I時のセピス×６０\x01\x07\x02",

            "#61I空のセピス×６０\x01\x07\x02",

            "#62I幻のセピス×６０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E7, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_2495")

    label("loc_2470")


    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_2495")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_2340 end

    def Function_10_24A7(): pass

    label("Function_10_24A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_265F")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_2640")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0010
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_263B")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2638")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2561():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2561)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0011
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
    Battle("BattleInfo_BA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2633")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_261A")
    Call(1, 5)
    Jump("loc_2633")

    label("loc_261A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2630")
    Call(1, 4)
    Jump("loc_2633")

    label("loc_2630")

    Call(1, 3)

    label("loc_2633")

    Jump("loc_263B")

    label("loc_2638")

    Call(1, 1)

    label("loc_263B")

    Jump("loc_2656")

    label("loc_2640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2656")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2656")

    TalkEnd(0xFF)
    Return()

    label("loc_265F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_27EA")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0012
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27E5")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_27E2")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_270B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_270B)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0013
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
    Battle("BattleInfo_BE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27DD")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27C4")
    Call(1, 5)
    Jump("loc_27DD")

    label("loc_27C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_27DA")
    Call(1, 4)
    Jump("loc_27DD")

    label("loc_27DA")

    Call(1, 3)

    label("loc_27DD")

    Jump("loc_27E5")

    label("loc_27E2")

    Call(1, 1)

    label("loc_27E5")

    Jump("loc_2800")

    label("loc_27EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_2800")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2800")

    TalkEnd(0xFF)
    Return()

    # Function_10_24A7 end

    def Function_11_2805(): pass

    label("Function_11_2805")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_29BD")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_299E")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0014
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2999")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2996")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_28BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_28BF)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0015
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
    Battle("BattleInfo_BA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2991")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2978")
    Call(1, 5)
    Jump("loc_2991")

    label("loc_2978")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_298E")
    Call(1, 4)
    Jump("loc_2991")

    label("loc_298E")

    Call(1, 3)

    label("loc_2991")

    Jump("loc_2999")

    label("loc_2996")

    Call(1, 1)

    label("loc_2999")

    Jump("loc_29B4")

    label("loc_299E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_29B4")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_29B4")

    TalkEnd(0xFF)
    Return()

    label("loc_29BD")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_2B48")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0016
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B43")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2B40")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2A69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A69)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0017
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
    Battle("BattleInfo_BE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3B")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B22")
    Call(1, 5)
    Jump("loc_2B3B")

    label("loc_2B22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2B38")
    Call(1, 4)
    Jump("loc_2B3B")

    label("loc_2B38")

    Call(1, 3)

    label("loc_2B3B")

    Jump("loc_2B43")

    label("loc_2B40")

    Call(1, 1)

    label("loc_2B43")

    Jump("loc_2B5E")

    label("loc_2B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2B5E")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2B5E")

    TalkEnd(0xFF)
    Return()

    # Function_11_2805 end

    def Function_12_2B63(): pass

    label("Function_12_2B63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B85")
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)

    label("loc_2B85")

    Return()

    # Function_12_2B63 end

    def Function_13_2B86(): pass

    label("Function_13_2B86")

    Call(1, 6)
    Return()

    # Function_13_2B86 end

    def Function_14_2B8A(): pass

    label("Function_14_2B8A")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BBC")
    SetScenarioFlags(0x31, 2)

    label("loc_2BBC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2C02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2BFC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BF1")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2BF7")

    label("loc_2BF1")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2BF7")

    Jump("loc_2C02")

    label("loc_2BFC")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_2C02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_2C7B")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C5B"),
        (SWITCH_DEFAULT, "loc_2C6C"),
    )


    label("loc_2C5B")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2C76")

    label("loc_2C6C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C76")

    Jump("loc_2EBA")

    label("loc_2C7B")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2CAF")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_2CAF")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CE3"),
        (1, "loc_2DE7"),
        (2, "loc_2E78"),
        (SWITCH_DEFAULT, "loc_2EB0"),
    )


    label("loc_2CE3")

    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D14")
    OP_70(0x3, 0x12C)
    OP_71(0x3, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2D24")

    label("loc_2D14")

    OP_70(0x3, 0xF0)
    OP_71(0x3, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2D24")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D7A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D7A")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D9D")
    Sound(461, 0, 100, 0)

    label("loc_2D9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DBD")
    OP_70(0x3, 0x14A)
    OP_71(0x3, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2DCD")

    label("loc_2DBD")

    OP_70(0x3, 0x10E)
    OP_71(0x3, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2DCD")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x3, "light", 0x1, 0x1)
    OP_70(0x3, 0x0)
    Jump("loc_2C02")

    label("loc_2DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2E59")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2E1C")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2E34")

    label("loc_2E1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E2F")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2E34")

    label("loc_2E2F")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2E34")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E73")

    label("loc_2E59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2E69")
    OP_AF(0xFB)
    Jump("loc_2E73")

    label("loc_2E69")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E73")

    Jump("loc_2EBA")

    label("loc_2E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E91")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2EAB")

    label("loc_2E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2EA1")
    OP_AF(0xFB)
    Jump("loc_2EAB")

    label("loc_2EA1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EAB")

    Jump("loc_2EBA")

    label("loc_2EB0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2EBA")

    Jump("loc_2C02")

    label("loc_2EBF")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_2B8A end

    def Function_15_2ECD(): pass

    label("Function_15_2ECD")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2F28")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F1D")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_2F23")

    label("loc_2F1D")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_2F23")

    Jump("loc_2F4C")

    label("loc_2F28")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F46")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_2F4C")

    label("loc_2F46")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_2F4C")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_2ECD end

    def Function_16_2F61(): pass

    label("Function_16_2F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 4)), scpexpr(EXPR_END)), "loc_2F6B")
    Return()

    label("loc_2F6B")

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

    #A0018
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_304D"),
        (SWITCH_DEFAULT, "loc_3066"),
    )


    label("loc_304D")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -27610, 7990, 141110, 270)
    EventEnd(0x5)
    Return()

    label("loc_3066")

    Battle("BattleInfo_C28", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-27610, 8990, 141110, 0)
    OP_90(0x0, -27610, 7990, 141110, 270)
    OP_90(0x1, -27610, 7990, 141110, 270)
    OP_90(0x2, -27610, 7990, 141110, 270)
    OP_90(0x3, -27610, 7990, 141110, 270)
    OP_90(0x4, -27610, 7990, 141110, 270)
    OP_90(0x5, -27610, 7990, 141110, 270)
    OP_90(0x6, -27610, 7990, 141110, 270)
    OP_90(0x7, -27610, 7990, 141110, 270)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3128"),
        (1, "loc_312D"),
        (SWITCH_DEFAULT, "loc_3130"),
    )


    label("loc_3128")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_312D")

    OP_B9(0x0)
    Return()

    label("loc_3130")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x24, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21D, 4)
    OP_29(0x98, 0x4, 0x2)
    OP_29(0x98, 0x4, 0x10)
    OP_29(0x98, 0x1, 0x0)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_16_2F61 end

    def Function_17_31CD(): pass

    label("Function_17_31CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50515.itc", 0x1E)
    LoadEffect(0x0, "event/ev14001.eff")
    SoundLoad(868)
    SoundLoad(863)
    SoundLoad(864)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x16, 0x80)
    OP_78(0x11, 0x16)
    OP_49()
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_74(0x11, 0x1E)
    OP_71(0x11, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x12, 0x17)
    OP_49()
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x13, 0x18)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x3D, 0x78, 0x0, 0x20)
    OP_7D(0xFF, 0xA0, 0x96, 0x0, 0x0)
    SetChrPos(0x16, -89850, 0, 202000, 270)
    SetChrPos(0xE, -90000, 0, 206650, 0)
    PlayEffect(0x0, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xF, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-90100, 1100, 205600, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(-89900, 2000, 201900, 3000)
    MoveCamera(65, 30, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(21500, 3000)
    Sound(868, 2, 50, 0)
    Sound(863, 2, 50, 0)
    Sound(864, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x1000)
    SetChrPos(0x18, -71000, 0, 152150, 275)
    SetChrPos(0xE, -72000, 0, 157200, 315)
    SetChrPos(0xF, -68850, 0, 147550, 90)
    PlayEffect(0x0, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xF, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-73500, 1400, 156000, 0)
    MoveCamera(50, 18, -5, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(-69500, 1400, 153700, 4000)
    MoveCamera(50, 18, -5, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(16500, 4000)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x13, 0x1000)
    SetChrPos(0x17, -32900, 0, 42000, 225)
    SetChrPos(0xE, -33200, 0, 38100, 315)
    SetChrPos(0xF, -30450, 0, 40200, 90)
    PlayEffect(0x0, 0x0, 0xE, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xF, 0x5, 0, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_68(-33700, 1700, 41100, 0)
    MoveCamera(355, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(-33150, 1700, 41650, 3000)
    MoveCamera(15, 20, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15500, 3000)
    Sleep(2000)
    StopSound(863, 1000, 50)
    StopSound(864, 1000, 50)
    OP_24(0x364)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_31CD end

    def Function_18_361A(): pass

    label("Function_18_361A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch41900.itc", 0x23)
    LoadChrToIndex("chr/ch41950.itc", 0x24)
    LoadChrToIndex("chr/ch41951.itc", 0x25)
    LoadChrToIndex("chr/ch03400.itc", 0x28)
    LoadChrToIndex("chr/ch03450.itc", 0x29)
    LoadChrToIndex("chr/ch03451.itc", 0x2A)
    SoundLoad(863)
    SoundLoad(864)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x24)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    OP_7D(0xFF, 0xA0, 0x96, 0x0, 0x0)
    SetMapObjFrame(0xFF, "glow_3", 0x0, 0x1)
    ClearMapObjFlags(0x14, 0x4)
    SetChrPos(0x15, -2000, 0, -3500, 180)
    SetChrPos(0x10, -2000, 0, -1000, 180)
    SetChrPos(0x11, -1000, 0, 1000, 180)
    SetChrPos(0x12, -3000, 0, 1000, 180)
    SetChrPos(0x13, -1000, 0, 2500, 180)
    SetChrPos(0x14, -3000, 0, 2500, 180)
    OP_68(-2000, 1000, -5500, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-2000, 1000, -2500, 2000)
    MoveCamera(50, 25, 0, 2000)
    SetCameraDistance(19000, 2000)
    Sound(863, 2, 50, 0)
    Sound(864, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0021
    ChrTalk(
        0x10,
        (
            "#5P……隊長。\x01",
            "いかがしますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x15,
        (
            "#04606F#5Pんー、そうだなぁ。\x02\x03",

            "#04600Fここで頑張られてもウザいし、\x01",
            "ちょっと遊んでくるよ。\x02\x03",

            "フォローはお願い。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10,
        "#5P了解#4Rヤ ー#。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x11,
        "#5P隊長に続くぞ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2000, 1000, -3500, 800)
    SetCameraDistance(14700, 800)
    Sleep(300)
    Sound(358, 0, 100, 0)
    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_0D()
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0025
    ChrTalk(
        0x15,
        (
            "#04604F#5Pさあ、《テスタ＝ロッサ》。\x01",
            "獲物はまだまだ残ってるよ……\x02\x03",

            "#04602Fシャーリィと一緒に\x01",
            "めいっぱい楽しんじゃおう！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0x15, 0x2A)

    def lambda_394D():
        OP_9B(0x0, 0x15, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_394D)
    OP_93(0x10, 0xB4, 0x1F4)
    SetChrChipByIndex(0x10, 0x25)
    SetChrChipByIndex(0x11, 0x25)
    SetChrChipByIndex(0x12, 0x25)
    SetChrChipByIndex(0x13, 0x25)
    SetChrChipByIndex(0x14, 0x25)
    FadeToDark(500, 0, -1)

    def lambda_3987():
        OP_9B(0x0, 0x10, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3987)
    Sleep(50)

    def lambda_399F():
        OP_9B(0x0, 0x11, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_399F)
    Sleep(50)

    def lambda_39B7():
        OP_9B(0x0, 0x12, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_39B7)
    Sleep(50)

    def lambda_39CF():
        OP_9B(0x0, 0x13, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_39CF)
    Sleep(50)

    def lambda_39E7():
        OP_9B(0x0, 0x14, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_39E7)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_361A end

    def Function_19_3A1C(): pass

    label("Function_19_3A1C")

    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_11(0x0, 0x0, 0x0, 0x19, 0x28, 0x0)
    SetMapObjFrame(0xFF, "object09_lantern", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model07_light", 0x0, 0x1)
    BeginChrThread(0xD, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 4)), scpexpr(EXPR_END)), "loc_3AA2")
    SetScenarioFlags(0x0, 1)

    label("loc_3AA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AF7")
    OP_C3(0x0, 0x3, 0x2, 0x1194, 0x6E, 0x1, -88800, -1000, 192450, 2000, 2000, 0)
    OP_C4(0x0, 0x2, 0x3, 0xD90)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x10000000)
    SetMapObjFlags(0x5, 0x800000)
    OP_1C(0x0, 0x5, 0x0, 0x0, 0x0, 0x0, 0xD9C, 0x0)

    label("loc_3AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 5)), scpexpr(EXPR_END)), "loc_3B03")
    SetScenarioFlags(0x0, 2)

    label("loc_3B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B58")
    OP_C3(0x1, 0x3, 0x2, 0x1194, 0x6E, 0x1, -90600, -1000, 184350, 2000, 2000, 0)
    OP_C4(0x1, 0x2, 0x3, 0xD91)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x10000000)
    SetMapObjFlags(0x6, 0x800000)
    OP_1C(0x0, 0x6, 0x0, 0x0, 0x0, 0x0, 0xD9D, 0x0)

    label("loc_3B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 6)), scpexpr(EXPR_END)), "loc_3B64")
    SetScenarioFlags(0x0, 3)

    label("loc_3B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BB9")
    OP_C3(0x2, 0x3, 0x2, 0x1194, 0x6E, 0x1, -85120, -1000, 181010, 2000, 2000, 0)
    OP_C4(0x2, 0x2, 0x3, 0xD92)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x10000000)
    SetMapObjFlags(0x7, 0x800000)
    OP_1C(0x0, 0x7, 0x0, 0x0, 0x0, 0x0, 0xD9E, 0x0)

    label("loc_3BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 7)), scpexpr(EXPR_END)), "loc_3BC5")
    SetScenarioFlags(0x0, 4)

    label("loc_3BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C1A")
    OP_C3(0x3, 0x3, 0x2, 0x1194, 0x6E, 0x1, -79990, -1000, 163480, 2000, 2000, 0)
    OP_C4(0x3, 0x2, 0x3, 0xD93)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x10000000)
    SetMapObjFlags(0x8, 0x800000)
    OP_1C(0x0, 0x8, 0x0, 0x0, 0x0, 0x0, 0xD9F, 0x0)

    label("loc_3C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 0)), scpexpr(EXPR_END)), "loc_3C26")
    SetScenarioFlags(0x0, 5)

    label("loc_3C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C7B")
    OP_C3(0x4, 0x3, 0x2, 0x1194, 0x6E, 0x1, -66570, -1000, 155940, 2000, 2000, 0)
    OP_C4(0x4, 0x2, 0x3, 0xD94)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x9, 0x10000000)
    SetMapObjFlags(0x9, 0x800000)
    OP_1C(0x0, 0x9, 0x0, 0x0, 0x0, 0x0, 0xDA0, 0x0)

    label("loc_3C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 1)), scpexpr(EXPR_END)), "loc_3C87")
    SetScenarioFlags(0x0, 6)

    label("loc_3C87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3CDC")
    OP_C3(0x5, 0x3, 0x2, 0x1194, 0x6E, 0x1, -70370, -1000, 145190, 2000, 2000, 0)
    OP_C4(0x5, 0x2, 0x3, 0xD95)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x10000000)
    SetMapObjFlags(0xA, 0x800000)
    OP_1C(0x0, 0xA, 0x0, 0x0, 0x0, 0x0, 0xDA1, 0x0)

    label("loc_3CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 2)), scpexpr(EXPR_END)), "loc_3CE8")
    SetScenarioFlags(0x0, 7)

    label("loc_3CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D3D")
    OP_C3(0x6, 0x3, 0x2, 0x1194, 0x6E, 0x1, -62710, -1000, 124440, 2000, 2000, 0)
    OP_C4(0x6, 0x2, 0x3, 0xD96)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x10000000)
    SetMapObjFlags(0xB, 0x800000)
    OP_1C(0x0, 0xB, 0x0, 0x0, 0x0, 0x0, 0xDA2, 0x0)

    label("loc_3D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 3)), scpexpr(EXPR_END)), "loc_3D49")
    SetScenarioFlags(0x1, 0)

    label("loc_3D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D9E")
    OP_C3(0x7, 0x3, 0x2, 0x1194, 0x6E, 0x1, -61700, -1000, 106350, 2000, 2000, 0)
    OP_C4(0x7, 0x2, 0x3, 0xD97)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x10000000)
    SetMapObjFlags(0xC, 0x800000)
    OP_1C(0x0, 0xC, 0x0, 0x0, 0x0, 0x0, 0xDA3, 0x0)

    label("loc_3D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 4)), scpexpr(EXPR_END)), "loc_3DAA")
    SetScenarioFlags(0x1, 1)

    label("loc_3DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DFF")
    OP_C3(0x8, 0x3, 0x2, 0x1194, 0x6E, 0x1, -54430, -1000, 89830, 2000, 2000, 0)
    OP_C4(0x8, 0x2, 0x3, 0xD98)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x10000000)
    SetMapObjFlags(0xD, 0x800000)
    OP_1C(0x0, 0xD, 0x0, 0x0, 0x0, 0x0, 0xDA4, 0x0)

    label("loc_3DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 5)), scpexpr(EXPR_END)), "loc_3E0B")
    SetScenarioFlags(0x1, 2)

    label("loc_3E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E60")
    OP_C3(0x9, 0x3, 0x2, 0x1194, 0x6E, 0x1, -54220, -1000, 58200, 2000, 2000, 0)
    OP_C4(0x9, 0x2, 0x3, 0xD99)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x10000000)
    SetMapObjFlags(0xE, 0x800000)
    OP_1C(0x0, 0xE, 0x0, 0x0, 0x0, 0x0, 0xDA5, 0x0)

    label("loc_3E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 6)), scpexpr(EXPR_END)), "loc_3E6C")
    SetScenarioFlags(0x1, 3)

    label("loc_3E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC1")
    OP_C3(0xA, 0x3, 0x2, 0x1194, 0x6E, 0x1, -32170, -1000, 41830, 2000, 2000, 0)
    OP_C4(0xA, 0x2, 0x3, 0xD9A)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x10000000)
    SetMapObjFlags(0xF, 0x800000)
    OP_1C(0x0, 0xF, 0x0, 0x0, 0x0, 0x0, 0xDA6, 0x0)

    label("loc_3EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 7)), scpexpr(EXPR_END)), "loc_3ECD")
    SetScenarioFlags(0x1, 4)

    label("loc_3ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F22")
    OP_C3(0xB, 0x3, 0x2, 0x1194, 0x6E, 0x1, -5660, -1000, 24900, 2000, 2000, 0)
    OP_C4(0xB, 0x2, 0x3, 0xD9B)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x10000000)
    SetMapObjFlags(0x10, 0x800000)
    OP_1C(0x0, 0x10, 0x0, 0x0, 0x0, 0x0, 0xDA7, 0x0)

    label("loc_3F22")

    Return()

    # Function_19_3A1C end

    def Function_20_3F23(): pass

    label("Function_20_3F23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_E2(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F47")
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)

    label("loc_3F47")

    LoadChrToIndex("chr/ch03256.itc", 0x1E)
    LoadChrToIndex("apl/ch51608.itc", 0x1F)
    LoadEffect(0x0, "event/ev17049.eff")
    SetChrPos(0x101, -2000, 0, 1000, 0)
    SetChrPos(0x106, -1150, 0, 0, 0)
    SetChrPos(0x103, -3350, 0, -1000, 0)
    SetChrPos(0x107, -4600, 0, -1750, 0)
    SetChrPos(0x105, -2000, 0, -2450, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-2000, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(-2000, 1000, 2500, 2500)
    MoveCamera(45, 25, 0, 2500)
    OP_6E(510, 2500)
    SetCameraDistance(18860, 2500)

    def lambda_4027():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4027)
    Sleep(50)

    def lambda_403F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_403F)
    Sleep(50)

    def lambda_4057():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4057)
    Sleep(50)

    def lambda_406F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_406F)
    Sleep(50)

    def lambda_4087():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4087)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 2, 0, 21)
    WaitChrThread(0x106, 1)
    BeginChrThread(0x106, 2, 0, 21)
    WaitChrThread(0x103, 1)
    BeginChrThread(0x103, 2, 0, 21)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 2, 0, 21)
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x101, 0x2)

    def lambda_40DE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40DE)
    EndChrThread(0x106, 0x2)

    def lambda_40EF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_40EF)
    EndChrThread(0x103, 0x2)

    def lambda_4100():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4100)
    EndChrThread(0x105, 0x2)

    def lambda_4111():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4111)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x106, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0026
    ChrTalk(
        0x101,
        "#00011F#11Pこれは……！？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        (
            "#10408F#12Pどうやら照明が消されて\x01",
            "しまってるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x106,
        "#10701F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x103,
        "#00208F#12P……？（これは……）\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x107,
        "#01201F#12P#3Cふむ……\x02",
    )

    CloseMessageWindow()

    def lambda_41FB():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41FB)
    OP_68(-2009, 1000, 4600, 2000)
    MoveCamera(43, 24, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(17000, 2000)
    Sleep(1000)
    Sound(853, 0, 100, 0)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    #Sound(2087, 255, 100, 0)    #voice#Lloyd

    #C0031
    ChrTalk(
        0x101,
        "#00011F#11P#5Aえ──\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#00207F#12P#9A#Nロイドさん！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(540, 0, 50, 0)

    def lambda_4309():

        label("loc_4309")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_4309")

    QueueWorkItem2(0x106, 2, lambda_4309)
    SetChrChipByIndex(0x106, 0x1E)
    SetChrSubChip(0x106, 0x4)
    #Sound(3204, 255, 80, 0)    #voice#Rixia

    #C0033
    ChrTalk(
        0x106,
        "#10707F#11P#7Aくっ……\x02",
    )
    #Auto

    Sleep(500)
    Sound(250, 0, 40, 0)
    Sound(307, 0, 100, 0)
    SetChrSubChip(0x106, 0x2)
    PlayEffect(0x0, 0x0, 0x106, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x101, 0, 0, 0, 0)
    Sleep(500)
    EndChrThread(0x101, 0x1)
    Sound(308, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0xA, 0xFF, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(196, 0, 100, 0)
    OP_68(-1660, 1000, 3060, 800)
    MoveCamera(40, 25, 0, 800)
    OP_6E(510, 800)

    def lambda_441A():
        OP_9A(0xFE, 0x106, 0x1F4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_441A)

    def lambda_442E():
        OP_95(0xFE, -3500, 0, 3000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_442E)
    #Sound(2031, 255, 100, 0)    #voice#Lloyd

    #C0034
    ChrTalk(
        0x101,
        "#00015F#11P#6Aうおっ……！\x02",
    )
    #Auto

    WaitChrThread(0x101, 1)
    EndChrThread(0x106, 0x2)
    CancelBlur(500)
    Sound(811, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x106, 0x4)
    Sleep(1000)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)

    def lambda_449C():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_449C)
    Sleep(50)

    def lambda_44AC():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_44AC)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    #C0035
    ChrTalk(
        0x103,
        "#00207F#6Pロイドさん……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30Wくっ……大丈夫だ。\x02\x03",

            "#00008F……すまない。\x01",
            "助かったよ、リーシャ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x106,
        (
            "#10710F#11Pいえ……\x01",
            "間に合って良かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10406F#12Pふう、やれやれだね。\x02\x03",

            "#10401Fしかし……今のは地雷かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        (
            "#00206F#6Pええ……接触式の\x01",
            "導力地雷のようです。\x02\x03",

            "#00201F爆発力が弱かったので\x01",
            "対人用だとは思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x107,
        (
            "#01201F#6P#3Cどうやらトンネル道全体に\x01",
            "バラ撒かれているようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    OP_93(0x101, 0x10E, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()

    def lambda_468C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_468C)
    OP_9B(0x1, 0x106, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)

    #C0041
    ChrTalk(
        0x101,
        (
            "#00006F#5Pくっ、こんなものを\x01",
            "一般道に仕掛けるなんて……\x02\x03",

            "#00013Fレジスタンスの退路を\x01",
            "断つのが目的ってところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x106,
        (
            "#10703F#11Pその可能性は高そうです。\x02\x03",

            "#10708F本腰を入れて掃討する\x01",
            "つもりではないかと……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0043
    ChrTalk(
        0x101,
        (
            "#00003F#5P──時間がない。\x01",
            "このまま通り抜けよう。\x02\x03",

            "#00007F足元に気をつけて\x01",
            "慎重かつ迅速に進むぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#00201F#6P了解です……！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10406F#12Pやれやれ。\x01",
            "面倒をかけてくれるね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_49()
    OP_37()
    SetChrPos(0x0, -2000, 0, 4000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A2, 4)
    OP_29(0xAF, 0x1, 0xB)
    ClearMapFlags(0x10000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_3F23 end

    def Function_21_4887(): pass

    label("Function_21_4887")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A4")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)

    label("loc_48A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48C8")
    OP_93(0xFE, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(500)
    Jump("loc_48A4")

    label("loc_48C8")

    Return()

    # Function_21_4887 end

    def Function_22_48C9(): pass

    label("Function_22_48C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4933")
    EventBegin(0x1)
    OP_E2(0x3)

    #C0046
    ChrTalk(
        0x101,
        (
            "#00000Fこちらは《僧院》方面だな。\x01",
            "今はマインツ方面に急ごう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70120, 0, 99240, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_4933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B44")
    EventBegin(0x0)
    Fade(500)
    OP_E2(0x3)
    OP_68(-72420, 2500, 95810, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x0, -70560, 0, 97340, 179)
    SetChrPos(0x1, -68710, 0, 98170, 179)
    SetChrPos(0x2, -71980, 0, 98170, 179)
    SetChrPos(0x3, -69810, 0, 99060, 179)
    OP_0D()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000Fこっちの道を進むと、\x01",
            "確か《月の僧院》とかいう\x01",
            "中世の遺跡があるんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x109,
        (
            "#10100Fはい、以前皆さんと一緒に\x01",
            "調査させていただきましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x105,
        "#10300Fへえ、そんなことがあったんだ。\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00100Fとりあえず、今は町長さんの\x01",
            "依頼もあることだし。\x02\x03",

            "こちらの方面を\x01",
            "探索している余裕はなさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00000Fそうだな、様子を見るにしても\x01",
            "またの機会にしておこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_E2(0x2)
    SetScenarioFlags(0x0, 0)
    EventEnd(0x5)
    Jump("loc_4BB8")

    label("loc_4B44")

    EventBegin(0x1)
    OP_E2(0x3)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000F今は遺跡方面を探索している\x01",
            "余裕はなさそうだ。\x02\x03",

            "訪れるのはまたの機会にしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -70120, 0, 99240, 0)
    OP_E2(0x2)
    EventEnd(0x4)

    label("loc_4BB8")

    Return()

    # Function_22_48C9 end

    SaveToFile()

Try(main)
