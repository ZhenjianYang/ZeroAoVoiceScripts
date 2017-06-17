from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r3130.bin",                # FileName
        "r3130",                    # MapName
        "r3130",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -6000, 0, -16500, 0, 0, 1, 102, 0, 0, 0, 1],
    )

    BuildStringList((
        "r3130",                  # 0
        "br0000",                 # 1
        "br000b",                 # 2
        "br1000",                 # 3
        "br0100",                 # 4
        "br1500",                 # 5
        "br1510",                 # 6
        "br1520",                 # 7
        "br2000",                 # 8
        "br2010",                 # 9
        "br2040",                 # 10
        "br2050",                 # 11
        "br2060",                 # 12
        "br206b",                 # 13
        "br2070",                 # 14
        "br3000",                 # 15
        "br300b",                 # 16
        "br3100",                 # 17
        "bm1000",                 # 18
        "bm1010",                 # 19
        "bm1020",                 # 20
        "bm1030",                 # 21
        "bm1040",                 # 22
        "bm2000",                 # 23
        "bm2020",                 # 24
        "bm2050",                 # 25
        "bm2099",                 # 26
        "bm3000",                 # 27
        "bm3010",                 # 28
        "bm3020",                 # 29
        "bm3030",                 # 30
        "bm3040",                 # 31
        "bm3050",                 # 32
        "bm3060",                 # 33
        "bm3070",                 # 34
        "bm3080",                 # 35
        "bm3081",                 # 36
        "bm3090",                 # 37
        "bc130b",                 # 38
        "bc1400",                 # 39
        "bc140b",                 # 40
        "bc1410",                 # 41
        "bc141b",                 # 42
        "bc1420",                 # 43
        "bc0510",                 # 44
        "bc0520",                 # 45
        "bc0530",                 # 46
        "bc0540",                 # 47
        "bc0550",                 # 48
        "bc1460",                 # 49
        "bc1470",                 # 50
        "bm0000",                 # 51
        "bm0001",                 # 52
        "bm0002",                 # 53
        "bm0010",                 # 54
        "bm0011",                 # 55
        "bm0012",                 # 56
        "bm0013",                 # 57
        "bm0100",                 # 58
        "bm0101",                 # 59
        "bm0102",                 # 60
        "bm0110",                 # 61
        "bm0111",                 # 62
        "bm0112",                 # 63
        "bm0113",                 # 64
        "bm0114",                 # 65
        "bt050b",                 # 66
        "bt0600",                 # 67
        "bt0610",                 # 68
        "BT150b",                 # 69
        "BT152b",                 # 70
        "BT154b",                 # 71
        "BT160b",                 # 72
        "BT162b",                 # 73
        "BT163b",                 # 74
        "BT100b",                 # 75
        "BT101b",                 # 76
        "BT102b",                 # 77
        "BT110b",                 # 78
        "BT111b",                 # 79
        "BT112b",                 # 80
        "BT113b",                 # 81
        "BT114b",                 # 82
        "BT115b",                 # 83
    ))

    ATBonus("ATBonus_1A0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_1E0", 100, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_1F0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_274", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_278", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_27C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_284", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_288", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)

    # monster count: 0

    # event battle count: 83

    BattleInfo(
        "BattleInfo_2F0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_334", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br000b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_378", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_400", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_444", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_488", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br1520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4CC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02100.dat", "ms02200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_554", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_598", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_620", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br206b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_664", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br2070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_774", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7B8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7FC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_840", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_884", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8C8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_90C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02100.dat", "ms02200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_950", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_994", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm2099", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6A8", 0x0010, 3, 6, 3, 90, 1, 1000, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1E0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6EC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br300b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "br3100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A1C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A60", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AA4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3030", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AE8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B2C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B70", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BF8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3080", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C3C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3081", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_C80", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm3090", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_CC4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D08", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D4C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc140b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_D90", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1410", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_DD4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc141b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_E18", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1420", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_EA0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_EE4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F28", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_F6C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc0550", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_FB0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1460", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_FF4", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bc1470", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1038", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_107C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0001", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_10C0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0002", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1104", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1148", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0011", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_118C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0012", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_11D0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0013", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1214", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1258", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0101", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_129C", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0102", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_12E0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0110", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1324", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0111", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1368", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0112", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_13AC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_13F0", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bm0114", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1434", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bt050b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1478", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bt0600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_14BC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "bt0610", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1500", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT150b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1544", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1588", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT154b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_15CC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT160b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1610", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT162b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1654", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT163b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1698", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT100b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_16DC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT101b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1720", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT102b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1764", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT110b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_17A8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT111b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_17EC", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT112b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1830", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT113b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_1874", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT114b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_18B8", 0x0000, 3, 6, 3, 90, 1, 1000, 0, "BT115b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65000.dat", "ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1F0", "MonsterBattlePostion_270", "ed7400", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    DeclActor(6500,    100,     7500,    1200,    6000,    1100,    -10500,  0x007C, 0,  2,  0x0000)
    DeclActor(6500,    100,     0,       1200,    -6000,   1100,    28500,   0x007C, 0,  3,  0x0000)
    DeclActor(6500,    100,     -7500,   1200,    -6000,   1100,    28500,   0x007C, 0,  4,  0x0000)
    DeclActor(6500,    100,     -25000,  1200,    -6000,   1100,    28500,   0x007C, 0,  5,  0x0000)
    DeclActor(6500,    100,     -29500,  1200,    -6000,   1100,    28500,   0x007C, 0,  6,  0x0000)
    DeclActor(6500,    100,     -35000,  1200,    -6000,   1100,    28500,   0x007C, 0,  7,  0x0000)
    DeclActor(6500,    100,     -42000,  1200,    -6000,   1100,    28500,   0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_1938",         # 00, 0
        "Function_1_1939",         # 01, 1
        "Function_2_193A",         # 02, 2
        "Function_3_1C0E",         # 03, 3
        "Function_4_1E03",         # 04, 4
        "Function_5_2142",         # 05, 5
        "Function_6_2491",         # 06, 6
        "Function_7_2808",         # 07, 7
        "Function_8_2BB7",         # 08, 8
    ))


    def Function_0_1938(): pass

    label("Function_0_1938")

    Return()

    # Function_0_1938 end

    def Function_1_1939(): pass

    label("Function_1_1939")

    Return()

    # Function_1_1939 end

    def Function_2_193A(): pass

    label("Function_2_193A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1944")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BFD")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "br0000 东街道\x01",                # 0
            "br000b 东街道（夜之桥）\x01",      # 1
            "br1000 西街道\x01",                # 2
            "br0100 阿尔摩利卡\x01",            # 3
            "br1500 乌尔斯拉崖边\x01",          # 4
            "br1510 乌尔斯拉森林\x01",          # 5
            "br1520 乌尔斯拉水边\x01",          # 6
            "br2000 玛因兹\x01",                # 7
            "br2010 玛因兹河沿\x01",            # 8
            "br2040 玛因兹坑道\x01",            # 9
            "br2050 玛因兹随到\x01",            # 10
            "br2060 玛因兹高地\x01",            # 11
            "br206b 玛因兹高地（夜）\x01",      # 12
            "br2070 玛因兹高地崖边\x01",        # 13
            "取消\x01",                         # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AC8"),
        (1, "loc_1ADD"),
        (2, "loc_1AF2"),
        (3, "loc_1B07"),
        (4, "loc_1B1C"),
        (5, "loc_1B31"),
        (6, "loc_1B46"),
        (7, "loc_1B5B"),
        (8, "loc_1B70"),
        (9, "loc_1B85"),
        (10, "loc_1B9A"),
        (11, "loc_1BAF"),
        (12, "loc_1BC4"),
        (13, "loc_1BD9"),
        (SWITCH_DEFAULT, "loc_1BEE"),
    )


    label("loc_1AC8")

    Battle("BattleInfo_2F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1ADD")

    Battle("BattleInfo_334", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1AF2")

    Battle("BattleInfo_378", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B07")

    Battle("BattleInfo_3BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B1C")

    Battle("BattleInfo_400", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B31")

    Battle("BattleInfo_444", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B46")

    Battle("BattleInfo_488", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B5B")

    Battle("BattleInfo_4CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B70")

    Battle("BattleInfo_510", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B85")

    Battle("BattleInfo_554", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1B9A")

    Battle("BattleInfo_598", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1BAF")

    Battle("BattleInfo_5DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1BC4")

    Battle("BattleInfo_620", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1BD9")

    Battle("BattleInfo_664", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BEE")

    label("loc_1BEE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1944")

    label("loc_1BFD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_2_193A end

    def Function_3_1C0E(): pass

    label("Function_3_1C0E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bm1000 星见之塔１\x01",                # 0
            "bm1010 星见之塔ＢＯＳＳ房间\x01",      # 1
            "bm1020 星见之塔２\x01",                # 2
            "bm1030 星见之塔入口\x01",              # 3
            "bm1040 星见之塔图书室\x01",            # 4
            "bm2000 僧院\x01",                      # 5
            "bm2020 僧院墓地\x01",                  # 6
            "bm2050 僧院室外\x01",                  # 7
            "bm2099 僧院ＢＯＳＳ房间\x01",          # 8
            "取消\x01",                             # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D26"),
        (1, "loc_1D3B"),
        (2, "loc_1D50"),
        (3, "loc_1D65"),
        (4, "loc_1D7A"),
        (5, "loc_1D8F"),
        (6, "loc_1DA4"),
        (7, "loc_1DB9"),
        (8, "loc_1DCE"),
        (SWITCH_DEFAULT, "loc_1DE3"),
    )


    label("loc_1D26")

    Battle("BattleInfo_774", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1D3B")

    Battle("BattleInfo_7B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1D50")

    Battle("BattleInfo_7FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1D65")

    Battle("BattleInfo_840", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1D7A")

    Battle("BattleInfo_884", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1D8F")

    Battle("BattleInfo_8C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1DA4")

    Battle("BattleInfo_90C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1DB9")

    Battle("BattleInfo_950", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1DCE")

    Battle("BattleInfo_994", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DE3")

    label("loc_1DE3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C18")

    label("loc_1DF2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_1C0E end

    def Function_4_1E03(): pass

    label("Function_4_1E03")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2131")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "br3000 古战场\x01",                            # 0
            "br300b 古战场（夜）\x01",                      # 1
            "br3100 古战场　室内\x01",                      # 2
            "bm3000 太阳堡垒第１层\x01",                    # 3
            "bm3010 太阳堡垒实验室\x01",                    # 4
            "bm3020 太阳堡垒第３层\x01",                    # 5
            "bm3030 太阳堡垒第４层　室内\x01",              # 6
            "bm3040 太阳堡垒第４层　室外\x01",              # 7
            "bm3050 最终ＢＯＳＳ（人类ver）\x01",           # 8
            "bm3060 最终ＢＯＳＳ（魔神ver）\x01",           # 9
            "bm3070 最终ＢＯＳＳ（红魔神ver）\x01",         # 10
            "bm3080 太阳堡垒３→４层竖坑\x01",              # 11
            "bm3081 太阳堡垒３→４层竖坑（红）\x01",        # 12
            "bm3090 太阳堡垒３→４层中级ＢＯＳＳ\x01",      # 13
            "取消\x01",                                     # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FFC"),
        (1, "loc_2011"),
        (2, "loc_2026"),
        (3, "loc_203B"),
        (4, "loc_2050"),
        (5, "loc_2065"),
        (6, "loc_207A"),
        (7, "loc_208F"),
        (8, "loc_20A4"),
        (9, "loc_20B9"),
        (10, "loc_20CE"),
        (11, "loc_20E3"),
        (12, "loc_20F8"),
        (13, "loc_210D"),
        (SWITCH_DEFAULT, "loc_2122"),
    )


    label("loc_1FFC")

    Battle("BattleInfo_6A8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_2011")

    Battle("BattleInfo_6EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_2026")

    Battle("BattleInfo_730", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_203B")

    Battle("BattleInfo_9D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_2050")

    Battle("BattleInfo_A1C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_2065")

    Battle("BattleInfo_A60", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_207A")

    Battle("BattleInfo_AA4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_208F")

    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_20A4")

    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_20B9")

    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_20CE")

    Battle("BattleInfo_BB4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_20E3")

    Battle("BattleInfo_BF8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_20F8")

    Battle("BattleInfo_C3C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_210D")

    Battle("BattleInfo_C80", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2122")

    label("loc_2122")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E0D")

    label("loc_2131")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_4_1E03 end

    def Function_5_2142(): pass

    label("Function_5_2142")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_214C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2480")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bc130b IBC前（夜）\x01",                   # 0
            "bc1400 旧市街１\x01",                      # 1
            "bc140b 旧市街１（夜）\x01",                # 2
            "bc1410 旧市街２\x01",                      # 3
            "bc141b 旧市街２（夜）\x01",                # 4
            "bc1420 旧车库·鬼火\x01",                  # 5
            "bc0520 鲁巴彻右（一般道路）\x01",          # 6
            "bc0530 鲁巴彻右（ＢＯＳＳ广场）\x01",      # 7
            "bc0540 鲁巴彻左（一般道路）\x01",          # 8
            "bc0550 鲁巴彻左（ＢＯＳＳ广场）\x01",      # 9
            "bc1460 废弃公寓室内\x01",                  # 10
            "bc1470 废弃公寓走廊\x01",                  # 11
            "bm0000 地下空间A初期广阔区域\x01",         # 12
            "bm0001 地下空间A初期道路\x01",             # 13
            "bm0002 地下空间A初期ＢＯＳＳ\x01",         # 14
            "取消\x01",                                 # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2336"),
        (1, "loc_234B"),
        (2, "loc_2360"),
        (3, "loc_2375"),
        (4, "loc_238A"),
        (5, "loc_239F"),
        (6, "loc_23B4"),
        (7, "loc_23C9"),
        (8, "loc_23DE"),
        (9, "loc_23F3"),
        (10, "loc_2408"),
        (11, "loc_241D"),
        (12, "loc_2432"),
        (13, "loc_2447"),
        (14, "loc_245C"),
        (SWITCH_DEFAULT, "loc_2471"),
    )


    label("loc_2336")

    Battle("BattleInfo_CC4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_234B")

    Battle("BattleInfo_D08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_2360")

    Battle("BattleInfo_D4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_2375")

    Battle("BattleInfo_D90", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_238A")

    Battle("BattleInfo_DD4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_239F")

    Battle("BattleInfo_E18", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_23B4")

    Battle("BattleInfo_EA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_23C9")

    Battle("BattleInfo_EE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_23DE")

    Battle("BattleInfo_F28", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_23F3")

    Battle("BattleInfo_F6C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_2408")

    Battle("BattleInfo_FB0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_241D")

    Battle("BattleInfo_FF4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_2432")

    Battle("BattleInfo_1038", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_2447")

    Battle("BattleInfo_107C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_245C")

    Battle("BattleInfo_10C0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2471")

    label("loc_2471")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_214C")

    label("loc_2480")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_5_2142 end

    def Function_6_2491(): pass

    label("Function_6_2491")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_249B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27F7")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bm0010 地下空间A后期广阔区域\x01",          # 0
            "bm0011 地下空间A后期道路\x01",              # 1
            "bm0012 地下空间A后期ＢＯＳＳ\x01",          # 2
            "bm0013 地下空间A后期管道\x01",              # 3
            "bm0100 地下空间B初期广阔区域\x01",          # 4
            "bm0101 地下空间B初期道路\x01",              # 5
            "bm0102 地下空间B初期ＢＯＳＳ\x01",          # 6
            "bm0110 地下空间B后期广阔区域\x01",          # 7
            "bm0111 地下空间B后期道路\x01",              # 8
            "bm0112 地下空间B后期ＢＯＳＳ\x01",          # 9
            "bm0111 地下空间B后期冰冻广阔区域\x01",      # 10
            "bm0112 地下空间B后期冰冻道路\x01",          # 11
            "bt050b 玛因兹镇（夜）\x01",                 # 12
            "bt0600 矿山（无水）\x01",                   # 13
            "bt0610 矿山（有水）\x01",                   # 14
            "取消\x01",                                  # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26AD"),
        (1, "loc_26C2"),
        (2, "loc_26D7"),
        (3, "loc_26EC"),
        (4, "loc_2701"),
        (5, "loc_2716"),
        (6, "loc_272B"),
        (7, "loc_2740"),
        (8, "loc_2755"),
        (9, "loc_276A"),
        (10, "loc_277F"),
        (11, "loc_2794"),
        (12, "loc_27A9"),
        (13, "loc_27BE"),
        (14, "loc_27D3"),
        (SWITCH_DEFAULT, "loc_27E8"),
    )


    label("loc_26AD")

    Battle("BattleInfo_1104", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_26C2")

    Battle("BattleInfo_1148", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_26D7")

    Battle("BattleInfo_118C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_26EC")

    Battle("BattleInfo_11D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_2701")

    Battle("BattleInfo_1214", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_2716")

    Battle("BattleInfo_1258", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_272B")

    Battle("BattleInfo_129C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_2740")

    Battle("BattleInfo_12E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_2755")

    Battle("BattleInfo_1324", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_276A")

    Battle("BattleInfo_1368", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_277F")

    Battle("BattleInfo_13AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_2794")

    Battle("BattleInfo_13F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_27A9")

    Battle("BattleInfo_1434", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_27BE")

    Battle("BattleInfo_1478", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_27D3")

    Battle("BattleInfo_14BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27E8")

    label("loc_27E8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_249B")

    label("loc_27F7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_6_2491 end

    def Function_7_2808(): pass

    label("Function_7_2808")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "BT150b 医科大学外部（夜）\x01",              # 0
            "BT152b 医科大·食堂住宿设施（夜）\x01",      # 1
            "BT154b 医科大·病房楼走廊（夜）\x01",        # 2
            "BT160b 医科大·楼顶（夜）\x01",              # 3
            "BT162b 医科大·研究楼走廊（夜）\x01",        # 4
            "BT163b 医科大·ＢＯＳＳ（夜）\x01",          # 5
            "BT100b 米修拉姆酒店外部（夜）\x01",          # 6
            "BT101b 米修拉姆贵族宅邸街（夜）\x01",        # 7
            "BT102b 米修拉姆酒店外部（夜）\x01",          # 8
            "BT110b 米修拉姆贵族宅邸前（夜）\x01",        # 9
            "BT111b 贵族宅邸内部走廊（夜）\x01",          # 10
            "BT112b 贵族宅邸内部道路（夜）\x01",          # 11
            "BT113b 贵族宅邸内部房间（夜）\x01",          # 12
            "BT114b 贵族宅邸内部大厅（夜）\x01",          # 13
            "BT115b 贵族宅邸特殊大厅（夜）\x01",          # 14
            "取消\x01",                                   # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A5C"),
        (1, "loc_2A71"),
        (2, "loc_2A86"),
        (3, "loc_2A9B"),
        (4, "loc_2AB0"),
        (5, "loc_2AC5"),
        (6, "loc_2ADA"),
        (7, "loc_2AEF"),
        (8, "loc_2B04"),
        (9, "loc_2B19"),
        (10, "loc_2B2E"),
        (11, "loc_2B43"),
        (12, "loc_2B58"),
        (13, "loc_2B6D"),
        (14, "loc_2B82"),
        (SWITCH_DEFAULT, "loc_2B97"),
    )


    label("loc_2A5C")

    Battle("BattleInfo_1500", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2A71")

    Battle("BattleInfo_1544", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2A86")

    Battle("BattleInfo_1588", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2A9B")

    Battle("BattleInfo_15CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2AB0")

    Battle("BattleInfo_1610", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2AC5")

    Battle("BattleInfo_1654", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2ADA")

    Battle("BattleInfo_1698", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2AEF")

    Battle("BattleInfo_16DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B04")

    Battle("BattleInfo_1720", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B19")

    Battle("BattleInfo_1764", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B2E")

    Battle("BattleInfo_17A8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B43")

    Battle("BattleInfo_17EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B58")

    Battle("BattleInfo_1830", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B6D")

    Battle("BattleInfo_1874", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B82")

    Battle("BattleInfo_18B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B97")

    label("loc_2B97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2812")

    label("loc_2BA6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_7_2808 end

    def Function_8_2BB7(): pass

    label("Function_8_2BB7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C1A")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "预约\x01",      # 0
            "取消\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BF6"),
        (SWITCH_DEFAULT, "loc_2C0B"),
    )


    label("loc_2BF6")

    Battle("BattleInfo_1500", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C0B")

    label("loc_2C0B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BC1")

    label("loc_2C1A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_8_2BB7 end

    SaveToFile()

Try(main)
