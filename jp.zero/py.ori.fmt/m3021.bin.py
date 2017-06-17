from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "鉱員ガンツ",             # 1
        "市民",                   # 2
        "市民",                   # 3
        "ディーノ",               # 4
        "ニコル",                 # 5
        "ボンド",                 # 6
        "貿易商リゼロ",           # 7
        "技師",                   # 8
        "アーネスト",             # 9
        "魔人アーネスト",         # 10
        "翼竜",                   # 11
        "翼竜",                   # 12
        "シームーン	",            # 13
        "SE制御",                 # 14
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
        "Function_7_B0D",          # 07, 7
        "Function_8_C5A",          # 08, 8
        "Function_9_DCB",          # 09, 9
        "Function_10_F18",         # 0A, 10
        "Function_11_10E5",        # 0B, 11
        "Function_12_12A2",        # 0C, 12
        "Function_13_1416",        # 0D, 13
        "Function_14_15AB",        # 0E, 14
        "Function_15_16E2",        # 0F, 15
        "Function_16_1881",        # 10, 16
        "Function_17_1BDF",        # 11, 17
        "Function_18_2010",        # 12, 18
        "Function_19_2072",        # 13, 19
        "Function_20_20CE",        # 14, 20
        "Function_21_2122",        # 15, 21
        "Function_22_27EF",        # 16, 22
        "Function_23_2932",        # 17, 23
        "Function_24_2A75",        # 18, 24
        "Function_25_2FF3",        # 19, 25
        "Function_26_41BA",        # 1A, 26
        "Function_27_421A",        # 1B, 27
        "Function_28_427A",        # 1C, 28
        "Function_29_4A29",        # 1D, 29
        "Function_30_4A46",        # 1E, 30
        "Function_31_4A79",        # 1F, 31
        "Function_32_4AAC",        # 20, 32
        "Function_33_4ADF",        # 21, 33
        "Function_34_4B12",        # 22, 34
        "Function_35_4B6B",        # 23, 35
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x109, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5")
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
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_9D6"),
        (2, "loc_9E5"),
        (1, "loc_9F2"),
        (SWITCH_DEFAULT, "loc_9F5"),
    )


    label("loc_9D6")

    SetScenarioFlags(0x76, 7)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_9F5")

    label("loc_9E5")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_9F2")

    OP_B7(0x0)
    Return()

    label("loc_9F5")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41B, 1)"), scpexpr(EXPR_END)), "loc_A52")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x109, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_AC2")

    label("loc_A52")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x41B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x41B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_AC2")

    Jump("loc_B01")

    label("loc_AC7")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_B01")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8FA end

    def Function_7_B0D(): pass

    label("Function_7_B0D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C09")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x47, 1)"), scpexpr(EXPR_END)), "loc_B92")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x47),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_C04")

    label("loc_B92")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x47),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x47),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C04")

    Jump("loc_C4E")

    label("loc_C09")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_C4E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B0D end

    def Function_8_C5A(): pass

    label("Function_8_C5A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D94")
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
            "#56I地のセピス×２００\x01\x07\x02",

            "#57I水のセピス×２００\x01\x07\x02",

            "#58I火のセピス×２００\x01\x07\x02",

            "#59I風のセピス×２００\x01\x07\x02",

            "#60I時のセピス×２００\x01\x07\x02",

            "#61I空のセピス×２００\x01\x07\x02",

            "#62I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x10D, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_DB9")

    label("loc_D94")


    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_DB9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C5A end

    def Function_9_DCB(): pass

    label("Function_9_DCB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC7")
    Sound(14, 0, 100, 0)
    OP_71(0x18, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x49, 1)"), scpexpr(EXPR_END)), "loc_E50")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x49),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10D, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_EC2")

    label("loc_E50")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x49),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x49),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x18, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EC2")

    Jump("loc_F0C")

    label("loc_EC7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_F0C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_DCB end

    def Function_10_F18(): pass

    label("Function_10_F18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FAA")

    #C0013
    ChrTalk(
        0xFE,
        (
            "今はとにかく\x01",
            "早くマインツに帰りたいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "あんたら、もう一度だけお願いだ！\x01",
            "俺たちをここから助け出してくれ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_FAA")


    #C0015
    ChrTalk(
        0xFE,
        (
            "なああんたら、\x01",
            "もうすぐ助けがくるんだろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "お、俺も……あん時のことは\x01",
            "凄い反省してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "あの薬を飲んだら\x01",
            "何でも思い通りになって……\x01",
            "態度もでかくなっちまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……町長には迷惑ばっか\x01",
            "掛けちまったよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1092")

    Jump("loc_10E1")

    label("loc_1097")


    #C0019
    ChrTalk(
        0xFE,
        (
            "た、助かった。\x01",
            "これで帰れるんだな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "早く連れ帰ってくれ！！\x02",
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_10E1")

    TalkEnd(0xFE)
    Return()

    # Function_10_F18 end

    def Function_11_10E5(): pass

    label("Function_11_10E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1178")

    #C0021
    ChrTalk(
        0xFE,
        (
            "オレ、やけになって\x01",
            "薬なんかに手を出しちまった\x01",
            "ダメ人間だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "女の子の１人くらい\x01",
            "守ってやらないとな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1256")

    label("loc_1178")


    #C0023
    ChrTalk(
        0xFE,
        (
            "話を聞いてみると……\x01",
            "彼女は薬に手を出した\x01",
            "覚えはないそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "ただウルスラ病院で処方された\x01",
            "内服薬を飲んでいたそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "と、ともかく\x01",
            "こんな場所じゃ心細いだろうし。\x01",
            "オレが守ってやるって決めたんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1256")

    Jump("loc_129E")

    label("loc_125B")


    #C0026
    ChrTalk(
        0xFE,
        (
            "よかった……\x01",
            "これでようやく自由だ。\x01",
            "僕らも街に帰れますね！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_129E")

    TalkEnd(0xFE)
    Return()

    # Function_11_10E5 end

    def Function_12_12A2(): pass

    label("Function_12_12A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1340")
    TurnDirection(0xFE, 0x0, 0)

    #C0027
    ChrTalk(
        0xFE,
        (
            "彼、見ず知らずのわたしに\x01",
            "優しくしてくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "あの、わたしはどうして\x01",
            "こんな所にいるんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x0)
    Jump("loc_13C7")

    label("loc_1340")

    OP_4B(0x9, 0xFF)

    #C0029
    ChrTalk(
        0x9,
        (
            "し、心配するな。\x01",
            "助けは必ず来る……！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        (
            "それまでみんなと一緒にいよう。\x01",
            "きっとここが一番安全なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "う、うん。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_13C7")

    Jump("loc_1412")

    label("loc_13CC")


    #C0032
    ChrTalk(
        0xFE,
        (
            "助けが来るなんて夢みたい……\x01",
            "早くここから助けてください……！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1412")

    TalkEnd(0xFE)
    Return()

    # Function_12_12A2 end

    def Function_13_1416(): pass

    label("Function_13_1416")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_14D1")

    #C0033
    ChrTalk(
        0xFE,
        (
            "こんな事しちまって……\x01",
            "みんな許してくれないよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんにコウキさん、\x01",
            "先輩たち……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……ううっ、でもやっぱり\x01",
            "みんなに会いたいよぅ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1566")

    label("loc_14D1")


    #C0036
    ChrTalk(
        0xFE,
        "ヴァルドさん、すんません！！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "俺、強くなりたくて……\x01",
            "でも調子乗っちまったみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "うわーん……！！\x01",
            "ホントにすんません……っ！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1566")

    Jump("loc_15A7")

    label("loc_156B")


    #C0039
    ChrTalk(
        0xFE,
        (
            "や、やった、助かった……\x01",
            "これで街に帰れるよっ……！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 19)

    label("loc_15A7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1416 end

    def Function_14_15AB(): pass

    label("Function_14_15AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1604")

    #C0040
    ChrTalk(
        0xFE,
        (
            "劇団長……イリアさん……\x01",
            "僕は……僕はどう償えば……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1699")

    label("loc_1604")


    #C0041
    ChrTalk(
        0xFE,
        "あああ、どうしてこんな事に……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "助かると思ったら\x01",
            "急に気が滅入ってきたよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "ぼ、僕はどうしてあんな物に\x01",
            "手を出してしまったんだ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_1699")

    Jump("loc_16DE")

    label("loc_169E")


    #C0044
    ChrTalk(
        0xFE,
        (
            "こ、これぞ女神のお導きだ……\x01",
            "ばんざーい、助かったぞ！！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_16DE")

    TalkEnd(0xFE)
    Return()

    # Function_14_15AB end

    def Function_15_16E2(): pass

    label("Function_15_16E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1815")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1759")

    #C0045
    ChrTalk(
        0xFE,
        "僕はどうしてこんな所に……！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "家族は……クレイユと\x01",
            "サニータは無事なのか……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1810")

    label("loc_1759")


    #C0047
    ChrTalk(
        0xFE,
        (
            "僕らはみんな途中の記憶が曖昧で……\x01",
            "気が付いたらこんな\x01",
            "不気味な場所にいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "一体ここはどこなんだ……？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "それに僕の家族は……\x01",
            "クレイユとサニータは\x01",
            "無事なのか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1810")

    Jump("loc_187D")

    label("loc_1815")


    #C0050
    ChrTalk(
        0xFE,
        "君たち、助けに来てくれたのか……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "感謝する、これで街に帰れるんだな。\x01",
            "本当に感謝するよ……！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_187D")

    TalkEnd(0xFE)
    Return()

    # Function_15_16E2 end

    def Function_16_1881(): pass

    label("Function_16_1881")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 2)), scpexpr(EXPR_END)), "loc_1A79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A74")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A26")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_197D")

    #C0052
    ChrTalk(
        0xFE,
        (
            "ともかく今は\x01",
            "ここから生きて出たいものだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "そのためにも、\x01",
            "君たちには全面的に\x01",
            "協力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A17")

    label("loc_197D")


    #C0054
    ChrTalk(
        0xFE,
        "わ、私の心が弱かったんだ……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "投資で大損をしてな、\x01",
            "それを一気に挽回したいと\x01",
            "思ってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……今さら何を言っても\x01",
            "無意味だろうがな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_1A17")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A6F")

    label("loc_1A26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A49")
    OP_60(0x0)
    OP_AF(0xBE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A6F")

    label("loc_1A49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A6F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A6F")

    Jump("loc_18A4")

    label("loc_1A74")

    Jump("loc_1B6D")

    label("loc_1A79")


    #C0057
    ChrTalk(
        0xFE,
        (
            "ともかく牢屋から\x01",
            "出してくれて感謝する。\x01",
            "少しは落ち着けた気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "そうそう……ここには\x01",
            "少しなら備蓄があるようなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "必要なときは\x01",
            "私に声をかけてくれないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "ここは一つ、君たちに全面的に\x01",
            "協力させてもらおうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 2)

    label("loc_1B6D")

    Jump("loc_1BDB")

    label("loc_1B72")


    #C0061
    ChrTalk(
        0xFE,
        (
            "まさか助けがくるとは……\x01",
            "これぞ女神のお導きだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "君たち、早く我々を\x01",
            "地上へ連れて行ってくれ！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)

    label("loc_1BDB")

    TalkEnd(0xFE)
    Return()

    # Function_16_1881 end

    def Function_17_1BDF(): pass

    label("Function_17_1BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 3)), scpexpr(EXPR_END)), "loc_1E5B")
    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E53")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "改造・合成する\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C62")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1C62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C88")
    OP_C7(0x1, 0x80)
    OP_AF(0xBF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1E4E")

    label("loc_1C88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C9C")
    Jump("loc_1E4E")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E4E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1D4F")

    #C0063
    ChrTalk(
        0xFE,
        (
            "何とか商売道具も無事だったようです。\x01",
            "オーブメントの調整が必要なら\x01",
            "遠慮なく声をかけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        "全力でお手伝いさせて頂きますから。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E4E")

    label("loc_1D4F")


    #C0065
    ChrTalk(
        0xFE,
        (
            "自分は共和国からの帰りに\x01",
            "黒服の男たちに襲われ、\x01",
            "ここに連れて来られたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "やはり日が落ちてから\x01",
            "街道をドライブしていたのが\x01",
            "まずかったんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "ともかく、一刻も早く\x01",
            "こんな所からは抜け出したい。\x01",
            "全力でお手伝いさせて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)

    label("loc_1E4E")

    Jump("loc_1C02")

    label("loc_1E53")

    TalkEnd(0xFE)
    Jump("loc_1F95")

    label("loc_1E5B")

    TalkBegin(0xFE)
    OP_93(0xFE, 0x87, 0x0)
    OP_70(0x19, 0x1)
    Sound(72, 0, 100, 0)
    Sleep(300)

    #C0068
    ChrTalk(
        0xFE,
        (
            "ああ、よかった。\x01",
            "まだ動いてくれていますね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0069
    ChrTalk(
        0xFE,
        (
            "実は自分は技師をやっていまして、\x01",
            "オーブメントの調整ならお手の物です。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "何とか商売道具も\x01",
            "無事だったみたいですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "あの、もし調整が必要になった時は\x01",
            "声をかけてくださいませんか。\x01",
            "お手伝いさせて頂きますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEF, 3)
    TalkEnd(0xFE)
    OP_93(0xFE, 0x10E, 0x0)

    label("loc_1F95")

    Jump("loc_200F")

    label("loc_1F9A")

    TalkBegin(0xFE)

    #C0072
    ChrTalk(
        0xFE,
        (
            "はあ、一時はどうなる事かと\x01",
            "思いましたよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "ですが警察の方が来てくれるとは。\x01",
            "これで一安心ですね！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    TalkEnd(0xFE)

    label("loc_200F")

    Return()

    # Function_17_1BDF end

    def Function_18_2010(): pass

    label("Function_18_2010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2071")

    #C0074
    ChrTalk(
        0x101,
        (
            "#0006Fええと、少しお待ち下さい。\x01",
            "もう一方の牢も開放してから\x01",
            "ご説明しますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_2071")

    Return()

    # Function_18_2010 end

    def Function_19_2072(): pass

    label("Function_19_2072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20CD")

    #C0075
    ChrTalk(
        0x101,
        (
            "#0006Fえっと、少し待ってくれ。\x01",
            "もう一方の牢も開放してから\x01",
            "説明するから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_20CD")

    Return()

    # Function_19_2072 end

    def Function_20_20CE(): pass

    label("Function_20_20CE")

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
            "アーネストは完全に気絶している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_20_20CE end

    def Function_21_2122(): pass

    label("Function_21_2122")

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

    def lambda_22A8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22A8)

    def lambda_22B5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22B5)
    Sleep(50)

    def lambda_22C5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_22C5)

    def lambda_22D2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_22D2)
    Sleep(50)

    def lambda_22E2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_22E2)

    def lambda_22EF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_22EF)
    OP_6F(0x10)

    #C0078
    ChrTalk(
        0x101,
        "#5P#0011Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        (
            "#5P#0205Fもしかして……\x01",
            "行方不明になった？\x02",
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
        "#11Pあ、あんたらは……！\x02",
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
            "#6P#0002Fガンツさん……\x01",
            "ご無事で何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#11P警察の兄ちゃんたち……！\x01",
            "た、助けに来てくれたのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        "#11Pほ、本当に……！？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        "#11Pあたしたち、出られるの！？\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#6P#0008Fそれは……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0086
    ChrTalk(
        0x102,
        (
            "#0101F#5P……とにかく扉だけでも\x01",
            "開いてしまいましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x108, 0xB4, 0x1F4)

    #C0087
    ChrTalk(
        0x108,
        (
            "#5P#0901Fどうやらあれが\x01",
            "扉の開閉装置みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2700, 1700, 206000, 3000)
    MoveCamera(50, 25, 0, 3000)
    SetCameraDistance(20000, 3000)

    def lambda_2689():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2689)
    Sleep(50)

    def lambda_2699():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2699)
    Sleep(50)

    def lambda_26A9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_26A9)
    Sleep(50)

    def lambda_26B9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_26B9)
    OP_6F(0x79)
    Sleep(300)

    #C0088
    ChrTalk(
        0x107,
        (
            "#0801F向こう側にもあるから\x01",
            "とっとと開いちゃいましょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        "#0001Fああ！\x02",
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

    # Function_21_2122 end

    def Function_22_27EF(): pass

    label("Function_22_27EF")

    EventBegin(0x1)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "頑丈そうなレバーがある。\x07\x00\x02",
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
            "レバーを下ろす\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_286C"),
        (1, "loc_292A"),
        (SWITCH_DEFAULT, "loc_292F"),
    )


    label("loc_286C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2925")
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 24)

    label("loc_2925")

    Jump("loc_292F")

    label("loc_292A")

    Jump("loc_292F")

    label("loc_292F")

    EventEnd(0x1)
    Return()

    # Function_22_27EF end

    def Function_23_2932(): pass

    label("Function_23_2932")

    EventBegin(0x1)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "頑丈そうなレバーがある。\x07\x00\x02",
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
            "レバーを下ろす\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29AF"),
        (1, "loc_2A6D"),
        (SWITCH_DEFAULT, "loc_2A72"),
    )


    label("loc_29AF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A68")
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 24)

    label("loc_2A68")

    Jump("loc_2A72")

    label("loc_2A6D")

    Jump("loc_2A72")

    label("loc_2A72")

    EventEnd(0x1)
    Return()

    # Function_23_2932 end

    def Function_24_2A75(): pass

    label("Function_24_2A75")

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
        "す、すぐには出られない！？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#6P#0006F……すみません。\x01",
            "自分たちも敵の目を盗んで\x01",
            "何とか潜入している状態です。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#12P#0303F魔獣や操られたマフィアが\x01",
            "あたりをウロウロしている……\x02\x03",

            "#0301Fこの遺跡もそうだが\x01",
            "街までの安全も保障できねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x103,
        (
            "#6P#0201Fしばらくここで救援を\x01",
            "待っていただく方がいいかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        "#11Pそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        (
            "#5Pああっ……\x01",
            "……どうしてこんな事に……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#12P#0104Fじきに混乱が収まれば\x01",
            "警官隊も駆けつけると思います。\x02\x03",

            "#0100Fどうかそれまでご辛抱を。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x108,
        (
            "#0901F#12P遊撃士協会も全面的に\x01",
            "事態の収拾に協力しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x107,
        (
            "#0800F#6Pみんなの事は絶対に助けるから\x01",
            "どうか安心して！\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xD,
        "#5Pわ、分かった……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        (
            "#11P私たちも出来るだけの\x01",
            "協力をさせてもらおう……！\x02",
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

    # Function_24_2A75 end

    def Function_25_2FF3(): pass

    label("Function_25_2FF3")

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
        "青年の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "フフ……\x01",
            "やっと来たようだね。\x02",
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
            "#12P#0010Fこの声は……！\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        "#0107Fアーネストさん……！\x02",
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

    def lambda_345E():
        OP_96(0xFE, 0x6E8C, 0xFFFEFE30, 0xFFFFFC18, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_345E)
    Sleep(50)

    def lambda_347B():
        OP_96(0xFE, 0x72D8, 0xFFFEFE30, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_347B)
    Sleep(50)

    def lambda_3498():
        OP_96(0xFE, 0x6B6C, 0xFFFEFE30, 0xFFFFF63C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3498)
    Sleep(50)

    def lambda_34B5():
        OP_96(0xFE, 0x6FB8, 0xFFFEFE30, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34B5)
    Sleep(50)

    def lambda_34D2():
        OP_96(0xFE, 0x73A0, 0xFFFEFE30, 0xFFFFEE6C, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_34D2)
    Sleep(50)

    def lambda_34EF():
        OP_96(0xFE, 0x7148, 0xFFFEFE30, 0xFFFFEA84, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_34EF)
    WaitChrThread(0x107, 1)

    def lambda_350D():
        OP_95(0xFE, 31600, -66000, -1200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_350D)
    WaitChrThread(0x108, 1)

    def lambda_352B():
        OP_95(0xFE, 30900, -66000, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_352B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)

    def lambda_3559():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_3559)
    WaitChrThread(0x108, 1)

    def lambda_356A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_356A)
    WaitChrThread(0x108, 2)
    OP_6F(0x79)

    #C0106
    ChrTalk(
        0x107,
        (
            "#0807Fあ……！\x01",
            "その人って確か……！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x108,
        (
            "#0901F君たちが逮捕した\x01",
            "市長暗殺未遂事件の犯人か……\x02",
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
            "クク、遊撃士諸君もご一緒とは。\x02\x03",

            "《銀#2Rイン#》といい、君たちも\x01",
            "なかなか顔が広いじゃないか。\x02",
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
            "#12P#0003F──戯言はそのくらいに\x01",
            "してもらいましょう。\x02\x03",

            "#0001Fマフィアや警備隊と違って\x01",
            "あなたは意志を封じられて\x01",
            "操られているわけではない……\x02\x03",

            "自分の意志で協力しているなら\x01",
            "さらに罪が重くなりますよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613Fクク、その“罪”というのは\x01",
            "人間が勝手に決めたものだろう？\x02\x03",

            "今日から、このクロスベルは\x01",
            "新たなる《聖地》となる……\x02\x03",

            "#6600Fどうしてそんな下らないルールを\x01",
            "気にかける必要があるんだい……？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0101Fアーネストさん……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        "#12P#0211F話が通じませんね……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#4P#0306F……駄目だな、これは。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#12P#0008F……貴方がどんな経緯で\x01",
            "ヨアヒムに取り込まれたのか……\x02\x03",

            "#0003Fいずれ、事件の後にでも\x01",
            "きちんと聞かせてもらいます。\x02",
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
            "#12P#0007Fだが今は──\x01",
            "そこを退#2Rど#いてもらう……！\x02",
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
            "#6600Fハハ、いいだろう！\x02\x03",

            "#6613F偉大なる同志から授かった\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》に至る力……！\x02\x03",

            "#6610Fその目で確かめるがいい……！\x02",
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

    def lambda_3B19():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3B19)
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
        "#0801F#12P#Nこ、これって……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0118
    ChrTalk(
        0x108,
        "#0907F#12P#Nまさか……！\x02",
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

    def lambda_3C70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3C70)

    def lambda_3C81():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3C81)
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

    def lambda_3D21():
        OP_A6(0xFE, 0x0, 0x0, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3D21)

    #C0119
    ChrTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#5S#24A#N#5Pオオオオオオオオンッ！\x02",
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
        "#0207F#6P#N魔人化#6Rデモナイズ#……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0121
    ChrTalk(
        0x104,
        (
            "#0310F#12P#Nしかもこいつは、\x01",
            "あのマフィアどもより……！\x02",
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
            "#5P……ククク……イイ心地ダ……\x02",
        )
    )

    CloseMessageWindow()

    #A0123
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P魔ノチカラヲ取リ込ミ\x01",
            "人ヲ超エタ存在ニ進化スル……\x02",
        )
    )

    CloseMessageWindow()

    #A0124
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5Pコレゾ真ナル叡智#10Rぐ の ー し す#ヘノ道！\x02",
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
            "#0106Fアーネストさん……！\x01",
            "どうしてそこまで……！\x02\x03",

            "#0110Fどこまで堕ちれば\x01",
            "気が済むんですか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x107,
        "#0806F……なんか哀れね……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#0003Fどんな姿になろうとも同じだ……\x02\x03",

            "#0013F──アーネスト・ライズ。\x02\x03",

            "公務執行妨害の現行犯により、\x01",
            "これより身柄を拘束させてもらう！\x02",
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
            "#3P#4S#10Aシャアアアアアアアッ！\x02",
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

    def lambda_4160():
        OP_9D(0xFE, 0x6F54, 0xFFFEFE30, 0xFFFFFA24, 0x384, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4160)
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

    # Function_25_2FF3 end

    def Function_26_41BA(): pass

    label("Function_26_41BA")


    def lambda_41BF():
        OP_9E(0xFE, 0x8E94, 0x14B4, 0xFFFE2B40, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_41BF)

    label("loc_41D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4215")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_420D")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4215")

    label("loc_420D")

    Sleep(15)
    Jump("loc_41D5")

    label("loc_4215")

    WaitChrThread(0x12, 1)
    Return()

    # Function_26_41BA end

    def Function_27_421A(): pass

    label("Function_27_421A")


    def lambda_421F():
        OP_9E(0xFE, 0x5014, 0x14B4, 0x1D4C0, 0x1B58, 0x1)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_421F)

    label("loc_4235")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4275")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_426D")
    OP_52(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x101D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4275")

    label("loc_426D")

    Sleep(15)
    Jump("loc_4235")

    label("loc_4275")

    WaitChrThread(0x13, 1)
    Return()

    # Function_27_421A end

    def Function_28_427A(): pass

    label("Function_28_427A")

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

    def lambda_44B2():
        OP_A6(0xFE, 0x0, 0x32, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_44B2)

    def lambda_44CB():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_44CB)
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
            "#3P#4S#20Aガアアアアアッ……！\x02",
        )
    )
    #Auto

    Sleep(2000)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x10, 0x800)

    def lambda_455E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_455E)

    def lambda_456F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_456F)
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
        "#12P#0006Fはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x107,
        (
            "#0806Fと、とんでもない\x01",
            "強さだったわね……\x02\x03",

            "#0801F同じ秘書でも誰かさんとは\x01",
            "えらい違いだわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x108,
        (
            "#0906Fまあ、こちらの彼は\x01",
            "元々武闘派みたいだし……\x02\x03",

            "#0908Fしかし《グノーシス》……\x01",
            "どこまで常識外れなんだ……？\x02",
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

    def lambda_477D():
        OP_96(0xFE, 0x733C, 0xFFFEFE30, 0x76C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_477D)
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
        "#12P#0001F……生きているか？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#0106F#11Pええ……何とか。\x02\x03",

            "#0101Fかなり消耗したみたいだから\x01",
            "しばらく動けないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#12P#0003Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x103,
        (
            "#12P#0206Fまあ、ここに\x01",
            "放っておくしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#12P#0301Fああ……\x01",
            "とっとと先に進もうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#12P#0006Fそうだな……\x02\x03",

            "#0000Fエリィ、行こう。\x02",
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
            "#0103F#11Pええ……\x02\x03",

            "#0108F（……さようなら。\x01",
            "  アーネスト先生。）\x02",
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

    # Function_28_427A end

    def Function_29_4A29(): pass

    label("Function_29_4A29")

    Sleep(400)

    label("loc_4A2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A45")
    Sound(966, 0, 100, 0)
    Sleep(650)
    Jump("loc_4A2C")

    label("loc_4A45")

    Return()

    # Function_29_4A29 end

    def Function_30_4A46(): pass

    label("Function_30_4A46")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A5F")
    Call(0, 34)
    Jump("loc_4A62")

    label("loc_4A5F")

    Call(0, 35)

    label("loc_4A62")

    Sleep(50)
    SetChrPos(0x0, 0, 0, 239660, 180)
    EventEnd(0x4)
    Return()

    # Function_30_4A46 end

    def Function_31_4A79(): pass

    label("Function_31_4A79")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A92")
    Call(0, 34)
    Jump("loc_4A95")

    label("loc_4A92")

    Call(0, 35)

    label("loc_4A95")

    Sleep(50)
    SetChrPos(0x0, -11150, 0, 200000, 90)
    EventEnd(0x4)
    Return()

    # Function_31_4A79 end

    def Function_32_4AAC(): pass

    label("Function_32_4AAC")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AC5")
    Call(0, 34)
    Jump("loc_4AC8")

    label("loc_4AC5")

    Call(0, 35)

    label("loc_4AC8")

    Sleep(50)
    SetChrPos(0x0, -16000, 0, 12940, 180)
    EventEnd(0x4)
    Return()

    # Function_32_4AAC end

    def Function_33_4ADF(): pass

    label("Function_33_4ADF")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF8")
    Call(0, 34)
    Jump("loc_4AFB")

    label("loc_4AF8")

    Call(0, 35)

    label("loc_4AFB")

    Sleep(50)
    SetChrPos(0x0, 9730, 0, 199950, 270)
    EventEnd(0x4)
    Return()

    # Function_33_4ADF end

    def Function_34_4B12(): pass

    label("Function_34_4B12")


    #C0141
    ChrTalk(
        0x101,
        (
            "#0001Fすぐそこに\x01",
            "扉の開閉装置があるみたいだ。\x02\x03",

            "とにかく扉だけでも\x01",
            "開いてしまおう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_34_4B12 end

    def Function_35_4B6B(): pass

    label("Function_35_4B6B")


    #C0142
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……\x01",
            "もう一方の牢屋がまだだ。\x02\x03",

            "#0001F向こうの扉も開いてしまおう。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_35_4B6B end

    SaveToFile()

Try(main)
