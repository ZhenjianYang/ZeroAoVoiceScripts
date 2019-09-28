from ZeroScenarioHelper import *

def main():
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
        "埃里克",                 # 1
        "桑多拉",                 # 2
        "达德利搜查官",           # 3
        "艾玛搜查官",             # 4
        "客人",                   # 5
        "客人",                   # 6
        "客人",                   # 7
        "游击士斯克特",           # 8
        "游击士温蔡尔",           # 9
        "格蕾丝",                 # 10
        "赛尔盖科长",             # 11
        "索妮亚副司令",           # 12
        "餐具",                   # 13
        "餐具",                   # 14
        "椅子",                   # 15
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
        "Function_6_2240",         # 06, 6
        "Function_7_22C4",         # 07, 7
        "Function_8_2568",         # 08, 8
        "Function_9_2753",         # 09, 9
        "Function_10_336A",        # 0A, 10
        "Function_11_3490",        # 0B, 11
        "Function_12_3626",        # 0C, 12
        "Function_13_374A",        # 0D, 13
        "Function_14_38B3",        # 0E, 14
        "Function_15_3914",        # 0F, 15
        "Function_16_3967",        # 10, 16
        "Function_17_3996",        # 11, 17
        "Function_18_3CF5",        # 12, 18
        "Function_19_3D34",        # 13, 19
        "Function_20_3EF5",        # 14, 20
        "Function_21_4477",        # 15, 21
        "Function_22_471E",        # 16, 22
        "Function_23_479F",        # 17, 23
        "Function_24_47F8",        # 18, 24
        "Function_25_4850",        # 19, 25
        "Function_26_48FF",        # 1A, 26
        "Function_27_4D27",        # 1B, 27
        "Function_28_54C1",        # 1C, 28
        "Function_29_5688",        # 1D, 29
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

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_223C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AF")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CF")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2237")

    label("loc_8CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E3")
    Jump("loc_2237")

    label("loc_8E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2237")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_9BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_95A")

    #C0001
    ChrTalk(
        0x8,
        (
            "我并不知道鲁巴彻\x01",
            "的成员去了哪里。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "我一直\x01",
            "都在这里\x01",
            "做调酒师。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B5")

    label("loc_95A")


    #C0003
    ChrTalk(
        0x8,
        (
            "刚才搜查一科的人\x01",
            "来做过调查取证。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "真是麻烦死了……\x01",
            "我只不过是个调酒师而已啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_9B5")

    Jump("loc_2237")

    label("loc_9BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_A20")

    #C0005
    ChrTalk(
        0x8,
        (
            "鲁巴彻事务所从昨晚开始\x01",
            "就有点奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "……也许正在里面做些\x01",
            "见不得人的勾当吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A93")

    #C0007
    ChrTalk(
        0x8,
        (
            "接下来就要看黑月那边的态度了……\x01",
            "……很担心事态的发展啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_END)), "loc_A8E")

    #C0008
    ChrTalk(
        0x8,
        "……欢迎再来。\x02",
    )

    CloseMessageWindow()

    label("loc_A8E")

    Jump("loc_AEF")

    label("loc_A93")


    #C0009
    ChrTalk(
        0x8,
        "袭击事务所吗……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "又是这么唐突的事件啊……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "但愿不会因此而演变成\x01",
            "全面对抗。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AEF")

    Jump("loc_2237")

    label("loc_AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_B97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B2B")

    #C0012
    ChrTalk(
        0x8,
        "……请慢慢享用，尽情放松。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B92")

    label("loc_B2B")


    #C0013
    ChrTalk(
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "本店的舞台表演\x01",
            "要到晚上八点后才开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "在那之前，请放松休息，\x01",
            "耐心等待吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B92")

    Jump("loc_2237")

    label("loc_B97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_D3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C00")

    #C0016
    ChrTalk(
        0x8,
        (
            "……我不知道\x01",
            "什么重要的内情。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "至多也就是听说了一些\x01",
            "黑道那边的流言而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_C00")


    #C0018
    ChrTalk(
        0x8,
        "最近听说了一些奇妙的都市传说呢。\x02",
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
            "不过，在这座城市里，都市传说\x01",
            "也不是什么稀奇的东西。\x01",
            "还是赶快做开店准备吧。\x02",
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
            "#0005F（都市传说……？\x01",
            "  听到了奇怪的事情呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D35")

    Jump("loc_2237")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_FEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 4)), scpexpr(EXPR_END)), "loc_F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DB8")

    #C0022
    ChrTalk(
        0x8,
        (
            "听说，好像是在竞拍会上\x01",
            "出了差错，发生了什么意外……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "鲁巴彻的内部\x01",
            "似乎也乱成一团了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_DB8")


    #C0024
    ChrTalk(
        0x8,
        (
            "最近这一个星期，鲁巴彻商会\x01",
            "安静得有点异常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "听说，好像是在竞拍会上\x01",
            "出了差错，发生了什么意外……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "马尔克尼会长似乎也让哈尔特曼议长\x01",
            "很不满意。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9B")

    #C0027
    ChrTalk(
        0x102,
        (
            "#0108F（看来流言已经\x01",
            "  传播到后巷了呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1C")

    label("loc_E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EDB")

    #C0028
    ChrTalk(
        0x103,
        (
            "#0200F（流言已经\x01",
            "  传播到后巷了呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1C")

    label("loc_EDB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F1C")

    #C0029
    ChrTalk(
        0x104,
        (
            "#0306F（嗯——流言已经\x01",
            "  传播到后巷了啊。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1C")

    SetScenarioFlags(0x0, 0)

    label("loc_F1F")

    Jump("loc_FE6")

    label("loc_F24")


    #C0030
    ChrTalk(
        0x8,
        (
            "欢迎光临。\x01",
            "本店还没到营业时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x153,
        "#1111F这里是什么店呢～？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "……………………………\x01",
            "……是爵士酒吧，\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "不是小孩子可以来的地方哦。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0012F对、对不起，\x01",
            "我们只是顺路过来看看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 4)

    label("loc_FE6")

    Jump("loc_2237")

    label("loc_FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1046")

    #C0035
    ChrTalk(
        0x8,
        (
            "鲁巴彻商会\x01",
            "今天好安静啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "多亏如此，\x01",
            "我们才能安心营业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_1046")


    #C0037
    ChrTalk(
        0x8,
        (
            "鲁巴彻商会\x01",
            "今天好安静啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "有一半的成员都\x01",
            "去那个地方了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "……在这七八年里，\x01",
            "那对他们来说都是一笔重要的生意。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#0001F（『黑之竞拍会』……\x01",
            "  好像在黑道中广为人知呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0103F（在黑道之外也可以说是很有名吧，\x01",
            "  连我都听说过那个传闻……）\x02\x03",

            "#0101F（可能是鲁巴彻方面也在进行宣传，\x01",
            "  把出席这个竞拍会树立为在黑道势力中\x01",
            "  的地位象征了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11B0")

    Jump("loc_2237")

    label("loc_11B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_END)), "loc_121E")

    #C0042
    ChrTalk(
        0x8,
        (
            "听说游行队伍经过了\x01",
            "彩虹剧团的门前。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "把本店的客人\x01",
            "都给引走了啊。\x01",
            "真是令人头疼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_121E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_136C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_1267")

    #C0044
    ChrTalk(
        0x8,
        "本店谢绝儿童入内。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "一个小孩都看不到哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1367")

    label("loc_1267")


    #C0046
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这个人\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x8,
        (
            "是迷路的小孩吗？\x01",
            "没看到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "而且本店是爵士酒吧，\x01",
            "基本上是不允许儿童入内的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0003F是这样吗……\x01",
            "十分感谢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 2)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 22)

    label("loc_1367")

    Jump("loc_2237")

    label("loc_136C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_13D5")

    #C0051
    ChrTalk(
        0x8,
        (
            "听说游行队伍经过了\x01",
            "彩虹剧团的门前。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "把本店的客人\x01",
            "都给引走了啊。\x01",
            "真是令人头疼……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_13D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_143D")

    #C0053
    ChrTalk(
        0x8,
        "今天更热闹了。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "……但愿游客们不要兴奋过头，\x01",
            "不小心迷失方向，\x01",
            "闯进鲁巴彻商会啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2237")

    label("loc_143D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1490")

    #C0055
    ChrTalk(
        0x8,
        "负责警卫工作的警察们也真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "我深表同情啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15A9")

    label("loc_1490")


    #C0057
    ChrTalk(
        0x8,
        "负责警卫工作的警察们也真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "偶尔会遇到\x01",
            "穿着便服的一科警察\x01",
            "在巡视。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "真不愧是搜查一科，\x01",
            "伪装得很好。\x02",
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
        "#0100F您眼力真好……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        "看得多了，就能分辨出来了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15A9")

    Jump("loc_2237")

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_167A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_161F")

    #C0062
    ChrTalk(
        0x8,
        (
            "因为我们店是夜间营业的，\x01",
            "所以只能削减\x01",
            "自己的休息时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        "哎呀呀，真是麻烦啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1675")

    label("loc_161F")


    #C0064
    ChrTalk(
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "在纪念庆典期间，\x01",
            "我们白天也会开店。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "哎呀呀，真是麻烦……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1675")

    Jump("loc_2237")

    label("loc_167A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1723")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1697")
    Call(0, 6)
    Jump("loc_171E")

    label("loc_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_16A8")
    Call(0, 6)
    Jump("loc_171E")

    label("loc_16A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_171B")

    #C0067
    ChrTalk(
        0x8,
        (
            "你要找桑多拉小姐吗，\x01",
            "她还在吧台前\x01",
            "的座位上休息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "要是有什么在意的事，\x01",
            "就去问问她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_171E")

    label("loc_171B")

    Call(0, 6)

    label("loc_171E")

    Jump("loc_2237")

    label("loc_1723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_17C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1740")
    Call(0, 21)
    Jump("loc_17BB")

    label("loc_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_1751")
    Call(0, 21)
    Jump("loc_17BB")

    label("loc_1751")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_17B8")

    #C0069
    ChrTalk(
        0x8,
        (
            "桑多拉小姐还在\x01",
            "吧台前的座位上\x01",
            "休息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "要是有什么在意的事，\x01",
            "就去问问她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BB")

    label("loc_17B8")

    Call(0, 21)

    label("loc_17BB")

    Jump("loc_2237")

    label("loc_17C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_185D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17DD")
    Call(0, 7)
    Jump("loc_1858")

    label("loc_17DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_17EE")
    Call(0, 7)
    Jump("loc_1858")

    label("loc_17EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1855")

    #C0071
    ChrTalk(
        0x8,
        (
            "桑多拉小姐还在\x01",
            "吧台前的座位上\x01",
            "休息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "要是有什么在意的事，\x01",
            "就去问问她吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1858")

    label("loc_1855")

    Call(0, 7)

    label("loc_1858")

    Jump("loc_2237")

    label("loc_185D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18B7")

    #C0073
    ChrTalk(
        0x8,
        "……您是客人吗？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "我们现在正在做营业的准备，\x01",
            "请稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_18B7")


    #C0075
    ChrTalk(
        0x8,
        "……马上就要到营业时间了。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "必须快点准备鸡尾酒，\x01",
            "还得去叫舞台的工作人员。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_190D")

    Jump("loc_2237")

    label("loc_1912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1B1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA8")

    #C0077
    ChrTalk(
        0x8,
        "最近听到了一些可怕的传闻呢。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "听说黑月那边正在击溃\x01",
            "鲁巴彻的各处走私渠道……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F4")

    #C0079
    ChrTalk(
        0x101,
        "#0000F您说的是真的吗……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A0C")

    label("loc_19F4")


    #C0080
    ChrTalk(
        0x101,
        "#0000F那些事情……\x02",
    )

    CloseMessageWindow()

    label("loc_1A0C")


    #C0081
    ChrTalk(
        0x8,
        "虽然不过是传闻。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "但黑月似乎是在一般市民看不见的地方，\x01",
            "手段高超地把鲁巴彻的渠道切断了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "听说，出于这个原因，\x01",
            "连游击士协会也无法出手。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B16")

    label("loc_1AA8")


    #C0084
    ChrTalk(
        0x8,
        (
            "黑月那边似乎采用了\x01",
            "特别聪明的做法。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "虽然我不知道详情，但听说鲁巴彻那边\x01",
            "已经损失了好几条走私渠道了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B16")

    Jump("loc_2237")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B9A")

    #C0086
    ChrTalk(
        0x8,
        (
            "上个月的那件事，对于鲁巴彻\x01",
            "来说，应该根本不值一提吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "对于那些人来说，\x01",
            "应该是件司空见惯的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C52")

    label("loc_1B9A")


    #C0088
    ChrTalk(
        0x8,
        (
            "因为上个月的那件事，\x01",
            "鲁巴彻事务所\x01",
            "也变得忙乱不堪。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "听说有些干部\x01",
            "还被责骂了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "……不过，鲁巴彻\x01",
            "是根植于这里的巨大组织。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "他们的地位不会因为这点事情\x01",
            "就产生动摇的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1C52")

    Jump("loc_2237")

    label("loc_1C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1DA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1CF2")

    #C0092
    ChrTalk(
        0x8,
        (
            "听说东方组织『黑月』\x01",
            "似乎已经开始经营\x01",
            "『洗黑钱事业』了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "那可是由鲁巴彻所掌控的\x01",
            "主要产业之一。\x01",
            "他们肯定不会坐视不管的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DA2")

    label("loc_1CF2")


    #C0094
    ChrTalk(
        0x8,
        (
            "听说东方组织『黑月』\x01",
            "似乎已经开始经营\x01",
            "『洗黑钱事业』了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "黑月最近一直在抢鲁巴彻\x01",
            "的饭碗。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "……因此，\x01",
            "这两个组织展开正式的全面对抗，\x01",
            "恐怕也只是时间的问题吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1DA2")

    Jump("loc_2237")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E14")

    #C0097
    ChrTalk(
        0x8,
        (
            "不管客人是什么来头，\x01",
            "总之请不要妨碍营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "我不想做出让\x01",
            "本店声誉下降的行为。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E85")

    label("loc_1E14")


    #C0099
    ChrTalk(
        0x8,
        (
            "有人在我们店\x01",
            "的门前揽客。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        "哎呀呀，真是给人添麻烦……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "我们可是申请到了经营许可证的\x01",
            "正规酒吧啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E85")

    Jump("loc_2237")

    label("loc_1E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1F0E")

    #C0102
    ChrTalk(
        0x8,
        (
            "不干涉客人的私事\x01",
            "是本店的原则。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "也正因为如此，\x01",
            "才更容易听到一些情报吧。\x01",
            "……虽然这并非我们的本意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2021")

    label("loc_1F0E")


    #C0104
    ChrTalk(
        0x8,
        (
            "最近，有位客人在狂喝一顿之后，\x01",
            "就开始大声抱怨。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "比如什么他在旧城区的任务失败了之类的……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "唉……这种事情，\x01",
            "真希望他不要大声地到处宣扬啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#0005F难道说……他是\x01",
            "鲁巴彻的人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "恕我无法回答。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "呼，这虽然并非我们的本意，\x01",
            "但是这种客人确实比较多呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2021")

    Jump("loc_2237")

    label("loc_2026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_216B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20BD")

    #C0110
    ChrTalk(
        0x8,
        (
            "……鲁巴彻商会\x01",
            "似乎在努力进行组织的强化工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "似乎是为了对抗敌对组织……\x01",
            "我只是听说了这样的传言，并不太清楚详细情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2166")

    label("loc_20BD")


    #C0112
    ChrTalk(
        0x8,
        (
            "……鲁巴彻商会\x01",
            "最近好像在重新布署成员的结构。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "听说还在积极购买武器\x01",
            "和导力车……\x01",
            "具体的事我就不清楚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "我说的这些话，\x01",
            "也只是这附近流传的小道消息而已。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2166")

    Jump("loc_2237")

    label("loc_216B")


    #C0115
    ChrTalk(
        0x8,
        "请问您需要什么？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x103,
        "#0200F请给我橙汁。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        "本店不提供果汁。\x02",
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
            "#0100F缇欧，要不就算了？\x01",
            "这里好像是面向成年人的酒吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2237")

    Jump("loc_85F")

    label("loc_223C")

    TalkEnd(0x8)
    Return()

    # Function_5_7FC end

    def Function_6_2240(): pass

    label("Function_6_2240")


    #C0119
    ChrTalk(
        0x8,
        (
            "……桑多拉小姐\x01",
            "还真的在这里坐了一天呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "虽然不干涉客人的私事\x01",
            "是本店的经营原则，\x01",
            "但她这样做已经妨碍了我们的正常营业啊。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_6_2240 end

    def Function_7_22C4(): pass

    label("Function_7_22C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249F")

    #C0121
    ChrTalk(
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "本店并不贩卖情报。\x01",
            "希望您在点单的时候，只点鸡尾酒类。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003F那么……\x01",
            "来一杯有关『银』的鸡尾酒吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1800)

    #C0124
    ChrTalk(
        0x8,
        (
            "黑月有个叫曹·李的人，\x01",
            "似乎相当聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "他善于使用『头脑』，把对手逼上绝路，\x01",
            "而在『武力』方面，听说他雇佣了神秘的\x01",
            "暗杀者。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "受到这两方面的夹击，\x01",
            "就算是那位加尔西亚·罗西，\x01",
            "也会感到棘手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "……我能说的\x01",
            "也就是这些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#0006F（我、我只是试着问了问……）\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        "#0306F（没想到还真的知道啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x95, 0)
    Jump("loc_2567")

    label("loc_249F")


    #C0130
    ChrTalk(
        0x8,
        (
            "黑月的那位名叫曹·李的人，\x01",
            "似乎相当聪明。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "他善于使用自己的智慧，\x01",
            "把敌人逼上绝路，再从另一个方面\x01",
            "利用神秘的暗杀者来斩尽杀绝……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "真是个可怕的人呢。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "……话说回来，\x01",
            "各位不喝点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2567")

    Return()

    # Function_7_22C4 end

    def Function_8_2568(): pass

    label("Function_8_2568")


    #C0134
    ChrTalk(
        0x8,
        "……请问有什么事？\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        "本店还没有正式开店呢。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        (
            "#0100F这似乎是只在夜晚营业的\x01",
            "爵士酒吧呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        "是啊，正如您所说。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x104,
        (
            "#0309F这店里有很多不错的酒。\x01",
            "是个很棒的店哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0003F爵士酒吧『加兰特』啊……\x02\x03",

            "#0000F（说起来，好像也听\x01",
            "  大哥提起过呢……）\x02",
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
            "但要是客人们在白天走累了，也可以来这里休息一下，\x01",
            "本店不会不识趣到拒绝提供酒水招待的。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "您也可以点些鸡尾酒。\x01",
            "但我们是不会把酒卖给那位小姑娘的。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        (
            "#0201F哼……\x01",
            "（只有我一个人\x01",
            "  被排除在外吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 0)
    Return()

    # Function_8_2568 end

    def Function_9_2753(): pass

    label("Function_9_2753")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27E7")
    Jump("loc_2831")

    label("loc_27E7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2807")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2831")

    label("loc_2807")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2827")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2831")

    label("loc_2827")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2831")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2864")
    Jump("loc_288C")

    label("loc_2864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_288C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_288C")
    Call(0, 27)
    Return()

    label("loc_288C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_290F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x18)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A8")
    Call(0, 12)
    Jump("loc_290A")

    label("loc_28A8")


    #C0143
    ChrTalk(
        0x9,
        "今天也是不停给客人倒酒……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "唉，做这份工作\x01",
            "真是感觉有点空虚了，\x01",
            "是不是该收手不干了呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290A")

    Jump("loc_3362")

    label("loc_290F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_29EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2959")

    #C0145
    ChrTalk(
        0x9,
        (
            "啊——可能有点喝多了。\x01",
            "头一阵一阵地疼啊～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29EA")

    label("loc_2959")


    #C0146
    ChrTalk(
        0x9,
        "啊——头好疼～……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        (
            "昨天还去接待议员先生了。\x01",
            "真是的，超级缠人～……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x9,
        (
            "都说了很多次，本店不允许身体接触，\x01",
            "要说多少次他才会明白啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29EA")

    Jump("loc_3362")

    label("loc_29EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2A47")
    OP_64(0x9)
    SetChrSubChip(0x9, 0x0)

    #C0149
    ChrTalk(
        0x9,
        (
            "（唔嗯……）\x01",
            "那个臭老头，总是毛手毛脚～……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_3362")

    label("loc_2A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2AA9")

    #C0150
    ChrTalk(
        0x9,
        "今天好像要接待帝国派议员吧。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x9,
        (
            "唉，根本不想看到那些老头子\x01",
            "的脸啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE5")

    label("loc_2AA9")


    #C0152
    ChrTalk(
        0x9,
        (
            "埃里克\x01",
            "让我快点去工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x9,
        "呜呜，最近好冷淡啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2AE5")

    Jump("loc_3362")

    label("loc_2AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2BD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B60")

    #C0154
    ChrTalk(
        0x9,
        "最近有一些很豪气的客人。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        (
            "但那些人虽然给钱爽快，\x01",
            "却总是一副高高在上的样子，很难相处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BCB")

    label("loc_2B60")


    #C0156
    ChrTalk(
        0x9,
        (
            "最近这些日子，\x01",
            "有些很有钱的客人来店里。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x9,
        (
            "花钱像流水一样，\x01",
            "特别豪爽。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        "这种人最近有不少啊～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2BCB")

    Jump("loc_3362")

    label("loc_2BD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2C6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2C12")

    #C0159
    ChrTalk(
        0x9,
        (
            "我也有点上了年纪吧，\x01",
            "虽然才二十多岁～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C68")

    label("loc_2C12")


    #C0160
    ChrTalk(
        0x9,
        "啊呜……早上的太阳真刺眼……\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x9,
        (
            "可恶，早上起床的时候，\x01",
            "一年比一年痛苦啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C68")

    Jump("loc_3362")

    label("loc_2C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D02")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C8A")
    Call(0, 10)
    Jump("loc_2CFD")

    label("loc_2C8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2CFA")
    SetChrSubChip(0x9, 0x0)
    OP_64(0x9)

    #C0162
    ChrTalk(
        0x9,
        (
            "呜呜……\x01",
            "呜嗯～……嗯嗯嗯……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        "再让我睡一会吧，埃里克～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_2CFD")

    label("loc_2CFA")

    Call(0, 10)

    label("loc_2CFD")

    Jump("loc_3362")

    label("loc_2D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D93")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D1F")
    Call(0, 11)
    Jump("loc_2D8E")

    label("loc_2D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 7)), scpexpr(EXPR_END)), "loc_2D30")
    Call(0, 11)
    Jump("loc_2D8E")

    label("loc_2D30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2D8B")
    SetChrSubChip(0x9, 0x0)

    #C0164
    ChrTalk(
        0x9,
        (
            "呜呜……\x01",
            "呜嗯～……嗯嗯嗯……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x9,
        "再让我睡一会吧，埃里克～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D8E")

    label("loc_2D8B")

    Call(0, 11)

    label("loc_2D8E")

    Jump("loc_3362")

    label("loc_2D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2E19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DC6")

    #C0166
    ChrTalk(
        0x9,
        "客人要是美少年就好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E14")

    label("loc_2DC6")


    #C0167
    ChrTalk(
        0x9,
        "马上就要到上班时间了。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x9,
        (
            "啊——好讨厌好讨厌，\x01",
            "不想陪老头子聊天啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E14")

    Jump("loc_3362")

    label("loc_2E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2ED8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E88")

    #C0169
    ChrTalk(
        0x9,
        (
            "对于干我们这行的人来说，\x01",
            "现在可是睡眠时间哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "够了啦，\x01",
            "就让人家睡一会嘛～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED3")

    label("loc_2E88")


    #C0171
    ChrTalk(
        0x9,
        (
            "我知道的一切\x01",
            "全都告诉你们了～\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x9,
        (
            "好了啦，\x01",
            "就让人家睡一会嘛～……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2ED3")

    Jump("loc_3362")

    label("loc_2ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2F5E")

    #C0173
    ChrTalk(
        0x9,
        (
            "话说回来，埃里克\x01",
            "总是那么冷静呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x9,
        (
            "还能一脸平静地给\x01",
            "鲁巴彻的老兄端酒呢。\x01",
            "……我好像真的要迷上他了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF3")

    label("loc_2F5E")


    #C0175
    ChrTalk(
        0x9,
        (
            "昨天，鲁巴彻的老兄\x01",
            "也来这里喝酒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x9,
        (
            "不过他好像心情很差，\x01",
            "来了之后就一直在抱怨。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x9,
        (
            "说什么\x01",
            "警察局的臭小鬼……\x01",
            "难道是发生了什么争执吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2FF3")

    Jump("loc_3362")

    label("loc_2FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_30BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3040")

    #C0178
    ChrTalk(
        0x9,
        (
            "最近共和国派的先生们\x01",
            "特别活跃，气派十足呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B9")

    label("loc_3040")


    #C0179
    ChrTalk(
        0x9,
        (
            "昨晚被叫去接待共和国派的\x01",
            "议员们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x9,
        (
            "虽然议员们都有权有势，但就是好累哦～\x01",
            "看着埃里克的侧脸，治愈一下自己吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_30B9")

    Jump("loc_3362")

    label("loc_30BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3188")

    #C0181
    ChrTalk(
        0x9,
        (
            "最近我在欢乐街上\x01",
            "看到了一位很帅的少年。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x9,
        (
            "虽然冷静从容，但又很神秘……\x01",
            "最受不了他那种中性的感觉了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x9,
        (
            "不过他总跟有钱的夫人在一起，\x01",
            "让人无法靠近呢～\x01",
            "那个孩子，应该是个男公关吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3362")

    label("loc_3188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_31CC")

    #C0184
    ChrTalk(
        0x9,
        (
            "最近工作越来越吃力了。\x01",
            "已经上年纪了吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_321C")

    label("loc_31CC")


    #C0185
    ChrTalk(
        0x9,
        "哎呀，已经是早上了……？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x9,
        (
            "呜呜，让我睡一会嘛……\x01",
            "再让我睡一会嘛～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_321C")

    Jump("loc_3362")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_330A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3277")

    #C0187
    ChrTalk(
        0x9,
        (
            "埃里克真帅呢。\x01",
            "而且还很酷。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "嗯——嗯，得到治愈了～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3305")

    label("loc_3277")


    #C0189
    ChrTalk(
        0x9,
        (
            "鲁巴彻的人也经常来这间\x01",
            "酒吧里喝酒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        (
            "因此，那个冷淡的调酒师\x01",
            "才会知道那么多情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x9,
        (
            "嗯嗯——真是被他那\x01",
            "冷峻的美貌治愈了啊～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3305")

    Jump("loc_3362")

    label("loc_330A")

    SetChrSubChip(0x9, 0x0)

    #C0192
    ChrTalk(
        0x9,
        (
            "那个可恶的臭老头，\x01",
            "总是毛手毛脚～！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x9,
        (
            "呼，好累啊……\x01",
            "做接待也不轻松啊～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3362")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_2753 end

    def Function_10_336A(): pass

    label("Function_10_336A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_33AF")

    #C0194
    ChrTalk(
        0x9,
        "呜呜，埃里克好冷淡……\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x9,
        (
            "人家才没有\x01",
            "耍酒疯呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_348F")

    label("loc_33AF")

    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x2)

    #C0196
    ChrTalk(
        0x9,
        (
            "对吧，埃里克～\x01",
            "再给我点酒嘛～……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0197
    ChrTalk(
        0x8,
        (
            "#3P桑多拉小姐，\x01",
            "也差不多该回去了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        "#3P已经过了中午了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3481")

    #C0199
    ChrTalk(
        0x101,
        "#0000F（还在喝啊……）\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x103,
        (
            "#0200F（很担心她是否也会\x01",
            "  弄丢什么东西。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3481")

    SetScenarioFlags(0x0, 1)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)

    label("loc_348F")

    Return()

    # Function_10_336A end

    def Function_11_3490(): pass

    label("Function_11_3490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34D1")

    #C0201
    ChrTalk(
        0x9,
        (
            "纪念庆典什么的，\x01",
            "要是没有就好了（咕噜噜……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3625")

    label("loc_34D1")


    #C0202
    ChrTalk(
        0x9,
        (
            "马上就要到纪念庆典了啊～\x01",
            "大家一定都很期待吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x9,
        (
            "……让人生气～……\x01",
            "纪念庆典时，我们做接待可是非常辛苦哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "从早到晚都要陪着客人喝酒，\x01",
            "还要附和他们做出笑脸……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x9,
        (
            "呃……光是想象，就让人提不起精神了～……\x01",
            "真是干不下去啊（咕噜噜噜……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x15, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3622")

    #C0206
    ChrTalk(
        0x101,
        "#0000F（还在喝啊……）\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        (
            "#0200F（很担心她是否也会\x01",
            "  弄丢什么东西。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3622")

    SetScenarioFlags(0x0, 1)

    label("loc_3625")

    Return()

    # Function_11_3490 end

    def Function_12_3626(): pass

    label("Function_12_3626")


    #C0208
    ChrTalk(
        0xFE,
        (
            "呜呜，已经到傍晚了……？\x01",
            "必须得去工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "……呼……今天就告诉你们\x01",
            "一个秘密吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "这是某位客人以前教给我的\x01",
            "鸡尾酒调制法哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xFE,
        (
            "这么甜美的鸡尾酒，\x01",
            "以后也想再喝几次呢……\x02",
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
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x18)
    Return()

    # Function_12_3626 end

    def Function_13_374A(): pass

    label("Function_13_374A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385D")

    #C0214
    ChrTalk(
        0x101,
        (
            "#0000F达、达德利搜查官，\x01",
            "好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "#0601F………………………………\x02\x03",

            "#0603F……原来是你们这些问题儿童啊，\x01",
            "不要妨碍我们的调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#0306F（就算问他，\x01",
            "  他也不会向我们透露什么吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#0108F（竞拍会的那件事，\x01",
            "  好像给他添了不少麻烦呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_38AF")

    label("loc_385D")


    #C0218
    ChrTalk(
        0xFE,
        (
            "#0603F……你们干的蠢事\x01",
            "已经够多了。\x02\x03",

            "#0601F今后别再做出\x01",
            "这种引人注目的事了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38AF")

    TalkEnd(0xFE)
    Return()

    # Function_13_374A end

    def Function_14_38B3(): pass

    label("Function_14_38B3")

    TalkBegin(0xFE)

    #C0219
    ChrTalk(
        0xFE,
        (
            "我们搜查一科\x01",
            "现在正在调查很重要的案件。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "……没有特别任务支援科\x01",
            "可以插手的余地。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_38B3 end

    def Function_15_3914(): pass

    label("Function_15_3914")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3963")

    #C0221
    ChrTalk(
        0xFE,
        (
            "听说这里是鲁巴彻成员\x01",
            "经常光顾的酒吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "好，去打听一下吧！\x02",
    )

    CloseMessageWindow()

    label("loc_3963")

    TalkEnd(0xFE)
    Return()

    # Function_15_3914 end

    def Function_16_3967(): pass

    label("Function_16_3967")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_3992")

    #C0223
    ChrTalk(
        0xFE,
        (
            "嗯嗯……\x01",
            "真不习惯这种店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3992")

    TalkEnd(0xFE)
    Return()

    # Function_16_3967 end

    def Function_17_3996(): pass

    label("Function_17_3996")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A2A")
    Jump("loc_3A74")

    label("loc_3A2A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A4A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A74")

    label("loc_3A4A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A6A")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A74")

    label("loc_3A6A")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A74")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B38")

    #C0224
    ChrTalk(
        0xC,
        (
            "呼……今天就在\x01",
            "『巴鲁卡』之类的地方打发下时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "呵呵，不管胜败，\x01",
            "都是一招定胜负。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "这也是很适合给纪念庆典\x01",
            "画上句号的爽快玩法吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CED")

    label("loc_3B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3B94")

    #C0227
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔自治州\x01",
            "已经诞生七十年了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "呵呵，喝点酒，\x01",
            "开心一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CED")

    label("loc_3B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3C04")

    #C0229
    ChrTalk(
        0xC,
        (
            "听说麦克道尔市长在上个月\x01",
            "遭遇了危险事件呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xC,
        "呵呵，他安然无恙真是再好不过了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C99")

    label("loc_3C04")


    #C0231
    ChrTalk(
        0xC,
        (
            "今年伴随着纪念庆典，\x01",
            "好像还要召开一场\x01",
            "什么国际研讨会。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xC,
        (
            "听说原本是由麦克道尔\x01",
            "市长提议的。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        (
            "呵呵，他的年纪也不小了，\x01",
            "还真是有精力啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3C99")

    Jump("loc_3CED")

    label("loc_3C9E")


    #C0234
    ChrTalk(
        0xC,
        "呼，这酒可真是不错啊。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xC,
        (
            "虽然调酒师很冷淡，\x01",
            "但是我很喜欢这家店的气氛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_3996 end

    def Function_18_3CF5(): pass

    label("Function_18_3CF5")

    TalkBegin(0xFE)

    #C0236
    ChrTalk(
        0xFE,
        "好了……先喝上一杯吧。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        "嗯嗯，夜晚还很漫长啊～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_3CF5 end

    def Function_19_3D34(): pass

    label("Function_19_3D34")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DC8")
    Jump("loc_3E12")

    label("loc_3DC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E12")

    label("loc_3DE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E08")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E12")

    label("loc_3E08")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E12")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA2")

    #C0238
    ChrTalk(
        0xFE,
        "咕咚咕咚……呼啊～！\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "话说回来，那位经理\x01",
            "可真是够慢的。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        "难得我有空接待他～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3EED")

    label("loc_3EA2")


    #C0241
    ChrTalk(
        0xFE,
        "今天要陪贸易公司的经理……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "嗯，你们要干什么？\x01",
            "可以不要打扰我吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EED")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_3D34 end

    def Function_20_3EF5(): pass

    label("Function_20_3EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F0B")
    Call(0, 29)
    Jump("loc_4476")

    label("loc_3F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_446D")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FA8")
    Jump("loc_3FF2")

    label("loc_3FA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3FC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FF2")

    label("loc_3FC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FF2")

    label("loc_3FE8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FF2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4328")
    SetChrSubChip(0xFE, 0x0)

    #C0243
    ChrTalk(
        0x11,
        (
            "#2106F………………………………\x02\x03",

            "……纪念庆典的最后一天吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#0005F格蕾丝小姐……？\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4132")
    Jump("loc_417C")

    label("loc_4132")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4152")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_417C")

    label("loc_4152")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4172")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_417C")

    label("loc_4172")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_417C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0245
    ChrTalk(
        0x11,
        (
            "#2105F啊……罗伊德，是你们啊。\x02\x03",

            "#2102F吓我一跳……\x01",
            "别总是突然跳出来吓人嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        "#0002F哈哈，对不起。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#0105F格蕾丝小姐\x01",
            "在庆典最后一天休假吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x11,
        (
            "#2109F怎么会～\x01",
            "只是稍微休息一下而已啦。\x02\x03",

            "#2100F过一会，到傍晚的时候，\x01",
            "还有闭幕式要报道呢。\x02\x03",

            "#2104F……其实我本想去\x01",
            "其它地方取材呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        (
            "#0013F其它地方……\x01",
            "（……难道是……）\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x102,
        (
            "#0108F（她大概已经知道\x01",
            "  竞拍会的事情了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB6, 4)
    Jump("loc_4461")

    label("loc_4328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43E0")

    #C0251
    ChrTalk(
        0x11,
        (
            "#2100F啊，对了对了，\x01",
            "关于那个拍照的委托，如果照片数量够了，\x01",
            "就拿到通讯社的接待处去吧。\x02\x03",

            "#2109F今天就是截稿日了，\x01",
            "多加注意，不要错过提交期限哦～¤\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 6)
    Jump("loc_4461")

    label("loc_43E0")


    #C0252
    ChrTalk(
        0x11,
        (
            "#2104F呵呵，话说回来，\x01",
            "还真是稍微吃了一惊呢。\x02\x03",

            "#2100F……口气虽然完全不同，\x01",
            "但是声音的感觉又很相似……\x02",
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

    label("loc_4461")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_4476")

    label("loc_446D")

    TalkBegin(0xFE)
    Call(0, 21)
    TalkEnd(0xFE)

    label("loc_4476")

    Return()

    # Function_20_3EF5 end

    def Function_21_4477(): pass

    label("Function_21_4477")

    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_44EE")

    #C0254
    ChrTalk(
        0x11,
        (
            "#2100F不过，那家店的东西\x01",
            "不是都超级昂贵的吗？\x02\x03",

            "资金周转就那么灵活吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x8,
        "不知道啊，那种事……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4719")

    label("loc_44EE")


    #C0256
    ChrTalk(
        0x11,
        (
            "#2105F哎～是吗。\x02\x03",

            "#2109F然后呢然后呢？\x01",
            "那个用来接待的店是哪家呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "好像是最近\x01",
            "众口相传的那家店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "是大约半年前\x01",
            "从帝都入驻这里的……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x11,
        (
            "#2105F什么～！？\x01",
            "你是说『诺艾·布朗』！？\x02\x03",

            "那不是一个超高级的会员制俱乐部吗，\x01",
            "连女公关也都是超一流的！\x02\x03",

            "#2109F真好啊～！\x01",
            "我也好想去享受一下！\x02",
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
        "#0000F（看起来，她似乎正在询问情报呢……）\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#0306F（不过看她这种兴奋的样子……\x01",
            "  到底是真实感情，还是演技呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x103,
        "#0200F（我认为恐怕两者都有吧。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4719")

    OP_4C(0x8, 0xFF)
    Return()

    # Function_21_4477 end

    def Function_22_471E(): pass

    label("Function_22_471E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_479E")
    OP_29(0x46, 0x1, 0x4)

    #C0263
    ChrTalk(
        0x101,
        (
            "#0003F（好了，后巷的调查\x01",
            "  也进行得差不多了。）\x02\x03",

            "#0001F（接下来，就去\x01",
            "  中央广场看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 4)

    label("loc_479E")

    Return()

    # Function_22_471E end

    def Function_23_479F(): pass

    label("Function_23_479F")

    TalkBegin(0xFF)

    #C0264
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "呜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        "#0003F没有在这里留下什么气味吗……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_23_479F end

    def Function_24_47F8(): pass

    label("Function_24_47F8")

    TalkBegin(0xFF)

    #C0266
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "呜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x103,
        (
            "#0200F当事人并没有\x01",
            "在这里坐过呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_24_47F8 end

    def Function_25_4850(): pass

    label("Function_25_4850")

    TalkBegin(0xFF)

    #C0268
    ChrTalk(
        0x11C,
        (
            "#1200F（嗅嗅）………\x02\x03",

            "……呜～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0269
    ChrTalk(
        0x101,
        "#0005F在这里留下了味道吗……\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x103,
        (
            "#0200F看样子，副局长似乎\x01",
            "曾坐在这里喝过酒呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x15, 0x1, 0x7)
    TalkEnd(0xFF)
    Return()

    # Function_25_4850 end

    def Function_26_48FF(): pass

    label("Function_26_48FF")

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
            "#11P欢迎光临，\x01",
            "请问您要点些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        (
            "#6P#0001F不好意思，虽然可能有些唐突。\x01",
            "……但请问，您昨晚有没有看到过\x01",
            "我们的副局长呢？\x02\x03",

            "#0003F唔，是个身材比较矮小，\x01",
            "长着一张狐狸脸的……\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x8,
        "#11P是指皮埃尔副局长吗？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x8,
        (
            "#11P昨晚他确实来过，\x01",
            "不过似乎醉得\x01",
            "十分严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#6P#0203F听副局长说，他把结婚戒指\x01",
            "弄丢了。\x02\x03",

            "#0200F请问店里的人有没有看到？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x8,
        "#11P完全没有。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x101,
        (
            "#6P#0006F是、是、是这样吗……\x01",
            "（竟然否定得如此干脆……）\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x8,
        (
            "#11P不过……说到这个，\x01",
            "我记得他当时很激动地\x01",
            "在抱怨夫人的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        "#11P说什么『我要离开你』之类的。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "#11P然后就很积极地\x01",
            "『接触』这里的\x01",
            "女公关。\x02",
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
        "#6P#0006F没想到会听到这种事……\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x103,
        "#6P#0203F完全不想听呢。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "#11P当时的那位女公关──桑多拉小姐，\x01",
            "现在还坐在吧台那里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#11P如果您想知道详情，\x01",
            "就直接去问她吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#6P#0000F说得也是……\x02\x03",

            "#0003F（副局长在那个时候\x01",
            "  是否还戴着结婚戒指……\x01",
            "  关于这点，去向她确认一下吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -1070, 0, 4440, 45)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0x15, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_26_48FF end

    def Function_27_4D27(): pass

    label("Function_27_4D27")

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
            "#5P#0000F那个，打扰一下，\x01",
            "我们是克洛斯贝尔警察局的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0287
    ChrTalk(
        0x9,
        "#12P呜呜……嗯嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x9,
        "#12P让我多睡会嘛，埃里克～……\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(300)

    #C0289
    ChrTalk(
        0x103,
        "#5P#0200F好像正在睡觉呢。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        "#5P#0006F没办法了……\x02",
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    SetChrName("")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德摇晃了一下这位女性的肩部。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0292
    ChrTalk(
        0x101,
        (
            "#5P#0001F对不起，打扰了，\x01",
            "我们是克洛斯贝尔警察局的人！\x02",
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
            "#12P嗯……\x01",
            "干什么啊，真是的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x101,
        (
            "#5P#0003F十分抱歉，\x01",
            "有些事想向您打听。\x02\x03",

            "#0001F昨晚，我们的副局长似乎\x01",
            "与您在一起……\x02\x03",

            "请问您记不记得，副局长当时\x01",
            "有没有戴着结婚戒指呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#12P副局长？\x01",
            "啊，就是那个老往我面前凑的大叔啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x9,
        (
            "#12P呜呜……人家都说了\x01",
            "只喜欢年轻帅气的男人啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        (
            "#12P结果他还死皮赖脸地纠缠，还说什么\x01",
            "『你好漂亮啊』之类的话，真是个恶心的大叔！\x02",
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
            "#5P#0006F不行，这个人好像\x01",
            "也醉得相当厉害……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#5P#0200F看她的样子，似乎是\x01",
            "连着喝了一整夜的酒……\x01",
            "好强烈的酒臭味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#12P因为啊，那个男人\x01",
            "说要请人家喝酒的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x9,
        (
            "#12P还过来握住\x01",
            "人家的手。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "#12P还说什么会跟老婆分手，\x01",
            "这样我们就可以在一起了。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#5P#0003F（我实在是……\x01",
            "  听不下去了……\x01",
            "  暂时到此为止吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#5P#0200F（是啊，听起来\x01",
            "  这个话题会变得很长……）\x02",
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
            "#12P对了，记得那时候\x01",
            "他好像给过我什么。\x02",
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
        "#5P#0005F给过你什么……？\x02",
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x9,
        "#12P对对，就是这个了。\x02",
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
            "#800M红耀石的结婚戒指\x07\x00",
            "收下了。\x02",
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
            "#12P『这是送给你的』——\x01",
            "他当时是这么说的，\x01",
            "不过这根本就不是我喜欢的类型啦～\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        "#12P你们尽管拿走吧。\x02",
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
            "#5P#0200F………结婚戒指………\x01",
            "竟然找到了……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#5P#0011F副局长……\x01",
            "原来戒指不是无心丢失的吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x9,
        "#12P那个，请问发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11C,
        (
            "#5P#1203F呜噜噜噜噜噜……\x01",
            "（哼，真是个无聊的结局啊。）\x02",
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

    # Function_27_4D27 end

    def Function_28_54C1(): pass

    label("Function_28_54C1")

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

    # Function_28_54C1 end

    def Function_29_5688(): pass

    label("Function_29_5688")

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
            "#6P#2102F哦，你们来了啊。\x02\x03",

            "#2109F恕我单刀直入吧，关于『黑月受袭』事件，\x01",
            "你们可以把了解到的情况都告诉我吗？\x02\x03",

            "你们在事务所里听曹先生\x01",
            "透露了很多内情吧？\x02",
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
        "#0006F#11P还真是直截了当呢……\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#11P#0211F话说回来，您怎么知道\x01",
            "我们去拜访过黑月呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#6P#2106F哎呀，那个～我一大早就听到了消息，\x01",
            "然后申请去采访曹先生，\x01",
            "结果达德利那家伙突然出现了。\x02\x03",

            "#2105F就在我静观其变的时候，\x01",
            "你们几个又跑了进去。\x02\x03",

            "#2100F接着达德利他们就摆着一张苦瓜脸，\x01",
            "垂头丧气地走了出来。\x01",
            "再后来，你们也带着若有所思的表情出来了。\x02\x03",

            "#2109F按这种情况来看，唯一的答案\x01",
            "就是你们探听到了许多情报吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#0001F#11P原来如此……\x01",
            "是这么一回事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        (
            "#12P#0101F不管怎样，我想您应该也知道，\x01",
            "在调查过程中探听到的情报\x01",
            "是不能透露给一般人的……\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        (
            "#6P#2109F我当然知道啦～\x01",
            "所以我们才要『互相帮助』嘛。\x02\x03",

            "#2102F你们难道不想知道加尔西亚\x01",
            "的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#0005F#11P这个……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x104,
        (
            "#5P#0306F还是和以前一样，很擅长\x01",
            "撒下美味的诱饵，引别人上勾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x11,
        (
            "#6P#2100F连那个『竞拍会』的前后经过，\x01",
            "我都听说了哦～\x02\x03",

            "#2104F鲁巴彻的人似乎做出了蠢事，\x01",
            "让议长发火了……\x02\x03",

            "#2102F关于这些事情的前前后后，\x01",
            "你们难道不想知道吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#0006F#11P唉，我明白了。\x02\x03",

            "#0013F不过，曹先生说的只是一些\x01",
            "暗示性的话，并不能算是正式情报。\x02\x03",

            "还请理解。\x02",
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
            "#5P#2101F……原来如此。\x02\x03",

            "#2106F嗯……看来目前的状况\x01",
            "比我们想象中的还要糟呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……是这样的。\x02\x03",

            "#0001F就目前的状况来看，\x01",
            "他们双方都还算是节制，\x01",
            "不想把普通市民卷入其中……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x11,
        (
            "#5P#2101F不，如果真是这样，\x01",
            "这次的事件也太过唐突了。\x02\x03",

            "虽说是在深夜，但居然在\x01",
            "通讯社的附近发动袭击哦？！\x02\x03",

            "#2106F而且离我们不远就是天下闻名的ＩＢＣ……\x01",
            "再怎么想，也做得太欠考虑了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#6P#0106F嗯，是啊……\x02\x03",

            "#0101F如此贸然行动，会使大家对\x01",
            "克洛斯贝尔市这个金融贸易中心的\x01",
            "信赖感产生动摇呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x11,
        (
            "#5P#2100F说到这里，可就是重点啦。\x02\x03",

            "#2103F嗯……如此看来，我所掌握的这些情报\x01",
            "或许并不是假的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#6P#0205F格蕾丝小姐掌握的情报……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        "#6P#0001F……可以告诉我们吗？\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x11,
        (
            "#5P#2100F好啊，\x01",
            "下面该轮到我说了。\x02\x03",

            "#2103F事实上……\x01",
            "这是关于黑手党内部的情报。\x02\x03",

            "#2101F有传言说，在最近这段时间，\x01",
            "副头目加尔西亚的统率力\x01",
            "已经没有以前那么强大了～\x02",
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
        "#6P#0005F这是……真的吗？\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x104,
        (
            "#12P#0306F真是有点难以相信呢……\x02\x03",

            "#0301F没想到，连那个像怪物一样的大叔\x01",
            "也会被部下违抗啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x11,
        (
            "#5P#2106F嗯，说得也是。\x02\x03",

            "#2101F不过，之前在旧城区发生的那起事件，\x01",
            "还有针对矿山镇的争夺权益行动，\x01",
            "好像都不是加尔西亚下达的指示。\x02\x03",

            "似乎是他手下的人急于立功，\x01",
            "擅做主张而做出的行动……\x02\x03",

            "这些年轻人肆意妄为的做法，\x01",
            "最近似乎越发增多了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        "#12P#0301F嗯……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#6P#0105F请、请等一下。\x02\x03",

            "#0101F难道说，昨天晚上的袭击事件\x01",
            "也只是那些年轻人的擅自行动吗……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x11,
        (
            "#5P#2106F不，那件事闹得太大了，\x01",
            "我想应该不会吧……\x02\x03",

            "#2100F不过，考虑到这些情况，\x01",
            "加尔西亚刚才的态度\x01",
            "似乎也很好理解了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x104,
        (
            "#12P#0308F的确……\x01",
            "他的部下也没有和他在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x101,
        (
            "#6P#0003F鲁巴彻内部的统率工作，\x01",
            "让他疲于应付了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#6P#0200F不过，那位会长\x01",
            "到底在做些什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x11,
        (
            "#5P#2106F从我了解到的情况来看，\x01",
            "他似乎很想挽回在『竞拍会』\x01",
            "上丢掉的面子。\x02\x03",

            "#2101F当然要拼命去讨\x01",
            "哈尔特曼议长的欢心……\x02\x03",

            "不过同时也要笼络自治州内\x01",
            "新的权势人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x102,
        (
            "#6P#0101F新的权势人物……\x01",
            "会是哪边的人呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x11,
        (
            "#5P#2103F简单来说，就是共和国派的议员了。\x02\x03",

            "#2101F还有传闻说，他们与警备队司令等人\x01",
            "曾经多次会面。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#6P#0103F原来如此……\x01",
            "他们的目的是抑制『黑月』\x01",
            "的政治影响力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#6P#0008F笼络警备队司令，是为了\x01",
            "强化武器走私的渠道吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        (
            "#12P#0306F大概就是这样吧。\x02\x03",

            "#0301F另外，听说那个笨蛋司令\x01",
            "很会讨哈尔特曼议长的欢心。\x02\x03",

            "也许是想借着讨好他的机会，\x01",
            "来间接地笼络\x01",
            "议长吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x11,
        (
            "#5P#2104F嗯，我也这么认为。\x02\x03",

            "#2102F哎呀～跟你们谈一下之后，\x01",
            "思绪果然就更加清晰了！\x02\x03",

            "#2109F嗯嗯！\x01",
            "情报交换果然有价值啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#6P#0002F哈哈……\x01",
            "说实话，您的情报对我们也很有帮助呢。\x02\x03",

            "#0006F不过，把情报稍微整理一下之后，\x01",
            "果然能感觉到有些地方明显不对劲啊……\x02",
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
        "#6P#0105F不对劲？\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x11,
        "#5P#2105F……什么意思？\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        (
            "#6P#0003F虽然他们的每一项行动\x01",
            "都有令人信服的理由……\x02\x03",

            "但所有的行动好像都显得冲动莽撞，缺乏组织性，\x01",
            "感觉并不像是有人在背后策划。\x02\x03",

            "#0008F我对鲁巴彻的看法是，\x01",
            "……虽然有贬义的成分在内，\x01",
            "但他们拥有大都市所特有的『精明』……\x02\x03",

            "#0001F但从这些行动上，却完全看不出『精明』的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x102,
        "#6P#0101F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x11,
        (
            "#5P#2101F嗯……\x01",
            "听你这么一说，好像的确如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x103,
        (
            "#6P#0203F从克洛斯贝尔这株摇钱树上，\x01",
            "吸取甘甜汁液的系统……\x02\x03",

            "#0201F作为能确立如此精密系统的组织，\x01",
            "那些举动的确都太过冲动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        (
            "#12P#0308F会不会，有一些足以让他们发狂，\x01",
            "但我们却并不知晓的『要素』混于其中呢……\x02\x03",

            "#0301F会是这样的吗？\x02",
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
            "#5P#0000F嗯……不过这也只是我的直觉而已。\x02\x03",

            "#0003F袭击『黑月』的那些人员，战斗力\x01",
            "简直高得离谱……\x02\x03",

            "#0001F加尔西亚的态度会变得那么奇怪，\x01",
            "我想大概也与此有关。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x11,
        (
            "#5P#2102F嗯——真不愧是罗伊德，\x01",
            "感觉很敏锐嘛。\x02\x03",

            "#2109F喂，我说，你如果被警察局给开除的话，\x01",
            "要不要来我们克洛斯贝尔时代周刊社工作啊？\x02\x03",

            "让我们一起冲击\x01",
            "菲利策奖吧！\x02",
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
            "#6P#0006F不必了，好意心领……\x02\x03",

            "#0013F另外，请不要突然说出这么\x01",
            "不吉利的话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x104,
        (
            "#12P#0305F话说回来，\x01",
            "那个菲利策奖\x01",
            "是什么啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#6P#0100F好像是授予当年\x01",
            "最优秀记者的\x01",
            "国际性奖项……\x02",
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
            "#6P#0001F──不好意思，\x01",
            "我接听一下通讯。\x02",
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
            "#0001F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("老人的声音")

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "打扰了，是我！\x01",
            "玛因兹的比克森！\x02",
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
            "#0000F啊，是镇长先生啊。\x02\x03",

            "您怎么了？\x01",
            "冈兹先生出了什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "其、其实……\x01",
            "他现在正在克洛斯贝尔的\x01",
            "『巴鲁卡』呢，但是……\x02\x03",

            "他、他看上去好像有点奇怪，\x01",
            "所以我才与你联络……\x02",
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
            "#0005F看上去有点奇怪……？\x02\x03",

            "#0001F是哪里奇怪呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从刚才开始，冈兹就一直在和\x01",
            "其他的客人玩扑克……\x02\x03",

            "但好像有种让人紧张的恐怖气氛，\x01",
            "总感觉似乎会演变成暴力事件……\x02\x03",

            "对不起，总而言之，\x01",
            "你们能过来看看吗！？\x02",
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
            "#0011F我知道了。\x02\x03",

            "#0001F是『巴鲁卡』吧？\x01",
            "我们就在附近，马上就过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("镇长的声音")

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好的，那就拜托你们了！\x07\x00\x02",
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
        "#6P#0101F玛因兹的镇长先生？\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        (
            "#12P#0305F怎么回事，好像\x01",
            "提到了『巴鲁卡』？\x02",
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
            "#5P#0013F嗯，那个冈兹先生\x01",
            "正在和其他客人玩牌，\x01",
            "但似乎要演变为暴力事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x102,
        "#6P#0105F哎……？\x02",
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x103,
        (
            "#6P#0201F难道是因为他百战百胜，\x01",
            "引起了对手的怨恨吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#12P#0306F他那种傲慢的态度，再加上总是赢牌，\x01",
            "把对手给惹火也不足为奇吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x11,
        (
            "#5P#2103F嗯，必须快点过去，\x01",
            "看看到底发生了什么。\x02\x03",

            "#2110F那我们就赶快出发吧！\x01",
            "一起去『巴鲁卡』！\x02",
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
        "#5P#2105F哎，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x102,
        "#6P#0109F不，那个……\x02",
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
            "#5P#0006F……就算叫她别跟来应该也没用吧。\x01",
            "别在意这些了，赶快走吧。\x02",
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

    # Function_29_5688 end

    SaveToFile()

Try(main)
