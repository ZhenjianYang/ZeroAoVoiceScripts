from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0570.bin",                # FileName
        "c0570",                    # MapName
        "c0570",                    # Location
        0x0027,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 39, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0570",                  # 0
        "エリック",               # 1
        "サンドラ",               # 2
        "ダドリー捜査官",         # 3
        "エマ捜査官",             # 4
        "客",                     # 5
        "客",                     # 6
        "客",                     # 7
        "遊撃士スコット",         # 8
        "遊撃士ヴェンツェル",     # 9
        "グレイス",               # 10
        "セルゲイ課長",           # 11
        "ソーニャ副司令",         # 12
        "食器",                   # 13
        "食器",                   # 14
        "いす",                   # 15
    ))

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch26802.itc",                   # 01
        "chr/ch32202.itc",                   # 02
        "chr/ch06002.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00900.itc",                   # 06
        "chr/ch30500.itc",                   # 07
        "chr/ch27200.itc",                   # 08
        "chr/ch27300.itc",                   # 09
        "chr/ch21600.itc",                   # 0A
        "chr/ch27802.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
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

    DeclNpc(0,       0,       6400,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-4699,   79,      4449,    0,    261,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-1200,   0,       4190,    45,   389,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-1340,   0,       2930,    45,   389,  0x0, 0,   7,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-2349,   100,     4449,    0,    389,  0x0, 0,   2,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(1240,    0,       1799,    0,    389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-8199,   100,     -479,    90,   405,  0x0, 0,   11,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(1480,    0,       2569,    0,    389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(1019,    0,       1539,    315,  389,  0x0, 0,   9,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-8399,   100,     -500,    90,   405,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       5000,    1000,    0,       1500,    6400,    0x007E, 0,  4,  0x0000)
    DeclActor(-4600,   0,       -480,    2500,    -4600,   1000,    -480,    0x007C, 0,  23, 0x0000)
    DeclActor(-8640,   0,       -490,    2500,    -8640,   1000,    -490,    0x007C, 0,  24, 0x0000)
    DeclActor(-6950,   0,       4150,    2000,    -6950,   500,     4150,    0x007C, 0,  25, 0x0000)

    ScpFunction((
        "Function_0_3B8",          # 00, 0
        "Function_1_470",          # 01, 1
        "Function_2_545",          # 02, 2
        "Function_3_66E",          # 03, 3
        "Function_4_7F8",          # 04, 4
        "Function_5_7FC",          # 05, 5
        "Function_6_257C",         # 06, 6
        "Function_7_25FA",         # 07, 7
        "Function_8_2900",         # 08, 8
        "Function_9_2B05",         # 09, 9
        "Function_10_385E",        # 0A, 10
        "Function_11_39C2",        # 0B, 11
        "Function_12_3B6E",        # 0C, 12
        "Function_13_3CC2",        # 0D, 13
        "Function_14_3E3D",        # 0E, 14
        "Function_15_3EA4",        # 0F, 15
        "Function_16_3F13",        # 10, 16
        "Function_17_3F48",        # 11, 17
        "Function_18_42D3",        # 12, 18
        "Function_19_4326",        # 13, 19
        "Function_20_4507",        # 14, 20
        "Function_21_4AB1",        # 15, 21
        "Function_22_4D7C",        # 16, 22
        "Function_23_4E0B",        # 17, 23
        "Function_24_4E60",        # 18, 24
        "Function_25_4EC4",        # 19, 25
        "Function_26_4F75",        # 1A, 26
        "Function_27_5409",        # 1B, 27
        "Function_28_5C51",        # 1C, 28
        "Function_29_5E18",        # 1D, 29
    ))


    def Function_0_3B8(): pass

    label("Function_0_3B8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3F8"),
        (1, "loc_404"),
        (2, "loc_410"),
        (3, "loc_41C"),
        (4, "loc_428"),
        (5, "loc_434"),
        (6, "loc_440"),
        (SWITCH_DEFAULT, "loc_44C"),
    )


    label("loc_3F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_404")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_410")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_41C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_428")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_434")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_440")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_458")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_46F")

    Return()

    # Function_0_3B8 end

    def Function_1_470(): pass

    label("Function_1_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_544")
    OP_95(0xFE, 780, 0, 1880, 1000, 0x0)
    OP_95(0xFE, -6210, 0, 1880, 1000, 0x0)
    OP_95(0xFE, -6210, 0, 830, 1000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -6210, 0, 1880, 1000, 0x0)
    OP_95(0xFE, -8480, 0, 1680, 1000, 0x0)
    OP_95(0xFE, -8480, 0, 6780, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0xFA)
    Sleep(2200)
    OP_95(0xFE, -8480, 0, 2480, 1000, 0x0)
    OP_95(0xFE, 290, 0, 2480, 1000, 0x0)
    OP_95(0xFE, 1170, 0, 3820, 1000, 0x0)
    Sleep(2800)
    Jump("Function_1_470")

    label("loc_544")

    Return()

    # Function_1_470 end

    def Function_2_545(): pass

    label("Function_2_545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_554")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 28)

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    ClearChrFlags(0x11, 0x80)

    label("loc_567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_584")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_66D")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_592")
    Jump("loc_66D")

    label("loc_592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_5AA")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_66D")

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5C2")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_66D")

    label("loc_5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_5D0")
    Jump("loc_66D")

    label("loc_5D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5F9")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -4700, 80, 4450, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_66D")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_611")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_66D")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_61F")
    Jump("loc_66D")

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_648")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -130, 0, 4420, 360)
    SetChrFlags(0x8, 0x10)
    Jump("loc_66D")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_656")
    Jump("loc_66D")

    label("loc_656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_664")
    Jump("loc_66D")

    label("loc_664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_66D")

    label("loc_66D")

    Return()

    # Function_2_545 end

    def Function_3_66E(): pass

    label("Function_3_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C2")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_70C")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 1)), scpexpr(EXPR_END)), "loc_70C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_70C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_728")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)
    Jump("loc_74D")

    label("loc_728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_744")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_74D")

    label("loc_744")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)

    label("loc_74D")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_767")
    Jump("loc_7A8")

    label("loc_767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_781")
    Jump("loc_7A8")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_78F")
    Jump("loc_7A8")

    label("loc_78F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_7A8")
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D7")
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_7D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7")
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)

    label("loc_7F7")

    Return()

    # Function_3_66E end

    def Function_4_7F8(): pass

    label("Function_4_7F8")

    Call(0, 5)
    Return()

    # Function_4_7F8 end

    def Function_5_7FC(): pass

    label("Function_5_7FC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_80D")
    Jump("loc_855")

    label("loc_80D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_83A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_835")
    Call(0, 26)
    Return()

    label("loc_835")

    Jump("loc_855")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_855")
    Call(0, 8)
    TalkEnd(0x8)
    Return()

    label("loc_855")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_85F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2578")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8BD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DD")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2573")

    label("loc_8DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F1")
    Jump("loc_2573")

    label("loc_8F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2573")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_992")

    #C0001
    ChrTalk(
        0x8,
        (
            "ルバーチェ構成員の\x01",
            "行方なんて知りませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "私はずっとここで\x01",
            "バーテンダーをやってる\x01",
            "だけなんですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A07")

    label("loc_992")


    #C0003
    ChrTalk(
        0x8,
        (
            "さっきから捜査一課の人が\x01",
            "事情を聴きに来るんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "まったく迷惑な話だ……\x01",
            "私はただのバーテンダーなのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A07")

    Jump("loc_2573")

    label("loc_A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A82")

    #C0005
    ChrTalk(
        0x8,
        (
            "昨晩からルバーチェ事務所の\x01",
            "様子がおかしい気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "……中で何を\x01",
            "やっているんでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AF3")

    #C0007
    ChrTalk(
        0x8,
        (
            "黒月の出方次第でしょうが……\x01",
            "……先行きが心配ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_END)), "loc_AEE")

    #C0008
    ChrTalk(
        0x8,
        "……またどうぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_AEE")

    Jump("loc_B67")

    label("loc_AF3")


    #C0009
    ChrTalk(
        0x8,
        "……事務所を襲撃、ですか。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "また唐突ですね……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "これで全面戦争なんてことに\x01",
            "ならなきゃいいんですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B67")

    Jump("loc_2573")

    label("loc_B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B9F")

    #C0012
    ChrTalk(
        0x8,
        "……ごゆっくりどうぞ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C1C")

    label("loc_B9F")


    #C0013
    ChrTalk(
        0x8,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "当店のステージは\x01",
            "夜８時を回ってからとなります。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "それまではごゆっくり\x01",
            "おくつろぎ下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C1C")

    Jump("loc_2573")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C96")

    #C0016
    ChrTalk(
        0x8,
        (
            "……自分は大した事は\x01",
            "知りませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "裏社会に流れる噂話を\x01",
            "耳にする程度なんですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DCB")

    label("loc_C96")


    #C0018
    ChrTalk(
        0x8,
        "近頃、妙な都市伝説を聞きますね。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "まあ、この街で都市伝説なんて\x01",
            "珍しくもない事です。\x01",
            "店の支度でもしましょう。\x02",
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

    #C0021
    ChrTalk(
        0x101,
        (
            "#0005F（都市伝説……？\x01",
            "  変な聞き込みだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_DCB")

    Jump("loc_2573")

    label("loc_DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_10DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 4)), scpexpr(EXPR_END)), "loc_FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E52")

    #C0022
    ChrTalk(
        0x8,
        (
            "なんでも競売会で\x01",
            "ヘマをやらかしたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "ルバーチェ内部も\x01",
            "ごたごたしているようですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE3")

    label("loc_E52")


    #C0024
    ChrTalk(
        0x8,
        (
            "この一週間、ルバーチェ商会も\x01",
            "やけに静かですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "なんでも競売会で\x01",
            "ヘマをやらかしたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "マルコーニ会長もハルトマン議長の\x01",
            "不興を買ったそうですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F47")

    #C0027
    ChrTalk(
        0x102,
        (
            "#0108F（さすがに裏通りには\x01",
            "  噂が流れているようね……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE0")

    label("loc_F47")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F93")

    #C0028
    ChrTalk(
        0x103,
        (
            "#0200F（さすがに裏通りには\x01",
            "  噂が流れてますね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE0")

    label("loc_F93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FE0")

    #C0029
    ChrTalk(
        0x104,
        (
            "#0306F（うーん、さすがに\x01",
            "  裏通りには噂が流れてるか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE0")

    SetScenarioFlags(0x0, 0)

    label("loc_FE3")

    Jump("loc_10D8")

    label("loc_FE8")


    #C0030
    ChrTalk(
        0x8,
        (
            "いらっしゃいませ。\x01",
            "ウチはまだ営業時間じゃありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x153,
        "#1111Fここは何のおミセ～？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "……………………………\x01",
            "……ジャズバーです。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "お子さんの入る店ではありませんよ。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0012Fす、すみません。\x01",
            "少し立ち寄っただけなんで。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 4)

    label("loc_10D8")

    Jump("loc_2573")

    label("loc_10DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_12D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_114E")

    #C0035
    ChrTalk(
        0x8,
        (
            "ルバーチェ商会は\x01",
            "今日は静かですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "お陰でこちらは\x01",
            "安心して営業できそうです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D0")

    label("loc_114E")


    #C0037
    ChrTalk(
        0x8,
        (
            "ルバーチェ商会は\x01",
            "今日は静かですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "構成員の半数は\x01",
            "例の屋敷に向かっているのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "……ここ７、８年は\x01",
            "毎年の事業のようですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0001F（《黒の競売会》……\x01",
            "  裏じゃ結構知られてるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0103F（有名と言ってもいいわね。\x01",
            "  私も噂は知っていたし……）\x02\x03",

            "#0101F（ルバーチェ側も宣伝を行って\x01",
            "  裏社会のステータス的なものに\x01",
            "  しているんじゃないかしら。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12D0")

    Jump("loc_2573")

    label("loc_12D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_1356")

    #C0042
    ChrTalk(
        0x8,
        (
            "アルカンシェルの前を\x01",
            "パレードが通過したそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "お客さんもこぞって\x01",
            "流れてしまいました。\x01",
            "やれやれ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_1356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_14F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_13B1")

    #C0044
    ChrTalk(
        0x8,
        "当店はお子様はお断りです。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "子供など１人も見ていませんよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14EF")

    label("loc_13B1")


    #C0046
    ChrTalk(
        0x101,
        (
            "#0001F（うん、この人なら\x01",
            "  何か知っているかもしれないな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0047
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

    #C0048
    ChrTalk(
        0x8,
        (
            "迷子ですか？\x01",
            "見ていませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "そもそも当店はジャズバーです。\x01",
            "子供のお客様は基本的にお断りですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003Fそ、そうですか……\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 22)

    label("loc_14EF")

    Jump("loc_2573")

    label("loc_14F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1575")

    #C0051
    ChrTalk(
        0x8,
        (
            "アルカンシェルの前を\x01",
            "パレードが通過したそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "お客さんもこぞって\x01",
            "流れてしまいました。\x01",
            "やれやれ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_1575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_15F1")

    #C0053
    ChrTalk(
        0x8,
        "今日は一段と賑やかですね。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "……調子に乗って\x01",
            "ルバーチェ商会の前に迷い込む\x01",
            "人がいなきゃいいんですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2573")

    label("loc_15F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1784")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_163E")

    #C0055
    ChrTalk(
        0x8,
        "警察の方も警戒で大変ですね。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "同情しますよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_177F")

    label("loc_163E")


    #C0057
    ChrTalk(
        0x8,
        "警察の方も警戒で大変ですね。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "時折一課の方が\x01",
            "私服で巡回しておられるのを\x01",
            "見かけますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "さすが捜査一課、\x01",
            "うまくカモフラージュしておいでだ。\x02",
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

    #C0060
    ChrTalk(
        0x102,
        "#0100Fよく分かりますね……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "慣れていると分かるものです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_177F")

    Jump("loc_2573")

    label("loc_1784")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17FB")

    #C0062
    ChrTalk(
        0x8,
        (
            "ウチは夜間営業ですから\x01",
            "自分の休憩時間を\x01",
            "削るしかありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        "やれやれ、面倒な話だ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1861")

    label("loc_17FB")


    #C0064
    ChrTalk(
        0x8,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "記念祭の間は日中も\x01",
            "店を開けているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "やれやれ、面倒だな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1861")

    Jump("loc_2573")

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1915")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1883")
    Call(0, 6)
    Jump("loc_1910")

    label("loc_1883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1894")
    Call(0, 6)
    Jump("loc_1910")

    label("loc_1894")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_190D")

    #C0067
    ChrTalk(
        0x8,
        (
            "サンドラさんなら\x01",
            "まだカウンター席で\x01",
            "うたた寝していますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "気になるのなら\x01",
            "話を聞いてみては？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1910")

    label("loc_190D")

    Call(0, 6)

    label("loc_1910")

    Jump("loc_2573")

    label("loc_1915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_19C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1932")
    Call(0, 21)
    Jump("loc_19BF")

    label("loc_1932")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1943")
    Call(0, 21)
    Jump("loc_19BF")

    label("loc_1943")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_19BC")

    #C0069
    ChrTalk(
        0x8,
        (
            "サンドラさんなら\x01",
            "まだカウンター席で\x01",
            "うたた寝していますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "気になるのなら\x01",
            "話を聞いてみては？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BF")

    label("loc_19BC")

    Call(0, 21)

    label("loc_19BF")

    Jump("loc_2573")

    label("loc_19C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1A73")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19E1")
    Call(0, 7)
    Jump("loc_1A6E")

    label("loc_19E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_19F2")
    Call(0, 7)
    Jump("loc_1A6E")

    label("loc_19F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1A6B")

    #C0071
    ChrTalk(
        0x8,
        (
            "サンドラさんなら\x01",
            "まだカウンター席で\x01",
            "うたた寝していますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "気になるのなら\x01",
            "話を聞いてみては？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A6E")

    label("loc_1A6B")

    Call(0, 7)

    label("loc_1A6E")

    Jump("loc_2573")

    label("loc_1A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1B38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1AD5")

    #C0073
    ChrTalk(
        0x8,
        "……お客さんですか？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "ただ今開店準備中です。\x01",
            "少々お待ちください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B33")

    label("loc_1AD5")


    #C0075
    ChrTalk(
        0x8,
        "……そろそろ営業時間ですね。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "カクテルの準備をして\x01",
            "ステージさんをお呼びしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B33")

    Jump("loc_2573")

    label("loc_1B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCE")

    #C0077
    ChrTalk(
        0x8,
        "近頃、物騒な噂を聞きますね。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "黒月側がルバーチェの密輸ルートを\x01",
            "潰し回っているとか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C26")

    #C0079
    ChrTalk(
        0x101,
        "#0000Fそれ、本当ですか……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C40")

    label("loc_1C26")


    #C0080
    ChrTalk(
        0x101,
        "#0000Fその話って……\x02",
    )

    CloseMessageWindow()

    label("loc_1C40")


    #C0081
    ChrTalk(
        0x8,
        "あくまで噂、ですが。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "市民の目には触れない所で\x01",
            "スマートに切り崩しているそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "お陰で遊撃士協会も\x01",
            "手が出せないとか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D58")

    label("loc_1CCE")


    #C0084
    ChrTalk(
        0x8,
        (
            "黒月側はかなりスマートな方法を\x01",
            "取っているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "詳しくは知りませんが、ルバーチェも\x01",
            "いくつか密輸ルートを失ったそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D58")

    Jump("loc_2573")

    label("loc_1D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DE6")

    #C0086
    ChrTalk(
        0x8,
        (
            "先月の件、ルバーチェにとっては\x01",
            "事件にも入らないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "あの人たちにとっては\x01",
            "時々ある出来事ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EC0")

    label("loc_1DE6")


    #C0088
    ChrTalk(
        0x8,
        (
            "先月の一件で\x01",
            "ルバーチェの事務所も\x01",
            "ゴタゴタしたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "一部の幹部が\x01",
            "叱りを受けたと聞きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "……まあ、ルバーチェは\x01",
            "この街に根を張る巨大組織です。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "この程度の出来事じゃ\x01",
            "びくともしませんよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1EC0")

    Jump("loc_2573")

    label("loc_1EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2033")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F6C")

    #C0092
    ChrTalk(
        0x8,
        (
            "東方系組織・黒月が\x01",
            "ミラ・ロンダリングに\x01",
            "着手したそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "ルバーチェが持つ\x01",
            "主要な商売の一つです。\x01",
            "連中も黙ってはいないでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202E")

    label("loc_1F6C")


    #C0094
    ChrTalk(
        0x8,
        (
            "東方系組織・黒月が\x01",
            "ミラ・ロンダリングに\x01",
            "着手したそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "黒月は近頃、ルバーチェの\x01",
            "シノギを奪い続けています。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "……この分では\x01",
            "両者が全面抗争に入るのも\x01",
            "時間の問題でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_202E")

    Jump("loc_2573")

    label("loc_2033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_214E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20BC")

    #C0097
    ChrTalk(
        0x8,
        (
            "お客さんの職柄はともかく\x01",
            "営業迷惑な真似はやめてほしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "店の品格を落とすような事は\x01",
            "したくありません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2149")

    label("loc_20BC")


    #C0099
    ChrTalk(
        0x8,
        (
            "うちの店前で客引きを\x01",
            "やっている人がいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        "やれやれ、迷惑な話だ……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "ウチは営業許可を取っている\x01",
            "真面目なバーなんですが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2149")

    Jump("loc_2573")

    label("loc_214E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_231E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21DA")

    #C0102
    ChrTalk(
        0x8,
        (
            "客に干渉しないのが\x01",
            "ウチのモットーなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "だからこそ情報も\x01",
            "入りやすいのでしょう。\x01",
            "……不本意な話ですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_21DA")


    #C0104
    ChrTalk(
        0x8,
        (
            "近頃、乱暴に飲んでは\x01",
            "愚痴っていくお客さんがいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "なんでも旧市街の事業に失敗したとか……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "ふう……そういった事は\x01",
            "大っぴらに喋らないで頂きたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#0005Fそれって……やっぱり\x01",
            "ルバーチェの人ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "お答えしかねますね。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "まあ、ウチは不本意ながら\x01",
            "そういう客も多いと言っておきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2319")

    Jump("loc_2573")

    label("loc_231E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23BF")

    #C0110
    ChrTalk(
        0x8,
        (
            "……ルバーチェ商会は\x01",
            "最近組織の強化に努めているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "ライバル組織に対抗している……\x01",
            "という噂ですが、詳しい事は知りません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247E")

    label("loc_23BF")


    #C0112
    ChrTalk(
        0x8,
        (
            "……ルバーチェ商会は\x01",
            "最近構成員の配置換えをしたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "武器や導力車の購入も\x01",
            "進めているそうですけど……\x01",
            "詳しい事は知りません。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "あくまでこの辺りで\x01",
            "囁かれている噂ですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_247E")

    Jump("loc_2573")

    label("loc_2483")


    #C0115
    ChrTalk(
        0x8,
        "何かご注文ですか？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        "#0200Fオレンジジュースください。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        "ジュースの類はありません。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x102,
        (
            "#0100Fティオちゃん、諦めたら？\x01",
            "ここ大人向けのお店みたいだから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2573")

    Jump("loc_85F")

    label("loc_2578")

    TalkEnd(0x8)
    Return()

    # Function_5_7FC end

    def Function_6_257C(): pass

    label("Function_6_257C")


    #C0119
    ChrTalk(
        0x8,
        (
            "……サンドラさんは\x01",
            "本当に一日中居座りますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "客に干渉しないのが\x01",
            "ウチのモットーなんですが\x01",
            "さすがに営業迷惑だな。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_6_257C end

    def Function_7_25FA(): pass

    label("Function_7_25FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2821")

    #C0121
    ChrTalk(
        0x8,
        "いらっしゃいませ。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "ウチは情報屋ではありません。\x01",
            "注文はカクテルのみでお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003Fえっと……\x01",
            "《銀》についての情報#4Rカクテル#を１つ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0124
    ChrTalk(
        0x8,
        (
            "黒月のツァオ・リーという人は\x01",
            "相当知恵が回るようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "その《知力》を駆使して相手を追い詰め、\x01",
            "また《武力》の方は謎の暗殺者を\x01",
            "雇っているそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "この２面攻撃に\x01",
            "さすがのガルシア・ロッシも\x01",
            "手を焼いているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "……お話できるのは\x01",
            "この辺りまでですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#0006F（た、試しに言ってみたら……）\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        "#0306F（知ってるんじゃねえかよ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 0)
    Jump("loc_28FF")

    label("loc_2821")


    #C0130
    ChrTalk(
        0x8,
        (
            "黒月のツァオ・リーという人は\x01",
            "相当知恵が回るようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "その知力を使って\x01",
            "敵を追い詰め、さらに別方面から\x01",
            "謎の暗殺者を使って切り崩す……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "まったく物騒な話です。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "……ところで、何か\x01",
            "注文していかれませんか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FF")

    Return()

    # Function_7_25FA end

    def Function_8_2900(): pass

    label("Function_8_2900")


    #C0134
    ChrTalk(
        0x8,
        "……何か御用ですか？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        "ウチはまだ開店していませんよ。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        (
            "#0100F夜間営業の\x01",
            "ジャズバーみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        "ええ、その通りです。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#0309Fこの店はウマイ酒を揃えててな。\x01",
            "結構穴場なんだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0003Fジャズバー《ガランテ》か……\x02\x03",

            "#0000F（そういや兄貴から\x01",
            "  聞いた事がある気がするけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0140
    ChrTalk(
        0x8,
        (
            "まあ、街を歩き疲れたお客さんに\x01",
            "何も出さないほど野暮じゃありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "カクテルくらいならどうぞ。\x01",
            "そちらのお嬢さんには出せませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        (
            "#0201Fむっ……\x01",
            "（わたしだけ\x01",
            "  仲間外れですか……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 0)
    Return()

    # Function_8_2900 end

    def Function_9_2B05(): pass

    label("Function_9_2B05")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B99")
    Jump("loc_2BE3")

    label("loc_2B99")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BB9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BE3")

    label("loc_2BB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BD9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BE3")

    label("loc_2BD9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BE3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2C16")
    Jump("loc_2C3E")

    label("loc_2C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2C3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C3E")
    Call(0, 27)
    Return()

    label("loc_2C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2CC5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x18)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5A")
    Call(0, 12)
    Jump("loc_2CC0")

    label("loc_2C5A")


    #C0143
    ChrTalk(
        0x9,
        "今日も客に酒を注ぐ毎日……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "はあ、この仕事が\x01",
            "空しくなってきたわ。\x01",
            "そろそろ足洗おうかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC0")

    Jump("loc_3856")

    label("loc_2CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2DBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2D15")

    #C0145
    ChrTalk(
        0x9,
        (
            "あー、ちょっと飲みすぎかも。\x01",
            "頭ガンガンするわ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBA")

    label("loc_2D15")


    #C0146
    ChrTalk(
        0x9,
        "あー、頭ガンガンする～……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "昨日も議員先生の接待だったのよ。\x01",
            "ったく粘りやがってぇ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "うちはお触り禁止なんだって\x01",
            "何度言ったら分かるんだっつーの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2DBA")

    Jump("loc_3856")

    label("loc_2DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2E23")
    OP_64(0x9)
    SetChrSubChip(0x9, 0x0)

    #C0149
    ChrTalk(
        0x9,
        (
            "むにゃむにゃ……\x01",
            "あの親父、べたべた触りやがってぇ～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_3856")

    label("loc_2E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2EE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E93")

    #C0150
    ChrTalk(
        0x9,
        "今日は帝国派議員の接待だっけ。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "はあ、年増のオヤジの顔なんて\x01",
            "見たくないのに～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EDF")

    label("loc_2E93")


    #C0152
    ChrTalk(
        0x9,
        (
            "エリックが\x01",
            "早く仕事に行けっていうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "ううっ、最近冷たいわ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2EDF")

    Jump("loc_3856")

    label("loc_2EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2FEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F60")

    #C0154
    ChrTalk(
        0x9,
        "最近派手な客がよく来るのよ。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "でも連中、気前はいいんだけど\x01",
            "態度でかくて相手しづらいのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE9")

    label("loc_2F60")


    #C0156
    ChrTalk(
        0x9,
        (
            "最近うちの店を\x01",
            "派手に利用する客が居るの。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "お札をばらまいてさ、\x01",
            "すんごい気前がいいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        "最近多いわよね、そういう奴～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2FE9")

    Jump("loc_3856")

    label("loc_2FEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_30A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_303E")

    #C0159
    ChrTalk(
        0x9,
        (
            "あたしももう年かしら。\x01",
            "まだ２０代なんだけどなぁ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A0")

    label("loc_303E")


    #C0160
    ChrTalk(
        0x9,
        "あうっ……朝日がまぶしいわ……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "ちくしょう、年々朝を迎えるのが\x01",
            "辛くなってくるわね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30A0")

    Jump("loc_3856")

    label("loc_30A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3142")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_30C2")
    Call(0, 10)
    Jump("loc_313D")

    label("loc_30C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_313A")
    SetChrSubChip(0x9, 0x0)
    OP_64(0x9)

    #C0162
    ChrTalk(
        0x9,
        (
            "うう……\x01",
            "う～ん……ムニャムニャ……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "寝かせてよう、エリックぅ～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_313D")

    label("loc_313A")

    Call(0, 10)

    label("loc_313D")

    Jump("loc_3856")

    label("loc_3142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_31DB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_315F")
    Call(0, 11)
    Jump("loc_31D6")

    label("loc_315F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_3170")
    Call(0, 11)
    Jump("loc_31D6")

    label("loc_3170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_31D3")
    SetChrSubChip(0x9, 0x0)

    #C0164
    ChrTalk(
        0x9,
        (
            "うう……\x01",
            "う～ん……ムニャムニャ……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        "寝かせてよう、エリックぅ～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_31D6")

    label("loc_31D3")

    Call(0, 11)

    label("loc_31D6")

    Jump("loc_3856")

    label("loc_31DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3271")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3218")

    #C0166
    ChrTalk(
        0x9,
        "客が美少年だったらいいのにねぇ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_326C")

    label("loc_3218")


    #C0167
    ChrTalk(
        0x9,
        "そろそろ出勤時間だわ。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "あー、やだやだ。\x01",
            "また親父どもの話相手だなんて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_326C")

    Jump("loc_3856")

    label("loc_3271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32E2")

    #C0169
    ChrTalk(
        0x9,
        (
            "あたしたちホステスは\x01",
            "今が睡眠時間なのよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "もういいじゃない、\x01",
            "寝かせてよぅ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333F")

    label("loc_32E2")


    #C0171
    ChrTalk(
        0x9,
        (
            "あたしの知ってることは\x01",
            "全部話したわよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "もういいじゃない、\x01",
            "寝かせてよぅ～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_333F")

    Jump("loc_3856")

    label("loc_3344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_34A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33EE")

    #C0173
    ChrTalk(
        0x9,
        (
            "にしてもエリックは\x01",
            "いっつも平然としてるわよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "ルバーチェのお兄さんにも\x01",
            "平然とお酒持って行くんだもの。\x01",
            "……本気で惚れちゃいそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A3")

    label("loc_33EE")


    #C0175
    ChrTalk(
        0x9,
        (
            "昨日もルバーチェのお兄さんが\x01",
            "飲みに来てたんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "何だかイラついた様子で\x01",
            "しきりと愚痴ってたわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "警察のガキども……\x01",
            "とか言ってたけど、\x01",
            "何か揉めてるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_34A3")

    Jump("loc_3856")

    label("loc_34A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_357A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34F4")

    #C0178
    ChrTalk(
        0x9,
        (
            "最近共和国派の先生達、\x01",
            "随分羽振りがいいわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3575")

    label("loc_34F4")


    #C0179
    ChrTalk(
        0x9,
        (
            "昨晩は共和国派の\x01",
            "議員先生の接待に呼ばれたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "羽振りはよかったけど疲れたわ～。\x01",
            "エリックの横顔を見て癒されましょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3575")

    Jump("loc_3856")

    label("loc_357A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_364E")

    #C0181
    ChrTalk(
        0x9,
        (
            "最近、歓楽街で\x01",
            "ステキな少年を見かけるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "涼しげだけど神秘的で……\x01",
            "中性的なカンジが堪らないの㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "でもいつも金持ちマダムと\x01",
            "一緒で近寄れないのよね～。\x01",
            "あの子、やっぱりホストなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3856")

    label("loc_364E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_36E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3690")

    #C0184
    ChrTalk(
        0x9,
        (
            "最近仕事が辛いのよ。\x01",
            "もう年かしら～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DC")

    label("loc_3690")


    #C0185
    ChrTalk(
        0x9,
        "あれ、もう朝……？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "ううん、寝かせて……\x01",
            "もっと寝かせてよぅ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_36DC")

    Jump("loc_3856")

    label("loc_36E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_37EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3745")

    #C0187
    ChrTalk(
        0x9,
        (
            "エリックって美形よね。\x01",
            "おまけにクールだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "んーん、癒されるわ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37E9")

    label("loc_3745")


    #C0189
    ChrTalk(
        0x9,
        (
            "このバー、ルバーチェの連中も\x01",
            "時々飲みに来てるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "そこの無愛想なバーテンダーさんは\x01",
            "それで情報通ってわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "んーん、クールな\x01",
            "美貌に癒されるわ～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_37E9")

    Jump("loc_3856")

    label("loc_37EE")

    SetChrSubChip(0x9, 0x0)

    #C0192
    ChrTalk(
        0x9,
        (
            "あのクソ親父、\x01",
            "べたべた触ってきやがって～！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "はあ、疲れた……\x01",
            "ホステスも楽じゃないわ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3856")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_2B05 end

    def Function_10_385E(): pass

    label("Function_10_385E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_38BB")

    #C0194
    ChrTalk(
        0x9,
        "ううっ、エリックが冷たいの……\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x9,
        (
            "あたしは悪酔いなんて\x01",
            "してないわよう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C1")

    label("loc_38BB")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x2)

    #C0196
    ChrTalk(
        0x9,
        (
            "ねェん、エリック～。\x01",
            "お酒ちょうだいよぅ～……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0197
    ChrTalk(
        0x8,
        (
            "#3Pサンドラさん、\x01",
            "そろそろ帰ったらどうですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        "#3Pもう昼過ぎですよ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_39B3")

    #C0199
    ChrTalk(
        0x101,
        "#0000F（まだ飲んでいる……）\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x103,
        (
            "#0200F（この方も何かを\x01",
            "  失くさないか、心配です。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39B3")

    SetScenarioFlags(0x0, 1)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)

    label("loc_39C1")

    Return()

    # Function_10_385E end

    def Function_11_39C2(): pass

    label("Function_11_39C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3A01")

    #C0201
    ChrTalk(
        0x9,
        (
            "記念祭なんて\x01",
            "こなきゃいいのよ、ぐびぐび……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B6D")

    label("loc_3A01")


    #C0202
    ChrTalk(
        0x9,
        (
            "もうすぐ記念祭だ～って、\x01",
            "みんな楽しみにしてるんでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "……ムカツク～……\x01",
            "ホステスは記念祭、大変なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "朝から晩まで客に酒ついでさ、\x01",
            "相槌うってニコニコして……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "あ゛ー、考えるだけで気が滅入る～……\x01",
            "まったくやってられないわ、ぐびぐび……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3B6A")

    #C0206
    ChrTalk(
        0x101,
        "#0000F（まだ飲んでいる……）\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#0200F（この方も何かを\x01",
            "  失くさないか、心配です。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B6A")

    SetScenarioFlags(0x0, 1)

    label("loc_3B6D")

    Return()

    # Function_11_39C2 end

    def Function_12_3B6E(): pass

    label("Function_12_3B6E")


    #C0208
    ChrTalk(
        0xFE,
        (
            "ううっ、もう夕方……？\x01",
            "そろそろ仕事に行かなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "……ふう……あなたたちに\x01",
            "今日はイイコト教えてあげるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "以前、客に教えてもらった\x01",
            "カクテルの作り方よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "こんな甘いカクテル、\x01",
            "また飲んでみたいわぁ……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを教えてもらった。\x02",
        )
    )

    CloseMessageWindow()

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x18)
    Return()

    # Function_12_3B6E end

    def Function_13_3CC2(): pass

    label("Function_13_3CC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DD5")

    #C0214
    ChrTalk(
        0x101,
        (
            "#0000Fダ、ダドリー捜査官。\x01",
            "お久しぶりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "#0601F………………………………\x02\x03",

            "#0603F……問題児どもか。\x01",
            "我々の捜査の邪魔をするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#0306F（取り付く島も\x01",
            "  ねえって感じだなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#0108F（競売会の一件で色々と\x01",
            "  迷惑をかけたみたいね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3E39")

    label("loc_3DD5")


    #C0218
    ChrTalk(
        0xFE,
        (
            "#0603F……お前たちの\x01",
            "やらかした事はもういい。\x02\x03",

            "#0601F今後は余計な\x01",
            "スタンドプレーは慎んでおけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E39")

    TalkEnd(0xFE)
    Return()

    # Function_13_3CC2 end

    def Function_14_3E3D(): pass

    label("Function_14_3E3D")

    TalkBegin(0xFE)

    #C0219
    ChrTalk(
        0xFE,
        (
            "我々捜査一課は\x01",
            "現在重要な案件を調査中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "……特務支援課の\x01",
            "出る幕ではありませんよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_3E3D end

    def Function_15_3EA4(): pass

    label("Function_15_3EA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3F0F")

    #C0221
    ChrTalk(
        0xFE,
        (
            "この店はルバーチェの構成員が\x01",
            "御用達にしているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "よし、一丁聞き込みといくか！\x02",
    )

    CloseMessageWindow()

    label("loc_3F0F")

    TalkEnd(0xFE)
    Return()

    # Function_15_3EA4 end

    def Function_16_3F13(): pass

    label("Function_16_3F13")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3F44")

    #C0223
    ChrTalk(
        0xFE,
        (
            "ううむ……\x01",
            "こういう店は苦手だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F44")

    TalkEnd(0xFE)
    Return()

    # Function_16_3F13 end

    def Function_17_3F48(): pass

    label("Function_17_3F48")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FDC")
    Jump("loc_4026")

    label("loc_3FDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FFC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4026")

    label("loc_3FFC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_401C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4026")

    label("loc_401C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4026")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_40EC")

    #C0224
    ChrTalk(
        0xC,
        (
            "ふぅ……今日は\x01",
            "カジノにでも繰り出すとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "フフ、勝っても負けても\x01",
            "一度きりの勝負。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "記念祭の締めくくりに\x01",
            "相応しい楽しみ方だろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CB")

    label("loc_40EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_415A")

    #C0227
    ChrTalk(
        0xC,
        (
            "クロスベル自治州が\x01",
            "生まれて７０年……か。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "フフ、酒でも飲みながら\x01",
            "楽しもうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42CB")

    label("loc_415A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_41D0")

    #C0229
    ChrTalk(
        0xC,
        (
            "マクダエル市長はつい先月、\x01",
            "危険な目に遭ったそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        "フフ、お元気そうで何よりだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_426D")

    label("loc_41D0")


    #C0231
    ChrTalk(
        0xC,
        (
            "今年は記念祭に併せて\x01",
            "国際シンポジウムとやらも\x01",
            "開かれるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "元々はマクダエル市長の\x01",
            "発案だとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        (
            "フフ、ご高齢ながら\x01",
            "精力的なお方だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_426D")

    Jump("loc_42CB")

    label("loc_4272")


    #C0234
    ChrTalk(
        0xC,
        "ふうむ、中々美味い酒だな。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        (
            "バーテンダーが無愛想だが\x01",
            "店の雰囲気は気に入ったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42CB")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_3F48 end

    def Function_18_42D3(): pass

    label("Function_18_42D3")

    TalkBegin(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        "さて……まずは一杯飲むとするか。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "むふふ、夜は長いんじゃからのう。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_42D3 end

    def Function_19_4326(): pass

    label("Function_19_4326")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43BA")
    Jump("loc_4404")

    label("loc_43BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4404")

    label("loc_43DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43FA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4404")

    label("loc_43FA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4404")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AC")

    #C0238
    ChrTalk(
        0xFE,
        "ぐびぐび……ぷは～！\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "しかし向こうの社長さん、\x01",
            "おっそいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        "せっかく接待してやろうってのによ～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_44FF")

    label("loc_44AC")


    #C0241
    ChrTalk(
        0xFE,
        "今日は貿易会社の社長さんに……と。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "ん、何だ君ら。\x01",
            "邪魔はしないでくれよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44FF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_4326 end

    def Function_20_4507(): pass

    label("Function_20_4507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_451D")
    Call(0, 29)
    Jump("loc_4AB0")

    label("loc_451D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4AA7")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_45BA")
    Jump("loc_4604")

    label("loc_45BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45DA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4604")

    label("loc_45DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45FA")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4604")

    label("loc_45FA")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4604")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_496C")
    SetChrSubChip(0xFE, 0x0)

    #C0243
    ChrTalk(
        0x11,
        (
            "#2106F………………………………\x02\x03",

            "……記念祭の最終日、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#0005Fグレイスさん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4744")
    Jump("loc_478E")

    label("loc_4744")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4764")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_478E")

    label("loc_4764")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4784")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_478E")

    label("loc_4784")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_478E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0245
    ChrTalk(
        0x11,
        (
            "#2105Fあ……ロイド君たちか。\x02\x03",

            "#2102Fビックリした……\x01",
            "あんまり驚かせないでよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#0002Fはは、すみません。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#0105Fグレイスさんも\x01",
            "最終日はお休みですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x11,
        (
            "#2109Fまさか～。\x01",
            "ちょっと休憩してただけよ。\x02\x03",

            "#2100Fこの後、夕方には\x01",
            "閉会式だってあるんだし。\x02\x03",

            "#2104F……ホントは別のところに\x01",
            "取材に行きたいんだけどね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#0013F別のところ……\x01",
            "（……もしかして……）\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        (
            "#0108F（多分、競売会の存在を\x01",
            "  知っているのでしょうね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 4)
    Jump("loc_4A9B")

    label("loc_496C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A10")

    #C0251
    ChrTalk(
        0x11,
        (
            "#2100Fあ、そうそう。\x01",
            "写真の方は十分撮れたら\x01",
            "通信社の受付に渡しちゃって。\x02\x03",

            "#2109F締め切りは今日までだから\x01",
            "よろしくお願いね～♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_4A9B")

    label("loc_4A10")


    #C0252
    ChrTalk(
        0x11,
        (
            "#2104Fふふ、それにしても\x01",
            "ちょっとビックリしたなぁ。\x02\x03",

            "#2100F……口調は全然違うけど\x01",
            "声の感じが似てるっていうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#0005F？？？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4A9B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4AB0")

    label("loc_4AA7")

    TalkBegin(0xFE)
    Call(0, 21)
    TalkEnd(0xFE)

    label("loc_4AB0")

    Return()

    # Function_20_4507 end

    def Function_21_4AB1(): pass

    label("Function_21_4AB1")

    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_4B32")

    #C0254
    ChrTalk(
        0x11,
        (
            "#2100Fでも、あのお店って\x01",
            "メチャメチャ高いんでしょ？\x02\x03",

            "そんなミラ回りがいいわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        "さて、そこまでは……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D77")

    label("loc_4B32")


    #C0256
    ChrTalk(
        0x11,
        (
            "#2105Fへ～、そうなんだ。\x02\x03",

            "#2109Fそれでそれで？\x01",
            "その接待に使ったお店って？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "どうやら、最近話題の\x01",
            "あの店のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "半年ほど前に\x01",
            "帝都から進出したという……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x11,
        (
            "#2105Fええ～っ！？\x01",
            "《ノイエ・ブラン》のこと！？\x02\x03",

            "会員制の超高級クラブで\x01",
            "ホステスさんも一流揃いっていう！\x02\x03",

            "#2109Fいいな～！\x01",
            "あたしも接待されたーい！\x02",
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

    #C0260
    ChrTalk(
        0x101,
        "#0000F（どうやら取材中みたいだな……）\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#0306F（しかしこのハシャギっぷり……\x01",
            "  演技なんだか本気なんだか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        "#0200F（恐らく両方でないかと。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4D77")

    OP_4C(0x8, 0xFF)
    Return()

    # Function_21_4AB1 end

    def Function_22_4D7C(): pass

    label("Function_22_4D7C")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E0A")
    OP_29(0x46, 0x1, 0x4)

    #C0263
    ChrTalk(
        0x101,
        (
            "#0003F（よし、裏通りの聞き込みは\x01",
            "  これで十分だな。）\x02\x03",

            "#0001F（次は中央広場で\x01",
            "  聞き込みをしてみよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)

    label("loc_4E0A")

    Return()

    # Function_22_4D7C end

    def Function_23_4E0B(): pass

    label("Function_23_4E0B")

    TalkBegin(0xFF)

    #C0264
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#0003Fここには痕跡なし……か。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_23_4E0B end

    def Function_24_4E60(): pass

    label("Function_24_4E60")

    TalkBegin(0xFF)

    #C0266
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x103,
        (
            "#0200Fこの辺りの席には\x01",
            "座ってないようですね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_24_4E60 end

    def Function_25_4EC4(): pass

    label("Function_25_4EC4")

    TalkBegin(0xFF)

    #C0268
    ChrTalk(
        0x11C,
        (
            "#1200Fフンフン………\x02\x03",

            "……ウォン！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x101,
        "#0005F匂いが残ってるのか……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#0200Fどうやらこの席で\x01",
            "飲んでいたようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x7)
    TalkEnd(0xFF)
    Return()

    # Function_25_4EC4 end

    def Function_26_4F75(): pass

    label("Function_26_4F75")

    EventBegin(0x0)
    Fade(500)
    OP_68(-120, 1430, 4230, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -1070, 0, 4440, 45)
    SetChrPos(0x103, -470, 0, 2890, 359)
    SetChrPos(0x11C, -1680, 0, 2890, 45)
    TurnDirection(0x8, 0x101, 0)
    OP_0D()

    #C0271
    ChrTalk(
        0x8,
        (
            "#11Pいらっしゃいませ。\x01",
            "何かご用ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#6P#0001Fつかぬことをお伺いしますが\x01",
            "……昨晩ウチの副局長を\x01",
            "見かけませんでしたか？\x02\x03",

            "#0003Fええと、やや小柄で\x01",
            "キツネ顔の……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x8,
        "#11Pピエール副局長ですか？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#11P確かに昨晩はお越しになりました。\x01",
            "ひどいグデングデンの\x01",
            "酔いようでしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#6P#0203F副局長は結婚指輪を\x01",
            "失くされたそうなのですが。\x02\x03",

            "#0200F店の方で心当たりなどは？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        "#11P全くありません。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそ、そ、そうですか……\x01",
            "（随分ハッキリ否定されたな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#11Pですが……そういえば。\x01",
            "奥様のことを激しく\x01",
            "愚痴っておられましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        "#11Pもう別れてやるーとか仰って。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "#11Pその上でホステスの方に\x01",
            "しきりとアプローチ\x01",
            "なさっていたようです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        "#6P#0006Fまさかそんな話を聞くとは……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        "#6P#0203F聞きたくなかったです。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "#11Pそのホステス──サンドラさんは\x01",
            "まだカウンター席にいらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#11P気になるのなら\x01",
            "話を聞いてみては？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそうですね……\x02\x03",

            "#0003F（そのときまだ\x01",
            "  結婚指輪をしていたか……\x01",
            "  それだけは確認しておこう。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -1070, 0, 4440, 45)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0x15, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_26_4F75 end

    def Function_27_5409(): pass

    label("Function_27_5409")

    EventBegin(0x0)
    Fade(500)
    OP_68(-5160, 1430, 3850, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21270, 0)
    SetChrPos(0x101, -5730, 0, 4480, 90)
    SetChrPos(0x103, -5700, 0, 3490, 45)
    SetChrPos(0x11C, -6960, 0, 2880, 45)
    SetChrSubChip(0x9, 0x0)
    OP_0D()

    #C0286
    ChrTalk(
        0x101,
        (
            "#5P#0000Fあの、スミマセン。\x01",
            "クロスベル警察の者ですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0287
    ChrTalk(
        0x9,
        "#12Pううん……ムニャムニャ……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x9,
        "#12P寝かせてよう、エリックぅ～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(300)

    #C0289
    ChrTalk(
        0x103,
        "#5P#0200F寝てますね。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#5P#0006F仕方がない……\x02",
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    SetChrName("")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは女性の肩を揺り動かした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0292
    ChrTalk(
        0x101,
        (
            "#5P#0001Fスミマセン、\x01",
            "クロスベル警察の者ですが！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    SetChrSubChip(0x9, 0x1)
    Sleep(500)

    #C0293
    ChrTalk(
        0x9,
        (
            "#12Pん……\x01",
            "なによう、もう……！\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#5P#0003F申し訳ありませんが\x01",
            "お伺いしたい事が。\x02\x03",

            "#0001F昨晩はウチの副局長と\x01",
            "ご一緒だったとか……\x02\x03",

            "その時に副局長が指輪をしていたか、\x01",
            "覚えてないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#12Pフクキョクチョウ？\x01",
            "あー、あの言い寄ってきた男ね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x9,
        (
            "#12Pヒック……アタシは\x01",
            "若い男がタイプだって言ってるのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        (
            "#12P君はウツクシイとか\x01",
            "口走っちゃってさぁ、オヤジがぁ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#0006Fだめだ、この人も\x01",
            "相当酔っ払っている……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#5P#0200Fこの様子だと一晩飲み明かした\x01",
            "続き……みたいですね。\x01",
            "アルコール臭すぎです。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#12Pだってぇ、あの男が\x01",
            "お酒奢ってくれるって言うんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x9,
        (
            "#12Pその上でアタシの手を\x01",
            "握っちゃったりしてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "#12P奥さんとは別れるから\x01",
            "一緒になろうとかなんとかぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#5P#0003F（これ以上は……\x01",
            "  さすがに聞くに堪えない……\x01",
            "  やっぱり一度引き上げようか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#5P#0200F（ええ、話も\x01",
            "  長くなりそうですし……）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x9,
        "#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x9,
        (
            "#12Pそういえば、あのとき\x01",
            "なんか貰った気がするわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0307
    ChrTalk(
        0x101,
        "#5P#0005F何かを貰った……？\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        "#12Pあ、確かこれだわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x1)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0309
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#800M紅耀石の結婚指輪\x07\x00",
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0310
    ChrTalk(
        0x9,
        (
            "#12P『これは君への贈り物だ！』\x01",
            "とか言ってくれたんだけど\x01",
            "ゼンゼンタイプじゃないし～。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        "#12P持って行っちゃっていいわよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x103)

    #C0312
    ChrTalk(
        0x103,
        (
            "#5P#0200F………結婚指輪#8Rウェディングリング#………\x01",
            "見つけてしまいました……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#5P#0011F副局長……\x01",
            "落としたんじゃないじゃないか！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x9,
        "#12Pえっと、何かあったのぉ？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11C,
        (
            "#5P#1203Fグルルルルル……\x01",
            "（フン、つまらぬ幕引きだな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 2)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_27_5409 end

    def Function_28_5C51(): pass

    label("Function_28_5C51")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02502.itc", 0x1E)
    LoadChrToIndex("chr/ch08602.itc", 0x1F)
    LoadChrToIndex("apl/ch50091.itc", 0x20)
    SetChrPos(0x0, -5780, 0, 1780, 142)
    SetChrPos(0x1, -5780, 0, 1780, 142)
    SetChrPos(0x2, -5780, 0, 1780, 142)
    SetChrPos(0x3, -5780, 0, 1780, 142)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x16)
    SetChrPos(0x16, -5800, 0, 4250, 0)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, -5800, 80, 4450, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, -6900, 80, 4450, 0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x4)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5800, 500, 5300, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -3800, 0, 6400, 180)
    FadeToBright(2000, 0)
    OP_68(-13480, 1830, 5770, 0)
    MoveCamera(315, 16, 0, 0)
    OP_6E(410, 0)
    SetCameraDistance(25500, 0)
    OP_68(-6040, 1430, 4480, 10000)
    MoveCamera(297, 16, 0, 10000)
    OP_6E(310, 10000)
    SetCameraDistance(25500, 10000)
    Sleep(9000)
    SetChrSubChip(0x13, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5E, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_5C51 end

    def Function_29_5E18(): pass

    label("Function_29_5E18")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-8000, 1200, 500, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -8000, 0, 1400, 180)
    SetChrPos(0x102, -6800, 0, 1500, 225)
    SetChrPos(0x103, -8400, 0, 2800, 180)
    SetChrPos(0x104, -9500, 0, 2100, 135)
    SetChrPos(0x11, -8400, 100, -500, 90)
    SetChrSubChip(0x11, 0x1)
    OP_0D()

    #C0316
    ChrTalk(
        0x11,
        (
            "#6P#2102Fおっ、来たわね。\x02\x03",

            "#2109F早速だけど、黒月襲撃について\x01",
            "知ってる事を喋ってもらおうかしら？\x02\x03",

            "事務所でツァオ氏から\x01",
            "色々と話を聞いたんでしょ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0317
    ChrTalk(
        0x101,
        "#0006F#11Pいきなりですね……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#11P#0211Fというか、何故わたし達が黒月を\x01",
            "訪ねた事を知っているのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#6P#2106Fいや～、朝一番で話を聞いて\x01",
            "ツァオ氏に取材を申し込もうとしたら\x01",
            "ダドリーのヤツが現れちゃってさぁ。\x02\x03",

            "#2105Fどうしたもんかと様子を伺ってると\x01",
            "君たちが後から入っていくじゃないの。\x02\x03",

            "#2100Fそしたらダドリーたちが\x01",
            "苦虫を噛み潰したような顔で出てきて\x01",
            "その後、君たちも思案顔で出てきたわけ。\x02\x03",

            "#2109Fこりゃあ色々聞いたと\x01",
            "思わない方がおかしいでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#0001F#11Pなるほど……\x01",
            "そういう事でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#12P#0101Fどちらにしても、捜査上の情報を\x01",
            "簡単に漏らすわけにはいかないのは\x01",
            "ご存知かとは思いますが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "#6P#2109Fもちろん判ってるってば～。\x01",
            "だからギブ・アンド・テイクじゃない。\x02\x03",

            "#2102Fガルシア氏についての情報、\x01",
            "知りたくないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#0005F#11Pそれは……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        (
            "#5P#0306F相変わらず、美味しいエサを\x01",
            "ちらつかせてくるのが上手いよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x11,
        (
            "#6P#2100F例の《競売会》の顛末も\x01",
            "色々と聞いてるわよ～？\x02\x03",

            "#2104Fルバーチェがヘマをやらかして\x01",
            "議長のご不興を買ったらしいけど……\x02\x03",

            "#2102Fそのあたりの状況と合わせて\x01",
            "色々と知りたくな～い？\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#0006F#11Pはぁ、判りました。\x02\x03",

            "#0013Fただし、ツァオ氏の話は全て\x01",
            "仄#2Rほの#めかされた非公式のものです。\x02\x03",

            "そのあたりは了解してください。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xBB8)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50091.itc", 0x22)
    LoadChrToIndex("apl/ch50011.itc", 0x23)
    SoundLoad(806)
    OP_68(-7510, 800, -380, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(18450, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -7000, 100, -2050, 0)
    SetChrPos(0x102, -5800, 100, -2050, 0)
    SetChrPos(0x103, -4600, 100, -2050, 0)
    SetChrPos(0x104, -3100, 100, -500, 270)
    SetChrPos(0x11, -8400, 100, -500, 90)
    SetChrSubChip(0x11, 0x2)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x5)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -7200, 300, -500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    SetCameraDistance(19450, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0327
    ChrTalk(
        0x11,
        (
            "#5P#2101F……なるほどね。\x02\x03",

            "#2106Fうーん、思っていた以上に\x01",
            "ヤバイ状況になってるわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#0003Fええ……そうなんです。\x02\x03",

            "#0001F今の所はどちらも\x01",
            "一般市民を巻き込まない配慮は\x01",
            "しているみたいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x11,
        (
            "#5P#2101Fいやあ、それにしたって\x01",
            "今回の事件は唐突すぎるわよ。\x02\x03",

            "いくら真夜中とはいえ、\x01",
            "通信社#6Rウ　チ#の近くでの襲撃よ？\x02\x03",

            "#2106Fしかも近隣には天下のＩＢＣ……\x01",
            "さすがに思い切りが良すぎだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#6P#0106Fええ、そうですね……\x02\x03",

            "#0101F下手をすればクロスベルの\x01",
            "金融・貿易センターとしての信頼も\x01",
            "揺るがしかねない出来事だと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x11,
        (
            "#5P#2100Fそこなのよね、ポイントは。\x02\x03",

            "#2103Fうーん、こりゃあたしが掴んだ情報も\x01",
            "あながち嘘じゃないかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#6P#0205Fグレイスさんが掴んだ情報……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        "#6P#0001F……話してもらえますか？\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x11,
        (
            "#5P#2100Fオーケー。\x01",
            "今度はこっちのターンね。\x02\x03",

            "#2103F実はね……\x01",
            "マフィアの内部事情なんだけど。\x02\x03",

            "#2101F最近、若頭のガルシア氏の統制が\x01",
            "行き届かなくなっているって噂が\x01",
            "あるみたいなのよね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    Sleep(1000)

    #C0335
    ChrTalk(
        0x101,
        "#6P#0005Fそれは……本当ですか？\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        (
            "#12P#0306Fちょいと信じられねぇな……\x02\x03",

            "#0301Fあの化物みたいなオッサンに\x01",
            "部下どもが逆らえるとは思えねぇが。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x11,
        (
            "#5P#2106Fまあ、そうなんだけどね。\x02\x03",

            "#2101Fただ旧市街の一件についても、\x01",
            "鉱山町の利権を狙おうとしたのも\x01",
            "ガルシア氏の指示じゃないらしいの。\x02\x03",

            "手柄を立てようとした下っ端が\x01",
            "独断でした結果らしいんだけど……\x02\x03",

            "そうした若手ならではの暴走が\x01",
            "目立ってきているらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        "#12P#0301Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#6P#0105Fちょ、ちょっと待ってください。\x02\x03",

            "#0101Fそれでは昨夜の襲撃も\x01",
            "若手の勝手な暴走だと……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x11,
        (
            "#5P#2106Fまあ、さすがに事が大きすぎるし、\x01",
            "それは無いとは思うんだけどね……\x02\x03",

            "#2100Fただ、そういう事情を踏まえると、\x01",
            "ガルシア氏のさっきの態度は\x01",
            "何となく理解できるんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#12P#0308F確かに……\x01",
            "取り巻きもいなかったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#6P#0003Fルバーチェ内を統制するのに\x01",
            "苦労しているという事か……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#6P#0200Fでも、例の会長さんの方は\x01",
            "いったい何をしているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x11,
        (
            "#5P#2106F聞いた話によると\x01",
            "《競売会》での失態を取り戻そうと\x01",
            "必死になっているみたいね。\x02\x03",

            "#2101F機嫌を損ねたハルトマン議長への\x01",
            "ご機嫌取りはもちろんだけど……\x02\x03",

            "新たに自治州内の有力者を\x01",
            "取り込もうとしているらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        (
            "#6P#0101F新たな有力者……\x01",
            "どのあたりなんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x11,
        (
            "#5P#2103F端的に言うと共和国派議員ね。\x02\x03",

            "#2101Fそれに警備隊司令あたりとも\x01",
            "何度か会合をしているって噂よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#6P#0103Fなるほど……\x01",
            "《黒月》の政治的な影響を\x01",
            "抑えるのが目的でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#6P#0008F警備隊の司令を取り込んだのは\x01",
            "武器の密輸を強化するためか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        (
            "#12P#0306Fま、そんな所だろうな。\x02\x03",

            "#0301Fあと、あの阿呆司令は\x01",
            "ハルトマン議長の腰巾着って話だ。\x02\x03",

            "そっちに働きかけることで\x01",
            "間接的に議長のご機嫌取りも\x01",
            "しようとしてんのかもしれねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        (
            "#5P#2104Fええ、あたしもそう睨んでるわ。\x02\x03",

            "#2102Fいや～、やっぱ君たちと話してると\x01",
            "考えがまとまるわねぇ！\x02\x03",

            "#2109Fうんうん！\x01",
            "情報交換した甲斐があったわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#6P#0002Fはは……\x01",
            "正直こちらも助かりました。\x02\x03",

            "#0006Fでも、こうして整理してみると\x01",
            "やっぱり違和感を感じますね……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x102,
        "#6P#0105F違和感？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x11,
        "#5P#2105F……どういうこと？\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        (
            "#6P#0003F一つ一つの行動については\x01",
            "納得いく理由があるようですが……\x02\x03",

            "どれも場当たり的だし、組織として\x01",
            "全く連携が取れていない気がします。\x02\x03",

            "#0008F俺がルバーチェに感じていたのは\x01",
            "悪い意味での、大都市ならではの\x01",
            "“スマートさ”だったんですが……\x02\x03",

            "#0001Fそれが殆んど感じられないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        "#6P#0101Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x11,
        (
            "#5P#2101Fふむ……\x01",
            "言われてみればそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#6P#0203Fクロスベルという金#2Rミラ#の成る木から\x01",
            "甘い汁を吸うためのシステム……\x02\x03",

            "#0201Fそれを確立した組織にしては\x01",
            "確かに場当たり的かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        (
            "#12P#0308F何か、そのあたりを狂わせるような\x01",
            "俺たちの知らない“要素”がある……\x02\x03",

            "#0301Fそういう事かよ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(150)

    #C0359
    ChrTalk(
        0x101,
        (
            "#5P#0000Fああ……あくまでカンだけどね。\x02\x03",

            "#0003F《黒月》を襲った襲撃者の戦闘力も\x01",
            "不自然に高かったみたいだし……\x02\x03",

            "#0001Fガルシアの奇妙な態度にしても\x01",
            "それが原因じゃないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x11,
        (
            "#5P#2102Fうーん、さすがはロイド君。\x01",
            "鋭い読みをしてくれるじゃない。\x02\x03",

            "#2109Fね、警察をクビになったら\x01",
            "クロスベルタイムズに入らない？\x02\x03",

            "そんであたしと一緒に\x01",
            "フューリッツァ賞を狙いましょ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0361
    ChrTalk(
        0x101,
        (
            "#6P#0006Fいや、遠慮しときます……\x02\x03",

            "#0013Fていうか縁起でもないこと\x01",
            "言わないでくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        (
            "#12P#0305Fところでその\x01",
            "フューリッツァ賞ってのは\x01",
            "何なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#6P#0100F確かその年で最も優秀な\x01",
            "ジャーナリストに贈られる\x01",
            "国際的な賞だったはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)

    #C0364
    ChrTalk(
        0x101,
        (
            "#6P#0001F──すみません。\x01",
            "ちょっと失礼します。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0xB)
    OP_24(0x326)
    Sound(804, 0, 100, 0)
    Sound(807, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0365
    AnonymousTalk(
        0x101,
        (
            "#0001Fはい、特務支援課、\x01",
            "ロイド・バニングスですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("老人の声")

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すまない、私だ！\x01",
            "マインツのビクセンだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0367
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0000Fああ、町長さんでしたか。\x02\x03",

            "どうかされましたか？\x01",
            "ガンツさんの事で問題でも？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そ、それが……\x01",
            "今クロスベルのカジノハウスに\x01",
            "来ているんだが……\x02\x03",

            "ど、どうも様子がおかしくなって\x01",
            "それで連絡を……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0369
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F様子がおかしい……？\x02\x03",

            "#0001F一体、どうおかしいんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "さっきからガンツが他の客と\x01",
            "ポーカーをしているんだが……\x02\x03",

            "妙に暴力的というか\x01",
            "物騒な雰囲気になってきて……\x02\x03",

            "すまない、とにかく様子を\x01",
            "見に来てもらえないだろうか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0371
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011Fりょ、了解しました。\x02\x03",

            "#0001Fカジノハウスですね？\x01",
            "近くにいるのですぐに行きます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("町長の声")

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、よろしく頼むよ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    Sound(825, 0, 100, 0)
    Sleep(300)

    #C0373
    ChrTalk(
        0x102,
        "#6P#0101Fマインツの町長さん？\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        (
            "#12P#0305Fカジノがどうとか\x01",
            "言ってたみてぇだが？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0375
    ChrTalk(
        0x101,
        (
            "#5P#0013Fああ、例のガンツさんが\x01",
            "客同士の勝負で暴力的な事に\x01",
            "巻き込まれそうな感じらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        "#6P#0105Fええっ……？\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        (
            "#6P#0201F相手の逆恨みでも\x01",
            "買ったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#12P#0306Fあの態度でバカヅキなら\x01",
            "いかにもありそうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x11,
        (
            "#5P#2103Fふむ、それは急いで\x01",
            "様子を見に行かないとね。\x02\x03",

            "#2110Fそれじゃあ\x01",
            "カジノにレッツ・ゴー！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0380
    ChrTalk(
        0x11,
        "#5P#2105Fあれれ、どしたの？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x102,
        "#6P#0109Fいえ、その……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0382
    ChrTalk(
        0x101,
        (
            "#5P#0006F……言っても無駄だろうから\x01",
            "気にせずに行こう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    AddParty(0x3C, 0xFF, 0xFF)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_68(-8000, 1430, 1200, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -8000, 0, 1200, 0)
    SetChrPos(0x1, -8000, 0, 1200, 0)
    SetChrPos(0x2, -8000, 0, 1200, 0)
    SetChrPos(0x3, -8000, 0, 1200, 0)
    SetChrPos(0x4, -8000, 0, 1200, 0)
    SetScenarioFlags(0xC2, 6)
    OP_C7(0x0, 0x1000)
    OP_29(0x4A, 0x1, 0x8)
    OP_29(0x4B, 0x1, 0x4)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_29_5E18 end

    SaveToFile()

Try(main)
