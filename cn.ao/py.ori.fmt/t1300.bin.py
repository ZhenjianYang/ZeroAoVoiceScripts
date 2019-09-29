from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1300.bin",                # FileName
        "t1300",                    # MapName
        "t1300",                    # Location
        0x00B6,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x05,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -10000, 0, 0, 1, 182, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1300",                  # 0
        "琪雅",                   # 1
        "芙兰",                   # 2
        "塞茜尔",                 # 3
        "伊莉娅",                 # 4
        "莉夏",                   # 5
        "修利",                   # 6
        "艾莉",                   # 7
        "缇欧",                   # 8
        "兰迪",                   # 9
        "诺艾尔",                 # 10
        "瓦吉",                   # 11
        "蔡特",                   # 12
        "咪西",                   # 13
        "梅尔斯",                 # 14
        "柯洛娜",                 # 15
        "利玛",                   # 16
        "奇幻乐园工作人员",       # 17
        "游客",                   # 18
        "游客",                   # 19
        "游客",                   # 20
        "游客",                   # 21
        "游客",                   # 22
        "职员亨克斯",             # 23
        "游客",                   # 24
        "游客",                   # 25
        "游客",                   # 26
        "游客",                   # 27
        "游客",                   # 28
        "游客",                   # 29
        "游客",                   # 30
        "游客",                   # 31
        "游客",                   # 32
        "游客",                   # 33
        "咪雪",                   # 34
        "幻兽",                   # 35
        "幻兽",                   # 36
        "幻兽",                   # 37
        "SE控制",                 # 38
        "bt1300",                 # 39
        "镜之城方向",             # 40
        "摩天轮方向",             # 41
        "恐怖过山车方向",         # 42
        "翠雀酒店方向",           # 43
    ))

    ATBonus("ATBonus_64C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_70C", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_710", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_700", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_704", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_72C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bt1300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88701.dat", "ms88801.dat", "ms88801.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_70C", "MonsterBattlePostion_6EC", "ed7454", "ed7453", "ATBonus_64C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch08500.itc",                   # 01
        "chr/ch05200.itc",                   # 02
        "chr/ch05100.itc",                   # 03
        "chr/ch07500.itc",                   # 04
        "chr/ch10100.itc",                   # 05
        "chr/ch00100.itc",                   # 06
        "chr/ch00200.itc",                   # 07
        "chr/ch00300.itc",                   # 08
        "chr/ch02900.itc",                   # 09
        "chr/ch03000.itc",                   # 0A
        "chr/ch02710.itc",                   # 0B
        "chr/ch10200.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
        "chr/ch22700.itc",                   # 0E
        "chr/ch20700.itc",                   # 0F
        "chr/ch44500.itc",                   # 10
        "chr/ch24400.itc",                   # 11
        "chr/ch21300.itc",                   # 12
        "chr/ch20200.itc",                   # 13
        "chr/ch21900.itc",                   # 14
        "chr/ch23000.itc",                   # 15
        "apl/ch50387.itc",                   # 16
        "chr/ch00202.itc",                   # 17
        "chr/ch03002.itc",                   # 18
        "chr/ch07502.itc",                   # 19
        "chr/ch45400.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-4139,   0,       5000,    0,    389,  0x0, 0,   13,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-4989,   0,       4989,    0,    389,  0x0, 0,   14,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-4699,   0,       7539,    0,    389,  0x0, 0,   15,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(8369,    0,       5630,    225,  389,  0x0, 0,   16,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(500,     0,       -10300,  270,  389,  0x0, 0,   17,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-500,    0,       -10300,  90,   389,  0x0, 0,   18,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5309,    0,       6300,    180,  389,  0x0, 0,   19,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(5119,    0,       4349,    45,   389,  0x0, 0,   20,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(6190,    0,       5000,    270,  389,  0x0, 0,   21,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    421,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(2029,    0,       3349,    180,  389,  0x0, 0,   26,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 32,  0.0,                   -17.0,                 -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.6666669845581055,    0.20000000298023224,   1.0])

    DeclActor(3030,    0,       3660,    1000,    2029,    1500,    3350,    0x007E, 0,  42, 0x0000)

    PlaceName(0.0, 0.0, 30.0, 0x0000, 0x0000, "镜之城方向")
    PlaceName(-40.0, 0.0, 10.0, 0x0000, 0x0000, "摩天轮方向")
    PlaceName(60.0, 0.0, 10.0, 0x0000, 0x0000, "恐怖过山车方向")
    PlaceName(0.0, 0.0, -80.0, 0x0000, 0x0000, "翠雀酒店方向")
    PlaceName(10.0, 0.0, 10.0, 0x0000, 0x0053, "")

    ChipFrameInfo(2120, 0)                                       # 0

    ScpFunction((
        "Function_0_848",          # 00, 0
        "Function_1_900",          # 01, 1
        "Function_2_9BD",          # 02, 2
        "Function_3_D2F",          # 03, 3
        "Function_4_E07",          # 04, 4
        "Function_5_FF3",          # 05, 5
        "Function_6_108F",         # 06, 6
        "Function_7_1187",         # 07, 7
        "Function_8_12C5",         # 08, 8
        "Function_9_1418",         # 09, 9
        "Function_10_14E6",        # 0A, 10
        "Function_11_1618",        # 0B, 11
        "Function_12_1708",        # 0C, 12
        "Function_13_17DA",        # 0D, 13
        "Function_14_18C7",        # 0E, 14
        "Function_15_199A",        # 0F, 15
        "Function_16_1DFC",        # 10, 16
        "Function_17_1E86",        # 11, 17
        "Function_18_1F1F",        # 12, 18
        "Function_19_1FDA",        # 13, 19
        "Function_20_218F",        # 14, 20
        "Function_21_21F6",        # 15, 21
        "Function_22_223D",        # 16, 22
        "Function_23_22A1",        # 17, 23
        "Function_24_2308",        # 18, 24
        "Function_25_2354",        # 19, 25
        "Function_26_260B",        # 1A, 26
        "Function_27_26CD",        # 1B, 27
        "Function_28_2793",        # 1C, 28
        "Function_29_3F57",        # 1D, 29
        "Function_30_43E3",        # 1E, 30
        "Function_31_43FA",        # 1F, 31
        "Function_32_446C",        # 20, 32
        "Function_33_4A65",        # 21, 33
        "Function_34_4A8A",        # 22, 34
        "Function_35_4F43",        # 23, 35
        "Function_36_4F76",        # 24, 36
        "Function_37_4FA9",        # 25, 37
        "Function_38_4FDC",        # 26, 38
        "Function_39_50D4",        # 27, 39
        "Function_40_51C8",        # 28, 40
        "Function_41_5231",        # 29, 41
        "Function_42_5262",        # 2A, 42
        "Function_43_5A1B",        # 2B, 43
        "Function_44_6038",        # 2C, 44
        "Function_45_71F2",        # 2D, 45
        "Function_46_720F",        # 2E, 46
        "Function_47_722C",        # 2F, 47
        "Function_48_7249",        # 30, 48
        "Function_49_72BC",        # 31, 49
        "Function_50_732F",        # 32, 50
        "Function_51_7443",        # 33, 51
        "Function_52_7557",        # 34, 52
        "Function_53_7576",        # 35, 53
    ))


    def Function_0_848(): pass

    label("Function_0_848")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_888"),
        (1, "loc_894"),
        (2, "loc_8A0"),
        (3, "loc_8AC"),
        (4, "loc_8B8"),
        (5, "loc_8C4"),
        (6, "loc_8D0"),
        (SWITCH_DEFAULT, "loc_8DC"),
    )


    label("loc_888")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_894")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_8E8")

    label("loc_8FF")

    Return()

    # Function_0_848 end

    def Function_1_900(): pass

    label("Function_1_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_90E")
    Jump("loc_97C")

    label("loc_90E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_91C")
    Jump("loc_97C")

    label("loc_91C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_92A")
    Jump("loc_97C")

    label("loc_92A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_93B")
    Call(0, 25)
    Jump("loc_97C")

    label("loc_93B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_949")
    Jump("loc_97C")

    label("loc_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_957")
    Jump("loc_97C")

    label("loc_957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_965")
    Jump("loc_97C")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_973")
    Jump("loc_97C")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_97C")

    label("loc_97C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_990")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_9BC")

    label("loc_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_9AA")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    SetScenarioFlags(0x1, 4)
    Event(0, 29)
    Jump("loc_9BC")

    label("loc_9AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_9BC")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 5)
    Event(0, 44)

    label("loc_9BC")

    Return()

    # Function_1_900 end

    def Function_2_9BD(): pass

    label("Function_2_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9D7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)
    Jump("loc_9E9")

    label("loc_9D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9E9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_A00")
    OP_24(0x7E)
    OP_24(0x335)
    ClearScenarioFlags(0x1, 4)
    Jump("loc_ACB")

    label("loc_A00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_A1A")
    Sound(821, 1, 60, 0)
    OP_24(0x7E)
    ClearScenarioFlags(0x1, 5)
    Jump("loc_ACB")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A62")
    OP_24(0x335)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    SoundLoad(918)
    BeginChrThread(0x2D, 3, 0, 53)
    Jump("loc_ACB")

    label("loc_A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_A9C")
    OP_24(0x335)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)
    Jump("loc_ACB")

    label("loc_A9C")

    Sound(821, 1, 60, 0)
    SoundDistance(0x7E, 0xFFFFB5D2, 0xBB8, 0xFFFF26F8, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x639C, 0xBB8, 0xFFFF26F8)

    label("loc_ACB")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AE3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B8E")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x1F4, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_C5E")

    label("loc_B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_C39")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x1F4, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_C5E")

    label("loc_C39")

    SetMapObjFrame(0xFF, "water", 0x2, "loop_off")
    SetMapObjFrame(0xFF, "back00", 0x2, "loop_off")

    label("loc_C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CBF")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_CE8")

    label("loc_CBF")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)

    label("loc_CE8")

    OP_1B(0x3, 0x0, 0x26)
    OP_1B(0x2, 0x0, 0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D01")
    OP_1B(0x0, 0x0, 0x28)

    label("loc_D01")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2E")
    OP_66(0x0, 0x1)

    label("loc_D2E")

    Return()

    # Function_2_9BD end

    def Function_3_D2F(): pass

    label("Function_3_D2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D90")

    #C0001
    ChrTalk(
        0xE,
        (
            "#00102F缇欧缇欧，\x01",
            "看这边。\x02\x03",

            "我来给你和咪西\x01",
            "拍张合影。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DAB")

    label("loc_D90")


    #C0002
    ChrTalk(
        0xE,
        "#00102F好的，笑一个！\x02",
    )

    CloseMessageWindow()

    label("loc_DAB")

    Jump("loc_E03")

    label("loc_DB0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC6")
    Jump("loc_E03")

    label("loc_DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDC")
    Jump("loc_E03")

    label("loc_DDC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF2")
    Jump("loc_E03")

    label("loc_DF2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E03")

    label("loc_E03")

    TalkEnd(0xFE)
    Return()

    # Function_3_D2F end

    def Function_4_E07(): pass

    label("Function_4_E07")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2D")
    Call(0, 5)
    Jump("loc_E80")

    label("loc_E2D")


    #C0003
    ChrTalk(
        0xF,
        (
            "#00204F我终于……\x01",
            "终于来\x01",
            "主题公园玩了……\x02\x03",

            "#00202F……首先要和\x01",
            "咪西握个手……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E80")

    Jump("loc_FEF")

    label("loc_E85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9B")
    Jump("loc_FEF")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB1")
    Jump("loc_FEF")

    label("loc_EB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC7")
    Jump("loc_FEF")

    label("loc_EC7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F84")

    #C0004
    ChrTalk(
        0xF,
        (
            "#00203F我们不能一直\x01",
            "在这里玩到晚上吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00000F嗯，因为晚上还要去\x01",
            "迎宾馆参加晚餐会呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xF,
        "#00206F……唉……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#00012F（她好像很遗憾呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FEF")

    label("loc_F84")


    #C0008
    ChrTalk(
        0xF,
        (
            "#00200F如果可以，\x01",
            "本想看看晚间活动\x01",
            "中的咪西巡游呢……\x02\x03",

            "#00206F……算了，也只能等\x01",
            "下次有机会时再看了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEF")

    TalkEnd(0xFE)
    Return()

    # Function_4_E07 end

    def Function_5_FF3(): pass

    label("Function_5_FF3")

    OP_4B(0xF, 0xFF)
    OP_4B(0x14, 0xFF)

    #C0009
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "呀哈，小姑娘。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，玩得开心吗～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xF,
        "#00201F活的咪西……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00009F（哈哈，她好像真的很开心呢。）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_5_FF3 end

    def Function_6_108F(): pass

    label("Function_6_108F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1101")

    #C0013
    ChrTalk(
        0x10,
        (
            "#00303F好，这就开始\x01",
            "尽情搭讪吧。\x02\x03",

            "#00309F嘿嘿，哪里有漂亮的\x01",
            "大姐姐呢～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_112B")

    label("loc_1101")


    #C0014
    ChrTalk(
        0x10,
        (
            "#00309F嘿嘿，哪里有漂亮的\x01",
            "大姐姐呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112B")

    Jump("loc_1183")

    label("loc_1130")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1146")
    Jump("loc_1183")

    label("loc_1146")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115C")
    Jump("loc_1183")

    label("loc_115C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1172")
    Jump("loc_1183")

    label("loc_1172")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1183")

    label("loc_1183")

    TalkEnd(0xFE)
    Return()

    # Function_6_108F end

    def Function_7_1187(): pass

    label("Function_7_1187")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    Jump("loc_12C1")

    label("loc_11A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1284")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1232")

    #C0015
    ChrTalk(
        0x11,
        (
            "#10105F说起来，\x01",
            "我看到咪西了，但是没有\x01",
            "看到它的妹妹『咪雪』呢。\x02\x03",

            "#10103F嗯……大概是藏到\x01",
            "什么地方了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_127F")

    label("loc_1232")


    #C0016
    ChrTalk(
        0x11,
        (
            "#10100F咪西的妹妹『咪雪』\x01",
            "会在什么地方呢？\x02\x03",

            "#10103F我一定可以找到它的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_127F")

    Jump("loc_12C1")

    label("loc_1284")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129A")
    Jump("loc_12C1")

    label("loc_129A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B0")
    Jump("loc_12C1")

    label("loc_12B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C1")

    label("loc_12C1")

    TalkEnd(0xFE)
    Return()

    # Function_7_1187 end

    def Function_8_12C5(): pass

    label("Function_8_12C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DE")
    Jump("loc_1414")

    label("loc_12DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1371")

    #C0017
    ChrTalk(
        0x12,
        (
            "#10300F伊莉娅小姐刚才把\x01",
            "塞茜尔小姐从休息所拉走了。\x02\x03",

            "#10303F呵呵，那种强硬的方式\x01",
            "似乎也可以用来邀约女孩呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_13D2")

    label("loc_1371")


    #C0018
    ChrTalk(
        0x12,
        (
            "#10300F伊莉娅小姐那种强硬的方式\x01",
            "似乎也可以用来邀约女孩呢。\x02\x03",

            "#10309F呵呵，你也努力试试如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D2")

    Jump("loc_1414")

    label("loc_13D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13ED")
    Jump("loc_1414")

    label("loc_13ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1403")
    Jump("loc_1414")

    label("loc_1403")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1414")

    label("loc_1414")

    TalkEnd(0xFE)
    Return()

    # Function_8_12C5 end

    def Function_9_1418(): pass

    label("Function_9_1418")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1431")
    Jump("loc_14E2")

    label("loc_1431")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1447")
    Jump("loc_14E2")

    label("loc_1447")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145D")
    Jump("loc_14E2")

    label("loc_145D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D1")

    #C0019
    ChrTalk(
        0x8,
        (
            "#01111F对了，稍后还要\x01",
            "买件咪西的周边，\x01",
            "送给小滴当礼物。\x02\x03",

            "#01106F不知道我的零用钱够不够。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E2")

    label("loc_14D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E2")

    label("loc_14E2")

    TalkEnd(0xFE)
    Return()

    # Function_9_1418 end

    def Function_10_14E6(): pass

    label("Function_10_14E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FF")
    Jump("loc_1614")

    label("loc_14FF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1515")
    Jump("loc_1614")

    label("loc_1515")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152B")
    Jump("loc_1614")

    label("loc_152B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1603")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AC")

    #C0020
    ChrTalk(
        0xA,
        (
            "#05900F我的票已经\x01",
            "用掉一半了。\x02\x03",

            "#05902F呵呵，和大家一起游玩各种项目，\x01",
            "票很快就用掉了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_15FE")

    label("loc_15AC")


    #C0021
    ChrTalk(
        0xA,
        (
            "#05900F我的票已经\x01",
            "用掉一半了。\x02\x03",

            "#05903F天色渐渐开始暗了，\x01",
            "不然就回休息所吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15FE")

    Jump("loc_1614")

    label("loc_1603")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1614")

    label("loc_1614")

    TalkEnd(0xFE)
    Return()

    # Function_10_14E6 end

    def Function_11_1618(): pass

    label("Function_11_1618")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1631")
    Jump("loc_1704")

    label("loc_1631")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1647")
    Jump("loc_1704")

    label("loc_1647")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166A")
    Call(0, 12)
    Jump("loc_16D8")

    label("loc_166A")


    #C0022
    ChrTalk(
        0xB,
        (
            "#01705F对了，\x01",
            "还有什么有趣的\x01",
            "游乐设施吗？\x02\x03",

            "#01702F我要把好玩的\x01",
            "惊险型游乐设施都玩一次，\x01",
            "有什么推荐的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D8")

    Jump("loc_1704")

    label("loc_16DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F3")
    Jump("loc_1704")

    label("loc_16F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1704")

    label("loc_1704")

    TalkEnd(0xFE)
    Return()

    # Function_11_1618 end

    def Function_12_1708(): pass

    label("Function_12_1708")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0023
    ChrTalk(
        0xB,
        (
            "#01700F莉夏、修利，\x01",
            "你们也玩得很开心吧？\x02\x03",

            "#01709F我们这些做演员的人\x01",
            "也很需要转换心情，\x01",
            "今天一定要玩个痛快哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        "#01809F呵呵，说的对。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xD,
        (
            "#14003F哼、哼，不用你说\x01",
            "我也知道。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_12_1708 end

    def Function_13_17DA(): pass

    label("Function_13_17DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F3")
    Jump("loc_18C3")

    label("loc_17F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1809")
    Jump("loc_18C3")

    label("loc_1809")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182C")
    Call(0, 12)
    Jump("loc_1897")

    label("loc_182C")


    #C0026
    ChrTalk(
        0xC,
        (
            "#01805F说起来，\x01",
            "恐怖过山车的附近\x01",
            "有很多惊险型的游乐设施呢。\x02\x03",

            "#01803F伊莉娅小姐应该\x01",
            "会喜欢那一带吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1897")

    Jump("loc_18C3")

    label("loc_189C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18B2")
    Jump("loc_18C3")

    label("loc_18B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C3")

    label("loc_18C3")

    TalkEnd(0xFE)
    Return()

    # Function_13_17DA end

    def Function_14_18C7(): pass

    label("Function_14_18C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E0")
    Jump("loc_1996")

    label("loc_18E0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18F6")
    Jump("loc_1996")

    label("loc_18F6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_196F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1919")
    Call(0, 12)
    Jump("loc_196A")

    label("loc_1919")


    #C0027
    ChrTalk(
        0xD,
        (
            "#14006F这……\x01",
            "我的肚子突然有点饿了。\x02\x03",

            "#14000F我们还是先去休息所吃点东西吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196A")

    Jump("loc_1996")

    label("loc_196F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1985")
    Jump("loc_1996")

    label("loc_1985")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1996")

    label("loc_1996")

    TalkEnd(0xFE)
    Return()

    # Function_14_18C7 end

    def Function_15_199A(): pass

    label("Function_15_199A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C0")
    Call(0, 5)
    Jump("loc_1A01")

    label("loc_19C0")


    #C0028
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，\x01",
            "欢迎光临主题公园☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "一定要玩开心哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A01")

    Jump("loc_1DF8")

    label("loc_1A06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A1C")
    Jump("loc_1DF8")

    label("loc_1A1C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A32")
    Jump("loc_1DF8")

    label("loc_1A32")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B9B")

    #C0030
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，我已经听说了哦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "你们正在努力寻找\x01",
            "我妹妹咪雪吧～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "还是说……已经想认输了呢？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不认输】\x01",      # 0
            "【认输】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B93")

    #C0033
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "是吗～\x01",
            "那就加油吧☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "如果实在找不到，\x01",
            "就到我这里宣布认输吧，\x01",
            "我会转告给咪雪的～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B96")

    label("loc_1B93")

    Call(0, 43)

    label("loc_1B96")

    Jump("loc_1D05")

    label("loc_1B9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C15")

    #C0035
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "你们好像已经成功\x01",
            "找到咪雪了啊～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，那个奖品\x01",
            "可是很不错的东西，\x01",
            "一定要好好珍藏哦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D05")

    label("loc_1C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1C99")

    #C0037
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "虽说你们玩捉迷藏游戏\x01",
            "输给了咪雪，\x01",
            "但是也不必沮丧哦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "尽情游玩一番，\x01",
            "把不愉快的心情彻底抛开吧～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D05")

    label("loc_1C99")


    #C0039
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "你有没有看到过一只和我\x01",
            "长得一模一样的粉色猫咪？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "那是我的妹妹……\x01",
            "唔～到底跑到哪里了呢～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D05")

    Jump("loc_1DF8")

    label("loc_1D0A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D99")

    #C0041
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，谢谢了～！\x01",
            "我一定会加油的～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "距离天黑\x01",
            "还有点时间，\x01",
            "尽情游玩到最后时刻吧～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 0)
    Jump("loc_1DF8")

    label("loc_1D99")


    #C0043
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "我最喜欢的就是\x01",
            "孩子们的笑脸～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，顺便一说，\x01",
            "第二喜欢的是\x01",
            "巨大的甜瓜哦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DF8")

    TalkEnd(0xFE)
    Return()

    # Function_15_199A end

    def Function_16_1DFC(): pass

    label("Function_16_1DFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E15")
    Jump("loc_1E82")

    label("loc_1E15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2B")
    Jump("loc_1E82")

    label("loc_1E2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E41")
    Jump("loc_1E82")

    label("loc_1E41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E57")
    Jump("loc_1E82")

    label("loc_1E57")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E82")

    #C0045
    ChrTalk(
        0xFE,
        "是啊……真是来对了。\x02",
    )

    CloseMessageWindow()

    label("loc_1E82")

    TalkEnd(0xFE)
    Return()

    # Function_16_1DFC end

    def Function_17_1E86(): pass

    label("Function_17_1E86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9F")
    Jump("loc_1F1B")

    label("loc_1E9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB5")
    Jump("loc_1F1B")

    label("loc_1EB5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ECB")
    Jump("loc_1F1B")

    label("loc_1ECB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE1")
    Jump("loc_1F1B")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F1B")

    #C0046
    ChrTalk(
        0xFE,
        (
            "呵呵……看啊，亲爱的，\x01",
            "利玛多开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1B")

    TalkEnd(0xFE)
    Return()

    # Function_17_1E86 end

    def Function_18_1F1F(): pass

    label("Function_18_1F1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F38")
    Jump("loc_1FD6")

    label("loc_1F38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4E")
    Jump("loc_1FD6")

    label("loc_1F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F64")
    Jump("loc_1FD6")

    label("loc_1F64")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F7A")
    Jump("loc_1FD6")

    label("loc_1F7A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD6")

    #C0047
    ChrTalk(
        0xFE,
        "哇，是咪西～！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "利玛不能参加晚间活动了，\x01",
            "但你一定要加油巡游哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FD6")

    TalkEnd(0xFE)
    Return()

    # Function_18_1F1F end

    def Function_19_1FDA(): pass

    label("Function_19_1FDA")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2037")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2037")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2057")
    OP_AF(0x6C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2186")

    label("loc_2057")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206B")
    Jump("loc_2186")

    label("loc_206B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2083")
    TalkEnd(0xFE)
    Return()

    label("loc_2083")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2186")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210F")

    #C0049
    ChrTalk(
        0x18,
        (
            "欢迎，\x01",
            "这里出售多种\x01",
            "咪西周边哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x18,
        (
            "你也戴上一条咪西尾巴，\x01",
            "在主题公园里开心游玩吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2186")

    label("loc_210F")


    #C0051
    ChrTalk(
        0x18,
        (
            "要不要买些咪西的周边，\x01",
            "作为来主题公园游玩的留念呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x18,
        (
            "在返回克洛斯贝尔市之前\x01",
            "一直戴着咪西尾巴的人\x01",
            "意外地多呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2186")

    Jump("loc_1FE7")

    label("loc_218B")

    TalkEnd(0xFE)
    Return()

    # Function_19_1FDA end

    def Function_20_218F(): pass

    label("Function_20_218F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CF")

    #C0053
    ChrTalk(
        0xFE,
        (
            "去那边那个\x01",
            "新建的游乐设施玩玩吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F2")

    label("loc_21CF")


    #C0054
    ChrTalk(
        0xFE,
        (
            "难得来一次，\x01",
            "就玩到晚上好了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F2")

    TalkEnd(0xFE)
    Return()

    # Function_20_218F end

    def Function_21_21F6(): pass

    label("Function_21_21F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2227")

    #C0055
    ChrTalk(
        0xFE,
        "接下来要去哪里呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2239")

    label("loc_2227")


    #C0056
    ChrTalk(
        0xFE,
        "要回去了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2239")

    TalkEnd(0xFE)
    Return()

    # Function_21_21F6 end

    def Function_22_223D(): pass

    label("Function_22_223D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229D")

    #C0057
    ChrTalk(
        0xFE,
        (
            "我们有\x01",
            "主题公园的年票。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "这里真是太棒了，来多少次都不会腻呢！\x02",
    )

    CloseMessageWindow()
    Jump("loc_229D")

    label("loc_229D")

    TalkEnd(0xFE)
    Return()

    # Function_22_223D end

    def Function_23_22A1(): pass

    label("Function_23_22A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2304")

    #C0059
    ChrTalk(
        0xFE,
        (
            "这孩子非常\x01",
            "喜欢咪西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "陪孩子来了这么多次，\x01",
            "连我都开始沉迷了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2304")

    label("loc_2304")

    TalkEnd(0xFE)
    Return()

    # Function_23_22A1 end

    def Function_24_2308(): pass

    label("Function_24_2308")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2350")

    #C0061
    ChrTalk(
        0xFE,
        (
            "买一个、买一个～\x01",
            "给我买一个咪西玩偶嘛～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2350")

    label("loc_2350")

    TalkEnd(0xFE)
    Return()

    # Function_24_2308 end

    def Function_25_2354(): pass

    label("Function_25_2354")

    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x10)
    SetChrFlags(0x29, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240F")
    EndChrThread(0xE, 0x0)
    SetChrChipByIndex(0xE, 0x16)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -5160, 0, 3100, 315)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7100, 0, 4400, 315)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 6000, 0, -150, 180)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -8010, 0, 5260, 135)
    SetChrFlags(0x14, 0x10)
    Jump("loc_260A")

    label("loc_240F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2462")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -9350, 0, 6350, 135)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -7930, 200, 8240, 135)
    SetChrChipByIndex(0x12, 0x18)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    Jump("loc_260A")

    label("loc_2462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C9")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8320, 0, -2390, 180)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -7690, 0, -3590, 270)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -9110, 0, -3590, 90)
    SetChrFlags(0xD, 0x10)
    Jump("loc_260A")

    label("loc_24C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258A")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 7600, 0, -360, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -7930, 200, 8240, 135)
    SetChrChipByIndex(0xA, 0x19)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 0, 0, -6210, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_256A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_255C")
    SetChrFlags(0x8, 0x80)
    Jump("loc_256A")

    label("loc_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_256A")
    SetChrFlags(0xA, 0x80)

    label("loc_256A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2585")
    ClearChrFlags(0x29, 0x80)

    label("loc_2585")

    Jump("loc_260A")

    label("loc_258A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_260A")
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -7930, 200, 8240, 135)
    SetChrChipByIndex(0xF, 0x17)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -4700, 0, 8680, 180)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)

    label("loc_260A")

    Return()

    # Function_25_2354 end

    def Function_26_260B(): pass

    label("Function_26_260B")

    EventBegin(0x1)

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F◆这边是大摩天轮和休息所，\x01",
            "要去哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        240,
        1,
        (
            "去大摩天轮方向\x01",      # 0
            "去休息所\x01",            # 1
            "放弃\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2682"),
        (1, "loc_269B"),
        (SWITCH_DEFAULT, "loc_26B4"),
    )


    label("loc_2682")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_26CC")

    label("loc_269B")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_26CC")

    label("loc_26B4")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Jump("loc_26CC")

    label("loc_26CC")

    Return()

    # Function_26_260B end

    def Function_27_26CD(): pass

    label("Function_27_26CD")

    EventBegin(0x1)

    #C0063
    ChrTalk(
        0x101,
        (
            "#0000F◆这边是恐怖过山车和占卜馆，\x01",
            "要去哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        240,
        1,
        (
            "去恐怖过山车方向\x01",      # 0
            "去占卜馆\x01",              # 1
            "放弃\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2748"),
        (1, "loc_2761"),
        (SWITCH_DEFAULT, "loc_277A"),
    )


    label("loc_2748")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_2792")

    label("loc_2761")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_2792")

    label("loc_277A")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Jump("loc_2792")

    label("loc_2792")

    Return()

    # Function_27_26CD end

    def Function_28_2793(): pass

    label("Function_28_2793")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x4)
    OP_90(0x101, 0, 5000, -27000, 0)
    OP_90(0x8, -1280, 5000, -27940, 0)
    OP_90(0xF, 200, 5000, -28510, 0)
    OP_90(0xE, 1130, 5000, -28360, 0)
    OP_90(0xA, -1730, 5000, -29480, 0)
    OP_90(0xB, -650, 5000, -29360, 0)
    OP_90(0xD, 580, 5000, -29850, 0)
    OP_90(0xC, 1700, 5000, -29810, 0)
    OP_90(0x11, -340, 5000, -30690, 0)
    OP_90(0x9, -1340, 5000, -30960, 0)
    OP_90(0x12, 1010, 5000, -31210, 0)
    OP_90(0x10, -850, 5000, -32340, 0)
    OP_90(0x13, 400, 5000, -32700, 0)
    OP_68(0, 1800, -24500, 0)
    MoveCamera(0, 36, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 9000, -500, 9000)
    MoveCamera(0, 3, 0, 9000)
    SetCameraDistance(66000, 9000)
    PlaceName2(340, 200, "c_plac46", 0x0, 5000)

    def lambda_2994():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2994)

    def lambda_29A9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29A9)
    Sleep(50)

    def lambda_29C1():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_29C1)

    def lambda_29D6():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_29D6)
    Sleep(50)

    def lambda_29EE():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_29EE)

    def lambda_2A03():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2A03)

    def lambda_2A18():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2A18)
    Sleep(50)

    def lambda_2A30():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A30)

    def lambda_2A45():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2A45)

    def lambda_2A5A():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A5A)
    Sleep(50)

    def lambda_2A72():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A72)

    def lambda_2A87():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A87)

    def lambda_2A9C():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2A9C)
    OP_6F(0x79)
    Fade(1000)
    OP_68(0, 1000, 0, 0)
    OP_68(0, 1000, -8000, 5500)
    MoveCamera(0, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x8, 1)
    Sleep(300)
    #Sound(3033, 255, 100, 0)    #voice#KeA

    #C0064
    ChrTalk(
        0x8,
        "#01109F#15A#4S哇哇哇……！\x02",
    )
    #Auto

    CloseMessageWindow()
    WaitChrThread(0xF, 1)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x11, 1)
    WaitChrThread(0x12, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 0x1E)
    SetChrSubChip(0x13, 0x0)
    BeginChrThread(0x13, 3, 0, 0)
    OP_6F(0x79)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#00002F这里就是米修拉姆奇幻乐园……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xF,
        "#00203F……………………（深呼吸）\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xD,
        "#14005F……好、好棒啊……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "#01705F嘿，我也是第一次来，\x01",
            "看起来好像很有趣嘛。\x02\x03",

            "#01709F游乐设施似乎\x01",
            "相当多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x10,
        (
            "#00309F哈，反正一天是\x01",
            "不可能玩遍的。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x12,
        (
            "#10304F我们今天已经在\x01",
            "湖水浴场玩了一上午……\x02\x03",

            "#10302F既然现在才入场，就以代表性的\x01",
            "设施为中心来游玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "#05905F代表性的设施\x01",
            "都有什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "#06403F嗯……左手边那个可以望到的\x01",
            "摩天轮自然不能不坐。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(325, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    #C0073
    ChrTalk(
        0x9,
        (
            "#06409F无论是全家出行的游客还是\x01",
            "来此约会的情侣，都对它赞不绝口。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x11,
        (
            "#10109F确实是最棒的眺望地点呢。\x02\x03",

            "#10102F作为愉快一天的收尾，\x01",
            "留到最后去享受也是很不错的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        "#01702F嗯嗯，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xC,
        (
            "#01809F呵呵……\x01",
            "我也开始兴奋起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xE,
        (
            "#00102F说起代表性的设施……\x01",
            "中央的那座『城堡』也不能不提。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(0, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    #C0078
    ChrTalk(
        0xE,
        (
            "#00100F『镜之城』──可以算是\x01",
            "这座主题公园的象征呢。\x02\x03",

            "#00104F最上层还有一面\x01",
            "『实现愿望的镜子』……\x02\x03",

            "#00102F听说只要先将钟敲响，\x01",
            "然后再立于镜前，就可以实现心愿了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#05909F呀，真浪漫呢。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x10,
        (
            "#00304F嗯，去那里的人大多都是\x01",
            "情侣或全家出行的游客。\x02\x03",

            "#00300F毕竟敲钟的钟绳有两条，\x01",
            "而且悬挂在大钟的左右两侧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#00011F那、那一个人去敲的话，\x01",
            "好像确实是挺孤单的。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        "#01101F你们看！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 10500, -7500, 3000)
    MoveCamera(35, 0, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11000, 3000)
    OP_6F(0x79)

    #C0083
    ChrTalk(
        0x8,
        (
            "#01110F那边那座房子里\x01",
            "是不是住着什么人？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xD,
        (
            "#14011F那、那座房子\x01",
            "看起来好阴森啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x10,
        (
            "#00305F我也不知道那是什么……\x01",
            "是最近才建成的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "#06404F嗯，好像是这座主题公园中\x01",
            "最新的游乐设施呢。\x02\x03",

            "#06402F叫做『恐怖过山车』，\x01",
            "听说气氛相当逼真呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xF,
        (
            "#00204F我也查到过\x01",
            "有关它的情报。\x02\x03",

            "#00202F好像是使用了最新\x01",
            "技术的恐怖刺激型\x01",
            "游乐设施。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xE,
        (
            "#00106F竟、竟然新建了\x01",
            "那种东西……\x02\x03",

            "#00111F……贝尔真是的，\x01",
            "一直都没和我提过……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -300, 0, -7000, 180)
    SetChrPos(0x8, -1280, 0, -7940, 135)
    SetChrPos(0xF, 200, 0, -8510, 180)
    SetChrPos(0xE, 1130, 0, -8360, 225)
    SetChrPos(0xA, -1730, 0, -9280, 90)
    SetChrPos(0xB, -750, 0, -9360, 90)
    SetChrPos(0xD, 580, 0, -9850, 270)
    SetChrPos(0xC, 1700, 0, -9810, 270)
    SetChrPos(0x11, -340, 0, -10940, 0)
    SetChrPos(0x9, -1340, 0, -10960, 45)
    SetChrPos(0x12, 1010, 0, -11210, 315)
    SetChrPos(0x10, -850, 0, -12340, 0)
    SetChrPos(0x13, 400, 0, -12700, 0)
    OP_68(0, 1500, -9600, 0)
    OP_68(0, 1000, -9600, 2000)
    MoveCamera(315, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0089
    ChrTalk(
        0xB,
        (
            "#01709F嗯嗯，真不错！\x01",
            "我的情绪越来越高涨啦！\x02\x03",

            "#01700F还有其它的必玩项目吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x12,
        (
            "#10304F#6P虽然不是游乐设施，\x01",
            "但『占卜馆』也是一定要去的。\x02\x03",

            "#10300F有传闻说，去年新来\x01",
            "的占卜师相当厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#06403F嗯，听说无论是测算缘分\x01",
            "还是寻找失物，全都准确无比。\x02\x03",

            "#06400F好像是一位气质神秘，\x01",
            "具有异国风情的美女占卜师。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "#01805F#12P这……\x01",
            "真让人有些兴趣呢。\x02\x03",

            "#01808F（是东方的占卜术士吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xF,
        (
            "#00203F……说起来，\x01",
            "『追踪咪西』也是\x01",
            "不能错过的游玩项目。\x02\x03",

            "#00201F在园内追赶到处巡游\x01",
            "的咪西是很有意思的。\x02\x03",

            "#00207F如果运气好的话，\x01",
            "还有可能遇到\x01",
            "咪西的妹妹『咪雪』……！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00012F#11P是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10,
        "#00301F#6P阿缇的目光好认真啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0096
    ChrTalk(
        0xA,
        (
            "#05905F对了……\x02\x03",

            "#05900F有什么可以休息\x01",
            "的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x13B, 0x1F4)

    #C0097
    ChrTalk(
        0x11,
        (
            "#10105F#6P哦，走过左边那座桥，\x01",
            "有个休息所。\x02\x03",

            "#10100F那里还出售\x01",
            "零食之类的东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1300, -9600, 1500)

    def lambda_36AA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36AA)

    def lambda_36B7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_36B7)
    Sleep(50)

    def lambda_36C7():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_36C7)

    def lambda_36D4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_36D4)
    Sleep(50)

    def lambda_36E4():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_36E4)

    def lambda_36F1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_36F1)
    Sleep(50)

    def lambda_3701():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3701)

    def lambda_370E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_370E)
    Sleep(50)

    def lambda_371E():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_371E)

    def lambda_372B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_372B)
    Sleep(50)

    def lambda_373B():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_373B)

    def lambda_3748():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3748)

    def lambda_3755():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3755)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x13, 2)
    OP_6F(0x79)

    #C0098
    ChrTalk(
        0xA,
        (
            "#05904F既然如此，我们就把那里\x01",
            "当作集合地点吧。\x02\x03",

            "#05902F我会尽量留在那里，\x01",
            "如果大家出现贫血现象，或是感到\x01",
            "身体不适，请不必客气，尽管来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00006F#11P塞茜尔姐姐，没必要在这种时候\x01",
            "也主动担负护士的义务啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        "#00108F#12P是啊，那样也太不好意思了。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "#00303F#6P……不过，仔细想想，\x01",
            "这正是可以被塞茜尔小姐\x01",
            "温柔照料的大好机会啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xF,
        (
            "#00211F#12P兰迪前辈，\x01",
            "别把真实想法说出来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        (
            "#01706F#11P总之，差不多就行了，\x01",
            "你也要玩得尽兴些哦。\x02\x03",

            "#01702F平时都没什么机会玩，\x01",
            "这种时候一定要好好补偿！\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xA,
        (
            "#05909F呵呵，知道了，\x01",
            "那就恭敬不如从命啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, -9600, 1500)
    Sleep(500)

    def lambda_39D9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_39D9)
    Sleep(50)

    def lambda_39E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_39E9)
    Sleep(50)

    def lambda_39F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_39F9)
    Sleep(50)

    def lambda_3A09():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3A09)
    Sleep(50)

    def lambda_3A19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3A19)
    Sleep(50)

    def lambda_3A29():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3A29)
    Sleep(50)

    def lambda_3A39():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3A39)
    Sleep(50)

    def lambda_3A49():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3A49)
    Sleep(50)

    def lambda_3A59():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3A59)
    Sleep(50)

    def lambda_3A69():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A69)
    Sleep(50)

    def lambda_3A79():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3A79)
    Sleep(50)

    def lambda_3A89():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3A89)
    Sleep(50)

    def lambda_3A99():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3A99)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x8, 2)
    WaitChrThread(0xF, 2)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x13, 2)
    OP_6F(0x79)

    #C0105
    ChrTalk(
        0x101,
        (
            "#00003F#11P晚上还要去参加晚餐会，\x01",
            "所以我们只能玩到傍晚左右……\x02\x03",

            "#00000F好啦，票已经发到大家手中了，\x01",
            "我们接下来就自由行动吧。\x02\x03",

            "#00002F要是想玩什么游乐设施，\x01",
            "就去找伙伴一起进去……\x02\x03",

            "这样可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xE,
        "#00109F#6P嗯，这样很好啊。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xF,
        "#00204F#6P明白了。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        "#01802F#6P知道啦。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x10,
        "#00309F#6P好，去玩喽～！\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        "#06409F#6P超级兴奋呢！\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x11,
        "#10112F#6P啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x12,
        "#10304F#6P哎呀呀，真有精神啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x8, 0x87, 0x1F4)
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x7D0, 0x0)

    #C0113
    ChrTalk(
        0x8,
        (
            "#01109F#5P修利修利！\x01",
            "我们一起去逛吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xD, 0x13B, 0x1F4)
    Sleep(1000)
    OP_64(0xD)

    #C0114
    ChrTalk(
        0xD,
        "#14011F#12P都、都说过不要拽我啦！\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xB,
        (
            "#01709F#6P啊哈哈，不由得\x01",
            "回想起了学生时代呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "#05909F#6P呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x13,
        "#01203F#6P咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0118
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了五张。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x35D, 5)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在主题公园内，\x01",
            "可以去『摩天轮』、『镜之城』、\x01",
            "『占卜馆』、『恐怖过山车』四处场所游玩。\x02\x03",

            "在各场所的检票处选择同行伙伴，\x01",
            "并使用一张票，\x01",
            "即可开始游玩。\x02\x03",

            "当五张票全部用完后，主线剧情就会继续进展，\x01",
            "因此在使用之前请谨慎决定\x01",
            "要玩的项目及同行伙伴。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, -6750, 0)
    SetScenarioFlags(0x145, 4)
    OP_29(0xA5, 0x1, 0x6)
    EndChrThread(0x13, 0x3)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    OP_49()
    OP_D7(0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_4C(0x8, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xC, 0xFF)
    Call(0, 25)
    EventEnd(0x5)
    Return()

    # Function_28_2793 end

    def Function_29_3F57(): pass

    label("Function_29_3F57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_4B(0x8, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0x13, 0x4)
    SetChrPos(0x8, 0, 0, -10000, 0)
    SetChrPos(0xF, -1000, 0, -10000, 0)
    SetChrPos(0x9, 1000, 0, -10000, 0)
    SetChrPos(0xA, -1500, 0, -11250, 0)
    SetChrPos(0xB, -500, 0, -11250, 0)
    SetChrPos(0xD, 500, 0, -11250, 0)
    SetChrPos(0xC, 1500, 0, -11250, 0)
    SetChrPos(0x11, -1000, 0, -12500, 0)
    SetChrPos(0xE, 0, 0, -12500, 0)
    SetChrPos(0x12, 1000, 0, -12500, 0)
    SetChrPos(0x10, -500, 0, -13750, 0)
    SetChrPos(0x101, 500, 0, -13750, 0)
    SetChrPos(0x13, -1500, 0, -15000, 0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrFlags(0xF, 0x8000)
    OP_4B(0x14, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 0, 0, -7500, 180)
    OP_4B(0x18, 0xFF)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 1000, 0, -7000, 180)
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrName("")

    #A0120
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W就这样，快乐的时光\x01",
            "转瞬即逝。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-870, 1030, -9460, 0)
    MoveCamera(310, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    PlayBGM("ed7514", 0)
    SetCameraDistance(17500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_63(0x14, 0x0, 2300, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    SetCameraDistance(25000, 15000)
    OP_68(0, 1500, -12000, 15000)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(150)
    BeginChrThread(0x10, 3, 0, 30)
    Sleep(100)
    BeginChrThread(0x13, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 30)
    Sleep(150)
    BeginChrThread(0x11, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0x12, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 30)
    Sleep(400)
    BeginChrThread(0xA, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0xD, 3, 0, 30)
    Sleep(200)
    BeginChrThread(0xC, 3, 0, 30)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 30)
    Sleep(250)
    BeginChrThread(0x9, 3, 0, 30)
    Sleep(400)
    BeginChrThread(0xF, 3, 0, 31)
    Sleep(500)
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#35A#40W罗伊德等人放弃了刚刚开始的晚间活动，\x01",
            "恋恋不舍地离开了主题公园……\x02\x03",

            "#35A#40W一行人暂且返回酒店，\x01",
            "随后准备前往迎宾馆参加晚餐会。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3F57 end

    def Function_30_43E3(): pass

    label("Function_30_43E3")

    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
    Return()

    # Function_30_43E3 end

    def Function_31_43FA(): pass

    label("Function_31_43FA")

    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x32C8, 0x7D0, 0x0)
    Return()

    # Function_31_43FA end

    def Function_32_446C(): pass

    label("Function_32_446C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\cr036301.eff")
    SetChrPos(0x101, 100, 0, -21000, 0)
    SetChrPos(0x102, 800, 0, -22100, 0)
    SetChrPos(0x103, -750, 0, -21900, 0)
    SetChrPos(0x104, -100, 0, -23000, 0)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x1, 0x2A)
    OP_49()
    SetChrPos(0x2A, 0, 0, -8500, 180)
    OP_D5(0x2A, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2A, 0x8000)
    OP_75(0x1, 0x1, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x2, 0x2B)
    OP_49()
    SetChrPos(0x2B, -4000, 0, -7000, 165)
    OP_D5(0x2B, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2B, 0x8000)
    OP_75(0x2, 0x1, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x3, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, -7000, 195)
    OP_D5(0x2C, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2C, 0x8000)
    OP_75(0x3, 0x1, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, 0, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20000, 4000)
    OP_6F(0x79)
    OP_68(0, 1000, -12000, 4500)
    MoveCamera(0, 20, 0, 4500)
    SetCameraDistance(15000, 4500)

    def lambda_467D():
        OP_9B(0x0, 0x101, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_467D)
    Sleep(100)

    def lambda_4695():
        OP_9B(0x0, 0x102, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4695)
    Sleep(100)

    def lambda_46AD():
        OP_9B(0x0, 0x103, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_46AD)
    Sleep(100)

    def lambda_46C5():
        OP_9B(0x0, 0x104, 0x0, 0x1F40, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_46C5)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()

    #C0122
    ChrTalk(
        0x101,
        "#00010F#6P灵智之草……！\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        "#00201F#6P咪西的花坛被……！\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x2A, 0, 0, 33)
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
    Sleep(300)
    Fade(1000)
    OP_68(0, 2000, -8500, 0)
    MoveCamera(30, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(17500, 4000)
    MoveCamera(0, 20, 0, 4000)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x2A, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_4854():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_4854)

    def lambda_4865():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_4865)

    def lambda_4876():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4876)
    OP_75(0x1, 0x2, 0x3E8)
    OP_75(0x2, 0x2, 0x3E8)
    OP_75(0x3, 0x2, 0x3E8)
    WaitChrThread(0x2A, 2)
    WaitChrThread(0x2B, 2)
    WaitChrThread(0x2C, 2)
    CancelBlur(1000)
    EndChrThread(0x2A, 0x0)
    OP_6F(0x79)
    OP_68(0, 1600, -10150, 3000)
    MoveCamera(0, 14, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(17500, 3000)
    Sleep(1000)

    def lambda_48E4():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48E4)
    Sleep(50)

    def lambda_48FC():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48FC)
    Sleep(50)

    def lambda_4914():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4914)
    Sleep(50)

    def lambda_492C():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_492C)
    WaitChrThread(0x104, 1)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0124
    ChrTalk(
        0x102,
        "#00107F#12P#N这是曾出现在沼泽的……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0125
    ChrTalk(
        0x104,
        "#00310F#6P#N哼，干掉它！\x02",
    )

    CloseMessageWindow()
    OP_74(0x1, 0x14)
    OP_74(0x2, 0x14)
    OP_74(0x3, 0x14)
    OP_71(0x1, 0x5B, 0x69, 0xFA, 0x8)
    OP_71(0x2, 0x8D, 0xA0, 0xFA, 0x8)
    OP_71(0x3, 0x8D, 0xA0, 0xFA, 0x8)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(8000, 1000)
    OP_74(0x1, 0x1E)
    OP_74(0x2, 0x1E)
    OP_74(0x3, 0x1E)
    OP_71(0x1, 0x69, 0x73, 0x0, 0x8)
    OP_71(0x2, 0xA1, 0xAA, 0x0, 0x8)
    OP_71(0x3, 0xA1, 0xAA, 0x0, 0x8)
    Sleep(500)
    Battle("BattleInfo_72C", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 34)
    Return()

    # Function_32_446C end

    def Function_33_4A65(): pass

    label("Function_33_4A65")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A89")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_33_4A65")

    label("loc_4A89")

    Return()

    # Function_33_4A65 end

    def Function_34_4A8A(): pass

    label("Function_34_4A8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadEffect(0x0, "battle\\bs000000.eff")
    LoadEffect(0x1, "battle\\bs000001.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 100, 0, -13000, 0)
    SetChrPos(0x102, 800, 0, -14100, 0)
    SetChrPos(0x103, -750, 0, -13900, 0)
    SetChrPos(0x104, -100, 0, -15000, 0)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x1, 0x2A)
    OP_49()
    SetChrPos(0x2A, 0, 0, -8500, 180)
    OP_D5(0x2A, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2A, 0x8000)
    OP_75(0x1, 0x2, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x2, 0x2B)
    OP_49()
    SetChrPos(0x2B, -4000, 0, -7000, 165)
    OP_D5(0x2B, 0x0, 0x28488, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2B, 0x8000)
    OP_75(0x2, 0x2, 0x0)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0x3, 0x2C)
    OP_49()
    SetChrPos(0x2C, 4000, 0, -7000, 195)
    OP_D5(0x2C, 0x0, 0x2F9B8, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0xA, 0x32, 0x0, 0x20)
    SetChrFlags(0x2C, 0x8000)
    OP_75(0x3, 0x2, 0x0)
    OP_A7(0x2C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 2000, -8500, 0)
    MoveCamera(330, 45, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(22500, 0)
    FadeToBright(1000, 0)
    MoveCamera(0, 20, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0x2A, 0, 0, 33)
    BeginChrThread(0x2A, 3, 0, 35)
    BeginChrThread(0x2B, 3, 0, 36)
    BeginChrThread(0x2C, 3, 0, 37)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x2A, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x2A, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_4D40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_4D40)

    def lambda_4D51():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_4D51)

    def lambda_4D62():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_4D62)
    OP_75(0x1, 0x1, 0x3E8)
    OP_75(0x2, 0x1, 0x3E8)
    OP_75(0x3, 0x1, 0x3E8)
    WaitChrThread(0x2A, 2)
    WaitChrThread(0x2B, 2)
    WaitChrThread(0x2C, 2)
    CancelBlur(1000)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    EndChrThread(0x2C, 0x3)
    EndChrThread(0x2A, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2B, 0x80)
    SetChrFlags(0x2C, 0x80)
    Sleep(500)
    OP_68(0, 1000, -11400, 3000)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    #C0126
    ChrTalk(
        0x101,
        (
            "#00006F#5P……我们之前曾在\x01",
            "这个地方遇到过\x01",
            "『结社』的肯帕雷拉……\x02\x03",

            "#00013F仔细想想，琪雅当时\x01",
            "也正巧在这前方……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        (
            "#00108F#12P嗯……\x01",
            "看来前方的确有什么东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        (
            "#00303F#6P胡思乱想也没用……\x01",
            "我们只能过去看看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        "#00201F#6P嗯，走吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    SetChrPos(0x0, 0, 0, -10000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x182, 7)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_34_4A8A end

    def Function_35_4F43(): pass

    label("Function_35_4F43")

    OP_74(0x1, 0xF)

    label("loc_4F47")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F75")
    OP_71(0x1, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_4F47")

    label("loc_4F75")

    Return()

    # Function_35_4F43 end

    def Function_36_4F76(): pass

    label("Function_36_4F76")

    OP_74(0x2, 0xF)

    label("loc_4F7A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FA8")
    OP_71(0x2, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x2)
    OP_71(0x2, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x2)
    Jump("loc_4F7A")

    label("loc_4FA8")

    Return()

    # Function_36_4F76 end

    def Function_37_4FA9(): pass

    label("Function_37_4FA9")

    OP_74(0x3, 0xF)

    label("loc_4FAD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4FDB")
    OP_71(0x3, 0x3D, 0x50, 0x0, 0x8)
    OP_79(0x3)
    OP_71(0x3, 0x50, 0x3D, 0x0, 0x8)
    OP_79(0x3)
    Jump("loc_4FAD")

    label("loc_4FDB")

    Return()

    # Function_37_4FA9 end

    def Function_38_4FDC(): pass

    label("Function_38_4FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FFE")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    label("loc_4FFE")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要前往哪里呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "恐怖过山车\x01",      # 0
            "占卜馆\x01",          # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5089"),
        (1, "loc_50A2"),
        (2, "loc_50BB"),
        (SWITCH_DEFAULT, "loc_50C0"),
    )


    label("loc_5089")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1350", 100, 0, 0)
    IdleLoop()
    Jump("loc_50C0")

    label("loc_50A2")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1380", 100, 0, 0)
    IdleLoop()
    Jump("loc_50C0")

    label("loc_50BB")

    Jump("loc_50C0")

    label("loc_50C0")

    SetChrPos(0x0, 10670, 0, 4280, 225)
    EventEnd(0x4)
    Return()

    # Function_38_4FDC end

    def Function_39_50D4(): pass

    label("Function_39_50D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_50F6")
    EventBegin(0x1)
    Call(0, 41)
    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    label("loc_50F6")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要前往哪里呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "摩天轮\x01",      # 0
            "休息所\x01",      # 1
            "放弃\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_517D"),
        (1, "loc_5196"),
        (2, "loc_51AF"),
        (SWITCH_DEFAULT, "loc_51B4"),
    )


    label("loc_517D")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1330", 100, 0, 0)
    IdleLoop()
    Jump("loc_51B4")

    label("loc_5196")

    FadeToDark(500, 0, -1)
    OP_0D()
    NewScene("t1370", 100, 0, 0)
    IdleLoop()
    Jump("loc_51B4")

    label("loc_51AF")

    Jump("loc_51B4")

    label("loc_51B4")

    SetChrPos(0x0, -11020, 0, 4080, 135)
    EventEnd(0x4)
    Return()

    # Function_39_50D4 end

    def Function_40_51C8(): pass

    label("Function_40_51C8")

    EventBegin(0x1)

    #C0132
    ChrTalk(
        0x101,
        (
            "#00000F哦，往这边走\x01",
            "就离开主题公园了。\x02\x03",

            "今天要和大家一起\x01",
            "在奇幻乐园尽情享受。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 3000, -55560, 0)
    EventEnd(0x4)
    Return()

    # Function_40_51C8 end

    def Function_41_5231(): pass

    label("Function_41_5231")


    #C0133
    ChrTalk(
        0x101,
        (
            "#00000F现在并不需要去这边……\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_41_5231 end

    def Function_42_5262(): pass

    label("Function_42_5262")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4930, 2500, 2360, 0)
    MoveCamera(323, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    SetChrPos(0x101, 2160, 0, 5860, 180)
    SetChrPos(0xEF, 3750, 0, 5560, 225)
    OP_4B(0x29, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0134
    ChrTalk(
        0x101,
        "#00005F哦，原来在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_9C(0x29, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x29, 0x101, 500)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0135
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "呀，被发现了☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(4410, 2500, 5160, 0)
    MoveCamera(333, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    SetChrPos(0x29, 2800, 0, 5760, 0)
    SetChrPos(0x101, 2970, 0, 8380, 180)
    SetChrPos(0xEF, 4120, 0, 7980, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0136
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "唔……或许我有些小看\x01",
            "小哥哥你了呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "竟能连续三次把我找到，\x01",
            "光靠好运显然是不可能的，\x01",
            "唔……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#00012F哪、哪里～\x01",
            "并没有你说的那么厉害啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "好！既然如此，\x01",
            "我可要认真躲藏了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x29,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，这次一定\x01",
            "不会被你找到的～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54B0():

        label("loc_54B0")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_54B0")

    QueueWorkItem2(0x101, 1, lambda_54B0)

    def lambda_54C2():

        label("loc_54C2")

        TurnDirection(0xFE, 0x29, 500)
        Yield()
        Jump("loc_54C2")

    QueueWorkItem2(0xEF, 1, lambda_54C2)
    SetChrFlags(0x29, 0x1000)
    OP_95(0x29, -550, 0, 6760, 5000, 0x0)
    OP_95(0x29, -5830, 0, 4550, 5000, 0x0)

    def lambda_5501():
        OP_95(0xFE, -10560, 0, 4110, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_5501)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    OP_68(3360, 2500, 6680, 0)
    MoveCamera(297, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12170, 0)
    SetChrPos(0x101, 1880, 0, 6910, 270)
    SetChrPos(0xEF, 2170, 0, 8550, 270)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_55E2")

    #C0141
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，总算是\x01",
            "赢下第二场了呢。\x02\x03",

            "#00103F不过，它说这次\x01",
            "要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_55E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_5632")

    #C0142
    ChrTalk(
        0x103,
        (
            "#00200F总算赢下\x01",
            "两局了。\x02\x03",

            "#00203F不过它这次\x01",
            "好像要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_5632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_568A")

    #C0143
    ChrTalk(
        0x104,
        (
            "#00300F总算是\x01",
            "连胜两场啊。\x02\x03",

            "#00303F不过它这次\x01",
            "好像要拿出真本事了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_568A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_56E0")

    #C0144
    ChrTalk(
        0x109,
        (
            "#10100F呵呵，总算\x01",
            "赢下第二局了！\x02\x03",

            "#10103F不过它说\x01",
            "这次要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_56E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_5736")

    #C0145
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，总算\x01",
            "赢下第二场了。\x02\x03",

            "#10303F不过它说\x01",
            "这次要认真了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_5736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_5784")

    #C0146
    ChrTalk(
        0x153,
        (
            "#01109F好，连赢\x01",
            "两场啦！\x02\x03",

            "#01111F可是它说\x01",
            "这次要认真了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_5784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_57DE")

    #C0147
    ChrTalk(
        0x156,
        (
            "#06400F呵呵，总算是\x01",
            "赢下第二局了～\x02\x03",

            "#06403F不过它这次\x01",
            "似乎要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_57DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_5838")

    #C0148
    ChrTalk(
        0x14C,
        (
            "#05900F呵呵，总算赢下\x01",
            "第二局了啊。\x02\x03",

            "#05904F但是它这次\x01",
            "好像要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_5838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_5896")

    #C0149
    ChrTalk(
        0x134,
        (
            "#01700F呵呵，第二场\x01",
            "也赢得这么轻松啊。\x02\x03",

            "#01705F不过它这次好像\x01",
            "要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_5896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_58EE")

    #C0150
    ChrTalk(
        0x135,
        (
            "#01802F呵呵，总算\x01",
            "赢下第二场了。\x02\x03",

            "#01805F不过，它说这次\x01",
            "要认真了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5932")

    label("loc_58EE")


    #C0151
    ChrTalk(
        0x166,
        (
            "#14000F总算赢下\x01",
            "第二局了啊。\x02\x03",

            "#14006F不过它说这次\x01",
            "要认真了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_5993")

    #C0152
    ChrTalk(
        0x101,
        (
            "#00006F虽然有点没把握，\x01",
            "但还是努力找找吧。\x02\x03",

            "#00000F这次它会藏到什么地方呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59E6")

    label("loc_5993")


    #C0153
    ChrTalk(
        0x101,
        (
            "#00006F虽然有点没把握，\x01",
            "但还是努力找找吧。\x02\x03",

            "#00000F这次它会藏到什么地方呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59E6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x7F, 0x1, 0xC)
    SetScenarioFlags(0x1C9, 4)
    OP_65(0x0, 0x1)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x0, -20, 0, 8600, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_42_5262 end

    def Function_43_5A1B(): pass

    label("Function_43_5A1B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(1060, 2500, -8580, 0)
    MoveCamera(319, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14940, 0)
    OP_93(0x14, 0xB4, 0x0)
    SetChrPos(0x101, -510, 0, -7920, 0)
    SetChrPos(0xEF, 530, 0, -7970, 0)
    OP_4B(0x14, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0154
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "是吗～算啦，这也没办法。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "我会替你们\x01",
            "转告给咪雪的～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x14,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "请你们继续\x01",
            "在园内游玩吧～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        "#00006F嗯，不好意思，那就拜托你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_5B80")

    #C0158
    ChrTalk(
        0x102,
        (
            "#00106F算啦，既然找不到，\x01",
            "也只能这样了……\x02\x03",

            "#00100F那我就先\x01",
            "告辞啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_5BD4")

    #C0159
    ChrTalk(
        0x103,
        (
            "#00206F怎么找都找不到，\x01",
            "真没办法啊……\x02\x03",

            "#00200F那我就先\x01",
            "失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_5C24")

    #C0160
    ChrTalk(
        0x104,
        (
            "#00306F算啦，找不到\x01",
            "也没办法啊。\x02\x03",

            "#00300F那我就\x01",
            "先走一步了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_5C7A")

    #C0161
    ChrTalk(
        0x109,
        (
            "#10106F呼，既然找不到，\x01",
            "也只能这样了……\x02\x03",

            "#10100F那我就先\x01",
            "告辞了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_5CC8")

    #C0162
    ChrTalk(
        0x105,
        (
            "#10306F算了，找不到\x01",
            "也没办法呢。\x02\x03",

            "#10300F那我就此\x01",
            "失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_5D24")

    #C0163
    ChrTalk(
        0x153,
        (
            "#01106F哎，难得的机会，\x01",
            "真想把它找到啊。\x02\x03",

            "#01100F算了，\x01",
            "琪雅去别处玩吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_5D74")

    #C0164
    ChrTalk(
        0x156,
        (
            "#06406F算啦，找不到\x01",
            "也没办法呢～\x02\x03",

            "#06400F那我就\x01",
            "先走一步了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5D74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_5DC4")

    #C0165
    ChrTalk(
        0x14C,
        (
            "#05906F算了，找不到\x01",
            "也没办法嘛。\x02\x03",

            "#05900F那我就先\x01",
            "去别处啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_5E26")

    #C0166
    ChrTalk(
        0x134,
        (
            "#01706F唔～虽然很想把它找到……\x01",
            "但也只能这样了。\x02\x03",

            "#01702F那我就先\x01",
            "去别处玩啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_5E7E")

    #C0167
    ChrTalk(
        0x135,
        (
            "#01806F算啦，既然找不到，\x01",
            "也只能这样了……\x02\x03",

            "#01802F那我就先\x01",
            "失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EC0")

    label("loc_5E7E")


    #C0168
    ChrTalk(
        0x166,
        (
            "#14006F算啦，找不到\x01",
            "也没办法。\x02\x03",

            "#14000F那我就先去\x01",
            "别处玩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EC0")

    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_5EF3")

    #C0169
    ChrTalk(
        0x101,
        "#00000F嗯，一会见吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F0E")

    label("loc_5EF3")


    #C0170
    ChrTalk(
        0x101,
        "#00000F好，一会见吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5F0E")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_5F2A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_5FD0")

    label("loc_5F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_5F3B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_5FD0")

    label("loc_5F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_5F4C")
    RemoveParty(0x3, 0xFF)
    Jump("loc_5FD0")

    label("loc_5F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_5F5D")
    RemoveParty(0x8, 0xFF)
    Jump("loc_5FD0")

    label("loc_5F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_5F6E")
    RemoveParty(0x4, 0xFF)
    Jump("loc_5FD0")

    label("loc_5F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_5F84")
    RemoveParty(0x52, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_5FD0")

    label("loc_5F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_5F95")
    RemoveParty(0x55, 0xFF)
    Jump("loc_5FD0")

    label("loc_5F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_5FAB")
    RemoveParty(0x4B, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_5FD0")

    label("loc_5FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_5FBC")
    RemoveParty(0x33, 0xFF)
    Jump("loc_5FD0")

    label("loc_5FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_5FCD")
    RemoveParty(0x34, 0xFF)
    Jump("loc_5FD0")

    label("loc_5FCD")

    RemoveParty(0x65, 0xFF)

    label("loc_5FD0")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0171
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【咪雪的挑战】\x07\x00",
            "失败了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7F, 0x1, 0x10)
    OP_29(0x7F, 0x4, 0x40)
    OP_65(0x0, 0x1)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x0, -30, 0, -8310, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_43_5A1B end

    def Function_44_6038(): pass

    label("Function_44_6038")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch45400.itc", 0x1E)
    LoadChrToIndex("chr/ch28100.itc", 0x1F)
    LoadChrToIndex("chr/ch20600.itc", 0x20)
    LoadChrToIndex("chr/ch24500.itc", 0x21)
    LoadChrToIndex("chr/ch33000.itc", 0x22)
    LoadChrToIndex("chr/ch23700.itc", 0x23)
    LoadChrToIndex("chr/ch24400.itc", 0x24)
    LoadChrToIndex("chr/ch20700.itc", 0x25)
    LoadChrToIndex("chr/ch22200.itc", 0x26)
    LoadChrToIndex("chr/ch22100.itc", 0x27)
    LoadChrToIndex("chr/ch32300.itc", 0x28)
    LoadChrToIndex("chr/ch32400.itc", 0x29)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(820)
    SoundLoad(819)
    SoundLoad(501)
    SoundLoad(626)
    SetChrChipByIndex(0x101, 0xC)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x103, 0x20)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrChipByIndex(0x1F, 0x20)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x20, 0x21)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x21, 0x22)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrChipByIndex(0x22, 0x23)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrChipByIndex(0x23, 0x24)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x24, 0x25)
    SetChrFlags(0x24, 0x8000)
    ClearChrFlags(0x24, 0x80)
    SetChrChipByIndex(0x25, 0x26)
    SetChrFlags(0x25, 0x8000)
    ClearChrFlags(0x25, 0x80)
    SetChrChipByIndex(0x26, 0x27)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x26, 0x80)
    SetChrChipByIndex(0x27, 0x28)
    SetChrFlags(0x27, 0x8000)
    ClearChrFlags(0x27, 0x80)
    SetChrChipByIndex(0x28, 0x29)
    SetChrFlags(0x28, 0x8000)
    ClearChrFlags(0x28, 0x80)
    OP_68(170, 2200, -8360, 0)
    MoveCamera(358, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16680, 0)
    SetChrPos(0x101, -700, 0, -7790, 180)
    SetChrPos(0x103, 1000, 0, -7790, 180)
    SetChrPos(0x1E, 3550, 0, -7790, 180)
    SetChrPos(0x1F, 990, 0, -11190, 0)
    SetChrPos(0x20, 50, 0, -12810, 0)
    SetChrPos(0x21, -2600, 0, -10830, 0)
    SetChrPos(0x22, 3350, 0, -9980, 0)
    SetChrPos(0x23, -1650, 0, -13660, 0)
    SetChrPos(0x24, -700, 0, -10910, 0)
    SetChrPos(0x25, 2320, 0, -11400, 0)
    SetChrPos(0x26, -4090, 0, -7750, 45)
    SetChrPos(0x27, 4430, 0, -8039, 315)
    SetChrPos(0x28, 1880, 0, -13990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_68(170, 1000, -8360, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()

    #C0172
    ChrTalk(
        0x1E,
        "让大家久等了！\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1E,
        (
            "接下来，咪西＆咪雪\x01",
            "的舞蹈表演就要开始了！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1F,
        "哇！咪西～！\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x20,
        "好可爱！\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（……终于要开始跳舞了吗，\x01",
            "  呜呜，好紧张啊……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F（没关系的，\x01",
            "  这个舞蹈是即兴表演，\x01",
            "  每次的动作都不同。）\x02\x03",

            "#05520F（只要我们把跳舞的\x01",
            "  基本方针统一，\x01",
            "  就不会有什么问题了。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（基本方针吗……）\x02\x03",

            "#05208F（说起来，在开始工作之前，\x01",
            "  我们还领到了一本\x01",
            "  关于舞蹈的介绍手册呢。）\x02\x03",

            "#05201F（只要努力回想起其中的内容……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1E,
        (
            "那么……\x01",
            "就请大家一起参与吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1E, 0x10E, 0x1F4)
    Sleep(300)

    #C0180
    ChrTalk(
        0x1E,
        (
            "咪西＆咪雪！\x01",
            "舞蹈表演开始！！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    WaitBGM()

    #C0181
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05201F（开始了……！）\x02\x03",

            "#05207F（……我们上吧，缇欧！！\x01",
            "  要『充满热情，且富有想象力』！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05521F（明白……！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    PlayBGM("ed7589", 0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x103, 0x20)
    BeginChrThread(0x101, 1, 0, 50)
    BeginChrThread(0x103, 1, 0, 51)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 50, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x103, 0x20)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    BeginChrThread(0x101, 0, 0, 45)
    BeginChrThread(0x103, 0, 0, 45)
    BeginChrThread(0x101, 2, 0, 48)
    BeginChrThread(0x103, 2, 0, 49)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x101, 2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x103, 0x20)
    ClearScenarioFlags(0x1, 2)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    Sleep(200)
    BeginChrThread(0x101, 1, 0, 51)
    BeginChrThread(0x103, 1, 0, 50)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x103, 0x20)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 1)
    BeginChrThread(0x101, 0, 0, 45)
    BeginChrThread(0x103, 0, 0, 45)
    BeginChrThread(0x101, 2, 0, 49)
    BeginChrThread(0x103, 2, 0, 48)
    Sound(819, 0, 80, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    ClearScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 1)

    #C0183
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（现在要喊出最后的标志性口号了！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ＬＯＶＥ咪西☆\x01",        # 0
            "ＨＡＰＰＹ咪西☆\x01",      # 1
            "ＥＮＪＯＹ咪西☆\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B43")
    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x177, 0)

    #C0184
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SＥＮＪＯＹ——咪西☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("众观众")

    #A0185
    AnonymousTalk(
        0xFF,
        "#4SＥＮＪＯＹ——！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("众观众")

    #A0186
    AnonymousTalk(
        0xFF,
        "#4S咪西——☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 66, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0187
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05522F（一下就把观众的情绪带动起来了呢……\x01",
            "  真不愧是罗伊德前辈！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7021")

    label("loc_6B43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D05")

    #C0188
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SＬＯＶＥ——咪西☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    Sleep(2000)
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("众观众")

    #A0189
    AnonymousTalk(
        0xFF,
        "#4SＬＯＶＥ——！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("众观众")

    #A0190
    AnonymousTalk(
        0xFF,
        "#4S咪西——☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_6EB7")

    label("loc_6D05")


    #C0191
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#4SＨＡＰＰＹ——咪西☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0x101, 0, 0, 47)
    BeginChrThread(0x103, 0, 0, 47)
    BeginChrThread(0x101, 2, 0, 52)
    BeginChrThread(0x103, 2, 0, 52)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    Sleep(2000)
    OP_63(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("众观众")

    #A0192
    AnonymousTalk(
        0xFF,
        "#4SＨＡＰＰＹ——！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("众观众")

    #A0193
    AnonymousTalk(
        0xFF,
        "#4S咪西——☆\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6EB7")

    Sound(819, 0, 66, 0)
    Sound(820, 0, 50, 0)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0194
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F（……糟、糟糕……\x01",
            "  好像喊错台词了吧？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05526F（……唉，都到最后的最后了。）\x02\x03",

            "#05531F（结束之后别想逃过惩罚。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7021")

    StopSound(821, 3000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7105")
    SetChrName("")

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "凭借罗伊德和缇欧的热情演出，\x01",
            "舞蹈表演在热烈的\x01",
            "欢呼声中顺利结束了。\x02\x03",

            "舞蹈表演顺利结束后，罗伊德仍然\x01",
            "被一股不可思议的奇妙余韵所包围……\x02\x03",

            "随后，二人一同\x01",
            "回到了休息所。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x86, 0x1, 0x7)
    Jump("loc_71E5")

    label("loc_7105")

    SetChrName("")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "凭借罗伊德和缇欧的热情演出，\x01",
            "舞蹈表演在热烈的\x01",
            "欢呼声中顺利结束了。\x02\x03",

            "舞蹈表演结束之后，\x01",
            "二人一同\x01",
            "返回休息所……\x02\x03",

            "在归途中，罗伊德遭受了\x01",
            "喊错台词的惩罚。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(501, 0, 80, 0)
    Sound(815, 0, 40, 0)
    Sleep(800)
    #Sound(3319, 255, 100, 0)    #voice#Lloyd

    #C0198
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F#N哇啊！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x86, 0x1, 0x8)

    label("loc_71E5")

    SetScenarioFlags(0x22, 0)
    NewScene("t1370", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_6038 end

    def Function_45_71F2(): pass

    label("Function_45_71F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_720E")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(100)
    Jump("Function_45_71F2")

    label("loc_720E")

    Return()

    # Function_45_71F2 end

    def Function_46_720F(): pass

    label("Function_46_720F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_722B")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(50)
    Jump("Function_46_720F")

    label("loc_722B")

    Return()

    # Function_46_720F end

    def Function_47_722C(): pass

    label("Function_47_722C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_7248")
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(33)
    Jump("Function_47_722C")

    label("loc_7248")

    Return()

    # Function_47_722C end

    def Function_48_7249(): pass

    label("Function_48_7249")

    OP_96(0xFE, 0xFFFFF768, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFDD14, 0x7D0, 0x0)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_48_7249 end

    def Function_49_72BC(): pass

    label("Function_49_72BC")

    OP_96(0xFE, 0x9C4, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0xBB8)
    OP_96(0xFE, 0x3E8, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    OP_96(0xFE, 0x96, 0x0, 0xFFFFE4D0, 0x7D0, 0x0)
    OP_96(0xFE, 0xFFFFFD44, 0x0, 0xFFFFE192, 0x7D0, 0x0)
    Return()

    # Function_49_72BC end

    def Function_50_732F(): pass

    label("Function_50_732F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7442")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    OP_93(0xFE, 0x10E, 0x0)
    Sleep(100)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    Jump("Function_50_732F")

    label("loc_7442")

    Return()

    # Function_50_732F end

    def Function_51_7443(): pass

    label("Function_51_7443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_7556")
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(100)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(100)
    OP_97(0xFE, 0x1F4, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    OP_97(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    Sleep(500)
    OP_98(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetScenarioFlags(0x1, 2)
    BeginChrThread(0xFE, 0, 0, 46)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    ClearScenarioFlags(0x1, 2)
    Jump("Function_51_7443")

    label("loc_7556")

    Return()

    # Function_51_7443 end

    def Function_52_7557(): pass

    label("Function_52_7557")

    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0xBB8)
    OP_93(0xFE, 0xB4, 0x0)
    Return()

    # Function_52_7557 end

    def Function_53_7576(): pass

    label("Function_53_7576")

    Sleep(1000)

    label("loc_7579")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_759B")
    Sound(918, 0, 50, 0)
    Sleep(2200)
    Sound(918, 0, 40, 0)
    Sleep(5000)
    Jump("loc_7579")

    label("loc_759B")

    Return()

    # Function_53_7576 end

    SaveToFile()

Try(main)
