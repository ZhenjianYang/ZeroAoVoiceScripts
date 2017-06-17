from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1120.bin",                # FileName
        "c1120",                    # MapName
        "c1120",                    # Location
        0x0017,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1120",                  # 0
        "グレイス",               # 1
        "レインズ",               # 2
        "フェン",                 # 3
        "オスカー",               # 4
        "受付嬢シンシア",         # 5
        "アイリス",               # 6
        "ケイト巡査",             # 7
        "ピアノ奏者",             # 8
        "案内人",                 # 9
        "メイド",                 # 10
        "市民",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "男の子",                 # 14
        "市民",                   # 15
        "シスター・リース",       # 16
        "サンサン",               # 17
        "ジョアンナ",             # 18
        "モルス老人",             # 19
        "ロイ",                   # 20
        "ウェンディ",             # 21
        "市民",                   # 22
        "市民",                   # 23
        "市民",                   # 24
        "市民",                   # 25
        "市民",                   # 26
        "市民",                   # 27
        "市民",                   # 28
        "キャンベル議員",         # 29
        "帝国派議員",             # 30
        "独立派議員",             # 31
        "独立派議員",             # 32
        "司会",                   # 33
    ))

    AddCharChip((
        "chr/ch06000.itc",                   # 00
        "chr/ch28100.itc",                   # 01
        "chr/ch25100.itc",                   # 02
        "chr/ch07000.itc",                   # 03
        "chr/ch34600.itc",                   # 04
        "chr/ch26900.itc",                   # 05
        "chr/ch30600.itc",                   # 06
        "chr/ch33302.itc",                   # 07
        "chr/ch25900.itc",                   # 08
        "chr/ch25600.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch21000.itc",                   # 0B
        "chr/ch20300.itc",                   # 0C
        "chr/ch23000.itc",                   # 0D
        "chr/ch21702.itc",                   # 0E
        "chr/ch14000.itc",                   # 0F
        "chr/ch26902.itc",                   # 10
        "chr/ch32500.itc",                   # 11
        "chr/ch25700.itc",                   # 12
    ))

    DeclNpc(-4659,   0,       9239,    0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-5949,   0,       9800,    45,   261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-10529,  0,       1179,    90,   261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-10189,  0,       7269,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-6579,   0,       -2069,   109,  261,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(5000,    0,       2289,    270,  261,  0x0, 0,   16,  0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-4070,   0,       6420,    135,  261,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-3309,   1049,    13500,   135,  261,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-1019,   0,       -9300,   270,  261,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-790,    0,       7590,    348,  261,  0x0, 0,   9,   0,   0,   1,   0,   16,  255,  0)
    DeclNpc(-2180,   0,       3890,    315,  261,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-90,     0,       4420,    45,   261,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-730,    0,       -2769,   135,  261,  0x0, 0,   12,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-29,     0,       -3329,   315,  261,  0x0, 0,   13,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(5000,    0,       -2769,   270,  261,  0x0, 0,   14,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   15,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   10,  255,  0)
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

    DeclActor(7750,    4000,    12300,   1200,    7750,    5450,    12300,   0x007C, 0,  5,  0x0000)
    DeclActor(-2170,   880,     11540,   1000,    -3310,   2550,    13500,   0x007E, 0,  17, 0x0000)

    ChipFrameInfo(1392, 0)                                       # 0

    ScpFunction((
        "Function_0_570",          # 00, 0
        "Function_1_620",          # 01, 1
        "Function_2_76E",          # 02, 2
        "Function_3_85B",          # 03, 3
        "Function_4_990",          # 04, 4
        "Function_5_A5A",          # 05, 5
        "Function_6_B78",          # 06, 6
        "Function_7_F53",          # 07, 7
        "Function_8_1034",         # 08, 8
        "Function_9_12B5",         # 09, 9
        "Function_10_141D",        # 0A, 10
        "Function_11_1527",        # 0B, 11
        "Function_12_18B0",        # 0C, 12
        "Function_13_1B27",        # 0D, 13
        "Function_14_1D74",        # 0E, 14
        "Function_15_1E59",        # 0F, 15
        "Function_16_1F8C",        # 10, 16
        "Function_17_20DF",        # 11, 17
        "Function_18_2183",        # 12, 18
        "Function_19_22A9",        # 13, 19
        "Function_20_2379",        # 14, 20
        "Function_21_2438",        # 15, 21
        "Function_22_24C0",        # 16, 22
        "Function_23_25A9",        # 17, 23
        "Function_24_2969",        # 18, 24
        "Function_25_4C2E",        # 19, 25
        "Function_26_4C98",        # 1A, 26
        "Function_27_4CD9",        # 1B, 27
        "Function_28_4DD8",        # 1C, 28
        "Function_29_7C19",        # 1D, 29
        "Function_30_7C57",        # 1E, 30
        "Function_31_7C76",        # 1F, 31
        "Function_32_7CA7",        # 20, 32
        "Function_33_7CDB",        # 21, 33
        "Function_34_7D0F",        # 22, 34
        "Function_35_7D2B",        # 23, 35
        "Function_36_7D5C",        # 24, 36
        "Function_37_7D78",        # 25, 37
        "Function_38_7D94",        # 26, 38
        "Function_39_7DDF",        # 27, 39
        "Function_40_7E19",        # 28, 40
        "Function_41_7E7B",        # 29, 41
        "Function_42_7FB0",        # 2A, 42
    ))


    def Function_0_570(): pass

    label("Function_0_570")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_5A8"),
        (1, "loc_5B4"),
        (2, "loc_5C0"),
        (3, "loc_5CC"),
        (4, "loc_5D8"),
        (5, "loc_5E4"),
        (6, "loc_5F0"),
        (SWITCH_DEFAULT, "loc_5FC"),
    )


    label("loc_5A8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5B4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5C0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5CC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5D8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5E4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_5FC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_608")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_608")

    label("loc_61F")

    Return()

    # Function_0_570 end

    def Function_1_620(): pass

    label("Function_1_620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76D")
    SetChrPos(0xFE, 3130, 0, 9060, 270)
    OP_95(0xFE, -160, 0, 7500, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_95(0xFE, -1340, 0, 3750, 1000, 0x0)
    OP_95(0xFE, -80, 0, -190, 1000, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, -1120, 0, 1760, 1000, 0x0)
    OP_95(0xFE, -3830, 0, 1460, 1000, 0x0)
    OP_95(0xFE, -4390, 0, 2430, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, -4330, 0, -270, 1000, 0x0)
    Sleep(2000)
    OP_95(0xFE, -2360, 0, 1350, 1000, 0x0)
    OP_95(0xFE, 1010, 0, 2510, 1000, 0x0)
    OP_95(0xFE, 1630, 0, 3540, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    OP_95(0xFE, 3710, 0, 4130, 1000, 0x0)
    OP_95(0xFE, 4290, 0, 7130, 1000, 0x0)
    OP_95(0xFE, 3130, 0, 9060, 1000, 0x0)
    Jump("Function_1_620")

    label("loc_76D")

    Return()

    # Function_1_620 end

    def Function_2_76E(): pass

    label("Function_2_76E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85A")
    OP_95(0x17, -7300, 0, -2510, 2000, 0x0)
    OP_95(0x17, -7330, 0, 1430, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -5910, 0, 4260, 2000, 0x0)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -6960, 0, 7410, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -5910, 0, 4260, 2000, 0x0)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -7330, 0, 1430, 2000, 0x0)
    OP_93(0x17, 0x10E, 0x1F4)
    Sleep(2000)
    OP_95(0x17, -7300, 0, -2510, 2000, 0x0)
    OP_95(0x17, -5820, 0, -3790, 2000, 0x0)
    OP_93(0x17, 0x2D, 0x1F4)
    Sleep(2000)
    Jump("Function_2_76E")

    label("loc_85A")

    Return()

    # Function_2_76E end

    def Function_3_85B(): pass

    label("Function_3_85B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_872")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 3)
    Event(0, 24)
    Jump("loc_881")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_881")
    ClearScenarioFlags(0x22, 2)
    Event(0, 41)

    label("loc_881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89C")
    Event(0, 42)

    label("loc_89C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_98F")
    SetScenarioFlags(0x1, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_96A")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -4500, 0, -7300, 270)
    SetChrPos(0x8, -5560, 0, -7300, 90)
    SetChrPos(0x9, -5160, 0, -6000, 135)
    SetChrPos(0x18, -8590, 0, 2730, 225)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0x19, 3340, 0, 10090, 90)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x17, -5820, 0, -3790, 45)
    BeginChrThread(0x17, 0, 0, 2)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0xD, 0x10)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_97E")

    label("loc_96A")

    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)

    label("loc_97E")

    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)

    label("loc_98F")

    Return()

    # Function_3_85B end

    def Function_4_990(): pass

    label("Function_4_990")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B3")
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetScenarioFlags(0x1, 3)

    label("loc_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F2")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light04", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A27")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light04", 0x0, 0x1)

    label("loc_A27")

    OP_65(0x0, 0x1)
    SetMapObjFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A44")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_A59")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)

    label("loc_A59")

    Return()

    # Function_4_990 end

    def Function_5_A5A(): pass

    label("Function_5_A5A")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★特製スイートショコラの作り方★\x01",
            "　～　みなさまもご家庭で\x01",
            "　　　いかがですか？　　～\x02",
        )
    )

    CloseMessageWindow()

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイートショコラのレシピが書かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B74")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『スイートショコラ』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B74")

    TalkEnd(0xFF)
    Return()

    # Function_5_A5A end

    def Function_6_B78(): pass

    label("Function_6_B78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC3")
    TurnDirection(0x8, 0x0, 500)

    #C0004
    ChrTalk(
        0x8,
        (
            "#02102Fあっ、あなた達もお疲れ様！\x02\x03",

            "今、ミスコンの参加者たちに\x01",
            "インタビューしてるところなの。\x02\x03",

            "#02109Fフフ、あなたたちも後で\x01",
            "ちゃんと付き合ってよね～♪\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#00006F（う、う～ん、悪いけど、\x01",
            "  時間をとられそうだしなあ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x105,
        (
            "#10302F（フフ、こっそり逃げた方が\x01",
            "  よさそうだね。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    SetScenarioFlags(0x0, 4)
    Jump("loc_D41")

    label("loc_CC3")


    #C0007
    ChrTalk(
        0x8,
        (
            "#02105Fあらま、そうなんですか？\x02\x03",

            "#02100F確かにあんな事件があった後だし、\x01",
            "ご家族に顔を見せたほうが\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D41")

    Jump("loc_F4F")

    label("loc_D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")

    #C0008
    ChrTalk(
        0x8,
        "#02109Fやっほー、ロイド君たち！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#00000Fグレイスさん……\x01",
            "チャリティイベントの取材ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#02100Fふふ、そういうこと☆\x02\x03",

            "かなり賑やかみたいだし、\x01",
            "クロスベル市民たちも\x01",
            "元気になれる記事が書けそうだわ。\x02\x03",

            "#02103Fあの襲撃事件の傷跡は\x01",
            "まだ消えていないし……\x02\x03",

            "#02102Fあたしたちマスコミも、\x01",
            "出来ることをやんなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#00309Fはは、がんばって下さいッス。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 6)
    Jump("loc_F4F")

    label("loc_EC5")


    #C0012
    ChrTalk(
        0x8,
        (
            "#02102Fなんでも、チャリティイベントには\x01",
            "面白そうなプログラムがあるって\x01",
            "噂になってるし……\x02\x03",

            "#02109Fふふ、ばっちりスクープするわよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F4F")

    TalkEnd(0xFE)
    Return()

    # Function_6_B78 end

    def Function_7_F53(): pass

    label("Function_7_F53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FD3")

    #C0013
    ChrTalk(
        0xFE,
        (
            "ミスコン、なかなか\x01",
            "見応えがありましたねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "いい写真も一杯撮れたし、\x01",
            "早く帰ってまとめ直さないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1030")

    label("loc_FD3")


    #C0015
    ChrTalk(
        0xFE,
        (
            "チャリティイベントに呼ばれた\x01",
            "美人ピアノ奏者……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "なかなかいい写真が撮れそうですね。\x02",
    )

    CloseMessageWindow()

    label("loc_1030")

    TalkEnd(0xFE)
    Return()

    # Function_7_F53 end

    def Function_8_1034(): pass

    label("Function_8_1034")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F5")

    #C0017
    ChrTalk(
        0xFE,
        (
            "いや～、まさかサンサンが\x01",
            "ミスコンに参加するとは\x01",
            "思ってなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "ま、おかげでいつもの調子が\x01",
            "少しは戻ってきたみたいだし、\x01",
            "結果オーライって感じだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1154")

    label("loc_10F5")


    #C0019
    ChrTalk(
        0xFE,
        (
            "しかし、サンサンが\x01",
            "ミスコンに参加したとなると……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "……マスター、怒ってなきゃいいが。\x02",
    )

    CloseMessageWindow()

    label("loc_1154")

    Jump("loc_12B1")

    label("loc_1159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122C")

    #C0021
    ChrTalk(
        0xFE,
        (
            "《龍老飯店》から\x01",
            "チャリティイベントに\x01",
            "料理を出してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "店のほうでは俺がいない穴を\x01",
            "パックとルースに任せてる。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "ちょっと心配だが、\x01",
            "あいつらもマシになったし\x01",
            "多分大丈夫だろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_12B1")

    label("loc_122C")


    #C0024
    ChrTalk(
        0xFE,
        (
            "しかし……サンサンのヤツが\x01",
            "最近元気がねえんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "コンテストの参加も\x01",
            "断っちまったみたいだし……\x01",
            "早く元気になりゃいいが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B1")

    TalkEnd(0xFE)
    Return()

    # Function_8_1034 end

    def Function_9_12B5(): pass

    label("Function_9_12B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396")

    #C0026
    ChrTalk(
        0xFE,
        (
            "うふふ、これで\x01",
            "お店のお客さんが増えたら\x01",
            "パパも大喜びね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "……リーシャの事は心配だけど、\x01",
            "きっと帰ってくるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "その時に笑顔で迎えられるように、\x01",
            "私も元気にして待ってないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_1414")

    label("loc_1396")


    #C0029
    ChrTalk(
        0xFE,
        (
            "リーシャの事は心配だけど、\x01",
            "きっと帰ってくるはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "その時に笑顔で迎えられるように、\x01",
            "私も元気にして待ってないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1414")

    Jump("loc_1419")

    label("loc_1419")

    TalkEnd(0xFE)
    Return()

    # Function_9_12B5 end

    def Function_10_141D(): pass

    label("Function_10_141D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DD")

    #C0031
    ChrTalk(
        0xFE,
        (
            "はあ……私のような者が、\x01",
            "あんな壇上に上がってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00109Fふふ……ジョアンナ、\x01",
            "とってもかわいらしかったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "うう、お恥ずかしいです……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_151E")

    label("loc_14DD")


    #C0034
    ChrTalk(
        0xFE,
        (
            "私のような者が、あんな壇上に……\x01",
            "うう、お恥ずかしいです……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_151E")

    Jump("loc_1523")

    label("loc_1523")

    TalkEnd(0xFE)
    Return()

    # Function_10_141D end

    def Function_11_1527(): pass

    label("Function_11_1527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_16D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1671")

    #C0035
    ChrTalk(
        0xFE,
        (
            "よお、ロイドと支援課の！\x01",
            "なかなかカッコよかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "はは、出てきたときは\x01",
            "さすがにビビったが、\x01",
            "個人的にはあんたらが優勝だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_15FE")

    #C0037
    ChrTalk(
        0x102,
        "#00109Fふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1669")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_1637")

    #C0038
    ChrTalk(
        0x103,
        "#00202Fふふっ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1669")

    label("loc_1637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_1669")

    #C0039
    ChrTalk(
        0x109,
        "#10109Fふふ、ありがとうございます！\x02",
    )

    CloseMessageWindow()

    label("loc_1669")

    SetScenarioFlags(0x0, 6)
    Jump("loc_16CB")

    label("loc_1671")


    #C0040
    ChrTalk(
        0xFE,
        (
            "ま、あんたらも引き続き\x01",
            "楽しんでいってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "料理もまだまだ\x01",
            "たっぷりあるからよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CB")

    Jump("loc_18AC")

    label("loc_16D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1825")

    #C0042
    ChrTalk(
        0xFE,
        "おお、ロイドじゃねえか。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00005Fオスカー……？\x01",
            "イベントの手伝いに来てたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "ああ、店はベネットたちに任せて\x01",
            "俺はこっちに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "テーブルにはウチのバゲットも\x01",
            "並んでるし、パンに合う料理も\x01",
            "いくつか作れるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#00102Fうーん、流石ですね。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "はは、お前たちもしっかりと\x01",
            "楽しんでいってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19C, 7)
    Jump("loc_18AC")

    label("loc_1825")


    #C0048
    ChrTalk(
        0xFE,
        (
            "テーブルにはウチのバゲットも\x01",
            "並んでるし、パンに合う料理も\x01",
            "いくつか作ってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "お前たちもしっかりと\x01",
            "楽しんでいってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AC")

    TalkEnd(0xFE)
    Return()

    # Function_11_1527 end

    def Function_12_18B0(): pass

    label("Function_12_18B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18C4")
    Jump("loc_1B23")

    label("loc_18C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_1950")

    #C0050
    ChrTalk(
        0xFE,
        (
            "ロイド君たち、ミスコンの参加者を\x01",
            "集めているらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "ふふ、がんばってちょうだい。\x01",
            "私もここで応援させてもらうわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B23")

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA8")

    #C0052
    ChrTalk(
        0xFE,
        "あら、ロイド君たちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003Fあれ、ケイト先輩？\x01",
            "こんな所で何を……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "うん、一応イベントの\x01",
            "手伝いで来てるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "私の出番が来るまで\x01",
            "まだ少し時間があるから、\x01",
            "腹ごしらえしてるところなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#00105F出番……？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "おっと、これは\x01",
            "まだヒミツだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ふふ、まあ楽しみに\x01",
            "していてちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 0)
    Jump("loc_1B23")

    label("loc_1AA8")


    #C0059
    ChrTalk(
        0xFE,
        (
            "私の出番が来るまで\x01",
            "まだ少し時間があるから、\x01",
            "腹ごしらえしてるところなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "ふふ、まあ楽しみに\x01",
            "していてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B23")

    TalkEnd(0xFE)
    Return()

    # Function_12_18B0 end

    def Function_13_1B27(): pass

    label("Function_13_1B27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1C55")

    #C0061
    ChrTalk(
        0x8,
        (
            "#02100Fふむふむ、それじゃあ\x01",
            "職場の同僚から勧められて？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        "ええ、そうなんです。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ふふ、ミスコンの壇上は\x01",
            "本当に緊張しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "でも、皆さんに拍手をもらえたのは\x01",
            "素直に嬉しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "ふふ、やっぱり出てよかったですね。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#02104Fふんふん……（サラサラ）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CDB")

    label("loc_1C55")


    #C0067
    ChrTalk(
        0xFE,
        (
            "実は私、近い内に\x01",
            "故郷のレミフェリアに帰る予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "すぐに戻ってくるつもりですが……\x01",
            "両親へのいい土産話ができましたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDB")

    Jump("loc_1D70")

    label("loc_1CE0")


    #C0069
    ChrTalk(
        0xFE,
        (
            "この後のプログラムで、\x01",
            "壇上に上がらなくては\x01",
            "いけないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "人前に立つのは\x01",
            "職業柄慣れているのですが、\x01",
            "やっぱり緊張してしまいますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D70")

    TalkEnd(0xFE)
    Return()

    # Function_13_1B27 end

    def Function_14_1D74(): pass

    label("Function_14_1D74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1DFE")

    #C0071
    ChrTalk(
        0xFE,
        (
            "あ～ん、やっぱり他人に\x01",
            "ちやほやされるのって最高だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "とっても楽しかったし、\x01",
            "機会があればまたやりたいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E55")

    label("loc_1DFE")


    #C0073
    ChrTalk(
        0xFE,
        (
            "パフパフ……\x01",
            "うん、お化粧のノリもバッチリ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        "やるからにはトップを狙うわよ～。\x02",
    )

    CloseMessageWindow()

    label("loc_1E55")

    TalkEnd(0xFE)
    Return()

    # Function_14_1D74 end

    def Function_15_1E59(): pass

    label("Function_15_1E59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F01")

    #C0075
    ChrTalk(
        0xFE,
        (
            "ミスコンのおかげで、\x01",
            "クロスベル市復興義援金も\x01",
            "随分と集まりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "市民のみなさま、そして\x01",
            "特務支援課の皆様には\x01",
            "本当に感謝しておりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F88")

    label("loc_1F01")


    #C0077
    ChrTalk(
        0xFE,
        (
            "今日の立食パーティの飲食代は、\x01",
            "すべてクロスベル市の\x01",
            "復興義援金として寄付されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "どうか、心行くまで\x01",
            "お楽しみくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F88")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E59 end

    def Function_16_1F8C(): pass

    label("Function_16_1F8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_200A")

    #C0079
    ChrTalk(
        0xFE,
        (
            "参加者のみなさん、\x01",
            "とっても素敵でしたね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "やっぱり私もメイド枠で\x01",
            "立候補すればよかったです～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_END)), "loc_2094")

    #C0081
    ChrTalk(
        0xFE,
        (
            "私は立食パーティのお世話があるので\x01",
            "ミスコンには出られませんよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "すみませんが、\x01",
            "他の方を探してきてくださいね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DB")

    label("loc_2094")


    #C0083
    ChrTalk(
        0xFE,
        (
            "お食事、お飲み物が必要でしたら\x01",
            "お気軽にお申し付けくださいませ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DB")

    TalkEnd(0xFE)
    Return()

    # Function_16_1F8C end

    def Function_17_20DF(): pass

    label("Function_17_20DF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_215D")

    #C0084
    ChrTalk(
        0xF,
        (
            "ミスコンって俗っぽすぎる\x01",
            "気がしてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xF,
        (
            "ふふ、なかなか楽しかったわ。\x01",
            "あなたたちもお疲れ様。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_215D")


    #C0086
    ChrTalk(
        0xF,
        "次は何の曲を弾こうかしら……\x02",
    )

    CloseMessageWindow()

    label("loc_217F")

    TalkEnd(0xF)
    Return()

    # Function_17_20DF end

    def Function_18_2183(): pass

    label("Function_18_2183")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2207")

    #C0087
    ChrTalk(
        0xFE,
        (
            "……む、むぐぐう……\x01",
            "流石に食いすぎたようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "だが、クロスベル市のために……\x01",
            "わしは食いまくるぞい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A5")

    label("loc_2207")


    #C0089
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "クロスベル中の美味いモノが\x01",
            "この会場に揃っておるようじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "食べれば食べるほど\x01",
            "市のためになるというし、\x01",
            "ここは気合をいれて食べるぞい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A5")

    TalkEnd(0xFE)
    Return()

    # Function_18_2183 end

    def Function_19_22A9(): pass

    label("Function_19_22A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2303")

    #C0091
    ChrTalk(
        0xFE,
        "は～、いい目の保養になったな。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "やはり酒の肴は美人に限るよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2375")

    label("loc_2303")


    #C0093
    ChrTalk(
        0xFE,
        (
            "ん～、なんだか会場内に\x01",
            "綺麗どころが一杯いるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "あとでやるっていう、\x01",
            "目玉プログラムと関係あるのかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2375")

    TalkEnd(0xFE)
    Return()

    # Function_19_22A9 end

    def Function_20_2379(): pass

    label("Function_20_2379")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23FB")

    #C0095
    ChrTalk(
        0xFE,
        (
            "ふふ、女の私から見ても\x01",
            "綺麗な人たちばかりだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "この子も働くお姉さんに\x01",
            "憧れちゃったみたいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2434")

    label("loc_23FB")


    #C0097
    ChrTalk(
        0xFE,
        (
            "ほらほら、口の周りに\x01",
            "ケチャップがべったりじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2434")

    TalkEnd(0xFE)
    Return()

    # Function_20_2379 end

    def Function_21_2438(): pass

    label("Function_21_2438")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2493")

    #C0098
    ChrTalk(
        0xFE,
        "ぼくねー、ぼくねー……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "けーさつの人が\x01",
            "かっこよかったと思う！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24BC")

    label("loc_2493")


    #C0100
    ChrTalk(
        0xFE,
        (
            "むぐむぐ……\x01",
            "えへへ、おいしいね～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24BC")

    TalkEnd(0xFE)
    Return()

    # Function_21_2438 end

    def Function_22_24C0(): pass

    label("Function_22_24C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_252F")

    #C0101
    ChrTalk(
        0xFE,
        "ミスコンは楽しかったですね。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ふふ、わたしも３０年若ければ\x01",
            "立候補したんですけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25A5")

    label("loc_252F")


    #C0103
    ChrTalk(
        0xFE,
        (
            "さっき演奏されていた\x01",
            "ピアノの曲がいい音色だったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "襲撃事件で沈んだ気持ちも、\x01",
            "安らかになる気がするわねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25A5")

    TalkEnd(0xFE)
    Return()

    # Function_22_24C0 end

    def Function_23_25A9(): pass

    label("Function_23_25A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AF")

    #C0105
    ChrTalk(
        0x17,
        (
            "#04402F皆さん、お誘いいただき\x01",
            "ありがとうございました。\x02\x03",

            "教会ではなかなか経験できない\x01",
            "面白い試みだったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        "#00109Fふふ、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#00302Fせっかくだから\x01",
            "リースちゃんにも\x01",
            "投票したかったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x17,
        (
            "#04406Fさすがに市民でない私が\x01",
            "他の方と競うというのは、\x01",
            "違う気がしたもので……\x02\x03",

            "#04409Fですが、ありがとうございます。\x01",
            "お世辞でもうれしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        (
            "#00005F（うーん、投票できてたら\x01",
            "  結構な票が入った気がするけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#00202F（彼女はその辺無自覚ですよね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 1)
    Jump("loc_2965")

    label("loc_27AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CE")

    #C0111
    ChrTalk(
        0x17,
        (
            "#04402F投票については辞退させて\x01",
            "いただきましたが、\x01",
            "面白い試みだったと思います。\x02\x03",

            "#04404Fもぐもぐ……\x01",
            "こうして、立食パーティも\x01",
            "楽しむ事ができますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#00011F（持ってる皿に山のように\x01",
            "  料理が盛られてるんだが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        "#00109F（ふふ、さすがリースさんだわ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2965")

    label("loc_28CE")


    #C0114
    ChrTalk(
        0x17,
        (
            "#04404Fもぐもぐ……\x01",
            "私も、もう少ししたら\x01",
            "大聖堂の方に戻るつもりです。\x02\x03",

            "#04402F……しばらくは、この立食パーティを\x01",
            "堪能させていただくつもりですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2965")

    TalkEnd(0xFE)
    Return()

    # Function_23_25A9 end

    def Function_24_2969(): pass

    label("Function_24_2969")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev15001.eff")
    LoadEffect(0x1, "event\\ev290_03.eff")
    LoadChrToIndex("chr/ch20800.itc", 0x1F)
    LoadChrToIndex("chr/ch21200.itc", 0x20)
    LoadChrToIndex("apl/ch51257.itc", 0x21)
    LoadChrToIndex("chr/ch26100.itc", 0x22)
    LoadChrToIndex("apl/ch51547.itc", 0x24)
    LoadChrToIndex("chr/ch20200.itc", 0x25)
    LoadChrToIndex("chr/ch20700.itc", 0x26)
    LoadChrToIndex("chr/ch21100.itc", 0x27)
    LoadChrToIndex("chr/ch28000.itc", 0x28)
    LoadChrToIndex("chr/ch20000.itc", 0x29)
    LoadChrToIndex("chr/ch20100.itc", 0x2A)
    LoadChrToIndex("chr/ch20400.itc", 0x2B)
    SoundLoad(803)
    SoundLoad(821)
    SoundLoad(877)
    SoundLoad(818)
    SoundLoad(819)
    SoundLoad(820)
    SoundLoad(420)
    SoundLoad(421)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    OP_68(-5060, 1500, 1290, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(28100, 0)
    SetChrPos(0x10, -10190, 0, 7270, 90)
    SetChrPos(0x11, -10530, 0, 1180, 90)
    SetChrPos(0x12, -3480, 0, 2530, 340)
    SetChrPos(0x13, -2870, 0, -3210, 290)
    SetChrPos(0x14, -5740, 0, 3660, 70)
    SetChrPos(0x15, -4630, 0, 2520, 25)
    SetChrPos(0x16, 5000, 0, 2290, 270)
    SetChrPos(0x8, 3180, 0, 9920, 308)
    SetChrPos(0x9, 1230, 0, 9680, 0)
    SetChrChipByIndex(0x1D, 0x25)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 680, 0, 3780, 25)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 820, 0, 7140, 160)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -200, 0, 4660, 70)
    SetChrChipByIndex(0x20, 0x28)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -6170, 0, -3230, 70)
    SetChrChipByIndex(0x21, 0x29)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, -3630, 0, -4340, 335)
    SetChrChipByIndex(0x22, 0x2A)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, -5180, 0, -4080, 25)
    SetChrChipByIndex(0x23, 0x2B)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, -6160, 0, -1580, 115)
    BeginChrThread(0x1D, 0, 0, 0)
    BeginChrThread(0x1E, 0, 0, 0)
    BeginChrThread(0x1F, 0, 0, 0)
    BeginChrThread(0x20, 0, 0, 0)
    BeginChrThread(0x21, 0, 0, 0)
    BeginChrThread(0x22, 0, 0, 0)
    BeginChrThread(0x23, 0, 0, 0)
    BeginChrThread(0x1A, 0, 0, 0)
    BeginChrThread(0x1B, 0, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1460, 880, 10670, 180)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -3880, 0, 8840, 180)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -4600, 0, -520, 180)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3140, 0, 6130, 245)
    SetChrChipByIndex(0xD, 0x5)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2290, 0, 4950, 245)
    BeginChrThread(0x18, 0, 0, 0)
    BeginChrThread(0x1C, 0, 0, 0)
    BeginChrThread(0x19, 0, 0, 0)
    SetChrFlags(0x18, 0x8000)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -4880, 0, 5930, 155)
    SetChrChipByIndex(0x1C, 0x22)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, -230, 0, 6070, 110)
    SetChrFlags(0x19, 0x8000)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -2790, 0, -1720, 245)
    OP_4B(0xE, 0xFF)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 2900, 0, -2250, 290)
    SetChrPos(0x101, 3000, 0, -1000, 245)
    SetChrPos(0x102, 2000, 0, -3250, 335)
    SetChrPos(0x103, 550, 0, -3270, 20)
    SetChrPos(0x104, -400, 0, -2400, 65)
    SetChrPos(0x109, -550, 0, -970, 110)
    SetChrPos(0x105, 600, 0, 100, 155)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x1A, -5310, 0, 8840, 180)
    PlayBGM("ed7162", 0)
    Sound(821, 2, 60, 0)
    Sound(877, 2, 60, 0)
    FadeToBright(2000, 0)
    OP_68(-1240, 2250, 12460, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(29120, 0)
    Sleep(2000)
    OP_68(-1980, 1500, 6460, 10000)
    MoveCamera(62, 23, 0, 10000)
    OP_6E(380, 10000)
    Sleep(10000)
    Fade(500)
    OP_68(-5990, 1500, 630, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(29120, 0)
    OP_63(0x17, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)
    OP_95(0x17, -6030, 0, 980, 3000, 0x0)
    OP_95(0x17, -7300, 0, 1270, 3000, 0x0)
    Sleep(1000)
    OP_63(0x17, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(2000)

    def lambda_2EBD():
        OP_95(0xFE, -8350, 0, 6120, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2EBD)
    Sleep(1000)
    Fade(500)
    OP_68(1040, 1700, -1990, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21120, 0)
    OP_0D()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00003Fうーん……リースさん、\x01",
            "ずっと食べ歩いてるなぁ。\x02\x03",

            "#00012Fシスター服だから\x01",
            "余計に目立つというか。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#00109Fふふ……そうね。\x02\x03",

            "#00102Fでも、本当にこの料理は\x01",
            "おいしいわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#00302F市内の各飲食店が料理を\x01",
            "提供しているらしいしな。\x02\x03",

            "#00309Fあっちの方には《龍老飯店》の\x01",
            "激辛麻婆もあったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x109,
        (
            "#10109Fおおっ、それは\x01",
            "行かないといけませんね！\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xE,
        (
            "ふふ……\x01",
            "あなたたちって本当、仲がいいわね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30A2():

        label("loc_30A2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30A2")

    QueueWorkItem2(0x109, 0, lambda_30A2)

    def lambda_30B4():

        label("loc_30B4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30B4")

    QueueWorkItem2(0x102, 0, lambda_30B4)

    def lambda_30C6():

        label("loc_30C6")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30C6")

    QueueWorkItem2(0x104, 0, lambda_30C6)

    def lambda_30D8():

        label("loc_30D8")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30D8")

    QueueWorkItem2(0x101, 0, lambda_30D8)

    def lambda_30EA():

        label("loc_30EA")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30EA")

    QueueWorkItem2(0x105, 0, lambda_30EA)

    def lambda_30FC():

        label("loc_30FC")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_30FC")

    QueueWorkItem2(0x103, 0, lambda_30FC)

    #C0120
    ChrTalk(
        0xE,
        (
            "食事も本当に美味しいし、\x01",
            "イベントも大成功じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x105,
        (
            "#10304Fフフ……\x01",
            "そう上手くいけばいいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#00006Fこらこら……\x01",
            "せっかくのチャリティなのに、\x01",
            "不吉なことを言うなよな。\x02\x03",

            "#00000Fそれにしても先輩、\x01",
            "よくミスコンなんてものに\x01",
            "参加する気になりましたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x103,
        (
            "#00200F警察も、本部が襲撃されて\x01",
            "結構忙しいと思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xE,
        (
            "うーん、まあ……\x01",
            "誘われちゃった時は\x01",
            "私も迷ったンだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xE,
        (
            "ジョーリッジ課長から\x01",
            "是非とも参加するようにと\x01",
            "言われてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#00102Fふふ、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xE,
        (
            "私たちも、こういうときだから\x01",
            "市民により近い形で\x01",
            "何かがしたかったのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xE,
        (
            "ふふ、ある意味あなたたちの\x01",
            "マネがしたくなっちゃったのかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00002Fはは、俺たちは\x01",
            "そんな大したもんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(803, 2, 100, 0)
    Sleep(500)

    #C0130
    ChrTalk(
        0xE,
        (
            "あっ……私だわ。\x01",
            "ちょっとごめんなさいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0xE, 4600, 0, -1680, 2000, 0x0)
    OP_93(0xE, 0xB4, 0x1F4)
    OP_0D()
    Fade(250)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0xE, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0131
    ChrTalk(
        0xE,
        (
            "はい、こちらケイト巡査……\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "……はい、はい……\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xE,
        (
            "……そうですか、分かりました。\x01",
            "すぐに向かいます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(150)
    OP_95(0xE, 2900, 0, -2250, 2000, 0x0)

    #C0134
    ChrTalk(
        0x101,
        "#00005Fケイト先輩、今のって……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)

    #C0135
    ChrTalk(
        0xE,
        (
            "うーん……\x01",
            "悪いけど、外せない\x01",
            "急な仕事が入っちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xE,
        (
            "申し訳ないけど、\x01",
            "ちょっとミスコンには\x01",
            "出てられないわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#00306Fうはあっ、マジっすか！\x02\x03",

            "#00301Fいやまあ、仕事なら仕方ないわな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x104, 500)

    #C0138
    ChrTalk(
        0xE,
        (
            "ごめんね、\x01",
            "すぐにでも行かなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xE,
        (
            "ロイさんには謝っておいて\x01",
            "もらえるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#00000Fええ、分かりました。\x01",
            "お疲れ様です、先輩。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xE,
        "お疲れ様っ。\x02",
    )

    CloseMessageWindow()
    OP_68(760, 1700, -3000, 3000)
    BeginChrThread(0xE, 3, 0, 25)
    Sleep(4000)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x103, 0x0)
    OP_4B(0x1B, 0xFF)
    BeginChrThread(0x1B, 3, 0, 26)

    #C0142
    ChrTalk(
        0x102,
        (
            "#00106Fうーん、もう少し\x01",
            "話したかったけど\x01",
            "残念だったわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#00003Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_68(1040, 1700, -1990, 2000)
    MoveCamera(38, 23, 0, 2000)
    WaitChrThread(0x1B, 3)
    OP_6F(0x79)

    #C0144
    ChrTalk(
        0x1B,
        (
            "おおい、みんな。\x01",
            "楽しんでくれてるかい？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3799():

        label("loc_3799")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_3799")

    QueueWorkItem2(0x109, 0, lambda_3799)

    def lambda_37AB():

        label("loc_37AB")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37AB")

    QueueWorkItem2(0x102, 0, lambda_37AB)

    def lambda_37BD():

        label("loc_37BD")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37BD")

    QueueWorkItem2(0x104, 0, lambda_37BD)

    def lambda_37CF():

        label("loc_37CF")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37CF")

    QueueWorkItem2(0x101, 0, lambda_37CF)

    def lambda_37E1():

        label("loc_37E1")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37E1")

    QueueWorkItem2(0x105, 0, lambda_37E1)

    def lambda_37F3():

        label("loc_37F3")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_37F3")

    QueueWorkItem2(0x103, 0, lambda_37F3)

    #C0145
    ChrTalk(
        0x1B,
        (
            "そろそろミスコンが始まるから\x01",
            "参加者への声かけを\x01",
            "手伝ってくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x1B,
        (
            "……って、あれ？\x01",
            "ここにいた婦警さんは？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        "#00005Fええっと、実は……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ケイトに急な仕事が\x01",
            "入ってしまったことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x103, 0x0)

    #C0149
    ChrTalk(
        0x1B,
        "な、なんだってぇ～！？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x1B,
        (
            "う～ん、困ったぞ。\x01",
            "どうしたもんか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1B)
    OP_63(0x1B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x1B,
        "……そうだ！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x1B,
        (
            "あんたたちの誰かが、代わりに\x01",
            "『婦警』枠で出てくれないか？\x02",
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x101,
        "#00011Fえぇっ……！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x103,
        "#00205Fわたしたちから……？\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#00309Fはは、面白そうじゃねえか。\x02\x03",

            "せっかくだし\x01",
            "やってみたらいいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x109,
        "#10106Fせ、先輩、他人事だと思って……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x1B,
        "た、頼むよ！\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x1B,
        (
            "このチャリティイベントには、\x01",
            "復興支援の他にも、純粋に人々を\x01",
            "活気付ける意味もあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x1B,
        (
            "クロスベル市民たちのためにも……\x01",
            "どうかよろしくお願いするよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x109)

    #C0160
    ChrTalk(
        0x102,
        (
            "#00106F……ふう、それもそうですね。\x02\x03",

            "#00100Fみんな、いい？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x103,
        "#00203F……異論ないです。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x109,
        (
            "#10100Fあたしの本職は警備隊ですけど、\x01",
            "それでもいいなら……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x1B,
        "あ、ありがとう！\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x1B,
        (
            "それじゃあ……\x01",
            "誰がミスコンに出てくれるかな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0165
    ChrTalk(
        0x104,
        (
            "#00309Fそんじゃ、ロイド。\x01",
            "パッと選んでくれや。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D3E)

    def lambda_3D4B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3D4B)

    def lambda_3D58():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D58)

    def lambda_3D65():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D65)
    TurnDirection(0x101, 0x104, 500)

    #C0166
    ChrTalk(
        0x101,
        "#00011Fお、俺がか！？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、支援課のリーダーとして\x01",
            "当然の義務だと思うけど。\x02\x03",

            "#10302Fま、後腐れなく決めちゃいなよ。\x01",
            "時間もないみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00006Fそ、それもそうだな……\x02\x03",

            "#00003Fええっと、それじゃあ、\x01",
            "ミスコンに出てもらうのは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4833")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0169
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "誰がミスコンに出る？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "ロイド")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3ED1")
    MenuCmd(3, 0, 0x0)

    label("loc_3ED1")

    MenuCmd(1, 0, "エリィ")
    MenuCmd(1, 0, "ティオ")
    MenuCmd(1, 0, "ランディ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3EFE")
    MenuCmd(3, 0, 0x3)

    label("loc_3EFE")

    MenuCmd(1, 0, "ノエル")
    MenuCmd(1, 0, "ワジ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3F1D")
    MenuCmd(3, 0, 0x5)

    label("loc_3F1D")

    MenuCmd(2, 0, -1, 80, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F66"),
        (3, "loc_40E8"),
        (5, "loc_42A2"),
        (1, "loc_44FB"),
        (2, "loc_4601"),
        (4, "loc_4709"),
        (SWITCH_DEFAULT, "loc_482E"),
    )


    label("loc_3F66")

    TurnDirection(0x101, 0x104, 500)

    #C0170
    ChrTalk(
        0x101,
        (
            "#00001F……分かった。\x01",
            "そういうことなら俺が出よう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3FAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FAA)

    def lambda_3FB7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3FB7)

    def lambda_3FC4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3FC4)

    def lambda_3FD1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FD1)

    def lambda_3FDE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FDE)

    #C0171
    ChrTalk(
        0x102,
        "#00105Fえっ……ロイドが！？\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        "#00205F……女装でもするつもりですか。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        "#00309Fいやいや、案外似合うかもな？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x105,
        (
            "#10306Fうーん、微妙なセンだね。\x02\x03",

            "#10300F君、割と肩幅があるから\x01",
            "ちょっと工夫がいりそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        "#10114F（ドキドキ……）\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 0)
    Jump("loc_482E")

    label("loc_40E8")

    TurnDirection(0x101, 0x104, 500)

    #C0176
    ChrTalk(
        0x101,
        (
            "#00001F……ランディ。\x01",
            "出てくれないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4120():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4120)

    def lambda_412D():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_412D)

    def lambda_413A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_413A)

    def lambda_4147():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4147)

    def lambda_4154():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4154)

    #C0177
    ChrTalk(
        0x104,
        "#00305F……マ、マジでか。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x102,
        "#00101Fラ、ランディですって……？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00211F……いやな想像を\x01",
            "してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x105,
        (
            "#10306Fうーん、メイクと衣装しだいで\x01",
            "男装の麗人のように見えなくは\x01",
            "ないかもしれないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x109,
        (
            "#10106F流石にムチャですよ……\x01",
            "先輩大きいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#00306Fトホホ……\x01",
            "なんだよ、ウケ悪ィなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 1)
    Jump("loc_482E")

    label("loc_42A2")

    TurnDirection(0x101, 0x105, 500)

    #C0183
    ChrTalk(
        0x101,
        (
            "#00001F……ワジ。\x01",
            "出てくれないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42D6():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42D6)

    def lambda_42E3():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_42E3)

    def lambda_42F0():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_42F0)

    def lambda_42FD():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42FD)

    def lambda_430A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_430A)

    #C0184
    ChrTalk(
        0x105,
        (
            "#10302Fフフ……\x01",
            "僕は別に構わないけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        (
            "#00105Fちょ、ちょっとワジ君？\x01",
            "なんで反論しないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x105,
        (
            "#10309Fそりゃ、なんだか\x01",
            "面白そうだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x109,
        (
            "#10101Fロイドさんもロイドさんです！\x02\x03",

            "ま、まさかあたしたちより\x01",
            "ワジ君のほうが色気がある\x01",
            "なんて言うつもりじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        "#00011Fい、いや別にそんなつもりは……\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#00309Fははっ、ある意味\x01",
            "言えてるかもしれねえけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        (
            "#00203F……ランディさん、\x01",
            "黙るのと黙らせられるのと、\x01",
            "どっちがいいですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#00306F……スイマセンでした。\x02",
    )

    CloseMessageWindow()
    Call(0, 27)
    SetScenarioFlags(0x0, 2)
    Jump("loc_482E")

    label("loc_44FB")

    TurnDirection(0x101, 0x102, 500)

    #C0192
    ChrTalk(
        0x101,
        (
            "#00000F……エリィ。\x01",
            "出てくれないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4531():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4531)

    def lambda_453E():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_453E)

    def lambda_454B():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_454B)

    def lambda_4558():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4558)

    def lambda_4565():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4565)

    #C0193
    ChrTalk(
        0x102,
        (
            "#00112Fわ、私！？\x02\x03",

            "#00113Fうーん……\x01",
            "そ、そうね、分かったわ。\x02\x03",

            "#00100Fちょっと恥ずかしいけど……\x01",
            "やれるだけやってみる。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x6)
    SetScenarioFlags(0x19A, 1)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_482E")

    label("loc_4601")

    TurnDirection(0x101, 0x103, 500)

    #C0194
    ChrTalk(
        0x101,
        (
            "#00000F……ティオ。\x01",
            "出てくれないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4637():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4637)

    def lambda_4644():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4644)

    def lambda_4651():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4651)

    def lambda_465E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_465E)

    def lambda_466B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_466B)

    #C0195
    ChrTalk(
        0x103,
        (
            "#00205Fわ、わたしですか。\x02\x03",

            "#00204F………………\x01",
            "が、がってんです。\x02\x03",

            "#00201F多少、恥ずかしいですが\x01",
            "できるだけやってみます。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x7)
    SetScenarioFlags(0x19A, 2)
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_482E")

    label("loc_4709")

    TurnDirection(0x101, 0x109, 500)

    #C0196
    ChrTalk(
        0x101,
        (
            "#00000F……ノエル。\x01",
            "出てくれないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_473F():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_473F)

    def lambda_474C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_474C)

    def lambda_4759():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4759)

    def lambda_4766():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4766)

    def lambda_4773():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4773)

    #C0197
    ChrTalk(
        0x109,
        (
            "#10114Fあ、あたしですか！？\x01",
            "うーん……\x02\x03",

            "#10103F……りょ、了解しました！\x02\x03",

            "#10102Fあまりこういうのって\x01",
            "慣れてないんですけど……\x01",
            "できるだけがんばります！\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x8)
    SetScenarioFlags(0x19A, 3)
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_482E")

    label("loc_482E")

    Jump("loc_3E6E")

    label("loc_4833")


    #C0198
    ChrTalk(
        0x104,
        (
            "#00302Fはは、案外ステージに立てば\x01",
            "なんとかなるんじゃね？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x105,
        (
            "#10304Fまあ、戦闘や捜査の緊張感とは\x01",
            "質が違うとは思うけどね。\x02\x03",

            "#10302Fそれに、制服姿じゃないから\x01",
            "優勝を狙うには不利そうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x1B,
        (
            "まあ、『私服警官』としてなら\x01",
            "ひとまずの体裁は整うさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x1B,
        "婦警姿……惜しいんだけどな。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#00012F（妙な所に拘ってるなあ……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_4A3E")

    #C0203
    ChrTalk(
        0x109,
        (
            "#10102F今はとにかく、イベントを\x01",
            "成功させる事を考えましょう！\x02\x03",

            "#10109Fがんばってくださいね、エリィさん！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        "#00202Fふふ、応援してます。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        "#00102Fええ、なんとかやってみるわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BC7")

    label("loc_4A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4B05")

    #C0206
    ChrTalk(
        0x102,
        (
            "#00102F今はとにかく、イベントを\x01",
            "成功させる事を考えましょう。\x02\x03",

            "#00109Fがんばってね、ティオちゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x109,
        "#10109Fふふ、あたしも応援するから！\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        "#00201Fええ、なんとかやってみます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BC7")

    label("loc_4B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4BC7")

    #C0209
    ChrTalk(
        0x103,
        (
            "#00204F今はとにかく、イベントを\x01",
            "成功させる事を考えましょう。\x02\x03",

            "#00202Fがんばってください、ノエルさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        "#00109Fふふ、応援してるわね。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x109,
        "#10101Fええ、なんとかやってみせます！\x02",
    )

    CloseMessageWindow()

    label("loc_4BC7")


    #C0212
    ChrTalk(
        0x1B,
        (
            "──さあ、余り時間がない。\x01",
            "楽屋裏で段取りをおしえるぜ！\x02",
        )
    )

    CloseMessageWindow()
    StopSound(821, 2000, 50)
    StopSound(877, 2000, 50)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    OP_24(0x323)
    OP_24(0x335)
    OP_24(0x36D)
    Call(0, 28)
    Return()

    # Function_24_2969 end

    def Function_25_4C2E(): pass

    label("Function_25_4C2E")

    OP_95(0xFE, 3050, 0, -3910, 3000, 0x0)
    OP_95(0xFE, 1400, 0, -4710, 3000, 0x0)
    OP_95(0xFE, -1250, 0, -5460, 3000, 0x0)
    OP_95(0xFE, -940, 130, -7420, 3000, 0x0)
    OP_95(0xFE, 3690, 3560, -7710, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_4C2E end

    def Function_26_4C98(): pass

    label("Function_26_4C98")

    SetChrPos(0xFE, -3350, 0, 1340, 0)
    OP_95(0xFE, 1650, 0, 1870, 2000, 0x0)
    OP_95(0xFE, 3130, 0, 520, 2000, 0x0)
    TurnDirection(0xFE, 0x104, 500)
    Return()

    # Function_26_4C98 end

    def Function_27_4CD9(): pass

    label("Function_27_4CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D16")

    #C0213
    ChrTalk(
        0x1B,
        (
            "だぁー、何を真剣に\x01",
            "相談してるんだよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4D2A")

    label("loc_4D16")


    #C0214
    ChrTalk(
        0x1B,
        "だーかーらー！\x02",
    )

    CloseMessageWindow()

    label("loc_4D2A")


    #C0215
    ChrTalk(
        0x1B,
        (
            "これはミスコン！\x01",
            "男は出場できないんだよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x1B,
        (
            "以上、さっさと別の人から\x01",
            "選んでくれ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00011Fわ、分かりました。\x02\x03",

            "#00008Fええっと、\x01",
            "ミスコンに出てもらうのは……\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_27_4CD9 end

    def Function_28_4DD8(): pass

    label("Function_28_4DD8")

    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0x18, 0xFF)
    EndChrThread(0x1C, 0xFF)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x1A, 0xFF)
    SetChrPos(0xC, -4460, 750, 16000, 180)
    SetChrPos(0xD, -3460, 750, 16000, 180)
    SetChrPos(0x18, -2460, 750, 16000, 180)
    SetChrPos(0x1C, -1460, 750, 16000, 180)
    SetChrPos(0x19, -460, 750, 16000, 180)
    SetChrPos(0x17, 540, 750, 16000, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_4E93")
    LoadChrToIndex("chr/ch00155.itc", 0x1E)
    SetChrPos(0x102, 1540, 750, 16000, 180)
    Jump("loc_4ED8")

    label("loc_4E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_4EB8")
    LoadChrToIndex("chr/ch00255.itc", 0x1E)
    SetChrPos(0x103, 1540, 750, 16000, 180)
    Jump("loc_4ED8")

    label("loc_4EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_4ED8")
    LoadChrToIndex("chr/ch02955.itc", 0x1E)
    SetChrPos(0x109, 1540, 750, 16000, 180)

    label("loc_4ED8")

    SetChrFlags(0xF, 0x80)
    SetMapObjFlags(0x1, 0x4)
    OP_68(-1310, 7400, 11320, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19820, 0)
    OP_68(-1310, 2500, 11320, 5000)
    MoveCamera(0, 11, 0, 5000)
    SetCameraDistance(20760, 5000)
    FadeToBright(2000, 0)
    SetChrPos(0x1B, -5720, 750, 13840, 180)
    OP_95(0x1B, -1530, 750, 12520, 2000, 0x0)
    OP_93(0x1B, 0xB4, 0x12C)
    OP_95(0x1B, -1520, 880, 10600, 1000, 0x0)
    OP_6F(0x79)

    #C0218
    ChrTalk(
        0x1B,
        "レディース＆ジェントルメン！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x1B,
        (
            "皆様、長らくお待たせしました。\x01",
            "本日のメインプログラム──\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x1B,
        (
            "『ミス・クロスベルコンテスト\x01",
            "  　～働く女性よ、永遠に～　』を\x01",
            "開催したいと思います！！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sleep(1500)

    #C0221
    ChrTalk(
        0x1B,
        (
            "では、コンテストの流れを\x01",
            "説明させていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x1B,
        (
            "これから、参加者の皆様に\x01",
            "１人ずつ前に出てきてもらって、\x01",
            "アピールメッセージを言ってもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x1B,
        (
            "アピールメッセージは、\x01",
            "仕事中に使っている挨拶や\x01",
            "商売文句などを使ってもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x1B,
        (
            "観客の皆様はそれを参考に、\x01",
            "一番魅力的だと思う女性の名前を\x01",
            "お手元の投票用紙に記入してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x1B,
        (
            "投票数が一番多かった女性に、\x01",
            "『ミス・クロスベル』の称号を\x01",
            "差し上げたいと思います！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    #C0226
    ChrTalk(
        0x1B,
        (
            "──それでは、\x01",
            "早速始めていきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x1B,
        (
            "アピールターイム……\x01",
            "スタ──────トッ！\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    Fade(500)
    OP_68(-1450, 2250, 14880, 0)
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    OP_95(0x1B, -2180, 750, 13210, 3000, 0x0)
    OP_95(0x1B, -5730, 750, 13620, 3000, 0x0)
    OP_93(0x1B, 0x5A, 0x1F4)
    Sleep(500)

    #C0228
    ChrTalk(
        0x1B,
        "まずはエントリーナンバー１番！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x1B,
        (
            "百貨店《タイムズ》の看板娘、\x01",
            "清楚で可憐なデパートガール──\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x1B,
        "シンシアさん！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 0, 0, 29)
    WaitChrThread(0xC, 0)

    #C0231
    ChrTalk(
        0xC,
        "ようこそ、百貨店《タイムズ》へ。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "何か分からないことがありましたら\x01",
            "遠慮なくお申し付けくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xC, 0, 0, 31)
    Sleep(1000)

    #C0233
    ChrTalk(
        0x1B,
        "すばらしーーい！\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x1B,
        (
            "彼女の清楚な雰囲気に\x01",
            "ノックアウトされた人も\x01",
            "多いんじゃないでしょーか！\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x1B,
        (
            "ちなみに彼女、現在フリーだそう！\x01",
            "一体シンシアさんを手に入れる\x01",
            "幸せ者はどこのどいつだー！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 0)

    #C0236
    ChrTalk(
        0x1B,
        (
            "──さあ、どんどん参りましょう！\x01",
            "続いてエントリーナンバー２番！\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x1B,
        (
            "裏通りを舞う夜の蝶にして\x01",
            "妖艶な魅力を放つ一輪の薔薇──\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x1B,
        "アイリスさん！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 0, 0, 29)
    WaitChrThread(0xD, 0)

    #C0239
    ChrTalk(
        0xD,
        (
            "ご指名ありがと～！\x01",
            "あなたのアイリスよ～ん☆\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xD,
        (
            "今日もたっくさん飲んでいってね！\x01",
            "──ちゅっ㈱\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0xD, 0, 0, 32)
    Sleep(1000)

    #C0241
    ChrTalk(
        0x1B,
        (
            "ブラヴォォーーー！\x01",
            "まさかの投げキッスだあ！\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x1B,
        (
            "アイリスさんと飲めるお店は\x01",
            "裏通りにあるそうです！\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x1B,
        (
            "ただーし、お酒は大人になってから！\x01",
            "そこの所は気をつけて下さいネ！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xD, 0)

    #C0244
    ChrTalk(
        0x1B,
        (
            "──この勢いのまま、\x01",
            "エントリーナンバー３番！\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1B,
        (
            "東通りの老舗《龍老飯店》店員、\x01",
            "東方より舞い降りた天使──\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x1B,
        "サンサンちゃん！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x18, 0, 0, 29)
    WaitChrThread(0x18, 0)

    #C0247
    ChrTalk(
        0x18,
        (
            "いらっしゃ～い！\x01",
            "ようこそね、お客さんたち。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x18,
        (
            "パパの料理は天下一品ね。\x01",
            "たっくさん注文してよ～㈱\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x18, 0, 0, 33)
    Sleep(1000)

    #C0249
    ChrTalk(
        0x1B,
        (
            "キターーーーーー！\x01",
            "見よ、この屈託ない笑顔！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1B,
        (
            "看板娘、サンサンちゃんは\x01",
            "東通りでは有名な人気者！\x01",
            "かくいう私も大ファンだったり！\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x1B,
        (
            "ただーし、父上のチャンホイ氏は\x01",
            "サンサンちゃんにつく虫を許さない！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x1B,
        (
            "命を捨てる覚悟がある人だけ\x01",
            "挑戦して下さい！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 0)

    #C0253
    ChrTalk(
        0x1B,
        (
            "──さあ、折り返しの\x01",
            "エントリーナンバー４番！\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x1B,
        (
            "オーバルストア《ゲンテン》より、\x01",
            "麗しの女性オーブメント職人──\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x1B,
        "ウェンディさん！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1C, 0, 0, 29)
    WaitChrThread(0x1C, 0)

    #C0256
    ChrTalk(
        0x1C,
        (
            "……んーと、コホン。\x01",
            "私はあんまし気の利いたことは\x01",
            "言えないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x1C,
        (
            "導力器が壊れたりしたら、\x01",
            "いつでも頼ってちょうだいね！\x02",
        )
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x1C, 0, 0, 34)
    Sleep(1000)

    #C0258
    ChrTalk(
        0x1B,
        (
            "頼もしーい！\x01",
            "これが彼女の持ち味、\x01",
            "そして魅力と言えるでしょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1B,
        (
            "彼女に会うために、\x01",
            "わざと導力器を壊したり\x01",
            "しないように！\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x1B,
        (
            "彼女のスパナで\x01",
            "コツンとお仕置きされちゃいますよ！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1C, 0)

    #C0261
    ChrTalk(
        0x1B,
        (
            "さてさて、あっというまに\x01",
            "エントリーナンバー５番！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x1B,
        (
            "クロスベル自治州議会の長、\x01",
            "ヘンリー・マクダエル議長に\x01",
            "仕える健気なメイド──\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1B,
        "ジョアンナさん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x19, 0, 0, 30)
    WaitChrThread(0x19, 0)
    OP_64(0x19)

    #C0264
    ChrTalk(
        0x19,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x19,
        (
            "………………あ、あの…………\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x19)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0266
    ChrTalk(
        0x19,
        (
            "お、お帰りなさいませ旦那様。\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x19,
        "…………………し、失礼します。\x02",
    )

    CloseMessageWindow()
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x19, 0, 0, 35)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x1B,
        "お、おおおおお……！\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x1B,
        (
            "なんだか新鮮な気持ちになりました！\x01",
            "こんなメイドさんもいいですね！\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x1B,
        (
            "会場のみなさんの何人かは、\x01",
            "マクダエル議長が憎らしくすら\x01",
            "思えてきたんじゃないでしょうか！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5D22")
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5D22")

    Sleep(1000)
    WaitChrThread(0x19, 0)

    #C0271
    ChrTalk(
        0x1B,
        (
            "さあ、終盤にさしかかりました！\x01",
            "エントリーナンバー６番！\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x1B,
        (
            "空の女神に仕えし\x01",
            "清らかなる新入りシスター──\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x1B,
        "リースさん！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x17, 0, 0, 30)
    WaitChrThread(0x17, 0)
    Fade(250)
    Sound(802, 0, 90, 0)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    OP_A1(0x17, 0x5DC, 0x4, 0x3, 0x2, 0x1, 0x0)
    Sleep(500)

    #A0274
    AnonymousTalk(
        0x17,
        (
            "七耀の教えは\x01",
            "人々の心の中にあります。\x02\x03",

            "皆様に女神の加護と導きを……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(500)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)
    BeginChrThread(0x17, 0, 0, 36)
    Sleep(1000)

    #C0275
    ChrTalk(
        0x1B,
        (
            "おお、おおおお……！\x01",
            "なんと神々しいお姿でしょうか！\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x1B,
        (
            "先ほどまで立食パーティを\x01",
            "練り歩いていた姿との\x01",
            "ギャップもまたイイですね！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0)

    #C0277
    ChrTalk(
        0x1B,
        (
            "それでは、いよいよ最後の方です！\x01",
            "エントリーナンバー７番！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_5F7D")

    #C0278
    ChrTalk(
        0x1B,
        (
            "警察・特務支援課に所属する、\x01",
            "由緒正しき麗しのお嬢様──\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x1B,
        "エリィ・マクダエルさん！\x02",
    )

    CloseMessageWindow()
    Jump("loc_604C")

    label("loc_5F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_5FEA")

    #C0280
    ChrTalk(
        0x1B,
        (
            "警察・特務支援課に所属する、\x01",
            "静かなるオーラをまとう少女──\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x1B,
        "ティオ・プラトーちゃん！\x02",
    )

    CloseMessageWindow()
    Jump("loc_604C")

    label("loc_5FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_604C")

    #C0282
    ChrTalk(
        0x1B,
        (
            "警察・特務支援課に出向中、\x01",
            "折り目正しき女性警備隊員──\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x1B,
        "ノエル・シーカーさん！\x02",
    )

    CloseMessageWindow()

    label("loc_604C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6064")
    BeginChrThread(0x102, 0, 0, 30)
    WaitChrThread(0x102, 0)
    Jump("loc_608F")

    label("loc_6064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_607C")
    BeginChrThread(0x103, 0, 0, 30)
    WaitChrThread(0x103, 0)
    Jump("loc_608F")

    label("loc_607C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_608F")
    BeginChrThread(0x109, 0, 0, 30)
    WaitChrThread(0x109, 0)

    label("loc_608F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_627A")

    #C0284
    ChrTalk(
        0x102,
        (
            "#00105F（ええと……\x01",
            "  確かアピールメッセージを\x01",
            "  言わなきゃいけないのよね。）\x02\x03",

            "#00103F（何を言おうかしら？）\x02",
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
            "逮捕の宣言でアピール\x01",      # 0
            "銃の腕前でアピール\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x102, 0x2)
    OP_A1(0x102, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_A1(0x102, 0x640, 0x6, 0x0, 0x0, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0x102, 0x640, 0x8, 0x7, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_61C4"),
        (1, "loc_621E"),
        (SWITCH_DEFAULT, "loc_6275"),
    )


    label("loc_61C4")

    SetScenarioFlags(0x19A, 4)

    #C0285
    ChrTalk(
        0x102,
        (
            "#00107F──手を上げて！\x02\x03",

            "自治州法に基づき、\x01",
            "諸々の罪状であなたを逮捕します！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6275")

    label("loc_621E")


    #C0286
    ChrTalk(
        0x102,
        (
            "#00104F──ふぅっ……百発百中ね。\x02\x03",

            "#00101F逃げられると思ったら、大間違いよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6275")

    label("loc_6275")

    Jump("loc_66FD")

    label("loc_627A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_64D6")

    #C0287
    ChrTalk(
        0x103,
        (
            "#00200F（さて……\x01",
            "  確かアピールメッセージを\x01",
            "  言う必要があるとか。）\x02\x03",

            "#00203F（何を言うべきでしょうか？）\x02",
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
            "逮捕の宣言でアピール\x01",            # 0
            "エイオンシステムでアピール\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x103, 0x2)
    OP_A1(0x103, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(533, 0, 80, 0)
    OP_A1(0x103, 0x640, 0x5, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_A1(0x103, 0x640, 0x3, 0x8, 0x9, 0xA)
    Sound(337, 0, 70, 0)
    OP_A1(0x103, 0x640, 0x5, 0xB, 0xC, 0xD, 0xE, 0xF)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_63C6"),
        (1, "loc_644C"),
        (SWITCH_DEFAULT, "loc_64D1"),
    )


    label("loc_63C6")

    SetScenarioFlags(0x19A, 4)

    #C0288
    ChrTalk(
        0x103,
        (
            "#00203F──データ収集、完了しました。\x01",
            "犯人は……あなたです。\x02\x03",

            "#00201Fもはや逃れられません。\x01",
            "おとなしく、ご同行願います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D1")

    label("loc_644C")


    #C0289
    ChrTalk(
        0x103,
        (
            "#00203F──《エイオンシステム》作動……\x01",
            "導力フィールドを高速展開。\x02\x03",

            "#00201Fこの魔導状の性能……\x01",
            "とくとご覧にいれましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64D1")

    label("loc_64D1")

    Jump("loc_66FD")

    label("loc_64D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_66FD")

    #C0290
    ChrTalk(
        0x109,
        (
            "#10105F（えっと……\x01",
            "  確かアピールメッセージを\x01",
            "  言わなきゃいけないはず。）\x02\x03",

            "#10103F（何を言おうかな？）\x02",
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
            "逮捕の宣言でアピール\x01",        # 0
            "警備隊の号令でアピール\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x109, 0x2)
    OP_A1(0x109, 0x640, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_A1(0x109, 0x640, 0x5, 0x3, 0x3, 0x4, 0x5, 0x6)
    OP_A1(0x109, 0x640, 0x5, 0x7, 0x7, 0x8, 0x9, 0xA)
    Sound(590, 0, 100, 0)
    OP_A1(0x109, 0x640, 0x5, 0xB, 0xC, 0xD, 0xC, 0xB)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6618"),
        (1, "loc_6685"),
        (SWITCH_DEFAULT, "loc_66FD"),
    )


    label("loc_6618")

    SetScenarioFlags(0x19A, 4)

    #C0291
    ChrTalk(
        0x109,
        (
            "#10101F──完全に包囲しました……\x01",
            "もはや逃げ場はありません！\x02\x03",

            "#10107F速やかに投降してください！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66FD")

    label("loc_6685")


    #C0292
    ChrTalk(
        0x109,
        (
            "#10101F──目標、敵機甲部隊の迎撃及び、\x01",
            "孤立した補給部隊の救出！\x02\x03",

            "#10107F戦闘開始#7Rオープンコンバット#ッ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66FD")

    label("loc_66FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_6775")
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)

    #C0293
    ChrTalk(
        0x1B,
        (
            "おお……\x01",
            "ブラボーーーーーーー！\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x1B,
        (
            "これぞ、婦警さんというものを\x01",
            "見せていただきました！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67D7")

    label("loc_6775")

    Sound(819, 0, 100, 0)
    Sound(820, 0, 80, 0)

    #C0295
    ChrTalk(
        0x1B,
        (
            "おお……\x01",
            "ブラボーーーーーーー！\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x1B,
        (
            "えーっと、いいものを見せて\x01",
            "いただきました！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_683E")

    #C0297
    ChrTalk(
        0x102,
        (
            "#00106F（う、うーん……\x01",
            "  警察官らしいことを\x01",
            "  言うべきだったかしら……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68EE")

    label("loc_683E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_689A")

    #C0298
    ChrTalk(
        0x103,
        (
            "#00206F（……もう少し警察官らしい事を\x01",
            "  言うべきだったかもしれません。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68EE")

    label("loc_689A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_68EE")

    #C0299
    ChrTalk(
        0x109,
        (
            "#10106F（しまった……\x01",
            "  警察官らしいことを\x01",
            "  言うべきだったかも……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_6919")
    Fade(250)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    BeginChrThread(0x102, 0, 0, 37)
    WaitChrThread(0x102, 0)
    Jump("loc_696A")

    label("loc_6919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_6944")
    Fade(250)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    BeginChrThread(0x103, 0, 0, 37)
    WaitChrThread(0x103, 0)
    Jump("loc_696A")

    label("loc_6944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_696A")
    Fade(250)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    BeginChrThread(0x109, 0, 0, 37)
    WaitChrThread(0x109, 0)

    label("loc_696A")


    #C0300
    ChrTalk(
        0x1B,
        (
            "これで全７名の\x01",
            "アピールタイムを終了します！\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x1B,
        (
            "参加者のみなさまに\x01",
            "今一度盛大な拍手を！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    Sound(821, 2, 60, 0)
    Sound(877, 2, 60, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、観客たちによって\x01",
            "ミスコンの投票が行われた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "シスター・リースが投票前に、\x01",
            "クロスベル市民でないことを理由に\x01",
            "自ら投票を辞退したため……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それ以外の参加者の中から\x01",
            "優勝者が選ばれる運びになった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0305
    AnonymousTalk(
        0x101,
        (
            "#00000F（さてと、俺も投票用紙を\x01",
            "  もらってきたけど……\x01",
            "  仲間に入れるのもなんだよな。）\x02\x03",

            "#00003F（……それじゃ、誰に入れようか？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "シンシアに投票する\x01",        # 0
            "アイリスに投票する\x01",        # 1
            "サンサンに投票する\x01",        # 2
            "ウェンディに投票する\x01",      # 3
            "ジョアンナに投票する\x01",      # 4
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6C1F"),
        (1, "loc_6C5D"),
        (2, "loc_6C9B"),
        (3, "loc_6CDB"),
        (4, "loc_6D17"),
        (SWITCH_DEFAULT, "loc_6D57"),
    )


    label("loc_6C1F")


    #A0306
    AnonymousTalk(
        0x101,
        "#00002F（よし……シンシアさんに投票しよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x9)
    Jump("loc_6D57")

    label("loc_6C5D")


    #A0307
    AnonymousTalk(
        0x101,
        "#00002F（よし……アイリスさんに投票しよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xA)
    Jump("loc_6D57")

    label("loc_6C9B")


    #A0308
    AnonymousTalk(
        0x101,
        "#00002F（よし……サンサンちゃんに投票しよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xB)
    Jump("loc_6D57")

    label("loc_6CDB")


    #A0309
    AnonymousTalk(
        0x101,
        "#00002F（よし……ウェンディに投票しよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xC)
    Jump("loc_6D57")

    label("loc_6D17")


    #A0310
    AnonymousTalk(
        0x101,
        "#00002F（よし……ジョアンナさんに投票しよう。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0xD)
    Jump("loc_6D57")

    label("loc_6D57")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0311
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──そして……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-1450, 2250, 14880, 0)
    StopSound(821, 2000, 50)
    StopSound(877, 2000, 50)
    StopBGM(0x7D0)
    WaitBGM()
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0xF, 0x17, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, -1450, 880, 10860, 180)
    SetChrPos(0x1B, -190, 750, 13500, 180)
    FadeToBright(2000, 0)
    OP_0D()

    #C0312
    ChrTalk(
        0x1A,
        (
            "先ほど行われたミスコンの\x01",
            "結果発表を持ってこの場を\x01",
            "締めさせていただきたいと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x0, 0x1F4)
    OP_95(0x1A, -1450, 750, 12450, 2000, 0x0)
    OP_95(0x1A, 1620, 750, 12450, 2000, 0x0)
    OP_93(0x1A, 0xE0, 0x1F4)
    OP_95(0x1B, -1450, 750, 13500, 2000, 0x0)
    OP_93(0x1B, 0xB4, 0x12C)
    OP_95(0x1B, -1450, 880, 11370, 2000, 0x0)
    Sleep(1000)

    #C0313
    ChrTalk(
        0x1B,
        "第１回、ミス・クロスベルコンテスト。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x1B,
        "栄えある優勝に輝いたのは……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(420, 1, 80, 0)
    SetChrFlags(0x101, 0x48)
    SetChrFlags(0x105, 0x48)
    BeginChrThread(0x101, 1, 0, 38)
    BeginChrThread(0x105, 1, 0, 38)
    SetChrPos(0x101, 1540, 750, 16000, 180)
    SetChrPos(0x105, -4460, 750, 16000, 180)

    def lambda_6F89():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6F89)

    def lambda_6FA3():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6FA3)

    def lambda_6FBD():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_6FBD)
    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    WaitChrThread(0x101, 0)

    def lambda_6FE2():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6FE2)

    def lambda_6FFC():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6FFC)
    WaitChrThread(0x101, 0)

    def lambda_701A():
        OP_96(0xFE, 0xFFFFEE94, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_701A)

    def lambda_7034():
        OP_96(0xFE, 0x604, 0x2EE, 0x3E80, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7034)
    WaitChrThread(0x101, 0)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x105, 0x1)
    StopEffect(0x1, 0x0)
    Sleep(1000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    OP_11(0x0, 0x0, 0x0, 0x10, 0x1E, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_70BA"),
        (1, "loc_71CF"),
        (2, "loc_72DA"),
        (3, "loc_73EB"),
        (4, "loc_7507"),
        (SWITCH_DEFAULT, "loc_7626"),
    )


    label("loc_70BA")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xC, 1, 0, 38)

    def lambda_70CE():

        label("loc_70CE")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_70CE")

    QueueWorkItem2(0x1B, 1, lambda_70CE)

    #C0315
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー１番！\x01",
            "シンシアさんです！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0xC, 0, 0, 39)
    WaitChrThread(0xC, 0)
    EndChrThread(0xC, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0316
    ChrTalk(
        0x1B,
        (
            "優勝者には記念の盾が授与されます。\x01",
            "……どうぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xC,
        "ふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xC, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_71CF")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0xD, 1, 0, 38)

    def lambda_71E3():

        label("loc_71E3")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_71E3")

    QueueWorkItem2(0x1B, 1, lambda_71E3)

    #C0318
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー２番！\x01",
            "アイリスさんです！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0xD, 0, 0, 39)
    WaitChrThread(0xD, 0)
    EndChrThread(0xD, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0319
    ChrTalk(
        0x1B,
        (
            "優勝者には記念の盾が授与されます。\x01",
            "……どうぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xD,
        "うふふ、アリガト㈱\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0xD, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_72DA")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x18, 1, 0, 38)

    def lambda_72EE():

        label("loc_72EE")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_72EE")

    QueueWorkItem2(0x1B, 1, lambda_72EE)

    #C0321
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー３番！\x01",
            "サンサンちゃんです！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x18, 0, 0, 39)
    WaitChrThread(0x18, 0)
    EndChrThread(0x18, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0322
    ChrTalk(
        0x1B,
        (
            "優勝者には記念の盾が授与されます。\x01",
            "……どうぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x18,
        "えへへ、ありがとね～。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x18, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x18, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_73EB")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x1C, 1, 0, 38)

    def lambda_73FF():

        label("loc_73FF")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_73FF")

    QueueWorkItem2(0x1B, 1, lambda_73FF)

    #C0324
    ChrTalk(
        0x1C,
        (
            "#4S──エントリーナンバー４番！\x01",
            "ウェンディさんです！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    OP_24(0x1A4)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x1C, 0, 0, 39)
    WaitChrThread(0x1C, 0)
    EndChrThread(0x1C, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0325
    ChrTalk(
        0x1B,
        (
            "優勝者には記念の盾が授与されます。\x01",
            "……どうぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x1C,
        "あはは、いいの？　ありがと～。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x1C, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_7507")

    Sound(421, 0, 80, 0)
    OP_24(0x1A4)
    BeginChrThread(0x19, 1, 0, 38)

    def lambda_751B():

        label("loc_751B")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_751B")

    QueueWorkItem2(0x1B, 1, lambda_751B)

    #C0327
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー５番！\x01",
            "ジョアンナさんです！\x02",
        )
    )

    CloseMessageWindow()
    Sound(818, 0, 100, 0)
    Sound(820, 0, 100, 0)
    PlayBGM("ed7565", 0)
    BeginChrThread(0x19, 0, 0, 39)
    WaitChrThread(0x19, 0)
    EndChrThread(0x19, 0x1)
    StopEffect(0x1, 0x0)
    OP_96(0x1B, 0xFFFFFC40, 0x370, 0x2C6A, 0x3E8, 0x0)

    #C0328
    ChrTalk(
        0x1B,
        (
            "優勝者には記念の盾が授与されます。\x01",
            "……どうぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x19,
        "あ、あの、ありがとう……ございます。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_93(0x19, 0xB4, 0x1F4)
    Jump("loc_7626")

    label("loc_7626")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 4)), scpexpr(EXPR_END)), "loc_7AA3")
    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    #C0330
    ChrTalk(
        0x1B,
        (
            "そして今回は、特別枠として\x01",
            "審査員特別賞をご用意しました！\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76AF"),
        (1, "loc_76CF"),
        (2, "loc_76EF"),
        (3, "loc_770F"),
        (4, "loc_772F"),
        (SWITCH_DEFAULT, "loc_774F"),
    )


    label("loc_76AF")

    OP_96(0xC, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xC, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_76CF")

    OP_96(0xD, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0xD, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_76EF")

    OP_96(0x18, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x18, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_770F")

    OP_96(0x1C, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x1C, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_772F")

    OP_96(0x19, 0xFFFFF63C, 0x2EE, 0x2EE0, 0x3E8, 0x0)
    OP_93(0x19, 0x87, 0x1F4)
    Jump("loc_774F")

    label("loc_774F")

    OP_2C(0x8F, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_77B0")
    BeginChrThread(0x102, 1, 0, 38)

    def lambda_7768():

        label("loc_7768")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_7768")

    QueueWorkItem2(0x1B, 0, lambda_7768)

    #C0331
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー７番！\x01",
            "エリィさんです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7863")

    label("loc_77B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_780C")
    BeginChrThread(0x103, 1, 0, 38)

    def lambda_77C4():

        label("loc_77C4")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_77C4")

    QueueWorkItem2(0x1B, 0, lambda_77C4)

    #C0332
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー７番！\x01",
            "ティオさんです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7863")

    label("loc_780C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7863")
    BeginChrThread(0x109, 1, 0, 38)

    def lambda_7820():

        label("loc_7820")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_7820")

    QueueWorkItem2(0x1B, 0, lambda_7820)

    #C0333
    ChrTalk(
        0x1B,
        (
            "#4S──エントリーナンバー７番！\x01",
            "ノエルさんです！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7863")

    OP_96(0x1B, 0xFFFFFE0C, 0x370, 0x2C6A, 0x3E8, 0x0)
    Sound(818, 0, 80, 0)
    Sound(820, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_78A2")
    BeginChrThread(0x102, 0, 0, 40)
    WaitChrThread(0x102, 0)
    EndChrThread(0x102, 0x1)
    Jump("loc_78D5")

    label("loc_78A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_78BE")
    BeginChrThread(0x103, 0, 0, 40)
    WaitChrThread(0x103, 0)
    EndChrThread(0x103, 0x1)
    Jump("loc_78D5")

    label("loc_78BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_78D5")
    BeginChrThread(0x109, 0, 0, 40)
    WaitChrThread(0x109, 0)
    EndChrThread(0x109, 0x1)

    label("loc_78D5")

    StopEffect(0x1, 0x0)

    #C0334
    ChrTalk(
        0x1B,
        (
            "特別賞の方にも、\x01",
            "記念の盾が授与されます。\x01",
            "……どうぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 1)), scpexpr(EXPR_END)), "loc_799F")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0335
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x341, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0336
    ChrTalk(
        0x102,
        "#00109Fふふ、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xB4, 0x1F4)
    Jump("loc_7A98")

    label("loc_799F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 2)), scpexpr(EXPR_END)), "loc_7A1E")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0337
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x342, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0338
    ChrTalk(
        0x103,
        "#00205F……ど、どうも。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0xB4, 0x1F4)
    Jump("loc_7A98")

    label("loc_7A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19A, 3)), scpexpr(EXPR_END)), "loc_7A98")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0339
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x343, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0340
    ChrTalk(
        0x109,
        "#10109Fふふ、恐縮です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0xB4, 0x1F4)

    label("loc_7A98")

    EndChrThread(0x1B, 0xFF)
    OP_93(0x1B, 0xB4, 0x1F4)

    label("loc_7AA3")

    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0xB4, 0x0)
    OP_93(0x18, 0xB4, 0x0)
    OP_93(0x1C, 0xB4, 0x0)
    OP_93(0x19, 0xB4, 0x0)
    OP_93(0x17, 0xB4, 0x0)
    Fade(500)
    Fade(500)
    OP_11(0x0, 0x0, 0x0, 0x10, 0x1E, 0x0)
    StopEffect(0x0, 0x0)
    ClearMapFlags(0x10)
    OP_0D()
    Sleep(500)

    #C0341
    ChrTalk(
        0x1B,
        (
            "それでは、これにて\x01",
            "ミス・クロスベルコンテストを\x01",
            "終了いたします！\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x1B,
        (
            "この後、立食パーティが\x01",
            "再開されますので、皆様は引き続き\x01",
            "イベントをお楽しみください！\x02",
        )
    )

    CloseMessageWindow()
    OP_6E(580, 3000)
    Sound(819, 0, 100, 0)
    Sound(820, 0, 100, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrName("")

    #A0343
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして、チャリティイベントの\x01",
            "ミスコンは幕を閉じたのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    WaitBGM()
    OP_0D()
    OP_24(0x335)
    OP_24(0x36D)
    SetScenarioFlags(0x22, 1)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_4DD8 end

    def Function_29_7C19(): pass

    label("Function_29_7C19")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x10E, 0x3E8)
    OP_93(0xFE, 0x0, 0x3E8)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_93(0xFE, 0xB4, 0x3E8)
    Sleep(1000)
    Return()

    # Function_29_7C19 end

    def Function_30_7C57(): pass

    label("Function_30_7C57")

    OP_95(0xFE, -1460, 750, 12650, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    Return()

    # Function_30_7C57 end

    def Function_31_7C76(): pass

    label("Function_31_7C76")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -4460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_31_7C76 end

    def Function_32_7CA7(): pass

    label("Function_32_7CA7")

    OP_63(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -3460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_7CA7 end

    def Function_33_7CDB(): pass

    label("Function_33_7CDB")

    OP_63(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_95(0xFE, -2460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_7CDB end

    def Function_34_7D0F(): pass

    label("Function_34_7D0F")

    OP_95(0xFE, -1460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_34_7D0F end

    def Function_35_7D2B(): pass

    label("Function_35_7D2B")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -460, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_64(0xFE)
    Return()

    # Function_35_7D2B end

    def Function_36_7D5C(): pass

    label("Function_36_7D5C")

    OP_95(0xFE, 540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_36_7D5C end

    def Function_37_7D78(): pass

    label("Function_37_7D78")

    OP_95(0xFE, 1540, 750, 16000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_37_7D78 end

    def Function_38_7D94(): pass

    label("Function_38_7D94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7DDE")
    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3200)
    Jump("Function_38_7D94")

    label("loc_7DDE")

    Return()

    # Function_38_7D94 end

    def Function_39_7DDF(): pass

    label("Function_39_7DDF")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, -1910, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_39_7DDF end

    def Function_40_7E19(): pass

    label("Function_40_7E19")

    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(1000)
    OP_95(0xFE, 800, 750, 14930, 3000, 0x0)
    OP_95(0xFE, -1500, 750, 13910, 2000, 0x0)
    OP_95(0xFE, -1500, 880, 11420, 3000, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_40_7E19 end

    def Function_41_7E7B(): pass

    label("Function_41_7E7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1500, 900, 14300, 180)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    OP_68(-1500, 2500, 14000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_41_7E7B end

    def Function_42_7FB0(): pass

    label("Function_42_7FB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    LoadChrToIndex("chr/ch27702.itc", 0x1E)
    LoadChrToIndex("chr/ch27500.itc", 0x1F)
    LoadChrToIndex("chr/ch27802.itc", 0x20)
    LoadChrToIndex("chr/ch27600.itc", 0x21)
    LoadChrToIndex("chr/ch25900.itc", 0x22)
    LoadChrToIndex("chr/ch27502.itc", 0x23)
    LoadChrToIndex("chr/ch27602.itc", 0x24)
    LoadChrToIndex("chr/ch44202.itc", 0x25)
    LoadChrToIndex("chr/ch21002.itc", 0x26)
    LoadChrToIndex("chr/ch20302.itc", 0x27)
    SoundLoad(851)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x24, 2230, 900, 12630, 252)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    EndChrThread(0x24, 0x0)
    SetChrBattleFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x25, 2280, 750, 14110, 252)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x26, -5210, 900, 12820, 107)
    SetChrChipByIndex(0x26, 0x20)
    SetChrSubChip(0x26, 0x0)
    EndChrThread(0x26, 0x0)
    SetChrBattleFlags(0x26, 0x4)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x27, -3140, 750, 13930, 110)
    SetChrChipByIndex(0x27, 0x21)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x28, -340, 750, 14570, 180)
    SetChrChipByIndex(0x28, 0x22)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x1E, -5800, 150, 7350, 0)
    SetChrChipByIndex(0x1E, 0x26)
    SetChrSubChip(0x1E, 0x0)
    EndChrThread(0x1E, 0x0)
    SetChrBattleFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1F, -4000, 150, 7350, 0)
    SetChrChipByIndex(0x1F, 0x27)
    SetChrSubChip(0x1F, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrBattleFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x20, -2250, 150, 7350, 0)
    SetChrChipByIndex(0x20, 0x23)
    SetChrSubChip(0x20, 0x0)
    EndChrThread(0x20, 0x0)
    SetChrBattleFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x21, -450, 150, 7350, 0)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    EndChrThread(0x21, 0x0)
    SetChrBattleFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x22, 1250, 150, 7350, 0)
    SetChrChipByIndex(0x22, 0xE)
    SetChrSubChip(0x22, 0x0)
    EndChrThread(0x22, 0x0)
    SetChrBattleFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x23, 2930, 150, 7350, 0)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    EndChrThread(0x23, 0x0)
    SetChrBattleFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x15, 6880, 4000, 7260, 315)
    SetChrChipByIndex(0x15, 0xA)
    SetChrFlags(0x15, 0x8000)
    EndChrThread(0x15, 0x0)
    SetChrPos(0x16, 6880, 4000, -610, 315)
    SetChrChipByIndex(0x16, 0xC)
    SetChrFlags(0x16, 0x8000)
    OP_68(2390, 1500, -520, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(32530, 0)
    Sound(851, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_68(-1450, 2250, 12090, 5000)
    MoveCamera(40, 23, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(30820, 5000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-1450, 2250, 12090, 0)
    MoveCamera(28, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22540, 0)
    OP_0D()
    Sleep(500)

    #C0344
    ChrTalk(
        0x26,
        (
            "外国人、とりわけ帝国人と共和国人を\x01",
            "優遇する不平等な法体制！\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x26,
        (
            "市民の血税の１０％をも\x01",
            "２大国に納めねばならぬ取り決め！\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x26,
        (
            "どう考えても\x01",
            "おかしいとは思わないのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x27,
        (
            "我々が今、立ち上がらなければ\x01",
            "この状況は未来永劫に渡って\x01",
            "続くんですよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x27,
        "本当にそれでいいんですか！？\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x25,
        "……フン、馬鹿馬鹿しい。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x25,
        (
            "現実問題として、力が伴わなければ\x01",
            "国家独立など絵に描いた餅にすぎん。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x25,
        (
            "いざ他国の大軍が侵攻してきたら\x01",
            "戦車も持たない警備隊でどう防ぐのだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x26,
        (
            "その他国というのはどう考えても\x01",
            "エレボニア帝国のことだろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x26,
        (
            "西のガレリア要塞に《列車砲》なる\x01",
            "クロスベル市を狙える大量破壊兵器が\x01",
            "配備されているのは周知の事実だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x27,
        (
            "戦車にしても、軍用飛行艇にしても\x01",
            "クロスベルの豊かな財政なら\x01",
            "十分に配備することが可能です！\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x27,
        (
            "重要なのは我々の\x01",
            "決断なのではありませんか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x25,
        (
            "判らん連中だな……\x01",
            "現実を見ろと言っているのだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x25,
        (
            "第一、クロスベルの繁栄は\x01",
            "帝国と共和国から流れ込んでくる\x01",
            "ミラに負うところが大きいのだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x25,
        (
            "独立などして壁を作ってしまったら\x01",
            "その富も消えるかもしれんのだぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x24,
        "まあまあ、皆さん落ち着いて。\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x24,
        (
            "……いずれにしても問題は、\x01",
            "このような強引な独立提言を\x01",
            "国際社会が容認するかどうかにある。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x24,
        "その議論が欠けているのではないかね？\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x26,
        "この際、国際社会は関係ない！\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x26,
        (
            "クロスベルの国家独立こそ\x01",
            "“正義”を実現する唯一無二の道！\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x27,
        (
            "所詮あなたもカルバードの\x01",
            "都合のいい代弁者に過ぎないわけか！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x24,
        (
            "た、確かに私は\x01",
            "共和国派などと呼ばれてはいるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x24,
        (
            "クロスベルを愛する心にかけては\x01",
            "誰にも負けない自信はあるつもりだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x24,
        "その言葉、訂正してもらおうか！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(6040, 5500, -5410, 0)
    MoveCamera(29, 31, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21420, 0)
    SetChrPos(0x101, 6940, 4000, -3750, 315)
    SetChrPos(0x103, 6910, 4000, -4960, 315)
    SetChrPos(0x102, 8010, 4000, -4600, 315)
    SetChrPos(0x109, 7960, 4000, -5740, 315)
    SetChrPos(0x104, 4750, 4120, -6880, 0)
    SetChrPos(0x105, 5580, 4120, -8020, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0368
    ChrTalk(
        0x104,
        (
            "#00300F雨の日だっつーのに、\x01",
            "なかなか盛り上がってるなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#00000Fああ、市民からの参加者も\x01",
            "思っていた以上に多いな……\x02\x03",

            "#00003Fしかし帝国派と共和国派の有力議員と\x01",
            "最近、勢いを増しているっていう\x01",
            "独立派の若手議員たちの論戦か。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、今のクロスベルの政治状況を\x01",
            "反映したかのような顔ぶれだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#00200F何だか、どちらの言い分も\x01",
            "もっともらしく聞こえますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#00103F……実際、この問題は\x01",
            "簡単に結論できるものではないわ。\x02\x03",

            "それこそ何十年にも渡って\x01",
            "同じような議論が繰り返されてきた。\x02\x03",

            "#00101Fでも、確かにそろそろ真剣に\x01",
            "結論を出すべき時かもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x109,
        (
            "#10101F………そうですね。\x02\x03",

            "#10108F（前途多難な独立か\x01",
            "  それとも正義なき従属か……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(821, 500, 90)
    SetScenarioFlags(0x17B, 6)
    SetScenarioFlags(0x22, 2)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_7FB0 end

    SaveToFile()

Try(main)
