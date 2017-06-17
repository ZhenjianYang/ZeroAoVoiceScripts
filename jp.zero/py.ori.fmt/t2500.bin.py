from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2500.bin",                # FileName
        "t2500",                    # MapName
        "t2500",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -25330, 0, -250, 0, 0, 1, 90, 0, 2, 0, 4],
    )

    BuildStringList((
        "t2500",                  # 0
        "ノウェ隊員",             # 1
        "ダイモン隊員",           # 2
        "ギャリソン隊員",         # 3
        "バレル隊員",             # 4
        "アレクセイ隊員",         # 5
        "商人",                   # 6
        "観光客",                 # 7
        "女の子",                 # 8
        "観光客",                 # 9
        "商人",                   # 10
        "観光客",                 # 11
        "女の子",                 # 12
        "観光客",                 # 13
        "観光客",                 # 14
        "観光客ロン",             # 15
        "観光客アルフェット",     # 16
        "ノエル曹長",             # 17
        "ソーニャ副司令",         # 18
        "新人隊員",               # 19
        "新人隊員",               # 20
        "新人隊員",               # 21
        "新人隊員",               # 22
        "バス",                   # 23
        "バスの運転手",           # 24
        "車１",                   # 25
        "bt2500",                 # 26
        "bt2500",                 # 27
        "東クロスベル街道",       # 28
    ))

    ATBonus("ATBonus_52C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_60C", 3, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 13, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_620", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_628", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_5EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_600", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_604", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_608", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_62C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 6, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_64C", 0x0022, 16, 6, 0, 0, 1, 0, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31201.dat", "ms31301.dat", "ms31301.dat", "ms31301.dat", 0, 0, 0, 0, "MonsterBattlePostion_60C", "MonsterBattlePostion_5EC", "ed7402", "ed7403", "ATBonus_52C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_690", 0x0022, 16, 6, 0, 0, 1, 0, 0, "bt2500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms00801.dat", "ms31201.dat", "ms31301.dat", "ms31301.dat", "ms31301.dat", 0, 0, 0, "MonsterBattlePostion_62C", "MonsterBattlePostion_5EC", "ed7402", "ed7403", "ATBonus_52C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31300.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21100.itc",                   # 03
        "chr/ch21500.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch23600.itc",                   # 06
        "chr/ch20800.itc",                   # 07
        "chr/ch28300.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch22100.itc",                   # 0A
    ))

    DeclNpc(-22430,  0,       4730,    270,  257,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-22239,  0,       -5489,   270,  257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(13659,   10000,   2849,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(13859,   10000,   -2640,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(13859,   10000,   -2640,   90,   385,  0x0, 0,   1,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-31389,  0,       19799,   90,   385,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-34919,  0,       15539,   45,   385,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-34409,  0,       15039,   315,  401,  0x0, 0,   4,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-37229,  0,       -3910,   270,  385,  0x0, 0,   5,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-19379,  0,       13590,   90,   385,  0x0, 0,   2,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-20319,  0,       -11380,  270,  385,  0x0, 0,   3,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-24770,  0,       -11600,  180,  385,  0x0, 0,   4,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-31459,  0,       22420,   90,   385,  0x0, 0,   6,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-31409,  0,       23840,   90,   385,  0x0, 0,   7,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(2450,    5000,    -17899,  90,   385,  0x0, 0,   5,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-20709,  159,     -25729,  180,  385,  0x0, 0,   10,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-31139,  0,       23909,   90,   453,  0x0, 0,   8,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 35,  -50.41999816894531,    -0.07999999821186066,  0.0,                   256.0,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0625,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   25.209999084472656,    0.004999999888241291,  -0.0,                  1.0])
    DeclEvent(0x0000, 0, 33,  -31.280000686645508,   23.739999771118164,    0.0,                   2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   3.128000020980835,     -2.374000072479248,    -0.0,                  1.0])

    DeclActor(-31150,  0,       27650,   1200,    -31150,  1000,    27650,   0x007C, 0,  28, 0x0000)
    DeclActor(-18980,  200,     -11720,  1200,    -18980,  1700,    -11720,  0x007C, 0,  34, 0x0000)
    DeclActor(-39780,  0,       1010,    1200,    -39780,  2000,    1010,    0x007C, 0,  11, 0x0000)
    DeclActor(-8000,   1500,    -37500,  1200,    -8000,   2500,    -37500,  0x007C, 0,  5,  0x0000)

    PlaceName(-71.0, 0.0, -8.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-5.25, 0.0, -2.5, 0x0000, 0x0052, "")
    PlaceName(-30.950000762939453, 0.0, 28.100000381469727, 0x0000, 0x0055, "")
    PlaceName(-39.619998931884766, 0.0, 2.5999999046325684, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_764",          # 00, 0
        "Function_1_81C",          # 01, 1
        "Function_2_847",          # 02, 2
        "Function_3_8B7",          # 03, 3
        "Function_4_9AE",          # 04, 4
        "Function_5_BB8",          # 05, 5
        "Function_6_D05",          # 06, 6
        "Function_7_DF0",          # 07, 7
        "Function_8_F0C",          # 08, 8
        "Function_9_FA1",          # 09, 9
        "Function_10_1553",        # 0A, 10
        "Function_11_1642",        # 0B, 11
        "Function_12_1650",        # 0C, 12
        "Function_13_1D7F",        # 0D, 13
        "Function_14_24BB",        # 0E, 14
        "Function_15_2BC1",        # 0F, 15
        "Function_16_32B6",        # 10, 16
        "Function_17_33BE",        # 11, 17
        "Function_18_3449",        # 12, 18
        "Function_19_34C6",        # 13, 19
        "Function_20_3506",        # 14, 20
        "Function_21_3543",        # 15, 21
        "Function_22_35C9",        # 16, 22
        "Function_23_361C",        # 17, 23
        "Function_24_3654",        # 18, 24
        "Function_25_36EC",        # 19, 25
        "Function_26_3778",        # 1A, 26
        "Function_27_3888",        # 1B, 27
        "Function_28_3973",        # 1C, 28
        "Function_29_3977",        # 1D, 29
        "Function_30_3E9F",        # 1E, 30
        "Function_31_4589",        # 1F, 31
        "Function_32_527C",        # 20, 32
        "Function_33_659C",        # 21, 33
        "Function_34_69A7",        # 22, 34
        "Function_35_6A0D",        # 23, 35
    ))


    def Function_0_764(): pass

    label("Function_0_764")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7A4"),
        (1, "loc_7B0"),
        (2, "loc_7BC"),
        (3, "loc_7C8"),
        (4, "loc_7D4"),
        (5, "loc_7E0"),
        (6, "loc_7EC"),
        (SWITCH_DEFAULT, "loc_7F8"),
    )


    label("loc_7A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_7F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_804")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_81B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_804")

    label("loc_81B")

    Return()

    # Function_0_764 end

    def Function_1_81C(): pass

    label("Function_1_81C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_846")
    OP_94(0xFE, 0xFFFF9D40, 0xFFFFC20C, 0xFFFFADE4, 0xFFFFDCC4, 0x3E8)
    Sleep(250)
    Jump("Function_1_81C")

    label("loc_846")

    Return()

    # Function_1_81C end

    def Function_2_847(): pass

    label("Function_2_847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_END)), "loc_853")
    Call(0, 3)

    label("loc_853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_875")
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_875")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 30)

    label("loc_875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    SetMapFlags(0x10000000)
    Event(0, 29)
    SetScenarioFlags(0x88, 2)
    Jump("loc_8B6")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_89E")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_89E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_8B6")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_8B6")

    Return()

    # Function_2_847 end

    def Function_3_8B7(): pass

    label("Function_3_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8CA")
    ClearChrFlags(0x15, 0x80)
    Jump("loc_995")

    label("loc_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8DD")
    ClearChrFlags(0x14, 0x80)
    Jump("loc_995")

    label("loc_8DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8F5")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_995")

    label("loc_8F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_913")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    BeginChrThread(0x13, 0, 0, 1)
    Jump("loc_995")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_926")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_995")

    label("loc_926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_966")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_945")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_961")

    label("loc_945")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_961")
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_961")

    label("loc_961")

    Jump("loc_995")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_97E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_995")

    label("loc_97E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_98C")
    Jump("loc_995")

    label("loc_98C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_995")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AD")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_9AD")

    Return()

    # Function_3_8B7 end

    def Function_4_9AE(): pass

    label("Function_4_9AE")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    SetMapObjFrame(0x4, "chukin", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A01")
    Jump("loc_AFD")

    label("loc_A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A0F")
    Jump("loc_AFD")

    label("loc_A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A1D")
    Jump("loc_AFD")

    label("loc_A1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A2B")
    Jump("loc_AFD")

    label("loc_A2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A3F")
    ClearMapObjFlags(0x4, 0x4)
    Jump("loc_AFD")

    label("loc_A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_ACC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC7")
    OP_65(0x0, 0x1)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x2)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    SetChrPos(0x1E, -26910, 0, 24000, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_71(0x5, 0x1E, 0x1E, 0x0, 0x0)
    OP_74(0x5, 0x1E)

    label("loc_AC7")

    Jump("loc_AFD")

    label("loc_ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_ADA")
    Jump("loc_AFD")

    label("loc_ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_AE8")
    Jump("loc_AFD")

    label("loc_AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_AFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_AFD")
    ClearScenarioFlags(0x5C, 0)

    label("loc_AFD")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6A")
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x20)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetChrPos(0x20, -40000, 0, 2500, 0)
    OP_D3(0x20, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x2, 0x1E)
    OP_70(0x2, 0x0)
    OP_66(0x2, 0x1)
    Jump("loc_B6F")

    label("loc_B6A")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8C")
    SetMapObjFlags(0x2, 0x4)

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA0")
    SetMapObjFlags(0x2, 0x4)

    label("loc_BA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3")
    OP_70(0x6, 0x0)
    Jump("loc_BB7")

    label("loc_BB3")

    OP_70(0x6, 0x1E)

    label("loc_BB7")

    Return()

    # Function_4_9AE end

    def Function_5_BB8(): pass

    label("Function_5_BB8")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB4")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_C3D")
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
    SetScenarioFlags(0x113, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_CAF")

    label("loc_C3D")

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
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_CAF")

    Jump("loc_CF9")

    label("loc_CB4")

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

    label("loc_CF9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BB8 end

    def Function_6_D05(): pass

    label("Function_6_D05")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市東口\x01",      # 0
            "アルモリカ村\x01",          # 1
            "停留所（三叉路）\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_DE8")

    label("loc_DA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC8")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_DE8")

    label("loc_DC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE8")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_DE8")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_D05 end

    def Function_7_DF0(): pass

    label("Function_7_DF0")

    Fade(1000)
    OP_68(-27530, 1000, 24550, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(24000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -32119, 0, 25500, 89)
    SetChrPos(0x1, -32119, 0, 24000, 89)
    SetChrPos(0x2, -32119, 0, 22500, 89)
    SetChrPos(0x3, -32119, 0, 21000, 89)
    ClearChrFlags(0x1E, 0x80)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1E, -27000, 0, 4810, 0)
    OP_D3(0x1E, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_0D()
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    def lambda_EC6():
        OP_95(0xFE, -27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_EC6)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1E, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_DF0 end

    def Function_8_F0C(): pass

    label("Function_8_F0C")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -31260, 0, 26050, 89)
    SetChrPos(0x1, -31260, 0, 26050, 89)
    SetChrPos(0x2, -31260, 0, 26050, 89)
    SetChrPos(0x3, -31260, 0, 26050, 89)
    OP_68(-31260, 1000, 26050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_F0C end

    def Function_9_FA1(): pass

    label("Function_9_FA1")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154B")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E8")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1051")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_106D")

    label("loc_1051")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_106D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109F")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_10B9")

    label("loc_109F")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_10B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10EB")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_1105")

    label("loc_10EB")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_1105")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1137")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1151")

    label("loc_1137")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_1151")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1183")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_119D")

    label("loc_1183")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_119D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C7")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_11D9")

    label("loc_11C7")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_11D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1203")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_1215")

    label("loc_1203")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_1215")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1243")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1259")

    label("loc_1243")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_1259")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1283")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_1295")

    label("loc_1283")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_1295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C1")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_12D5")

    label("loc_12C1")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_12D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1307")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_1321")

    label("loc_1307")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_1321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1355")

    label("loc_1347")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_1355")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14D9")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x2)
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
        (0, "loc_142C"),
        (1, "loc_143A"),
        (2, "loc_1448"),
        (3, "loc_1456"),
        (4, "loc_1464"),
        (5, "loc_1472"),
        (6, "loc_1480"),
        (7, "loc_148E"),
        (8, "loc_149C"),
        (9, "loc_14AA"),
        (10, "loc_14B8"),
        (11, "loc_14C6"),
        (SWITCH_DEFAULT, "loc_14D4"),
    )


    label("loc_142C")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_143A")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_1448")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_1456")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_1464")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_1472")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_1480")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_148E")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_149C")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_14AA")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_14B8")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_14C6")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14D4")

    label("loc_14D4")

    Jump("loc_14E3")

    label("loc_14D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14E3")

    Jump("loc_1546")

    label("loc_14E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1533")
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
    Jump("loc_1546")

    label("loc_1533")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1546")

    Jump("loc_FBB")

    label("loc_154B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_FA1 end

    def Function_10_1553(): pass

    label("Function_10_1553")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -39760, 0, -650, 180)
    SetChrPos(0x1, -39760, 0, -650, 180)
    SetChrPos(0x2, -39760, 0, -650, 180)
    SetChrPos(0x3, -39760, 0, -650, 180)
    SetChrPos(0x4, -39760, 0, -650, 180)
    SetChrPos(0x5, -39760, 0, -650, 180)
    Sleep(1)
    OP_68(-39760, 1000, -650, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1627")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_162D")

    label("loc_1627")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_162D")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1553 end

    def Function_11_1642(): pass

    label("Function_11_1642")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_1642 end

    def Function_12_1650(): pass

    label("Function_12_1650")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_16D7")

    #C0005
    ChrTalk(
        0xFE,
        (
            "ノエル曹長なら朝早くに\x01",
            "クロスベル大聖堂に向かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "例の遺跡の報告書を\x01",
            "エラルダ大司教に渡しにいくそうだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7B")

    label("loc_16D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_176A")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ノエル曹長と君たち支援課に\x01",
            "任務を任せてしまったのは、\x01",
            "少し不甲斐ない思いだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "僕たち一般隊員も\x01",
            "もっと強くならなきゃな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7B")

    label("loc_176A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1850")

    #C0009
    ChrTalk(
        0xFE,
        (
            "記念祭の終わりに１日だけ休みを取って、\x01",
            "アルモリカ村に行ってきたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "もう１ヶ月近くも前の話だけど、\x01",
            "あの時のリフレッシュがよかったのか\x01",
            "ここ最近調子がよくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "よぉし、今日もがんばるぞ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18B1")

    label("loc_1850")


    #C0012
    ChrTalk(
        0xFE,
        (
            "疲れた体じゃどうしても\x01",
            "仕事の効率はおちるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "やっぱり、適度に休む事は大切だよね。\x02",
    )

    CloseMessageWindow()

    label("loc_18B1")

    Jump("loc_1D7B")

    label("loc_18B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1941")

    #C0014
    ChrTalk(
        0xFE,
        (
            "うへぇ……\x01",
            "まさに帰省ラッシュだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "明日は休暇の予定だったけど、\x01",
            "明日までは忙しそうだし\x01",
            "１日くらい遅らせようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7B")

    label("loc_1941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_199E")

    #C0016
    ChrTalk(
        0xFE,
        (
            "ぼちぼち共和国側に帰る\x01",
            "観光客が現れだしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "明日は混むだろうな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D7B")

    label("loc_199E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1B61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1AD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A57")

    #C0018
    ChrTalk(
        0xFE,
        (
            "……実はさ、\x01",
            "記念祭が終わったあとに\x01",
            "１日だけ休暇をとってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "観光客を真似して、\x01",
            "アルモリカ村にでも行って\x01",
            "ゆっくり休むとしようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACB")

    label("loc_1A57")


    #C0020
    ChrTalk(
        0xFE,
        (
            "仕事さえきっちりやってれば\x01",
            "ソーニャ司令は\x01",
            "休暇も許可してくれるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "その分、仕事はキビしいんだけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_1ACB")

    Jump("loc_1B5C")

    label("loc_1AD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_1B30")

    #C0022
    ChrTalk(
        0xFE,
        (
            "今通った人の中に\x01",
            "偽ブランド業者が……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……う～ん……\x01",
            "誰なんだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B5C")

    label("loc_1B30")


    #C0024
    ChrTalk(
        0xFE,
        "ふぁ～……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "……おっと、いけねっ。\x02",
    )

    CloseMessageWindow()

    label("loc_1B5C")

    Jump("loc_1D7B")

    label("loc_1B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1BF8")

    #C0026
    ChrTalk(
        0xFE,
        (
            "昨日、共和国からの観光客が\x01",
            "大挙してきてね。\x01",
            "流石に忙しかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "まだしばらくは通行量も多いだろう。\x01",
            "気を引き締めとかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7B")

    label("loc_1BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C92")

    #C0028
    ChrTalk(
        0xFE,
        (
            "タングラム門を指揮する\x01",
            "ソーニャ副司令は\x01",
            "とても有能な方でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "実質、警備隊のトップは\x01",
            "あの人と言っても過言じゃないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CEB")

    label("loc_1C92")


    #C0030
    ChrTalk(
        0xFE,
        "あの司令さえいなきゃな……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "……っと失礼。\x01",
            "今のは聞かなかったことにしてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEB")

    Jump("loc_1D7B")

    label("loc_1CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D7B")

    #C0032
    ChrTalk(
        0xFE,
        (
            "最近、このタングラム門を抜けた先で\x01",
            "運搬車が事故っちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "特にブツけるようなものもないのに\x01",
            "一体どうしたんだろうね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7B")

    TalkEnd(0xFE)
    Return()

    # Function_12_1650 end

    def Function_13_1D7F(): pass

    label("Function_13_1D7F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1E0E")

    #C0034
    ChrTalk(
        0xFE,
        (
            "行き来する人々から\x01",
            "嫌な噂を耳にした……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "昨日、クロスベル市のほうで\x01",
            "抗争があったそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "……嫌な雰囲気だ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_1E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE1")

    #C0037
    ChrTalk(
        0xFE,
        (
            "遺跡の調査において\x01",
            "ノエル曹長への協力を感謝する……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "やはり、特務支援課とは\x01",
            "なかなかやるものだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "おかげで借りができた。\x01",
            "助けて欲しいことがあったら\x01",
            "いつでも言ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F49")

    label("loc_1EE1")


    #C0040
    ChrTalk(
        0xFE,
        (
            "タングラム部隊は\x01",
            "特務支援課に借りが出来た……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "助けて欲しいことがあったら\x01",
            "いつでも言ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F49")

    Jump("loc_24B7")

    label("loc_1F4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_20C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2097")

    #C0042
    ChrTalk(
        0xFE,
        "ノエル曹長、お疲れ様です！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x109,
        (
            "#0500Fお疲れ様です。\x01",
            "共和国方面に異常は？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "ハッ、異常ありません！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "通行する観光客の間でも\x01",
            "特にトラブルは発生していません。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x109,
        (
            "#0503F了解しました。\x01",
            "自分は特務支援課の皆さんと\x01",
            "例の遺跡へ向かいます。\x02\x03",

            "#0501F引き続き警備をよろしくおねがいします。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "ハッ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20BB")

    label("loc_2097")


    #C0048
    ChrTalk(
        0xFE,
        "タングラム門、異常ありません！\x02",
    )

    CloseMessageWindow()

    label("loc_20BB")

    Jump("loc_24B7")

    label("loc_20C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2138")

    #C0049
    ChrTalk(
        0xFE,
        "今日で最終日か……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "ここにいる観光客は\x01",
            "閉会式には興味ないというわけか。\x01",
            "……現金な感じがするな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_2138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2194")

    #C0051
    ChrTalk(
        0xFE,
        (
            "この賑わい……\x01",
            "共和国への定期バスも\x01",
            "本数を増やしたほうがよさそうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_2194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2397")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2248")

    #C0052
    ChrTalk(
        0xFE,
        (
            "さすがに共和国からの観光客は\x01",
            "減ってきたが……\x01",
            "今日は折り返し地点だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "明日あたりからまたぽつぽつ、\x01",
            "共和国に帰省する人々が\x01",
            "現れるだろうな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2392")

    label("loc_2248")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_2283")

    #C0054
    ChrTalk(
        0xFE,
        (
            "あの黒髪の女性……\x01",
            "何か、あるな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2392")

    label("loc_2283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_232B")

    #C0055
    ChrTalk(
        0xFE,
        (
            "ノウェのやつ、\x01",
            "あくびなんかしやがって。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "ソーニャ副司令にバレても知らんぞ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0057
    ChrTalk(
        0xFE,
        (
            "そういや、あんたら\x01",
            "警察の何たら課だったか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_232B")


    #C0058
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令に会いに来たんなら\x01",
            "中に入って２階に上がるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "今ならいらっしゃるはずだぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_2392")

    Jump("loc_24B7")

    label("loc_2397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2402")

    #C0060
    ChrTalk(
        0xFE,
        (
            "記念祭、俺も行きたいものだが……\x01",
            "忙しいからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "ベルガード門の方も大変だろうな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_2402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2470")

    #C0062
    ChrTalk(
        0xFE,
        (
            "来月は記念祭……\x01",
            "相当多くの観光客が\x01",
            "この門を通っていくだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "……忙しくなりそうだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B7")

    label("loc_2470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_24B7")

    #C0064
    ChrTalk(
        0xFE,
        (
            "この門を抜けると\x01",
            "カルバード共和国領だ。\x01",
            "……なにか用か？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D7F end

    def Function_14_24BB(): pass

    label("Function_14_24BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2547")

    #C0065
    ChrTalk(
        0xFE,
        (
            "俺たちの国境監視警備は\x01",
            "本当に役に立ってるんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ここまで平穏だと\x01",
            "考えなくていいことまで\x01",
            "考えてしまうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_2547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_25DC")

    #C0067
    ChrTalk(
        0xFE,
        (
            "バレルのやつが\x01",
            "早いうちに復帰できてよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "警備隊員ともあろう者が\x01",
            "お化けにビビって倒れてたんじゃ\x01",
            "カッコつかないからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_25DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2642")

    #C0069
    ChrTalk(
        0xFE,
        (
            "バレルのやつ……\x01",
            "大丈夫なのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "っといかんいかん。\x01",
            "警備に集中しないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_2642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26A7")

    #C0071
    ChrTalk(
        0xFE,
        (
            "足元から次々と\x01",
            "共和国へのバスが出て行く……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "……記念祭も終わっていく、か……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_26A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2727")

    #C0073
    ChrTalk(
        0xFE,
        "受付は段々慌しくなってきたみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "くぁ……\x01",
            "いかんいかん、ここはのどかすぎて\x01",
            "アクビが出てしまうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_2727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_27D6")

    #C0075
    ChrTalk(
        0xFE,
        (
            "共和国の人達が\x01",
            "にこやかに入国してくるのを見ると\x01",
            "なんだか安心するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "不戦条約締結前は、\x01",
            "テロなんかが横行していたからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "やはり、平和が一番だよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_27D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2889")

    #C0078
    ChrTalk(
        0xFE,
        (
            "昨日のここからの眺めは\x01",
            "壮観だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "共和国からぞろぞろと\x01",
            "こちらに向かう人と導力バス……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "行軍以外であれほど人の流れが\x01",
            "くっきり見えたのは初めてだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BBD")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299A")

    #C0081
    ChrTalk(
        0xFE,
        (
            "カルバードからこの門までは\x01",
            "結構距離があって見晴らしもいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "かといって、\x01",
            "警戒の気を抜けるわけじゃないけど……\x01",
            "ベルガード門よりはマシって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "あそこはなんたって、\x01",
            "あの無能の司令が仕切ってるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        "#0301F……………………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A1B")

    label("loc_299A")


    #C0085
    ChrTalk(
        0xFE,
        (
            "タングラム門に配置された俺たちは\x01",
            "ある意味幸運だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "無能の司令じゃなく、\x01",
            "聡明なソーニャ副司令の下で\x01",
            "働けるんだからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1B")

    Jump("loc_2BBD")

    label("loc_2A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B34")

    #C0087
    ChrTalk(
        0xFE,
        (
            "あの大きな川の向こうに見える街が\x01",
            "カルバード共和国の国境の町、\x01",
            "アルタイル市だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "不戦条約が締結される前までは\x01",
            "その前に広がるタングラム丘陵で\x01",
            "大規模な演習が行われていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "まるで、銃口を向けられているようで\x01",
            "生きた心地がしなかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BBD")

    label("loc_2B34")


    #C0090
    ChrTalk(
        0xFE,
        (
            "不戦条約が締結される前までは\x01",
            "国境に広がるタングラム丘陵で\x01",
            "大規模な演習が行われていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "あの頃の緊張は\x01",
            "凄まじいものだったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBD")

    TalkEnd(0xFE)
    Return()

    # Function_14_24BB end

    def Function_15_2BC1(): pass

    label("Function_15_2BC1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C92")

    #C0092
    ChrTalk(
        0xFE,
        (
            "みんな、色んな考えを持って\x01",
            "クロスベルにやって来るんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "中にはきっと悪いヤツも\x01",
            "大勢いるだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "こうして警備する以上は\x01",
            "一人でも多くの悪いヤツを\x01",
            "取り締まりたいもんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_2C92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D42")

    #C0095
    ChrTalk(
        0xFE,
        (
            "例の遺跡の調査の時に\x01",
            "化け物にビビっちゃって、\x01",
            "今まで寝込んでたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "皆には迷惑をかけてしまったな。\x01",
            "これからバリバリ仕事を頑張って\x01",
            "借りを返さないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_2D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D50")
    Jump("loc_32B2")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2DF1")

    #C0097
    ChrTalk(
        0xFE,
        (
            "下を手伝いたいのは\x01",
            "山々だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "持ち場を離れるわけには\x01",
            "行かないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "申し訳ないのとラッキーってのが\x01",
            "半々ぐらいの気持ちかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E89")

    #C0100
    ChrTalk(
        0xFE,
        (
            "こうして共和国との国境を監視していると\x01",
            "実に美しいと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "あの国もクロスベルを狙ってると考えると\x01",
            "なんだか複雑なんだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_2E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F1C")

    #C0102
    ChrTalk(
        0xFE,
        (
            "あー……\x01",
            "やっぱり眺めがいいなここは……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "クロスベル市に行くと\x01",
            "ゴチャゴチャしてて落ち着かないし\x01",
            "案外、国境監視も悪くないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_2F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_306B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FE6")

    #C0104
    ChrTalk(
        0xFE,
        (
            "ベルガード門に配属された\x01",
            "ブルードのヤツは元気かな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "あいつとは日曜学校時代からの\x01",
            "幼馴染なんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "あっちは何かと大変って聞くし……\x01",
            "元気にしてりゃいいけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3066")

    label("loc_2FE6")


    #C0107
    ChrTalk(
        0xFE,
        (
            "ベルガード門のブルードのヤツ……\x01",
            "元気にしてるかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "警備隊員は詰め所暮らしだから、\x01",
            "なかなか会いに行けないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3066")

    Jump("loc_32B2")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3119")

    #C0109
    ChrTalk(
        0xFE,
        (
            "俺たち警備隊は、\x01",
            "帝国と共和国を刺激しないように\x01",
            "大規模な演習ができないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "せっかく必死こいて訓練して\x01",
            "警備隊に入ったのに……\x01",
            "なんかやるせないよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326A")

    #C0111
    ChrTalk(
        0xFE,
        (
            "おっ……君たち、\x01",
            "例の特務支援課だろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "先月の魔獣被害の解決は\x01",
            "ご苦労だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0012Fは、はは……\x01",
            "まぁ、ギリギリでしたけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#0203F実際、ツァイトが来なければ\x01",
            "どうなっていたことか……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "おいおい、謙遜するなよ～。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令も\x01",
            "君たちには期待してるみたいだし、\x01",
            "頑張ってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32B2")

    label("loc_326A")


    #C0117
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令も\x01",
            "君たちには期待してるみたいだ。\x01",
            "頑張ってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B2")

    TalkEnd(0xFE)
    Return()

    # Function_15_2BC1 end

    def Function_16_32B6(): pass

    label("Function_16_32B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3348")

    #C0118
    ChrTalk(
        0xFE,
        (
            "バレルのやつと\x01",
            "見張りを交代してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "あいつの様子を見てしまったら、\x01",
            "誰も調査になんて\x01",
            "志願したくなくなるよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_33BA")

    label("loc_3348")


    #C0120
    ChrTalk(
        0xFE,
        (
            "遺跡の調査の後、\x01",
            "バレルのヤツが寝込んじまってね。\x01",
            "見張りを交代してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "……しかし、腹減ったな～……\x02",
    )

    CloseMessageWindow()

    label("loc_33BA")

    TalkEnd(0xFE)
    Return()

    # Function_16_32B6 end

    def Function_17_33BE(): pass

    label("Function_17_33BE")

    TalkBegin(0xFE)

    #C0122
    ChrTalk(
        0xFE,
        "ふぅ、着いた着いた。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "クロスベルでの買いつけも\x01",
            "ようやく終わったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "さっさと手続きを済ませて\x01",
            "共和国に帰るとしよう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_33BE end

    def Function_18_3449(): pass

    label("Function_18_3449")

    TalkBegin(0xFE)

    #C0125
    ChrTalk(
        0xFE,
        (
            "共和国では導力バスが\x01",
            "かなり普及しているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "こっちで運用されているバスも、\x01",
            "共和国ヴェルヌ社製なんだから。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3449 end

    def Function_19_34C6(): pass

    label("Function_19_34C6")

    TalkBegin(0xFE)

    #C0127
    ChrTalk(
        0xFE,
        (
            "ママ、早くバスに乗りましょ。\x01",
            "早くお祭り行きたーい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_34C6 end

    def Function_20_3506(): pass

    label("Function_20_3506")

    TalkBegin(0xFE)

    #C0128
    ChrTalk(
        0xFE,
        (
            "うーん、\x01",
            "景色のいいところだなぁ\x01",
            "クロスベルは……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_3506 end

    def Function_21_3543(): pass

    label("Function_21_3543")

    TalkBegin(0xFE)

    #C0129
    ChrTalk(
        0xFE,
        (
            "さっさと手続きを済ませて\x01",
            "帰りたいところだが……\x01",
            "意外と混んでるようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "うーん、列車で来たほうが\x01",
            "正解だったかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3543 end

    def Function_22_35C9(): pass

    label("Function_22_35C9")

    TalkBegin(0xFE)

    #C0131
    ChrTalk(
        0xFE,
        (
            "オホホ、ここで待っていれば\x01",
            "共和国行きの導力バスに\x01",
            "一番乗りできますわ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_35C9 end

    def Function_23_361C(): pass

    label("Function_23_361C")

    TalkBegin(0xFE)

    #C0132
    ChrTalk(
        0xFE,
        (
            "兵隊さんがいるねー。\x01",
            "遊んでもらおっかなー。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_361C end

    def Function_24_3654(): pass

    label("Function_24_3654")

    TalkBegin(0xFE)

    #C0133
    ChrTalk(
        0xFE,
        (
            "クロスベル……\x01",
            "町中にマフィアが普通にいるとは\x01",
            "なかなか刺激的な場所だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "大陸一の魔都……という噂も\x01",
            "あながち大げさじゃないらしい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3654 end

    def Function_25_36EC(): pass

    label("Function_25_36EC")

    TalkBegin(0xFE)

    #C0135
    ChrTalk(
        0xFE,
        (
            "ふぅ……クロスベル市までは\x01",
            "バスの乗り継ぎか。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "年寄りにはなかなかしんどいわい。\x01",
            "ゆっくり座れる鉄道で来れば\x01",
            "よかったかのう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_36EC end

    def Function_26_3778(): pass

    label("Function_26_3778")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3818")

    #C0137
    ChrTalk(
        0xFE,
        (
            "うは～～……アルタイル市が\x01",
            "あんなに小さく見えるとはなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "この広大なタングラム丘陵を\x01",
            "横断してきたかと思うと、\x01",
            "何だか感慨深いよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3884")

    label("loc_3818")


    #C0139
    ChrTalk(
        0xFE,
        (
            "この広大なタングラム丘陵を\x01",
            "横断してきたんだなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "……まぁ、バスで来たから\x01",
            "楽チンだったけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3884")

    TalkEnd(0xFE)
    Return()

    # Function_26_3778 end

    def Function_27_3888(): pass

    label("Function_27_3888")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_392C")

    #C0141
    ChrTalk(
        0xFE,
        (
            "ここに立ってると、\x01",
            "列車が通るときにガタガタ揺れて\x01",
            "なかなかスリル満点よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "楽しいけど、風でスカートが\x01",
            "めくれそうになるのが玉にキズね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_396F")

    label("loc_392C")


    #C0143
    ChrTalk(
        0xFE,
        "わーお！\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "……風でめくれるスカートを\x01",
            "素早く抑える練習よ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396F")

    TalkEnd(0xFE)
    Return()

    # Function_27_3888 end

    def Function_28_3973(): pass

    label("Function_28_3973")

    Call(0, 6)
    Return()

    # Function_28_3973 end

    def Function_29_3977(): pass

    label("Function_29_3977")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(-16650, 400, -10470, 0)
    MoveCamera(65, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22430, 0)
    OP_0D()
    Sleep(500)
    OP_68(-14930, 400, 890, 5000)
    MoveCamera(80, 18, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56040, 5000)
    PlaceName2(340, 200, "c_plac19", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(-48970, 1000, -460, 4700)
    MoveCamera(45, 30, 0, 4700)
    OP_6E(510, 4700)
    SetCameraDistance(26660, 4700)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D74")
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3A93")
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    Jump("loc_3AAA")

    label("loc_3A93")

    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x1E)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_3AAA")

    OP_49()
    SetChrPos(0x1E, -63820, 0, -120, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3AF3")
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_3B09")

    label("loc_3AF3")

    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    label("loc_3B09")

    Sleep(2200)

    def lambda_3B11():
        OP_95(0xFE, -26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3B11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3B43")
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Jump("loc_3B49")

    label("loc_3B43")

    Sound(485, 0, 100, 0)

    label("loc_3B49")

    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3B74")
    SetChrFlags(0x1E, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_3BAB")

    label("loc_3B74")

    SetChrPos(0x1E, -40000, 0, 2500, 0)
    OP_D3(0x1E, 0x0, 0x41EB0, 0x0, 0x0)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x2)
    OP_66(0x2, 0x1)

    label("loc_3BAB")

    OP_68(-50970, 1000, -460, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3C90")
    SetChrPos(0x0, -31260, 0, 26050, 89)
    SetChrPos(0x1, -31260, 0, 26050, 89)
    SetChrPos(0x2, -31260, 0, 26050, 89)
    SetChrPos(0x3, -31260, 0, 26050, 89)
    OP_68(-31260, 1000, 26050, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    ClearScenarioFlags(0x7E, 0)
    Jump("loc_3D5F")

    label("loc_3C90")

    SetChrPos(0x0, -39760, 0, -650, 180)
    SetChrPos(0x1, -39760, 0, -650, 180)
    SetChrPos(0x2, -39760, 0, -650, 180)
    SetChrPos(0x3, -39760, 0, -650, 180)
    SetChrPos(0x4, -39760, 0, -650, 180)
    SetChrPos(0x5, -39760, 0, -650, 180)
    Sleep(1)
    OP_68(-39760, 1000, -650, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D4A")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_3D50")

    label("loc_3D4A")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_3D50")

    Sleep(500)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x7E, 1)

    label("loc_3D5F")

    Call(0, 3)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_3E97")

    label("loc_3D74")

    Sleep(2500)
    SetChrPos(0x0, -54820, 0, -130, 270)
    SetChrPos(0x1, -56020, 0, -1200, 270)
    SetChrPos(0x2, -56170, 0, 1010, 270)
    SetChrPos(0x3, -57750, 0, -190, 270)
    OP_0D()

    def lambda_3DC1():
        OP_95(0xFE, -50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3DC1)

    def lambda_3DDB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3DDB)
    Sleep(100)

    def lambda_3DEF():
        OP_95(0xFE, -52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3DEF)

    def lambda_3E09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3E09)
    Sleep(120)

    def lambda_3E1D():
        OP_95(0xFE, -52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3E1D)

    def lambda_3E37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_3E37)
    Sleep(90)

    def lambda_3E4B():
        OP_95(0xFE, -53750, 0, -190, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3E4B)

    def lambda_3E65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_3E65)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    WaitChrThread(0x0, 2)
    WaitChrThread(0x1, 2)
    WaitChrThread(0x2, 2)
    WaitChrThread(0x3, 2)
    Sleep(1000)
    Call(0, 3)

    label("loc_3E97")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_3977 end

    def Function_30_3E9F(): pass

    label("Function_30_3E9F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22750, 3100, 20090, 0)
    MoveCamera(52, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch31250.itc", 0x24)
    LoadChrToIndex("chr/ch31350.itc", 0x25)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x18, -17000, 0, 22500, 270)
    SetChrPos(0x19, -16500, 0, 21500, 270)
    SetChrPos(0x101, -21000, 0, 19000, 0)
    SetChrPos(0x102, -22000, 0, 18000, 0)
    SetChrPos(0x103, -20000, 0, 18000, 0)
    SetChrPos(0x104, -21000, 0, 17000, 0)
    SetChrPos(0x1A, -19500, 0, 26000, 180)
    SetChrPos(0x1B, -20500, 0, 25500, 180)
    SetChrPos(0x1C, -21500, 0, 25500, 180)
    SetChrPos(0x1D, -22500, 0, 26000, 180)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_68(-22750, 2200, 20090, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0145
    ChrTalk(
        0x18,
        (
            "#11P#0501F……それでは、これより\x01",
            "実戦演習を始めます。\x02\x03",

            "形式は４対４のチーム戦……\x01",
            "各自、互いの長所を生かしながら\x01",
            "戦闘に臨むように。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x1A,
        (
            "#11P最近噂の特務支援課か……\x01",
            "相手にとって不足なしだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x1B,
        (
            "#11Pだが、あの有名な\x01",
            "ランディ・オルランドも\x01",
            "いるみたいだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x1B,
        "#11Pひぇぇ……大丈夫かなぁ。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x1C,
        (
            "#5Pだが噂じゃ、女に手を出して\x01",
            "クビになったそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x1C,
        (
            "#5Pそんな軟派者、\x01",
            "本当に強いのかね……？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1D,
        (
            "#5P俺たちの力を見せ付けて、\x01",
            "鼻っ柱を折ってやろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        "#12P#0203F……言われてますよ。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#12P#0304Fへぇ……新人隊員ってわりにゃ\x01",
            "活きの良さそうなのが揃ってら。\x02\x03",

            "#0300Fま、胸は貸してやるから\x01",
            "どっからでもかかってきな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x19,
        (
            "#11P#2003F……ランディ・オルランド。\x01",
            "私語は慎むように。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        "#12P#0306Fな、なんで俺だけ……！？\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x18,
        "#11P#0507F#4S#N……全員、前へ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x9C4)
    SetCameraDistance(16079, 1000)
    OP_68(-22750, 1900, 20090, 1000)

    def lambda_436C():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_436C)

    def lambda_4386():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4386)

    def lambda_43A0():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43A0)

    def lambda_43BA():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43BA)

    def lambda_43D4():
        OP_98(0xFE, 0x1F4, 0x0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_43D4)

    def lambda_43EE():
        OP_98(0xFE, 0x12C, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_43EE)

    def lambda_4408():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4408)

    def lambda_4422():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4422)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1D, 1)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x25)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrSubChip(0x1D, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)

    #C0157
    ChrTalk(
        0x101,
        "#12P#0005Fこいつは……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#12P#0101Fかなり統率されてるわね。\x02\x03",

            "やはり新人隊員だからと言って\x01",
            "侮らない方がよさそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x18,
        "#11P#0507F#4S#N……始めっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_64C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_457F")
    Call(0, 31)
    Jump("loc_4588")

    label("loc_457F")

    OP_29(0xF, 0x1, 0x1)
    Call(0, 32)

    label("loc_4588")

    Return()

    # Function_30_3E9F end

    def Function_31_4589(): pass

    label("Function_31_4589")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22750, 2200, 20090, 0)
    MoveCamera(52, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19040, 0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch00850.itc", 0x24)
    LoadChrToIndex("chr/ch31250.itc", 0x25)
    LoadChrToIndex("chr/ch31350.itc", 0x26)
    LoadChrToIndex("chr/ch31253.itc", 0x27)
    LoadChrToIndex("chr/ch31353.itc", 0x28)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x2)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x2)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x28)
    SetChrSubChip(0x1C, 0x2)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x18, -17000, 0, 22500, 270)
    SetChrPos(0x19, -16500, 0, 21500, 270)
    SetChrPos(0x101, -21000, 0, 20000, 0)
    SetChrPos(0x102, -22000, 0, 19000, 0)
    SetChrPos(0x103, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 18000, 0)
    SetChrPos(0x1A, -19000, 0, 24000, 180)
    SetChrPos(0x1B, -20200, 0, 25200, 180)
    SetChrPos(0x1C, -21800, 0, 25200, 180)
    SetChrPos(0x1D, -23000, 0, 24000, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0160
    ChrTalk(
        0x18,
        "#11P#0507F#4S#Nそこまでっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0161
    ChrTalk(
        0x1A,
        "#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x1B,
        "#11Pや、やっぱり強えぇ……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x1C,
        (
            "#5Pランディ・オルランドも……\x01",
            "噂以上の強さだ……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()

    #C0164
    ChrTalk(
        0x104,
        (
            "#12P#0304Fま、ざっとこんなもんだな。\x02\x03",

            "#0300Fお前さんたちも新人にしちゃ\x01",
            "なかなかよくやった方だが……\x02\x03",

            "俺たちには今一歩、\x01",
            "及ばなかったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x1D,
        "#5Pくそっ……！\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#0006F調子の良いやつだな……\x02\x03",

            "#0000Fでも、さすがは警備隊だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそうね。\x01",
            "少しでも油断があったら\x01",
            "負けていたかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#12P#0200Fでも、これで任務は終わりですね。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#12P#0305Fおっと、そうだな。\x02\x03",

            "#0309Fつーわけで副司令。\x01",
            "今日はこれでお暇さして\x01",
            "もらいますよ。\x02\x03",

            "#0304Fさてロイド、次の仕事に──\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 300)

    #C0170
    ChrTalk(
        0x19,
        "#11P#2005Fあら、誰がこの一戦で終わりだと？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0171
    ChrTalk(
        0x104,
        "#12P#0305F……へ？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#12P#0005Fど、どういうことですか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 300)

    #C0173
    ChrTalk(
        0x19,
        "#11P#2003F……ノエル曹長！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x18,
        "#11P#0501F#N#4Sハッ！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_4AF1():
        OP_95(0xFE, -21000, 0, 23700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4AF1)
    WaitChrThread(0x18, 1)

    def lambda_4B0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B0F)
    WaitChrThread(0x18, 1)
    Fade(500)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0175
    ChrTalk(
        0x18,
        "#5P#0507F#4S警備隊員、全員、起立！\x02",
    )

    CloseMessageWindow()

    #N0176
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N#4S……は、はっ！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0177
    ChrTalk(
        0x102,
        (
            "#12P#0105Fふ、副司令？\x01",
            "これは一体……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 300)

    #C0178
    ChrTalk(
        0x19,
        (
            "#11P#2004F見ての通りよ。\x02\x03",

            "#2001Fあなた達には続けて、\x01",
            "ノエル曹長の指揮する\x01",
            "隊員たちと戦っていただきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0179
    ChrTalk(
        0x104,
        (
            "#12P#0305Fな、なんだそりゃ……\x01",
            "２連続なんて聞いてないッスよ！\x02\x03",

            "#0306Fそれに、ノエルが入って４対５なんて\x01",
            "いくらなんでも……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x19,
        (
            "#11P#2005Fあら、私の出した支援要請は\x01",
            "『新人隊員の実戦演習』への参加よ。\x02\x03",

            "#2002Fならば、新人の訓練になるよう\x01",
            "付き合うのは当然の義務ではなくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        "#12P#0305Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x19,
        (
            "#11P#2003Fそれに、さっきあなた達は\x01",
            "４人の新人を倒した。\x02\x03",

            "#2000Fそこにノエル曹長が加われば、\x01",
            "実力はほぼ対等だと思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        "#12P#0206F……そういうことですか。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはは……副司令は思った以上に\x01",
            "曲者だったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x18,
        (
            "#5P#0506Fす、すみません。\x01",
            "突然の挑戦になってしまいますが……\x02\x03",

            "#0501F私も皆さんと戦って、\x01",
            "実力を確かめてみたいんです。\x02\x03",

            "#0503Fどうか……よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        "#12P#0306F……だぁ～もう、仕方ねぇな！\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#12P#0100F……これは、やるしかないわね。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#12P#0000Fああ……こうなったら思う存分\x01",
            "戦わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#12P#0202F……よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    def lambda_502E():
        OP_95(0xFE, -17000, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_502E)
    WaitChrThread(0x19, 1)

    def lambda_504C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_504C)
    WaitChrThread(0x19, 1)

    #C0190
    ChrTalk(
        0x19,
        (
            "#11P#2004Fふふ、ではあらためて……\x01",
            "今度は私が仕切らせてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x19,
        "#11P#2001F#4S#N……全員、構え！！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0xBB8)
    SetCameraDistance(16079, 1000)
    OP_68(-22750, 1900, 20090, 1000)
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    Sound(808, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)

    #C0192
    ChrTalk(
        0x1B,
        (
            "#11Pよ、よし、ノエル曹長がいるなら\x01",
            "今度こそ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x1C,
        "#5Pああ、やってやろうぜ！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)

    #C0194
    ChrTalk(
        0x101,
        (
            "#12P#0001F敵は警備隊……\x01",
            "戦いのエキスパートだ。\x02\x03",

            "#0007F疲れは残っていないものとみて\x01",
            "全力で臨むぞっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        "#12P#0307Fおうよっ！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x19,
        "#11P#2001F#4S#N……始め！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_690", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5272")
    OP_29(0xF, 0x1, 0x3)
    Jump("loc_5278")

    label("loc_5272")

    OP_29(0xF, 0x1, 0x2)

    label("loc_5278")

    Call(0, 32)
    Return()

    # Function_31_4589 end

    def Function_32_527C(): pass

    label("Function_32_527C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-22750, 1900, 20090, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18940, 0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch05700.itc", 0x22)
    LoadChrToIndex("chr/ch00800.itc", 0x23)
    LoadChrToIndex("chr/ch00850.itc", 0x24)
    LoadChrToIndex("chr/ch31250.itc", 0x25)
    LoadChrToIndex("chr/ch31350.itc", 0x26)
    LoadChrToIndex("chr/ch31253.itc", 0x27)
    LoadChrToIndex("chr/ch31353.itc", 0x28)
    LoadChrToIndex("chr/ch00053.itc", 0x29)
    LoadChrToIndex("chr/ch00153.itc", 0x2A)
    LoadChrToIndex("chr/ch00253.itc", 0x2B)
    LoadChrToIndex("chr/ch00353.itc", 0x2C)
    LoadChrToIndex("chr/ch00853.itc", 0x2D)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    SetChrPos(0x101, -21000, 0, 20000, 0)
    SetChrPos(0x102, -22000, 0, 19000, 0)
    SetChrPos(0x103, -20000, 0, 19000, 0)
    SetChrPos(0x104, -21000, 0, 18000, 0)
    SetChrPos(0x1A, -19000, 0, 24000, 180)
    SetChrPos(0x1B, -20200, 0, 25200, 180)
    SetChrPos(0x1C, -21800, 0, 25200, 180)
    SetChrPos(0x1D, -23000, 0, 24000, 180)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_59A1")
    SetChrPos(0x18, -21000, 0, 23700, 180)
    SetChrPos(0x19, -17000, 0, 22500, 270)
    SetChrChipByIndex(0x18, 0x2D)
    SetChrSubChip(0x18, 0x2)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x2)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x2)
    SetChrChipByIndex(0x1C, 0x28)
    SetChrSubChip(0x1C, 0x2)
    SetChrChipByIndex(0x1D, 0x27)
    SetChrSubChip(0x1D, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0197
    ChrTalk(
        0x19,
        "#11P#2001F#4S#Nそこまで！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0198
    ChrTalk(
        0x1A,
        (
            "#11Pち、ちくしょう……\x01",
            "ダメだったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x1D,
        (
            "#5Pノエル曹長がついていながら、\x01",
            "情けない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x18,
        (
            "#5P#0506F……やはり、やりますね。\x02\x03",

            "自分もまだまだ未熟です。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#12P#0000Fはは、謙遜はしないでくれ。\x01",
            "今度こそ負けるかと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#12P#0300Fノエルが指揮していた時は、\x01",
            "最初より新人たちの\x01",
            "戦いぶりがよくなってたぜ。\x02\x03",

            "#0304Fへっ、さすがは警備隊\x01",
            "期待のホープってとこか……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x18,
        "#5P#0509Fあ、あはは……恐縮です。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    TurnDirection(0x19, 0x1C, 300)

    #C0204
    ChrTalk(
        0x19,
        (
            "#11P#2001Fさて……あなたたち。\x02\x03",

            "これがマフィア達や魔獣を相手に\x01",
            "実戦経験を持つ者たちの強さよ。\x02\x03",

            "#2003F新人のあなた達には\x01",
            "その“経験”の絶対量が\x01",
            "どうしても足りないわ。\x02\x03",

            "加えて、クロスベルの警備隊は\x01",
            "大規模な演習はできない事情がある……\x02\x03",

            "#2001Fだけど、経験を積む方法は\x01",
            "演習以外にもいくらでもあるはず。\x02\x03",

            "クロスベルの警備隊として、\x01",
            "市民を守る存在であり続けるためにも\x01",
            "今後も精進していって頂戴。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #N0205
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N#4Sハッ！！\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x19,
        (
            "#11P#2002Fふふ……いい返事ね。\x02\x03",

            "ごほうびに、詰め所に戻ったら\x01",
            "特別自主トレメニューを\x01",
            "プレゼントしてあげるわ。\x02\x03",

            "#2004F配属先の正式決定があるまで、\x01",
            "毎日こなすこと……いいわね？\x02",
        )
    )

    CloseMessageWindow()

    #N0207
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N（ひ、ひぃ～！！）\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#12P#0100Fふふ……この人には敵わないわね。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        (
            "#12P#0200Fさすが、女性ながらに\x01",
            "副司令を務める方ですね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6496")

    label("loc_59A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5F61")
    SetChrPos(0x18, -21000, 0, 23700, 180)
    SetChrPos(0x19, -17000, 0, 22500, 270)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x2C)
    SetChrSubChip(0x104, 0x3)
    FadeToBright(1000, 0)
    OP_0D()

    #C0210
    ChrTalk(
        0x19,
        "#11P#2001F#4S#Nそこまで！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0211
    ChrTalk(
        0x101,
        (
            "#12P#0010Fいつつ……\x01",
            "ダメだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        (
            "#12P#0306Fノエルが指揮していた時は、\x01",
            "最初より新人たちの\x01",
            "戦いぶりがよくなってたぜ。\x02\x03",

            "#0300Fへっ、さすがは警備隊\x01",
            "期待のホープってとこか……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x18,
        (
            "#5P#0502Fあはは……そんな、\x01",
            "ランディ先輩たちも\x01",
            "すごく強かったですよ。\x02\x03",

            "#0504F少しでも油断していたら\x01",
            "こちらが負けていたと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x1A,
        (
            "#11P勝ったけど……\x01",
            "やっぱり実力不足は否めないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x1D,
        "#5Pああ、曹長がいたおかげだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1C, 300)

    #C0216
    ChrTalk(
        0x19,
        (
            "#11P#2001Fさて……あなたたちも\x01",
            "課題が見えたのではないかしら。\x02\x03",

            "これがマフィア達や魔獣を相手に\x01",
            "実戦経験を持つ者たちの強さよ。\x02\x03",

            "#2003F新人のあなた達には\x01",
            "その“経験”の絶対量が\x01",
            "どうしても足りないわ。\x02\x03",

            "加えて、クロスベルの警備隊は\x01",
            "大規模な演習はできない事情がある……\x02\x03",

            "#2001Fだけど、経験を積む方法は\x01",
            "演習以外にもいくらでもあるはず。\x02\x03",

            "クロスベルの警備隊として、\x01",
            "市民を守る存在であり続けるためにも\x01",
            "今後も精進していって頂戴。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #N0217
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N#4Sハッ！！\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x19,
        (
            "#11P#2002Fふふ……いい返事ね。\x02\x03",

            "ごほうびに、詰め所に戻ったら\x01",
            "特別自主トレメニューを\x01",
            "プレゼントしてあげるわ。\x02\x03",

            "#2004F配属先の正式決定があるまで、\x01",
            "毎日こなすこと……いいわね？\x02",
        )
    )

    CloseMessageWindow()

    #N0219
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N（ひ、ひぃ～！！）\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        "#12P#0100Fふふ……この人には敵わないわね。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#12P#0200Fさすが、女性ながらに\x01",
            "副司令を務める方ですね……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Jump("loc_6496")

    label("loc_5F61")

    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x26)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x26)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x3)
    SetChrChipByIndex(0x102, 0x2A)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x2C)
    SetChrSubChip(0x104, 0x3)
    SetChrPos(0x18, -17000, 0, 22500, 270)
    SetChrPos(0x19, -16500, 0, 21500, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0222
    ChrTalk(
        0x18,
        "#5P#0507F#4S#Nそこまでっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0223
    ChrTalk(
        0x101,
        (
            "#12P#0010Fいつつ……\x01",
            "ダメだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        (
            "#12P#0310Fちっ……油断しちまったぜ。\x02\x03",

            "#0306F新人にやられちまうとは\x01",
            "カッコつかねぇな、くそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x1A,
        (
            "#11Pな、なんとか勝てたけど……\x01",
            "特務支援課ってこんなに強いのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x1A,
        (
            "#11P俺たちは戦いのエリートだと\x01",
            "思っていたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1D,
        (
            "#5Pああ……\x01",
            "もうすっかりクタクタだ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1C, 300)

    #C0228
    ChrTalk(
        0x19,
        (
            "#11P#2001Fさて……あなたたちも\x01",
            "課題が見えたのではないかしら。\x02\x03",

            "これがマフィア達や魔獣を相手に\x01",
            "実戦経験を持つ者たちの強さよ。\x02\x03",

            "#2003F新人のあなた達には\x01",
            "その“経験”の絶対量が\x01",
            "どうしても足りないわ。\x02\x03",

            "加えて、クロスベルの警備隊は\x01",
            "大規模な演習はできない事情がある……\x02\x03",

            "#2001Fだけど、経験を積む方法は\x01",
            "演習以外にもいくらでもあるはず。\x02\x03",

            "クロスベルの警備隊として、\x01",
            "市民を守る存在であり続けるためにも\x01",
            "今後も精進していって頂戴。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x1A, 0x1)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1B, 0x1)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x1)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0x1D, 0x0)
    SetChrSubChip(0x1D, 0x0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #N0229
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N#4Sハッ！！\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x19,
        (
            "#11P#2002Fふふ……いい返事ね。\x02\x03",

            "ごほうびに、詰め所に戻ったら\x01",
            "特別自主トレメニューを\x01",
            "プレゼントしてあげるわ。\x02\x03",

            "#2004F配属先の正式決定があるまで、\x01",
            "毎日こなすこと……いいわね？\x02",
        )
    )

    CloseMessageWindow()

    #N0231
    NpcTalk(
        0x1B,
        "警備隊員たち",
        "#N（ひ、ひぃ～！！）\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        "#12P#0100Fふふ……この人には敵わないわね。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#12P#0200Fさすが、女性ながらに\x01",
            "副司令を務める方ですね……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    label("loc_6496")

    TurnDirection(0x19, 0x101, 300)

    #C0234
    ChrTalk(
        0x19,
        (
            "#11P#2002Fあなた達もご苦労様。\x02\x03",

            "おかげさまで有意義な\x01",
            "演習になったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#12P#0012Fはは……\x01",
            "少し疲れてしまいましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x19,
        (
            "#11P#2004Fふふ、立ち話も何だし……\x01",
            "一度、司令室の方に戻るとしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        "#12P#0000Fはい、そうですね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x5C, 0)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_527C end

    def Function_33_659C(): pass

    label("Function_33_659C")

    EventBegin(0x0)
    OP_4B(0x1F, 0xFF)
    ClearMapObjFlags(0x5, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-31410, 1000, 22290, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18050, 0)
    SetChrPos(0x101, -32500, 0, 21500, 0)
    SetChrPos(0x102, -31000, 0, 21500, 0)
    SetChrPos(0x103, -32500, 0, 20000, 0)
    SetChrPos(0x104, -31000, 0, 20000, 0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_93(0x1F, 0xB4, 0x1F4)

    #C0238
    ChrTalk(
        0x1F,
        "#5Pおや、君たちも乗るのかい？\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#12P#0000Fはい、お待たせしてすみません。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x1F,
        (
            "#5P他のお客さんはもう乗ってるよ。\x01",
            "早く乗りな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66C3():
        OP_95(0xFE, -27390, 600, 24150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_66C3)
    Sleep(1500)

    def lambda_66E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_66E0)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x1F, 2)

    #C0241
    ChrTalk(
        0x101,
        (
            "#5P#0001F……さっきも言ったとおり、\x01",
            "バスの中で偽ブランド業者に\x01",
            "目星をつけるつもりだ。\x02\x03",

            "クロスベル市に着くまでに\x01",
            "急いで考えをまとめよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#12P#0300Fオーケー。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        "#12P#0200F時間との勝負になりそうですね。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        "#11P#0100Fじゃあ、早速乗り込みましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-27170, 1000, 24690, 0)
    MoveCamera(68, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19950, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    Sound(470, 0, 100, 0)
    OP_79(0x5)
    Sound(473, 0, 100, 0)
    OP_68(-26730, 1000, -2100, 6000)
    MoveCamera(37, 21, 0, 6000)
    OP_6E(510, 0)
    SetCameraDistance(23500, 6000)
    OP_71(0x5, 0xB4, 0x79, 0x0, 0x20)

    def lambda_68D9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF92A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_68D9)
    WaitChrThread(0x1E, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x5)
    OP_68(-49120, 1000, -60, 5000)
    MoveCamera(45, 21, 0, 5000)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Sound(467, 0, 100, 0)
    Sound(470, 0, 100, 0)

    def lambda_694C():
        OP_9E(0xFE, 0xFFFF865C, 0xFFFFF060, 0xFFFEA070, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_694C)
    WaitChrThread(0x1E, 1)
    Sound(465, 0, 100, 0)

    def lambda_6971():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_6971)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_659C end

    def Function_34_69A7(): pass

    label("Function_34_69A7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カルバード共和国方面国境\x01",
            "    『タングラム門』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_69A7 end

    def Function_35_6A0D(): pass

    label("Function_35_6A0D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6A50")

    #C0246
    ChrTalk(
        0x101,
        (
            "#0001Fバスの停留所は……\x01",
            "たしか駐車場の方だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AA8")

    label("loc_6A50")


    #C0247
    ChrTalk(
        0x101,
        (
            "#0001Fバスの停留所は……\x01",
            "たしか駐車場の方だ。\x02\x03",

            "早くしないとバスに乗り遅れるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_6AA8")

    SetChrPos(0x0, -45520, 0, -30, 90)
    EventEnd(0x5)
    Return()

    # Function_35_6A0D end

    SaveToFile()

Try(main)
