from ZeroScenarioHelper import *

def main():
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
        "警备队员",               # 1
        "警备队员",               # 2
        "警备队员",               # 3
        "警备队员",               # 4
        "警备队员",               # 5
        "警备队员",               # 6
        "警备队员",               # 7
        "警备队员",               # 8
        "警备队员",               # 9
        "警备队员",               # 10
        "警备队员",               # 11
        "警备队员",               # 12
        "警备队员",               # 13
        "警备队员",               # 14
        "警备队员",               # 15
        "警备队员",               # 16
        "基约姆师傅",             # 17
        "警备员汪古",             # 18
        "警备员珀尔",             # 19
        "曹",                     # 20
        "刘",                     # 21
        "格蕾丝",                 # 22
        "雷因兹",                 # 23
        "雷克特",                 # 24
        "琪雅",                   # 25
        "亚里欧斯",               # 26
        "赛尔盖科长",             # 27
        "达德利搜查官",           # 28
        "蔡特",                   # 29
        "迪塔总裁",               # 30
        "玛丽亚贝尔",             # 31
        "滴",                     # 32
        "炸弹",                   # 33
        "炸弹",                   # 34
        "SE控制",                 # 35
        "BC130b",                 # 36
        "BC130b",                 # 37
        "BC130b",                 # 38
        "BC130b",                 # 39
        "BC130b",                 # 40
        "BC130b",                 # 41
        "中央广场",               # 42
        "西街",                   # 43
        "行政区",                 # 44
        "住宅街",                 # 45
        "欢乐街",                 # 46
        "东街",                   # 47
        "旧城区",                 # 48
        "港湾区",                 # 49
        "ＩＢＣ",                 # 50
        "站前街道",               # 51
        "后巷",                   # 52
        "乌尔斯拉间道",           # 53
        "东克洛斯贝尔街道",       # 54
        "西克洛斯贝尔街道",       # 55
        "玛因兹山道",             # 56
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

    PlaceName(-133.72000122070312, 0.0, -187.47999572753906, 0x0000, 0x0000, "中央广场")
    PlaceName(-223.1999969482422, 0.0, -181.35000610351562, 0x0000, 0x0000, "西街")
    PlaceName(-96.97000122070312, 0.0, -66.3499984741211, 0x0000, 0x0000, "行政区")
    PlaceName(-306.2300109863281, 0.0, -79.95999908447266, 0x0000, 0x0000, "住宅街")
    PlaceName(-206.8699951171875, 0.0, -90.8499984741211, 0x0000, 0x0000, "欢乐街")
    PlaceName(-23.139999389648438, 0.0, -218.77999877929688, 0x0000, 0x0000, "东街")
    PlaceName(25.18000030517578, 0.0, -293.6400146484375, 0x0000, 0x0000, "旧城区")
    PlaceName(14.970000267028809, 0.0, -128.9499969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-20.420000076293945, 0.0, -1.0199999809265137, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-118.41000366210938, 0.0, -281.3900146484375, 0x0000, 0x0000, "站前街道")
    PlaceName(-182.3699951171875, 0.0, -139.83999633789062, 0x0000, 0x0000, "后巷")
    PlaceName(-122.48999786376953, 0.0, -323.5799865722656, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(50.36000061035156, 0.0, -199.72999572753906, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-292.6199951171875, 0.0, -183.38999938964844, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-284.45001220703125, 0.0, -47.290000915527344, 0x0000, 0x0000, "玛因兹山道")
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
        "Function_9_1B48",         # 09, 9
        "Function_10_1BAC",        # 0A, 10
        "Function_11_1C48",        # 0B, 11
        "Function_12_1CE8",        # 0C, 12
        "Function_13_1DA4",        # 0D, 13
        "Function_14_1E2F",        # 0E, 14
        "Function_15_1EBA",        # 0F, 15
        "Function_16_2248",        # 10, 16
        "Function_17_286A",        # 11, 17
        "Function_18_2EE2",        # 12, 18
        "Function_19_2FD8",        # 13, 19
        "Function_20_31DB",        # 14, 20
        "Function_21_3A95",        # 15, 21
        "Function_22_6F9B",        # 16, 22
        "Function_23_707C",        # 17, 23
        "Function_24_7156",        # 18, 24
        "Function_25_7194",        # 19, 25
        "Function_26_71C9",        # 1A, 26
        "Function_27_7A0C",        # 1B, 27
        "Function_28_7AA6",        # 1C, 28
        "Function_29_7B40",        # 1D, 29
        "Function_30_7B98",        # 1E, 30
        "Function_31_7BF0",        # 1F, 31
        "Function_32_7C48",        # 20, 32
        "Function_33_7CA0",        # 21, 33
        "Function_34_7CF8",        # 22, 34
        "Function_35_7D50",        # 23, 35
        "Function_36_7DA8",        # 24, 36
        "Function_37_7E26",        # 25, 37
        "Function_38_7E5B",        # 26, 38
        "Function_39_7E8A",        # 27, 39
        "Function_40_7EBF",        # 28, 40
        "Function_41_7EEE",        # 29, 41
        "Function_42_7F1D",        # 2A, 42
        "Function_43_7F4C",        # 2B, 43
        "Function_44_7F7B",        # 2C, 44
        "Function_45_7FAA",        # 2D, 45
        "Function_46_7FED",        # 2E, 46
        "Function_47_A676",        # 2F, 47
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
            "#1K同日，２２：００──\x02",
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
        "众警备员",
        "#5P#N噢噢……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0003
    ChrTalk(
        0x18,
        "#5P干得不错嘛！\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#5P#0013F好……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#11P#0301F不要大意啊！\x01",
            "下一批敌人马上就会来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#11P#0207F炸弹还未启动……！\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#5P#0107F请立即搬运到里面，\x01",
            "进行拆除工作！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x18,
        "#5P交给我们吧！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x19,
        "#2P开始搬吧！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0010
    ChrTalk(
        0x1A,
        "#1P嘿……！\x02",
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
        "#0007F来了吗……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#0307F阻止他们！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, -27000, 2000)
    MoveCamera(37, 17, 0, 2000)
    SetCameraDistance(15500, 2000)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x0)

    def lambda_1AC3():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AC3)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_1AE8():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AE8)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_1B0A():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1B0A)
    OP_6F(0x79)
    Battle("BattleInfo_8D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    Return()

    # Function_8_14F4 end

    def Function_9_1B48(): pass

    label("Function_9_1B48")


    def lambda_1B4D():
        OP_95(0xFE, -1500, 0, -21900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1B4D)
    WaitChrThread(0x18, 1)
    OP_93(0x18, 0x5A, 0x1F4)

    def lambda_1B72():
        OP_96(0xFE, 0xFFFFFA24, 0x0, 0xFFFFD184, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1B72)

    def lambda_1B8C():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFD24C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1B8C)
    Sound(964, 0, 100, 0)
    WaitChrThread(0x18, 1)
    Return()

    # Function_9_1B48 end

    def Function_10_1BAC(): pass

    label("Function_10_1BAC")

    Sleep(100)

    def lambda_1BB4():
        OP_95(0xFE, 1400, 0, -21900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BB4)
    Sleep(300)

    def lambda_1BD1():
        OP_95(0xFE, 700, 0, -20900, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1BD1)
    WaitChrThread(0x19, 1)
    OP_93(0x19, 0x10E, 0x1F4)
    WaitChrThread(0x1A, 1)

    def lambda_1BFA():
        OP_96(0xFE, 0x578, 0x0, 0xFFFFD184, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1BFA)

    def lambda_1C14():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFD56C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1C14)

    def lambda_1C2E():
        OP_96(0xFE, 0x2BC, 0x0, 0xFFFFD24C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_1C2E)
    WaitChrThread(0x19, 1)
    Return()

    # Function_10_1BAC end

    def Function_11_1C48(): pass

    label("Function_11_1C48")

    Sound(1011, 255, 100, 0)    #voice#Lloyd
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x1)

    def lambda_1C65():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFF96EC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C65)
    WaitChrThread(0x101, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x9, 3, 0, 14)
    Sleep(400)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x2)
    Sound(814, 0, 100, 0)

    def lambda_1CAB():
        OP_9D(0xFE, 0xFFFFFCE0, 0x0, 0xFFFF9C64, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CAB)
    WaitChrThread(0x101, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x9, 3)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Return()

    # Function_11_1C48 end

    def Function_12_1CE8(): pass

    label("Function_12_1CE8")

    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    Sleep(150)
    SetChrSubChip(0x104, 0x1)

    def lambda_1D06():
        OP_96(0xFE, 0x384, 0x0, 0xFFFF96EC, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D06)
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

    def lambda_1D67():
        OP_9D(0xFE, 0x320, 0x0, 0xFFFF9E58, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D67)
    WaitChrThread(0x104, 1)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x1000)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Return()

    # Function_12_1CE8 end

    def Function_13_1DA4(): pass

    label("Function_13_1DA4")

    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x4)
    Sound(246, 0, 100, 0)

    def lambda_1DF5():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1DF5)

    def lambda_1E0E():
        OP_9C(0xFE, 0x1F4, 0x0, 0xFFFFE890, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E0E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    Return()

    # Function_13_1DA4 end

    def Function_14_1E2F(): pass

    label("Function_14_1E2F")

    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    Sound(246, 0, 100, 0)

    def lambda_1E80():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E80)

    def lambda_1E99():
        OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFE890, 0xC8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1E99)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Return()

    # Function_14_1E2F end

    def Function_15_1EBA(): pass

    label("Function_15_1EBA")

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
        "#5P#0000F好，这样一来──\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x103,
        "#0207F#11P第二波增援要来了！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        "#5P#0010F唔……\x02",
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

    def lambda_219D():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_219D)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)

    def lambda_21BF():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21BF)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_21E4():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21E4)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_2206():
        OP_98(0xFE, 0x0, 0x0, 0x4E20, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2206)
    OP_6F(0x79)
    Battle("BattleInfo_91C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    Return()

    # Function_15_1EBA end

    def Function_16_2248(): pass

    label("Function_16_2248")

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
            "#5P#0013F可恶，在这种连绵不绝的攻势下，\x01",
            "我们就连撤回去的机会都没有……！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0101F#5P无论如何，我们都要争取到\x01",
            "将大门关闭的时间……！\x02",
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
            "#11P#3209F呵呵……很努力嘛。\x02\x03",

            "#3202F根据『银』大人的报告来判断，\x01",
            "我们这次似乎也只能老老实实地\x01",
            "退避旁观了……\x02\x03",

            "不过，好像能欣赏到一场出乎意料的精彩大戏呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x1B, 500)
    Sleep(300)

    #C0019
    ChrTalk(
        0x1C,
        (
            "#11P可、可是，曹先生，\x01",
            "这样下去，终究会……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1B,
        (
            "#11P#3204F如果在此地倒下，\x01",
            "那说明他们的实力终究\x01",
            "不过如此而已，难成大器──\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x10E, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0x1B,
        "#11P#3210F看啊，下一批已经来了哦。\x02",
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

    def lambda_2781():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2781)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)

    def lambda_27A6():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_27A6)
    SetChrChipByIndex(0x12, 0x2B)
    SetChrSubChip(0x12, 0x0)

    def lambda_27C8():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_27C8)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_27ED():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27ED)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_280F():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_280F)
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

    # Function_16_2248 end

    def Function_17_286A(): pass

    label("Function_17_286A")

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
            "#5P#0208F如果敌人保持这种攻势的话，\x01",
            "恐怕连大门都……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#5P#0007F是啊……！\x01",
            "所以无论如何也要在此拦下他们！\x02",
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
            "#5P格、格蕾丝前辈……\x01",
            "究竟发生了什么事啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x1D,
        (
            "#6P#2101F别管那么多，好好拍摄就行了！\x02\x03",

            "对于只有笔和相机作为武器的我们\x01",
            "而言，这就是唯一能做到的战斗哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1E)

    #C0026
    ChrTalk(
        0x1E,
        "#5P是、是的……！\x02",
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
            "#6P#2103F（罗伊德，各位……\x01",
            "  我一定会为你们写出最精彩的报道。）\x02\x03",

            "#2101F（所以，绝对要活下来啊……\x01",
            "  然后亲眼在杂志上见证到自己的活跃！）\x02",
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

    def lambda_2DC7():
        OP_96(0xFE, 0x0, 0xFFFFF95C, 0xFFFF7748, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2DC7)
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

    def lambda_2E77():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2E77)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_2E99():
        OP_98(0xFE, 0x1F4, 0x0, 0x7530, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2E99)
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

    # Function_17_286A end

    def Function_18_2EE2(): pass

    label("Function_18_2EE2")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)

    label("loc_2F1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FD7")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F4D")
    Sleep(500)
    Jump("loc_2F95")

    label("loc_2F4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F64")
    Sleep(1500)
    Jump("loc_2F95")

    label("loc_2F64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F7B")
    Sleep(2000)
    Jump("loc_2F95")

    label("loc_2F7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F92")
    Sleep(3000)
    Jump("loc_2F95")

    label("loc_2F92")

    Sleep(4000)

    label("loc_2F95")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Jump("loc_2F1F")

    label("loc_2FD7")

    Return()

    # Function_18_2EE2 end

    def Function_19_2FD8(): pass

    label("Function_19_2FD8")

    Sleep(400)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    Sound(854, 0, 100, 0)

    def lambda_2FF3():
        OP_9D(0xFE, 0x10CC, 0xFFFFF7CC, 0xFFFF6488, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2FF3)
    SetChrChipByIndex(0x10, 0x2B)
    SetChrSubChip(0x11, 0x2)
    SetChrFlags(0x11, 0x20)

    def lambda_301D():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFF7CC, 0xFFFF6488, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_301D)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_304E():
        OP_9D(0xFE, 0x10CC, 0xFFFFFAEC, 0xFFFF7428, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_304E)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_3079():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFFAEC, 0xFFFF7428, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3079)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_30AA():
        OP_9D(0xFE, 0x10CC, 0xFFFFFE0C, 0xFFFF83C8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_30AA)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_30D5():
        OP_9D(0xFE, 0xFFFFEF34, 0xFFFFFE0C, 0xFFFF83C8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_30D5)
    WaitChrThread(0x10, 1)
    SetChrSubChip(0x10, 0x4)
    Sound(925, 0, 100, 0)
    Sound(55, 0, 100, 0)

    def lambda_3106():
        OP_9D(0xFE, 0x10CC, 0x320, 0xFFFF9368, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3106)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x11, 0x4)
    Sound(814, 0, 100, 0)

    def lambda_3131():
        OP_9D(0xFE, 0xFFFFEF34, 0x320, 0xFFFF9368, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3131)
    WaitChrThread(0x10, 1)
    Sleep(100)
    SetChrChipByIndex(0x10, 0x29)
    SetChrSubChip(0x10, 0x1)

    def lambda_315D():
        OP_93(0xFE, 0x13B, 0x2BC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_315D)
    Sound(854, 0, 100, 0)
    Sound(925, 0, 100, 0)

    def lambda_3176():
        OP_9D(0xFE, 0x708, 0x0, 0xFFFF9A70, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3176)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x1)

    def lambda_319F():
        OP_93(0xFE, 0x2D, 0x2BC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_319F)

    def lambda_31AC():
        OP_9D(0xFE, 0xFFFFF8F8, 0x0, 0xFFFF9A70, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_31AC)
    Sleep(300)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x11, 0x2)
    Sleep(100)
    SetChrSubChip(0x10, 0x3)
    SetChrSubChip(0x11, 0x3)
    Return()

    # Function_19_2FD8 end

    def Function_20_31DB(): pass

    label("Function_20_31DB")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x1)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3578")

    #C0028
    ChrTalk(
        0x101,
        "#0010F#5P刚、刚刚的是米蕾优准尉……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#0106F#5P怎么会，连准尉都……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#0201F#5P！！　兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0310F#5P混蛋……\x01",
            "开什么玩笑啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360F")

    label("loc_3578")


    #C0032
    ChrTalk(
        0x104,
        "#0308F#5P呜……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#5P#0013F刚才那个女性队员……　\x01",
            "是兰迪的旧识吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        (
            "#0303F#5P是啊……是我曾经的同事……\x02\x03",

            "#0310F混蛋……\x01",
            "开什么玩笑啊……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360F")

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
            "#5P#3502F哎呀呀，真是很努力啊。\x02\x03",

            "#3506F不过，\x01",
            "这样下去的话，似乎就正中\x01",
            "吉利亚斯大叔的下怀了呢。\x02\x03",

            "#3510F嗯～该怎么办好呢～\x02",
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
            "#5P#3505F啊呀呀……\x01",
            "下一场大概就是他们的极限了吧。\x02\x03",

            "#3504F算啦，总之就尽量加油吧～\x02",
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

    def lambda_392B():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_392B)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x20)

    def lambda_3952():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3952)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x2A)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x20)

    def lambda_397C():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_397C)
    SetChrChipByIndex(0x12, 0x2A)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x20)

    def lambda_39A3():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_39A3)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)

    def lambda_39C5():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_39C5)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)

    def lambda_39E7():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39E7)
    Sleep(50)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)

    def lambda_3A0C():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A0C)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)

    def lambda_3A2E():
        OP_98(0xFE, 0x0, 0x0, 0x7530, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3A2E)
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

    # Function_20_31DB end

    def Function_21_3A95(): pass

    label("Function_21_3A95")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404B")

    #C0039
    ChrTalk(
        0x101,
        "#5P#0010F#N#40W唔……\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#5P#0301F#N#40W可恶……\x01",
            "数量也未免太多了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_419D")

    label("loc_404B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AA")

    #C0041
    ChrTalk(
        0x101,
        "#5P#0010F#N#40W……唔啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#5P#0206F#N#40W已、已经到极限了……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_419D")

    label("loc_40AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4115")

    #C0043
    ChrTalk(
        0x101,
        "#5P#0008F#N#40W……不、不行了吗……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#5P#0106F#N#40W竟、竟然会在这种地方……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_419D")

    label("loc_4115")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4164")

    #C0045
    ChrTalk(
        0x101,
        (
            "#5P#0008F#N#40W……唔……\x01",
            "（怎么可以在这里倒下……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_419D")

    label("loc_4164")


    #C0046
    ChrTalk(
        0x101,
        (
            "#5P#0006F#N#40W……唔……\x01",
            "（只能撑到这里了吗……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_419D")

    Sleep(300)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    #Sound(1957, 255, 100, 0)    #voice#Joachim
    Sleep(1000)

    #N0047
    NpcTalk(
        0x13,
        "男人的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "呵呵……\x01",
            "你们似乎很是拼命啊。\x02",
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

    def lambda_42A4():
        OP_96(0xFE, 0x0, 0x0, 0xFFFF9B9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_42A4)
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
            "#5P#0307F#5P罗金斯！？\x01",
            "为什么你会──\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P啊啊，兰迪，\x01",
            "你可不要误会了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P『我』并不是你的前同事。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x13,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P只是借用一下他的身体，\x01",
            "用这种形式来与你们进行对话而已。\x07\x00\x02",
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
        "#5P#0101F那个声音……！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x103,
        "#5P#0205F难、难道是……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#5P#0013F约亚西姆医生……！？\x02",
    )

    CloseMessageWindow()

    #N0056
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P呵呵，答对啦。\x02",
        )
    )

    CloseMessageWindow()

    #N0057
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P我发出的邀请函，\x01",
            "你们似乎已经过目了吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0058
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P阿奈斯特也\x01",
            "算是起到作用了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0310F你这混蛋……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#5P#0108F你究竟，有什么目的……\x02\x03",

            "#0110F竟然做出这种事情……\x01",
            "让整个克洛斯贝尔陷入混乱……！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#5P#0007F你到底……你们『Ｄ∴Ｇ教团』\x01",
            "到底有何企图……！？\x02",
        )
    )

    CloseMessageWindow()

    #N0062
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P哈哈，如果想知道这些，\x01",
            "唯一的方法就是成为我们的同伴了。\x02",
        )
    )

    CloseMessageWindow()

    #N0063
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P只要服下『真知』，\x01",
            "我就可以将你们引领至那种境界哦。\x02",
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
            "#5P#0207F别、别开玩笑了……！\x02\x03",

            "#0210F#30W……你……\x01",
            "你做了那样残酷的事情……！\x02",
        )
    )

    CloseMessageWindow()

    #N0065
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P呵呵，各据点的仪式并不是\x01",
            "由我来负责的哦。\x02",
        )
    )

    CloseMessageWindow()

    #N0066
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P当然，『真知』原型的\x01",
            "实验资料是由我回收的。\x02",
        )
    )

    CloseMessageWindow()

    #N0067
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P以那些资料为基础，我才在\x01",
            "这个古老的圣地将『真知』完成……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0068
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P#4S没错，这一切全部都是命运啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0013F你、你在……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        "#5P#0301F莫名其妙地说些什么啊……\x02",
    )

    CloseMessageWindow()

    #N0071
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P哼哼……\x01",
            "我也没打算让你们这些『无法达到\x01",
            "那种境界』的人真正理解。\x02",
        )
    )

    CloseMessageWindow()

    #N0072
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P我们的要求只有一个。\x02",
        )
    )

    CloseMessageWindow()

    #N0073
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P请将那位大人──将琪雅大人\x01",
            "交还给我，仅此而已。\x02",
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
            "#5P#0105F那、那位大人……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#5P#0201F……琪雅……大人……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#5P#0013F你……\x01",
            "你打算对那孩子做什么！？\x02",
        )
    )

    CloseMessageWindow()

    #N0077
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P请不要误会。\x02",
        )
    )

    CloseMessageWindow()

    #N0078
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P琪雅大人原本就是我们的『圣子』。\x02",
        )
    )

    CloseMessageWindow()

    #N0079
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P她会暂时留在你们的身边，\x01",
            "不过只是个单纯的偶然罢了。\x02",
        )
    )

    CloseMessageWindow()

    #N0080
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P我想做的，仅仅是请那位大人\x01",
            "回到她该去的地方而已。\x02",
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
            "#5P#0010F别开玩笑了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_4B7E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B7E)
    Fade(500)
    SetChrChipByIndex(0x101, 0x14)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 80, 0)
    OP_0D()

    def lambda_4BB1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4BB1)

    def lambda_4BCA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4BCA)

    def lambda_4BE3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4BE3)
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
            "#0007F#5P你难道想把那个孩子……\x01",
            "也卷进你们的邪教里吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x102,
        (
            "#0110F#5P从刚才开始，你所说的……\x01",
            "……全都是充满妄想的胡言乱语……！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#5P#0307F我们怎么可能让阿琪\x01",
            "回到你这种变态混蛋的身边……！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        "#0201F#5P收起你的妄想滚回去吧……就这样……！\x02",
    )

    CloseMessageWindow()

    #N0086
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P哎呀呀……交涉决裂了吗？\x02",
        )
    )

    CloseMessageWindow()

    #N0087
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P既然如此，我就只有跨过你们的尸体，\x01",
            "然后恭迎琪雅大人回归了。\x02",
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

    def lambda_4DF9():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4DF9)
    ClearChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_4E20():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4E20)
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
            "#0010F#5P唔……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#5P#0312F哈……口气还真大嘛……\x02",
    )

    CloseMessageWindow()

    #N0090
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P哼哼，已经向你们那所谓的\x01",
            "女神祈祷完毕了吗……？\x02",
        )
    )

    CloseMessageWindow()

    #N0091
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P那么，准备受死吧──\x02",
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

    def lambda_5116():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFAA10, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_5116)
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
        "#0007F#5P琪、琪雅……！？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        "#0107F#5P#N怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #N0094
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P噢噢，琪雅大人……\x02",
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
            "#5P#1107F不许你欺负罗伊德他们！\x02\x03",

            "如果你敢欺负他们，\x01",
            "琪雅绝对不会原谅你的！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        (
            "#0307F#11P阿琪……！\x01",
            "听话，赶快退后！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x103,
        "#0207F#11P#N不可以到前面来……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #N0098
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P琪雅大人，\x01",
            "我来迎接您了。\x02",
        )
    )

    CloseMessageWindow()

    #N0099
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P请抛弃那些愚蠢的家伙，\x01",
            "回到我们的身边吧。\x02",
        )
    )

    CloseMessageWindow()

    #N0100
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P您现在还什么都不明白呢，\x01",
            "其实您是我们的──\x02",
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
            "够了，别再多说，\x01",
            "马上答应我……！\x02\x03",

            "不要再对罗伊德他们\x01",
            "做出过分的事……！\x07\x00\x02",
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

    def lambda_5464():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5464)
    Sleep(50)

    def lambda_5480():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5480)

    def lambda_5499():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5499)

    def lambda_54B2():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_54B2)
    Sleep(50)

    def lambda_54CE():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_54CE)

    def lambda_54E7():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_54E7)
    Sleep(50)

    def lambda_5503():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5503)

    def lambda_551C():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_551C)
    Sleep(300)

    #N0102
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#5P哎……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#0105F#5P#N小、小琪雅……？\x02",
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
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P呵呵……哈哈哈……\x02",
        )
    )

    CloseMessageWindow()

    #N0107
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P……这正是……！\x01",
            "这正是我们的圣子啊……唔！\x02",
        )
    )

    CloseMessageWindow()

    #N0108
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P那么，谨遵圣子意愿。\x02",
        )
    )

    CloseMessageWindow()

    #N0109
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P只要琪雅大人您能回来，\x01",
            "我便绝对不会再加害于他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#1119F……是真的吗？\x02\x03",

            "不会再对他们做过分的事了？\x02",
        )
    )

    CloseMessageWindow()

    #N0111
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P嗯，那是自然。\x02",
        )
    )

    CloseMessageWindow()

    #N0112
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P那么……请您到这边来。\x02",
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
            "#0007F#5P不行啊……！\x02",
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

    def lambda_57C8():
        OP_96(0xFE, 0xFFFFFC7C, 0x0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57C8)
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
            "#1117F#11P罗伊德……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0010F琪雅……\x01",
            "你很害怕『黑暗』吧！？\x02\x03",

            "如果从我们的身边离开，\x01",
            "你会很寂寞，很难过的吧……！？\x02\x03",

            "所以，绝对不要听信\x01",
            "这种家伙说的话啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1119F#11P#30W……可、可是……\x02\x03",

            "#1118F琪雅……没有记忆……\x02\x03",

            "连、连自己是谁都不知道……\x02\x03",

            "#1120F如果总是像这样给罗伊德和大家添麻烦，\x01",
            "……是、是不能在一起的……！\x02",
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
            "#5P#0007F根本就没添什么麻烦……！\x02\x03",

            "#0000F是我──是我们希望琪雅\x01",
            "能陪在我们身边的啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1117F#11P………哎……………\x02",
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
            "#5P#0104F我想，我们几个……\x01",
            "正是因为有琪雅在身边，\x01",
            "才在真正意义上成长了起来……\x02\x03",

            "#0102F就在默默守护你……陪伴你\x01",
            "的过程中，才逐渐找到了\x01",
            "各自所追寻的人生意义……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    #C0120
    ChrTalk(
        0x103,
        (
            "#5P#0204F是啊……\x02\x03",

            "#0208F……虽然我至今连自己为何而活\x01",
            "也还不明白……\x02\x03",

            "#0214F但只要是为了与大家一起守护琪雅，\x01",
            "我就觉得自己什么都能做到……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)

    #C0121
    ChrTalk(
        0x104,
        (
            "#0300F#5P所以啊，阿琪……\x01",
            "不要再担心那些多余的事啦。\x02\x03",

            "你只要开开心心地欢笑，\x01",
            "轻松茁壮地成长就好。\x02\x03",

            "#0309F只需这样，就能\x01",
            "让我们充满力量啦……！\x02",
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
            "#6P#1119F#40W……艾莉……\x01",
            "缇欧……兰迪……\x02",
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

    def lambda_5C7D():
        OP_92(0xFE, 0xA28, 0xFFFFC43C, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5C7D)
    Sound(814, 0, 90, 0)

    def lambda_5C96():
        OP_9D(0xFE, 0xA28, 0x0, 0xFFFFC43C, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5C96)
    WaitChrThread(0x24, 1)
    Sound(832, 0, 100, 0)

    def lambda_5CBD():
        OP_92(0xFE, 0xFFFFF5D8, 0xFFFFA8E4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5CBD)
    SetChrSubChip(0x24, 0x1)
    Sleep(50)
    SetChrSubChip(0x24, 0x2)
    Sleep(50)
    SetChrSubChip(0x24, 0x3)
    Sleep(50)
    SetChrSubChip(0x24, 0x0)
    Sleep(50)
    Sound(854, 0, 90, 0)

    def lambda_5CF2():
        OP_9D(0xFE, 0xFFFFF5D8, 0x0, 0xFFFFA8E4, 0x6A4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_5CF2)
    WaitChrThread(0x24, 1)
    Sound(832, 0, 100, 0)
    SetChrSubChip(0x24, 0x1)
    Sleep(50)
    SetChrSubChip(0x24, 0x2)
    Sleep(50)
    SetChrSubChip(0x24, 0x3)
    Sleep(50)

    def lambda_5D2E():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5D2E)
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
            "#6P#1200F呜噜噜噜……\x02",
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
            "#1116F#11P#40W连蔡特也……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0004F我们是搜查官。\x02\x03",

            "如果你很在意自己的过去和记忆，\x01",
            "我们可以帮你一起找回来……\x02\x03",

            "#0008F再怎么说，也没有必要\x01",
            "接受这种家伙的条件。\x02\x03",

            "#0001F所以，琪雅……不要离开。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x20,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#1116F#11P#40W……罗伊德………\x02",
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
            "#1104F#11P#40W…………嗯。\x02\x03",

            "#1102F琪雅，要和大家在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#5P#0002F是吗……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#5P#0102F小琪雅……\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, -23700, 1500)
    OP_6F(0x1)
    #Sound(1956, 255, 100, 0)    #voice#Joachim
    Sleep(150)

    #N0130
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P哼哼……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    #Sound(1959, 255, 100, 0)    #voice#Joachim
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #N0131
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#4S哈哈哈哈哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F8B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_5F8B)
    Sleep(50)

    def lambda_5F9B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_5F9B)
    SetChrChipByIndex(0x24, 0x33)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x24, 2)

    def lambda_5FD5():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFB244, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_5FD5)
    Sleep(500)

    #N0132
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P竟然用如此荒唐可笑的妄语\x01",
            "来欺骗我们的圣子啊……\x02",
        )
    )

    CloseMessageWindow()

    #N0133
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P……本来是想静观其变，所以才容许圣子暂时留在\x01",
            "你们的身边。但现在看来，似乎是我失算了呢……\x02",
        )
    )

    CloseMessageWindow()

    #N0134
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P特别任务支援科……！\x01",
            "我会将你们所有人都碎尸万段！\x02",
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

    def lambda_6147():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6147)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)

    def lambda_6169():
        OP_98(0xFE, 0x0, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6169)
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
            "#0101F#5P唔……！\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#0202F#5P#N……不过……\x01",
            "我们已经稍微休息过了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0137
    ChrTalk(
        0x101,
        "#0007F#5P琪雅，退后！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)

    #C0138
    ChrTalk(
        0x104,
        (
            "#0307F#5P至少也要让阿琪一人\x01",
            "退回大门内……！\x02",
        )
    )

    CloseMessageWindow()

    #N0139
    NpcTalk(
        0x21,
        "男性的声音",
        "#1P──没有那个必要。\x02",
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
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        "#0105F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#0005F#5P……您是……！\x02",
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
        "八叶一刀流·二式『疾风』──\x02",
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
        "#5P#1407F#4S#9A斩……！\x02",
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
        "#5P#0002F亚里欧斯先生……！\x02",
    )

    CloseMessageWindow()

    def lambda_6946():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6946)
    WaitChrThread(0x13, 2)
    Sleep(300)

    #N0146
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P#40W风、风之剑圣……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0309F喂喂！\x01",
            "登场时机也太巧了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        "#5P#0202F好像是故意等到关键时刻才出手呢……！\x02",
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
            "#5P#1404F呵呵……\x01",
            "我并没有那种想法。\x02\x03",

            "#1402F顺便一说，\x01",
            "来的人并不只有我一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#5P#0005F哎……\x02",
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

    def lambda_6B89():
        OP_96(0xFE, 0x2BC, 0xFFFFEE08, 0xFFFF4868, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6B89)
    Sleep(100)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrSubChip(0x22, 0x0)

    def lambda_6BAE():
        OP_96(0xFE, 0xFFFFFD44, 0xFFFFEDA4, 0xFFFF4674, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6BAE)
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
        "#11P#0601F哼……被抢先了一步吗！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x22,
        (
            "#5P#1004F呼……\x01",
            "看来我也上年纪了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x20,
        "#1110F啊，是科长！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#0002F达德利警官也……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)

    def lambda_6C79():
        OP_96(0xFE, 0x514, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6C79)
    Sleep(50)
    SetChrChipByIndex(0x22, 0x2B)
    SetChrSubChip(0x22, 0x0)

    def lambda_6C9E():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6C9E)
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

    def lambda_6D6D():
        OP_96(0xFE, 0x514, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_6D6D)
    Sleep(50)

    def lambda_6D8A():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFF93CC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_6D8A)
    WaitChrThread(0x23, 1)
    SetChrChipByIndex(0x23, 0x2C)
    SetChrSubChip(0x23, 0x0)
    Sound(531, 0, 100, 0)
    Sound(820, 0, 100, 0)

    def lambda_6DBC():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_6DBC)
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
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#40W你、你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0309F#5P#N哈哈……\x01",
            "也太会耍帅了吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x102,
        (
            "#0102F#5P#N两位……\x01",
            "太好了，你们都平安无事……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0158
    ChrTalk(
        0x22,
        (
            "#5P#1002F所幸能在最佳时机\x01",
            "和亚里欧斯会合啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x23,
        (
            "#0602F#11P因为出现了意料之外的援军，\x01",
            "我们才能顺利赶过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#0005F#5P#N意料之外的援军……？\x02\x03",

            "#0000F……啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0161
    ChrTalk(
        0x103,
        "#0202F#5P#N那是……！\x02",
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

    # Function_21_3A95 end

    def Function_22_6F9B(): pass

    label("Function_22_6F9B")

    OP_82(0xC8, 0x0, 0xBB8, 0x96)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_7001():
        OP_9C(0xFE, 0xFFFFFC7C, 0x0, 0x9C4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7001)

    def lambda_701E():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_701E)
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

    # Function_22_6F9B end

    def Function_23_707C(): pass

    label("Function_23_707C")

    OP_82(0xC8, 0x0, 0xBB8, 0x96)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)

    def lambda_70E2():
        OP_9C(0xFE, 0x384, 0x0, 0x9C4, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_70E2)

    def lambda_70FF():
        OP_A6(0xFE, 0x32, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_70FF)
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

    # Function_23_707C end

    def Function_24_7156(): pass

    label("Function_24_7156")

    SetChrChipByIndex(0xC, 0x1D)
    SetChrSubChip(0xC, 0x0)

    def lambda_7163():
        OP_96(0xFE, 0xFFFFF7CC, 0xFFFFDB20, 0xFFFEFA48, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7163)
    Sleep(1500)
    BeginChrThread(0x14, 3, 0, 25)
    WaitChrThread(0xC, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x2)
    Return()

    # Function_24_7156 end

    def Function_25_7194(): pass

    label("Function_25_7194")

    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)

    def lambda_71A1():
        OP_96(0xFE, 0x384, 0xFFFFDEA4, 0xFFFF0920, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_71A1)
    WaitChrThread(0x14, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    Return()

    # Function_25_7194 end

    def Function_26_71C9(): pass

    label("Function_26_71C9")

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

    def lambda_7301():
        OP_96(0xFE, 0xFFFFF574, 0xFFFFDC10, 0xFFFF0024, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7301)

    def lambda_731B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0xC8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_731B)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_734F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_734F)
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

    def lambda_7425():
        OP_96(0xFE, 0x8FC, 0xFFFFDECC, 0xFFFF0BDC, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7425)

    def lambda_743F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0xC8)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_743F)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_7473():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7473)
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

    def lambda_757C():
        OP_96(0xFE, 0xFFFFF95C, 0xFFFFE4A8, 0xFFFF2540, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_757C)

    def lambda_7596():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7596)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x0)

    def lambda_75CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_75CA)
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

    def lambda_7679():
        OP_96(0xFE, 0x76C, 0xFFFFE9BC, 0xFFFF3990, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7679)

    def lambda_7693():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7693)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0x15, 3, 0, 28)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_76C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_76C7)
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

    def lambda_7776():
        OP_96(0xFE, 0xFFFFF9C0, 0xFFFFEF98, 0xFFFF522C, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7776)

    def lambda_7790():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7790)
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

    def lambda_77CD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_77CD)
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

    def lambda_787C():
        OP_96(0xFE, 0x514, 0xFFFFF5D8, 0xFFFF6B90, 0x4268, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_787C)

    def lambda_7896():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x37, 0x96)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_7896)
    Sleep(200)
    Sound(815, 0, 100, 0)
    BeginChrThread(0xF, 3, 0, 27)
    StopEffect(0x2, 0x2)
    Sleep(50)
    Sound(834, 0, 100, 0)
    SetChrChipByIndex(0x21, 0x3B)
    SetChrSubChip(0x21, 0x1)

    def lambda_78CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_78CA)
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

    def lambda_793F():
        OP_9D(0xFE, 0x0, 0x0, 0xFFFFA04C, 0x157C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_793F)
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

    def lambda_79BF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_79BF)
    PlayEffect(0x4, 0xFF, 0x21, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChip(0x1, 0x21, 0x0, 0x0)
    Sleep(100)
    OP_6F(0x79)
    Return()

    # Function_26_71C9 end

    def Function_27_7A0C(): pass

    label("Function_27_7A0C")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7A50():
        OP_A6(0xFE, 0x1E, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A50)
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

    # Function_27_7A0C end

    def Function_28_7AA6(): pass

    label("Function_28_7AA6")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_7AEA():
        OP_A6(0xFE, 0x1E, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7AEA)
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

    # Function_28_7AA6 end

    def Function_29_7B40(): pass

    label("Function_29_7B40")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7B5E():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7B5E)

    def lambda_7B77():
        OP_9C(0xFE, 0x5DC, 0xFFFFFA24, 0xFFFFE4A8, 0x44C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7B77)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_7B40 end

    def Function_30_7B98(): pass

    label("Function_30_7B98")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7BB6():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7BB6)

    def lambda_7BCF():
        OP_9C(0xFE, 0xFFFFFA24, 0xFFFFFA24, 0xFFFFE4A8, 0x44C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7BCF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_30_7B98 end

    def Function_31_7BF0(): pass

    label("Function_31_7BF0")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7C0E():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7C0E)

    def lambda_7C27():
        OP_9C(0xFE, 0xBB8, 0xFFFFE890, 0xFFFFEC78, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7C27)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_31_7BF0 end

    def Function_32_7C48(): pass

    label("Function_32_7C48")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7C66():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7C66)

    def lambda_7C7F():
        OP_9C(0xFE, 0xFFFFF448, 0xFFFFE890, 0xFFFFEC78, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7C7F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_32_7C48 end

    def Function_33_7CA0(): pass

    label("Function_33_7CA0")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7CBE():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_7CBE)

    def lambda_7CD7():
        OP_9C(0xFE, 0x1F40, 0xFFFFE890, 0xFFFFF830, 0x514, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7CD7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_33_7CA0 end

    def Function_34_7CF8(): pass

    label("Function_34_7CF8")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7D16():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7D16)

    def lambda_7D2F():
        OP_9C(0xFE, 0xFFFFE0C0, 0xFFFFE890, 0xFFFFF830, 0x514, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7D2F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_34_7CF8 end

    def Function_35_7D50(): pass

    label("Function_35_7D50")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7D6E():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7D6E)

    def lambda_7D87():
        OP_9C(0xFE, 0x0, 0xFFFFFA24, 0xFFFFE890, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7D87)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_35_7D50 end

    def Function_36_7DA8(): pass

    label("Function_36_7DA8")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))

    def lambda_7DC1():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7DC1)

    def lambda_7DDA():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7DDA)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_7DFF():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7DFF)
    SetChrChipByIndex(0xFE, 0x38)
    SetChrSubChip(0xFE, 0x0)
    Sound(514, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_36_7DA8 end

    def Function_37_7E26(): pass

    label("Function_37_7E26")

    SetChrChipByIndex(0x102, 0x30)
    SetChrSubChip(0x102, 0x0)

    def lambda_7E33():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E33)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x16)
    SetChrSubChip(0x102, 0x0)
    Return()

    # Function_37_7E26 end

    def Function_38_7E5B(): pass

    label("Function_38_7E5B")

    SetChrChipByIndex(0x103, 0x31)
    SetChrSubChip(0x103, 0x0)

    def lambda_7E68():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFAEC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E68)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x18)
    SetChrSubChip(0x103, 0x0)
    Return()

    # Function_38_7E5B end

    def Function_39_7E8A(): pass

    label("Function_39_7E8A")

    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x0)

    def lambda_7E97():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFBB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E97)
    WaitChrThread(0x104, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x1A)
    SetChrSubChip(0x104, 0x0)
    Return()

    # Function_39_7E8A end

    def Function_40_7EBF(): pass

    label("Function_40_7EBF")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_7ECC():
        OP_98(0xFE, 0x1F4, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7ECC)
    WaitChrThread(0x10, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_7EBF end

    def Function_41_7EEE(): pass

    label("Function_41_7EEE")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_7EFB():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7EFB)
    WaitChrThread(0x11, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_7EEE end

    def Function_42_7F1D(): pass

    label("Function_42_7F1D")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_7F2A():
        OP_98(0xFE, 0x514, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7F2A)
    WaitChrThread(0x12, 1)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_42_7F1D end

    def Function_43_7F4C(): pass

    label("Function_43_7F4C")

    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_7F59():
        OP_98(0xFE, 0x2BC, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F59)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_7F4C end

    def Function_44_7F7B(): pass

    label("Function_44_7F7B")

    SetChrChipByIndex(0xFE, 0x1D)
    SetChrSubChip(0xFE, 0x0)

    def lambda_7F88():
        OP_98(0xFE, 0xFFFFFD44, 0x0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7F88)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_7F7B end

    def Function_45_7FAA(): pass

    label("Function_45_7FAA")

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

    # Function_45_7FAA end

    def Function_46_7FED(): pass

    label("Function_46_7FED")

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
        "#5P#0002F那些家伙……！\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        "#5P#0202F已经完全占据了上风……！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#5P#0309F哈哈……以职业士兵为对手\x01",
            "还能有如此表现，干得不错嘛！\x02",
        )
    )

    CloseMessageWindow()

    #N0165
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P唔……\x01",
            "区区不良团伙，为什么会……\x02",
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

    def lambda_8462():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_8462)

    def lambda_846F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_846F)

    def lambda_847C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_847C)

    def lambda_8489():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8489)
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
            "#5P#0005F啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#5P#0102F直到刚才，导力通讯还\x01",
            "一直都联络不上的……！\x02",
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
            "#0001F您好，我是特别任务支援科的──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少女的声音")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "太、太好了～！\x01",
            "罗伊德警官，你没事吗！\x02\x03",

            "听到你们被警备队追击的消息后，　\x01",
            "还在想大家都怎样了……！\x02",
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
            "#0002F芙兰……你也没事吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是的……！\x01",
            "我们这边也转入反击了！\x02\x03",

            "另外，游击士们还帮忙将\x01",
            "被破坏的通讯终端\x01",
            "修复了……\x02\x03",

            "虽然功能受到了限制，\x01",
            "但导力通讯总算恢复了！\x02",
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
            "#0000F是吗……！\x02",
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
    SetChrName("少年的声音")

    #A0173
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，能顺利恢复，\x01",
            "全都多亏了我的情报啊！\x02",
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
            "#0005F这声音……是约纳吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("约纳的声音")

    #A0175
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是啊，正是我天才约纳大人！\x02\x03",

            "我顺便还与ＩＢＣ进行合作，\x01",
            "把导力网络也恢复啦！\x02\x03",

            "感激我吧！\x02",
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
            "#0014F哈哈……非常感谢！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0177
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "警队现在已经\x01",
            "前往你们那边支援了！！\x02\x03",

            "那么，我再试着和姐姐\x01",
            "那里联络一下！\x02\x03",

            "罗伊德警官，总之请小心啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("约纳的声音")

    #A0178
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "注意别死掉啊～！\x02",
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
            "#0000F嗯……！\x02",
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
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P唔……怎么会有这种荒唐事……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x21,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#1403F──就是这样。\x02",
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

    def lambda_89CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_89CA)

    def lambda_89D7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_89D7)

    def lambda_89E4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_89E4)

    def lambda_89F1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_89F1)
    SetCameraDistance(14000, 1000)

    def lambda_8A07():
        OP_96(0xFE, 0x0, 0x0, 0xFFFF9A70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8A07)
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
            "#5P#1401F『Ｄ∴Ｇ教团』的干部祭司，\x01",
            "约亚西姆·琼塔。\x02\x03",

            "我们不会容忍你继续在\x01",
            "克洛斯贝尔肆意妄为了。\x02",
        )
    )

    CloseMessageWindow()

    #N0183
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P哼哼……好啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P……我们的战斗力，\x01",
            "包括黑手党在内，接近千名……\x02",
        )
    )

    CloseMessageWindow()

    #N0185
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P而且都拥有无穷无尽的体力，\x01",
            "连睡眠都不需要……\x02",
        )
    )

    CloseMessageWindow()

    #N0186
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P反抗者一律格杀勿论，\x01",
            "我们一定会将圣子夺回的……\x02",
        )
    )

    CloseMessageWindow()

    #N0187
    NpcTalk(
        0x13,
        "约亚西姆的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P哈哈哈……！\x01",
            "你们就好好期待吧……！！！\x02",
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

    def lambda_8C74():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8C74)
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
            "#12P#0601F……完全失去意识了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        "#0013F#5P#N这、这是……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0190
    ChrTalk(
        0x103,
        (
            "#0206F#11P#N看来是在其它地方\x01",
            "进行操控的啊……\x02\x03",

            "#0201F而且……\x01",
            "那个地方可能相当远呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0191
    ChrTalk(
        0x102,
        (
            "#0101F#5P#N莫非……\x01",
            "他也是在那里操纵警备队全体队员的！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0301F#11P#N嘁……\x01",
            "也就是说，如果不打倒约亚西姆本人，\x01",
            "这个事件就永远都无法彻底收场吧！？\x02",
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
        "#5P#1404F──已经发现他的藏身之处了。\x02",
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
        "#0011F#5P#N哎……\x02",
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

    def lambda_8FA9():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFA1DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8FA9)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)
    Sleep(300)

    #C0195
    ChrTalk(
        0x21,
        (
            "#11P#1403F发现『教团』据点的是\x01",
            "艾丝蒂尔和约修亚。\x02\x03",

            "#1401F具体位置是位于克洛斯贝尔\x01",
            "东北方向的『阿尔摩利卡古战场』──\x02\x03",

            "据说是在那里发现了\x01",
            "失踪者们进入的痕迹。\x02\x03",

            "#1403F而他们现在正在\x01",
            "调查潜入内部的路线。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#0013F#5P古战场……竟然在那种地方！\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        (
            "#0101F#5P那个遗迹里确实\x01",
            "像是有很多谜团……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        "#5P#0300F那么，只要将那里捣毁……！\x02",
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

    def lambda_9144():
        OP_95(0xFE, 1000, 0, -24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_9144)
    Sleep(150)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)

    def lambda_9169():
        OP_95(0xFE, -800, 0, -25400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9169)
    WaitChrThread(0x23, 1)
    WaitChrThread(0x22, 1)
    OP_6F(0x1)

    #C0199
    ChrTalk(
        0x23,
        (
            "#0606F#11P……并没有那么简单。\x02\x03",

            "#0601F东克洛斯贝尔街道似乎也被\x01",
            "布下了相当数量的敌人。\x02\x03",

            "好像主要是那些黑手党啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x22,
        (
            "#12P#1003F无论怎么说……\x01",
            "凭我们目前这种有限的战斗力，\x01",
            "也不能鲁莽地强行突围。\x02\x03",

            "#1001F如果能有辆导力车，\x01",
            "说不定倒还有一些希望……\x02\x03",

            "但很不幸，警察的车辆好像\x01",
            "基本上都已经被警备队夺走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        "#0010F#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x103,
        "#5P#0206F……彻底无路可走了呢。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x25, 0x8)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)

    #N0203
    NpcTalk(
        0x25,
        "男性的声音",
        "──那么，我来想点办法吧。\x02",
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

    def lambda_93D1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_93D1)

    def lambda_93DE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_93DE)

    def lambda_93EB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_93EB)

    def lambda_93F8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_93F8)

    def lambda_9405():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_9405)
    ClearChrFlags(0x25, 0x8)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetCameraDistance(15500, 3000)
    OP_68(0, 1000, 0, 3000)

    def lambda_9445():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9445)
    Sleep(50)

    def lambda_9462():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_9462)

    def lambda_947C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_947C)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    WaitChrThread(0x27, 1)
    OP_6F(0x1)

    #C0204
    ChrTalk(
        0x101,
        "#0005F迪塔总裁……！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x20,
        "#1110F啊，滴，还有贝尔！\x02",
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

    def lambda_95EF():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95EF)

    def lambda_9609():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9609)

    def lambda_9623():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9623)
    Sleep(50)

    def lambda_9640():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9640)

    def lambda_965A():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_965A)

    def lambda_9674():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_9674)

    def lambda_968E():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_968E)

    def lambda_96A8():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_96A8)
    Sleep(50)

    def lambda_96C5():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_96C5)

    def lambda_96DF():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_96DF)

    def lambda_96F9():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_96F9)

    def lambda_9713():
        OP_98(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9713)
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
            "#6P#2904F呵呵……\x01",
            "各位真是辛苦了啊。\x02\x03",

            "#2901F还有，小琪雅，\x01",
            "你未免也太过乱来了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x27,
        (
            "#6P#6001F是、是啊……！\x01",
            "突然就跑出去……！\x02\x03",

            "#6008F……不要再这么莽撞了哦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x20,
        "#11P#1106F对、对不起……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x21,
        (
            "#1404F#11P……呵呵。\x02\x03",

            "#1402F滴，你没事就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x27,
        "#6P#6010F嗯……爸爸也是……！\x02",
    )

    CloseMessageWindow()

    def lambda_989D():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD3DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_989D)
    WaitChrThread(0x22, 1)
    Sleep(300)

    #C0211
    ChrTalk(
        0x22,
        (
            "#11P#1003F──初次见面，\x01",
            "我是特别任务支援科的赛尔盖。\x02\x03",

            "#1000F那么……\x01",
            "您说的办法是指？\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x25,
        (
            "#6P#2804F车库里停放着我的轿车。\x02\x03",

            "#2800F不但有防弹外壳，而且速度相当快，\x01",
            "应该可以用来强行突围吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x22,
        "#11P#1005F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x23,
        "#11P#0602F#N确实如此，那样一来……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x22, 500)
    Sleep(300)

    #C0215
    ChrTalk(
        0x21,
        (
            "#1403F#11P既然如此，似乎有必要\x01",
            "选择一下乘车人员啊。\x02\x03",

            "#1400F毕竟这里也需要有人守卫，\x01",
            "乘车人员除了我之外……\x02",
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
            "#11P#0003F……不。\x02\x03",

            "#0001F可不可以将突围的任务\x01",
            "交给我们呢？\x02",
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

    def lambda_9B5E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9B5E)
    Sleep(50)

    def lambda_9B6E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_9B6E)
    Sleep(50)

    def lambda_9B7E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_9B7E)

    #C0217
    ChrTalk(
        0x21,
        "#11P#1405F什么……？\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x23,
        "#11P#0605F突、突然说些什么啊！？\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x22,
        "#5P#1001F嗯……\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#11P#0006F……约亚西姆的目标\x01",
            "恐怕只有琪雅一人而已。\x02\x03",

            "#0008F如果琪雅被夺走，\x01",
            "就意味着我们彻底失败了……\x02\x03",

            "#0000F反过来说，只要能保护好琪雅，\x01",
            "并将他逮捕，那就是我们的胜利了。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        (
            "#11P#0304F由此可见，这栋大楼是\x01",
            "无论如何也要守住的……\x02\x03",

            "#0300F所以，应该在这里配备足够的战斗力。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x102,
        (
            "#0104F#11P如果亚里欧斯先生能留下来，\x01",
            "这里就等于有了铜墙铁壁般的防御……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x103,
        (
            "#6P#0202F#11P再加上科长他们和警队的支援，\x01",
            "应该就万无一失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x21,
        "#11P#1404F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x23,
        "#11P#0601F道、道理我虽然明白，可是……\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x22,
        "#5P#1006F──不行。\x02",
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

    def lambda_9E54():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9E54)
    Sleep(50)

    def lambda_9E64():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E64)

    def lambda_9E71():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9E71)

    def lambda_9E7E():
        TurnDirection(0xFE, 0x22, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9E7E)
    WaitChrThread(0x104, 2)

    #C0227
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x22,
        (
            "#5P#1003F你们忘了最重要的事啊。\x02\x03",

            "#1001F在你们几个之中，好像\x01",
            "并没有会开车的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        "#6P#0011F啊……\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        "#12P#0106F说、说起来……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x23,
        "#11P#0607F那么，就由我来──\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x22,
        (
            "#5P#1003F不，你还要负责指挥警队，\x01",
            "并对亚里欧斯进行支援。\x02\x03",

            "#1002F开车的任务就交给我吧。\x02",
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
        "#12P#0105F哎！？\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#12P#0305F科长……\x01",
            "您会开车吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x22,
        (
            "#5P#1004F再怎么说，我在警察学校时\x01",
            "也曾兼任过驾驶课的教官呢。\x02\x03",

            "#1002F总之，就交给我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        "#12P#0202F真是让人意外的经历呢……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        (
            "#6P#0000F……帮大忙了，\x01",
            "那就拜托您了。\x02",
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
            "#12P#1112F罗伊德……\x01",
            "……你们要走了吗……？\x02",
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

    def lambda_A19F():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A19F)
    Sleep(50)

    def lambda_A1AF():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A1AF)

    def lambda_A1BC():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A1BC)

    def lambda_A1C9():
        TurnDirection(0xFE, 0x20, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A1C9)
    Sleep(300)

    #C0239
    ChrTalk(
        0x101,
        (
            "#0004F#5P是啊……不过没关系的。\x02\x03",

            "#0002F大家一定都会回来的，\x01",
            "回到琪雅的身边。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#5P#0109F嗯……那当然。\x02\x03",

            "#0102F等我们回来以后，\x01",
            "还要请你帮忙一起制作料理哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x20,
        "#12P#1110F啊……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#11P#0202F确实呢，经过琪雅之手的料理，\x01",
            "就像被施了魔法一般美味。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x104,
        (
            "#11P#0309F要不，到时候干脆\x01",
            "就办个大型聚会好啦。\x02\x03",

            "把所有认识的家伙\x01",
            "都叫到支援科来。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#0009F#5P哈哈……那也不错啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(15000, 1200)
    OP_68(270, 1100, -11520, 1200)

    def lambda_A370():
        OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A370)
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
            "#0006F#5P……琪雅，\x01",
            "你一直都很迷茫，很不安吧。\x02\x03",

            "#0008F以前的经历全都无法想起，\x01",
            "连自己是谁也一无所知……\x02\x03",

            "#0001F抱歉，我们一直都没有察觉到。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x20,
        "#12P#1112F#40W罗伊德……\x02",
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
            "#12P#1106F#30W……嗯，虽然觉得心里稍微\x01",
            "有一点点不安……\x02\x03",

            "#1104F可是……因为有罗伊德和大家在，\x01",
            "我一点都没觉得寂寞哦……\x02\x03",

            "#1108F……所以……所以啊……！\x02\x03",

            "#1112F绝对要平安回来哦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x101,
        "#0002F#5P嗯……一言为定！\x02",
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

    # Function_46_7FED end

    def Function_47_A676(): pass

    label("Function_47_A676")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6B2")
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
    Jump("Function_47_A676")

    label("loc_A6B2")

    Return()

    # Function_47_A676 end

    SaveToFile()

Try(main)
