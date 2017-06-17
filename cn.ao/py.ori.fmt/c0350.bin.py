from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0350.bin",                # FileName
        "c0350",                    # MapName
        "c0350",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0350",                  # 0
        "尤利",                   # 1
        "塞克斯",                 # 2
        "瑞吉",                   # 3
        "女公关",                 # 4
        "女公关",                 # 5
        "女公关",                 # 6
        "女公关",                 # 7
    ))

    AddCharChip((
        "chr/ch44100.itc",                   # 00
        "chr/ch47500.itc",                   # 01
        "chr/ch23600.itc",                   # 02
        "chr/ch44102.itc",                   # 03
        "chr/ch26802.itc",                   # 04
        "chr/ch26900.itc",                   # 05
    ))

    DeclNpc(7989,    200,     1600,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5699,    0,       469,     45,   261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7780,    0,       -810,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(7989,    200,     2200,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(2309,    0,       3529,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(6270,    0,       1580,    1000,    7990,    1500,    2200,    0x007E, 0,  11, 0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_2CB",          # 02, 2
        "Function_3_6FA",          # 03, 3
        "Function_4_7B2",          # 04, 4
        "Function_5_133D",         # 05, 5
        "Function_6_14CF",         # 06, 6
        "Function_7_15BB",         # 07, 7
        "Function_8_1D0F",         # 08, 8
        "Function_9_1D92",         # 09, 9
        "Function_10_1EF9",        # 0A, 10
        "Function_11_25E3",        # 0B, 11
        "Function_12_25E7",        # 0C, 12
        "Function_13_2659",        # 0D, 13
        "Function_14_26E0",        # 0E, 14
        "Function_15_3381",        # 0F, 15
        "Function_16_4641",        # 10, 16
        "Function_17_4685",        # 11, 17
        "Function_18_46DD",        # 12, 18
        "Function_19_4728",        # 13, 19
        "Function_20_4780",        # 14, 20
        "Function_21_47CB",        # 15, 21
        "Function_22_47FB",        # 16, 22
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_94(0xFE, 0x334, 0x2904, 0xFFFFF31C, 0x3804, 0x3E8)
    Sleep(300)
    Jump("Function_1_2A0")

    label("loc_2CA")

    Return()

    # Function_1_2A0 end

    def Function_2_2CB(): pass

    label("Function_2_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_31B")

    Jump("loc_6B8")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_367")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_397")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3DE")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_6B8")

    label("loc_3DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3FB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_3FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_442")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 8119, 0, -2400, 135)
    Jump("loc_6B8")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_45F")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_45F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47C")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CB")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, -2370, 4000, 13480, 90)
    SetChrPos(0xA, -840, 4000, 13480, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C6")
    SetChrFlags(0xFE, 0x10)

    label("loc_4C6")

    Jump("loc_6B8")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_516")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 1000, 0, 3700, 270)
    SetChrPos(0xA, -500, 0, 3700, 90)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    Jump("loc_6B8")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5BD")
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_569")
    SetChrPos(0x9, -1100, 4000, 12070, 90)
    BeginChrThread(0x9, 0, 0, 1)
    SetChrPos(0xA, 6510, 0, -2040, 180)
    Jump("loc_5B8")

    label("loc_569")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B8")
    SetChrPos(0x8, 7140, 4500, 5660, 180)
    SetChrPos(0x9, 7910, 0, -1840, 90)
    SetChrPos(0xA, 5410, 4000, 5440, 90)
    Jump("loc_5B8")

    label("loc_5B8")

    Jump("loc_6B8")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5DA")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_6B8")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6A0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_69B")

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_69B")

    label("loc_61D")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_65D")

    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0x8, 0x2)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0x9, 1000, 0, 3730, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A")
    SetChrFlags(0x9, 0x10)

    label("loc_68A")

    SetChrPos(0xA, 8060, 0, -2310, 135)

    label("loc_69B")

    Jump("loc_6B8")

    label("loc_6A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6B8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6CC")
    ClearScenarioFlags(0x22, 0)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_6CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F9")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_6F9")

    Return()

    # Function_2_2CB end

    def Function_3_6FA(): pass

    label("Function_3_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73F")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_73F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_77A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_77A")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E")
    Jump("loc_7B1")

    label("loc_79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AD")
    Jump("loc_7B1")

    label("loc_7AD")

    OP_66(0x0, 0x1)

    label("loc_7B1")

    Return()

    # Function_3_6FA end

    def Function_4_7B2(): pass

    label("Function_4_7B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7C3")
    Jump("loc_1339")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_80C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")
    Call(0, 5)
    Jump("loc_807")

    label("loc_7DE")


    #C0001
    ChrTalk(
        0xFE,
        (
            "可恶……\x01",
            "我们为何会遭遇这种事情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_807")

    Jump("loc_1339")

    label("loc_80C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_95B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E0")

    #C0002
    ChrTalk(
        0xFE,
        (
            "共和国政府已经下达了通知，\x01",
            "要我们尽早离开克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "哼，但我无论如何\x01",
            "也不想坐那种\x01",
            "人挤人的列车回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "拿回被扣留的驾照之后，\x01",
            "我们就可以买辆新车，\x01",
            "悠哉悠哉地开回国了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_956")

    label("loc_8E0")


    #C0005
    ChrTalk(
        0xFE,
        (
            "我无论如何\x01",
            "也不想坐那种\x01",
            "人挤人的列车回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "拿回被扣留的驾照之后，\x01",
            "我们就可以买辆新车，\x01",
            "悠哉悠哉地开回国了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_956")

    Jump("loc_1339")

    label("loc_95B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_ABD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5C")

    #C0007
    ChrTalk(
        0xFE,
        (
            "听说在之前那起袭击事件中，\x01",
            "警察局和警备队\x01",
            "遭受到了惨重损失呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "嘿嘿嘿……真痛快。\x01",
            "竟敢对我们无礼，\x01",
            "这下遭到天谴了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00103F（……我们走吧，\x01",
            "  没空理会这种人。）\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10300F（呼，对蠢人说什么\x01",
            "  都是无济于事的。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AB8")

    label("loc_A5C")


    #C0011
    ChrTalk(
        0xFE,
        (
            "听说在之前那起袭击事件中，\x01",
            "警察局和警备队\x01",
            "遭受到了惨重损失呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "嘿嘿嘿……真痛快。\x02",
    )

    CloseMessageWindow()

    label("loc_AB8")

    Jump("loc_1339")

    label("loc_ABD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C69")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_BC2")

    #C0013
    ChrTalk(
        0xFE,
        (
            "哼，既然遭到了处罚，\x01",
            "这段时间就老实些好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "……你们赶快到别处去，\x01",
            "我可没空搭理你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        (
            "#10100F（凯特巡警当时的怒斥\x01",
            "  好像很有效果呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00004F（嗯……\x01",
            "  他们暂时应该不会再做蠢事了，\x01",
            "  总算可以松一口气。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C61")

    label("loc_BC2")


    #C0017
    ChrTalk(
        0xFE,
        "……干什么？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "我可没空\x01",
            "理会警察。\x01",
            "……快出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00005F（发生什么事了吗……？）\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        (
            "#10105F（说起来，一直停在门外的\x01",
            "  那辆导力车似乎不见了……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C61")

    SetScenarioFlags(0x0, 0)
    Jump("loc_C98")

    label("loc_C69")


    #C0021
    ChrTalk(
        0xFE,
        (
            "……你们赶快到别处去，\x01",
            "我可没空搭理你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C98")

    Jump("loc_1339")

    label("loc_C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CAB")
    Jump("loc_1339")

    label("loc_CAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D1B")

    #C0022
    ChrTalk(
        0xFE,
        (
            "啧，瑞吉那家伙除了开车之外，\x01",
            "什么事情都做不好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "不过就是泡杯红茶而已，\x01",
            "就不能快点吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1339")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D29")
    Jump("loc_1339")

    label("loc_D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_D37")
    Jump("loc_1339")

    label("loc_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE4")

    #C0024
    ChrTalk(
        0xFE,
        (
            "我们今天准备\x01",
            "去欢乐街的\x01",
            "『诺艾·布朗』玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "哼哼，像你们这样的庶民，\x01",
            "和那种高档店永远无缘啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#00012F（其、其实还真是说错了呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E21")

    label("loc_DE4")


    #C0027
    ChrTalk(
        0xFE,
        (
            "……话说回来，塞克斯和瑞吉\x01",
            "好慢啊，他们到底在干什么……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E21")

    Jump("loc_1339")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1025")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAC")

    #C0028
    ChrTalk(
        0xFE,
        "……这么晚来，要干什么？\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "你们白天干的好事……\x01",
            "可别说已经忘记了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10A,
        (
            "#00605F（你们几个……\x01",
            "  与他们发生过什么矛盾吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00306F（哎，这个嘛……\x01",
            "  只能说是没办法的事……）\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x10A,
        (
            "#00603F（真是的……在这种敏感时期，\x01",
            "  不要引起无谓的纠纷啊。）\x02\x03",

            "#00600F（在明天的正式会议结束之前，\x01",
            "  绝对不能有丝毫松懈。\x01",
            "  ……知道了吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00005F（明、明白了。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x149, 3)
    Jump("loc_1020")

    label("loc_FAC")


    #C0034
    ChrTalk(
        0xFE,
        (
            "你们白天干的好事……\x01",
            "可别说已经忘记了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "有朝一日，一定会让你们后悔的。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#00306F（真是纠缠不休啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_1020")

    Jump("loc_1339")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12B3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")

    #C0037
    ChrTalk(
        0xFE,
        (
            "你们竟敢这样对待我……\x01",
            "可别想轻易了结。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "不过就是些自治州的小警察，\x01",
            "未免也太得意忘形了吧……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10E1")

    label("loc_10B4")


    #C0039
    ChrTalk(
        0xFE,
        (
            "你们竟敢这样对待我……\x01",
            "可别想轻易了结。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E1")

    Jump("loc_12AE")

    label("loc_10E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1225")

    #C0040
    ChrTalk(
        0xFE,
        (
            "……可恶……\x01",
            "竟敢这样对待我……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "你们几个……\x01",
            "……可别想轻易了结……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x1A3,
        (
            "#04609F啊哈哈，实力那么弱，\x01",
            "又何必在嘴上逞强嘛～\x02\x03",

            "#04604F也罢，如果你们想报仇，\x01",
            "我随时都可以奉陪。\x02\x03",

            "#04611F不过，可要做好被杀的觉悟哟¤\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        "……呜……！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#00303F……够了，谢莉，我们走吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_125D")

    label("loc_1225")


    #C0045
    ChrTalk(
        0xFE,
        (
            "……可恶……\x01",
            "竟敢这样对待我……\x01",
            "绝对不能原谅……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125D")

    Jump("loc_12AE")

    label("loc_1262")


    #C0046
    ChrTalk(
        0xFE,
        (
            "哼哼，竟然擅自闯入\x01",
            "我们的城堡。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "这点小小的惩罚\x01",
            "也是理所当然的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AE")

    Jump("loc_1339")

    label("loc_12B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12C1")
    Jump("loc_1339")

    label("loc_12C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1330")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E4")
    Call(0, 6)
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_12E4")


    #C0048
    ChrTalk(
        0xFE,
        "你们怎么还没走？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "哼，工作已经完成了吧？\x01",
            "赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0x8, 0x2)
    Return()

    label("loc_1330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1339")

    label("loc_1339")

    TalkEnd(0xFE)
    Return()

    # Function_4_7B2 end

    def Function_5_133D(): pass

    label("Function_5_133D")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0050
    ChrTalk(
        0x9,
        "喂！外面到处都是怪物啊！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        (
            "那些家伙该不会\x01",
            "袭击我们吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        "怎、怎么办啊！？尤利！！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "我、我正在想办法啊，你快闭嘴！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "可恶……\x01",
            "我们为何会遭遇这种事情……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14B4")

    #C0055
    ChrTalk(
        0x101,
        (
            "#00005F（『高贵之血』……\x01",
            "  还滞留在克洛斯贝尔啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#00200F（他们似乎错过了\x01",
            "  返回共和国的时机呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00303F（算了，既然都在屋子里，\x01",
            "  不管他们也没什么问题。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B4")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_133D end

    def Function_6_14CF(): pass

    label("Function_6_14CF")


    #C0058
    ChrTalk(
        0xB,
        (
            "话说回来，你们这么年轻，\x01",
            "却住在这么大的房子里，\x01",
            "真是了不起啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        "呵呵，这算什么。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "和我在共和国的家相比，\x01",
            "这里不过就是间小狗窝罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        "#10105F（小、小狗窝……）\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#10309F（哈哈，真是相当\x01",
            "  得意忘形呢。）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_6_14CF end

    def Function_7_15BB(): pass

    label("Function_7_15BB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15CC")
    Jump("loc_1D0B")

    label("loc_15CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E7")
    Call(0, 5)
    Jump("loc_1642")

    label("loc_15E7")


    #C0063
    ChrTalk(
        0xFE,
        "啊啊！真是够了！到底是怎么回事啊！？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "要是我们遭到袭击了，\x01",
            "谁来承担这个责任啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1642")

    Jump("loc_1D0B")

    label("loc_1647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16D4")

    #C0065
    ChrTalk(
        0xFE,
        (
            "独立宣言吗？\x01",
            "说起来，从前一段时间开始，\x01",
            "好像就一直在闹腾什么独立了……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "算了，反正尤利说不会有事，\x01",
            "应该没什么问题的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1773")

    #C0067
    ChrTalk(
        0xFE,
        (
            "唉，最近这段时间，\x01",
            "市里的气氛变得很阴沉，\x01",
            "真是受不了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "好，我们就去\x01",
            "外面兜兜风吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "唉，不过……\x01",
            "已经没有车了呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17C8")

    label("loc_1773")


    #C0070
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "车已经坏了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "本想开车兜风，\x01",
            "转换一下心情……\x01",
            "但现在也只能忍耐了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C8")

    Jump("loc_1D0B")

    label("loc_17CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1822")

    #C0072
    ChrTalk(
        0xFE,
        (
            "唉，那辆导力车\x01",
            "是坐起来最爽的……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "暂时可能都会很无聊了吧……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_1822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1830")
    Jump("loc_1D0B")

    label("loc_1830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1893")

    #C0074
    ChrTalk(
        0xFE,
        (
            "嘿嘿，最近兜风的那条路线\x01",
            "真是太棒了。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        "比起市内，还是到郊外兜风的感觉更爽。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_1893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18A1")
    Jump("loc_1D0B")

    label("loc_18A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18AF")
    Jump("loc_1D0B")

    label("loc_18AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1959")

    #C0076
    ChrTalk(
        0xFE,
        (
            "昨夜带尤利那家伙兜了一阵风，\x01",
            "他的心情好像已经完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "哎呀呀，简直就像哄小孩一样。\x01",
            "……不过，在他面前可绝对不能这么说。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    TalkEnd(0xFE)
    SetChrFlags(0xFE, 0x10)
    Return()

    label("loc_1959")


    #C0078
    ChrTalk(
        0xFE,
        (
            "好，我们准备出发，\x01",
            "去『诺艾·布朗』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "……怎么了？瑞吉，\x01",
            "你怎么一副快要睡着的样子？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_19BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_19CF")
    Call(0, 9)
    Jump("loc_1D0B")

    label("loc_19CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A58")

    #C0080
    ChrTalk(
        0xFE,
        "哇……！？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "……嗯？那个红毛小丫头\x01",
            "已经不在了吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "……哼、哼！\x01",
            "你们不要太嚣张啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A92")

    label("loc_1A58")


    #C0083
    ChrTalk(
        0xFE,
        "我可没有怕你们……！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        "……你、你们不要太嚣张啊！\x02",
    )

    CloseMessageWindow()

    label("loc_1A92")

    Jump("loc_1C8A")

    label("loc_1A97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD9")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    #C0085
    ChrTalk(
        0xFE,
        "哇……又来了吗！？\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        "不、不要再靠近我了！！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x1A3,
        (
            "#04606F嗯……我对你们几个\x01",
            "已经没有兴趣了啊。\x02\x03",

            "#04609F好啦好啦，我们赶快去找玛丽吧¤\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00003F啊……嗯……说的对。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x105,
        (
            "#10302F好一个天真烂漫的女孩，\x01",
            "真难想象刚才的杀气是她发出的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C18")

    label("loc_1BD9")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0090
    ChrTalk(
        0xFE,
        (
            "不、不要再靠近我了！！\x01",
            "一边去！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C18")

    Jump("loc_1C8A")

    label("loc_1C1D")


    #C0091
    ChrTalk(
        0xFE,
        (
            "哈哈，真是个胆小鬼啊！\x01",
            "只是稍微吓了吓它，\x01",
            "马上就屁滚尿流地逃跑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "欺负弱小的生物\x01",
            "为何如此有趣呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8A")

    Jump("loc_1D0B")

    label("loc_1C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1C9D")
    Jump("loc_1D0B")

    label("loc_1C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB8")
    Call(0, 8)
    Jump("loc_1CFD")

    label("loc_1CB8")


    #C0093
    ChrTalk(
        0xFE,
        (
            "……怎么？\x01",
            "你们想加入我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "哼哼，在那边咬着手指看着吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1CFD")

    Jump("loc_1D0B")

    label("loc_1D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D0B")

    label("loc_1D0B")

    TalkEnd(0xFE)
    Return()

    # Function_7_15BB end

    def Function_8_1D0F(): pass

    label("Function_8_1D0F")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0095
    ChrTalk(
        0x9,
        "好，快到那边坐下吧。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "我们准备了高级葡萄酒，\x01",
            "二位姐姐也来一起喝吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xC,
        (
            "呵呵呵，那就\x01",
            "不客气啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_1D0F end

    def Function_9_1D92(): pass

    label("Function_9_1D92")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9F")

    #C0098
    ChrTalk(
        0x9,
        (
            "尤利那家伙的\x01",
            "心情非常糟糕啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "本想带他去欢乐街转换一下心情，\x01",
            "但很多警官在那一带\x01",
            "守卫各国要人。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        (
            "嗯，既然如此……\x01",
            "就开车去山道那边来个\x01",
            "夜间兜风吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xA,
        (
            "这个时间行人\x01",
            "应该很少，可以\x01",
            "尽情驰骋一番……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        "哦哦，这主意相当不错嘛。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EF0")

    label("loc_1E9F")


    #C0103
    ChrTalk(
        0x9,
        (
            "好，既然决定了，\x01",
            "那就去问问尤利吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "瑞吉，你去准备车吧。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xA,
        "知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_1EF0")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_1D92 end

    def Function_10_1EF9(): pass

    label("Function_10_1EF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F0A")
    Jump("loc_25DF")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F25")
    Call(0, 5)
    Jump("loc_1F6F")

    label("loc_1F25")


    #C0106
    ChrTalk(
        0xFE,
        (
            "早知如此，在独立宣言刚刚发表的时候，\x01",
            "说什么也应该\x01",
            "立刻回共和国啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F6F")

    Jump("loc_25DF")

    label("loc_1F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2003")

    #C0107
    ChrTalk(
        0xFE,
        (
            "尤利好像显得很轻松……\x01",
            "……应、应该不会有事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "如果错过了这个机会，\x01",
            "万一遇到什么意外，\x01",
            "我们可就再也回不去共和国了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25DF")

    label("loc_2003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_207A")

    #C0109
    ChrTalk(
        0xFE,
        (
            "（尤利竟然那样说……\x01",
            "  真是有点过分了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "（不过我和塞克斯\x01",
            "  可没那么想，\x01",
            "  你们不要介意。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25DF")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2187")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210A")

    #C0111
    ChrTalk(
        0xFE,
        (
            "……啊嚏！！\x01",
            "好像感冒了……\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "都是因为昨天\x01",
            "掉进了水池啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "……唉，这就是所谓的自作自受吗？\x01",
            "真郁闷啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2182")

    label("loc_210A")


    #C0114
    ChrTalk(
        0xFE,
        (
            "啊嚏……！\x01",
            "要不要去乌尔斯拉医院\x01",
            "开些药呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "但是听说玛因兹发生了\x01",
            "很严重的事情，\x01",
            "不知巴士是否还在正常运行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2182")

    Jump("loc_25DF")

    label("loc_2187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2195")
    Jump("loc_25DF")

    label("loc_2195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2227")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2202")

    #C0116
    ChrTalk(
        0xFE,
        (
            "哎，刚才好像听到了\x01",
            "警笛声呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "……不管了。\x01",
            "呃……尤利喜欢的红茶是……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2222")

    label("loc_2202")


    #C0118
    ChrTalk(
        0xFE,
        "呃……尤利喜欢的红茶是……\x02",
    )

    CloseMessageWindow()

    label("loc_2222")

    Jump("loc_25DF")

    label("loc_2227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2235")
    Jump("loc_25DF")

    label("loc_2235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2243")
    Jump("loc_25DF")

    label("loc_2243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DB")

    #C0119
    ChrTalk(
        0xFE,
        (
            "从昨晚到今早，\x01",
            "我驾车在山道中驰骋了好几个来回……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "呼，好困啊……\x01",
            "真希望尤利和塞克斯也学会开车，\x01",
            "偶尔也替我开开啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_233B")

    label("loc_22DB")


    #C0121
    ChrTalk(
        0xFE,
        (
            "不过总算让尤利恢复精神了，\x01",
            "倒是不错……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "呼，好困啊……\x01",
            "出去喝酒之前，先让我睡睡吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233B")

    Jump("loc_25DF")

    label("loc_2340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2351")
    Call(0, 9)
    Jump("loc_25DF")

    label("loc_2351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2564")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_23D8")

    #C0123
    ChrTalk(
        0xFE,
        (
            "无、无论如何也不能\x01",
            "再欺负猫了……\x01",
            "必须要牢记这一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "不然的话，如果那小丫头再来……\x01",
            "……（发抖）。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255F")

    label("loc_23D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0xA2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E8")
    OP_93(0xFE, 0x5A, 0x0)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xFE, 0x1A3, 500)

    #C0125
    ChrTalk(
        0xFE,
        "哇，又来了吗……！？\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x1A3,
        "#4S#04602F……哇！！\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "哇啊啊啊啊！！\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x1A3,
        "#04609F啊哈哈哈，你在怕什么啊～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A3, 500)

    #C0129
    ChrTalk(
        0x102,
        (
            "#00106F（呼……这种天真无邪的性格\x01",
            "  从某种意义上说也很危险呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2519")

    label("loc_24E8")


    #C0130
    ChrTalk(
        0xFE,
        (
            "饶、饶了我吧……\x01",
            "我以后再也不敢欺负猫了！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2519")

    Jump("loc_255F")

    label("loc_251E")


    #C0131
    ChrTalk(
        0xFE,
        "嘿嘿，真是有趣啊～\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "不过那只猫那么小，\x01",
            "倒也有点可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_255F")

    Jump("loc_25DF")

    label("loc_2564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2572")
    Jump("loc_25DF")

    label("loc_2572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25D6")

    #C0133
    ChrTalk(
        0xFE,
        (
            "嗯……赶快再做点\x01",
            "下酒菜吃吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "嘿嘿，从共和国带来的\x01",
            "高级葡萄酒已经喝光了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25DF")

    label("loc_25D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_25DF")

    label("loc_25DF")

    TalkEnd(0xFE)
    Return()

    # Function_10_1EF9 end

    def Function_11_25E3(): pass

    label("Function_11_25E3")

    Call(0, 12)
    Return()

    # Function_11_25E3 end

    def Function_12_25E7(): pass

    label("Function_12_25E7")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FC")
    Call(0, 6)
    Jump("loc_2651")

    label("loc_25FC")


    #C0135
    ChrTalk(
        0xB,
        "（好久没遇到过这么豪爽的客人了☆）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xB,
        (
            "（呵呵，一定要从他们身上\x01",
            "  多榨些钱。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2651")

    TalkEnd(0xB)
    SetChrSubChip(0xB, 0x1)
    Return()

    # Function_12_25E7 end

    def Function_13_2659(): pass

    label("Function_13_2659")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266E")
    Call(0, 8)
    Jump("loc_26DC")

    label("loc_266E")

    OP_4B(0xFE, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0137
    ChrTalk(
        0xFE,
        (
            "哎？这么说，停在外面的\x01",
            "那辆车也是你们的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "嘿嘿，很棒吧～\x01",
            "下次要不要一起兜风啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_26DC")

    TalkEnd(0xFE)
    Return()

    # Function_13_2659 end

    def Function_14_26E0(): pass

    label("Function_14_26E0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch47502.itc", 0x1E)
    LoadChrToIndex("chr/ch26800.itc", 0x1F)
    LoadChrToIndex("chr/ch26900.itc", 0x20)
    LoadChrToIndex("chr/ch44102.itc", 0x21)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5700, 200, 4900, 180)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 7900, 200, 2450, 270)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5700, 0, 470, 360)
    OP_4B(0xA, 0xFF)
    OP_68(5030, 1500, 1370, 0)
    MoveCamera(30, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24150, 0)
    SetCameraDistance(23150, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0139
    ChrTalk(
        0x8,
        (
            "#5P哈，说起来，今天早上的\x01",
            "兜风真是太爽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xA,
        (
            "#12P嘿嘿，充分利用了今天的雨水，\x01",
            "顺利玩出了漂移呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#5P嗯，确实\x01",
            "相当刺激啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#5P对了，瑞吉，\x01",
            "今天早上约的那两个姐姐\x01",
            "肯定会来吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#12P嗯，再等等吧。\x01",
            "差不多也快……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    Sleep(300)
    Fade(500)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x105, 0x80)
    OP_68(2670, 1400, -1580, 0)
    MoveCamera(19, 14, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 1500, 50, -2250, 45)
    SetChrPos(0x109, 500, 50, -2500, 45)
    SetChrPos(0x102, 1500, 50, -3500, 45)
    SetChrPos(0x105, 500, 50, -3750, 45)
    OP_0D()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2988():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2988)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)

    #C0144
    ChrTalk(
        0xA,
        "哦！来了吗¤\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        "#5P呵呵，来得正是时候啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C22")
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0146
    ChrTalk(
        0xA,
        "嗯！？你们不是昨天那几个巡警吗！？\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x9,
        "为、为什么要来这里……！\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        (
            "#6P#00105F……是昨天超速飙车的三人组啊。\x02\x03",

            "#00103F这是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x105,
        "#6P#10302F莫非你们正在入室盗窃吗？\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x109,
        "#6P#10101F那就要当场逮捕了。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        "说、说什么蠢话……！\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "如果是小偷，\x01",
            "早就会跑掉了！\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#5P说啊，你们这些巡警\x01",
            "来这里干什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#5P竟敢擅自闯入我们的家，\x01",
            "胆子真不小啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        "#6P#00105F你们的家？也就是说……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，看来他们就是\x01",
            "这座房子的新住户呢。\x02\x03",

            "#00000F我们今日来此别无他意，\x01",
            "只是为了执行警察的工作。\x02\x03",

            "不会占用各位太多时间的，\x01",
            "还请配合我们的调查。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DBF")

    label("loc_2C22")

    OP_63(0xA, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0157
    ChrTalk(
        0xA,
        "嘿嘿嘿，真是上等货色啊。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        "是啊，比期待中的更漂亮呢。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        "#6P#00105F……哎？\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        "#6P#10106F这是什么意思？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#5P哦，护送员也辛苦了，\x01",
            "过来领小费吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#6P#10306F哎呀呀……\x01",
            "看来是把你们误认为\x01",
            "上门服务的女公关了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        (
            "#6P#00003F……还是开门见山地说吧。\x02\x03",

            "#00000F不好意思，打扰了，\x01",
            "我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "不会占用各位太多时间的，\x01",
            "还请配合我们的调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBF")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 300, 0, 3250, 180)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1700, 0, 3250, 180)
    SetChrPos(0x101, -1260, 0, -250, 0)
    SetChrPos(0x102, -100, 0, -250, 0)
    SetChrPos(0x109, -1260, 0, -1800, 0)
    SetChrPos(0x105, -100, 0, -1800, 0)
    OP_68(-890, 1400, 510, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(42740, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00003F也就是说，你们三人\x01",
            "来克洛斯贝尔是为了学习处世……\x02\x03",

            "在寻找居住地点时，正好\x01",
            "发现了这座公开出售的房子，\x01",
            "于是尤利先生便把它买下了……\x02\x03",

            "#00001F……情况就是这样吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        "#5P嗯，你们已经明白了吧？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#12P#00105F顺便一问，\x01",
            "『高贵之血』这个名字\x01",
            "是什么意思呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "#5P嘿嘿，你很想知道吗？\x01",
            "这是我们三人组的称号。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "#5P这名字和我们这些\x01",
            "深受女神怜爱的上流人士\x01",
            "十分相配吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x9,
        (
            "#5P哼哼，告诉你们吧，\x01",
            "我们的父亲全都是\x01",
            "乌尔努公司的高层领导。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x9,
        (
            "#5P其中，尤利的父亲更是公司的董事。\x01",
            "如果想向他讨好献媚，可就要趁现在喽。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        "#5P哼哼，正是如此。\x02",
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    OP_68(-580, 1400, -640, 3000)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xD, 1260, 0, -4800, 0)
    SetChrPos(0xE, 1260, 0, -6000, 0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3134():
        OP_95(0xD, 1260, 0, -2000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3134)
    Sleep(50)

    def lambda_3151():
        OP_95(0xE, 1260, 0, -3000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3151)
    Sleep(50)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0xD, 1)
    Sound(104, 0, 100, 0)

    def lambda_31A2():
        OP_93(0xD, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_31A2)
    Sleep(50)
    WaitChrThread(0xE, 1)

    def lambda_31B6():
        OP_93(0xE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_31B6)
    Sleep(50)

    def lambda_31C6():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_31C6)
    Sleep(50)

    def lambda_31D6():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_31D6)
    Sleep(50)

    def lambda_31E6():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31E6)
    Sleep(50)

    def lambda_31F6():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31F6)

    #C0172
    ChrTalk(
        0xA,
        "#5P哦，正等着你们呢¤\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x9,
        "#5P哈哈，这次好像是真来了。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xD,
        (
            "#12P那个……\x01",
            "请问『高贵之血』\x01",
            "是哪位？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xE,
        (
            "#12P哎，他们好像\x01",
            "有事在忙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#5P哦，二位小姐，\x01",
            "不必担心，已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "#5P情况就是这样，\x01",
            "请你们赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_32E8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_32E8)
    Sleep(50)

    def lambda_32F8():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32F8)
    Sleep(50)

    def lambda_3308():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3308)
    Sleep(50)

    def lambda_3318():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3318)
    Sleep(300)

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，不用你说，\x01",
            "我们也要走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c0300", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_26E0 end

    def Function_15_3381(): pass

    label("Function_15_3381")

    EventBegin(0x0)
    LoadChrToIndex("apl/ch51269.itc", 0x1E)
    SoundLoad(3975)
    SoundLoad(3976)
    SoundLoad(3977)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5700, 200, 4900, 180)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 950, 0, 700, 180)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 5700, 0, 470, 360)
    OP_68(1710, 2500, -380, 0)
    MoveCamera(24, 16, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, 980, 0, -6650, 0)
    SetChrPos(0x102, 980, 0, -6650, 0)
    SetChrPos(0x109, 980, 0, -6650, 0)
    SetChrPos(0x105, 980, 0, -6650, 0)
    SetChrPos(0x104, 980, 0, -6650, 0)
    SetChrPos(0x1A3, 980, 0, -6650, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(1710, 1400, -380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(103, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 18)
    Sleep(700)
    BeginChrThread(0x1A3, 3, 0, 21)
    WaitChrThread(0x1A3, 3)
    OP_6F(0x1)

    #C0179
    ChrTalk(
        0x9,
        "哦？怎么回事？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)
    TurnDirection(0xA, 0x101, 500)
    WaitChrThread(0xA, 1)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0180
    ChrTalk(
        0xA,
        (
            "哎，\x01",
            "你们不是之前那些巡警吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "#11P哼……\x01",
            "好像是叫『特别任务支援科』吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00003F正是。\x02\x03",

            "#6P#00000F我们有点事情想请教，\x01",
            "可以占用你们一些时间吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrPos(0xA, 300, 0, 3250, 180)
    SetChrPos(0x9, -1700, 0, 3250, 180)
    OP_68(-1040, 1400, 630, 0)
    MoveCamera(38, 26, 0, 0)
    OP_6E(190, 0)
    SetCameraDistance(42740, 0)
    SetChrPos(0x101, -1240, 0, 500, 0)
    SetChrPos(0x102, 160, 0, 200, 0)
    SetChrPos(0x109, -1180, 0, -900, 0)
    SetChrPos(0x105, 120, 120, -1080, 0)
    SetChrPos(0x104, -1140, 120, -2300, 0)
    SetChrPos(0x1A3, 90, 0, -2500, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0183
    ChrTalk(
        0xA,
        "嘿，猫啊……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "哼哼……\x01",
            "原来如此。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#12P#00105F你们好像有线索啊？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        (
            "#12P#00300F大家的时间都很宝贵，\x01",
            "能不能快点告诉我们啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        "唔……怎么办呢……\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "尤利，该怎么办？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E5")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆是否完成了取缔超速车事件？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已完成】\x01",        # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D1")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_38E5")

    label("loc_38D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38E5")
    OP_29(0x69, 0x3, 0x10)

    label("loc_38E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_399E")

    #C0190
    ChrTalk(
        0x8,
        "哼哼，这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x8,
        (
            "之前我们只是开个快车而已，\x01",
            "却承蒙你们那么关照……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "如果想让我们帮忙，\x01",
            "就要拿出像样的『诚意』。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        "向我们下跪，或者跳裸舞，任选其一吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A36")

    label("loc_399E")


    #C0194
    ChrTalk(
        0x8,
        "哼哼，这个嘛……\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "你们的询问态度\x01",
            "未免也太傲慢了……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "如果想让我们帮忙，\x01",
            "就要拿出像样的『诚意』。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        "向我们下跪，或者跳裸舞，任选其一吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3A36")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0198
    ChrTalk(
        0xA,
        "#11P哈哈，不错不错！\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x9,
        (
            "就是这样，赶快决定吧，\x01",
            "是要下跪还是要跳裸舞？\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        "哦，男人的裸体就算了。\x02",
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x109,
        "#12P#10101F（这、这些家伙……）\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x102,
        "#12P#00106F（比想象中更加恶劣呢……）\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x105,
        (
            "#12P#10306F（哎呀呀，他们好像\x01",
            "  并没有搞清楚情况呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#12P#00301F（啧……\x01",
            "  但又不能威胁他们。）\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        "#12P#00000F（嗯，接下来就交给我吧──）\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)

    #C0206
    ChrTalk(
        0x1A3,
        (
            "#12P#04605F#3975V喂，我说你们……\x02\x03",

            "#3976V为何要费\x01",
            "这么多工夫？\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF88)
    OP_C9(0x1, 0x80000000)

    def lambda_3CA9():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CA9)
    Sleep(50)

    def lambda_3CB9():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CB9)
    Sleep(50)

    def lambda_3CC9():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CC9)
    Sleep(50)

    def lambda_3CD9():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CD9)
    Sleep(50)

    def lambda_3CE9():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CE9)
    Sleep(500)

    #C0207
    ChrTalk(
        0x101,
        "#00005F哎……\x02",
    )

    CloseMessageWindow()
    OP_68(-1220, 1400, 1530, 1000)
    SetChrChip(0x0, 0x1A3, 0x1E, 0x12C)
    Sound(809, 0, 100, 0)
    OP_95(0x1A3, -440, 0, -330, 8000, 0x0)
    OP_95(0x1A3, -660, 0, 2440, 8000, 0x0)
    SetChrChip(0x1, 0x1A3, 0x0, 0x0)
    OP_0D()
    SetChrChipByIndex(0x1A3, 0x1E)
    SetChrSubChip(0x1A3, 0x0)
    SetChrFlags(0x1A3, 0x2)
    OP_0D()
    SetChrPos(0x8, -700, 0, 3000, 180)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Sound(811, 0, 30, 0)
    SetChrSubChip(0x1A3, 0x1)
    SetChrPos(0x8, -700, 200, 3000, 180)
    BeginChrThread(0x8, 3, 0, 22)
    OP_6F(0x1)

    def lambda_3DA7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DA7)
    Sleep(50)

    def lambda_3DB7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3DB7)
    Sleep(50)

    def lambda_3DC7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3DC7)
    Sleep(50)

    def lambda_3DD7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3DD7)
    Sleep(50)

    def lambda_3DE7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DE7)
    Sleep(50)

    def lambda_3DF7():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3DF7)
    Sleep(50)

    def lambda_3E07():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E07)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0208
    ChrTalk(
        0x8,
        "#5P呜……！？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x1A3,
        (
            "#12P#04609F好了，\x01",
            "赶快说出来吧。\x02\x03",

            "#04611F如果继续抵抗，\x01",
            "我就让你把胃里的东西全吐出来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        "#5P呜呜，你……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_3F96():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F96)
    Sleep(50)

    def lambda_3FB3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FB3)
    WaitChrThread(0x9, 1)

    def lambda_3FD1():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3FD1)
    WaitChrThread(0xA, 1)

    def lambda_3FE2():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FE2)
    Sleep(300)

    #C0211
    ChrTalk(
        0xA,
        (
            "#11P喂、喂！\x01",
            "你怎么突然……！\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "#5P这臭丫头！\x01",
            "你要对尤利做什么！？\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0213
    ChrTalk(
        0x1A3,
        (
            "#12P#04611F#3977V别烦我，\x01",
            "不然我会杀了他哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF89)
    OP_C9(0x1, 0x80000000)
    OP_64(0x9)
    OP_64(0xA)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x9,
        "#5P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        "#12P#00011F等、等一下！\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        "#12P#00101F这、这未免也太……\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x104,
        (
            "#12P#00303F呼……哎呀呀。\x02\x03",

            "#00301F你们几个，\x01",
            "还是赶快交代吧。\x02\x03",

            "这家伙相当危险，\x01",
            "她可不是在危言耸听。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        "#5P呜……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        "#11P明、明白了……我说我说！\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xA,
        (
            "#11P确、确实有小猫来过！\x01",
            "你们来之前刚刚来过！\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xA,
        (
            "#11P我、我稍微吓了它一下，\x01",
            "它马上就逃走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xA,
        "#11P说、说不定还在附近哦！\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xA,
        (
            "#11P这、这样就行了吧！？\x01",
            "赶、赶快放下尤利！\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x1A3,
        (
            "#12P#04604F嘿，吓唬可爱的小猫吗？\x02\x03",

            "#04609F就像这样？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x2)
    SetChrPos(0x9, -1500, 0, 2400, 90)
    Sleep(300)
    Sound(802, 0, 100, 0)
    Sound(811, 0, 30, 0)
    SetChrSubChip(0x1A3, 0x3)
    SetChrPos(0x9, -1500, 200, 2400, 90)
    BeginChrThread(0x9, 3, 0, 22)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0225
    ChrTalk(
        0x9,
        "#5P呜……！\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        "#5P哇……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1A3, 0x4)

    #C0227
    ChrTalk(
        0x1A3,
        "#6P#04611F这位小哥，你也想体会一下吗？\x02",
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xA, 0xB4, 0x1F4, 0x7D0, 0x0)

    #C0228
    ChrTalk(
        0xA,
        "#11P（全身颤抖）……！\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x1A3,
        (
            "#6P#04609F啊哈哈，倒也挺识趣嘛。\x02\x03",

            "#04604F好啦，我们走吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    ClearChrFlags(0x1A3, 0x2)
    SetChrPos(0x8, -700, 0, 3250, 180)
    SetChrPos(0x9, -1700, 0, 2400, 90)
    Sleep(100)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0xB4, 0x0)

    def lambda_4498():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4498)
    Sleep(50)

    def lambda_44B0():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_44B0)

    #C0230
    ChrTalk(
        0x8,
        "呜啊……呼、呼！\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        "……呜、呜！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A3, 0x101, 500)

    #C0232
    ChrTalk(
        0x1A3,
        (
            "#5P#04600F玛丽好像就在\x01",
            "这附近哦。\x02\x03",

            "#04609F赶快去找吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#12P#00005F啊……嗯……\x02\x03",

            "#12P#00003F那个……\x01",
            "感谢你们的协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，顺便一说，\x01",
            "她和警察局没有任何关系哦。\x02\x03",

            "#10309F你们就当是被小猫咬了一口吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "#5P烦、烦死人了……！\x01",
            "赶快走吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "#5P你们几个……\x01",
            "……可别想轻易了结……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c0300", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_15_3381 end

    def Function_16_4641(): pass

    label("Function_16_4641")


    def lambda_4646():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4646)

    def lambda_4657():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4657)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 920, 0, -1940, 2000, 0x0)
    Return()

    # Function_16_4641 end

    def Function_17_4685(): pass

    label("Function_17_4685")


    def lambda_468A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_468A)

    def lambda_469B():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_469B)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -100, 0, -3320, 2000, 0x0)
    OP_95(0x102, -100, 0, -1870, 2000, 0x0)
    Return()

    # Function_17_4685 end

    def Function_18_46DD(): pass

    label("Function_18_46DD")


    def lambda_46E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_46E2)

    def lambda_46F3():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_46F3)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 2210, 0, -3320, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_18_46DD end

    def Function_19_4728(): pass

    label("Function_19_4728")


    def lambda_472D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_472D)

    def lambda_473E():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_473E)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 2210, 0, -3320, 2000, 0x0)
    OP_95(0x109, 2210, 0, -1870, 2000, 0x0)
    Return()

    # Function_19_4728 end

    def Function_20_4780(): pass

    label("Function_20_4780")


    def lambda_4785():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4785)

    def lambda_4796():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4796)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -100, 0, -3320, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_20_4780 end

    def Function_21_47CB(): pass

    label("Function_21_47CB")


    def lambda_47D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_47D0)

    def lambda_47E1():
        OP_95(0xFE, 940, 0, -3320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_47E1)
    WaitChrThread(0x1A3, 1)
    Return()

    # Function_21_47CB end

    def Function_22_47FB(): pass

    label("Function_22_47FB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_482B")

    def lambda_480B():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_480B)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    Jump("Function_22_47FB")

    label("loc_482B")

    Return()

    # Function_22_47FB end

    SaveToFile()

Try(main)
