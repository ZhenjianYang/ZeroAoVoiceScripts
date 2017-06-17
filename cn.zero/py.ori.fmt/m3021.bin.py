from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3021.bin",                # FileName
        "m3021",                    # MapName
        "m3021",                    # Location
        0x007D,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 2200, 238000, 0, 0, 1, 125, 0, 4, 0, 5],
    )

    BuildStringList((
        "m3021",                  # 0
        "矿工冈兹",               # 1
        "市民",                   # 2
        "市民",                   # 3
        "迪诺",                   # 4
        "尼克鲁",                 # 5
        "本德",                   # 6
        "贸易商利泽罗",           # 7
        "技师",                   # 8
        "阿奈斯特",               # 9
        "魔人阿奈斯特",           # 10
        "翼龙",                   # 11
        "翼龙",                   # 12
        "海洋月魔",               # 13
        "SE控制",                 # 14
        "bm3090",                 # 15
        "bm3081",                 # 16
    ))

    ATBonus("ATBonus_34C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_36C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_38C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_410", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_414", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_418", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_41C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_420", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_424", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_42C", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 0, 0, 180)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_490", 0x0010, 40, 6, 60, 0, 1, 0, 0, "bm3081", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68400.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", "ms75700.dat", 0, "ms75700.dat", 0, "MonsterBattlePostion_38C", "MonsterBattlePostion_40C", "ed7402", "ed7403", "ATBonus_34C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_44C", 0x0042, 40, 6, 60, 0, 0, 0, 0, "bm3090", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67400.dat", "ms70000.dat", "ms70000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_40C", "ed7405", "ed7000", "ATBonus_36C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch37600.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch20500.itc",                   # 02
        "chr/ch06800.itc",                   # 03
        "chr/ch28900.itc",                   # 04
        "chr/ch27600.itc",                   # 05
        "chr/ch27700.itc",                   # 06
        "apl/ch50523.itc",                   # 07
        "chr/ch26000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch68450.itc",               # 10
        "monster/ch68450.itc",               # 11
    ))

    DeclNpc(4500,    0,       235300,  270,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5800,    0,       236199,  270,  261,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(5800,    0,       234399,  270,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4610,    0,       188539,  270,  261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4500,    0,       223899,  270,  261,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4949,    0,       187440,  270,  261,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(4500,    0,       176000,  270,  261,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(5800,    0,       175100,  270,  261,  0x0, 0,   8,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    277,  0x0, 0,   7,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28500,   -46500,  26250,   0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(2300,    0,       206000,  1500,    2300,    2000,    206000,  0x007C, 0,  22, 0x0000)
    DeclActor(2300,    0,       194000,  1500,    2300,    2000,    194000,  0x007C, 0,  23, 0x0000)
    DeclActor(28500,   -48000,  26250,   1200,    28500,   -47000,  26250,   0x007C, 0,  6,  0x0000)
    DeclActor(0,       -240000, 31400,   1200,    0,       -239000, 31400,   0x007C, 0,  7,  0x0000)
    DeclActor(10500,   0,       214750,  1200,    10500,   1000,    214750,  0x007C, 0,  8,  0x0000)
    DeclActor(22250,   -66000,  30000,   1200,    22250,   -65000,  30000,   0x007C, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_564",          # 00, 0
        "Function_1_61C",          # 01, 1
        "Function_2_638",          # 02, 2
        "Function_3_655",          # 03, 3
        "Function_4_672",          # 04, 4
        "Function_5_785",          # 05, 5
        "Function_6_8FA",          # 06, 6
        "Function_7_AF4",          # 07, 7
        "Function_8_C2A",          # 08, 8
        "Function_9_D8D",          # 09, 9
        "Function_10_EC3",         # 0A, 10
        "Function_11_1064",        # 0B, 11
        "Function_12_120F",        # 0C, 12
        "Function_13_1379",        # 0D, 13
        "Function_14_14E6",        # 0E, 14
        "Function_15_1611",        # 0F, 15
        "Function_16_17A2",        # 10, 16
        "Function_17_1AB8",        # 11, 17
        "Function_18_1E5F",        # 12, 18
        "Function_19_1EBB",        # 13, 19
        "Function_20_1F15",        # 14, 20
        "Function_21_1F61",        # 15, 21
        "Function_22_25F6",        # 16, 22
        "Function_23_272F",        # 17, 23
        "Function_24_2868",        # 18, 24
        "Function_25_2DD2",        # 19, 25
        "Function_26_3EC5",        # 1A, 26
        "Function_27_3F25",        # 1B, 27
        "Function_28_3F85",        # 1C, 28
        "Function_29_4700",        # 1D, 29
        "Function_30_471D",        # 1E, 30
        "Function_31_4750",        # 1F, 31
        "Function_32_4783",        # 20, 32
        "Function_33_47B6",        # 21, 33
        "Function_34_47E9",        # 22, 34
        "Function_35_4832",        # 23, 35
    ))


    def Function_0_564(): pass

    label("Function_0_564")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5A4"),
        (1, "loc_5B0"),
        (2, "loc_5BC"),
        (3, "loc_5C8"),
        (4, "loc_5D4"),
        (5, "loc_5E0"),
        (6, "loc_5EC"),
        (SWITCH_DEFAULT, "loc_5F8"),
    )


    label("loc_5A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_5F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_604")

    label("loc_61B")

    Return()

    # Function_0_564 end

    def Function_1_61C(): pass

    label("Function_1_61C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_637")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_61C")

    label("loc_637")

    Return()

    # Function_1_61C end

    def Function_2_638(): pass

    label("Function_2_638")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_654")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_2_638")

    label("loc_654")

    Return()

    # Function_2_638 end

    def Function_3_655(): pass

    label("Function_3_655")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_671")
    OP_A1(0xFE, 0x5DC, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_3_655")

    label("loc_671")

    Return()

    # Function_3_655 end

    def Function_4_672(): pass

    label("Function_4_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_688")
    Event(0, 21)
    Jump("loc_6A2")

    label("loc_688")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A2")
    Event(0, 25)

    label("loc_6A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 3)), scpexpr(EXPR_END)), "loc_6BC")
    SetChrPos(0x10, 32500, -66000, 2000, 180)

    label("loc_6BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_775")
    SetChrPos(0x8, 980, 0, 204950, 225)
    SetChrPos(0x9, 2390, 0, 196530, 225)
    SetChrPos(0xA, 740, 0, 195430, 45)
    SetChrPos(0xB, -5420, 0, 196800, 0)
    SetChrPos(0xC, -3950, 0, 202880, 180)
    SetChrPos(0xD, 3840, 0, 201430, 270)
    SetChrPos(0xE, 7860, 0, 177060, 225)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_75F")
    SetChrPos(0xF, 8560, 0, 175050, 270)
    Jump("loc_770")

    label("loc_75F")

    SetChrPos(0xF, 8560, 0, 175050, 135)

    label("loc_770")

    SetChrFlags(0xA, 0x10)

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_784")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_784")

    Return()

    # Function_4_672 end

    def Function_5_785(): pass

    label("Function_5_785")

    ClearMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0xB, 0x10)
    ClearMapObjFlags(0xC, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0xE, 0x10)
    ClearMapObjFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_END)), "loc_7C6")
    OP_65(0x0, 0x1)
    OP_70(0x10, 0x1E)
    OP_70(0xA, 0x32)
    OP_70(0xB, 0x32)
    OP_70(0xC, 0x32)

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_END)), "loc_7E3")
    OP_65(0x1, 0x1)
    OP_70(0x11, 0x1E)
    OP_70(0xD, 0x32)
    OP_70(0xE, 0x32)
    OP_70(0xF, 0x32)

    label("loc_7E3")

    ClearMapObjFlags(0x13, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 2)), scpexpr(EXPR_END)), "loc_7FB")
    OP_70(0x13, 0x1E)
    Jump("loc_7FF")

    label("loc_7FB")

    OP_70(0x13, 0x0)

    label("loc_7FF")

    ClearMapObjFlags(0x14, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 5)), scpexpr(EXPR_END)), "loc_817")
    OP_70(0x14, 0x1E)
    Jump("loc_81B")

    label("loc_817")

    OP_70(0x14, 0x0)

    label("loc_81B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_828")
    OP_70(0x19, 0x1)

    label("loc_828")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_85D")
    SetMapFlags(0x2000)
    OP_E0(0x0)
    Jump("loc_862")

    label("loc_85D")

    ClearMapFlags(0x2000)

    label("loc_862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_875")
    OP_70(0x0, 0x0)
    Jump("loc_879")

    label("loc_875")

    OP_70(0x0, 0x1E)

    label("loc_879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88C")
    OP_70(0x1, 0x0)
    Jump("loc_890")

    label("loc_88C")

    OP_70(0x1, 0x1E)

    label("loc_890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A3")
    OP_70(0x12, 0x0)
    Jump("loc_8A7")

    label("loc_8A3")

    OP_70(0x12, 0x1E)

    label("loc_8A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA")
    OP_70(0x18, 0x0)
    Jump("loc_8BE")

    label("loc_8BA")

    OP_70(0x18, 0x1E)

    label("loc_8BE")

    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F9")
    OP_1B(0x0, 0x0, 0x1E)
    OP_1B(0x1, 0x0, 0x1F)
    OP_1B(0x2, 0x0, 0x20)
    OP_1B(0x3, 0x0, 0x21)

    label("loc_8F9")

    Return()

    # Function_5_785 end

    def Function_6_8FA(): pass

    label("Function_6_8FA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB6")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F3")
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x14, 0x0, 0)
    OP_98(0x14, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_953():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_953)

    def lambda_96D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_96D)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x14, 1)
    Battle("BattleInfo_490", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x14, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_9D4"),
        (2, "loc_9E3"),
        (1, "loc_9F0"),
        (SWITCH_DEFAULT, "loc_9F3"),
    )


    label("loc_9D4")

    SetScenarioFlags(0x76, 7)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_9F3")

    label("loc_9E3")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_9F0")

    OP_B7(0x0)
    Return()

    label("loc_9F3")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('星之脉冲', 1)"), scpexpr(EXPR_END)), "loc_A4A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '星之脉冲'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x109, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_AB1")

    label("loc_A4A")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '星之脉冲'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '星之脉冲'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_AB1")

    Jump("loc_AE8")

    label("loc_AB6")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_AE8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8FA end

    def Function_7_AF4(): pass

    label("Function_7_AF4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE1")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('云之使者', 1)"), scpexpr(EXPR_END)), "loc_B73")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '云之使者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_BDC")

    label("loc_B73")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '云之使者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '云之使者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BDC")

    Jump("loc_C1E")

    label("loc_BE1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_C1E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_AF4 end

    def Function_8_C2A(): pass

    label("Function_8_C2A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5E")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10D, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_D7B")

    label("loc_D5E")


    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_D7B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C2A end

    def Function_9_D8D(): pass

    label("Function_9_D8D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7A")
    Sound(14, 0, 100, 0)
    OP_71(0x18, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('太阳灵摆', 1)"), scpexpr(EXPR_END)), "loc_E0C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '太阳灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_E75")

    label("loc_E0C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '太阳灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '太阳灵摆'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x18, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E75")

    Jump("loc_EB7")

    label("loc_E7A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_EB7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D8D end

    def Function_10_EC3(): pass

    label("Function_10_EC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F37")

    #C0013
    ChrTalk(
        0xFE,
        (
            "我现在只想早点\x01",
            "回到玛因兹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "你们几个，拜托了！\x01",
            "把我们从这个地方救出去吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100F")

    label("loc_F37")


    #C0015
    ChrTalk(
        0xFE,
        (
            "喂，我说，\x01",
            "救援应该很快就会来吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "我、我也……我也好好反省过\x01",
            "那个时候的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "自从服用了那个药之后，\x01",
            "不管做什么都能称心如意……\x01",
            "态度也自然变得蛮横自大……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……真是给镇长\x01",
            "添了很多麻烦啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_100F")

    Jump("loc_1060")

    label("loc_1014")


    #C0019
    ChrTalk(
        0xFE,
        (
            "得、得救了。\x01",
            "这样一来，我就可以回去了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "赶快带我回去啊！！\x02",
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1060")

    TalkEnd(0xFE)
    Return()

    # Function_10_EC3 end

    def Function_11_1064(): pass

    label("Function_11_1064")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10F5")

    #C0021
    ChrTalk(
        0xFE,
        (
            "我虽然是个自暴自弃，\x01",
            "只能依靠药物来实现愿望\x01",
            "的废物……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "但是，我已经下定决心，\x01",
            "至少要保护好这个女孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11BF")

    label("loc_10F5")


    #C0023
    ChrTalk(
        0xFE,
        (
            "在和她谈话的时候得知……\x01",
            "她好像并不记得自己\x01",
            "主动服用过这种药。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "似乎只是服用了乌尔斯拉医院\x01",
            "开出的内服处方药而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "总、总之，待在这种地方，\x01",
            "她肯定会觉得非常不安。\x01",
            "我决定要好好保护她。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_11BF")

    Jump("loc_120B")

    label("loc_11C4")


    #C0026
    ChrTalk(
        0xFE,
        (
            "太好了……这样一来，\x01",
            "总算是恢复自由了。\x01",
            "我们也可以回到市里啦！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_120B")

    TalkEnd(0xFE)
    Return()

    # Function_11_1064 end

    def Function_12_120F(): pass

    label("Function_12_120F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1297")
    TurnDirection(0xFE, 0x0, 0)

    #C0027
    ChrTalk(
        0xFE,
        (
            "虽然并不认识，也从没见过面，\x01",
            "但他对我非常温柔。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "那个，我为什么\x01",
            "会在这种地方呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x0)
    Jump("loc_1320")

    label("loc_1297")

    OP_4B(0x9, 0xFF)

    #C0029
    ChrTalk(
        0x9,
        (
            "不、不用担心啦，\x01",
            "救援人员一定会来的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "在那之前，大家就一起共渡难关吧。\x01",
            "这里肯定是最安全的地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "嗯、嗯。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_1320")

    Jump("loc_1375")

    label("loc_1325")


    #C0032
    ChrTalk(
        0xFE,
        (
            "真的有人来救我们了，简直像做梦一样……\x01",
            "请快点把我们从这里救出来吧……！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1375")

    TalkEnd(0xFE)
    Return()

    # Function_12_120F end

    def Function_13_1379(): pass

    label("Function_13_1379")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1422")

    #C0033
    ChrTalk(
        0xFE,
        (
            "做出了这种事情……\x01",
            "大家一定不会原谅我吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥，寇奇兄，\x01",
            "还有前辈们……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……呜呜，可是我果然\x01",
            "还是很想见到大家啊！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_1422")


    #C0036
    ChrTalk(
        0xFE,
        "瓦鲁多大哥，对不起！！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "我、我想变得更强……\x01",
            "不过好像做得太过火了……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "哇～！！\x01",
            "真是对不起啊……！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1497")

    Jump("loc_14E2")

    label("loc_149C")


    #C0039
    ChrTalk(
        0xFE,
        (
            "太、太好了，终于得救了……\x01",
            "这样的话，就可以回到市里了啊……！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 19)

    label("loc_14E2")

    TalkEnd(0xFE)
    Return()

    # Function_13_1379 end

    def Function_14_14E6(): pass

    label("Function_14_14E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1545")

    #C0040
    ChrTalk(
        0xFE,
        (
            "剧团长……伊莉娅小姐……\x01",
            "我……我该怎么弥补这一切才好……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D4")

    label("loc_1545")


    #C0041
    ChrTalk(
        0xFE,
        "啊啊啊，为什么会发生这种事……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "一想到已经得救了，\x01",
            "却一下就变得消沉起来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "我、我为什么要鬼迷心窍，\x01",
            "向那种东西伸手呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_15D4")

    Jump("loc_160D")

    label("loc_15D9")


    #C0044
    ChrTalk(
        0xFE,
        (
            "这、这一定是女神的引导……\x01",
            "万岁～得救啦！！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_160D")

    TalkEnd(0xFE)
    Return()

    # Function_14_14E6 end

    def Function_15_1611(): pass

    label("Function_15_1611")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1740")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1680")

    #C0045
    ChrTalk(
        0xFE,
        "我为什么会在这种地方……！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "我的家人……库雷优和\x01",
            "萨妮塔都没事吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173B")

    label("loc_1680")


    #C0047
    ChrTalk(
        0xFE,
        (
            "我们大家的记忆都很模糊，想不起来事情的过程了……\x01",
            "等到恢复意识之后，\x01",
            "就已经在这个鬼地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "这里究竟是什么地方啊……？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "还有，我的家人们……\x01",
            "库雷优和萨妮塔\x01",
            "都没事吧……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_173B")

    Jump("loc_179E")

    label("loc_1740")


    #C0050
    ChrTalk(
        0xFE,
        "你们是来救我们的吗……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "十分感谢，这下就可以回到市里了啊。\x01",
            "真是非常感谢你们……！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_179E")

    TalkEnd(0xFE)
    Return()

    # Function_15_1611 end

    def Function_16_17A2(): pass

    label("Function_16_17A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 2)), scpexpr(EXPR_END)), "loc_1980")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_197B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192D")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_188C")

    #C0052
    ChrTalk(
        0xFE,
        (
            "总之，现在的最大目标\x01",
            "就是要活着离开这里啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "为了达成这个目标，\x01",
            "我一定会对你们\x01",
            "进行全面协助的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_191E")

    label("loc_188C")


    #C0054
    ChrTalk(
        0xFE,
        "我、我的心理承受能力太差了……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "投资失败，损失严重，\x01",
            "所以就想要一口气\x01",
            "挽回全部损失。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……如今不管再说什么\x01",
            "都已经没有意义了啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_191E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1976")

    label("loc_192D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1950")
    OP_60(0x0)
    OP_AF(0xBE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1976")

    label("loc_1950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1976")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1976")

    Jump("loc_17C5")

    label("loc_197B")

    Jump("loc_1A4E")

    label("loc_1980")


    #C0057
    ChrTalk(
        0xFE,
        (
            "总之，非常感谢你们\x01",
            "把我从牢房中救出来，\x01",
            "我的心情多少也能平静一点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "对了对了……我这里\x01",
            "好像还有一点储备呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "有需要的时候，\x01",
            "就请和我说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "这也可以算是能对你们\x01",
            "做出的一种协助吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 2)

    label("loc_1A4E")

    Jump("loc_1AB4")

    label("loc_1A53")


    #C0061
    ChrTalk(
        0xFE,
        (
            "真没想到会被解救啊……\x01",
            "这一定是女神的引导！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "你们几个，请赶快\x01",
            "把我们带回到地面上吧！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1AB4")

    TalkEnd(0xFE)
    Return()

    # Function_16_17A2 end

    def Function_17_1AB8(): pass

    label("Function_17_1AB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_1CF2")
    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1ADB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B31")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1B31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B57")
    OP_C7(0x1, 0x80)
    OP_AF(0xBF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CE5")

    label("loc_1B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B6B")
    Jump("loc_1CE5")

    label("loc_1B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1C08")

    #C0063
    ChrTalk(
        0xFE,
        (
            "万幸，做生意的道具好像都没有损坏。\x01",
            "如果需要调整导力器，\x01",
            "请不用客气，尽管和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "我一定会全力提供协助的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE5")

    label("loc_1C08")


    #C0065
    ChrTalk(
        0xFE,
        (
            "我在从共和国回来的路上\x01",
            "遭到了一群黑衣男子的袭击，\x01",
            "然后就被带到了这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "日落之后在郊外\x01",
            "开车兜风，果然是件\x01",
            "很危险的事吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "我会从技术上全力协助你们的，\x01",
            "所以哪怕只是早一刻也好，\x01",
            "希望你们能尽快解救大家啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_1CE5")

    Jump("loc_1ADB")

    label("loc_1CEA")

    TalkEnd(0xFE)
    Jump("loc_1DE6")

    label("loc_1CF2")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x87, 0x0)
    OP_70(0x19, 0x1)
    Sound(72, 0, 100, 0)
    Sleep(300)

    #C0068
    ChrTalk(
        0xFE,
        (
            "啊啊，太好了，\x01",
            "好像还可以运转呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0069
    ChrTalk(
        0xFE,
        (
            "其实我是一名技师，\x01",
            "导力器的调整正是我的专长。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "万幸，做生意的道具\x01",
            "好像都没有损坏……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "那个，如果需要进行调整，\x01",
            "就请随时和我说吧，\x01",
            "我会尽力帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 3)
    TalkEnd(0xFE)
    OP_93(0xFE, 0x10E, 0x0)

    label("loc_1DE6")

    Jump("loc_1E5E")

    label("loc_1DEB")

    TalkBegin(0xFE)

    #C0072
    ChrTalk(
        0xFE,
        (
            "呼，当时还在担心\x01",
            "到底要怎么办呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "但真没想到警察会来救我们啊。\x01",
            "这样一来，就可以暂时安心了呢！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    TalkEnd(0xFE)

    label("loc_1E5E")

    Return()

    # Function_17_1AB8 end

    def Function_18_1E5F(): pass

    label("Function_18_1E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBA")

    #C0074
    ChrTalk(
        0x101,
        (
            "#0006F那个，请稍等片刻。\x01",
            "等我把另一边的牢房也打开之后，\x01",
            "再一起进行说明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_1EBA")

    Return()

    # Function_18_1E5F end

    def Function_19_1EBB(): pass

    label("Function_19_1EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F14")

    #C0075
    ChrTalk(
        0x101,
        (
            "#0006F那个，请稍等片刻。\x01",
            "等我把另一边的牢房打开之后，\x01",
            "再一起进行说明。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_1F14")

    Return()

    # Function_19_1EBB end

    def Function_20_1F15(): pass

    label("Function_20_1F15")

    TalkBegin(0xFE)

    #C0076
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "阿奈斯特完全失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_20_1F15 end

    def Function_21_1F61(): pass

    label("Function_21_1F61")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 238100, 0)
    MoveCamera(55, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24750, 0)
    SetChrPos(0x101, 600, 0, 237500, 180)
    SetChrPos(0x102, -600, 0, 237500, 180)
    SetChrPos(0x103, -600, 0, 238800, 180)
    SetChrPos(0x104, 600, 0, 238800, 180)
    SetChrPos(0x107, 0, 0, 240100, 180)
    SetChrPos(0x108, 0, 0, 241400, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 4500, 0, 235300, 90)
    SetChrPos(0x9, 5800, 0, 236200, 180)
    SetChrPos(0xA, 5800, 0, 234400, 0)
    SetCameraDistance(24000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_20E7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20E7)

    def lambda_20F4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_20F4)
    Sleep(50)

    def lambda_2104():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2104)

    def lambda_2111():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2111)
    Sleep(50)

    def lambda_2121():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2121)

    def lambda_212E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_212E)
    OP_6F(0x10)

    #C0078
    ChrTalk(
        0x101,
        "#5P#0011F啊……！\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        (
            "#5P#0205F莫非是……\x01",
            "那些失踪的……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMapObjFlags(0x19, 0x1000)
    Fade(500)
    OP_68(5000, 1100, 176000, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(5000, 1100, 188000, 4000)
    OP_6F(0x1)
    Fade(500)
    OP_68(5000, 900, 223900, 0)
    MoveCamera(70, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(5000, 900, 235300, 4000)
    OP_6F(0x1)
    ClearMapObjFlags(0x19, 0x1000)
    OP_4B(0x8, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0x13B, 0x1F4)

    #C0080
    ChrTalk(
        0x8,
        "#11P你、你们是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(3500, 900, 235300, 0)
    MoveCamera(56, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 1900, 0, 234700, 90)
    SetChrPos(0x102, 1900, 0, 235900, 90)
    SetChrPos(0x103, 600, 0, 234700, 90)
    SetChrPos(0x104, 600, 0, 235900, 90)
    SetChrPos(0x107, 1000, 0, 233000, 45)
    SetChrPos(0x108, 1000, 0, 232000, 45)
    SetChrPos(0x8, 4000, 0, 235300, 270)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 5800, 0, 236200, 270)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, 5800, 0, 234400, 270)
    Sleep(500)
    SetCameraDistance(22500, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0081
    ChrTalk(
        0x101,
        (
            "#6P#0002F冈兹先生……\x01",
            "幸好您平安无事。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#11P是警察小兄弟啊……！\x01",
            "你、你们是来救我的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "#11P真、真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        "#11P我们可以出去了吗！？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#6P#0008F那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0086
    ChrTalk(
        0x102,
        (
            "#0101F#5P……至少先帮他们\x01",
            "把牢门打开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x108, 0xB4, 0x1F4)

    #C0087
    ChrTalk(
        0x108,
        (
            "#5P#0901F看起来，那个好像就是\x01",
            "牢门的开关装置哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2700, 1700, 206000, 3000)
    MoveCamera(50, 25, 0, 3000)
    SetCameraDistance(20000, 3000)

    def lambda_249A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_249A)
    Sleep(50)

    def lambda_24AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24AA)
    Sleep(50)

    def lambda_24BA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_24BA)
    Sleep(50)

    def lambda_24CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24CA)
    OP_6F(0x79)
    Sleep(300)

    #C0088
    ChrTalk(
        0x107,
        (
            "#0801F对面也有一样的装置，\x01",
            "我们快点去打开吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        "#0001F嗯！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(0, 2250, 235300, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 0, 0, 235300, 90)
    SetChrPos(0x1, 0, 0, 235300, 90)
    SetChrPos(0x2, 0, 0, 235300, 90)
    SetChrPos(0x3, 0, 0, 235300, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 4500, 0, 235300, 270)
    SetChrPos(0x9, 5800, 0, 236200, 270)
    SetChrPos(0xA, 5800, 0, 234400, 270)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0xE5, 6)
    OP_29(0x4F, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_21_1F61 end

    def Function_22_25F6(): pass

    label("Function_22_25F6")

    EventBegin(0x1)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个看起来很牢固的拉杆。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "拉下拉杆\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2669"),
        (1, "loc_2727"),
        (SWITCH_DEFAULT, "loc_272C"),
    )


    label("loc_2669")

    Sound(143, 0, 100, 0)
    OP_71(0x10, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x10)
    Fade(250)
    OP_68(2500, 2300, 208500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    OP_68(2500, 2300, 218500, 3000)
    OP_6F(0x1)
    Sound(155, 2, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0xA, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xB, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xC, 0x0, 0x32, 0x0, 0x0)
    OP_79(0xA)
    OP_79(0xB)
    OP_79(0xC)
    OP_24(0x9B)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xE5, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2722")
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 24)

    label("loc_2722")

    Jump("loc_272C")

    label("loc_2727")

    Jump("loc_272C")

    label("loc_272C")

    EventEnd(0x1)
    Return()

    # Function_22_25F6 end

    def Function_23_272F(): pass

    label("Function_23_272F")

    EventBegin(0x1)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个看起来很牢固的拉杆。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "拉下拉杆\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27A2"),
        (1, "loc_2860"),
        (SWITCH_DEFAULT, "loc_2865"),
    )


    label("loc_27A2")

    Sound(143, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x11)
    Fade(250)
    OP_68(2500, 2300, 191500, 0)
    MoveCamera(135, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    OP_68(2500, 2300, 181500, 3000)
    OP_6F(0x1)
    Sound(155, 2, 100, 0)
    Sound(120, 0, 100, 0)
    OP_71(0xD, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xE, 0x0, 0x32, 0x0, 0x0)
    OP_71(0xF, 0x0, 0x32, 0x0, 0x0)
    OP_79(0xD)
    OP_79(0xE)
    OP_79(0xF)
    OP_24(0x9B)
    OP_65(0x1, 0x1)
    SetScenarioFlags(0xE6, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_285B")
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 24)

    label("loc_285B")

    Jump("loc_2865")

    label("loc_2860")

    Jump("loc_2865")

    label("loc_2865")

    EventEnd(0x1)
    Return()

    # Function_23_272F end

    def Function_24_2868(): pass

    label("Function_24_2868")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-500, 900, 200000, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -2000, 0, 200600, 90)
    SetChrPos(0x102, -2000, 0, 199400, 90)
    SetChrPos(0x103, -3200, 0, 201400, 90)
    SetChrPos(0x104, -3200, 0, 198600, 90)
    SetChrPos(0x107, -4000, 0, 200600, 90)
    SetChrPos(0x108, -4000, 0, 199400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x8, 500, 0, 200000, 270)
    SetChrPos(0xB, 1100, 0, 198900, 270)
    SetChrPos(0xC, 1300, 0, 202500, 225)
    SetChrPos(0xD, 2300, 0, 201200, 270)
    SetChrPos(0xE, 1500, 0, 197500, 315)
    SetChrPos(0x9, -1500, 0, 203100, 225)
    SetChrPos(0xA, -200, 0, 203700, 225)
    SetChrPos(0xF, -1000, 0, 196900, 315)
    Sleep(500)
    SetCameraDistance(24500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0092
    ChrTalk(
        0x8,
        "还、还不能马上出去！？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#6P#0006F……对不起。\x01",
            "我们也是瞒过敌人的耳目，\x01",
            "暗中潜入这里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#12P#0303F魔兽，还有那些被操纵的\x01",
            "黑手党成员都在这附近徘徊……\x02\x03",

            "#0301F这个遗迹内自不必说，\x01",
            "连市内的安全也没有得到保障啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        (
            "#6P#0201F所以，各位还是暂时留在原地，\x01",
            "耐心等待救援比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        "#11P怎、怎么会……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        (
            "#5P啊啊……\x01",
            "……为什么会发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#12P#0104F我想，等混乱平息之后，\x01",
            "警队应该也会立刻赶到这里的。\x02\x03",

            "#0100F在那之前，就请大家暂且忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x108,
        (
            "#0901F#12P游击士协会也会全面提供协助，\x01",
            "努力将事件解决。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x107,
        (
            "#0800F#6P我们绝对会把大家救出去的。\x01",
            "所以，请放心吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xD,
        "#5P明、明白了……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        (
            "#11P我们也会在力所能及\x01",
            "的范围内尽量协助你们……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1500, 2250, 200000, 0)
    MoveCamera(90, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, -1500, 0, 200000, 90)
    SetChrPos(0x1, -1500, 0, 200000, 90)
    SetChrPos(0x2, -1500, 0, 200000, 90)
    SetChrPos(0x3, -1500, 0, 200000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 980, 0, 204950, 225)
    SetChrPos(0x9, 2390, 0, 196530, 225)
    SetChrPos(0xA, 740, 0, 195430, 45)
    SetChrPos(0xB, -5420, 0, 196800, 0)
    SetChrPos(0xC, -3950, 0, 202880, 180)
    SetChrPos(0xD, 3840, 0, 201430, 270)
    SetChrPos(0xE, 7860, 0, 177060, 225)
    SetChrPos(0xF, 8560, 0, 175050, 135)
    SetChrFlags(0xA, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0xE6, 1)
    OP_29(0x4F, 0x1, 0x7)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_1B(0x1, 0xFF, 0xFFFF)
    OP_1B(0x2, 0xFF, 0xFFFF)
    OP_1B(0x3, 0xFF, 0xFFFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_24_2868 end

    def Function_25_2DD2(): pass

    label("Function_25_2DD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00250.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00350.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00650.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00750.itc", 0x29)
    LoadChrToIndex("chr/ch02350.itc", 0x2A)
    LoadChrToIndex("monster/ch67450.itc", 0x2B)
    LoadChrToIndex("monster/ch70050.itc", 0x2C)
    LoadChrToIndex("monster/ch70051.itc", 0x2D)
    LoadChrToIndex("chr/ch02357.itc", 0x2E)
    LoadChrToIndex("monster/ch67452.itc", 0x2F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06600.itp")
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_02.eff")
    SoundLoad(861)
    OP_68(28500, -65000, -26000, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 27900, -66000, -26500, 0)
    SetChrPos(0x102, 29100, -66000, -26500, 0)
    SetChrPos(0x103, 27900, -66000, -27800, 0)
    SetChrPos(0x104, 29100, -66000, -27800, 0)
    SetChrPos(0x107, 31000, -66000, -27200, 0)
    SetChrPos(0x108, 31700, -66000, -27900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x10, 0x2A)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 28500, -66000, 3800, 180)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 28500, -66000, 3800, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x12, 0x2D)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 42000, -61000, 14800, 120)
    OP_52(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x2D)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 15500, -61000, 14800, 240)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(15500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    #Sound(1905, 255, 100, 0)    #voice#Earnest
    Sleep(1000)

    #N0103
    NpcTalk(
        0x10,
        "青年的声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "呵呵……\x01",
            "终于来了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0104
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#12P#0010F这个声音是……！\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#0107F阿奈斯特先生……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(28500, -65000, -10000, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 28300, -66000, -18000, 0)
    SetChrPos(0x102, 29400, -66000, -18500, 0)
    SetChrPos(0x103, 27500, -66000, -19500, 0)
    SetChrPos(0x104, 28600, -66000, -20000, 0)
    SetChrPos(0x107, 29600, -66000, -21200, 0)
    SetChrPos(0x108, 29000, -66000, -22400, 0)
    OP_68(28500, -65000, 1000, 4000)
    MoveCamera(43, 15, 0, 4000)
    SetCameraDistance(19000, 4000)

    def lambda_3237():
        OP_96(0xFE, 0x6E8C, 0xFFFEFE30, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3237)
    Sleep(50)

    def lambda_3254():
        OP_96(0xFE, 0x72D8, 0xFFFEFE30, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3254)
    Sleep(50)

    def lambda_3271():
        OP_96(0xFE, 0x6B6C, 0xFFFEFE30, 0xFFFFF63C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3271)
    Sleep(50)

    def lambda_328E():
        OP_96(0xFE, 0x6FB8, 0xFFFEFE30, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_328E)
    Sleep(50)

    def lambda_32AB():
        OP_96(0xFE, 0x73A0, 0xFFFEFE30, 0xFFFFEE6C, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_32AB)
    Sleep(50)

    def lambda_32C8():
        OP_96(0xFE, 0x7148, 0xFFFEFE30, 0xFFFFEA84, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_32C8)
    WaitChrThread(0x107, 1)

    def lambda_32E6():
        OP_95(0xFE, 31600, -66000, -1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_32E6)
    WaitChrThread(0x108, 1)

    def lambda_3304():
        OP_95(0xFE, 30900, -66000, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3304)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)

    def lambda_3332():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3332)
    WaitChrThread(0x108, 1)

    def lambda_3343():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_3343)
    WaitChrThread(0x108, 2)
    OP_6F(0x79)

    #C0106
    ChrTalk(
        0x107,
        (
            "#0807F啊……！\x01",
            "这个人不就是……！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x108,
        (
            "#0901F被你们逮捕的那个\x01",
            "暗杀市长未遂的犯人吗……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1902, 255, 100, 0)    #voice#Earnest
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0108
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "哼哼，两位游击士竟然也在一起啊。\x02\x03",

            "又是『银』，又是游击士，\x01",
            "你们的人脉倒是挺广的嘛。\x02",
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

    #C0109
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#12P#0003F──无聊的玩笑话\x01",
            "就到此为止吧。\x02\x03",

            "#0001F和黑手党还有警备队不同，\x01",
            "你并不是被人\x01",
            "所操纵的……\x02\x03",

            "如果是以自己的意志协助凶手，\x01",
            "就更是罪加一等了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F哼哼，那些所谓的『罪行』，\x01",
            "不过就是人类擅自制定的东西吧？\x02\x03",

            "从今天开始，克洛斯贝尔\x01",
            "就会成为新的『圣地』……\x02\x03",

            "#6600F试问，还有什么必要在意\x01",
            "那些荒谬无聊的陈腐规则……？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0101F阿奈斯特先生……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#12P#0211F看来是没办法沟通呢……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#4P#0306F……无药可救了。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#12P#0008F……你究竟是如何\x01",
            "与约亚西姆勾结到一起的……\x02\x03",

            "#0003F具体经由，等到事件彻底结束之后\x01",
            "再好好询问你。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetCameraDistance(18500, 500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0007F但现在──\x01",
            "请你先退到一边，不要挡路……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_0D()
    Sleep(500)
    #Sound(1899, 255, 100, 0)    #voice#Earnest
    Sleep(500)

    #C0116
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6600F哈哈，好吧！\x02\x03",

            "#6613F由伟大的同志授予我的，\x01",
            "可以到达『真之睿智（真知）』的力量……！\x02\x03",

            "#6610F就让你们亲眼见识一下吧……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(28500, -65000, 2800, 2000)
    MoveCamera(0, 19, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(16000, 4000)
    Sound(1904, 255, 100, 0)    #voice#Earnest
    Sleep(500)
    OP_6F(0x41)
    PlayEffect(0x0, 0x0, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)
    StopBGM(0x1388)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0x2E)
    SetChrSubChip(0x10, 0x2)

    def lambda_387B():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_387B)
    Sound(540, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x10, 0x3)
    Sleep(800)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0x107,
        "#0801F#12P#N这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0118
    ChrTalk(
        0x108,
        "#0907F#12P#N难道……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    Sound(1906, 255, 100, 0)    #voice#Earnest
    OP_6F(0x10)
    SetChrChipByIndex(0x11, 0x2F)
    SetChrSubChip(0x11, 0x3)
    SetChrFlags(0x11, 0x800)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)

    def lambda_39CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_39CC)

    def lambda_39DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_39DD)
    Sound(202, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0x11, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(315, 0, 100, 0)
    OP_24(0x35D)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(0, 15, 0, 1000)
    SetCameraDistance(18000, 1000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sound(965, 0, 100, 0)
    Sound(948, 0, 100, 0)

    def lambda_3A7D():
        OP_A6(0xFE, 0x0, 0x0, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3A7D)

    #C0119
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#5S#24A#N#5P噢噢噢噢噢噢噢噢噢！\x02",
        )
    )
    #Auto

    SetChrSubChip(0x11, 0x4)
    Sleep(150)
    SetChrSubChip(0x11, 0x5)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x11, 1)
    OP_6F(0x79)
    CancelBlur(0)
    EndChrThread(0x10, 0x1)
    ClearChrFlags(0x11, 0x800)

    #C0120
    ChrTalk(
        0x103,
        "#0207F#6P#N魔人化……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0121
    ChrTalk(
        0x104,
        (
            "#0310F#12P#N而且，这家伙要比\x01",
            "那些黑手党更加……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(300)
    Fade(500)
    OP_68(28500, -60000, 10000, 0)
    MoveCamera(33, 35, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    OP_68(28500, -64500, 1000, 4500)
    MoveCamera(43, 15, 0, 4500)
    SetCameraDistance(18500, 4500)
    SetChrChipByIndex(0x11, 0x2B)
    SetChrSubChip(0x11, 0x0)
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    BeginChrThread(0x12, 0, 0, 3)
    BeginChrThread(0x12, 3, 0, 26)
    BeginChrThread(0x15, 1, 0, 29)
    Sleep(700)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    BeginChrThread(0x13, 0, 0, 3)
    BeginChrThread(0x13, 3, 0, 27)
    WaitChrThread(0x12, 3)
    SetChrChipByIndex(0x12, 0x2C)
    SetChrSubChip(0x12, 0x0)
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 2)
    WaitChrThread(0x13, 3)
    SetChrChipByIndex(0x13, 0x2C)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x13, 0, 0, 2)
    OP_6F(0x79)
    Sleep(500)
    SetMessageWindowPos(40, 5, -1, -1)
    Sound(965, 0, 100, 0)

    #A0122
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P……哼哼哼……感觉真不错……\x02",
        )
    )

    CloseMessageWindow()

    #A0123
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P借助恶魔的力量，\x01",
            "进化为超越人类的存在……\x02",
        )
    )

    CloseMessageWindow()

    #A0124
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P这正是真正的睿智之道！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0125
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0106F阿奈斯特先生……！\x01",
            "你为什么会堕落至此……！\x02\x03",

            "#0110F你究竟要堕落到什么地步\x01",
            "才会满足呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x107,
        "#0806F……真是悲哀啊……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#0003F无论你变成什么样子都没有区别……\x02\x03",

            "#0013F──阿奈斯特·莱兹。\x02\x03",

            "我们会以妨碍执行公务罪，\x01",
            "将你当场逮捕！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x15, 0x1)
    Sleep(300)
    Sound(965, 0, 100, 0)
    Sound(948, 0, 100, 0)
    #Sound(1907, 255, 100, 0)    #voice#Earnest
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetMessageWindowPos(40, 5, -1, -1)

    #A0128
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3P#4S#10A呀啊啊啊啊啊啊啊！\x02",
        )
    )
    #Auto

    Sleep(700)
    SetMessageWindowPos(14, 280, 60, 3)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(15500, 300)
    SetChrChipByIndex(0x11, 0x2F)
    SetChrSubChip(0x11, 0x6)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x11, 0x1E, 0x12C)
    Sound(814, 0, 100, 0)

    def lambda_3E6B():
        OP_9D(0xFE, 0x6F54, 0xFFFEFE30, 0xFFFFFA24, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3E6B)
    Sleep(100)
    SetChrSubChip(0x11, 0x7)
    Sleep(200)
    OP_24(0x35D)
    Battle("BattleInfo_44C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0x11, 0x0, 0x0)
    EndChrThread(0x11, 0xFF)
    Call(0, 28)
    Return()

    # Function_25_2DD2 end

    def Function_26_3EC5(): pass

    label("Function_26_3EC5")


    def lambda_3ECA():
        OP_9E(0xFE, 0x8E94, 0x14B4, 0xFFFE2B40, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3ECA)

    label("loc_3EE0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F20")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3F18")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F20")

    label("loc_3F18")

    Sleep(15)
    Jump("loc_3EE0")

    label("loc_3F20")

    WaitChrThread(0x12, 1)
    Return()

    # Function_26_3EC5 end

    def Function_27_3F25(): pass

    label("Function_27_3F25")


    def lambda_3F2A():
        OP_9E(0xFE, 0x5014, 0x14B4, 0x1D4C0, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3F2A)

    label("loc_3F40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F80")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3F78")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F80")

    label("loc_3F78")

    Sleep(15)
    Jump("loc_3F40")

    label("loc_3F80")

    WaitChrThread(0x13, 1)
    Return()

    # Function_27_3F25 end

    def Function_28_3F85(): pass

    label("Function_28_3F85")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("chr/ch02353.itc", 0x24)
    LoadChrToIndex("monster/ch67453.itc", 0x25)
    LoadChrToIndex("chr/ch00156.itc", 0x26)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    OP_68(28500, -65000, 1000, 0)
    MoveCamera(43, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 28300, -66000, -1000, 0)
    SetChrPos(0x102, 29400, -66000, -1500, 0)
    SetChrPos(0x103, 27500, -66000, -2500, 0)
    SetChrPos(0x104, 28600, -66000, -3000, 0)
    SetChrPos(0x107, 31600, -66000, -1200, 315)
    SetChrPos(0x108, 30900, -66000, -2400, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x10, 0x24)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 28500, -66000, 2000, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x1)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 28500, -66000, 2000, 180)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    PlayEffect(0x0, 0x0, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_41BD():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_41BD)

    def lambda_41D6():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_41D6)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)
    SetCameraDistance(19000, 4000)
    FadeToBright(2000, 0)
    Sound(903, 0, 100, 0)
    Sleep(1000)
    Sleep(500)
    Sound(965, 0, 100, 0)
    #Sound(1908, 255, 100, 0)    #voice#Joachim
    SetMessageWindowPos(100, 0, -1, -1)

    #A0129
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3P#4S#20A嘎啊啊啊啊啊……！\x02",
        )
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x10, 0x800)

    def lambda_4267():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_4267)

    def lambda_4278():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4278)
    PlayEffect(0x1, 0xFF, 0x10, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    Sleep(500)
    SetChrSubChip(0x10, 0x2)
    SetChrSubChip(0x11, 0x2)
    Sleep(200)
    SetChrSubChip(0x10, 0x3)
    SetChrSubChip(0x11, 0x3)
    Sleep(300)
    Fade(500)
    EndChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    Sound(514, 0, 100, 0)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x800)
    OP_0D()
    OP_6F(0x10)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x101,
        "#12P#0006F呼、呼……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x107,
        (
            "#0806F实、实在是\x01",
            "强得夸张啊……\x02\x03",

            "#0801F同样都是秘书，但和某人\x01",
            "真是有很大不同呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x108,
        (
            "#0906F嗯，毕竟这个人原本\x01",
            "就拥有相当的战斗能力……\x02\x03",

            "#0908F不过，『真知』……\x01",
            "究竟超越常识到了何等地步呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        "#0108F………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_68(28700, -65000, 1290, 1500)

    def lambda_4478():
        OP_96(0xFE, 0x733C, 0xFFFEFE30, 0x76C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4478)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x10E, 0x1F4)
    Fade(250)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0134
    ChrTalk(
        0x101,
        "#12P#0001F……还活着吗？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#0106F#11P嗯……还有呼吸。\x02\x03",

            "#0101F看起来，似乎是消耗过度了，\x01",
            "暂时应该无法动弹了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#12P#0003F是吗……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x103,
        (
            "#12P#0206F不过，现在也只能\x01",
            "先把他放下不管了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#12P#0301F嗯……\x01",
            "我们赶快继续前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#12P#0006F是啊……\x02\x03",

            "#0000F艾莉，走吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0140
    ChrTalk(
        0x102,
        (
            "#0103F#11P嗯……\x02\x03",

            "#0108F（……再见了，\x01",
            "  阿奈斯特先生。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 32500, -66000, 2000, 180)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_37()
    OP_68(28500, -65000, -500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 28500, -66000, -500, 0)
    SetChrPos(0x1, 28500, -66000, -500, 0)
    SetChrPos(0x2, 28500, -66000, -500, 0)
    SetChrPos(0x3, 28500, -66000, -500, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0xE6, 3)
    OP_29(0x4F, 0x1, 0x9)
    OP_24(0x35D)
    Sleep(500)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_28_3F85 end

    def Function_29_4700(): pass

    label("Function_29_4700")

    Sleep(400)

    label("loc_4703")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_471C")
    Sound(966, 0, 100, 0)
    Sleep(650)
    Jump("loc_4703")

    label("loc_471C")

    Return()

    # Function_29_4700 end

    def Function_30_471D(): pass

    label("Function_30_471D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4736")
    Call(0, 34)
    Jump("loc_4739")

    label("loc_4736")

    Call(0, 35)

    label("loc_4739")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 239660, 180)
    EventEnd(0x4)
    Return()

    # Function_30_471D end

    def Function_31_4750(): pass

    label("Function_31_4750")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4769")
    Call(0, 34)
    Jump("loc_476C")

    label("loc_4769")

    Call(0, 35)

    label("loc_476C")

    Sleep(50)
    SetChrPos(0x0, -11150, 0, 200000, 90)
    EventEnd(0x4)
    Return()

    # Function_31_4750 end

    def Function_32_4783(): pass

    label("Function_32_4783")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_479C")
    Call(0, 34)
    Jump("loc_479F")

    label("loc_479C")

    Call(0, 35)

    label("loc_479F")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)
    Return()

    # Function_32_4783 end

    def Function_33_47B6(): pass

    label("Function_33_47B6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47CF")
    Call(0, 34)
    Jump("loc_47D2")

    label("loc_47CF")

    Call(0, 35)

    label("loc_47D2")

    Sleep(50)
    SetChrPos(0x0, 9730, 0, 199950, 270)
    EventEnd(0x4)
    Return()

    # Function_33_47B6 end

    def Function_34_47E9(): pass

    label("Function_34_47E9")


    #C0141
    ChrTalk(
        0x101,
        (
            "#0001F附近好像就有\x01",
            "牢门的开关装置。\x02\x03",

            "总之，至少先去把\x01",
            "牢门打开吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_34_47E9 end

    def Function_35_4832(): pass

    label("Function_35_4832")


    #C0142
    ChrTalk(
        0x101,
        (
            "#0005F啊……\x01",
            "还没将另一边的牢房打开呢。\x02\x03",

            "#0001F去把对面的门也打开吧。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_35_4832 end

    SaveToFile()

Try(main)
