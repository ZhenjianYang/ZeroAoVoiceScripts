from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0250.bin",                # FileName
        "c0250",                    # MapName
        "c0250",                    # Location
        0x000E,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 14, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0250",                  # 0
        "マイルズ",               # 1
        "レイテ",                 # 2
        "コウケン",               # 3
        "コウケン",               # 4
        "パンセ",                 # 5
        "リュウ",                 # 6
        "アンリ",                 # 7
        "フェイ",                 # 8
        "フェイ",                 # 9
        "チルル",                 # 10
        "カテリーナ",             # 11
        "仔猫",                   # 12
    ))

    AddCharChip((
        "chr/ch20200.itc",                   # 00
        "chr/ch10300.itc",                   # 01
        "chr/ch21000.itc",                   # 02
        "chr/ch21002.itc",                   # 03
        "chr/ch22300.itc",                   # 04
        "chr/ch20600.itc",                   # 05
        "chr/ch22200.itc",                   # 06
        "chr/ch32700.itc",                   # 07
        "apl/ch50148.itc",                   # 08
        "chr/ch20500.itc",                   # 09
        "chr/ch24500.itc",                   # 0A
        "chr/ch39000.itc",                   # 0B
    ))

    DeclNpc(57950,   0,       103470,  90,   261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-51919,  0,       108370,  90,   261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-51779,  150,     112519,  90,   469,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-54310,  0,       52840,   225,  261,  0x0, 0,   4,   0,   0,   3,   0,   15,  255,  0)
    DeclNpc(-58000,  0,       107489,  0,    389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-57930,  0,       110510,  180,  389,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-54310,  0,       52840,   225,  389,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-51250,  500,     57180,   315,  469,  0x0, 0,   8,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-57729,  0,       106739,  180,  389,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(57950,   0,       103470,  90,   389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-58200,  699,     108930,  225,  468,  0x0, 0,   11,  0,   0,   4,   255, 255, 255,  0)

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_37B",          # 02, 2
        "Function_3_3A6",          # 03, 3
        "Function_4_3D1",          # 04, 4
        "Function_5_431",          # 05, 5
        "Function_6_45C",          # 06, 6
        "Function_7_9A6",          # 07, 7
        "Function_8_A04",          # 08, 8
        "Function_9_1683",         # 09, 9
        "Function_10_3903",        # 0A, 10
        "Function_11_408D",        # 0B, 11
        "Function_12_4264",        # 0C, 12
        "Function_13_4B79",        # 0D, 13
        "Function_14_4D6F",        # 0E, 14
        "Function_15_5300",        # 0F, 15
        "Function_16_67F2",        # 10, 16
        "Function_17_6A0E",        # 11, 17
        "Function_18_6B54",        # 12, 18
        "Function_19_70F8",        # 13, 19
        "Function_20_7555",        # 14, 20
        "Function_21_7862",        # 15, 21
        "Function_22_7AD9",        # 16, 22
        "Function_23_7D53",        # 17, 23
        "Function_24_7E49",        # 18, 24
        "Function_25_7EFA",        # 19, 25
        "Function_26_84D9",        # 1A, 26
        "Function_27_8814",        # 1B, 27
        "Function_28_91A5",        # 1C, 28
        "Function_29_9B53",        # 1D, 29
        "Function_30_A160",        # 1E, 30
        "Function_31_A190",        # 1F, 31
        "Function_32_A1AC",        # 20, 32
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D8"),
        (1, "loc_2E4"),
        (2, "loc_2F0"),
        (3, "loc_2FC"),
        (4, "loc_308"),
        (5, "loc_314"),
        (6, "loc_320"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_2D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_308")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_314")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_32C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_34F")

    Return()

    # Function_0_298 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37A")
    OP_94(0xFE, 0xCF80, 0x19938, 0xD890, 0x190AA, 0x3E8)
    Sleep(300)
    Jump("Function_1_350")

    label("loc_37A")

    Return()

    # Function_1_350 end

    def Function_2_37B(): pass

    label("Function_2_37B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5")
    OP_94(0xFE, 0xFFFF2676, 0x19C08, 0xFFFF2F22, 0x1A3CE, 0x3E8)
    Sleep(300)
    Jump("Function_2_37B")

    label("loc_3A5")

    Return()

    # Function_2_37B end

    def Function_3_3A6(): pass

    label("Function_3_3A6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D0")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_3_3A6")

    label("loc_3D0")

    Return()

    # Function_3_3A6 end

    def Function_4_3D1(): pass

    label("Function_4_3D1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_430")
    OP_94(0xFE, 0xFFFF1ED8, 0x1ABA8, 0xFFFF1A78, 0x1A7E8, 0x12C)
    Sleep(1200)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")
    Sleep(500)
    Jump("loc_42B")

    label("loc_419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    Sleep(800)

    label("loc_42B")

    Jump("Function_4_3D1")

    label("loc_430")

    Return()

    # Function_4_3D1 end

    def Function_5_431(): pass

    label("Function_5_431")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45B")
    OP_94(0xFE, 0xFFFF2CD4, 0x1B5B2, 0xFFFF270C, 0x1A90A, 0x3E8)
    Sleep(300)
    Jump("Function_5_431")

    label("loc_45B")

    Return()

    # Function_5_431 end

    def Function_6_45C(): pass

    label("Function_6_45C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4A1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, -54590, 0, 106800, 180)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -51630, 0, 101720, 90)
    Jump("loc_9A5")

    label("loc_4A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4EC")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrPos(0xA, -55660, 0, 105850, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -54300, 0, 105850, 270)
    Jump("loc_9A5")

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_510")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jump("loc_9A5")

    label("loc_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_53E")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_9A5")

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5AB")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57950, 0, 103470, 90)
    SetChrPos(0xC, -54920, 0, 51450, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -53650, 0, 51450, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -54530, 0, 106440, 180)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_9A5")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_600")
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -57280, 0, 114110, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -58290, 0, 114110, 90)
    Jump("loc_9A5")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_66C")
    SetChrPos(0x8, 54190, 0, 103940, 270)
    BeginChrThread(0x8, 0, 0, 1)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -53150, 0, 112450, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -54140, 0, 112450, 0)
    Jump("loc_9A5")

    label("loc_66C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_6D2")
    SetChrPos(0x8, 54410, 0, 103050, 90)
    SetChrPos(0x9, 55730, 0, 103050, 270)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -51530, 0, 102490, 180)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -51530, 0, 101260, 0)
    Jump("loc_9A5")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6EF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_6EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_756")
    SetChrPos(0x8, 57080, 0, 106510, 315)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -53130, 0, 105180, 0)
    SetChrPos(0xA, -53120, 0, 106320, 180)
    SetChrPos(0xC, -52650, 0, 54740, 45)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_9A5")

    label("loc_756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_784")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_9A5")

    label("loc_784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7C9")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xC, -51660, 0, 46480, 90)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_9A5")

    label("loc_7C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_7FC")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_7FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_825")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    SetChrFlags(0xC, 0x80)
    Jump("loc_9A5")

    label("loc_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_85C")
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_857")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_857")

    Jump("loc_9A5")

    label("loc_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_930")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -10020, 0, 3600, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_8A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8E2")
    SetChrPos(0xD, -54470, 0, 110810, 315)
    SetChrPos(0xE, -57280, 0, 107430, 315)
    BeginChrThread(0xD, 0, 0, 5)
    Jump("loc_92B")

    label("loc_8E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926")
    SetChrPos(0xD, -57650, 0, 110300, 180)
    SetChrPos(0xE, -58450, 0, 110300, 180)
    Jump("loc_92B")

    label("loc_926")

    ClearChrFlags(0x13, 0x80)

    label("loc_92B")

    Jump("loc_9A5")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_978")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_973")
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, -58260, 0, 58850, 0)

    label("loc_973")

    Jump("loc_9A5")

    label("loc_978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_99C")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 57080, 0, 106510, 315)
    Jump("loc_9A5")

    label("loc_99C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_9A5")

    label("loc_9A5")

    Return()

    # Function_6_45C end

    def Function_7_9A6(): pass

    label("Function_7_9A6")

    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CA")
    OP_10(0x0, 0x0)
    OP_10(0xD, 0x1)
    Jump("loc_9D0")

    label("loc_9CA")

    OP_10(0x0, 0x1)
    OP_10(0xD, 0x0)

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EC")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A03")

    label("loc_9EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A03")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_A03")

    label("loc_A03")

    Return()

    # Function_7_9A6 end

    def Function_8_A04(): pass

    label("Function_8_A04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_A9D")

    #C0001
    ChrTalk(
        0xFE,
        "記念祭も今日で最終日だね。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "本来は自治州の創立と\x01",
            "平和を祝う祭りなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "今日はゆっくり過ごして\x01",
            "思索にふけりたいものだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_B89")
    TurnDirection(0xFE, 0x101, 0)

    #C0004
    ChrTalk(
        0xFE,
        (
            "ロイド君、迷子の子は\x01",
            "見つかったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "きっと親御さんも\x01",
            "心配しているだろう。\x01",
            "早く探してあげなさい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B81")

    #C0006
    ChrTalk(
        0x101,
        (
            "#0000Fうん大丈夫、居場所も何とか\x01",
            "突き止められたし……\x02\x03",

            "さっきはありがとう、おじさん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B81")

    SetScenarioFlags(0x0, 0)
    Jump("loc_167F")

    label("loc_B89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_EB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFA")

    #C0007
    ChrTalk(
        0x101,
        (
            "#0003F（マイルズおじさんは\x01",
            "  パレードを見に行っていた筈だ……\x01",
            "  一応聞いてみよう。）\x02\x03",

            "#0000Fおじさん、少しいいかな。\x01",
            "ちょっと聞きたい事があって……\x02",
        )
    )

    CloseMessageWindow()

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはコリンの写真を見せ\x01",
            "心当たりが無いか尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0009
    ChrTalk(
        0xFE,
        "おや、この子は……？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "……やはりそうだ。\x01",
            "確かにさっき会った子だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0005F本当に……！？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "ああ、東通りのことだ。\x01",
            "後ろから僕に\x01",
            "ぶつかりそうになってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "その後は北の方に\x01",
            "駆けて行ったようだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x160,
        (
            "#3308F東通りから北の方角……\x01",
            "港湾区の方になるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#0003Fああ、そうみたいだ。\x02\x03",

            "#0000F……おじさん、ありがとう。\x01",
            "かなり参考になったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAD, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 24)
    Jump("loc_EB0")

    label("loc_DFA")


    #C0016
    ChrTalk(
        0xFE,
        (
            "確かにさっき会った\x01",
            "元気のいい男の子だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "東通りの交差点だったが、\x01",
            "その後は北の方に\x01",
            "駆けて行ったようだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "……迷子とは心配だな……\x01",
            "ロイド君、早く探してあげなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB0")

    Jump("loc_167F")

    label("loc_EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F20")

    #C0019
    ChrTalk(
        0xFE,
        "いやはや、凄い人出だったね。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "ははは、この年にして\x01",
            "迷子になるかと思ってしまったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_167F")

    label("loc_F20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FDD")

    #C0021
    ChrTalk(
        0xFE,
        (
            "これからパレードを\x01",
            "見に行く所なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "はは、さすがに\x01",
            "ロイド君たちは誘えないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "……仕事、気をつけてな。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD5")

    #C0024
    ChrTalk(
        0x101,
        "#0000Fうん、ありがとう、おじさん。\x02",
    )

    CloseMessageWindow()

    label("loc_FD5")

    SetScenarioFlags(0x0, 0)
    Jump("loc_167F")

    label("loc_FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_116C")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1105")

    #C0025
    ChrTalk(
        0xFE,
        "おお、ロイド君か。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "そうか、今日から\x01",
            "仕事があるんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#0000Fうん、一応正規の警察官だから。\x02\x03",

            "おじさんは\x01",
            "今日からお休みだったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ああ、母さんと\x01",
            "一通り回ってみるつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "セシルも一緒なら良かったんだが\x01",
            "あの子も忙しいからねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1167")

    label("loc_1105")


    #C0030
    ChrTalk(
        0xFE,
        (
            "この人出では\x01",
            "警察官も大変だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "ほどほどに休憩をして\x01",
            "バテないように気を付けるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1167")

    Jump("loc_167F")

    label("loc_116C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_167F")
    TurnDirection(0xFE, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1496")

    #C0032
    ChrTalk(
        0x101,
        (
            "#0000Fおじさん、久し振り。\x01",
            "長い間ご無沙汰してました。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "おや？　もしかして……\x01",
            "隣に住んでいたロイド君じゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "ははは、いや驚いた！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "戻ってくるとは聞いていたが\x01",
            "……こりゃあ見違えたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#0012Fいや、背ばかり伸びちゃって。\x01",
            "中身はまだまだだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "そんな事はない。\x01",
            "捜査官の試験にだって\x01",
            "見事に合格したのだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "きっとガイ君も\x01",
            "喜んでくれているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0008Fそう……かな。\x02\x03",

            "……だとしたら俺も嬉しいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "うむ、きっとそうだとも。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FA")

    #C0041
    ChrTalk(
        0xFE,
        (
            "そうだ、台所にいる母さんにも\x01",
            "挨拶してあげなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        "きっと跳んで喜ぶだろうからな。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0000Fははは……そうだね。\x01",
            "それじゃそうさせて貰うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148E")

    label("loc_13FA")


    #C0044
    ChrTalk(
        0xFE,
        (
            "僕は仕事で留守がちだが\x01",
            "母さんは大抵家にいるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "何かあったら母さんを頼りなさい。\x01",
            "……いいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0000Fはい、またお世話になります。\x02",
    )

    CloseMessageWindow()

    label("loc_148E")

    SetScenarioFlags(0x4D, 7)
    Jump("loc_167F")

    label("loc_1496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1639")

    #C0047
    ChrTalk(
        0xFE,
        (
            "君がこんなに大きくなって\x01",
            "戻ってくるとは……\x01",
            "はは、僕ももう歳だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "セシルには挨拶したのかね？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0000Fうん一応、通信でだけど。\x02\x03",

            "今度の休みにでも\x01",
            "会いに行こうかと思ってるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "そうか。\x01",
            "うむ、それがいいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "何はともあれ、君は家族同然だ。\x01",
            "帰ってきてくれてほっとした。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "僕は仕事で留守がちだが\x01",
            "母さんは大抵家にいるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "何かあれば母さんを頼りなさい。\x01",
            "……いいね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_167F")

    label("loc_1639")


    #C0054
    ChrTalk(
        0xFE,
        (
            "君は家族同然なんだ、\x01",
            "何かあれば母さんを頼りなさい。\x01",
            "……いいね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167F")

    TalkEnd(0xFE)
    Return()

    # Function_8_A04 end

    def Function_9_1683(): pass

    label("Function_9_1683")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169C")
    Call(0, 25)
    TalkEnd(0xFE)
    Return()

    label("loc_169C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A7A")

    #C0055
    ChrTalk(
        0x101,
        (
            "#0000Fおばさん、久し振り。\x02\x03",

            "#0006F……ゴメン、最近ちょっと忙しくで\x01",
            "ご無沙汰してたみたいで。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "あらロイド君たちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "最近なんだか\x01",
            "活躍してるって聞いたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズにも\x01",
            "載ったんですって？\x01",
            "うふふ、おばさんも鼻が高いわ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ささ、おばさんに\x01",
            "どーんと自慢して頂戴！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0300Fんじゃおばさん、\x01",
            "遠慮なくオレの武勇伝を……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、色々と\x01",
            "大変だったんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#0202Fついでにご入用の際は\x01",
            "特務支援課へ\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0063
    ChrTalk(
        0x101,
        (
            "#0006Fちょ、ちょっとみんな……\x01",
            "厚かましいっていうか……\x02\x03",

            "最近おばさんに\x01",
            "馴染みすぎてないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#0100Fあらいいじゃない。\x01",
            "セシルさんのお母様なんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#0300Fそうそう、時々\x01",
            "メシも奢ってもらってるんだ。\x01",
            "家族も同然だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "そうよロイド君。\x01",
            "遠慮なんてしちゃダメよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "……みんなもまた\x01",
            "遊びに来て頂戴ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#0300Fうーっす！\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0100Fはい。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#0200F……了解です。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0071
    ChrTalk(
        0x101,
        (
            "#0006F（やっぱりみんな、\x01",
            "  馴染みすぎだって……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8F, 6)
    TalkEnd(0xFE)
    Return()

    label("loc_1A7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1A88")
    Jump("loc_38FF")

    label("loc_1A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1AEC")

    #C0072
    ChrTalk(
        0xFE,
        (
            "今日は大聖堂に\x01",
            "お祈りに行くつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "早めに支度を\x01",
            "しないといけないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_1AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAB")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0074
    ChrTalk(
        0xFE,
        "あら、ティオちゃん……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#0200Fはい、何でしょう。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "少し顔色が悪い気が\x01",
            "したのだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        "気のせいだったかしら。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        (
            "#0208F……昨日の《僧院》の捜索で\x01",
            "疲れたのだと思います。\x02\x03",

            "#0203Fその、わたしなりに\x01",
            "気を張り詰めていたもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#0300Fティオすけの感知能力には\x01",
            "毎度助けられてるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0000Fそうなんだよなぁ……\x01",
            "ティオ、無理しないでくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#0202Fええ、分かっています。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D1D")

    label("loc_1CAB")


    #C0082
    ChrTalk(
        0xFE,
        (
            "なんだか分からないけど\x01",
            "昨日は大変だったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "疲れたときに無理は禁物。\x01",
            "十分にお休みを取りなさいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1D")

    Jump("loc_38FF")

    label("loc_1D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2161")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B1")

    #C0084
    ChrTalk(
        0x104,
        (
            "#0300Fちわーっす。\x01",
            "セシルさんのお母様、\x01",
            "ご無沙汰してまっす！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#0102Fご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0006Fおばさんゴメン、\x01",
            "いつも大勢で押しかけちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "うふふ、構わないわよ。\x01",
            "みんなしていつも元気なこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "その分だと今日も\x01",
            "お仕事頑張っているみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0089
    ChrTalk(
        0xFE,
        (
            "あら……そちらの子は\x01",
            "見るのは初めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "支援課の新入りさんかしら。\x01",
            "うふふ、また可愛らしい方だこと。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F05")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_1F05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F46")
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x109)

    label("loc_1F46")


    #C0091
    ChrTalk(
        0x109,
        (
            "#0505Fか、可愛らしい……だなんて。\x02\x03",

            "じ、自分は警備隊勤務の者で、\x01",
            "その、本日は……\x01",
            "特務支援課殿への協力要請を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        "#0300Fノエル、まあ落ち着けって。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x109,
        (
            "#0505Fす、すみません、つい……\x02\x03",

            "#0503Fそんなことを言われたのは\x01",
            "は、初めてだったもので。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#0200F（……ノエルさんの\x01",
            "  意外な弱点発覚です。）\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "うふふ、やっぱり\x01",
            "可愛らしい子じゃないの～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 0)
    Jump("loc_215C")

    label("loc_20B1")


    #C0096
    ChrTalk(
        0xFE,
        (
            "警備隊の方だったかしら。\x01",
            "ゆっくりしていって頂戴ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        (
            "#0501Fはっ……ノエル・シーカー\x01",
            "そうさせて頂きます！\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0000F（ノエル曹長……\x01",
            "  まだ少し緊張してるな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215C")

    Jump("loc_38FF")

    label("loc_2161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_220E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217C")
    Call(0, 10)
    Jump("loc_2209")

    label("loc_217C")


    #C0099
    ChrTalk(
        0xFE,
        (
            "ふふ、キーアちゃんも\x01",
            "本が大好きなのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "今度子供向けの本も\x01",
            "並べておこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "お父さんに話したら\x01",
            "喜んで揃えてくれそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2209")

    Jump("loc_38FF")

    label("loc_220E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2309")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C5")

    #C0102
    ChrTalk(
        0xFE,
        "あら、ロイド君たちじゃないの。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "記念祭もじっくり楽しんだし\x01",
            "今日はゆっくりしようと思っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "もちろん締めの花火は\x01",
            "見るつもりですけれどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2304")

    label("loc_22C5")


    #C0105
    ChrTalk(
        0xFE,
        (
            "ふふ、たまにはお父さんと\x01",
            "ゆっくりするのも悪くないわねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2304")

    Jump("loc_38FF")

    label("loc_2309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 7)), scpexpr(EXPR_END)), "loc_23D3")

    #C0106
    ChrTalk(
        0xFE,
        (
            "パレードは混雑したから\x01",
            "親御さんとはぐれちゃったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "ロイド君、警察の出番じゃない。\x01",
            "早く探してあげなさいな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23CB")

    #C0108
    ChrTalk(
        0x101,
        (
            "#0000Fそうだね……\x01",
            "みんな、なるべく急いで行こう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CB")

    SetScenarioFlags(0x0, 1)
    Jump("loc_38FF")

    label("loc_23D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_249B")

    #C0109
    ChrTalk(
        0xFE,
        (
            "あらロイド君、\x01",
            "迷子の子を探しているの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "そういえばお父さんが\x01",
            "小さな男の子と会っていたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "あの子は１人だったから\x01",
            "親御さんはどうしたのかしらって\x01",
            "思っていたのだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_249B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2583")

    #C0112
    ChrTalk(
        0xFE,
        (
            "ふう、パレードは\x01",
            "凄い人出だったわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "ロイド君たちは平気だった？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0012Fあはは、実は……\x01",
            "今年は見逃しちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        "あら、そうだったの！？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "それは残念ねぇ……\x01",
            "今年は特に凄かったのよ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25EB")

    label("loc_2583")


    #C0117
    ChrTalk(
        0xFE,
        (
            "そうだ、おばさんちゃんと\x01",
            "写真を取ってあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "後でロイド君たちにも\x01",
            "焼き増ししてあげるわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25EB")

    Jump("loc_38FF")

    label("loc_25F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_265E")

    #C0119
    ChrTalk(
        0xFE,
        (
            "そろそろパレードが\x01",
            "始まるらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "ふふ、セシルも一緒に\x01",
            "来れれば良かったのにねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_265E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_27D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275C")

    #C0121
    ChrTalk(
        0xFE,
        (
            "今日はお父さんは\x01",
            "出かけちゃってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、おばさんは\x01",
            "一緒じゃないの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "ええ、なんでも\x01",
            "市のセレモニーホールで\x01",
            "国際シンポジウムがあるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "ふふ、お父さんたら\x01",
            "こういう催しに目が無いのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27CC")

    label("loc_275C")


    #C0125
    ChrTalk(
        0xFE,
        (
            "お父さんが戻ってくるまで\x01",
            "１人でお留守番なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "やれやれ、今のうちに\x01",
            "ご馳走でも作っておきましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CC")

    Jump("loc_38FF")

    label("loc_27D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BB")

    #C0127
    ChrTalk(
        0x101,
        (
            "#0000Fあ、おばさん……\x02\x03",

            "#0009F昨日はご馳走様。\x01",
            "お料理とっても美味しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "うふふ、お粗末様でした。\x01",
            "また遊びに来て頂戴ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        (
            "#0200F……ロイドさんは\x01",
            "セシルさんの実家に\x01",
            "お邪魔していたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#0301Fおいロイド、なんで俺たちを\x01",
            "誘ってくれなかったんだよ。\x02\x03",

            "#0306Fセシルお姉様と\x01",
            "ご一緒したかったのによ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0131
    ChrTalk(
        0x101,
        (
            "#0006F後輩の子と\x01",
            "合コンしてたくせに\x01",
            "よく言うよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        "#0111F本当に無節操よねえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A1F")

    label("loc_29BB")


    #C0133
    ChrTalk(
        0xFE,
        (
            "うふふ、これからお父さんと\x01",
            "お祭りを見て回るつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "みんなもお仕事、\x01",
            "頑張って頂戴ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1F")

    Jump("loc_38FF")

    label("loc_2A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE3")

    #C0135
    ChrTalk(
        0xFE,
        "あらいらっしゃい。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "ロイド君たちは\x01",
            "またどこかへ出かけるようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0000Fうん、また少し\x01",
            "調べ事があってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "うふふ、毎日お仕事\x01",
            "頑張ってるみたいで嬉しいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "今度ゆっくり聞かせて頂戴ね。\x01",
            "おばさん、みんなの活躍を\x01",
            "楽しみにしてるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        "#0100Fええ、喜んで。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0003F（アルカンシェルの話は\x01",
            "  しばらく伏せるしかないけどな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        (
            "#0301F（だな。\x01",
            "  とっとと解決して\x01",
            "  笑い話にしたいもんだぜ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C37")

    label("loc_2BE3")


    #C0143
    ChrTalk(
        0xFE,
        (
            "今度ゆっくり聞かせて頂戴ね。\x01",
            "おばさん、みんなの活躍を\x01",
            "楽しみにしてるんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C37")

    Jump("loc_38FF")

    label("loc_2C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E1C")

    #C0144
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "……ロイド君？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0005Fえ？　なに、おばさん……\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "なんだかいつもより\x01",
            "大人びて見えるわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "ふふっ、顔立ちがきりっとして、\x01",
            "少しガイ君に似てきた気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#0012Fはは、そうかな？\x01",
            "年が追いついてきた所為かな……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0304F昨晩の一件の\x01",
            "せいだったりして……（ボソッ）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x103,
        (
            "#0204F大人の階段を登る……\x01",
            "というやつですか。（ボソッ）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 0)

    #C0151
    ChrTalk(
        0x101,
        (
            "#0011Fだ、だから\x01",
            "全然違うって言ってるだろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        "#0106F#2Sはあ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E92")

    label("loc_2E1C")


    #C0153
    ChrTalk(
        0xFE,
        (
            "ロイド君、最近\x01",
            "顔立ちが大人びてきたみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "ふふっ、きりっとした所なんて\x01",
            "少しガイ君に似てきた気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E92")

    Jump("loc_38FF")

    label("loc_2E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F38")

    #C0155
    ChrTalk(
        0xFE,
        (
            "来月はやっぱり\x01",
            "記念祭で盛り上がるんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "セシルったら\x01",
            "お休みは取れるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "今度きちんと\x01",
            "確認しておかないといけないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_2F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2F95")

    #C0158
    ChrTalk(
        0xFE,
        (
            "支援課のみんなも\x01",
            "遠慮なんてしちゃダメよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        "いつでも遊びに来て頂戴ね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38FF")

    label("loc_2F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3138")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB1")
    Call(0, 11)
    Jump("loc_3133")

    label("loc_2FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC3")
    Call(0, 26)
    Jump("loc_3133")

    label("loc_2FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CF")

    #C0160
    ChrTalk(
        0xFE,
        (
            "まああの子も成人なのだから\x01",
            "すぐにどうと\x01",
            "言うつもりはないけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "そろそろ……自分の将来を\x01",
            "考えるべきだと思うのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "そうだわ、今日は大聖堂で\x01",
            "いいご縁があるように\x01",
            "お祈りしておこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#0006F（複雑だ……\x01",
            "  すごく複雑だよ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3133")

    label("loc_30CF")


    #C0164
    ChrTalk(
        0xFE,
        (
            "今日は午後から\x01",
            "大聖堂にお祈りに行くのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "ついでにセシルのご縁を\x01",
            "お祈りしておこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3133")

    Jump("loc_38FF")

    label("loc_3138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_32D8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3154")
    Call(0, 11)
    Jump("loc_32D3")

    label("loc_3154")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328E")

    #C0166
    ChrTalk(
        0xFE,
        (
            "セシルったら、仕事仕事で\x01",
            "週末だって帰ってこないのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "まだ一人娘を\x01",
            "嫁にやった覚えはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0012Fまあまあ、おばさん……\x01",
            "セシル姉も色々と\x01",
            "忙しいみたいだしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "ええ、それは承知してますけれど。\x01",
            "たまには顔を見たいじゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "ご飯くらい食べに\x01",
            "戻ってくればいいのにねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32D3")

    label("loc_328E")


    #C0171
    ChrTalk(
        0xFE,
        (
            "セシルったら、仕事仕事って……\x01",
            "週末くらい帰ってもいいのにねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D3")

    Jump("loc_38FF")

    label("loc_32D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_34BA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F4")
    Call(0, 11)
    Jump("loc_34B5")

    label("loc_32F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344F")

    #C0172
    ChrTalk(
        0xFE,
        "あらロイド君たちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "しばらく顔を見なかったけど\x01",
            "警察のお仕事は頑張ってるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#0000Fはは、まあ何とか。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x104,
        "#0300F地味な仕事ばかりッスけど。\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "うふふ、初めのうちは\x01",
            "誰だってそんなものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "頑張って頂戴ね。\x01",
            "きっとガイ君もあなた達の事を\x01",
            "見守ってくれているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0008F……うん。\x01",
            "ありがとう、おばさん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34B5")

    label("loc_344F")


    #C0179
    ChrTalk(
        0xFE,
        (
            "さて、お父さんも\x01",
            "仕事に出かけちゃったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "お祈りに行く前に\x01",
            "洗いものを片付けちゃわないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B5")

    Jump("loc_38FF")

    label("loc_34BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_376A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E0")
    OP_93(0xFE, 0x13B, 0x0)

    #C0181
    ChrTalk(
        0xFE,
        (
            "あの子が大きな怪我もなく\x01",
            "帰ってきてくれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "空の女神#8Rエ イ ド ス#よ、感謝いたします。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#0100F（信仰の厚い方なのね。）\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#0000F（ああ、昔からね。）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CA")

    #C0185
    ChrTalk(
        0x101,
        (
            "#0000F（兄貴のときも……\x01",
            "  おばさんはそうだったな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360F")

    label("loc_35CA")


    #C0186
    ChrTalk(
        0x101,
        (
            "#0000F（兄貴が殉職したときも……\x01",
            "  おばさんはそうだったな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_360F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    #C0187
    ChrTalk(
        0xFE,
        (
            "あらら、ごめんなさい。\x01",
            "ついつい気付かなくて。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "お父さんなら図書館の仕事に\x01",
            "行ってしまったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "あの人、司書の仕事が大好きだから\x01",
            "毎日張り切って出かけるのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3765")

    label("loc_36E0")


    #C0190
    ChrTalk(
        0xFE,
        (
            "お父さんなら\x01",
            "仕事に行ってしまったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "本好きだからって\x01",
            "図書館の司書になったくらいだもの。\x01",
            "毎日嬉しそうに出かけるのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3765")

    Jump("loc_38FF")

    label("loc_376A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_38FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388D")

    #C0192
    ChrTalk(
        0xFE,
        (
            "あれからもう\x01",
            "３年も経ったのねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "セシルなんて毎日のように\x01",
            "寂しい寂しいって言っていたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "これは皆を呼んで\x01",
            "パーティでもやらなきゃダメかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        (
            "#0011F（う……止めても無駄な雰囲気だ。）\x02\x03",

            "#0006F（このパワー……\x01",
            "  おばさんも変わってないなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38FF")

    label("loc_388D")


    #C0196
    ChrTalk(
        0xFE,
        (
            "ロイド君が３年ぶりに\x01",
            "戻ってきたんだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "ここはやっぱり、皆を呼んで\x01",
            "パーティでもやらなきゃダメかしら！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38FF")

    TalkEnd(0xFE)
    Return()

    # Function_9_1683 end

    def Function_10_3903(): pass

    label("Function_10_3903")

    OP_93(0x9, 0x5A, 0x0)
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(56890, 1000, 103430, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x101, 55780, 0, 103550, 90)
    SetChrPos(0xEF, 55940, 0, 104600, 135)
    SetChrPos(0x153, 55940, 0, 102750, 90)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(750)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_39D7")

    #C0198
    ChrTalk(
        0x9,
        "あらロイド君にエリィちゃん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_39D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3A09")

    #C0199
    ChrTalk(
        0x9,
        "あらロイド君にティオちゃん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A34")

    label("loc_3A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3A34")

    #C0200
    ChrTalk(
        0x9,
        "あらロイド君にランディ君……\x02",
    )

    CloseMessageWindow()

    label("loc_3A34")


    #C0201
    ChrTalk(
        0x9,
        (
            "と……あらま、\x01",
            "その可愛らしい子は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#0000Fはは、キーアっていって\x01",
            "少し支援課の方で\x01",
            "預かってる子なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x153,
        (
            "#1110Fこんにちはー！\x01",
            "ほんがいっぱいだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        "はいこんにちは。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "キーアちゃんも\x01",
            "本が大好きなのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "うちのお父さんも本好きでね、\x01",
            "今は図書館の司書をやっているのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D73")

    #C0207
    ChrTalk(
        0x153,
        (
            "#1111Fとしょかん～？\x02\x03",

            "#1110Fあ、わかった！\x01",
            "ほんを貸してくれる所だ！\x02\x03",

            "#1109Fねえロイド～、今度は\x01",
            "としょかんに行かない？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#0003Fうーん、そうだな……\x01",
            "そこまで寄り道すると\x01",
            "長引きそうな気が……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3C9A")

    #C0209
    ChrTalk(
        0x102,
        (
            "#0100Fでも、キーアちゃんなら\x01",
            "きっと喜ぶんじゃないかしら。\x01",
            "少しくらいならいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D41")

    label("loc_3C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3CF2")

    #C0210
    ChrTalk(
        0x103,
        (
            "#0200Fでも、キーアなら\x01",
            "喜ぶかもしれません……\x01",
            "連れて行くのも手かと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D41")

    label("loc_3CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3D41")

    #C0211
    ChrTalk(
        0x104,
        (
            "#0300Fでもよ、キー坊なら\x01",
            "喜びそうじゃねえか？\x01",
            "折角の機会だしよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D41")


    #C0212
    ChrTalk(
        0x101,
        (
            "#0000Fそうか、そういう\x01",
            "考えもあるな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F73")

    label("loc_3D73")


    #C0213
    ChrTalk(
        0x153,
        (
            "#1110Fとしょかん～？\x01",
            "さっき行ったとこだねー！\x02\x03",

            "#1109Fねえロイド～、\x01",
            "キーアまたとしょかんに\x01",
            "行きたくなってきたなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        (
            "#0000Fはは、でも\x01",
            "あまり寄り道するのはなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3E7F")

    #C0215
    ChrTalk(
        0x102,
        (
            "#0100Fあら、いいじゃないロイド。\x01",
            "キーアちゃんもあんなに\x01",
            "喜んでいたんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F38")

    label("loc_3E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3EF4")

    #C0216
    ChrTalk(
        0x103,
        (
            "#0200F……ロイドさん。\x01",
            "キーアは図書館が\x01",
            "気に入ったようです。\x02\x03",

            "それを断るのは\x01",
            "酷いのではないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F38")

    label("loc_3EF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3F38")

    #C0217
    ChrTalk(
        0x104,
        (
            "#0300Fいいじゃんかロイド。\x01",
            "キー坊は随分喜んでたしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F38")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x101,
        "#0000Fみんな親馬鹿だな……\x02",
    )

    CloseMessageWindow()

    label("loc_3F73")


    #C0219
    ChrTalk(
        0x9,
        (
            "……ふふ、なんだか\x01",
            "贅沢な悩みを抱えてるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "キーアちゃん、\x01",
            "また遊びに来て頂戴。\x01",
            "おばさん喜んで歓迎するから。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x153,
        (
            "#1109Fうん、キーアそうする。\x02\x03",

            "またねー、おばさん！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x9,
        "はい、またねキーアちゃん。\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#0000F（さすがおばさんは\x01",
            "  子供の扱いがなれてるなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAF, 7)
    EventEnd(0x5)
    Return()

    # Function_10_3903 end

    def Function_11_408D(): pass

    label("Function_11_408D")


    #C0224
    ChrTalk(
        0xFE,
        "あらロイド君たちじゃない。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "しばらく顔を見なかったけど\x01",
            "警察のお仕事は頑張ってるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#0000Fはは、まあ何とか。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        "#0300F地味な仕事ばかりッスけど。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "うふふ、初めのうちは\x01",
            "誰だってそんなものよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "そうだわ、今日はおばさんが\x01",
            "料理のコツを教えてあげる。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        (
            "ロイド君たちは働き盛りだもの、\x01",
            "栄養のあるものを食べないとね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4263")
    SetScenarioFlags(0x0, 1)

    label("loc_4263")

    Return()

    # Function_11_408D end

    def Function_12_4264(): pass

    label("Function_12_4264")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_431F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42DF")

    #C0233
    ChrTalk(
        0xFE,
        (
            "マインツから山越えして\x01",
            "レマン自治州まで行くじゃと……？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        "すまん、やはり無理じゃ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_431A")

    label("loc_42DF")


    #C0235
    ChrTalk(
        0xFE,
        (
            "うちの子供たちときたら……\x01",
            "難しい子ばかりじゃのう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431A")

    Jump("loc_4B75")

    label("loc_431F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4330")
    Call(0, 13)
    Jump("loc_4B75")

    label("loc_4330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_440F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43DB")

    #C0236
    ChrTalk(
        0xFE,
        (
            "タリーズ商店のモモちゃんは\x01",
            "実によい子じゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "利発そうで、よく店の手伝いもして……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "リュウにもつめの垢を\x01",
            "せんじて飲ませたいわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_440A")

    label("loc_43DB")


    #C0239
    ChrTalk(
        0xFE,
        (
            "やれやれ……リュウには\x01",
            "見習わせたいわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440A")

    Jump("loc_4B75")

    label("loc_440F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_448D")

    #C0240
    ChrTalk(
        0xFE,
        (
            "チルルの奴は\x01",
            "まだどこかに出かけるらしいのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "リュウも困った奴じゃが\x01",
            "チルルもよう分からん子じゃわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B75")

    label("loc_448D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4530")

    #C0242
    ChrTalk(
        0xFE,
        (
            "わはは、めでたい祭りじゃ！\x01",
            "今日は中央広場に行くかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "にしても……チルルは\x01",
            "付き合いが悪いのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "今日はなんでも\x01",
            "奢っちゃるっちゅうに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B75")

    label("loc_4530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_45F0")

    #C0245
    ChrTalk(
        0xFE,
        (
            "今日は西通りと住宅街辺りの子の\x01",
            "日曜学校の日なんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "リュウのやつもまじめに\x01",
            "勉強しておればいいんじゃが。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 0)), scpexpr(EXPR_END)), "loc_45EB")

    #C0247
    ChrTalk(
        0x101,
        (
            "#0003F（……ツァイトと\x01",
            "  遊んでいたけどな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45EB")

    Jump("loc_4B75")

    label("loc_45F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_473E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BE")

    #C0248
    ChrTalk(
        0xFE,
        (
            "わしは将来リュウのやつに\x01",
            "商売を継がせるつもりでおる。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "じゃが……あやつ\x01",
            "今日も遊びまわっておるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "日曜学校の勉強もさっぱりじゃし\x01",
            "……まったくできの悪い息子じゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4739")

    label("loc_46BE")


    #C0251
    ChrTalk(
        0xFE,
        (
            "リュウに商売の基本を\x01",
            "叩き込んでやりたいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "あのお調子モン、\x01",
            "わしの言うことなど\x01",
            "ちっとも聞きおらんしのう……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4739")

    Jump("loc_4B75")

    label("loc_473E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_47C1")
    OP_93(0xFE, 0x0, 0x0)

    #C0253
    ChrTalk(
        0xFE,
        (
            "ふむ、リュウの奴。\x01",
            "まさかあのまま飼う気では……\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "今回だけと言うとるのが\x01",
            "分かっとるんじゃろうな……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B75")

    label("loc_47C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_48CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4893")

    #C0255
    ChrTalk(
        0xFE,
        (
            "今日は百貨店に\x01",
            "商品を卸しに行くんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "目新しい雑貨を見つけたのでな、\x01",
            "売り込んでくるというわけじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "百貨店に出入りする問屋は多い……\x01",
            "わしもウカウカしてられんわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_48C8")

    label("loc_4893")


    #C0258
    ChrTalk(
        0xFE,
        (
            "目新しい商品は\x01",
            "ぐぐいと売り込んでいかんとのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48C8")

    Jump("loc_4B75")

    label("loc_48CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B6")

    #C0259
    ChrTalk(
        0xFE,
        (
            "わしは３年ほど前から\x01",
            "クロスベルで商売をしておるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        (
            "問屋業といってな、\x01",
            "百貨店のような大型商店に\x01",
            "細々とした品を卸しておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "ふふ、わしは共和国人だからな。\x01",
            "共和国の品なら目利きは確かじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4A4E")

    label("loc_49B6")


    #C0262
    ChrTalk(
        0xFE,
        (
            "クロスベルで問屋業を始めて\x01",
            "３年になるが\x01",
            "ようやく仕事も安定してきたわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "やはりタイムズ百貨店と\x01",
            "契約できたのが大きいじゃろうな、\x01",
            "わはは……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A4E")

    Jump("loc_4B75")

    label("loc_4A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_4B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B23")

    #C0264
    ChrTalk(
        0xFE,
        (
            "今朝クロスベルタイムズを\x01",
            "広げてみれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "なんと、リュウの奴が\x01",
            "写真つきで載っておったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "あ、あの馬鹿息子め……！\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xFE,
        (
            "もちろんその場で\x01",
            "きつく叱り付けてやったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B75")

    label("loc_4B23")


    #C0268
    ChrTalk(
        0xFE,
        (
            "まったくリュウの奴め。\x01",
            "きつく叱り付けてやったが\x01",
            "本当に反省しとるんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B75")

    TalkEnd(0xFE)
    Return()

    # Function_12_4264 end

    def Function_13_4B79(): pass

    label("Function_13_4B79")

    OP_4B(0xA, 0xFF)
    OP_4B(0x11, 0xFF)
    TurnDirection(0xA, 0x11, 0)
    TurnDirection(0x11, 0xA, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C89")

    #C0269
    ChrTalk(
        0xA,
        (
            "おうチルル、戻ったか。\x01",
            "今回の旅はどうじゃった？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x11,
        "……３回ほど溺れた。\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x11,
        (
            "あの湿原地帯、\x01",
            "あちこち底なし沼みたいに\x01",
            "なってて危ないね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0272
    ChrTalk(
        0xA,
        (
            "ななっ……危なすぎじゃろ！\x01",
            "お前どこまで行っとったんじゃ！？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4D66")

    label("loc_4C89")


    #C0273
    ChrTalk(
        0xA,
        (
            "チルル、お前やはり\x01",
            "一人で出かけちゃいかんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "今度はワシも連れていけい。\x01",
            "たまには付き合って\x01",
            "やろうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x11,
        (
            "いいけど……すごく歩くよ？\x01",
            "たぶんお父さんには無理。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "これこれ！\x01",
            "父の偉大さを舐めるなよ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D66")

    OP_4C(0xA, 0xFF)
    OP_4C(0x11, 0xFF)
    Return()

    # Function_13_4B79 end

    def Function_14_4D6F(): pass

    label("Function_14_4D6F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E03")
    Jump("loc_4E4D")

    label("loc_4E03")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4E23")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E4D")

    label("loc_4E23")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E43")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4E4D")

    label("loc_4E43")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E4D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4E80")
    Jump("loc_52F8")

    label("loc_4E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4E8E")
    Jump("loc_52F8")

    label("loc_4E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E9C")
    Jump("loc_52F8")

    label("loc_4E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5A")

    #C0277
    ChrTalk(
        0xFE,
        (
            "わはは……！\x01",
            "景気がいいとはこの事じゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "今月に入って３件も\x01",
            "新しい店と契約したんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "それも先方からのオファーでな。\x01",
            "わはは、嬉しいもんじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4FBE")

    label("loc_4F5A")


    #C0280
    ChrTalk(
        0xFE,
        (
            "今月に入って３件も\x01",
            "新しい店と契約したんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "わはは……！\x01",
            "わしも名が売れてきたのかのう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FBE")

    Jump("loc_52F8")

    label("loc_4FC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5060")
    SetChrSubChip(0xFE, 0x0)

    #C0282
    ChrTalk(
        0xFE,
        (
            "ううむ、予想以上の仕入れじゃな。\x01",
            "ここは鉄道便を一便確保して……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "いや今からでは遅いか。\x01",
            "アルタイル市でトラック便に\x01",
            "積み替えて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52F8")

    label("loc_5060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5122")

    #C0284
    ChrTalk(
        0xFE,
        (
            "仕入れ伝票の整理に\x01",
            "運搬の手はず、決算書類の手続き……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        "ううむ、仕事が山積みじゃな。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "……じゃがこれも\x01",
            "記念祭に休みを作るため……\x01",
            "今は踏ん張らねばな……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_518E")

    label("loc_5122")


    #C0287
    ChrTalk(
        0xFE,
        (
            "わしだってクロスベル市民じゃ。\x01",
            "記念祭は休んで楽しみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "今のうちに仕事を\x01",
            "片付けてしまわんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518E")

    Jump("loc_52F8")

    label("loc_5193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_52F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_527F")

    #C0289
    ChrTalk(
        0xFE,
        (
            "記念祭には大抵の商店で\x01",
            "大型セールを開くんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        "問屋としても大忙しじゃわい。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)

    #C0291
    ChrTalk(
        0xFE,
        (
            "歯磨き粉８４箱に\x01",
            "いつもの雑誌を２５０部増し……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "ううむ、何とかやりくりせんと……\x01",
            "（パチパチ、パチパチ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_52F8")

    label("loc_527F")


    #C0293
    ChrTalk(
        0xFE,
        (
            "……ちなみにこれは\x01",
            "ソロバンと言ってな。\x01",
            "東方の手動計算器じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "東方出の商人は\x01",
            "これを弾いて計算をするんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_14_4D6F end

    def Function_15_5300(): pass

    label("Function_15_5300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_532A")
    Call(0, 27)
    Return()

    label("loc_532A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5616")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5594")

    #C0295
    ChrTalk(
        0x101,
        (
            "#0000Fちょっといいかな。\x02\x03",

            "君は猫を\x01",
            "飼ってたりしないかな？\x01",
            "もしくは心当たりとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "あら、リュウが\x01",
            "見つけたっていう仔猫の話ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "あの２人にも言ったけど\x01",
            "あたしは知らないわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "おとーさんやお姉ちゃんが\x01",
            "勝手に飼いだした可能性も\x01",
            "否定できないケド……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "２人とも機械工#6Rエンジニア#一直線だもの。\x01",
            "ナマモノに興味あるとは\x01",
            "思えないわね。\x02",
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
    Sleep(1200)

    #C0300
    ChrTalk(
        0x101,
        (
            "#0006F（ウェンディの妹……\x01",
            "  辛らつだなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x103,
        (
            "#0200Fまあともかく\x01",
            "心当たりは無いようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8, 0x1, 0x3)
    Jump("loc_5611")

    label("loc_5594")


    #C0302
    ChrTalk(
        0xFE,
        (
            "リュウとアンリも聞きにきたけど\x01",
            "仔猫なんては知らないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "このベルハイムで\x01",
            "ペットを飼ってる人は\x01",
            "いないと思うわよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5611")

    Jump("loc_67EE")

    label("loc_5616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_56ED")

    #C0304
    ChrTalk(
        0xC,
        (
            "その本は多分、おとーさんが\x01",
            "あたしを鉄道技師の世界に\x01",
            "連れて行くために借りたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xC,
        (
            "お姉ちゃんもお父さんが\x01",
            "導力オモチャで育てて\x01",
            "技師にしちゃったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xC,
        (
            "あたしはその手には\x01",
            "乗らないんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67EE")

    label("loc_56ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5900")

    #C0307
    ChrTalk(
        0x101,
        (
            "#0000Fやあパンセ、\x01",
            "今日もお留守番みたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xFE,
        (
            "あ、お兄さん確か\x01",
            "ウェンディお姉ちゃんの\x01",
            "お友達だっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        (
            "どーも、いつもお姉ちゃんが\x01",
            "お世話になってマス。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x102,
        (
            "#0102Fふふっ、ウェンディさんには\x01",
            "私たちがお世話になってるんだけど。\x02\x03",

            "#0100F妹さんは、今日はお掃除かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "うん、そーなの。\x01",
            "おとーさんもお姉ちゃんも\x01",
            "お片付けがへったくそなんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0xFE,
        (
            "みなさんからも言ってやってくれない？\x01",
            "もー少しせーかつりょくをつけろって。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#0009Fははは……\x01",
            "（ウェンディの妹は\x01",
            "  しっかりしてるんだよな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 1)
    Jump("loc_67EE")

    label("loc_5900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FE")

    #C0314
    ChrTalk(
        0xFE,
        (
            "あのね、マリアベルさんってね、\x01",
            "ＩＢＣの技術部を率いてるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        "導力技術にもすっごく詳しいらしいの。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xFE,
        (
            "……………………………………\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "び、美人なのに技師も\x01",
            "できるなんて、さすがね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5A49")

    label("loc_59FE")


    #C0318
    ChrTalk(
        0xFE,
        (
            "やっぱりマリアベルさんは\x01",
            "カッコイイわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        "理想の大人のオンナよね！\x02",
    )

    CloseMessageWindow()

    label("loc_5A49")

    Jump("loc_67EE")

    label("loc_5A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AFE")

    #C0320
    ChrTalk(
        0xFE,
        (
            "今日ウェンディお姉ちゃんったら\x01",
            "寝坊したのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "何度起こしても\x01",
            "『オーバル回路……』とか言って\x01",
            "起きないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        "んもう、ダメダメよね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5B3B")

    label("loc_5AFE")


    #C0323
    ChrTalk(
        0xFE,
        (
            "ウェンディお姉ちゃんたら\x01",
            "いっつもだらしないんだから～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B3B")

    Jump("loc_67EE")

    label("loc_5B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5C53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C04")

    #C0324
    ChrTalk(
        0xFE,
        (
            "今日発売の経済雑誌にね、\x01",
            "マリアベルさんが写真入りで\x01",
            "載ってるらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xFE,
        (
            "経済雑誌だろうがなんだろうが、\x01",
            "大急ぎで買ってこなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        "切抜きにして保存確定ね！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5C4E")

    label("loc_5C04")


    #C0327
    ChrTalk(
        0xFE,
        (
            "マリアベルさんって\x01",
            "ホントステキよね～！\x01",
            "オトナの女はこうでなくちゃ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C4E")

    Jump("loc_67EE")

    label("loc_5C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5DE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7A")

    #C0328
    ChrTalk(
        0xFE,
        (
            "ロイドさんって\x01",
            "ウェンディおねーちゃんの\x01",
            "お知り合いなのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000Fああ……\x01",
            "同じアパルトメントだったし\x01",
            "幼馴染だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "ふーん、よく\x01",
            "おねーちゃんなんかと\x01",
            "付き合ってられたわよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "今朝もすごい寝癖のまま\x01",
            "仕事にでていったのよ。\x01",
            "あたしもう信じらんない。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5DDF")

    label("loc_5D7A")


    #C0332
    ChrTalk(
        0xFE,
        "やっぱり技師なんてダメダメね。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "お化粧もしないで出かけるなんて\x01",
            "オンナの風上にも置けないわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DDF")

    Jump("loc_67EE")

    label("loc_5DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DFF")
    Call(0, 17)
    Jump("loc_5E68")

    label("loc_5DFF")


    #C0334
    ChrTalk(
        0xFE,
        "おとーさん、また出張なのよねー。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "……おミヤゲなんていらないから\x01",
            "家にいてくれたらいいのにー……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E68")

    Jump("loc_67EE")

    label("loc_5E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5EC9")
    OP_93(0xFE, 0x2D, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        "ちょっとおとーさん！？\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "お祭りに\x01",
            "連れてってくれる約束でしょ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67EE")

    label("loc_5EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6B")

    #C0338
    ChrTalk(
        0xFE,
        (
            "今日発売のファッション雑誌、\x01",
            "表紙はマリアベルさんだったの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    #C0339
    ChrTalk(
        0xFE,
        (
            "きゃっ、カッコイイ！\x01",
            "これは保存版確定ねっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5FEC")

    label("loc_5F6B")


    #C0340
    ChrTalk(
        0xFE,
        (
            "クロスベル一の令嬢、\x01",
            "若き天才女性経営者にして\x01",
            "超絶美貌の持ち主……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xFE,
        (
            "マリアベルさんが表紙だなんて\x01",
            "これは保存版確定ねっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FEC")

    Jump("loc_67EE")

    label("loc_5FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60F5")

    #C0342
    ChrTalk(
        0xFE,
        (
            "お買い物に行ったら\x01",
            "アルカンシェルの噂をしてたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xFE,
        (
            "でもあたし、イリアさんより\x01",
            "マリアベルさんの方が好きかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "マリアベルさんはＩＢＣに勤めていて\x01",
            "クロスベル一の令嬢って言われてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xFE,
        "すっごくカッコイイんだから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_617C")

    label("loc_60F5")


    #C0346
    ChrTalk(
        0xFE,
        (
            "マリアベルさんは\x01",
            "ＩＢＣ総裁の一人娘なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xFE,
        (
            "若き天才女性経営者で\x01",
            "おまけに超絶美貌の持ち主なのよ。\x01",
            "すっごくカッコイイんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_617C")

    Jump("loc_67EE")

    label("loc_6181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6240")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6208")

    #C0348
    ChrTalk(
        0xFE,
        "あしたは日曜学校があるの。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "は～あ、面倒ねー。\x01",
            "モデルさんになるのに\x01",
            "学校のお勉強も必要なのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_623B")

    label("loc_6208")


    #C0350
    ChrTalk(
        0xFE,
        (
            "あしたは日曜学校があるの。\x01",
            "は～あ、面倒ねー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_623B")

    Jump("loc_67EE")

    label("loc_6240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_630E")

    #C0351
    ChrTalk(
        0xFE,
        (
            "クロスベルには有名な\x01",
            "ファッション雑誌が５つもあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "３つはクロスベルの雑誌社で、\x01",
            "２つは帝国と共和国の雑誌なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "あたし、全部ばっちり\x01",
            "チェックしてるんだから～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_636C")

    label("loc_630E")


    #C0354
    ChrTalk(
        0xFE,
        (
            "あたし、将来は\x01",
            "モデルさんになるんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "ファッション雑誌の\x01",
            "チェックは基本よね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_636C")

    Jump("loc_67EE")

    label("loc_6371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_657E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6506")

    #C0356
    ChrTalk(
        0xFE,
        (
            "おとーさんは\x01",
            "鉄道技師なのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "今日も出張だって。\x01",
            "また２ヶ月は帰ってこないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#0000Fウェンディのお父さんは\x01",
            "忙しい人だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        "でもねー、でもねー……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "そのくせお姉ちゃんを\x01",
            "導力オモチャで育て上げて\x01",
            "技師にしちゃったのよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        "あたしも気をつけないと。\x02",
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
    SetScenarioFlags(0x0, 3)
    Jump("loc_6576")

    label("loc_6506")


    #C0362
    ChrTalk(
        0xFE,
        "おとーさんは鉄道技師なの。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xFE,
        (
            "でもあたし、おとーさんがくれる\x01",
            "導力オモチャじゃ\x01",
            "ぜったい遊ばないんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6576")

    SetScenarioFlags(0x71, 5)
    Jump("loc_67EE")

    label("loc_657E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_6760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6599")
    Call(0, 16)
    Jump("loc_675B")

    label("loc_6599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E7")

    #C0364
    ChrTalk(
        0xFE,
        (
            "あたしね、大きくなったら\x01",
            "モデルさんになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "まちがってもお姉ちゃんみたいな\x01",
            "機械工にはならないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xFE,
        (
            "ぜったいボン・キュッ・ボ～ンの\x01",
            "おねーさんになるんだから！\x02",
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

    #C0367
    ChrTalk(
        0x104,
        "#0300F志は買うぜ、お嬢ちゃん……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_675B")

    label("loc_66E7")


    #C0368
    ChrTalk(
        0xFE,
        (
            "あたしね、大きくなったら\x01",
            "モデルさんになるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0xFE,
        (
            "まちがってもお姉ちゃんみたいな\x01",
            "機械工にはならないんだから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_675B")

    Jump("loc_67EE")

    label("loc_6760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_67EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677E")
    Call(0, 16)
    SetScenarioFlags(0x0, 3)
    Jump("loc_67EE")

    label("loc_677E")


    #C0370
    ChrTalk(
        0xFE,
        (
            "おとーさんもお姉ちゃんも\x01",
            "お片付けがへったくそなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0xFE,
        (
            "ぜーんぶあたしがやらなくちゃ\x01",
            "いけないんだから～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67EE")

    TalkEnd(0xFE)
    Return()

    # Function_15_5300 end

    def Function_16_67F2(): pass

    label("Function_16_67F2")


    #C0372
    ChrTalk(
        0xC,
        "掃除、洗濯、食器洗い……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xC,
        (
            "おとーさんもお姉ちゃんも\x01",
            "お片付けがへったくそなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xC,
        (
            "んもう、せーかつりょくが\x01",
            "無いんだから……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A0D")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0375
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、君は確か……\x01",
            "ウェンディの所の小さかった子？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0376
    ChrTalk(
        0xC,
        (
            "ほえ～？\x01",
            "お姉ちゃんのお知り合い？\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        (
            "#0000Fあ、いや何でもないよ。\x01",
            "ゴメン邪魔したみたいだな。\x02\x03",

            "#0004F（そっか……３年振りじゃ\x01",
            "  さすがに覚えてないよな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#0309Fへえ～、ロイドって\x01",
            "結構守備範囲が広いじゃんか㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0003Fち・が・い・ま・す。\x01",
            "誤解のある事を言わないでくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 1)

    label("loc_6A0D")

    Return()

    # Function_16_67F2 end

    def Function_17_6A0E(): pass

    label("Function_17_6A0E")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xC, 0xF, 0)
    TurnDirection(0xF, 0xC, 0)

    #C0380
    ChrTalk(
        0xF,
        (
            "パンセ、次の出張に行く前に\x01",
            "お土産を渡しておくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xF,
        (
            "ほら、導力車の動く模型だ！\x01",
            "僕の手作りだよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xF,
        (
            "しかもなんと、こうやって\x01",
            "導力波で遠隔操作できるんだ。\x01",
            "すごいだろ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xC,
        (
            "……何ソレ。\x01",
            "そんなのいらな～い。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0384
    ChrTalk(
        0xF,
        (
            "がーん……\x01",
            "画期的なおもちゃなのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x0, 5)
    Return()

    # Function_17_6A0E end

    def Function_18_6B54(): pass

    label("Function_18_6B54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B72")
    Call(0, 28)
    Return()

    label("loc_6B72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B8C")
    Call(0, 32)
    Return()

    label("loc_6B8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6C42")

    #C0385
    ChrTalk(
        0xFE,
        "あ、支援課お兄ちゃんたちだ。\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "祭りの日にパトかよ。\x01",
            "へへっ、残念だな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#0000Fはいはい。\x01",
            "……これから出かけるみたいだけど\x01",
            "あんまりはしゃぎすぎるなよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70F4")

    label("loc_6C42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D3C")

    #C0388
    ChrTalk(
        0xFE,
        (
            "ちぇっ、たった\x01",
            "１週間くらいだったんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "もうちょっと\x01",
            "飼いたかったのに、ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        (
            "まあいいや。\x01",
            "兄ちゃんたち、ありがとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "ちょっとだけ\x01",
            "見直してやったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x101,
        "#0003F君は素直じゃないな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6DB8")

    label("loc_6D3C")


    #C0393
    ChrTalk(
        0xFE,
        (
            "ちぇっ、父ちゃんさえ\x01",
            "うんって言ってくれりゃあ\x01",
            "飼えたのにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "……まあいいや。\x01",
            "飼い主のトコに\x01",
            "戻ったんだもんなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB8")

    Jump("loc_70F4")

    label("loc_6DBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E93")

    #C0395
    ChrTalk(
        0xFE,
        (
            "ホントはオレたちで\x01",
            "飼いたかったんだけどさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "父ちゃんがどーしても\x01",
            "許してくれないんだよな。\x01",
            "アンリん家もペット禁止らしいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xFE,
        (
            "つーわけで\x01",
            "頼むぜ兄ちゃんたち！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70F4")

    label("loc_6E93")

    TurnDirection(0xE, 0x0, 0)
    OP_4B(0xE, 0xFF)

    #C0398
    ChrTalk(
        0xD,
        (
            "兄ちゃんたち、\x01",
            "用事ってのはもういいのか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        (
            "ならこいつの飼い主を\x01",
            "探してやってくれよな～。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6F63"),
        (1, "loc_7018"),
        (SWITCH_DEFAULT, "loc_70E9"),
    )


    label("loc_6F63")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    SetChrPos(0x101, -55490, 0, 108350, 270)
    SetChrPos(0x102, -54150, 0, 108180, 270)
    SetChrPos(0x103, -55490, 0, 109530, 270)
    SetChrPos(0x104, -54090, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 90)
    SetChrPos(0xE, -57930, 0, 110500, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_29(0x8, 0x1, 0x1)
    Call(0, 29)
    Return()

    label("loc_7018")


    #C0400
    ChrTalk(
        0x101,
        (
            "#0006F悪いけど今は用事があるんだ。\x01",
            "手が開いたら\x01",
            "来れると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xE,
        (
            "分かりました、それまでは\x01",
            "僕たちで面倒をみてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xD,
        (
            "ちぇっ、しょーがねーな。\x01",
            "来るなら早めに頼むぜ、\x01",
            "兄ちゃんたち！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_70E9")

    label("loc_70E9")

    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)

    label("loc_70F4")

    TalkEnd(0xFE)
    Return()

    # Function_18_6B54 end

    def Function_19_70F8(): pass

    label("Function_19_70F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7116")
    Call(0, 28)
    Return()

    label("loc_7116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7130")
    Call(0, 32)
    Return()

    label("loc_7130")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7278")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7207")

    #C0403
    ChrTalk(
        0xFE,
        (
            "皆さん、ありがとう\x01",
            "ございました！\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "ちゃんと後で掃除するって\x01",
            "リュウのお父さんとの\x01",
            "約束だったので、大変ですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "少しの間でも仔猫が飼えて\x01",
            "とっても楽しかったです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_7273")

    label("loc_7207")


    #C0406
    ChrTalk(
        0xFE,
        (
            "少しの間でも仔猫が飼えて\x01",
            "とっても楽しかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        (
            "僕も……いつかカワイイ猫を\x01",
            "飼ってみたいなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7273")

    Jump("loc_7551")

    label("loc_7278")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x2)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_731B")

    #C0408
    ChrTalk(
        0xFE,
        (
            "リュウのお父さんは厳しいから\x01",
            "きちんと後片付けをしないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xFE,
        (
            "あ、皆さん。\x01",
            "その子のことよろしく\x01",
            "お願いしますね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7551")

    label("loc_731B")

    TurnDirection(0xD, 0x0, 0)
    OP_4B(0xD, 0xFF)

    #C0410
    ChrTalk(
        0xE,
        (
            "皆さん、この子の飼い主を\x01",
            "探してもらっていいですか？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_73C0"),
        (1, "loc_7475"),
        (SWITCH_DEFAULT, "loc_7546"),
    )


    label("loc_73C0")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    SetChrPos(0x101, -55490, 0, 108350, 270)
    SetChrPos(0x102, -54150, 0, 108180, 270)
    SetChrPos(0x103, -55490, 0, 109530, 270)
    SetChrPos(0x104, -54090, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 90)
    SetChrPos(0xE, -57930, 0, 110500, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_29(0x8, 0x1, 0x1)
    Call(0, 29)
    Return()

    label("loc_7475")


    #C0411
    ChrTalk(
        0x101,
        (
            "#0006F悪いけど今は用事があるんだ。\x01",
            "手が開いたら\x01",
            "来れると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        (
            "分かりました、それまでは\x01",
            "僕たちで面倒をみてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xD,
        (
            "ちぇっ、しょーがねーな。\x01",
            "来るなら早めに頼むぜ、\x01",
            "兄ちゃんたち！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_7546")

    label("loc_7546")

    OP_93(0xD, 0x0, 0x0)
    OP_4C(0xD, 0xFF)

    label("loc_7551")

    TalkEnd(0xFE)
    Return()

    # Function_19_70F8 end

    def Function_20_7555(): pass

    label("Function_20_7555")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7712")

    #C0414
    ChrTalk(
        0xFE,
        (
            "やあロイド君、久し振りだね。\x01",
            "お仕事は頑張ってるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x101,
        (
            "#0000Fフェイさん……\x01",
            "ご無沙汰してました。\x02\x03",

            "記念祭は帰国なさってたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "あはは……明日からは\x01",
            "また２ヶ月ほど出張なんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        "#0005Fまた鉄道の敷設工事ですか……？\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "世界にはまだまだ\x01",
            "導力技術が低い国が多いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "鉄道を作るだけじゃなくて\x01",
            "管理や安全な運用の\x01",
            "ノウハウを伝えなきゃならない。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0xFE,
        (
            "僕も技術指導員として\x01",
            "頑張らないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 2)
    Jump("loc_7751")

    label("loc_7712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7724")
    Call(0, 17)
    Jump("loc_7751")

    label("loc_7724")


    #C0421
    ChrTalk(
        0xFE,
        (
            "うーん、パンセには\x01",
            "まだ早かったかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7751")

    Jump("loc_785E")

    label("loc_7756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_785E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_781D")

    #C0422
    ChrTalk(
        0x101,
        (
            "#0005Fあ、ウェンディの\x01",
            "お父さんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        "#0100Fなんだかお疲れ……みたいね。\x02",
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0xFE,
        (
            "むにゃむにゃ……\x01",
            "出張から戻ったばかりなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        "パンセ、今日は寝かせておくれ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_785E")

    label("loc_781D")


    #C0426
    ChrTalk(
        0xFE,
        (
            "我が家のふかふかベッド……\x01",
            "むにゃむにゃ、気持ちいいなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_785E")

    TalkEnd(0xFE)
    Return()

    # Function_20_7555 end

    def Function_21_7862(): pass

    label("Function_21_7862")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_78E0")

    #C0427
    ChrTalk(
        0xFE,
        "……旅の支度をしなくっちゃ。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "今度はマインツ連山を\x01",
            "踏破してくるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0xFE,
        "前から行ってみたかったの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AD5")

    label("loc_78E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_78F1")
    Call(0, 13)
    Jump("loc_7AD5")

    label("loc_78F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_7941")

    #C0430
    ChrTalk(
        0xFE,
        "そろそろ次の旅に出かけようかな。\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        "……次はどこに行こう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AD5")

    label("loc_7941")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_79C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795C")
    Call(0, 22)
    Jump("loc_79BC")

    label("loc_795C")


    #C0432
    ChrTalk(
        0xFE,
        (
            "今日はカテリーナと\x01",
            "郊外を散歩する予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "……見晴らしのいい所を\x01",
            "案内してあげよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79BC")

    Jump("loc_7AD5")

    label("loc_79C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A10")
    OP_93(0xFE, 0x0, 0x0)

    #C0434
    ChrTalk(
        0xFE,
        "うん、パレードはいいね。\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        "あのまま旅に出れそう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7AD5")

    label("loc_7A10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7A21")
    Call(0, 22)
    Jump("loc_7AD5")

    label("loc_7A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_7A2F")
    Jump("loc_7AD5")

    label("loc_7A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7A3D")
    Jump("loc_7AD5")

    label("loc_7A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7AD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AB8")

    #C0436
    ChrTalk(
        0xFE,
        (
            "久し振りに家に帰ってきたら\x01",
            "……街が騒がしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xFE,
        (
            "うるさい……\x01",
            "これだからニンゲンは……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7AD5")

    label("loc_7AB8")

    OP_93(0xFE, 0xB4, 0x0)

    #C0438
    ChrTalk(
        0xFE,
        "もういい、寝る。\x02",
    )

    CloseMessageWindow()

    label("loc_7AD5")

    TalkEnd(0xFE)
    Return()

    # Function_21_7862 end

    def Function_22_7AD9(): pass

    label("Function_22_7AD9")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7B81")
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x12, 0x5A, 0x0)

    #C0439
    ChrTalk(
        0x12,
        "チルルって、料理上手なんだ……\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x11,
        "宿がないときは野宿だから。\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0x11,
        "さっさと食べて出かけよう。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x12,
        "う、うん、そうだね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 7)
    Jump("loc_7D4A")

    label("loc_7B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7D4A")
    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CA2")

    #C0443
    ChrTalk(
        0x11,
        "リュウたち出かけてるし、遊ぼう。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x12,
        "いいけど、何して遊ぶの？\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x11,
        (
            "わたしが方々で\x01",
            "集めてきた記念品がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x11,
        (
            "この砂は、共和国の砂浜で\x01",
            "小瓶に詰めてきたもの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0447
    ChrTalk(
        0x12,
        (
            "……チルルって相変わらず\x01",
            "変てこな趣味してるねー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7D4A")

    label("loc_7CA2")


    #C0448
    ChrTalk(
        0x11,
        (
            "これは古い鉄道車両のプレート。\x01",
            "ベルガード門の人にもらったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x11,
        (
            "こっちはリベールの飛行船で\x01",
            "使われていた導力灯の部品だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x12,
        "ふふっ、変てこなのばっかりねー。\x02",
    )

    CloseMessageWindow()

    label("loc_7D4A")

    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_22_7AD9 end

    def Function_23_7D53(): pass

    label("Function_23_7D53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D71")
    Call(0, 22)
    Jump("loc_7DDB")

    label("loc_7D71")


    #C0451
    ChrTalk(
        0xFE,
        (
            "さすが、いつも\x01",
            "一人旅してるだけのことはあるわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0xFE,
        (
            "味付けまでカンペキなのは\x01",
            "ちょっと意外だけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DDB")

    Jump("loc_7E45")

    label("loc_7DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7E39")
    OP_93(0xFE, 0x0, 0x0)

    #C0453
    ChrTalk(
        0xFE,
        "今年は車が沢山出てたね。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0xFE,
        "チルルも凄かったって思うでしょ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E45")

    label("loc_7E39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7E45")
    Call(0, 22)

    label("loc_7E45")

    TalkEnd(0xFE)
    Return()

    # Function_23_7D53 end

    def Function_24_7E49(): pass

    label("Function_24_7E49")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF9")
    OP_29(0x46, 0x1, 0xB)

    #C0455
    ChrTalk(
        0x101,
        (
            "#0003F（これで西通りも\x01",
            "  一通り回ったけど……）\x02\x03",

            "#0001F（……みんなの捜索状況は\x01",
            "  どうなってるかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x160,
        "#3308F（…………………………）\x02",
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 7)

    label("loc_7EF9")

    Return()

    # Function_24_7E49 end

    def Function_25_7EFA(): pass

    label("Function_25_7EFA")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7F81")
    OP_68(56910, 1000, 104970, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 56750, 0, 104300, 0)
    SetChrPos(0x102, 57300, 0, 103300, 0)
    SetChrPos(0x103, 56100, 0, 103300, 0)
    SetChrPos(0x104, 56750, 0, 102300, 0)
    Jump("loc_7FF3")

    label("loc_7F81")

    OP_68(51830, 1200, 115000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 51830, 0, 114500, 0)
    SetChrPos(0x102, 51300, 0, 113500, 0)
    SetChrPos(0x103, 52300, 0, 113650, 0)
    SetChrPos(0x104, 51830, 0, 112500, 0)

    label("loc_7FF3")

    OP_93(0x9, 0xB4, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0457
    ChrTalk(
        0x9,
        "#1Pあら？\x02",
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x9,
        "#1Pあらあら？　その顔は……\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x101,
        (
            "#0012Fははは……\x01",
            "おばさん、ただいま。\x02\x03",

            "顔を出すのが\x01",
            "遅くなっちゃったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x9,
        (
            "#1Pロイド君じゃない……！\x01",
            "まあまあ、よく帰ってきたわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x9,
        (
            "#1P無事に警察に\x01",
            "就職したって聞いたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x9,
        (
            "#1P……どうなの、職場の方は。\x01",
            "もうお仕事は始まったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#0004Fうん、まあ……\x01",
            "とっても（気楽で）いい所だよ。\x02\x03",

            "#0000F課長も放任主義みたいでさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x9,
        (
            "#1Pあらあら、そうなの？\x01",
            "何だか楽しそうな部署なのねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x9,
        (
            "#1Pまあ何はともあれ、元気に\x01",
            "顔を出してくれて嬉しいわ。\x01",
            "これは空の女神#8Rエ イ ド ス#に感謝ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x9,
        (
            "#1P……ロイド君、寮暮らしで\x01",
            "困った事があったら\x01",
            "いつでも言って頂戴ね？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x9,
        "#1Pおばさん、寮まで駆けつけるから！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0468
    ChrTalk(
        0x101,
        (
            "#0012Fいや、もう子供じゃないんだし。\x01",
            "警察学校も寮だったから\x01",
            "全然平気なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x9,
        (
            "#1P……ダメよ、ロイド君！\x01",
            "ようやく戻ってきたんだから\x01",
            "おばさんに世話を焼かせて頂戴！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1200)

    #C0470
    ChrTalk(
        0x101,
        (
            "#0006Fゴ、ゴメンおばさん……\x01",
            "今度菓子折りでも\x01",
            "持ってくるからさ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x104,
        "#0300F（ロイド、押されてるなぁ。）\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x103,
        (
            "#0200F（優しそうなのに\x01",
            "  パワフルな人ですね。）\x02\x03",

            "（……血縁の方では\x01",
            "  ないようですが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x102,
        (
            "#0100F（ふふ、でも家族って感じね。\x01",
            "  ……少し羨ましいかも。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_84C2")
    SetChrPos(0x0, 56750, 0, 105300, 0)
    Jump("loc_84D3")

    label("loc_84C2")

    SetChrPos(0x0, 51830, 0, 114500, 0)

    label("loc_84D3")

    SetScenarioFlags(0x4E, 0)
    EventEnd(0x5)
    Return()

    # Function_25_7EFA end

    def Function_26_84D9(): pass

    label("Function_26_84D9")

    EventBegin(0x0)
    Fade(500)
    OP_68(51830, 1200, 115000, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x101, 51830, 0, 114500, 0)
    SetChrPos(0x102, 51300, 0, 113500, 0)
    SetChrPos(0x103, 52300, 0, 113650, 0)
    SetChrPos(0x104, 51830, 0, 112350, 0)
    OP_93(0x9, 0xB4, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    #C0474
    ChrTalk(
        0x101,
        (
            "#0005Fそうだ、おばさん……\x01",
            "昨日セシル姉に会ってきたよ。\x02\x03",

            "#0000F全然変わってなかったけど、\x01",
            "やっぱり久し振りに会うと\x01",
            "照れるかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x9,
        "あら、そうだったの……\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x9,
        (
            "……で、どうだったの？\x01",
            "いい人でもいそうだった！？\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x101,
        (
            "#0005Fえ゛……\x01",
            "そ、それは分からないけど……\x01",
            "（というか、いて欲しくない……）\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x9,
        (
            "ふう、あの子もそろそろ\x01",
            "将来の事を考えなきゃダメなのにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x9,
        (
            "……一度お見合いなんかも\x01",
            "セッティングしてみようかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x104, 0x0, 0x0, 0xFA, 0x3E8, 0x0)

    #C0480
    ChrTalk(
        0x104,
        (
            "#0309F（むむ、そういう事か！？\x01",
            "  よしここは一つ\x01",
            "  俺が立候補して……ッ！）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0481
    ChrTalk(
        0x102,
        "#0111F（ランディ、あなたねぇ……）\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x101,
        (
            "#0012Fはは、ははは……\x01",
            "（まさか、そんな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x103,
        (
            "#0200Fあのロイドさん……\x01",
            "声が乾いてますよ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 51830, 0, 114500, 0)
    SetScenarioFlags(0x70, 5)
    EventEnd(0x5)
    Return()

    # Function_26_84D9 end

    def Function_27_8814(): pass

    label("Function_27_8814")

    EventBegin(0x0)
    Fade(500)
    OP_68(-58260, 1000, 57850, 0)
    MoveCamera(46, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32000, 0)
    SetChrPos(0x101, -57760, 0, 57480, 0)
    SetChrPos(0x102, -58760, 0, 57230, 0)
    SetChrPos(0x103, -57760, 0, 55980, 0)
    SetChrPos(0x104, -58760, 0, 55730, 0)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 1)), scpexpr(EXPR_END)), "loc_89E1")

    #C0484
    ChrTalk(
        0x101,
        (
            "#11P#0000F（フェイさん、いないみたいだし……\x01",
            "  パンセちゃんに聞いてみるか。）\x02\x03",

            "……やぁパンセ。\x01",
            "フェイおじさんは今日は仕事かい？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xC, 0xB4, 0x1F4)

    #C0485
    ChrTalk(
        0xC,
        (
            "#5Pあ、ウェンディお姉ちゃんの\x01",
            "お友達のひと。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xC,
        "#5Pどーも、なにかご用？\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        (
            "#11P#0000Fうん、ちょっと\x01",
            "フェイおじさんに聞きたい事が\x01",
            "あるんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B8C")

    label("loc_89E1")


    #C0488
    ChrTalk(
        0x101,
        (
            "#11P#0000F（フェイさん、いないみたいだし……\x01",
            "  ちょっとこの子に聞いてみるか。）\x02\x03",

            "#0005Fってあれ、君は確か……\x01",
            "フェイさんの所の\x01",
            "あの小さかった子だよな？\x02\x03",

            "ウェンディの妹なのに\x01",
            "全然似てないっていう……\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xC, 0xFF)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0xC, 0xB4, 0x1F4)

    #C0489
    ChrTalk(
        0xC,
        (
            "#5Pあ……お兄さん確か、\x01",
            "ウェンディお姉ちゃんの\x01",
            "お友達だっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x101,
        (
            "#11P#0002Fはは、覚えててくれたかな。\x02\x03",

            "ちょっとフェイおじさんに\x01",
            "聞きたい事があるんだけど……\x01",
            "おじさんは今日は仕事かい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8C")


    #C0491
    ChrTalk(
        0xC,
        "#5Pおとーさんは今、出張中なの。\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0xC,
        "#5Pまだ２ヶ月は帰ってこないのよ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 5)), scpexpr(EXPR_END)), "loc_8C29")

    #C0493
    ChrTalk(
        0x101,
        (
            "#11P#0003Fああ、そんな事言ってたっけ……\x01",
            "………まいったな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C53")

    label("loc_8C29")


    #C0494
    ChrTalk(
        0x101,
        "#11P#0003Fそ、そうか、まいったな……\x02",
    )

    CloseMessageWindow()

    label("loc_8C53")


    #C0495
    ChrTalk(
        0x104,
        (
            "#12P#0306F勝手に家捜しするワケにも\x01",
            "いかねーしな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0496
    ChrTalk(
        0xC,
        "#5P何か探してるの？\x02",
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#12P#0100Fお姉さんたちは、お嬢ちゃんの\x01",
            "お父さんが借りたご本を\x01",
            "返してもらいに来たのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x103,
        "#11P#0200F……何か聞いてませんか？\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0xC,
        "#5Pんー……\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xC,
        (
            "#5Pもしかして、\x01",
            "あたしが読んでるこの本かな。\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x101,
        (
            "#11P#0005Fあ……\x01",
            "ちょっと見せてもらっていいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0xC,
        "#5Pどーぞ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0503
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パンセは自分の持っていた本を\x01",
            "ロイドたちに見せた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0504
    ChrTalk(
        0x101,
        (
            "#11P#0000F……図書館の印が入ってる。\x01",
            "この本に間違いなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xC,
        "#5Pあ、そーなんだ。\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xC,
        (
            "#5Pまったく、おとーさんったら\x01",
            "本を返さずに出張に\x01",
            "行っちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xC,
        (
            "#5Pお兄さん、なんなら\x01",
            "その本持ってっていいよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x101,
        (
            "#11P#0005Fいいのかい？\x01",
            "今、読んでいたんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x103,
        (
            "#11P#0200F改めて申請すれば、\x01",
            "返却期限の延長も可能かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xC,
        "#5Pいーの。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xC,
        (
            "#5Pヒマだから読んでたけど、\x01",
            "つまらないんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xC,
        "#5P本のタイトル見てよ。\x02",
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        (
            "#11P#0000Fえーっと、なになに……\x01",
            "『鉄道マニアのススメ』……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x104,
        "#12P#0300F妙にマニアックな本だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xC,
        (
            "#5Pたぶん、おとーさんが\x01",
            "あたしを鉄道技師の世界に\x01",
            "連れて行くために借りたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0xC,
        (
            "#5Pその手には乗らないんだから。\x01",
            "お兄さんたち、さっさとそれ\x01",
            "持っていっちゃって。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x101,
        (
            "#11P#0000Fう、うん、そうだな。\x01",
            "ご協力感謝するよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0518
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D5, 1)
    OP_29(0x5, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x3)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x5, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9183")
    OP_29(0x5, 0x1, 0x1F)

    label("loc_9183")

    SetChrPos(0x0, -58260, 0, 57480, 0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 4)
    EventEnd(0x5)
    Return()

    # Function_27_8814 end

    def Function_28_91A5(): pass

    label("Function_28_91A5")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-56430, 1100, 108630, 0)
    MoveCamera(37, 18, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34090, 0)
    OP_4B(0x13, 0xFF)
    SetChrPos(0x101, -55690, 0, 108350, 270)
    SetChrPos(0x102, -54350, 0, 108180, 270)
    SetChrPos(0x103, -55690, 0, 109530, 270)
    SetChrPos(0x104, -54390, 0, 109530, 270)
    SetChrPos(0xD, -58000, 0, 107500, 0)
    SetChrPos(0xE, -57930, 0, 110500, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_93(0xE, 0x5A, 0x1F4)
    Sleep(300)

    #C0519
    ChrTalk(
        0xD,
        "#12Pあっ、支援課の兄ちゃんたち！？\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xE,
        (
            "#6P皆さん……\x01",
            "あの、お久しぶりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x101,
        (
            "#11P#0000Fああ、１週間ぶりくらいだな。\x02\x03",

            "#0005Fで……何をやってるんだ？\x01",
            "その仔猫は……？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x102,
        (
            "#11P#0105F随分小さい仔猫ね。\x01",
            "生後半年くらいかしら。\x02\x03",

            "#0100Fあなた達で飼っているの？\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xE,
        (
            "#6Pいえ、実は……\x01",
            "西通りで見つけたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0xE,
        "#6P迷子になってたみたいで。\x02",
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xD,
        (
            "#12Pへっへー、だいぶ弱ってたけど\x01",
            "オレたちでエサをやってさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0xD,
        (
            "#12Pこのとおり元気になったんだぜ～。\x01",
            "すげえだろっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0527
    ChrTalk(
        0xE,
        "#6Pあはは、でも………\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 500)
    Sleep(300)

    #C0528
    ChrTalk(
        0xE,
        (
            "#6Pねえリュウ、支援課の\x01",
            "皆さんに頼んでみない？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(300)

    #C0529
    ChrTalk(
        0xD,
        "#12Pえっ、あれをか～？\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xE,
        "#6Pだって僕たちじゃ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0531
    ChrTalk(
        0x104,
        "#0305F#11Pあれって……何の話だ？\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_93(0xE, 0x5A, 0x1F4)

    #C0532
    ChrTalk(
        0xE,
        (
            "#6Pあの、実は\x01",
            "皆さんに頼みごとが……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xE,
        "#6P聞いていただけますか？\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(300)
    SetChrName("")

    #A0534
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達はリュウとアンリから\x01",
            "仔猫を見つけた経緯を詳しく聞いた。\x02",
        )
    )

    CloseMessageWindow()

    #A0535
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そして……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0536
    ChrTalk(
        0x103,
        (
            "#0205F#11P仔猫の飼い主を\x01",
            "探して欲しい……？\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0xE,
        (
            "#6Pはい、実は見つけたときは\x01",
            "首輪をしていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xE,
        (
            "#6P弱ってるときは苦しそうだから\x01",
            "外しちゃったんですけど\x01",
            "ホントは飼い主がいるのかなって。\x02",
        )
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0xD,
        (
            "#12Pなんかオレたちには\x01",
            "イマイチなつかねーしさぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        (
            "#11P#0003Fそうか、確かに飼い主がいるなら\x01",
            "心配しているだろうし……\x02\x03",

            "#0001F仔猫のためにも返すべきだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x102,
        (
            "#11P#0100F飼い主の手がかりは\x01",
            "あるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xD,
        (
            "#12Pん～、そうだな。\x01",
            "アンリとは子供じゃないかって\x01",
            "話してたんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0543
    ChrTalk(
        0xE,
        "#6P付けていた首輪は手作りみたいで。\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xE,
        (
            "#6P大人と言うよりは\x01",
            "僕たちくらいの子供が\x01",
            "作ったものみたいでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x104,
        (
            "#0303F#11Pふむ、となると\x01",
            "子供のいる世帯を中心に\x01",
            "聞き込みってことになるか……\x02\x03",

            "そこそこ時間は掛かりそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0546
    ChrTalk(
        0x104,
        "#0300F#11Pロイド、どうする？\x02",
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x101,
        "#11P#0003Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_29(0x8, 0x4, 0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめておく】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9A34"),
        (1, "loc_9A3E"),
        (SWITCH_DEFAULT, "loc_9B20"),
    )


    label("loc_9A34")

    OP_29(0x8, 0x1, 0x2)
    Call(0, 29)
    Return()

    label("loc_9A3E")


    #C0548
    ChrTalk(
        0x101,
        (
            "#11P#0006F悪いけど今は用事があるんだ。\x01",
            "手が開いたら\x01",
            "来れると思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0xE,
        (
            "#6P分かりました、それまでは\x01",
            "僕たちで面倒をみてますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xD,
        (
            "#12Pちぇっ、しょーがねーな。\x01",
            "来るなら早めに頼むぜ、\x01",
            "兄ちゃんたち！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_29(0x8, 0x1, 0x0)
    Jump("loc_9B20")

    label("loc_9B20")

    Fade(500)
    SetChrPos(0x0, -55530, 0, 109140, 270)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0xB4, 0x0)
    OP_4C(0x13, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_91A5 end

    def Function_29_9B53(): pass

    label("Function_29_9B53")

    SetChrFlags(0xD, 0x40)
    OP_4B(0x13, 0xFF)

    #C0551
    ChrTalk(
        0x101,
        (
            "#11P#0000Fよし、ウルスラ病院に行くのは\x01",
            "少し遅れるけど……\x01",
            "仔猫の飼い主を探してしまおう。\x02\x03",

            "まずは仔猫を\x01",
            "連れて行かないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x104, 0x101, 500)
    Sleep(200)

    #C0552
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさん、相手は\x01",
            "体力の無い仔猫ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x102,
        (
            "#11P#0105F連れて歩くのは\x01",
            "酷じゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9CB8():

        label("loc_9CB8")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_9CB8")

    QueueWorkItem2(0xE, 1, lambda_9CB8)

    def lambda_9CCA():

        label("loc_9CCA")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_9CCA")

    QueueWorkItem2(0x103, 1, lambda_9CCA)

    def lambda_9CDC():

        label("loc_9CDC")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_9CDC")

    QueueWorkItem2(0x104, 1, lambda_9CDC)

    def lambda_9CEE():

        label("loc_9CEE")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_9CEE")

    QueueWorkItem2(0x102, 1, lambda_9CEE)
    BeginChrThread(0x101, 1, 0, 30)
    OP_68(-55760, 500, 110100, 3000)

    #C0554
    ChrTalk(
        0x101,
        (
            "#11P#0004Fいや、大丈夫だと思う。\x02\x03",

            "#0000Fちょっといいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0xD,
        "#6Pえ、うん……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    BeginChrThread(0xD, 1, 0, 31)
    Sleep(300)

    def lambda_9D79():
        OP_95(0xFE, -58000, 0, 107500, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D79)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(500)
    OP_6F(0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x102, 0x1)

    #C0556
    ChrTalk(
        0x101,
        "#11P#0009Fよし、おいでおいで……\x02",
    )

    CloseMessageWindow()
    Sound(823, 0, 100, 0)
    Sleep(200)
    TurnDirection(0x13, 0x101, 300)
    Sleep(800)
    OP_95(0x13, -58010, 700, 108520, 300, 0x0)
    OP_93(0x13, 0xB4, 0x1F4)
    Sleep(1000)
    Sound(804, 0, 100, 0)
    Fade(500)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0557
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは仔猫を抱きかかえ\x01",
            "そっとジャケットの中に保護した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0558
    ChrTalk(
        0x101,
        (
            "#11P#0000Fうん、うまく\x01",
            "行ったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0559
    ChrTalk(
        0x101,
        (
            "#5P#0000Fどうかな。\x01",
            "安全に移動できると思うんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0x104,
        "#0309F#11Pおお、いいんじゃねえか？\x02",
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x103,
        "#0200F#11P中々やりますね。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        (
            "#11P#0100Fふふ、意外とスムーズに\x01",
            "行ってくれたみたいね。\x02\x03",

            "それじゃあ聞き込みの方だけど\x01",
            "……子供がいる世帯を中心に\x01",
            "という事でよかったのよね？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 500)
    TurnDirection(0xD, 0x102, 500)

    #C0563
    ChrTalk(
        0xE,
        "#6Pええ、それと……\x02",
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xE,
        (
            "#6P見つけた場所が住宅街に\x01",
            "近かったので、もしかすると\x01",
            "向こうから迷い込んだのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x101,
        (
            "#11P#0003Fどちらにしろ\x01",
            "ベッドタウンだな……\x02\x03",

            "#0000Fよし、子供がいる家を\x01",
            "１軒ずつ当たってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0566
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【仔猫の飼い主探し】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x0, 0x1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -55530, 0, 109140, 180)
    SetChrPos(0xD, -57650, 0, 110300, 180)
    SetChrPos(0xE, -58450, 0, 110300, 180)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    ClearChrFlags(0xD, 0x40)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_9B53 end

    def Function_30_A160(): pass

    label("Function_30_A160")

    OP_95(0x101, -56270, 0, 107500, 1000, 0x0)
    OP_95(0x101, -57120, 0, 107500, 1000, 0x0)
    OP_93(0x101, 0x10E, 0x1F4)
    Return()

    # Function_30_A160 end

    def Function_31_A190(): pass

    label("Function_31_A190")

    OP_95(0xD, -57290, 0, 106710, 1000, 0x0)
    OP_93(0xD, 0x0, 0x1F4)
    Return()

    # Function_31_A190 end

    def Function_32_A1AC(): pass

    label("Function_32_A1AC")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(-54300, 700, 110230, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(31500, 0)
    SetChrPos(0x101, -54200, 0, 108980, 0)
    SetChrPos(0x102, -55340, 0, 107320, 0)
    SetChrPos(0x103, -55340, 0, 108980, 0)
    SetChrPos(0x104, -54200, 0, 107320, 0)
    SetChrPos(0xD, -53900, 0, 110740, 180)
    SetChrPos(0xE, -55030, 0, 110700, 180)
    OP_0D()

    #C0567
    ChrTalk(
        0xD,
        "#5Pおっ、兄ちゃんたち。\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0xD,
        (
            "#5Pどうだったんだ～？\x01",
            "仔猫の飼い主、みつかったかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0x101,
        (
            "#0000Fああ、勿論だ。\x02\x03",

            "少しトラブルはあったけど\x01",
            "本来の飼い主の元で\x01",
            "元気にしているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xD,
        (
            "#5Pそ、そっかー……\x01",
            "…………………\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0xE,
        (
            "#5Pよかったです、\x01",
            "僕たちのせわだけじゃ\x01",
            "やっぱり心配でしたし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0xD, 300)
    Sleep(300)

    #C0572
    ChrTalk(
        0xE,
        (
            "#5P……リュウ？\x01",
            "もしかして寂しいの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xD, 0xE, 500)

    #C0573
    ChrTalk(
        0xD,
        "#11Pそ、そんなんじゃねえよ！\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)

    #C0574
    ChrTalk(
        0xD,
        (
            "#11Pほらアンリ、\x01",
            "さっさと片付けすませて\x01",
            "遊びにいこうぜっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0xE,
        "#5Pうん、そうだね。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(300)

    #C0576
    ChrTalk(
        0xE,
        (
            "#5P皆さん、ありがとう\x01",
            "ございました！\x02",
        )
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x104,
        "#12P#0309Fおう、素直でいいこった。\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0x102,
        (
            "#12P#0100Fまた何かあったら\x01",
            "支援課に連絡して頂戴ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -54960, 0, 107860, 0)
    SetChrPos(0xD, -54470, 0, 110810, 315)
    SetChrPos(0xE, -57280, 0, 107430, 315)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x70, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_32_A1AC end

    SaveToFile()

Try(main)
