from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c134b.bin",                # FileName
        "c134b",                    # MapName
        "c134b",                    # Location
        0x001D,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 29, 0, 1, 0, 3],
    )

    BuildStringList((
        "c134b",                  # 0
        "迪塔总裁",               # 1
        "玛丽亚贝尔",             # 2
        "琪雅",                   # 3
        "滴",                     # 4
        "艾莉",                   # 5
        "缇欧",                   # 6
        "兰迪",                   # 7
        "人偶",                   # 8
        "人偶",                   # 9
    ))

    AddCharChip((
        "chr/ch05602.itc",                   # 00
        "chr/ch05500.itc",                   # 01
        "apl/ch50512.itc",                   # 02
        "apl/ch50512.itc",                   # 03
        "chr/ch05502.itc",                   # 04
        "apl/ch50093.itc",                   # 05
        "chr/ch00102.itc",                   # 06
        "chr/ch00100.itc",                   # 07
        "chr/ch00200.itc",                   # 08
        "chr/ch00300.itc",                   # 09
    ))

    DeclNpc(55000,   150,     128800,  180,  261,  0x0, 0,   0,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(57799,   29,      126400,  225,  261,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(171500,  200,     123500,  270,  343,  0x0, 1,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(171500,  200,     124400,  270,  343,  0x0, 0,   3,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(59090,   29,      121360,  0,    341,  0x0, 0,   6,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(59090,   0,       -1070,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(59090,   0,       -1070,   135,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(172360,  800,     120099,  0,    374,  0x0, 3,   5,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(172360,  800,     120800,  0,    374,  0x0, 4,   5,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(55000,   150,     128800,  2500,    55000,   1800,    128800,  0x007E, 0,  8,  0x0000)
    DeclActor(170460,  0,       122680,  1500,    171500,  1200,    123000,  0x007E, 0,  6,  0x0000)
    DeclActor(170300,  0,       125140,  1500,    171500,  1200,    124000,  0x007E, 0,  4,  0x0000)
    DeclActor(172500,  0,       121000,  1200,    172500,  1500,    121000,  0x007C, 0,  21, 0x0000)
    DeclActor(172500,  0,       120000,  1200,    172500,  1500,    120250,  0x007C, 0,  21, 0x0000)

    ScpFunction((
        "Function_0_2C4",          # 00, 0
        "Function_1_37C",          # 01, 1
        "Function_2_480",          # 02, 2
        "Function_3_487",          # 03, 3
        "Function_4_4CA",          # 04, 4
        "Function_5_4CE",          # 05, 5
        "Function_6_5B9",          # 06, 6
        "Function_7_5BD",          # 07, 7
        "Function_8_61C",          # 08, 8
        "Function_9_620",          # 09, 9
        "Function_10_912",         # 0A, 10
        "Function_11_DD0",         # 0B, 11
        "Function_12_14BA",        # 0C, 12
        "Function_13_2E46",        # 0D, 13
        "Function_14_49B9",        # 0E, 14
        "Function_15_6938",        # 0F, 15
        "Function_16_7F8E",        # 10, 16
        "Function_17_83BE",        # 11, 17
        "Function_18_99AE",        # 12, 18
        "Function_19_99E1",        # 13, 19
        "Function_20_9A1E",        # 14, 20
        "Function_21_9A72",        # 15, 21
    ))


    def Function_0_2C4(): pass

    label("Function_0_2C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_304"),
        (1, "loc_310"),
        (2, "loc_31C"),
        (3, "loc_328"),
        (4, "loc_334"),
        (5, "loc_340"),
        (6, "loc_34C"),
        (SWITCH_DEFAULT, "loc_358"),
    )


    label("loc_304")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_310")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_31C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_328")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_334")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_340")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_34C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_358")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_364")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_364")

    label("loc_37B")

    Return()

    # Function_0_2C4 end

    def Function_1_37C(): pass

    label("Function_1_37C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_394")
    ClearScenarioFlags(0x5F, 1)
    Event(0, 2)

    label("loc_394")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    Event(0, 17)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3BD")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 15)

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 4)), scpexpr(EXPR_END)), "loc_3CB")
    Jump("loc_47F")

    label("loc_3CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 59090, 30, 124780, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_448")
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x10)
    SetChrChipByIndex(0xC, 0x7)
    SetChrSubChip(0xC, 0x0)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 59090, 0, -1070, 135)
    Jump("loc_47F")

    label("loc_448")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_466")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_47F")

    label("loc_466")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xE, 0x80)

    label("loc_47F")

    Return()

    # Function_1_37C end

    def Function_2_480(): pass

    label("Function_2_480")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_480 end

    def Function_3_487(): pass

    label("Function_3_487")

    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x2D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_487 end

    def Function_4_4CA(): pass

    label("Function_4_4CA")

    Call(0, 5)
    Return()

    # Function_4_4CA end

    def Function_5_4CE(): pass

    label("Function_5_4CE")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_572")

    #C0001
    ChrTalk(
        0xB,
        "#1503F#40W呼～……呼～……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0006F（两个人都毫发无伤，\x01",
            "  真是太好了……）\x02\x03",

            "#0000F（………能保护好她们，真是太好了………）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEE, 5)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5B5")

    label("loc_572")


    #C0003
    ChrTalk(
        0xB,
        "#1503F#40W呼～……呼～……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "小滴静静地睡着。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xA)

    label("loc_5B5")

    TalkEnd(0xB)
    Return()

    # Function_5_4CE end

    def Function_6_5B9(): pass

    label("Function_6_5B9")

    Call(0, 7)
    Return()

    # Function_6_5B9 end

    def Function_7_5BD(): pass

    label("Function_7_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D3")
    Call(0, 16)
    Jump("loc_61B")

    label("loc_5D3")

    TalkBegin(0xA)

    #C0005
    ChrTalk(
        0xA,
        "#1113F#40W……呼～呼～………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "琪雅静静地睡着。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xA)

    label("loc_61B")

    Return()

    # Function_7_5BD end

    def Function_8_61C(): pass

    label("Function_8_61C")

    Call(0, 9)
    Return()

    # Function_8_61C end

    def Function_9_620(): pass

    label("Function_9_620")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B4")
    Jump("loc_6FE")

    label("loc_6B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D4")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FE")

    label("loc_6D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F4")
    OP_52(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6FE")

    label("loc_6F4")

    OP_52(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FE")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C")
    SetScenarioFlags(0xEE, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7C8")

    #C0007
    ChrTalk(
        0x8,
        (
            "#2800F去和一层服务台的接待员说一声，\x01",
            "应该就能利用各项服务项目了。\x02\x03",

            "罗伊德，为了谨慎起见，\x01",
            "不要忘记好好休息，养精蓄锐啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90A")

    label("loc_7C8")


    #C0008
    ChrTalk(
        0x8,
        (
            "#2803FＩＢＣ的保安部非常优秀，\x01",
            "把警备工作放心交给他们就行了。\x02\x03",

            "#2800F罗伊德，如果想要进行补给，\x01",
            "就去找一层服务柜台的接待员吧。\x02\x03",

            "#2804F还有……为了谨慎起见，\x01",
            "不要忘记好好休息，养精蓄锐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0002F好的，承蒙您的关照，\x01",
            "实在是非常感谢。\x02\x03",

            "#0003F（总之，至少先去补给吧。\x01",
            "  ……因为无法预料接下来将会遇到什么情况。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_90A")

    SetChrSubChip(0x8, 0x0)
    TalkEnd(0x8)
    Return()

    # Function_9_620 end

    def Function_10_912(): pass

    label("Function_10_912")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A6")
    Jump("loc_9F0")

    label("loc_9A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9C6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F0")

    label("loc_9C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F0")

    label("loc_9E6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2E")
    SetScenarioFlags(0xEF, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A89")

    #C0010
    ChrTalk(
        0x9,
        "#2901F（紧盯）……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0005F？？？\x01",
            "（怎么了啊……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C")

    label("loc_A89")


    #C0012
    ChrTalk(
        0x9,
        (
            "#2903F真是让人不得不防啊……\x02\x03",

            "#2901F……等将一切都解决后，就要考虑好对策，\x01",
            "无论如何都要妨碍一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0006F（好像在说什么让人不安的话……）\x02",
    )

    CloseMessageWindow()

    label("loc_B1C")

    Jump("loc_DC8")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BC0")

    #C0014
    ChrTalk(
        0x9,
        (
            "#2904F关于通讯网络的恢复，\x01",
            "我已经向技术部发出指示了，\x01",
            "稍后应该就能有所进展了吧。\x02\x03",

            "#2900F……总之，现在的首要任务\x01",
            "就是努力弄清眼下的情况啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC8")

    label("loc_BC0")


    #C0015
    ChrTalk(
        0x9,
        (
            "#2903F虽然已经考虑过好几个打破\x01",
            "如今这种僵局的计划……\x02\x03",

            "#2901F但无奈的是，手段终究还是不够啊。\x02\x03",

            "最重要的是，无论是对方的真实身份，\x01",
            "还是对方的目的，我们都还没有完全搞清，\x01",
            "所以也无法采取恰当的行动啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#0008F首先还是要努力把握情况呢。\x02\x03",

            "#0006F然后就是思考对手的下一步动作，\x01",
            "并采取最有效的对策……\x01",
            "大概就是这样吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#2905F……难得我们想法一致呢。\x02\x03",

            "#2904F算了，先这样吧。\x01",
            "关于通讯网络的恢复，\x01",
            "我已经向技术部发出指示了。\x02\x03",

            "#2902F缇欧也会提供协助。\x01",
            "对了，要不要去那个终端室\x01",
            "看看情况呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0000F嗯，我会去的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_DC8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_912 end

    def Function_11_DD0(): pass

    label("Function_11_DD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE8")
    Call(0, 12)
    Return()

    label("loc_DE8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E7C")
    Jump("loc_EC6")

    label("loc_E7C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E9C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC6")

    label("loc_E9C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC6")

    label("loc_EBC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_END)), "loc_11AA")

    #C0019
    ChrTalk(
        0xC,
        (
            "#0112F啊，罗伊德……\x02\x03",

            "#0113F那、那个，你还是稍微\x01",
            "再休息一下比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0012F啊……\x01",
            "我再稍微去转转，然后就休息。\x02\x03",

            "#0002F艾莉也一直在四处奔走，\x01",
            "也要好好休息啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xC,
        "#0102F嗯，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0022
    ChrTalk(
        0x9,
        "#2901F……你们很可疑啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xC, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    SetChrSubChip(0xC, 0x0)
    TurnDirection(0x101, 0x9, 500)

    #C0023
    ChrTalk(
        0x101,
        "#0011F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xC,
        (
            "#0112F贝、贝尔你真是的……！\x01",
            "突然说些什么呀！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_64(0xC)

    #C0025
    ChrTalk(
        0x9,
        (
            "#2903F因为，刚才艾莉你是\x01",
            "红着脸回来的呢。\x02\x03",

            "#2901F难道……\x01",
            "你该不会是利用这种紧急状况，\x01",
            "对艾莉做出了一些寡廉鲜耻的事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0012F没、没那回事……！\x01",
            "（虽然差一点就……）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xC,
        "#0113F…………………………（脸红）\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        "#2910F……………………（瞪视）\x02",
    )

    CloseMessageWindow()
    Jump("loc_135D")

    label("loc_11AA")


    #C0029
    ChrTalk(
        0xC,
        (
            "#0108F罗伊德……\x01",
            "事情变得很麻烦了呢。\x02\x03",

            "#0101F『教团』的……\x01",
            "约亚西姆医生的目的到底是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0008F不知道啊……\x02\x03",

            "#0006F话说回来，最后把这里的人\x01",
            "都卷进来了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0031
    ChrTalk(
        0xC,
        (
            "#0102F呵呵……\x01",
            "你还是一点都没变。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0005F……………………？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xC,
        (
            "#0104F没关系的。\x01",
            "叔叔也好，贝尔也好，\x01",
            "大家都是很坚强的人。\x02\x03",

            "#0100F比起他们，我们现在\x01",
            "更应该想想怎么才能\x01",
            "保护好小琪雅和小滴。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#0000F啊，也是呢，\x01",
            "那我先去别处转转。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135D")

    SetScenarioFlags(0xE4, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14B2")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_END)), "loc_1427")

    #C0035
    ChrTalk(
        0xC,
        (
            "#0109F那、那个……\x01",
            "补给和调整装备就拜托你了啊。\x02\x03",

            "#0102F我还要和贝尔再\x01",
            "商讨一下今后的对策……\x02\x03",

            "我们都在不要累倒的\x01",
            "前提下加油吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")

    #C0036
    ChrTalk(
        0x101,
        "#0000F是啊……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1422")

    Jump("loc_14B2")

    label("loc_1427")


    #C0037
    ChrTalk(
        0xC,
        (
            "#0103F虽然和贝尔谈了很多，\x01",
            "但现在这种状况，还真是无计可施啊。\x02\x03",

            "#0108F等到天亮……\x01",
            "如果能与某处取得联络的话，\x01",
            "或许还有些希望，可是……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_DD0 end

    def Function_12_14BA(): pass

    label("Function_12_14BA")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xC, 0xFF)
    LoadChrToIndex("apl/ch50541.itc", 0x1E)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    SetChrPos(0x101, 59090, 0, 360, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00101.itp")
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0038
    ChrTalk(
        0xC,
        "#0108F#5P#40W………………………………\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0000F#5P艾莉……\x01",
            "原来你在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x0, 0x190)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    #Sound(1178, 255, 90, 0)    #voice#Elie
    Sleep(150)

    #A0040
    AnonymousTalk(
        0xC,
        "#40W罗伊德……\x02",
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
            "#0006F#5P……虽然完全没有说的必要，\x01",
            "但事态真是变得很严重啊。\x02\x03",

            "#0001F希望市内的人们……\x01",
            "能够平安无事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "#0106F#11P#30W是啊……\x02\x03",

            "#0108F#40W………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0043
    ChrTalk(
        0x101,
        (
            "#0004F#5P……艾莉，\x01",
            "麦克道尔市长一定不会有事的。\x02\x03",

            "#0000F加害市长的话，对操纵警备队的\x01",
            "幕后黑手来说，也没有什么好处。\x02\x03",

            "总之，咱们还是要努力打破\x01",
            "这种僵局，解救市长他们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "#0102F#11P罗伊德……\x01",
            "嗯，谢谢你。\x02\x03",

            "#0104F对哦，外公曾经也经历过\x01",
            "多次战争……\x02\x03",

            "像这种程度的危机，\x01",
            "他一定可以顺利跨越的。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0002F#5P是啊……\x01",
            "市长的话，绝对没问题！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        (
            "#0102F#11P……呵呵………\x02\x03",

            "#0106F唉～为什么\x01",
            "你会对我这么了解呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#0005F#5P哎？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#0113F#11P……仔细想想，真是不公平呢。\x02\x03",

            "我都已经……将很多秘密\x01",
            "告诉你了。\x02\x03",

            "#0111F可是你却……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#0011F#5P那、那个，艾莉……？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0050
    ChrTalk(
        0xC,
        (
            "#0103F#11P──我说，罗伊德。\x02\x03",

            "#0100F你是不是\x01",
            "稍微追上哥哥了呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x101,
        "#0005F#5P啊……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        (
            "#0104F#11P你大概……\x01",
            "一直都在追赶着哥哥的背影，\x01",
            "才一步一步走到了现在吧。\x02\x03",

            "你经常说起的那个\x01",
            "『壁障』……\x02\x03",

            "#0100F那莫非也是在\x01",
            "暗指你哥哥这个\x01",
            "难以超越的目标吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0053
    ChrTalk(
        0x101,
        (
            "#0004F#5P……嗯，\x01",
            "我想多半是如此。\x02\x03",

            "#0008F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_68(57610, 1500, 240, 2800)
    MoveCamera(105, 24, 0, 2800)
    OP_6E(500, 2800)
    SetCameraDistance(13000, 2800)
    OP_93(0x101, 0x10E, 0x1F4)

    def lambda_1B10():
        OP_96(0x101, 0xE10A, 0x0, 0xF0, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B10)
    Sleep(1000)

    def lambda_1B2D():
        OP_93(0xC, 0x122, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1B2D)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xC, 2)
    OP_6F(0x79)
    Fade(200)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1B)
    OP_0D()
    Sleep(500)

    #C0054
    ChrTalk(
        0x101,
        (
            "#0004F#5P──从以前开始，\x01",
            "大哥就一直是我心中的英雄。\x02\x03",

            "他无论面对何等逆境也毫不退缩，\x01",
            "一定会将自己想做的事贯彻到底，非常厉害。\x02\x03",

            "#0008F但就在三年前……\x01",
            "他的身影突然从眼前消失，\x01",
            "我也迷失了方向……\x02\x03",

            "我想，自己那时应该是在逃避吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xC,
        "#0105F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0006F#5P因为我……\x01",
            "并没有自信能变得像\x01",
            "大哥一样出色。\x02\x03",

            "也没有自信能像大哥一样，\x01",
            "保护那么多需要保护的人……\x02\x03",

            "#0008F所以……\x01",
            "我才逃到了完全不熟悉的城市。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        (
            "#0103F#11P……不过，你最终\x01",
            "还是回到了克洛斯贝尔。\x02\x03",

            "#0100F那是为什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0004F#5P哈哈，因为我……\x01",
            "果然还是很喜欢这里啊。\x02\x03",

            "大哥，塞茜尔姐姐，\x01",
            "还有曾经共度过无数时光的朋友们……\x02\x03",

            "即使生活在其它地方，\x01",
            "他们也都是我的一部分，\x01",
            "永远无法忘记……\x02\x03",

            "#0000F所以我才强迫自己在\x01",
            "警察学校时就考取了\x01",
            "搜查官的资格。\x02\x03",

            "#0008F因为我觉得，即使是一小步也好，也必须要努力追上大哥……\x02\x03",

            "#0003F如果我不能成为可以\x01",
            "替代大哥的存在，那就没有资格\x01",
            "再回到克洛斯贝尔了……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "#0105F#11P可、可是你最后真的\x01",
            "取得了搜查官的资格啊。\x02\x03",

            "#0102F所以应该相信自己拥有\x01",
            "不逊于哥哥的天分吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0006F#5P不……坦白来说，\x01",
            "其实那也只是狡猾的作弊而已。\x02\x03",

            "#0002F再怎么说，我也一直都在注视着\x01",
            "一位虽然不按常理出牌，\x01",
            "但却仍属一流的搜查官……\x02\x03",

            "#0004F遇到这种事，大哥会怎么做，\x01",
            "如果是大哥，绝对不会放弃……\x02\x03",

            "我就是这样不断自问自答，\x01",
            "然后不知不觉一直走到现在的。\x02\x03",

            "#0008F可是……\x01",
            "那并不代表我自身\x01",
            "真的变强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        "#0101F#11P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0000F#5P……直到最近，\x01",
            "我觉得自己才终于明白了。\x02\x03",

            "如果仅是一直追赶着大哥的背影，\x01",
            "是无法在真正意义上变强的。\x02\x03",

            "#0012F哈哈，虽然我在察觉到\x01",
            "这点之前，已经花费了\x01",
            "太长太长的时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        "#0103F#11P……罗伊德。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    SetChrFlags(0xC, 0x40)
    OP_95(0xC, 57880, 0, -270, 800, 0x0)
    Fade(500)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xC, 57970, 0, -180, 300)
    SetChrSubChip(0x101, 0x0)
    MoveCamera(75, 27, 0, 0)
    SetCameraDistance(14500, 0)
    OP_68(57640, 1500, 140, 0)
    OP_0D()
    Sound(804, 0, 70, 0)
    Sound(910, 0, 80, 0)
    OP_A1(0x101, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        "#0011F#5P艾、艾莉……？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetCameraDistance(13500, 60000)
    OP_A1(0x101, 0x3E8, 0x3, 0x18, 0x19, 0x1A)

    #C0065
    ChrTalk(
        0xC,
        (
            "#0100F#11P……那个，罗伊德。\x02\x03",

            "我对盖伊先生……\x01",
            "对你的哥哥并不了解。\x02\x03",

            "#0104F不过，有一点我可以断言。\x02\x03",

            "至今为止，一直在引领着\x01",
            "我们的并不是别人，正是\x01",
            "你本身。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xC,
        (
            "#0102F#11P无论何时，你总是……\x01",
            "引领着我──引领着大家。\x02\x03",

            "在这座灰色的城市中，很多人\x01",
            "都迷失了方向。我，缇欧，\x01",
            "大概连兰迪也是……\x02\x03",

            "#0104F而你……温和谦逊，勇往直前，   \x01",
            "虽然在关键时刻可能还有点迟钝……  \x02\x03",

            "但在重要的时候，\x01",
            "始终都能陪伴在我们身边，\x01",
            "与我们一同寻找答案……\x02\x03",

            "#0102F正是因为有这样的你，\x01",
            "我们才能一直走到这里。\x02\x03",

            "而做到这点的并不是盖伊先生或\x01",
            "别的什么人，正是你啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0005F#5P……啊………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    Sleep(300)

    #C0069
    ChrTalk(
        0xC,
        (
            "#0104F#11P所以……\x01",
            "能在这个城市中与你相遇，\x01",
            "我真的要为这份幸运感谢空之女神呢。\x02\x03",

            "呵呵，如果是小时候\x01",
            "在主日学校认识就更好了……\x02\x03",

            "#0102F我就是如此庆幸与你的相遇，\x01",
            "以至于会考虑这种毫无意义的假设呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x384, 0x2, 0x4, 0x5)

    #C0070
    ChrTalk(
        0x101,
        "#0004F#5P艾莉……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "#0104F#11P拿出自信来，\x01",
            "罗伊德·班宁斯。\x02\x03",

            "无论是你憧憬哥哥这点，\x01",
            "还是努力想要做自己这点，\x01",
            "都是你自身的一部分……\x02\x03",

            "那样的你，我们大家……\x01",
            "不──我很喜欢。\x02\x03",

            "#0102F所以……\x01",
            "你只要坚持做自己就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0004F#5P……艾莉………\x02\x03",

            "#0002F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x514, 0x4, 0x6, 0x7, 0x8, 0x9)
    Sleep(500)

    #C0073
    ChrTalk(
        0xC,
        "#0112F#11P………啊……………\x02",
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    OP_A1(0x101, 0x4B0, 0x6, 0xA, 0xB, 0xC, 0x15, 0x16, 0x17)
    Sleep(500)
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    VolumeBGM(0x3C, 0x5DC)
    SetChrSubChip(0x101, 0x1E)
    Sleep(8)
    SetChrSubChip(0x101, 0x1F)
    OP_63(0x101, 0xFFFFFFB0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0xFFFFFF9C, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──留在大楼内\x01",
            "的各位请注意。\x02",
        )
    )

    CloseMessageWindow()

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于目前处于非常时期，\x01",
            "所以我们将关闭一部分楼层的\x01",
            "照明系统。\x02",
        )
    )

    CloseMessageWindow()

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "此外，考虑到保安工作的需要，\x01",
            "除了正门入口之外，\x01",
            "其它紧急入口将全部关闭。\x02",
        )
    )

    CloseMessageWindow()

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请您多加谅解，同时也请小心火源。\x01",
            "对于给您造成的不便，\x01",
            "我们致以诚挚的歉意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0xBB8)
    OP_63(0x101, 0xFFFFFFB0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0xFFFFFF9C, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0xC, 0x8)
    TurnDirection(0x101, 0xC, 0)
    OP_0D()
    Sleep(500)

    #C0078
    ChrTalk(
        0x101,
        "#0012F#5P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "#0109F#11P呵呵……\x02\x03",

            "#0112F……那、那个……\x01",
            "我先回去找贝尔啦。\x02\x03",

            "#0113F或许还能帮\x01",
            "叔叔他们做些\x01",
            "什么事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0004F#5P啊，好的……\x01",
            "我也趁现在去进行补给，\x01",
            "顺便检查一下装备吧。\x02\x03",

            "#0002F……一会见。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "#0102F#11P嗯……\x02\x03",

            "#0113F……那个……刚才做到一半的事，\x01",
            "等到把全部事情都解决之后再……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#0005F#5P哎？\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_29DA():

        label("loc_29DA")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_29DA")

    QueueWorkItem2(0x101, 2, lambda_29DA)
    OP_96(0xC, 0xE394, 0x0, 0xFFFFFD3A, 0x3E8, 0x0)

    #C0083
    ChrTalk(
        0xC,
        (
            "#0112F#11P没、没什么啦。\x02\x03",

            "#0109F那、那么，一会见哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x12C)
    OP_95(0xC, 58570, 0, 1430, 2000, 0x0)
    OP_95(0xC, 57880, 0, 4330, 2000, 0x0)
    ClearChrFlags(0xC, 0x40)

    def lambda_2A6E():
        OP_95(0xFE, 53120, 0, 17620, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A6E)
    EndChrThread(0x101, 0x2)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Fade(500)
    MoveCamera(105, 24, 0, 0)
    SetCameraDistance(14000, 0)
    OP_93(0x101, 0x14A, 0x0)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1B)
    OP_0D()
    Sleep(300)

    #C0084
    ChrTalk(
        0x101,
        (
            "#0002F#5P（……艾莉，\x01",
            "  感觉好柔软啊……）\x02\x03",

            "#0002F（而且味道好香……）\x02\x03",

            "#0006F（唉……\x01",
            "  明明只差一点就──）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        "#0011F#5P──现在不是想这种事的时候！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x3E8, 0x2, 0x1C, 0x1D)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0086
    ChrTalk(
        0x101,
        (
            "#0004F#5P（……我只要做我\x01",
            "  自己就好了吗……）\x02\x03",

            "（如果是在不久之前听到别人\x01",
            "  这样说，也许反而会陷入迷茫呢……）\x02\x03",

            "#0000F（不过现在……\x01",
            "  真不可思议，好像已经完全认同了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x101, 0x4B0, 0x2, 0x1C, 0x1B)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_0D()
    Sleep(300)
    OP_93(0x101, 0x13B, 0x12C)

    #C0087
    ChrTalk(
        0x101,
        "#0002F#11P──谢谢你，艾莉。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(14500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DBE")
    StopBGM(0xFA0)
    WaitBGM()
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "罗伊德和艾莉\x01",
            "习得了星辰爆击Ⅱ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和艾莉的组合战技\x01",
            "『星辰爆击』得到了强化。\x02",
        )
    )

    CloseMessageWindow()

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除了攻击力和射程·范围之外，\x01",
            "硬直时间等性能也有了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)

    label("loc_2DBE")

    OP_CA(0x1, 0xFF, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xC, 0x1)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 59090, 30, 121360, 0)
    OP_68(57610, 1500, 240, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 57610, 0, 240, 315)
    SetScenarioFlags(0xE7, 2)
    OP_DE(0x2D, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_12_14BA end

    def Function_13_2E46(): pass

    label("Function_13_2E46")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xD, 0xFF)
    LoadChrToIndex("apl/ch50543.itc", 0x1E)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    SetChrPos(0x101, 59090, 0, 360, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00200.itp")
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0091
    ChrTalk(
        0xD,
        "#0208F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        "#0005F#5P缇欧……？\x02",
    )

    CloseMessageWindow()
    Sound(1269, 255, 90, 0)    #voice#Tio
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(1267, 255, 90, 0)    #voice#Tio
    OP_93(0xD, 0x0, 0x190)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0093
    AnonymousTalk(
        0xD,
        "……罗伊德前辈。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, -1, -1)

    #A0094
    AnonymousTalk(
        0x101,
        (
            "#0005F你在做什……噢，对了。\x02\x03",

            "#0000F是在观察外面\x01",
            "的情况吗？\x02",
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

    #C0095
    ChrTalk(
        0xD,
        (
            "#0203F#11P……嗯，算是吧。\x01",
            "果然还是有些在意呢。\x02\x03",

            "#0205F不过，你立刻就想到了啊……？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#0000F#5P那是当然，因为平时经常会\x01",
            "依靠缇欧的这种感应力啊。\x02\x03",

            "#0001F对了……\x01",
            "市内的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xD,
        (
            "#0206F#11P……零星的枪战\x01",
            "似乎正在各处发生。\x02\x03",

            "#0208F我想多半是警察部队\x01",
            "和警备队展开了\x01",
            "战斗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#0008F#5P是吗……\x02\x03",

            "#0003F……至少没有波及到市民们，\x01",
            "算是万幸了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xD,
        "#0208F#11P……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x101,
        (
            "#0005F#5P……？\x01",
            "缇欧，你是不是\x01",
            "有些累了呢？\x02\x03",

            "#0001F我们一直都在四处奔走呢，\x01",
            "你还是去和琪雅她们一起休息一下……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xD,
        "#0211F#11P……（瞪）\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#0011F#5P啊，不是，我并没有\x01",
            "把你当成小孩子的意思啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xD,
        (
            "#0202F#11P呵呵……我知道的。\x02\x03",

            "因为一直都和罗伊德前辈\x01",
            "还有大家一起行动，\x01",
            "所以我的体力也有所增加了。\x02\x03",

            "#0204F而且，情绪似乎稍微有些高昂，\x01",
            "因此没有什么睡意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        (
            "#0002F#5P是吗……\x02\x03",

            "#0006F……不过，事态还真是\x01",
            "变得相当严重了呢。\x02\x03",

            "#0001F缇欧原本并不是警官，\x01",
            "却还是被卷入到这种事件中……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0105
    ChrTalk(
        0xD,
        "#0211F#11P（瞪）\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#0012F#5P啊，我、我并没有\x01",
            "把你排除在外的意思啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xD,
        "#0206F#11P……真是的。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    #C0108
    ChrTalk(
        0xD,
        (
            "#0206F#11P不、不过……\x01",
            "事态既然已经变得如此严重，\x01",
            "确实很担心今后情况会如何发展呢。\x02\x03",

            "而关于我的调职，\x01",
            "财团又会如何判断……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#0005F#5P哎？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xD,
        (
            "#0208F#11P魔导杖的测试工作，\x01",
            "在克洛斯贝尔以外的地区也可以进行。\x02\x03",

            "根据财团的方针，\x01",
            "我调入警察局的计划\x01",
            "或许会被中止……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        (
            "#0001F#5P是、是吗……\x02\x03",

            "#0003F………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xD,
        (
            "#0208F#11P……那个………\x02\x03",

            "#0200F如果真的变成那样，\x01",
            "前辈会不会感觉有点寂寞呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯、嗯……\x02\x03",

            "别说会觉得寂寞了，简直都有点\x01",
            "令人无法想象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        "#0205F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#0012F#5P那个，就是说，\x01",
            "我没法想象，少了缇欧的\x01",
            "支援科会是什么样啊……\x02\x03",

            "#0000F而且那个终端，\x01",
            "也像是缇欧专用\x01",
            "的特等席吧。\x02\x03",

            "所以也想象不出我们，或是\x01",
            "其他人坐在那里操作的景象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xD,
        "#0205F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#0008F#5P不过，是这样啊……\x01",
            "缇欧的调职计划\x01",
            "还有可能会被中止吗……\x02\x03",

            "#0006F……这要如何是好呢，\x01",
            "以前从来没考虑过这种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xD,
        (
            "#0206F#11P──终究也只是\x01",
            "可能性而已。\x02\x03",

            "#0202F财团在克洛斯贝尔\x01",
            "使用了最先进的技术进行试验，\x01",
            "同时也投入了巨额资金。\x02\x03",

            "所以我想，虽然发生了这种严重事件，\x01",
            "财团也不太可能就此放弃。\x02\x03",

            "#0204F而只要财团不放弃，那么这里\x01",
            "就仍会是测试魔导杖性能的最佳地点。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0002F#5P是、是吗……\x02\x03",

            "#0000F──嗯，既然如此，\x01",
            "我们无论如何也要打破僵局，\x01",
            "然后将事件解决呢！\x02\x03",

            "#0009F就算是为了让缇欧\x01",
            "继续留在支援科，也要拼命！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)

    #C0120
    ChrTalk(
        0xD,
        "#0205F#11P…………！………………\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0121
    ChrTalk(
        0x101,
        (
            "#0011F#5P哎，我、我是不是\x01",
            "又说出什么不经大脑的话了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xD,
        (
            "#0203F#5P……是啊。\x01",
            "老实说，真是荒谬绝伦呢。\x02\x03",

            "#0211F果然正如艾莉前辈所说，\x01",
            "罗伊德前辈是很危险的……\x02\x03",

            "我还真的没想到，\x01",
            "你会做出那种反应呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#0005F#5P这种反应……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "#0208F#5P……就是说…………！\x01",
            "罗伊德前辈是个没用、\x01",
            "迟钝的软弱弟弟型！\x02\x03",

            "#0201F从某种意义上来说，你在这方面\x01",
            "已经超越了盖伊先生呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F#5P那个，完全不明白你在说什么啊……\x02\x03",

            "#0001F……嗯～不过，说到我大哥嘛。\x02\x03",

            "确实是有些迟钝，\x01",
            "甚至可以说是个木头脑袋呢。\x02\x03",

            "#0008F长久以来，好像也一直都没有\x01",
            "察觉到塞茜尔姐姐对他的感情……\x02\x03",

            "#0006F有好几次，我都想把他踢飞，\x01",
            "让他快点明白过来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)
    OP_93(0xD, 0x0, 0x1F4)
    Sleep(300)
    OP_68(58920, 1400, -10, 1200)
    OP_96(0xD, 0xE6F0, 0x0, 0xFFFFFE52, 0x320, 0x0)
    Sound(1197, 255, 85, 0)    #voice#Tio
    Sleep(500)
    Fade(150)
    Sound(819, 0, 100, 0)
    OP_82(0x50, 0x0, 0x7D0, 0xC8)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sound(1029, 255, 90, 1)    #voice#Lloyd

    def lambda_3C74():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C74)
    Sleep(390)
    Fade(250)
    SetChrChipByIndex(0xD, 0x8)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0126
    ChrTalk(
        0x101,
        "#0012F#5P啊，缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xD,
        (
            "#0203F#11P──失礼，不自觉就……\x02\x03",

            "#0211F不过呢，说实话，\x01",
            "刚才那应该是前辈自作自受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#0011F#5P？？？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(801, 0, 100, 0)
    Sleep(500)
    VolumeBGM(0x3C, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    #A0129
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──留在大楼内\x01",
            "的各位请注意。\x02",
        )
    )

    CloseMessageWindow()

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于目前处于非常时期，\x01",
            "所以我们将关闭一部分楼层的\x01",
            "照明系统。\x02",
        )
    )

    CloseMessageWindow()

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "此外，考虑到保安工作的需要，\x01",
            "除了大门入口之外，\x01",
            "其它紧急入口将全部关闭。\x02",
        )
    )

    CloseMessageWindow()

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请您多加谅解，同时也请小心火源。\x01",
            "对于给您造成的不便，\x01",
            "我们致以诚挚的歉意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0xBB8)

    #C0133
    ChrTalk(
        0x101,
        (
            "#0001F#5P嗯……终于要\x01",
            "要开始真正的警戒封锁了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xD,
        (
            "#0204F#11P我准备去地下的\x01",
            "终端室帮忙。\x02\x03",

            "要是能和约纳他们取得联络，\x01",
            "可采取的对策也许就会有所增加了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#0002F#5P是吗……\x01",
            "那就拜托你了。\x02\x03",

            "那么我去进行补给工作，\x01",
            "然后再检查一下装备。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xD,
        "#0202F#11P拜托了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    StopBGM(0xFA0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0137
    ChrTalk(
        0x101,
        (
            "#0011F#5P……缇欧？\x01",
            "（莫非我又惹她生气了……？）\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    SetCameraDistance(14500, 60000)

    #C0138
    ChrTalk(
        0xD,
        (
            "#0208F#11P……罗伊德前辈之前\x01",
            "和我做了一个『约定』……\x02\x03",

            "#0201F还记得吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊，当然……\x02\x03",

            "#0000F并不是继承大哥与你的约定，\x01",
            "而是以我自己的身份来与你约定，没错吧。\x02\x03",

            "#0006F抱歉，关于约定的内容，\x01",
            "在那之后，我也考虑了很多。\x01",
            "但并没有想出什么合适的内容。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xD,
        (
            "#0203F#11P既然如此……\x01",
            "就由我来提议好了。\x02\x03",

            "#0201F那样也可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊……\x01",
            "当然没问题。\x02\x03",

            "#0000F好──尽管说来听听吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xD,
        "#0202F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x190)
    Sleep(300)
    OP_68(58720, 1400, -290, 1500)
    OP_96(0xD, 0xE6D2, 0x0, 0xFFFFFBD2, 0x320, 0x0)
    OP_6F(0x1)

    #C0143
    ChrTalk(
        0xD,
        (
            "#0204F#5P……米修拉姆的主题公园。\x02\x03",

            "如果能顺利解决此次骚乱，\x01",
            "请带我去那里玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        "#0005F#5P嘿……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0145
    ChrTalk(
        0x101,
        (
            "#0011F#5P哎……\x01",
            "那样就行了吗！？\x02\x03",

            "#0001F不，可是……\x01",
            "还是做个更加正式一点\x01",
            "的约定比较好吧？\x02\x03",

            "比如说，当缇欧遇到困难时，\x01",
            "无论如何我都要马上赶去帮忙之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xD,
        (
            "#0204F#5P不，这样就够了。\x02\x03",

            "#0208F而且，如果不解决此次事件，\x01",
            "这个约定也等同于无法履行……\x02\x03",

            "#0202F从这层意义上来说，\x01",
            "也已经算是个非常正式的约定了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#0004F#5P是吗……\x01",
            "……嗯，确实如你所说啊。\x02\x03",

            "#0002F好──那就一言为定。\x02\x03",

            "如果能顺利解决此次事件，\x01",
            "我们就一起去主题公园玩吧。\x02\x03",

            "#0005F噢，对了，是不是\x01",
            "把大家都叫上比较好？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x0, 0x320)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0148
    ChrTalk(
        0xD,
        "#0211F#11P（瞪）……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#0012F#5P还、还是算了，\x01",
            "毕竟这是和缇欧两人的约定啊。\x02\x03",

            "#0006F嗯～不过，如果可以的话，\x01",
            "还是想把琪雅也带上呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xD,
        (
            "#0204F#11P既然如此，那就修正约定内容。\x02\x03",

            "#0202F首先是支援科全体一起去玩……\x01",
            "然后是罗伊德前辈和我两个人去。\x02\x03",

            "这样就没有问题了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#0000F#5P啊，是啊……\x01",
            "这样一来，确实就没有问题了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xD,
        (
            "#0209F#11P呵呵……\x01",
            "我很期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_462A():

        label("loc_462A")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_462A")

    QueueWorkItem2(0x101, 2, lambda_462A)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_68(55630, 1500, 13810, 8000)
    MoveCamera(54, 22, 0, 8000)
    OP_6E(500, 8000)
    SetCameraDistance(21500, 8000)
    Sleep(300)
    OP_95(0xD, 58140, 0, -380, 2000, 0x0)
    OP_95(0xD, 58350, 0, 1520, 2000, 0x0)
    OP_95(0xD, 57740, 0, 4190, 2000, 0x0)
    OP_95(0xD, 53180, 0, 8070, 2000, 0x0)
    OP_95(0xD, 53190, 0, 13960, 2000, 0x0)
    OP_95(0xD, 55730, 0, 13960, 2000, 0x0)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_4711():
        OP_96(0xFE, 0xE4E8, 0x0, 0x3688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4711)
    Sleep(1000)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(600)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0xD, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(58830, 1500, 600, 0)
    MoveCamera(127, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    OP_93(0x101, 0x0, 0x0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0153
    ChrTalk(
        0x101,
        (
            "#0006F#11P嗯～不过，那么简单\x01",
            "的约定真的可以吗……\x02\x03",

            "#0002F……算了，这也不错。\x01",
            "缇欧看上去似乎也很期待。\x02\x03",

            "#0004F就算是为了履行和缇欧的约定……\x01",
            "也绝对要把这次事件解决啊。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495E")
    StopBGM(0xFA0)
    WaitBGM()
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "罗伊德和缇欧\x01",
            "习得了Ω强袭Ⅱ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和缇欧的组合战技\x01",
            "『Ω强袭』得到了强化。\x02",
        )
    )

    CloseMessageWindow()

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除了攻击力和射程·范围之外，\x01",
            "硬直时间等性能也有了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7513", 0)

    label("loc_495E")

    OP_D5(0x1E)
    OP_CA(0x1, 0xFF, 0x0)
    OP_68(59090, 1500, 360, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 59090, 0, 360, 315)
    SetScenarioFlags(0xE7, 3)
    OP_DE(0x2E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_13_2E46 end

    def Function_14_49B9(): pass

    label("Function_14_49B9")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_4B(0xE, 0xFF)
    OP_68(58810, 1400, -420, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16550, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00300.itp")
    SetChrPos(0x101, 59090, 0, 360, 180)
    SetCameraDistance(15550, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0157
    ChrTalk(
        0xE,
        "#0308F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        "#0005F#5P咦，兰迪……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    #Sound(1364, 255, 100, 0)    #voice#Randy
    OP_93(0xE, 0x0, 0x1F4)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0159
    AnonymousTalk(
        0xE,
        (
            "──哟，搭档。\x02\x03",

            "真没想到事情会变得\x01",
            "如此不可收拾啊。\x02",
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

    #C0160
    ChrTalk(
        0x101,
        "#0005F#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "#0305F#11P嗯，怎么了？\x01",
            "我说了什么奇怪的话吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#0012F#5P没、没有啦……\x02\x03",

            "#0008F……不过，说实话，\x01",
            "兰迪现在是怎么想的呢？\x02\x03",

            "#0001F如果警备队全力攻向这里，\x01",
            "你觉得我们能支撑多久……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xE,
        (
            "#0303F#11P呼，说实话，形势确实很严峻呢。\x02\x03",

            "#0301F克洛斯贝尔的警备队\x01",
            "可是正规的军事组织。\x02\x03",

            "虽然没有战车和飞行船，\x01",
            "但队员都训练有素，\x01",
            "而且每个人都配有最高级的装备。\x02\x03",

            "#0306F就算这栋大楼用最先进的高科技进行了\x01",
            "全副武装，但民间设施终究不是军事要塞，\x01",
            "恐怕很难支撑太久吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#0008F#5P果然如此吗……\x02\x03",

            "#0003F……这样的话，无论如何\x01",
            "也要和警察局总部或游击士协会\x01",
            "取得联络啊……\x02\x03",

            "#0013F所以至少必须在通讯恢复\x01",
            "之前将这栋大楼守住……\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        (
            "#0303F#11P嗯，就是这么一回事啦。\x02\x03",

            "#0308F……真是的，如果早知道会遇到这种事，\x01",
            "我就把那个东西给带来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#0005F#5P那个东西？\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        "#0303F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xE, 0xB4, 0x1F4)
    Sleep(500)

    #C0168
    ChrTalk(
        0xE,
        (
            "#0304F#5P……是我一直用到两年前\x01",
            "的导力来复枪。\x02\x03",

            "#0300F拥有相当惊人的巨大火力。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#0008F#5P是吗，那是你在猎兵时代……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7515", 0)

    #C0170
    ChrTalk(
        0x101,
        (
            "#0003F#5P……在『赤色星座』时使用的吗？\x02\x03",

            "#0000F在那之后，我稍微调查过一下，\x01",
            "那个猎兵团在业内似乎算得上是声名远播吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xE,
        (
            "#0309F#5P哈哈……\x01",
            "应该是『恶名昭著』才对吧。\x02\x03",

            "#0304F大陆西部最残暴的猎兵团……\x01",
            "蹂躏战场的红色死神……\x02\x03",

            "#0300F就在不久之前，他们好像\x01",
            "还在共和国那边和『黑月』打了一场。\x02\x03",

            "那可是真正意义上的搏命厮杀。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#0008F#5P……是这样吗……\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)
    Sleep(300)

    #C0173
    ChrTalk(
        0xE,
        (
            "#0302F#11P……抱歉，\x01",
            "我并没打算说这么多无聊的废话。\x02\x03",

            "#0303F总之，如果警备队动起了真格，\x01",
            "那我们的处境大概就会相当不妙了。\x02\x03",

            "#0301F另外，如果连传闻中刚刚配备的\x01",
            "那些新型装甲车也被用上的话──\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#0004F#5P──那个，兰迪。\x02\x03",

            "#0002F我之前说过的话……\x01",
            "现在可以收回吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        "#0305F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        (
            "#0000F#5P就是在旧城区赛跑之后说的话。\x02\x03",

            "在变得像大哥那样可以独当一面之前，\x01",
            "不会再问兰迪的过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xE,
        "#0305F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0008F#5P──之前也曾说过，\x01",
            "对我来说，大哥他就是\x01",
            "如同英雄一般的存在。\x02\x03",

            "#0003F科长、达德利警官，\x01",
            "连亚里欧斯先生都这么说过……\x02\x03",

            "#0000F只要有大哥站在那里，\x01",
            "便能够跨越任何逆境——\x01",
            "他就是一个能给人带来如此信心的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xE,
        (
            "#0300F#11P……我想也是呢。\x02\x03",

            "#0306F真是的，他到底是个强到\x01",
            "什么程度的怪物级大哥啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0002F#5P哈哈，我觉得他真正强大的\x01",
            "地方其实并不在于力量呢。\x02\x03",

            "#0006F……一开始呢，\x01",
            "我一直都觉得自己必须要\x01",
            "成为能够替代大哥的人。\x02\x03",

            "否则，我就没有资格\x01",
            "回到克洛斯贝尔……\x02\x03",

            "#0008F在那种想法的驱使之下，\x01",
            "我拼命考取了搜查官资格，\x01",
            "并一直努力到现在……\x02\x03",

            "#0002F可是，我果然还是觉得……\x01",
            "自己在某些地方似乎太过勉强了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xE,
        (
            "#0303F#11P……是吗………\x02\x03",

            "#0300F但是，你好像却\x01",
            "露出了一副轻松释怀的表情啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0012F#5P哈哈，大概吧。\x02\x03",

            "#0004F……想通这点后，\x01",
            "我反而莫名地变得积极乐观了。\x02\x03",

            "我也许并不能成为像大哥那样厉害的人……\x02\x03",

            "#0000F──所以呢，我只需要努力做自己，\x01",
            "按照自己的步伐来慢慢变强……\x01",
            "这样不就足够了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xE,
        "#0305F#11P！\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#0006F#5P哈，虽然还没想清楚\x01",
            "具体要怎样变强……\x02\x03",

            "又要看护琪雅，又要率领着\x01",
            "大家，在这种立场之下，\x01",
            "我是没有时间来烦恼这种事的吧？\x02\x03",

            "#0002F幸运的是，有兰迪和大家帮助我，\x01",
            "我就算不变得那么强，也总能渡过各种难关……\x02\x03",

            "所以，面对目前这种状况，\x01",
            "我想坦率地依赖你们一下呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xE,
        (
            "#0309F#11P哈哈……什么嘛……\x02\x03",

            "#0302F……你这话说得不是已经\x01",
            "足够成熟了吗～\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0004F#5P兰迪，你应该明白的吧？\x02\x03",

            "#0000F如果只是不断追赶着大哥的背影，\x01",
            "我终究会走进死胡同……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xE,
        (
            "#0306F#11P……差不多吧～\x02\x03",

            "#0304F不过，那样一来，你所遭遇的挫折，\x01",
            "对你自身来说也会成为一笔很有价值的财富。\x02\x03",

            "#0302F不过，真没想到你会在\x01",
            "遭遇挫折之前，就自己察觉到了这一点啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#0004F#5P哈哈，如果仅凭我自己，\x01",
            "大概是没法察觉到的吧。\x02\x03",

            "#0002F──所以，在那个时候\x01",
            "为了耍帅而没有问出口的问题，\x01",
            "现在我想正式问一次。\x02\x03",

            "因为我想更加了解某个\x01",
            "像大哥一样，一直都在\x01",
            "默默守护着我，激励我成长的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xE,
        "#0309F#11P#40W………哈哈……………\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1388)
    OP_93(0xE, 0xB4, 0x190)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0xE)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7001", 0)
    SetCameraDistance(14500, 60000)
    Sleep(1000)

    #C0190
    ChrTalk(
        0xE,
        (
            "#0308F#5P──那么，罗伊德。\x02\x03",

            "#0304F你觉得，我至今为止，\x01",
            "在战场上一共杀过多少敌人？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#0006F#5P……这真是无法想象啊。\x02\x03",

            "#0001F兰迪经历过的战场，大概是和我所\x01",
            "生活的这个环境完全不同的世界吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xE,
        (
            "#0312F#5P呵呵，答对了。\x01",
            "说实话，连我自己都数不清了。\x02\x03",

            "#0304F……从我刚懂事开始，\x01",
            "就一直生活在名为战场的世界里。\x02\x03",

            "四岁的时候开始摸刀，\x01",
            "六岁的时候就学会了用手枪射击。\x02\x03",

            "#0303F……初次实战是在九岁。\x01",
            "在父亲的部队里担任侦察兵，\x01",
            "杀死了两名敌人。\x02\x03",

            "然后，十二岁时担任小队长，\x01",
            "十四岁时担任中队长……\x02\x03",

            "#0311F五年间……\x01",
            "就像狗一样在战场四处奔走。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        "#0005F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xE,
        (
            "#0308F#5P……但是，我最后还是逃跑了。\x02\x03",

            "并不是像加尔西亚那个大叔那样，\x01",
            "迎来了光荣的退役……\x02\x03",

            "也不是厌倦了令人作呕的\x01",
            "无休止厮杀……\x02\x03",

            "#0303F只是，好像丢失了什么一样，\x01",
            "充满迷茫地离开了战场。\x02\x03",

            "#0311F感觉自己就像是一个腐烂的死人。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0001F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xE,
        (
            "#0304F#5P自那之后，我就浑浑噩噩地四处游荡，\x01",
            "最后流落到了克洛斯贝尔……\x02\x03",

            "虽然混进了警备队，还算是不错，\x01",
            "但因为拒绝使用来复枪，\x01",
            "所以被那个白痴司令开除出队……\x02\x03",

            "#0308F就在那时，我被科长收留了……\x01",
            "然后，不知为何，就站在了这个地方。\x02\x03",

            "#0312F这就是我……\x01",
            "一个名叫兰道夫·奥兰多的男人。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#0003F#5P兰迪……\x02\x03",

            "#0002F……谢谢，\x01",
            "谢谢你能和我说这些。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x190)
    Sleep(300)

    #C0198
    ChrTalk(
        0xE,
        (
            "#0306F#11P真是的……你这家伙，\x01",
            "该不会是有些Ｍ的倾向吧？\x02\x03",

            "#0308F为什么会想要知道我这种\x01",
            "混账家伙的过去，还要\x01",
            "特意来问呢……\x02\x03",

            "#0301F……可别说你没有想过要回避这个话题啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        (
            "#0004F#5P哈哈……\x01",
            "当初的确是有些想回避这个话题的。\x02\x03",

            "但即使如此，我果然还是\x01",
            "无论如何都想知道呢。\x02\x03",

            "#0000F另外，如果只有兰迪单方面了解我的情况，\x01",
            "而我却对你的过去一无所知，\x01",
            "未免也有点令人不平衡……\x02\x03",

            "#0002F只有彼此之间都了解到一定程度，\x01",
            "才能算是真正的『搭档』吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0200
    ChrTalk(
        0xE,
        "#0305F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#0001F#5P怎么了，兰迪之前不是\x01",
            "也叫了我『搭档』吗？\x02\x03",

            "就在刚才和我打招呼的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xE,
        (
            "#0305F#11P啊，那不过是\x01",
            "我打招呼时随便喊的而已～……\x02\x03",

            "#0301F……咦，对了。\x01",
            "难道说，我以前从来都没有\x01",
            "那样叫过你吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#0002F#5P……大概没有哦。\x02\x03",

            "#0012F那个，所以刚才我还\x01",
            "觉得有点高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    #Sound(1376, 255, 100, 0)    #voice#Randy
    Sleep(150)
    OP_82(0x64, 0x0, 0x7D0, 0x12C)

    #C0204
    ChrTalk(
        0xE,
        (
            "#0309F#11P呵呵……\x01",
            "#4S哈哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0205
    ChrTalk(
        0x101,
        (
            "#0011F#5P也、也不用\x01",
            "笑成那样吧？\x02\x03",

            "#0006F虽然我自己也觉得\x01",
            "稍微有点不好意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xE,
        (
            "#0302F#11P呵呵……只是因为那种理由，\x01",
            "就一直把话题引到这里吗……\x02\x03",

            "#0304F而且还先来段自曝，\x01",
            "然后再把我逼到死胡同……\x02\x03",

            "#0309F哎呀，你是这种类型的吧——先造成\x01",
            "自己是Ｍ的假象，摘下面具后却是个Ｓ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        "#0011F#5P说、说些什么呢……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(801, 0, 100, 0)
    Sleep(500)
    VolumeBGM(0x3C, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──留在大楼内\x01",
            "的各位请注意。\x02",
        )
    )

    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于目前处于非常时期，\x01",
            "所以我们将关闭一部分楼层的\x01",
            "照明系统。\x02",
        )
    )

    CloseMessageWindow()

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "此外，考虑到保安工作的需要，\x01",
            "除了正门入口之外，\x01",
            "其它紧急入口将全部关闭。\x02",
        )
    )

    CloseMessageWindow()

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "请您多加谅解，同时也请小心火源。\x01",
            "对于给您造成的不便，\x01",
            "我们致以诚挚的歉意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    VolumeBGM(0x64, 0x7D0)

    #C0212
    ChrTalk(
        0xE,
        (
            "#0304F#11P看来，终于进入真正的\x01",
            "警戒封锁状态了啊。\x02\x03",

            "#0300F慎重起见，\x01",
            "我准备下到一层，\x01",
            "去正门入口那里看守。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#0000F#5P明白了，那我就来负责\x01",
            "补给工作和装备的检查。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xE,
        "#0302F#11P哦，交给你啦。\x02",
    )

    CloseMessageWindow()

    def lambda_6542():

        label("loc_6542")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_6542")

    QueueWorkItem2(0x101, 2, lambda_6542)
    OP_68(57170, 1500, 860, 2500)
    MoveCamera(119, 22, 0, 2500)
    OP_95(0xE, 58140, 0, -380, 1200, 0x0)
    OP_6F(0x1)

    #C0215
    ChrTalk(
        0xE,
        (
            "#0303F#11P──警备队要是真的攻过来，\x01",
            "战到最后的应该是我们吧。\x02\x03",

            "#0300F我可不想让大小姐和阿缇\x01",
            "做出太过逞强的事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#0004F#5P……嗯，我明白的。\x02\x03",

            "#0000F无论如何，我和兰迪两个人都必须阻止他们，\x01",
            "绝对不能让他们迈进这里半步。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xE,
        (
            "#0302F#11P就是这样。\x02\x03",

            "#0309F我的背后就托付给你啦──搭档。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#0005F#5P啊……\x02\x03",

            "#0002F──了解！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_68(55630, 1500, 13810, 8000)
    MoveCamera(54, 22, 0, 8000)
    OP_6E(550, 8000)
    SetCameraDistance(21500, 8000)
    OP_95(0xE, 58350, 0, 1520, 2000, 0x0)
    OP_95(0xE, 57740, 0, 4190, 2000, 0x0)
    OP_95(0xE, 53180, 0, 8070, 2000, 0x0)
    OP_95(0xE, 53190, 0, 13960, 2000, 0x0)
    OP_95(0xE, 55730, 0, 13960, 2000, 0x0)
    StopBGM(0x2AF8)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)

    def lambda_6797():
        OP_96(0xFE, 0xE4E8, 0x0, 0x3688, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6797)
    Sleep(1000)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    Sleep(600)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    Sleep(500)
    SetMapObjFlags(0x0, 0x10)
    EndChrThread(0xE, 0x1)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68DB")
    Sound(517, 0, 100, 0)
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "罗伊德和兰迪\x01",
            "习得了燃烧之怒Ⅱ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和兰迪的组合战技\x01",
            "『燃烧之怒』得到了强化。\x02",
        )
    )

    CloseMessageWindow()

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "除了攻击力和射程·范围之外，\x01",
            "硬直时间等性能也有了强化。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_68DB")

    OP_CA(0x1, 0xFF, 0x0)
    OP_68(59090, 1500, 360, 0)
    MoveCamera(88, 16, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 59090, 0, 360, 315)
    PlayBGM("ed7513", 0)
    SetScenarioFlags(0xE7, 4)
    OP_DE(0x2F, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_14_49B9 end

    def Function_15_6938(): pass

    label("Function_15_6938")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(171000, 1400, 123500, 0)
    MoveCamera(35, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0xA, 171500, 200, 123500, 270)
    SetChrPos(0xB, 171500, 200, 124400, 270)
    MoveCamera(40, 23, 0, 6000)
    SetCameraDistance(19000, 6000)
    FadeToBright(2000, 0)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(55000, 1200, 125000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 54500, 30, 124600, 0)
    SetChrPos(0x102, 55500, 30, 124600, 0)
    SetChrPos(0x103, 54300, 30, 123500, 0)
    SetChrPos(0x104, 55700, 30, 123500, 0)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x9, 56600, 30, 126100, 315)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_68(55000, 1200, 126500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0222
    ChrTalk(
        0x8,
        "#5P#2803F………………………………\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x9,
        "#2901F#11P……父亲……\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x101,
        (
            "#12P#0006F──这些只是通过现状而推断出的结论，\x01",
            "目前还无法确定。\x02\x03",

            "#0008F所以我觉得，无论如何\x01",
            "都有必要找出充分而确凿的证据……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "#5P#2800F是啊……\x01",
            "从你们的立场来看确实是该这样想吧。\x02\x03",

            "#2806F……可我……\x01",
            "现在只是感到非常失望啊。\x02\x03",

            "『教团』残党的深重罪孽\x01",
            "自不必说……\x02\x03",

            "#2801F而对于被他们趁机利用，\x01",
            "使事态恶化到如此地步的愚蠢之辈，\x01",
            "我真是发自内心地感到震惊与无奈。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#12P#0003F………我理解。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "#5P#2803F而我，因为也明白\x01",
            "克洛斯贝尔目前的状况相当复杂。\x02\x03",

            "所以对于鲁巴彻那种组织的存在也好、\x01",
            "议员和官员们的腐败也好，从某种程度上来说，\x01",
            "都当成了无可奈何的事态，没有做出任何努力去试着改善……\x02\x03",

            "#2801F……现在看来，似乎连我自己\x01",
            "也是个相当愚蠢的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x102,
        "#0108F#12P……叔叔……\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x9,
        (
            "#2903F#11P也是呢……\x02\x03",

            "ＩＢＣ在克洛斯贝尔的政治界\x01",
            "也多少有一些影响力。\x02\x03",

            "#2901F但至今为止，父亲却一直都\x01",
            "保持着中立……\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x8,
        (
            "#5P#2801F这种消极怠惰的态度，\x01",
            "也是引发如今这种事态的原因之一吧。\x02\x03",

            "#2803F……对不起，\x01",
            "现在说什么都无法表达我的歉意。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x101,
        "#12P#0011F没、没那回事啊……\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        (
            "#12P#0306F不，我觉得再怎么说，\x01",
            "您也有点过于自责了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#12P#0200F实际上，您并没有\x01",
            "那么多权限与责任的……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "#5P#2800F不，经济界能对执政当局\x01",
            "产生一定程度的影响，\x01",
            "这本来就是常识啊。\x02\x03",

            "#2803F……而且就算不谈那些，\x01",
            "我以前应该也一直自负为\x01",
            "一名热爱克洛斯贝尔的市民。\x02\x03",

            "#2801F但随着事业逐渐扩大，工作变得忙碌……\x01",
            "那份对家乡的热爱似乎也慢慢淡薄了。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#12P#0008F………………………………\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        (
            "#0106F#12P……我想，我们每个市民\x01",
            "应该都存在这样的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "#5P#2803F是啊……\x02\x03",

            "#2800F……不管怎么说，\x01",
            "在这里发牢骚也于事无补。\x02\x03",

            "为了扭转如今的事态，\x01",
            "我们ＩＢＣ一定会倾尽全部力量，\x01",
            "为你们提供协助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#12P#0002F总裁……\x01",
            "谢谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x102,
        "#0102F#12P……您的话真是令人信心百倍呢。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0240
    ChrTalk(
        0x9,
        (
            "#5P#2906F话虽如此，\x01",
            "但以如今的状况来看，我们还是一筹莫展。\x02\x03",

            "#2901F和警察局总部，还有唐古拉姆门\x01",
            "的联络好像都已经中断了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_71A9():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71A9)
    Sleep(50)

    def lambda_71B9():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71B9)
    Sleep(50)

    def lambda_71C9():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_71C9)
    Sleep(150)

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#0006F是的……\x01",
            "虽然尝试着联络过很多次。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x103,
        (
            "#6P#0206F……似乎是由于某种原因，\x01",
            "导致通讯被干扰了。\x02\x03",

            "#0201F能否尝试利用导力网络\x01",
            "来联络呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x9,
        (
            "#5P#2903F……目前来看，\x01",
            "地下空间的导力缆线\x01",
            "似乎已经被某些人阻断了呢。\x02\x03",

            "#2901F如果能建立起一条迂回线路，\x01",
            "我想应该可以将通讯网恢复……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)

    #C0244
    ChrTalk(
        0x8,
        (
            "#5P#2801F那么，就将此事定为\x01",
            "技术部的最优先任务。\x02\x03",

            "#2803F与警察局总部、唐古拉姆门，\x01",
            "还有游击士协会的联络自不必说……\x02\x03",

            "#2800F另外，如果能与市内的各处终端取得联络，\x01",
            "应该也有助于我们进一步把握状况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)

    #C0245
    ChrTalk(
        0x9,
        "#2902F#11P明白了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0246
    ChrTalk(
        0x8,
        (
            "#5P#2801F还有……\x01",
            "另一个让人担心的问题就是琪雅吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7420():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7420)
    Sleep(50)

    def lambda_7430():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7430)
    Sleep(50)

    def lambda_7440():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7440)
    Sleep(50)

    def lambda_7450():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7450)
    Sleep(200)

    #C0247
    ChrTalk(
        0x101,
        (
            "#12P#0008F是的……\x02\x03",

            "#0013F……那些被操纵的警备队\x01",
            "之所以会如此执著地追击我们，\x01",
            "目的很有可能就是夺取琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        (
            "#12P#0303F实际上，他们在对我们开枪时，\x01",
            "所进行的几乎都是威吓性射击。\x02\x03",

            "#0301F而对殿后的科长他们，\x01",
            "其攻击却是毫不留情。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        (
            "#12P#0203F在绝对不能伤害到琪雅\x01",
            "的前提下将她夺走……\x02\x03",

            "#0201F……他们被操纵时，\x01",
            "行动模式恐怕就是被设定成这样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "#5P#2904F嗯，琪雅这么可爱，\x01",
            "也不难理解对方为什么想夺走她了。\x02\x03",

            "#2901F那个人是叫约亚西姆吧？\x01",
            "真是个非常诡异的男人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#12P#0006F嗯……\x01",
            "说实话，他究竟在想些什么，\x01",
            "目前我们还没有明确了解。\x02\x03",

            "#0008F他为什么必须夺走琪雅……\x02\x03",

            "#0013F白色相册中最后的那张照片\x01",
            "到底是在哪里拍摄的……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#0106F#12P……最重要的是，琪雅为什么\x01",
            "会出现在那个竞拍会的会场，\x01",
            "这些疑问我们都还没弄清楚。\x02\x03",

            "#0108F如果那个孩子恢复了记忆，\x01",
            "或许还能得到一些线索，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        "#5P#2901F原来如此……这还真是让人心急啊。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x8,
        (
            "#5P#2803F不管怎么说，引起如今这种\x01",
            "事态的人物应该就是他。\x02\x03",

            "所以，他一定是个异常危险的男人，\x01",
            "关于这一点，还是不要怀疑为好。\x02\x03",

            "#2801F你们藏身在ＩＢＣ大厦内这件事，\x01",
            "他应该无法轻易查出……\x02\x03",

            "但凡事就怕万一，\x01",
            "所以至少得做好心理准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#12P#0013F……是。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x104,
        "#12P#0301F也是啊……\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "#5P#2804F至于和各地的联络工作，\x01",
            "我会让ＩＢＣ的员工继续进行。\x02\x03",

            "琪雅她们已经去休息了，\x01",
            "你们也稍微休息一下吧。\x02\x03",

            "#2800F需要给你们准备床铺吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#12P#0002F啊，这倒不用……\x01",
            "好意心领了。\x02\x03",

            "#0000F比起那个，这座大楼内\x01",
            "有没有可以进行补给的地方呢？\x02\x03",

            "目前的装备似乎有些不足……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x104,
        (
            "#12P#0306F确实，刚才突然遭到袭击，\x01",
            "实在是需要进行补给啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "#5P#2800F那么，就去一层的服务柜台吧，\x01",
            "我会预先安排一下，让那里\x01",
            "提供各项服务的。\x02\x03",

            "各制造商的分公司也都在大厦里，\x01",
            "所以武器的购买应该不成问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "#5P#2902F而爱普斯泰恩财团也在这里，\x01",
            "所以工房服务项目也可以使用吧……\x02\x03",

            "为了应对紧急情况，\x01",
            "食材应该也有足够的储备。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x102,
        "#0102F#12P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x103,
        (
            "#12P#0202F确实，感觉这栋大厦里\x01",
            "似乎备有各种物品呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        (
            "#12P#0309F哎呀，真不愧是\x01",
            "天下闻名的ＩＢＣ大厦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#12P#0004F……感谢您如此费心。\x02\x03",

            "#0002F那么，我们就暂时\x01",
            "休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "队伍暂时解散。\x02",
        )
    )

    CloseMessageWindow()

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "与一层服务柜台的接待员谈话，\x01",
            "即可与各类商店进行交易。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "另外，此时也可以\x01",
            "继续调整队伍外成员的\x01",
            "装备·回路。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetMapFlags(0x10000)
    OP_68(53000, 1500, 45000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 53000, 0, 45000, 180)
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x8)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 59090, 30, 124780, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D5D")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D96")

    label("loc_7D5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D7C")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7D96")

    label("loc_7D7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x79), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7D96")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7DB5")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7DEE")

    label("loc_7DB5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7DD4")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7DEE")

    label("loc_7DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7A), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7DEE")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7DEE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7E0D")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E46")

    label("loc_7E0D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7E2C")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7E46")

    label("loc_7E2C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7B), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7E46")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_END)), "loc_7E5B")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_END)), "loc_7E70")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_7E85")
    OP_50(0x65, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_END)), "loc_7E9A")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_END)), "loc_7EAF")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_7EC4")
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_END)), "loc_7ED9")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_END)), "loc_7EEE")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_7F03")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F03")

    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F4B")
    ClearChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x7)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xC, 0x10)
    SetChrPos(0xC, 59090, 0, -1070, 135)
    Jump("loc_7F82")

    label("loc_7F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F69")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_7F82")

    label("loc_7F69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_DA(0x41)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F82")
    ClearChrFlags(0xE, 0x80)

    label("loc_7F82")

    SetScenarioFlags(0xE3, 7)
    OP_C7(0x0, 0x1000)
    EventEnd(0x5)
    Return()

    # Function_15_6938 end

    def Function_16_7F8E(): pass

    label("Function_16_7F8E")

    EventBegin(0x0)
    Fade(1000)
    OP_68(171500, 900, 122600, 0)
    MoveCamera(50, 24, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 171000, 0, 121600, 0)
    OP_0D()
    Sleep(500)

    #C0269
    ChrTalk(
        0xA,
        "#5P#1113F#80W……呼～呼～………\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#11P#0002F（哈哈……\x01",
            "  好像睡得很香呢……）\x02\x03",

            "#0004F（这也难怪……\x01",
            "  毕竟长途跋涉了那么久……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)

    def lambda_806C():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_806C)
    WaitChrThread(0xA, 2)
    Sleep(500)

    #C0271
    ChrTalk(
        0xA,
        (
            "#5P#1114F#80W……嗯嗯………\x02\x03",

            "#70W……罗伊德……你在哪里……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetCameraDistance(21000, 30000)

    #C0272
    ChrTalk(
        0xA,
        (
            "#1P#1114F#60W#5P艾莉……缇欧……\x01",
            "……兰迪……\x02\x03",

            "……好黑……好黑啊……\x02\x03",

            "在哪里……你们去哪里了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#11P#0001F（……琪雅………）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(820, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德轻轻抚摸了琪雅的头。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(300)

    #C0275
    ChrTalk(
        0x101,
        (
            "#11P#0004F……没事的，\x01",
            "我们绝对会保护好你。\x02\x03",

            "#0002F所以，琪雅……请安下心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        (
            "#5P#1113F#70W………嗯…………\x02\x03",

            "#5P#1104F#70W……………呼………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0277
    ChrTalk(
        0x101,
        (
            "#11P#0008F（至今为止，我们连自己的事\x01",
            "  都自顾不暇了，但是……）\x02\x03",

            "#0004F（如今……我终于有些明白了。）\x02\x03",

            "（自己究竟是为了什么才回到克洛斯贝尔，\x01",
            "  为了什么才以搜查官为目标……）\x02\x03",

            "#0002F（……大哥当年也跟我一样吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(169830, 1400, 121000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 169830, 0, 121000, 270)
    SetScenarioFlags(0xE4, 0)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_16_7F8E end

    def Function_17_83BE(): pass

    label("Function_17_83BE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08700.itc", 0x1F)
    SoundLoad(806)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    ClearMapFlags(0x10000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01100.itp")
    OP_68(55000, 1000, 128000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 55000, 30, 118000, 0)
    SetChrPos(0x102, 56200, 30, 125800, 90)
    SetChrPos(0x103, 54500, 30, 117000, 0)
    SetChrPos(0x104, 55600, 30, 117000, 0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 55000, 150, 128800, 180)
    SetChrPos(0x9, 57800, 30, 126400, 270)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    SetCameraDistance(18500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0278
    ChrTalk(
        0x101,
        "#0001F──打扰了。\x02",
    )

    CloseMessageWindow()
    OP_68(55000, 1000, 126500, 2000)

    def lambda_8519():
        OP_95(0xFE, 55000, 0, 124100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8519)
    Sleep(200)

    def lambda_8536():

        label("loc_8536")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_8536")

    QueueWorkItem2(0x102, 2, lambda_8536)
    Sleep(100)

    def lambda_854B():

        label("loc_854B")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_854B")

    QueueWorkItem2(0x9, 2, lambda_854B)
    Sleep(1200)

    #C0279
    ChrTalk(
        0x102,
        "#5P#0101F罗伊德……！\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        "#5P#2800F哦，你来了啊。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)

    #C0281
    ChrTalk(
        0x101,
        "#12P#0001F究竟发生了什么事？\x02",
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#5P#2803F嗯，好像是有两名警备队的队员\x01",
            "来到了大门前。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0283
    ChrTalk(
        0x101,
        "#12P#0013F然后呢……！？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        (
            "#11P#2903F现在倒是还没有发动攻击，\x01",
            "只是停留在原地而已。\x02\x03",

            "#2901F反正大门是由特殊合金制造而成，\x01",
            "想突破进来恐怕也很难吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        (
            "#12P#0006F是吗……\x02\x03",

            "#0008F……我们藏身于此的事情\x01",
            "很可能已经暴露了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        "#5P#0106F……嗯嗯……\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)

    #C0287
    ChrTalk(
        0x103,
        "#0201F……打扰了。\x02",
    )

    CloseMessageWindow()

    def lambda_8739():
        OP_95(0xFE, 55600, 30, 122600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8739)

    def lambda_8753():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8753)
    Sleep(150)

    def lambda_8767():
        OP_95(0xFE, 54500, 30, 122500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8767)

    def lambda_8781():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8781)
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0288
    ChrTalk(
        0x101,
        "#5P#0005F缇欧、兰迪。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)

    #C0289
    ChrTalk(
        0x104,
        (
            "#12P#0301F听说警备队员\x01",
            "已经来到大门前了？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#5P#0001F是啊，不过，目前看来，\x01",
            "他们好像还没采取任何行动……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_88CC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88CC)

    def lambda_88D9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_88D9)

    def lambda_88E6():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_88E6)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(500)

    #C0291
    ChrTalk(
        0x8,
        (
            "#5P#2801F──是我。\x02\x03",

            "#2805F……什么……\x02\x03",

            "#2803F……嗯……嗯……\x02\x03",

            "………………………………\x02\x03",

            "#2801F………怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        "#12P#0001F（……怎么了……？）\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        "#0108F（有种不祥的预感呢……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(300)

    #C0294
    ChrTalk(
        0x8,
        (
            "#5P#2803F……据说大门之前的警备队员\x01",
            "开始了可疑的举动。\x02\x03",

            "#2801F似乎是在安置某种\x01",
            "圆筒状的装置……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x103,
        "#12P#0201F难道……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x104,
        "#12P#0307F是定向导力炸弹吗！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_8B0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8B0F)
    Sleep(50)

    def lambda_8B1F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8B1F)
    Sleep(50)

    def lambda_8B2F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8B2F)

    #C0297
    ChrTalk(
        0x101,
        "#5P#0011F那、那是什么东西啊！？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#12P#0301F是在军队中用来进行\x01",
            "爆破作业的导力炸弹！\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#12P#0206F即使是用特殊合金制造\x01",
            "的大门，恐怕也很难撑过那种爆炸吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        "#5P#0101F怎么会……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        "#5P#2801F可恶，还有那种东西吗……\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "#11P#2901F……都已经被操纵了，\x01",
            "竟然还保持着相当的理性呢。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    #C0303
    ChrTalk(
        0x101,
        (
            "#5P#0003F──没办法了。\x02\x03",

            "#0000F兰迪，我们出去迎击吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x104,
        (
            "#12P#0304F是啊……\x01",
            "看来也只有如此了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_8D21():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8D21)

    #C0305
    ChrTalk(
        0x8,
        "#5P#2805F罗伊德……！？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x9,
        (
            "#11P#2910F你们……\x01",
            "难道想去白白送死吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#0000F不，只是阻止他们\x01",
            "安装导力炸弹而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#12P#0309F哈，不过我感觉多少\x01",
            "也会遭遇到一点小冲突啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        "#5P#0100F当然，我们也要去哦。\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        "#12P#0202F身为支援科成员之一，这是当然的。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯……\x01",
            "那援护工作就交给你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x9,
        "#11P#2901F艾莉、缇欧……\x02",
    )

    CloseMessageWindow()

    def lambda_8E8D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8E8D)
    Sleep(100)
    TurnDirection(0x103, 0x9, 500)
    Sleep(200)

    #C0313
    ChrTalk(
        0x102,
        (
            "#6P#0109F呵呵……\x01",
            "这是我的工作啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#12P#0204F……不必担心。\x02",
    )

    CloseMessageWindow()

    def lambda_8EED():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8EED)
    Sleep(150)

    def lambda_8EFD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8EFD)
    Sleep(50)
    TurnDirection(0x103, 0x8, 500)
    Sleep(200)

    #C0315
    ChrTalk(
        0x101,
        (
            "#12P#0004F当然，我们也没有打算\x01",
            "要去白白送死。\x02\x03",

            "#0000F只是在警察局总部或副司令的部队……\x01",
            "在他们的增援到来之前，先坚持一下而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#12P#0300F在门前的话，地形也对我们有利。\x02\x03",

            "总之，就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#5P#2803F……明白了。\x02\x03",

            "#2801F愿女神保佑你们──\x01",
            "请万分小心！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(52700, 1100, 45900, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 52200, 0, 46500, 180)
    SetChrPos(0x102, 53200, 0, 46500, 180)
    SetChrPos(0x103, 52200, 0, 46500, 180)
    SetChrPos(0x104, 53200, 0, 46500, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 52700, 0, 46500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0xA, 56500, 0, 38800, 270)
    SetChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xB, 56500, 0, 38800, 270)
    SetChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(52700, 1100, 39800, 4000)

    def lambda_9195():
        OP_96(0xFE, 0xCB84, 0x0, 0x9B78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9195)

    def lambda_91AF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_91AF)
    Sleep(400)

    def lambda_91C3():
        OP_96(0xFE, 0xD034, 0x0, 0x9B78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91C3)

    def lambda_91DD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_91DD)
    Sleep(400)

    def lambda_91F1():
        OP_96(0xFE, 0xCB84, 0x0, 0x9FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_91F1)

    def lambda_920B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_920B)
    Sleep(400)

    def lambda_921F():
        OP_96(0xFE, 0xD034, 0x0, 0x9FC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_921F)

    def lambda_9239():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9239)
    Sleep(700)

    def lambda_924D():
        OP_96(0xFE, 0xCDDC, 0x0, 0xA604, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_924D)

    def lambda_9267():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9267)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_92C1():

        label("loc_92C1")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_92C1")

    QueueWorkItem2(0x101, 2, lambda_92C1)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_92EF():

        label("loc_92EF")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_92EF")

    QueueWorkItem2(0x102, 2, lambda_92EF)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_931D():

        label("loc_931D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_931D")

    QueueWorkItem2(0x103, 2, lambda_931D)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_934B():

        label("loc_934B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_934B")

    QueueWorkItem2(0x104, 2, lambda_934B)

    def lambda_935D():

        label("loc_935D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_935D")

    QueueWorkItem2(0x9, 2, lambda_935D)
    Sleep(1000)
    OP_79(0x1)
    OP_79(0x2)
    WaitChrThread(0x9, 1)
    OP_6F(0x1)
    Fade(500)
    OP_68(53200, 1100, 39730, 0)
    MoveCamera(67, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)

    def lambda_93B1():
        OP_95(0xFE, 54100, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_93B1)

    def lambda_93CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_93CB)
    Sound(2040, 255, 100, 0)    #voice#KeA
    WaitChrThread(0xA, 2)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)
    OP_93(0xA, 0x12C, 0x1F4)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0318
    AnonymousTalk(
        0xA,
        "#40W……罗伊德，你们要去哪里啊～？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0319
    ChrTalk(
        0x101,
        "#6P#0005F琪雅……\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        (
            "#5P#0309F哈哈……\x01",
            "稍微有一点工作啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xA,
        (
            "#11P#1100F嗯……\x02\x03",

            "#1109F能不能也带琪雅一起去？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x102,
        "#5P#0108F这、这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x103,
        "#6P#0208F……那个……\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#6P#0003F……不行不行，\x01",
            "都这么晚了，小孩子应该睡觉了吧？\x02\x03",

            "#0000F你看小滴，不是都已经\x01",
            "乖乖睡着了──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_95A7():
        OP_95(0xFE, 55200, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_95A7)

    def lambda_95C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_95C1)
    WaitChrThread(0xB, 1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_9621():

        label("loc_9621")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_9621")

    QueueWorkItem2(0x102, 2, lambda_9621)

    def lambda_9633():

        label("loc_9633")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_9633")

    QueueWorkItem2(0x103, 2, lambda_9633)
    WaitChrThread(0xB, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    OP_93(0xB, 0x12C, 0x1F4)

    #C0325
    ChrTalk(
        0x102,
        "#5P#0105F……小滴。\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x104,
        "#5P#0306F……是被我们吵醒的吗？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xB,
        (
            "#11P#6005F对、对不起……\x01",
            "不知不觉就醒了……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        (
            "#6P#0002F哪里……\x01",
            "是我们吵到你了，抱歉。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(300)

    #C0329
    ChrTalk(
        0x101,
        (
            "#12P#0003F──玛丽亚贝尔小姐，\x01",
            "这两个孩子就拜托你了。\x02\x03",

            "#0000F请务必把她们哄睡着。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(150)

    #C0330
    ChrTalk(
        0x9,
        "#2904F#5P……好的，我明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_9783():

        label("loc_9783")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_9783")

    QueueWorkItem2(0x101, 2, lambda_9783)
    OP_68(53790, 1100, 39870, 1000)

    def lambda_97A6():
        OP_95(0xFE, 54700, 0, 41500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_97A6)
    WaitChrThread(0x9, 1)

    def lambda_97C4():
        OP_95(0xFE, 54700, 0, 40000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_97C4)
    WaitChrThread(0x9, 1)
    OP_6F(0x1)

    #C0331
    ChrTalk(
        0x9,
        (
            "#5P#2902F──好了，你们两个，\x01",
            "我去给你们泡些热可可，\x02\x03",

            "喝完以后就早点休息吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9836():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9836)
    Sleep(50)
    TurnDirection(0xB, 0x9, 500)

    #C0332
    ChrTalk(
        0xA,
        "#11P#1112F哎、哎……\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xB,
        "#11P#6008F………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 5000)
    BeginChrThread(0xB, 3, 0, 18)
    BeginChrThread(0xA, 3, 0, 19)
    BeginChrThread(0x9, 3, 0, 20)

    def lambda_98AA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_98AA)
    Sleep(50)

    def lambda_98BA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_98BA)
    Sleep(50)

    def lambda_98CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_98CA)
    Sleep(50)

    def lambda_98DA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_98DA)
    WaitChrThread(0x101, 2)

    def lambda_98EB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98EB)
    Sleep(50)

    def lambda_9908():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9908)
    Sleep(50)

    def lambda_9925():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9925)
    Sleep(50)

    def lambda_9942():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9942)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x9, 3)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7513", "ed7512")
    OP_24(0x326)
    SetScenarioFlags(0x5C, 0)
    NewScene("c133B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_83BE end

    def Function_18_99AE(): pass

    label("Function_18_99AE")


    def lambda_99B3():
        OP_95(0xFE, 56500, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_99B3)
    Sleep(300)

    def lambda_99D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_99D0)
    WaitChrThread(0xB, 1)
    Return()

    # Function_18_99AE end

    def Function_19_99E1(): pass

    label("Function_19_99E1")

    OP_93(0xA, 0x12C, 0x1F4)
    Sleep(500)

    def lambda_99F0():
        OP_96(0xFE, 0xDCB4, 0x0, 0x9790, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_99F0)
    Sleep(500)

    def lambda_9A0D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9A0D)
    WaitChrThread(0xA, 1)
    Return()

    # Function_19_99E1 end

    def Function_20_9A1E(): pass

    label("Function_20_9A1E")

    Sleep(900)

    def lambda_9A26():
        OP_95(0xFE, 55200, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9A26)
    WaitChrThread(0x9, 1)

    def lambda_9A44():
        OP_95(0xFE, 56500, 0, 38800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9A44)
    Sleep(300)

    def lambda_9A61():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9A61)
    WaitChrThread(0x9, 1)
    Return()

    # Function_20_9A1E end

    def Function_21_9A72(): pass

    label("Function_21_9A72")

    TalkBegin(0xFF)
    SetChrName("")

    #A0334
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
    TalkEnd(0xFF)
    Return()

    # Function_21_9A72 end

    SaveToFile()

Try(main)
