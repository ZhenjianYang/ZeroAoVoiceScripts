from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1400.bin",                # FileName
        "t1400",                    # MapName
        "t1400",                    # Location
        0x00BB,                     # MapIndex
        "ed7160",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, -30000, 0, 0, 1, 187, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1400",                  # 0
        "艾莉",                   # 1
        "兰迪",                   # 2
        "诺艾尔",                 # 3
        "瓦吉",                   # 4
        "琪雅",                   # 5
        "芙兰",                   # 6
        "塞茜尔",                 # 7
        "伊莉娅",                 # 8
        "莉夏",                   # 9
        "修利",                   # 10
        "咪西",                   # 11
        "梅尔斯",                 # 12
        "柯洛娜",                 # 13
        "利玛",                   # 14
        "奇幻乐园工作人员",       # 15
        "游客",                   # 16
        "游客",                   # 17
        "游客",                   # 18
        "游客",                   # 19
        "游客",                   # 20
        "幻兽",                   # 21
        "咪雪",                   # 22
        "男孩",                   # 23
        "男孩",                   # 24
        "SE控制",                 # 25
        "bt1450",                 # 26
        "奇幻乐园入口广场方向",   # 27
    ))

    ATBonus("ATBonus_490", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_550", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_564", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_568", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_534", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_538", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_53C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_540", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_544", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_548", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_570", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bt1450", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_550", "MonsterBattlePostion_530", "ed7454", "ed7000", "ATBonus_490"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch00300.itc",                   # 01
        "chr/ch02900.itc",                   # 02
        "chr/ch03000.itc",                   # 03
        "chr/ch08200.itc",                   # 04
        "chr/ch08500.itc",                   # 05
        "chr/ch07500.itc",                   # 06
        "chr/ch05100.itc",                   # 07
        "chr/ch05200.itc",                   # 08
        "chr/ch10100.itc",                   # 09
        "chr/ch10200.itc",                   # 0A
        "chr/ch26200.itc",                   # 0B
        "chr/ch22700.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
        "chr/ch44500.itc",                   # 0E
        "chr/ch27600.itc",                   # 0F
        "chr/ch20300.itc",                   # 10
        "chr/ch22300.itc",                   # 11
        "chr/ch33100.itc",                   # 12
        "chr/ch33300.itc",                   # 13
        "chr/ch45400.itc",                   # 14
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

    DeclNpc(1309,    2329,    -67430,  0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(1309,    2329,    -67430,  0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(2109,    2319,    -67309,  0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(2609,    2220,    -66120,  222,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(1309,    2329,    -67430,  0,    389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(1679,    2299,    -67059,  42,   389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2549,    2309,    -67239,  312,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(1200,    2289,    -67010,  42,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(2109,    2319,    -67309,  0,    389,  0x0, 0,   8,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(2109,    2319,    -67309,  0,    389,  0x0, 0,   9,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(2240,    2200,    -65849,  222,  389,  0x0, 0,   10,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-1750,   0,       -27190,  231,  389,  0x0, 0,   11,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-2750,   0,       -27760,  90,   389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-1809,   9,       -28510,  336,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       1600,    -23149,  180,  389,  0x0, 0,   14,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-2329,   6010,    -90419,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-2769,   5590,    -88610,  148,  389,  0x0, 0,   16,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-1269,   5690,    -89069,  234,  389,  0x0, 0,   17,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(889,     509,     -45069,  270,  389,  0x0, 0,   18,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-109,    509,     -45069,  90,   389,  0x0, 0,   19,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(5420,    9,       -21950,  180,  389,  0x0, 0,   20,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 27,  0.0,                   -71.0,                 1.7000000476837158,    625.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  14.199999809265137,    -0.3400000035762787,   1.0])

    DeclActor(3680,    1460,    -22620,  1000,    5420,    1500,    -21950,  0x007E, 0,  36, 0x0000)

    PlaceName(-0.05999999865889549, 0.0, -140.4499969482422, 0x0000, 0x0000, "奇幻乐园入口广场方向")

    ChipFrameInfo(1620, 0)                                       # 0

    ScpFunction((
        "Function_0_654",          # 00, 0
        "Function_1_70C",          # 01, 1
        "Function_2_7A7",          # 02, 2
        "Function_3_94F",          # 03, 3
        "Function_4_A23",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_C9A",          # 06, 6
        "Function_7_D7A",          # 07, 7
        "Function_8_E5F",          # 08, 8
        "Function_9_EFC",          # 09, 9
        "Function_10_F7A",         # 0A, 10
        "Function_11_102C",        # 0B, 11
        "Function_12_115B",        # 0C, 12
        "Function_13_1251",        # 0D, 13
        "Function_14_130F",        # 0E, 14
        "Function_15_14BB",        # 0F, 15
        "Function_16_1575",        # 10, 16
        "Function_17_1647",        # 11, 17
        "Function_18_1701",        # 12, 18
        "Function_19_17CB",        # 13, 19
        "Function_20_189E",        # 14, 20
        "Function_21_198A",        # 15, 21
        "Function_22_19E4",        # 16, 22
        "Function_23_1A33",        # 17, 23
        "Function_24_1A79",        # 18, 24
        "Function_25_1B18",        # 19, 25
        "Function_26_1BC8",        # 1A, 26
        "Function_27_1D34",        # 1B, 27
        "Function_28_2586",        # 1C, 28
        "Function_29_25AB",        # 1D, 29
        "Function_30_2656",        # 1E, 30
        "Function_31_2676",        # 1F, 31
        "Function_32_2940",        # 20, 32
        "Function_33_2964",        # 21, 33
        "Function_34_3179",        # 22, 34
        "Function_35_3935",        # 23, 35
        "Function_36_3975",        # 24, 36
        "Function_37_454E",        # 25, 37
        "Function_38_55EF",        # 26, 38
        "Function_39_562A",        # 27, 39
    ))


    def Function_0_654(): pass

    label("Function_0_654")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_694"),
        (1, "loc_6A0"),
        (2, "loc_6AC"),
        (3, "loc_6B8"),
        (4, "loc_6C4"),
        (5, "loc_6D0"),
        (6, "loc_6DC"),
        (SWITCH_DEFAULT, "loc_6E8"),
    )


    label("loc_694")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_6F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_6F4")

    label("loc_70B")

    Return()

    # Function_0_654 end

    def Function_1_70C(): pass

    label("Function_1_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_71A")
    Jump("loc_788")

    label("loc_71A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_728")
    Jump("loc_788")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_736")
    Jump("loc_788")

    label("loc_736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_747")
    Call(0, 26)
    Jump("loc_788")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_755")
    Jump("loc_788")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_763")
    Jump("loc_788")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_771")
    Jump("loc_788")

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_77F")
    Jump("loc_788")

    label("loc_77F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_788")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_797")
    ClearScenarioFlags(0x22, 0)
    Event(0, 37)

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_7A6")
    ClearScenarioFlags(0x22, 1)
    Event(0, 34)

    label("loc_7A6")

    Return()

    # Function_1_70C end

    def Function_2_7A7(): pass

    label("Function_2_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B9")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D8")
    OP_24(0x335)
    SoundLoad(918)
    BeginChrThread(0x20, 3, 0, 39)
    Jump("loc_7EF")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_7E9")
    OP_24(0x335)
    Jump("loc_7EF")

    label("loc_7E9")

    Sound(821, 1, 50, 0)

    label("loc_7EF")

    Sound(126, 1, 80, 0)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A")
    SetMapObjFrame(0xFF, "water", 0x2, "loop_off")
    SetMapObjFrame(0xFF, "main", 0x2, "loop_off")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89B")
    SetMapObjFrame(0xFF, "sky01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x1, 0x1)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x26, 0x1F4, 0x0)
    Jump("loc_8C4")

    label("loc_89B")

    SetMapObjFrame(0xFF, "sky01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky01_y", 0x0, 0x1)

    label("loc_8C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8EB")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x12C, 0x0)
    Jump("loc_90D")

    label("loc_8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_90D")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x14, 0x12C, 0x0)

    label("loc_90D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_921")
    ClearMapObjFlags(0x0, 0x10)

    label("loc_921")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94E")
    OP_66(0x0, 0x1)

    label("loc_94E")

    Return()

    # Function_2_7A7 end

    def Function_3_94F(): pass

    label("Function_3_94F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_968")
    Jump("loc_A1F")

    label("loc_968")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E")
    Jump("loc_A1F")

    label("loc_97E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_994")
    Jump("loc_A1F")

    label("loc_994")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E")

    #C0001
    ChrTalk(
        0x8,
        (
            "#00100F刚才从城堡方向\x01",
            "传来了悦耳的钟声呢。\x02\x03",

            "#00109F呵呵，或许是某对情侣\x01",
            "正在里面向镜子许愿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1F")

    label("loc_A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")

    label("loc_A1F")

    TalkEnd(0xFE)
    Return()

    # Function_3_94F end

    def Function_4_A23(): pass

    label("Function_4_A23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3C")
    Jump("loc_B99")

    label("loc_A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A52")
    Jump("loc_B99")

    label("loc_A52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")
    Jump("loc_B99")

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7E")
    Jump("loc_B99")

    label("loc_A7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B20")

    #C0002
    ChrTalk(
        0x9,
        (
            "#00302F等到了晚上，那座镜之城\x01",
            "还会亮起灯光呢。\x02\x03",

            "#00304F伴随着烟花和巡游队伍，\x01",
            "可以让人充分感受到\x01",
            "主题公园精彩一日的结束。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B99")

    label("loc_B20")


    #C0003
    ChrTalk(
        0x9,
        (
            "#00302F难得有机会来玩，\x01",
            "本想找个漂亮的大姐姐\x01",
            "一起享受晚间活动……\x02\x03",

            "#00306F但今天还要去参加晚餐会，\x01",
            "也只能放弃了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B99")

    TalkEnd(0xFE)
    Return()

    # Function_4_A23 end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    Jump("loc_C96")

    label("loc_BB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCC")
    Jump("loc_C96")

    label("loc_BCC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE2")
    Jump("loc_C96")

    label("loc_BE2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C85")

    #C0004
    ChrTalk(
        0xA,
        (
            "#10103F『实现愿望的镜子』……\x01",
            "真的能实现愿望吧？\x02\x03",

            "#10100F正所谓『无风不起浪』，既然有\x01",
            "那样的传闻，多少会有一定道理，\x01",
            "我还是有点期待的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_C85")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C96")

    label("loc_C96")

    TalkEnd(0xFE)
    Return()

    # Function_5_B9D end

    def Function_6_C9A(): pass

    label("Function_6_C9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB3")
    Jump("loc_D76")

    label("loc_CB3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC9")
    Jump("loc_D76")

    label("loc_CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEC")
    Call(0, 7)
    Jump("loc_D4A")

    label("loc_CEC")


    #C0005
    ChrTalk(
        0xB,
        (
            "#10302F如果不信，就太没趣了吗……？\x01",
            "呵呵，确实有道理呢。\x02\x03",

            "#10304F我也尽量\x01",
            "期待一下好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    Jump("loc_D76")

    label("loc_D4F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D65")
    Jump("loc_D76")

    label("loc_D65")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D76")

    label("loc_D76")

    TalkEnd(0xFE)
    Return()

    # Function_6_C9A end

    def Function_7_D7A(): pass

    label("Function_7_D7A")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0006
    ChrTalk(
        0xB,
        (
            "#10300F『实现愿望的镜子』……\x02\x03",

            "#10302F你觉得它真的能\x01",
            "实现自己的愿望吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xD,
        (
            "#06409F那当然！\x02\x03",

            "#06400F而且，如果不信，\x01",
            "进去玩这个\x01",
            "就未免太没趣了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "#10300F呵呵，原来如此，\x01",
            "确实如你所说呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_7_D7A end

    def Function_8_E5F(): pass

    label("Function_8_E5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E85")
    Call(0, 9)
    Jump("loc_EA0")

    label("loc_E85")


    #C0009
    ChrTalk(
        0xC,
        "#01109F镜之城真高呀！\x02",
    )

    CloseMessageWindow()

    label("loc_EA0")

    Jump("loc_EF8")

    label("loc_EA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBB")
    Jump("loc_EF8")

    label("loc_EBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ED1")
    Jump("loc_EF8")

    label("loc_ED1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE7")
    Jump("loc_EF8")

    label("loc_EE7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF8")

    label("loc_EF8")

    TalkEnd(0xFE)
    Return()

    # Function_8_E5F end

    def Function_9_EFC(): pass

    label("Function_9_EFC")

    OP_4B(0xC, 0xFF)
    OP_4B(0x11, 0xFF)

    #C0010
    ChrTalk(
        0xC,
        (
            "#01109F哇啊啊……\x01",
            "镜之城好高呀！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x11,
        (
            "#14005F嗯……走近一看，\x01",
            "感觉和在远处看时完全不同……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_9_EFC end

    def Function_10_F7A(): pass

    label("Function_10_F7A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F93")
    Jump("loc_1028")

    label("loc_F93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA9")
    Jump("loc_1028")

    label("loc_FA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1001")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCC")
    Call(0, 7)
    Jump("loc_FFC")

    label("loc_FCC")


    #C0012
    ChrTalk(
        0xD,
        (
            "#06409F主题公园的游乐设施\x01",
            "真是太有趣了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FFC")

    Jump("loc_1028")

    label("loc_1001")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1017")
    Jump("loc_1028")

    label("loc_1017")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")

    label("loc_1028")

    TalkEnd(0xFE)
    Return()

    # Function_10_F7A end

    def Function_11_102C(): pass

    label("Function_11_102C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1045")
    Jump("loc_1157")

    label("loc_1045")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D7")

    #C0013
    ChrTalk(
        0xE,
        (
            "#05900F呵呵，大受欢迎的咪西\x01",
            "和超级明星伊莉娅竟然在一起，\x01",
            "这真是难得一见呢。\x02\x03",

            "#05909F简直就是\x01",
            "超级名组合。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1115")

    label("loc_10D7")


    #C0014
    ChrTalk(
        0xE,
        (
            "#05909F咪西和伊莉娅竟然在一起，\x01",
            "这简直就是超级名组合啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1115")

    Jump("loc_1157")

    label("loc_111A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1130")
    Jump("loc_1157")

    label("loc_1130")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1146")
    Jump("loc_1157")

    label("loc_1146")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")

    label("loc_1157")

    TalkEnd(0xFE)
    Return()

    # Function_11_102C end

    def Function_12_115B(): pass

    label("Function_12_115B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1174")
    Jump("loc_124D")

    label("loc_1174")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1210")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1197")
    Call(0, 13)
    Jump("loc_120B")

    label("loc_1197")


    #C0015
    ChrTalk(
        0xF,
        (
            "#01705F说起来，如果咱们一直站在一起，\x01",
            "大概会引来很多人围观的。\x02\x03",

            "#01702F我今天是和朋友们一起来的，\x01",
            "就先失陪了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_120B")

    Jump("loc_124D")

    label("loc_1210")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1226")
    Jump("loc_124D")

    label("loc_1226")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123C")
    Jump("loc_124D")

    label("loc_123C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124D")

    label("loc_124D")

    TalkEnd(0xFE)
    Return()

    # Function_12_115B end

    def Function_13_1251(): pass

    label("Function_13_1251")

    OP_4B(0xF, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0016
    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "啊，莫非……\x01",
            "你是彩虹剧团的\x01",
            "伊莉娅小姐吗～？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，我一直\x01",
            "都很支持你哟～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xF,
        (
            "#01700F呵呵，我也经常在市里\x01",
            "看到你的形象呢。\x02\x03",

            "#01709F我们一起加油吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xF, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_13_1251 end

    def Function_14_130F(): pass

    label("Function_14_130F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1328")
    Jump("loc_14B7")

    label("loc_1328")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133E")
    Jump("loc_14B7")

    label("loc_133E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1354")
    Jump("loc_14B7")

    label("loc_1354")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_136A")
    Jump("loc_14B7")

    label("loc_136A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1436")

    #C0019
    ChrTalk(
        0x10,
        (
            "#01802F听说到了夜晚，\x01",
            "会有很多情侣来这一带。\x02\x03",

            "#01804F今晚好像是满月……\x01",
            "到时候，明月映照在湖面上，\x01",
            "景色必定会很美呢。\x02\x03",

            "#01809F呵呵，光是想象一下，\x01",
            "就觉得很浪漫了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_14B7")

    label("loc_1436")


    #C0020
    ChrTalk(
        0x10,
        (
            "#01802F今晚好像是满月……\x01",
            "到时候，明月映照在湖面上，\x01",
            "这里的景色必定会很美呢。\x02\x03",

            "#01809F呵呵，光是想象一下，\x01",
            "就觉得很浪漫了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B7")

    TalkEnd(0xFE)
    Return()

    # Function_14_130F end

    def Function_15_14BB(): pass

    label("Function_15_14BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E1")
    Call(0, 9)
    Jump("loc_1519")

    label("loc_14E1")


    #C0021
    ChrTalk(
        0x11,
        (
            "#14005F走近一看，竟然这么高……\x01",
            "简直都有些眩晕了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1519")

    Jump("loc_1571")

    label("loc_151E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1534")
    Jump("loc_1571")

    label("loc_1534")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_154A")
    Jump("loc_1571")

    label("loc_154A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1560")
    Jump("loc_1571")

    label("loc_1560")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1571")

    label("loc_1571")

    TalkEnd(0xFE)
    Return()

    # Function_15_14BB end

    def Function_16_1575(): pass

    label("Function_16_1575")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158E")
    Jump("loc_1643")

    label("loc_158E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B1")
    Call(0, 13)
    Jump("loc_1601")

    label("loc_15B1")


    #C0022
    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "竟然能遇到伊莉娅小姐，\x01",
            "好激动哦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x12,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "咪嘻嘻，那就请尽情\x01",
            "游玩吧～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1601")

    Jump("loc_1643")

    label("loc_1606")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161C")
    Jump("loc_1643")

    label("loc_161C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1632")
    Jump("loc_1643")

    label("loc_1632")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1643")

    label("loc_1643")

    TalkEnd(0xFE)
    Return()

    # Function_16_1575 end

    def Function_17_1647(): pass

    label("Function_17_1647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1660")
    Jump("loc_16FD")

    label("loc_1660")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1676")
    Jump("loc_16FD")

    label("loc_1676")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_168C")
    Jump("loc_16FD")

    label("loc_168C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16EC")

    #C0024
    ChrTalk(
        0x13,
        (
            "镜之城中的气氛\x01",
            "就如梦幻一般。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x13,
        (
            "让人觉得奇幻乐园\x01",
            "果然名副其实呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FD")

    label("loc_16EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FD")

    label("loc_16FD")

    TalkEnd(0xFE)
    Return()

    # Function_17_1647 end

    def Function_18_1701(): pass

    label("Function_18_1701")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171A")
    Jump("loc_17C7")

    label("loc_171A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1730")
    Jump("loc_17C7")

    label("loc_1730")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1746")
    Jump("loc_17C7")

    label("loc_1746")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B6")

    #C0026
    ChrTalk(
        0x14,
        (
            "城堡里的阶梯很长，\x01",
            "上来下去的还真是累人。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x14,
        (
            "不过利玛很开心，\x01",
            "这番劳累还是值得的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C7")

    label("loc_17B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C7")

    label("loc_17C7")

    TalkEnd(0xFE)
    Return()

    # Function_18_1701 end

    def Function_19_17CB(): pass

    label("Function_19_17CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E4")
    Jump("loc_189A")

    label("loc_17E4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17FA")
    Jump("loc_189A")

    label("loc_17FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1810")
    Jump("loc_189A")

    label("loc_1810")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1889")

    #C0028
    ChrTalk(
        0x15,
        (
            "我和爸爸一起敲响了\x01",
            "城堡里的大钟～\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x15,
        (
            "嘿嘿嘿，我许的\x01",
            "愿望是『以后还能\x01",
            "和爸爸妈妈一起来玩』～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_1889")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189A")

    label("loc_189A")

    TalkEnd(0xFE)
    Return()

    # Function_19_17CB end

    def Function_20_189E(): pass

    label("Function_20_189E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1986")
    TalkBegin(0xFE)

    #C0030
    ChrTalk(
        0xFE,
        "欢迎来到『镜之城』。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "这里是一座探索型的娱乐设施，\x01",
            "进去之后，目标就是爬到\x01",
            "『实现愿望的镜子』所在的最顶层。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00003F（我们正在和咪雪捉迷藏……\x01",
            "　现在还是不要去\x01",
            "　游乐设施游玩了。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1989")

    label("loc_1986")

    Call(0, 33)

    label("loc_1989")

    Return()

    # Function_20_189E end

    def Function_21_198A(): pass

    label("Function_21_198A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E0")

    #C0033
    ChrTalk(
        0xFE,
        (
            "要爬到那座\x01",
            "巨大城堡的顶层吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "……好像很累人呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19E0")

    label("loc_19E0")

    TalkEnd(0xFE)
    Return()

    # Function_21_198A end

    def Function_22_19E4(): pass

    label("Function_22_19E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2F")

    #C0035
    ChrTalk(
        0xFE,
        (
            "为了让孩子开心，\x01",
            "必须要让老公\x01",
            "也努力爬上去～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A2F")

    label("loc_1A2F")

    TalkEnd(0xFE)
    Return()

    # Function_22_19E4 end

    def Function_23_1A33(): pass

    label("Function_23_1A33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A75")

    #C0036
    ChrTalk(
        0xFE,
        (
            "（兴奋）……\x01",
            "要向镜子许什么愿望呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A75")

    label("loc_1A75")

    TalkEnd(0xFE)
    Return()

    # Function_23_1A33 end

    def Function_24_1A79(): pass

    label("Function_24_1A79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD1")

    #C0037
    ChrTalk(
        0xFE,
        "好啦，赶快进城堡吧。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "然后一起尽情享受\x01",
            "浪漫的气氛吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B14")

    label("loc_1AD1")


    #C0039
    ChrTalk(
        0xFE,
        "接下来就要到晚间活动了。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "一起度过一个\x01",
            "难忘的美妙夜晚吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B14")

    TalkEnd(0xFE)
    Return()

    # Function_24_1A79 end

    def Function_25_1B18(): pass

    label("Function_25_1B18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B70")

    #C0041
    ChrTalk(
        0xFE,
        "呵呵，真是座美丽的城堡啊。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "简直就像来到了\x01",
            "童话世界。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_1B70")


    #C0043
    ChrTalk(
        0xFE,
        (
            "我和男友\x01",
            "在镜之城中度过了\x01",
            "一段浪漫的时光。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "呵呵，晚间活动也很值得期待啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1BC4")

    TalkEnd(0xFE)
    Return()

    # Function_25_1B18 end

    def Function_26_1BC8(): pass

    label("Function_26_1BC8")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x10)
    SetChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1F")
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    Jump("loc_1D33")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C4E")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x10)
    Jump("loc_1D33")

    label("loc_1C4E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C78")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    Jump("loc_1D33")

    label("loc_1C78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFF")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_1CD1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_1CDF")

    label("loc_1CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_1CDF")
    SetChrFlags(0xA, 0x80)

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CFA")
    ClearChrFlags(0x1D, 0x80)

    label("loc_1CFA")

    Jump("loc_1D33")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D33")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x10)
    ClearChrFlags(0x1B, 0x10)

    label("loc_1D33")

    Return()

    # Function_26_1BC8 end

    def Function_27_1D34(): pass

    label("Function_27_1D34")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadEffect(0x0, "battle\\cr036301.eff")
    LoadEffect(0x1, "event\\ev15010.eff")
    OP_90(0x101, 100, 5000, -73000, 0)
    OP_90(0x102, -800, 5000, -74100, 0)
    OP_90(0x103, 750, 5000, -73900, 0)
    OP_90(0x104, -100, 5000, -75000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x1, 0x1C)
    OP_49()
    SetChrPos(0x1C, 0, 1600, -56000, 180)
    OP_D5(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x2F, 0x0, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x1)
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x1, 0x1, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 3400, -68000, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 3000)

    def lambda_1EBF():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EBF)
    Sleep(50)

    def lambda_1ED7():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1ED7)
    Sleep(50)

    def lambda_1EEF():
        OP_9B(0x0, 0x103, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1EEF)
    Sleep(50)

    def lambda_1F07():
        OP_9B(0x0, 0x104, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F07)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(0, 42000, -7500, 0)
    MoveCamera(0, -25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_11(0x47, 0x99, 0xF3, 0x4B, 0x12C, 0x2710)
    OP_68(0, 24000, -7500, 10000)
    MoveCamera(335, 20, 0, 10000)
    SetCameraDistance(100000, 10000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(0, 3500, -68000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(12500, 2500)
    OP_90(0x102, -800, 5000, -67650, 0)
    OP_90(0x103, 750, 5000, -68350, 0)
    OP_90(0x104, 0, 5000, -69100, 0)
    OP_11(0x47, 0x99, 0xF3, 0x14, 0x12C, 0x0)
    OP_6F(0x79)
    OP_0D()

    #C0045
    ChrTalk(
        0x104,
        (
            "#00303F#6P『镜之城』……\x02\x03",

            "#00301F本以为只是主题公园\x01",
            "中的一座代表性娱乐设施……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#00203F#6P……如今却能清晰地感应到\x01",
            "这座城堡正在散发着很强的灵压。\x02\x03",

            "#00201F而且应该是从最上层散发出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#00106F#5P……我听说\x01",
            "这座城堡是在\x01",
            "『她』的提议下建造的……\x02\x03",

            "#00108F难道说……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#00003F#5P……总之，我们进去吧。\x02\x03",

            "#00001F如果运气好，说不定可以一口气登上顶层……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(842, 0, 100, 0)
    BeginChrThread(0x1C, 0, 0, 28)
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
    Fade(250)
    OP_68(0, 9500, -56000, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23500, 0)
    MoveCamera(315, 0, 0, 4000)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    Sleep(490)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0x1C, 0x0, 0, 8500, 0, 0, 0, 0, 4000, 4000, 4000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1C, 3, 0, 29)

    def lambda_22B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_22B6)
    OP_75(0x1, 0x2, 0x3E8)
    WaitChrThread(0x1C, 2)
    CancelBlur(1000)
    EndChrThread(0x1C, 0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    OP_68(0, 5100, -56000, 1000)
    MoveCamera(330, 5, 0, 1000)
    OP_6E(650, 1000)
    SetCameraDistance(20000, 1000)
    OP_6F(0x79)
    Sleep(700)
    OP_68(-1350, 4700, -62800, 2000)
    MoveCamera(317, 5, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(20000, 2000)
    OP_90(0x102, -700, 5000, -67450, 0)
    OP_90(0x103, 1000, 5000, -68850, 0)
    OP_90(0x104, -100, 5000, -69300, 0)
    Sleep(1000)

    def lambda_237E():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_237E)
    Sleep(50)

    def lambda_2396():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2396)
    Sleep(50)

    def lambda_23AE():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23AE)
    Sleep(50)

    def lambda_23C6():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23C6)
    WaitChrThread(0x104, 1)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    Sleep(300)

    #C0049
    ChrTalk(
        0x102,
        "#00110F#1P曾在旧矿山出现的……！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#00307F#1P啧……！\x01",
            "它想守卫城堡吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00007F#1P准备战斗！\x01",
            "全力打倒它！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(60, 80, -1, -1)
    SetChrName("众同伴")

    #A0052
    AnonymousTalk(
        0xFF,
        "#4S#5P好！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2220, 5100, -59370, 1500)
    SetCameraDistance(11500, 1500)

    def lambda_24E7():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24E7)

    def lambda_24FC():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_24FC)

    def lambda_2511():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2511)

    def lambda_2526():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2526)
    EndChrThread(0x1C, 0x3)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(400)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    Battle("BattleInfo_570", 0x0, 0x0, 0x0, 0x28, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 31)
    Return()

    # Function_27_1D34 end

    def Function_28_2586(): pass

    label("Function_28_2586")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25AA")
    OP_82(0x64, 0x64, 0x1F40, 0x1F4)
    Sleep(500)
    Jump("Function_28_2586")

    label("loc_25AA")

    Return()

    # Function_28_2586 end

    def Function_29_25AB(): pass

    label("Function_29_25AB")

    OP_74(0x1, 0x5)

    label("loc_25AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E1")
    OP_71(0x1, 0x137, 0x13C, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x13C, 0x137, 0x0, 0x8)
    OP_79(0x1)
    Jump("loc_25AF")

    label("loc_25E1")

    OP_74(0x1, 0xF)
    OP_71(0x1, 0x137, 0x14E, 0x0, 0x8)
    Sleep(550)
    PlayEffect(0x1, 0xFF, 0x1C, 0x0, 0, 1600, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x1C2, 0x96, 0x1388, 0x226)
    OP_79(0x1)
    OP_74(0x1, 0x19)
    OP_71(0x1, 0xA, 0x2F, 0x15E, 0x20)
    Return()

    # Function_29_25AB end

    def Function_30_2656(): pass

    label("Function_30_2656")

    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x78, 0x8C, 0x12C, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x8D, 0x95, 0x0, 0x20)
    Return()

    # Function_30_2656 end

    def Function_31_2676(): pass

    label("Function_31_2676")

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
    OP_90(0x101, 0, 5000, -63000, 0)
    OP_90(0x102, -600, 5000, -64000, 0)
    OP_90(0x103, 600, 5000, -64000, 0)
    OP_90(0x104, 0, 5000, -65000, 0)
    SetMapObjFlags(0x0, 0x1000)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x1, 0x1C)
    OP_49()
    SetChrPos(0x1C, 0, 1600, -56000, 180)
    OP_D5(0x1C, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x1, 0x4)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x2F, 0x0, 0x20)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1C, 0x1)
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1D4C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_75(0x1, 0x2, 0x0)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(0, 12000, -56000, 0)
    MoveCamera(315, -10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_68(0, 8500, -56000, 3000)
    MoveCamera(0, 15, 0, 3000)
    SetCameraDistance(35000, 3000)
    BeginChrThread(0x1C, 0, 0, 28)
    BeginChrThread(0x1C, 3, 0, 32)
    Sound(919, 0, 80, 0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0x0, 0x1C, 0x0, 0, 0, 0, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x1C, 0x0, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_28A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_28A8)
    OP_75(0x1, 0x1, 0x3E8)
    WaitChrThread(0x1C, 2)
    CancelBlur(1000)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1C, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_6F(0x79)
    OP_0D()
    SetMapObjFlags(0x1, 0x4)
    SetChrFlags(0x1C, 0x80)
    Sleep(700)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_90(0x0, 0, 5000, -63000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_31_2676 end

    def Function_32_2940(): pass

    label("Function_32_2940")

    OP_74(0x1, 0x19)
    OP_71(0x1, 0x50, 0x5A, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x5A, 0x6D, 0x0, 0x20)
    Return()

    # Function_32_2940 end

    def Function_33_2964(): pass

    label("Function_33_2964")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 2500, -23700, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x16, 0xFF)
    SetChrPos(0x101, 0, 1210, -24340, 0)
    OP_0D()

    #C0053
    ChrTalk(
        0x16,
        "欢迎来到『镜之城』。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x16,
        (
            "这里是一座探索型的娱乐设施，\x01",
            "进去之后，目标就是爬到\x01",
            "『实现愿望的镜子』所在的最顶层。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x16,
        (
            "如果有条件，建议您\x01",
            "与同伴一起入场……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#00004F#6P（……要邀请谁呢？）\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要邀请谁？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "艾莉")
    MenuCmd(1, 0, "缇欧")
    MenuCmd(1, 0, "兰迪")
    MenuCmd(1, 0, "诺艾尔")
    MenuCmd(1, 0, "瓦吉")
    MenuCmd(1, 0, "琪雅")
    MenuCmd(1, 0, "芙兰")
    MenuCmd(1, 0, "塞茜尔")
    MenuCmd(1, 0, "伊莉娅")
    MenuCmd(1, 0, "莉夏")
    MenuCmd(1, 0, "修利")
    MenuCmd(1, 0, "放弃")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B25")
    MenuCmd(3, 0, 0x0)

    label("loc_2B25")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B37")
    MenuCmd(3, 0, 0x1)

    label("loc_2B37")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B49")
    MenuCmd(3, 0, 0x2)

    label("loc_2B49")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B5B")
    MenuCmd(3, 0, 0x3)

    label("loc_2B5B")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B6D")
    MenuCmd(3, 0, 0x4)

    label("loc_2B6D")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B7F")
    MenuCmd(3, 0, 0x5)

    label("loc_2B7F")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2B91")
    MenuCmd(3, 0, 0x6)

    label("loc_2B91")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2BA3")
    MenuCmd(3, 0, 0x7)

    label("loc_2BA3")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2BB5")
    MenuCmd(3, 0, 0x8)

    label("loc_2BB5")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2BC7")
    MenuCmd(3, 0, 0x9)

    label("loc_2BC7")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2BD9")
    MenuCmd(3, 0, 0xA)

    label("loc_2BD9")

    MenuCmd(2, 0, -1, 55, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3131")
    OP_D2(0x5, (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C73"),
        (1, "loc_2CA9"),
        (2, "loc_2CDF"),
        (3, "loc_2D15"),
        (4, "loc_2D4D"),
        (5, "loc_2D83"),
        (6, "loc_2DB9"),
        (7, "loc_2DEF"),
        (8, "loc_2E2B"),
        (9, "loc_2E67"),
        (10, "loc_2E9D"),
        (SWITCH_DEFAULT, "loc_2ED3"),
    )


    label("loc_2C73")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0058
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请艾莉吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2CA9")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0059
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请缇欧吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2CDF")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0060
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请兰迪吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2D15")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0061
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请诺艾尔吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2D4D")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请瓦吉吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2D83")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0063
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请琪雅吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2DB9")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0064
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请芙兰吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2DEF")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0065
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请塞茜尔姐姐吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2E2B")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0066
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请伊莉娅小姐吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2E67")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0067
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请莉夏吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2E9D")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0068
    ChrTalk(
        0x101,
        "#00000F#6P（好……就邀请修利吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2ED3")

    FadeToDark(500, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F2A"),
        (1, "loc_2F33"),
        (2, "loc_2F3C"),
        (3, "loc_2F45"),
        (4, "loc_2F4E"),
        (5, "loc_2F57"),
        (6, "loc_2F60"),
        (7, "loc_2F69"),
        (8, "loc_2F72"),
        (9, "loc_2F7B"),
        (10, "loc_2F84"),
        (SWITCH_DEFAULT, "loc_2F8D"),
    )


    label("loc_2F2A")

    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F33")

    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F3C")

    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F45")

    AddParty(0x8, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F4E")

    AddParty(0x4, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F57")

    AddParty(0x52, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F60")

    AddParty(0x55, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F69")

    AddParty(0x4B, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F72")

    AddParty(0x33, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F7B")

    AddParty(0x34, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F84")

    AddParty(0x65, 0xEF, 0xFF)
    Jump("loc_2F8D")

    label("loc_2F8D")

    SetChrPos(0x101, -500, 1030, -24600, 0)
    SetChrPos(0xEF, 500, 1030, -24600, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0069
    ChrTalk(
        0x16,
        "好，请把票交给我。\x02",
    )

    CloseMessageWindow()
    SubItemNumber('米修拉姆·奇幻乐园游乐券', 1)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把一张票交给了检票人员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0071
    ChrTalk(
        0x16,
        "已经收到您的票了。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x16,
        (
            "请到梦幻城堡『镜之城』中\x01",
            "尽情探索吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x16, 0x0, 0x1F4)
    OP_9B(0x0, 0x16, 0x0, 0x1F4, 0x7D0, 0x0)
    Sleep(200)
    Sound(116, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x1, 0xA, 0x1, 0x0)
    OP_79(0x0)

    def lambda_30A8():
        OP_98(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_30A8)
    OP_93(0x16, 0x5A, 0x1F4)
    WaitChrThread(0x16, 1)
    Sleep(300)
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)

    def lambda_30E6():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30E6)
    Sleep(50)

    def lambda_30FE():
        OP_9B(0x0, 0xEF, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_30FE)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1401", 0, 0, 0)
    IdleLoop()
    Jump("loc_3161")

    label("loc_3131")


    #C0073
    ChrTalk(
        0x16,
        "哦，不进去了吗？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x16,
        (
            "期待您\x01",
            "再次前来。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3161")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -28000, 180)
    EventEnd(0x5)
    Return()

    # Function_33_2964 end

    def Function_34_3179(): pass

    label("Function_34_3179")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -600, 1030, -24600, 90)
    SetChrPos(0xEF, 600, 1030, -24600, 270)
    OP_4B(0x16, 0xFF)
    FadeToBright(1000, 0)
    OP_68(0, 3000, -23700, 0)
    OP_68(0, 2500, -23700, 2500)
    MoveCamera(0, 12, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3241"),
        (1, "loc_32C6"),
        (2, "loc_3344"),
        (3, "loc_33CE"),
        (4, "loc_343F"),
        (5, "loc_34C4"),
        (6, "loc_354F"),
        (7, "loc_35CD"),
        (8, "loc_3662"),
        (9, "loc_36E7"),
        (10, "loc_3773"),
        (SWITCH_DEFAULT, "loc_37F1"),
    )


    label("loc_3241")


    #C0075
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，一起在城堡里闲逛，\x01",
            "真是很开心呢。\x02\x03",

            "#00100F那我就先\x01",
            "走啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#00100F呵呵，一会见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_32C6")


    #C0078
    ChrTalk(
        0x103,
        (
            "#00202F一起逛了镜之城……\x01",
            "真是很开心。\x02\x03",

            "#00202F那我就先失陪啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        "#00200F好的，一会见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_3344")


    #C0081
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，两个男人一起去玩\x01",
            "也挺开心呢。\x02\x03",

            "#00300F好，那我就先去别处逛逛了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        "#00300F嗯，我走啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_33CE")


    #C0084
    ChrTalk(
        0x109,
        (
            "#10109F镜之城真有意思呢。\x02\x03",

            "#10100F那我就先失陪啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x109,
        "#10100F好的，稍后见！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_343F")


    #C0087
    ChrTalk(
        0x105,
        (
            "#10304F镜之城……\x01",
            "真是相当有趣呢。\x02\x03",

            "#10300F好了，那我就先去\x01",
            "别处转转吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x105,
        "#10300F呵呵，再会。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_34C4")


    #C0090
    ChrTalk(
        0x153,
        (
            "#01109F哈，好大的城堡啊，\x01",
            "玩得真开心！\x02\x03",

            "#01100F那我先去\x01",
            "别处玩啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x153,
        "#01100F嘿嘿，一会见啦，罗伊德！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_354F")


    #C0093
    ChrTalk(
        0x156,
        (
            "#06409F呵呵，镜之城……\x01",
            "真是很有趣呢！\x02\x03",

            "#06400F那我就先失陪了～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x156,
        "#06400F好的，一会见！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_35CD")


    #C0096
    ChrTalk(
        0x14C,
        (
            "#05902F呵呵，看到了那么大的镜子和钟，\x01",
            "真是很开心呢。\x02\x03",

            "#05900F好啦，我要去\x01",
            "其它地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x14C,
        "#05900F嗯，那我走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_3662")


    #C0099
    ChrTalk(
        0x134,
        (
            "#01709F呵呵，真是个\x01",
            "值得一去的城堡啊。\x02\x03",

            "#01700F好，那我要去\x01",
            "别的地方啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x134,
        "#01700F嗯，我走啦～\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_36E7")


    #C0102
    ChrTalk(
        0x135,
        (
            "#01809F呵呵，在那么漂亮的城堡里散步，\x01",
            "真是很开心呢。\x02\x03",

            "#01802F那我这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x135,
        "#01802F好的，失陪……\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_3773")


    #C0105
    ChrTalk(
        0x166,
        (
            "#14002F……在城堡里逛逛\x01",
            "倒也有点意思。\x02\x03",

            "#14000F好，那我这就走啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#00000F嗯，稍后见。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x166,
        "#14000F嗯，先走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37F1")

    label("loc_37F1")

    BeginChrThread(0xEF, 3, 0, 35)
    WaitChrThread(0xEF, 3)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3846"),
        (1, "loc_3854"),
        (2, "loc_3862"),
        (3, "loc_3870"),
        (4, "loc_387E"),
        (5, "loc_388C"),
        (6, "loc_389A"),
        (7, "loc_38A8"),
        (8, "loc_38B6"),
        (9, "loc_38C4"),
        (10, "loc_38D2"),
        (SWITCH_DEFAULT, "loc_38E0"),
    )


    label("loc_3846")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_3854")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x20000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_3862")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_3870")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_387E")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_388C")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x200000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_389A")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x400000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_38A8")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x800000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_38B6")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_38C4")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_38D2")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_38E0")

    label("loc_38E0")

    OP_D2(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('米修拉姆·奇幻乐园游乐券', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_391D")
    StopSound(126, 1000, 70)
    StopSound(821, 1000, 40)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1300", 0, 0, 0)
    IdleLoop()

    label("loc_391D")

    OP_4C(0x16, 0xFF)
    SetChrPos(0x0, 0, 0, -29000, 180)
    EventEnd(0x5)
    Return()

    # Function_34_3179 end

    def Function_35_3935(): pass

    label("Function_35_3935")


    def lambda_393A():
        OP_93(0xFE, 0xB4, 0xC8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_393A)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_394E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_394E)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0xFE, 1)
    EndChrThread(0x101, 0x2)
    Return()

    # Function_35_3935 end

    def Function_36_3975(): pass

    label("Function_36_3975")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1D, 0x0)
    OP_68(6540, 5060, -25400, 0)
    MoveCamera(320, 41, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(8910, 0)
    SetChrPos(0x101, 2560, 1600, -22190, 90)
    SetChrPos(0xEF, 2590, 1290, -23560, 90)
    OP_4B(0x1D, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    #C0108
    ChrTalk(
        0x101,
        "#00000F找到了……！\x02",
    )

    CloseMessageWindow()
    OP_9C(0x1D, 0x0, 0x0, 0x0, 0x1F4, 0xBB8)
    Sleep(500)
    TurnDirection(0x1D, 0x101, 500)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "呀！被发现啦☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，小哥哥，你好厉害呀～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2110, 3600, -34340, 0)
    MoveCamera(30, 32, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(10310, 0)
    SetChrPos(0x1D, 80, 0, -29860, 180)
    SetChrPos(0x101, -500, 0, -31500, 0)
    SetChrPos(0xEF, 500, 0, -31500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0111
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "竟然能在这么短的时间内\x01",
            "连续五次找到我……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，我这次\x01",
            "真是彻底败了呢～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "小哥哥，你才是真正的\x01",
            "捉迷藏之王哟～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3BB2")
    OP_63(0x153, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3C2A")

    label("loc_3BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_3BD2")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3C2A")

    label("loc_3BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3BF2")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3C2A")

    label("loc_3BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3C12")
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_3C2A")

    label("loc_3C12")

    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3C2A")

    Sleep(1000)

    #C0114
    ChrTalk(
        0x101,
        "#00006F捉、捉迷藏之王……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_3C8A")

    #C0115
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，得到了一个\x01",
            "不可思议的称号呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_3CC0")

    #C0116
    ChrTalk(
        0x103,
        (
            "#00202F不愧是咪雪……\x01",
            "性格真开朗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_3CF4")

    #C0117
    ChrTalk(
        0x104,
        (
            "#00302F得到了一个\x01",
            "奇怪的称号啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3CF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_3D32")

    #C0118
    ChrTalk(
        0x109,
        (
            "#10102F啊哈哈……得到了一个\x01",
            "奇怪的称号呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_3D66")

    #C0119
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，这称号\x01",
            "倒也挺帅嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_3D8D")

    #C0120
    ChrTalk(
        0x153,
        "#01109F罗伊德好棒！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_3DC9")

    #C0121
    ChrTalk(
        0x156,
        (
            "#06409F呵呵，得到了一个\x01",
            "很有趣的称号啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_3DFA")

    #C0122
    ChrTalk(
        0x14C,
        "#05902F呵呵，很可爱的称号啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_3E25")

    #C0123
    ChrTalk(
        0x134,
        "#01702F呵呵，很不错嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_3E63")

    #C0124
    ChrTalk(
        0x135,
        (
            "#01802F啊、啊哈哈……\x01",
            "真是个奇妙的称号呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E91")

    label("loc_3E63")


    #C0125
    ChrTalk(
        0x166,
        (
            "#14002F啊哈哈，\x01",
            "得到了一个奇怪的称号呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E91")


    #C0126
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "另外，作为\x01",
            "找到我的奖励，\x01",
            "就把这个奖品送给你们吧～☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0127
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '咪雪挂饰'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('咪雪挂饰', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0128
    ChrTalk(
        0x101,
        "#00000F嗯，谢谢啦。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "咪嘻嘻，不用客气☆\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "嗯，那我差不多\x01",
            "也该离开啦～\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1D,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "在接下来的时间里，一定要在\x01",
            "奇幻乐园内多留下些美好回忆哦～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3FBA():

        label("loc_3FBA")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_3FBA")

    QueueWorkItem2(0x101, 1, lambda_3FBA)

    def lambda_3FCC():

        label("loc_3FCC")

        TurnDirection(0xFE, 0x1D, 500)
        Yield()
        Jump("loc_3FCC")

    QueueWorkItem2(0xEF, 1, lambda_3FCC)
    OP_95(0x1D, -1420, 0, -29670, 2000, 0x0)
    OP_95(0x1D, -1630, 230, -38320, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)

    def lambda_400E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_400E)
    Sleep(50)

    def lambda_401E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_401E)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4066")

    #C0132
    ChrTalk(
        0x101,
        (
            "#00012F哈哈……\x01",
            "咪西的妹妹\x01",
            "真是很活泼呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_4066")


    #C0133
    ChrTalk(
        0x101,
        (
            "#00012F哈哈……\x01",
            "咪西的妹妹\x01",
            "真是很活泼啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4095")

    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_40DF")

    #C0134
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，是啊。\x02\x03",

            "#00100F好啦，\x01",
            "我也该走了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_40DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4135")

    #C0135
    ChrTalk(
        0x103,
        (
            "#00204F呵呵，是啊，\x01",
            "比传闻中更可爱。\x02\x03",

            "#00200F那么，我就此\x01",
            "失陪了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_4135")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_417E")

    #C0136
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，是啊。\x02\x03",

            "#00300F好了，我差不多\x01",
            "也该走啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_417E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_41C1")

    #C0137
    ChrTalk(
        0x109,
        (
            "#10109F呵呵，是啊。\x02\x03",

            "#10100F那么，\x01",
            "我也要走啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_41C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4206")

    #C0138
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，是啊。\x02\x03",

            "#10300F好，我也就此\x01",
            "失陪啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_4206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_4259")

    #C0139
    ChrTalk(
        0x153,
        (
            "#01109F嘿嘿，真想再次遇到它。\x02\x03",

            "#01104F好，琪雅也要\x01",
            "去别处玩了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_4259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_42AA")

    #C0140
    ChrTalk(
        0x156,
        (
            "#06409F呵呵，的确～\x02\x03",

            "#06400F好了，我差不多\x01",
            "也该去别处看看了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_42AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_42F3")

    #C0141
    ChrTalk(
        0x14C,
        (
            "#05904F呵呵，确实。\x02\x03",

            "#05900F好，我也去\x01",
            "别处逛逛好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_42F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4344")

    #C0142
    ChrTalk(
        0x134,
        (
            "#01709F呵呵，的确很不错。\x02\x03",

            "#01700F好，我也要去\x01",
            "别的地方玩了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_4344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_4397")

    #C0143
    ChrTalk(
        0x135,
        (
            "#01809F呵呵，确实。\x02\x03",

            "#01802F那么，我差不多也该走啦，\x01",
            "就此告辞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D6")

    label("loc_4397")


    #C0144
    ChrTalk(
        0x166,
        (
            "#14006F真是个奇怪的家伙。\x02\x03",

            "#14000F好啦，我要去\x01",
            "别处玩了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43D6")

    TurnDirection(0x101, 0xEF, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_4404")

    #C0145
    ChrTalk(
        0x101,
        "#00000F嗯，一会见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_441F")

    label("loc_4404")


    #C0146
    ChrTalk(
        0x101,
        "#00000F嗯，一会见吧。\x02",
    )

    CloseMessageWindow()

    label("loc_441F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 7)), scpexpr(EXPR_END)), "loc_4440")
    RemoveParty(0x1, 0xFF)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_44E1")

    label("loc_4440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 0)), scpexpr(EXPR_END)), "loc_4451")
    RemoveParty(0x2, 0xFF)
    Jump("loc_44E1")

    label("loc_4451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 1)), scpexpr(EXPR_END)), "loc_4462")
    RemoveParty(0x3, 0xFF)
    Jump("loc_44E1")

    label("loc_4462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 2)), scpexpr(EXPR_END)), "loc_4478")
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_44E1")

    label("loc_4478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 3)), scpexpr(EXPR_END)), "loc_4489")
    RemoveParty(0x4, 0xFF)
    Jump("loc_44E1")

    label("loc_4489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 4)), scpexpr(EXPR_END)), "loc_449A")
    RemoveParty(0x52, 0xFF)
    Jump("loc_44E1")

    label("loc_449A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 5)), scpexpr(EXPR_END)), "loc_44AB")
    RemoveParty(0x55, 0xFF)
    Jump("loc_44E1")

    label("loc_44AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 6)), scpexpr(EXPR_END)), "loc_44BC")
    RemoveParty(0x4B, 0xFF)
    Jump("loc_44E1")

    label("loc_44BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C8, 7)), scpexpr(EXPR_END)), "loc_44CD")
    RemoveParty(0x33, 0xFF)
    Jump("loc_44E1")

    label("loc_44CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C9, 0)), scpexpr(EXPR_END)), "loc_44DE")
    RemoveParty(0x34, 0xFF)
    Jump("loc_44E1")

    label("loc_44DE")

    RemoveParty(0x65, 0xFF)

    label("loc_44E1")

    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【咪雪的挑战】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7F, 0x1, 0xF)
    OP_29(0x7F, 0x4, 0x10)
    SetScenarioFlags(0x1C9, 7)
    OP_65(0x0, 0x1)
    SetChrFlags(0x1D, 0x80)
    SetChrPos(0x0, 10, 150, -36180, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_36_3975 end

    def Function_37_454E(): pass

    label("Function_37_454E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10200.itc", 0x1E)
    LoadChrToIndex("chr/ch45400.itc", 0x1F)
    LoadChrToIndex("chr/ch22200.itc", 0x20)
    LoadChrToIndex("chr/ch23000.itc", 0x21)
    LoadEffect(0x0, "battle/ms00109.eff")
    SoundLoad(862)
    SoundLoad(645)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x1E, 0x20)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x103, 0x1000)
    SetChrFlags(0x1E, 0x1000)
    SetChrFlags(0x1F, 0x1000)
    OP_68(1270, 2520, -36760, 0)
    MoveCamera(51, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(11430, 0)
    SetChrPos(0x101, -300, 300, -43880, 0)
    SetChrPos(0x103, 770, 340, -44750, 0)
    SetChrPos(0x109, 3940, 150, -36320, 0)
    SetChrPos(0x105, 3870, 50, -34830, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_68(1110, 2520, -36960, 3000)
    SetCameraDistance(13230, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_4677():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4677)
    Sleep(50)

    def lambda_4694():
        OP_97(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4694)
    Sleep(500)
    OP_63(0x109, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    WaitChrThread(0x103, 1)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4711():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4711)
    Sleep(50)

    def lambda_4721():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4721)
    Sleep(300)

    #C0148
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F呀，是诺艾尔和瓦吉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4756():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4756)
    Sleep(50)

    def lambda_4766():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4766)
    Sleep(300)

    def lambda_4776():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4776)
    Sleep(50)

    def lambda_4793():
        OP_97(0xFE, 0x3E8, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4793)
    WaitChrThread(0x101, 1)

    def lambda_47B1():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47B1)
    Sleep(50)

    def lambda_47C1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_47C1)
    Sleep(300)

    #C0149
    ChrTalk(
        0x105,
        "#10300F呵呵，好久不见啦。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        (
            "#10101F啊，听我说哦，\x01",
            "罗伊德警官！\x02\x03",

            "#10103F瓦吉可真是的，\x01",
            "稍微一不注意，\x01",
            "马上就到处乱逛……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，反正应该也不会\x01",
            "发生什么大事件。\x02\x03",

            "#10304F既然来这里巡视，\x01",
            "自然应该适当玩一玩，\x01",
            "难道你不这么想吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F当然不这么想，\x01",
            "真是的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x1, 0x8)
    OP_79(0x0)
    Fade(250)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1E, -760, 1600, -21700, 180)
    SetChrPos(0x1F, 650, 1600, -21700, 180)
    OP_0D()
    TurnDirection(0x103, 0x1F, 500)
    Sleep(300)

    #C0153
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F啊……\x01",
            "罗伊德前辈，有小孩子来了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("小孩的声音")

    #A0154
    AnonymousTalk(
        0xFF,
        "#4S是咪西！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 20, -1, -1)
    SetChrName("小孩的声音")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            "#4S啊，咪雪也在\x01",
            "这里！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_49E0():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_49E0)
    Sleep(50)

    def lambda_49F0():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_49F0)
    Sleep(50)

    def lambda_4A00():
        TurnDirection(0xFE, 0x1F, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A00)
    OP_63(0x101, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_70(0x0, 0x0)
    OP_68(-800, 2520, -37470, 3000)
    MoveCamera(43, 32, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(11660, 3000)

    def lambda_4A93():
        OP_95(0xFE, -440, 60, -35850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4A93)
    Sleep(100)

    def lambda_4AB0():
        OP_95(0xFE, 710, 10, -34740, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4AB0)

    def lambda_4ACA():

        label("loc_4ACA")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_4ACA")

    QueueWorkItem2(0x109, 1, lambda_4ACA)

    def lambda_4ADC():

        label("loc_4ADC")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_4ADC")

    QueueWorkItem2(0x105, 1, lambda_4ADC)
    WaitChrThread(0x1E, 1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)

    def lambda_4AFA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4AFA)
    Sleep(50)

    def lambda_4B0A():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4B0A)
    Sleep(300)

    #C0156
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05528F（……来不及躲藏了。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x1E,
        "嘿！我踢！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    BeginChrThread(0x1E, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x1F, 3, 0, 38)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F（等、等一下……！？）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        "#10309F哈哈……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        (
            "#10105F等、等一下，\x01",
            "你们不能这样啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x1E,
        (
            "大姐姐，你不知道吗～？\x01",
            "踢咪西\x01",
            "会得到幸福哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x1F,
        (
            "因为咪西的屁股里\x01",
            "有很多幸福呢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x1F,
        "呀哈哈哈！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F（得、得到幸福……我从来没听说过！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    WaitChrThread(0x1E, 3)
    OP_64(0x101)

    def lambda_4C88():
        TurnDirection(0x1E, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_4C88)
    Sleep(50)
    TurnDirection(0x1F, 0x103, 500)

    #C0165
    ChrTalk(
        0x1F,
        "咪雪也可以踢吧？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F（……！）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F（怎、怎么办？\x01",
            "  必须要马上做出应对……）\x07\x00\x02",
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
            "喝斥对方\x01",      # 0
            "胳肢对方\x01",      # 1
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
        (0, "loc_4D82"),
        (1, "loc_4E42"),
        (SWITCH_DEFAULT, "loc_4F2C"),
    )


    label("loc_4D82")

    TurnDirection(0x101, 0x1E, 500)

    #C0168
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "喂！小鬼！\x01",
            "不要太得寸进尺啊！\x02\x03",

            "再敢乱来，\x01",
            "我可饶不了你们！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)
    Sleep(100)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0169
    ChrTalk(
        0x1E,
        "哇哇，咪西发怒了！？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1F,
        "快逃吧！\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x3)
    Jump("loc_4F2C")

    label("loc_4E42")

    OP_2C(0x86, 0x1)
    SetScenarioFlags(0x176, 6)
    TurnDirection(0x101, 0x1E, 500)

    #C0171
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "对付你们这样的孩子……\x01",
            "就要这样！\x02\x03",

            "我挠挠挠挠挠……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1F, 0x101, 500)
    Sleep(100)
    OP_9C(0x1E, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    OP_63(0x1E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x1E,
        (
            "呀……\x01",
            "呀哈哈哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1F,
        (
            "哇哇，咪西\x01",
            "反击了！！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1F,
        "快逃呀！\x02",
    )

    CloseMessageWindow()
    OP_29(0x86, 0x1, 0x4)
    Jump("loc_4F2C")

    label("loc_4F2C")


    def lambda_4F31():
        OP_97(0xFE, 0xFFFFF95C, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4F31)
    Sleep(100)

    def lambda_4F4E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_4F4E)
    WaitChrThread(0x1F, 1)

    def lambda_4F6C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4F6C)

    def lambda_4F86():

        label("loc_4F86")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_4F86")

    QueueWorkItem2(0x101, 1, lambda_4F86)

    def lambda_4F98():

        label("loc_4F98")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_4F98")

    QueueWorkItem2(0x103, 1, lambda_4F98)

    def lambda_4FAA():

        label("loc_4FAA")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_4FAA")

    QueueWorkItem2(0x109, 1, lambda_4FAA)

    def lambda_4FBC():

        label("loc_4FBC")

        TurnDirection(0xFE, 0x1E, 500)
        Yield()
        Jump("loc_4FBC")

    QueueWorkItem2(0x105, 1, lambda_4FBC)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x1F, 1)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_93(0x105, 0xB4, 0x1F4)
    Sleep(50)
    OP_93(0x109, 0xB4, 0x1F4)
    OP_0D()

    #C0175
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05200F呼，总算走了。\x02\x03",

            "#05206F没想到突然就被踢了……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5040():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5040)
    Sleep(50)

    def lambda_5050():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5050)
    Sleep(300)

    #C0176
    ChrTalk(
        0x105,
        (
            "#10300F最近好像正在流行\x01",
            "这种踢咪西的游戏呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x109,
        "#10112F啊哈哈……真是灾难啊。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05203F话说回来……我刚才\x01",
            "那种行为不要紧吧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51CF")
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0179
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F……总比怒吼喝斥\x01",
            "好得多。\x02\x03",

            "#05520F咪西是治愈系的角色，\x01",
            "就算要驱赶对方，\x01",
            "也必须选择合适的方法。\x02\x03",

            "#05522F罗伊德前辈，\x01",
            "你的判断力果然很出色。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0180
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05202F哈哈……\x01",
            "多谢夸奖。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_531C")

    label("loc_51CF")

    OP_99(0x103, 0x101, 0xFA, 0x1388, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 700, 450, -35880, 315, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(645, 0, 30, 0)
    Sound(862, 0, 50, 0)
    Sound(811, 0, 100, 0)
    OP_9B(0x1, 0x103, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    #Sound(2031, 255, 100, 0)    #voice#Lloyd

    #C0181
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05211F哇哇！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)
    #Sound(2681, 255, 100, 0)    #voice#Tio

    #C0182
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05531F……真差劲。\x02\x03",

            "#05526F咪西是治愈系的角色，\x01",
            "就算要驱赶对方，\x01",
            "也必须选择合适的方法。\x02\x03",

            "#05520F遇到刚才那种情况时，\x01",
            "应该选择更温和的方式。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F好、好难啊……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_531C")


    #C0184
    ChrTalk(
        0x109,
        (
            "#10100F好啦，至少缇欧没有被踢，\x01",
            "总算是万幸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，你简直就像是\x01",
            "保护妹妹的骑士呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0186
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05206F穿成这种样子，就算被\x01",
            "如此夸奖也觉得很奇怪……\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05524F顺便一提，我听说\x01",
            "咪西的屁股很结实，\x01",
            "就算被踢也不会有事的。\x02\x03",

            "#05520F刚才应该没有想象中那么疼吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05205F原、原来如此，的确呢……\x02\x03",

            "#05203F（看来填充了缓冲材料，\x01",
            "  怪不得感觉硬梆梆的……）\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x15),
            "#05520F……啊，罗伊德前辈，\x01",
            "我们差不多也该去\x01",
            "下一个区域了。\x02\x03",

            "#05524F上午的任务安排\x01",
            "是很紧张的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "#05204F知、知道了。\x01",
            "……诺艾尔，瓦吉，\x01",
            "那我们就先走啦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x109,
        "#10109F请加油哦！\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x105,
        "#10300F呵呵，稍后再见吧。\x02",
    )

    CloseMessageWindow()

    def lambda_5582():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5582)
    Sleep(1000)

    def lambda_559F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_559F)
    Sleep(50)

    def lambda_55BC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_55BC)
    Sleep(50)

    def lambda_55CC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55CC)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("t1330", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_454E end

    def Function_38_55EF(): pass

    label("Function_38_55EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5629")
    OP_99(0xFE, 0x101, 0xFA, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    Sound(862, 0, 20, 0)
    OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1388, 0x0)
    Sleep(500)
    Jump("Function_38_55EF")

    label("loc_5629")

    Return()

    # Function_38_55EF end

    def Function_39_562A(): pass

    label("Function_39_562A")

    Sleep(1000)

    label("loc_562D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_564F")
    Sound(918, 0, 70, 0)
    Sleep(2200)
    Sound(918, 0, 60, 0)
    Sleep(5000)
    Jump("loc_562D")

    label("loc_564F")

    Return()

    # Function_39_562A end

    SaveToFile()

Try(main)
