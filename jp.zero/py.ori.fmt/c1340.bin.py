from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ディーター総裁",         # 1
        "マリアベル",             # 2
        "バレッタ取締役",         # 3
        "人形",                   # 4
        "人形",                   # 5
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
        "Function_6_F43",          # 06, 6
        "Function_7_1EC6",         # 07, 7
        "Function_8_2548",         # 08, 8
        "Function_9_2567",         # 09, 9
        "Function_10_2589",        # 0A, 10
        "Function_11_25A8",        # 0B, 11
        "Function_12_25C0",        # 0C, 12
        "Function_13_25DF",        # 0D, 13
        "Function_14_25FE",        # 0E, 14
        "Function_15_2619",        # 0F, 15
        "Function_16_2866",        # 10, 16
        "Function_17_2D49",        # 11, 17
        "Function_18_734A",        # 12, 18
        "Function_19_7414",        # 13, 19
        "Function_20_7498",        # 14, 20
        "Function_21_7E99",        # 15, 21
        "Function_22_7ED6",        # 16, 22
        "Function_23_810B",        # 17, 23
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7D1")
    TalkBegin(0x8)
    OP_4B(0xA, 0xFF)

    #C0001
    ChrTalk(
        0x8,
        (
            "#2803Fああ、後の事は\x01",
            "お前とマリアベルに任せる。\x02\x03",

            "#2800F私はこれから\x01",
            "市長と会食があるんだ。\x01",
            "すまないが行かせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        "はっ、お任せ下さいませ……！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    TalkEnd(0x8)
    Jump("loc_F42")

    label("loc_7D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AD5")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_86E")
    Jump("loc_8B8")

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_88E")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8")

    label("loc_88E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AE")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B8")

    label("loc_8AE")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B8")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_976")

    #C0003
    ChrTalk(
        0x8,
        (
            "#2800F実は午後から\x01",
            "出張を入れていてね。\x02\x03",

            "今のうちに残務を\x01",
            "片付けておく必要があるんだ。\x02\x03",

            "#2806Fお陰で朝から会議続きさ。\x01",
            "やれやれだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC9")

    label("loc_976")


    #C0004
    ChrTalk(
        0x8,
        "#2800Fやあ諸君か。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#0105Fすみません、\x01",
            "お仕事中みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#2800F見ての通りさ。\x01",
            "朝から会議続きでね。\x02\x03",

            "#2806F私だってクロスベル人だ、\x01",
            "パレードくらい\x01",
            "見に行きたいんだがねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0000Fあはは……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#2804Fま、冗談だ。\x02\x03",

            "#2800Fエリィ、諸君。\x01",
            "そちらも仕事を\x01",
            "頑張ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#0100Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AC9")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Jump("loc_F42")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_F42")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B72")
    Jump("loc_BBC")

    label("loc_B72")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B92")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BBC")

    label("loc_B92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB2")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BBC")

    label("loc_BB2")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BBC")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E38")

    #C0010
    ChrTalk(
        0x8,
        (
            "#2800Fやあ諸君、仕事は順調かね？\x02\x03",

            "#2809Fハハハ、何か用事があれば\x01",
            "いつでも訪ねに来てくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#0306Fなんつー爽やかな……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0105Fおじさま、記念祭の間は\x01",
            "特にお忙しいのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#2804Fハハ、確かに会談やパーティが\x01",
            "立て込んではいるんだが。\x02\x03",

            "#2800F君達ならいつでも歓迎だ。\x01",
            "……なんなら、私と一緒に\x01",
            "明日の会談に出席してみないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0012Fさ、さすがにそれは……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#0206F謹んで辞退させていただきます。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#2806Fおやそうか……それは残念。\x02\x03",

            "#2809Fハハハ、飛び込みでも構わないから\x01",
            "考えておいてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0106F（おじさまはやっぱり\x01",
            "  スケールが違うわね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F3B")

    label("loc_E38")


    #C0018
    ChrTalk(
        0x8,
        (
            "#2803F記念祭中は私も仕事が\x01",
            "立て込んではいるんだが……\x02\x03",

            "#2800Fハハ、君達ならいつでも歓迎だ。\x01",
            "オトナの都合など気にせず\x01",
            "アポなしで来てくれて構わんよ。\x02\x03",

            "#2800Fそれより……君たちの方も\x01",
            "記念祭の間は仕事も大変だろう。\x02\x03",

            "無理をしない程度に\x01",
            "頑張ってくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F3B")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)

    label("loc_F42")

    Return()

    # Function_5_716 end

    def Function_6_F43(): pass

    label("Function_6_F43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F65")
    Call(0, 20)
    Return()

    label("loc_F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_108F")
    TalkBegin(0xFE)

    #C0019
    ChrTalk(
        0x9,
        (
            "#2900Fカーラさんはメイドに向かって\x01",
            "グランセル見物がどうのと\x01",
            "言ってましたわね。\x02\x03",

            "#2903F家出目的なら\x01",
            "わたくしの前で言いふらすのも\x01",
            "どうかと思いますけれど……\x02\x03",

            "#2900Fま、わたくしも今日は忙しいのだから\x01",
            "気にも留めていませんでしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0003Fお、お忙しい所を\x01",
            "お邪魔しました。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_108F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_12A7")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1180")

    #C0021
    ChrTalk(
        0x9,
        (
            "#2901Fそれにしても……\x01",
            "ハルトマン議長は一体、\x01",
            "何をしているんですの？\x02\x03",

            "#2903F付き合いのある連中が\x01",
            "あんな事をしでかしたのに\x01",
            "ロクに動いてなさそうですし……\x02\x03",

            "#2910Fいくら議会中とはいえ、\x01",
            "あまりに呑気すぎますわね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129F")

    label("loc_1180")


    #C0022
    ChrTalk(
        0x9,
        (
            "#2906Fふぅ、襲撃事件の株価への影響は\x01",
            "何とか喰い止められそうですわね。\x02\x03",

            "#2903Fでも、このまま抗争が続けば\x01",
            "金融・貿易市場にどんな悪影響を\x01",
            "与えるか分かりませんわ。\x02\x03",

            "#2901F警察にはもう少し\x01",
            "頑張って欲しいですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#0001Fそ、それはもちろん！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#0104F全力を尽くさせてもらうわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_129F")

    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_12A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1537")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_132F")

    #C0025
    ChrTalk(
        0x9,
        (
            "#2903Fまったく、お父様の\x01",
            "留守中に馬鹿げた騒ぎを……\x02\x03",

            "#2910F《ルバーチェ》には\x01",
            "ほとほと呆れ果てましたわ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152F")

    label("loc_132F")


    #C0026
    ChrTalk(
        0x9,
        (
            "#2910Fまったくもう……！\x01",
            "馬鹿な事をしてくれますわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#0005Fマリアベルさん……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0101Fその様子だと……\x01",
            "もう知ってるみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#2901F当然ですわ……！\x01",
            "目と鼻の先の出来事ですから！\x02\x03",

            "#2903FよくもＩＢＣビルの近くで\x01",
            "銃撃戦などを……\x02\x03",

            "#2910Fおのれ《ルバーチェ》……\x01",
            "株価に影響が出たら許しませんわよ！\x02",
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
        "#0006Fそういう事ですか……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#0106Fま、まあベルの立場なら\x01",
            "当然といえば当然の心配かしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_152F")

    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_1537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_180D")
    TalkBegin(0xFE)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1601")

    #C0032
    ChrTalk(
        0xA,
        (
            "そういえば、お嬢様。\x01",
            "本日は午後から……？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#2904Fええ、商談で出かけますわ。\x02\x03",

            "#2900F夜も私用で戻りませんから\x01",
            "後はよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xA,
        "ええ、お任せください。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1801")

    label("loc_1601")


    #C0035
    ChrTalk(
        0x9,
        (
            "#2904Fそうですわね、こちらの書類は\x01",
            "わたくしの方で処理しておきます。\x02\x03",

            "#2900F銀行部門、投資部門の方は\x01",
            "引き続きお願いしますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "ふむ、では次の重役会議で\x01",
            "報告し合うといたしましょう。\x02",
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
            "#2905Fあら、お父様なら\x01",
            "また出張ですわよ。\x02\x03",

            "#2906F残りの仕事を全て押し付けて……\x01",
            "いつもながら見事な手際ですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#0000Fはは……そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#2900Fええ、他人に仕事を\x01",
            "押し付けるのが大得意な人ですから。\x02\x03",

            "#2906Fお陰でわたくしも\x01",
            "随分慣れてしまいましたわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x0, 0x0, 0x41EB0, 0x0, 0x0)
    SetScenarioFlags(0x0, 1)

    label("loc_1801")

    OP_4C(0xA, 0xFF)
    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_180D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_198F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18D2")
    OP_4B(0xA, 0xFF)

    #C0040
    ChrTalk(
        0x9,
        (
            "#2900Fそうですわね、そちらの事業は\x01",
            "わたくしの方で受け持ちますわ。\x02\x03",

            "報告はバレッタさんに行う\x01",
            "ということでよろしくて？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        (
            "ええ、では\x01",
            "そのようにお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_1987")

    label("loc_18D2")


    #C0042
    ChrTalk(
        0x9,
        (
            "#2900FＩＢＣの手がけている事業は\x01",
            "常に２０を下りませんわ。\x02\x03",

            "企画書や報告書だけでこの有様……\x02\x03",

            "#2906Fふう、お父様のサポートも\x01",
            "楽ではありませんわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0x0, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)

    label("loc_1987")

    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_198F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DFA")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A2C")
    Jump("loc_1A76")

    label("loc_1A2C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1A4C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A76")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A6C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A76")

    label("loc_1A6C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A76")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1BD6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B1F")

    #C0043
    ChrTalk(
        0x9,
        (
            "#2904Fお父様もようやく\x01",
            "戻ったことですし……\x02\x03",

            "#2902Fエリィ、夕方からでもいいから\x01",
            "是非いらっしゃいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA2")

    label("loc_1B1F")


    #C0044
    ChrTalk(
        0x9,
        (
            "#2904F今日のパーティは\x01",
            "わたくしの身内だけでやる\x01",
            "ささやかな物ですの。\x02\x03",

            "#2902Fエリィ、夕方からでもいいから\x01",
            "是非いらっしゃいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA2")


    #C0045
    ChrTalk(
        0x102,
        (
            "#0102Fうーん……\x01",
            "仕事の都合が付いたらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEE")

    label("loc_1BD6")


    #C0046
    ChrTalk(
        0x9,
        (
            "#2909Fあらエリィ、これから\x01",
            "パーティに来ませんこと？\x02\x03",

            "#2902F午後からになりますけど、\x01",
            "絶対に退屈させませんわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#0106Fベルったら……昨日祝賀会に\x01",
            "付き合ったばかりじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "#2905Fあら、今日のパーティは\x01",
            "わたくしの身内だけでやる\x01",
            "ささやかな物ですのよ。\x02\x03",

            "#2901Fエリィを招かないでどうしますの。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0012Fあの、とりあえず\x01",
            "支援課は仕事があるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        "#2904Fじゃ、休みなさい。\x02",
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
        "#0309F（相変わらずの女王様だねぇ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1DEE")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_END)), "loc_1EC2")
    TalkBegin(0xFE)

    #C0052
    ChrTalk(
        0x9,
        (
            "#2904Fそれはそうと、ことの顛末が\x01",
            "分かったら教えてください。\x02\x03",

            "#2902Fわたくしも興味がありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#0000Fえ、ええ。\x01",
            "一通り解決した暁には。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        "#0100Fまた来るわね、ベル。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_1EC5")

    label("loc_1EC2")

    Call(0, 7)

    label("loc_1EC5")

    Return()

    # Function_6_F43 end

    def Function_7_1EC6(): pass

    label("Function_7_1EC6")

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
            "#2902F#11Pあら、わたくしの\x01",
            "プライベートルームへようこそ。\x02\x03",

            "#2904Fそちらのハレンチな\x01",
            "誰かさん以外は歓迎しますわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        "#0006F#6P（まだ目を付けられてる……）\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#0300F#6Pにしても、高そうな絵画とか\x01",
            "美術品が飾ってあるッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0205F#6Pいずれも著名な芸術家の\x01",
            "作品みたいですが……\x02",
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
            "#0005F#6Pな……！？\x02\x03",

            "#0001Fあの……失礼ですが\x01",
            "その後ろにあるのは……？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0xB4, 0x1F4)

    #C0060
    ChrTalk(
        0x102,
        (
            "#0109F#5Pあれがローゼンベルク工房製の人形よ。\x02\x03",

            "#0102Fまるで生きているみたいでしょう？\x01",
            "……ベルはローゼンベルクの\x01",
            "コレクターなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "#2904F#11Pフフ、この２体は\x01",
            "特に気に入っている子達ですわ。\x02\x03",

            "#2902F宜しかったら近くで\x01",
            "ご覧になってはどうかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#0005F#6Pいいんですか……？\x02",
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
            "#0202F#6Pこれがローゼンベルクの人形……\x01",
            "肌もきめ細かくて\x01",
            "とても人形には見えません……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0302F#6Pとんでもない精巧ぶりだな……\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0002F#6P凄い……\x02\x03",

            "#0004F相当値段がするって聞いたけど\x01",
            "これは頷ける気がするな……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "#2904F#11P触ってみても構いませんわよ。\x02\x03",

            "#2902Fただし、傷でも付けたら\x01",
            "弁償してもらいますけれど。\x02",
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
        "#0106F#5Pベルったら……\x02",
    )

    CloseMessageWindow()

    def lambda_2474():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2474)
    Sleep(50)

    def lambda_2484():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2484)
    Sleep(60)

    def lambda_2494():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2494)
    WaitChrThread(0x101, 1)

    #C0068
    ChrTalk(
        0x101,
        (
            "#0012F#5Pそんな難しい事\x01",
            "言わないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#0211F#5P怖くてとても触れません。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        "#2909F#11Pうふふ、冗談ですわ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168730, 0, 120050, 90)
    SetChrPos(0x9, 170830, 0, 120150, 90)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0xB8, 3)
    EventEnd(0x5)
    Return()

    # Function_7_1EC6 end

    def Function_8_2548(): pass

    label("Function_8_2548")

    OP_93(0x103, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(500)
    OP_93(0x103, 0x5A, 0x1F4)
    Sleep(500)
    Return()

    # Function_8_2548 end

    def Function_9_2567(): pass

    label("Function_9_2567")

    Sleep(300)
    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(500)
    OP_93(0x104, 0x5A, 0x1F4)
    Sleep(500)
    Return()

    # Function_9_2567 end

    def Function_10_2589(): pass

    label("Function_10_2589")

    OP_95(0x9, 171500, 0, 118600, 2000, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(500)
    Return()

    # Function_10_2589 end

    def Function_11_25A8(): pass

    label("Function_11_25A8")

    Sleep(500)
    OP_95(0x101, 170930, 0, 119600, 2000, 0x0)
    Return()

    # Function_11_25A8 end

    def Function_12_25C0(): pass

    label("Function_12_25C0")

    Sleep(600)
    OP_95(0x102, 171100, 0, 121670, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_12_25C0 end

    def Function_13_25DF(): pass

    label("Function_13_25DF")

    Sleep(800)
    OP_95(0x103, 171000, 0, 120710, 2000, 0x0)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_13_25DF end

    def Function_14_25FE(): pass

    label("Function_14_25FE")

    Sleep(1000)
    OP_95(0x104, 170010, 0, 121040, 2000, 0x0)
    Sleep(500)
    Return()

    # Function_14_25FE end

    def Function_15_2619(): pass

    label("Function_15_2619")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26B0")

    #C0071
    ChrTalk(
        0xFE,
        (
            "総裁がお留守の間は\x01",
            "我々と重役たちで切り盛りせねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "マリアベルお嬢様にも負担を掛けるが\x01",
            "どうかご容赦願いたいものだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_271E")

    #C0073
    ChrTalk(
        0xFE,
        (
            "記念祭だからこそ\x01",
            "総裁は大変お忙しい……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "……我らも一丸となって\x01",
            "お支えせねばならんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_278C")

    #C0075
    ChrTalk(
        0xFE,
        "はっ、詳細はお手元の資料を。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "投資部門の成長率は\x01",
            "極めて高いのが特徴ですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2862")

    label("loc_278C")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0077
    ChrTalk(
        0xFE,
        (
            "む……保安部の者は\x01",
            "何をしておるのだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "……と思えば、\x01",
            "エリィ様のご同僚でしたか。\x01",
            "これは失礼。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "ですが今は会議中ですぞ。\x01",
            "お静かに願いたいものですな。\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0xA, 0x0, 0x0, 0x15F90, 0x0, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_2862")

    TalkEnd(0xFE)
    Return()

    # Function_15_2619 end

    def Function_16_2866(): pass

    label("Function_16_2866")

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

    def lambda_293F():
        OP_96(0xFE, 0xCF08, 0x0, 0x396C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_293F)

    def lambda_2959():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2959)
    Sleep(450)

    def lambda_296D():
        OP_96(0xFE, 0xCF08, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_296D)

    def lambda_2987():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2987)
    Sleep(450)

    def lambda_299B():
        OP_96(0xFE, 0xD3B8, 0x0, 0x396C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_299B)

    def lambda_29B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_29B5)
    Sleep(450)

    def lambda_29C9():
        OP_96(0xFE, 0xD3B8, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29C9)

    def lambda_29E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_29E3)
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

    def lambda_2A50():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A50)
    Sleep(50)

    def lambda_2A60():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2A60)

    #C0080
    ChrTalk(
        0x101,
        "#0005F#5Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(60000, 1000, 4300, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_2A9C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A9C)
    Sleep(100)

    def lambda_2AAC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AAC)
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
        "#0002F#5P凄いな……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#0302Fは～……いかにもミラが\x01",
            "かかってますって感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#0204F……下のフロアにある\x01",
            "エプスタイン財団の事務所には\x01",
            "何度か来たことはありますが……\x02\x03",

            "#0202F最上階は見晴らしも格別ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        "#0102Fそうね……\x02",
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
            "#0100F#5P総裁室は奥の突き当たりよ。\x02\x03",

            "お待たせしても悪いから\x01",
            "そろそろ行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2CE3():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CE3)
    Sleep(50)

    def lambda_2CF3():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2CF3)
    Sleep(50)
    TurnDirection(0x103, 0x102, 500)

    #C0086
    ChrTalk(
        0x101,
        "#11P#0000Fああ、そうだな。\x02",
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

    # Function_16_2866 end

    def Function_17_2D49(): pass

    label("Function_17_2D49")

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

    def lambda_2DC8():
        OP_95(0xFE, 52500, 0, 44900, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DC8)
    WaitChrThread(0x102, 1)
    Sleep(300)
    Sound(811, 0, 100, 0)
    Sleep(800)

    #C0087
    ChrTalk(
        0x102,
        "#11P#0102F──おじさま、エリィです。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 52500, 0, 47500, 0)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0088
    NpcTalk(
        0x8,
        "男性の声",
        "#5P#2Sおお、入りたまえ。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#11P#0104Fはい、失礼します。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x2)
    Sleep(300)

    def lambda_2EA7():
        OP_95(0xFE, 52500, 0, 45900, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EA7)
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

    def lambda_307F():
        OP_95(0xFE, 55000, 0, 125300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_307F)
    Sleep(300)

    def lambda_309C():
        OP_95(0xFE, 54100, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_309C)
    Sleep(200)

    def lambda_30B9():
        OP_95(0xFE, 55900, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30B9)
    Sleep(200)

    def lambda_30D6():
        OP_95(0xFE, 55000, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_30D6)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)

    #N0090
    NpcTalk(
        0x8,
        "スーツの男性",
        (
            "#5P#2800Fやあエリィ、久しぶりだ。\x02\x03",

            "半年ぶりくらいになるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#12P#0109Fはい、ディーターおじさまも\x01",
            "お元気そうで何よりです。\x02\x03",

            "#0100Fその、アポイントもなしに\x01",
            "お邪魔して申しわけありません。\x02",
        )
    )

    CloseMessageWindow()

    #N0092
    NpcTalk(
        0x8,
        "スーツの男性",
        (
            "#5P#2804Fハハ、水臭いことは\x01",
            "言わないでくれたまえ。\x02\x03",

            "#2800F君は友人の娘で\x01",
            "わが娘の幼なじみでもある。\x02\x03",

            "身内も同然じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        "#12P#0104F……ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #N0094
    NpcTalk(
        0x8,
        "スーツの男性",
        (
            "#5P#2800Fふむ、警察に入ったというのは\x01",
            "娘から聞いていたが……\x02\x03",

            "そちらの彼らが同僚なのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#12P#0100Fはい。\x01",
            "同じ《特務支援課》の仲間です。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    def lambda_3335():
        OP_96(0xFE, 0xDC50, 0x0, 0x1EC30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3335)
    WaitChrThread(0x102, 1)

    #C0096
    ChrTalk(
        0x101,
        (
            "#12P#0004F初めまして。\x01",
            "ロイド・バニングスといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        (
            "#4P#0300Fランディ・オルランド。\x01",
            "よろしくッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#4P#0204Fティオ・プラトーです。\x01",
            "初めまして……\x02",
        )
    )

    CloseMessageWindow()

    #N0099
    NpcTalk(
        0x8,
        "スーツの男性",
        (
            "#5P#2804Fふふ、クロスベルタイムズで\x01",
            "君たちの事は一応知っているよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("スーツの男性")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            "ＩＢＣの総裁を務める\x01",
            "ディーター・クロイスだ。\x02\x03",

            "ロイド君、ランディ君、ティオ君。\x02\x03",

            "どうか私のことは遠慮なく、\x01",
            "ディーターと呼んでくれたまえ。\x02",
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
        "#12P#0012Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x103,
        "#12P#0205F（今、歯が光ったような……）\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#12P#0309F（な、なんかムチャクチャ\x01",
            "  爽やかそうなオッサンだな。）\x02",
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
            "#5P#2801Fしかし、何やら警察の仕事で\x01",
            "相談したい事があるそうだが……\x02\x03",

            "#2800F一体、どうしたのかね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(300)

    #C0105
    ChrTalk(
        0x102,
        (
            "#0103Fはい、実は……\x02\x03",

            "#0101F私たち、ある事件を追って\x01",
            "捜査を進めているのですが──\x02",
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
            "#5P#2803F──なるほど。\x02\x03",

            "#2801Fその《銀#2Rイン#》とやらの導力メールが\x01",
            "ＩＢＣから君たちのオフィスに\x01",
            "送られてきたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#0106Fええ……そうなんです。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x103,
        (
            "#12P#0203F……恐らくこのビルにある\x01",
            "メイン端末からだと思います。\x02\x03",

            "#0200Fそれを操作して\x01",
            "送った可能性が高いかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#5P#2803Fふむ……\x02\x03",

            "このビルのセキュリティには\x01",
            "正直、自信を持っていてね。\x02\x03",

            "#2801F特に端末室があるフロアには\x01",
            "許可されている人間しか\x01",
            "入れないようにしているんだ。\x02\x03",

            "端末の操作も、権限がある者しか\x01",
            "出来ないようになっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#12P#0001F大変失礼ですが……\x01",
            "端末を操作できるスタッフの中に\x01",
            "不審な方はおられないでしょうか。\x02\x03",

            "最近入ったばかりとか、\x01",
            "何か後ろ暗いことがあるとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#5P#2803Fふむ……私の知る限り、\x01",
            "信頼できる者ばかりだけどね。\x02\x03",

            "#2800F──それより、ロイド君。\x02\x03",

            "他の可能性はあり得ないのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#5P#2804F例えば、そうだな……\x02\x03",

            "#2800F《銀》の正体がこの私で\x01",
            "君たちにメールを送ったとか。\x02",
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
        "#12P#4S#0011Fええっ！？\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        "#0307Fマ、マジかよ！？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0105Fお、おじさま……！？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#5P#2809Fハハ、例えばと言っただろう。\x02\x03",

            "#2800F伝説の刺客とやらの正体が\x01",
            "私みたいな立場の人間だったら\x01",
            "なかなか面白いとは思うが……\x02\x03",

            "さすがに現実はそこまで\x01",
            "奇想天外ではないだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#12P#0012Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#0106Fもう……\x01",
            "驚かせないでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x103,
        "#12P#0203Fお茶目な方ですね……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#5P#2809Fハッハッハッ、これは失敬。\x02\x03",

            "#2803Fしかし、考えてもみたまえ。\x02\x03",

            "#2801Fもし、そのメールを送ったのが\x01",
            "ここのスタッフだった場合……\x02\x03",

            "自分が犯人だと名乗るのも\x01",
            "等しい行為なのではないかな？\x02",
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
        "#0101Fあ……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        "#12P#0205F……確かにそうですね。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0301F逆にスタッフ以外の可能性を\x01",
            "考えた方がいいってことか……\x02",
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
            "#5P#0001F──ティオ。\x02\x03",

            "あのメールが、ＩＢＣの端末から\x01",
            "支援課に送られたという記録……\x02\x03",

            "それを偽装することは可能なのか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F5C():
        OP_93(0xFE, 0xBE, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3F5C)

    def lambda_3F69():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3F69)

    #C0126
    ChrTalk(
        0x103,
        (
            "#12P#0203Fそうですね……\x02\x03",

            "#0200F別の場所から、ＩＢＣの端末に\x01",
            "《ハッキング》を仕掛けた可能性は\x01",
            "ゼロではないかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#5P#0005F《ハッキング》……？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x104,
        "#0305Fなんだそりゃ……？\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#5P#0106F私も詳しくは知らないけど……\x02\x03",

            "#0100Fたしか、端末を守っている\x01",
            "セキュリティを解除することで\x01",
            "不正に操作する技術だったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#12P#0204Fおおむね合っています。\x02\x03",

            "導力ネットワークで\x01",
            "繋がっている端末同士であれば\x01",
            "原理的にはどこからでも可能です。\x02\x03",

            "#0200Fもっとも高度な知識と技術を\x01",
            "持っている必要がありますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#5P#2803Fちなみに、それを行う者を\x01",
            "《ハッカー》と言うらしい。\x02\x03",

            "#2801F導力ネットは、大陸全土でも\x01",
            "まだ限られた地域で試験的にしか\x01",
            "運用されていないんだが……\x02\x03",

            "早くもそういう事例が\x01",
            "報告されているらしいね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4246():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4246)
    Sleep(100)

    def lambda_4256():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4256)
    Sleep(100)

    def lambda_4266():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4266)
    Sleep(50)
    OP_93(0x104, 0x0, 0x1F4)

    #C0132
    ChrTalk(
        0x101,
        "#12P#0001Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x104,
        (
            "#0303Fってことは……\x02\x03",

            "#0301F《銀》ってのは刺客だけじゃなくて\x01",
            "《ハッカー》でもあるってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#0106F#5Pそこまでは断定できないけど……\x02\x03",

            "#0101F例のメールが、このビルの外部から\x01",
            "送られた可能性はあるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#5P#2803Fふむ、信頼するスタッフを\x01",
            "疑わずに済むのはいいんだが……\x02\x03",

            "#2801Fメイン端末が\x01",
            "ハッキングされたというのも\x01",
            "それはそれで由々しき問題だ。\x02",
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
            "#5P#2804Fよし、こうしよう。\x02\x03",

            "#2800F君たちが端末室に入れるよう\x01",
            "手配しようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#0105Fい、いいんですか？\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#5P#2800Fああ、メイン端末を調べれば\x01",
            "ハッキングの痕跡などが\x01",
            "残っているかもしれないし……\x02\x03",

            "スタッフも詰めているから\x01",
            "話を聞くこともできるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#12P#0002F……助かります。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            "#0104Fおじさま……\x01",
            "どうもありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#5P#2804Fいや、こちらにとっても\x01",
            "見過ごせない問題だからね。\x02\x03",

            "#2800Fふふ──しかしエリィ。\x02\x03",

            "なかなか充実した日々を\x01",
            "過ごしているようじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        "#0105Fえ……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#5P#2804F最初、君が警察に入ったと聞いて\x01",
            "少々疑問に思ったものだが……\x02\x03",

            "なるほど確かに\x01",
            "良い経験が出来そうな職場だ。\x02\x03",

            "#2800F私も改めて、応援させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0102Fおじさま……\x02\x03",

            "#0104Fそう言っていただけると\x01",
            "とても心強いです。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "#5P#2804Fふふ、それに君たちも……\x02\x03",

            "#2800F雑誌で読んだ以上に\x01",
            "可能性を感じさせてくれるね。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0147
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
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

    def lambda_47F6():
        OP_95(0xFE, 56000, 0, 131100, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47F6)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)

    #C0148
    ChrTalk(
        0x8,
        (
            "#2803F#11P……気付いているだろうが\x01",
            "このクロスベルという自治州は\x01",
            "非常に難しい場所だ。\x02\x03",

            "おそらくエリィなどは\x01",
            "それを痛感しているだろうが……\x02\x03",

            "#2801F一番、問題だと思われるのは\x01",
            "《正義》というものが完全に\x01",
            "形骸化してしまっていることだ。\x02",
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
        "#12P#0001F《正義》の形骸化……\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x102,
        (
            "#0101Fそれは……\x01",
            "どういう意味でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#2801F#11P《正義》は、ともすれば\x01",
            "“奇麗事”と同じ意味と\x01",
            "捉えられる場合も多いだろう。\x02\x03",

            "#2803F在り方も人それぞれ……\x01",
            "だから正義などは存在しないと\x01",
            "嘯#2Rうそぶ#く者もいるかもしれない。\x02\x03",

            "#2804Fだが、どんな形であれ……\x02\x03",

            "#2800F結局のところ、人は正義を\x01",
            "求めてしまう生き物なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#12P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x103,
        "#12P#0205F人が正義を求める生き物……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(300)

    #C0154
    ChrTalk(
        0x8,
        (
            "#2804F#5Pなぜなら《正義》というものは\x01",
            "人が社会を信頼する“根拠”だからだ。\x02\x03",

            "#2800Fもし、犯罪が起こった時に\x01",
            "それを法によって裁くという\x01",
            "《正義》が存在しなければ……\x02\x03",

            "多くの者は家に閉じこもり、\x01",
            "滅多に街に出ることはないだろう。\x02\x03",

            "そうなったら社会生活は\x01",
            "まともに成り立たなくなってしまう。\x02\x03",

            "#2803Fだが──このクロスベルでは\x01",
            "《正義》の形が曖昧でも\x01",
            "何とか成り立ってしまっている。\x02",
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
        "#0108F……それは………\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x8,
        (
            "#2801F#5P政治の腐敗や、マフィアの問題……\x02\x03",

            "それを警察が取り締まらなくても\x01",
            "経済的には恵まれているから\x01",
            "多くの市民は生活に困らない。\x02\x03",

            "結果的に、単純犯罪は少ないが、\x01",
            "目に見えない悪が蔓延#4Rはびこ#っていく……\x02\x03",

            "#2803Fだが、そんな中でも\x01",
            "やはり人は《正義》というものを\x01",
            "どこかに求めざるを得ない。\x02\x03",

            "どんな形であれ、社会を信頼できる\x01",
            "安心感を欲してしまうからだ。\x02\x03",

            "#2800F──だからクロスベルでは\x01",
            "ここまで遊撃士の人気が高いのだよ。\x02",
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
        "#12P#0005Fあ……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#12P#0204F『民間人の安全を最優先で守る』……\x02\x03",

            "#0202F確かに《正義の味方》って感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        (
            "#0306Fなるほどねぇ……\x02\x03",

            "#0301F他の国に比べて、妙に遊撃士が\x01",
            "持ち上げられてるとは思ったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        "#0106F……とても納得がいきます。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "#2803F#5Pだが、知っての通り、\x01",
            "遊撃士協会が行使できる正義は\x01",
            "あくまで限定的なものだ。\x02\x03",

            "この街の歪みを根本的に\x01",
            "解決することは不可能だろう。\x02\x03",

            "#2800Fだからこそ私は──\x01",
            "君たちに期待したいのだよ。\x02",
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
        "#12P#0011Fえっ……！？\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#0305F遊撃士の代わりに\x01",
            "悪を倒せってことッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#2804F#5Pはは、そんな単純なことを\x01",
            "言うつもりは毛頭ないよ。\x02\x03",

            "#2800F君たちが、君たちなりに\x01",
            "《正義》を追求している姿……\x02\x03",

            "それが目に見える形で市民に\x01",
            "示される事が重要だと思うのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#12P#0002Fあ……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#0104Fクロスベルにもまだ\x01",
            "《正義》が存在している……\x02\x03",

            "#0100Fそう信じられるきっかけを\x01",
            "市民に与えるという事ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "#2800F#5Pその通りだ。\x02\x03",

            "#2804Fふふ、その意味では\x01",
            "あのクロスベルタイムズの記事も\x01",
            "非常に有意義だと言えるだろう。\x02\x03",

            "まだまだ未熟な警察の若者が\x01",
            "時に失敗しながらも\x01",
            "《正義》を求めて奮闘する姿……\x02\x03",

            "#2800F面白がる者もいるだろうが\x01",
            "否定的な市民は少ないはずだ。\x02\x03",

            "温度差の違いはあっても……\x01",
            "皆、君たちに期待しているのだよ。\x02",
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
            "#5P#2804Fふふ、どうやら興にのって\x01",
            "一席ぶってしまったようだな。\x02\x03",

            "#2800F──本題に戻ろう。\x02\x03",

            "端末室への立入りを\x01",
            "君たちに許可する話だったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ……\x02\x03",

            "#0000Fはい、そうして頂ければ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#0100Fどちらに行けば\x01",
            "許可がいただけるでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "#5P#2801Fふむ、そうだな。\x02\x03",

            "私も端末室には入れるから\x01",
            "案内しても良かったんだが……\x02\x03",

            "#2803Fあいにくこの後、\x01",
            "色々予定が立て込んでいてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x102,
        (
            "#0106Fすみません。\x01",
            "本当にお忙しいところを……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#5P#2804Fなに、気にしないでくれ。\x02\x03",

            "#2800Fしかしそうだな……\x01",
            "ならばスタッフの誰かを\x01",
            "ここに呼ぶとしようか。\x02",
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
        "娘の声",
        "──その必要はありませんわ。\x02",
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

    def lambda_57C7():
        OP_95(0xFE, 55200, 0, 122800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_57C7)

    def lambda_57E1():
        OP_95(0xFE, 56000, 0, 128900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_57E1)
    OP_0D()
    Sound(104, 0, 100, 0)

    def lambda_5802():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5802)
    Sleep(150)

    def lambda_5812():

        label("loc_5812")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5812")

    QueueWorkItem2(0x103, 2, lambda_5812)
    Sleep(100)

    def lambda_5827():

        label("loc_5827")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5827")

    QueueWorkItem2(0x101, 2, lambda_5827)
    Sleep(100)

    def lambda_583C():

        label("loc_583C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_583C")

    QueueWorkItem2(0x104, 2, lambda_583C)
    WaitChrThread(0x9, 1)
    OP_6F(0x11)

    #C0177
    ChrTalk(
        0x101,
        "#5P#0005Fえ……\x02",
    )

    CloseMessageWindow()

    def lambda_5869():
        OP_95(0xFE, 55200, 0, 124200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5869)
    WaitChrThread(0x102, 1)

    #C0178
    ChrTalk(
        0x102,
        "#5P#0105Fベル……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 1)

    #C0179
    ChrTalk(
        0x8,
        "#2800Fおお、帰ってきたか。\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("金髪の娘")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            "お父様、ただ今戻りました。\x02\x03",

            "ふふっ……\x01",
            "エリィ、久しぶりですわね！\x02",
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

    def lambda_598A():
        OP_95(0xFE, 55200, 0, 123700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_598A)
    WaitChrThread(0x9, 1)

    def lambda_59A8():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59A8)
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
        "#0112Fちょ、ちょっと……\x02",
    )

    CloseMessageWindow()

    #N0182
    NpcTalk(
        0x9,
        "金髪の娘",
        (
            "#11P#2904Fん～、２ヶ月ぶりですわね。\x02\x03",

            "#2901Fでも貴女……\x01",
            "少し痩せたんじゃなくて？\x02\x03",

            "手とか足とか\x01",
            "ちょっと固くなっていてよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        (
            "#0104Fふふ、鍛えているから\x01",
            "少し筋肉が付いただけよ。\x02\x03",

            "#0102Fむしろ体重は少し\x01",
            "増えたんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #N0184
    NpcTalk(
        0x9,
        "金髪の娘",
        (
            "#11P#2905Fなるほど……\x02\x03",

            "言われてみれば筋肉の\x01",
            "しなやかさを感じますわね。\x02\x03",

            "#2909Fふふ、これはこれで\x01",
            "なかなかの感触ですわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#0113Fも、もう……\x02",
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
        "#5P#0012F（な、なんか凄い人だな……）\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x104,
        (
            "#11P#0302F（しかし美人同士が絡むと\x01",
            "  それだけで絵になるっつーか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#5P#0211F（というか、ただの友達同士には\x01",
            "  ちょっと見えないんですが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "#2804Fやれやれ、スキンシップは\x01",
            "そのくらいにしたらどうかね？\x02\x03",

            "#2800F他の客人が呆れているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x102,
        "#0112Fあ……\x02",
    )

    CloseMessageWindow()

    #N0191
    NpcTalk(
        0x9,
        "金髪の娘",
        "#12P#2905F……あら…………\x02",
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

    def lambda_5D95():
        OP_96(0xFE, 0xD7A0, 0x0, 0x1E014, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D95)
    WaitChrThread(0x9, 1)
    OP_93(0x102, 0x0, 0x1F4)

    #C0192
    ChrTalk(
        0x102,
        (
            "#0113F#11Pしょ、紹介するわね。\x02\x03",

            "#0102F彼女はマリアベル……\x01",
            "総裁の娘さんで、私の友人よ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(150)

    #C0193
    ChrTalk(
        0x102,
        (
            "#0100Fベル、彼らは私の同僚で、\x01",
            "ロイドとランディとティオちゃんって──\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x9,
        (
            "#12P#2903F紹介は結構ですわ。\x02\x03",

            "#2901F自分で検分しますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x102,
        "#0105Fえ。\x02",
    )

    CloseMessageWindow()

    def lambda_5EBC():

        label("loc_5EBC")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5EBC")

    QueueWorkItem2(0x102, 2, lambda_5EBC)

    def lambda_5ECE():

        label("loc_5ECE")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_5ECE")

    QueueWorkItem2(0x8, 2, lambda_5ECE)
    BeginChrThread(0x9, 3, 0, 18)
    WaitChrThread(0x9, 3)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    #C0196
    ChrTalk(
        0x101,
        "#11P#0012Fな、なにか……？\x02",
    )

    CloseMessageWindow()

    def lambda_5F1F():
        OP_95(0xFE, 53600, 0, 124100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F1F)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x103, 500)

    def lambda_5F44():

        label("loc_5F44")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_5F44")

    QueueWorkItem2(0x9, 2, lambda_5F44)
    OP_9E(0x103, 0xD160, 0x1E4C4, 0x15F90, 0x5DC, 0x0)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x9, 0x2)

    #C0197
    ChrTalk(
        0x103,
        "#11P#0205Fえ……\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "#2909F#5P貴女は合格。\x01",
            "ふふ、可愛らしいですわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(55000, 1100, 125300, 1300)
    MoveCamera(55, 21, 0, 1300)

    def lambda_5FDB():
        OP_95(0xFE, 55000, 0, 125300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5FDB)
    Sleep(300)

    def lambda_5FF8():
        OP_96(0xFE, 0xD7A0, 0x0, 0x1E3FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FF8)
    Sleep(300)

    def lambda_6015():
        OP_96(0xFE, 0xD1C4, 0x0, 0x1E460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6015)
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
        "#11P#2901Fで、貴方たちは不合格ですわ。\x02",
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
        "#6P#0011Fへ……！？\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        "#0305F#11Pな、何だそりゃ……！？\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "#11P#2903Fフン、こんなムサ苦しい男どもが\x01",
            "わたくしのエリィの側にいるなんて。\x02\x03",

            "#2901F女神も許さざる所業ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        "#6P#0006Fムサ苦しいって……\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x102,
        "#12P#0101Fちょ、ちょっとベル……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "#11P#2901F大体、なんですの？\x01",
            "そのラフすぎる服装は。\x02\x03",

            "せめてスーツくらい着るのが\x01",
            "礼儀というものでしょうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#6P#0005Fこ、これはその……\x02\x03",

            "#0012F街中や市外で捜査活動する時は\x01",
            "この方が都合がいいといいますか……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        (
            "#11P#2903F言い訳は結構ですわ。\x02\x03",

            "#2901Fまったく、だからわたくしは\x01",
            "警察入りなんて反対したのよ。\x02\x03",

            "わたくしの事業を手伝ってくれた方が\x01",
            "遥かに有意義だったでしょうに……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 19)

    #C0208
    ChrTalk(
        0x102,
        "#12P#0106Fああもう……ベルってば！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 3)

    #C0209
    ChrTalk(
        0x8,
        (
            "#2809Fハッハッハッ。\x01",
            "盛り上がっているようだね。\x02\x03",

            "#2804Fうむ、若い者は若い者同士で、\x01",
            "親交を暖めてくれたまえ。\x02\x03",

            "#2800F約束の時間なので\x01",
            "私はそろそろ失礼するよ。\x02\x03",

            "ベル、後で彼らを\x01",
            "端末室に案内してあげたまえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6444():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_6444)
    Sleep(150)

    def lambda_6454():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6454)
    Sleep(50)

    def lambda_6464():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6464)

    def lambda_6471():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6471)
    Sleep(50)
    TurnDirection(0x103, 0x8, 500)

    #C0210
    ChrTalk(
        0x9,
        (
            "#6P#2905F端末室……\x01",
            "どういうことですの？\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#2800F事情は彼らから聞くといい。\x02\x03",

            "#2809Fそれではさらばだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_64F6():

        label("loc_64F6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_64F6")

    QueueWorkItem2(0x102, 2, lambda_64F6)

    def lambda_6508():

        label("loc_6508")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_6508")

    QueueWorkItem2(0x9, 2, lambda_6508)

    def lambda_651A():

        label("loc_651A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_651A")

    QueueWorkItem2(0x103, 2, lambda_651A)

    def lambda_652C():

        label("loc_652C")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_652C")

    QueueWorkItem2(0x104, 2, lambda_652C)

    def lambda_653E():

        label("loc_653E")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_653E")

    QueueWorkItem2(0x101, 2, lambda_653E)
    OP_68(55000, 1100, 121300, 3000)

    def lambda_6561():
        OP_95(0xFE, 55000, 0, 118000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6561)
    WaitChrThread(0x8, 1)

    def lambda_657F():
        OP_95(0xFE, 55000, 0, 115000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_657F)
    Sound(103, 0, 100, 0)
    Sleep(500)

    def lambda_65A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_65A2)
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
        "#6P#0105Fあ……\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#6P#0206F逃げましたね……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        "#5P#2906Fもう、お父様ったら……\x02",
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
            "#6P#0012Fそ、それじゃあ早速、\x01",
            "案内をお願いできれば……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 700)

    #C0216
    ChrTalk(
        0x9,
        "#11P#2901Fまだ話は終わってませんわ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x104, 700)
    Sleep(300)

    #C0217
    ChrTalk(
        0x9,
        (
            "#2906F#6Pそちらの赤毛の貴方も、\x01",
            "そんな派手な格好をして……\x02\x03",

            "#2901F立派な体格をしているのだから\x01",
            "きちんとしたスーツを着なさい！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6777():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6777)
    Sleep(150)

    def lambda_6787():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6787)
    Sleep(50)
    TurnDirection(0x103, 0x9, 500)

    #C0218
    ChrTalk(
        0x104,
        (
            "#0305F#11Pお、俺ッスか？\x02\x03",

            "#0309Fいや～、でも俺って\x01",
            "根っからの遊び人だしなあ。\x02\x03",

            "#0302Fあ、それにソイツみたいに\x01",
            "夜の屋上で同僚のお嬢さんと\x01",
            "良い雰囲気になったりしないし。\x02",
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
        "#11P#2910F#4Sな、なんですって～！？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        "#6P#0011Fランディ、お前……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 700)

    #C0221
    ChrTalk(
        0x102,
        (
            "#12P#0101Fご、誤解されるようなことを\x01",
            "言わないでちょうだい！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0222
    ChrTalk(
        0x103,
        (
            "#6P#0204Fあながち誤解では\x01",
            "ないみたいですけど……\x02\x03",

            "#0202Fエリィさんも随分、\x01",
            "元気になったみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69BC():
        TurnDirection(0xFE, 0x103, 700)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_69BC)
    Sleep(100)
    TurnDirection(0x101, 0x103, 700)

    #C0223
    ChrTalk(
        0x102,
        "#11P#0112Fティ、ティオちゃん……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#5P#0013Fああもう、ティオも\x01",
            "引っ掻き回さないでくれ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A33():
        OP_99(0xFE, 0x101, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6A33)
    WaitChrThread(0x9, 1)
    Sound(804, 0, 100, 0)
    TurnDirection(0x101, 0x9, 700)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    OP_52(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_6A6D():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A6D)

    def lambda_6A86():
        OP_98(0xFE, 0x0, 0xC8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A86)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)

    #C0225
    ChrTalk(
        0x9,
        (
            "#11P#2909Fフフフ……\x01",
            "ロイドさんと言ったかしら……？\x02\x03",

            "その辺りの事をもう少し詳しく\x01",
            "聞かせてくれないかしら……？\x02\x03",

            "#2910Fわたくしのエリィに\x01",
            "どんな破廉恥な事をしたのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#6P#0012Fいや、してませんってば！\x02",
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
            "#6P#0011Fだからエリィも\x01",
            "何でそこで黙るんだよ！？\x02",
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
            "#2903F#11P──なるほど。\x01",
            "事情はわかりましたわ。\x02\x03",

            "#2900Fそれで、あなたたちを\x01",
            "端末室に案内すればいいのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        "#6P#0100Fええ、頼めるかしら？\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        (
            "#2906F#11P無論、エリィの頼みなら\x01",
            "言うまでもありませんけど……\x02",
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
            "#0012Fえっと……\x01",
            "誤解は解けたはずでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x9,
        (
            "#2903F#11Pフン、まあいいでしょう。\x02\x03",

            "特務支援課……\x01",
            "わたくしもどの程度のものか\x01",
            "気になっていましたし。\x02\x03",

            "#2902Fエリィの同僚に相応しいか……\x01",
            "貴方に証明していただこうかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#0011Fは、はあ……\x01",
            "（何で俺限定なんだろう……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#6P#0302F（こりゃ、完全に\x01",
            "  目を付けられちまったなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        "#6P#0204F（……ご愁傷様ですね。）\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#6P#0106Fもう……\x01",
            "ベル、いいかげんにして。\x02\x03",

            "#0101F端末室に案内、してくれないの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 500)

    #C0238
    ChrTalk(
        0x9,
        (
            "#2904F#11Pもちろん案内しますわ。\x02\x03",

            "#2900F端末室は、ＩＢＣビルの\x01",
            "地下５階に設置されています。\x02\x03",

            "さ、エレベーターに乗りますわよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xB4, 0x1F4)

    def lambda_701C():

        label("loc_701C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_701C")

    QueueWorkItem2(0x102, 2, lambda_701C)

    def lambda_702E():

        label("loc_702E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_702E")

    QueueWorkItem2(0x103, 2, lambda_702E)

    def lambda_7040():

        label("loc_7040")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7040")

    QueueWorkItem2(0x104, 2, lambda_7040)

    def lambda_7052():

        label("loc_7052")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_7052")

    QueueWorkItem2(0x101, 2, lambda_7052)
    OP_68(55100, 1200, 120000, 3000)

    def lambda_7075():
        OP_95(0xFE, 55000, 0, 117500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7075)
    WaitChrThread(0x9, 1)

    def lambda_7093():
        OP_95(0xFE, 55000, 0, 115000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7093)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_70B6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_70B6)
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
        "#0006F#5P……はあ、すごい人だな。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x102,
        (
            "#5P#0105Fその、悪い人じゃないのよ？\x02\x03",

            "#0106Fただちょっと、強引というか\x01",
            "行動力がありすぎるというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#0300F#5Pしかし、オヤジさんといい\x01",
            "やたらとパワフルな父娘だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#0204F#5Pさすが天下のＩＢＣの\x01",
            "オーナーといった所でしょうか。\x02",
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

    # Function_17_2D49 end

    def Function_18_734A(): pass

    label("Function_18_734A")


    def lambda_734F():
        OP_95(0xFE, 56300, 0, 124000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_734F)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x104, 500)
    Sleep(500)

    #C0243
    ChrTalk(
        0x9,
        "#2901Fふむ……\x02",
    )

    CloseMessageWindow()

    def lambda_738B():
        OP_95(0xFE, 55200, 0, 122900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_738B)
    WaitChrThread(0x9, 1)

    def lambda_73A9():
        OP_95(0xFE, 53400, 0, 123900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_73A9)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x103, 500)
    Sleep(500)

    #C0244
    ChrTalk(
        0x9,
        "#5P#2902F……なるほど……\x02",
    )

    CloseMessageWindow()

    def lambda_73F0():
        OP_95(0xFE, 52600, 0, 125600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_73F0)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x101, 500)
    Sleep(500)
    Return()

    # Function_18_734A end

    def Function_19_7414(): pass

    label("Function_19_7414")

    EndChrThread(0x8, 0x2)

    def lambda_741D():
        OP_95(0xFE, 56000, 0, 130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_741D)
    WaitChrThread(0x8, 1)

    def lambda_743B():
        OP_95(0xFE, 58600, 0, 130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_743B)
    WaitChrThread(0x8, 1)

    def lambda_7459():
        OP_95(0xFE, 58600, 0, 127500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7459)
    WaitChrThread(0x8, 1)

    def lambda_7477():
        OP_95(0xFE, 58000, 0, 126900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7477)
    WaitChrThread(0x8, 1)
    TurnDirection(0x8, 0x9, 500)
    Return()

    # Function_19_7414 end

    def Function_20_7498(): pass

    label("Function_20_7498")

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
            "#5P#2901Fまったくもう……\x01",
            "例の《ルバーチェ》のお陰で\x01",
            "こちらは会議続きですわ！\x02\x03",

            "#2903F襲撃事件の株価への影響は\x01",
            "何とか喰い止められそうですけど……\x02\x03",

            "#2901Fあとで賠償金でも\x01",
            "請求したいくらいですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        "#12P#0103F相変わらず大変そうね……\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x9,
        (
            "#5P#2900Fお父様が留守なので\x01",
            "なおの事、といった所ですわね。\x02\x03",

            "#2905F……それはそうと。\x01",
            "エリィ、なにか御用かしら？\x02\x03",

            "私用といった風でも\x01",
            "なさそうだけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#12P#0100Fええ、実はベルに\x01",
            "聞きたい事があるの。\x02\x03",

            "今日こちらにカーラさんが\x01",
            "来たはずなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x9,
        (
            "#5P#2905Fカーラさん……？\x02\x03",

            "#2900Fそうですわね、\x01",
            "先ほど訪ねてきましたわ。\x02\x03",

            "#2904Fあの子とは社交界なんかで\x01",
            "多少面識がありますの。\x02\x03",

            "今日は緊急だとかで……\x02\x03",

            "#2900Fわたくしに直接話を通して、\x01",
            "自分の定期預金を\x01",
            "取り崩して行きましたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        "#12P#0303Fやっぱそうだったか。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#11P#0005F……でも、どうしてまた\x01",
            "マリアベルさんを通して？\x02\x03",

            "受付で事足りる気もしますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "#5P#2903F額が多額だったからですわ。\x02\x03",

            "#2900F通常なら手続きが必要な所を、\x01",
            "今日はどうしてもという事でしたの。\x02\x03",

            "具体的な額はさすがに\x01",
            "明かせはしませんけれど……\x01",
            "数十万ミラ、といった所ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#12P#0205Fそれは大金ですね……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        (
            "#12P#0103F実はカーラさんは\x01",
            "家出したらしくて……\x01",
            "私たちで行方を追っている所なの。\x02\x03",

            "#0100Fベル、何か心当たりは無いかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        (
            "#5P#2905Fあら、そういう事でしたの。\x02\x03",

            "#2903Fとなると……額からして\x01",
            "外国かもしれませんわね。\x02",
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
        "#11P#0000Fありえますね……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x103,
        (
            "#12P#0200F一体どこへ\x01",
            "向かったんでしょうか。\x02",
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
            "#5P#2903Fそういえば……\x02\x03",

            "メイドに向かって\x01",
            "グランセル見物がどうのと\x01",
            "言ってましたわね。\x02\x03",

            "#2900Fホテルを予約しておくように、\x01",
            "とも言っていたようですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#11P#0005Fグランセル……？\x01",
            "リベール王国の王都ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        "#12P#0301F……リベール方面か！\x02",
    )

    CloseMessageWindow()

    def lambda_7C0C():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C0C)

    def lambda_7C19():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C19)

    def lambda_7C26():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C26)

    def lambda_7C33():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C33)
    Sleep(800)

    #C0261
    ChrTalk(
        0x103,
        (
            "#12P#0200Fだとしたら空港ですね……\x02\x03",

            "まだ国際便の時間には\x01",
            "間に合うはずです。\x01",
            "受付さんに話をつけましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        "#6P#0101Fええ、みんな急ぎましょう！\x02",
    )

    CloseMessageWindow()

    def lambda_7CDA():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_7CDA)

    def lambda_7CE7():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_7CE7)

    def lambda_7CF4():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7CF4)

    def lambda_7D01():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_7D01)
    Sleep(300)

    #C0263
    ChrTalk(
        0x101,
        (
            "#11P#0001Fどうもお騒がせしました。\x01",
            "ご協力感謝します。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        "#12P#0101Fまたね、ベル！\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        "#5P#2905Fえ、ええ……\x02",
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
        "#5P#2903Fやれやれ、慌しいですわね。\x02",
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

    # Function_20_7498 end

    def Function_21_7E99(): pass

    label("Function_21_7E99")

    OP_95(0xFE, 55000, 0, 118710, 5000, 0x1)

    def lambda_7EB2():
        OP_95(0xFE, 55000, 0, 114830, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7EB2)
    Sleep(100)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_21_7E99 end

    def Function_22_7ED6(): pass

    label("Function_22_7ED6")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FDB")

    #C0268
    ChrTalk(
        0x102,
        "#0102F（ここは……ベルの部屋ね。）\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x101,
        "#0005Fエリィ、どうかしたのか？\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        (
            "#0104Fううん、別に。\x02\x03",

            "#0100Fロイド、総裁室なら正面の部屋よ。\x01",
            "行ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        "#0000Fああ、そうしよう。\x02",
    )

    CloseMessageWindow()

    label("loc_7FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8104")

    #C0272
    ChrTalk(
        0x138,
        (
            "#2905Fあら、そこは\x01",
            "わたくしの部屋ですわよ。\x02\x03",

            "#2902F宜しかったら\x01",
            "お茶でもいかがかしら？\x01",
            "ご馳走いたしますわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#0012Fハハ、今はちょっと……\x02\x03",

            "#0000F先に端末室という所に\x01",
            "案内してもらっていいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x138,
        (
            "#2904Fええ、構いませんわ。\x02\x03",

            "#2900Fそれではエレベーターに\x01",
            "乗りますわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8104")

    SetScenarioFlags(0x0, 3)

    label("loc_8107")

    TalkEnd(0xFF)
    Return()

    # Function_22_7ED6 end

    def Function_23_810B(): pass

    label("Function_23_810B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_END)), "loc_81B5")
    TalkBegin(0xFF)
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まるで生きているかのような\x01",
            "精巧な人形がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81AD")

    #C0276
    ChrTalk(
        0x101,
        (
            "#0003F（傷でも付けたら事だ……\x01",
            "  無闇に触らないでおこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_81AD")

    TalkEnd(0xFF)
    Jump("loc_81B8")

    label("loc_81B5")

    Call(0, 7)

    label("loc_81B8")

    Jump("loc_842E")

    label("loc_81BD")

    TalkBegin(0xFF)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "まるで生きているかのような\x01",
            "精巧な人形がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83DD")
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
            "#0005Fな……！？\x02\x03",

            "#0003Fこれは……凄いな。\x01",
            "本当に人形なのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#0100Fローゼンベルク工房製の人形ね。\x02\x03",

            "ベルのコレクションの一部よ。\x01",
            "この２体が特にお気に入りみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x103,
        (
            "#0205Fこれがローゼンベルク製……\x01",
            "肌もしっとりしていて\x01",
            "とても人形には見えません……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x104,
        "#0303Fとんでもない精巧ぶりだな……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        (
            "#0003F相当値段がするって聞いたけど……\x01",
            "これは頷ける気がするな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB8, 3)

    label("loc_83DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_842B")

    #C0283
    ChrTalk(
        0x101,
        (
            "#0003F（傷でも付けたら事だ……\x01",
            "  無闇に触らないでおこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_842B")

    TalkEnd(0xFF)

    label("loc_842E")

    Return()

    # Function_23_810B end

    SaveToFile()

Try(main)
