from ZeroScenarioHelper import *

def main():
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
        "诺威队员",               # 1
        "戴蒙队员",               # 2
        "加利森队员",             # 3
        "巴雷尔队员",             # 4
        "阿雷库瑟队员",           # 5
        "商人",                   # 6
        "游客",                   # 7
        "女孩",                   # 8
        "游客",                   # 9
        "商人",                   # 10
        "游客",                   # 11
        "女孩",                   # 12
        "游客",                   # 13
        "游客",                   # 14
        "游客罗恩",               # 15
        "游客阿鲁菲特",           # 16
        "诺艾尔上士",             # 17
        "索妮亚副司令",           # 18
        "新队员",                 # 19
        "新队员",                 # 20
        "新队员",                 # 21
        "新队员",                 # 22
        "巴士",                   # 23
        "巴士司机",               # 24
        "车１",                   # 25
        "bt2500",                 # 26
        "bt2500",                 # 27
        "东克洛斯贝尔街道",       # 28
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

    PlaceName(-71.0, 0.0, -8.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
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
        "Function_6_CEE",          # 06, 6
        "Function_7_DD5",          # 07, 7
        "Function_8_EF1",          # 08, 8
        "Function_9_F86",          # 09, 9
        "Function_10_1520",        # 0A, 10
        "Function_11_160F",        # 0B, 11
        "Function_12_161D",        # 0C, 12
        "Function_13_1C5C",        # 0D, 13
        "Function_14_22E8",        # 0E, 14
        "Function_15_290E",        # 0F, 15
        "Function_16_2EF7",        # 10, 16
        "Function_17_2FDD",        # 11, 17
        "Function_18_304C",        # 12, 18
        "Function_19_30A9",        # 13, 19
        "Function_20_30E1",        # 14, 20
        "Function_21_3114",        # 15, 21
        "Function_22_3186",        # 16, 22
        "Function_23_31CF",        # 17, 23
        "Function_24_3201",        # 18, 24
        "Function_25_327F",        # 19, 25
        "Function_26_3305",        # 1A, 26
        "Function_27_33EB",        # 1B, 27
        "Function_28_34C4",        # 1C, 28
        "Function_29_34C8",        # 1D, 29
        "Function_30_39F0",        # 1E, 30
        "Function_31_407C",        # 1F, 31
        "Function_32_4C65",        # 20, 32
        "Function_33_5DFB",        # 21, 33
        "Function_34_61DA",        # 22, 34
        "Function_35_6236",        # 23, 35
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA5")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E2, 1)"), scpexpr(EXPR_END)), "loc_C37")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_CA0")

    label("loc_C37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x5E2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_CA0")

    Jump("loc_CE2")

    label("loc_CA5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
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

    label("loc_CE2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BB8 end

    def Function_6_CEE(): pass

    label("Function_6_CEE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市东出口\x01",      # 0
            "阿尔摩利卡村\x01",            # 1
            "巴士站（三叉路）\x01",        # 2
            "放弃\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D88")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_DCD")

    label("loc_D88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAD")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_DCD")

    label("loc_DAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DCD")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_DCD")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_CEE end

    def Function_7_DD5(): pass

    label("Function_7_DD5")

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

    def lambda_EAB():
        OP_95(0xFE, -27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_EAB)
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

    # Function_7_DD5 end

    def Function_8_EF1(): pass

    label("Function_8_EF1")

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

    # Function_8_EF1 end

    def Function_9_F86(): pass

    label("Function_9_F86")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1518")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动。\x01",      # 0
            "在此处休息\x01",                    # 1
            "放弃\x01",                          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B5")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1030")
    MenuCmd(1, 1, "★克洛斯贝尔市·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_104C")

    label("loc_1030")

    MenuCmd(1, 1, "　克洛斯贝尔市·中央广场")

    label("loc_104C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107E")
    MenuCmd(1, 1, "★克洛斯贝尔市·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_1098")

    label("loc_107E")

    MenuCmd(1, 1, "　克洛斯贝尔市·东出口")

    label("loc_1098")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CA")
    MenuCmd(1, 1, "★克洛斯贝尔市·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_10E4")

    label("loc_10CA")

    MenuCmd(1, 1, "　克洛斯贝尔市·西出口")

    label("loc_10E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1116")
    MenuCmd(1, 1, "★克洛斯贝尔市·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_1130")

    label("loc_1116")

    MenuCmd(1, 1, "　克洛斯贝尔市·南出口")

    label("loc_1130")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1162")
    MenuCmd(1, 1, "★克洛斯贝尔市·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_117C")

    label("loc_1162")

    MenuCmd(1, 1, "　克洛斯贝尔市·北出口")

    label("loc_117C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A4")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_11B4")

    label("loc_11A4")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_11B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DC")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_11EC")

    label("loc_11DC")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_11EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121A")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_1230")

    label("loc_121A")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_1230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125A")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_126C")

    label("loc_125A")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_126C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1296")
    MenuCmd(1, 1, "★矿山镇玛因兹")
    MenuCmd(3, 1, 0x9)
    Jump("loc_12A8")

    label("loc_1296")

    MenuCmd(1, 1, "　矿山镇玛因兹")

    label("loc_12A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D8")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_12F0")

    label("loc_12D8")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_12F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1316")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_1324")

    label("loc_1316")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_1324")

    MenuCmd(1, 1, "  放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A6")
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
        (0, "loc_13F9"),
        (1, "loc_1407"),
        (2, "loc_1415"),
        (3, "loc_1423"),
        (4, "loc_1431"),
        (5, "loc_143F"),
        (6, "loc_144D"),
        (7, "loc_145B"),
        (8, "loc_1469"),
        (9, "loc_1477"),
        (10, "loc_1485"),
        (11, "loc_1493"),
        (SWITCH_DEFAULT, "loc_14A1"),
    )


    label("loc_13F9")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1407")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1415")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1423")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1431")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_143F")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_144D")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_145B")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1469")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1477")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1485")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_1493")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_14A1")

    label("loc_14A1")

    Jump("loc_14B0")

    label("loc_14A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14B0")

    Jump("loc_1513")

    label("loc_14B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1500")
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
    Jump("loc_1513")

    label("loc_1500")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1513")

    Jump("loc_FA0")

    label("loc_1518")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_F86 end

    def Function_10_1520(): pass

    label("Function_10_1520")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15F4")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_15FA")

    label("loc_15F4")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_15FA")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1520 end

    def Function_11_160F(): pass

    label("Function_11_160F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_160F end

    def Function_12_161D(): pass

    label("Function_12_161D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1694")

    #C0005
    ChrTalk(
        0xFE,
        (
            "诺艾尔上士一大早就\x01",
            "去克洛斯贝尔大圣堂了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "好像是去把上次的遗迹报告书\x01",
            "交给艾拉尔达大主教。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1713")

    #C0007
    ChrTalk(
        0xFE,
        (
            "任务都得靠诺艾尔上士和\x01",
            "你们支援科来完成，\x01",
            "我们都觉得自己很窝囊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "我们这些普通队员\x01",
            "也必须变得更强啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1843")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F7")

    #C0009
    ChrTalk(
        0xFE,
        (
            "上次纪念庆典结束的时候我请了一天假，\x01",
            "然后到阿尔摩利卡村去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "虽然已经是快一个月前的事了，\x01",
            "但不知道是不是因为那次的放松，\x01",
            "我觉得自己最近的精神状态一直都很好。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "好，我今天也会努力工作的！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_183E")

    label("loc_17F7")


    #C0012
    ChrTalk(
        0xFE,
        (
            "身体太疲惫的话，\x01",
            "工作效率就会下降。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "适当的休息果然十分重要。\x02",
    )

    CloseMessageWindow()

    label("loc_183E")

    Jump("loc_1C58")

    label("loc_1843")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18C4")

    #C0014
    ChrTalk(
        0xFE,
        (
            "唔……\x01",
            "又是一轮返乡潮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "本来我明天是要休假的，\x01",
            "但这两天工作很忙，\x01",
            "所以我正在考虑要不要把休假推延一天。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1913")

    #C0016
    ChrTalk(
        0xFE,
        (
            "回共和国的游客\x01",
            "渐渐多起来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "明天应该会很拥挤吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1A86")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199A")

    #C0018
    ChrTalk(
        0xFE,
        (
            "……其实，\x01",
            "纪念庆典结束后，\x01",
            "我准备请一天假。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "做一回游客，\x01",
            "去阿尔摩利卡村\x01",
            "好好放松下。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F4")

    label("loc_199A")


    #C0020
    ChrTalk(
        0xFE,
        (
            "只要好好完成工作，\x01",
            "索妮亚司令应该\x01",
            "会允许我请假。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "但最近的工作肯定会非常辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_19F4")

    Jump("loc_1A81")

    label("loc_19F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_1A59")

    #C0022
    ChrTalk(
        0xFE,
        (
            "在刚才经过这里的人群中，\x01",
            "竟然混有假货贩子吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……嗯……\x01",
            "是谁呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A81")

    label("loc_1A59")


    #C0024
    ChrTalk(
        0xFE,
        "呼啊～……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "……糟糕，不好了。\x02",
    )

    CloseMessageWindow()

    label("loc_1A81")

    Jump("loc_1C58")

    label("loc_1A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B0F")

    #C0026
    ChrTalk(
        0xFE,
        (
            "昨天从共和国那边来的\x01",
            "游客蜂拥而至，\x01",
            "我都忙得快累趴下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "入境量暂时应该还不会减少吧，\x01",
            "必须要打起十二分精神才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C58")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B89")

    #C0028
    ChrTalk(
        0xFE,
        (
            "管理唐古拉姆门的\x01",
            "索妮亚副司令\x01",
            "非常有能力。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "实际上，说她是\x01",
            "警备队的一把手也不为过哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BE4")

    label("loc_1B89")


    #C0030
    ChrTalk(
        0xFE,
        "要是没那个司令就好了……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "……啊，抱歉。刚才是我失言了，\x01",
            "你们就当什么也没听到吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE4")

    Jump("loc_1C58")

    label("loc_1BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C58")

    #C0032
    ChrTalk(
        0xFE,
        (
            "最近，唐古拉姆门的前方\x01",
            "经常发生搬运车的事故。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "路上明明就没有什么障碍物，\x01",
            "到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C58")

    TalkEnd(0xFE)
    Return()

    # Function_12_161D end

    def Function_13_1C5C(): pass

    label("Function_13_1C5C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1CE9")

    #C0034
    ChrTalk(
        0xFE,
        (
            "我从过往行人那里听来了一个\x01",
            "令人不安的传闻……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "据说克洛斯贝尔市\x01",
            "昨天发生了一场混战。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "……气氛真让人不安啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_1CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D94")

    #C0037
    ChrTalk(
        0xFE,
        (
            "感谢你们协助\x01",
            "诺艾尔上士调查遗迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "特别任务支援科\x01",
            "果然名不虚传啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "我们欠了你们一份人情，\x01",
            "如果有什么需要帮忙的，\x01",
            "请随时提出来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DF0")

    label("loc_1D94")


    #C0040
    ChrTalk(
        0xFE,
        (
            "唐古拉姆部队欠了\x01",
            "特别任务支援科一份人情……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "如果有什么需要帮忙的，\x01",
            "请随时提出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF0")

    Jump("loc_22E4")

    label("loc_1DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1F31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F10")

    #C0042
    ChrTalk(
        0xFE,
        "诺艾尔上士，您辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x109,
        (
            "#0500F你也辛苦了，\x01",
            "共和国方面有什么异常吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "报告，没有异常！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "入境的游客之间\x01",
            "也没有发生什么纠纷。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x109,
        (
            "#0503F我知道了。\x01",
            "接下来，我要与特别任务支援科\x01",
            "的各位前往那个遗迹。\x02\x03",

            "#0501F后续警备的工作就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "遵命！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F2C")

    label("loc_1F10")


    #C0048
    ChrTalk(
        0xFE,
        "唐古拉姆门，没有异常！\x02",
    )

    CloseMessageWindow()

    label("loc_1F2C")

    Jump("loc_22E4")

    label("loc_1F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FA9")

    #C0049
    ChrTalk(
        0xFE,
        "今日是纪念庆典的最后一天了啊……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "在这里的游客应该\x01",
            "都对闭幕式没兴趣吧。\x01",
            "……感觉真是目光短浅呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_1FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1FFB")

    #C0051
    ChrTalk(
        0xFE,
        (
            "人真多啊……\x01",
            "要是能多增加几班前往\x01",
            "共和国的定期巴士就好了啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_1FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_21C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_209F")

    #C0052
    ChrTalk(
        0xFE,
        (
            "虽然从共和国那边来的游客\x01",
            "已经有所减少……\x01",
            "但回程大潮似乎也快到了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "从明天开始，\x01",
            "应该就会陆续有人踏上\x01",
            "返回共和国的归途了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_209F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xD)"), scpexpr(EXPR_END)), "loc_20DE")

    #C0054
    ChrTalk(
        0xFE,
        (
            "那位黑发的女性……\x01",
            "好像有很多故事呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C3")

    label("loc_20DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2178")

    #C0055
    ChrTalk(
        0xFE,
        (
            "诺威这家伙，\x01",
            "竟然敢打哈欠。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "要是被索妮亚副司令看到了，我可不管他。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0057
    ChrTalk(
        0xFE,
        (
            "话说回来，你们是\x01",
            "警察局的什么科来着？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2178")


    #C0058
    ChrTalk(
        0xFE,
        (
            "找索妮亚副司令的话，\x01",
            "进去里面上二楼就行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "她现在应该在司令室。\x02",
    )

    CloseMessageWindow()

    label("loc_21C3")

    Jump("loc_22E4")

    label("loc_21C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2233")

    #C0060
    ChrTalk(
        0xFE,
        (
            "纪念庆典，虽然我也很想去玩玩……\x01",
            "不过实在太忙了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "贝尔加德门那边应该也一样吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_2233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2299")

    #C0062
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典……\x01",
            "应该会有相当多的\x01",
            "游客通过这个门吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "……到时一定会很忙。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_2299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22E4")

    #C0064
    ChrTalk(
        0xFE,
        (
            "通过这个门后，\x01",
            "就是卡尔瓦德共和国的领土了。\x01",
            "……有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E4")

    TalkEnd(0xFE)
    Return()

    # Function_13_1C5C end

    def Function_14_22E8(): pass

    label("Function_14_22E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2374")

    #C0065
    ChrTalk(
        0xFE,
        (
            "我们这些监察国境线的警备队员，\x01",
            "真的能发挥出什么作用吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "这工作实在安稳得\x01",
            "让人闲得慌，我都盼着\x01",
            "发生点什么了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_2374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2409")

    #C0067
    ChrTalk(
        0xFE,
        (
            "巴雷尔那家伙这么快\x01",
            "就重新回到了岗位，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "身为警备队员，却被怪物吓得昏倒，\x01",
            "这实在是太丢脸了，\x01",
            "所以他才会急着复归吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_2409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2465")

    #C0069
    ChrTalk(
        0xFE,
        (
            "巴雷尔那家伙……\x01",
            "没事吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "不行不行，\x01",
            "得集中注意力，做好警备工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24CA")

    #C0071
    ChrTalk(
        0xFE,
        (
            "开往共和国的巴士接二连三地\x01",
            "从我的脚下出发……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "……纪念庆典终于要结束了吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_24CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_252C")

    #C0073
    ChrTalk(
        0xFE,
        "接待处好像越来越忙了。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "不行不行，实在太悠闲了，\x01",
            "忍不住打了个呵欠。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_252C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_25C5")

    #C0075
    ChrTalk(
        0xFE,
        (
            "看到共和国的人\x01",
            "和和气气地入境，\x01",
            "总算安心了许多。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "因为在互不侵犯条约缔结前，\x01",
            "到处都横行着一些恐怖分子。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "和平果然是最重要的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_25C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2656")

    #C0078
    ChrTalk(
        0xFE,
        (
            "昨天这里的情景\x01",
            "很壮观哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "从共和国那边来的\x01",
            "人和导力巴士络绎不绝……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "除了行军之外，\x01",
            "我还是第一次看到那么壮观的人流。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_290A")

    label("loc_2656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_27BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2737")

    #C0081
    ChrTalk(
        0xFE,
        (
            "卡尔瓦德到这里\x01",
            "有一大段距离，所以视野非常好。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "虽然不能因此而放松警戒……\x01",
            "但真是觉得这边要比贝尔加德门好得多。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "因为掌管那里的\x01",
            "是一个无能的司令。\x02",
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
    Jump("loc_27B6")

    label("loc_2737")


    #C0085
    ChrTalk(
        0xFE,
        (
            "被分配到唐古拉姆门的我们\x01",
            "从某种意义上来说十分幸运。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "因为不是受无能司令的领导，\x01",
            "而是在聪明的索妮亚副司令\x01",
            "手底下做事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B6")

    Jump("loc_290A")

    label("loc_27BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_290A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2897")

    #C0087
    ChrTalk(
        0xFE,
        (
            "那条大河对面的城市，\x01",
            "是卡尔瓦德共和国的边境城市，\x01",
            "阿尔泰尔市哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "互不侵犯条约缔结之前，\x01",
            "在那座城市前面的唐古拉姆丘陵\x01",
            "经常举行大规模演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "当时我们的感觉就好像是\x01",
            "活在枪口下一样。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_290A")

    label("loc_2897")


    #C0090
    ChrTalk(
        0xFE,
        (
            "互不侵犯条约缔结之前，\x01",
            "在国境前面的唐古拉姆丘陵\x01",
            "经常有大规模的演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "那个时候的气氛\x01",
            "可以说是剑拔弩张啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290A")

    TalkEnd(0xFE)
    Return()

    # Function_14_22E8 end

    def Function_15_290E(): pass

    label("Function_15_290E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29AF")

    #C0092
    ChrTalk(
        0xFE,
        (
            "大家是怀着不同的目的\x01",
            "来到克洛斯贝尔的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "所以其中一定也有\x01",
            "很多居心不良的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "既然我们在此进行警备，\x01",
            "就要努力\x01",
            "多抓到几个坏人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_29AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2A39")

    #C0095
    ChrTalk(
        0xFE,
        (
            "我在调查那个遗迹时\x01",
            "被怪物吓晕了，\x01",
            "直到不久前才刚醒过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "实在是给各位添麻烦了。\x01",
            "我一定会努力工作，\x01",
            "偿还这份人情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A47")
    Jump("loc_2EF3")

    label("loc_2A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2AC0")

    #C0097
    ChrTalk(
        0xFE,
        (
            "虽然我十分想下去\x01",
            "帮帮他们……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "但我也不能擅自\x01",
            "离开工作岗位。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "我现在心里半是抱歉\x01",
            "半是庆幸吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2AC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B48")

    #C0100
    ChrTalk(
        0xFE,
        (
            "像这样监视共和国国境时，\x01",
            "真的觉得那里很美……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "但只要一想到那个国家也在对克洛斯贝尔\x01",
            "虎视眈眈，心情就很复杂了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BD3")

    #C0102
    ChrTalk(
        0xFE,
        (
            "啊……\x01",
            "这里的景色果然非常棒啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "如果是在克洛斯贝尔市里工作，\x01",
            "就会忙得不可开交了。\x01",
            "监视国境这份工作其实挺不错的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C95")

    #C0104
    ChrTalk(
        0xFE,
        (
            "布鲁德被分配到贝尔加德门了，\x01",
            "不知道那家伙过得好不好啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "我跟那家伙在主日学校就认识了，\x01",
            "可以说是童年玩伴哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "听说那边工作很辛苦呢……\x01",
            "希望他能万事保重。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CFB")

    label("loc_2C95")


    #C0107
    ChrTalk(
        0xFE,
        (
            "在贝尔加德门的布鲁德那家伙……\x01",
            "不知道过得好不好。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "警备队实行驻扎制，\x01",
            "所以都没机会去见见他。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFB")

    Jump("loc_2EF3")

    label("loc_2D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D90")

    #C0109
    ChrTalk(
        0xFE,
        (
            "我们警备队为了\x01",
            "不刺激帝国和共和国，\x01",
            "所以没法进行大规模的演习。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "枉费我经过拼死拼活的训练\x01",
            "才进了警备队……\x01",
            "真让人郁闷啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF3")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2EF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC1")

    #C0111
    ChrTalk(
        0xFE,
        (
            "哦……你们是\x01",
            "那个特别任务支援科的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "上个月魔兽灾害的事件多亏了你们，\x01",
            "真是辛苦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0012F哈、哈哈……\x01",
            "我们也是勉强解决的。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#0203F要是当时蔡特没来的话，\x01",
            "还不知道事情会怎样呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "喂喂，别这么谦虚了～\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "索妮亚副司令也\x01",
            "很看好你们哦，\x01",
            "你们要加油啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2EF3")

    label("loc_2EC1")


    #C0117
    ChrTalk(
        0xFE,
        (
            "索妮亚副司令也\x01",
            "很看好你们哦，\x01",
            "你们要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF3")

    TalkEnd(0xFE)
    Return()

    # Function_15_290E end

    def Function_16_2EF7(): pass

    label("Function_16_2EF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F73")

    #C0118
    ChrTalk(
        0xFE,
        (
            "我接替了\x01",
            "巴雷尔那家伙的岗位。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "要是看到那家伙现在的情况，\x01",
            "估计没有人会愿意\x01",
            "主动参与调查的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2FD9")

    label("loc_2F73")


    #C0120
    ChrTalk(
        0xFE,
        (
            "调查遗迹之后，\x01",
            "巴雷尔那家伙就一直昏迷不醒。\x01",
            "所以我接替了他的岗位。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "……不过肚子好饿啊～……\x02",
    )

    CloseMessageWindow()

    label("loc_2FD9")

    TalkEnd(0xFE)
    Return()

    # Function_16_2EF7 end

    def Function_17_2FDD(): pass

    label("Function_17_2FDD")

    TalkBegin(0xFE)

    #C0122
    ChrTalk(
        0xFE,
        "呼，到了到了。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "在克洛斯贝尔的采购任务\x01",
            "终于完成了……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "我想快点办好手续，\x01",
            "然后回共和国去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2FDD end

    def Function_18_304C(): pass

    label("Function_18_304C")

    TalkBegin(0xFE)

    #C0125
    ChrTalk(
        0xFE,
        (
            "在共和国，导力巴士\x01",
            "非常普及。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "这边的导力巴士也都是\x01",
            "共和国乌尔努公司生产的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_304C end

    def Function_19_30A9(): pass

    label("Function_19_30A9")

    TalkBegin(0xFE)

    #C0127
    ChrTalk(
        0xFE,
        (
            "妈妈，我们快去坐巴士吧，\x01",
            "我想早点去庆典玩。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_30A9 end

    def Function_20_30E1(): pass

    label("Function_20_30E1")

    TalkBegin(0xFE)

    #C0128
    ChrTalk(
        0xFE,
        (
            "嗯，\x01",
            "景色真不错啊。\x01",
            "克洛斯贝尔这边……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_30E1 end

    def Function_21_3114(): pass

    label("Function_21_3114")

    TalkBegin(0xFE)

    #C0129
    ChrTalk(
        0xFE,
        (
            "我想快点办好手续，\x01",
            "然后回共和国去……\x01",
            "但没想到会这么拥挤。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "嗯，当时要是选择乘坐\x01",
            "导力列车就好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3114 end

    def Function_22_3186(): pass

    label("Function_22_3186")

    TalkBegin(0xFE)

    #C0131
    ChrTalk(
        0xFE,
        (
            "呵呵，只要在这里等，\x01",
            "就能第一个乘上\x01",
            "前往共和国的导力巴士了！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3186 end

    def Function_23_31CF(): pass

    label("Function_23_31CF")

    TalkBegin(0xFE)

    #C0132
    ChrTalk(
        0xFE,
        (
            "有军人叔叔在呢～\x01",
            "我去让他们陪我玩吧～\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_31CF end

    def Function_24_3201(): pass

    label("Function_24_3201")

    TalkBegin(0xFE)

    #C0133
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔……\x01",
            "市区里黑手党横行，\x01",
            "实在是一个很刺激的城市。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "大陆第一的魔都……看来这\x01",
            "称号并不算是言过其实啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3201 end

    def Function_25_327F(): pass

    label("Function_25_327F")

    TalkBegin(0xFE)

    #C0135
    ChrTalk(
        0xFE,
        (
            "呼……还要换乘巴士\x01",
            "才能到克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "这对我这种老年人来说，实在很吃力。\x01",
            "要是当时乘坐较为平稳的\x01",
            "导力列车就好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_327F end

    def Function_26_3305(): pass

    label("Function_26_3305")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3383")

    #C0137
    ChrTalk(
        0xFE,
        (
            "哇～～……阿尔泰尔市\x01",
            "竟然变得那么小了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "一想到我穿过了\x01",
            "这广阔的唐古拉姆丘陵，\x01",
            "心中就无限感慨。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_33E7")

    label("loc_3383")


    #C0139
    ChrTalk(
        0xFE,
        (
            "我竟然穿过了\x01",
            "这广阔的唐古拉姆丘陵……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "……不过，其实也没什么，\x01",
            "巴士让这一切都变得简单了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E7")

    TalkEnd(0xFE)
    Return()

    # Function_26_3305 end

    def Function_27_33EB(): pass

    label("Function_27_33EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3483")

    #C0141
    ChrTalk(
        0xFE,
        (
            "站在这里的话，\x01",
            "每当导力列车经过时，脚下\x01",
            "都会随之摇晃，真是惊险十足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "虽然很开心，但美中不足的是，\x01",
            "裙子总会被风吹起来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_34C0")

    label("loc_3483")


    #C0143
    ChrTalk(
        0xFE,
        "哇哦！\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "……我得练习迅速阻止\x01",
            "裙子被风吹起的方法呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C0")

    TalkEnd(0xFE)
    Return()

    # Function_27_33EB end

    def Function_28_34C4(): pass

    label("Function_28_34C4")

    Call(0, 6)
    Return()

    # Function_28_34C4 end

    def Function_29_34C8(): pass

    label("Function_29_34C8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_38C5")
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_35E4")
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x1E)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    Jump("loc_35FB")

    label("loc_35E4")

    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0x1E)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)

    label("loc_35FB")

    OP_49()
    SetChrPos(0x1E, -63820, 0, -120, 0)
    OP_D3(0x1E, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3644")
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_365A")

    label("loc_3644")

    SetMapObjFlags(0x2, 0x1000)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    label("loc_365A")

    Sleep(2200)

    def lambda_3662():
        OP_95(0xFE, -26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3662)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_3694")
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Jump("loc_369A")

    label("loc_3694")

    Sound(485, 0, 100, 0)

    label("loc_369A")

    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1E, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_36C5")
    SetChrFlags(0x1E, 0x80)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_36FC")

    label("loc_36C5")

    SetChrPos(0x1E, -40000, 0, 2500, 0)
    OP_D3(0x1E, 0x0, 0x41EB0, 0x0, 0x0)
    OP_71(0x2, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x2)
    OP_66(0x2, 0x1)

    label("loc_36FC")

    OP_68(-50970, 1000, -460, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_37E1")
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
    Jump("loc_38B0")

    label("loc_37E1")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_389B")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_38A1")

    label("loc_389B")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_38A1")

    Sleep(500)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x7E, 1)

    label("loc_38B0")

    Call(0, 3)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_39E8")

    label("loc_38C5")

    Sleep(2500)
    SetChrPos(0x0, -54820, 0, -130, 270)
    SetChrPos(0x1, -56020, 0, -1200, 270)
    SetChrPos(0x2, -56170, 0, 1010, 270)
    SetChrPos(0x3, -57750, 0, -190, 270)
    OP_0D()

    def lambda_3912():
        OP_95(0xFE, -50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3912)

    def lambda_392C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_392C)
    Sleep(100)

    def lambda_3940():
        OP_95(0xFE, -52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3940)

    def lambda_395A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_395A)
    Sleep(120)

    def lambda_396E():
        OP_95(0xFE, -52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_396E)

    def lambda_3988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_3988)
    Sleep(90)

    def lambda_399C():
        OP_95(0xFE, -53750, 0, -190, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_399C)

    def lambda_39B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_39B6)
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

    label("loc_39E8")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_34C8 end

    def Function_30_39F0(): pass

    label("Function_30_39F0")

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
            "#11P#0501F……那么，准备开始\x01",
            "实战演习。\x02\x03",

            "形式为四对四的小组战……\x01",
            "希望各位在战斗中充分发挥\x01",
            "自己的优势，与队友互补长短。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x1A,
        (
            "#11P最近名声鹊起的特别任务支援科吗……\x01",
            "完全有资格当我们的对手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x1B,
        (
            "#11P不过，那个有名的\x01",
            "兰迪·奥兰多原来\x01",
            "也是特别任务支援科的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x1B,
        "#11P咦咦……我们没问题吧？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x1C,
        (
            "#5P但听说他之前因为作风问题\x01",
            "而被开除了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x1C,
        (
            "#5P那样的花花公子，\x01",
            "真的能厉害到哪里去吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1D,
        (
            "#5P一定要展现出我们的实力，\x01",
            "挫挫他们的锐气。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        "#12P#0203F……他们说得很嚣张哦。\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x104,
        (
            "#12P#0304F嘿……没想到新队员\x01",
            "都这么有活力啊。\x02\x03",

            "#0300F我会陪你们练练的，\x01",
            "不用客气，尽管来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x19,
        (
            "#11P#2003F……兰迪·奥兰多，\x01",
            "请不要窃窃私语。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        "#12P#0306F为、为什么只说我……！？\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x18,
        "#11P#0507F#4S#N……全员，出列！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopBGM(0x9C4)
    SetCameraDistance(16079, 1000)
    OP_68(-22750, 1900, 20090, 1000)

    def lambda_3E7F():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E7F)

    def lambda_3E99():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E99)

    def lambda_3EB3():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3EB3)

    def lambda_3ECD():
        OP_98(0xFE, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3ECD)

    def lambda_3EE7():
        OP_98(0xFE, 0x1F4, 0x0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3EE7)

    def lambda_3F01():
        OP_98(0xFE, 0x12C, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3F01)

    def lambda_3F1B():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0xFFFFFC18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3F1B)

    def lambda_3F35():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFF830, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3F35)
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
        "#12P#0005F这是……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#12P#0101F看来训练有素啊。\x02\x03",

            "虽然是新队员，\x01",
            "但还是不能小看啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x18,
        "#11P#0507F#4S#N……开始！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_64C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4072")
    Call(0, 31)
    Jump("loc_407B")

    label("loc_4072")

    OP_29(0xF, 0x1, 0x1)
    Call(0, 32)

    label("loc_407B")

    Return()

    # Function_30_39F0 end

    def Function_31_407C(): pass

    label("Function_31_407C")

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
        "#11P#0507F#4S#N到此为止！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0161
    ChrTalk(
        0x1A,
        "#11P呼……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x1B,
        "#11P果、果然很强啊……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x1C,
        (
            "#5P兰迪·奥兰多也是……\x01",
            "比传说中还要厉害……\x02",
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
            "#12P#0304F结果大概就是这样了吧。\x02\x03",

            "#0300F虽然你们作为新人来讲，\x01",
            "已经很不错了……\x02\x03",

            "但还是差\x01",
            "我们一点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x1D,
        "#5P可恶……！\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#12P#0006F兰迪，你这家伙真容易得意忘形……\x02\x03",

            "#0000F不过，警备队果然名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#12P#0100F确实。\x01",
            "只要稍微有点马虎大意，\x01",
            "我们或许就已经输了。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#12P#0200F这样一来，任务总算完成了。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x104,
        (
            "#12P#0305F嗯，也是。\x02\x03",

            "#0309F所以，副司令。\x01",
            "今天就\x01",
            "到这里吧。\x02\x03",

            "#0304F那么，罗伊德，我们去做下一个工作吧——\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 300)

    #C0170
    ChrTalk(
        0x19,
        "#11P#2005F哎呀，谁说过只进行一场战斗就结束了？\x02",
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
        "#12P#0305F……哎？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        "#12P#0005F什、什么情况啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 300)

    #C0173
    ChrTalk(
        0x19,
        "#11P#2003F……诺艾尔上士！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x18,
        "#11P#0501F#N#4S到！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_4592():
        OP_95(0xFE, -21000, 0, 23700, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4592)
    WaitChrThread(0x18, 1)

    def lambda_45B0():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_45B0)
    WaitChrThread(0x18, 1)
    Fade(500)
    SetChrChipByIndex(0x18, 0x24)
    SetChrSubChip(0x18, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0175
    ChrTalk(
        0x18,
        "#5P#0507F#4S警备队员，全体起立！\x02",
    )

    CloseMessageWindow()

    #N0176
    NpcTalk(
        0x1B,
        "警备队员们",
        "#N#4S……遵命！\x02",
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
            "#12P#0105F副、副司令？\x01",
            "您这是要……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x101, 300)

    #C0178
    ChrTalk(
        0x19,
        (
            "#11P#2004F如你们所见。\x02\x03",

            "#2001F你们接下来\x01",
            "要继续跟诺艾尔上士所指挥的\x01",
            "队员们进行战斗。\x02",
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
            "#12P#0305F怎、怎么会这样……\x01",
            "我们可没听说过还要进行二连战啊！\x02\x03",

            "#0306F而且还加上了诺艾尔，\x01",
            "四对五，这再怎么说也太……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x19,
        (
            "#11P#2005F哎呀，我提出的支援请求是\x01",
            "『参加新队员的实战演习』哦。\x02\x03",

            "#2002F所以你们应该有义务陪队员\x01",
            "一直练到产生训练效果为止吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        "#12P#0305F唔……\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x19,
        (
            "#11P#2003F而且你们刚才\x01",
            "打倒了四名新人。\x02\x03",

            "#2000F再加上诺艾尔上士，\x01",
            "就刚好实力相当了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        "#12P#0206F……是这么一回事啊。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0000F哈哈……副司令比想象中的\x01",
            "更老谋深算呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x18,
        (
            "#5P#0506F非、非常抱歉。\x01",
            "虽然这场挑战来得很唐突……\x02\x03",

            "#0501F但我也希望通过和各位的战斗，\x01",
            "来检测一下自己的实力。\x02\x03",

            "#0503F请……多多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        "#12P#0306F……啊～真是的，真没办法啊！\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#12P#0100F……这样一来，只能硬着头皮上了。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#12P#0000F嗯……既然决定要战斗了，\x01",
            "那就让我们拿出全力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        "#12P#0202F……请多指教。\x02",
    )

    CloseMessageWindow()

    def lambda_4A3F():
        OP_95(0xFE, -17000, 0, 22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4A3F)
    WaitChrThread(0x19, 1)

    def lambda_4A5D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4A5D)
    WaitChrThread(0x19, 1)

    #C0190
    ChrTalk(
        0x19,
        (
            "#11P#2004F呵呵，那么这次演习战斗……\x01",
            "由我来主持。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x19,
        "#11P#2001F#4S#N……全员，准备！！\x02",
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
            "#11P太、太好了，有诺艾尔上士在的话，\x01",
            "这次一定能赢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x1C,
        "#5P是啊，给他们点厉害看看！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)

    #C0194
    ChrTalk(
        0x101,
        (
            "#12P#0001F对方是警备队……\x01",
            "战斗的专家。\x02\x03",

            "#0007F让我们竭尽全力\x01",
            "去战斗吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        "#12P#0307F了解！\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x19,
        "#11P#2001F#4S#N……开始！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_690", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C5B")
    OP_29(0xF, 0x1, 0x3)
    Jump("loc_4C61")

    label("loc_4C5B")

    OP_29(0xF, 0x1, 0x2)

    label("loc_4C61")

    Call(0, 32)
    Return()

    # Function_31_407C end

    def Function_32_4C65(): pass

    label("Function_32_4C65")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5318")
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
        "#11P#2001F#4S#N到此为止！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0198
    ChrTalk(
        0x1A,
        (
            "#11P可、可恶……\x01",
            "还是不行吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x1D,
        (
            "#5P枉费诺艾尔上士的帮助，\x01",
            "我们真是没出息……！\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x18,
        (
            "#5P#0506F……各位果然很厉害啊。\x02\x03",

            "我还是尚不成熟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#12P#0000F哈哈，你别这么谦虚。\x01",
            "刚才我们还以为自己会输呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x104,
        (
            "#12P#0300F诺艾尔指挥的时候，\x01",
            "新队员的表现\x01",
            "比刚开始进步了许多。\x02\x03",

            "#0304F真不愧是警备队\x01",
            "备受期待的新星啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x18,
        "#5P#0509F啊、啊哈哈……过奖了。\x02",
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
            "#11P#2001F好了……你们明白了吧。\x02\x03",

            "他们那强悍的实力就是通过与\x01",
            "黑手党和魔兽战斗而磨练出来的。\x02\x03",

            "#2003F你们这些新人，\x01",
            "还十分欠缺\x01",
            "这种实战经验。\x02\x03",

            "虽然克洛斯贝尔的警备队现在\x01",
            "因为某种原因而无法进行大规模演习……\x02\x03",

            "#2001F但除了演习之外，\x01",
            "还有很多种方法可以积累经验。\x02\x03",

            "我们作为克洛斯贝尔的警备队，\x01",
            "为了更好地履行保护市民的职责，\x01",
            "必须要自强不息，不断进步。\x02",
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
        "警备队员们",
        "#N#4S遵命！！\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x19,
        (
            "#11P#2002F呵呵……回答得不错。\x02\x03",

            "作为奖励，等回去后，\x01",
            "我会给你们准备一份\x01",
            "精心制定的锻炼计划。\x02\x03",

            "#2004F在正式决定所属部门之前，\x01",
            "每天都要严格按计划进行锻炼……听明白了没有？\x02",
        )
    )

    CloseMessageWindow()

    #N0207
    NpcTalk(
        0x1B,
        "警备队员们",
        "#N（咦、咦～！！）\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#12P#0100F呵呵……这个人总是令人毫无应对之策啊。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x103,
        (
            "#12P#0200F不愧是肩负副司令重任\x01",
            "的女中豪杰呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D1B")

    label("loc_5318")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_585A")
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
        "#11P#2001F#4S#N到此为止！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0211
    ChrTalk(
        0x101,
        (
            "#12P#0010F唔……\x01",
            "输了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        (
            "#12P#0306F诺艾尔指挥的时候，\x01",
            "新队员的表现\x01",
            "比刚开始进步了许多啊。\x02\x03",

            "#0300F真不愧是警备队\x01",
            "备受期待的新星啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x18,
        (
            "#5P#0502F啊哈哈……过奖了。\x01",
            "兰迪前辈\x01",
            "你们也非常厉害了。\x02\x03",

            "#0504F要是稍微有点马虎大意，\x01",
            "我想输的就是我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x1A,
        (
            "#11P虽然侥幸赢了……\x01",
            "但无法否认我们的实力还是很不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x1D,
        "#5P嗯，我们能赢都是多亏了上士相助。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1C, 300)

    #C0216
    ChrTalk(
        0x19,
        (
            "#11P#2001F那么……经过这次演习，\x01",
            "你们都知道自己该怎么做了吧。\x02\x03",

            "他们那强悍的实力就是通过跟\x01",
            "黑手党和魔兽战斗而磨练出来的。\x02\x03",

            "#2003F你们这些新人，\x01",
            "还十分欠缺\x01",
            "这种实战经验。\x02\x03",

            "虽然克洛斯贝尔的警备队现在\x01",
            "因为某种原因而无法进行大规模演习……\x02\x03",

            "#2001F但除了演习之外，\x01",
            "还有很多种方法可以积累经验。\x02\x03",

            "我们作为克洛斯贝尔的警备队，\x01",
            "为了更好地履行保护市民的职责，\x01",
            "必须要自强不息，不断进步。\x02",
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
        "警备队员们",
        "#N#4S遵命！！\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x19,
        (
            "#11P#2002F呵呵……回答得不错。\x02\x03",

            "作为奖励，等回去后，\x01",
            "我会给你们准备一份\x01",
            "精心制定的锻炼计划。\x02\x03",

            "#2004F在正式决定所属部门之前，\x01",
            "每天都要严格按计划进行锻炼……听明白了没有？\x02",
        )
    )

    CloseMessageWindow()

    #N0219
    NpcTalk(
        0x1B,
        "警备队员们",
        "#N（咦、咦～！！）\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        "#12P#0100F呵呵……没办法跟她相比啊。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x103,
        (
            "#12P#0200F不愧是肩负副司令重任\x01",
            "的女中豪杰呢……\x02",
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
    Jump("loc_5D1B")

    label("loc_585A")

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
        "#5P#0507F#4S#N到此为止！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0223
    ChrTalk(
        0x101,
        (
            "#12P#0010F唔……\x01",
            "输了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x104,
        (
            "#12P#0310F嘁……大意了啊。\x02\x03",

            "#0306F竟然被新人打败，\x01",
            "真是丢脸丢到家了，可恶。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x1A,
        (
            "#11P虽、虽然侥幸赢了……\x01",
            "但没想到特别任务支援科竟然会这么厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x1A,
        (
            "#11P还以为我们算是\x01",
            "战斗的精英了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1D,
        (
            "#5P是啊……\x01",
            "我已近累得不行了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x1C, 300)

    #C0228
    ChrTalk(
        0x19,
        (
            "#11P#2001F那么……经过这次演习，\x01",
            "你们都知道自己该怎么做了吧。\x02\x03",

            "他们那强悍的实力就是通过跟\x01",
            "黑手党和魔兽战斗而磨练出来的。\x02\x03",

            "#2003F你们这些新人，\x01",
            "还十分欠缺\x01",
            "这种实战经验。\x02\x03",

            "虽然克洛斯贝尔的警备队现在\x01",
            "因为某种原因而无法进行大规模演习……\x02\x03",

            "#2001F但除了演习之外，\x01",
            "还有很多种方法可以积累经验。\x02\x03",

            "我们作为克洛斯贝尔的警备队，\x01",
            "为了更好地履行保护市民的职责，\x01",
            "必须要自强不息，不断进步。\x02",
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
        "警备队员们",
        "#N#4S遵命！！\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x19,
        (
            "#11P#2002F呵呵……回答得不错。\x02\x03",

            "作为奖励，等回去后，\x01",
            "我会给你们准备一份\x01",
            "精心制定的锻炼计划。\x02\x03",

            "#2004F在正式决定所属部门之前，\x01",
            "每天都要严格按计划进行锻炼……听明白了没有？\x02",
        )
    )

    CloseMessageWindow()

    #N0231
    NpcTalk(
        0x1B,
        "警备队员们",
        "#N（咦、咦～！！）\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x102,
        "#12P#0100F呵呵……没办法跟她相比啊。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#12P#0200F不愧是肩负副司令重任\x01",
            "的女中豪杰呢……\x02",
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

    label("loc_5D1B")

    TurnDirection(0x19, 0x101, 300)

    #C0234
    ChrTalk(
        0x19,
        (
            "#11P#2002F各位也辛苦了。\x02\x03",

            "托你们的福，\x01",
            "演习才会这么成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        (
            "#12P#0012F哈哈……\x01",
            "我们也有点累了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x19,
        (
            "#11P#2004F呵呵，别站在这里说话了……\x01",
            "我们先回司令室吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        "#12P#0000F好，您说得也是呢。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x5C, 0)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_4C65 end

    def Function_33_5DFB(): pass

    label("Function_33_5DFB")

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
        "#5P哦，你们也要乘坐吗？\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#12P#0000F是的，不好意思，让你们等了这么久。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x1F,
        (
            "#5P其他乘客早都上车了，\x01",
            "你们快点吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F16():
        OP_95(0xFE, -27390, 600, 24150, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5F16)
    Sleep(1500)

    def lambda_5F33():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_5F33)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x1F, 2)

    #C0241
    ChrTalk(
        0x101,
        (
            "#5P#0001F……就像刚才所说的，\x01",
            "假货贩子就混在巴士的乘客里，\x01",
            "我们的目的是把他找出来。\x02\x03",

            "在到达克洛斯贝尔市之前，\x01",
            "必须快点做出推理。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#12P#0300F没问题。\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x103,
        "#12P#0200F这是在跟时间比赛呢。\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        "#11P#0100F那我们快点上车吧。\x02",
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

    def lambda_610C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFF92A0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_610C)
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

    def lambda_617F():
        OP_9E(0xFE, 0xFFFF865C, 0xFFFFF060, 0xFFFEA070, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_617F)
    WaitChrThread(0x1E, 1)
    Sound(465, 0, 100, 0)

    def lambda_61A4():
        OP_98(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_61A4)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("e0010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_5DFB end

    def Function_34_61DA(): pass

    label("Function_34_61DA")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "卡尔瓦德共和国国境\x01",
            "  『唐古拉姆门』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_61DA end

    def Function_35_6236(): pass

    label("Function_35_6236")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_6277")

    #C0246
    ChrTalk(
        0x101,
        (
            "#0001F巴士停靠站在……\x01",
            "好像是在停车场那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C7")

    label("loc_6277")


    #C0247
    ChrTalk(
        0x101,
        (
            "#0001F巴士停靠站在……\x01",
            "好像是在停车场那边。\x02\x03",

            "不抓紧时间的话会来不及的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_62C7")

    SetChrPos(0x0, -45520, 0, -30, 90)
    EventEnd(0x5)
    Return()

    # Function_35_6236 end

    SaveToFile()

Try(main)
