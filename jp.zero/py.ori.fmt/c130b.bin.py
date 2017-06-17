from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c130b.bin",                # FileName
        "c130b",                    # MapName
        "c130b",                    # Location
        0x001B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 27, 0, 0, 0, 1],
    )

    BuildStringList((
        "c130b",                  # 0
        "警備隊員",               # 1
        "警備隊員",               # 2
        "警備隊員",               # 3
        "警備隊員",               # 4
        "警備隊員",               # 5
        "警備隊員",               # 6
        "警備隊員",               # 7
        "警備隊員",               # 8
        "警備隊員",               # 9
        "警備隊員",               # 10
        "警備隊員",               # 11
        "警備隊員",               # 12
        "警備隊員",               # 13
        "警備隊員",               # 14
        "警備隊員",               # 15
        "警備隊員",               # 16
        "ギヨーム親方",           # 17
        "警備員ウォング",         # 18
        "警備員ポール",           # 19
        "ツァオ",                 # 20
        "ラウ",                   # 21
        "グレイス",               # 22
        "レインズ",               # 23
        "レクター",               # 24
        "キーア",                 # 25
        "アリオス",               # 26
        "セルゲイ課長",           # 27
        "ダドリー捜査官",         # 28
        "ツァイト",               # 29
        "ディーター総裁",         # 30
        "マリアベル",             # 31
        "シズク",                 # 32
        "爆弾",                   # 33
        "爆弾",                   # 34
        "SE制御",                 # 35
        "BC130b",                 # 36
        "BC130b",                 # 37
        "BC130b",                 # 38
        "BC130b",                 # 39
        "BC130b",                 # 40
        "BC130b",                 # 41
        "中央広場",               # 42
        "西通り",                 # 43
        "行政区",                 # 44
        "住宅街",                 # 45
        "歓楽街",                 # 46
        "東通り",                 # 47
        "旧市街",                 # 48
        "港湾区",                 # 49
        "ＩＢＣ",                 # 50
        "駅前通り",               # 51
        "裏通り",                 # 52
        "ウルスラ間道",           # 53
        "東クロスベル街道",       # 54
        "西クロスベル街道",       # 55
        "マインツ山道",           # 56
    ))

    ATBonus("ATBonus_754", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_814", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_818", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_81C", 2, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_820", 14, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_824", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_828", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_82C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_800", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_804", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_808", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_80C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_810", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_834", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_838", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_83C", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_840", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_844", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_848", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_850", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_854", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_858", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_85C", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_860", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_864", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_868", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_86C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_870", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_874", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_878", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_87C", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_880", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_884", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_888", 9, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_88C", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_890", 10, 12, 180)

    # monster count: 0

    # event battle count: 6

    BattleInfo(
        "BattleInfo_894", 0x00CA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31200.dat", "ms31200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_814", "MonsterBattlePostion_7F4", "ed7404", "ed7000", "ATBonus_754"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8D8", 0x00CA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_834", "MonsterBattlePostion_7F4", "ed7404", "ed7000", "ATBonus_754"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_91C", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, 0, "MonsterBattlePostion_814", "MonsterBattlePostion_7F4", "ed7404", "ed7000", "ATBonus_754"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_960", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_834", "MonsterBattlePostion_7F4", "ed7404", "ed7000", "ATBonus_754"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9A4", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms32600.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", 0, 0, 0, "MonsterBattlePostion_854", "MonsterBattlePostion_7F4", "ed7404", "ed7000", "ATBonus_754"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9E8", 0x00EA, 35, 6, 0, 0, 0, 0, 0, "BC130b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31300.dat", "ms31200.dat", "ms31200.dat", "ms31200.dat", "ms31200.dat", "MonsterBattlePostion_874", "MonsterBattlePostion_7F4", "ed7404", "ed7000", "ATBonus_754"),
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央広場")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西通り")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "歓楽街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧市街")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "駅前通り")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "裏通り")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-163.66000366210938, 0.0, -206.52999877929688, 0x0000, 0x0051, "")
    PlaceName(-90.51000213623047, 0.0, -171.14999389648438, 0x0000, 0x0054, "")
    PlaceName(-130.32000732421875, 0.0, -217.4199981689453, 0x0000, 0x0057, "")
    PlaceName(-164.67999267578125, 0.0, -167.05999755859375, 0x0000, 0x0053, "")
    PlaceName(-136.77999877929688, 0.0, -134.39999389648438, 0x0000, 0x0053, "")
    PlaceName(-205.85000610351562, 0.0, -173.8699951171875, 0x0000, 0x0053, "")
    PlaceName(-219.1199951171875, 0.0, -145.2899932861328, 0x0000, 0x0053, "")
    PlaceName(-186.4600067138672, 0.0, -101.7300033569336, 0x0000, 0x0052, "")
    PlaceName(-179.99000549316406, 0.0, -119.43000030517578, 0x0000, 0x0053, "")
    PlaceName(-168.0800018310547, 0.0, -131.0, 0x0000, 0x0053, "")
    PlaceName(-129.3000030517578, 0.0, -34.369998931884766, 0x0000, 0x0051, "")
    PlaceName(23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0052, "")
    PlaceName(0.0, 0.0, -341.95001220703125, 0x0000, 0x0053, "")
    PlaceName(-17.690000534057617, 0.0, -316.7699890136719, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_AEC",          # 00, 0
        "Function_1_B41",          # 01, 1
        "Function_2_B63",          # 02, 2
        "Function_3_CC8",          # 03, 3
        "Function_4_1212",         # 04, 4
        "Function_5_12BE",         # 05, 5
        "Function_6_1372",         # 06, 6
        "Function_7_1433",         # 07, 7
        "Function_8_14F4",         # 08, 8
        "Function_9_1B64",         # 09, 9
        "Function_10_1BC8",        # 0A, 10
        "Function_11_1C64",        # 0B, 11
        "Function_12_1D04",        # 0C, 12
        "Function_13_1DC0",        # 0D, 13
        "Function_14_1E4B",        # 0E, 14
        "Function_15_1ED6",        # 0F, 15
        "Function_16_2264",        # 10, 16
        "Function_17_2886",        # 11, 17
        "Function_18_2F04",        # 12, 18
        "Function_19_2FFA",        # 13, 19
        "Function_20_31FD",        # 14, 20
        "Function_21_3AD1",        # 15, 21
        "Function_22_718D",        # 16, 22
        "Function_23_726E",        # 17, 23
        "Function_24_7348",        # 18, 24
        "Function_25_7386",        # 19, 25
        "Function_26_73BB",        # 1A, 26
        "Function_27_7BFE",        # 1B, 27
        "Function_28_7C98",        # 1C, 28
        "Function_29_7D32",        # 1D, 29
        "Function_30_7D8A",        # 1E, 30
        "Function_31_7DE2",        # 1F, 31
        "Function_32_7E3A",        # 20, 32
        "Function_33_7E92",        # 21, 33
        "Function_34_7EEA",        # 22, 34
        "Function_35_7F42",        # 23, 35
        "Function_36_7F9A",        # 24, 36
        "Function_37_8018",        # 25, 37
        "Function_38_804D",        # 26, 38
        "Function_39_807C",        # 27, 39
        "Function_40_80B1",        # 28, 40
        "Function_41_80E0",        # 29, 41
        "Function_42_810F",        # 2A, 42
        "Function_43_813E",        # 2B, 43
        "Function_44_816D",        # 2C, 44
        "Function_45_819C",        # 2D, 45
        "Function_46_81DF",        # 2E, 46
        "Function_47_AA64",        # 2F, 47
    ))


    def Function_0_AEC(): pass

    label("Function_0_AEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B09")
    SetScenarioFlags(0x0, 0)
    Event(0, 3)

    label("loc_B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_B1D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_B40")

    label("loc_B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_B31")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 21)
    Jump("loc_B40")

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_B40")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 46)

    label("loc_B40")

    Return()

    # Function_0_AEC end

    def Function_1_B41(): pass

    label("Function_1_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B56")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x201), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_B56")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    Return()

    # Function_1_B41 end

    def Function_2_B63(): pass

    label("Function_2_B63")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch28600.itc", 0x1E)
    OP_68(0, 2500, -26500, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 2300, 400, 6000, 180)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2300, 400, 6000, 180)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x0)
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日、２２：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7513", 0)
    OP_68(0, 7500, -20500, 10000)
    MoveCamera(0, -9, 0, 10000)
    SetCameraDistance(14000, 10000)
    FadeToBright(2000, 0)
    Sleep(8000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 0)
    NewScene("c134B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_B63 end

    def Function_3_CC8(): pass

    label("Function_3_CC8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31200.itc", 0x26)
    LoadChrToIndex("chr/ch31250.itc", 0x27)
    LoadChrToIndex("chr/ch31251.itc", 0x28)
    LoadChrToIndex("chr/ch31253.itc", 0x29)
    LoadChrToIndex("chr/ch31252.itc", 0x2A)
    LoadChrToIndex("chr/ch0005C.itc", 0x2B)
    LoadChrToIndex("chr/ch00056.itc", 0x2C)
    LoadChrToIndex("chr/ch00352.itc", 0x2D)
    LoadChrToIndex("chr/ch00359.itc", 0x2E)
    LoadEffect(0x0, "battle\\ms00001.eff")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -22700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -700, 0, 4800, 180)
    SetChrPos(0x102, -1500, 0, 6600, 180)
    SetChrPos(0x103, 1500, 0, 6600, 180)
    SetChrPos(0x104, 700, 0, 4800, 180)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 2000, 0, -22900, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -2000, 0, -22900, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_78(0xD, 0x28)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x4)
    OP_49()
    SetChrPos(0x28, 900, 0, -22700, 0)
    OP_D3(0x28, 0x0, 0x0, 0x0, 0x0)
    OP_70(0xD, 0x0)
    OP_78(0xE, 0x29)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetChrFlags(0x29, 0x8000)
    ClearChrFlags(0x29, 0x4)
    OP_49()
    SetChrPos(0x29, -900, 0, -22700, 0)
    OP_D3(0x29, 0x0, 0x0, 0x0, 0x0)
    OP_70(0xD, 0x0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7513", "ed7000")
    SetCameraDistance(17500, 2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(963, 0, 100, 0)
    OP_71(0xD, 0x1, 0x19, 0x0, 0x0)
    Sleep(10)
    OP_71(0xE, 0x1, 0x19, 0x0, 0x0)
    OP_79(0xD)
    OP_71(0xD, 0x19, 0x28, 0x0, 0x20)
    OP_79(0xE)
    OP_71(0xE, 0x19, 0x28, 0x0, 0x20)
    Sound(140, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x10)
    Sound(115, 0, 100, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(400)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(200)

    def lambda_FB1():
        OP_96(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFB1E0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FB1)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 5)
    Sleep(200)

    def lambda_FD7():
        OP_96(0xFE, 0x640, 0x0, 0xFFFFB820, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FD7)

    def lambda_FF1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FF1)

    def lambda_FFE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FFE)
    OP_79(0xC)
    PlayBGM("ed7404", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    OP_68(0, 900, -6500, 0)
    MoveCamera(40, 27, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(12500, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_68(0, 900, -11500, 1500)
    SetCameraDistance(14500, 1500)
    OP_6F(0x11)
    OP_68(0, 800, -15500, 0)
    MoveCamera(25, 11, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x8, 1400, 0, -22900, 0)
    SetChrPos(0x9, -1400, 0, -22900, 0)
    SetChrPos(0x28, 600, 0, -22400, 0)
    SetChrPos(0x29, -600, 0, -22400, 0)
    Sleep(500)
    OP_68(0, 800, -20500, 1500)
    MoveCamera(50, 11, 0, 1500)
    SetCameraDistance(17500, 1500)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15000, 300)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)

    def lambda_1155():
        OP_96(0xFE, 0x514, 0x0, 0xFFFFAE5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1155)

    def lambda_116F():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFAE5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_116F)
    Sleep(300)
    Battle("BattleInfo_894", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    Call(0, 8)
    Call(0, 15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C5")
    OP_2C(0x4E, 0x1)
    Call(0, 16)

    label("loc_11C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DB")
    OP_2C(0x4E, 0x1)
    Call(0, 17)

    label("loc_11DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F1")
    OP_2C(0x4E, 0x1)
    Call(0, 20)

    label("loc_11F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120E")
    OP_2C(0x4E, 0x3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_120E")

    Call(0, 21)
    Return()

    # Function_3_CC8 end

    def Function_4_1212(): pass

    label("Function_4_1212")


    def lambda_1217():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFFC0B8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1217)
    Sleep(3500)
    Sound(1091, 255, 100, 0)    #voice#Lloyd
    WaitChrThread(0x101, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x18)
    SetChrChip(0x0, 0x101, 0x1E, 0x12C)
    Sound(854, 0, 100, 0)

    def lambda_125E():
        OP_9D(0xFE, 0xFFFFFB50, 0x0, 0xFFFFAD30, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_125E)
    Sleep(450)
    SetChrSubChip(0x101, 0x19)
    Sound(533, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x101, 0x1A)
    BeginChrThread(0x9, 3, 0, 7)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2C)
    SetChrSubChip(0x101, 0x0)
    Sleep(300)
    SetChrChip(0x1, 0x101, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x9, 3)
    Return()

    # Function_4_1212 end

    def Function_5_12BE(): pass

    label("Function_5_12BE")


    def lambda_12C3():
        OP_96(0xFE, 0x3E8, 0x0, 0xFFFFC4A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_12C3)
    WaitChrThread(0x104, 1)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x1)
    SetChrChip(0x0, 0x104, 0x1E, 0x12C)
    Sound(814, 0, 100, 0)

    def lambda_1301():
        OP_9D(0xFE, 0x4B0, 0x0, 0xFFFFB118, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1301)
    Sleep(110)
    SetChrSubChip(0x104, 0x2)
    Sleep(110)
    SetChrSubChip(0x104, 0x3)
    Sleep(110)
    SetChrSubChip(0x104, 0x4)
    Sleep(110)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x15)
    Sleep(70)
    Sound(1373, 255, 100, 1)    #voice#Randy
    SetChrSubChip(0x104, 0x1D)
    BeginChrThread(0x8, 3, 0, 6)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x104, 0x2)
    ClearChrFlags(0x104, 0x20)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x3)
    Sleep(300)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    WaitChrThread(0x8, 3)
    Return()

    # Function_5_12BE end

    def Function_6_1372(): pass

    label("Function_6_1372")

    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x0, 0xFF, 0x8, 0x0, 0, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sleep(100)
    Sound(246, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)

    def lambda_13D6():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_13D6)

    def lambda_13EF():
        OP_9D(0xFE, 0x6A4, 0x0, 0xFFFF9AD4, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13EF)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Sound(514, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 80, 0)
    OP_0D()
    Return()

    # Function_6_1372 end

    def Function_7_1433(): pass

    label("Function_7_1433")

    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x0, 0xFF, 0x9, 0x0, 0, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    Sleep(100)
    Sound(246, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)

    def lambda_1497():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1497)

    def lambda_14B0():
        OP_9D(0xFE, 0xFFFFF95C, 0x0, 0xFFFF9AD4, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14B0)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sound(514, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x2)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 80, 0)
    OP_0D()
    Return()

    # Function_7_1433 end

    def Function_8_14F4(): pass

    label("Function_8_14F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31252.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    LoadChrToIndex("chr/ch26400.itc", 0x2D)
    LoadChrToIndex("chr/ch28600.itc", 0x2E)
    LoadChrToIndex("chr/ch00057.itc", 0x2F)
    LoadChrToIndex("chr/ch0035B.itc", 0x30)
    LoadChrToIndex("chr/ch00056.itc", 0x31)
    LoadChrToIndex("chr/ch00356.itc", 0x32)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -26700, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x3)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 1100, 0, -28000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -1100, 0, -28000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x18, 0x2D)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x2E)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x1A, 0x2E)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -1300, 0, -18800, 180)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 1300, 0, -18700, 180)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 800, 0, -17700, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    OP_78(0xD, 0x28)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x4)
    OP_49()
    SetChrPos(0x28, 700, 0, -21700, 0)
    OP_D3(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xD, 0x19, 0x28, 0x0, 0x20)
    OP_78(0xE, 0x29)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetChrFlags(0x29, 0x8000)
    ClearChrFlags(0x29, 0x4)
    OP_49()
    SetChrPos(0x29, -700, 0, -21700, 0)
    OP_D3(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xE, 0x19, 0x28, 0x0, 0x20)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    LoadEffect(0x0, "battle\\ms00001.eff")
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 12)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_68(0, 1000, -24000, 1500)
    OP_6F(0x1)

    #N0002
    NpcTalk(
        0x19,
        "警備員たち",
        "#5P#Nおおっ……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0003
    ChrTalk(
        0x18,
        "#5Pやるじゃねえか！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#5P#0013Fよし……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#11P#0301F油断すんな！\x01",
            "すぐ次が来るぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#11P#0207Fまだ爆弾は起動前です……！\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#5P#0107F中に運び込んで\x01",
            "解体してしまってください！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x18,
        "#5P任せとけ！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x19,
        "#2P運び込むぞ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0010
    ChrTalk(
        0x1A,
        "#1Pひええっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 1000, -21700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    BeginChrThread(0x18, 3, 0, 9)
    BeginChrThread(0x19, 3, 0, 10)
    Sleep(4000)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x8, -1200, -2800, -39500, 0)
    SetChrPos(0x9, 1200, -2800, -39500, 0)
    SetChrPos(0x10, 0, -2500, -38000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    OP_68(0, -1800, -38000, 2000)
    OP_6F(0x1)
    ClearMapObjFlags(0xD, 0x1000)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xE, 0x4)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)

    #C0011
    ChrTalk(
        0x101,
        "#0007F来たか……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#0307F喰い止めるぞ！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, -27000, 2000)
    MoveCamera(37, 17, 0, 2000)
    SetCameraDistance(15500, 2000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_1ADF():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1ADF)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_1B04():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B04)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_1B26():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B26)
    OP_6F(0x79)
    Battle("BattleInfo_8D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    Return()

    # Function_8_14F4 end

    def Function_9_1B64(): pass

    label("Function_9_1B64")


    def lambda_1B69():
        OP_95(0xFE, -1500, 0, -21900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1B69)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x5A, 0x1F4)

    def lambda_1B8E():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0xFFFFD184, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1B8E)

    def lambda_1BA8():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFD24C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1BA8)
    Sound(964, 0, 100, 0)
    WaitChrThread(0x18, 1)
    Return()

    # Function_9_1B64 end

    def Function_10_1BC8(): pass

    label("Function_10_1BC8")

    Sleep(100)

    def lambda_1BD0():
        OP_95(0xFE, 1400, 0, -21900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BD0)
    Sleep(300)

    def lambda_1BED():
        OP_95(0xFE, 700, 0, -20900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BED)
    WaitChrThread(0x19, 1)
    OP_93(0x19, 0x10E, 0x1F4)
    WaitChrThread(0x1A, 1)

    def lambda_1C16():
        OP_96(0xFE, 0x578, 0x0, 0xFFFFD184, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1C16)

    def lambda_1C30():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFD56C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C30)

    def lambda_1C4A():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFD24C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1C4A)
    WaitChrThread(0x19, 1)
    Return()

    # Function_10_1BC8 end

    def Function_11_1C64(): pass

    label("Function_11_1C64")

    Sound(1011, 255, 100, 0)    #voice#Lloyd
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x1)

    def lambda_1C81():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFF96EC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C81)
    WaitChrThread(0x101, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(400)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x2)
    Sound(814, 0, 100, 0)

    def lambda_1CC7():
        OP_9D(0xFE, 0xFFFFFCE0, 0x0, 0xFFFF9C64, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CC7)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Return()

    # Function_11_1C64 end

    def Function_12_1D04(): pass

    label("Function_12_1D04")

    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    Sleep(150)
    SetChrSubChip(0x104, 0x1)

    def lambda_1D22():
        OP_96(0xFE, 0x384, 0x0, 0xFFFF96EC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D22)
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(100)
    Sound(1320, 255, 100, 1)    #voice#Randy
    SetChrSubChip(0x104, 0x3)
    WaitChrThread(0x104, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x8, 3, 0, 13)
    Sleep(300)
    SetChrSubChip(0x104, 0x4)
    Sleep(300)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x2)
    Sound(814, 0, 100, 0)

    def lambda_1D83():
        OP_9D(0xFE, 0x320, 0x0, 0xFFFF9E58, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D83)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Return()

    # Function_12_1D04 end

    def Function_13_1DC0(): pass

    label("Function_13_1DC0")

    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    Sound(246, 0, 100, 0)

    def lambda_1E11():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1E11)

    def lambda_1E2A():
        OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFE890, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E2A)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Return()

    # Function_13_1DC0 end

    def Function_14_1E4B(): pass

    label("Function_14_1E4B")

    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    Sound(246, 0, 100, 0)

    def lambda_1E9C():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E9C)

    def lambda_1EB5():
        OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFE890, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EB5)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Return()

    # Function_14_1E4B end

    def Function_15_1ED6(): pass

    label("Function_15_1ED6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31252.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -24200, 180)
    SetChrPos(0x104, 800, 0, -25500, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 1800, -3800, -47500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1800, -3800, -47500, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, 900, -3500, -46000, 0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, -900, -3500, -46000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    #C0013
    ChrTalk(
        0x101,
        "#5P#0000Fよし、これで──\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x103,
        "#0207F#11P第二波、来ます！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        "#5P#0010Fくっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    Fade(250)
    OP_68(0, -4000, -39000, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(0, 0, -27000, 3000)
    MoveCamera(0, 17, 0, 3000)
    SetCameraDistance(17500, 3000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_21B9():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_21B9)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)

    def lambda_21DB():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21DB)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_2200():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2200)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_2222():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2222)
    OP_6F(0x79)
    Battle("BattleInfo_91C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    Return()

    # Function_15_1ED6 end

    def Function_16_2264(): pass

    label("Function_16_2264")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31252.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    LoadChrToIndex("chr/ch06300.itc", 0x2D)
    LoadChrToIndex("chr/ch31400.itc", 0x2E)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 1100, -3800, -47500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1100, -3800, -47500, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, 0, -3300, -45500, 0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, 1700, -3500, -46000, 0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, -1700, -3500, -46000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x1B, 0x2D)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x2E)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 10700, -7000, -70400, 0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 11800, -7000, -70400, 0)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    FadeToBright(500, 0)
    OP_0D()

    #C0016
    ChrTalk(
        0x101,
        (
            "#5P#0013Fくっ、中に入ろうにも\x01",
            "こう矢継ぎ早に来られたら……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0101F#5Pゲートを閉める時間を\x01",
            "何とか稼がないと……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    Fade(1000)
    OP_68(11300, -6000, -70400, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 2000)
    OP_0D()
    OP_6F(0x10)
    SetCameraDistance(14500, 10000)

    #C0018
    ChrTalk(
        0x1B,
        (
            "#11P#3209Fフフ……頑張りますね。\x02\x03",

            "#3202F《銀#2Rイン#》殿の報告から判断して\x01",
            "今回は大人しく引っ込んでいるしか\x01",
            "なさそうでしたが……\x02\x03",

            "存外面白い物が見られそうです。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)
    Sleep(300)

    #C0019
    ChrTalk(
        0x1C,
        (
            "#11Pで、ですがツァオ様。\x01",
            "あのままではいずれ……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1B,
        (
            "#11P#3204Fここで倒れてしまうのであれば\x01",
            "彼らも所詮、\x01",
            "その程度の器だったという事──\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x10E, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0x1B,
        "#11P#3210Fほら、次が来ましたよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    Fade(1000)
    OP_68(0, -3000, -39000, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 500, -28000, 3000)
    MoveCamera(35, 15, 0, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_279D():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_279D)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)

    def lambda_27C2():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_27C2)
    SetChrChipByIndex(0x12, 0x2B)
    SetChrSubChip(0x12, 0x0)

    def lambda_27E4():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_27E4)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_2809():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2809)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_282B():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_282B)
    OP_0D()
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    OP_6F(0x79)
    Battle("BattleInfo_960", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    Return()

    # Function_16_2264 end

    def Function_17_2886(): pass

    label("Function_17_2886")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31352.itc", 0x29)
    LoadChrToIndex("chr/ch31350.itc", 0x2A)
    LoadChrToIndex("chr/ch31351.itc", 0x2B)
    LoadChrToIndex("chr/ch31353.itc", 0x2C)
    LoadChrToIndex("chr/ch32650.itc", 0x2D)
    LoadChrToIndex("chr/ch32651.itc", 0x2E)
    LoadChrToIndex("chr/ch06000.itc", 0x2F)
    LoadChrToIndex("chr/ch28100.itc", 0x30)
    LoadChrToIndex("chr/ch32600.itc", 0x31)
    LoadChrToIndex("chr/ch32654.itc", 0x32)
    LoadChrToIndex("apl/ch50314.itc", 0x33)
    LoadEffect(0x0, "event\\eva02_00.eff")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x17, 0x31)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 2000, -3800, -44500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -2000, -3800, -44500, 0)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x10, 0x4)
    OP_90(0x10, 4300, -3000, -43800, 0)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x11, 0x4)
    OP_90(0x11, -4300, -3000, -43800, 0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    OP_90(0x17, 0, -2000, -42000, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1D, 0x2F)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x1E, 0x30)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -17700, -4200, -72900, 45)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -17900, -4200, -71800, 45)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    FadeToBright(500, 0)
    OP_0D()

    #C0022
    ChrTalk(
        0x103,
        (
            "#5P#0208Fこの勢いで攻め込まれたら\x01",
            "ゲートもおそらく……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#5P#0007Fああ……！\x01",
            "ここで喰い止めるしない！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    Fade(1000)
    OP_68(-17800, -3300, -72300, 0)
    MoveCamera(20, 27, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(14500, 2000)
    OP_0D()
    OP_6F(0x10)
    SetCameraDistance(14000, 10000)
    OP_63(0x1E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    TurnDirection(0x1E, 0x1D, 500)

    #C0024
    ChrTalk(
        0x1E,
        (
            "#5Pグ、グレイス先輩……\x01",
            "一体何が起こってるんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x1D,
        (
            "#6P#2101Fいいから撮りまくりなさい！\x02\x03",

            "それがペンとカメラしか武器の無い\x01",
            "あたしたちが出来る唯一の戦いよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1E)

    #C0026
    ChrTalk(
        0x1E,
        "#5Pは、はい……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x2D, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x1E, 0x33)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    BeginChrThread(0x1E, 0, 0, 18)
    Sleep(500)

    #C0027
    ChrTalk(
        0x1D,
        (
            "#6P#2103F（ロイド君たち……\x01",
            "  きっと凄い記事にしてみせるわ。）\x02\x03",

            "#2101F（だから絶対に生き延びて……\x01",
            "  自分たちの活躍を読んでちょうだい！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    EndChrThread(0x1E, 0xFF)
    Fade(1000)
    OP_68(0, -500, -35000, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(11500, 3000)

    def lambda_2DE9():
        OP_96(0xFE, 0x0, 0xFFFFF95C, 0xFFFF7748, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2DE9)
    OP_0D()
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    WaitChrThread(0x17, 1)
    OP_6F(0x10)
    SetChrChipByIndex(0x17, 0x32)
    SetChrSubChip(0x17, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x17, 0x4)
    Fade(250)
    OP_68(0, -1000, -35000, 0)
    MoveCamera(0, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(19000, 0)
    OP_68(0, -500, -29000, 2000)
    MoveCamera(0, 15, 0, 2000)
    SetCameraDistance(15000, 2000)
    BeginChrThread(0x17, 3, 0, 19)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_2E99():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E99)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_2EBB():
        OP_98(0xFE, 0x1F4, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2EBB)
    OP_6F(0x79)
    Sleep(700)
    Battle("BattleInfo_9A4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x17, 0xFF)
    Return()

    # Function_17_2886 end

    def Function_18_2F04(): pass

    label("Function_18_2F04")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)

    label("loc_2F41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FF9")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F6F")
    Sleep(500)
    Jump("loc_2FB7")

    label("loc_2F6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F86")
    Sleep(1500)
    Jump("loc_2FB7")

    label("loc_2F86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F9D")
    Sleep(2000)
    Jump("loc_2FB7")

    label("loc_2F9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2FB4")
    Sleep(3000)
    Jump("loc_2FB7")

    label("loc_2FB4")

    Sleep(4000)

    label("loc_2FB7")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Jump("loc_2F41")

    label("loc_2FF9")

    Return()

    # Function_18_2F04 end

    def Function_19_2FFA(): pass

    label("Function_19_2FFA")

    Sleep(400)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    Sound(854, 0, 100, 0)

    def lambda_3015():
        OP_9D(0xFE, 0x10CC, 0xFFFFF7CC, 0xFFFF6488, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3015)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x11, 0x2)
    SetChrFlags(0x11, 0x20)

    def lambda_303F():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFF7CC, 0xFFFF6488, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_303F)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_3070():
        OP_9D(0xFE, 0x10CC, 0xFFFFFAEC, 0xFFFF7428, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3070)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_309B():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFFAEC, 0xFFFF7428, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_309B)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_30CC():
        OP_9D(0xFE, 0x10CC, 0xFFFFFE0C, 0xFFFF83C8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30CC)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_30F7():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFFE0C, 0xFFFF83C8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30F7)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_3128():
        OP_9D(0xFE, 0x10CC, 0x320, 0xFFFF9368, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3128)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_3153():
        OP_9D(0xFE, 0xFFFFEF34, 0x320, 0xFFFF9368, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3153)
    WaitChrThread(0x10, 1)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x1)

    def lambda_317F():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_317F)
    Sound(854, 0, 100, 0)
    Sound(925, 0, 100, 0)

    def lambda_3198():
        OP_9D(0xFE, 0x708, 0x0, 0xFFFF9A70, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3198)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x1)

    def lambda_31C1():
        OP_93(0xFE, 0x2D, 0x2BC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_31C1)

    def lambda_31CE():
        OP_9D(0xFE, 0xFFFFF8F8, 0x0, 0xFFFF9A70, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31CE)
    Sleep(300)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x11, 0x2)
    Sleep(100)
    SetChrSubChip(0x10, 0x3)
    SetChrSubChip(0x11, 0x3)
    Return()

    # Function_19_2FFA end

    def Function_20_31FD(): pass

    label("Function_20_31FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31250.itc", 0x26)
    LoadChrToIndex("chr/ch31251.itc", 0x27)
    LoadChrToIndex("chr/ch31253.itc", 0x28)
    LoadChrToIndex("chr/ch31350.itc", 0x29)
    LoadChrToIndex("chr/ch31351.itc", 0x2A)
    LoadChrToIndex("chr/ch31353.itc", 0x2B)
    LoadChrToIndex("chr/ch07400.itc", 0x2C)
    LoadChrToIndex("chr/ch00357.itc", 0x2D)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 1000, -25000, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -800, 0, -25500, 180)
    SetChrPos(0x102, -1500, 0, -24200, 180)
    SetChrPos(0x103, 1500, 0, -23200, 180)
    SetChrPos(0x104, 800, 0, -25000, 180)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x26)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    OP_90(0x8, 1000, -3800, -47700, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_90(0x9, -1000, -3800, -47700, 0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    OP_90(0xA, 2300, -4500, -48500, 0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    OP_90(0xB, -2300, -4500, -48500, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    OP_90(0x10, 0, -3300, -45500, 0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    OP_90(0x11, 1700, -3500, -46000, 0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    OP_90(0x12, -1700, -3500, -46000, 0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x13, 0, -3800, -46800, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x1F, 0x2C)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -16800, -7500, -46500, 45)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "battle\\cr003301.eff")
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35A6")

    #C0028
    ChrTalk(
        0x101,
        "#0010F#5Pい、今のはミレイユ准尉……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0106F#5Pそんな、あの人まで……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#0201F#5P！！　ランディさん……？\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0310F#5Pクソが……\x01",
            "ふざけやがって……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363F")

    label("loc_35A6")


    #C0032
    ChrTalk(
        0x104,
        "#0308F#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#5P#0013F今の女性隊員……　\x01",
            "ランディの知り合いか？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#0303F#5Pああ……元同僚だ……\x02\x03",

            "#0310Fクソが……\x01",
            "ふざけやがって……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363F")

    Sleep(300)
    OP_68(800, 1000, -25000, 2000)
    MoveCamera(0, 30, 0, 2000)
    SetCameraDistance(14500, 2000)
    Sound(1301, 255, 100, 0)    #voice#Randy
    PlayEffect(0x0, 0xFF, 0x104, 0x0, 0, 600, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    OP_82(0x64, 0x64, 0xBB8, 0x7D0)
    Sleep(2000)
    OP_6F(0x79)
    Sound(1310, 255, 100, 0)    #voice#Randy
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(17500, 1000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)
    SetChrSubChip(0x104, 0x1)
    PlayEffect(0x1, 0xFF, 0x104, 0x0, 0, 100, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_6F(0x10)
    Sleep(300)
    CancelBlur(0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    Fade(1000)
    OP_68(-16750, -6500, -46520, 0)
    MoveCamera(20, 23, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_0D()
    OP_6F(0x10)
    SetCameraDistance(13500, 10000)

    #C0035
    ChrTalk(
        0x1F,
        (
            "#5P#3502Fやれやれ、頑張るねぇ。\x02\x03",

            "#3506Fしかしこのままだと\x01",
            "ギリアスのオッサンの狙い通りに\x01",
            "なっちまいそうだなァ。\x02\x03",

            "#3510Fんー、どうしたもんか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1F, 0x87, 0x1F4)

    #C0036
    ChrTalk(
        0x1F,
        (
            "#5P#3505Fあっちゃあ……\x01",
            "次で終わりかもな。\x02\x03",

            "#3504Fま、せいぜい頑張れよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Fade(1000)
    OP_68(0, -3000, -39000, 0)
    MoveCamera(35, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(0, 500, -28000, 3000)
    MoveCamera(35, 15, 0, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x20)

    def lambda_3967():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3967)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x20)

    def lambda_398E():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_398E)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x20)

    def lambda_39B8():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_39B8)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x20)

    def lambda_39DF():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_39DF)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_3A01():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3A01)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_3A23():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3A23)
    Sleep(50)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_3A48():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A48)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)

    def lambda_3A6A():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A6A)
    OP_0D()
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    OP_6F(0x79)
    OP_32(0x3, 0xFE, 0x0)
    OP_32(0x3, 0x5, 0xC8)
    Battle("BattleInfo_9E8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x13, 0xFF)
    Return()

    # Function_20_31FD end

    def Function_21_3AD1(): pass

    label("Function_21_3AD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x14)
    LoadChrToIndex("chr/ch00053.itc", 0x15)
    LoadChrToIndex("chr/ch00150.itc", 0x16)
    LoadChrToIndex("chr/ch00153.itc", 0x17)
    LoadChrToIndex("chr/ch00250.itc", 0x18)
    LoadChrToIndex("chr/ch00253.itc", 0x19)
    LoadChrToIndex("chr/ch00350.itc", 0x1A)
    LoadChrToIndex("chr/ch00353.itc", 0x1B)
    LoadChrToIndex("chr/ch31250.itc", 0x1C)
    LoadChrToIndex("chr/ch31251.itc", 0x1D)
    LoadChrToIndex("chr/ch31253.itc", 0x1E)
    LoadChrToIndex("chr/ch31252.itc", 0x1F)
    LoadChrToIndex("chr/ch31350.itc", 0x20)
    LoadChrToIndex("chr/ch31351.itc", 0x21)
    LoadChrToIndex("chr/ch31353.itc", 0x22)
    LoadChrToIndex("chr/ch31300.itc", 0x23)
    LoadChrToIndex("chr/ch00056.itc", 0x24)
    LoadChrToIndex("chr/ch00156.itc", 0x25)
    LoadChrToIndex("chr/ch00256.itc", 0x26)
    LoadChrToIndex("chr/ch00356.itc", 0x27)
    LoadChrToIndex("chr/ch02400.itc", 0x28)
    LoadChrToIndex("apl/ch50539.itc", 0x29)
    LoadChrToIndex("apl/ch50509.itc", 0x2A)
    LoadChrToIndex("apl/ch50506.itc", 0x2B)
    LoadChrToIndex("chr/ch00950.itc", 0x2C)
    LoadChrToIndex("chr/ch00951.itc", 0x2D)
    LoadChrToIndex("chr/ch08200.itc", 0x2E)
    LoadChrToIndex("chr/ch00051.itc", 0x2F)
    LoadChrToIndex("chr/ch00151.itc", 0x30)
    LoadChrToIndex("chr/ch00251.itc", 0x31)
    LoadChrToIndex("chr/ch00351.itc", 0x32)
    LoadChrToIndex("chr/ch02750.itc", 0x33)
    LoadChrToIndex("chr/ch02751.itc", 0x34)
    LoadChrToIndex("chr/ch02702.itc", 0x35)
    LoadChrToIndex("chr/ch08201.itc", 0x36)
    LoadChrToIndex("apl/ch50513.itc", 0x37)
    LoadChrToIndex("apl/ch50514.itc", 0x38)
    LoadChrToIndex("apl/ch50515.itc", 0x39)
    LoadChrToIndex("apl/ch50540.itc", 0x3A)
    LoadChrToIndex("apl/ch50545.itc", 0x3B)
    LoadEffect(0x0, "event\\ev500_00.eff")
    LoadEffect(0x1, "event\\eva03_00.eff")
    LoadEffect(0x2, "event\\ev609_00.eff")
    LoadEffect(0x3, "event\\ev609_01.eff")
    LoadEffect(0x4, "event\\eva04_00.eff")
    LoadEffect(0x5, "event\\eva03_00.eff")
    LoadEffect(0x6, "event\\ev001_00.eff")
    LoadEffect(0x7, "battle\\ms00001.eff")
    SoundLoad(840)
    OP_68(0, 800, -23700, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x15)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x17)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x19)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x1B)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x101, -800, 0, -22000, 180)
    SetChrPos(0x102, -1500, 0, -20700, 180)
    SetChrPos(0x103, 1500, 0, -19700, 180)
    SetChrPos(0x104, 800, 0, -21500, 180)
    SetChrChipByIndex(0x8, 0x1C)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1C)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1C)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x20)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 800, 0, -27500, 0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, -800, 0, -27500, 0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, 3000, -150, -28700, 0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, -3000, -150, -28700, 0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    SetChrPos(0x10, 2100, 0, -26200, 315)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x4)
    SetChrPos(0x11, -2100, 0, -26200, 45)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x4)
    SetChrPos(0x12, 0, -300, -29500, 0)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x13, 0, -1500, -34500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x21, 0x28)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x4)
    OP_90(0x21, 0, -10500, -71500, 0)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x4)
    OP_90(0x22, -700, -6700, -55800, 0)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x4)
    OP_90(0x23, 700, -6700, -55800, 0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 0, 0, -8400, 180)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01101.itp")
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(0, 800, -25700, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)

    #C0037
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#35W…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4087")

    #C0039
    ChrTalk(
        0x101,
        "#5P#0010F#N#40Wくっ……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#5P#0301F#N#40Wクソ……\x01",
            "数が多すぎるぜ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_41D9")

    label("loc_4087")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E4")

    #C0041
    ChrTalk(
        0x101,
        "#5P#0010F#N#40W……ぐうっ……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#5P#0206F#N#40Wげ、限界です……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_41D9")

    label("loc_40E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4147")

    #C0043
    ChrTalk(
        0x101,
        "#5P#0008F#N#40W……だ、駄目か……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#5P#0106F#N#40Wこ、こんな所で……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_41D9")

    label("loc_4147")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419A")

    #C0045
    ChrTalk(
        0x101,
        (
            "#5P#0008F#N#40W……くっ……\x01",
            "（ここで倒れるわけには……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_41D9")

    label("loc_419A")


    #C0046
    ChrTalk(
        0x101,
        (
            "#5P#0006F#N#40W……くっ……\x01",
            "（これしか粘れないのか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_41D9")

    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    #Sound(1957, 255, 100, 0)    #voice#Joachim
    Sleep(1000)

    #N0047
    NpcTalk(
        0x13,
        "男の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "フフ……\x01",
            "なかなか頑張ったようだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    PlayBGM("ed7526", 0)
    Fade(500)
    OP_68(0, -500, -30500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x25)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x26)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x27)
    SetChrSubChip(0x104, 0x0)
    OP_68(0, 500, -26500, 3000)

    def lambda_42E2():
        OP_96(0xFE, 0x0, 0x0, 0xFFFF9B9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_42E2)
    Sleep(1000)
    BeginChrThread(0x12, 3, 0, 42)
    Sleep(1300)
    BeginChrThread(0x8, 3, 0, 43)
    BeginChrThread(0x9, 3, 0, 44)
    Sleep(200)
    BeginChrThread(0x10, 3, 0, 40)
    BeginChrThread(0x11, 3, 0, 41)
    OP_6F(0x1)
    Fade(500)
    OP_68(20, 1000, -23530, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    WaitChrThread(0x13, 1)
    OP_0D()
    OP_6F(0x10)

    #C0048
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0005F……？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#5P#0307F#5Pロギンス！？\x01",
            "なんでお前が──\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pああ、ランディ君。\x01",
            "勘違いしないで欲しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P“僕”は君の元同僚ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P彼の身体を借りて\x01",
            "こうして話しかけているだけさ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x102,
        "#5P#0101Fその口調……！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#5P#0205Fま、まさか……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#5P#0013Fヨアヒム先生……！？\x02",
    )

    CloseMessageWindow()

    #N0056
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pフフ、正解だ。\x02",
        )
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P僕からの招待状は\x01",
            "目を通してくれたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #N0058
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pアーネスト君も一応、\x01",
            "役に立ってくれたというわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0310Fてめぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#5P#0108F一体、何のつもりですか……\x02\x03",

            "#0110Fこんな事をしでかして……\x01",
            "クロスベル全土を混乱に陥れて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#5P#0007Fあなたは……《Ｄ∴Ｇ教団》は\x01",
            "一体何をするつもりなんだ……！？\x02",
        )
    )

    CloseMessageWindow()

    #N0062
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pハハ、それが知りたいのであれば\x01",
            "僕らの仲間になってもらうしかないな。\x02",
        )
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P《グノーシス》を服用してもらえれば\x01",
            "その境地へと導かせてもらうよ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)

    #C0064
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0207Fふ、ふざけないでください……！\x02\x03",

            "#0210F#30W……あなたが……\x01",
            "あなたがあんな酷いことを……！\x02",
        )
    )

    CloseMessageWindow()

    #N0065
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pフフ、別に各ロッジの儀式は\x01",
            "僕がやった事ではないけれどね。\x02",
        )
    )

    CloseMessageWindow()

    #N0066
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P無論《グノーシス》のプロトタイプの\x01",
            "実験データは回収させてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0067
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pそのデータを元に、この古の聖地で\x01",
            "僕は《グノーシス》を完成させた……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0068
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P#4Sそう、全ては運命だったのさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0013Fあ、あんた……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        "#5P#0301F何を口走ってやがる……\x02",
    )

    CloseMessageWindow()

    #N0071
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pクク……\x01",
            "“至らぬ”身である君たちに\x01",
            "理解してもらうつもりはない。\x02",
        )
    )

    CloseMessageWindow()

    #N0072
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P我々の要求はただ一つ。\x02",
        )
    )

    CloseMessageWindow()

    #N0073
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pあの方を──キーア様を\x01",
            "返してもらうというだけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0074
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0105Fあ、あの方……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#5P#0201F……キーア様って……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#5P#0013Fあんた……\x01",
            "あの子をどうするつもりだ！？\x02",
        )
    )

    CloseMessageWindow()

    #N0077
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P勘違いしないでもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #N0078
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pキーア様は元々、我らが御子#4Rみ　こ#。\x02",
        )
    )

    CloseMessageWindow()

    #N0079
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pその身を君たちが預かったのは\x01",
            "ただの偶然に過ぎない。\x02",
        )
    )

    CloseMessageWindow()

    #N0080
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pあの方にはただ、あるべき場所に\x01",
            "還っていただくというだけさ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0081
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0010Fふざけるな……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4C5E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C5E)
    Fade(500)
    SetChrChipByIndex(0x101, 0x14)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    OP_0D()

    def lambda_4C91():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C91)

    def lambda_4CAA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4CAA)

    def lambda_4CC3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4CC3)
    Fade(500)
    SetChrChipByIndex(0x102, 0x16)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x18)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x1A)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0082
    ChrTalk(
        0x101,
        (
            "#0007F#5Pあんたらの狂信に……\x01",
            "あの子を巻き込ませるものか！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0110F#5Pさっきから聞いていれば……\x01",
            "……妄想めいたことばかり……！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#5P#0307Fてめぇみたいな変態野郎の元に\x01",
            "キー坊を戻せるわけねぇだろうが……！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        "#0201F#5Pおととい来やがれ……です……！\x02",
    )

    CloseMessageWindow()

    #N0086
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pやれやれ……交渉は決裂か。\x02",
        )
    )

    CloseMessageWindow()

    #N0087
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pならば君たちの屍を越えて\x01",
            "キーア様をお迎えさせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x2)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(190, 1000, -23260, 1000)
    ClearChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_4EE1():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4EE1)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_4F08():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F08)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    OP_6F(0x1)
    Sleep(500)

    #C0088
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F#5Pくっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#5P#0312Fハッ……上等じゃねぇか……\x02",
    )

    CloseMessageWindow()

    #N0090
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pクク、君たちの女神への\x01",
            "祈りは済ませたかな……？\x02",
        )
    )

    CloseMessageWindow()

    #N0091
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2Pそれでは、死にたまえ──\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x20, 0x8)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    Sleep(300)
    StopBGM(0x1770)
    Sound(2041, 255, 100, 0)    #voice#KeA
    Sleep(150)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    Sleep(1200)
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
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x20, 0x8)
    OP_68(0, 700, -15500, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x8, 0x1C)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1C)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xA, 0x1C)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x1C)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x8, 1500, 0, -28000, 0)
    SetChrPos(0x9, -1500, 0, -28000, 0)
    SetChrPos(0xA, 3000, -150, -29200, 0)
    SetChrPos(0xB, -3000, -150, -29200, 0)
    SetChrPos(0x10, 2600, 0, -26700, 315)
    SetChrPos(0x11, -2600, 0, -26700, 45)
    SetChrPos(0x12, 0, 0, -30000, 0)
    SetChrPos(0x13, 0, 0, -26500, 0)
    SetChrPos(0x101, -900, 0, -20800, 180)
    SetChrPos(0x102, -1600, 0, -19500, 180)
    SetChrPos(0x103, 1600, 0, -18500, 180)
    SetChrPos(0x104, 900, 0, -20300, 180)
    OP_68(0, 700, -22500, 2500)
    MoveCamera(0, 19, 0, 2500)
    SetCameraDistance(19500, 2500)
    SetChrChipByIndex(0x20, 0x36)
    SetChrSubChip(0x20, 0x0)

    def lambda_5204():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFAA10, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_5204)
    WaitChrThread(0x20, 1)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x37)
    SetChrSubChip(0x20, 0x4)
    Sound(804, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x20, 0x3)
    Sleep(100)
    SetChrSubChip(0x20, 0x2)
    Sleep(300)
    OP_6F(0x79)

    #C0092
    ChrTalk(
        0x101,
        "#0007F#5Pキ、キーア……！？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        "#0107F#5P#Nそ、そんな……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #N0094
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pおお、キーア様……\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7534", 0)
    SetCameraDistance(15000, 60000)

    #C0095
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#1107Fロイドたちをいじめちゃだめ！\x02\x03",

            "いじめたらキーア、\x01",
            "絶対にゆるさないんだからっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        (
            "#0307F#11Pキー坊……！\x01",
            "いいから下がってろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        "#0207F#11P#N前に出てはダメです……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #N0098
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pキーア様。\x01",
            "お迎えに上がりました。\x02",
        )
    )

    CloseMessageWindow()

    #N0099
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pそのような愚物どもなど放って\x01",
            "我らの元にお戻りください。\x02",
        )
    )

    CloseMessageWindow()

    #N0100
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P今は何も分からないでしょうが、\x01",
            "貴女は我らの──\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0x20, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(931, 0, 80, 0)
    Sound(840, 2, 100, 0)
    SetChrSubChip(0x20, 0x2)
    Sleep(100)
    SetChrSubChip(0x20, 0x1)
    Sleep(100)
    SetChrSubChip(0x20, 0x0)
    Sleep(100)
    SetChrSubChip(0x20, 0x1)
    Sleep(100)
    SetChrSubChip(0x20, 0x2)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #A0101
    AnonymousTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "いいから早く\x01",
            "ヤクソクしなさいっ……！\x02\x03",

            "ロイドたちにこれ以上、\x01",
            "ひどいことしないって……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    def lambda_558C():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_558C)
    Sleep(50)

    def lambda_55A8():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_55A8)

    def lambda_55C1():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_55C1)

    def lambda_55DA():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_55DA)
    Sleep(50)

    def lambda_55F6():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_55F6)

    def lambda_560F():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_560F)
    Sleep(50)

    def lambda_562B():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_562B)

    def lambda_5644():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5644)
    Sleep(300)

    #N0102
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#5Pえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#0105F#5P#Nキ、キーアちゃん……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0105
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#1115F…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #N0106
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pフフ……ハハハハ……\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P……それでこそ……！\x01",
            "それでこそ我らの御子だ……ッ！\x02",
        )
    )

    CloseMessageWindow()

    #N0108
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pかしこまりました。\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pキーア様さえお戻りになれば\x01",
            "彼らには決して危害は加えません。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#1119F……ホントウに？\x02\x03",

            "ヒドイことしたりしない？\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pええ、もちろんですとも。\x02",
        )
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pさあ……どうぞこちらへ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0113
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0007F#5P駄目だ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(270, 800, -21290, 0)
    MoveCamera(43, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 60000)
    SetChrSubChip(0x20, 0xA)
    SetChrPos(0x13, 0, 0, -26200, 0)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x0)

    def lambda_5906():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5906)
    WaitChrThread(0x101, 1)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    SetChrChipByIndex(0x101, 0x14)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x20, 0x20)
    ClearChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    TurnDirection(0x20, 0x101, 500)
    Sleep(300)

    #C0114
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1117F#11Pロイド……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0010Fキーア……\x01",
            "“暗い”のが怖いんだろう！？\x02\x03",

            "俺たちから離れるのが\x01",
            "寂しくて嫌なんだろう……！？\x02\x03",

            "だったら、こんなヤツの\x01",
            "言うことなんて聞いたら駄目だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1119F#11P#30W……で、でも……\x02\x03",

            "#1118Fキーア……キオクがないし……\x02\x03",

            "だ、誰なのかもわからないし……\x02\x03",

            "#1120Fロイドたちにメーワクかけるなら\x01",
            "……い、いっしょになんて……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0117
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0007F迷惑なんかじゃない……！\x02\x03",

            "#0000F俺は──俺たちの方こそ\x01",
            "キーアに側にいて欲しいんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1117F#11P………え……………\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 37)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 39)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 38)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    Sleep(300)

    #C0119
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0104F多分、私たちは……\x01",
            "あなたがいてくれたおかげで\x01",
            "本当の意味で成長できたと思う……\x02\x03",

            "#0102Fあなたを見守る……\x01",
            "その事に、それぞれが求める\x01",
            "意味を見出すことによって……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    #C0120
    ChrTalk(
        0x103,
        (
            "#5P#0204Fはい……\x02\x03",

            "#0208F……何のために生きているのか\x01",
            "分からないわたしですけど……\x02\x03",

            "#0214Fみんなとキーアを守るためなら\x01",
            "何だってできる気がします……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)

    #C0121
    ChrTalk(
        0x104,
        (
            "#0300F#5Pだからキー坊……\x01",
            "余計なことは気にすんじゃねえ。\x02\x03",

            "お前はノンキに笑いながら\x01",
            "すくすく育っていけばいいんだ。\x02\x03",

            "#0309Fそれだけで俺たちは\x01",
            "パワーを貰えてるんだからよ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x13B, 0x190)
    Sleep(750)
    OP_93(0x20, 0x2D, 0x190)
    Sleep(300)

    #C0122
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#6P#1119F#40W……エリィ……\x01",
            "ティオ……ランディ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x4)
    SetChrChipByIndex(0x24, 0x34)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x24, -2600, 1000, -8300, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)

    def lambda_5E19():
        OP_92(0xFE, 0xA28, 0xFFFFC43C, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5E19)
    Sound(814, 0, 90, 0)

    def lambda_5E32():
        OP_9D(0xFE, 0xA28, 0x0, 0xFFFFC43C, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5E32)
    WaitChrThread(0x24, 1)
    Sound(832, 0, 100, 0)

    def lambda_5E59():
        OP_92(0xFE, 0xFFFFF5D8, 0xFFFFA8E4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5E59)
    SetChrSubChip(0x24, 0x1)
    Sleep(50)
    SetChrSubChip(0x24, 0x2)
    Sleep(50)
    SetChrSubChip(0x24, 0x3)
    Sleep(50)
    SetChrSubChip(0x24, 0x0)
    Sleep(50)
    Sound(854, 0, 90, 0)

    def lambda_5E8E():
        OP_9D(0xFE, 0xFFFFF5D8, 0x0, 0xFFFFA8E4, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5E8E)
    WaitChrThread(0x24, 1)
    Sound(832, 0, 100, 0)
    SetChrSubChip(0x24, 0x1)
    Sleep(50)
    SetChrSubChip(0x24, 0x2)
    Sleep(50)
    SetChrSubChip(0x24, 0x3)
    Sleep(50)

    def lambda_5ECA():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5ECA)
    SetChrChipByIndex(0x24, 0x35)
    SetChrSubChip(0x24, 0x0)
    WaitChrThread(0x24, 2)
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    #Sound(2053, 255, 100, 0)    #voice#Zeit

    #C0123
    ChrTalk(
        0x24,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#1200Fグルルル……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x20, 0x24, 500)
    Sleep(300)

    #C0124
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1116F#11P#40Wツァイトも……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0004F俺たちは捜査官だ。\x02\x03",

            "過去や記憶が気になるんだったら\x01",
            "俺たちが一緒に取り戻してやる……\x02\x03",

            "#0008F少なくともこんなヤツの\x01",
            "言いなりになる必要はないんだ。\x02\x03",

            "#0001Fだからキーア……行かないでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1116F#11P#40W……ロイド………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetCameraDistance(15000, 800)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x2A, 1, 0, 45)
    OP_0D()
    Sleep(1000)

    #C0127
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1104F#11P#40W…………うん。\x02\x03",

            "#1102Fキーア、みんなと一緒にいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#5P#0002F……そっか。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#5P#0102Fキーアちゃん……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, -23700, 1500)
    OP_6F(0x1)
    #Sound(1956, 255, 100, 0)    #voice#Joachim
    Sleep(150)

    #N0130
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11Pクク……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    #Sound(1959, 255, 100, 0)    #voice#Joachim
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #N0131
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#4Sハハハハハハハハッ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6155():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_6155)
    Sleep(50)

    def lambda_6165():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_6165)
    SetChrChipByIndex(0x24, 0x33)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x24, 2)

    def lambda_619F():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFB244, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_619F)
    Sleep(500)

    #N0132
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11Pよくもそんな妄言で\x01",
            "我らの御子を誑#2Rたぶら#かしたものだ……\x02",
        )
    )

    CloseMessageWindow()

    #N0133
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P……様子見に預けておいたのが\x01",
            "そもそもの誤りだったわけか……\x02",
        )
    )

    CloseMessageWindow()

    #N0134
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P特務支援課……！\x01",
            "貴様ら全員、嬲り殺しにしてくれる！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x2)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_68(160, 800, -23310, 1000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)

    def lambda_62FB():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_62FB)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_631D():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_631D)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x20, 1)
    OP_6F(0x1)
    Sleep(500)

    #C0135
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0101F#5Pくっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#0202F#5P#N……でも……\x01",
            "少し休めました……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0137
    ChrTalk(
        0x101,
        "#0007F#5Pキーア、下がっていろ！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    #C0138
    ChrTalk(
        0x104,
        (
            "#0307F#5Pせめてキー坊だけでも\x01",
            "ゲートの中に……！\x02",
        )
    )

    CloseMessageWindow()

    #N0139
    NpcTalk(
        0x21,
        "男性の声",
        "#1P──その必要はない。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
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
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_93(0x13, 0xB4, 0x1F4)

    #N0140
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        "#0105F#5Pあ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#0005F#5P……あなたは……！\x02",
    )

    CloseMessageWindow()
    OP_68(0, -200, -28700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x8, 1500, 0, -29500, 0)
    OP_90(0x9, -1500, 0, -29500, 0)
    OP_90(0xA, 3000, -150, -30700, 0)
    OP_90(0xB, -3000, -150, -30700, 0)
    OP_90(0x10, 2600, 0, -28200, 315)
    OP_90(0x11, -2600, 0, -28200, 45)
    OP_90(0x12, 0, 0, -31500, 0)
    OP_90(0x13, 0, 0, -27700, 180)
    OP_68(0, -9500, -71500, 0)
    MoveCamera(33, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x10)
    SetChrChipByIndex(0xC, 0x1C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x1C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x1C)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x1C)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    OP_90(0xC, -2100, -6340, -54200, 150)
    OP_90(0xD, -400, -7120, -57400, 180)
    OP_90(0xE, 1100, -4800, -47900, 190)
    OP_90(0xF, -600, -3100, -40800, 180)
    OP_90(0x14, 900, -6340, -54200, 190)
    OP_90(0x15, 1500, -5880, -52200, 190)
    OP_90(0x16, -900, -4400, -46100, 170)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0x14, 0x8000)
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x2A, 0x1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    SetCameraDistance(15000, 2000)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0xC, 3, 0, 24)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    WaitChrThread(0xC, 3)
    SetChrSubChip(0x21, 0x11)
    Sleep(130)
    SetChrSubChip(0x21, 0x12)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0143
    AnonymousTalk(
        0x21,
        "八葉一刀流、二の型《疾風#4Rはやて#》──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 300)
    Sleep(100)
    SetChrSubChip(0x21, 0x13)
    Sleep(90)
    SetChrSubChip(0x21, 0x14)
    OP_6F(0x10)
    CancelBlur(0)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x14, 3)
    BeginChrThread(0x21, 3, 0, 26)
    WaitChrThread(0x21, 3)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Fade(250)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x9)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    SetCameraDistance(14000, 1000)
    OP_6F(0x10)
    SetChrSubChip(0x21, 0x17)
    Sleep(110)
    SetChrSubChip(0x21, 0x16)
    Sleep(110)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 900, -27500, 1000)
    SetCameraDistance(18500, 1000)
    MoveCamera(43, 23, 0, 1000)

    #C0144
    ChrTalk(
        0x21,
        "#5P#1407F#4S#9A斬#2Rザン#……！\x02",
    )
    #Auto

    SetChrSubChip(0x21, 0x15)
    Sound(532, 0, 100, 0)
    Sleep(70)
    PlayEffect(0x3, 0xFF, 0x21, 0x40, 0, 1000, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(541, 0, 100, 0)
    Sleep(30)
    SetChrSubChip(0x21, 0x1D)
    OP_82(0x1F4, 0x0, 0xBB8, 0x384)
    Sound(816, 0, 100, 0)
    Sound(340, 0, 100, 0)
    BeginChrThread(0x11, 3, 0, 34)
    Sleep(10)
    BeginChrThread(0xB, 3, 0, 32)
    Sleep(10)
    BeginChrThread(0x9, 3, 0, 30)
    Sleep(10)
    BeginChrThread(0x13, 3, 0, 36)
    Sleep(10)
    BeginChrThread(0x12, 3, 0, 35)
    Sleep(10)
    BeginChrThread(0x8, 3, 0, 29)
    Sleep(10)
    BeginChrThread(0x10, 3, 0, 33)
    Sleep(10)
    BeginChrThread(0xA, 3, 0, 31)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    CancelBlur(0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1100, -25500, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_90(0x13, 0, 0, -28100, 0)
    OP_68(0, 1100, -24500, 1500)
    OP_6F(0x1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    Sleep(500)

    #C0145
    ChrTalk(
        0x101,
        "#5P#0002Fアリオスさん……！\x02",
    )

    CloseMessageWindow()

    def lambda_6B1A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6B1A)
    WaitChrThread(0x13, 2)
    Sleep(300)

    #N0146
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P#40Wか、風の剣聖……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0309Fおいおい！\x01",
            "すげえタイミングだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        "#5P#0202F狙ってたみたいです……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x21, 0x20)
    ClearChrFlags(0x21, 0x2)
    SetChrSubChip(0x21, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    Sound(541, 0, 100, 0)
    Sound(531, 0, 80, 0)
    OP_0D()
    Sleep(500)

    #C0149
    ChrTalk(
        0x21,
        (
            "#5P#1404Fフフ……\x01",
            "そんなつもりは無かったが。\x02\x03",

            "#1402Fちなみに、\x01",
            "来たのは俺だけではないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    OP_90(0xD, -2700, -5300, -49800, 135)
    OP_90(0x15, 2200, -5000, -48600, 315)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0x14, 0x1)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x2)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    OP_90(0xC, 900, -4340, -46000, 180)
    OP_90(0x14, -1100, -4500, -46500, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    Fade(500)
    OP_68(0, -3700, -47500, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(15500, 3000)
    OP_0D()
    Sound(567, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 23)
    Sleep(500)
    Sound(845, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 22)
    Sleep(500)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)

    def lambda_6D61():
        OP_96(0xFE, 0x2BC, 0xFFFFEE08, 0xFFFF4868, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6D61)
    Sleep(100)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrSubChip(0x22, 0x0)

    def lambda_6D86():
        OP_96(0xFE, 0xFFFFFD44, 0xFFFFEDA4, 0xFFFF4674, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6D86)
    WaitChrThread(0x23, 1)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    WaitChrThread(0x22, 1)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    Sound(531, 0, 100, 0)
    OP_6F(0x10)
    Sleep(300)

    #C0151
    ChrTalk(
        0x23,
        "#11P#0601Fクッ……先を越されたか！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x22,
        (
            "#5P#1004Fフ……\x01",
            "さすがに俺もトシだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x20,
        "#1110Fあ、かちょーだぁ！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#0002Fダドリーさんも……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)

    def lambda_6E5D():
        OP_96(0xFE, 0x514, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6E5D)
    Sleep(50)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrSubChip(0x22, 0x0)

    def lambda_6E82():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6E82)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 1100, -28700, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x22, 0x1)
    OP_90(0x22, -1100, -2500, -36700, 0)
    OP_90(0x23, 1100, -2500, -36700, 0)
    SetChrPos(0x102, -1600, 0, -20800, 180)
    SetChrPos(0x103, 1600, 0, -19300, 180)
    SetChrPos(0x104, 900, 0, -21400, 180)
    SetChrPos(0x20, 300, 0, -20300, 180)
    OP_68(0, 1100, -26700, 2000)

    def lambda_6F51():
        OP_96(0xFE, 0x514, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6F51)
    Sleep(50)

    def lambda_6F6E():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6F6E)
    WaitChrThread(0x23, 1)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    Sound(531, 0, 100, 0)
    Sound(820, 0, 100, 0)

    def lambda_6FA0():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_6FA0)
    WaitChrThread(0x22, 1)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x22, 0x0)
    TurnDirection(0x22, 0x13, 500)
    SetChrChipByIndex(0x22, 0x2A)
    SetChrSubChip(0x22, 0x4)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    Sleep(500)

    #N0155
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#40Wき、貴様ら……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0309F#5P#Nははっ……\x01",
            "カッコつけすぎだろ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x102,
        (
            "#0102F#5P#Nお２人とも……\x01",
            "よくご無事で……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0158
    ChrTalk(
        0x22,
        (
            "#5P#1002F幸い、良いタイミングで\x01",
            "アリオスと合流できてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x23,
        (
            "#0602F#11P思わぬ加勢もあったから\x01",
            "こうして辿り着けたわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#0005F#5P#N思わぬ加勢……？\x02\x03",

            "#0000F……あ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0161
    ChrTalk(
        0x103,
        "#0202F#5P#Nあれは……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(0, 100, -31700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_CA(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x348)
    SetScenarioFlags(0x5C, 2)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_3AD1 end

    def Function_22_718D(): pass

    label("Function_22_718D")

    OP_82(0xC8, 0x0, 0xBB8, 0x96)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_71F3():
        OP_9C(0xFE, 0xFFFFFC7C, 0x0, 0x9C4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71F3)

    def lambda_7210():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7210)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    OP_93(0xFE, 0x10E, 0x0)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_22_718D end

    def Function_23_726E(): pass

    label("Function_23_726E")

    OP_82(0xC8, 0x0, 0xBB8, 0x96)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_72D4():
        OP_9C(0xFE, 0x384, 0x0, 0x9C4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72D4)

    def lambda_72F1():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72F1)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_726E end

    def Function_24_7348(): pass

    label("Function_24_7348")

    SetChrChipByIndex(0xC, 0x1D)
    SetChrSubChip(0xC, 0x0)

    def lambda_7355():
        OP_96(0xFE, 0xFFFFF7CC, 0xFFFFDB20, 0xFFFEFA48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7355)
    Sleep(1500)
    BeginChrThread(0x14, 3, 0, 25)
    WaitChrThread(0xC, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x2)
    Return()

    # Function_24_7348 end

    def Function_25_7386(): pass

    label("Function_25_7386")

    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)

    def lambda_7393():
        OP_96(0xFE, 0x384, 0xFFFFDEA4, 0xFFFF0920, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7393)
    WaitChrThread(0x14, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_25_7386 end

    def Function_26_73BB(): pass

    label("Function_26_73BB")

    PlayEffect(0x5, 0x0, 0x21, 0x40, 0, 0, 0, 180, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0x1, 0x21, 0x40, 0, 0, 0, 180, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-2500, -8300, -66600, 500)
    MoveCamera(10, 19, 5, 500)
    SetCameraDistance(13500, 500)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    SetChrFlags(0x21, 0x20)
    ClearChrFlags(0x21, 0x1)
    SetChrChip(0x0, 0x21, 0x32, 0x1F4)
    ClearChrFlags(0x21, 0x2)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x6)
    OP_92(0x21, 0xFFFFF574, 0xFFFF0024, 0x0)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_74F3():
        OP_96(0xFE, 0xFFFFF574, 0xFFFFDC10, 0xFFFF0024, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_74F3)

    def lambda_750D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0xC8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_750D)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_7541():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7541)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    OP_6F(0x79)
    Sleep(350)
    OP_68(1200, -7700, -63700, 500)
    MoveCamera(20, 15, -7, 500)
    SetCameraDistance(13000, 500)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0x8FC, 0xFFFF0BDC, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7617():
        OP_96(0xFE, 0x8FC, 0xFFFFDECC, 0xFFFF0BDC, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7617)

    def lambda_7631():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0xC8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7631)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_7665():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7665)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    OP_6F(0x79)
    Sleep(300)
    OP_68(0, -6100, -57500, 0)
    MoveCamera(180, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(0, -3700, -43500, 2000)
    MoveCamera(137, 37, -5, 2000)
    SetCameraDistance(15500, 2000)
    SetChrFlags(0x21, 0x800)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0xFFFFF95C, 0xFFFF234C, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x6)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_776E():
        OP_96(0xFE, 0xFFFFF95C, 0xFFFFE4A8, 0xFFFF2540, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_776E)

    def lambda_7788():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7788)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_77BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_77BC)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0x76C, 0xFFFF3990, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_786B():
        OP_96(0xFE, 0x76C, 0xFFFFE9BC, 0xFFFF3990, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_786B)

    def lambda_7885():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7885)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x15, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_78B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_78B9)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(150)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0xFFFFF9C0, 0xFFFF522C, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x6)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7968():
        OP_96(0xFE, 0xFFFFF9C0, 0xFFFFEF98, 0xFFFF522C, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7968)

    def lambda_7982():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7982)
    Sleep(100)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xE, 3, 0, 27)
    Sleep(100)
    Sound(834, 0, 100, 0)
    BeginChrThread(0x16, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_79BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_79BF)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(100)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sound(250, 0, 100, 0)
    OP_92(0x21, 0x514, 0xFFFF6B90, 0x0)
    ClearChrFlags(0x21, 0x1)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    PlayEffect(0x2, 0x2, 0x21, 0x140, 0, 1000, 0, 0, 10, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7A6E():
        OP_96(0xFE, 0x514, 0xFFFFF5D8, 0xFFFF6B90, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7A6E)

    def lambda_7A88():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7A88)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xF, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_7ABC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7ABC)
    WaitChrThread(0x21, 1)
    WaitChrThread(0x21, 2)
    SetChrFlags(0x21, 0x1)
    Sleep(300)
    OP_6F(0x79)
    ClearChrFlags(0x21, 0x800)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x21, 0x3A)
    SetChrSubChip(0x21, 0x7)
    SetChrChip(0x0, 0x21, 0x1E, 0x12C)
    Sound(814, 0, 100, 0)

    def lambda_7B31():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFA04C, 0x157C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7B31)
    Sleep(250)
    Sound(854, 0, 100, 0)
    Fade(100)
    OP_68(0, 2900, -28000, 0)
    MoveCamera(48, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    OP_68(0, 900, -24500, 500)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    WaitChrThread(0x21, 1)
    Sound(58, 0, 100, 0)
    Sound(31, 0, 100, 0)

    def lambda_7BB1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7BB1)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x1, 0x21, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)
    Return()

    # Function_26_73BB end

    def Function_27_7BFE(): pass

    label("Function_27_7BFE")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7C42():
        OP_A6(0xFE, 0x1E, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C42)
    OP_82(0x190, 0x0, 0xBB8, 0x258)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_7BFE end

    def Function_28_7C98(): pass

    label("Function_28_7C98")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7CDC():
        OP_A6(0xFE, 0x1E, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7CDC)
    OP_82(0x190, 0x0, 0xBB8, 0x258)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x39)
    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_28_7C98 end

    def Function_29_7D32(): pass

    label("Function_29_7D32")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7D50():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7D50)

    def lambda_7D69():
        OP_9C(0xFE, 0x5DC, 0xFFFFFA24, 0xFFFFE4A8, 0x44C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7D69)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_7D32 end

    def Function_30_7D8A(): pass

    label("Function_30_7D8A")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7DA8():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7DA8)

    def lambda_7DC1():
        OP_9C(0xFE, 0xFFFFFA24, 0xFFFFFA24, 0xFFFFE4A8, 0x44C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7DC1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_30_7D8A end

    def Function_31_7DE2(): pass

    label("Function_31_7DE2")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7E00():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7E00)

    def lambda_7E19():
        OP_9C(0xFE, 0xBB8, 0xFFFFE890, 0xFFFFEC78, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7E19)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_31_7DE2 end

    def Function_32_7E3A(): pass

    label("Function_32_7E3A")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7E58():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7E58)

    def lambda_7E71():
        OP_9C(0xFE, 0xFFFFF448, 0xFFFFE890, 0xFFFFEC78, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7E71)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_7E3A end

    def Function_33_7E92(): pass

    label("Function_33_7E92")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7EB0():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_7EB0)

    def lambda_7EC9():
        OP_9C(0xFE, 0x1F40, 0xFFFFE890, 0xFFFFF830, 0x514, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7EC9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_33_7E92 end

    def Function_34_7EEA(): pass

    label("Function_34_7EEA")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7F08():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7F08)

    def lambda_7F21():
        OP_9C(0xFE, 0xFFFFE0C0, 0xFFFFE890, 0xFFFFF830, 0x514, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7F21)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_34_7EEA end

    def Function_35_7F42(): pass

    label("Function_35_7F42")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7F60():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7F60)

    def lambda_7F79():
        OP_9C(0xFE, 0x0, 0xFFFFFA24, 0xFFFFE890, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F79)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_35_7F42 end

    def Function_36_7F9A(): pass

    label("Function_36_7F9A")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7FB3():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7FB3)

    def lambda_7FCC():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7FCC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_7FF1():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7FF1)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Sound(514, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_7F9A end

    def Function_37_8018(): pass

    label("Function_37_8018")

    SetChrChipByIndex(0x102, 0x30)
    SetChrSubChip(0x102, 0x0)

    def lambda_8025():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8025)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x16)
    SetChrSubChip(0x102, 0x0)
    Return()

    # Function_37_8018 end

    def Function_38_804D(): pass

    label("Function_38_804D")

    SetChrChipByIndex(0x103, 0x31)
    SetChrSubChip(0x103, 0x0)

    def lambda_805A():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_805A)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x18)
    SetChrSubChip(0x103, 0x0)
    Return()

    # Function_38_804D end

    def Function_39_807C(): pass

    label("Function_39_807C")

    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x0)

    def lambda_8089():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFBB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8089)
    WaitChrThread(0x104, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x1A)
    SetChrSubChip(0x104, 0x0)
    Return()

    # Function_39_807C end

    def Function_40_80B1(): pass

    label("Function_40_80B1")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_80BE():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_80BE)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_80B1 end

    def Function_41_80E0(): pass

    label("Function_41_80E0")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_80ED():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_80ED)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_80E0 end

    def Function_42_810F(): pass

    label("Function_42_810F")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_811C():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_811C)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_810F end

    def Function_43_813E(): pass

    label("Function_43_813E")

    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_814B():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_814B)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_813E end

    def Function_44_816D(): pass

    label("Function_44_816D")

    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_817A():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_817A)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_816D end

    def Function_45_819C(): pass

    label("Function_45_819C")

    OP_25(0x348, 0x5A)
    Sleep(200)
    OP_25(0x348, 0x50)
    Sleep(200)
    OP_25(0x348, 0x46)
    Sleep(200)
    OP_25(0x348, 0x3C)
    Sleep(200)
    OP_25(0x348, 0x32)
    Sleep(200)
    OP_25(0x348, 0x28)
    Sleep(200)
    OP_25(0x348, 0x1E)
    Sleep(200)
    OP_25(0x348, 0x14)
    Sleep(200)
    OP_25(0x348, 0xA)
    Sleep(200)
    OP_24(0x348)
    Return()

    # Function_45_819C end

    def Function_46_81DF(): pass

    label("Function_46_81DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50514.itc", 0x1E)
    LoadChrToIndex("apl/ch50515.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch02500.itc", 0x22)
    LoadChrToIndex("apl/ch50509.itc", 0x23)
    LoadChrToIndex("chr/ch00900.itc", 0x24)
    LoadChrToIndex("chr/ch00950.itc", 0x25)
    LoadChrToIndex("chr/ch00951.itc", 0x26)
    LoadChrToIndex("chr/ch08200.itc", 0x27)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    LoadChrToIndex("chr/ch05500.itc", 0x29)
    LoadChrToIndex("chr/ch08700.itc", 0x2A)
    LoadChrToIndex("apl/ch50011.itc", 0x2B)
    LoadChrToIndex("chr/ch00953.itc", 0x2C)
    LoadChrToIndex("chr/ch02750.itc", 0x2D)
    LoadChrToIndex("chr/ch02700.itc", 0x2E)
    LoadChrToIndex("chr/ch02702.itc", 0x2F)
    LoadChrToIndex("apl/ch50516.itc", 0x30)
    LoadChrToIndex("apl/ch50517.itc", 0x31)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    SoundLoad(806)
    OP_68(260, 1000, -25050, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -900, 0, -22200, 180)
    SetChrPos(0x102, -1600, 0, -21100, 180)
    SetChrPos(0x103, 1600, 0, -20100, 180)
    SetChrPos(0x104, 900, 0, -21700, 180)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x1)
    SetChrFlags(0x13, 0x8000)
    OP_90(0x13, 0, 0, -28100, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, 0, 0, -24500, 180)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    OP_90(0x22, -1300, 0, -27700, 0)
    TurnDirection(0x22, 0x13, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x25)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    OP_90(0x23, 1300, 0, -27700, 0)
    TurnDirection(0x23, 0x13, 0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x20, 0x27)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 0, 0, -20600, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x24, 0x8000)
    SetChrFlags(0x24, 0x4)
    SetChrChipByIndex(0x24, 0x2D)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x24, -2600, 0, -22300, 135)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x28)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 400, 0, 6000, 180)
    SetChrChipByIndex(0x26, 0x29)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -700, 0, 6500, 180)
    SetChrChipByIndex(0x27, 0x2A)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -1700, 0, 6500, 180)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    OP_68(260, 1000, -23050, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0162
    ChrTalk(
        0x101,
        "#5P#0002Fあいつら……！\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        "#5P#0202Fしかも結構、押してます……！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#5P#0309Fはは……\x01",
            "プロ相手にやるじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #N0165
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11Pくっ……\x01",
            "不良ごときがどうして……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
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
    Sleep(1000)

    def lambda_8644():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_8644)

    def lambda_8651():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8651)

    def lambda_865E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_865E)

    def lambda_866B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_866B)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0166
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0005Fあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#5P#0102Fさっきまで通信が\x01",
            "繋がらなかったのに……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0168
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001Fはい、こちら特務支援課──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("娘の声")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よ、よかった～！\x01",
            "ロイドさん、無事でしたか！\x02\x03",

            "警備隊に追われてるって聞いて　\x01",
            "どうなったのかと……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0170
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002Fフラン……無事だったのか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい……！\x01",
            "こちらも反撃に転じました！\x02\x03",

            "それと遊撃士たちが\x01",
            "破壊された通信ターミナルを\x01",
            "復旧してくれたらしくて……\x02\x03",

            "限定的ではありますが\x01",
            "導力通信が回復できました！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0172
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fそうか……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(1200)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(200)
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("少年の声")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、復旧できたのは\x01",
            "ボクの情報のおかげだけどな！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0174
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fその声は……ヨナか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ヨナの声")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、天才ヨナ様さ！\x02\x03",

            "ついでにＩＢＣと協力して\x01",
            "導力ネットも回復してやったぜ！\x02\x03",

            "ありがたく思えよな！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0176
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0014Fはは……恩に着るよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "現在、警官隊が\x01",
            "そちらに応援に向かっています！\x02\x03",

            "それとお姉ちゃんたちへの連絡は\x01",
            "こちらでも試してみます！\x02\x03",

            "ロイドさん、どうか気をつけて！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("ヨナの声")

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "せいぜい死ぬなよな～！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0179
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fああ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_CA(0x0, 0x0, 0x3)
    Fade(250)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #N0180
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11Pくっ、馬鹿な……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x21,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#1403F──そういう事だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)
    Fade(500)
    OP_68(0, 1000, -26500, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)

    def lambda_8BFA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_8BFA)

    def lambda_8C07():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8C07)

    def lambda_8C14():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8C14)

    def lambda_8C21():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8C21)
    SetCameraDistance(14000, 1000)

    def lambda_8C37():
        OP_96(0xFE, 0x0, 0x0, 0xFFFF9A70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8C37)
    WaitChrThread(0x21, 1)
    SetChrChipByIndex(0x21, 0x30)
    SetChrSubChip(0x21, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_6F(0x10)
    Sleep(500)

    #C0182
    ChrTalk(
        0x21,
        (
            "#5P#1401F《Ｄ∴Ｇ教団》幹部司祭、\x01",
            "ヨアヒム・ギュンター。\x02\x03",

            "これ以上、このクロスベルで\x01",
            "好き勝手な真似はさせんぞ？\x02",
        )
    )

    CloseMessageWindow()

    #N0183
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pクク……いいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P……こちらの戦力は\x01",
            "マフィアと合わせて千名近く……\x02",
        )
    )

    CloseMessageWindow()

    #N0185
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pしかも無尽蔵の体力を持ち、\x01",
            "眠る必要すらない……\x02",
        )
    )

    CloseMessageWindow()

    #N0186
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P歯向かう者は皆殺しにした上で\x01",
            "我らが御子#4Rみ　こ#を取り戻してくれる……\x02",
        )
    )

    CloseMessageWindow()

    #N0187
    NpcTalk(
        0x13,
        "ヨアヒムの声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6Pハハハ……！\x01",
            "楽しみにしているがいい……！！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1961, 255, 100, 0)    #voice#Joachim
    SetChrSubChip(0x13, 0x0)
    PlayEffect(0x0, 0x0, 0x13, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(1000)
    PlayEffect(0x1, 0xFF, 0x13, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x0, 0x2)

    def lambda_8ED0():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8ED0)
    Sleep(500)
    Fade(500)
    Sound(514, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
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
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x3)
    SetChrSubChip(0x22, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0188
    ChrTalk(
        0x23,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#12P#0601F……完全に気絶したか……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        "#0013F#5P#Nい、今のは……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0190
    ChrTalk(
        0x103,
        (
            "#0206F#11P#Nどうやら全く別の場所から\x01",
            "操っていたみたいですね……\x02\x03",

            "#0201Fしかも……\x01",
            "かなり離れた場所かもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0191
    ChrTalk(
        0x102,
        (
            "#0101F#5P#Nもしかして……\x01",
            "そこから警備隊全員を操って！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0301F#11P#Nチッ……\x01",
            "ヨアヒム本人を叩かない限り、\x01",
            "どうしようもねぇってことかよ！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0193
    ChrTalk(
        0x21,
        "#5P#1404F──居場所は判明している。\x02",
    )

    CloseMessageWindow()
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

    #C0194
    ChrTalk(
        0x101,
        "#0011F#5P#Nえ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(0, 1000, -23870, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x21, 0x0, 0x190)
    OP_68(0, 1000, -23200, 1000)

    def lambda_921D():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFA1DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_921D)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)
    Sleep(300)

    #C0195
    ChrTalk(
        0x21,
        (
            "#11P#1403Fエステルとヨシュアが\x01",
            "《教団》の拠点#4Rロッジ#を発見した。\x02\x03",

            "#1401F場所はクロスベル北東にある\x01",
            "《アルモリカ古戦場》──\x02\x03",

            "そこに行方不明者たちが\x01",
            "入った痕跡を発見したそうだ。\x02\x03",

            "#1403Fちょうど今、\x01",
            "潜入経路を調べてもらっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#0013F#5P古戦場……あんな場所に！\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        (
            "#0101F#5P確かに何か\x01",
            "ありそうな遺跡でしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        "#5P#0300Fだったらそっちを叩けば……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(110, 1000, -22710, 1000)

    def lambda_93DC():
        OP_95(0xFE, 1000, 0, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_93DC)
    Sleep(150)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)

    def lambda_9401():
        OP_95(0xFE, -800, 0, -25400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9401)
    WaitChrThread(0x23, 1)
    WaitChrThread(0x22, 1)
    OP_6F(0x1)

    #C0199
    ChrTalk(
        0x23,
        (
            "#0606F#11P……そう単純な話じゃない。\x02\x03",

            "#0601Fどうやら東クロスベル街道にも\x01",
            "相当な戦力が展開しているようだ。\x02\x03",

            "主にマフィアどもらしいがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x22,
        (
            "#12P#1003Fいずれにしても……\x01",
            "こちらの戦力が限られている以上、\x01",
            "闇雲に突っ込むわけにもいかん。\x02\x03",

            "#1001Fせめて車#2Rアシ#さえあれば\x01",
            "何とかなるかもしれんが……\x02\x03",

            "生憎、警察の車両はあらかた\x01",
            "警備隊に奪われてしまったようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        "#0010F#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        "#5P#0206F……徹底していますね。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x25, 0x8)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)

    #N0203
    NpcTalk(
        0x25,
        "男性の声",
        "──それは私が何とかしよう。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_96A3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_96A3)

    def lambda_96B0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_96B0)

    def lambda_96BD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_96BD)

    def lambda_96CA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_96CA)

    def lambda_96D7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_96D7)
    ClearChrFlags(0x25, 0x8)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetCameraDistance(15500, 3000)
    OP_68(0, 1000, 0, 3000)

    def lambda_9717():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9717)
    Sleep(50)

    def lambda_9734():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_9734)

    def lambda_974E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_974E)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)
    OP_6F(0x1)

    #C0204
    ChrTalk(
        0x101,
        "#0005Fディーター総裁……！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x20,
        "#1110Fあ、シズクにベル！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1000, -10500, 0)
    MoveCamera(135, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 200, 0, -16100, 0)
    SetChrPos(0x102, 700, 0, -17300, 0)
    SetChrPos(0x103, -700, 0, -17900, 0)
    SetChrPos(0x104, 500, 0, -18400, 0)
    SetChrPos(0x20, -600, 0, -16500, 0)
    SetChrPos(0x22, 1900, 0, -16900, 0)
    SetChrPos(0x23, 2300, 0, -18300, 0)
    SetChrPos(0x21, -1800, 0, -18500, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, 1000, 0, -20300, 0)
    SetChrPos(0x25, 900, 0, -3400, 180)
    SetChrPos(0x26, -300, 0, -3200, 180)
    SetChrPos(0x27, -1000, 0, -3300, 180)
    SetCameraDistance(16000, 2500)

    def lambda_98C7():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98C7)

    def lambda_98E1():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_98E1)

    def lambda_98FB():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_98FB)
    Sleep(50)

    def lambda_9918():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9918)

    def lambda_9932():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9932)

    def lambda_994C():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_994C)

    def lambda_9966():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_9966)

    def lambda_9980():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_9980)
    Sleep(50)

    def lambda_999D():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_999D)

    def lambda_99B7():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_99B7)

    def lambda_99D1():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_99D1)

    def lambda_99EB():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_99EB)
    Sleep(1000)
    Sound(115, 0, 100, 0)
    OP_71(0xC, 0x3C, 0x0, 0x0, 0x0)
    WaitChrThread(0x24, 1)
    SetChrChipByIndex(0x24, 0x2F)
    SetChrSubChip(0x24, 0x0)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x22, 1)
    WaitChrThread(0x23, 1)
    WaitChrThread(0x21, 1)
    OP_79(0xC)
    OP_6F(0x10)

    #C0206
    ChrTalk(
        0x26,
        (
            "#6P#2904Fふふ……\x01",
            "皆さん、お疲れさまですわ。\x02\x03",

            "#2901Fしかしキーアちゃん。\x01",
            "無茶をしてくれますわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x27,
        (
            "#6P#6001Fそ、そうだよ……！\x01",
            "いきなり走っていくから……！\x02\x03",

            "#6008F……あんまり無茶しないで……！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x20,
        "#11P#1106Fご、ごめんなさぃ……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x21,
        (
            "#1404F#11P……フフ。\x02\x03",

            "#1402Fシズク、無事で何よりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x27,
        "#6P#6010Fうん……お父さんも……！\x02",
    )

    CloseMessageWindow()

    def lambda_9BA7():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD3DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9BA7)
    WaitChrThread(0x22, 1)
    Sleep(300)

    #C0211
    ChrTalk(
        0x22,
        (
            "#11P#1003F──初めまして。\x01",
            "特務支援課のセルゲイです。\x02\x03",

            "#1000Fそれで……\x01",
            "何とかできるというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x25,
        (
            "#6P#2804Fガレージに私のリムジンがある。\x02\x03",

            "#2800F防弾だし、かなりの速度だから\x01",
            "強行突破には打って付けだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x22,
        "#11P#1005Fほう……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x23,
        "#11P#0602F#N確かにそれなら……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0215
    ChrTalk(
        0x21,
        (
            "#1403F#11Pならば、乗り込むメンバーを\x01",
            "選ぶ必要がありそうですね。\x02\x03",

            "#1400Fここの守りも必要でしょうし、\x01",
            "私の他には……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Fade(500)
    OP_68(680, 1100, -11430, 0)
    MoveCamera(123, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    #C0216
    ChrTalk(
        0x101,
        (
            "#11P#0003F……いえ。\x02\x03",

            "#0001Fどうかここは俺たちに\x01",
            "行かせてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_9E8C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9E8C)
    Sleep(50)

    def lambda_9E9C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9E9C)
    Sleep(50)

    def lambda_9EAC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_9EAC)

    #C0217
    ChrTalk(
        0x21,
        "#11P#1405Fなに……？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x23,
        "#11P#0605Fい、いきなり何を！？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x22,
        "#5P#1001Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#11P#0006F……ヨアヒムの狙いは\x01",
            "恐らくキーアただ一人です。\x02\x03",

            "#0008Fキーアを奪われたら\x01",
            "その時点で俺たちの負けですが……\x02\x03",

            "#0000F逆に言えば、キーアを守り抜いて\x01",
            "彼を逮捕できれば俺たちの勝ちです。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        (
            "#11P#0304Fその意味じゃ、このビルは\x01",
            "絶対に守りきる必要がある……\x02\x03",

            "#0300F確実な戦力を残すべきだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        (
            "#0104F#11P恐らくアリオスさんが残れば、\x01",
            "ここは鉄壁の守りになるはず……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x103,
        (
            "#6P#0202F#11P課長たちと警官隊の応援があれば\x01",
            "完全に死角も無くなるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x21,
        "#11P#1404F……なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x23,
        "#11P#0601Fり、理屈は分かるが……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x22,
        "#5P#1006F──駄目だな。\x02",
    )

    CloseMessageWindow()
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

    def lambda_A19E():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A19E)
    Sleep(50)

    def lambda_A1AE():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A1AE)

    def lambda_A1BB():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A1BB)

    def lambda_A1C8():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A1C8)
    WaitChrThread(0x104, 2)

    #C0227
    ChrTalk(
        0x101,
        "#6P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x22,
        (
            "#5P#1003F肝心なことを忘れているぞ。\x02\x03",

            "#1001Fお前らの中で、車の運転が\x01",
            "出来るヤツはいないだろうが。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#6P#0011Fあ……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        "#12P#0106Fそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x23,
        "#11P#0607Fならば、ここは私が──\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x22,
        (
            "#5P#1003Fいや、お前には警官隊の指揮と\x01",
            "アリオスのサポートを頼む。\x02\x03",

            "#1002Fここは俺が行かせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
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

    #C0233
    ChrTalk(
        0x102,
        "#12P#0105Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#12P#0305F課長……\x01",
            "車の運転なんて出来たのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x22,
        (
            "#5P#1004Fこれでも警察学校じゃ、\x01",
            "車両運転の教官も兼任していた。\x02\x03",

            "#1002Fまあ、任せておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        "#12P#0202F意外な経歴ですね……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#6P#0000F……助かります。\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x20)

    #C0238
    ChrTalk(
        0x20,
        (
            "#12P#1112Fロイドたち……\x01",
            "……行っちゃうの……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A535():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A535)
    Sleep(50)

    def lambda_A545():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A545)

    def lambda_A552():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A552)

    def lambda_A55F():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A55F)
    Sleep(300)

    #C0239
    ChrTalk(
        0x101,
        (
            "#0004F#5Pああ……でも大丈夫だ。\x02\x03",

            "#0002F絶対にキーアのところに\x01",
            "みんなで戻ってくるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#5P#0109Fええ……もちろんよ。\x02\x03",

            "#0102F戻ってきたらまた\x01",
            "料理を手伝ってちょうだいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x20,
        "#12P#1110Fあ……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#11P#0202F確かにキーアが手伝ってくれたら\x01",
            "魔法みたいに美味しくなりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#11P#0309Fだったらいっそ、\x01",
            "派手にパーティでもやろうぜ。\x02\x03",

            "知ってる連中全員、\x01",
            "支援課に集めまくってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#0009F#5Pはは……それもいいな。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(15000, 1200)
    OP_68(270, 1100, -11520, 1200)

    def lambda_A736():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A736)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_6F(0x10)
    Fade(250)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x2)
    SetChrChipByIndex(0x20, 0x31)
    SetChrSubChip(0x20, 0x8)
    OP_0D()
    Sound(910, 0, 100, 0)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x20, 0xA)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x20, 0x8)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x20, 0xA)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x20, 0x8)
    Sleep(130)
    BeginChrThread(0x101, 3, 0, 47)
    Sleep(500)

    #C0245
    ChrTalk(
        0x101,
        (
            "#0006F#5P……キーア。\x01",
            "本当は心細かったんだな。\x02\x03",

            "#0008F昔のことを覚えてなくて\x01",
            "自分が誰かも判らなくて……\x02\x03",

            "#0001Fゴメンな、気付いてやれなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x20,
        "#12P#1112F#40Wロイド……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    EndChrThread(0x101, 0x3)
    Sound(804, 0, 100, 0)
    SetChrSubChip(0x101, 0x3)
    SetChrSubChip(0x20, 0xB)
    Sleep(100)
    SetChrSubChip(0x101, 0x4)
    SetChrSubChip(0x20, 0xC)
    Sleep(100)
    SetChrSubChip(0x101, 0x5)
    SetChrSubChip(0x20, 0xD)
    Sleep(500)

    #C0247
    ChrTalk(
        0x20,
        (
            "#12P#1106F#30W……うん、何だかちょっとずつ、\x01",
            "胸がモヤモヤしてきちゃって……\x02\x03",

            "#1104Fでも……ロイドたちがいてくれて\x01",
            "ゼンゼン寂しくなかったよ……\x02\x03",

            "#1108F……だから……だからね……！\x02\x03",

            "#1112Fゼッタイに無事に戻ってきて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        "#0002F#5Pああ……約束だ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_CA(0x1, 0xFF, 0x0)
    OP_E3(0xA)
    OP_29(0x4E, 0x1, 0x2)
    OP_29(0x4E, 0x4, 0x10)
    OP_E3(0x3)
    OP_E3(0xB)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 2)
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_81DF end

    def Function_47_AA64(): pass

    label("Function_47_AA64")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAA0")
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x20, 0xA)
    Sleep(130)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x20, 0x9)
    Sleep(130)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x20, 0x8)
    Sleep(130)
    Jump("Function_47_AA64")

    label("loc_AAA0")

    Return()

    # Function_47_AA64 end

    SaveToFile()

Try(main)
