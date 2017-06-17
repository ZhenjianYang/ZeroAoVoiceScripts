from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1340.bin",                # FileName
        "c1340",                    # MapName
        "c1340",                    # Location
        0x001D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 56000, 0, 14000, 0, 0, 1, 29, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1340",                  # 0
        "迪塔总裁",               # 1
        "玛丽亚贝尔",             # 2
        "巴雷塔董事长",           # 3
        "人偶",                   # 4
        "人偶",                   # 5
    ))

    AddCharChip((
        "chr/ch05600.itc",                   # 00
        "chr/ch05500.itc",                   # 01
        "chr/ch05602.itc",                   # 02
        "chr/ch05502.itc",                   # 03
        "chr/ch27400.itc",                   # 04
        "apl/ch50093.itc",                   # 05
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(172360,  800,     120099,  0,    374,  0x0, 1,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(172360,  800,     120800,  0,    374,  0x0, 2,   5,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(53000,   0,       45800,   1500,    53000,   1000,    45800,   0x007C, 0,  17, 0x0000)
    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  4,  0x0000)
    DeclActor(55660,   0,       38920,   1200,    55660,   1000,    38920,   0x007C, 0,  22, 0x0000)
    DeclActor(172500,  0,       121000,  1200,    172500,  1500,    121000,  0x007C, 0,  23, 0x0000)
    DeclActor(172500,  0,       120000,  1200,    172500,  1500,    120250,  0x007C, 0,  23, 0x0000)

    ScpFunction((
        "Function_0_24C",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_59D",          # 02, 2
        "Function_3_5A4",          # 03, 3
        "Function_4_712",          # 04, 4
        "Function_5_716",          # 05, 5
        "Function_6_F27",          # 06, 6
        "Function_7_1D5C",         # 07, 7
        "Function_8_237E",         # 08, 8
        "Function_9_239D",         # 09, 9
        "Function_10_23BF",        # 0A, 10
        "Function_11_23DE",        # 0B, 11
        "Function_12_23F6",        # 0C, 12
        "Function_13_2415",        # 0D, 13
        "Function_14_2434",        # 0E, 14
        "Function_15_244F",        # 0F, 15
        "Function_16_268E",        # 10, 16
        "Function_17_2B3F",        # 11, 17
        "Function_18_6D76",        # 12, 18
        "Function_19_6E3E",        # 13, 19
        "Function_20_6EC2",        # 14, 20
        "Function_21_7847",        # 15, 21
        "Function_22_7884",        # 16, 22
        "Function_23_7A55",        # 17, 23
    ))


    def Function_0_24C(): pass

    label("Function_0_24C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_24C end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31C")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 2)

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32D")
    Event(0, 16)

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_33B")
    Jump("loc_59C")

    label("loc_33B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_36F")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 53490, 30, 125950, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_59C")

    label("loc_36F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A3")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 53490, 30, 125950, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_59C")

    label("loc_3A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3B1")
    Jump("loc_59C")

    label("loc_3B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40A")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 55790, 30, 125880, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 53480, 30, 125770, 90)
    Jump("loc_59C")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_465")
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 55790, 30, 125880, 340)
    Jump("loc_59C")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4E1")
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 55790, 30, 125880, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 53480, 30, 125770, 90)
    Jump("loc_59C")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4EF")
    Jump("loc_59C")

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_56D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_52C")
    ClearChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)

    label("loc_52C")

    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 167200, 0, 128330, 270)
    Jump("loc_59C")

    label("loc_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_59C")
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 170830, 0, 120150, 90)
    BeginChrThread(0x9, 0, 0, 0)

    label("loc_59C")

    Return()

    # Function_1_304 end

    def Function_2_59D(): pass

    label("Function_2_59D")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_59D end

    def Function_3_5A4(): pass

    label("Function_3_5A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BB")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D7")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_5D7")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5E9")
    Jump("loc_67A")

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5F7")
    Jump("loc_67A")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_605")
    Jump("loc_67A")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_613")
    Jump("loc_67A")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_621")
    Jump("loc_67A")

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_62F")
    Jump("loc_67A")

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_641")
    OP_66(0x1, 0x1)
    Jump("loc_67A")

    label("loc_641")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_653")
    OP_66(0x1, 0x1)
    Jump("loc_67A")

    label("loc_653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_661")
    Jump("loc_67A")

    label("loc_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_67A")
    OP_66(0x1, 0x1)

    label("loc_67A")

    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_6EF")

    label("loc_6D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6EF")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_6EF")

    label("loc_6EF")

    SetMapObjFlags(0x1, 0x10)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_711")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x2, 0x1)

    label("loc_711")

    Return()

    # Function_3_5A4 end

    def Function_4_712(): pass

    label("Function_4_712")

    Call(0, 5)
    Return()

    # Function_4_712 end

    def Function_5_716(): pass

    label("Function_5_716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7D5")
    TalkBegin(0x8)
    OP_4B(0xA, 0xFF)

    #C0001
    ChrTalk(
        0x8,
        (
            "#2803F嗯，接下来的事情\x01",
            "就交给你和玛丽亚贝尔了。\x02\x03",

            "#2800F我一会还要去\x01",
            "和市长会面，一起吃个饭。\x01",
            "虽然不好意思，但我实在是非去不可呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        "是，请交给我们吧……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    TalkEnd(0x8)
    Jump("loc_F26")

    label("loc_7D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_ABD")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_872")
    Jump("loc_8BC")

    label("loc_872")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_892")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BC")

    label("loc_892")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B2")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8BC")

    label("loc_8B2")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8BC")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_972")

    #C0003
    ChrTalk(
        0x8,
        (
            "#2800F其实，我下午\x01",
            "又要去出差了。\x02\x03",

            "必须要趁现在将\x01",
            "剩下的工作处理完才行。\x02\x03",

            "#2806F所以从早上一直开会到现在。\x01",
            "哎呀，可真够受的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB1")

    label("loc_972")


    #C0004
    ChrTalk(
        0x8,
        "#2800F哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0105F真不好意思，\x01",
            "您好像正在工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#2800F如你所见，\x01",
            "从早上到现在，一直都在开会。\x02\x03",

            "#2806F我毕竟也是个克洛斯贝尔人，\x01",
            "像游行这种重大活动\x01",
            "还是想去看一看的……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0000F啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#2804F算了，说笑而已。\x02\x03",

            "#2800F艾莉，还有各位。\x01",
            "你们也要加油\x01",
            "工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#0100F是的，谢谢您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AB1")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Jump("loc_F26")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F26")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B5A")
    Jump("loc_BA4")

    label("loc_B5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B7A")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BA4")

    label("loc_B7A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9A")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BA4")

    label("loc_B9A")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BA4")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1A")

    #C0010
    ChrTalk(
        0x8,
        (
            "#2800F哎呀，诸位，工作还顺利吧？\x02\x03",

            "#2809F哈哈哈，如果有什么要事，\x01",
            "随时都可以过来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#0306F真是爽朗的大叔啊……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0105F叔叔，在纪念庆典期间，\x01",
            "您可是特别忙呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#2804F哈哈，确实，会谈和宴会\x01",
            "之类的事情堆积如山。\x02\x03",

            "#2800F不过，如果来访的是诸位，我随时都欢迎。\x01",
            "……要不然，干脆就和我一起\x01",
            "出席明天的会谈如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0012F再、再怎么说，那也太不合适了……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#0206F感谢您的好意，但还请容我们婉言谢绝。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#2806F哦，这样啊……那可真是遗憾。\x02\x03",

            "#2809F哈哈哈，你们就算半途入场也没问题，\x01",
            "所以不妨再考虑考虑哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0106F（叔叔的心胸气度\x01",
            "  果然不一般啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1F")

    label("loc_E1A")


    #C0018
    ChrTalk(
        0x8,
        (
            "#2803F在纪念庆典期间，我的工作\x01",
            "也是堆积如山，不过……\x02\x03",

            "#2800F哈哈，如果来访的是诸位，我随时都欢迎。\x01",
            "不用在意成人世界的那些规矩，\x01",
            "有没有预约都无所谓，想来就来吧。\x02\x03",

            "#2800F比起这些……你们几个\x01",
            "在纪念庆典期间的工作也很艰巨吧。\x02\x03",

            "不必太勉强自己，\x01",
            "适当努力就好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1F")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_F26")

    Return()

    # Function_5_716 end

    def Function_6_F27(): pass

    label("Function_6_F27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F49")
    Call(0, 20)
    Return()

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_104F")
    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0x9,
        (
            "#2900F卡拉小姐和女仆说，\x01",
            "想要一起去格兰赛尔\x01",
            "参观呢。\x02\x03",

            "#2903F如果是以离家出走为目的，\x01",
            "竟还在我面前正大光明地说出来，\x01",
            "也真是相当奇怪呢……\x02\x03",

            "#2900F算了，我今天实在很忙，\x01",
            "也没空理会这些事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0003F抱、抱歉，您这么忙，\x01",
            "我们还来打扰。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_1229")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1118")

    #C0021
    ChrTalk(
        0x9,
        (
            "#2901F不过，话说回来……\x01",
            "哈尔特曼议长究竟\x01",
            "在做些什么呢？\x02\x03",

            "#2903F自己的同伙做出了\x01",
            "那种事情，他应该也\x01",
            "没法再轻举妄动了吧……\x02\x03",

            "#2910F就算是在议会期间，\x01",
            "也未免太过狂妄了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_1118")


    #C0022
    ChrTalk(
        0x9,
        (
            "#2906F呼，袭击事件给股价造成的负面影响，\x01",
            "似乎有希望抑制住呢。\x02\x03",

            "#2903F不过，如果他们再继续这样争斗下去，\x01",
            "不知道还会对金融界·贸易市场\x01",
            "造成多么恶劣的影响。\x02\x03",

            "#2901F希望警察那边也能\x01",
            "再稍微努力一点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0001F这、这是当然的！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#0104F我们一定会全力以赴。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1221")

    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_1229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_14B7")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12B5")

    #C0025
    ChrTalk(
        0x9,
        (
            "#2903F真是的，父亲不在的时候，\x01",
            "竟然发生了这种荒唐至极的骚乱……\x02\x03",

            "#2910F『鲁巴彻』的行为\x01",
            "实在是让人难以置信！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14AF")

    label("loc_12B5")


    #C0026
    ChrTalk(
        0x9,
        (
            "#2910F真是的，我已经受够了……！\x01",
            "居然做下这种蠢事！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#0005F玛丽亚贝尔小姐……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0101F看样子……\x01",
            "你好像已经知道了啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#2901F那当然了……！\x01",
            "事情就发生在我的眼皮底下啊！\x02\x03",

            "#2903F竟然在ＩＢＣ大厦的附近\x01",
            "展开枪战……\x02\x03",

            "#2910F可恨的『鲁巴彻』……\x01",
            "要是给股价造成不良影响，我是不会饶恕你们的！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x101,
        "#0006F原来是因为这个生气啊……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#0106F算、算了，以贝尔的立场来说，\x01",
            "这种担心也是理所当然的呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_14AF")

    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_14B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1711")
    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1571")

    #C0032
    ChrTalk(
        0xA,
        (
            "说起来，大小姐。\x01",
            "今天下午是不是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#2904F嗯，我要出去谈生意。\x02\x03",

            "#2900F晚上也有些私事，所以不回来了，\x01",
            "之后就拜托你了。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        "嗯，请放心交给我吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1705")

    label("loc_1571")


    #C0035
    ChrTalk(
        0x9,
        (
            "#2904F对了，这些文件\x01",
            "由我来处理。\x02\x03",

            "#2900F银行部门和投资部门那边的事情\x01",
            "就拜托你继续应对了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "嗯，那就在下次的高层会议上\x01",
            "进行报告吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)
    Sleep(500)

    #C0037
    ChrTalk(
        0x9,
        (
            "#2905F啊，父亲他\x01",
            "又出差去了哦。\x02\x03",

            "#2906F把剩下的工作全都推给了我……\x01",
            "他总是这么狡猾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0000F哈哈，是吗……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#2900F嗯，他最擅长的事情\x01",
            "就是把工作推给别人。\x02\x03",

            "#2906F所以我现在也已经\x01",
            "完全习惯了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x0, 0x0, 0x41EB0, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)

    label("loc_1705")

    OP_4C(0xA, 0xFF)
    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_1711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1851")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17A0")
    OP_4B(0xA, 0xFF)

    #C0040
    ChrTalk(
        0x9,
        (
            "#2900F嗯，那边的事情\x01",
            "就由我来负责。\x02\x03",

            "报告就交给巴雷塔先生了，\x01",
            "这样可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            "嗯，那么\x01",
            "就这么决定吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_1849")

    label("loc_17A0")


    #C0042
    ChrTalk(
        0x9,
        (
            "#2900FＩＢＣ所涉足的事业\x01",
            "一般都不会少于二十件呢。\x02\x03",

            "光是企划书和报告书就已经多到这种程度了……\x02\x03",

            "#2906F呼，给父亲当帮手\x01",
            "也真是不轻松呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x0, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_1849")

    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1C9E")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18EE")
    Jump("loc_1938")

    label("loc_18EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_190E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1938")

    label("loc_190E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_192E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1938")

    label("loc_192E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1938")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A8A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19CF")

    #C0043
    ChrTalk(
        0x9,
        (
            "#2904F父亲他\x01",
            "总算回来了……\x02\x03",

            "#2902F艾莉，有时间一定要来哦，\x01",
            "就算是晚上也没关系的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A56")

    label("loc_19CF")


    #C0044
    ChrTalk(
        0x9,
        (
            "#2904F今天这场宴会，\x01",
            "来宾都是我的亲朋好友，\x01",
            "所以场面不算太正式，很轻松的。\x02\x03",

            "#2902F艾莉，有时间一定要来啊，\x01",
            "就算是晚上也没关系的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A56")


    #C0045
    ChrTalk(
        0x102,
        (
            "#0102F嗯……\x01",
            "如果时间上与工作不冲突的话…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C92")

    label("loc_1A8A")


    #C0046
    ChrTalk(
        0x9,
        (
            "#2909F啊，艾莉，稍后\x01",
            "和我一起去参加宴会吧？\x02\x03",

            "#2902F虽然要到下午才会正式开始，\x01",
            "但一定不会让你感到无聊的。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#0106F贝尔真是的……昨天\x01",
            "不是才刚刚参加过庆祝会嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "#2905F啊，今天来参加宴会的人\x01",
            "全都是我的亲朋好友，\x01",
            "所以场面不算太正式，很轻松的。\x02\x03",

            "#2901F这种场合怎么可以缺了艾莉嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0012F那个，可是我们支援科\x01",
            "还有工作要做呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "#2904F那么，请假吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x104,
        "#0309F（还是一点都没有变，典型的女王风格呢。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1C92")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_1C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_END)), "loc_1D58")
    TalkBegin(0xFE)

    #C0052
    ChrTalk(
        0x9,
        (
            "#2904F既然如此，到时可要把\x01",
            "事情的详细经过说给我听哦。\x02\x03",

            "#2902F我也是很感兴趣的。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#0000F啊，好的。\x01",
            "等到彻底解决之后，一定。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        "#0100F我们还会再来的，贝尔。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1D5B")

    label("loc_1D58")

    Call(0, 7)

    label("loc_1D5B")

    Return()

    # Function_6_F27 end

    def Function_7_1D5C(): pass

    label("Function_7_1D5C")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x9, 0xFF)
    OP_68(169000, 1500, 120150, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(200, 0)
    SetCameraDistance(36080, 0)
    SetChrPos(0x101, 169000, 0, 119650, 90)
    SetChrPos(0x102, 168750, 0, 120650, 90)
    SetChrPos(0x103, 167500, 0, 119650, 90)
    SetChrPos(0x104, 167250, 0, 120650, 90)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_93(0x9, 0x10E, 0x1F4)

    #C0055
    ChrTalk(
        0x9,
        (
            "#2902F#11P啊，欢迎来到\x01",
            "我的私人房间。\x02\x03",

            "#2904F除了那个寡廉鲜耻的某人之外，\x01",
            "其他客人全部欢迎哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        "#0006F#6P（还在对我耿耿于怀啊……）\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0300F#6P话说回来，这里装饰着\x01",
            "不少高价名画与美术品啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0205F#6P看起来，似乎每一件\x01",
            "都是艺术名家的作品呢……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 1, 0, 8)
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_68(170830, 1400, 120150, 1500)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        (
            "#0005F#6P这……！？\x02\x03",

            "#0001F那个……冒昧地问一下，\x01",
            "后面的那个是……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0060
    ChrTalk(
        0x102,
        (
            "#0109F#5P那是罗赞贝尔克工房制造的人偶哦。\x02\x03",

            "#0102F看起来栩栩如生吧？\x01",
            "……贝尔可是罗赞贝尔克产品\x01",
            "的大收藏家哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "#2904F#11P呵呵，那两个可是我\x01",
            "特别喜爱的孩子呢。\x02\x03",

            "#2902F如果有兴趣，\x01",
            "就离近一点去观赏吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#0005F#6P可以吗……？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 1, 0, 10)
    BeginChrThread(0x101, 1, 0, 11)
    BeginChrThread(0x102, 1, 0, 12)
    BeginChrThread(0x103, 1, 0, 13)
    BeginChrThread(0x104, 1, 0, 14)
    Sleep(1000)
    OP_68(171960, 1400, 119960, 2500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0063
    ChrTalk(
        0x103,
        (
            "#0202F#6P这就是罗赞贝尔克工房的人偶……\x01",
            "皮肤纹理也如此细腻，\x01",
            "完全不像是制作出来的人偶呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0302F#6P真是精巧得让人难以置信啊……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0002F#6P好厉害……\x02\x03",

            "#0004F之前听说这些人偶的价格相当昂贵，\x01",
            "现在看来，的确是物有所值……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "#2904F#11P你可以摸一摸。\x02\x03",

            "#2902F只是，如果不小心碰坏的话，\x01",
            "还是要照价赔偿哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0067
    ChrTalk(
        0x102,
        "#0106F#5P贝尔可真是的……\x02",
    )

    CloseMessageWindow()

    def lambda_22B6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22B6)
    Sleep(50)

    def lambda_22C6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_22C6)
    Sleep(60)

    def lambda_22D6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22D6)
    WaitChrThread(0x101, 1)

    #C0068
    ChrTalk(
        0x101,
        (
            "#0012F#5P请不要说这么\x01",
            "恐怖的话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#0211F#5P太可怕了，绝对不敢碰。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        "#2909F#11P呵呵，开个玩笑啦。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168730, 0, 120050, 90)
    SetChrPos(0x9, 170830, 0, 120150, 90)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0xB8, 3)
    EventEnd(0x5)
    Return()

    # Function_7_1D5C end

    def Function_8_237E(): pass

    label("Function_8_237E")

    OP_93(0x103, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(500)
    Return()

    # Function_8_237E end

    def Function_9_239D(): pass

    label("Function_9_239D")

    Sleep(300)
    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x104, 0x5A, 0x1F4)
    Sleep(500)
    Return()

    # Function_9_239D end

    def Function_10_23BF(): pass

    label("Function_10_23BF")

    OP_95(0x9, 171500, 0, 118600, 2000, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(500)
    Return()

    # Function_10_23BF end

    def Function_11_23DE(): pass

    label("Function_11_23DE")

    Sleep(500)
    OP_95(0x101, 170930, 0, 119600, 2000, 0x0)
    Return()

    # Function_11_23DE end

    def Function_12_23F6(): pass

    label("Function_12_23F6")

    Sleep(600)
    OP_95(0x102, 171100, 0, 121670, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_12_23F6 end

    def Function_13_2415(): pass

    label("Function_13_2415")

    Sleep(800)
    OP_95(0x103, 171000, 0, 120710, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_13_2415 end

    def Function_14_2434(): pass

    label("Function_14_2434")

    Sleep(1000)
    OP_95(0x104, 170010, 0, 121040, 2000, 0x0)
    Sleep(500)
    Return()

    # Function_14_2434 end

    def Function_15_244F(): pass

    label("Function_15_244F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24F4")

    #C0071
    ChrTalk(
        0xFE,
        (
            "总裁外出不在的时候，我们这些\x01",
            "高层人员必须要撑起场面才行。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "虽然也会让玛丽亚贝尔大小姐承受不小的负担，\x01",
            "但这也是没办法的事情，希望她能谅解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268A")

    label("loc_24F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2566")

    #C0073
    ChrTalk(
        0xFE,
        (
            "正是因为到了纪念庆典，\x01",
            "总裁才会如此忙碌……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "……我们也必须要团结一心，\x01",
            "共同在后方支持他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268A")

    label("loc_2566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_268A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25CE")

    #C0075
    ChrTalk(
        0xFE,
        "嗯，详细情况请参考您手边的资料。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "投资部门的成长速率\x01",
            "虽然极高，不过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268A")

    label("loc_25CE")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0077
    ChrTalk(
        0xFE,
        (
            "嗯……保安部的人\x01",
            "到底在干什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……哦，原来是艾莉小姐\x01",
            "的同事吗，\x01",
            "实在是不好意思了。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "但我们现在正在开会，\x01",
            "还请保持安静。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_268A")

    TalkEnd(0xFE)
    Return()

    # Function_15_244F end

    def Function_16_268E(): pass

    label("Function_16_268E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(55500, 1000, 14000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 57500, 0, 13700, 270)
    SetChrPos(0x102, 57500, 0, 14400, 270)
    SetChrPos(0x103, 57500, 0, 14400, 270)
    SetChrPos(0x104, 57500, 0, 13700, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    Sleep(500)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)

    def lambda_2767():
        OP_96(0xFE, 0xCF08, 0x0, 0x396C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2767)

    def lambda_2781():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2781)
    Sleep(450)

    def lambda_2795():
        OP_96(0xFE, 0xCF08, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2795)

    def lambda_27AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27AF)
    Sleep(450)

    def lambda_27C3():
        OP_96(0xFE, 0xD3B8, 0x0, 0x396C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_27C3)

    def lambda_27DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_27DD)
    Sleep(450)

    def lambda_27F1():
        OP_96(0xFE, 0xD3B8, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_27F1)

    def lambda_280B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_280B)
    WaitChrThread(0x102, 1)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    Sleep(100)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2878():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2878)
    Sleep(50)

    def lambda_2888():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2888)

    #C0080
    ChrTalk(
        0x101,
        "#0005F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(60000, 1000, 4300, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_28C4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_28C4)
    Sleep(100)

    def lambda_28D4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28D4)
    OP_6F(0x11)
    Sleep(300)
    Fade(1000)
    OP_68(62400, 1200, 0, 0)
    MoveCamera(110, 10, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, 54500, 0, 6300, 135)
    SetChrPos(0x102, 54500, 0, 8200, 135)
    SetChrPos(0x103, 53500, 0, 7400, 135)
    SetChrPos(0x104, 55500, 0, 7200, 135)
    OP_68(60000, 1200, 3800, 8000)
    MoveCamera(90, 10, 0, 8000)
    SetCameraDistance(23500, 8000)
    OP_6F(0x79)

    #C0081
    ChrTalk(
        0x101,
        "#0002F#5P好厉害啊……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0302F呼～……这里一看\x01",
            "就知道花了很多钱啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#0204F……位于下层的\x01",
            "爱普斯泰恩财团的事务所，\x01",
            "我倒是来过不少次……\x02\x03",

            "#0202F不过，最上层的视野确实与众不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        "#0102F是啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(54500, 1100, 7200, 0)
    MoveCamera(76, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0085
    ChrTalk(
        0x102,
        (
            "#0100F#5P总裁室就是最里面的那间。\x02\x03",

            "让叔叔等太久可不好，\x01",
            "快点过去吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2ADF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2ADF)
    Sleep(50)

    def lambda_2AEF():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2AEF)
    Sleep(50)
    TurnDirection(0x103, 0x102, 500)

    #C0086
    ChrTalk(
        0x101,
        "#11P#0000F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 53200, 0, 6700, 0)
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    SetScenarioFlags(0x82, 4)
    EventEnd(0x5)
    Return()

    # Function_16_268E end

    def Function_17_2B3F(): pass

    label("Function_17_2B3F")

    EventBegin(0x0)
    Fade(1000)
    OP_68(52500, 1000, 45000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 51800, 0, 43000, 0)
    SetChrPos(0x102, 52500, 0, 44400, 0)
    SetChrPos(0x103, 52800, 0, 43000, 0)
    SetChrPos(0x104, 53800, 0, 43000, 0)
    OP_0D()

    def lambda_2BBE():
        OP_95(0xFE, 52500, 0, 44900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BBE)
    WaitChrThread(0x102, 1)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(800)

    #C0087
    ChrTalk(
        0x102,
        "#11P#0102F──叔叔，我是艾莉。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 52500, 0, 47500, 0)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0088
    NpcTalk(
        0x8,
        "男性的声音",
        "#5P#2S哦，快进来吧。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#11P#0104F是，失礼了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_2C8F():
        OP_95(0xFE, 52500, 0, 45900, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C8F)
    OP_0D()
    EndChrThread(0x102, 0x1)
    OP_70(0x2, 0x0)
    SetMapObjFlags(0x2, 0x10)
    LoadChrToIndex("apl/ch50217.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02900.itp")
    OP_68(55000, 1000, 128199, 0)
    MoveCamera(0, 13, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x8, 0x8)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x101, 54100, 0, 116900, 0)
    SetChrPos(0x102, 55000, 0, 118300, 0)
    SetChrPos(0x103, 55000, 0, 116900, 0)
    SetChrPos(0x104, 55900, 0, 116900, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(14500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)
    Fade(1000)
    OP_68(55000, 1100, 128800, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(55000, 1100, 127000, 4000)

    def lambda_2E67():
        OP_95(0xFE, 55000, 0, 125300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E67)
    Sleep(300)

    def lambda_2E84():
        OP_95(0xFE, 54100, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E84)
    Sleep(200)

    def lambda_2EA1():
        OP_95(0xFE, 55900, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EA1)
    Sleep(200)

    def lambda_2EBE():
        OP_95(0xFE, 55000, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2EBE)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    #N0090
    NpcTalk(
        0x8,
        "穿西装的男性",
        (
            "#5P#2800F呀，艾莉，好久不见了。\x02\x03",

            "都有半年左右了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#12P#0109F是的，迪塔叔叔还是\x01",
            "这么有精神，实在是太好了。\x02\x03",

            "#0100F那个，没有预约就来打扰您，\x01",
            "实在是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #N0092
    NpcTalk(
        0x8,
        "穿西装的男性",
        (
            "#5P#2804F哈哈，不要和我说\x01",
            "那么见外的客套话。\x02\x03",

            "#2800F你是我好友的女儿，\x01",
            "又是我女儿的童年玩伴，\x02\x03",

            "对我来说与亲人无异。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        "#12P#0104F……谢谢您。\x02",
    )

    CloseMessageWindow()

    #N0094
    NpcTalk(
        0x8,
        "穿西装的男性",
        (
            "#5P#2800F嗯，我听小女说过，\x01",
            "你已经当了警察……\x02\x03",

            "这几位都是你的同事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#12P#0100F是的，\x01",
            "他们都是我在『特别任务支援科』的同伴。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    def lambda_30DF():
        OP_96(0xFE, 0xDC50, 0x0, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30DF)
    WaitChrThread(0x102, 1)

    #C0096
    ChrTalk(
        0x101,
        (
            "#12P#0004F初次见面，\x01",
            "我叫罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        (
            "#4P#0300F兰迪·奥兰多，\x01",
            "请多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#4P#0204F我是缇欧·普拉托，\x01",
            "初次见面……\x02",
        )
    )

    CloseMessageWindow()

    #N0099
    NpcTalk(
        0x8,
        "穿西装的男性",
        (
            "#5P#2804F呵呵，我在克洛斯贝尔时代周刊上\x01",
            "看到过关于你们的报道，也算是有了大致了解。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("穿西装的男性")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            "我是ＩＢＣ的总裁，\x01",
            "迪塔·库罗伊斯。\x02\x03",

            "罗伊德、兰迪、缇欧，\x02\x03",

            "请你们不要拘束，\x01",
            "直接叫我迪塔就可以了。\x02",
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
    OP_63(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(860, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0101
    ChrTalk(
        0x101,
        "#12P#0012F啊，这……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#12P#0205F（他的牙齿似乎在闪光呢……）\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#12P#0309F（还、还真是个性格超级\x01",
            "  爽朗的大叔啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)
    SetChrSubChip(0x8, 0x1)

    #C0104
    ChrTalk(
        0x8,
        (
            "#5P#2801F对了，不是说有工作方面\x01",
            "的事情要找我谈吗……\x02\x03",

            "#2800F到底是什么事呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    #C0105
    ChrTalk(
        0x102,
        (
            "#0103F嗯，其实是……\x02\x03",

            "#0101F我们正在对某个案件进行调查，\x01",
            "在此过程中──\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6F(0x10)
    OP_68(55180, 1100, 127250, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 54100, 0, 125600, 0)
    SetChrPos(0x102, 55200, 0, 125800, 0)
    SetChrPos(0x103, 54600, 0, 124400, 0)
    SetChrPos(0x104, 55700, 0, 124600, 0)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(19000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0106
    ChrTalk(
        0x8,
        (
            "#5P#2803F──原来如此。\x02\x03",

            "#2801F那个自称为『银』的人\x01",
            "通过ＩＢＣ的终端把导力邮件\x01",
            "发送到了你们的办公室吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#0106F嗯……没错。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x103,
        (
            "#12P#0203F……我想，其发件地址恐怕是\x01",
            "这座大厦的主终端。\x02\x03",

            "#0200F而犯人很可能就是操作了\x01",
            "那台终端装置，而将邮件发出的。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#5P#2803F嗯……\x02\x03",

            "说句实话，我对这座大厦的安全系统\x01",
            "还是很有自信的。\x02\x03",

            "#2801F特别是终端室所在的区域，\x01",
            "只有获得许可的人\x01",
            "才能够进入。\x02\x03",

            "终端装置也是一样，没有权限的人\x01",
            "是无法进行操作的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#12P#0001F这样问也许非常失礼……\x01",
            "不过，在可以操作终端装置的技术员之中，\x01",
            "有没有什么比较可疑的人呢？\x02\x03",

            "比如，最近刚刚入职的新人，\x01",
            "或者是有过什么前科的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#5P#2803F嗯……据我所知，\x01",
            "那里的人全都值得信赖呢。\x02\x03",

            "#2800F──比起那个，罗伊德。\x02\x03",

            "你再想想，有没有其它可能性呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#5P#2804F比如说，对了……\x02\x03",

            "#2800F真正的『银』其实就是我，\x01",
            "给你们发邮件的也是我，之类的。\x02",
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0114
    ChrTalk(
        0x101,
        "#12P#4S#0011F哎！？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        "#0307F真、真的假的！？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0105F叔、叔叔……！？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#5P#2809F哈哈，我不是都说了『比如』嘛。\x02\x03",

            "#2800F传说中的神秘杀手，如果\x01",
            "其真实身份是我这种地位的人，\x01",
            "倒也很有意思……\x02\x03",

            "不过，在现实中，毕竟不可能\x01",
            "出现那种异想天开的状况啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#12P#0012F是、是啊……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#0106F真是的……\x01",
            "请不要吓唬人嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x103,
        "#12P#0203F真是位爱开玩笑的人啊……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#5P#2809F哈哈哈，真是失敬了。\x02\x03",

            "#2803F不过，你们试想一下。\x02\x03",

            "#2801F如果发送邮件的人\x01",
            "真的是这里的技术员……\x02\x03",

            "那他这种行为，不就等于是\x01",
            "自行暴露身份吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x102,
        "#0101F啊……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        "#12P#0205F……确实如此呢。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0301F也就是说，我们反而应该\x01",
            "考虑一下技术员作案之外的可能性吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0125
    ChrTalk(
        0x101,
        (
            "#5P#0001F──缇欧。\x02\x03",

            "从记录上看，虽然邮件是从\x01",
            "ＩＢＣ的终端发送到支援科的……\x02\x03",

            "但这记录有没有可能是伪造的呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C1C():
        OP_93(0xFE, 0xBE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C1C)

    def lambda_3C29():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3C29)

    #C0126
    ChrTalk(
        0x103,
        (
            "#12P#0203F这个嘛……\x02\x03",

            "#0200F从其它地方入侵ＩＢＣ\x01",
            "的终端，然后再进行远程操作。\x01",
            "这种可能性也不是完全没有。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#5P#0005F『入侵』……？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        "#0305F那是什么意思啊……？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#5P#0106F详细知识我虽然也不太懂……\x02\x03",

            "#0100F但大致来说，就是破解保护着\x01",
            "终端的安全系统，然后再进行\x01",
            "非法操作的技术，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#12P#0204F基本没错。\x02\x03",

            "如果是被导力网络相连的终端，\x01",
            "从理论上来说，在任何一处终端上\x01",
            "都可以对其它终端进行远程操作。\x02\x03",

            "#0200F不过，这需要非常高端\x01",
            "的知识与技术……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#5P#2803F顺便一说，从事这种行为的人，\x01",
            "我们一般都会称之为『黑客』。\x02\x03",

            "#2801F导力网络如今还没有普及，\x01",
            "就整个大陆来说，也只在很有限\x01",
            "的一些地域内进行试验运用……\x02\x03",

            "不过，像这样的事例，\x01",
            "似乎很早就有过报告呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3ED0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3ED0)
    Sleep(100)

    def lambda_3EE0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3EE0)
    Sleep(100)

    def lambda_3EF0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3EF0)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0132
    ChrTalk(
        0x101,
        "#12P#0001F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x104,
        (
            "#0303F也就是说……\x02\x03",

            "#0301F『银』不仅是个刺客，\x01",
            "而且还是个『黑客』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#0106F#5P虽然现在还无法完全断定……\x02\x03",

            "#0101F不过，以目前的情况来看，那封邮件\x01",
            "很可能是从这幢大厦之外的某处发送的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#5P#2803F嗯，我所信赖的技术人员们\x01",
            "得以洗清嫌疑，这倒是令人欣慰……\x02\x03",

            "#2801F不过，现在又出现了一个\x01",
            "很严重的新问题，那就是主终端\x01",
            "很有可能遭到了黑客的入侵。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0136
    ChrTalk(
        0x8,
        (
            "#5P#2804F好，那就这样吧。\x02\x03",

            "#2800F我安排你们\x01",
            "进入终端室。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#0105F这、这样做没问题吗？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#5P#2800F嗯，只要调查一下主终端，\x01",
            "或许就能查出黑客留下的\x01",
            "痕迹之类的线索……\x02\x03",

            "技术员都在那里工作，\x01",
            "要是有什么话想问，也可以问他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#12P#0002F……真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#0104F叔叔……\x01",
            "真是太谢谢您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#5P#2804F哪里，发生了这种问题，\x01",
            "我们这边也无法袖手旁观啊。\x02\x03",

            "#2800F呵呵──话说回来，艾莉。\x02\x03",

            "看起来，你最近好像生活得\x01",
            "相当充实吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#0105F哎……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#5P#2804F刚听说你要当警察的时候，\x01",
            "我还稍微怀有一点疑问……\x02\x03",

            "不过，现在看来，这份职业似乎\x01",
            "确实能够让你积累很好的经验。\x02\x03",

            "#2800F我现在正式对你表示声援。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0102F叔叔……\x02\x03",

            "#0104F听您这么一说，\x01",
            "我真是信心百倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "#5P#2804F呵呵，还有，你们几个也是……\x02\x03",

            "#2800F你们比起杂志上所报道的，\x01",
            "让我感到了更大的潜力呢。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0147
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 56000, 0, 128900, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(500)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7001", 0)
    OP_68(56450, 900, 129560, 2500)
    MoveCamera(47, 13, 0, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_442C():
        OP_95(0xFE, 56000, 0, 131100, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_442C)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    #C0148
    ChrTalk(
        0x8,
        (
            "#2803F#11P……我想，你们应该已经察觉到了吧，\x01",
            "这座名为克洛斯贝尔的自治州，\x01",
            "其实是个非常复杂的是非之地。\x02\x03",

            "关于这一点，恐怕艾莉\x01",
            "是最深有感触的吧……\x02\x03",

            "#2801F我认为，最严重的一个问题，\x01",
            "就是『正义』这个词早已经变得\x01",
            "形同虚设了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0149
    ChrTalk(
        0x101,
        "#12P#0001F形同虚设的『正义』……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#0101F那……\x01",
            "到底是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#2801F#11P所谓的『正义』，\x01",
            "在很多人眼里，\x01",
            "只不过就是一句漂亮话罢了。\x02\x03",

            "#2803F而且在每个人的心中，正义的具体标准\x01",
            "也都各不相同……所以，可能有一些人会\x01",
            "偏激地叫嚣着正义并不存在。\x02\x03",

            "#2804F然而，无论以何种方式……\x02\x03",

            "#2800F归根结底，人类终究还是一种\x01",
            "会去追逐正义的生物。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#12P#0005F哎……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x103,
        "#12P#0205F人是追逐正义的生物……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(300)

    #C0154
    ChrTalk(
        0x8,
        (
            "#2804F#5P因为所谓的『正义』，\x01",
            "就是使人信赖社会的『基础』。\x02\x03",

            "#2800F比如，当发生犯罪行为时，\x01",
            "如果没有依法制裁犯罪者的\x01",
            "这种『正义』……\x02\x03",

            "那么很多人就会把自己关在家中，\x01",
            "不在必要之时绝不出门吧。\x02\x03",

            "这样一来，我们的社会生活\x01",
            "也就无法存续下去了。\x02\x03",

            "#2803F不过──在克洛斯贝尔，\x01",
            "『正义』的形式虽然很模糊，\x01",
            "但终究还是存在的。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x101,
        "#12P#0013F！！\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        "#0108F……那个………\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x8,
        (
            "#2801F#5P腐败的政治，以及黑手党问题……\x02\x03",

            "虽然警察不会对其进行整治，\x01",
            "但由于经济十分繁荣发达，\x01",
            "所以多数市民并不会为生计发愁。\x02\x03",

            "这样的结果就是表面上的犯罪事件很少，\x01",
            "但我们看不到的邪恶却在不断蔓延……\x02\x03",

            "#2803F然而，即使是在这种环境下，\x01",
            "人们还是会以各种方式\x01",
            "来追寻所谓的『正义』。\x02\x03",

            "因为不管是以何种形式，人们始终\x01",
            "需要可以对社会产生信赖的『安全感』。\x02\x03",

            "#2800F──正因如此，在克洛斯贝尔，\x01",
            "游击士才会受到如此热烈的欢迎。\x02",
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

    #C0158
    ChrTalk(
        0x101,
        "#12P#0005F啊……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#12P#0204F『以民间人士的安全为最优先』……\x02\x03",

            "#0202F确实是很有『正义伙伴』的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#0306F原来如此啊……\x02\x03",

            "#0301F之前一直都觉得，与其它国家相比，游击士\x01",
            "在这里好像被追捧到了一个不太正常的程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        "#0106F……现在总算可以理解了。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "#2803F#5P但是，正如你们所知，\x01",
            "游击士协会所能声张的正义，\x01",
            "终究还是有限的。\x02\x03",

            "而这个城市的毒瘤已经根深蒂固，\x01",
            "仅凭他们无法将其摘除。\x02\x03",

            "#2800F正因如此──\x01",
            "我才对你们的表现十分期待。\x02",
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

    #C0163
    ChrTalk(
        0x101,
        "#12P#0011F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#0305F是想让我们代替游击士，\x01",
            "将那些邪恶之徒全部打倒吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#2804F#5P哈哈，我想说的可不是\x01",
            "那么单纯浅显的事啊。\x02\x03",

            "#2800F你们要用自己的方式，\x01",
            "去追求自己心中的『正义』……\x02\x03",

            "然后以清晰可见的形式，将你们追寻正义的\x01",
            "身姿展现给市民们。我认为，这是非常重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#12P#0002F啊……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#0104F克洛斯贝尔仍然\x01",
            "存在着『正义』……\x02\x03",

            "#0100F而我们的职责，就是制造契机，\x01",
            "使市民们开始相信它吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "#2800F#5P正是如此。\x02\x03",

            "#2804F呵呵，从这层意义上来说，\x01",
            "克洛斯贝尔时代周刊上的那篇报道\x01",
            "也可谓十分有意义吧。\x02\x03",

            "几个尚不成熟的年轻警察，\x01",
            "在不时遭遇失败的境况下\x01",
            "却仍然为了追求正义而不断奋斗……\x02\x03",

            "#2800F虽然有些人会认为你们滑稽可笑，\x01",
            "但真正从心里否定你们的市民应该很少。\x02\x03",

            "即使程度有高有低……\x01",
            "大家也确实都在期待着你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#12P#0003F……………………………………\x02",
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

    #C0170
    ChrTalk(
        0x8,
        (
            "#5P#2804F呵呵，我一时兴起，\x01",
            "不知不觉说了这么多啊。\x02\x03",

            "#2800F──还是言归正传吧。\x02\x03",

            "刚才说到要批准你们\x01",
            "进入终端室了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#12P#0005F啊……\x02\x03",

            "#0000F是的，如果您可以批准，我们将感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0100F我们需要去找哪位\x01",
            "才能办理许可手续呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "#5P#2801F嗯，这个嘛。\x02\x03",

            "我也可以进入终端室，所以由我\x01",
            "带你们去是最好不过的，但是……\x02\x03",

            "#2803F很不巧，接下来我还有\x01",
            "很多事需要处理。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x102,
        (
            "#0106F真是不好意思，\x01",
            "在您如此繁忙的时候还前来打扰……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#5P#2804F哪里，不用在意。\x02\x03",

            "#2800F不过呢，对了……\x01",
            "既然如此，就找个\x01",
            "技术员带你们过去吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 55200, 0, 116800, 0)
    StopBGM(0xBB8)
    Sound(103, 0, 100, 0)
    Sleep(300)

    #N0176
    NpcTalk(
        0x9,
        "少女的声音",
        "──没有那个必要。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    Fade(500)
    OP_68(55200, 1100, 119300, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 53600, 0, 125600, 0)
    SetChrPos(0x102, 55200, 0, 125800, 0)
    SetChrPos(0x103, 54100, 0, 124600, 0)
    SetChrPos(0x104, 56300, 0, 125000, 0)
    OP_68(55200, 1100, 124300, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_5377():
        OP_95(0xFE, 55200, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5377)

    def lambda_5391():
        OP_95(0xFE, 56000, 0, 128900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5391)
    OP_0D()
    Sound(104, 0, 100, 0)

    def lambda_53B2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_53B2)
    Sleep(150)

    def lambda_53C2():

        label("loc_53C2")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_53C2")

    QueueWorkItem2(0x103, 2, lambda_53C2)
    Sleep(100)

    def lambda_53D7():

        label("loc_53D7")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_53D7")

    QueueWorkItem2(0x101, 2, lambda_53D7)
    Sleep(100)

    def lambda_53EC():

        label("loc_53EC")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_53EC")

    QueueWorkItem2(0x104, 2, lambda_53EC)
    WaitChrThread(0x9, 1)
    OP_6F(0x11)

    #C0177
    ChrTalk(
        0x101,
        "#5P#0005F哎……？\x02",
    )

    CloseMessageWindow()

    def lambda_541B():
        OP_95(0xFE, 55200, 0, 124200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_541B)
    WaitChrThread(0x102, 1)

    #C0178
    ChrTalk(
        0x102,
        "#5P#0105F贝尔……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    #C0179
    ChrTalk(
        0x8,
        "#2800F噢，你回来了啊。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("金发的少女")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            "父亲，我回来了。\x02\x03",

            "呵呵……\x01",
            "艾莉，好久不见了呢！\x02",
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
    OP_68(55240, 1100, 124620, 1000)

    def lambda_5528():
        OP_95(0xFE, 55200, 0, 123700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5528)
    WaitChrThread(0x9, 1)

    def lambda_5546():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5546)
    Sound(804, 0, 100, 0)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    SetChrSubChip(0x102, 0x1)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    Sleep(100)
    SetChrSubChip(0x102, 0x6)
    Sleep(100)
    SetChrSubChip(0x102, 0x7)
    Sleep(100)
    SetChrSubChip(0x102, 0x6)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)

    #C0181
    ChrTalk(
        0x102,
        "#0112F等、等一下啦……\x02",
    )

    CloseMessageWindow()

    #N0182
    NpcTalk(
        0x9,
        "金发的少女",
        (
            "#11P#2904F嗯～都有两个月没见了吧。\x02\x03",

            "#2901F不过，你……\x01",
            "好像稍微有些削瘦了啊？\x02\x03",

            "但手脚倒是变得\x01",
            "比以前结实一点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        (
            "#0104F呵呵，因为一直注意锻炼，\x01",
            "所以稍微长了点肌肉。\x02\x03",

            "#0102F其实，体重反而\x01",
            "有所增加呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x9,
        "金发的少女",
        (
            "#11P#2905F原来如此……\x02\x03",

            "听你这么一说，倒也真觉得\x01",
            "你身上的肌肉变得很有弹性了呢。\x02\x03",

            "#2909F呵呵，这里也是，\x01",
            "手感真是不错呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#0113F真、真是的……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0186
    ChrTalk(
        0x101,
        "#5P#0012F（真、真是个很有个性的人啊……）\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x104,
        (
            "#11P#0302F（不过，两个美人一起嬉戏，\x01",
            "  简直就是一幅养眼的画卷啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#5P#0211F（话说回来，总觉得她们\x01",
            "  并不只是普通朋友呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "#2804F哎呀哎呀，亲密的身体接触\x01",
            "不如就先到此为止如何？\x02\x03",

            "#2800F其他客人们可都被吓呆了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        "#0112F啊……\x02",
    )

    CloseMessageWindow()

    #N0191
    NpcTalk(
        0x9,
        "金发的少女",
        "#12P#2905F……啊呀…………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x3)
    Sleep(100)
    SetChrSubChip(0x102, 0x4)
    Sleep(100)
    SetChrSubChip(0x102, 0x0)
    Sleep(100)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x9, 0x8)

    def lambda_5911():
        OP_96(0xFE, 0xD7A0, 0x0, 0x1E014, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5911)
    WaitChrThread(0x9, 1)
    OP_93(0x102, 0x0, 0x1F4)

    #C0192
    ChrTalk(
        0x102,
        (
            "#0113F#11P我、我来介绍一下吧。\x02\x03",

            "#0102F她是玛丽亚贝尔……\x01",
            "总裁的女儿，也是我的朋友。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(150)

    #C0193
    ChrTalk(
        0x102,
        (
            "#0100F贝尔，他们都是我的同事，\x01",
            "罗伊德、兰迪还有缇欧──\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        (
            "#12P#2903F用不着介绍。\x02\x03",

            "#2901F我来亲自检验就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x102,
        "#0105F哎？\x02",
    )

    CloseMessageWindow()

    def lambda_5A1C():

        label("loc_5A1C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A1C")

    QueueWorkItem2(0x102, 2, lambda_5A1C)

    def lambda_5A2E():

        label("loc_5A2E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5A2E")

    QueueWorkItem2(0x8, 2, lambda_5A2E)
    BeginChrThread(0x9, 3, 0, 18)
    WaitChrThread(0x9, 3)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    #C0196
    ChrTalk(
        0x101,
        "#11P#0012F怎、怎么了吗……？\x02",
    )

    CloseMessageWindow()

    def lambda_5A81():
        OP_95(0xFE, 53600, 0, 124100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5A81)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x103, 500)

    def lambda_5AA6():

        label("loc_5AA6")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_5AA6")

    QueueWorkItem2(0x9, 2, lambda_5AA6)
    OP_9E(0x103, 0xD160, 0x1E4C4, 0x15F90, 0x5DC, 0x0)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x9, 0x2)

    #C0197
    ChrTalk(
        0x103,
        "#11P#0205F哎……\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "#2909F#5P她合格了。\x01",
            "呵呵，真是个可爱的女孩啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(55000, 1100, 125300, 1300)
    MoveCamera(55, 21, 0, 1300)

    def lambda_5B3B():
        OP_95(0xFE, 55000, 0, 125300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5B3B)
    Sleep(300)

    def lambda_5B58():
        OP_96(0xFE, 0xD7A0, 0x0, 0x1E3FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B58)
    Sleep(300)

    def lambda_5B75():
        OP_96(0xFE, 0xD1C4, 0x0, 0x1E460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B75)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    TurnDirection(0x9, 0x104, 500)
    Sleep(500)
    TurnDirection(0x9, 0x101, 500)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0199
    ChrTalk(
        0x9,
        "#11P#2901F然后，你们两个都不合格。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0200
    ChrTalk(
        0x101,
        "#6P#0011F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        "#0305F#11P这、这是什么意思啊……！？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "#11P#2903F哼，如此不修边幅的臭男人，\x01",
            "竟然还一直和我的艾莉在一起。\x02\x03",

            "#2901F如此行为，连女神都无法原谅哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        "#6P#0006F不修边幅……\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        "#12P#0101F等、等一下啦，贝尔……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "#11P#2901F这算什么啊？\x01",
            "如此随便的服装。\x02\x03",

            "至少也该穿件西装吧，\x01",
            "这可是最基本的礼仪。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#6P#0005F这、这个，那个……\x02\x03",

            "#0012F在市内和市外展开调查活动的时候，\x01",
            "还是穿这种衣服比较方便啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "#11P#2903F不必狡辩了。\x02\x03",

            "#2901F真是的，所以我才\x01",
            "反对艾莉当警察。\x02\x03",

            "和我一起做些大事业，\x01",
            "明显要比当警察有意义得多嘛……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 19)

    #C0208
    ChrTalk(
        0x102,
        "#12P#0106F啊，好啦……贝尔你可真是的！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)

    #C0209
    ChrTalk(
        0x8,
        (
            "#2809F哈哈哈，\x01",
            "你们聊得可真够热闹啊。\x02\x03",

            "#2804F嗯，你们都是些年轻人，\x01",
            "就多亲近一下吧。\x02\x03",

            "#2800F已经到了约好的时间，\x01",
            "我差不多也该出发了。\x02\x03",

            "贝尔，稍后就带他们\x01",
            "去终端室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5F2C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_5F2C)
    Sleep(150)

    def lambda_5F3C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5F3C)
    Sleep(50)

    def lambda_5F4C():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5F4C)

    def lambda_5F59():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F59)
    Sleep(50)
    TurnDirection(0x103, 0x8, 500)

    #C0210
    ChrTalk(
        0x9,
        (
            "#6P#2905F终端室……\x01",
            "这是怎么一回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#2800F关于具体情况，你就问他们好了。\x02\x03",

            "#2809F那么，失陪了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5FDC():

        label("loc_5FDC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5FDC")

    QueueWorkItem2(0x102, 2, lambda_5FDC)

    def lambda_5FEE():

        label("loc_5FEE")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5FEE")

    QueueWorkItem2(0x9, 2, lambda_5FEE)

    def lambda_6000():

        label("loc_6000")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6000")

    QueueWorkItem2(0x103, 2, lambda_6000)

    def lambda_6012():

        label("loc_6012")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6012")

    QueueWorkItem2(0x104, 2, lambda_6012)

    def lambda_6024():

        label("loc_6024")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6024")

    QueueWorkItem2(0x101, 2, lambda_6024)
    OP_68(55000, 1100, 121300, 3000)

    def lambda_6047():
        OP_95(0xFE, 55000, 0, 118000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6047)
    WaitChrThread(0x8, 1)

    def lambda_6065():
        OP_95(0xFE, 55000, 0, 115000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6065)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_6088():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6088)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    ClearChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x101, 0x2)
    OP_6F(0x1)
    Sound(104, 0, 100, 0)

    #C0212
    ChrTalk(
        0x102,
        "#6P#0105F啊……\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#6P#0206F逃跑了呢……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        "#5P#2906F父亲可真是的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(55000, 1100, 125300, 0)
    MoveCamera(55, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
    TurnDirection(0x101, 0x9, 500)

    #C0215
    ChrTalk(
        0x101,
        (
            "#6P#0012F那、那么，要是方便的话，\x01",
            "就麻烦您快点带我们去终……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 700)

    #C0216
    ChrTalk(
        0x9,
        "#11P#2901F我的话还没说完呢！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 700)
    Sleep(300)

    #C0217
    ChrTalk(
        0x9,
        (
            "#2906F#6P那边的那个红毛也是一样，\x01",
            "竟然穿得这么花哨……\x02\x03",

            "#2901F你的身材明明很不错，\x01",
            "应该穿套正经的西装才对！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_623F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_623F)
    Sleep(150)

    def lambda_624F():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_624F)
    Sleep(50)
    TurnDirection(0x103, 0x9, 500)

    #C0218
    ChrTalk(
        0x104,
        (
            "#0305F#11P在、在说我吗？\x02\x03",

            "#0309F呀～但我从骨子里\x01",
            "就是个游手好闲的人啦。\x02\x03",

            "#0302F啊，而且我也不会像那家伙一样，\x01",
            "大半夜跑到楼顶上，悄悄的和某位\x01",
            "同事大小姐在甜蜜美好的氛围里谈心。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 700)
    OP_82(0xC8, 0x0, 0xBB8, 0x190)

    #C0219
    ChrTalk(
        0x9,
        "#11P#2910F#4S什、什么～！？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        "#6P#0011F兰迪，你……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 700)

    #C0221
    ChrTalk(
        0x102,
        (
            "#12P#0101F请、请不要随便说出那种\x01",
            "容易招人误解的话啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0222
    ChrTalk(
        0x103,
        (
            "#6P#0204F但也未必\x01",
            "就是误解吧……\x02\x03",

            "#0202F艾莉前辈在那之后\x01",
            "好像变得有精神了很多。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6460():
        TurnDirection(0xFE, 0x103, 700)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6460)
    Sleep(100)
    TurnDirection(0x101, 0x103, 700)

    #C0223
    ChrTalk(
        0x102,
        "#11P#0112F缇、缇欧……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#5P#0013F啊啊，真是的！竟然连\x01",
            "缇欧都在一旁煽风点火！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64CD():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_64CD)
    WaitChrThread(0x9, 1)
    Sound(804, 0, 100, 0)
    TurnDirection(0x101, 0x9, 700)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6507():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6507)

    def lambda_6520():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6520)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    #C0225
    ChrTalk(
        0x9,
        (
            "#11P#2909F呵呵……\x01",
            "你是叫罗伊德吧……？\x02\x03",

            "关于这件事情，能不能\x01",
            "再和我详细说说呢……？\x02\x03",

            "#2910F你对我的艾莉到底做出了\x01",
            "什么不知廉耻的事情……！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#6P#0012F不，什么都没做啊！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        "#11P#0113F………………………………\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x101,
        (
            "#6P#0011F话说，艾莉你为什么\x01",
            "完全不辩解啊！？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(55100, 1200, 124000, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(19500, 0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x4)
    SetChrPos(0x101, 54200, 30, 125400, 135)
    SetChrPos(0x102, 53900, 30, 124000, 90)
    SetChrPos(0x103, 52500, 30, 123400, 90)
    SetChrPos(0x104, 52400, 30, 124400, 90)
    SetChrPos(0x9, 56200, 0, 124000, 270)
    SetCameraDistance(20000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0229
    ChrTalk(
        0x9,
        (
            "#2903F#11P──原来如此，\x01",
            "情况我已经明白了。\x02\x03",

            "#2900F那么，我现在就带你们\x01",
            "去终端室，这样就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        "#6P#0100F咦，你愿意带我们去了吗？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        (
            "#2906F#11P那还用说，我当然不会\x01",
            "拒绝艾莉的请求啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x9)

    #C0232
    ChrTalk(
        0x101,
        (
            "#0012F那个……\x01",
            "刚才的误解算是已经澄清了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#2903F#11P哼，算了，就先这样吧。\x02\x03",

            "特别任务支援科……\x01",
            "我也一直很在意\x01",
            "这个部门的实力到底如何。\x02\x03",

            "#2902F而你是否有资格当艾莉的同事……\x01",
            "今后就用行动来证明给我看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#0011F这、这样啊……\x01",
            "（为什么只针对我一个呢……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#6P#0302F（哎呀，好像完全\x01",
            "  被盯上了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        "#6P#0204F（……令人同情。）\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#6P#0106F真是的……\x01",
            "贝尔，适可而止吧。\x02\x03",

            "#0101F你不是要带我们去终端室吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 500)

    #C0238
    ChrTalk(
        0x9,
        (
            "#2904F#11P当然要带你们去啊。\x02\x03",

            "#2900F终端室就在ＩＢＣ大厦\x01",
            "的地下五层。\x02\x03",

            "好了，我们去坐导力梯吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_6A44():

        label("loc_6A44")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6A44")

    QueueWorkItem2(0x102, 2, lambda_6A44)

    def lambda_6A56():

        label("loc_6A56")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6A56")

    QueueWorkItem2(0x103, 2, lambda_6A56)

    def lambda_6A68():

        label("loc_6A68")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6A68")

    QueueWorkItem2(0x104, 2, lambda_6A68)

    def lambda_6A7A():

        label("loc_6A7A")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_6A7A")

    QueueWorkItem2(0x101, 2, lambda_6A7A)
    OP_68(55100, 1200, 120000, 3000)

    def lambda_6A9D():
        OP_95(0xFE, 55000, 0, 117500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6A9D)
    WaitChrThread(0x9, 1)

    def lambda_6ABB():
        OP_95(0xFE, 55000, 0, 115000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6ABB)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_6ADE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6ADE)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    ClearChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x101, 0x2)
    Sleep(500)
    Fade(500)
    OP_68(53890, 1200, 124430, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0239
    ChrTalk(
        0x101,
        "#0006F#5P……呼，真是个很厉害的人啊。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#5P#0105F那个，其实她并没有恶意哦。\x02\x03",

            "#0106F只是有点，那个，该说是性格强势，\x01",
            "还是行动力过剩呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#0300F#5P话说回来，那位大叔也好，这位小姐也好，\x01",
            "性格都那么强势，真不愧是父女。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#0204F#5P真不愧是天下闻名的ＩＢＣ\x01",
            "集团的领导者啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    AddParty(0x37, 0xFF, 0xFF)
    OP_68(53000, 1500, 44200, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 53000, 0, 44200, 180)
    SetChrPos(0x1, 53000, 0, 44200, 180)
    SetChrPos(0x2, 53000, 0, 44200, 180)
    SetChrPos(0x3, 53000, 0, 44200, 180)
    SetChrPos(0x4, 53000, 0, 44200, 180)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0x82, 5)
    ClearScenarioFlags(0x0, 3)
    OP_29(0x43, 0x1, 0x3)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_2B3F end

    def Function_18_6D76(): pass

    label("Function_18_6D76")


    def lambda_6D7B():
        OP_95(0xFE, 56300, 0, 124000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D7B)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x104, 500)
    Sleep(500)

    #C0243
    ChrTalk(
        0x9,
        "#2901F嗯……\x02",
    )

    CloseMessageWindow()

    def lambda_6DB5():
        OP_95(0xFE, 55200, 0, 122900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6DB5)
    WaitChrThread(0x9, 1)

    def lambda_6DD3():
        OP_95(0xFE, 53400, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6DD3)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x103, 500)
    Sleep(500)

    #C0244
    ChrTalk(
        0x9,
        "#5P#2902F……原来如此……\x02",
    )

    CloseMessageWindow()

    def lambda_6E1A():
        OP_95(0xFE, 52600, 0, 125600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6E1A)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    Return()

    # Function_18_6D76 end

    def Function_19_6E3E(): pass

    label("Function_19_6E3E")

    EndChrThread(0x8, 0x2)

    def lambda_6E47():
        OP_95(0xFE, 56000, 0, 130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6E47)
    WaitChrThread(0x8, 1)

    def lambda_6E65():
        OP_95(0xFE, 58600, 0, 130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6E65)
    WaitChrThread(0x8, 1)

    def lambda_6E83():
        OP_95(0xFE, 58600, 0, 127500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6E83)
    WaitChrThread(0x8, 1)

    def lambda_6EA1():
        OP_95(0xFE, 58000, 0, 126900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6EA1)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x9, 500)
    Return()

    # Function_19_6E3E end

    def Function_20_6EC2(): pass

    label("Function_20_6EC2")

    EventBegin(0x0)
    OP_4B(0x9, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(53290, 1430, 123860, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16630, 0)
    SetChrPos(0x101, 54450, 30, 123460, 0)
    SetChrPos(0x102, 53320, 30, 123460, 0)
    SetChrPos(0x103, 53320, 30, 121930, 0)
    SetChrPos(0x104, 54450, 30, 121930, 0)
    SetChrPos(0x9, 54010, 30, 125480, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0245
    ChrTalk(
        0x9,
        (
            "#5P#2901F真是的，我受够了……\x01",
            "都是因为那个『鲁巴彻』，\x01",
            "我们这边还要继续开会！\x02\x03",

            "#2903F袭击事件给股价造成的负面影响，\x01",
            "似乎有希望抑制住，但是……\x02\x03",

            "#2901F我还是觉得之后应该\x01",
            "向他们索要赔偿金。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        "#12P#0103F你们还是一如既往地辛苦呢……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        (
            "#5P#2900F因为爸爸外出不在，所以我们\x01",
            "比平时还要辛苦，应该这么说。\x02\x03",

            "#2905F……先不说这个了。\x01",
            "艾莉，来这里有什么事吗？\x02\x03",

            "看起来，你好像也不是\x01",
            "为了私事而来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，其实我有些事情\x01",
            "想问问贝尔。\x02\x03",

            "卡拉小姐今天应该\x01",
            "来过这边吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "#5P#2905F卡拉小姐……？\x02\x03",

            "#2900F是啊，她不久之前\x01",
            "是来找过我呢。\x02\x03",

            "#2904F因为在社交界有一定往来，\x01",
            "所以我和她也算是认识。\x02\x03",

            "她说今天有什么紧急情况…………\x02\x03",

            "#2900F所以就直接来找我了，\x01",
            "然后还提前取出了自己的\x01",
            "定期存款呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        "#12P#0303F果然如此啊。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#11P#0005F……不过，为什么还要\x01",
            "特意来找玛丽亚贝尔小姐呢？\x02\x03",

            "这种业务只要到柜台就可以直接办理了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "#5P#2903F因为她要取出的款项数额巨大啊。\x02\x03",

            "#2900F在一般情况下，是需要固定手续的，\x01",
            "但她似乎很急，说今天无论如何也要取出。\x02\x03",

            "虽然无法将具体数额透露给你们……\x01",
            "但大致说来，\x01",
            "有几十万米拉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#12P#0205F那可真是一笔巨款呢……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        (
            "#12P#0103F其实，卡拉小姐她\x01",
            "离家出走了……\x01",
            "我们正在追寻她的行踪。\x02\x03",

            "#0100F贝尔，你有没有什么线索呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        (
            "#5P#2905F哎呀，原来是这样啊。\x02\x03",

            "#2903F让我想想……从取款金额来看，\x01",
            "她也许是要去国外吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0256
    ChrTalk(
        0x101,
        "#11P#0000F是有这个可能啊……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x103,
        (
            "#12P#0200F但她究竟要去\x01",
            "什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Sleep(300)

    #C0258
    ChrTalk(
        0x9,
        (
            "#5P#2903F这么一说……\x02\x03",

            "她曾经和女仆说过，\x01",
            "想要到格兰赛尔去\x01",
            "参观呢。\x02\x03",

            "#2900F好像还说过要女仆去酒店订房\x01",
            "之类的话呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#11P#0005F格兰赛尔……？\x01",
            "那是利贝尔王国的王都吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        "#12P#0301F……是利贝尔那边吗？！\x02",
    )

    CloseMessageWindow()

    def lambda_75CE():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75CE)

    def lambda_75DB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75DB)

    def lambda_75E8():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_75E8)

    def lambda_75F5():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_75F5)
    Sleep(800)

    #C0261
    ChrTalk(
        0x103,
        (
            "#12P#0200F那样一来，我们就要去空港了……\x02\x03",

            "应该还能赶得上\x01",
            "国际航班的起飞时间，\x01",
            "快去询问一下票务员吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        "#6P#0101F嗯，我们快点出发吧！\x02",
    )

    CloseMessageWindow()

    def lambda_7692():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7692)

    def lambda_769F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_769F)

    def lambda_76AC():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_76AC)

    def lambda_76B9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_76B9)
    Sleep(300)

    #C0263
    ChrTalk(
        0x101,
        (
            "#11P#0001F真是给您添麻烦了，\x01",
            "感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        "#12P#0101F下次见了，贝尔！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        "#5P#2905F啊，好……\x02",
    )

    CloseMessageWindow()
    OP_68(55390, 1400, 119040, 1600)
    SetCameraDistance(17100, 1600)
    BeginChrThread(0x104, 0, 0, 21)
    Sleep(220)
    BeginChrThread(0x103, 0, 0, 21)
    Sleep(180)
    BeginChrThread(0x101, 0, 0, 21)
    Sleep(240)
    BeginChrThread(0x102, 0, 0, 21)
    Sleep(200)
    Sound(103, 0, 100, 0)
    Sleep(1500)
    Sound(104, 0, 100, 0)
    Sleep(1500)
    Fade(500)
    OP_68(53680, 1430, 124740, 0)
    OP_0D()

    #C0266
    ChrTalk(
        0x9,
        "#5P#2903F哎呀哎呀，真是匆匆忙忙呢。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(52870, 1500, 44710, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 52870, 0, 44710, 180)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_4C(0x9, 0xFF)
    OP_29(0x2D, 0x1, 0x8)
    SetScenarioFlags(0x0, 5)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_6EC2 end

    def Function_21_7847(): pass

    label("Function_21_7847")

    OP_95(0xFE, 55000, 0, 118710, 5000, 0x1)

    def lambda_7860():
        OP_95(0xFE, 55000, 0, 114830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7860)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_21_7847 end

    def Function_22_7884(): pass

    label("Function_22_7884")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门上着锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7969")

    #C0268
    ChrTalk(
        0x102,
        "#0102F（这里是……贝尔的房间呢。）\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#0005F艾莉，怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        (
            "#0104F不，没什么。\x02\x03",

            "#0100F罗伊德，总裁室是正面的房间哦。\x01",
            "我们快点过去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        "#0000F啊，知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_7969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A4E")

    #C0272
    ChrTalk(
        0x138,
        (
            "#2905F啊，那里是\x01",
            "我的房间哦。\x02\x03",

            "#2902F如果愿意，\x01",
            "进去喝杯茶如何？\x01",
            "我会好好招待你们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，现在还是算了……\x02\x03",

            "#0000F能不能先带我们\x01",
            "去终端室呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x138,
        (
            "#2904F嗯，没问题。\x02\x03",

            "#2900F那我们就去坐\x01",
            "导力梯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A4E")

    SetScenarioFlags(0x0, 3)

    label("loc_7A51")

    TalkEnd(0xFF)
    Return()

    # Function_22_7884 end

    def Function_23_7A55(): pass

    label("Function_23_7A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_END)), "loc_7AFF")
    TalkBegin(0xFF)
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着栩栩如生，几乎像是\x01",
            "有生命般的精致人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AF7")

    #C0276
    ChrTalk(
        0x101,
        (
            "#0003F（万一不小心碰坏了，可就……\x01",
            "  还是不要随便乱动吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7AF7")

    TalkEnd(0xFF)
    Jump("loc_7B02")

    label("loc_7AFF")

    Call(0, 7)

    label("loc_7B02")

    Jump("loc_7D7A")

    label("loc_7B07")

    TalkBegin(0xFF)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "放置着栩栩如生，几乎像是\x01",
            "有生命般的精致人偶。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D27")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0005F什、什么……！？\x02\x03",

            "#0003F这……太惊人了，\x01",
            "真的只是人偶吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#0100F这是罗赞贝尔克工房制造的人偶哦。\x02\x03",

            "是贝尔的收藏品之一，\x01",
            "她好像尤其喜欢这两个呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#0205F这就是罗赞贝尔克工房所制造的……\x01",
            "连皮肤看上去都如此光滑水灵，\x01",
            "怎么看都不像是人偶呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x104,
        "#0303F真是精巧得让人难以置信啊……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#0003F之前听说这些人偶的价格相当昂贵，\x01",
            "现在看来，的确是物有所值……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 3)

    label("loc_7D27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D77")

    #C0283
    ChrTalk(
        0x101,
        (
            "#0003F（万一不小心碰坏的话，可就……\x01",
            "  还是不要随便乱动吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_7D77")

    TalkEnd(0xFF)

    label("loc_7D7A")

    Return()

    # Function_23_7A55 end

    SaveToFile()

Try(main)
