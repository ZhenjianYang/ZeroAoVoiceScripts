from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1540.bin",                # FileName
        "c1540",                    # MapName
        "c1540",                    # Location
        0x00AF,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 175, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1540",                  # 0
        "レクター書記官",         # 1
        "ミュラー少佐",           # 2
        "ユリア准佐",             # 3
        "キリカ補佐官",           # 4
        "共和国軍将校",           # 5
        "帝国軍将校",             # 6
        "共和国軍将校",           # 7
        "帝国軍将校",             # 8
        "王室親衛隊隊士",         # 9
        "公室護衛官",             # 10
        "公室護衛官",             # 11
        "執事",                   # 12
        "執事",                   # 13
        "メイド",                 # 14
        "メイド",                 # 15
        "アリオス",               # 16
        "市役所職員",             # 17
        "ピエール副局長",         # 18
        "警官",                   # 19
        "警官",                   # 20
        "警官",                   # 21
        "ディーター市長",         # 22
        "オズボーン宰相",         # 23
        "オリヴァルト皇子",       # 24
        "クローディア姫",         # 25
        "アルバート大公",         # 26
        "ロックスミス大統領",     # 27
        "マクダエル議長",         # 28
        "イアン弁護士",           # 29
        "ダドリー捜査官",         # 30
        "帝国系テロリスト",       # 31
        "帝国系テロリスト",       # 32
        "帝国系テロリスト",       # 33
        "帝国系テロリスト",       # 34
        "帝国系テロリスト",       # 35
        "帝国系テロリスト",       # 36
        "帝国系テロリスト",       # 37
        "帝国系テロリスト",       # 38
        "共和国系テロリスト",     # 39
        "共和国系テロリスト",     # 40
        "共和国系テロリスト",     # 41
        "共和国系テロリスト",     # 42
        "共和国系テロリスト",     # 43
        "共和国系テロリスト",     # 44
        "共和国系テロリスト",     # 45
        "共和国系テロリスト",     # 46
        "警官",                   # 47
        "警官",                   # 48
        "警官",                   # 49
        "警官",                   # 50
        "警備隊員",               # 51
        "警備隊員",               # 52
        "ダミー",                 # 53
        "グレイス",               # 54
        "レインズ",               # 55
        "記者",                   # 56
        "記者",                   # 57
        "記者",                   # 58
        "記者",                   # 59
        "記者",                   # 60
        "飛空挺",                 # 61
        "飛空挺",                 # 62
        "椅子",                   # 63
        "椅子",                   # 64
        "ノートパソコン",         # 65
        "イベント用モンスター",   # 66
        "イベント用モンスター",   # 67
        "イベント用モンスター",   # 68
        "SE制御",                 # 69
        "bc1560",                 # 70
    ))

    ATBonus("ATBonus_A70", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B50", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B54", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B58", 11, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B5C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B60", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B64", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B68", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B6C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B30", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_B34", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_B38", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_B3C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_B40", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_B44", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_B48", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_B70", 0x000A, 3, 6, 45, 3, 3, 30, 0, "bc1560", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84101.dat", "ms84301.dat", "ms84201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B50", "MonsterBattlePostion_B30", "ed7544", "ed7453", "ATBonus_A70"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch11300.itc",                   # 01
        "chr/ch11200.itc",                   # 02
        "chr/ch13300.itc",                   # 03
        "chr/ch12400.itc",                   # 04
        "chr/ch41200.itc",                   # 05
        "chr/ch41000.itc",                   # 06
        "chr/ch41600.itc",                   # 07
        "chr/ch28600.itc",                   # 08
        "chr/ch25900.itc",                   # 09
        "chr/ch25600.itc",                   # 0A
        "chr/ch02400.itc",                   # 0B
        "chr/ch25800.itc",                   # 0C
        "chr/ch27800.itc",                   # 0D
        "chr/ch28200.itc",                   # 0E
        "chr/ch06400.itc",                   # 0F
        "chr/ch13302.itc",                   # 10
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(171350,  0,       74290,   270,  453,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(174860,  0,       72669,   270,  453,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(85529,   0,       80650,   135,  453,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(88940,   0,       80209,   135,  453,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(171059,  0,       78610,   270,  453,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(87379,   0,       80379,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(172130,  0,       77980,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(175050,  0,       71419,   271,  389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(88099,   0,       72809,   89,   389,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(88260,   0,       71559,   89,   389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(170720,  0,       82220,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52180,  0,       124000,  180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(173529,  0,       74540,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-49459,  0,       112459,  89,   389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(86529,   0,       80650,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-52000,  0,       120730,  0,    389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-41799,  0,       128199,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 28,  86.02999877929688,     83.37000274658203,     -1.0,                  5184.0,                [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -7.169166564941406,    -6.947500228881836,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 29,  36.47999954223633,     0.0,                   -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -12.15999984741211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 133, 9.699999809265137,     3.5,                   -1.0,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.2333333492279053,   -1.75,                 0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 134, 91.69999694824219,     76.5,                  -1.0,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -45.849998474121094,   -25.5,                 0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  132, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  132, 0x0000)

    ChipFrameInfo(3540, 0)                                       # 0

    ScpFunction((
        "Function_0_DD4",          # 00, 0
        "Function_1_E84",          # 01, 1
        "Function_2_ED7",          # 02, 2
        "Function_3_130D",         # 03, 3
        "Function_4_150C",         # 04, 4
        "Function_5_15AB",         # 05, 5
        "Function_6_169B",         # 06, 6
        "Function_7_1918",         # 07, 7
        "Function_8_199C",         # 08, 8
        "Function_9_1C7B",         # 09, 9
        "Function_10_1D1C",        # 0A, 10
        "Function_11_2065",        # 0B, 11
        "Function_12_21FE",        # 0C, 12
        "Function_13_226F",        # 0D, 13
        "Function_14_2319",        # 0E, 14
        "Function_15_23BA",        # 0F, 15
        "Function_16_249E",        # 10, 16
        "Function_17_24BC",        # 11, 17
        "Function_18_2548",        # 12, 18
        "Function_19_25D7",        # 13, 19
        "Function_20_2AAD",        # 14, 20
        "Function_21_2B44",        # 15, 21
        "Function_22_2C93",        # 16, 22
        "Function_23_2D23",        # 17, 23
        "Function_24_2E1D",        # 18, 24
        "Function_25_2E9C",        # 19, 25
        "Function_26_39AA",        # 1A, 26
        "Function_27_4125",        # 1B, 27
        "Function_28_4898",        # 1C, 28
        "Function_29_4E82",        # 1D, 29
        "Function_30_536C",        # 1E, 30
        "Function_31_5373",        # 1F, 31
        "Function_32_539C",        # 20, 32
        "Function_33_6163",        # 21, 33
        "Function_34_61FA",        # 22, 34
        "Function_35_624B",        # 23, 35
        "Function_36_628B",        # 24, 36
        "Function_37_707C",        # 25, 37
        "Function_38_730B",        # 26, 38
        "Function_39_759A",        # 27, 39
        "Function_40_79C9",        # 28, 40
        "Function_41_7A82",        # 29, 41
        "Function_42_8C3E",        # 2A, 42
        "Function_43_9903",        # 2B, 43
        "Function_44_AEB2",        # 2C, 44
        "Function_45_AF7F",        # 2D, 45
        "Function_46_B04C",        # 2E, 46
        "Function_47_B0A7",        # 2F, 47
        "Function_48_B123",        # 30, 48
        "Function_49_B181",        # 31, 49
        "Function_50_B24E",        # 32, 50
        "Function_51_B31E",        # 33, 51
        "Function_52_B398",        # 34, 52
        "Function_53_B40B",        # 35, 53
        "Function_54_B47E",        # 36, 54
        "Function_55_B4EA",        # 37, 55
        "Function_56_B53F",        # 38, 56
        "Function_57_B594",        # 39, 57
        "Function_58_B607",        # 3A, 58
        "Function_59_B788",        # 3B, 59
        "Function_60_D143",        # 3C, 60
        "Function_61_D1D4",        # 3D, 61
        "Function_62_D237",        # 3E, 62
        "Function_63_D2E7",        # 3F, 63
        "Function_64_D4E9",        # 40, 64
        "Function_65_D589",        # 41, 65
        "Function_66_D5C0",        # 42, 66
        "Function_67_D63B",        # 43, 67
        "Function_68_D672",        # 44, 68
        "Function_69_D6ED",        # 45, 69
        "Function_70_D931",        # 46, 70
        "Function_71_D9EC",        # 47, 71
        "Function_72_DC18",        # 48, 72
        "Function_73_DC5F",        # 49, 73
        "Function_74_DCA8",        # 4A, 74
        "Function_75_DCEB",        # 4B, 75
        "Function_76_DD45",        # 4C, 76
        "Function_77_DEA6",        # 4D, 77
        "Function_78_E158",        # 4E, 78
        "Function_79_E265",        # 4F, 79
        "Function_80_E2C4",        # 50, 80
        "Function_81_E30B",        # 51, 81
        "Function_82_E539",        # 52, 82
        "Function_83_E609",        # 53, 83
        "Function_84_E689",        # 54, 84
        "Function_85_E709",        # 55, 85
        "Function_86_E789",        # 56, 86
        "Function_87_E7ED",        # 57, 87
        "Function_88_E851",        # 58, 88
        "Function_89_E8A7",        # 59, 89
        "Function_90_E918",        # 5A, 90
        "Function_91_E937",        # 5B, 91
        "Function_92_E956",        # 5C, 92
        "Function_93_E975",        # 5D, 93
        "Function_94_E994",        # 5E, 94
        "Function_95_E9B3",        # 5F, 95
        "Function_96_E9D2",        # 60, 96
        "Function_97_EA08",        # 61, 97
        "Function_98_EA5C",        # 62, 98
        "Function_99_EAB0",        # 63, 99
        "Function_100_EACC",       # 64, 100
        "Function_101_EC63",       # 65, 101
        "Function_102_EDF4",       # 66, 102
        "Function_103_EE44",       # 67, 103
        "Function_104_EE87",       # 68, 104
        "Function_105_EEE3",       # 69, 105
        "Function_106_EF0A",       # 6A, 106
        "Function_107_EF31",       # 6B, 107
        "Function_108_EF58",       # 6C, 108
        "Function_109_EF7F",       # 6D, 109
        "Function_110_EFDD",       # 6E, 110
        "Function_111_F030",       # 6F, 111
        "Function_112_F097",       # 70, 112
        "Function_113_F0EE",       # 71, 113
        "Function_114_F159",       # 72, 114
        "Function_115_F1B0",       # 73, 115
        "Function_116_F1D2",       # 74, 116
        "Function_117_F219",       # 75, 117
        "Function_118_F256",       # 76, 118
        "Function_119_F27D",       # 77, 119
        "Function_120_F2A4",       # 78, 120
        "Function_121_F2CB",       # 79, 121
        "Function_122_F2F2",       # 7A, 122
        "Function_123_F30F",       # 7B, 123
        "Function_124_F329",       # 7C, 124
        "Function_125_F35B",       # 7D, 125
        "Function_126_10B44",      # 7E, 126
        "Function_127_10B5F",      # 7F, 127
        "Function_128_10B7B",      # 80, 128
        "Function_129_1147C",      # 81, 129
        "Function_130_12960",      # 82, 130
        "Function_131_12978",      # 83, 131
        "Function_132_129F1",      # 84, 132
        "Function_133_12CE1",      # 85, 133
        "Function_134_12D53",      # 86, 134
        "Function_135_12DBE",      # 87, 135
    ))


    def Function_0_DD4(): pass

    label("Function_0_DD4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E0C"),
        (1, "loc_E18"),
        (2, "loc_E24"),
        (3, "loc_E30"),
        (4, "loc_E3C"),
        (5, "loc_E48"),
        (6, "loc_E54"),
        (SWITCH_DEFAULT, "loc_E60"),
    )


    label("loc_E0C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E18")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E24")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E30")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E3C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E48")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E54")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E60")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E83")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E83")

    Return()

    # Function_0_DD4 end

    def Function_1_E84(): pass

    label("Function_1_E84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ED6")
    OP_95(0xFE, -4530, 0, -2520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 20720, 0, -2520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_E84")

    label("loc_ED6")

    Return()

    # Function_1_E84 end

    def Function_2_ED7(): pass

    label("Function_2_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_EE5")
    Jump("loc_11BA")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1068")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 11220, 0, 2300, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 7990, 0, 2300, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 20720, 0, -2520, 270)
    BeginChrThread(0x1C, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xD, 75530, 0, 2000, 0)
    SetChrPos(0xC, 73730, 0, 2000, 0)

    label("loc_F6C")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 170720, 0, 82220, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 173530, 0, 74540, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xB, 87380, 0, 84160, 180)
    SetChrChipByIndex(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0x17, 89160, 0, 85000, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -41800, 0, 128199, 0)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -52180, 0, 124000, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -49460, 0, 112460, 89)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -52000, 0, 120730, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104D")
    Event(0, 26)

    label("loc_104D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1063")
    Event(0, 27)

    label("loc_1063")

    Jump("loc_11BA")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_11BA")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 11220, 0, 2300, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 7990, 0, 2300, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 20720, 0, -2520, 270)
    BeginChrThread(0x1C, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 174860, 0, 72670, 270)
    SetChrPos(0x10, 175050, 0, 71420, 271)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x40)
    SetChrPos(0x9, 171350, 0, 74290, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, 171060, 0, 78610, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 172130, 0, 77980, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 84390, 150, 84160, 180)
    SetChrChipByIndex(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 88940, 0, 80210, 135)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 87380, 0, 80380, 135)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 88100, 0, 72810, 89)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 88260, 0, 71560, 89)

    label("loc_11BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E4")
    ClearScenarioFlags(0x25, 1)
    Call(0, 30)

    label("loc_11E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11F8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 32)
    Jump("loc_12C7")

    label("loc_11F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_120F")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 36)
    Jump("loc_12C7")

    label("loc_120F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1226")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 39)
    Jump("loc_12C7")

    label("loc_1226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_123D")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 41)
    Jump("loc_12C7")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1251")
    ClearScenarioFlags(0x22, 4)
    Event(0, 42)
    Jump("loc_12C7")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1265")
    ClearScenarioFlags(0x22, 5)
    Event(0, 43)
    Jump("loc_12C7")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1279")
    ClearScenarioFlags(0x22, 6)
    Event(0, 58)
    Jump("loc_12C7")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_128D")
    ClearScenarioFlags(0x22, 7)
    Event(0, 59)
    Jump("loc_12C7")

    label("loc_128D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_12A1")
    ClearScenarioFlags(0x23, 0)
    Event(0, 125)
    Jump("loc_12C7")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_12B8")
    ClearScenarioFlags(0x23, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 129)
    Jump("loc_12C7")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_12C7")
    ClearScenarioFlags(0x23, 2)
    Event(0, 128)

    label("loc_12C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E5")
    Event(0, 37)

    label("loc_12E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130C")
    Event(0, 38)

    label("loc_130C")

    Return()

    # Function_2_ED7 end

    def Function_3_130D(): pass

    label("Function_3_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1322")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
    VolumeBGM(0x46, 0xC8)

    label("loc_1336")

    OP_10(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134D")
    OP_10(0x13, 0x1)
    OP_10(0x3, 0x0)

    label("loc_134D")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_137D")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A9")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_1B(0xD, 0x0, 0x87)
    Jump("loc_13AE")

    label("loc_13A9")

    OP_1B(0xD, 0xFF, 0xFFFF)

    label("loc_13AE")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "paper", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1423")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1437")
    ClearMapObjFlags(0xE, 0x4)

    label("loc_1437")

    ClearMapObjFlags(0x9, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1464")
    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)

    label("loc_1464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_148B")
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0xD, 0x4)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D0")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_14D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_150B")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_150B")

    Return()

    # Function_3_130D end

    def Function_4_150C(): pass

    label("Function_4_150C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_155C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "本会議も残す所あと半分……\x01",
            "最後まで気張っていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15A7")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_15A7")

    #C0002
    ChrTalk(
        0xFE,
        "今は本会議の真っ最中だ。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "中の様子は回廊室で窺ってくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_15A7")

    TalkEnd(0xFE)
    Return()

    # Function_4_150C end

    def Function_5_15AB(): pass

    label("Function_5_15AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1622")

    #C0004
    ChrTalk(
        0xFE,
        (
            "今は職員の方たちが\x01",
            "会議場を改めて\x01",
            "セッティングしている所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "どうぞご自由にお通り下さい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1697")

    label("loc_1622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1697")

    #C0006
    ChrTalk(
        0xFE,
        (
            "会議前半の終了時間は、\x01",
            "１５：００を予定しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "状況次第で多少の前後は\x01",
            "あると思いますけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1697")

    TalkEnd(0xFE)
    Return()

    # Function_5_15AB end

    def Function_6_169B(): pass

    label("Function_6_169B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_17CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")

    #C0008
    ChrTalk(
        0xFE,
        (
            "まだテロリストたちに\x01",
            "動きは見られないようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "蟻の這い出る隙もない\x01",
            "この警戒体制を突き崩せるとは\x01",
            "とても思えないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "最後まで油断は出来ないよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_17CA")

    label("loc_175C")


    #C0011
    ChrTalk(
        0xFE,
        (
            "蟻の這い出る隙もない\x01",
            "この警戒体制を突き崩せるとは\x01",
            "とても思えないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "最後まで油断は出来ないよ。\x02",
    )

    CloseMessageWindow()

    label("loc_17CA")

    Jump("loc_1914")

    label("loc_17CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_188F")

    #C0013
    ChrTalk(
        0xFE,
        "とうとう会議が始まったね。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "テロリストたちが何を\x01",
            "狙って来るかは読めないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "とにかく俺たちは\x01",
            "対策室の指示に従って、\x01",
            "与えられた役目を果たすだけさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1914")

    label("loc_188F")


    #C0016
    ChrTalk(
        0xFE,
        (
            "テロリストたちが何を\x01",
            "狙って来るかは読めないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "とにかく俺たちは\x01",
            "対策室の指示に従って、\x01",
            "与えられた役目を果たすだけさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1914")

    TalkEnd(0xFE)
    Return()

    # Function_6_169B end

    def Function_7_1918(): pass

    label("Function_7_1918")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192D")
    Call(0, 8)
    Jump("loc_1998")

    label("loc_192D")


    #C0018
    ChrTalk(
        0xA,
        (
            "#07103Fこの場は我々に任せて、\x01",
            "君たちは周囲の警戒に努めてくれ。\x02\x03",

            "#07100Fどうか君たちにも女神の加護を。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1998")

    TalkEnd(0xFE)
    Return()

    # Function_7_1918 end

    def Function_8_199C(): pass

    label("Function_8_199C")

    OP_4B(0x10, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    #C0019
    ChrTalk(
        0x10,
        "皆さん、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        (
            "#07102Fふむ、支援課の諸君か。\x02\x03",

            "会議場近辺のフロアを\x01",
            "警戒してくれているそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00000Fはい、何とか\x01",
            "ねじ込んでもらうことができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        (
            "#10302Fふふ、しかし\x01",
            "この部屋には相当な実力者が\x01",
            "揃っているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00300Fま、なんつってもほとんどが\x01",
            "将校クラスの人間なわけだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#00200Fええ、ここにいる方たちだけでも\x01",
            "余程の事態に対処できそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10109Fうんうん、それに何より\x01",
            "ユリア准佐の剣は\x01",
            "美しく苛烈と聞きますし！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "#07104Fフフ、過分な評価恐れ入る。\x02\x03",

            "#07100F……とにかく、\x01",
            "どのような者が現れようと\x01",
            "殿下には指一本触れさせはしない。\x02\x03",

            "この場は我々に任せて、\x01",
            "君たちは周囲の警戒に努めてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#00100Fええ、了解しました。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1C3, 0)
    Call(0, 31)
    Return()

    # Function_8_199C end

    def Function_9_1C7B(): pass

    label("Function_9_1C7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C90")
    Call(0, 8)
    Jump("loc_1D18")

    label("loc_1C90")


    #C0028
    ChrTalk(
        0xFE,
        (
            "我々王室親衛隊は何があっても\x01",
            "クローディア殿下をお守りします。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "会議場の方は心配いりませんので、\x01",
            "皆さんは巡回をお続けください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D18")

    TalkEnd(0xFE)
    Return()

    # Function_9_1C7B end

    def Function_10_1D1C(): pass

    label("Function_10_1D1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCA")

    #C0030
    ChrTalk(
        0x101,
        "#00000Fお疲れ様です、ミュラー少佐。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00100F何か異常はありませんか？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#07302Fああ、君たちか。\x02\x03",

            "#07303Fふむ、決して油断は出来ないが\x01",
            "至って平穏といったところか。\x02\x03",

            "首脳たちも声を荒げる様子もなく、\x01",
            "会議自体も順調のようだ。\x02\x03",

            "#07308Fこのまま無事に終わってくれれば、\x01",
            "皇子の肩の荷も少しは軽くなるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        "#10105Fミュラー少佐……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#00200Fどうやら色々あるみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#07302Fフフ、まあな。\x01",
            "といっても全てはあいつ自身が\x01",
            "撒いた種のせいなんだが……\x02\x03",

            "#07303Fふむ、どうやら口が過ぎたようだ。\x02\x03",

            "とにかく、今俺がすべきことは\x01",
            "護衛としての務めを果たすことだけ――\x02\x03",

            "#07300F君たちも君たちで、\x01",
            "それぞれの務めを果たしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00000Fええ、了解です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 2)
    Call(0, 31)
    Jump("loc_2061")

    label("loc_1FCA")


    #C0037
    ChrTalk(
        0x9,
        (
            "#07303F会議の方は見守ることしか\x01",
            "出来んが……武官は武官らしく\x01",
            "護衛の務めを果たすまでだ。\x02\x03",

            "#07300F君たちも君たちで、\x01",
            "それぞれの務めを果たしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2061")

    TalkEnd(0xFE)
    Return()

    # Function_10_1D1C end

    def Function_11_2065(): pass

    label("Function_11_2065")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2076")
    Jump("loc_21FA")

    label("loc_2076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_21FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219C")

    #C0038
    ChrTalk(
        0xFE,
        (
            "ふむ、君たちが\x01",
            "巡回役の特務支援課か。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "……お勤めご苦労。\x01",
            "見ての通り、\x01",
            "ここには異常も何もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "分かったら、部屋を\x01",
            "無闇にうろつかぬようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00001Fは、はい……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#00203F（何ていうか、露骨ですね。）\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#00306F（ああ、取り付くシマもねえな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_21FA")

    label("loc_219C")


    #C0044
    ChrTalk(
        0xFE,
        (
            "見ての通り、\x01",
            "ここには異常は何もない。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "分かったら、部屋を\x01",
            "無闇にうろつかぬようにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21FA")

    TalkEnd(0xFE)
    Return()

    # Function_11_2065 end

    def Function_12_21FE(): pass

    label("Function_12_21FE")

    TalkBegin(0xFE)

    #C0046
    ChrTalk(
        0xFE,
        (
            "……物音を立てると、\x01",
            "会議場に漏れてしまいますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "くれぐれも、\x01",
            "ここではお静かにお願いします。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_21FE end

    def Function_13_226F(): pass

    label("Function_13_226F")

    TalkBegin(0xFE)

    #C0048
    ChrTalk(
        0xFE,
        (
            "反対側の控え室ではアリオス様と\x01",
            "大統領の補佐官の方が\x01",
            "お話をされているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "どうやらお知り合いのようですが、\x01",
            "一体どういうご関係なんでしょうかね？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_226F end

    def Function_14_2319(): pass

    label("Function_14_2319")

    TalkBegin(0xFE)

    #C0050
    ChrTalk(
        0xFE,
        (
            "ここは、帝国と王国の\x01",
            "ご側近の方々がお控えになられる\x01",
            "お部屋です。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "――そう、つまりはここに\x01",
            "ユリア准佐がいたんです！\x01",
            "考えただけで悲鳴モノですね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_2319 end

    def Function_15_23BA(): pass

    label("Function_15_23BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_23CB")
    Jump("loc_249A")

    label("loc_23CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_249A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23EA")
    TalkEnd(0xFE)
    Call(0, 25)
    Return()

    label("loc_23EA")


    #C0052
    ChrTalk(
        0xB,
        (
            "#12004F言いたいことはあると思うけど……\x01",
            "今はとにかくお互い\x01",
            "成り行きを見守りましょう。\x02\x03",

            "#12000F警戒という意味では、\x01",
            "私とあなたたちの立ち位置も\x01",
            "そうは変わらないことだしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_249A")

    TalkEnd(0xFE)
    Return()

    # Function_15_23BA end

    def Function_16_249E(): pass

    label("Function_16_249E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_24AF")
    Jump("loc_24B8")

    label("loc_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_24B8")

    label("loc_24B8")

    TalkEnd(0xFE)
    Return()

    # Function_16_249E end

    def Function_17_24BC(): pass

    label("Function_17_24BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_24CD")
    Jump("loc_2544")

    label("loc_24CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2544")

    #C0053
    ChrTalk(
        0xFE,
        (
            "ふむ、皆さんが\x01",
            "巡回担当の特務支援課ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "お勤めご苦労様です。\x01",
            "何かあればいつでも言って下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2544")

    TalkEnd(0xFE)
    Return()

    # Function_17_24BC end

    def Function_18_2548(): pass

    label("Function_18_2548")

    TalkBegin(0xFE)

    #C0055
    ChrTalk(
        0xFE,
        "どうやら会議は順調のようですね。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "共和国議会と違って野党勢力の\x01",
            "しつこい追求もなく、大統領閣下も\x01",
            "気が楽なのではないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2548 end

    def Function_19_25D7(): pass

    label("Function_19_25D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_297C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F4")

    #C0057
    ChrTalk(
        0xFE,
        "あなた方は特務支援課の……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "昨日はアルバート大公閣下が\x01",
            "お世話になったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、お世話になったのは\x01",
            "むしろ俺たちのほうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#00100Fええ、大公閣下の医療知識には\x01",
            "本当に助けられました。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "はは、確かに大公閣下は\x01",
            "医師としても大変優秀なお方で\x01",
            "いらっしゃいますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "それはとにかく、\x01",
            "閣下は皆さんのことを非常に\x01",
            "気に入られたようでしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "こうして実際にお目にかかれて\x01",
            "私も嬉しく思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#00302Fはは、そいつはどうも。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        "#10100Fどうもありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 3)
    Jump("loc_2977")

    label("loc_27F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2907")

    #C0066
    ChrTalk(
        0xFE,
        (
            "そういえば、どうやら\x01",
            "テロリストが出現する可能性が\x01",
            "あるらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "このような国際会議の場では\x01",
            "常に想定される事ではありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "万が一にも、首脳たちを\x01",
            "危険にはさらせませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "お互い気合いを入れて、\x01",
            "やるべきことを尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2977")

    label("loc_2907")


    #C0070
    ChrTalk(
        0xFE,
        (
            "テロリストの情報は\x01",
            "こちらの耳にも届いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "お互い気合いを入れて、\x01",
            "やるべきことを尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2977")

    Jump("loc_2AA9")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A39")

    #C0072
    ChrTalk(
        0xFE,
        (
            "特務支援課の皆さんですね。\x01",
            "巡回のお仕事お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "テロリストの情報は\x01",
            "こちらの耳にも届いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "お互い気合いを入れて、\x01",
            "やるべきことを尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AA9")

    label("loc_2A39")


    #C0075
    ChrTalk(
        0xFE,
        (
            "テロリストの情報は\x01",
            "こちらの耳にも届いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "お互い気合いを入れて、\x01",
            "やるべきことを尽くしましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA9")

    TalkEnd(0xFE)
    Return()

    # Function_19_25D7 end

    def Function_20_2AAD(): pass

    label("Function_20_2AAD")

    TalkBegin(0xFE)

    #C0077
    ChrTalk(
        0xFE,
        (
            "今回の通商会議は、\x01",
            "我がレミフェリアにとっても\x01",
            "非常に有益な会議です。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "祖国の更なる発展のため、\x01",
            "実りある成果に\x01",
            "是非とも期待しています。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2AAD end

    def Function_21_2B44(): pass

    label("Function_21_2B44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4A")

    #C0079
    ChrTalk(
        0xFE,
        "ふむ、しかし大した眺めだな。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "まさか、テロリストが\x01",
            "この空を飛んで来るなんてことは\x01",
            "ないと思うが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    #C0081
    ChrTalk(
        0xFE,
        (
            "………はは、まさかな。\x01",
            "そんなことあるわけないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00006F（……何か、切ない後ろ姿だな。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2C81")

    label("loc_2C4A")


    #C0083
    ChrTalk(
        0xFE,
        (
            "はは、まさかな……\x01",
            "どうやら私は疲れているようだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C81")

    Jump("loc_2C8F")

    label("loc_2C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2C8F")

    label("loc_2C8F")

    TalkEnd(0xFE)
    Return()

    # Function_21_2B44 end

    def Function_22_2C93(): pass

    label("Function_22_2C93")

    TalkBegin(0xFE)

    #C0084
    ChrTalk(
        0xFE,
        (
            "さて、あとは\x01",
            "このマイクを片付けてと……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "ふむ、しかし先ほどまで\x01",
            "この後ろに首脳たちが並んでいたと\x01",
            "思うと何だか軽く緊張しますね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2C93 end

    def Function_23_2D23(): pass

    label("Function_23_2D23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEA")

    #C0086
    ChrTalk(
        0xFE,
        (
            "ふきふきふき……\x01",
            "うんしょっ、こらしょっ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0087
    ChrTalk(
        0xFE,
        (
            "会議の後半も皆さんには\x01",
            "気持ちよくお部屋を\x01",
            "使って頂かないとですからねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "心を沢山こめてお掃除中ですー！\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x59, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_2E19")

    label("loc_2DEA")


    #C0089
    ChrTalk(
        0xFE,
        (
            "ふきふきふき……\x01",
            "うんしょっ、こらしょっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E19")

    TalkEnd(0xFE)
    Return()

    # Function_23_2D23 end

    def Function_24_2E1D(): pass

    label("Function_24_2E1D")

    TalkBegin(0xFE)

    #C0090
    ChrTalk(
        0xFE,
        (
            "副局長さん、あんな所で\x01",
            "たそがれてどうかしたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "まあ邪魔にはなりません、\x01",
            "……けれど何か気になりますね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2E1D end

    def Function_25_2E9C(): pass

    label("Function_25_2E9C")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12000.itp")
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(83610, 1300, 82220, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15400, 0)
    SetChrPos(0x101, 84860, 0, 82570, 0)
    SetChrPos(0x102, 83260, 0, 81870, 0)
    SetChrPos(0x103, 84860, 0, 81470, 0)
    SetChrPos(0x104, 83060, 0, 80570, 0)
    SetChrPos(0x109, 85060, 0, 80570, 0)
    SetChrPos(0x105, 83460, 0, 79870, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_30D3")

    #C0092
    ChrTalk(
        0xB,
        (
            "#5P#12000Fあら、あなたたち。\x01",
            "警戒の方は順調かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#11P#00001Fキリカさん……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0094
    AnonymousTalk(
        0xB,
        (
            "その様子だと、またなにか\x01",
            "新しい情報を掴んだって所かしら。\x02\x03",

            "どうやら《アルセイユ》にも\x01",
            "招待されていたみたいだし、ね。\x02",
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
    Jump("loc_34F5")

    label("loc_30D3")


    #C0095
    ChrTalk(
        0xB,
        (
            "#5P#12000Fあなたたち……\x01",
            "フフ、お久しぶりね。\x02\x03",

            "警戒の方は順調かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#00001Fキリカさん……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0097
    AnonymousTalk(
        0xB,
        (
            "そうね、以前会った時とは\x01",
            "立場も違うし――改めて\x01",
            "自己紹介させてもらおうかしら。\x02\x03",

            "カルバード共和国で\x01",
            "大統領補佐官を務めている、\x01",
            "キリカ・ロウランよ。\x02\x03",

            "他にも肩書きはあるけど……\x01",
            "まあ敢えて語ることではないわね。\x02",
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

    #C0098
    ChrTalk(
        0x101,
        "#00003F――なるほど。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#12P#00100Fちなみに、以前仰っていた\x01",
            "芸能プロデューサーというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "#5P#12004Fふふ、それも\x01",
            "確かな肩書きの１つよ。\x02\x03",

            "#12002F事務所だって当然、\x01",
            "共和国に存在しているしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど、その辺に\x01",
            "抜かりはないんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x105,
        (
            "#12P#10302F（ふふ、表の顔を\x01",
            "  複数使い分ける女諜報員か。）\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#12P#00309F（う～ん、そんなミステリアスな\x01",
            "  キリカさんも素敵かもな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#12P#10106F（先輩、流石にその発言は\x01",
            "  緊張感に欠けるような……）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "#5P#12002Fふふ、私の顔に\x01",
            "何か付いているかしら？\x02\x03",

            "#12004Fそうそう――\x01",
            "そういえば、あなたたち。\x02\x03",

            "#12000F何でも昨日は《アルセイユ》に\x01",
            "招待されたらしいわね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F5")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0106
    ChrTalk(
        0x102,
        "#12P#00105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        "#00201F……当然、把握済みなんですね。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        "#12P#00306Fふぅ、なんつうか流石ッスね。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#5P#12004Fフフ、まあそれ自体は\x01",
            "大したことではないけれど。\x02\x03",

            "#12000Fそれで……\x01",
            "面白い話は聞けたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#00003Fええ、あくまで雑談ですが。\x02\x03",

            "#00001Fもっとも、どうしても\x01",
            "分からないことも多いですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "#5P#12004Fふふ、そう。\x02\x03",

            "まあでも、それは\x01",
            "こちらも同じことだけどね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0112
    ChrTalk(
        0x101,
        "#00005Fえ……？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "#5P#12000F例えばの話よ。\x02\x03",

            "もし私が何らかのシナリオを\x01",
            "思い描いていたとして――\x01",
            "それが実現するとは限らない。\x02\x03",

            "#12003F複数の思惑が絡む以上、\x01",
            "不確定な要素を\x01",
            "抱えるのは誰もが同じ。\x02\x03",

            "これから何が起こるのか、\x01",
            "それとも何も起こらないのか。\x02\x03",

            "#12000F現時点では、誰にも\x01",
            "分からないということよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00001F確かにそれはそうですが……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        "#12P#10304Fフフ、でもまあごもっともだね。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xB,
        (
            "#5P#12004Fとにかく、言っておきたいのは\x01",
            "私が大統領を守る立場であることは\x01",
            "間違いないということよ。\x02\x03",

            "つまり、その意味においては\x01",
            "あなたたちと立ち位置は同じ。\x02\x03",

            "#12000F要するに、お互い成り行きを\x01",
            "見守りましょうということね。\x02\x03",

            "それ以上のことについては……\x01",
            "今ここで語るつもりはないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00001Fなるほど……\x01",
            "いえ、十分参考になりました。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x1C3, 4)
    Call(0, 31)
    EventEnd(0x5)
    Return()

    # Function_25_2E9C end

    def Function_26_39AA(): pass

    label("Function_26_39AA")

    EventBegin(0x0)
    Fade(500)
    OP_68(86650, 1400, 75180, 0)
    MoveCamera(33, 8, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21450, 0)
    SetChrPos(0x101, 87120, 0, 70000, 0)
    SetChrPos(0x102, 86120, 0, 70000, 0)
    SetChrPos(0x103, 87120, 0, 68500, 0)
    SetChrPos(0x104, 86120, 0, 68500, 0)
    SetChrPos(0x109, 87120, 0, 67000, 0)
    SetChrPos(0x105, 86120, 0, 67000, 0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0118
    ChrTalk(
        0x101,
        (
            "#11P#00005F#12P（あれは……\x01",
            "  アリオスさんとキリカさんか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#11P#00105F#12P（みたいね、一体どんな話を\x01",
            "  しているのかしら……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    #C0120
    ChrTalk(
        0x17,
        (
            "#6P#01403F#11P──ギルドを離れてそろそろ１年か。\x02\x03",

            "#01400F新しい場所には慣れたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        (
            "#12004F#6P……それなりには。\x02\x03",

            "#12000Fギルドにいた頃とは\x01",
            "比べ物にならないくらい\x01",
            "働かされていますけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x17,
        "#6P#01403F#11Pそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    #C0123
    ChrTalk(
        0xB,
        (
            "#12000F#6P……シズクちゃんは\x01",
            "お元気ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x17,
        (
            "#6P#01402F#11Pああ、少々聞きわけが良すぎるが\x01",
            "いつも朗らかで居てくれている。\x02\x03",

            "#01404F最近、出会いにも恵まれてな。\x01",
            "……よく笑うようになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "#12004F#6Pそうですか、\x01",
            "それは良いことですね。\x02\x03",

            "#12003F……………………………\x02\x03",

            "サヤさんが亡くなられて……\x01",
            "もう５年になりますか。\x02\x03",

            "#12000F私が初めてお会いしたのは\x01",
            "６年前でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x17,
        (
            "#11P#01404F６年前……そうだったな。\x02\x03",

            "当時、あてもなく大陸中を\x01",
            "さすらっていたという君が\x01",
            "この街で偶然サヤと知り合い……\x02\x03",

            "遠慮する君を、\x01",
            "サヤの奴が強引に引っ張る形で\x01",
            "我が家に泊まったんだったか。\x02\x03",

            "#01402Fそんな君と、３年前に\x01",
            "リベールのギルドで再会した時は\x01",
            "驚かされたものだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "#12004F#6Pふふ、そうですね。\x01",
            "本当に人の縁は不思議なものだと\x01",
            "思わされます。\x02\x03",

            "#12003F……私はあの一宿一飯の\x01",
            "温もりを生涯忘れません。\x02\x03",

            "#12001F結局、その恩を直接返すことは\x01",
            "出来ませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x17,
        (
            "#11P#01404F……いや、そう思って\x01",
            "もらえているだけで\x01",
            "サヤはきっと喜んだだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(86040, 1500, 67910, 0)
    MoveCamera(46, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15440, 0)
    OP_4C(0x17, 0xFF)
    OP_0D()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00005F#11P（……どうやら、２人には\x01",
            "  ギルドで知り合う以前から\x01",
            "  面識があったみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#00108F#12P（ええ、でもこれ以上\x01",
            "  立ち聞きするのは\x01",
            "  悪い気がするわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#11P#00203F（ですね、邪魔しない内に\x01",
            "  引き揚げましょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 86960, 0, 68320, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C2, 6)
    EventEnd(0x5)
    Return()

    # Function_26_39AA end

    def Function_27_4125(): pass

    label("Function_27_4125")

    EventBegin(0x0)
    Fade(500)
    OP_68(89970, 1500, 79740, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 89590, 0, 78000, 315)
    SetChrPos(0x102, 90800, 0, 78000, 315)
    SetChrPos(0x103, 89590, 0, 76500, 315)
    SetChrPos(0x104, 90800, 0, 76500, 315)
    SetChrPos(0x109, 89590, 0, 75000, 315)
    SetChrPos(0x105, 90800, 0, 75000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x17, 0xFF)
    OP_0D()

    #C0132
    ChrTalk(
        0x101,
        (
            "#12P#00005F（あれは……\x01",
            "  アリオスさんとキリカさんか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#12P#00105F（みたいね、一体どんな話を\x01",
            "  しているのかしら……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    #C0134
    ChrTalk(
        0x17,
        (
            "#6P#01403F#11P──ギルドを離れてそろそろ１年か。\x02\x03",

            "#01400F新しい場所には慣れたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        (
            "#12004F#6P……それなりには。\x02\x03",

            "#12000Fギルドにいた頃とは\x01",
            "比べ物にならないくらい\x01",
            "働かされていますけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x17,
        "#6P#01403F#11Pそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    #C0137
    ChrTalk(
        0xB,
        (
            "#12000F#6P……シズクちゃんは\x01",
            "お元気ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x17,
        (
            "#6P#01402F#11Pああ、少々聞きわけが良すぎるが\x01",
            "いつも朗らかで居てくれている。\x02\x03",

            "#01404F最近、出会いにも恵まれてな。\x01",
            "……よく笑うようになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "#12004F#6Pそうですか、\x01",
            "それは良いことですね。\x02\x03",

            "#12003F……………………………\x02\x03",

            "サヤさんが亡くなられて……\x01",
            "もう５年になりますか。\x02\x03",

            "#12000F私が初めてお会いしたのは\x01",
            "６年前でしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x17,
        (
            "#11P#01404F６年前……そうだったな。\x02\x03",

            "当時、あてもなく大陸中を\x01",
            "さすらっていたという君が\x01",
            "この街で偶然サヤと知り合い……\x02\x03",

            "遠慮する君を、\x01",
            "サヤの奴が強引に引っ張る形で\x01",
            "我が家に泊まったんだったか。\x02\x03",

            "#01402Fそんな君と、３年前に\x01",
            "リベールのギルドで再会した時は\x01",
            "驚かされたものだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "#12004F#6Pふふ、そうですね。\x01",
            "本当に人の縁は不思議なものだと\x01",
            "思わされます。\x02\x03",

            "#12003F……私はあの一宿一飯の\x01",
            "温もりを生涯忘れません。\x02\x03",

            "#12001F結局、その恩を直接返すことは\x01",
            "出来ませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x17,
        (
            "#11P#01404F……いや、そう思って\x01",
            "もらえているだけで\x01",
            "サヤはきっと喜んだだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(90790, 1500, 76740, 0)
    MoveCamera(64, 26, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15480, 0)
    OP_4C(0x17, 0xFF)
    OP_0D()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00005F#11P（……どうやら、２人には\x01",
            "  ギルドで知り合う以前から\x01",
            "  面識があったみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        (
            "#11P#00108F（ええ、でもこれ以上\x01",
            "  立ち聞きするのは\x01",
            "  悪い気がするわね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        (
            "#12P#00203F（ですね、邪魔しない内に\x01",
            "  引き揚げましょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 91210, 0, 76450, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C2, 6)
    EventEnd(0x5)
    Return()

    # Function_27_4125 end

    def Function_28_4898(): pass

    label("Function_28_4898")

    EventBegin(0x0)
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x17, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CAE")

    #C0146
    ChrTalk(
        0x17,
        (
            "#11P#01404Fそういえば……\x01",
            "エステルとヨシュアが\x01",
            "君に会いたがっていたぞ。\x02\x03",

            "記念祭の時にリンと会ったと聞いて\x01",
            "かなり悔しがっていたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "#12004F#6Pふふ、そうですか。\x01",
            "それは悪いことをしましたね。\x02\x03",

            "時間に余裕があれば、もちろん\x01",
            "私も会いたかったのですが。\x02\x03",

            "#12002Fただ、２人のクロスベルでの\x01",
            "活躍はもちろん聞いています。\x02\x03",

            "私はあの子たちのことを\x01",
            "新人の頃から見ていますが……\x01",
            "本当に見違えたものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x17,
        (
            "#11P#01402Fああ、俺も２人には\x01",
            "随分助けられたからな。\x02\x03",

            "#01404F流石はカシウスさんの\x01",
            "子供たちと言うべきか……\x01",
            "まだまだ先が楽しみだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(86330, 1800, 73970, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14890, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 87080, 0, 73540, 0)
    SetChrPos(0x102, 88890, 0, 73750, 0)
    SetChrPos(0x103, 86550, 0, 71830, 0)
    SetChrPos(0x104, 88500, 0, 72620, 0)
    SetChrPos(0x109, 89790, 0, 72690, 0)
    SetChrPos(0x105, 87790, 0, 71090, 0)
    OP_0D()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00001F#11P（キリカさん……\x01",
            "  そういえばリベールで受付を\x01",
            "  やっていたって話だったな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            "#00300F#11P（つまり当然、\x01",
            "  エステルちゃんたちとも\x01",
            "  知り合いってことか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#00102F#11P（ふふ、人って本当に\x01",
            "  どこでどうつながっているか\x01",
            "  分からないわね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x0, 7)
    Jump("loc_4E56")

    label("loc_4CAE")


    #C0152
    ChrTalk(
        0x17,
        (
            "#11P#01405Fところで、ジンさんとは今も\x01",
            "連絡を取り合っているそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "#12004F#6Pええ、それなりには。\x02\x03",

            "#12000Fお互い立場もあるので、\x01",
            "そうそう会う機会はありませんが。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(86330, 1800, 73970, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14890, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 87080, 0, 73540, 0)
    SetChrPos(0x102, 88890, 0, 73750, 0)
    SetChrPos(0x103, 86550, 0, 71830, 0)
    SetChrPos(0x104, 88500, 0, 72620, 0)
    SetChrPos(0x109, 89790, 0, 72690, 0)
    SetChrPos(0x105, 87790, 0, 71090, 0)
    OP_0D()

    #C0154
    ChrTalk(
        0x101,
        (
            "#00003F#11P（これ以上、立ち聞きできないな。\x01",
            "  大人しく引き返そう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_4E56")

    SetChrPos(0x0, 87080, 0, 73540, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_4898 end

    def Function_29_4E82(): pass

    label("Function_29_4E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F4")
    EventBegin(0x0)
    Fade(500)
    OP_68(34230, 0, 320, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18390, 0)
    SetChrPos(0x101, 33280, 0, -280, 90)
    SetChrPos(0x102, 33280, 0, -1680, 90)
    SetChrPos(0x103, 32970, 0, 720, 90)
    SetChrPos(0x104, 31670, 0, -670, 90)
    SetChrPos(0x109, 31080, 0, -1750, 99)
    SetChrPos(0x105, 31070, 0, 740, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x101,
        "#00005Fあ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(73750, 1500, 1580, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    Sound(160, 0, 100, 0)
    OP_64(0xC)
    OP_64(0xD)
    Sleep(500)

    #C0156
    ChrTalk(
        0xD,
        (
            "……ふむ、エレベーターが\x01",
            "到着したようですが？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        "#6Pえ、ああ……お先にどうぞ。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "ああいえ、そちらの方こそ\x01",
            "お先にご使用下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        "私は特に急いでおりませんので。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0xD, 500)

    #C0160
    ChrTalk(
        0xC,
        (
            "#6Pいえ、ですが後から来たのは\x01",
            "私の方ですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(34230, 0, 320, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18390, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0x104,
        "#6P#00305Fどうかしたのか、ロイド？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00001Fああ、２大国の将校さんたちが\x01",
            "エレベーター前にいるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    TurnDirection(0x103, 0x104, 500)

    #C0163
    ChrTalk(
        0x102,
        (
            "#00106Fどうやら、お互いエレベーターを\x01",
            "譲り合っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x109,
        "#12P#10108F……な、何だか気まずそうですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0165
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、一体何を遠慮して\x01",
            "そんな事になっているんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        (
            "#00203F……とりあえず、\x01",
            "無理にエレベーターを使う\x01",
            "必要はないと思いますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00003Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x1C2, 7)
    EventEnd(0x5)
    Return()

    label("loc_52F4")

    EventBegin(0x1)

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000F……将校さんたちはまだ\x01",
            "エレベーター前にいるみたいだ。\x02\x03",

            "#00003F俺たちは階段を使おう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    EventEnd(0x4)
    Return()

    # Function_29_4E82 end

    def Function_30_536C(): pass

    label("Function_30_536C")

    Sound(160, 0, 100, 0)
    Return()

    # Function_30_536C end

    def Function_31_5373(): pass

    label("Function_31_5373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_539B")
    SetScenarioFlags(0x146, 3)

    label("loc_539B")

    Return()

    # Function_31_5373 end

    def Function_32_539C(): pass

    label("Function_32_539C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    CreatePortrait(0, 230, 192, 742, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis505.itp")
    OP_90(0x101, -51500, 0, 11300, 0)
    OP_90(0x102, -51500, 0, 10200, 0)
    OP_90(0x103, -51500, 0, 9100, 0)
    OP_90(0x104, -51500, 0, 8000, 0)
    OP_90(0x109, -51500, 0, 6900, 0)
    OP_90(0x105, -51500, 0, 5800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -51500, 0, 13500, 0)
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x3C)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    OP_68(-54000, 1100, 12700, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    BeginChrThread(0x1D, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 33)
    OP_0D()
    OP_68(-54000, 1100, -300, 8000)
    OP_6F(0x79)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xD, 0x10)
    OP_71(0xD, 0x0, 0x5, 0x0, 0x0)
    OP_79(0xD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(-12600, 1000, 0, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x1D, -10500, 0, 0, 90)
    SetChrPos(0x3C, -11600, -600, 0, 90)
    SetChrPos(0x101, -12600, 0, -800, 90)
    SetChrPos(0x102, -12600, 0, 700, 90)
    SetChrPos(0x103, -13800, 0, -400, 90)
    SetChrPos(0x104, -13800, 0, 1100, 90)
    SetChrPos(0x109, -15000, 0, -600, 90)
    SetChrPos(0x105, -15000, 0, 900, 90)
    OP_6B(0x3C)
    SetChrFlags(0x3C, 0x20)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3C, 0x8)
    SetChrFlags(0x3C, 0x4)

    def lambda_562C():
        OP_97(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_562C)

    def lambda_5646():
        OP_98(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_5646)

    def lambda_5660():
        OP_97(0x101, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5660)
    Sleep(50)

    def lambda_567D():
        OP_97(0x102, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_567D)
    Sleep(50)

    def lambda_569A():
        OP_97(0x103, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_569A)
    Sleep(50)

    def lambda_56B7():
        OP_97(0x104, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_56B7)
    Sleep(50)

    def lambda_56D4():
        OP_97(0x109, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_56D4)
    Sleep(50)

    def lambda_56F1():
        OP_97(0x105, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_56F1)
    FadeToBright(1000, 0)
    MoveCamera(37, 21, 0, 8000)
    SetCameraDistance(18000, 8000)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x1D, 1)

    def lambda_575E():
        OP_93(0xFE, 0x110, 0x15E)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_575E)
    WaitChrThread(0x101, 0)

    def lambda_576F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_576F)
    Sleep(100)
    WaitChrThread(0x102, 0)

    def lambda_5783():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5783)
    WaitChrThread(0x101, 2)

    #C0169
    ChrTalk(
        0x101,
        "#6P#00001Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#00101F#6Pそちらが……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)
    OP_68(10000, 1000, 3800, 2000)
    MoveCamera(0, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_57F6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_57F6)
    OP_6F(0x79)

    #C0171
    ChrTalk(
        0x1D,
        (
            "#6P#02804Fフフ、この後行われる\x01",
            "国際親善という名前の\x01",
            "肚#2Rハラ#の探り合いの舞台……\x02\x03",

            "#02800F国際会議場だ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x1D, -52000, 0, 101500, 0)
    SetChrPos(0x101, -51400, 0, 104200, 0)
    SetChrPos(0x102, -52600, 0, 104200, 0)
    SetChrPos(0x103, -50200, 0, 103400, 0)
    SetChrPos(0x104, -53800, 0, 103400, 0)
    SetChrPos(0x109, -51200, 0, 102600, 0)
    SetChrPos(0x105, -52900, 0, 102200, 0)
    OP_68(-52000, 5500, 118000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20500, 0)
    OP_68(-52660, 3000, 105850, 6000)
    MoveCamera(23, 7, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(16500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1500)

    def lambda_596A():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_596A)
    Sleep(50)

    def lambda_5987():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5987)
    Sleep(50)

    def lambda_59A4():
        OP_97(0x103, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_59A4)
    Sleep(50)

    def lambda_59C1():
        OP_97(0x104, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_59C1)
    Sleep(50)

    def lambda_59DE():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_59DE)
    Sleep(50)

    def lambda_59FB():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_59FB)
    Sleep(500)

    def lambda_5A18():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5A18)
    OP_6F(0x79)

    #C0172
    ChrTalk(
        0x101,
        "#00011F#11Pこれは……凄いな。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#00205F#11Pすごい見晴らしです……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00302F#5Pこれだけ天井が高いってことは\x01",
            "２フロアぶち抜きみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x1D,
        (
            "#02804F#11Pああ、そのため上の３６Ｆは\x01",
            "コの字型の構成になっている。\x02\x03",

            "#02800Fちなみに、両脇の部屋は\x01",
            "各国首脳の関係者が詰める\x01",
            "控え室になっていてね。\x02\x03",

            "護衛の将校などが\x01",
            "待機することになるだろう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B8B():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5B8B)
    Sleep(50)

    def lambda_5B9B():
        TurnDirection(0x109, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B9B)
    Sleep(50)

    def lambda_5BAB():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5BAB)
    Sleep(50)

    def lambda_5BBB():
        TurnDirection(0x105, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5BBB)
    Sleep(50)

    def lambda_5BCB():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5BCB)
    Sleep(50)

    def lambda_5BDB():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5BDB)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0176
    ChrTalk(
        0x109,
        "#10100F#5Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10302F#5P確かにそういう部屋も\x01",
            "必要だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x1D,
        (
            "#02804F#11Pさて、最後のフロアに\x01",
            "案内するとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    OP_68(13400, 900, 0, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x1D, 15500, 0, 0, 90)
    SetChrPos(0x3C, 13400, -600, 0, 90)
    SetChrPos(0x101, 13400, 0, -800, 90)
    SetChrPos(0x102, 13400, 0, 700, 90)
    SetChrPos(0x103, 12200, 0, -400, 90)
    SetChrPos(0x104, 12200, 0, 1100, 90)
    SetChrPos(0x109, 11000, 0, -600, 90)
    SetChrPos(0x105, 11000, 0, 900, 90)
    OP_6B(0x3C)
    SetChrFlags(0x3C, 0x20)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3C, 0x8)
    SetChrFlags(0x3C, 0x4)
    MoveCamera(47, 21, 0, 10000)
    SetCameraDistance(19000, 10000)

    def lambda_5D85():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5D85)

    def lambda_5D9F():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_5D9F)

    def lambda_5DB9():
        OP_97(0x101, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5DB9)
    Sleep(50)

    def lambda_5DD6():
        OP_97(0x102, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5DD6)
    Sleep(50)

    def lambda_5DF3():
        OP_97(0x103, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5DF3)
    Sleep(50)

    def lambda_5E10():
        OP_97(0x104, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5E10)
    Sleep(50)

    def lambda_5E2D():
        OP_97(0x109, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5E2D)
    Sleep(50)

    def lambda_5E4A():
        OP_97(0x105, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5E4A)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x3C, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(71900, 1000, 0, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x1D, 71900, 0, 0, 90)
    SetChrPos(0x3C, 71900, -500, 0, 90)
    SetChrPos(0x101, 70200, 0, -900, 90)
    SetChrPos(0x102, 70200, 0, 600, 90)
    SetChrPos(0x103, 69000, 0, -500, 90)
    SetChrPos(0x104, 69000, 0, 1000, 90)
    SetChrPos(0x109, 67800, 0, -700, 90)
    SetChrPos(0x105, 67800, 0, 800, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    SetCameraDistance(20000, 7000)

    def lambda_5F7D():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_5F7D)
    BeginChrThread(0x3C, 3, 0, 35)
    Sleep(100)
    FadeToBright(1000, 0)

    def lambda_5FA9():
        OP_97(0x101, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5FA9)
    Sleep(50)

    def lambda_5FC6():
        OP_97(0x102, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5FC6)
    Sleep(50)

    def lambda_5FE3():
        OP_97(0x103, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5FE3)
    Sleep(50)

    def lambda_6000():
        OP_97(0x104, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6000)
    Sleep(50)

    def lambda_601D():
        OP_97(0x109, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_601D)
    Sleep(50)

    def lambda_603A():
        OP_97(0x105, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_603A)
    Sleep(100)

    def lambda_6057():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6057)
    Sleep(50)

    def lambda_606B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_606B)
    OP_0D()
    WaitChrThread(0x1D, 0)
    BeginChrThread(0x1D, 3, 0, 34)
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x102, 0)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(100)
    WaitChrThread(0x103, 0)
    BeginChrThread(0x103, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x104, 0)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(100)
    WaitChrThread(0x109, 0)
    BeginChrThread(0x109, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 3, 0, 34)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    OP_0D()
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_539C end

    def Function_33_6163(): pass

    label("Function_33_6163")


    def lambda_6168():
        OP_95(0xFE, -51500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6168)
    WaitChrThread(0xFE, 1)

    def lambda_6186():
        OP_95(0xFE, -55500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6186)
    WaitChrThread(0xFE, 1)

    def lambda_61A4():
        OP_95(0xFE, -55500, 0, 1500, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61A4)
    WaitChrThread(0xFE, 1)

    def lambda_61C2():
        OP_95(0xFE, -53000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61C2)
    WaitChrThread(0xFE, 1)

    def lambda_61E0():
        OP_95(0xFE, -48000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61E0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_6163 end

    def Function_34_61FA(): pass

    label("Function_34_61FA")


    def lambda_61FF():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_61FF)
    WaitChrThread(0xFE, 1)

    def lambda_621D():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_621D)
    Sleep(700)

    def lambda_623A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_623A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_34_61FA end

    def Function_35_624B(): pass

    label("Function_35_624B")


    def lambda_6250():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_6250)
    WaitChrThread(0x3C, 1)

    def lambda_626E():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_626E)
    WaitChrThread(0xFE, 1)
    OP_6B(0xFF)
    Return()

    # Function_35_624B end

    def Function_36_628B(): pass

    label("Function_36_628B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    LoadChrToIndex("chr/ch05900.itc", 0x27)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    CreatePortrait(7, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    OP_4B(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日、１３：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0180
    AnonymousTalk(
        0x23,
        (
            "#02503F──それではこれより\x01",
            "『西ゼムリア通商会議』の\x01",
            "本会議を開始いたします。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-52000, 7500, 116000, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23000, 0)
    OP_68(-52000, 2500, 116000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-46800, 1000, 119400, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(-46800, 1000, 114800, 4000)
    MoveCamera(43, 21, 0, 4000)
    SetCameraDistance(14500, 4000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-57600, 900, 118600, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    MoveCamera(333, 29, 0, 4000)
    SetCameraDistance(15000, 4000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-52000, 900, 123900, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(14000, 3000)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0181
    AnonymousTalk(
        0x23,
        (
            "議事進行は僭越#4Rせんえつ#ながら\x01",
            "私、ヘンリー・マクダエルが\x01",
            "行わせていただきます。\x02\x03",

            "会議は一度休憩を挟んで、\x01",
            "約５時間を予定しております。\x02\x03",

            "ただし進行次第では\x01",
            "多少の延長はありえますので\x01",
            "よろしくご了承ください。\x02\x03",

            "それと──会議に際して\x01",
            "２名のオブザーバーに\x01",
            "参加してもらっています。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetChrSubChip(0x23, 0x1)
    SetChrSubChip(0x1D, 0x1)
    OP_68(-41100, 900, 121250, 2500)
    MoveCamera(90, 15, 0, 2500)
    SetCameraDistance(15000, 2500)
    OP_6F(0x79)
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x2)
    SetChrSubChip(0x20, 0x2)
    Sleep(300)

    #C0182
    ChrTalk(
        0x23,
        (
            "#02503F#6P#Nイアン・グリムウッド弁護士。\x02\x03",

            "クロスベルのみならず周辺諸国で\x01",
            "活躍している法律専門家です。\x02\x03",

            "#02500F国際法・慣習法にも通じているため\x01",
            "本会議への参加を要請しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x24, 0x27)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -40100, 0, 120250, 270)
    OP_0D()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0183
    AnonymousTalk(
        0x24,
        (
            "初めまして……\x01",
            "イアン・グリムウッドです。\x02",
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

    #C0184
    ChrTalk(
        0x1F,
        (
            "#07200F#12P#Nほう、あなたが\x01",
            "有名な《熊ヒゲ先生》か。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0185
    ChrTalk(
        0x21,
        (
            "ふむ、人権問題などにも\x01",
            "積極的に関わられているとか。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(100)

    #C0186
    ChrTalk(
        0x20,
        "#07002F#12P#Nふふ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0187
    ChrTalk(
        0x24,
        (
            "#5P#02210Fはは……誠心誠意、\x01",
            "務めさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-46900, 900, 126600, 2500)
    MoveCamera(0, 15, 0, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    Sleep(300)

    #C0188
    ChrTalk(
        0x23,
        (
            "#6P#02503F遊撃士、アリオス・マクレイン。\x02\x03",

            "やはり周辺諸国で多大な功績を\x01",
            "上げていることで知られています。\x02\x03",

            "#02500F遊撃士協会という中立的立場から\x01",
            "本会議の安全を保障してもらうため、\x01",
            "参加を要請しました。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x8)
    Sleep(130)
    SetChrSubChip(0x17, 0x9)
    Sleep(130)
    SetChrSubChip(0x17, 0xA)
    Sleep(800)
    SetChrSubChip(0x17, 0x9)
    Sleep(130)
    SetChrSubChip(0x17, 0x8)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("遊撃士アリオス")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            "アリオス・マクレインです。\x01",
            "お見知りおきを。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0190
    ChrTalk(
        0x22,
        (
            "#07509F#6P#Nハハ、《風の剣聖》だったか？\x02\x03",

            "#07500F共和国でも何度か\x01",
            "君の名前は耳にしておるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0191
    ChrTalk(
        0x1E,
        (
            "#07404F#11P#12P#N帝都でもたまに聞きますな。\x02\x03",

            "#07400Fかのクロスベルの地に\x01",
            "風をまとう《剣聖》ありと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x17, 0x8)
    Sleep(130)
    SetChrSubChip(0x17, 0xC)
    Sleep(130)
    SetChrSubChip(0x17, 0xD)

    #N0192
    NpcTalk(
        0x17,
        "遊撃士アリオス",
        "#01404F……恐縮です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-52000, 1000, 120500, 0)
    MoveCamera(90, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x23, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    OP_0D()
    Sleep(300)

    #C0193
    ChrTalk(
        0x23,
        (
            "#02503F#5Pそれでは早速となりますが、\x01",
            "各議案の検討に入りましょう。\x02\x03",

            "#02500F提議者、ディーター・クロイス市長。\x01",
            "説明と補足をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x1D,
        "#6P#02804Fは。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -54850, 50, 123900, 180)
    OP_0D()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0195
    AnonymousTalk(
        0x1D,
        (
            "まず、お手元にある資料の\x01",
            "最初にある議案ですが──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_628B end

    def Function_37_707C(): pass

    label("Function_37_707C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(73000, 1200, -1000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 74500, 0, -1000, 270)
    SetChrPos(0x102, 73800, 0, 200, 225)
    SetChrPos(0x103, 73800, 0, -2200, 315)
    SetChrPos(0x104, 72200, 0, 200, 135)
    SetChrPos(0x109, 71500, 0, -1000, 90)
    SetChrPos(0x105, 72200, 0, -2200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0196
    ChrTalk(
        0x101,
        (
            "#11P#00000Fよし……\x01",
            "これで一通り回ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x109,
        (
            "#6P#10100F今のところは\x01",
            "特に問題なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#5P#00302Fああ、この調子でもう一度、\x01",
            "見て回るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x02\x03",

            "#00108F……会議の方は\x01",
            "どうなっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな、市長や議長が\x01",
            "頑張っているとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        (
            "#12P#00201F問題は《鉄血宰相》に\x01",
            "ロックスミス大統領ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、休憩時間になったら\x01",
            "誰かに聞けばいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 39)
    Return()

    # Function_37_707C end

    def Function_38_730B(): pass

    label("Function_38_730B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-55500, 1200, -1500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -54000, 0, -1500, 270)
    SetChrPos(0x102, -54700, 0, -300, 225)
    SetChrPos(0x103, -54700, 0, -2700, 315)
    SetChrPos(0x104, -56300, 0, -300, 135)
    SetChrPos(0x109, -57000, 0, -1500, 90)
    SetChrPos(0x105, -56300, 0, -2700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0203
    ChrTalk(
        0x101,
        (
            "#11P#00000Fよし……\x01",
            "これで一通り回ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x109,
        (
            "#6P#10100F今のところは\x01",
            "特に問題なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x104,
        (
            "#5P#00302Fああ、この調子でもう一度、\x01",
            "見て回るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x02\x03",

            "#00108F……会議の方は\x01",
            "どうなっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな、市長や議長が\x01",
            "頑張っているとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#12P#00201F問題は《鉄血宰相》に\x01",
            "ロックスミス大統領ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、休憩時間になったら\x01",
            "誰かに聞けばいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 39)
    Return()

    # Function_38_730B end

    def Function_39_759A(): pass

    label("Function_39_759A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch11100.itc", 0x1F)
    LoadChrToIndex("chr/ch11000.itc", 0x20)
    LoadChrToIndex("chr/ch11800.itc", 0x21)
    LoadChrToIndex("chr/ch11700.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05800.itc", 0x24)
    LoadChrToIndex("chr/ch00900.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("chr/ch47900.itc", 0x27)
    LoadChrToIndex("apl/ch50314.itc", 0x28)
    LoadChrToIndex("chr/ch27400.itc", 0x29)
    LoadChrToIndex("chr/ch27800.itc", 0x2A)
    LoadChrToIndex("chr/ch27900.itc", 0x2B)
    LoadChrToIndex("chr/ch47500.itc", 0x2C)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(851)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -50800, 0, 125000, 180)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -49600, 0, 125000, 180)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -51900, 0, 125200, 180)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -54200, 0, 125000, 180)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -53100, 0, 125200, 180)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -48500, 0, 125200, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -55300, 0, 125200, 180)
    SetChrChipByIndex(0x25, 0x25)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -44300, 0, 122800, 225)
    SetChrChipByIndex(0x36, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -50040, 0, 120090, 180)
    SetChrChipByIndex(0x37, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, -54210, 0, 120370, 180)
    SetChrChipByIndex(0x3D, 0x26)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, -52870, 0, 116730, 358)
    SetChrChipByIndex(0x3E, 0x28)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, -53430, 0, 117400, 0)
    SetChrChipByIndex(0x3F, 0x27)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -51370, 0, 117370, 0)
    SetChrChipByIndex(0x40, 0x29)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -53630, 0, 115630, 0)
    SetChrChipByIndex(0x41, 0x2A)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrPos(0x41, -51990, 0, 116190, 0)
    SetChrChipByIndex(0x42, 0x2B)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrPos(0x42, -50340, 0, 116750, 0)
    SetChrChipByIndex(0x43, 0x2C)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    SetChrPos(0x43, -51300, 0, 115500, 348)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)
    OP_68(-52000, 1100, 120300, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日、１５：０５──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(300)
    SetChrName("")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やがて──会議の前半が終了し、\x01",
            "休憩時間に入る前に、報道陣による\x01",
            "各国首脳への合同取材が行われた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(40, 19, 0, 9000)
    SetCameraDistance(21500, 9000)
    BeginChrThread(0x3E, 0, 0, 40)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(851, 2, 100, 0)
    OP_0D()
    Sleep(5000)
    StopSound(851, 2000, 100)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    EndChrThread(0x3E, 0x0)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x142, 1)
    OP_24(0x353)
    SetScenarioFlags(0x22, 2)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_759A end

    def Function_40_79C9(): pass

    label("Function_40_79C9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7A81")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_79F7")
    Sleep(500)
    Jump("loc_7A3F")

    label("loc_79F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A0E")
    Sleep(1000)
    Jump("loc_7A3F")

    label("loc_7A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A25")
    Sleep(1500)
    Jump("loc_7A3F")

    label("loc_7A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7A3C")
    Sleep(2000)
    Jump("loc_7A3F")

    label("loc_7A3C")

    Sleep(2500)

    label("loc_7A3F")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_40_79C9")

    label("loc_7A81")

    Return()

    # Function_40_79C9 end

    def Function_41_7A82(): pass

    label("Function_41_7A82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 215)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    OP_68(-52580, 3500, 121120, 0)
    MoveCamera(104, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18820, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日、１６：３０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(300)
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして──通商会議の後半は\x01",
            "イアン弁護士の懸念どおり、\x01",
            "波乱含みの展開から始まった。\x02\x03",

            "帝国と共和国の双方から\x01",
            "クロスベルの安全保障に関する\x01",
            "厳しい問題提起が次々と出され……\x02\x03",

            "ディーター市長とマクダエル議長の\x01",
            "表情は次第に強張っていくのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-52580, 1500, 121120, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-53220, 1500, 119580, 100000)
    MoveCamera(81, 11, 0, 100000)

    #C0214
    ChrTalk(
        0x1E,
        (
            "#5P#07403F──問題は、たかが宗教団体一つで\x01",
            "ああも無様に治安が揺らいだことだ。\x02\x03",

            "#07401Fそれも治安維持組織が操られるなど、\x01",
            "前代未聞の形によって。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0215
    ChrTalk(
        0x1D,
        "#6P#02803F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0216
    ChrTalk(
        0x23,
        (
            "#02500F#6P……詳細については皆様にも\x01",
            "お伝えしてあると思いますが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0217
    ChrTalk(
        0x1E,
        (
            "#5P#07403F詳細が問題なのではない。\x01",
            "危機管理の“質”が問題なのだ。\x02\x03",

            "#07401F事件の際、滞在していた帝国人の\x01",
            "生命と財産が脅かされた事実もある。\x02\x03",

            "その事についてはどうお考えか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1F, 0x2)
    Sleep(300)

    #C0218
    ChrTalk(
        0x1F,
        (
            "#11P#07203F──待ちたまえ、宰相。\x02\x03",

            "#07201F損害賠償と慰謝料については\x01",
            "既に手続きが行われているはずだ。\x02\x03",

            "この上さらにミラを出せというのは\x01",
            "我が帝国の度量が問われるだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    #C0219
    ChrTalk(
        0x1E,
        (
            "#5P#07400Fいえ、殿下。\x01",
            "そういう問題ではありません。\x02\x03",

            "問題は彼らが……\x01",
            "クロスベル自治州政府がどうやって\x01",
            "様々な『安全』を保障できるかです。\x02\x03",

            "#07403F生命の安全、財産の安全、\x01",
            "貿易・金融市場への信頼の安全！\x02\x03",

            "#07401F政争にかまけ、怪しげな輩どもに\x01",
            "付け込まれるような者たちに\x01",
            "果たして保障できましょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0220
    ChrTalk(
        0x1F,
        "#11P#07208F……む………\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x21,
        (
            "#4P#Nだが、ハルトマン元議長が失脚し、\x01",
            "腐敗も浄化されつつあると聞く……\x02\x03",

            "今後は健全な政治体制の下で\x01",
            "しっかりとした安全保障の枠組みが\x01",
            "築かれればいいのではありませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x2)
    Sleep(300)

    #C0222
    ChrTalk(
        0x22,
        (
            "#6P#07500F#Nいやいや、大公閣下。\x01",
            "事はそう簡単ではありませんぞ？\x02\x03",

            "クロスベルの政治風土は\x01",
            "元々、腐敗しがちな傾向にあります。\x02\x03",

            "ディーター市長、マクダエル議長は\x01",
            "政治家としても傑出されていますが……\x02\x03",

            "仮に彼らに何かあった場合、\x01",
            "逆戻りになるのではありませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x21, 0x1)
    Sleep(300)

    #C0223
    ChrTalk(
        0x21,
        "#4P#Nふむ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0224
    ChrTalk(
        0x20,
        (
            "#11P#07003F……悲観的な話になりますが\x01",
            "元々、政治に腐敗は付きものです。\x02\x03",

            "#07008Fそれはクロスベルだけではなく、\x01",
            "我が国も含めてどこも同じ……\x02\x03",

            "#07001Fならば今は、お２人が任期中に\x01",
            "健全な政治体制を作れるか\x01",
            "見守るべきではないでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0225
    ChrTalk(
        0x1E,
        (
            "#5P#07404F……失礼ながら殿下はお若い。\x01",
            "希望を信じたくなる気も判ります。\x02\x03",

            "#07403Fですがクロスベルは、伝統ある\x01",
            "王家を戴#2Rいただ#くリベールとは違うのです。\x02\x03",

            "拠#2Rよ#り所となる権威の無いところでは\x01",
            "政治はかくも容易く弱体化する……\x02\x03",

            "#07401Fそれは歴史が証明しているでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0226
    ChrTalk(
        0x20,
        "#11P#07005Fそ、それは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x0)
    Sleep(300)

    #C0227
    ChrTalk(
        0x22,
        (
            "#6P#07503F#Nふむ、我が国には君主はおりませんが、\x01",
            "栄誉ある共和国憲章があります。\x02\x03",

            "#07500Fこれは、百年前の革命の時、\x01",
            "様々な勢力と民族が集まって\x01",
            "作り上げた奇跡的なものでしてな。\x02\x03",

            "それを頼りに、我が国の政治は\x01",
            "たとえ腐敗しても誇りを失わずに\x01",
            "存続できたと言えるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x2)
    Sleep(300)
    SetChrSubChip(0x1E, 0x0)

    #C0228
    ChrTalk(
        0x23,
        (
            "#02503F#5P……お言葉ですが、我々にも\x01",
            "誇りある自治州法が存在します。\x02\x03",

            "歴史的経緯から、様々な不備が\x01",
            "発生しているのも確かですが……\x02\x03",

            "#02500Fそれでも少しずつですが\x01",
            "改善できているのも確かです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    #C0229
    ChrTalk(
        0x1E,
        (
            "#11P#07400F……弁護士。\x01",
            "ここ１０年で行われた自治州法の\x01",
            "追加・改正項目はどの程度かな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0230
    ChrTalk(
        0x24,
        (
            "#5P#N#02205Fそ、そうですな。\x01",
            "詳しい資料はありませんが。\x02\x03",

            "#02203Fおよそ５０という所でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0231
    ChrTalk(
        0x22,
        (
            "#6P#07505F#N１０年でたった５０！\x01",
            "それはいささか驚きですな！\x02\x03",

            "１年にわずか５つですか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1D, 0x2)
    Sleep(300)

    #C0232
    ChrTalk(
        0x1D,
        (
            "#5P#02803Fいえ、ここ数年では\x01",
            "増加の傾向にあります。\x02\x03",

            "#02801F去年は確か、１２の項目が\x01",
            "追加・改正されたはずでしたね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_57(0x0)
    OP_5A()

    #C0233
    ChrTalk(
        0x23,
        (
            "#02505F#5Pああ、金融と導力ネットに関する\x01",
            "諸項目の追加が多いが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_57(0x0)
    OP_5A()

    #C0234
    ChrTalk(
        0x1E,
        (
            "#11P#07403Fいずれにせよ、その調子では\x01",
            "とても意義のある安全保障体制が\x01",
            "早急に構築できるとも思えぬ。\x02\x03",

            "#07401Fやはり現状を踏まえた対応策を\x01",
            "話し合うべきであろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0235
    ChrTalk(
        0x22,
        "#6P#07504F#Nええ、それは同感ですな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)

    #C0236
    ChrTalk(
        0x1F,
        (
            "#11P#07206F……やれやれ、あなた方が\x01",
            "そこまで気が合うとは思わなかった。\x02\x03",

            "#07201Fノルド高原の領有問題についても\x01",
            "すぐに合意できるのではないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0237
    ChrTalk(
        0x22,
        "#6P#07509F#Nはは、これは一本取られましたな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0238
    ChrTalk(
        0x1E,
        (
            "#5P#07404Fまあ、それについては\x01",
            "別の機会に話し合いましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0239
    ChrTalk(
        0x20,
        "#11P#07008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0240
    ChrTalk(
        0x21,
        (
            "#4P#Nふむ、時間が惜しい。\x01",
            "議論を移るべきでしょうな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0241
    ChrTalk(
        0x23,
        (
            "#02503F#5P……分かりました。\x01",
            "では宰相閣下の提議の通り──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19320, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_7A82 end

    def Function_42_8C3E(): pass

    label("Function_42_8C3E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05800.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x2)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -49100, 50, 123900, 135)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    OP_68(-46970, 2000, 122960, 0)
    MoveCamera(53, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21890, 0)
    VolumeBGM(0x64, 0x3E8)
    OP_68(-46970, 1000, 122960, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x23,
        (
            "#02501F#5P宰相閣下……\x01",
            "今、何とおっしゃられた？\x02\x03",

            "申しわけないが今一度、\x01",
            "繰り返していただきたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x1E,
        (
            "#07404F#11Pフフ、お望みなら何度でも。\x02\x03",

            "#07401F──クロスベル警備隊は解体。\x02\x03",

            "さらに、他国の治安維持部隊を\x01",
            "クロスベルに常駐させること……\x02\x03",

            "それが一番現実的だと申し上げた。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x23,
        "#02501F#5P……ッ！\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1D,
        "#6P#02801F#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0246
    ChrTalk(
        0x20,
        (
            "#5P#07007F#11P#Nお、お待ちください！\x02\x03",

            "宰相閣下は、不戦条約の条項を\x01",
            "お忘れではありませんか……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    #C0247
    ChrTalk(
        0x1E,
        (
            "#5P#07405Fああ、武力でクロスベル問題を\x01",
            "解決しないよう努める、ですか。\x02\x03",

            "#07404Fしかし別に侵略をすることを\x01",
            "意味している訳ではありません。\x02\x03",

            "#07402F──民間人を恐怖に陥れた\x01",
            "軍隊もどきの役立たずな組織など\x01",
            "解体すべきだと言っているのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0248
    ChrTalk(
        0x20,
        "#5P#11P#N#07005F！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)

    #C0249
    ChrTalk(
        0x1E,
        (
            "#11P#07404F実際、クロスベル警備隊など\x01",
            "帝国軍、または共和国軍の前には\x01",
            "存在しないも同然です。\x02\x03",

            "高性能な装甲車にしても\x01",
            "所詮、戦車の前では紙切れ同然。\x02\x03",

            "#07400Fそんなものに高い維持費を使うなら\x01",
            "他国の戦力に安全保障を委ねる──\x02\x03",

            "#07402Fそれが“自治州”ごときには\x01",
            "一番効率がいい在り方でしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0250
    ChrTalk(
        0x21,
        (
            "#11P……いささか\x01",
            "乱暴すぎる意見に思えますが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0251
    ChrTalk(
        0x1F,
        (
            "#11P#07203Fその『他国の戦力』というのは\x01",
            "どこを指しているのかな？\x02\x03",

            "#07200Fまさか宰相閣下ともあろう人が\x01",
            "歴史的経緯を忖度#4Rそんたく#もせず、\x01",
            "帝国軍などと言わないだろうね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0252
    ChrTalk(
        0x1E,
        (
            "#11P#07404Fハハ、そうは申していません。\x02\x03",

            "#07402F──ですが必要ならば\x01",
            "過去の因縁を水に流してでも\x01",
            "帝国軍の力を提供すべきでしょう。\x02\x03",

            "それがゼムリア大陸西部の\x01",
            "平和と発展に繋がるのならば。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x23,
        "#02501F#5Pくっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-52480, 1200, 120270, 0)
    MoveCamera(87, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21890, 0)
    SetChrPos(0x17, -46900, 0, 126600, 225)
    OP_0D()

    #C0254
    ChrTalk(
        0x22,
        (
            "#6P#07506F……まあまあ。\x01",
            "皆さん、そう熱くならずに。\x02\x03",

            "#07501F宰相閣下の提案は\x01",
            "私もいささか強引に思えますな。\x02\x03",

            "#07504F──ただまあ、警備隊などという\x01",
            "軍にもなりきれない治安維持組織が\x01",
            "中途半端というのも分かります。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    Sleep(200)

    def lambda_9525():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9525)
    SetChrSubChip(0x21, 0x1)
    Sleep(50)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    SetChrSubChip(0x1D, 0x2)
    Sleep(50)

    #C0255
    ChrTalk(
        0x1E,
        "#5P#07405Fふむ、それでは？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x22,
        (
            "#6P#07502Fそこで提案なのですが、\x01",
            "警備隊は規模を大幅に縮小……\x02\x03",

            "変わりにベルガード門を帝国軍、\x01",
            "タングラム門を共和国軍が\x01",
            "管理するというのはどうですかな？\x02\x03",

            "そうすれば、クロスベル市の有事にも\x01",
            "すぐに駆けつけることが出来ましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x1D,
        "#5P#02801Fっ……！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x21,
        "#11P大統領、それは……\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1E,
        (
            "#5P#07404Fふむ、検討に値するかと。\x02\x03",

            "#07400Fさすがは大統領閣下。\x01",
            "数多の野党の突き上げを捌#2Rさば#きながら\x01",
            "政権運営されているだけはありますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x22,
        (
            "#6P#07509Fいやいや、頑迷な貴族勢力を抑えて\x01",
            "改革をされている宰相閣下に比べれば。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x20,
        "#11P#07008Fあ、あなた方は……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x1F,
        (
            "#11P#07203F……いいかげんにしたまえ。\x01",
            "ここは２国だけの会議ではないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1E,
        "#5P#07405Fおお、これは失礼した。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    #C0264
    ChrTalk(
        0x1E,
        (
            "#11P#07404Fいずれにせよ、斯様#4R か よう#な方向に\x01",
            "議論は流れてきたわけだが……\x02\x03",

            "#07402Fお２人の意見はどうかな？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_987A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_987A)
    Sleep(100)
    SetChrSubChip(0x1D, 0x0)
    Sleep(250)

    #C0265
    ChrTalk(
        0x23,
        "#02501F#6P…………くっ………………\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x1D,
        "#6P#02803F……………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22390, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 3)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_8C3E end

    def Function_43_9903(): pass

    label("Function_43_9903")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    LoadChrToIndex("chr/ch00900.itc", 0x27)
    LoadChrToIndex("chr/ch10900.itc", 0x28)
    LoadChrToIndex("chr/ch11100.itc", 0x29)
    LoadChrToIndex("chr/ch11000.itc", 0x2A)
    LoadChrToIndex("chr/ch11800.itc", 0x2B)
    LoadChrToIndex("chr/ch11710.itc", 0x2C)
    LoadChrToIndex("chr/ch05800.itc", 0x2D)
    LoadChrToIndex("chr/ch05900.itc", 0x2E)
    LoadChrToIndex("chr/ch02400.itc", 0x2F)
    LoadEffect(0x1, "battle/sc008100.eff")
    LoadEffect(0x2, "event/ev12001.eff")
    SoundLoad(497)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(825)
    SoundLoad(866)
    SoundLoad(4051)
    SoundLoad(3457)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x1)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x1)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -54850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    SetChrChipByIndex(0x25, 0x27)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -52000, 0, 99000, 0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    OP_78(0x12, 0x44)
    OP_49()
    SetChrPos(0x44, -42000, -18000, 144000, 190)
    OP_D5(0x44, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x3D)
    OP_71(0x12, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x45, 0x80)
    OP_78(0x13, 0x45)
    OP_49()
    SetChrPos(0x45, -62000, -20000, 144000, 170)
    OP_D5(0x45, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x3D)
    OP_71(0x13, 0x3D, 0x78, 0x0, 0x20)
    OP_68(-54240, 3000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    VolumeBGM(0x64, 0x3E8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-54240, 2000, 116060, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)

    #C0267
    ChrTalk(
        0x1D,
        (
            "#5P#02803F今、この場で語られている\x01",
            "安全保障の議論について……\x02\x03",

            "#02800F一つ私の方から\x01",
            "提案させて欲しい事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x1E,
        "#11P#07405Fほう……？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x22,
        (
            "#6P#07509Fハハハ、先ほどから\x01",
            "大人しいと思っていたが……\x02\x03",

            "#07502F何を仰られるおつもりかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x1D,
        "#5P#02800Fええ、それは──\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x17, 0x20)
    OP_93(0x17, 0xE1, 0x320)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    #N0271
    NpcTalk(
        0x17,
        "遊撃士アリオス",
        "#01407F#4051V#6P#4S#15A──方々#4Rかたがた#、下がられよ！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_9DF2():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9DF2)
    OP_68(-52000, 1000, 128500, 2000)
    Sleep(1000)
    Fade(500)
    OP_68(-52000, 0, 135000, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-52000, 4000, 130000, 4000)
    MoveCamera(0, 13, 0, 4000)
    SetCameraDistance(30000, 4000)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    BeginChrThread(0x4C, 1, 0, 57)
    BeginChrThread(0x44, 3, 0, 44)
    BeginChrThread(0x45, 3, 0, 45)
    SetChrSubChip(0x1E, 0x2)

    def lambda_9E8D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9E8D)
    WaitChrThread(0x44, 3)
    WaitChrThread(0x45, 3)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)
    ReplaceBGM("ed7151", "ed7544")
    ReplaceBGM("ed7550", "ed7544")
    ReplaceBGM("ed7300", "ed7561")

    #C0272
    ChrTalk(
        0x23,
        "#02507F#12P#Nな──！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0273
    ChrTalk(
        0x20,
        "#07005F#12P#N飛行艇……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_87(0x1, 0x0, 0x13, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x12, "Null_gun_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x2, 0x12, "Null_gun_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x2, 0x3, 0xFF, 0x0, -44000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0xFF, 0x0, -60000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_71(0x14, 0x0, 0x1D, 0x0, 0x0)
    OP_71(0x15, 0x0, 0x1D, 0x0, 0x0)
    SetCameraDistance(27000, 2000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x1F40)
    Sleep(2000)
    Fade(500)
    SetChrPos(0x44, -40000, 1000, 144000, 0)
    SetChrPos(0x45, -60000, 1000, 144000, 0)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -49100, 50, 123900, 0)
    OP_68(-44000, 5000, 130000, 0)
    MoveCamera(43, 5, -10, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_68(-56000, 5000, 130000, 6000)
    MoveCamera(33, 5, 10, 6000)
    SetCameraDistance(24500, 6000)
    OP_0D()
    OP_71(0x14, 0x1E, 0x31, 0x0, 0x0)
    OP_71(0x15, 0x1E, 0x31, 0x0, 0x0)
    OP_6F(0x79)
    StopSound(865, 300, 100)
    StopSound(861, 300, 100)
    Sound(866, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)

    #C0274
    ChrTalk(
        0x21,
        "くっ……！\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x1F,
        (
            "#07207Fまさか……\x01",
            "テロリストどもか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x1E,
        "#07401F……………………………\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x22,
        "#07505F#5Pここで来たか……！\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x1D,
        (
            "#02807F#11Pご安心を！\x01",
            "砲撃にも耐えられる\x01",
            "特注の強化ガラスです！\x02\x03",

            "ですが念のため\x01",
            "全員、お下がりください！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x20)
    BeginChrThread(0x1D, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 47)
    BeginChrThread(0x23, 3, 0, 48)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_87(0x1, 0x0, 0x13, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x12, "Null_gun_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x2, 0x12, "Null_gun_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x2, 0x3, 0xFF, 0x0, -44000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0xFF, 0x0, -60000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x14, 0x32, 0x46, 0x0, 0x0)
    OP_71(0x15, 0x32, 0x46, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xBB8)
    Sleep(3000)
    StopSound(865, 300, 100)
    StopSound(861, 300, 100)
    Sound(866, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    BeginChrThread(0x44, 3, 0, 49)
    BeginChrThread(0x45, 3, 0, 50)
    Sleep(400)
    StopSound(497, 4000, 60)
    StopSound(825, 4000, 50)
    WaitChrThread(0x44, 3)
    WaitChrThread(0x45, 3)
    Fade(500)
    OP_68(-38000, 1100, 110200, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x23, 0xFF)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, -36500, 0, 110200, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, -36500, 0, 110200, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, -36500, 0, 110200, 270)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -36500, 0, 110200, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -67400, 0, 110200, 90)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    SetChrPos(0xB, -67400, 0, 110200, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1E, 0x28)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -50700, 0, 106700, 0)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -49500, 0, 106000, 0)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -50000, 0, 104300, 0)
    SetChrChipByIndex(0x21, 0x2B)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, -54000, 0, 104300, 0)
    SetChrChipByIndex(0x22, 0x2C)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -54900, 0, 105200, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -48900, 0, 103000, 0)
    SetChrPos(0x1D, -53100, 0, 107000, 0)
    SetChrPos(0x23, -52700, 0, 105600, 0)
    SetChrPos(0x17, -51000, 0, 108300, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    OP_68(-52000, 1100, 105600, 4000)
    MoveCamera(38, 23, 0, 4000)
    SetCameraDistance(17000, 4000)
    BeginChrThread(0xA, 3, 0, 51)
    Sleep(600)
    BeginChrThread(0x9, 3, 0, 52)
    Sleep(600)
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(600)
    BeginChrThread(0x8, 3, 0, 54)
    BeginChrThread(0xB, 3, 0, 55)
    Sleep(600)
    BeginChrThread(0xC, 3, 0, 56)
    WaitChrThread(0xA, 3)

    #C0279
    ChrTalk(
        0xA,
        "#07107F#11P殿下、ご無事ですか！\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x20,
        "#6P#07008Fええ、何とか……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(150)

    #C0281
    ChrTalk(
        0x9,
        (
            "#07301F今のは……\x01",
            "ラインフォルトの高速艇か。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(150)

    #C0282
    ChrTalk(
        0x1F,
        "#12P#07201Fああ、間違いないだろう。\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(150)

    #C0283
    ChrTalk(
        0xB,
        (
            "#12P#N#12001Fもう一隻はヴェルヌ社の\x01",
            "軍用ガンシップですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xC, 0x0, 0x1F4)
    Sleep(150)

    #C0284
    ChrTalk(
        0xC,
        (
            "ええ、連中に奪われたことは\x01",
            "報告にありましたが……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(121, 0, 100, 0)
    Sound(811, 0, 50, 0)
    ClearChrFlags(0x25, 0x80)

    def lambda_A86D():
        OP_96(0xFE, 0xFFFF34E0, 0x0, 0x19258, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_A86D)

    def lambda_A887():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_A887)
    WaitChrThread(0x25, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    #C0285
    ChrTalk(
        0x25,
        "#12P#00607F#3457V#30W皆さん、ご無事ですか！\x02",
    )

    CloseMessageWindow()
    OP_24(0xD81)
    OP_C9(0x1, 0x80000000)

    def lambda_A8ED():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_A8ED)

    def lambda_A8FA():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_A8FA)
    Sleep(50)

    def lambda_A90A():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A90A)

    def lambda_A917():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_A917)

    def lambda_A924():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_A924)
    Sleep(50)

    def lambda_A934():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_A934)

    def lambda_A941():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_A941)
    Sleep(50)

    def lambda_A951():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_A951)

    def lambda_A95E():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A95E)

    #C0286
    ChrTalk(
        0x23,
        "#02501F#5Pああ、何とか……！\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x1D,
        "#02801F#5Pしかし連中はどこへ……\x02",
    )

    CloseMessageWindow()
    Sound(867, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("男の声")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "……ふむ。\x01",
            "聞こえているようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-52000, 1100, 106600, 1000)
    SetCameraDistance(18000, 1000)

    def lambda_AA10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_AA10)

    def lambda_AA1D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_AA1D)
    Sleep(50)

    def lambda_AA2D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_AA2D)

    def lambda_AA3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_AA3A)

    def lambda_AA47():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_AA47)
    Sleep(50)

    def lambda_AA57():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_AA57)

    def lambda_AA64():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_AA64)

    def lambda_AA71():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AA71)

    def lambda_AA7E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_AA7E)
    Sleep(50)

    def lambda_AA8E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_AA8E)

    def lambda_AA9B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AA9B)

    def lambda_AAA8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_AAA8)

    def lambda_AAB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AAB5)
    OP_6F(0x79)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("男の声")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──会議に出席されている方々。\x01",
            "我々は『帝国解放戦線』である。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("青年の声")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──同じくカルバードの\x01",
            "旧き伝統を守るために立ち上がった\x01",
            "『反移民政策主義』の一派の者だ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0291
    ChrTalk(
        0x21,
        "#12Pなんだと……！？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x24,
        (
            "#12P#02205F帝国と共和国で活動している\x01",
            "テロリスト集団……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("男の声")

    #A0293
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "この度、我々は互いの\x01",
            "憎むべき怨敵#4Rおんてき#を討たんがため\x01",
            "共に協力することと相なった。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("男の声")

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "──覚悟してもらおう！\x01",
            "《鉄血宰相》ギリアス・オズボーン！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("青年の声")

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "ロックスミス大統領！\x01",
            "貴方にはここで消えていただく！\x02",
        )
    )

    CloseMessageWindow()

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "忌まわしき東方人に侵食された\x01",
            "カルバードの伝統を守るためには\x01",
            "そのくらいの荒療治が必要なのだッ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0297
    ChrTalk(
        0x22,
        "#6P#07506F……愚かなことを。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x1E,
        "#07403F#12Pフム、話にならんな。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#11P#N#11508Fだが……\x01",
            "ちょいとマズそうだなァ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0300
    NpcTalk(
        0x17,
        "遊撃士アリオス",
        "#11P#01401Fああ──来るぞ。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x25,
        "#12P#00610Fくっ……！\x02",
    )

    CloseMessageWindow()
    OP_68(-52000, 1600, 106600, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x1F1)
    OP_24(0x339)
    SetScenarioFlags(0x22, 2)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_9903 end

    def Function_44_AEB2(): pass

    label("Function_44_AEB2")


    def lambda_AEB7():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEB7)
    Sleep(1500)

    def lambda_AED4():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AED4)
    Sleep(300)

    def lambda_AEF1():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEF1)
    Sleep(300)

    def lambda_AF0E():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF0E)
    Sleep(300)

    def lambda_AF2B():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF2B)
    Sleep(300)

    def lambda_AF48():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF48)
    Sleep(300)

    def lambda_AF65():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF65)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_AEB2 end

    def Function_45_AF7F(): pass

    label("Function_45_AF7F")


    def lambda_AF84():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF84)
    Sleep(1500)

    def lambda_AFA1():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFA1)
    Sleep(300)

    def lambda_AFBE():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFBE)
    Sleep(300)

    def lambda_AFDB():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFDB)
    Sleep(300)

    def lambda_AFF8():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFF8)
    Sleep(300)

    def lambda_B015():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B015)
    Sleep(300)

    def lambda_B032():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B032)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_AF7F end

    def Function_46_B04C(): pass

    label("Function_46_B04C")


    def lambda_B051():
        OP_95(0xFE, -56700, 0, 123900, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B051)
    WaitChrThread(0x1D, 1)

    def lambda_B06F():
        OP_95(0xFE, -59000, 0, 120600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B06F)
    WaitChrThread(0x1D, 1)

    def lambda_B08D():
        OP_95(0xFE, -59000, 0, 118600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_B08D)
    WaitChrThread(0x1D, 1)
    Return()

    # Function_46_B04C end

    def Function_47_B0A7(): pass

    label("Function_47_B0A7")


    def lambda_B0AC():
        OP_95(0xFE, -48000, 0, 124600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B0AC)
    WaitChrThread(0x17, 1)
    Sleep(500)

    def lambda_B0CD():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B0CD)
    WaitChrThread(0x17, 1)

    def lambda_B0EB():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B0EB)
    WaitChrThread(0x17, 1)

    def lambda_B109():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B109)
    WaitChrThread(0x17, 1)
    Return()

    # Function_47_B0A7 end

    def Function_48_B123(): pass

    label("Function_48_B123")

    Sleep(1000)

    def lambda_B12B():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B12B)
    WaitChrThread(0x23, 1)

    def lambda_B149():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B149)
    WaitChrThread(0x23, 1)

    def lambda_B167():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_B167)
    WaitChrThread(0x23, 1)
    Return()

    # Function_48_B123 end

    def Function_49_B181(): pass

    label("Function_49_B181")


    def lambda_B186():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B186)
    Sleep(300)

    def lambda_B1A3():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1A3)
    Sleep(300)

    def lambda_B1C0():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1C0)
    Sleep(300)

    def lambda_B1DD():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1DD)
    Sleep(300)

    def lambda_B1FA():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1FA)
    Sleep(300)

    def lambda_B217():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B217)
    Sleep(300)

    def lambda_B234():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B234)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_B181 end

    def Function_50_B24E(): pass

    label("Function_50_B24E")

    Sleep(400)

    def lambda_B256():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B256)
    Sleep(300)

    def lambda_B273():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B273)
    Sleep(300)

    def lambda_B290():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B290)
    Sleep(300)

    def lambda_B2AD():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2AD)
    Sleep(300)

    def lambda_B2CA():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2CA)
    Sleep(300)

    def lambda_B2E7():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2E7)
    Sleep(300)

    def lambda_B304():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B304)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_B24E end

    def Function_51_B31E(): pass

    label("Function_51_B31E")


    def lambda_B323():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B323)

    def lambda_B33D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B33D)
    WaitChrThread(0xFE, 1)

    def lambda_B352():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B352)
    WaitChrThread(0xFE, 1)

    def lambda_B370():
        OP_95(0xFE, -48800, 0, 104500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B370)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xA, 0x20, 500)
    TurnDirection(0x20, 0xA, 500)
    Return()

    # Function_51_B31E end

    def Function_52_B398(): pass

    label("Function_52_B398")


    def lambda_B39D():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B39D)

    def lambda_B3B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B3B7)
    WaitChrThread(0xFE, 1)

    def lambda_B3CC():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3CC)
    WaitChrThread(0xFE, 1)

    def lambda_B3EA():
        OP_95(0xFE, -48000, 0, 106500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3EA)
    WaitChrThread(0xFE, 1)
    TurnDirection(0x1F, 0x9, 500)
    Return()

    # Function_52_B398 end

    def Function_53_B40B(): pass

    label("Function_53_B40B")


    def lambda_B410():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B410)

    def lambda_B42A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B42A)
    WaitChrThread(0xFE, 1)

    def lambda_B43F():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B43F)
    WaitChrThread(0xFE, 1)

    def lambda_B45D():
        OP_95(0xFE, -49200, 0, 108000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B45D)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1E, 500)
    Return()

    # Function_53_B40B end

    def Function_54_B47E(): pass

    label("Function_54_B47E")


    def lambda_B483():
        OP_95(0xFE, -39800, 0, 110200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B483)

    def lambda_B49D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B49D)
    WaitChrThread(0xFE, 1)

    def lambda_B4B2():
        OP_95(0xFE, -42500, 0, 108000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4B2)
    WaitChrThread(0xFE, 1)

    def lambda_B4D0():
        OP_95(0xFE, -48000, 0, 108000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_B47E end

    def Function_55_B4EA(): pass

    label("Function_55_B4EA")


    def lambda_B4EF():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4EF)

    def lambda_B509():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B509)
    WaitChrThread(0xFE, 1)

    def lambda_B51E():
        OP_95(0xFE, -55900, 0, 104400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B51E)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_55_B4EA end

    def Function_56_B53F(): pass

    label("Function_56_B53F")


    def lambda_B544():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B544)

    def lambda_B55E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B55E)
    WaitChrThread(0xFE, 1)

    def lambda_B573():
        OP_95(0xFE, -55600, 0, 106300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B573)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_56_B53F end

    def Function_57_B594(): pass

    label("Function_57_B594")

    Sound(497, 2, 10, 0)
    Sound(825, 2, 10, 0)
    Sleep(80)
    OP_25(0x1F1, 0xF)
    OP_25(0x339, 0xF)
    Sleep(80)
    OP_25(0x1F1, 0x14)
    OP_25(0x339, 0x14)
    Sleep(80)
    OP_25(0x1F1, 0x19)
    OP_25(0x339, 0x19)
    Sleep(80)
    OP_25(0x1F1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(80)
    OP_25(0x1F1, 0x23)
    OP_25(0x339, 0x23)
    Sleep(80)
    OP_25(0x1F1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(80)
    OP_25(0x1F1, 0x2D)
    OP_25(0x339, 0x2D)
    Sleep(80)
    OP_25(0x1F1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(80)
    OP_25(0x1F1, 0x37)
    Sleep(80)
    OP_25(0x1F1, 0x3C)
    Return()

    # Function_57_B594 end

    def Function_58_B607(): pass

    label("Function_58_B607")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    OP_68(-39500, 1000, 106000, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x1)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x25, 0x20)
    SetChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -39500, 0, 106000, 270)
    SetCameraDistance(15500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0302
    ChrTalk(
        0x25,
        (
            "#00607F#11P──こちらに\x01",
            "まっすぐ向かっているだと！？\x02\x03",

            "#00606Fクッ、あの図面はこのために……\x02\x03",

            "#00610Fとにかく待機させていた警備隊を\x01",
            "こちらの方に急行させて──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetCameraDistance(15000, 300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)

    #C0303
    ChrTalk(
        0x25,
        "#00607F#4S#11Pなんだとッ！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_B607 end

    def Function_59_B788(): pass

    label("Function_59_B788")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02450.itc", 0x5)
    LoadChrToIndex("chr/ch02451.itc", 0x6)
    LoadChrToIndex("chr/ch00950.itc", 0x7)
    LoadChrToIndex("chr/ch00951.itc", 0x8)
    LoadChrToIndex("chr/ch00952.itc", 0x9)
    LoadChrToIndex("chr/ch00953.itc", 0xA)
    LoadChrToIndex("chr/ch42250.itc", 0xB)
    LoadChrToIndex("chr/ch42251.itc", 0xC)
    LoadChrToIndex("chr/ch42252.itc", 0xD)
    LoadChrToIndex("chr/ch42253.itc", 0xE)
    LoadChrToIndex("chr/ch42254.itc", 0xF)
    LoadChrToIndex("chr/ch42350.itc", 0x10)
    LoadChrToIndex("chr/ch42351.itc", 0x11)
    LoadChrToIndex("chr/ch42352.itc", 0x12)
    LoadChrToIndex("chr/ch42353.itc", 0x13)
    LoadChrToIndex("chr/ch42550.itc", 0x14)
    LoadChrToIndex("chr/ch42551.itc", 0x15)
    LoadChrToIndex("chr/ch42552.itc", 0x16)
    LoadChrToIndex("chr/ch42553.itc", 0x17)
    LoadChrToIndex("chr/ch42554.itc", 0x18)
    LoadChrToIndex("apl/ch51236.itc", 0x19)
    LoadChrToIndex("apl/ch51262.itc", 0x1A)
    LoadChrToIndex("apl/ch51263.itc", 0x1B)
    LoadChrToIndex("apl/ch51264.itc", 0x1C)
    LoadChrToIndex("apl/ch51237.itc", 0x1D)
    LoadChrToIndex("apl/ch51265.itc", 0x1E)
    LoadChrToIndex("apl/ch51238.itc", 0x1F)
    LoadChrToIndex("apl/ch51267.itc", 0x20)
    LoadChrToIndex("chr/ch02452.itc", 0x21)
    LoadChrToIndex("chr/ch02456.itc", 0x22)
    LoadChrToIndex("chr/ch00900.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51266.itc", 0x25)
    LoadChrToIndex("apl/ch51268.itc", 0x26)
    LoadChrToIndex("chr/ch00959.itc", 0x27)
    LoadEffect(0x0, "event/ev12013.eff")
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "battle/cr425100.eff")
    LoadEffect(0x4, "event/ev12012.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    SoundLoad(860)
    SoundLoad(861)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -15000, 0, 0, 90)
    SetChrPos(0x102, -15000, 0, 500, 90)
    SetChrPos(0x103, -15000, 0, 0, 90)
    SetChrPos(0x104, -15000, 0, 1000, 90)
    SetChrPos(0x109, -15000, 0, -1000, 90)
    SetChrPos(0x105, -15000, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x5)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12000, 0, 0, 270)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 13000, 0, 0, 270)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1D)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 14000, 0, 0, 270)
    SetChrChipByIndex(0x25, 0x9)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 23700, 0, -800, 90)
    SetChrChipByIndex(0x36, 0x19)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 23900, 0, 1000, 90)
    SetChrChipByIndex(0x37, 0x19)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, 24400, 0, -1900, 90)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 81000, 0, 5500, 180)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 80500, 0, 5500, 180)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 81500, 0, 5500, 180)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 80500, 0, 5500, 180)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2A, 0xC)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 81500, 0, 5500, 180)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x15)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 81000, 0, 5500, 180)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x15)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 80500, 0, 5500, 180)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 81500, 0, 5500, 180)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 80500, 0, 5500, 180)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x32, 0x15)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, 81500, 0, 5500, 180)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x4)
    OP_68(79000, 2500, 0, 0)
    MoveCamera(60, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(79000, 1500, 0, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    Sound(160, 0, 100, 0)
    Sleep(300)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)
    OP_68(72000, 1500, 0, 4000)
    MoveCamera(53, 13, 0, 4000)
    SetCameraDistance(17000, 4000)
    BeginChrThread(0x2E, 3, 0, 83)
    Sleep(400)
    BeginChrThread(0x2F, 3, 0, 84)
    Sleep(200)
    Sound(937, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x32, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x26, 3, 0, 83)
    Sleep(400)
    BeginChrThread(0x27, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x28, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x29, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x2A, 3, 0, 85)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x30, 0xFF)
    EndChrThread(0x31, 0xFF)
    EndChrThread(0x32, 0xFF)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x26, 0xFF)
    EndChrThread(0x27, 0xFF)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x2A, 0xFF)
    ClearChrFlags(0x46, 0x80)
    OP_78(0xF, 0x46)
    OP_49()
    SetChrPos(0x46, 25500, 0, 0, 0)
    OP_D5(0x46, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    SetChrChipByIndex(0x2E, 0x16)
    SetChrSubChip(0x2E, 0x3)
    SetChrChipByIndex(0x2F, 0x16)
    SetChrSubChip(0x2F, 0x3)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    SetChrChipByIndex(0x32, 0x16)
    SetChrSubChip(0x32, 0x3)
    SetChrPos(0x2E, 32800, 0, 1500, 270)
    SetChrPos(0x2F, 32200, 0, -100, 270)
    SetChrPos(0x30, 37500, 0, 300, 270)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x31, 37500, 0, -300, 270)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x32, 33700, 0, -2500, 270)
    OP_68(32900, 900, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(29200, 900, 0, 4000)
    SetCameraDistance(17500, 4000)
    ClearScenarioFlags(0x0, 1)
    FadeToBright(1000, 0)
    BeginChrThread(0x2E, 3, 0, 101)
    BeginChrThread(0x36, 3, 0, 88)
    BeginChrThread(0x4C, 1, 0, 122)
    BeginChrThread(0x4C, 2, 0, 123)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 26000, 700, 700, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(860, 2, 80, 0)
    Sleep(100)
    BeginChrThread(0x2F, 3, 0, 100)
    BeginChrThread(0x37, 3, 0, 88)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 26400, 700, -1600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    BeginChrThread(0x32, 3, 0, 101)
    BeginChrThread(0x25, 3, 0, 89)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 27500, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 3, 0, 82)
    Sound(861, 2, 80, 0)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x30, 3, 0, 86)
    Sleep(500)
    BeginChrThread(0x31, 3, 0, 87)
    Sound(2512, 255, 100, 0)    #voice#Dudley
    Sleep(3000)
    Sound(2513, 255, 100, 0)    #voice#Dudley
    OP_6F(0x79)
    OP_AD(0x1)
    EndChrThread(0x2F, 0x3)
    SetChrChipByIndex(0x2F, 0x18)
    SetChrSubChip(0x2F, 0x2)
    Sleep(100)
    SetChrSubChip(0x2F, 0x3)
    Sleep(200)
    SetChrSubChip(0x2F, 0x4)
    Sound(809, 0, 100, 0)
    Sound(250, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x2F, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x4C, 0x1)
    OP_68(24000, 500, 0, 500)
    MoveCamera(35, 25, 0, 500)
    SetCameraDistance(15500, 500)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 26000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    ClearMapObjFlags(0x10, 0x4)
    OP_75(0xF, 0x1, 0x12C)
    OP_75(0x10, 0x2, 0x12C)
    EndChrThread(0x36, 0x3)
    BeginChrThread(0x36, 3, 0, 102)
    Sleep(50)
    EndChrThread(0x37, 0x3)
    BeginChrThread(0x37, 3, 0, 103)
    Sleep(50)
    EndChrThread(0x25, 0x3)
    BeginChrThread(0x25, 3, 0, 104)
    StopSound(860, 3000, 70)
    StopSound(861, 3000, 70)

    #C0304
    ChrTalk(
        0x36,
        "#13Aうわあ～っ！\x02",
    )
    #Auto

    Sleep(50)

    #C0305
    ChrTalk(
        0x37,
        "#5P#13Aぎゃっ！\x02",
    )
    #Auto

    Sleep(50)

    #C0306
    ChrTalk(
        0x25,
        "#6P#00610F#13Aくっ……！\x02",
    )
    #Auto

    WaitChrThread(0x25, 3)
    OP_6F(0x79)
    LoadEffect(0x0, "battle/cr024101.eff")
    LoadEffect(0x4, "battle/cr024100.eff")
    LoadEffect(0x6, "battle/cr024201.eff")
    LoadEffect(0x7, "battle/cr024401.eff")
    Fade(500)
    OP_68(34500, 700, 0, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(33500, 700, 0, 2000)
    SetCameraDistance(17500, 2000)
    StopEffect(0x3, 0x0)
    SetChrPos(0x2E, 32800, 0, 2500, 270)
    SetChrChipByIndex(0x2E, 0x14)
    SetChrSubChip(0x2E, 0x0)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x4C, 0x2)
    SetChrPos(0x2F, 32200, 0, 900, 270)
    SetChrChipByIndex(0x2F, 0x14)
    SetChrSubChip(0x2F, 0x0)
    EndChrThread(0x2F, 0xFF)
    SetChrPos(0x30, 34200, 0, 1500, 270)
    SetChrChipByIndex(0x30, 0x14)
    SetChrSubChip(0x30, 0x0)
    EndChrThread(0x30, 0xFF)
    SetChrPos(0x31, 33400, 0, -1800, 270)
    SetChrChipByIndex(0x31, 0x14)
    SetChrSubChip(0x31, 0x0)
    EndChrThread(0x31, 0xFF)
    SetChrPos(0x32, 33700, 0, -3000, 270)
    SetChrChipByIndex(0x32, 0x14)
    SetChrSubChip(0x32, 0x0)
    EndChrThread(0x32, 0xFF)
    SetChrPos(0x26, 37700, 0, -300, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x27, 38900, 0, -1000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x28, 38900, 0, 0, 270)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x29, 40200, 0, -650, 270)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x25, 19700, 0, -1500, 90)
    SetChrPos(0x36, 21100, 0, 2900, 135)
    SetChrPos(0x37, 21100, 0, -3300, 90)
    SetMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)

    def lambda_C3BC():
        OP_95(0xFE, 29700, 0, -300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_C3BC)

    def lambda_C3D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_C3D6)
    Sleep(100)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)

    def lambda_C3F2():
        OP_95(0xFE, 30900, 0, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_C3F2)

    def lambda_C40C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_C40C)
    Sleep(100)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)

    def lambda_C428():
        OP_95(0xFE, 30900, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_C428)

    def lambda_C442():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_C442)
    Sleep(100)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)

    def lambda_C45E():
        OP_95(0xFE, 32200, 0, -650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_C45E)

    def lambda_C478():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C478)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0xB)
    SetChrSubChip(0x26, 0x0)
    WaitChrThread(0x27, 1)
    SetChrChipByIndex(0x27, 0xB)
    SetChrSubChip(0x27, 0x0)
    WaitChrThread(0x28, 1)
    SetChrChipByIndex(0x28, 0xB)
    SetChrSubChip(0x28, 0x0)
    WaitChrThread(0x29, 1)
    SetChrChipByIndex(0x29, 0xB)
    SetChrSubChip(0x29, 0x0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0307
    ChrTalk(
        0x26,
        "#11P#4S今だ……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0308
    ChrTalk(
        0x27,
        "#11P#4S宰相の首を狙え！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x26, 3, 0, 105)
    BeginChrThread(0x17, 3, 0, 81)
    Sleep(150)
    BeginChrThread(0x27, 3, 0, 106)
    Sleep(150)
    BeginChrThread(0x28, 3, 0, 107)
    Sleep(150)
    BeginChrThread(0x29, 3, 0, 108)
    Fade(250)
    OP_68(24000, 700, 0, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(43, 25, -10, 1000)
    SetCameraDistance(16500, 1000)
    OP_0D()
    WaitChrThread(0x17, 3)

    #C0309
    ChrTalk(
        0x17,
        "#01401F#5P──ここは通さん。\x02",
    )

    CloseMessageWindow()

    def lambda_C5A9():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_C5A9)
    Sleep(500)

    def lambda_C5C5():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_C5C5)
    Sleep(300)
    SetChrSubChip(0x26, 0x1)
    Sleep(90)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 30, 0)
    SetChrChipByIndex(0x26, 0xB)
    SetChrSubChip(0x26, 0x0)
    Sleep(300)
    SetChrSubChip(0x29, 0x2)
    Sleep(90)
    SetChrSubChip(0x29, 0x1)
    Sleep(90)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 30, 0)
    SetChrChipByIndex(0x29, 0xB)
    SetChrSubChip(0x29, 0x0)

    #C0310
    ChrTalk(
        0x26,
        "#11Pぐっ、《風の剣聖》か！\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x31,
        (
            "#11Pひるむな！\x01",
            "波状攻撃を仕掛けるぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(23500, 900, 0, 2000)
    MoveCamera(50, 21, 0, 2000)
    SetCameraDistance(17000, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 11700, 0, 2100, 90)
    SetChrPos(0x9, 11100, 0, 700, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)

    def lambda_C6C5():
        OP_95(0xFE, 19400, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_C6C5)
    Sleep(200)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)

    def lambda_C6EA():
        OP_95(0xFE, 18900, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C6EA)
    WaitChrThread(0xA, 1)
    Sound(318, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x9, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x9, 0x1D)
    SetChrSubChip(0x9, 0x0)

    #C0312
    ChrTalk(
        0xA,
        "#07107F#5P──助太刀します！\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        "#07307F#5Pそちらは下がられよ！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x25,
        "#00610F#6P#Nかたじけない！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x25, 3, 0, 62)
    Sleep(300)
    BeginChrThread(0x36, 3, 0, 60)

    #C0315
    ChrTalk(
        0x26,
        "#12Pミュラー・ヴァンダール！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x29,
        "#12Pアルノール家の守護者か！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x2E,
        "#11Pあれはリベールの親衛隊……！？\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x2F,
        "#11P構うものか、やってしまえ！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "event/ev12015.eff")
    LoadEffect(0x2, "event/ev12017.eff")
    LoadEffect(0x4, "event/ev12018.eff")
    LoadEffect(0x8, "event/ev12019.eff")
    LoadEffect(0x6, "battle/ms00001.eff")
    OP_68(29000, 700, 0, 5000)
    MoveCamera(45, 21, 0, 5000)
    SetCameraDistance(16500, 5000)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    BeginChrThread(0x4C, 2, 0, 123)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 28000, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x2E, 0x16)
    SetChrSubChip(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x2F, 0x16)
    SetChrSubChip(0x2F, 0x3)
    BeginChrThread(0x2F, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x32, 0x16)
    SetChrSubChip(0x32, 0x3)
    BeginChrThread(0x32, 3, 0, 101)
    Sleep(100)
    BeginChrThread(0x17, 0, 0, 74)
    Sleep(1500)
    BeginChrThread(0xA, 0, 0, 69)
    BeginChrThread(0x9, 0, 0, 63)
    Sleep(3300)
    EndChrThread(0x25, 0x3)
    BeginChrThread(0x25, 0, 0, 73)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    StopSound(860, 1000, 75)
    StopSound(861, 1000, 75)
    OP_0D()
    OP_49()
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x25, 0xFF)
    EndChrThread(0x36, 0xFF)
    EndChrThread(0x37, 0xFF)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    EndChrThread(0x26, 0xFF)
    EndChrThread(0x27, 0xFF)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x4C, 0x2)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x30, 0xFF)
    EndChrThread(0x31, 0xFF)
    EndChrThread(0x32, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x5)
    LoadChrToIndex("chr/ch00150.itc", 0x6)
    LoadChrToIndex("chr/ch00250.itc", 0x7)
    LoadChrToIndex("chr/ch00350.itc", 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x9)
    LoadChrToIndex("chr/ch03050.itc", 0xA)
    LoadChrToIndex("monster/ch84150.itc", 0xB)
    LoadChrToIndex("monster/ch84250.itc", 0xC)
    LoadChrToIndex("monster/ch84350.itc", 0xD)
    SoundLoad(943)
    SoundLoad(863)
    SetChrChipByIndex(0x49, 0xB)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, -17500, 0, 0, 90)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4A, 0xC)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -17500, 0, 0, 90)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4B, 0xD)
    SetChrSubChip(0x4B, 0x0)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, -17500, 0, 0, 90)
    OP_A7(0x4B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-6000, 1100, 0, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_68(7000, 1100, 0, 5000)
    SetCameraDistance(18000, 5000)
    FadeToBright(1000, 0)
    Sound(863, 2, 60, 0)
    BeginChrThread(0x4C, 1, 0, 124)
    BeginChrThread(0x101, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 91)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 92)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 93)
    BeginChrThread(0x105, 3, 0, 95)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 94)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    #C0319
    ChrTalk(
        0x101,
        "#00011F凄い……！\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        "#6P#00306Fとんでもねぇな……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        "#00102F#5Pでも、あれなら何とか……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 9500, 0, 5000, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    Sleep(150)
    OP_68(8500, 1300, 1500, 1200)

    def lambda_CC28():
        OP_96(0xFE, 0x251C, 0x0, 0xE10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CC28)

    def lambda_CC42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CC42)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xE1, 0x1F4)

    def lambda_CC5E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CC5E)
    Sleep(50)

    def lambda_CC6E():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC6E)
    Sleep(50)

    def lambda_CC7E():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CC7E)
    Sleep(50)

    def lambda_CC8E():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CC8E)
    Sleep(50)

    def lambda_CC9E():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CC9E)
    Sleep(50)

    def lambda_CCAE():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CCAE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    #C0322
    ChrTalk(
        0x8,
        "#5P#11505Fお、来たか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0323
    ChrTalk(
        0x101,
        "#12P#00001Fレクターさん……！\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#6P#00101F出席者の皆さんは\x01",
            "無事なんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        "#5P#11503Fあー、今のところはな。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 10500, 0, 5000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_CDA2():
        OP_96(0xFE, 0x2904, 0x0, 0xDAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CDA2)

    def lambda_CDBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CDBC)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)

    #C0326
    ChrTalk(
        0xB,
        (
            "#11P#12001F──話は後。\x01",
            "後ろからも来るわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        "#12P#00005Fえ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_CE57():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CE57)
    Sleep(50)
    OP_93(0x105, 0x10E, 0x1F4)

    #C0328
    ChrTalk(
        0x103,
        "#11P#00201F機械音確認……！\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x105,
        "#11P#10301F何か来たみたいだね。\x02",
    )

    CloseMessageWindow()

    def lambda_CEB4():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CEB4)
    Sleep(50)

    def lambda_CEC4():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CEC4)
    Sleep(50)

    def lambda_CED4():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CED4)
    Sleep(50)

    def lambda_CEE4():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CEE4)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_CF04():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CF04)

    def lambda_CF11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CF11)
    Fade(500)
    OP_68(-13900, 900, 0, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(2100, 900, 0, 4500)
    MoveCamera(30, 23, 0, 4500)
    SetCameraDistance(18000, 4500)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    Sound(943, 2, 70, 0)
    BeginChrThread(0x49, 3, 0, 96)
    Sleep(600)
    BeginChrThread(0x4A, 3, 0, 97)
    Sleep(600)
    BeginChrThread(0x4B, 3, 0, 98)
    OP_6F(0x79)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x5)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x6)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x8)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x9)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xA)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    #C0330
    ChrTalk(
        0x109,
        "#12P#10111Fこ、これは……！？\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x104,
        (
            "#11P#00307Fマフィアのアジトにいたのと\x01",
            "似たようなタイプみてぇだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        "#00007Fとにかく撃退するぞ！\x02",
    )

    CloseMessageWindow()
    StopSound(863, 500, 60)
    EndChrThread(0x4C, 0x1)
    Sound(943, 2, 70, 0)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)

    def lambda_D08F():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_D08F)

    def lambda_D0A9():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_D0A9)

    def lambda_D0C3():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_D0C3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(3100, 900, 0, 500)
    SetCameraDistance(16000, 500)
    Sleep(500)
    EndChrThread(0x49, 0xFF)
    EndChrThread(0x4A, 0xFF)
    EndChrThread(0x4B, 0xFF)
    OP_24(0x3AF)
    OP_24(0x35C)
    OP_24(0x35D)
    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    Call(0, 125)
    Return()

    # Function_59_B788 end

    def Function_60_D143(): pass

    label("Function_60_D143")


    def lambda_D148():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D148)
    Sleep(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)

    def lambda_D187():
        OP_96(0xFE, 0x4844, 0x0, 0xB54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D187)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_D1AF():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1AF)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_60_D143 end

    def Function_61_D1D4(): pass

    label("Function_61_D1D4")


    def lambda_D1D9():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D1D9)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_D212():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D212)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_61_D1D4 end

    def Function_62_D237(): pass

    label("Function_62_D237")


    def lambda_D23C():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D23C)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D268():
        OP_95(0xFE, 21300, 0, -2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D268)
    WaitChrThread(0xFE, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x37, 3, 0, 61)
    Sleep(1300)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_D2BE():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2BE)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_62_D237 end

    def Function_63_D2E7(): pass

    label("Function_63_D2E7")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D2F7():
        OP_95(0xFE, 22000, 0, -2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2F7)
    WaitChrThread(0xFE, 1)
    Sound(288, 0, 100, 0)

    def lambda_D31B():
        OP_95(0xFE, 24000, 0, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D31B)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)

    def lambda_D363():
        OP_9D(0xFE, 0x6E8C, 0x0, 0xFFFFF6A0, 0x514, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D363)
    Sleep(300)
    Sound(540, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    SetChrSubChip(0xFE, 0x6)
    BeginChrThread(0x27, 3, 0, 64)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x7)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(400)
    SetChrSubChip(0xFE, 0x8)

    def lambda_D3BA():
        OP_9D(0xFE, 0x66BC, 0x0, 0xFFFFF7CC, 0x1F4, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D3BA)
    WaitChrThread(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sound(257, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x5, 300, 900, 1200, -20, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFE, 0x5, 300, 900, 1200, 10, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 65)
    EndChrThread(0x32, 0x3)
    BeginChrThread(0x32, 3, 0, 67)
    Sleep(2000)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(30)
    SetChrSubChip(0xFE, 0xC)
    Sleep(30)
    SetChrSubChip(0xFE, 0xE)
    Sleep(30)
    Sound(538, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    BeginChrThread(0x31, 3, 0, 66)
    BeginChrThread(0x32, 3, 0, 68)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_63_D2E7 end

    def Function_64_D4E9(): pass

    label("Function_64_D4E9")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_D53D():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_D53D)

    def lambda_D54A():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D54A)

    def lambda_D563():
        OP_9D(0xFE, 0x7BD4, 0x0, 0xFFFFF3E4, 0x514, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D563)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_64_D4E9 end

    def Function_65_D589(): pass

    label("Function_65_D589")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D5A6():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D5A6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_D589 end

    def Function_66_D5C0(): pass

    label("Function_66_D5C0")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_D5FC():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D5FC)

    def lambda_D615():
        OP_9D(0xFE, 0x7C9C, 0x0, 0xFFFFF8F8, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D615)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_66_D5C0 end

    def Function_67_D63B(): pass

    label("Function_67_D63B")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D658():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF4AC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D658)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_D63B end

    def Function_68_D672(): pass

    label("Function_68_D672")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_D6AE():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D6AE)

    def lambda_D6C7():
        OP_9D(0xFE, 0x7DC8, 0x0, 0xFFFFF254, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6C7)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_68_D672 end

    def Function_69_D6ED(): pass

    label("Function_69_D6ED")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D6FA():
        OP_95(0xFE, 22000, 0, 2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6FA)
    WaitChrThread(0xFE, 1)

    def lambda_D718():
        OP_95(0xFE, 24000, 0, 2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D718)
    WaitChrThread(0xFE, 1)
    Sound(318, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    BeginChrThread(0x28, 3, 0, 70)
    Sleep(100)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D7A1():
        OP_95(0xFE, 28000, 0, 2400, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7A1)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    BeginChrThread(0x26, 3, 0, 71)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D7DF():
        OP_9D(0xFE, 0x67E8, 0x0, 0x3E8, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7DF)
    WaitChrThread(0xFE, 1)

    def lambda_D800():
        OP_9D(0xFE, 0x6400, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D800)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x0)
    Sleep(550)
    SetChrSubChip(0xFE, 0x6)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D881():
        OP_95(0xFE, 28600, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D881)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)

    def lambda_D8AE():
        OP_9D(0xFE, 0x6978, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8AE)
    WaitChrThread(0xFE, 1)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D90C():
        OP_95(0xFE, 30300, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D90C)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Return()

    # Function_69_D6ED end

    def Function_70_D931(): pass

    label("Function_70_D931")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D93E():
        OP_95(0xFE, 28200, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D93E)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D9A0():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_D9A0)

    def lambda_D9AD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D9AD)

    def lambda_D9C6():
        OP_9D(0xFE, 0x7A44, 0x0, 0xCE4, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9C6)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_70_D931 end

    def Function_71_D9EC(): pass

    label("Function_71_D9EC")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D9F9():
        OP_95(0xFE, 29000, 0, 1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9F9)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)

    def lambda_DA2E():
        OP_95(0xFE, 28000, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA2E)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)

    def lambda_DA86():
        OP_95(0xFE, 26700, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA86)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 26500, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_DADF():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DADF)

    def lambda_DAF8():
        OP_96(0xFE, 0x6F54, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DAF8)
    WaitChrThread(0xFE, 1)
    Sleep(450)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28300, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_DB58():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DB58)

    def lambda_DB71():
        OP_96(0xFE, 0x79E0, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DB71)
    WaitChrThread(0xFE, 1)
    Sleep(600)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DBD1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DBD1)

    def lambda_DBEA():
        OP_9D(0xFE, 0x8084, 0x0, 0x7D0, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DBEA)
    Sleep(50)
    EndChrThread(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 72)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_71_D9EC end

    def Function_72_DC18(): pass

    label("Function_72_DC18")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DC25():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC25)

    def lambda_DC3E():
        OP_9D(0xFE, 0x86C4, 0x0, 0xBB8, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC3E)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_72_DC18 end

    def Function_73_DC5F(): pass

    label("Function_73_DC5F")

    SetChrPos(0x25, 17000, 0, 1800, 90)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DC7D():
        OP_96(0xFE, 0x6400, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC7D)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x25, 0, 0, 89)
    Return()

    # Function_73_DC5F end

    def Function_74_DCA8(): pass

    label("Function_74_DCA8")

    BeginChrThread(0x17, 3, 0, 75)
    BeginChrThread(0x17, 2, 0, 77)
    Sound(3987, 255, 100, 0)    #voice#Arios
    Sound(264, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(1300)
    BeginChrThread(0x17, 3, 0, 75)
    BeginChrThread(0x17, 2, 0, 77)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(1300)
    BeginChrThread(0x17, 3, 0, 76)
    Return()

    # Function_74_DCA8 end

    def Function_75_DCEB(): pass

    label("Function_75_DCEB")

    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x3)
    Sound(859, 0, 100, 0)
    Sound(534, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(60)
    Sound(569, 0, 100, 0)
    Sound(540, 0, 70, 0)
    SetChrSubChip(0x17, 0x1)
    Sleep(120)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(60)
    SetChrSubChip(0x17, 0x3)
    Sleep(180)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(60)
    SetChrSubChip(0x17, 0x1)
    Sleep(700)
    Return()

    # Function_75_DCEB end

    def Function_76_DD45(): pass

    label("Function_76_DD45")

    Sleep(500)
    BeginChrThread(0x29, 3, 0, 78)

    def lambda_DD53():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD53)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 93, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1200)

    def lambda_DDB8():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DDB8)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x3)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 500, 0, 85, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(90)
    SetChrSubChip(0x17, 0x1)
    Sleep(300)
    EndChrThread(0x2F, 0x3)
    BeginChrThread(0x2F, 3, 0, 79)
    Sleep(100)
    EndChrThread(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 80)
    StopEffect(0x1, 0x0)
    Sleep(1100)

    def lambda_DE45():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DE45)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 95, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1500)
    Return()

    # Function_76_DD45 end

    def Function_77_DEA6(): pass

    label("Function_77_DEA6")

    StopEffect(0x1, 0x0)
    PlayEffect(0x7, 0xFF, 0x17, 0x3, 0, 500, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1500, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1250, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 2000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 28000, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    Return()

    # Function_77_DEA6 end

    def Function_78_E158(): pass

    label("Function_78_E158")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E170():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E170)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E19B():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E19B)

    def lambda_E1B4():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1B4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E1FB():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1FB)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E226():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E226)

    def lambda_E23F():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E23F)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_78_E158 end

    def Function_79_E265(): pass

    label("Function_79_E265")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E272():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E272)

    def lambda_E28B():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E28B)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 3, 0, 101)
    Return()

    # Function_79_E265 end

    def Function_80_E2C4(): pass

    label("Function_80_E2C4")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E2D1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E2D1)

    def lambda_E2EA():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E2EA)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_E2C4 end

    def Function_81_E30B(): pass

    label("Function_81_E30B")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 13300, 0, 200, 90)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x17, 0x1E, 0xC8)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    PlayEffect(0x0, 0x0, 0x17, 0x3, 250, 1200, 500, 45, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_E378():
        OP_9D(0xFE, 0x571C, 0x0, 0x0, 0xDAC, 0x514)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E378)
    Sleep(500)
    Sound(844, 0, 70, 0)
    Sound(255, 0, 50, 0)
    Sound(3987, 255, 100, 0)    #voice#Arios
    WaitChrThread(0x17, 1)
    SetChrSubChip(0x17, 0x3)
    Sound(532, 0, 100, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    StopEffect(0x0, 0x0)
    PlayEffect(0x4, 0xFF, 0x17, 0x3, 0, 0, 2000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)
    Sound(289, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x26, 3, 0, 109)
    Sleep(50)
    BeginChrThread(0x27, 3, 0, 111)
    BeginChrThread(0x28, 3, 0, 113)
    Sleep(50)
    BeginChrThread(0x29, 3, 0, 115)
    Sleep(700)
    OP_68(27000, 700, 0, 500)
    MoveCamera(55, 17, 0, 500)
    SetCameraDistance(16000, 500)
    Sound(534, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sound(3992, 255, 100, 0)    #voice#Arios
    SetChrFlags(0x17, 0x20)

    def lambda_E472():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_E472)
    WaitChrThread(0x17, 1)
    ClearChrFlags(0x17, 0x20)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    PlayEffect(0x6, 0xFF, 0x17, 0x3, 0, 500, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x26, 3, 0, 110)
    BeginChrThread(0x27, 3, 0, 112)
    BeginChrThread(0x28, 3, 0, 114)
    BeginChrThread(0x29, 3, 0, 116)
    Sleep(60)
    SetChrSubChip(0x17, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    SetChrChip(0x1, 0x17, 0x0, 0x0)
    CancelBlur(0)
    SetChrSubChip(0x17, 0x2)
    Sleep(90)
    SetChrChipByIndex(0x17, 0x5)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_81_E30B end

    def Function_82_E539(): pass

    label("Function_82_E539")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E608")
    OP_82(0x32, 0x32, 0xBB8, 0x4B0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31500, 0, -1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 30500, 0, -1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31000, 0, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Jump("Function_82_E539")

    label("loc_E608")

    Return()

    # Function_82_E539 end

    def Function_83_E609(): pass

    label("Function_83_E609")


    def lambda_E60E():
        OP_95(0xFE, 81000, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E60E)

    def lambda_E628():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E628)
    WaitChrThread(0xFE, 1)

    def lambda_E63D():
        OP_95(0xFE, 75000, 0, 0, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E63D)
    WaitChrThread(0xFE, 1)

    def lambda_E65B():
        OP_95(0xFE, 65000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E65B)
    Sleep(1100)

    def lambda_E678():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E678)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_83_E609 end

    def Function_84_E689(): pass

    label("Function_84_E689")


    def lambda_E68E():
        OP_95(0xFE, 80500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E68E)

    def lambda_E6A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E6A8)
    WaitChrThread(0xFE, 1)

    def lambda_E6BD():
        OP_95(0xFE, 75000, 0, -300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6BD)
    WaitChrThread(0xFE, 1)

    def lambda_E6DB():
        OP_95(0xFE, 65000, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E6DB)
    Sleep(1100)

    def lambda_E6F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E6F8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_E689 end

    def Function_85_E709(): pass

    label("Function_85_E709")


    def lambda_E70E():
        OP_95(0xFE, 81500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E70E)

    def lambda_E728():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E728)
    WaitChrThread(0xFE, 1)

    def lambda_E73D():
        OP_95(0xFE, 75000, 0, 300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E73D)
    WaitChrThread(0xFE, 1)

    def lambda_E75B():
        OP_95(0xFE, 65000, 0, 300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E75B)
    Sleep(1100)

    def lambda_E778():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E778)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_E709 end

    def Function_86_E789(): pass

    label("Function_86_E789")

    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)

    def lambda_E796():
        OP_96(0xFE, 0x88B8, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E796)

    def lambda_E7B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E7B0)
    WaitChrThread(0xFE, 1)

    def lambda_E7C5():
        OP_96(0xFE, 0x8598, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7C5)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    Return()

    # Function_86_E789 end

    def Function_87_E7ED(): pass

    label("Function_87_E7ED")

    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)

    def lambda_E7FA():
        OP_96(0xFE, 0x88B8, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E7FA)

    def lambda_E814():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E814)
    WaitChrThread(0xFE, 1)

    def lambda_E829():
        OP_96(0xFE, 0x8278, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E829)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Return()

    # Function_87_E7ED end

    def Function_88_E851(): pass

    label("Function_88_E851")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E8A6")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_88_E851")

    label("loc_E8A6")

    Return()

    # Function_88_E851 end

    def Function_89_E8A7(): pass

    label("Function_89_E8A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E917")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_89_E8A7")

    label("loc_E917")

    Return()

    # Function_89_E8A7 end

    def Function_90_E918(): pass

    label("Function_90_E918")


    def lambda_E91D():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFFF38, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E91D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_90_E918 end

    def Function_91_E937(): pass

    label("Function_91_E937")


    def lambda_E93C():
        OP_96(0xFE, 0x1964, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E93C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_91_E937 end

    def Function_92_E956(): pass

    label("Function_92_E956")


    def lambda_E95B():
        OP_96(0xFE, 0x1450, 0x0, 0x64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E95B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_92_E956 end

    def Function_93_E975(): pass

    label("Function_93_E975")


    def lambda_E97A():
        OP_96(0xFE, 0x125C, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E97A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_93_E975 end

    def Function_94_E994(): pass

    label("Function_94_E994")


    def lambda_E999():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E999)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_E994 end

    def Function_95_E9B3(): pass

    label("Function_95_E9B3")


    def lambda_E9B8():
        OP_96(0xFE, 0x16A8, 0x0, 0xFFFFF8F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E9B8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_95_E9B3 end

    def Function_96_E9D2(): pass

    label("Function_96_E9D2")


    def lambda_E9D7():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E9D7)

    def lambda_E9F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E9F1)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_96_E9D2 end

    def Function_97_EA08(): pass

    label("Function_97_EA08")


    def lambda_EA0D():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA0D)

    def lambda_EA27():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA27)
    WaitChrThread(0xFE, 1)

    def lambda_EA3C():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA3C)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_97_EA08 end

    def Function_98_EA5C(): pass

    label("Function_98_EA5C")


    def lambda_EA61():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA61)

    def lambda_EA7B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EA7B)
    WaitChrThread(0xFE, 1)

    def lambda_EA90():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EA90)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_98_EA5C end

    def Function_99_EAB0(): pass

    label("Function_99_EAB0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EACB")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_99_EAB0")

    label("loc_EACB")

    Return()

    # Function_99_EAB0 end

    def Function_100_EACC(): pass

    label("Function_100_EACC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EC62")
    ClearScenarioFlags(0x0, 1)
    SetChrSubChip(0xFE, 0x4)

    def lambda_EAE3():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EAE3)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    SetScenarioFlags(0x0, 1)
    Sleep(500)
    Jump("Function_100_EACC")

    label("loc_EC62")

    Return()

    # Function_100_EACC end

    def Function_101_EC63(): pass

    label("Function_101_EC63")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDF3")
    SetChrSubChip(0xFE, 0x4)

    def lambda_EC77():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EC77)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("Function_101_EC63")

    label("loc_EDF3")

    Return()

    # Function_101_EC63 end

    def Function_102_EDF4(): pass

    label("Function_102_EDF4")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_EE12():
        OP_9D(0xFE, 0x5654, 0x0, 0x76C, 0x3E8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE12)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x0)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_102_EDF4 end

    def Function_103_EE44(): pass

    label("Function_103_EE44")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EE5C():
        OP_9D(0xFE, 0x5654, 0x0, 0xFFFFF31C, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EE5C)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_103_EE44 end

    def Function_104_EE87(): pass

    label("Function_104_EE87")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 100, 0)

    def lambda_EEA5():
        OP_9D(0xFE, 0x53FC, 0x0, 0xFFFFFCE0, 0x190, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EEA5)
    WaitChrThread(0xFE, 1)

    def lambda_EEC6():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EEC6)
    SetChrSubChip(0xFE, 0x2)
    WaitChrThread(0x25, 2)
    Return()

    # Function_104_EE87 end

    def Function_105_EEE3(): pass

    label("Function_105_EEE3")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EEF0():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EEF0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_105_EEE3 end

    def Function_106_EF0A(): pass

    label("Function_106_EF0A")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF17():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFF38, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF17)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_106_EF0A end

    def Function_107_EF31(): pass

    label("Function_107_EF31")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF3E():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xC8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF3E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_107_EF31 end

    def Function_108_EF58(): pass

    label("Function_108_EF58")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_EF65():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF65)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_108_EF58 end

    def Function_109_EF7F(): pass

    label("Function_109_EF7F")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_EF9D():
        OP_9D(0xFE, 0x6978, 0x0, 0x12C, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EF9D)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 100, 0)

    def lambda_EFC4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EFC4)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_109_EF7F end

    def Function_110_EFDD(): pass

    label("Function_110_EFDD")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_EFF0():
        OP_9D(0xFE, 0x7530, 0x0, 0x320, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EFF0)
    WaitChrThread(0xFE, 1)
    Sound(811, 0, 100, 0)

    def lambda_F017():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F017)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_110_EFDD end

    def Function_111_F030(): pass

    label("Function_111_F030")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F048():
        OP_9D(0xFE, 0x6720, 0x0, 0xFFFFF768, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F048)
    WaitChrThread(0xFE, 1)

    def lambda_F069():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F069)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_111_F030 end

    def Function_112_F097(): pass

    label("Function_112_F097")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_F0A9():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_F0A9)

    def lambda_F0B6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F0B6)

    def lambda_F0CF():
        OP_96(0xFE, 0x72D8, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F0CF)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_112_F097 end

    def Function_113_F0EE(): pass

    label("Function_113_F0EE")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F106():
        OP_9D(0xFE, 0x6720, 0x0, 0x5DC, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F106)
    WaitChrThread(0xFE, 1)

    def lambda_F127():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F127)
    SetChrSubChip(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_113_F0EE end

    def Function_114_F159(): pass

    label("Function_114_F159")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_F16B():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_F16B)

    def lambda_F178():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F178)

    def lambda_F191():
        OP_96(0xFE, 0x72D8, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F191)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_114_F159 end

    def Function_115_F1B0(): pass

    label("Function_115_F1B0")


    def lambda_F1B5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F1B5)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_115_F1B0 end

    def Function_116_F1D2(): pass

    label("Function_116_F1D2")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_F1DF():
        OP_9D(0xFE, 0x7A44, 0x0, 0xFFFFFB50, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F1DF)
    WaitChrThread(0xFE, 1)

    def lambda_F200():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F200)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_116_F1D2 end

    def Function_117_F219(): pass

    label("Function_117_F219")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_F231():
        OP_9C(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F231)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_117_F219 end

    def Function_118_F256(): pass

    label("Function_118_F256")


    def lambda_F25B():
        OP_96(0xFE, 0x7C9C, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F25B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_118_F256 end

    def Function_119_F27D(): pass

    label("Function_119_F27D")


    def lambda_F282():
        OP_96(0xFE, 0x76C0, 0x0, 0x76C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F282)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x12)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_119_F27D end

    def Function_120_F2A4(): pass

    label("Function_120_F2A4")


    def lambda_F2A9():
        OP_96(0xFE, 0x76C0, 0x0, 0xFFFFF894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2A9)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_120_F2A4 end

    def Function_121_F2CB(): pass

    label("Function_121_F2CB")


    def lambda_F2D0():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F2D0)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_121_F2CB end

    def Function_122_F2F2(): pass

    label("Function_122_F2F2")

    Sleep(1200)

    label("loc_F2F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F30E")
    Sound(530, 0, 80, 0)
    Sleep(1200)
    Jump("loc_F2F5")

    label("loc_F30E")

    Return()

    # Function_122_F2F2 end

    def Function_123_F30F(): pass

    label("Function_123_F30F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F328")
    Sound(356, 0, 50, 0)
    Sleep(1100)
    Jump("Function_123_F30F")

    label("loc_F328")

    Return()

    # Function_123_F30F end

    def Function_124_F329(): pass

    label("Function_124_F329")

    Sleep(1000)

    label("loc_F32C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F35A")
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(1600)
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(3000)
    Jump("loc_F32C")

    label("loc_F35A")

    Return()

    # Function_124_F329 end

    def Function_125_F35B(): pass

    label("Function_125_F35B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x5)
    LoadChrToIndex("chr/ch00150.itc", 0x6)
    LoadChrToIndex("chr/ch00250.itc", 0x7)
    LoadChrToIndex("chr/ch00350.itc", 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x9)
    LoadChrToIndex("chr/ch03050.itc", 0xA)
    LoadChrToIndex("chr/ch02450.itc", 0xB)
    LoadChrToIndex("chr/ch02451.itc", 0xC)
    LoadChrToIndex("chr/ch00950.itc", 0xD)
    LoadChrToIndex("chr/ch00951.itc", 0xE)
    LoadChrToIndex("chr/ch00952.itc", 0xF)
    LoadChrToIndex("apl/ch51237.itc", 0x10)
    LoadChrToIndex("apl/ch51265.itc", 0x11)
    LoadChrToIndex("apl/ch51238.itc", 0x12)
    LoadChrToIndex("apl/ch51267.itc", 0x13)
    LoadChrToIndex("chr/ch42250.itc", 0x14)
    LoadChrToIndex("chr/ch42251.itc", 0x15)
    LoadChrToIndex("chr/ch02452.itc", 0x16)
    LoadChrToIndex("chr/ch42253.itc", 0x17)
    LoadChrToIndex("chr/ch42254.itc", 0x18)
    LoadChrToIndex("chr/ch42550.itc", 0x19)
    LoadChrToIndex("chr/ch42551.itc", 0x1A)
    LoadChrToIndex("chr/ch00952.itc", 0x1B)
    LoadChrToIndex("chr/ch42553.itc", 0x1C)
    LoadChrToIndex("chr/ch42554.itc", 0x1D)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    LoadChrToIndex("apl/ch51235.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("chr/ch00900.itc", 0x21)
    LoadChrToIndex("apl/ch51021.itc", 0x22)
    LoadEffect(0x1, "event/ev12010.eff")
    LoadEffect(0x2, "event/ev12011.eff")
    SoundLoad(938)
    SoundLoad(145)
    SoundLoad(803)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x101, 0x5)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x6)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x8)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x9)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xA)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 7000, 0, -200, 270)
    SetChrPos(0x102, 6500, 0, 700, 270)
    SetChrPos(0x103, 5200, 0, 100, 270)
    SetChrPos(0x104, 4700, 0, 1000, 270)
    SetChrPos(0x109, 4900, 0, -1300, 270)
    SetChrPos(0x105, 5800, 0, -1800, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x16)
    SetChrSubChip(0x17, 0x1)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 26900, 0, 300, 90)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x12)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x20)
    SetChrPos(0xA, 25400, 0, 1900, 90)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x9, 25400, 0, -1900, 90)
    SetChrChipByIndex(0x25, 0x1B)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 24500, 0, -300, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9500, 0, 3600, 270)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 10500, 0, 3500, 270)
    SetChrChipByIndex(0x26, 0x18)
    SetChrSubChip(0x26, 0x3)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 33500, 0, 0, 270)
    SetChrChipByIndex(0x27, 0x18)
    SetChrSubChip(0x27, 0x3)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 33200, 0, 1700, 270)
    SetChrChipByIndex(0x28, 0x17)
    SetChrSubChip(0x28, 0x3)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 34700, 0, 1300, 270)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x3)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 33700, 0, 3100, 270)
    SetChrChipByIndex(0x2A, 0x17)
    SetChrSubChip(0x2A, 0x2)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2E, 0x1D)
    SetChrSubChip(0x2E, 0x2)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 34000, 0, -1900, 270)
    SetChrChipByIndex(0x2F, 0x1C)
    SetChrSubChip(0x2F, 0x2)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 34900, 0, -200, 270)
    SetChrChipByIndex(0x30, 0x1C)
    SetChrSubChip(0x30, 0x3)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 35900, 0, -900, 270)
    SetChrChipByIndex(0x31, 0x1C)
    SetChrSubChip(0x31, 0x2)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 34000, 0, -3100, 270)
    SetChrChipByIndex(0x32, 0x1D)
    SetChrSubChip(0x32, 0x2)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrChipByIndex(0x33, 0x1D)
    SetChrSubChip(0x33, 0x2)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x8000)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0xA)
    ClearChrFlags(0x48, 0x80)
    OP_78(0x17, 0x48)
    OP_49()
    SetChrPos(0x48, 34300, 100, -1600, 0)
    OP_D5(0x48, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFlags(0x17, 0x4)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    OP_68(4600, 900, 930, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0333
    ChrTalk(
        0x101,
        "#00010F#11Pくっ、こんなものまで……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x103,
        (
            "#00206F#12P多分、屋上からタワー内に\x01",
            "放ったのだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        (
            "#11P#00301Fしかし今のは《結社》ってのが\x01",
            "作ったモンじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x105,
        (
            "#12P#10308F闇に流れたのを手に入れたか\x01",
            "それとも……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(100)

    #C0337
    ChrTalk(
        0x8,
        (
            "#6P#11508F……どうでもいいが、\x01",
            "あっちもケリが付きそうだぜ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(29500, 700, 0, 3000)
    MoveCamera(43, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_FA1A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FA1A)

    def lambda_FA27():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FA27)
    Sleep(50)

    def lambda_FA37():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA37)
    Sleep(50)

    def lambda_FA47():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FA47)
    Sleep(50)

    def lambda_FA57():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FA57)
    Sleep(50)

    def lambda_FA67():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FA67)
    Sleep(50)

    def lambda_FA77():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FA77)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0338
    ChrTalk(
        0x26,
        "#12Pくっ……化物どもが！\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x2E,
        (
            "仕方ない！\x01",
            "最終プランに切り替えるぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2E, 0x3)
    Sound(809, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0x2E, 0x4)
    PlayEffect(0x1, 0x0, 0x2E, 0x5, 0, 0, 0, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x4C, 1, 0, 127)

    #C0340
    ChrTalk(
        0x17,
        "#01401F#7A#5Pむ……\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xA,
        "#07105F#10A#5Pスタングレネード……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x9,
        "#07307F#5A#5P下がれ！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x13)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 117)
    Sound(250, 0, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x9, 0x11)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 117)
    Sound(844, 0, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x17, 0xC)
    SetChrSubChip(0x17, 0x2)
    BeginChrThread(0x17, 3, 0, 117)
    Sleep(50)
    SetChrChipByIndex(0x25, 0x22)
    SetChrSubChip(0x25, 0x0)
    BeginChrThread(0x25, 3, 0, 117)
    Sleep(200)
    StopEffect(0x0, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 29000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sleep(100)
    Sound(174, 0, 100, 0)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    Sleep(2000)
    OP_68(29500, 900, 0, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x25, 0xFF)
    SetChrPos(0x17, 20900, 0, 300, 90)
    SetChrPos(0xA, 19400, 0, 1900, 90)
    SetChrPos(0x9, 19400, 0, -1900, 90)
    SetChrChipByIndex(0x25, 0xE)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, 18500, 0, -300, 90)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x10)
    ClearMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x1E)
    OP_74(0x11, 0x3C)
    FadeToBright(2000, 16777215)
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x3C, 0x0, 0x0, 0x0)
    OP_79(0x11)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_0D()
    OP_68(33500, 1000, 0, 2500)
    MoveCamera(43, 19, 0, 2500)
    SetCameraDistance(17500, 2500)
    BeginChrThread(0x17, 3, 0, 118)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 119)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 120)
    Sleep(50)
    BeginChrThread(0x25, 3, 0, 121)
    WaitChrThread(0x25, 3)
    OP_6F(0x79)

    #C0343
    ChrTalk(
        0x9,
        "#6P#07301Fチッ……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xA,
        "#07101F#5Pこのシャッターは……\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x17,
        (
            "#01403F#5P……どうやら簡単には\x01",
            "突破できなさそうですな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0346
    ChrTalk(
        0x101,
        "#00007F#6P#N皆さん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(28000, 1000, 0, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_68(31000, 1000, 0, 3000)
    SetCameraDistance(16500, 3000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 19500, 0, -300, 90)
    SetChrPos(0x102, 19500, 0, 1000, 90)
    SetChrPos(0x103, 18300, 0, -1700, 90)
    SetChrPos(0x104, 18300, 0, -400, 90)
    SetChrPos(0x109, 17100, 0, -1700, 90)
    SetChrPos(0x105, 17100, 0, -400, 90)
    SetChrPos(0x8, 17300, 0, 2100, 90)
    SetChrPos(0xB, 18400, 0, 2100, 90)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x17, 33500, 0, 300, 270)
    SetChrPos(0x25, 31500, 0, 0, 270)
    SetChrPos(0xA, 32400, 0, 1700, 270)
    SetChrPos(0x9, 32600, 0, -1300, 270)

    def lambda_FFED():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FFED)
    Sleep(100)

    def lambda_1000A():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1000A)
    Sleep(100)

    def lambda_10027():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10027)
    Sleep(100)

    def lambda_10044():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10044)
    Sleep(100)

    def lambda_10061():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10061)
    Sleep(100)

    def lambda_1007E():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1007E)
    Sleep(100)

    def lambda_1009B():
        OP_97(0xB, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_1009B)
    Sleep(100)

    def lambda_100B8():
        OP_97(0x8, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_100B8)
    WaitChrThread(0xB, 0)

    def lambda_100D6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_100D6)
    WaitChrThread(0x8, 0)

    def lambda_100E7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_100E7)

    #C0347
    ChrTalk(
        0x25,
        "#11P#00600Fお前たちか……\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#00300F#6Pどうやら無事、\x01",
            "撃退できたみてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x17,
        (
            "#11P#01403Fああ、しかしこのままでは\x01",
            "逃げられてしまうだろう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0350
    ChrTalk(
        0x101,
        "#11P#00001F#5Pティオ、やれるか？\x02",
    )

    CloseMessageWindow()

    def lambda_101B7():

        label("loc_101B7")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101B7")

    QueueWorkItem2(0x101, 2, lambda_101B7)

    def lambda_101C9():

        label("loc_101C9")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101C9")

    QueueWorkItem2(0x102, 2, lambda_101C9)

    def lambda_101DB():

        label("loc_101DB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101DB")

    QueueWorkItem2(0x109, 2, lambda_101DB)

    def lambda_101ED():

        label("loc_101ED")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101ED")

    QueueWorkItem2(0x105, 2, lambda_101ED)

    def lambda_101FF():

        label("loc_101FF")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_101FF")

    QueueWorkItem2(0x104, 2, lambda_101FF)
    TurnDirection(0x103, 0x101, 500)

    #C0351
    ChrTalk(
        0x103,
        (
            "#6P#00201F自信はありませんが\x01",
            "やるだけやってみます。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10251():
        OP_95(0xFE, 32800, 0, -2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_10251)
    Sleep(300)

    def lambda_1026E():

        label("loc_1026E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_1026E")

    QueueWorkItem2(0x25, 2, lambda_1026E)
    Sleep(50)

    def lambda_10283():

        label("loc_10283")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10283")

    QueueWorkItem2(0x17, 2, lambda_10283)
    Sleep(50)

    def lambda_10298():

        label("loc_10298")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_10298")

    QueueWorkItem2(0x9, 2, lambda_10298)
    Sleep(50)

    def lambda_102AD():

        label("loc_102AD")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_102AD")

    QueueWorkItem2(0xA, 2, lambda_102AD)
    WaitChrThread(0x103, 1)

    def lambda_102C3():
        OP_95(0xFE, 34200, 0, -2100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_102C3)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    OP_93(0x103, 0x0, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(71, 0, 70, 0)
    ClearMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 126)
    Sound(938, 2, 100, 0)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x103, 0x3)
    StopSound(938, 500, 100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x103,
        (
            "#11P#00206Fやはりセキュリティレベルが\x01",
            "最大まで上げられています。\x02\x03",

            "#00208F《エイオン》を使っても\x01",
            "このノート型の端末では……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#5P#00008Fそうか……\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_10415():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10415)

    def lambda_10422():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10422)

    def lambda_1042F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1042F)
    Sleep(50)

    def lambda_1043F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1043F)

    def lambda_1044C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1044C)
    Sleep(50)

    def lambda_1045C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1045C)

    def lambda_10469():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10469)

    def lambda_10476():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10476)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(800)
    OP_93(0x25, 0xB4, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x25, 0x2)
    SetChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x6)
    Sleep(500)
    SetChrSubChip(0x25, 0x7)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)

    #C0354
    ChrTalk(
        0x25,
        (
            "#5P#00600F──私だ。\x02\x03",

            "#00603Fああ、何とかこちらは\x01",
            "凌#2Rしの#いだばかりだが……\x02\x03",

            "………………………………\x02\x03",

            "#00601F……なに？\x02\x03",

            "連中がエレベーターで\x01",
            "地下へ降下しているだと……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0355
    ChrTalk(
        0x109,
        "#6P#N#10113Fど、どうして……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0356
    ChrTalk(
        0x102,
        (
            "#00105F#5P屋上にある飛行艇で\x01",
            "逃げるつもりじゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#11503F#5Pんー、考えられるとしたら。\x02\x03",

            "#11501F飛行艇に搭載した導力爆弾を\x01",
            "自爆させるってところか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10752():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10752)

    def lambda_1075F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1075F)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1079F():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1079F)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_107F7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_107F7)

    def lambda_10804():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10804)

    def lambda_10811():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10811)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10839():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10839)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1085E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1085E)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    ClearChrFlags(0x25, 0x10)
    ClearChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    Sound(802, 0, 100, 0)

    def lambda_108A0():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_108A0)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x101,
        "#11P#00007Fな……！？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x17,
        "#11P#01401Fそうか、確かにそれならば……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        (
            "#12P#07307Fこのビルごと宰相たちを\x01",
            "葬り去れるというわけか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xB,
        (
            "#12003F#5P確かに、テロリストたちなら\x01",
            "そこまでやりかねないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xA,
        "#11P#07101Fくっ、愚かな……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        "#12P#10306Fさすがにピンチだね……\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0x5A, 0x1F4)

    #C0364
    ChrTalk(
        0x25,
        (
            "#5P#00610Fクッ、こうなったら\x01",
            "力ずくでもこのシャッターを！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)

    #C0365
    ChrTalk(
        0x103,
        (
            "#11P#00204F#30W…………いえ………………\x02\x03",

            "#00202F#20Wどうやら何とか\x01",
            "なるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A7C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10A7C)

    def lambda_10A89():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10A89)

    def lambda_10A96():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_10A96)
    Sleep(50)

    def lambda_10AA6():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10AA6)

    def lambda_10AB3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10AB3)

    def lambda_10AC0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10AC0)
    Sleep(50)

    def lambda_10AD0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10AD0)

    def lambda_10ADD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10ADD)

    def lambda_10AEA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10AEA)
    WaitChrThread(0x25, 2)

    #C0366
    ChrTalk(
        0x25,
        "#5P#00605Fなに……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x91)
    OP_24(0x323)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 0)
    NewScene("e4820", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_125_F35B end

    def Function_126_10B44(): pass

    label("Function_126_10B44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10B5E")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_126_10B44")

    label("loc_10B5E")

    Return()

    # Function_126_10B44 end

    def Function_127_10B5F(): pass

    label("Function_127_10B5F")

    Sleep(200)
    Sound(555, 0, 80, 0)
    Sleep(500)
    Sound(555, 0, 60, 0)
    Sleep(200)
    Sound(555, 0, 30, 0)
    Return()

    # Function_127_10B5F end

    def Function_128_10B7B(): pass

    label("Function_128_10B7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x6)
    LoadChrToIndex("apl/ch51235.itc", 0x7)
    SoundLoad(938)
    SoundLoad(145)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 29500, 0, -300, 90)
    SetChrPos(0x102, 29500, 0, 1000, 90)
    SetChrPos(0x103, 34200, 0, -2100, 0)
    SetChrPos(0x104, 28300, 0, -400, 90)
    SetChrPos(0x109, 27100, 0, -1700, 90)
    SetChrPos(0x105, 27100, 0, -400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 33500, 0, 300, 270)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 32400, 0, 1700, 270)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32600, 0, -1300, 270)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 31500, 0, 0, 270)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 27300, 0, 2100, 135)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, 2100, 135)
    OP_4B(0xB, 0xFF)

    def lambda_10D03():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10D03)

    def lambda_10D10():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10D10)

    def lambda_10D1D():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10D1D)

    def lambda_10D2A():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_10D2A)

    def lambda_10D37():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10D37)

    def lambda_10D44():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_10D44)

    def lambda_10D51():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_10D51)

    def lambda_10D5E():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10D5E)

    def lambda_10D6B():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10D6B)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x10)
    ClearMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x0)
    ClearChrFlags(0x48, 0x80)
    OP_78(0x17, 0x48)
    OP_49()
    SetChrPos(0x48, 34300, 100, -1600, 0)
    OP_D5(0x48, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x1000)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    ClearMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 126)
    Sound(938, 2, 100, 0)
    OP_68(31000, 1000, 0, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0367
    ChrTalk(
        0x101,
        (
            "#5P#00002Fヨナ……\x01",
            "戻ってきてくれたのか！\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x103,
        (
            "#12P#00202F#11Pええ、どうやら今日の便で\x01",
            "帰ってきたみたいですね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)
    Sound(839, 0, 100, 0)
    EndChrThread(0x103, 0x3)
    StopSound(938, 500, 100)
    Sleep(500)

    #C0369
    ChrTalk(
        0x103,
        (
            "#12P#00204F#11P──やりました。\x01",
            "タワーの制御を解放します。\x02",
        )
    )

    CloseMessageWindow()
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10F72():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10F72)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10F97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10F97)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10FBF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10FBF)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_10FE4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10FE4)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1100C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1100C)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11031():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_11031)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11059():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11059)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_1107E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1107E)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_110A3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_110A3)
    Sleep(1000)
    OP_79(0x11)
    OP_24(0x91)
    Sound(143, 0, 100, 0)

    #C0370
    ChrTalk(
        0xA,
        "#5P#07102Fやった……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x103, 500)

    #C0371
    ChrTalk(
        0x25,
        "#5P#00602Fエレベーターは使えるか！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0x103, 0x25, 500)

    #C0372
    ChrTalk(
        0x103,
        (
            "#12P#00202F#11Pええ、ロックは解除しました。\x02\x03",

            "#00206Fテロリストたちが使用中の\x01",
            "１基は使えませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "#12004F#5Pならば私は屋上に。\x02\x03",

            "#12000F飛行船に搭載された\x01",
            "導力爆弾を解除するわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    #C0374
    ChrTalk(
        0x101,
        "#12P#00005Fキリカさん、出来るんですか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0375
    ChrTalk(
        0xB,
        (
            "#12004F#5Pええ、防諜関係者には\x01",
            "最低限のスキルだから。\x02\x03",

            "#12000Fレクター書記官。\x01",
            "手分けするとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        "#11504Fま、しゃーねえか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 500)

    #C0377
    ChrTalk(
        0x9,
        (
            "#11P#07303Fならば我々も付き合おう。\x02\x03",

            "#07300F連中が人形兵器の守りを\x01",
            "残している可能性はありそうだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x25, 500)

    def lambda_11327():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11327)

    #C0378
    ChrTalk(
        0xA,
        (
            "#5P#07101F──そちらはどうか、\x01",
            "テロリストたちの追撃を！\x02\x03",

            "今なら何とか\x01",
            "捕まえられるかもしれません！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    #C0379
    ChrTalk(
        0x17,
        "#11P#01400F承知した……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x101, 500)

    #C0380
    ChrTalk(
        0x25,
        (
            "#11P#00601Fバニングス！\x01",
            "我々も追撃に出るぞ！\x02\x03",

            "敵は２組……\x01",
            "手分けする必要がある！\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#6P#00007F了解しました！\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#00307F#6Pアイアイ・サー！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("c1520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_128_10B7B end

    def Function_129_1147C(): pass

    label("Function_129_1147C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("chr/ch47900.itc", 0x27)
    LoadChrToIndex("chr/ch28100.itc", 0x28)
    LoadChrToIndex("apl/ch51259.itc", 0x29)
    LoadChrToIndex("apl/ch50123.itc", 0x2A)
    SetChrPos(0x0, 0, 0, 5500, 0)
    SetChrPos(0x1, 0, 0, 5500, 0)
    SetChrPos(0x2, 0, 0, 5500, 0)
    SetChrPos(0x3, 0, 0, 5500, 0)
    SetChrChipByIndex(0x36, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 8500, 0, 2500, 180)
    SetChrChipByIndex(0x37, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, 11500, 0, 2500, 180)
    SetChrChipByIndex(0x38, 0x0)
    SetChrSubChip(0x38, 0x0)
    ClearChrFlags(0x38, 0x80)
    SetChrFlags(0x38, 0x8000)
    SetChrFlags(0x38, 0x20)
    SetChrPos(0x38, 33800, 0, -550, 45)
    SetChrChipByIndex(0x39, 0x0)
    SetChrSubChip(0x39, 0x0)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrFlags(0x39, 0x20)
    SetChrPos(0x39, 33800, 0, 550, 135)
    SetChrChipByIndex(0x3A, 0x2A)
    SetChrSubChip(0x3A, 0x0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrPos(0x3A, -5000, 0, -1000, 90)
    SetChrChipByIndex(0x3B, 0x2A)
    SetChrSubChip(0x3B, 0x0)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    SetChrPos(0x3B, 25000, 0, 1000, 270)
    SetChrChipByIndex(0x3D, 0x26)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrFlags(0x3D, 0x20)
    SetChrPos(0x3D, 34000, 0, 0, 270)
    BeginChrThread(0x3D, 3, 0, 130)
    SetChrChipByIndex(0x3E, 0x28)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, 34600, 50, -1300, 315)
    SetChrChipByIndex(0x3F, 0x27)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, 35700, 50, 400, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xFF, 0xC7, 0xBB, 0x12C, 0x384, 0x0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日、１８：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    PlayBGM("ed7151", 0)
    OP_68(10000, 1000, 0, 10000)
    MoveCamera(60, 13, 0, 10000)

    def lambda_11717():
        OP_96(0xFE, 0x61A8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_11717)

    def lambda_11731():
        OP_96(0xFE, 0xFFFFEC78, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_11731)
    FadeToBright(1000, 0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x39, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(35000, 1000, 0, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(18000, 5000)
    BeginChrThread(0x3D, 0, 0, 131)
    BeginChrThread(0x38, 0, 0, 131)
    BeginChrThread(0x39, 0, 0, 131)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x36)
    OP_64(0x37)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x1)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x1)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0x1D, -54850, 50, 123900, 270)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -45100, 0, 115300, 270)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -45100, 0, 118200, 270)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -58800, 0, 120000, 90)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -44800, 0, 121300, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -44400, 0, 120400, 270)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -58800, 0, 118600, 90)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -59300, 0, 115700, 90)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_70(0x14, 0x46)
    OP_70(0x15, 0x46)
    OP_68(-54240, 2000, 113000, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    OP_68(-54240, 2000, 117000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-56210, 2000, 121490, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    OP_0D()
    Sleep(300)

    #C0384
    ChrTalk(
        0x1D,
        (
            "#02803F#11P#30W……そうか……分かった。\x02\x03",

            "#02801F……こちらはもう安全だ。\x01",
            "安心してくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0385
    ChrTalk(
        0x1D,
        "#02806F#11P#30W……………………………\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x23,
        "#11P#02500F……テロリストたちの方は？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x1D, 0x2)
    ClearChrFlags(0x1D, 0x10)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x1D, 0xB4, 0x1F4)
    Fade(500)
    OP_68(-54240, 2000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    OP_0D()

    #C0387
    ChrTalk(
        0x1D,
        (
            "#02803F#5P共和国の一団は、《黒月#4Rヘイユエ#》という\x01",
            "貿易会社の社員に囚われたそうです。\x02\x03",

            "#02801F何でも共和国政府の逮捕委任状を\x01",
            "持っているとの事でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x20,
        "#07005F#11P#Nえ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0389
    ChrTalk(
        0x22,
        (
            "#6P#07502Fおお、それは重畳#4Rちょうじょう#！\x02\x03",

            "#07509F彼らは我々の友人でしてな。\x01",
            "身分は保証しますからご安心を。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xB,
        "#12004F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0391
    ChrTalk(
        0x1D,
        (
            "#02806Fそして帝国からの一団は……\x02\x03",

            "#02801F帝国政府による委任状の下に\x01",
            "《赤い星座》なる猟兵団に\x01",
            "ほぼ全員が処刑されたそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0392
    ChrTalk(
        0x21,
        "#6P……なんたることか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-49800, 2000, 116900, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13860, 0)
    SetChrSubChip(0x23, 0x0)
    OP_0D()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0393
    ChrTalk(
        0x1F,
        (
            "#07207F#11P──宰相！\x01",
            "いったいどういうつもりか！？\x02\x03",

            "帝国政府が処刑などの名目で\x01",
            "国外で猟兵団を運用しただと！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    #C0394
    ChrTalk(
        0x1E,
        (
            "#5P#07404Fええ、確実を期すために。\x02\x03",

            "#07401F私はともかく皇子殿下を狙った罪は\x01",
            "万死に値すると言わざるを得ません。\x02\x03",

            "背後にいる愚か者たちへの\x01",
            "良い警告にもなってくれるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x1F,
        "#07201Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        "#11508F#11P（……よく言うぜ。）\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0397
    ChrTalk(
        0x24,
        (
            "#02205F#11P#Nた、確かに自治州法では\x01",
            "認めざるを得ませんが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x23, 0x1)

    #C0398
    ChrTalk(
        0x23,
        (
            "#5P#02507Fだが、これはあまりに──\x02\x03",

            "あまりに信義にもとる\x01",
            "やり方ではありませんか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x22,
        "#6P#07505F#Nおお、それは誤解です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-54240, 2000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrSubChip(0x22, 0x0)

    def lambda_12119():
        TurnDirection(0xFE, 0x22, 0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_12119)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    Sleep(300)

    #C0400
    ChrTalk(
        0x22,
        (
            "#6P#07504Fそれよりも方々#4Rかたがた#……\x01",
            "図らずとも証明されましたな？\x02\x03",

            "#07502Fこの程度のアクシデントですら\x01",
            "クロスベル自治州政府には\x01",
            "自力で解決できないという事が。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0401
    ChrTalk(
        0x23,
        "#11P#02501F……！\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x1E,
        (
            "#11P#07404Fふむ、まんまとテロリストを\x01",
            "会議の場に近づけた挙句……\x02\x03",

            "無様に取り逃がし、\x01",
            "結局は我々の配慮によって\x01",
            "逃亡を阻止できたわけか。\x02\x03",

            "#07402F確かに、先ほどの議案の\x01",
            "良い事例と言えるであろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x22,
        (
            "#6P#07503Fええ、失礼ながら実際に\x01",
            "命を狙われた皆様方にとって……\x02\x03",

            "#07500F先ほどの駐留案、\x01",
            "もはや真剣に検討せざるを\x01",
            "得ないのではありませんかな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x0)
    Sleep(300)

    def lambda_12424():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_12424)
    WaitChrThread(0x23, 2)
    Sleep(500)

    #C0404
    ChrTalk(
        0x23,
        "#5P#02501Fあ、あなた方は……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x21,
        "#12P……なんと強引な………\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x20,
        "#07008F#11P#Nま、まさかそのために……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0407
    ChrTalk(
        0x1F,
        (
            "#07201F#11P……ここまで悪辣な仕掛けを\x01",
            "用意しているとはねぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1D)
    OP_93(0x1D, 0xB4, 0x1F4)
    Sleep(300)

    #C0408
    ChrTalk(
        0x1D,
        (
            "#02803F#5P──皆さん。\x01",
            "議論が脱線しているようです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x22, 0x1)
    SetChrSubChip(0x1F, 0x2)
    OP_68(-54850, 1300, 122600, 0)
    MoveCamera(63, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-55060, 1300, 123450, 20000)
    MoveCamera(49, 16, 0, 20000)
    OP_6E(500, 20000)
    SetCameraDistance(18000, 20000)
    Sleep(1000)

    #C0409
    ChrTalk(
        0x1D,
        (
            "#02800F#5P#30W宰相閣下と大統領閣下の\x01",
            "ご意見も拝聴に値しますが……\x02\x03",

            "その前に、襲撃によって邪魔された\x01",
            "私の発言を再開させていただきたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x23,
        "#11P#02505F#30Wディ、ディーター君……？\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x1E,
        "#11P#N#07405F#30Wほう……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0412
    ChrTalk(
        0x22,
        "#12P#N#07505F#30W………ふむ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0413
    ChrTalk(
        0x21,
        "#30Wして、どのような提議を？\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x1D,
        (
            "#5P#02804F#30Wいえ──提議ではなく\x01",
            "決意表明というべきでしょうか。\x02\x03",

            "迷いもあったのですが……\x01",
            "この事件で決意は固まりました。\x02\x03",

            "#02800F今、この場をお借りして\x01",
            "１つの提唱をさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x1E,
        "#11P#N#07401F#30W……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0416
    ChrTalk(
        0x22,
        "#12P#N#07501F#30Wなに……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    OP_6F(0x79)

    #C0417
    ChrTalk(
        0x1D,
        (
            "#5P#02803F#30W我々はもはや、他国の思惑に\x01",
            "振り回されるわけにはいきません。\x02\x03",

            "#02801F周辺地域の、いや大陸全土の\x01",
            "恒久的な平和と発展のためにも──\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-55060, 1300, 123450, 500)
    MoveCamera(49, 16, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(16500, 500)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0418
    ChrTalk(
        0x1D,
        (
            "#5P#02807F#4S私はここに、市民及び大陸諸国に対し、\x01",
            "『クロスベルの国家独立』を提唱します！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("m0401", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_129_1147C end

    def Function_130_12960(): pass

    label("Function_130_12960")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12977")
    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("Function_130_12960")

    label("loc_12977")

    Return()

    # Function_130_12960 end

    def Function_131_12978(): pass

    label("Function_131_12978")


    def lambda_1297D():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1297D)
    WaitChrThread(0xFE, 1)
    Sleep(1500)
    OP_63(0x3E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_129B6():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_129B6)
    WaitChrThread(0xFE, 1)
    Sleep(1500)

    def lambda_129D7():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_129D7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_12978 end

    def Function_132_129F1(): pass

    label("Function_132_129F1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C6E")
    SetChrName("")

    #A0419
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0420
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば、会議中は\x01",
            "手前のエレベーター以外は\x01",
            "使えないんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#00100Fええ、確か警備上の理由で\x01",
            "そういう事になっていたわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_12B8D")

    #C0422
    ChrTalk(
        0x103,
        (
            "#00200F非常階段同様、\x01",
            "ここも導力ネットによって\x01",
            "制御・管理されているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#00003Fああ、そうらしいな。\x02\x03",

            "#00000Fまあいい、移動する時は\x01",
            "手前のエレベーターを使おう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C66")

    label("loc_12B8D")


    #C0424
    ChrTalk(
        0x103,
        (
            "#00200Fちなみに、ロックの開閉は\x01",
            "導力ネットによって\x01",
            "制御・管理されているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        (
            "#00003Fああ、流石はオルキスターの\x01",
            "セキュリティってところだな。\x02\x03",

            "#00000Fまあいい、移動する時は\x01",
            "手前のエレベーターを使おう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C66")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_12CDD")

    label("loc_12C6E")

    SetChrName("")

    #A0426
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x02\x03",

            "会議中、このエレベーターは\x01",
            "使用できないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_12CDD")

    TalkEnd(0xFF)
    Return()

    # Function_132_129F1 end

    def Function_133_12CE1(): pass

    label("Function_133_12CE1")

    EventBegin(0x1)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    Sleep(500)

    #C0427
    ChrTalk(
        0x1A,
        "今は本会議の真っ最中だ。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x1A,
        "中の様子は回廊室で窺ってくれ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 9780, 0, 1430, 180)
    OP_93(0x1A, 0xB4, 0x0)
    OP_4C(0x1A, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_133_12CE1 end

    def Function_134_12D53(): pass

    label("Function_134_12D53")

    EventBegin(0x1)

    #C0429
    ChrTalk(
        0x101,
        (
            "#00003F……会議場に入るわけにはいかない。\x02\x03",

            "#00001F迷惑にならない内に離れよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 90250, 0, 76140, 270)
    EventEnd(0x4)
    Return()

    # Function_134_12D53 end

    def Function_135_12DBE(): pass

    label("Function_135_12DBE")

    EventBegin(0x1)

    #C0430
    ChrTalk(
        0x101,
        (
            "#00003F……会議場に入るわけにはいかない。\x02\x03",

            "#00001F迷惑にならない内に離れよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168870, 0, 76540, 90)
    EventEnd(0x4)
    Return()

    # Function_135_12DBE end

    SaveToFile()

Try(main)
