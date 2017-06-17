from ScenarioHelper import *

def main():
    CreateScenaFile(
        "a0003.bin",                # FileName
        "a0000",                    # MapName
        "a0002",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0003",                  # 0
        "bm4000",                 # 1
        "bm4000",                 # 2
        "bm4010",                 # 3
        "bm4020",                 # 4
        "bm4030",                 # 5
        "bm4040",                 # 6
        "bt2030",                 # 7
        "bt0000",                 # 8
        "be4800",                 # 9
        "bt2500",                 # 10
        "bc130b",                 # 11
        "bc1400",                 # 12
        "bc140b",                 # 13
        "bc1410",                 # 14
        "bc141b",                 # 15
        "bc1420",                 # 16
        "bc1460",                 # 17
        "bc1470",                 # 18
        "bc0100",                 # 19
        "bc0200",                 # 20
        "bc0300",                 # 21
        "bc0400",                 # 22
        "bc1000",                 # 23
        "bc1100",                 # 24
        "bc1200",                 # 25
        "bc120b",                 # 26
        "bc1510",                 # 27
        "bc1520",                 # 28
        "bc1530",                 # 29
        "bc1540",                 # 30
        "bc1550",                 # 31
        "bc1560",                 # 32
        "bc1600",                 # 33
        "bc122b",                 # 34
        "bm0100",                 # 35
        "bm0101",                 # 36
        "bm0102",                 # 37
        "bm0110",                 # 38
        "bm0111",                 # 39
        "bm0112",                 # 40
        "bm0113",                 # 41
        "bm0114",                 # 42
        "bm0200",                 # 43
        "bm0210",                 # 44
        "bm0300",                 # 45
        "bm0310",                 # 46
        "bm0220",                 # 47
        "bm0320",                 # 48
        "br0100",                 # 49
        "br0000",                 # 50
        "br0200",                 # 51
        "br1000",                 # 52
        "br1060",                 # 53
        "br1500",                 # 54
        "br1510",                 # 55
        "br1520",                 # 56
        "br1530",                 # 57
        "br1600",                 # 58
        "br2000",                 # 59
        "br2010",                 # 60
        "br2040",                 # 61
        "br2050",                 # 62
        "br2060",                 # 63
        "br2061",                 # 64
        "br2070",                 # 65
        "bt1110",                 # 66
        "bt1400",                 # 67
        "bt1410",                 # 68
        "bt1420",                 # 69
        "bt1430",                 # 70
        "bt1450",                 # 71
        "bt1010",                 # 72
        "bt1020",                 # 73
        "bt1030",                 # 74
        "bt103b",                 # 75
        "bt1300",                 # 76
        "bt130b",                 # 77
        "bt1310",                 # 78
        "bt1320",                 # 79
        "bm1000",                 # 80
        "bm1010",                 # 81
        "bm1020",                 # 82
        "bm1030",                 # 83
        "bm1040",                 # 84
        "bm1050",                 # 85
        "bm1061",                 # 86
        "bm1070",                 # 87
        "bm1080",                 # 88
        "bm2000",                 # 89
        "bm2020",                 # 90
        "bm2050",                 # 91
        "bm2099",                 # 92
        "bm2060",                 # 93
        "br2080",                 # 94
        "br3000",                 # 95
        "br3100",                 # 96
        "bm4110",                 # 97
        "bm4120",                 # 98
        "bm4130",                 # 99
        "bm4150",                 # 100
        "bm4160",                 # 101
        "bm4200",                 # 102
        "bm4210",                 # 103
        "bm4250",                 # 104
        "br4000",                 # 105
        "br4010",                 # 106
        "br4020",                 # 107
        "bt6000",                 # 108
        "bt6010",                 # 109
        "bt6020",                 # 110
        "bt6030",                 # 111
        "bt1510",                 # 112
        "bm9000",                 # 113
        "bm9010",                 # 114
        "bm9020",                 # 115
        "bm9030",                 # 116
        "bm9039",                 # 117
        "bm9040",                 # 118
        "bm9041",                 # 119
        "bm9049",                 # 120
        "bm9050",                 # 121
        "bm9059",                 # 122
        "bm9060",                 # 123
        "bm9069",                 # 124
        "bm9070",                 # 125
        "bm9099",                 # 126
    ))

    ATBonus("ATBonus_94", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    Sepith("Sepith_41E1", 100, 1,   2,   3,   70,  89,  99)

    MonsterBattlePostion("MonsterBattlePostion_184", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_194", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_198", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_19C", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A0", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_E4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_F4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_FC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_100", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_168", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_16C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_170", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_174", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_178", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_17C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 5, 5, 45)

    # monster count: 0

    # event battle count: 126

    BattleInfo(
        "BattleInfo_1A4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", "MonsterBattlePostion_184", "MonsterBattlePostion_184", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1E8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_22C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_270", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2B4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4030", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2F8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4040", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_33C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt2030", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_380", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt0000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3C4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "be4800", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_408", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt2500", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_44C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc130b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_490", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1400", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4D4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc140b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_518", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1410", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_55C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc141b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5A0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1420", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5E4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1460", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_628", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1470", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_66C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc0100", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6B0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc0200", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6F4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc0300", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_738", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc0400", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_77C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7C0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1100", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_804", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1200", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_848", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc120b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_88C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1510", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8D0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1520", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_914", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1530", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_958", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1540", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_99C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1550", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9E0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1560", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A24", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc1600", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A68", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bc122b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AAC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0100", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AF0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0101", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B34", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0102", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B78", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0110", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BBC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0111", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C00", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0112", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C44", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0113", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C88", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0114", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CCC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0200", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D10", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0210", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D54", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0300", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D98", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0310", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DDC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0220", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E20", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm0320", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E64", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br0100", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_EA8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br0000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_EEC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br0200", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F30", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F74", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1060", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_FB8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1500", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_FFC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1510", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1040", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1520", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1084", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1530", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_10C8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br1600", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_110C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1150", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1194", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2040", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_11D8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2050", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_121C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2060", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1260", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2061", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_12A4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2070", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_12E8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1110", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_132C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1400", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1370", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1410", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_13B4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1420", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_13F8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1430", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_143C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1450", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1480", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_14C4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1508", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1030", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_154C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt103b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1590", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1300", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_15D4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt130b", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1618", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1310", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_165C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1320", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_16A0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_16E4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1728", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_176C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1030", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_17B0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1040", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_17F4", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1050", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1838", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1061", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_187C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1070", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_18C0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm1080", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1904", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm2000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1948", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm2020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_198C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm2050", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_19D0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm2099", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1A14", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm2060", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1A58", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br2080", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1A9C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br3000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1AE0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br3100", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1B24", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4110", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1B68", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4120", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1BAC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4130", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1BF0", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4150", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1C34", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4160", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1C78", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4200", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1CBC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4210", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1D00", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm4250", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1D44", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br4000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1D88", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br4010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1DCC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "br4020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1E10", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt6000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1E54", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt6010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1E98", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt6020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1EDC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt6030", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1F20", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bt1510", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1F64", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9000", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1FA8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9010", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1FEC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9020", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2030", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9030", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2074", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9039", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_20B8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9040", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_20FC", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9041", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2140", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9049", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2184", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9050", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_21C8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9059", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_220C", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9060", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2250", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9069", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_2294", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9070", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_22D8", 0x0200, 0, 6, 0, 0, 0, 0, 0, "bm9099", "Sepith_41E1", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_E4", "MonsterBattlePostion_164", "ed7450", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    ChipFrameInfo(9000, 0)                                       # 0

    ScpFunction((
        "Function_0_2328",         # 00, 0
        "Function_1_232C",         # 01, 1
        "Function_2_232D",         # 02, 2
    ))


    def Function_0_2328(): pass

    label("Function_0_2328")

    Event(0, 2)
    Return()

    # Function_0_2328 end

    def Function_1_232C(): pass

    label("Function_1_232C")

    Return()

    # Function_1_232C end

    def Function_2_232D(): pass

    label("Function_2_232D")

    SetMapFlags(0x80)

    label("loc_2332")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41E0")
    OutputDebugInt(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "デバッグ用\x01",                  # 0
            "アルタイル、他\x01",              # 1
            "クロスベル（前）\x01",            # 2
            "クロスベル（新）\x01",            # 3
            "ジオフロント\x01",                # 4
            "街道①\x01",                      # 5
            "街道②\x01",                      # 6
            "ミシュラム\x01",                  # 7
            "星見の塔、月の僧院\x01",          # 8
            "古戦場、鉱山\x01",                # 9
            "湿地、森林、警察、病院\x01",      # 10
            "ラスダン\x01",                    # 11
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_244C"),
        (1, "loc_24B4"),
        (2, "loc_26D9"),
        (3, "loc_28EB"),
        (4, "loc_2CAD"),
        (5, "loc_2FF1"),
        (6, "loc_3249"),
        (7, "loc_340E"),
        (8, "loc_374E"),
        (9, "loc_3ABA"),
        (10, "loc_3C68"),
        (11, "loc_3EE4"),
        (SWITCH_DEFAULT, "loc_41DB"),
    )


    label("loc_244C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AF")

    Menu(
        1,
        -1,
        -1,
        1,
        "DB0000：テスト１\x01",
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_248B"),
        (SWITCH_DEFAULT, "loc_24A0"),
    )


    label("loc_248B")

    Battle("BattleInfo_1A4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_24AA")

    label("loc_24A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24AA")

    Jump("loc_244C")

    label("loc_24AF")

    Jump("loc_41DB")

    label("loc_24B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D4")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "+BM4000：アルタイルロッジ外\x01",            # 0
            "+BM4010：アルタイルロッジ内通常\x01",        # 1
            "+BM4020：アルタイルロッジ内中間\x01",        # 2
            "+BM4030：アルタイルロッジ内ボス１\x01",      # 3
            "+BM4040：アルタイルロッジ内ボス２\x01",      # 4
            "+BT2030：ベルガード門\x01",                  # 5
            "+BT0000：アルモリカ村\x01",                  # 6
            "+BE4800：列車上戦闘\x01",                    # 7
            "+BT2500：タングラム門\x01",                  # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2608"),
        (1, "loc_261D"),
        (2, "loc_2632"),
        (3, "loc_2647"),
        (4, "loc_265C"),
        (5, "loc_2671"),
        (6, "loc_2686"),
        (7, "loc_269B"),
        (8, "loc_26B0"),
        (SWITCH_DEFAULT, "loc_26C5"),
    )


    label("loc_2608")

    Battle("BattleInfo_1E8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_261D")

    Battle("BattleInfo_22C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_2632")

    Battle("BattleInfo_270", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_2647")

    Battle("BattleInfo_2B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_265C")

    Battle("BattleInfo_2F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_2671")

    Battle("BattleInfo_33C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_2686")

    Battle("BattleInfo_380", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_269B")

    Battle("BattleInfo_3C4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_26B0")

    Battle("BattleInfo_408", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_26CF")

    label("loc_26C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26CF")

    Jump("loc_24B4")

    label("loc_26D4")

    Jump("loc_41DB")

    label("loc_26D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28E6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            " BC130b：IBCゲート前広場（夜）\x01",        # 0
            " BC1400：旧市街地外観?広場（昼）\x01",      # 1
            " BC140b：旧市街地外観?広場（夜）\x01",      # 2
            " BC1410：旧市街地外観?路地（昼）\x01",      # 3
            " BC141b：旧市街地外観?路地（夜）\x01",      # 4
            " BC1420：イグニス倉庫内部\x09\x01",         # 5
            " BC1460：旧市街?廃アパート?部屋\x01",       # 6
            " BC1470：旧市街?廃アパート?廊下\x01",       # 7
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_282F"),
        (1, "loc_2844"),
        (2, "loc_2859"),
        (3, "loc_286E"),
        (4, "loc_2883"),
        (5, "loc_2898"),
        (6, "loc_28AD"),
        (7, "loc_28C2"),
        (SWITCH_DEFAULT, "loc_28D7"),
    )


    label("loc_282F")

    Battle("BattleInfo_44C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_2844")

    Battle("BattleInfo_490", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_2859")

    Battle("BattleInfo_4D4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_286E")

    Battle("BattleInfo_518", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_2883")

    Battle("BattleInfo_55C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_2898")

    Battle("BattleInfo_5A0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_28AD")

    Battle("BattleInfo_5E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_28C2")

    Battle("BattleInfo_628", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_28E1")

    label("loc_28D7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28E1")

    Jump("loc_26D9")

    label("loc_28E6")

    Jump("loc_41DB")

    label("loc_28EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CA8")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "+BC0100：中央区?通常（昼）\x01",                 # 0
            "+BC0200：西街区?通常（昼）\x01",                 # 1
            "+BC0300：住宅街?通常（昼）\x01",                 # 2
            "+BC0400：歓楽街?通常（昼）\x01",                 # 3
            "+BC1000：東街区?通常（昼）\x01",                 # 4
            "+BC1100：行政区?通常（昼）\x01",                 # 5
            "+BC1200：湾岸区?通常（昼）\x01",                 # 6
            "+BC120b：湾岸区?通常（夜）\x01",                 # 7
            "+BC1510：オルキスタワー?通常1\x01",              # 8
            "+BC1520：オルキスタワー?通常2\x01",              # 9
            "+BC1530：オルキスタワー?通常3\x01",              # 10
            "+BC1540：オルキスタワー?中ボス1\x01",            # 11
            "+BC1550：オルキスタワー?中ボス2\x01",            # 12
            "+BC1560：オルキスタワー?35階\x01",               # 13
            "+BC1600：オルキスタワー屋上?ボス\x01",           # 14
            "+BC122B：クロスベルタイムズ室内（夜）\x01",      # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B49"),
        (1, "loc_2B5E"),
        (2, "loc_2B73"),
        (3, "loc_2B88"),
        (4, "loc_2B9D"),
        (5, "loc_2BB2"),
        (6, "loc_2BC7"),
        (7, "loc_2BDC"),
        (8, "loc_2BF1"),
        (9, "loc_2C06"),
        (10, "loc_2C1B"),
        (11, "loc_2C30"),
        (12, "loc_2C45"),
        (13, "loc_2C5A"),
        (14, "loc_2C6F"),
        (15, "loc_2C84"),
        (SWITCH_DEFAULT, "loc_2C99"),
    )


    label("loc_2B49")

    Battle("BattleInfo_66C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2B5E")

    Battle("BattleInfo_6B0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2B73")

    Battle("BattleInfo_6F4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2B88")

    Battle("BattleInfo_738", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2B9D")

    Battle("BattleInfo_77C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2BB2")

    Battle("BattleInfo_7C0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2BC7")

    Battle("BattleInfo_804", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2BDC")

    Battle("BattleInfo_848", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2BF1")

    Battle("BattleInfo_88C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C06")

    Battle("BattleInfo_8D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C1B")

    Battle("BattleInfo_914", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C30")

    Battle("BattleInfo_958", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C45")

    Battle("BattleInfo_99C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C5A")

    Battle("BattleInfo_9E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C6F")

    Battle("BattleInfo_A24", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C84")

    Battle("BattleInfo_A68", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CA3")

    label("loc_2C99")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CA3")

    Jump("loc_28EB")

    label("loc_2CA8")

    Jump("loc_41DB")

    label("loc_2CAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FEC")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            " BM0100：ジオフロB初期（広間）\x01",        # 0
            " BM0101：ジオフロB初期（通路）\x01",        # 1
            " BM0102：ジオフロB初期（ボス）\x01",        # 2
            " BM0110：ジオフロB中盤（広間）\x01",        # 3
            " BM0111：ジオフロB中盤（通路）\x01",        # 4
            " BM0112：ジオフロB初期（ボス）\x01",        # 5
            " BM0113：ジオフロB中盤（広間氷）\x01",      # 6
            " BM0114：ジオフロB中盤（通路氷）\x01",      # 7
            "+BM0200：ジオフロC?通常\x01",               # 8
            "+BM0210：ジオフロC?ボス\x01",               # 9
            "+BM0300：ジオフロD?通常\x01",               # 10
            "+BM0310：ジオフロD?ボス\x01",               # 11
            "+BM0220：ジオフロC?EXTRA\x01",              # 12
            "+BM0320：ジオフロD?EXTRA\x01",              # 13
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EB7"),
        (1, "loc_2ECC"),
        (2, "loc_2EE1"),
        (3, "loc_2EF6"),
        (4, "loc_2F0B"),
        (5, "loc_2F20"),
        (6, "loc_2F35"),
        (7, "loc_2F4A"),
        (8, "loc_2F5F"),
        (9, "loc_2F74"),
        (10, "loc_2F89"),
        (11, "loc_2F9E"),
        (12, "loc_2FB3"),
        (13, "loc_2FC8"),
        (SWITCH_DEFAULT, "loc_2FDD"),
    )


    label("loc_2EB7")

    Battle("BattleInfo_AAC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2ECC")

    Battle("BattleInfo_AF0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2EE1")

    Battle("BattleInfo_B34", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2EF6")

    Battle("BattleInfo_B78", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F0B")

    Battle("BattleInfo_BBC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F20")

    Battle("BattleInfo_C00", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F35")

    Battle("BattleInfo_C44", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F4A")

    Battle("BattleInfo_C88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F5F")

    Battle("BattleInfo_CCC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F74")

    Battle("BattleInfo_D10", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F89")

    Battle("BattleInfo_D54", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2F9E")

    Battle("BattleInfo_D98", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2FB3")

    Battle("BattleInfo_DDC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2FC8")

    Battle("BattleInfo_E20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2FE7")

    label("loc_2FDD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2FE7")

    Jump("loc_2CAD")

    label("loc_2FEC")

    Jump("loc_41DB")

    label("loc_2FF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3244")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            " BR0100：アルモリカ古道\x01",              # 0
            " BR0000：東クロスベル街道\x01",            # 1
            "+BR0200：東クロスベル追加(幻獣)\x01",      # 2
            " BR1000：西クロスベル街道\x01",            # 3
            "+BR1060：西クロスベル街道線路\x01",        # 4
            " BR1500：ウルスラ間道\x01",                # 5
            " BR1510：ウルスラ間道?森①\x01",           # 6
            " BR1520：ウルスラ間道?水辺\x01",           # 7
            " BR1530：ウルスラ間道?森②\x01",           # 8
            "+BR1600：ウルスラ間道?小洞窟\x01",         # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3163"),
        (1, "loc_3178"),
        (2, "loc_318D"),
        (3, "loc_31A2"),
        (4, "loc_31B7"),
        (5, "loc_31CC"),
        (6, "loc_31E1"),
        (7, "loc_31F6"),
        (8, "loc_320B"),
        (9, "loc_3220"),
        (SWITCH_DEFAULT, "loc_3235"),
    )


    label("loc_3163")

    Battle("BattleInfo_E64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_3178")

    Battle("BattleInfo_EA8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_318D")

    Battle("BattleInfo_EEC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_31A2")

    Battle("BattleInfo_F30", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_31B7")

    Battle("BattleInfo_F74", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_31CC")

    Battle("BattleInfo_FB8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_31E1")

    Battle("BattleInfo_FFC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_31F6")

    Battle("BattleInfo_1040", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_320B")

    Battle("BattleInfo_1084", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_3220")

    Battle("BattleInfo_10C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_323F")

    label("loc_3235")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_323F")

    Jump("loc_2FF1")

    label("loc_3244")

    Jump("loc_41DB")

    label("loc_3249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3409")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            " BR2000：マインツ山道?森\x01",              # 0
            " BR2010：マインツ山道?森/水辺\x01",         # 1
            " BR2040：マインツ山道?トンネル岩\x01",      # 2
            " BR2050：マインツ山道?トンネル\x01",        # 3
            "+BR2060：マインツ山道?岩\x01",              # 4
            "+BR2061：マインツ山道?高台狙撃兵\x01",      # 5
            " BR2070：マインツ山道?岩崖\x01",            # 6
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3367"),
        (1, "loc_337C"),
        (2, "loc_3391"),
        (3, "loc_33A6"),
        (4, "loc_33BB"),
        (5, "loc_33D0"),
        (6, "loc_33E5"),
        (SWITCH_DEFAULT, "loc_33FA"),
    )


    label("loc_3367")

    Battle("BattleInfo_110C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_337C")

    Battle("BattleInfo_1150", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_3391")

    Battle("BattleInfo_1194", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_33A6")

    Battle("BattleInfo_11D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_33BB")

    Battle("BattleInfo_121C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_33D0")

    Battle("BattleInfo_1260", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_33E5")

    Battle("BattleInfo_12A4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3404")

    label("loc_33FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3404")

    Jump("loc_3249")

    label("loc_3409")

    Jump("loc_41DB")

    label("loc_340E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3749")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "+BT1110：議長邸エントランス（昼）\x01",      # 0
            "+BT1400：鏡の城?幻属性\x01",                 # 1
            "+BT1410：鏡の城?時属性\x01",                 # 2
            "+BT1420：鏡の城?空属性\x01",                 # 3
            "+BT1430：鏡の城?ボス\x01",                   # 4
            "+BT1450：鏡の城前（昼）\x01",                # 5
            "+BT1010：貴族邸街（昼）\x01",                # 6
            "+BT1020：ショッピングモール（昼）\x01",      # 7
            "+BT1030：テーマパーク前\x09",                # 8
            "（昼）\x01",                                 # 9
            "+BT103b：テーマパーク前\x09",                # 10
            "（夜）\x01",                                 # 11
            "+BT1300：テーマパーク広場（昼）\x01",        # 12
            "+BT130b：テーマパーク広場（夜）\x01",        # 13
            "+BT1310：ミシュラムビーチ（昼）\x01",        # 14
            "+BT1320：ミシュラムビーチ店前\x01",          # 15
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3614"),
        (1, "loc_3629"),
        (2, "loc_363E"),
        (3, "loc_3653"),
        (4, "loc_3668"),
        (5, "loc_367D"),
        (6, "loc_3692"),
        (7, "loc_36A7"),
        (8, "loc_36BC"),
        (9, "loc_36D1"),
        (10, "loc_36E6"),
        (11, "loc_36FB"),
        (12, "loc_3710"),
        (13, "loc_3725"),
        (SWITCH_DEFAULT, "loc_373A"),
    )


    label("loc_3614")

    Battle("BattleInfo_12E8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_3629")

    Battle("BattleInfo_132C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_363E")

    Battle("BattleInfo_1370", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_3653")

    Battle("BattleInfo_13B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_3668")

    Battle("BattleInfo_13F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_367D")

    Battle("BattleInfo_143C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_3692")

    Battle("BattleInfo_1480", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_36A7")

    Battle("BattleInfo_14C4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_36BC")

    Battle("BattleInfo_1508", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_36D1")

    Battle("BattleInfo_154C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_36E6")

    Battle("BattleInfo_1590", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_36FB")

    Battle("BattleInfo_15D4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_3710")

    Battle("BattleInfo_1618", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_3725")

    Battle("BattleInfo_165C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3744")

    label("loc_373A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3744")

    Jump("loc_340E")

    label("loc_3749")

    Jump("loc_41DB")

    label("loc_374E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AB5")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            " BM1000：星見の塔?室内（石）\x01",          # 0
            " BM1010：星見の塔?ボスマップ\x01",          # 1
            " BM1020：星見の塔?室内（クロス）\x01",      # 2
            " BM1030：星見の塔?室内（入口\x01",          # 3
            " BM1040：星見の塔?室内（書庫\x01",          # 4
            " BM1050：星見の塔?屋上\x01",                # 5
            "+BM1061：星見の塔（エンネア戦）\x01",       # 6
            "+BM1070：星見の塔?アリアンロード\x01",      # 7
            "+BM1080：星見の塔?入り口部分\x01",          # 8
            " BM2000：月の僧院\x01",                     # 9
            " BM2020：月の僧院?墓\x01",                  # 10
            " BM2050：月の僧院?野外\x01",                # 11
            " BM2099：月の僧院?ボス\x01",                # 12
            "+BM2060：月の僧院?異次元カンパネ\x01",      # 13
            "+BR2080：月の僧院?入り口前\x01",            # 14
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_396B"),
        (1, "loc_3980"),
        (2, "loc_3995"),
        (3, "loc_39AA"),
        (4, "loc_39BF"),
        (5, "loc_39D4"),
        (6, "loc_39E9"),
        (7, "loc_39FE"),
        (8, "loc_3A13"),
        (9, "loc_3A28"),
        (10, "loc_3A3D"),
        (11, "loc_3A52"),
        (12, "loc_3A67"),
        (13, "loc_3A7C"),
        (14, "loc_3A91"),
        (SWITCH_DEFAULT, "loc_3AA6"),
    )


    label("loc_396B")

    Battle("BattleInfo_16A0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3980")

    Battle("BattleInfo_16E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3995")

    Battle("BattleInfo_1728", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_39AA")

    Battle("BattleInfo_176C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_39BF")

    Battle("BattleInfo_17B0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_39D4")

    Battle("BattleInfo_17F4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_39E9")

    Battle("BattleInfo_1838", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_39FE")

    Battle("BattleInfo_187C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A13")

    Battle("BattleInfo_18C0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A28")

    Battle("BattleInfo_1904", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A3D")

    Battle("BattleInfo_1948", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A52")

    Battle("BattleInfo_198C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A67")

    Battle("BattleInfo_19D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A7C")

    Battle("BattleInfo_1A14", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3A91")

    Battle("BattleInfo_1A58", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3AB0")

    label("loc_3AA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AB0")

    Jump("loc_374E")

    label("loc_3AB5")

    Jump("loc_41DB")

    label("loc_3ABA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C63")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            " BR3000：古戦場\x01",                   # 0
            " BR3100：古戦場 室内\x01",              # 1
            "+BM4110：旧鉱山メイン?広場\x01",        # 2
            "+BM4120：旧鉱山メイン?ボス\x01",        # 3
            "+BM4130：旧鉱山メイン?EXTRA\x01",       # 4
            "+BM4150：旧鉱山抜け道?広場\x01",        # 5
            "+BM4160：旧鉱山抜け道?中ボス\x01",      # 6
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BC1"),
        (1, "loc_3BD6"),
        (2, "loc_3BEB"),
        (3, "loc_3C00"),
        (4, "loc_3C15"),
        (5, "loc_3C2A"),
        (6, "loc_3C3F"),
        (SWITCH_DEFAULT, "loc_3C54"),
    )


    label("loc_3BC1")

    Battle("BattleInfo_1A9C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3BD6")

    Battle("BattleInfo_1AE0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3BEB")

    Battle("BattleInfo_1B24", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3C00")

    Battle("BattleInfo_1B68", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3C15")

    Battle("BattleInfo_1BAC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3C2A")

    Battle("BattleInfo_1BF0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3C3F")

    Battle("BattleInfo_1C34", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3C5E")

    label("loc_3C54")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C5E")

    Jump("loc_3ABA")

    label("loc_3C63")

    Jump("loc_41DB")

    label("loc_3C68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EDF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "+BM4200：湿地帯?通常\x01",                # 0
            "+BM4210：湿地帯?滝あり\x01",              # 1
            "+BM4250：湿地帯?裏ボス\x01",              # 2
            "+BR4000：ノックス森林?街道\x09\x01",      # 3
            "+BR4010：ノックス森林?訓練地帯\x01",      # 4
            "+BR4020：ノックス森林?ボス\x01",          # 5
            "+BT6000：拘留施設?拘留部屋\x01",          # 6
            "+BT6010：拘留施設?通路\x01",              # 7
            "+BT6020：拘留施設?警備室\x01",            # 8
            "+BT6030：拘留施設?施設入口広場\x01",      # 9
            "+BT1510：病院正門前\x01",                 # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3DE9"),
        (1, "loc_3DFE"),
        (2, "loc_3E13"),
        (3, "loc_3E28"),
        (4, "loc_3E3D"),
        (5, "loc_3E52"),
        (6, "loc_3E67"),
        (7, "loc_3E7C"),
        (8, "loc_3E91"),
        (9, "loc_3EA6"),
        (10, "loc_3EBB"),
        (SWITCH_DEFAULT, "loc_3ED0"),
    )


    label("loc_3DE9")

    Battle("BattleInfo_1C78", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3DFE")

    Battle("BattleInfo_1CBC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E13")

    Battle("BattleInfo_1D00", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E28")

    Battle("BattleInfo_1D44", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E3D")

    Battle("BattleInfo_1D88", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E52")

    Battle("BattleInfo_1DCC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E67")

    Battle("BattleInfo_1E10", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E7C")

    Battle("BattleInfo_1E54", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3E91")

    Battle("BattleInfo_1E98", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3EA6")

    Battle("BattleInfo_1EDC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3EBB")

    Battle("BattleInfo_1F20", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_3EDA")

    label("loc_3ED0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EDA")

    Jump("loc_3C68")

    label("loc_3EDF")

    Jump("loc_41DB")

    label("loc_3EE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41DB")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "+BM9000：ラスダン?外郭\x01",            # 0
            "+BM9010：ラスダン?外部\x01",            # 1
            "+BM9020：ラスダン?内部\x01",            # 2
            "+BM9030：色の領域?通常\x01",            # 3
            "+BM9039：色の領域?ボス(昼)\x01",        # 4
            "+BM9040：象の領域?外部\x01",            # 5
            "+BM9041：象の領域?内部\x01",            # 6
            "+BM9049：象の領域?ボス\x01",            # 7
            "+BM9050：業の領域\x01",                 # 8
            "+BM9059：業の領域?ボス\x01",            # 9
            "+BM9060：戒の領域\x01",                 # 10
            "+BM9069：戒の領域?ボス\x01",            # 11
            "+BM9070：ラスダン?マリアベル\x01",      # 12
            "+BM9099：ラスダン?ラスボス\x01",        # 13
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_40A6"),
        (1, "loc_40BB"),
        (2, "loc_40D0"),
        (3, "loc_40E5"),
        (4, "loc_40FA"),
        (5, "loc_410F"),
        (6, "loc_4124"),
        (7, "loc_4139"),
        (8, "loc_414E"),
        (9, "loc_4163"),
        (10, "loc_4178"),
        (11, "loc_418D"),
        (12, "loc_41A2"),
        (13, "loc_41B7"),
        (SWITCH_DEFAULT, "loc_41CC"),
    )


    label("loc_40A6")

    Battle("BattleInfo_1F64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_40BB")

    Battle("BattleInfo_1FA8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_40D0")

    Battle("BattleInfo_1FEC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_40E5")

    Battle("BattleInfo_2030", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_40FA")

    Battle("BattleInfo_2074", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_410F")

    Battle("BattleInfo_20B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_4124")

    Battle("BattleInfo_20FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_4139")

    Battle("BattleInfo_2140", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_414E")

    Battle("BattleInfo_2184", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_4163")

    Battle("BattleInfo_21C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_4178")

    Battle("BattleInfo_220C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_418D")

    Battle("BattleInfo_2250", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_41A2")

    Battle("BattleInfo_2294", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_41B7")

    Battle("BattleInfo_22D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_41D6")

    label("loc_41CC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41D6")

    Jump("loc_3EE4")

    label("loc_41DB")

    Jump("loc_2332")

    label("loc_41E0")

    Return()

    # Function_2_232D end

    SaveToFile()

Try(main)
