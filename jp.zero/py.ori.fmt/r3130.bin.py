from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_3_1C2A",         # 03, 3
        "Function_4_1E25",         # 04, 4
        "Function_5_214B",         # 05, 5
        "Function_6_24AA",         # 06, 6
        "Function_7_280F",         # 07, 7
        "Function_8_2BB8",         # 08, 8
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C19")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "br0000 東街道\x01",                  # 0
            "br000b 東街道（夜の橋）\x01",        # 1
            "br1000 西街道\x01",                  # 2
            "br0100 アルモリカ\x01",              # 3
            "br1500 ウルスラ崖沿い\x01",          # 4
            "br1510 ウルスラ森\x01",              # 5
            "br1520 ウルスラ水辺\x01",            # 6
            "br2000 マインツ\x01",                # 7
            "br2010 マインツ川沿い\x01",          # 8
            "br2040 マインツ坑道\x01",            # 9
            "br2050 マインツトンネル\x01",        # 10
            "br2060 マインツ高台\x01",            # 11
            "br206b マインツ高台（夜）\x01",      # 12
            "br2070 マインツ高台崖沿い\x01",      # 13
            "キャンセル\x01",                     # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AE4"),
        (1, "loc_1AF9"),
        (2, "loc_1B0E"),
        (3, "loc_1B23"),
        (4, "loc_1B38"),
        (5, "loc_1B4D"),
        (6, "loc_1B62"),
        (7, "loc_1B77"),
        (8, "loc_1B8C"),
        (9, "loc_1BA1"),
        (10, "loc_1BB6"),
        (11, "loc_1BCB"),
        (12, "loc_1BE0"),
        (13, "loc_1BF5"),
        (SWITCH_DEFAULT, "loc_1C0A"),
    )


    label("loc_1AE4")

    Battle("BattleInfo_2F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1AF9")

    Battle("BattleInfo_334", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B0E")

    Battle("BattleInfo_378", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B23")

    Battle("BattleInfo_3BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B38")

    Battle("BattleInfo_400", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B4D")

    Battle("BattleInfo_444", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B62")

    Battle("BattleInfo_488", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B77")

    Battle("BattleInfo_4CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1B8C")

    Battle("BattleInfo_510", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1BA1")

    Battle("BattleInfo_554", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1BB6")

    Battle("BattleInfo_598", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1BCB")

    Battle("BattleInfo_5DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1BE0")

    Battle("BattleInfo_620", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1BF5")

    Battle("BattleInfo_664", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1C0A")

    label("loc_1C0A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1944")

    label("loc_1C19")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_2_193A end

    def Function_3_1C2A(): pass

    label("Function_3_1C2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E14")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bm1000 星見の塔１\x01",                # 0
            "bm1010 星見の塔ボス部屋\x01",          # 1
            "bm1020 星見の塔２\x01",                # 2
            "bm1030 星見の塔エントランス\x01",      # 3
            "bm1040 星見の塔図書室\x01",            # 4
            "bm2000 僧院\x01",                      # 5
            "bm2020 僧院墓所\x01",                  # 6
            "bm2050 僧院屋外\x01",                  # 7
            "bm2099 僧院ボス部屋\x01",              # 8
            "キャンセル\x01",                       # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D48"),
        (1, "loc_1D5D"),
        (2, "loc_1D72"),
        (3, "loc_1D87"),
        (4, "loc_1D9C"),
        (5, "loc_1DB1"),
        (6, "loc_1DC6"),
        (7, "loc_1DDB"),
        (8, "loc_1DF0"),
        (SWITCH_DEFAULT, "loc_1E05"),
    )


    label("loc_1D48")

    Battle("BattleInfo_774", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1D5D")

    Battle("BattleInfo_7B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1D72")

    Battle("BattleInfo_7FC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1D87")

    Battle("BattleInfo_840", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1D9C")

    Battle("BattleInfo_884", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1DB1")

    Battle("BattleInfo_8C8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1DC6")

    Battle("BattleInfo_90C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1DDB")

    Battle("BattleInfo_950", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1DF0")

    Battle("BattleInfo_994", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1E05")

    label("loc_1E05")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C34")

    label("loc_1E14")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_1C2A end

    def Function_4_1E25(): pass

    label("Function_4_1E25")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_213A")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "br3000 古戦場\x01",                          # 0
            "br300b 古戦場（夜）\x01",                    # 1
            "br3100 古戦場 室内\x01",                     # 2
            "bm3000 太陽の砦１層\x01",                    # 3
            "bm3010 太陽の砦ラボ\x01",                    # 4
            "bm3020 太陽の砦３層\x01",                    # 5
            "bm3030 太陽の砦４層 屋内\x01",               # 6
            "bm3040 太陽の砦４層 屋外\x01",               # 7
            "bm3050 ラスボス（人間ver）\x01",             # 8
            "bm3060 ラスボス（魔神ver）\x01",             # 9
            "bm3070 ラスボス（魔神赤ver）\x01",           # 10
            "bm3080 太陽の砦３→４層縦穴\x01",            # 11
            "bm3081 太陽の砦３→４層縦穴（赤）\x01",      # 12
            "bm3090 太陽の砦３→４層中ボス\x01",          # 13
            "キャンセル\x01",                             # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2005"),
        (1, "loc_201A"),
        (2, "loc_202F"),
        (3, "loc_2044"),
        (4, "loc_2059"),
        (5, "loc_206E"),
        (6, "loc_2083"),
        (7, "loc_2098"),
        (8, "loc_20AD"),
        (9, "loc_20C2"),
        (10, "loc_20D7"),
        (11, "loc_20EC"),
        (12, "loc_2101"),
        (13, "loc_2116"),
        (SWITCH_DEFAULT, "loc_212B"),
    )


    label("loc_2005")

    Battle("BattleInfo_6A8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_201A")

    Battle("BattleInfo_6EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_202F")

    Battle("BattleInfo_730", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_2044")

    Battle("BattleInfo_9D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_2059")

    Battle("BattleInfo_A1C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_206E")

    Battle("BattleInfo_A60", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_2083")

    Battle("BattleInfo_AA4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_2098")

    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_20AD")

    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_20C2")

    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_20D7")

    Battle("BattleInfo_BB4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_20EC")

    Battle("BattleInfo_BF8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_2101")

    Battle("BattleInfo_C3C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_2116")

    Battle("BattleInfo_C80", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_212B")

    label("loc_212B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E2F")

    label("loc_213A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_4_1E25 end

    def Function_5_214B(): pass

    label("Function_5_214B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2155")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2499")

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
            "bc1420 ガレージ・イグニス\x01",            # 5
            "bc0520 ルバーチェ右（通常通路）\x01",      # 6
            "bc0530 ルバーチェ右（ボス広場）\x01",      # 7
            "bc0540 ルバーチェ左（通常通路）\x01",      # 8
            "bc0550 ルバーチェ左（ボス広場）\x01",      # 9
            "bc1460 廃アパート室内\x01",                # 10
            "bc1470 廃アパート廊下\x01",                # 11
            "bm0000 ジオフロA初期広間\x01",             # 12
            "bm0001 ジオフロA初期通路\x01",             # 13
            "bm0002 ジオフロA初期ボス\x01",             # 14
            "キャンセル\x01",                           # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_234F"),
        (1, "loc_2364"),
        (2, "loc_2379"),
        (3, "loc_238E"),
        (4, "loc_23A3"),
        (5, "loc_23B8"),
        (6, "loc_23CD"),
        (7, "loc_23E2"),
        (8, "loc_23F7"),
        (9, "loc_240C"),
        (10, "loc_2421"),
        (11, "loc_2436"),
        (12, "loc_244B"),
        (13, "loc_2460"),
        (14, "loc_2475"),
        (SWITCH_DEFAULT, "loc_248A"),
    )


    label("loc_234F")

    Battle("BattleInfo_CC4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_2364")

    Battle("BattleInfo_D08", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_2379")

    Battle("BattleInfo_D4C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_238E")

    Battle("BattleInfo_D90", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_23A3")

    Battle("BattleInfo_DD4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_23B8")

    Battle("BattleInfo_E18", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_23CD")

    Battle("BattleInfo_EA0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_23E2")

    Battle("BattleInfo_EE4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_23F7")

    Battle("BattleInfo_F28", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_240C")

    Battle("BattleInfo_F6C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_2421")

    Battle("BattleInfo_FB0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_2436")

    Battle("BattleInfo_FF4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_244B")

    Battle("BattleInfo_1038", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_2460")

    Battle("BattleInfo_107C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_2475")

    Battle("BattleInfo_10C0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_248A")

    label("loc_248A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2155")

    label("loc_2499")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_5_214B end

    def Function_6_24AA(): pass

    label("Function_6_24AA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27FE")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "bm0010 ジオフロA後期広間\x01",        # 0
            "bm0011 ジオフロA後期通路\x01",        # 1
            "bm0012 ジオフロA後期ボス\x01",        # 2
            "bm0013 ジオフロA後期ダクト\x01",      # 3
            "bm0100 ジオフロB初期広間\x01",        # 4
            "bm0101 ジオフロB初期通路\x01",        # 5
            "bm0102 ジオフロB初期ボス\x01",        # 6
            "bm0110 ジオフロB後期広間\x01",        # 7
            "bm0111 ジオフロB後期通路\x01",        # 8
            "bm0112 ジオフロB後期ボス\x01",        # 9
            "bm0111 ジオフロB後期氷広間\x01",      # 10
            "bm0112 ジオフロB後期氷通路\x01",      # 11
            "bt050b マインツ町（夜）\x01",         # 12
            "bt0600 鉱山（水無し）\x01",           # 13
            "bt0610 鉱山（水あり）\x01",           # 14
            "キャンセル\x01",                      # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26B4"),
        (1, "loc_26C9"),
        (2, "loc_26DE"),
        (3, "loc_26F3"),
        (4, "loc_2708"),
        (5, "loc_271D"),
        (6, "loc_2732"),
        (7, "loc_2747"),
        (8, "loc_275C"),
        (9, "loc_2771"),
        (10, "loc_2786"),
        (11, "loc_279B"),
        (12, "loc_27B0"),
        (13, "loc_27C5"),
        (14, "loc_27DA"),
        (SWITCH_DEFAULT, "loc_27EF"),
    )


    label("loc_26B4")

    Battle("BattleInfo_1104", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_26C9")

    Battle("BattleInfo_1148", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_26DE")

    Battle("BattleInfo_118C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_26F3")

    Battle("BattleInfo_11D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_2708")

    Battle("BattleInfo_1214", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_271D")

    Battle("BattleInfo_1258", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_2732")

    Battle("BattleInfo_129C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_2747")

    Battle("BattleInfo_12E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_275C")

    Battle("BattleInfo_1324", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_2771")

    Battle("BattleInfo_1368", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_2786")

    Battle("BattleInfo_13AC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_279B")

    Battle("BattleInfo_13F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_27B0")

    Battle("BattleInfo_1434", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_27C5")

    Battle("BattleInfo_1478", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_27DA")

    Battle("BattleInfo_14BC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27EF")

    label("loc_27EF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24B4")

    label("loc_27FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_6_24AA end

    def Function_7_280F(): pass

    label("Function_7_280F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2819")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA7")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "BT150b 医科大学外観（夜）\x01",              # 0
            "BT152b 医科大・食堂宿泊（夜）\x01",          # 1
            "BT154b 医科大・病棟廊下（夜）\x01",          # 2
            "BT160b 医科大・屋上（夜）\x01",              # 3
            "BT162b 医科大・研究棟廊下（夜）\x01",        # 4
            "BT163b 医科大・ボス（夜）\x01",              # 5
            "BT100b ミシュラムホテル外観（夜）\x01",      # 6
            "BT101b ミシュラム貴族邸街（夜）\x01",        # 7
            "BT102b ミシュラムホテル内部（夜）\x01",      # 8
            "BT110b ミシュラム貴族邸前（夜）\x01",        # 9
            "BT111b 貴族邸内部廊下（夜）\x01",            # 10
            "BT112b 貴族邸内部通路（夜）\x01",            # 11
            "BT113b 貴族邸内部部屋（夜）\x01",            # 12
            "BT114b 貴族邸内部広間（夜）\x01",            # 13
            "BT115b 貴族邸特殊広間（夜）\x01",            # 14
            "キャンセル\x01",                             # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A5D"),
        (1, "loc_2A72"),
        (2, "loc_2A87"),
        (3, "loc_2A9C"),
        (4, "loc_2AB1"),
        (5, "loc_2AC6"),
        (6, "loc_2ADB"),
        (7, "loc_2AF0"),
        (8, "loc_2B05"),
        (9, "loc_2B1A"),
        (10, "loc_2B2F"),
        (11, "loc_2B44"),
        (12, "loc_2B59"),
        (13, "loc_2B6E"),
        (14, "loc_2B83"),
        (SWITCH_DEFAULT, "loc_2B98"),
    )


    label("loc_2A5D")

    Battle("BattleInfo_1500", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2A72")

    Battle("BattleInfo_1544", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2A87")

    Battle("BattleInfo_1588", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2A9C")

    Battle("BattleInfo_15CC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2AB1")

    Battle("BattleInfo_1610", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2AC6")

    Battle("BattleInfo_1654", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2ADB")

    Battle("BattleInfo_1698", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2AF0")

    Battle("BattleInfo_16DC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B05")

    Battle("BattleInfo_1720", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B1A")

    Battle("BattleInfo_1764", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B2F")

    Battle("BattleInfo_17A8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B44")

    Battle("BattleInfo_17EC", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B59")

    Battle("BattleInfo_1830", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B6E")

    Battle("BattleInfo_1874", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B83")

    Battle("BattleInfo_18B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2B98")

    label("loc_2B98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2819")

    label("loc_2BA7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_7_280F end

    def Function_8_2BB8(): pass

    label("Function_8_2BB8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C25")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "リザーブ\x01",        # 0
            "キャンセル\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C01"),
        (SWITCH_DEFAULT, "loc_2C16"),
    )


    label("loc_2C01")

    Battle("BattleInfo_1500", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2C16")

    label("loc_2C16")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BC2")

    label("loc_2C25")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_8_2BB8 end

    SaveToFile()

Try(main)
