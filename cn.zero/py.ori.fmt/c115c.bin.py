from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c115c.bin",                # FileName
        "c115c",                    # MapName
        "c115c",                    # Location
        0x0018,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 24, 0, 1, 0, 2],
    )

    BuildStringList((
        "c115c",                  # 0
        "接待小姐瑞贝卡",         # 1
        "接待小姐芙兰",           # 2
        "接待小姐芙兰",           # 3
        "多诺邦警督",             # 4
        "雷蒙德搜查官",           # 5
        "警官",                   # 6
        "乔里基科长",             # 7
        "艾玛搜查官",             # 8
        "嫌疑犯",                 # 9
        "警官",                   # 10
        "赛尔盖科长",             # 11
        "青年",                   # 12
        "雾香",                   # 13
        "假货商",                 # 14
        "雷蒙德搜查官",           # 15
        "凯特巡警",               # 16
    ))

    AddCharChip((
        "chr/ch30400.itc",                   # 00
        "chr/ch06900.itc",                   # 01
        "chr/ch06902.itc",                   # 02
        "chr/ch30100.itc",                   # 03
        "chr/ch30100.itc",                   # 04
        "chr/ch21000.itc",                   # 05
        "chr/ch30000.itc",                   # 06
        "chr/ch30300.itc",                   # 07
        "chr/ch30200.itc",                   # 08
        "chr/ch30500.itc",                   # 09
        "chr/ch30202.itc",                   # 0A
        "chr/ch24102.itc",                   # 0B
        "chr/ch30600.itc",                   # 0C
        "chr/ch02502.itc",                   # 0D
        "chr/ch23602.itc",                   # 0E
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

    DeclNpc(-100,    0,       15399,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(3000,    0,       15930,   90,   261,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-9600,   100,     18239,   270,  469,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   7,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   8,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    261,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-125379, 0,       19520,   0,    389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-125080, 150,     16309,   90,   469,  0x0, 0,   13,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-122440, 150,     16180,   270,  469,  0x0, 0,   14,  0,   255, 255, 0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-122300, 150,     16500,   270,  469,  0x0, 0,   11,  0,   255, 255, 0,   17,  255,  0)
    DeclNpc(-125080, 150,     16500,   90,   469,  0x0, 0,   10,  0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-59229,  29,      21360,   270,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)

    DeclEvent(0x0000, 0, 31,  -12.699999809265137,   19.8700008392334,      -0.5,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142984867096,    0.0,                   4.233333587646484,     -9.9350004196167,      0.1428571492433548,    1.0])

    DeclActor(-100,    0,       14400,   1100,    -100,    1500,    15400,   0x007E, 0,  3,  0x0000)
    DeclActor(2770,    0,       14280,   1000,    3000,    1500,    15930,   0x007E, 0,  7,  0x0000)
    DeclActor(-34480,  0,       20000,   1000,    -34480,  1000,    20000,   0x007C, 0,  18, 0x0000)
    DeclActor(-9850,   0,       16000,   1000,    -9850,   1500,    16000,   0x007C, 0,  32, 0x0000)
    DeclActor(-9850,   0,       13750,   1000,    -9850,   1500,    13750,   0x007C, 0,  32, 0x0000)

    ScpFunction((
        "Function_0_464",          # 00, 0
        "Function_1_51C",          # 01, 1
        "Function_2_75D",          # 02, 2
        "Function_3_7C9",          # 03, 3
        "Function_4_7CD",          # 04, 4
        "Function_5_BB2",          # 05, 5
        "Function_6_127D",         # 06, 6
        "Function_7_134B",         # 07, 7
        "Function_8_134F",         # 08, 8
        "Function_9_1D01",         # 09, 9
        "Function_10_1FCD",        # 0A, 10
        "Function_11_20F8",        # 0B, 11
        "Function_12_23CE",        # 0C, 12
        "Function_13_24AA",        # 0D, 13
        "Function_14_2741",        # 0E, 14
        "Function_15_281D",        # 0F, 15
        "Function_16_28BE",        # 10, 16
        "Function_17_2A51",        # 11, 17
        "Function_18_2C72",        # 12, 18
        "Function_19_2D0A",        # 13, 19
        "Function_20_2EA9",        # 14, 20
        "Function_21_3091",        # 15, 21
        "Function_22_3132",        # 16, 22
        "Function_23_31BE",        # 17, 23
        "Function_24_42C4",        # 18, 24
        "Function_25_4438",        # 19, 25
        "Function_26_4FD3",        # 1A, 26
        "Function_27_5CC0",        # 1B, 27
        "Function_28_5D54",        # 1C, 28
        "Function_29_5DC3",        # 1D, 29
        "Function_30_76FF",        # 1E, 30
        "Function_31_850D",        # 1F, 31
        "Function_32_8599",        # 20, 32
    ))


    def Function_0_464(): pass

    label("Function_0_464")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_4A4"),
        (1, "loc_4B0"),
        (2, "loc_4BC"),
        (3, "loc_4C8"),
        (4, "loc_4D4"),
        (5, "loc_4E0"),
        (6, "loc_4EC"),
        (SWITCH_DEFAULT, "loc_4F8"),
    )


    label("loc_4A4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4B0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4BC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4C8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4D4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4E0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4EC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_4F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_504")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_504")

    label("loc_51B")

    Return()

    # Function_0_464 end

    def Function_1_51C(): pass

    label("Function_1_51C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_52B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 29)

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_57B")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x11, -12850, 0, 7690, 90)
    SetChrPos(0xC, -11260, 0, 7690, 270)
    SetChrPos(0xE, -11040, 0, 13810, 90)
    Jump("loc_75C")

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_598")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_598")

    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xB, -10370, 0, 7070, 270)
    SetChrPos(0x17, -11980, 0, 8189, 135)
    SetChrPos(0xE, -11930, 0, 7110, 90)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 0, 15900, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_75C")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_637")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -58050, 0, 15900, 90)
    Jump("loc_75C")

    label("loc_637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E0")
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_67B")
    SetChrPos(0xB, -124850, 0, 14920, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_6B9")

    label("loc_67B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_697")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_6B9")

    label("loc_697")

    SetChrPos(0xB, -57730, 0, 16309, 180)
    SetChrPos(0xC, -57730, 0, 14480, 0)

    label("loc_6B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6DB")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -11040, 0, 13810, 90)

    label("loc_6DB")

    Jump("loc_75C")

    label("loc_6E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_75C")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, -12850, 0, 7690, 90)
    SetChrPos(0xD, -11260, 0, 7690, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -11040, 0, 13810, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_757")
    SetChrPos(0xE, -58050, 0, 15900, 90)
    Jump("loc_75C")

    label("loc_757")

    SetChrFlags(0xE, 0x80)

    label("loc_75C")

    Return()

    # Function_1_51C end

    def Function_2_75D(): pass

    label("Function_2_75D")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_779")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_7C8")

    label("loc_779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_787")
    Jump("loc_7C8")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_7A3")
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_65(0x1, 0x1)
    Jump("loc_7C8")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7B1")
    Jump("loc_7C8")

    label("loc_7B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7BF")
    Jump("loc_7C8")

    label("loc_7BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7C8")

    label("loc_7C8")

    Return()

    # Function_2_75D end

    def Function_3_7C9(): pass

    label("Function_3_7C9")

    Call(0, 4)
    Return()

    # Function_3_7C9 end

    def Function_4_7CD(): pass

    label("Function_4_7CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_816")
    TalkBegin(0x8)
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_811")
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0x8)
    Call(0, 25)
    Return()

    label("loc_811")

    Jump("loc_837")

    label("loc_816")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_837")
    Call(0, 23)
    Return()

    label("loc_837")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x35, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B02")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880")

    #C0001
    ChrTalk(
        0x8,
        (
            "关于通缉魔兽的讨伐，\x01",
            "辛苦大家了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_880")


    #C0002
    ChrTalk(
        0x8,
        (
            "对了，各位知道吗？\x01",
            "克洛斯贝尔警察正在进行\x01",
            "魔兽的情报调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        "#0005F是……情报调查吗？\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "嗯，我想各位应该知道\x01",
            "在战斗手册里记录着\x01",
            "有关魔兽的项目吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "各位曾经遭遇过的魔兽\x01",
            "都会被记录在战斗手册里哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "当情报积攒到一定程度时，\x01",
            "就请拿来给我看一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "因为各位所收集的情报对\x01",
            "警局内制定安全对策\x01",
            "很有帮助。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A02")

    #C0008
    ChrTalk(
        0x102,
        (
            "#0100F原来如此……警察局也\x01",
            "很下功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A81")

    label("loc_A02")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A44")

    #C0009
    ChrTalk(
        0x103,
        (
            "#0200F原来如此……警察局也\x01",
            "很下功夫啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A81")

    label("loc_A44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A81")

    #C0010
    ChrTalk(
        0x104,
        (
            "#0300F原来如此……警察局也\x01",
            "很下功夫啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A81")


    #C0011
    ChrTalk(
        0x8,
        (
            "嗯，这也是为了保障\x01",
            "市民的安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "各位在向我提交魔兽情报时，\x01",
            "局内会多少支付一些报酬的。\x01",
            "所以请不要客气，随时过来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x50, 2)
    SetScenarioFlags(0x1, 3)

    label("loc_B02")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "出示战斗手册\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)
    Call(0, 30)
    Jump("loc_BA9")

    label("loc_B79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8D")
    Jump("loc_BA9")

    label("loc_B8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_BA9")

    Jump("loc_B0C")

    label("loc_BAE")

    TalkEnd(0x8)
    Return()

    # Function_4_7CD end

    def Function_5_BB2(): pass

    label("Function_5_BB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C60")

    #C0013
    ChrTalk(
        0x8,
        "各位辛苦了啊。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "违章停车的取缔工作结束之后，\x01",
            "就请和我联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "我会通知\x01",
            "公共安全科的人的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000F嗯，到时候\x01",
            "就麻烦您了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127C")

    label("loc_C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_D13")

    #C0017
    ChrTalk(
        0x8,
        (
            "当情报积攒到一定程度时，\x01",
            "就请拿来给我看一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "因为各位所收集的情报对\x01",
            "制定安全对策很有帮助。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "而且我们多少会支付一些报酬的，\x01",
            "所以请不要客气，随时过来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127C")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D95")

    #C0020
    ChrTalk(
        0x8,
        "呵呵，各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "在纪念庆典期间，\x01",
            "事件好像也增加了呢……\x01",
            "各位在努力工作时，也请注意不要太过勉强自己哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127C")

    label("loc_D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_E15")

    #C0022
    ChrTalk(
        0x8,
        (
            "按照预定，在大圣堂的钟声响起，\x01",
            "宣告黄昏降临时，闭幕式就正式开始。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "我们差不多也该去帮忙\x01",
            "进行准备工作了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127C")

    label("loc_E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_EF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E99")

    #C0024
    ChrTalk(
        0x8,
        (
            "每年的纪念庆典都会出现\x01",
            "不少迷路的孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "今年也有很多呢……\x01",
            "这类事件大概\x01",
            "发生了二十起左右吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EEC")

    label("loc_E99")


    #C0026
    ChrTalk(
        0x8,
        (
            "无论是哪个孩子，其父母\x01",
            "应该都是一样心急如焚的……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "总之请尽力帮助他们吧。\x02",
    )

    CloseMessageWindow()

    label("loc_EEC")

    Jump("loc_127C")

    label("loc_EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_FB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5E")

    #C0028
    ChrTalk(
        0x8,
        (
            "呼，人潮总算是\x01",
            "渐渐退去了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "芙兰好像也很累了……\x01",
            "今天就早点收工好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FB4")

    label("loc_F5E")


    #C0030
    ChrTalk(
        0x8,
        (
            "芙兰应该在自动贩卖机\x01",
            "的附近休息呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "如果方便的话，\x01",
            "不妨过去和她打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB4")

    Jump("loc_127C")

    label("loc_FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1062")

    #C0032
    ChrTalk(
        0x8,
        (
            "今天预定要在市内\x01",
            "展开纪念游行活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "前来询问的人已经有几十位了，\x01",
            "对市民的引导工作也是十分必要的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "看起来……似乎有必要\x01",
            "拿出全部的干劲呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_127C")

    label("loc_1062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115C")

    #C0035
    ChrTalk(
        0x8,
        (
            "今天将要在市政厅\x01",
            "召开研讨会。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "虽然并不是那种\x01",
            "大量市民和游客聚集的活动，\x01",
            "但许多来自各个国家的知识分子将会出席。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "至于克洛斯贝尔的参加者，则是以市长为首。\x01",
            "另外，据说ＩＢＣ的总裁以及格里姆伍德先生\x01",
            "也都会参加呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121C")

    label("loc_115C")


    #C0038
    ChrTalk(
        0x8,
        (
            "警备工作自然是由警察来负责，\x01",
            "但那个亚里欧斯·马克莱因这次也会\x01",
            "作为特别增援而参加警备工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "警察局的高层人物虽然心情复杂，\x01",
            "但毕竟牵涉到各国相关人员的安危，\x01",
            "似乎也没办法提出反对呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121C")

    Jump("loc_127C")

    label("loc_1221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_127C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_123E")
    Call(0, 6)
    Jump("loc_127C")

    label("loc_123E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x13)"), scpexpr(EXPR_END)), "loc_1279")
    Call(0, 24)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1274")
    FadeToDark(1000, 0, -1)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    TalkEnd(0x8)
    Return()

    label("loc_1274")

    Jump("loc_127C")

    label("loc_1279")

    Call(0, 6)

    label("loc_127C")

    Return()

    # Function_5_BB2 end

    def Function_6_127D(): pass

    label("Function_6_127D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")

    #C0040
    ChrTalk(
        0x8,
        "啊，是支援科的各位。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "今年的情况果然\x01",
            "比往年都要混乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "支援请求的处理，请加油啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_134A")

    label("loc_12F0")


    #C0043
    ChrTalk(
        0x8,
        (
            "今年的纪念庆典，情况好像\x01",
            "比往年都要混乱呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "各位也要加油完成\x01",
            "支援请求的工作哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_134A")

    Return()

    # Function_6_127D end

    def Function_7_134B(): pass

    label("Function_7_134B")

    Call(0, 8)
    Return()

    # Function_7_134B end

    def Function_8_134F(): pass

    label("Function_8_134F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146F")

    #C0045
    ChrTalk(
        0x9,
        (
            "#1903F纪念庆典今天就是最终日了……\x01",
            "总算是快要撑过去了啊～\x02\x03",

            "#1900F大家也真是\x01",
            "辛苦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#0000F哈哈，芙兰你也辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        (
            "#0203F（不过对我们来说，真正的重头戏\x01",
            "  才刚要开始呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#0100F（算了，我们也不希望把她卷进来，\x01",
            "  就不要多说什么了吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_15A9")

    label("loc_146F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1543")

    #C0049
    ChrTalk(
        0x9,
        (
            "#1905F说起来……赛尔盖警督\x01",
            "也来总部参加会议了哦。\x02\x03",

            "#1900F各位要去见他吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0000F不了，现在就算了。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0300F小芙兰，我们就互相加油，\x01",
            "努力做好最后阶段的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        "#1900F啊，好的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_15A9")

    label("loc_1543")


    #C0053
    ChrTalk(
        0x9,
        (
            "#1900F最终日虽然很忙，\x01",
            "但应该能够努力撑过的。\x02\x03",

            "#1906F哈～不过，还好在\x01",
            "庆典第一天时得到了休假啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A9")

    Jump("loc_1CFD")

    label("loc_15AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_1616")

    #C0054
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位。\x02\x03",

            "委托人哈罗德先生应该\x01",
            "就在出口附近的喷泉前\x01",
            "等着你们呢。\x02\x03",

            "拜托了哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFD")

    label("loc_1616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1624")
    Jump("loc_1CFD")

    label("loc_1624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_170D")
    OP_93(0x9, 0x5A, 0x0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "芙兰正在用通讯器进行通话。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0056
    ChrTalk(
        0x9,
        (
            "#1903F是、是……\x02\x03",

            "#1901F今天的游行从十二点开始，\x01",
            "由市政厅前出发。\x02\x03",

            "之后会经过欢乐街，\x01",
            "在市内巡回一周……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1708")

    #C0057
    ChrTalk(
        0x101,
        (
            "#0000F（好像很忙呢……\x01",
            "  还是不要打扰她了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1708")

    Jump("loc_1CFD")

    label("loc_170D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1918")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1881")

    #C0058
    ChrTalk(
        0x9,
        (
            "#1900F各位，昨天真是\x01",
            "辛苦了～\x02\x03",

            "听说你们以游击士与不良团伙\x01",
            "为对手比赛了一场，相当出风头呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0000F也、也没有啊～……\x01",
            "并不算什么出风头……\x02\x03",

            "#0006F作为警官，那种行为\x01",
            "确实是稍微有些闹过头了，\x01",
            "我们也在反省呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0306F呵，说得也是啊。\x02\x03",

            "我今天都感觉\x01",
            "肌肉有点微痛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0111F那完全是自作自受吧。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "#1909F嘻嘻……\x01",
            "总之真是辛苦啦～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1913")

    label("loc_1881")


    #C0063
    ChrTalk(
        0x9,
        (
            "#1900F说起来，接待的工作\x01",
            "也变得越来越忙碌了呢～\x02\x03",

            "今天的研讨会，再加上\x01",
            "明天的游行活动，来询问\x01",
            "的人还在增加呢。\x02\x03",

            "#1906F呼……\x01",
            "明天也会很忙吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1913")

    Jump("loc_1CFD")

    label("loc_1918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1985")

    #C0064
    ChrTalk(
        0x9,
        (
            "#1900F啊，各位，\x01",
            "旧城区的不良团伙\x01",
            "好像正在港湾区斗殴呢。\x02\x03",

            "虽然很棘手，\x01",
            "但还是拜托你们啦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFD")

    label("loc_1985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1CFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C8A")

    #C0065
    ChrTalk(
        0x9,
        (
            "#1900F各位，真是辛苦了！\x02\x03",

            "#1909F嘿嘿，其实我昨天\x01",
            "申请了休假。\x02\x03",

            "和姐姐一起玩了一天，\x01",
            "真是好久都没玩得这么痛快了～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_1C17")

    #C0066
    ChrTalk(
        0x9,
        (
            "#1900F对了对了，\x01",
            "不是还和罗伊德警官一起去\x01",
            "看了小型演唱会嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0009F哈哈，我也玩得很开心呢，\x01",
            "多谢你们邀请我。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        "#0111F哼～是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0300F噢，那个演唱会啊，\x01",
            "我也去看了呢。\x02\x03",

            "#0309F还和乌尔斯拉医院\x01",
            "的护士妹妹们一起跳舞，\x01",
            "跳得很开心呢。⊥\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3D")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1B3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B63")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1B63")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B89")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1B89")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAF")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_1BAF")

    Sleep(1000)

    #C0070
    ChrTalk(
        0x103,
        (
            "#0211F兰迪前辈，\x01",
            "你真是太得意忘形了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，说不定我们曾经\x01",
            "还在哪里擦肩而过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C82")

    label("loc_1C17")


    #C0072
    ChrTalk(
        0x101,
        (
            "#0000F哈哈，你们似乎玩得很开心啊。\x02\x03",

            "那么，芙兰，\x01",
            "纪念庆典期间也请多关照啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        "#1900F好的，明白了！\x02",
    )

    CloseMessageWindow()

    label("loc_1C82")

    SetScenarioFlags(0xB1, 3)
    Jump("loc_1CFD")

    label("loc_1C8A")


    #C0074
    ChrTalk(
        0x9,
        (
            "#1900F在纪念庆典期间，\x01",
            "杂事真是非常多啊～\x02\x03",

            "我想发给各位的支援请求\x01",
            "应该也会有很多，\x01",
            "但还请各位不要太过勉强哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFD")

    TalkEnd(0x9)
    Return()

    # Function_8_134F end

    def Function_9_1D01(): pass

    label("Function_9_1D01")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D95")
    Jump("loc_1DDF")

    label("loc_1D95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DB5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DDF")

    label("loc_1DB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DD5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DDF")

    label("loc_1DD5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DDF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2C")

    #C0075
    ChrTalk(
        0xFE,
        (
            "#1906F呜呜，精疲力竭了……\x02\x03",

            "#1900F今天有很多市民和游客过来\x01",
            "询问有关游行方面的问题呢……\x02\x03",

            "#1906F现在总算能稍微松一口气了～……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        "#0000F哈哈，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，看来真的是\x01",
            "相当热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#0300F稍微休息一下吧，\x01",
            "让我请你喝瓶果汁如何。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "#1906F呜呜……\x01",
            "谢谢了～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FC5")

    label("loc_1F2C")


    #C0080
    ChrTalk(
        0xFE,
        (
            "#1903F那么……稍微喘口气，\x01",
            "马上就要继续努力工作啦。\x02\x03",

            "#1901F纪念庆典\x01",
            "还有一天才结束呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0000F（这种努力认真的性格，\x01",
            "  姐妹两人真是很像啊……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC5")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_1D01 end

    def Function_10_1FCD(): pass

    label("Function_10_1FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FDB")
    Jump("loc_20F7")

    label("loc_1FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2063")
    TalkBegin(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "闭幕式上的人员配置，\x01",
            "还是强化一下比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "今年的人数比往年都要多，\x01",
            "如果不拿出些干劲，后果恐怕不堪设想。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_20F7")

    label("loc_2063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2071")
    Jump("loc_20F7")

    label("loc_2071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20E6")
    TalkBegin(0xFE)

    #C0084
    ChrTalk(
        0xFE,
        (
            "唉，老婆婆……\x01",
            "您有没有在好好反省啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        "……算了，反正看上去也不像在反省啊。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_20E9")

    label("loc_20E6")

    Call(0, 26)

    label("loc_20E9")

    Jump("loc_20F7")

    label("loc_20EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20F7")

    label("loc_20F7")

    Return()

    # Function_10_1FCD end

    def Function_11_20F8(): pass

    label("Function_11_20F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_21E4")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2196")

    #C0086
    ChrTalk(
        0xFE,
        "哎呀，是你们啊～\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "警督他们正在参加\x01",
            "闭幕式警备工作的安排会议哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "真是的，真希望他们能分出一点人手来\x01",
            "帮帮我这边啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_21DC")

    label("loc_2196")


    #C0089
    ChrTalk(
        0xFE,
        (
            "呼，反正像这种混乱的状态，\x01",
            "应该也就到今天为止了吧～\x01",
            "一起加油吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DC")

    TalkEnd(0xFE)
    Jump("loc_23CD")

    label("loc_21E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_21F2")
    Jump("loc_23CD")

    label("loc_21F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2200")
    Jump("loc_23CD")

    label("loc_2200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_23C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23BC")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22A9")
    Jump("loc_22F3")

    label("loc_22A9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22C9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22F3")

    label("loc_22C9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22E9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_22F3")

    label("loc_22E9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_22F3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0090
    ChrTalk(
        0xFE,
        (
            "嗯～……笔录这种事情，\x01",
            "不管做多少次都无法习惯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "如果只是失足少年，\x01",
            "我倒是可以自己应付～\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#0006F（为什么身为警察还会怕给人做笔录啊……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_23BF")

    label("loc_23BC")

    Call(0, 26)

    label("loc_23BF")

    Jump("loc_23CD")

    label("loc_23C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_23CD")

    label("loc_23CD")

    Return()

    # Function_11_20F8 end

    def Function_12_23CE(): pass

    label("Function_12_23CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_23DF")
    Jump("loc_24A6")

    label("loc_23DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_243A")

    #C0093
    ChrTalk(
        0xFE,
        "今年的人数超出预料啊。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "简直就像克洛斯贝尔\x01",
            "的人口增加到了两倍一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A6")

    label("loc_243A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2448")
    Jump("loc_24A6")

    label("loc_2448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2456")
    Jump("loc_24A6")

    label("loc_2456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_24A6")

    #C0095
    ChrTalk(
        0xFE,
        "……嫌疑人带到！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "真是的，这些家伙，\x01",
            "在庆典期间还不安分一点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24A6")

    TalkEnd(0xFE)
    Return()

    # Function_12_23CE end

    def Function_13_24AA(): pass

    label("Function_13_24AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_256D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2519")

    #C0097
    ChrTalk(
        0xFE,
        (
            "啊～……今天外面\x01",
            "也很热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "呵，反正我只是\x01",
            "来买罐咖啡的。\x01",
            "不用在意～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2568")

    label("loc_2519")


    #C0099
    ChrTalk(
        0xFE,
        "其实现在还正在开会呢……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "哈，总之就快点把我\x01",
            "偷偷跑出来的事情忘掉吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2568")

    Jump("loc_273D")

    label("loc_256D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_25BE")

    #C0101
    ChrTalk(
        0xFE,
        (
            "嗯～那么，\x01",
            "二科也会帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "公共安全科已经竭尽全力了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_273D")

    label("loc_25BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_25CC")
    Jump("loc_273D")

    label("loc_25CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_26A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265F")

    #C0103
    ChrTalk(
        0xFE,
        (
            "……多诺邦他们刚才\x01",
            "押着好几个人过去了～\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "什么～那些人是怎么回事……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "大家的神经是不是有些\x01",
            "紧绷过头了啊～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_269C")

    label("loc_265F")


    #C0106
    ChrTalk(
        0xFE,
        (
            "啊～就算现在是纪念庆典，\x01",
            "但大家的神经也都绷得太紧了吧～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_269C")

    Jump("loc_273D")

    label("loc_26A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_273D")

    #C0107
    ChrTalk(
        0xFE,
        (
            "嗯～纪念庆典期间\x01",
            "果然是异常忙碌啊……\x01",
            "连悠闲品尝咖啡的时间都没有～\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "……啊～总之，今天真是帮大忙了～\x01",
            "以后也请多多关照了，特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273D")

    TalkEnd(0xFE)
    Return()

    # Function_13_24AA end

    def Function_14_2741(): pass

    label("Function_14_2741")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2752")
    Jump("loc_2819")

    label("loc_2752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_279D")

    #C0109
    ChrTalk(
        0xFE,
        "游行好像结束了呢。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "我也返回港湾区进行\x01",
            "重点警备吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2819")

    label("loc_279D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2819")

    #C0111
    ChrTalk(
        0xFE,
        (
            "达德利警官\x01",
            "出差去帝国了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "在这种忙碌不堪的时期，\x01",
            "竟然莫名其妙地让他去短期出差……\x01",
            "上层到底在想些什么啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2819")

    TalkEnd(0xFE)
    Return()

    # Function_14_2741 end

    def Function_15_281D(): pass

    label("Function_15_281D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286D")

    #C0113
    ChrTalk(
        0xFE,
        (
            "呜喔喔……\x01",
            "我什么都不知道！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "不知道不知道不知道！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_28BA")

    label("loc_286D")


    #C0115
    ChrTalk(
        0xFE,
        (
            "……没想到警官竟然会去\x01",
            "那种鬼地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "既然如此，也只有沉默到底了！\x02",
    )

    CloseMessageWindow()

    label("loc_28BA")

    TalkEnd(0xFE)
    Return()

    # Function_15_281D end

    def Function_16_28BE(): pass

    label("Function_16_28BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_297C")
    OP_4B(0xC, 0xFF)

    #C0117
    ChrTalk(
        0xFE,
        (
            "雷蒙德警官，\x01",
            "笔录室都已经满员了！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        "怎么办啊！？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xC,
        (
            "好～要是真的不够用了，\x01",
            "就把会议室也用上吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xC,
        (
            "不过，比起那个，重点还是巡逻啊～\x01",
            "向站前街道出发～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_2A4D")

    label("loc_297C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0C")

    #C0121
    ChrTalk(
        0xFE,
        (
            "从港湾区和欢乐街\x01",
            "那里派来了支援人手，\x01",
            "这样就能强化巡逻的力度了。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "哎呀呀……稍微喘口气，\x01",
            "就又要赶快出发啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2A4D")

    label("loc_2A0C")


    #C0123
    ChrTalk(
        0xFE,
        (
            "在纪念庆典时可是没空休息的啊，\x01",
            "必须要赶快返回到巡逻队伍……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4D")

    TalkEnd(0xFE)
    Return()

    # Function_16_28BE end

    def Function_17_2A51(): pass

    label("Function_17_2A51")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE5")
    Jump("loc_2B2F")

    label("loc_2AE5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B05")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B2F")

    label("loc_2B05")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B25")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B2F")

    label("loc_2B25")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B2F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1E")
    OP_82(0x0, 0x64, 0xBB8, 0xC8)
    OP_4B(0xB, 0xFF)

    #C0124
    ChrTalk(
        0xFE,
        (
            "#5S你、你们……\x01",
            "竟然敢再次出现\x01",
            "在我的面前！？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "#5S明年的纪念庆典\x01",
            "我还会来的！！\x01",
            "给我好好记住！！\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xB,
        (
            "……喂，老婆婆，面向这边啦。\x01",
            "我们还在做笔录啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x1, 2)
    Jump("loc_2C6A")

    label("loc_2C1E")

    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0127
    ChrTalk(
        0xFE,
        (
            "#5S明年的纪念庆典\x01",
            "我还会来的！！\x01",
            "你们给我好好记住！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_17_2A51 end

    def Function_18_2C72(): pass

    label("Function_18_2C72")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2CFE")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "「～　笔录室·使用中　～\x01",
            "　　现在正在进行笔录。\x01",
            "　　　　　　公共安全科」\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_2D07")

    label("loc_2CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2D07")

    label("loc_2D07")

    EventEnd(0x1)
    Return()

    # Function_18_2C72 end

    def Function_19_2D0A(): pass

    label("Function_19_2D0A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D9E")
    Jump("loc_2DE8")

    label("loc_2D9E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DBE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DE8")

    label("loc_2DBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DDE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DE8")

    label("loc_2DDE")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2DE8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E1F")
    Call(0, 20)
    Jump("loc_2EA1")

    label("loc_2E1F")


    #C0129
    ChrTalk(
        0xFE,
        (
            "#1004F（点烟）……\x01",
            "外面的游行\x01",
            "好像刚刚结束了呢。\x02\x03",

            "#1000F哎呀呀，今年的人流量\x01",
            "真是多得让人头疼啊。\x01",
            "想安安静静地看本书都没空。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_19_2D0A end

    def Function_20_2EA9(): pass

    label("Function_20_2EA9")


    #C0130
    ChrTalk(
        0xFE,
        (
            "#1005F噢，是你们几个啊。\x02\x03",

            "#1006F我本来在楼顶上偷懒，\x01",
            "结果接到了公务……\x02\x03",

            "他们还说什么『已经没有其他\x01",
            "持有搜查官资格的人员了』。\x01",
            "真是的，太麻烦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#0003F科长，请认真工作吧。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x104,
        (
            "#0306F我们几个可是忙得\x01",
            "都要累死了，你却……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#0201F有点难以置信呢。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "#1000F……别生气嘛。\x01",
            "来，这个就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑市医生格伦　８卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0136
    ChrTalk(
        0xFE,
        (
            "#1006F本来是打算\x01",
            "在今天之内读完的，\x01",
            "但无奈工作缠身啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#0100F呼，偷懒原来是\x01",
            "为了读这个啊……\x02",
        )
    )

    CloseMessageWindow()
    AddItemNumber('黑市医生格伦　８卷', 1)
    SetScenarioFlags(0x9C, 7)
    Return()

    # Function_20_2EA9 end

    def Function_21_3091(): pass

    label("Function_21_3091")

    TalkBegin(0xFE)
    OP_63(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0138
    ChrTalk(
        0xFE,
        (
            "竟、竟敢\x01",
            "瞧不起我们\x01",
            "『暗黑帝王』吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x12,
        (
            "#1006F……啊，那个我知道啦，\x01",
            "我在问你的名字啊，名字。\x02\x03",

            "#1000F喂，快点说啊，\x01",
            "你这白痴。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3091 end

    def Function_22_3132(): pass

    label("Function_22_3132")

    TalkBegin(0xFE)

    #C0140
    ChrTalk(
        0xFE,
        (
            "今年的人数之多超出预料，\x01",
            "到处都有事件发生，已经应付不完了。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "而且麻烦事恐怕\x01",
            "还会接连不断呢……\x01",
            "罗伊德，你们也要多加注意啊！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3132 end

    def Function_23_31BE(): pass

    label("Function_23_31BE")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(-140, 1540, 13420, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21380, 0)
    SetChrPos(0x101, 400, 0, 13450, 0)
    SetChrPos(0x102, -600, 0, 13200, 0)
    SetChrPos(0x103, 400, 0, 11950, 0)
    SetChrPos(0x104, -600, 0, 11700, 0)
    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0142
    ChrTalk(
        0x8,
        "#5P啊呀，是支援科的各位啊。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#5P……呼，今年果然比往年\x01",
            "都要混乱得多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#12P#0000F瑞贝卡小姐好像\x01",
            "也很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#6P#0104F呵呵，在纪念庆典期间，\x01",
            "警察局也有很多的工作要做啊。\x02\x03",

            "#0100F其实我们是为了公共安全科\x01",
            "所发出的支援请求而来的……\x01",
            "可以请您联系一下负责人员吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        "#5P哦哦，是『取缔违章停车』那件事吧。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "#5P大家都分散到各处工作了……\x01",
            "是现在就联系他们呢，还是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33CB():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33CB)
    Sleep(100)

    def lambda_33DB():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33DB)

    def lambda_33E8():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_33E8)

    def lambda_33F5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33F5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0148
    ChrTalk(
        0x101,
        (
            "#11P#0000F那么……\x01",
            "……就拜托她立刻去进行联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x103,
        "#12P#0200F说得也是呢。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        "#12P#0300F嗯，立刻着手处理吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3489():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3489)

    def lambda_3496():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3496)

    def lambda_34A3():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34A3)

    def lambda_34B0():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34B0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0151
    ChrTalk(
        0x101,
        "#12P#0000F那么，就麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "#5P明白了，\x01",
            "我立刻就联络他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#5P请各位在会议室里\x01",
            "稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(-62770, 2140, 17220, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22390, 0)
    OP_68(-62770, 1540, 17220, 2000)
    SetChrPos(0x101, -60500, 150, 20150, 180)
    SetChrPos(0x102, -64000, 150, 20150, 180)
    SetChrPos(0x103, -60500, 150, 15850, 0)
    SetChrPos(0x104, -64000, 150, 15850, 0)
    SetChrPos(0xE, -64599, 40, 8400, 0)
    SetChrPos(0x17, -65400, 40, 8250, 0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    OP_4B(0xE, 0xFF)
    OP_4B(0x17, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0154
    ChrTalk(
        0x101,
        (
            "#5P#0003F果然……很忙呢，\x01",
            "这么久还不来。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#6P#0300F算啦，从庆典如今的状况来看，\x01",
            "这也是没有办法的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(103, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x1)
    OP_68(-63070, 1540, 14720, 0)
    MoveCamera(37, 13, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23450, 0)
    OP_68(-63070, 1540, 14720, 1000)

    def lambda_3736():
        OP_97(0xE, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3736)

    def lambda_3750():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3750)
    Sleep(50)

    def lambda_3764():
        OP_97(0x17, 0x0, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3764)

    def lambda_377E():
        OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_377E)
    WaitChrThread(0xE, 1)
    WaitChrThread(0xE, 2)
    OP_93(0xE, 0x2D, 0x1F4)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x17, 2)
    OP_93(0x17, 0x2D, 0x1F4)
    OP_0D()

    #C0156
    ChrTalk(
        0xE,
        (
            "#12P噢～抱歉抱歉，\x01",
            "让大家久等了……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x17,
        "#6P真不好意思，来晚了……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#11P#0000F哪里，二位辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-61850, 1500, 18250, 0)
    MoveCamera(52, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24440, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x2)
    SetChrSubChip(0x104, 0x2)
    SetChrPos(0xE, -57450, 0, 15000, 0)
    SetChrPos(0x17, -57200, 0, 16400, 0)

    def lambda_387E():
        OP_97(0xE, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_387E)
    Sleep(50)

    def lambda_389B():
        OP_97(0x17, 0x0, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_389B)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x10E, 0x1F4)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -59750, 0, 19900, 135)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, -63250, 0, 19900, 90)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -59750, 0, 16100, 45)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x104, -63250, 0, 16100, 90)
    ClearChrFlags(0x104, 0x4)
    Sound(820, 0, 100, 0)
    OP_0D()

    #C0159
    ChrTalk(
        0xE,
        (
            "#11P啊～我是公共安全科的科长，\x01",
            "乔里基。\x01",
            "请多指教。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x17,
        (
            "#5P我是同属公共安全科的\x01",
            "凯特巡警。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x17,
        (
            "#5P特别任务支援科的各位，\x01",
            "感谢你们的协助！\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#6P#0005F（是吗，看来我们也有必要\x01",
            "  像这样进行正式的问候呢……）\x02\x03",

            "#0001F──特别任务支援科，\x01",
            "班宁斯搜查官等四名警员。\x02\x03",

            "希望能立即确认\x01",
            "任务的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xE,
        "#11P好～我马上就来说明～\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        (
            "#11P……对了，从现在起就不必拘束了～\x01",
            "随便放松就好～\x02",
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

    #C0165
    ChrTalk(
        0x17,
        (
            "#5P……不好意思啊，我们科长\x01",
            "稍微有些自我中心。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "#11P大致内容在支援请求中已经交代过了～\x01",
            "……就是希望你们能帮忙取缔\x01",
            "郊外的违章停车。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "#11P不过呢，在纪念庆典期间，\x01",
            "每个科的人手都很不足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xE,
        (
            "#11P只要记下车牌号，\x01",
            "然后把警告标志\x01",
            "贴上去就可以了～\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#6P#0005F那个，只要这样就可以了吗？\x01",
            "不用把车拖走之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xE,
        (
            "#11P不，不需要～\x01",
            "反正也不能处以罚款以上的惩罚啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x17,
        (
            "#5P而且其中也有很多帝国和共和国的人，\x01",
            "所以不能太过严厉……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x17,
        (
            "#5P相比之下，我倒觉得\x01",
            "还是准停车辆比较麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x103,
        "#12P#0200F准停车辆……吗？\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x17,
        (
            "#5P嗯，其实停泊在那里的车辆\x01",
            "并不全是违章停车。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x17,
        (
            "#5P也有一些人事先就得到了停车许可，\x01",
            "所以请务必注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#12P#0300F也就是说，只要找出那些\x01",
            "没有得到停车许可的车辆就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        "#6P#0100F原来如此，大致流程我们已经了解了。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯，西出口和东出口\x01",
            "应该各停着四五\x01",
            "辆车……\x02\x03",

            "#0000F两边都去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        "#12P#0200F也是呢。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xE,
        (
            "#11P好～那么，\x01",
            "把准停车辆的车牌清单给你们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F06():
        OP_97(0x101, 0x2EE, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F06)

    def lambda_3F20():
        OP_95(0xE, -58490, 30, 19160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3F20)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x87, 0x1F4)
    WaitChrThread(0xE, 1)
    Sleep(1000)
    OP_96(0xE, 0xFFFF1F96, 0x0, 0x4844, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0181
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2DB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2DB, 1)

    #C0182
    ChrTalk(
        0x17,
        (
            "#5P然后，这个就是要贴在\x01",
            "车辆上面的警告标志。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x17,
        (
            "#5P我们把这个称作\x01",
            "『违章停车取缔套件』！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4008():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4008)
    OP_96(0x17, 0xFFFF1CA8, 0x1E, 0x4DBC, 0x7D0, 0x0)
    Sleep(1000)
    OP_96(0x17, 0xFFFF2090, 0x0, 0x4DBC, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '迷你沙袋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('迷你沙袋', 1)

    #C0185
    ChrTalk(
        0x101,
        "#6P#0000F嗯，那我们就收下了。\x02",
    )

    CloseMessageWindow()

    def lambda_40AB():
        OP_93(0xE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_40AB)

    def lambda_40B8():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40B8)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x101, 1)

    #C0186
    ChrTalk(
        0xE,
        (
            "#11P工作完成之后，\x01",
            "就再来总部一趟，和瑞贝卡联络吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "#11P我和凯特也还要\x01",
            "到处巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#6P#0100F明白了，想要报告时就去\x01",
            "找接待处的瑞贝卡小姐，没错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x104,
        (
            "#12P#0300F那么，我们这就\x01",
            "前往城市的出口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x103,
        "#12P#0200F嗯，出发吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【违章停车的取缔】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_4C(0xE, 0xFF)
    OP_4C(0x17, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_49()
    OP_68(-65099, 1500, 14250, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -65099, 0, 14250, 180)
    SetChrPos(0x1, -65099, 0, 14250, 180)
    SetChrPos(0x2, -65099, 0, 14250, 180)
    SetChrPos(0x3, -65099, 0, 14250, 180)
    OP_29(0x17, 0x1, 0x0)
    SetScenarioFlags(0x0, 1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_23_31BE end

    def Function_24_42C4(): pass

    label("Function_24_42C4")


    #C0192
    ChrTalk(
        0x8,
        (
            "各位，违章停车的取缔工作\x01",
            "进行得怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        (
            "如果要报告的话，我现在就\x01",
            "联络公共安全科的各位了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【进行报告】\x01",      # 0
            "【不报告】\x01",        # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E5")

    #C0194
    ChrTalk(
        0x101,
        (
            "#0000F好的，那就\x01",
            "麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "明白了。\x01",
            "不好意思哦，\x01",
            "还要请你们稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        (
            "#0100F嗯，请不用\x01",
            "在意我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4437")

    label("loc_43E5")


    #C0197
    ChrTalk(
        0x8,
        (
            "工作完成以后，\x01",
            "就请与我联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "我会通知公共安全科的各位\x01",
            "前来听取报告的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4437")

    Return()

    # Function_24_42C4 end

    def Function_25_4438(): pass

    label("Function_25_4438")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xE, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_68(-57380, 1600, 17520, 0)
    MoveCamera(40, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25000, 0)
    OP_68(-57380, 900, 17520, 3000)
    SetChrPos(0x101, -57500, 0, 17000, 0)
    SetChrPos(0x102, -56750, 0, 16500, 0)
    SetChrPos(0x103, -58250, 0, 15500, 0)
    SetChrPos(0x104, -57500, 0, 15000, 0)
    SetChrPos(0xE, -57500, 0, 19000, 180)
    SetChrPos(0x17, -58500, 0, 19250, 180)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0199
    ChrTalk(
        0x101,
        (
            "#12P#0003F……以上就是报告内容。\x02\x03",

            "#0000F违章停车的车牌号\x01",
            "全都记录在这里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_98(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)

    #C0200
    ChrTalk(
        0xE,
        "#5P嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xE,
        (
            "#5P噢～很好，\x01",
            "看来是已经调查完毕了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4716")
    OP_2C(0x17, 0x2)
    OP_29(0x17, 0x1, 0x16)

    #C0202
    ChrTalk(
        0x102,
        (
            "#12P#0100F嗯，我想应该已经\x01",
            "调查完毕了，不会有差错。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x103,
        (
            "#6P#0200F车主中有很多帝国人\x01",
            "和共和国人，\x01",
            "让人多少有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xE,
        "#5P竟然做得这么漂亮啊……\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xE,
        (
            "#5P哎呀～其实就算适当敷衍一下\x01",
            "也是可以的，\x01",
            "我们就经常那么干哦～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47FD")

    label("loc_4716")

    OP_29(0x17, 0x1, 0x15)

    #C0206
    ChrTalk(
        0xE,
        (
            "#5P顺便问一下……没有出现搞错\x01",
            "车辆之类的情况吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0207
    ChrTalk(
        0x101,
        (
            "#12P#0005F哎……那个。\x02\x03",

            "#0006F（完成得太过匆忙，\x01",
            "  还是有点不安啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xE,
        "#5P嗯……算了，无所谓。\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xE,
        (
            "#5P这种工作，我们也是\x01",
            "经常敷衍了事的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47FD")

    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    TurnDirection(0x17, 0xE, 500)
    Sleep(500)

    #C0210
    ChrTalk(
        0x17,
        (
            "#5P科长～我们可都是\x01",
            "一直很认真的啊！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x17, 500)

    #C0211
    ChrTalk(
        0xE,
        "#11P噢～抱歉抱歉～\x02",
    )

    CloseMessageWindow()

    def lambda_48CD():
        OP_93(0xE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_48CD)

    def lambda_48DA():
        OP_93(0x17, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_48DA)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x17, 1)

    #C0212
    ChrTalk(
        0x17,
        (
            "#5P不过……这样一来，\x01",
            "总算是解决了一个工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x17,
        (
            "#5P多谢各位了，\x01",
            "这样我们或许也能轻松一点了！\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        (
            "#5P噢噢，由衷地表示感谢～\x01",
            "困难的时候果然还是要找支援科啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x104,
        (
            "#12P#0300F哈哈，在总部中我们也\x01",
            "都被当作什么工作都接的杂工啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x17, 0x1, 0x14)"), scpexpr(EXPR_END)), "loc_4E58")
    OP_2C(0x17, 0x2)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    #C0216
    ChrTalk(
        0x102,
        (
            "#12P#0105F说起来……\x01",
            "罗伊德，那件事要说一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x101, 0x102, 500)
    Sleep(500)

    #C0217
    ChrTalk(
        0x101,
        "#6P#0005F啊，对了……\x02",
    )

    CloseMessageWindow()

    def lambda_4A72():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A72)

    def lambda_4A7F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A7F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    #C0218
    ChrTalk(
        0x101,
        "#12P#0001F那个，其实……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xE,
        "#5P嗯？怎么了～\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#12P#0001F是关于得到过许可\x01",
            "的车辆编号……\x02\x03",

            "西出口和东出口似乎\x01",
            "有牌号相同的\x01",
            "车辆呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x101,
        (
            "#12P#0001F车牌号是……那个……\x01",
            "『ＣＬ　１１０１』吧，\x01",
            "应该没错。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0222
    ChrTalk(
        0x17,
        (
            "#5P怎、怎么会……\x01",
            "莫非有人伪造车牌号吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x17)

    #C0223
    ChrTalk(
        0xE,
        (
            "#5P啊～……\x01",
            "……多半就是如此了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x17, 0xE, 500)
    Sleep(500)

    #C0224
    ChrTalk(
        0xE,
        (
            "#5P如果想取得停车许可，\x01",
            "是需要上缴一定费用的……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xE,
        (
            "#5P而且费用是按日计算的，\x01",
            "如果在纪念庆典期间一直停放，\x01",
            "那可是一笔不小的数目呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xE,
        (
            "#5P大概是某个吝惜申请费的人\x01",
            "交了一份钱，却停了两辆车吧。\x02",
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
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x104,
        (
            "#12P#0306F好、好一个小气的家伙啊……\x01",
            "算啦，反正也不是什么\x01",
            "重大犯罪行为。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x103,
        "#6P#0200F也是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x17, 500)

    #C0229
    ChrTalk(
        0xE,
        (
            "#5P嗯，凯特，\x01",
            "稍后再去调查一下吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x17,
        (
            "#5P啊，是！\x01",
            "明白了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E58")


    #C0231
    ChrTalk(
        0x101,
        (
            "#12P#0001F那么……\x01",
            "特别任务支援科，\x01",
            "就此告辞了。\x02\x03",

            "#0000F如果今后还有什么困难，\x01",
            "请不用客气，随时联络我们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4ECC():
        OP_93(0xE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4ECC)

    def lambda_4ED9():
        OP_93(0x17, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4ED9)
    WaitChrThread(0xE, 1)
    WaitChrThread(0x17, 1)

    #C0232
    ChrTalk(
        0xE,
        "#5P噢～那到时候就麻烦你们啦。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x17,
        (
            "#5P虽然在纪念庆典期间，大家都很忙……\x01",
            "不过，就照这种势头继续努力吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0234
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【违章停车的取缔】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SetChrPos(0x0, -25580, 0, 11350, 180)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    OP_29(0x17, 0x4, 0x10)
    SetScenarioFlags(0x0, 2)
    EventEnd(0x5)
    Return()

    # Function_25_4438 end

    def Function_26_4FD3(): pass

    label("Function_26_4FD3")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-59660, 1500, 14140, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25010, 0)
    SetChrPos(0xB, -57730, 0, 16309, 225)
    SetChrPos(0xC, -57730, 0, 14480, 270)
    SetChrPos(0x101, -60000, 30, 14500, 45)
    SetChrPos(0x102, -60000, 0, 13000, 45)
    SetChrPos(0x103, -61500, 0, 14500, 45)
    SetChrPos(0x104, -61500, 0, 13000, 45)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0235
    ChrTalk(
        0x101,
        (
            "#6P#0000F多诺邦警督，您辛苦了。\x02\x03",

            "特别任务支援科的四名成员，\x01",
            "收到警督的请求，\x01",
            "前来拜访。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xB,
        (
            "#5P嗯，辛苦了。\x01",
            "你们来得正好。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xC,
        "#11P辛苦啦～\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#12P#0105F那么……\x01",
            "请问委托的具体内容\x01",
            "究竟是什么呢？\x02\x03",

            "#0101F从文字介绍上看，\x01",
            "似乎是紧急度很高的\x01",
            "案件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "#5P嗯，那现在就来开个\x01",
            "简单的临时会议吧。\x01",
            "请各自就坐。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x103,
        "#6P#0200F了解。\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x104,
        (
            "#6P#0309F嘿，好像一下子就有了\x01",
            "警察办案的感觉了啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-60460, 1900, 19460, 0)
    MoveCamera(48, 13, 0, 0)
    OP_6E(-3450, 0)
    SetCameraDistance(36130, 0)
    OP_68(-60460, 900, 19460, 3000)
    SetChrPos(0xB, -58000, 0, 18000, 270)
    SetChrPos(0xC, -57360, 0, 19780, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -60550, 150, 15950, 0)
    SetChrPos(0x102, -60550, 150, 20000, 180)
    SetChrPos(0x103, -64050, 150, 20000, 180)
    SetChrPos(0x104, -64050, 150, 15950, 0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0xB,
        (
            "#11P那么……言归正传，今天\x01",
            "把你们叫来不为其它。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "#11P就是想请你们协助我们\x01",
            "找出在克洛斯贝尔地区从事违法活动\x01",
            "的『假货贩子』，并将其捕获。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x101,
        "#12P#0005F假货贩子……吗？\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x103,
        (
            "#6P#0203F就是仿制那些名牌服饰品和导力器……\x02\x03",

            "并使用与真品酷似的商标，\x01",
            "然后将其卖给顾客们的\x01",
            "黑心商人吧。\x02\x03",

            "#0200F根据自治州的法律，这种行为属于轻度犯罪。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        (
            "#11P了、了解得真详细呢，\x01",
            "大概就是这么一回事。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "#11P每年纪念庆典期间，\x01",
            "都会有很多这样的假货贩子，伪装成\x01",
            "普通的游客，潜入克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xC,
        (
            "#11P像乌尔努公司制造的高级手表，\x01",
            "斯托雷加公司的绝版经典产品，\x01",
            "还有各种七耀石制的小物件……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "#11P他们将这些东西贩卖给\x01",
            "缺乏鉴别知识的顾客，\x01",
            "从而谋取不正当的利益。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#6P#0301F这根本就是靠行骗来赚钱啊，\x01",
            "真是些让人不爽的家伙。\x02\x03",

            "#0303F总而言之，就是让我们\x01",
            "帮忙抓捕那些家伙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xB,
        "#11P嗯，就是这样。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xB,
        (
            "#11P说起来，我们也真是没用……\x01",
            "每年都会接到好几件这样的报案。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xB,
        (
            "#11P而且，这种假货商人的存在也\x01",
            "关系到制造商与经销商的信用，\x01",
            "是个很大的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xB,
        (
            "#11P身为警察，我们今年一定要\x01",
            "阻止那些家伙潜入克洛斯贝尔，\x01",
            "并让市民们恢复对我们的信赖。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#6P#0003F原来如此……\x01",
            "事情的大致状况我们已经了解了。\x02\x03",

            "#0001F我们特别任务支援科也一定会\x01",
            "竭尽全力来协助各位的。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xB,
        "#11P嗯，非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        (
            "#6P#0105F不过……\x01",
            "我们该怎么做才好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xB,
        (
            "#11P他们的潜入路线，\x01",
            "我想共有克洛斯贝尔车站、空港，\x01",
            "以及唐古拉姆门这三条。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xB,
        (
            "#11P车站和空港就交给我们来控制，\x01",
            "希望你们能负责唐古拉姆门\x01",
            "那边的警戒工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "#11P二科也是人手不足啊……\x01",
            "没办法顾及到克洛斯贝尔\x01",
            "的郊外地区。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xC,
        (
            "#11P而你们好像和警备队\x01",
            "的索妮亚副司令\x01",
            "也认识吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        (
            "#11P既然是堵截作战，\x01",
            "那么就需要请求现场人员的合作，\x01",
            "所以，我想你们应该很适合担任此次任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x102,
        (
            "#6P#0103F原来如此……确实，\x01",
            "比起其它部门的警官，我们似乎\x01",
            "更容易与那边展开合作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        (
            "#6P#0306F哎呀呀，如果可能的话，\x01",
            "我还是想尽量不要和她见面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        "#11P……好，该交代的都说完了。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xB,
        (
            "#11P我们现在就打算\x01",
            "前往车站和空港埋伏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xB,
        (
            "#11P你们也赶快去唐古拉姆门，\x01",
            "与那边会合，进行警备吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        (
            "#6P#0001F明白了……\x01",
            "我们立刻就向唐古拉姆门\x01",
            "出发。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xB,
        "#11P拜托你们了。\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        "#11P那么，再见啦。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 27)
    BeginChrThread(0xC, 3, 0, 28)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    Fade(1000)
    OP_68(-61410, 900, 18100, 0)
    MoveCamera(61, 17, 0, 0)
    SetChrSubChip(0x101, 0x1)
    SetChrSubChip(0x102, 0x2)
    SetChrSubChip(0x103, 0x1)
    SetChrSubChip(0x104, 0x2)
    OP_0D()

    #C0271
    ChrTalk(
        0x101,
        (
            "#11P#0000F好，那么……\x01",
            "我们这就去唐古拉姆门吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x103,
        (
            "#6P#0200F必须要将事情告知索妮亚\x01",
            "副司令，然后请求她的协助呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【揭发假货贩子】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-61760, 1530, 15420, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x0, -61760, 30, 15420, 180)
    SetChrPos(0x1, -61760, 30, 15420, 180)
    SetChrPos(0x2, -61760, 30, 15420, 180)
    SetChrPos(0x3, -61760, 30, 15420, 180)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
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
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_29(0x1B, 0x1, 0x1)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_26_4FD3 end

    def Function_27_5CC0(): pass

    label("Function_27_5CC0")

    OP_68(-64370, 900, 15160, 6000)
    MoveCamera(59, 17, 0, 6000)

    def lambda_5CE1():
        OP_95(0xFE, -58000, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5CE1)
    WaitChrThread(0xB, 1)

    def lambda_5CFF():
        OP_95(0xFE, -65200, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5CFF)
    WaitChrThread(0xB, 1)
    Sound(103, 0, 100, 0)

    def lambda_5D23():
        OP_95(0xFE, -65200, 0, 8300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5D23)

    def lambda_5D3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5D3D)
    WaitChrThread(0xB, 1)
    Sound(104, 0, 100, 0)
    Return()

    # Function_27_5CC0 end

    def Function_28_5D54(): pass

    label("Function_28_5D54")

    Sleep(500)

    def lambda_5D5C():
        OP_95(0xFE, -57360, 0, 13000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D5C)
    WaitChrThread(0xC, 1)

    def lambda_5D7A():
        OP_95(0xFE, -65200, 0, 13100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D7A)
    WaitChrThread(0xC, 1)

    def lambda_5D98():
        OP_95(0xFE, -65200, 0, 9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5D98)

    def lambda_5DB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5DB2)
    WaitChrThread(0xC, 1)
    Return()

    # Function_28_5D54 end

    def Function_29_5DC3(): pass

    label("Function_29_5DC3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    ClearMapObjFlags(0x1, 0x10)
    LoadChrToIndex("chr/ch07300.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03400.itp")
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    OP_68(-123940, 2500, 16390, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22600, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -35500, 0, 16000, 0)
    SetChrPos(0x102, -34000, 0, 16000, 0)
    SetChrPos(0x103, -35500, 0, 14500, 0)
    SetChrPos(0x104, -34000, 0, 14500, 0)
    SetChrPos(0x14, -34750, 0, 13000, 0)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -34750, 0, 17500, 180)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x15, 0x80)
    Sleep(500)
    OP_68(-123940, 1500, 16390, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x1)

    #C0274
    ChrTalk(
        0x16,
        (
            "#6P那个～……\x01",
            "能不能请您把名字告诉我？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x15,
        (
            "#11P……哼，我的名字怎么会告诉\x01",
            "你这种乳臭未干的小鬼。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x16,
        "#6P乳、乳臭未干的小鬼……\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x16,
        (
            "#6P我说啊～……\x01",
            "老婆婆，您难道还不明白\x01",
            "自己都干了些什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x16,
        (
            "#6P您的同伙们已经\x01",
            "全都被逮捕了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x16,
        "#6P请放弃抵抗，老老实实地配合我们吧～\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0280
    ChrTalk(
        0x15,
        (
            "#11P#5S吵～吵～吵～吵～吵死人了！\x01",
            "而且你怎么那么不懂事……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0281
    ChrTalk(
        0x15,
        (
            "#11P#5S和女士谈话时，至少也该\x01",
            "倒杯茶来吧？这可是最基本的礼仪！\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x16,
        (
            "#6P唔、唔唔～……\x01",
            "稍后就会拿来的……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-35320, 1500, 15470, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23600, 0)
    SetCameraDistance(22600, 2000)
    FadeToBright(500, 0)
    OP_0D()

    #C0283
    ChrTalk(
        0x101,
        (
            "#6P#0006F那个……\x01",
            "雷蒙德警官\x01",
            "一个人没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "#5P虽然对方确实很难对付……\x01",
            "但不要紧，用不着担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xB,
        (
            "#5P这里毕竟是警察局总部，\x01",
            "她是绝对逃不出去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        (
            "#11P#0106F嗯～……如果是那个婆婆，\x01",
            "好像还真有可能凭蛮力硬逃出去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x103,
        "#12P#0203F……同感。\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xB,
        (
            "#5P话说回来……\x01",
            "那位美人是什么人啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_624C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_624C)
    Sleep(150)

    def lambda_625C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_625C)
    Sleep(70)

    def lambda_626C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_626C)
    Sleep(150)

    def lambda_627C():
        TurnDirection(0xFE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_627C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0289
    ChrTalk(
        0x104,
        (
            "#11P#0305F噢噢，不说都忘了，\x01",
            "我还没问呢！\x02\x03",

            "#0300F姐姐，您的名字和职业是？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    SetChrName("黑发女性")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            "#12P……雾香·楼兰。\x02\x03",

            "在共和国的演艺界从事\x01",
            "制作人的工作。\x02\x03",

            "来这里的目的是……\x01",
            "呵，可以说是随便过来转转吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0291
    ChrTalk(
        0x104,
        (
            "#11P#0304F雾香小姐啊……真是个好听的名字！\x02\x03",

            "#0309F而且，还从事演艺界制作人\x01",
            "这么棒的工作……真不错啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#6P#0000F多诺邦警督，\x01",
            "我们是在她的协助之下，\x01",
            "才顺利将嫌疑人抓捕的。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xB,
        "#5P嗯……原来如此啊。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xB,
        (
            "#5P……之前的态度真是失礼了。\x01",
            "很抱歉，感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xB,
        (
            "#5P如果不嫌弃，希望您能收下我的谢礼。\x01",
            "……虽然不是很贵重。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x14,
        (
            "#12P#3404F哪里，请不用介意。\x02\x03",

            "#3400F虽说是帮了点忙，\x01",
            "但也只是微不足道的小事，\x01",
            "并不值得您特意道谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xB,
        (
            "#5P哈哈，听您这么一说，\x01",
            "我的心情也轻松多了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65A9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_65A9)
    Sleep(150)

    def lambda_65B9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_65B9)
    Sleep(70)

    def lambda_65C9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_65C9)
    Sleep(150)

    def lambda_65D9():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65D9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0298
    ChrTalk(
        0x103,
        "#12P#0211F……警督，见到美女就开始献殷勤。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#6P#0000F话说回来……\x01",
            "车站和空港的埋伏行动\x01",
            "进展情况如何呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        (
            "#5P那个啊……\x01",
            "老婆婆的其他同伙也都被我们顺利逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xB,
        (
            "#5P他们准备搬运的那些假货\x01",
            "也都被我们扣押了。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        (
            "#5P他们今年恐怕是\x01",
            "不可能再次行动了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#11P#0105F今年？也就是说……\x01",
            "对他们的处罚果然\x01",
            "还是相当轻的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xB,
        (
            "#5P严重警告，\x01",
            "以及为期一个月的自治州驱逐令……\x01",
            "大概也就是这样了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x101,
        "#6P#0005F连、连拘留之类的惩罚都没有吗……？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#12P#0306F什么嘛～……\x01",
            "那还值得费这么大力气去抓吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xB,
        (
            "#5P没办法，根据自治州法律，这毕竟也只是轻微犯罪。\x01",
            "而且对方是外国人，\x01",
            "也不能太过强硬。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xB,
        (
            "#5P虽然这确实很令人郁闷……\x01",
            "但也是无可奈何的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x103,
        "#12P#0203F…………………………\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        (
            "#5P好啦，不用那么沮丧，\x01",
            "你们做得已经很好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xB,
        (
            "#5P至少在今年的纪念庆典中，不会再有\x01",
            "假货出现了，这就已经很好啦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("雷蒙德的声音")
    SetMessageWindowPos(-50, 20, -1, -1)

    #A0312
    AnonymousTalk(
        0x16,
        (
            "#2S警、警督～……\x01",
            "快来帮帮我啊～……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0313
    ChrTalk(
        0xB,
        (
            "#5P噢……\x01",
            "我必须赶快去帮帮\x01",
            "那家伙啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xB,
        "#5P特别任务支援科的各位，这次辛苦你们了。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        "#5P以后可能还会有需要你们帮忙的地方，到时就拜托了哦。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#6P#0000F是，\x01",
            "我们随时待命。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B39")

    #C0317
    ChrTalk(
        0xB,
        (
            "#5P……啊……\x01",
            "对了，有件事忘了说。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        (
            "#5P你们曾经把一名游客\x01",
            "误认为嫌疑人了……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xB,
        (
            "#5P警察局刚才已经送去了\x01",
            "当作谢罪的礼品。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0xB,
        (
            "#5P……今后可要更加慎重，\x01",
            "不要再做出这么轻率的判断了。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        (
            "#6P#0006F对、对不起，\x01",
            "以后一定会注意的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B39")

    OP_93(0xB, 0x0, 0x1F4)

    def lambda_6B45():
        OP_95(0xFE, -34750, 0, 18800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6B45)
    WaitChrThread(0xB, 1)
    Sleep(500)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x1)
    Sleep(500)

    def lambda_6B7E():
        OP_95(0xFE, -34750, 0, 21500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6B7E)

    def lambda_6B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_6B98)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x1)

    #C0322
    ChrTalk(
        0x14,
        (
            "#12P#3401F克洛斯贝尔自治州……\x01",
            "虽然早有耳闻，但今天才算体会到，\x01",
            "这里真是一个立场薄弱的地方呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        "#6P#0005F哎……\x02",
    )

    CloseMessageWindow()
    OP_68(-35070, 1500, 14300, 1000)

    def lambda_6C50():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C50)

    def lambda_6C5D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6C5D)

    def lambda_6C6A():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6C6A)

    def lambda_6C77():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C77)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0324
    ChrTalk(
        0x14,
        (
            "#12P#3403F法律本是为了保护\x01",
            "人们而定制的……\x02\x03",

            "但在克洛斯贝尔，\x01",
            "法律却成为了帝国与共和国\x01",
            "控制这里的手段。\x02\x03",

            "#3400F像这种既不甘心，却又\x01",
            "无可奈何的事情，恐怕你们也\x01",
            "经历了不止一次两次了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        "#5P#0008F……………………\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x14,
        (
            "#12P#3404F但即使如此……\x01",
            "你们也仍然在与这种现状进行斗争，\x01",
            "如此精神，确实值得我表示敬意。\x02\x03",

            "#3402F虽然这话由居住在共和国的我来说\x01",
            "并不太合适……\x01",
            "但希望你们今后也不要放弃哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x190)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x101,
        "#5P#0011F啊……\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#11P#0305F噢，雾香小姐\x01",
            "接下来有什么打算吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x14,
        (
            "#5P#3404F我在欢乐街的酒店里\x01",
            "订了房间。\x02\x03",

            "打算暂时在那里\x01",
            "住一段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#5P#0100F如果愿意的话，\x01",
            "我们可以为您带路……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x14,
        (
            "#5P#3400F呵呵……感谢你的好意，\x01",
            "不过我知道去那里的路。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        (
            "#5P#0205F欢乐街的话……\x02\x03",

            "#0200F莫非，雾香小姐来\x01",
            "克洛斯贝尔是为了……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0x0, 0x1F4)
    Sleep(300)

    #C0333
    ChrTalk(
        0x14,
        (
            "#12P#3400F呵呵……洞察力很不错哦。\x02\x03",

            "没错，我是为了观赏彩虹剧团\x01",
            "的表演而来到克洛斯贝尔的。\x02\x03",

            "#3404F如果有机会，我希望\x01",
            "能将他们请到共和国来进行公演。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#5P#0005F在共和国公演……！？\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x14,
        (
            "#12P#3404F彩虹剧团是沉眠在\x01",
            "克洛斯贝尔的，具有魔性的宝石……\x02\x03",

            "它是否拥有能将共和国\x01",
            "卷入狂热漩涡的力量……\x01",
            "目前还不得而知。\x02\x03",

            "#3402F而确认这个问题的答案，\x01",
            "就是我来克洛斯贝尔的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#5P#0000F啊……\x02\x03",

            "#0003F（在唐古拉姆门时所说的\x01",
            "  『前来寻找的宝石』，原来就是在指\x01",
            "  彩虹剧团吗……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x14)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_728F")

    #C0337
    ChrTalk(
        0x14,
        (
            "#12P#3404F你们几个……虽然尚不成熟，\x01",
            "但却有着某种能够迫近真相的能力呢。\x02\x03",

            "#3402F呵呵，竟能如此准确果断地\x01",
            "确定真正的犯人，不难看出，\x01",
            "你们的推理能力也算是登堂入室了。\x02\x03",

            "今后也互相加油，共同努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7423")

    label("loc_728F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7364")

    #C0338
    ChrTalk(
        0x14,
        (
            "#12P#3404F你们几个……虽然尚不成熟，\x01",
            "却有着某种能够迫近真相的能力呢。\x02\x03",

            "#3400F呵呵，但在最后的最后，\x01",
            "居然把我认定为真正的嫌疑人，\x01",
            "不得不说，你们还是很不成熟呢。\x02\x03",

            "今后也互相加油，共同努力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7423")

    label("loc_7364")


    #C0339
    ChrTalk(
        0x14,
        (
            "#12P#3404F你们几个……虽然尚不成熟，\x01",
            "但却有着某种能够迫近真相的能力呢。\x02\x03",

            "#3400F呵呵，但在离真相只有一步之遥\x01",
            "的时刻走错了路，不得不说，你们还是\x01",
            "不够成熟呢。\x02\x03",

            "今后也互相加油，共同努力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7423")


    #C0340
    ChrTalk(
        0x101,
        (
            "#5P#0003F说、说得也是啊。\x02\x03",

            "#0000F雾香小姐，\x01",
            "非常感谢您的协助。\x02\x03",

            "如果今后有什么需要，\x01",
            "请随时与支援科联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x14,
        (
            "#12P#3402F呵呵……有机会的话，一定。\x02\x03",

            "#3404F那么，我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xB4, 0x1F4)

    def lambda_74E4():
        OP_95(0xFE, -34750, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_74E4)
    WaitChrThread(0x14, 1)

    def lambda_7502():
        OP_95(0xFE, -28000, 0, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_7502)
    WaitChrThread(0x14, 1)

    #C0342
    ChrTalk(
        0x102,
        (
            "#5P#0106F呼……这次的任务\x01",
            "也真是相当棘手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        (
            "#11P#0306F完全赞同。\x02\x03",

            "#0309F算了，多亏如此，\x01",
            "才能结识到雾香小姐那样的美人啊！\x02\x03",

            "#0304F哎呀～虽然早已经看惯了\x01",
            "东方的美人……\x01",
            "但还是觉得雾香小姐尤其美艳超群呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_75F5():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_75F5)

    #C0344
    ChrTalk(
        0x103,
        "#6P#0206F……这人真是永远都学不乖啊。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#5P#0000F哈哈……算了，总之一切顺利。\x02\x03",

            "我们差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【揭发假货贩子】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_29(0x1B, 0x4, 0x10)
    SetChrPos(0xB, -124850, 0, 14920, 45)
    SetChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    SetMapObjFlags(0x1, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_29_5DC3 end

    def Function_30_76FF(): pass

    label("Function_30_76FF")

    ClearScenarioFlags(0x1, 4)
    ClearScenarioFlags(0x1, 5)
    ClearScenarioFlags(0x1, 6)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7712")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7935")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7751")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_7751")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7785")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_7785")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77B9")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_77B9")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77ED")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_77ED")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7821")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_7821")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7855")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_7855")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7889")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_7889")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78BD")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    Jump("loc_7930")

    label("loc_78BD")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78F4")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 5)
    Jump("loc_7930")

    label("loc_78F4")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xEE), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_792B")
    OP_D0(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1, 4)
    SetScenarioFlags(0x1, 6)
    Jump("loc_7930")

    label("loc_792B")

    Jump("loc_7935")

    label("loc_7930")

    Jump("loc_7712")

    label("loc_7935")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_8420")
    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-900, 1540, 13420, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19950, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79BF")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0xEF, 300, 40, 13000, 0)
    SetChrPos(0x153, -900, 40, 11800, 0)
    Jump("loc_7AE7")

    label("loc_79BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A31")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x109, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_7AE7")

    label("loc_7A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AA3")
    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)
    SetChrPos(0x10A, -900, 40, 10600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_7AE7")

    label("loc_7AA3")

    SetChrPos(0x101, -900, 40, 13000, 0)
    SetChrPos(0x102, 300, 40, 13000, 0)
    SetChrPos(0x103, -900, 40, 11800, 0)
    SetChrPos(0x104, 300, 40, 11800, 0)

    label("loc_7AE7")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    FadeToBright(500, 0)
    OP_0D()

    #C0347
    ChrTalk(
        0x8,
        (
            "啊，各位……\x01",
            "战斗手册的情报好像\x01",
            "有了大量的更新啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "我想记录一下魔兽的情报，\x01",
            "所以可以允许我看一下战斗手册吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#0000F嗯，当然可以。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0350
    ChrTalk(
        0x8,
        (
            "十分感谢，\x01",
            "手册还给你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x8,
        (
            "这是本次的奖励。\x01",
            "请收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C55")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0353
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了1个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 1)
    Jump("loc_7F4E")

    label("loc_7C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CAA")

    #A0354
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(1000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了2个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 2)
    Jump("loc_7F4E")

    label("loc_7CAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7CFF")

    #A0356
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(1500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了3个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 3)
    Jump("loc_7F4E")

    label("loc_7CFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D54")

    #A0358
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(2000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0359
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了4个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 4)
    Jump("loc_7F4E")

    label("loc_7D54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA9")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "２５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(2500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0361
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了5个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 5)
    Jump("loc_7F4E")

    label("loc_7DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DFE")

    #A0362
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(3000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0363
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了6个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 6)
    Jump("loc_7F4E")

    label("loc_7DFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E53")

    #A0364
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(3500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了7个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 7)
    Jump("loc_7F4E")

    label("loc_7E53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EA8")

    #A0366
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(4000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0367
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了8个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 8)
    Jump("loc_7F4E")

    label("loc_7EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EFD")

    #A0368
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "４５００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(4500)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0369
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了9个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 9)
    Jump("loc_7F4E")

    label("loc_7EFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F4E")

    #A0370
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "５０００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    AddMira(5000)
    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0371
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了10个。\x02",
        )
    )

    AddItemNumber('Ｕ材料', 10)

    label("loc_7F4E")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F82")
    Sound(17, 0, 100, 0)

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣布料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了2个。\x02",
        )
    )

    AddItemNumber('神圣布料', 2)
    CloseMessageWindow()
    Jump("loc_7FAD")

    label("loc_7F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7FAD")
    Sound(17, 0, 100, 0)

    #A0373
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '神圣布料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    AddItemNumber('神圣布料', 1)
    CloseMessageWindow()

    label("loc_7FAD")

    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80C0")

    #C0374
    ChrTalk(
        0x8,
        (
            "如果以后收集到了新的魔兽情报，\x01",
            "请再次过来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        "#0000F好的，到时就麻烦您了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_805C")

    #C0376
    ChrTalk(
        0x102,
        "#0100F那就下次再来打扰了哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_80BB")

    label("loc_805C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_808B")

    #C0377
    ChrTalk(
        0x103,
        "#0200F下次再来打扰。\x02",
    )

    CloseMessageWindow()
    Jump("loc_80BB")

    label("loc_808B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_80BB")

    #C0378
    ChrTalk(
        0x104,
        "#0300F那就下次再来打扰啦。\x02",
    )

    CloseMessageWindow()

    label("loc_80BB")

    Jump("loc_839D")

    label("loc_80C0")


    #C0379
    ChrTalk(
        0x8,
        (
            "谢谢你们帮忙\x01",
            "收集了这么多情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x8,
        (
            "其实我们也拜托过\x01",
            "其他搜查官帮忙收集这些情报……\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "但只有特别任务支援科的各位\x01",
            "收集得这么全面哦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_818D")

    #C0382
    ChrTalk(
        0x104,
        (
            "#0300F哈哈……因为我们\x01",
            "总是到处乱晃。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_820A")

    label("loc_818D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_81D1")

    #C0383
    ChrTalk(
        0x102,
        (
            "#0100F啊哈哈……因为我们\x01",
            "去了很多地方啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_820A")

    label("loc_81D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_820A")

    #C0384
    ChrTalk(
        0x103,
        (
            "#0200F……因为我们\x01",
            "总是四处奔波呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_820A")


    #C0385
    ChrTalk(
        0x101,
        (
            "#0000F而且我们也经常进行战斗。\x02\x03",

            "……总之，能帮上忙\x01",
            "就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x8,
        "呵呵……各位果然很可靠啊。\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x8,
        (
            "总部收集到的情报\x01",
            "也已经足够了，\x01",
            "所以本项调查就此结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x8,
        (
            "十分感谢各位\x01",
            "能帮忙到最后。\x01",
            "这次会给予各位特别报酬哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "１００００米拉\x07\x00",
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddMira(10000)

    #C0390
    ChrTalk(
        0x8,
        (
            "以后可能还会有事\x01",
            "需要各位帮忙。\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#0000F嗯，彼此彼此。\x01",
            "到时候就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_839D")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83BB")
    Jump("loc_83F5")

    label("loc_83BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83D8")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_83F5")

    label("loc_83D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83F5")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_83F5")

    label("loc_83F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_8401")
    ClearScenarioFlags(0x1, 3)

    label("loc_8401")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -340, 40, 13280, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Jump("loc_850C")

    label("loc_8420")

    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A3")

    #C0392
    ChrTalk(
        0x8,
        (
            "总部收集到的情报\x01",
            "也已经足够了，\x01",
            "所以本项调查就此结束。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x8,
        (
            "以后可能还会有事\x01",
            "需要各位帮忙。\x01",
            "到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_850C")

    label("loc_84A3")


    #C0394
    ChrTalk(
        0x8,
        (
            "战斗手册好像\x01",
            "没有新内容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x8,
        (
            "等情报得到进一步更新时，\x01",
            "请再拿来给我看。\x01",
            "我们会将情报记录整理的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_850C")

    Return()

    # Function_30_76FF end

    def Function_31_850D(): pass

    label("Function_31_850D")

    EventBegin(0x1)

    #C0396
    ChrTalk(
        0x101,
        (
            "#0003F……没有事情需要去楼上啊……\x02\x03",

            "#0000F要是没有正事就直接上去，\x01",
            "说不定又会被副局长训斥的。\x01",
            "还是不要上去了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -12810, 0, 14970, 180)
    EventEnd(0x4)
    Return()

    # Function_31_850D end

    def Function_32_8599(): pass

    label("Function_32_8599")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8ADB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A5")

    #C0397
    ChrTalk(
        0x101,
        (
            "#0005F对了……\x01",
            "我之前就一直很在意。\x02\x03",

            "#0001F这个是什么呢？\x01",
            "好像是某种装置……\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x104,
        (
            "#0305F哦哦，我也一直很在意啊。\x02\x03",

            "#0300F里面好像摆放了很多果汁\x01",
            "和咖啡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x103,
        (
            "#0202F这是『导力式自动贩卖机』。\x01",
            "两位是第一次见到吗？\x02\x03",

            "#0204F只要投入米拉硬币，\x01",
            "就可以买到相应\x01",
            "价格的饮料哦。\x02\x03",

            "这原本是由爱普斯泰恩财团所开发的，\x01",
            "所以在财团的\x01",
            "研究设施中经常能看到……\x02\x03",

            "#0202F如今似乎也在克洛斯贝尔\x01",
            "投入了实验性使用呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        "#0000F哎，原来如此啊……\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x104,
        "#0305F大小姐，你知道吗？\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#0104F不，我也是第一次见到。\x02\x03",

            "#0100F不过，由爱普斯泰恩财团\x01",
            "所研发的装置\x01",
            "还真是遍布各处呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x103,
        (
            "#0203F听说是因为有\x01",
            "实力雄厚的投资者提供资金……\x02\x03",

            "#0200F……各位如果想要使用，\x01",
            "就请投入硬币吧。\x01",
            "因为这种机器无法识别纸币。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#0000F知、知道了。\x01",
            "（这个装置挺少见的……\x01",
            "  就用一次看看吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AD3")

    label("loc_88A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0405
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一台导力式自动贩卖机。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0406
    ChrTalk(
        0x101,
        (
            "#0005F这个……我记得好像投入硬币\x01",
            "就能买到饮料吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8983")

    #C0407
    ChrTalk(
        0x103,
        (
            "#0200F嗯，这是由爱普斯泰恩财团开发的\x01",
            "自动贩卖机。\x02\x03",

            "在克洛斯贝尔\x01",
            "也投入了实验性使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A9A")

    label("loc_8983")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A09")

    #C0408
    ChrTalk(
        0x102,
        (
            "#0100F这个好像是由爱普斯泰恩财团开发的\x01",
            "自动贩卖机……\x02\x03",

            "据缇欧说，\x01",
            "是财团在克洛斯贝尔\x01",
            "将其投入实验性使用的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A9A")

    label("loc_8A09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8A9A")

    #C0409
    ChrTalk(
        0x104,
        (
            "#0300F这个好像是由爱普斯泰恩财团开发的\x01",
            "自动贩卖机……应该没记错吧。\x02\x03",

            "听阿缇说，\x01",
            "这东西是财团在克洛斯贝尔\x01",
            "为了试验而设置的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A9A")


    #C0410
    ChrTalk(
        0x101,
        (
            "#0000F真不愧是克洛斯贝尔……\x01",
            "果然有很多稀奇的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AD3")

    SetScenarioFlags(0x95, 3)
    Jump("loc_8AF2")

    label("loc_8ADB")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_8AF2")

    TalkEnd(0xFF)
    Return()

    # Function_32_8599 end

    SaveToFile()

Try(main)
