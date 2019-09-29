from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t150b.bin",                # FileName
        "t150b",                    # MapName
        "t150b",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 0, 0, 1],
    )

    BuildStringList((
        "t150b",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "黑手党",                 # 3
        "黑手党",                 # 4
        "狗",                     # 5
        "狗",                     # 6
        "狗",                     # 7
        "索妮亚副司令",           # 8
        "诺艾尔上士",             # 9
        "塞茜尔",                 # 10
        "玛萨护士长",             # 11
        "警备队车辆",             # 12
        "警备队车辆",             # 13
        "警备队车辆",             # 14
        "警备队员",               # 15
        "警备队员",               # 16
        "警备队员",               # 17
        "警备队员",               # 18
        "巴士的乘客",             # 19
        "巴士的乘客",             # 20
        "SE控制",                 # 21
        "bt150b",                 # 22
        "bt155b",                 # 23
        "bt160b",                 # 24
        "乌尔斯拉间道",           # 25
    ))

    ATBonus("ATBonus_41C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_43C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4B07", 16,  7,   7,   7,   7,   7,   7)

    MonsterBattlePostion("MonsterBattlePostion_47C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 8, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_508", 5, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_50C", 11, 1, 0)
    MonsterBattlePostion("MonsterBattlePostion_510", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_518", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_53C", 0x0000, 34, 6, 60, 6, 1, 40, 0, "bt150b", "Sepith_4B07", 50, 50, 0, 0,
        (
            ("ms67101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_47C", "MonsterBattlePostion_4DC", "ed7402", "ed7403", "ATBonus_41C"),
            ("ms67101.dat", "ms67101.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_45C", "MonsterBattlePostion_4DC", "ed7402", "ed7403", "ATBonus_41C"),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_5AC", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt155b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", "ms67101.dat", "ms67101.dat", 0, 0, 0, "MonsterBattlePostion_4FC", "MonsterBattlePostion_4DC", "ed7402", "ed7403", "ATBonus_43C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5F0", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt160b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31103.dat", "ms31003.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_45C", "MonsterBattlePostion_4DC", "ed7402", "ed7403", "ATBonus_41C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
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
        "monster/ch67150.itc",               # 10
        "monster/ch67151.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-24410,  -920,    0,       0x1010000,    "BattleInfo_53C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-32990,  -21890,  -850,    0x1010000,    "BattleInfo_53C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-15590,  -21490,  -850,    0x1010000,    "BattleInfo_53C", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-38000,  3000,    20500,   1500,    -38000,  4000,    20500,   0x007C, 0,  16, 0x0000)
    DeclActor(2500,    1000,    0,       1500,    3000,    1500,    0,       0x007C, 0,  4,  0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_6BC",          # 00, 0
        "Function_1_751",          # 01, 1
        "Function_2_ABF",          # 02, 2
        "Function_3_AEB",          # 03, 3
        "Function_4_B01",          # 04, 4
        "Function_5_CF1",          # 05, 5
        "Function_6_DA1",          # 06, 6
        "Function_7_1AA5",         # 07, 7
        "Function_8_1AC1",         # 08, 8
        "Function_9_1AE0",         # 09, 9
        "Function_10_1AFA",        # 0A, 10
        "Function_11_1B14",        # 0B, 11
        "Function_12_3005",        # 0C, 12
        "Function_13_308C",        # 0D, 13
        "Function_14_3107",        # 0E, 14
        "Function_15_33F8",        # 0F, 15
        "Function_16_3473",        # 10, 16
        "Function_17_3748",        # 11, 17
        "Function_18_3C1B",        # 12, 18
        "Function_19_3C67",        # 13, 19
        "Function_20_3C81",        # 14, 20
        "Function_21_3CC5",        # 15, 21
        "Function_22_3CFB",        # 16, 22
        "Function_23_47B3",        # 17, 23
        "Function_24_47EC",        # 18, 24
        "Function_25_49C6",        # 19, 25
        "Function_26_4A2F",        # 1A, 26
        "Function_27_4A82",        # 1B, 27
    ))


    def Function_0_6BC(): pass

    label("Function_0_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D7")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_6F1")

    label("loc_6D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F1")
    Event(0, 14)

    label("loc_6F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_705")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)
    Jump("loc_750")

    label("loc_705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_719")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 11)
    Jump("loc_750")

    label("loc_719")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_72D")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 17)
    Jump("loc_750")

    label("loc_72D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_741")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 22)
    Jump("loc_750")

    label("loc_741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 5)), scpexpr(EXPR_END)), "loc_750")
    ClearScenarioFlags(0x5C, 5)
    Event(0, 24)

    label("loc_750")

    Return()

    # Function_0_6BC end

    def Function_1_751(): pass

    label("Function_1_751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_782")

    label("loc_76D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_782")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_782")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79B")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_79F")

    label("loc_79B")

    OP_65(0x1, 0x1)

    label("loc_79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B0")
    Call(0, 13)

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C1")
    Call(0, 15)

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_803")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    Jump("loc_837")

    label("loc_803")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_837")

    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_AB4")
    OP_1B(0x0, 0x0, 0x19)

    label("loc_AB4")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_1_751 end

    def Function_2_ABF(): pass

    label("Function_2_ABF")

    TalkBegin(0xFE)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "黑手党成员失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_2_ABF end

    def Function_3_AEB(): pass

    label("Function_3_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFD")
    Call(0, 16)
    Jump("loc_B00")

    label("loc_AFD")

    Call(0, 2)

    label("loc_B00")

    Return()

    # Function_3_AEB end

    def Function_4_B01(): pass

    label("Function_4_B01")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(2260, 2000, -290, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 1470, 1000, -200, 90)
    SetChrPos(0x102, -30, 1000, 260, 90)
    SetChrPos(0x103, 500, 1000, -1570, 90)
    SetChrPos(0x104, -680, 1000, -1150, 90)
    SetChrPos(0x106, -1710, 1000, -440, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门上了锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1E")

    #C0003
    ChrTalk(
        0x101,
        "#0013F#5P呜……在这种时候！？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0301F#1P没办法……\x01",
            "稍后再来这里吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE6, 5)

    label("loc_C1E")

    Jump("loc_CCE")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5B")

    #C0005
    ChrTalk(
        0x101,
        "#0000F#5P（好，只要有刚才的钥匙……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C5B")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "使用病房楼钥匙\x01",      # 0
            "不使用\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CAB"),
        (1, "loc_CC9"),
        (SWITCH_DEFAULT, "loc_CCE"),
    )


    label("loc_CAB")

    Sleep(300)
    Sound(809, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x2, 0x10)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0xE1, 3)
    Jump("loc_CCE")

    label("loc_CC9")

    Jump("loc_CCE")

    label("loc_CCE")

    SetChrPos(0x0, 0, 1000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_B01 end

    def Function_5_CF1(): pass

    label("Function_5_CF1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    FadeToBright(1000, 0)
    OP_68(-37070, 1800, 4550, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(39780, 0)
    OP_68(-33430, 1800, 2000, 6000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-21950, 1800, 18380, 0)
    MoveCamera(35, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(41350, 0)
    SetCameraDistance(39280, 4000)
    OP_6F(0x10)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t152B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_CF1 end

    def Function_6_DA1(): pass

    label("Function_6_DA1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("monster/ch67150.itc", 0x2C)
    LoadChrToIndex("monster/ch67151.itc", 0x2D)
    SetChrPos(0x101, -55600, 0, 100, 90)
    SetChrPos(0x102, -56570, 0, 940, 90)
    SetChrPos(0x103, -56780, 0, -1100, 90)
    SetChrPos(0x104, -57910, 0, -360, 90)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0x0)
    StopBGM(0x7D0)
    WaitBGM()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日 １８：５０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    PlayBGM("ed7303", 0)
    FadeToBright(1000, 0)
    OP_68(-12000, 2500, 450, 0)
    MoveCamera(60, 12, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(37890, 0)
    OP_68(-35000, 2200, 450, 12000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)

    def lambda_FFA():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FFA)

    def lambda_100F():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_100F)

    def lambda_1024():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1024)

    def lambda_1039():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1039)
    OP_68(-49500, 900, 0, 0)
    MoveCamera(90, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25500, 0)
    SetCameraDistance(24000, 3000)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0108F#6P太阳落山了呢……\x02\x03",

            "#0101F……不过，怎么会……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        (
            "#0306F#12P屋外的照明虽然正常，\x01",
            "但建筑物内的灯却都没亮啊。\x02\x03",

            "#0301F不管怎么想，情况也都不太正常啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#0201F#12P……时间还早，\x01",
            "正门就已经关上了。\x02\x03",

            "#0208F警备员去哪里了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0013F#6P唔……\x01",
            "总之，先去里面看看情况──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sound(836, 0, 100, 0)
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

    def lambda_1231():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1231)

    def lambda_123E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_123E)
    Sleep(100)

    def lambda_124E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_124E)

    def lambda_125B():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_125B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(-55500, 1300, 0, 0)
    MoveCamera(55, 20, 0, 0)
    SetCameraDistance(22500, 0)
    SetCameraDistance(20500, 1000)
    SetChrPos(0xC, -61500, 0, 0, 90)
    SetChrPos(0xD, -62500, 0, 1700, 90)
    SetChrPos(0xE, -63500, 0, -1700, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2D)
    SetChrSubChip(0xE, 0x0)
    BeginChrThread(0x1C, 1, 0, 9)
    BeginChrThread(0xC, 0, 0, 7)
    Sleep(50)
    BeginChrThread(0xD, 0, 0, 7)
    Sleep(50)
    BeginChrThread(0xE, 0, 0, 7)

    def lambda_1343():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1343)

    def lambda_1358():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1358)

    def lambda_136D():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_136D)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0x1C, 0x1)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x0)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xD, 0, 0, 8)
    BeginChrThread(0xE, 0, 0, 8)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0x101,
        "#0007F#11P这些家伙……！？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)
    OP_68(-55000, 1300, 0, 1000)

    def lambda_144E():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_144E)
    Sleep(50)

    def lambda_1466():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1466)
    Sleep(50)

    def lambda_147E():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_147E)
    Sleep(50)

    def lambda_1496():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1496)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_6F(0x79)

    #C0012
    ChrTalk(
        0x102,
        "#0107F#11P黑手党的军犬……！\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0307F#11P嘁……\x01",
            "刚才并没感觉到气息啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x5A, 0x2BC)

    #C0014
    ChrTalk(
        0x103,
        "#0207F#5P后面也有……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        "#0011F#11P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_68(-49000, 1000, 0, 2000)
    MoveCamera(50, 20, 0, 2000)
    SetCameraDistance(20500, 2000)

    def lambda_15AE():
        OP_93(0xFE, 0x5A, 0x2BC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15AE)
    Sleep(50)

    def lambda_15BE():
        OP_93(0xFE, 0x5A, 0x2BC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15BE)
    Sleep(50)

    def lambda_15CE():
        OP_93(0xFE, 0x5A, 0x2BC)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_15CE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Sound(113, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    SetChrPos(0x8, -40000, 0, -800, 270)
    SetChrPos(0x9, -40000, 0, 800, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1637():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1637)

    def lambda_164C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_164C)
    Sleep(100)

    def lambda_1660():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1660)

    def lambda_1675():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1675)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_79(0x6)
    OP_6F(0x79)
    OP_0D()

    #C0016
    ChrTalk(
        0x101,
        "#0007F#6P你们是……！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0101F#6P正奇怪为何不见踪影呢，\x01",
            "原来竟在这种地方……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0301F#6P你们这些混账……\x01",
            "到底要干什么！？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetCameraDistance(19000, 0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
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

    #C0021
    ChrTalk(
        0x101,
        "#0013F#6P唔……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#0103F#6P看起来，好像无法沟通呢……\x02",
    )

    CloseMessageWindow()
    OP_68(-54000, 900, 0, 2000)
    OP_68(-53500, 1000, 0, 2000)
    MoveCamera(55, 20, 0, 2000)
    SetCameraDistance(19500, 2000)

    def lambda_1887():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1887)
    Sleep(50)

    def lambda_1897():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1897)
    Sleep(650)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0x1C, 1, 0, 10)
    BeginChrThread(0xC, 0, 0, 7)
    BeginChrThread(0xD, 0, 0, 7)
    BeginChrThread(0xE, 0, 0, 7)

    def lambda_18D7():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_18D7)

    def lambda_18EC():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_18EC)

    def lambda_1901():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1901)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0x1C, 0x1)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x2C)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0xC, 0, 0, 8)
    BeginChrThread(0xD, 0, 0, 8)
    BeginChrThread(0xE, 0, 0, 8)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_0D()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0207F#6P小心点……\x01",
            "我有种不妙的感觉！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0307F#11P来了……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2B)
    SetChrSubChip(0x9, 0x0)

    def lambda_19B1():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19B1)

    def lambda_19C6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_19C6)
    SetChrChipByIndex(0xC, 0x2D)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x0)
    BeginChrThread(0x1C, 1, 0, 10)
    BeginChrThread(0xC, 0, 0, 7)
    BeginChrThread(0xD, 0, 0, 7)
    BeginChrThread(0xE, 0, 0, 7)

    def lambda_1A0B():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A0B)

    def lambda_1A20():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1A20)

    def lambda_1A35():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1A35)
    SetCameraDistance(14500, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x1C, 0x1)
    Battle("BattleInfo_5AC", 0x30200011, 0x0, 0x0, 0xE, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    Call(0, 11)
    Return()

    # Function_6_DA1 end

    def Function_7_1AA5(): pass

    label("Function_7_1AA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AC0")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_7_1AA5")

    label("loc_1AC0")

    Return()

    # Function_7_1AA5 end

    def Function_8_1AC1(): pass

    label("Function_8_1AC1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1ADF")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_1AC1")

    label("loc_1ADF")

    Return()

    # Function_8_1AC1 end

    def Function_9_1AE0(): pass

    label("Function_9_1AE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AF9")
    Sound(832, 0, 100, 0)
    Sleep(500)
    Jump("Function_9_1AE0")

    label("loc_1AF9")

    Return()

    # Function_9_1AE0 end

    def Function_10_1AFA(): pass

    label("Function_10_1AFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B13")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_10_1AFA")

    label("loc_1B13")

    Return()

    # Function_10_1AFA end

    def Function_11_1B14(): pass

    label("Function_11_1B14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    AddParty(0x5, 0xFF, 0xFF)
    OP_32(0x5, 0x0, 0x23)
    OP_32(0x5, 0x5, 0x64)
    RemoveCraft(0x5, 0xFFFF)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x5, 0x81, 0x2)
    OP_38(0x5, 0x82, 0x2)
    OP_38(0x5, 0x83, 0x2)
    OP_38(0x5, 0x84, 0x2)
    OP_38(0x5, 0x85, 0x2)
    OP_38(0x5, 0x86, 0x2)
    OP_42(0x5, 0x43D, 0xFF)
    OP_42(0x5, 0x5EC, 0xFF)
    OP_42(0x5, 0x650, 0xFF)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0x113)
    SetChrChipPat(0x5, 0x6, 0x113)
    AddCraft(0x5, 0x13B)
    OP_42(0x5, 0x69, 0x0)
    OP_42(0x5, 0x99, 0x5)
    OP_42(0x5, 0x78, 0x4)
    OP_42(0x5, 0x90, 0x3)
    OP_42(0x5, 0x87, 0x2)
    OP_42(0x5, 0x80, 0x1)
    OP_42(0x5, 0x7E, 0x6)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch31000.itc", 0x26)
    LoadChrToIndex("chr/ch31050.itc", 0x27)
    LoadChrToIndex("chr/ch31051.itc", 0x28)
    LoadChrToIndex("chr/ch31100.itc", 0x29)
    LoadChrToIndex("chr/ch31150.itc", 0x2A)
    LoadChrToIndex("chr/ch31151.itc", 0x2B)
    LoadChrToIndex("chr/ch31053.itc", 0x2C)
    LoadChrToIndex("chr/ch31153.itc", 0x2D)
    OP_68(-49000, 600, 0, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -52400, 0, 10, 90)
    SetChrPos(0x102, -53490, 0, 920, 90)
    SetChrPos(0x103, -53630, 0, -1030, 90)
    SetChrPos(0x104, -54650, 0, -140, 90)
    SetChrPos(0x106, -51650, 0, 6000, 180)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -47830, 0, 810, 270)
    SetChrPos(0x9, -48930, 0, -950, 270)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev603_00.eff")
    LoadEffect(0x2, "event\\ev202_00.eff")
    FadeToBright(1000, 0)
    OP_68(-51000, 600, 0, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0025
    ChrTalk(
        0x102,
        (
            "#0110F#6P呼、呼……\x01",
            "怎么会这么强……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0006F#6P看样子，果然是用那个药物\x01",
            "强化了身体能力啊……\x02\x03",

            "#0013F军犬可能也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0301F#6P可是……\x01",
            "这些家伙到底怎么了？\x02\x03",

            "一句话也不说，\x01",
            "只是默默地发动攻击……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0206F#6P……几乎感觉不到\x01",
            "任何感情的波动。\x02\x03",

            "#0208F这简直就像是──\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#11P……呜嗷嗷嗷嗷………\x02",
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
    Fade(500)
    OP_68(-48150, 600, 0, 0)
    MoveCamera(90, 25, 0, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(18500, 3000)
    OP_0D()

    #C0030
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60W#5P………啊啊啊………\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(202, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0xC8, 0xFA0, 0x1F4)

    def lambda_2029():
        OP_A6(0xFE, 0x28, 0x28, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2029)

    def lambda_2042():
        OP_A6(0xFE, 0x28, 0x28, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2042)
    Sleep(250)
    Fade(1000)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x8, 0x27)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_68(-50000, 600, 0, 1500)
    MoveCamera(90, 17, 0, 1500)
    SetCameraDistance(20150, 1500)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x25)
    SetChrSubChip(0x104, 0x0)

    def lambda_2112():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2112)
    Sleep(50)

    def lambda_212A():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_212A)
    Sleep(50)

    def lambda_2142():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2142)
    Sleep(50)

    def lambda_215A():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_215A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_6F(0x79)

    #C0031
    ChrTalk(
        0x101,
        "#0011F#6P这些家伙……！？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0307F#6P嘁……\x01",
            "应该已经完全打倒他们了啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        (
            "#0201F#12P这就是……\x01",
            "『真知』的力量……！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0101F#6P该、该怎么办……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1627, 255, 100, 0)    #voice#Yin
    Sleep(500)
    SetMessageWindowPos(0, 40, -1, -1)
    SetChrName("声音")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "──唉，\x01",
            "真会给人添麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-48350, 700, 0, 0)
    MoveCamera(45, 18, 0, 0)
    MoveCamera(55, 18, 0, 2000)
    SetCameraDistance(25500, 0)
    SetCameraDistance(15500, 2000)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x140, 0, 900, 0, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(200)

    def lambda_2318():
        OP_A6(0xFE, 0x28, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2318)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x1)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    Sound(502, 0, 100, 0)

    #C0036
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P啊……\x05\x02",
        )
    )

    Sleep(300)
    PlayEffect(0x1, 0xFF, 0x9, 0x140, 0, 900, 0, 45, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(255, 0, 100, 0)
    Sleep(200)

    def lambda_23A4():
        OP_A6(0xFE, 0x28, 0x28, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_23A4)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x1)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    Sound(502, 0, 100, 0)

    #C0037
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2P……唔……\x05\x02",
        )
    )

    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2D)
    SetChrSubChip(0x9, 0x3)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Call(0, 13)
    Sound(514, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(-51000, 600, 0, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    #C0038
    ChrTalk(
        0x102,
        "#0105F#5P刚才的针是……！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#0007F#5P『银』──你杀了他们吗！？\x02",
    )

    CloseMessageWindow()
    OP_68(-52550, 1000, 1850, 3000)
    MoveCamera(30, 18, 0, 3000)
    SetCameraDistance(18500, 3000)
    Sleep(1000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    BeginChrThread(0x106, 3, 0, 12)
    Sleep(700)

    def lambda_2500():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2500)
    Sleep(50)

    def lambda_2510():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2510)
    Sleep(50)

    def lambda_2520():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2520)
    Sleep(50)

    def lambda_2530():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2530)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 3)
    OP_6F(0x79)
    #Sound(1629, 255, 100, 0)    #voice#Yin
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0040
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "呵……只是将暗器刺入经脉，\x01",
            "切断气的流动而已。\x02\x03",

            "无论身体得到了如何强化，\x01",
            "暂时都会睡上一阵吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0041
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F#12P是、是吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#0306F#6P话说，你这家伙\x01",
            "还是如此神出鬼没啊……\x02\x03",

            "#0301F打探着鲁巴彻的动向，\x01",
            "结果一路找到了这里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x103, 300)
    Sleep(150)

    #C0043
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P是受曹所托。\x02\x03",

            "#0700F看起来，情况似乎变得\x01",
            "比预想中还要麻烦啊。\x02\x03",

            "『真知』……\x01",
            "我原本还只是将信将疑……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0205F#12P你为什么会知道这个名字……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#0101F#6P你们……\x01",
            "到底了解多少？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P呵呵……\x01",
            "也就是你们所掌握的那种情报量。\x02\x03",

            "鲁巴彻成员们的失踪，\x01",
            "还有『Ｄ∴Ｇ教团』残党的存在……\x02\x03",

            "至于更多的信息，\x01",
            "我和曹也还没有掌握。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F#12P是吗……\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0048
    ChrTalk(
        0x101,
        (
            "#0006F#12P──先不管你们的目的如何，\x01",
            "总之，如今事态十分紧急。\x02\x03",

            "医院内部恐怕已经被\x01",
            "黑手党成员们占据了。\x02\x03",

            "#0008F必须要尽快去确认\x01",
            "院内人员的安全。\x02\x03",

            "#0001F所以，『银』──\x01",
            "你能不能暂时与我们合作？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    def lambda_29B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29B5)
    Sleep(50)

    def lambda_29C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29C5)
    Sleep(50)

    def lambda_29D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29D5)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0049
    ChrTalk(
        0x102,
        "#0105F#1P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        "#0305F#6P喂，这家伙可是……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P哼哼……\x01",
            "还以为你要说什么呢。\x02\x03",

            "你们难道想依靠\x01",
            "本该抓捕的犯罪者\x01",
            "的力量吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F#12P我不是说过了吗，如今事态紧急。\x02\x03",

            "#0000F而且，你应该也想用自己的方式\x01",
            "找到真相吧。\x02\x03",

            "那么，救助医院内的相关人士，\x01",
            "听取他们的证言，也是有所助益的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P呵呵……说到底，\x01",
            "也就是利益对等的合作关系吗？\x02\x03",

            "#0700F──好吧，\x01",
            "这次我就帮帮你们。\x02\x03",

            "只是，如果你们碍手碍脚，\x01",
            "我就会单独行动。\x02\x03",

            "没意见吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F#12P嗯，没问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#0106F#1P真是的……\x01",
            "该说你当机立断吗………\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#0211F#6P像这种时候，罗伊德前辈\x01",
            "还真是大胆得过头呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0303F#6P不过，现在的确也\x01",
            "不是犹豫不决的时候啊。\x02\x03",

            "#0300F那么，我们就尽快开始\x01",
            "医院内部的搜索吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0058
    ChrTalk(
        0x101,
        (
            "#0003F#11P嗯，总之，先去确认\x01",
            "医院内相关人员的安全吧。\x02\x03",

            "#0001F顺便向他们探听一下情况，\x01",
            "应该就能了解发生什么事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        "#0101F#1P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0201F#6P明白。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P呵呵……\x01",
            "那就走吧。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")

    def lambda_2D8D():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D8D)

    def lambda_2D9A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D9A)
    Sleep(100)

    def lambda_2DAA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DAA)

    def lambda_2DB7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2DB7)
    Sleep(100)

    def lambda_2DC7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2DC7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    Fade(1000)
    SetChrPos(0x101, -52190, 0, 160, 90)
    SetChrPos(0x102, -54770, 0, -200, 90)
    SetChrPos(0x103, -53560, 0, -810, 90)
    SetChrPos(0x104, -53990, 0, 790, 90)
    SetChrPos(0x106, -51770, 0, 2400, 90)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-49330, 2000, 0, 0)
    MoveCamera(90, 7, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(22500, 2000)
    OP_6F(0x10)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7510", 0)
    ReplaceBGM("ed7123", "ed7510")

    #C0062
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0008F#6P#N（塞茜尔姐姐……\x01",
            "  你一定要平安无事啊。）\x02\x03",

            "#0013F（我一定……\x01",
            "  会把大家都救出来的！）\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-49330, 3900, 0, 5000)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "银加入了队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在主菜单的[TACTICS]选项中\x01",
            "可以将其设置为参战队员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_37()
    SetChrPos(0x0, -53000, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0xE0, 3)
    OP_29(0x4D, 0x1, 0x3)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_11_1B14 end

    def Function_12_3005(): pass

    label("Function_12_3005")

    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_305A():
        OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_305A)

    def lambda_306F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_306F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_12_3005 end

    def Function_13_308C(): pass

    label("Function_13_308C")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, -47830, 0, 810, 315)
    SetChrPos(0x9, -48930, 0, -950, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_13_308C end

    def Function_14_3107(): pass

    label("Function_14_3107")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(-32180, 4200, 22060, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -34350, 3000, 21720, 270)
    SetChrPos(0x102, -33520, 3000, 20960, 270)
    SetChrPos(0x103, -33020, 3000, 22710, 270)
    SetChrPos(0x104, -31720, 3000, 22660, 270)
    SetChrPos(0x106, -31870, 3000, 21200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xA, -39000, 3000, 22500, 90)
    SetChrPos(0xB, -39000, 3000, 20500, 90)
    FadeToBright(1000, 0)
    OP_68(-35060, 4200, 21920, 1800)
    Sleep(1500)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#0013F#11P连这种地方也有……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0066
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#11P快收拾掉。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    SetCameraDistance(18000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)

    def lambda_3348():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3348)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)

    def lambda_3365():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3365)
    Sleep(500)
    Battle("BattleInfo_5F0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    Call(0, 15)
    SetMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_37()
    SetChrPos(0x0, -34500, 3000, 22500, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE0, 7)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_3107 end

    def Function_15_33F8(): pass

    label("Function_15_33F8")

    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xA, -38000, 3000, 22500, 90)
    SetChrPos(0xB, -38000, 3000, 20500, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Return()

    # Function_15_33F8 end

    def Function_16_3473(): pass

    label("Function_16_3473")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_68(-37230, 4400, 19950, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -36530, 3000, 20520, 270)
    SetChrPos(0x102, -35450, 3000, 19960, 270)
    SetChrPos(0x103, -34940, 3000, 21590, 270)
    SetChrPos(0x104, -33840, 3000, 21430, 270)
    SetChrPos(0x106, -33890, 3000, 20130, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "黑手党成员失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0068
    ChrTalk(
        0x101,
        "#0001F#11P嗯……？\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "倒下的黑手党旁边\x01",
            "似乎掉落了什么小东西……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x334, 1)

    #C0071
    ChrTalk(
        0x101,
        "#0005F#11P这是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 1)), scpexpr(EXPR_END)), "loc_3648")

    #C0072
    ChrTalk(
        0x102,
        (
            "#0103F#11P看起来，似乎是从护士长\x01",
            "那里抢来的病房楼入口钥匙。\x02\x03",

            "#0100F只要有这个的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3700")

    label("loc_3648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 5)), scpexpr(EXPR_END)), "loc_36A9")

    #C0073
    ChrTalk(
        0x103,
        (
            "#0203F#11P似乎是病房楼入口处\x01",
            "那个上锁大门的钥匙呢。\x02\x03",

            "#0202F只要有这个的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3700")

    label("loc_36A9")


    #C0074
    ChrTalk(
        0x104,
        (
            "#0303F#11P大概是他们从院内工作人士\x01",
            "的手中抢来的。\x02\x03",

            "#0300F应该可以用在什么地方吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3700")


    #C0075
    ChrTalk(
        0x101,
        "#0000F#11P嗯，试试看吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -35500, 3000, 21100, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xE1, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_16_3473 end

    def Function_17_3748(): pass

    label("Function_17_3748")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("chr/ch29600.itc", 0x21)
    LoadChrToIndex("apl/ch50157.itc", 0x22)
    LoadChrToIndex("apl/ch50157.itc", 0x23)
    LoadChrToIndex("chr/ch31350.itc", 0x24)
    LoadChrToIndex("chr/ch31351.itc", 0x25)
    LoadChrToIndex("chr/ch21000.itc", 0x26)
    LoadChrToIndex("chr/ch20300.itc", 0x27)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -23560, 0, -5040, 90)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -23900, 0, -3970, 90)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -21800, 0, -4800, 270)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -21800, 0, -3600, 270)
    SetChrFlags(0x12, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x5)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x16, 0x2)
    SetMapObjFlags(0x16, 0x400)
    SetChrFlags(0x13, 0x8000)
    OP_78(0x16, 0x13)
    SetMapObjFlags(0x16, 0x1000)
    SetMapObjFrame(0x16, "light", 0x0, 0x1)
    SetChrPos(0x13, -50360, 0, -2950, 0)
    OP_D3(0x13, 0x0, 0x1C138, 0x0, 0x0)
    OP_74(0x16, 0x1E)
    OP_70(0x16, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    SetMapObjFlags(0x17, 0x400)
    SetChrFlags(0x14, 0x8000)
    OP_78(0x17, 0x14)
    SetMapObjFlags(0x17, 0x1000)
    SetChrPos(0x14, -47990, 0, 10910, 0)
    OP_D3(0x14, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x17, 0x1E)
    OP_70(0x17, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x2)
    SetMapObjFlags(0x18, 0x400)
    SetChrFlags(0x15, 0x8000)
    OP_78(0x18, 0x15)
    SetMapObjFlags(0x18, 0x1000)
    SetChrPos(0x15, -61810, 0, 1170, 0)
    OP_D3(0x15, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x18, 0x1E)
    OP_70(0x18, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x22)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x26)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x27)
    SetChrSubChip(0x1B, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AF0")
    OP_68(-51000, 3600, 2300, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x16, -47870, 0, 4190, 270)
    SetChrPos(0x17, -51270, 0, 9800, 180)
    SetChrPos(0x18, -52570, 0, 9800, 180)
    SetChrPos(0x19, -54240, 0, -1180, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 18)
    BeginChrThread(0x18, 3, 0, 18)
    OP_68(-51000, 1900, 2300, 6000)
    OP_6F(0x1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)

    label("loc_3AF0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C0E")
    OP_68(-35000, 3500, -6110, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x16, -20930, 0, 2850, 225)
    SetChrPos(0x17, -34310, 0, 500, 90)
    SetChrPos(0x18, -35750, 0, -660, 90)
    SetChrPos(0x19, -24040, 0, 10340, 180)
    SetChrPos(0x1A, -24810, 0, 11740, 180)
    SetChrPos(0x1B, -23540, 0, 12520, 180)
    SetChrChipByIndex(0x19, 0x23)
    SetChrSubChip(0x19, 0x0)
    FadeToBright(1000, 0)
    BeginChrThread(0x17, 3, 0, 19)
    BeginChrThread(0x18, 3, 0, 19)
    BeginChrThread(0x19, 3, 0, 20)
    BeginChrThread(0x1A, 3, 0, 21)
    BeginChrThread(0x1B, 3, 0, 21)
    OP_68(-25000, 3500, -6110, 12000)
    Sleep(1500)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    Sleep(7000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    EndChrThread(0x18, 0x3)
    EndChrThread(0x19, 0x3)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x3)

    label("loc_3C0E")

    SetScenarioFlags(0x5C, 3)
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3748 end

    def Function_18_3C1B(): pass

    label("Function_18_3C1B")


    def lambda_3C20():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C20)
    WaitChrThread(0xFE, 1)

    def lambda_3C39():
        OP_9B(0x0, 0xFE, 0xFFC4, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C39)
    WaitChrThread(0xFE, 1)

    def lambda_3C52():
        OP_9B(0x0, 0xFE, 0xFFC4, 0x2328, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C52)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_3C1B end

    def Function_19_3C67(): pass

    label("Function_19_3C67")


    def lambda_3C6C():
        OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C6C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_3C67 end

    def Function_20_3C81(): pass

    label("Function_20_3C81")


    def lambda_3C86():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C86)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_3CB0():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CB0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_3C81 end

    def Function_21_3CC5(): pass

    label("Function_21_3CC5")


    def lambda_3CCA():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CCA)
    WaitChrThread(0xFE, 1)
    Sleep(1000)

    def lambda_3CE6():
        OP_9B(0x0, 0xFE, 0x5A, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CE6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_21_3CC5 end

    def Function_22_3CFB(): pass

    label("Function_22_3CFB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch05700.itc", 0x1E)
    LoadChrToIndex("chr/ch00800.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("apl/ch50109.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_68(-50800, 2500, 0, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20600, 0)
    SetChrPos(0x101, -51540, 0, -50, 90)
    SetChrPos(0x102, -51540, 0, 1580, 135)
    SetChrPos(0x103, -53200, 0, -830, 90)
    SetChrPos(0x104, -53140, 0, 680, 90)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, -48700, 0, -1200, 270)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, -52280, 0, -2180, 45)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, -49400, 0, 0, 270)
    SetChrFlags(0x11, 0x8000)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x2)
    SetMapObjFlags(0x17, 0x400)
    SetChrFlags(0x14, 0x8000)
    OP_78(0x17, 0x14)
    SetMapObjFrame(0x17, "light", 0x0, 0x1)
    SetMapObjFlags(0x17, 0x1000)
    SetChrPos(0x14, -47990, 0, 10910, 0)
    OP_D3(0x14, 0x0, 0x0, 0x0, 0x0)
    OP_74(0x17, 0x1E)
    OP_70(0x17, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x2)
    SetMapObjFlags(0x18, 0x400)
    SetChrFlags(0x15, 0x8000)
    OP_78(0x18, 0x15)
    SetMapObjFlags(0x18, 0x1000)
    SetChrPos(0x15, -59090, 0, 1500, 0)
    OP_D3(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x18, 0x1E)
    OP_70(0x18, 0x0)
    FadeToBright(1000, 0)
    OP_68(-50800, 1000, 0, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(300)

    #C0076
    ChrTalk(
        0x11,
        (
            "#1300F#11P……是吗，\x01",
            "你们要立刻回市里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0006F#6P抱歉，塞茜尔姐姐……\x02\x03",

            "#0008F其实我们应该留下来帮忙\x01",
            "收拾修复才对……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x11,
        (
            "#1302F#11P呵呵，别介意。\x02\x03",

            "#1304F这里毕竟有警备队的各位在，\x01",
            "你们现在应该去做那些\x01",
            "只有你们才能做到的事。\x02\x03",

            "#1301F……小琪雅\x01",
            "说不定也有危险吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0003F#6P嗯……\x02\x03",

            "#0008F……说实话，约亚西姆医生\x01",
            "的目的至今还不清楚。\x02\x03",

            "在这种混乱的状态下，\x01",
            "我们也不知道应该如何行动……\x02\x03",

            "#0001F但是琪雅……\x01",
            "那个孩子，我一定会守护好的！\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        "#0103F#6P……我也一样。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#0201F#6P一定会……守护她。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0300F#6P嗯，就算拼上性命，\x01",
            "也绝对不会让她回到那个危险的混账身边。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x11,
        (
            "#1304F#11P呵呵……\x02\x03",

            "#1302F我想，最重要的是，\x01",
            "你们要守护什么，怎样去守护。\x02\x03",

            "只要不迷失这一点，\x01",
            "就一定能找到答案的。\x02\x03",

            "#1309F没问题……\x01",
            "你们一定能做到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0002F#6P塞茜尔姐姐……谢谢。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0109F#6P……听您这样一说，\x01",
            "真是安心很多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xF,
        (
            "#2004F#11P呵呵，我想说的话\x01",
            "基本都被说完了呢。\x02\x03",

            "#2001F──拘留所那边也遭到了袭击，\x01",
            "警备队似乎也相当混乱……\x02\x03",

            "我们准备联同贝尔加德门的部队\x01",
            "平息事态，进行善后工作。\x02\x03",

            "#2002F这一夜似乎会很漫长……\x01",
            "各位，努力渡过难关吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0000F#6P是……！\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        (
            "#0300F#6P嗯，我们会\x01",
            "发奋努力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xF,
        (
            "#2004F#11P那么，诺艾尔。\x02\x03",

            "#2002F情况紧急，立刻将罗伊德等人\x01",
            "送到克洛斯贝尔市吧。\x02\x03",

            "越快越好，\x01",
            "但注意不要出事故。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 500)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    #Sound(1479, 255, 100, 0)    #voice#Noel

    #C0090
    ChrTalk(
        0x10,
        "#0500F#6P遵命，长官！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(750)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x15, -59090, 0, 0, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-48880, -1500, 2620, 0)
    MoveCamera(60, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24490, 0)
    Sound(488, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_68(-48880, 200, 2620, 3000)
    SetCameraDistance(22490, 3000)
    OP_71(0x18, 0x79, 0xB4, 0x0, 0x20)

    def lambda_44E9():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_44E9)
    WaitChrThread(0x15, 1)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)
    TurnDirection(0xF, 0x11, 500)
    Sleep(300)

    #C0091
    ChrTalk(
        0xF,
        (
            "#2004F#11P好了……\x01",
            "开始医院内的修复行动吧。\x02\x03",

            "#2002F塞茜尔小姐，\x01",
            "你能带我们去研究楼吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0xF, 500)

    #C0092
    ChrTalk(
        0x11,
        "#1300F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 3, 0, 23)
    Sleep(1000)
    OP_68(-47790, 200, 1230, 3000)
    SetCameraDistance(20250, 3000)
    OP_93(0x11, 0x10E, 0x12C)
    OP_6F(0x79)

    #C0093
    ChrTalk(
        0x11,
        (
            "#1303F#11P#30W（各位，请多加小心。）\x02\x03",

            "#1301F#20W（盖伊……\x01",
            "  也请你守护罗伊德吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    EndChrThread(0xF, 0x3)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xA)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_29(0x4D, 0x1, 0xF)
    OP_29(0x4D, 0x4, 0x10)
    OP_29(0x4E, 0x4, 0x2)
    OP_29(0x4E, 0x1, 0x0)
    SubItemNumber(0x334, 1)
    SubItemNumber(0x335, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46C7")
    OP_29(0x29, 0x4, 0x40)
    Jump("loc_46D9")

    label("loc_46C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x29, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46D9")
    OP_29(0x29, 0x4, 0x40)

    label("loc_46D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x32, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EB")
    OP_29(0x32, 0x4, 0x40)

    label("loc_46EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4709")
    OP_29(0x34, 0x4, 0x40)
    Jump("loc_471B")

    label("loc_4709")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_471B")
    OP_29(0x34, 0x4, 0x40)

    label("loc_471B")

    SubItemNumber(0x2DA, 1)
    SubItemNumber(0x2D9, 1)
    SubItemNumber(0x2D8, 1)
    SubItemNumber(0x34B, 1)
    SubItemNumber(0x349, 1)
    SubItemNumber(0x34A, 1)
    SubItemNumber(0x343, 1)
    SubItemNumber(0x342, 1)
    SubItemNumber(0x344, 1)
    SubItemNumber(0x345, 1)
    SubItemNumber(0x359, 1)
    OP_E3(0xA)
    OP_E3(0x3)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    SetScenarioFlags(0x5F, 0)
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_3CFB end

    def Function_23_47B3(): pass

    label("Function_23_47B3")

    OP_93(0xFE, 0x5A, 0x1F4)

    def lambda_47BF():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_47BF)
    Sleep(3000)

    def lambda_47D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_47D7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_47B3 end

    def Function_24_47EC(): pass

    label("Function_24_47EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("monster/ch75650.itc", 0x20)
    ClearMapObjFlags(0x15, 0x4)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x8000)
    OP_A7(0xC, 0x37, 0x37, 0x37, 0xFF, 0x0)
    OP_A7(0xD, 0x37, 0x37, 0x37, 0xFF, 0x0)
    OP_A7(0xE, 0x37, 0x37, 0x37, 0xFF, 0x0)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xE, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, -53470, 0, 16170, 90)
    SetChrPos(0xD, -54800, 0, 17760, 90)
    SetChrPos(0xE, -55280, 0, 14310, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x8, -50350, 0, 17450, 270)
    SetChrPos(0x9, -50350, 0, 15980, 270)
    OP_68(-51440, 1000, 16260, 0)
    MoveCamera(40, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23910, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(60000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    EventEnd(0x5)
    Return()

    # Function_24_47EC end

    def Function_25_49C6(): pass

    label("Function_25_49C6")

    EventBegin(0x1)

    #C0094
    ChrTalk(
        0x101,
        (
            "#0001F事态紧急，\x01",
            "现在可不是回去的时候。\x02\x03",

            "赶快去确认\x01",
            "院内众人的安危吧……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_25_49C6 end

    def Function_26_4A2F(): pass

    label("Function_26_4A2F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St.Ursula \x01",
            "Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_4A2F end

    def Function_27_4A82(): pass

    label("Function_27_4A82")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Medical College\x01",
            "～招待所『雷克切』～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_4A82 end

    SaveToFile()

Try(main)
