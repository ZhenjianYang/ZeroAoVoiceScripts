from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1430.bin",                # FileName
        "c1430",                    # MapName
        "c1430",                    # Location
        0x0032,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 50, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1430",                  # 0
        "基约姆师傅",             # 1
        "罗伯兹主任",             # 2
        "阿巴斯",                 # 3
    ))

    AddCharChip((
        "chr/ch26400.itc",                   # 00
        "chr/ch06700.itc",                   # 01
        "chr/ch29300.itc",                   # 02
    ))

    DeclNpc(5619,    0,       5329,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-51279,  0,       15350,   270,  389,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)

    DeclActor(4150,    0,       4740,    1000,    5620,    1500,    5330,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(376, 0)                                        # 0

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_3D2",          # 02, 2
        "Function_3_466",          # 03, 3
        "Function_4_46A",          # 04, 4
        "Function_5_514",          # 05, 5
        "Function_6_825",          # 06, 6
        "Function_7_1D1E",         # 07, 7
        "Function_8_21FD",         # 08, 8
        "Function_9_22FE",         # 09, 9
        "Function_10_293B",        # 0A, 10
        "Function_11_32E4",        # 0B, 11
        "Function_12_373F",        # 0C, 12
        "Function_13_3749",        # 0D, 13
        "Function_14_3A91",        # 0E, 14
        "Function_15_40DA",        # 0F, 15
        "Function_16_458B",        # 10, 16
        "Function_17_4C43",        # 11, 17
        "Function_18_5098",        # 12, 18
        "Function_19_5251",        # 13, 19
        "Function_20_5349",        # 14, 20
        "Function_21_5AED",        # 15, 21
        "Function_22_5C81",        # 16, 22
        "Function_23_6176",        # 17, 23
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B0"),
        (1, "loc_1BC"),
        (2, "loc_1C8"),
        (3, "loc_1D4"),
        (4, "loc_1E0"),
        (5, "loc_1EC"),
        (6, "loc_1F8"),
        (SWITCH_DEFAULT, "loc_204"),
    )


    label("loc_1B0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1BC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1C8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1D4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1E0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1EC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_204")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_227")

    Return()

    # Function_0_178 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_236")
    Jump("loc_3D1")

    label("loc_236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_244")
    Jump("loc_3D1")

    label("loc_244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_252")
    Jump("loc_3D1")

    label("loc_252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D3")
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_2AC")
    SetChrPos(0x8, 13130, 1000, 6290, 180)
    SetChrPos(0xA, 15170, 1000, 8560, 90)
    Jump("loc_2CE")

    label("loc_2AC")

    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0xA, 15240, 1000, 9210, 180)

    label("loc_2CE")

    Jump("loc_2E4")

    label("loc_2D3")

    SetChrPos(0x8, 15240, 1000, 7610, 90)

    label("loc_2E4")

    Jump("loc_3D1")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F7")
    Jump("loc_3D1")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_3D1")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_324")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_3D1")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_332")
    Jump("loc_3D1")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_340")
    Jump("loc_3D1")

    label("loc_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34E")
    Jump("loc_3D1")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_3D1")

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_396")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0x9, 15240, 1000, 9210, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3D1")

    label("loc_396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3B1")

    Jump("loc_3D1")

    label("loc_3B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1")
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3D1")

    Return()

    # Function_1_228 end

    def Function_2_3D2(): pass

    label("Function_2_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E4")
    OP_65(0x0, 0x1)

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F6")
    OP_65(0x0, 0x1)

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_408")
    OP_65(0x0, 0x1)

    label("loc_408")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_421")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_427")

    label("loc_421")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_427")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44E")
    Sound(128, 1, 50, 0)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_465")

    Return()

    # Function_2_3D2 end

    def Function_3_466(): pass

    label("Function_3_466")

    Call(0, 4)
    Return()

    # Function_3_466 end

    def Function_4_46A(): pass

    label("Function_4_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C")
    Call(0, 15)
    Return()

    label("loc_47C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_499")
    TalkBegin(0x8)
    Call(0, 8)
    TalkEnd(0x8)
    Return()

    label("loc_499")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C3")
    Call(0, 17)
    Return()

    label("loc_4C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    TalkBegin(0x8)
    Call(0, 7)
    TalkEnd(0x8)
    Return()

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
    Call(0, 9)
    Return()

    label("loc_50A")

    TalkBegin(0x8)
    Call(0, 5)
    TalkEnd(0x8)
    Return()

    # Function_4_46A end

    def Function_5_514(): pass

    label("Function_5_514")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A0")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "对话")
    MenuCmd(1, 0, "委托改造")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A")
    MenuCmd(1, 0, "交出Ｕ材料")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    MenuCmd(1, 0, "询问金属探测器")

    label("loc_5AA")

    MenuCmd(1, 0, "放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E9")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5E9")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_60D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    OP_AF(0xAD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_659")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659")
    Call(0, 21)
    Return()

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Return()

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69B")

    label("loc_69B")

    Jump("loc_53E")

    label("loc_6A0")

    Jump("loc_824")

    label("loc_6A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_824")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石碎片', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_714")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "委托改造\x01",          # 1
            "委托制作武器\x01",      # 2
            "放弃\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_74C")

    label("loc_714")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "委托改造\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_74C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_768")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_768")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_787")
    OP_AF(0xAE)
    Jump("loc_7C9")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_797")
    OP_AF(0xAD)
    Jump("loc_7C9")

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A7")
    OP_AF(0xAC)
    Jump("loc_7C9")

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C0")
    OP_AF(0xAF)
    Jump("loc_7C2")

    label("loc_7C0")

    OP_AF(0xAB)

    label("loc_7C2")

    Jump("loc_7C9")

    label("loc_7C7")

    OP_AF(0xAA)

    label("loc_7C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_81F")

    label("loc_7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EF")
    Call(0, 10)
    Jump("loc_81F")

    label("loc_7EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_803")
    Jump("loc_81F")

    label("loc_803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_81F")

    Jump("loc_6AF")

    label("loc_824")

    Return()

    # Function_5_514 end

    def Function_6_825(): pass

    label("Function_6_825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C")

    #C0001
    ChrTalk(
        0x8,
        (
            "居然出现了那种东西……\x01",
            "真是一波未平，一波又起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "……你们几个，如果打算前往\x01",
            "那棵『大树』，\x01",
            "记得要做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "既然要和那帮怪物一样的家伙战斗，\x01",
            "武器肯定是强化得\x01",
            "越厉害越好。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00000F嗯……这方面的事情就拜托您了！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_98E")

    label("loc_92C")


    #C0005
    ChrTalk(
        0x8,
        (
            "你们现在肯定很辛苦……\x01",
            "但千万不要放弃哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "虽说我只会改造武器，\x01",
            "但一定会尽力帮助你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98E")

    Jump("loc_1D1D")

    label("loc_993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD6")

    #C0007
    ChrTalk(
        0x8,
        (
            "你们是……\x01",
            "哈哈，大家都平安无事啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "已经和达德利他们\x01",
            "顺利会合了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00000F嗯，托您的福。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#00304F基约姆大叔，\x01",
            "再次感谢你帮我\x01",
            "修好『狂战士』……\x02\x03",

            "#00300F在市外那段时间，\x01",
            "它帮了我很大的忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "呵呵，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "不过，你可要牢牢记住，\x01",
            "机关部位始终是它的弱点。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "如果那把威力惊人的来复枪\x01",
            "再次坏掉，我可就没法保证\x01",
            "能马上修复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#00300F我知道，我会只在\x01",
            "关键时刻使用那东西的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "嗯，你明白就好。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "谁也不知道总统他们\x01",
            "究竟会用上什么手段。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "你们一定要用心\x01",
            "维护自己的武器。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00000F好的，以后大概还要来麻烦您。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 3)
    Jump("loc_C28")

    label("loc_BD6")


    #C0019
    ChrTalk(
        0x8,
        (
            "谁也不知道总统他们\x01",
            "究竟会用上什么手段。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "你们一定要用心\x01",
            "维护自己的武器。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C28")

    Jump("loc_1D1D")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_DE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")

    #C0021
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔独立国，还有国防军吗……\x01",
            "事情发展到如此地步，可真是不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "你们早就知道这件事了吗？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00003F不，我们也是刚刚才听说。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00101F所以现在正在四处\x01",
            "收集情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "是吗……你们也很辛苦啊。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "今后大概还会发生很多问题，\x01",
            "不要气馁，打起精神吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00304F嗯，当然。\x01",
            "谢谢啦，大叔。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DDB")

    label("loc_D79")


    #C0028
    ChrTalk(
        0x8,
        (
            "话说回来，竟然敢如此肆无忌惮地\x01",
            "向两大国挑衅。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "总之……暂时也只能\x01",
            "默默观望事态的发展了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDB")

    Jump("loc_1D1D")

    label("loc_DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1054")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E8B")

    #C0030
    ChrTalk(
        0x8,
        (
            "白天专注于旧城区的重建，\x01",
            "晚上则专注于工房的工作。\x01",
            "我现在是这样安排的。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "虽然完全没有休息的时间了，\x01",
            "但看到大家这么依赖我，\x01",
            "总觉得很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104F")

    label("loc_E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF3")
    TurnDirection(0x8, 0x104, 0)

    #C0032
    ChrTalk(
        0x8,
        (
            "至于来复枪……\x01",
            "我预计后天\x01",
            "就能修理好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "在那之前，\x01",
            "你就乖乖等着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104F")

    label("loc_EF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_END)), "loc_F47")

    #C0034
    ChrTalk(
        0x8,
        (
            "好，赶紧开始\x01",
            "加工Ｕ材料吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "实在是多谢你们啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_FDB")

    label("loc_F47")


    #C0036
    ChrTalk(
        0x8,
        (
            "白天专注于旧城区的重建，\x01",
            "晚上则专注于工房的工作。\x01",
            "我现在是这样安排的。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "虽然完全没有休息的时间了，\x01",
            "但看到大家这么依赖我，\x01",
            "总觉得很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDB")

    Jump("loc_104F")

    label("loc_FE0")


    #C0038
    ChrTalk(
        0x8,
        (
            "我刚才也去喝了碗\x01",
            "猪骨汤。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "喝完之后，好像全身都\x01",
            "充满力量了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "嘿嘿，拜其所赐，\x01",
            "我的工作进展飞快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104F")

    Jump("loc_1D1D")

    label("loc_1054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_10E3")

    #C0041
    ChrTalk(
        0x8,
        (
            "兰迪那小子，\x01",
            "一副钻进了牛角尖的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "我虽然不清楚具体是怎么一回事，\x01",
            "但在这种时候，他最需要的就是\x01",
            "你们这些同伴的支持。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_10E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A0")

    #C0043
    ChrTalk(
        0x8,
        "听说导力铁道昨天发生了脱轨事故。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "而且，据说是有个巨大的怪物突然出现，\x01",
            "一下就把列车撞倒了……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "难道那怪物想用列车来彰显自己的怪力吗？\x01",
            "真是莫名其妙。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11FC")

    label("loc_11A0")


    #C0046
    ChrTalk(
        0x8,
        (
            "袭击列车的那个怪物\x01",
            "到底想做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "总不会是想炫耀自己的力气吧……\x01",
            "真是莫名其妙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FC")

    Jump("loc_1D1D")

    label("loc_1201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1288")

    #C0048
    ChrTalk(
        0x8,
        "好，导力灯都已经修好了。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "接下来是……\x01",
            "维护战术导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "首先要准备好\x01",
            "检查时所需的结晶回路……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12EB")

    label("loc_1288")


    #C0051
    ChrTalk(
        0x8,
        (
            "结晶回路，结晶回路……\x01",
            "哦，这枚结晶回路的规格\x01",
            "还是上一代的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "真是的，我怎么\x01",
            "老是搞混。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EB")

    Jump("loc_1D1D")

    label("loc_12F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1368")

    #C0053
    ChrTalk(
        0x8,
        (
            "嗯，接下来是修理导力灯……\x01",
            "如果没记错，有五个需要修理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "好～在吃午饭之前，\x01",
            "把它们全部搞定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_1368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1411")

    #C0055
    ChrTalk(
        0x8,
        (
            "现在到处都在议论纷纷，\x01",
            "老实说，独立问题真是个\x01",
            "相当敏感的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "虽然赞成者占了多数，\x01",
            "但其中究竟有多少人真的\x01",
            "理解这件事的重要性呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_147D")

    label("loc_1411")


    #C0057
    ChrTalk(
        0x8,
        (
            "独立提案究竟会带来怎样的结果……\x01",
            "老实说，我也不是很清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "不管怎么说，反正我很在意\x01",
            "两大国的动向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147D")

    Jump("loc_1D1D")

    label("loc_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_193D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18EB")

    #C0059
    ChrTalk(
        0x8,
        (
            "哟，小姑娘。\x01",
            "看样子，你在财团的工作\x01",
            "已经告一段落了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        (
            "#00203F是的，其实那些工作\x01",
            "根本就是他们硬塞给我的。\x02\x03",

            "#00200F对了……\x01",
            "主任好像会定期\x01",
            "来这里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "哈哈，是啊。\x01",
            "之前还把新型魔导杖的设计图\x01",
            "留在这里了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x8,
        (
            "糟糕，我不该把\x01",
            "这件事告诉你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "罗伯兹那家伙要是知道了，又该啰嗦个没完了。\x01",
            "你可要替我保密哦。\x02",
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

    #C0064
    ChrTalk(
        0x103,
        (
            "#00203F……放心好了。\x02\x03",

            "#00211F其实我早就猜到\x01",
            "改造魔导杖的服务\x01",
            "与主任有关了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "哈哈，说的也是啊。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "正如你所知，\x01",
            "魔导杖这种东西的构造\x01",
            "实在是复杂得不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "如果没有人帮忙，就算是我，\x01",
            "也无法轻易完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#10105F那个……\x01",
            "我有些不明白……\x02\x03",

            "#10100F罗伯兹先生为什么\x01",
            "要瞒着缇欧\x01",
            "来办这件事呢？\x02\x03",

            "#10106F而且他这种行事方式\x01",
            "实在是绕了个大圈子啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#00302F哈哈，该怎么说呢。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00000F虽说我们也不太了解\x01",
            "主任这个人……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#00100F嗯……但可以把它理解为\x01",
            "类似于父母关爱孩子的心情吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#00204F………………………………\x01",
            "我并不想去理解那种心情，\x01",
            "但应该就是这么一回事了。\x02\x03",

            "#00200F总之，我已经习惯他这种\x01",
            "处理魔导杖的方式了。\x02\x03",

            "#00204F大家不必在意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 3)
    Jump("loc_1938")

    label("loc_18EB")


    #C0073
    ChrTalk(
        0x8,
        (
            "总之，我随时都可以改造\x01",
            "这位小姑娘的魔导杖。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "需要的时候就来找我吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1938")

    Jump("loc_1D1D")

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1B")

    #C0075
    ChrTalk(
        0x8,
        (
            "我刚才去看了一眼\x01",
            "那座兰花塔。\x01",
            "该怎么说呢……真是惊人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "我身为技术人员，自然对\x01",
            "最新锐的设备很感兴趣……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "但那座建筑物……简直就像在\x01",
            "夸耀着自身的『力量』一样，\x01",
            "我实在是喜欢不起来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A98")

    label("loc_1A1B")


    #C0078
    ChrTalk(
        0x8,
        (
            "兰花塔真是一座\x01",
            "惊人的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "我身为技术人员，自然对\x01",
            "最新锐的设备很感兴趣……\x01",
            "但对那座大楼，却实在是喜欢不起来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A98")

    Jump("loc_1D1D")

    label("loc_1A9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B1E")

    #C0080
    ChrTalk(
        0x8,
        (
            "你们特别任务支援科\x01",
            "现在只剩下那个叫缇欧的\x01",
            "小姑娘还没回来了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "嘿，真希望可以早日\x01",
            "再次拆装那把魔导杖啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1D")

    label("loc_1B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1C27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCE")

    #C0082
    ChrTalk(
        0x8,
        "今天竟然下雨了，真是少见。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "实在是不喜欢这样湿答答的……\x01",
            "因为这种湿气对精密机械\x01",
            "来说是个大麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "拆装机械的时候，\x01",
            "可要多花一番心神了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C22")

    label("loc_1BCE")


    #C0085
    ChrTalk(
        0x8,
        (
            "这种湿气对精密机械\x01",
            "来说是个大麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "拆装机械的时候，\x01",
            "可要多花一番心神了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C22")

    Jump("loc_1D1D")

    label("loc_1C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1D1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC5")

    #C0087
    ChrTalk(
        0x8,
        (
            "要是想改造武器，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "以前就说过，我过去\x01",
            "曾在爱普斯泰恩财团\x01",
            "专攻材料工学。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        "你们完全可以信任我的技术。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D1D")

    label("loc_1CC5")


    #C0090
    ChrTalk(
        0x8,
        (
            "要是想改造武器，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "别看我这个样子，\x01",
            "但技术却是值得信任的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1D")

    Return()

    # Function_6_825 end

    def Function_7_1D1E(): pass

    label("Function_7_1D1E")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x104, 0)
    Sleep(1000)

    #C0092
    ChrTalk(
        0x8,
        "啊，对了，兰迪。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "你之前让我修理的那把\x01",
            "来复枪……\x01",
            "能不能再稍微等等？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#00305F当然没问题……\x02\x03",

            "#00301F不过，是不是有什么问题？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "也不算什么问题吧，只是那东西的\x01",
            "零件几乎都是专用的特殊型号。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "因为无法直接替换零件，\x01",
            "如果想完全修复，无论如何\x01",
            "都需要花费一些时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "不过，跟你堂妹使用的\x01",
            "那把链锯枪相比，\x01",
            "这东西倒还不算太复杂。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#00306F你是说『赤颅』吗……\x01",
            "那确实是很恐怖的武器。\x02\x03",

            "#00301F真没想到那个小丫头\x01",
            "能得心应手地使用它……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "『赤颅』……\x01",
            "那是在帝国的某个古老传说中，\x01",
            "一个拥有千种武器的魔人的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "我以前也曾给自己制造的武器\x01",
            "起过一样的名字……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "但和你堂妹的那把武器相比，\x01",
            "实在是相差得太远了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，你别太介意了。\x02\x03",

            "#00308F毕竟那东西出自\x01",
            "相当特殊的武器工房……\x02\x03",

            "#00301F而且还是特别定制的，\x01",
            "自然会很厉害。\x02\x03",

            "#00306F不好意思啦，大叔，\x01",
            "让你费心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "哪里，我也趁此机会\x01",
            "学到了不少东西呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "而且还发现了很多可以\x01",
            "用在武器改造方面的新技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "总之，再过一周时间，\x01",
            "怎么都能修好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#00300F是吗，但你现在还有\x01",
            "重建方面的工作要忙吧？\x02\x03",

            "#00304F我并不着急用，\x01",
            "你不必急着赶工哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "嘿，连毛都还没长齐的小鬼头，\x01",
            "就别替大叔我操心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "总之，修好以后，\x01",
            "我会再联系你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        "在那之前，你就乖乖等着吧。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x104,
        (
            "#00302F哈哈……\x01",
            "谢啦，大叔。\x02\x03",

            "那就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x18D, 5)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_1D1E end

    def Function_8_21FD(): pass

    label("Function_8_21FD")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 0)

    #C0111
    ChrTalk(
        0x8,
        (
            "哦？这不是兰迪吗！\x01",
            "你终于回到支援科了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00300F嗯，总算回来了。\x02\x03",

            "#00304F话说回来，今后大概还要\x01",
            "拜托你帮我强化武器哦，大叔。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "没问题，只要有素材，\x01",
            "我随时都可以帮你改造。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "不过，你也别\x01",
            "要求得太过火哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x14D, 2)
    Return()

    # Function_8_21FD end

    def Function_9_22FE(): pass

    label("Function_9_22FE")

    EventBegin(0x0)
    Fade(500)
    OP_68(2470, 1400, 4820, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x101, 2240, 0, 4730, 90)
    SetChrPos(0x102, 870, 0, 5250, 90)
    SetChrPos(0x103, 1540, 0, 3220, 45)
    SetChrPos(0x104, 2040, 0, 6260, 135)
    SetChrPos(0xF4, 1080, 0, 6920, 135)
    SetChrPos(0xF5, 380, 0, 3940, 90)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(500)

    #C0115
    ChrTalk(
        0x8,
        (
            "#11P真是的，事情怎么会\x01",
            "变成这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#11P我很想帮上\x01",
            "你们的忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        "#11P……如果有『那东西』的话……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#6P#00005F『那东西』……？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#11P嗯，就是『塞姆里亚石』，\x01",
            "一种被称为古代文明遗物的\x01",
            "金属。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#11P那是一种坚硬得吓人的东西，\x01",
            "通过某位伟大学者的研究，\x01",
            "终于发现了它的加工方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#11P只要有那东西，我就可以造出\x01",
            "正在设计的强力武器了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_END)), "loc_25B3")

    #C0122
    ChrTalk(
        0x8,
        (
            "#11P如果能顺利造出，性能肯定会\x01",
            "远远胜过以前给你们造的那些武器。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#6P#00105F远远胜过……！？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        "#6P#00300F那可真是不得了啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_25ED")

    label("loc_25B3")


    #C0125
    ChrTalk(
        0x104,
        "#6P#00305F强力武器……！？\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#6P#00105F真的吗！？\x02",
    )

    CloseMessageWindow()

    label("loc_25ED")


    #C0127
    ChrTalk(
        0x103,
        (
            "#12P#00202F在这种状况下，我们实在是\x01",
            "很想得到强大的武器啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#11P嗯，只要有材料，\x01",
            "马上就能制造出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#11P对了，即使是小碎片也可以，\x01",
            "只要有五个左右，\x01",
            "就足够制造一件新武器了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_END)), "loc_27B7")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石碎片', 0x0)"), scpexpr(EXPR_END)), "loc_2740")

    #C0130
    ChrTalk(
        0x101,
        (
            "#6P#00000F（塞姆里亚石……\x01",
            "  那位占卜师正好\x01",
            "  送给我们一块呢。）\x02\x03",

            "#00003F（还有碎片……\x01",
            "  手上正巧\x01",
            "  也有一些呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27B2")

    label("loc_2740")


    #C0131
    ChrTalk(
        0x101,
        (
            "#6P#00000F（塞姆里亚石……\x01",
            "  那位占卜师正好\x01",
            "  送给我们一块呢。）\x02\x03",

            "#00003F（至于碎片……\x01",
            "  不妨四处找找看。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27B2")

    Jump("loc_27F4")

    label("loc_27B7")


    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#00003F（碎片吗……说起来，\x01",
            "  我们手上正好有一些呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F4")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x8,
        (
            "#11P哦哦，\x01",
            "难道你们有办法弄到吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#11P太好了，那我就开始\x01",
            "做制造武器的准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#11P如果你们得到了『塞姆里亚石』\x01",
            "或五个『塞姆里亚石碎片』，\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        "#11P到时候，我立刻就能给你们制造新武器。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#6P#00000F嗯，我明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x18A, 7)
    EventEnd(0x5)
    Return()

    # Function_9_22FE end

    def Function_10_293B(): pass

    label("Function_10_293B")

    EventBegin(0x0)
    Fade(500)
    OP_68(2470, 1400, 4820, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(18430, 0)
    SetChrPos(0x101, 2240, 0, 4730, 90)
    SetChrPos(0x102, 870, 0, 5250, 90)
    SetChrPos(0x103, 1540, 0, 3220, 45)
    SetChrPos(0x104, 2040, 0, 6260, 135)
    SetChrPos(0xF4, 1080, 0, 6920, 135)
    SetChrPos(0xF5, 380, 0, 3940, 90)
    OP_93(0x8, 0x10E, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B92")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_END)), "loc_2A78")

    #C0138
    ChrTalk(
        0x8,
        (
            "#11P那是塞姆里亚石……！\x01",
            "哈哈，你们弄到手了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#11P有了那东西，\x01",
            "就可以制造一个人的武器了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE4")

    label("loc_2A78")


    #C0140
    ChrTalk(
        0x8,
        (
            "#11P哦哦，这是塞姆里亚石碎片……\x01",
            "你们集够五个了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#11P有了那些碎片，\x01",
            "就可以制造一个人的武器了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE4")


    #C0142
    ChrTalk(
        0x8,
        (
            "#11P我随时都可以开始制造……\x01",
            "……如何，要试试看吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#6P#00000F嗯，那就麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        "#11P嘿嘿，很好！\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#11P要制造哪件武器呢？\x01",
            "考虑清楚之后再做决定吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2BBE")

    label("loc_2B92")


    #C0146
    ChrTalk(
        0x8,
        "#11P哦？已经决定好要制造哪件武器了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_2BBE")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "无限之光　　　　（罗伊德）\x01",      # 0
            "能天使威光　　　（艾莉）\x01",        # 1
            "宇宙崩坏　　　　（缇欧）\x01",        # 2
            "屠龙深渊　　　　（兰迪）\x01",        # 3
            "日耀弧光　　　　（诺艾尔）\x01",      # 4
            "七耀圣腕　　　　（瓦吉）\x01",        # 5
            "曳影之剑　　　　（莉夏）\x01",        # 6
            "制裁　　　　　　（达德利）\x01",      # 7
            "放弃\x01",                            # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3256")

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00000F那就请您制造\x01",
            "这件武器吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('塞姆里亚石', 0x0)"), scpexpr(EXPR_END)), "loc_2D43")
    SubItemNumber('塞姆里亚石', 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_2D8F")

    label("loc_2D43")

    SubItemNumber('塞姆里亚石碎片', 5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了５个。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_2D8F")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0150
    ChrTalk(
        0x8,
        (
            "#11P好～那就让我\x01",
            "大展身手吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    Sound(956, 0, 100, 0)
    Sleep(500)
    Sound(378, 0, 100, 0)
    Sleep(800)
    Sound(956, 0, 100, 0)
    Sleep(900)
    Sound(288, 0, 50, 0)
    Sleep(1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0151
    ChrTalk(
        0x8,
        (
            "#11P……来！做好了。\x01",
            "收下吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E76")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '无限之光'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('无限之光', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_2E76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED1")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0153
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '能天使威光'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('能天使威光', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_2ED1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2C")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0154
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '宇宙崩坏'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('宇宙崩坏', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_2F2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F87")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '屠龙深渊'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('屠龙深渊', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_2F87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE2")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0156
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '日耀弧光'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('日耀弧光', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_2FE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303D")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '七耀圣腕'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('七耀圣腕', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_303D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3098")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '曳影之剑'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('曳影之剑', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_30EE")

    label("loc_3098")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30EE")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0159
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '制裁'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('制裁', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_30EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D2")

    #C0160
    ChrTalk(
        0x101,
        (
            "#6P#00000F非常感谢您，基约姆师傅。\x01",
            "我们一定会好好使用它的。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#11P嘿嘿，不用客气！\x01",
            "身为技师，能用上如此珍贵的素材，\x01",
            "也算是三生有幸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "#11P你们就用这件武器，彻底解决\x01",
            "发生在克洛斯贝尔的事件吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E0(0x14, 0x0)
    SetScenarioFlags(0x18B, 1)
    Jump("loc_324E")

    label("loc_31D2")


    #C0163
    ChrTalk(
        0x8,
        (
            "#11P在这种特殊时期，\x01",
            "它一定能发挥作用……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        "#11P总之，你们就多加努力吧！\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#6P#00000F是，我们一定会好好使用的。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_324E")

    ClearScenarioFlags(0x0, 3)
    Jump("loc_32B4")

    label("loc_3256")


    #C0166
    ChrTalk(
        0x8,
        "#11P是吗？嗯，会犹豫也是理所当然的。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "#11P决定好要制造哪件武器之后，\x01",
            "就再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_32B4")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_293B end

    def Function_11_32E4(): pass

    label("Function_11_32E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3326")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331D")
    Call(0, 17)
    Return()

    label("loc_331D")

    Call(0, 19)
    Return()

    label("loc_3326")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3343")
    Call(0, 23)
    Return()

    label("loc_3343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E3")
    SetScenarioFlags(0x191, 5)
    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0x105,
        (
            "#10300F阿巴斯，你在这里\x01",
            "帮忙做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "#04100F哦，目前正在尽我所能，\x01",
            "帮忙对建材进行\x01",
            "修理和加工。\x02\x03",

            "#04102F细致工作比想象中要多，\x01",
            "但做起来还挺开心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#00005F开心吗……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00100F对了，阿巴斯先生也\x01",
            "负责『崔尼蒂』的\x01",
            "烹饪工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "#04100F嗯，以前是由我负责的。\x02\x03",

            "不过，最近已经转交给\x01",
            "良和亚泽尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，别看阿巴斯这个样子，\x01",
            "其实他的手很巧。\x02\x03",

            "#10304F不光是烹饪和手工，\x01",
            "连裁缝都是他的拿手活呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00305F哦？这可真是\x01",
            "不为人知的一面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        (
            "#00200F阿巴斯先生将来也许会\x01",
            "成为很棒的家庭主夫呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x109,
        (
            "#10106F嗯～而且总觉得他\x01",
            "还有不少优点尚未展现。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10309F呵呵，话说在先，\x01",
            "阿巴斯可是只属于\x01",
            "我一个人的哦⊥\x02\x03",

            "#10304F不过，如果只是暂时出借，\x01",
            "我还是可以考虑一下的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xA)

    #C0178
    ChrTalk(
        0xA,
        (
            "#04100F……到底在说什么啊。\x02\x03",

            "总之，我暂时会在这里\x01",
            "给基约姆师傅\x01",
            "打下手。\x02\x03",

            "如果有什么事，你们随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00002F好、好的……\x02\x03",

            "#00003F（阿巴斯……\x01",
            "  真是个充满谜团的人啊。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_373E")

    label("loc_36E3")

    TalkBegin(0xFE)

    #C0180
    ChrTalk(
        0xA,
        (
            "#04100F我暂时会在这里\x01",
            "给基约姆师傅\x01",
            "打下手。\x02\x03",

            "如果有什么事，你们随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_373E")

    Return()

    # Function_11_32E4 end

    def Function_12_373F(): pass

    label("Function_12_373F")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_12_373F end

    def Function_13_3749(): pass

    label("Function_13_3749")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CD")

    #C0181
    ChrTalk(
        0x9,
        (
            "这就是缇欧\x01",
            "目前正在使用的\x01",
            "魔导杖的设计图……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "哦哦，从构造来看，\x01",
            "似乎又是个高输出的产物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "没问题，我会做好准备的。\x01",
            "等小姑娘一回来，马上就能进行改造。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        "哎呀，真是帮了我的大忙～\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "这样一来，缇欧回来以后也能\x01",
            "继续顺畅地使用魔导杖了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "对了，那个小姑娘的\x01",
            "归期又推迟了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "嗯，是啊～！\x01",
            "据说又额外增加了不少工作～！\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "我最近每隔一个小时就联络她一次，\x01",
            "但她却不怎么回应，\x01",
            "真是担心死了～！\x02",
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
    OP_63(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0x8,
        "……那是因为你太烦人了吧。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#00012F（罗伯兹主任还是老样子啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_3A88")

    label("loc_39CD")


    #C0191
    ChrTalk(
        0x9,
        (
            "不知道缇欧有没有\x01",
            "好好吃饭……\x01",
            "会不会工作得太拼命，累坏自己的身体呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "啊啊！我又开始担心了～！\x01",
            "回财团之后，还要再联系她一次……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        (
            "#00106F（唔……\x01",
            "  这实在是保护过度了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A88")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_3749 end

    def Function_14_3A91(): pass

    label("Function_14_3A91")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(0, 2000, 500, 0)
    MoveCamera(35, 17, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16980, 0)
    SetChrPos(0x101, 0, 0, 1000, 45)
    SetChrPos(0x102, -1000, 0, 1000, 45)
    SetChrPos(0x109, 0, 0, 0, 45)
    SetChrPos(0x105, -1000, 0, 0, 45)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(600)
    TurnDirection(0x8, 0x0, 500)
    Sleep(300)

    #C0194
    ChrTalk(
        0x8,
        (
            "#11P哦？是你们啊，\x01",
            "真是好久不见啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2990, 1300, 3770, 2000)
    MoveCamera(49, 15, 0, 2000)
    OP_6E(440, 2000)
    SetCameraDistance(19900, 2000)

    def lambda_3B8A():
        OP_96(0xFE, 0xBB8, 0x0, 0xEBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B8A)
    Sleep(400)

    def lambda_3BA7():
        OP_96(0xFE, 0x6A4, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BA7)
    Sleep(400)

    def lambda_3BC4():
        OP_96(0xFE, 0xCE4, 0x0, 0xAD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3BC4)
    Sleep(400)

    def lambda_3BE1():
        OP_96(0xFE, 0x7D0, 0x0, 0x8DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BE1)
    WaitChrThread(0x101, 1)

    def lambda_3BFF():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BFF)
    WaitChrThread(0x102, 1)

    def lambda_3C10():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C10)
    WaitChrThread(0x109, 1)

    def lambda_3C21():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3C21)
    WaitChrThread(0x105, 1)

    def lambda_3C32():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3C32)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0195
    ChrTalk(
        0x101,
        "#6P#00000F您好，基约姆师傅。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        "#6P#00100F久疏问候了。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "#11P哈哈，\x01",
            "不用这么毕恭毕敬的。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#11P对了，我已经听说了，\x01",
            "圣书会的首领竟然会\x01",
            "加入特别任务支援科。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        "#11P真是的，着实让我吃了一惊啊。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，谢谢夸奖。\x02\x03",

            "#10302F对了，以后要是再找您\x01",
            "改造武器，就不会像\x01",
            "以前一样拒绝我了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D7A():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3D7A)

    def lambda_3D87():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3D87)
    TurnDirection(0x102, 0x105, 500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x101,
        "#00006F瓦吉，你还真是见缝就钻啊……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        "#11P哈哈，这个嘛。\x02",
    )

    CloseMessageWindow()

    def lambda_3E0F():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3E0F)

    def lambda_3E1C():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E1C)
    TurnDirection(0x102, 0x8, 500)

    #C0203
    ChrTalk(
        0x8,
        (
            "#11P只要不用于打架，\x01",
            "帮你改造也没问题哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x109,
        (
            "#12P#10100F改造店『基约姆工房』。\x02\x03",

            "#10104F听说这里不仅可以\x01",
            "修理导力制品，\x01",
            "还可以改造武器……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x109, 500)

    #C0205
    ChrTalk(
        0x8,
        "#5P哦？小姑娘，你也是新面孔啊。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "#5P说是改造，其实也只是在\x01",
            "不会带来危险的范围内\x01",
            "进行强化而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "#5P毕竟我最近已经拿到营业许可了，\x01",
            "不会做那种触犯法律的傻事。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        (
            "#5P总之，如果得到了什么好素材，\x01",
            "就来找我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        "#10100F#12P好、好的，我明白了。\x02",
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在『基约姆工房』，\x01\x07\x02",

            "　可以利用Ｕ材料\x07\x05",
            "等素材进行改造，从而获得\x01",
            "　性能比普通装备更强的改造品。\x02\x03",

            "※只要与柜台的基约姆对话，\x01",
            "　并选择『委托改造』，\x01",
            "　就会出现改造菜单。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 3000, 0, 3770, 45)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x138, 3)
    EventEnd(0x5)
    Return()

    # Function_14_3A91 end

    def Function_15_40DA(): pass

    label("Function_15_40DA")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(4500, 1000, 5330, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 3000, 0, 5000, 90)
    SetChrPos(0x102, 2800, 0, 4000, 90)
    SetChrPos(0x103, 1700, 0, 4300, 90)
    SetChrPos(0x109, 1900, 0, 5300, 90)
    SetChrPos(0x105, 2700, 0, 6500, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0211
    ChrTalk(
        0x8,
        "#11P哦！你们几个！\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#11P兰迪那家伙\x01",
            "到底怎么了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "#11P他让我给他检修了\x01",
            "很不寻常的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#6P#00006F他果然来过这里……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#6P#00101F是在今天早上吧？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "#11P是啊，五点左右的时候，\x01",
            "他突然跑来。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "#11P我当时刚好通宵赶工完毕，\x01",
            "所以就顺便答应了他的请求……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        (
            "#6P#00201F那么……\x01",
            "『很不寻常的东西』是指……？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x109,
        (
            "#6P#10101F应该……\x01",
            "是重型火器之类的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "#11P没错……但他只拿来一些\x01",
            "拆解下来的部件而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x8,
        (
            "#11P于是我就替他检修了那些\x01",
            "已经闲置了一段时日的\x01",
            "机关部位、排气零件等等……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "#11P如果把那些零件组装起来，\x01",
            "肯定会是一件很惊人的武器。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_4406")

    #C0223
    ChrTalk(
        0x105,
        (
            "#10308F应该就是兰迪以前用过的那把\x01",
            "导力来复枪吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_443C")

    label("loc_4406")


    #C0224
    ChrTalk(
        0x105,
        (
            "#10308F看来是兰迪以前用过的\x01",
            "特别定制版来复枪吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_443C")


    #C0225
    ChrTalk(
        0x101,
        (
            "#6P#00006F嗯……\x01",
            "应该没错。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#6P#00101F基约姆师傅，\x01",
            "多谢您提供情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        "#11P哦，不用客气。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#11P我虽然不清楚到底发生了什么事……\x01",
            "但从那小子的表情来看，\x01",
            "他似乎钻进了牛角尖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#11P你们这些同伴可要\x01",
            "全力帮他走出来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#6P#00000F当然！\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        "#6P#10100F明白了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 2500, 0, 5330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x165, 7)
    OP_29(0xAA, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_15_40DA end

    def Function_16_458B(): pass

    label("Function_16_458B")

    EventBegin(0x0)
    Fade(500)
    OP_68(13180, 2300, 7330, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13690, 1000, 7530, 180)
    SetChrPos(0x102, 12750, 1000, 7960, 180)
    SetChrPos(0x103, 13900, 1000, 8650, 180)
    SetChrPos(0x104, 12810, 1000, 9200, 180)
    SetChrPos(0x105, 13890, 1000, 9740, 180)
    SetChrPos(0x109, 12050, 1000, 9950, 180)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00000F基约姆师傅……\x01",
            "请问您有没有金属探测器\x01",
            "之类的东西？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        "金属探测器……？\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "我记得以前好像制造过\x01",
            "那种东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#00309F哦！看来没找错人啊，\x01",
            "真不愧是导力技师。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "不过，那也只是\x01",
            "做着玩的东西而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        "话说回来，你们要那东西干嘛？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#00000F其实是这样的……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将协助卡农回收废弃材料\x01",
            "一事做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0240
    ChrTalk(
        0x8,
        (
            "原来如此……\x01",
            "看来确实需要那东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "明白了，就把它\x01",
            "借给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "稍等一下，我好像\x01",
            "放到里面了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4800():

        label("loc_4800")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4800")

    QueueWorkItem2(0x109, 0, lambda_4800)

    def lambda_4812():

        label("loc_4812")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4812")

    QueueWorkItem2(0x102, 0, lambda_4812)

    def lambda_4824():

        label("loc_4824")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4824")

    QueueWorkItem2(0x104, 0, lambda_4824)

    def lambda_4836():

        label("loc_4836")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4836")

    QueueWorkItem2(0x101, 0, lambda_4836)

    def lambda_4848():

        label("loc_4848")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4848")

    QueueWorkItem2(0x105, 0, lambda_4848)

    def lambda_485A():

        label("loc_485A")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_485A")

    QueueWorkItem2(0x103, 0, lambda_485A)
    OP_95(0x8, 15210, 1000, 6330, 2000, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(1500)
    OP_95(0x8, 13130, 1000, 6290, 2000, 0x0)
    OP_93(0x8, 0x0, 0x1F4)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x102, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x104, 0x0)
    EndChrThread(0x109, 0x0)
    EndChrThread(0x105, 0x0)

    #C0243
    ChrTalk(
        0x8,
        (
            "哦，找到了、找到了。\x01",
            "来，给你。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0244
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '金属探测器'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('金属探测器', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0245
    ChrTalk(
        0x103,
        (
            "#00205F看上去相当精致呢。\x02\x03",

            "#00203F说不定都能媲美警方\x01",
            "使用的正规探测器了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#00105F真、真是相当\x01",
            "厉害啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "哈哈，其实也就是外观\x01",
            "还算像模像样而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        (
            "其实这东西的导力消耗量\x01",
            "很糟糕，是个不怎么\x01",
            "拿得出手的作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        "对了，你们知道怎么用吗？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x109,
        (
            "#10103F我在出入境检查时\x01",
            "曾使用过几次。\x02\x03",

            "#10102F只要在可能存在金属的地方\x01",
            "启动机器就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        "差不多就是那样吧。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "只要在机器有反应的地方\x01",
            "仔细调查一番，\x01",
            "应该就能找到金属了。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "另外，如果运气好，\x01",
            "说不定还能找到别的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004F原来如此……\x01",
            "我明白了。\x02\x03",

            "#00000F那么，我们就暂时借用一下了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※金属探测器只能在旧城区的\x01",
            "  室外场景中使用。\x01",
            "  按『△键＋Ｌ键』即可启动。\x02\x03",

            "※此外，也可以在主菜单的\x01",
            "  [ITEMS]选项中点选使用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x196, 5)
    OP_29(0x8E, 0x1, 0x7)
    SetChrPos(0x8, 13130, 1000, 6290, 180)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 12990, 1000, 9600, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_16_458B end

    def Function_17_4C43(): pass

    label("Function_17_4C43")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(58, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 12710, 990, 10110, 90)
    SetChrPos(0x103, 13360, 1000, 7350, 90)
    SetChrPos(0x104, 12750, 1000, 8440, 90)
    SetChrPos(0x105, 13580, 1000, 9460, 90)
    SetChrPos(0x109, 12000, 1000, 9100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    #C0256
    ChrTalk(
        0x105,
        "#10300F呵呵，你很努力嘛。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xA,
        (
            "#04100F瓦吉……\x01",
            "还有支援科的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        "你们是来了解委托详情的吧？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00000F是的，请向我们说明一下\x01",
            "现在的状况吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00103F从外面的状况来看，\x01",
            "距离完成重建，似乎还有一段\x01",
            "很长的路要走呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xA,
        (
            "#04100F嗯，正如你所说。\x02\x03",

            "虽然我们圣书会已经\x01",
            "带动着旧城区的全体居民，\x01",
            "开始了各种重建工作……\x02\x03",

            "但袭击造成的创痕实在是太严重了，\x01",
            "进展情况不容乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        (
            "#00303F说起来，\x01",
            "是魔人化的瓦鲁多亲手\x01",
            "袭击了旧城区呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x109,
        (
            "#10101F各位居民已经\x01",
            "知道这件事了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xA,
        (
            "#04100F不……除了剑蛇帮的\x01",
            "成员之外，应该没有人\x01",
            "察觉到这件事。\x02\x03",

            "毕竟他是以那种异形的\x01",
            "姿态出现的。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#00203F了解真相只会让大家受到严重打击……\x01",
            "暂时不公开也好。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x105,
        "#10303F………………\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "#04100F……我们先不谈\x01",
            "这个话题了。\x02\x03",

            "现在最重要的还是如何\x01",
            "推进这里的重建工作。\x02\x03",

            "这里毕竟是旧城区，\x01",
            "政府恐怕不会提供援助，\x01",
            "而且我们也没有雇佣专业人员的资金。\x02\x03",

            "如果特别任务支援科能施以援手，\x01",
            "那就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        "#00003F这样啊……\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_17_4C43 end

    def Function_18_5098(): pass

    label("Function_18_5098")

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
            "协助重建旧城区\x01",      # 0
            "再考虑一下\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5102"),
        (1, "loc_5112"),
        (SWITCH_DEFAULT, "loc_5250"),
    )


    label("loc_5102")

    OP_29(0x8E, 0x4, 0x2)
    SetScenarioFlags(0x196, 0)
    Call(0, 20)
    Jump("loc_5250")

    label("loc_5112")


    #C0269
    ChrTalk(
        0x101,
        (
            "#00006F我们很想提供协助……\x01",
            "但也要考虑到其它工作的进程。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x105,
        (
            "#10300F对了，可以稍后再来\x01",
            "接受委托吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "#04100F当然，只要你们愿意帮忙，\x01",
            "随时都可以过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "我并没有勉强各位的意思。\x01",
            "但如果有时间，还请前来协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#00000F好的，\x01",
            "我们会尽量安排时间过来的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 1)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13510, 1000, 9270, 90)
    EventEnd(0x5)
    Jump("loc_5250")

    label("loc_5250")

    Return()

    # Function_18_5098 end

    def Function_19_5251(): pass

    label("Function_19_5251")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(58, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 12710, 990, 10110, 90)
    SetChrPos(0x103, 13360, 1000, 7350, 90)
    SetChrPos(0x104, 12750, 1000, 8440, 90)
    SetChrPos(0x105, 13580, 1000, 9460, 90)
    SetChrPos(0x109, 12000, 1000, 9100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    #C0274
    ChrTalk(
        0xA,
        (
            "#04100F如何，可以协助我们\x01",
            "重建旧城区吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_19_5251 end

    def Function_20_5349(): pass

    label("Function_20_5349")


    #C0275
    ChrTalk(
        0x101,
        "#00000F嗯，交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        "#04100F感激不尽。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        (
            "嘿嘿，我就知道\x01",
            "你们会答应。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        (
            "#10300F那么，我们该\x01",
            "着手于哪些方面？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xA,
        (
            "#04100F目前，旧城区的重建工作\x01",
            "主要集中在三个地方。\x02\x03",

            "一个是『莲花公馆』，\x01",
            "有人在那里准备赈济给各位居民的食物。\x02\x03",

            "一个是『伊梅尔达馆』的废墟，\x01",
            "有人正在那附近回收废弃材料。\x02\x03",

            "最后就是这里——\x01",
            "『基约姆工房』，\x01",
            "我们正在收集和加工建筑材料。\x02\x03",

            "请你们去这几个地方，\x01",
            "看看有没有什么\x01",
            "需要帮忙的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#00103F原来如此……\x01",
            "都是相当重要的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x109,
        (
            "#10105F对了，这里的\x01",
            "具体工作是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "哦，为了重建被毁坏的建筑，\x01",
            "我正在置备所需的建筑材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "虽说工房里的剩余素材\x01",
            "也能派上点用场……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        "但我刚刚发现了一个很严重的问题。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x103,
        "#00205F问题？指的是……？\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "很简单，就是重组建材时所需的\x01",
            "螺丝、钉子等零件不足。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "这样下去，根本就无法\x01",
            "修理那些被毁建筑。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x104,
        (
            "#00305F外面堆着各种乱七八糟的东西……\x01",
            "那些散落在各处的废品\x01",
            "都派不上用场吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xA,
        (
            "#04100F嗯，我已经拜托一个名叫卡农的\x01",
            "孩子多加留意了……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "但主要还是为了筹集资金，\x01",
            "才会让他四处\x01",
            "寻找的。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "另外，零件的强度也是个问题，\x01",
            "尽量还是使用新品为好。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        (
            "#10306F哎呀呀，这可真难办啊。\x02\x03",

            "#10300F按照您的意思，\x01",
            "我们是不是应该去\x01",
            "采购螺丝和钉子呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "不，还有比那\x01",
            "更好的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "改造装备时使用的『Ｕ材料』\x01",
            "也是一种可以使用的素材。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "只要有那种素材，\x01",
            "我就可以制造出各种零件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#00203F『Ｕ材料』吗……\x01",
            "那种东西好像也很难收集呢。\x02\x03",

            "#00200F大概需要多少个呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "这个嘛……\x01",
            "十个就绰绰有余了。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        "怎么样，你们能弄到手吗？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#00000F我明白了。\x01",
            "收集到足够数量之后，会给您拿来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xA,
        "#04100F那就拜托你们了，特别任务支援科的各位。\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_5943():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5943)
    Sleep(250)

    def lambda_5953():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5953)
    Sleep(50)

    def lambda_5963():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5963)
    Sleep(50)

    def lambda_5973():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5973)
    Sleep(50)

    def lambda_5983():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5983)
    Sleep(500)

    #C0301
    ChrTalk(
        0x101,
        (
            "#00004F好，那我们就赶快\x01",
            "去各处帮忙吧。\x02\x03",

            "#00000F接下来，还要去了解一下\x01",
            "烹饪赈济餐和回收废弃材料这两方面的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#10300F明白了，队长。\x02\x03",

            "这可是我老巢的大危机呢，\x01",
            "我一定会全力相助的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【支援旧城区的重建】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x8E, 0x1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x8, 0x0, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13200, 1000, 8320, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_5349 end

    def Function_21_5AED(): pass

    label("Function_21_5AED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('Ｕ材料', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B61")

    #C0304
    ChrTalk(
        0x8,
        "你们要给我Ｕ材料吗？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "……怎么回事，\x01",
            "这数量不对啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "我需要十个哦。\x01",
            "拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C80")

    label("loc_5B61")


    #C0307
    ChrTalk(
        0x8,
        (
            "哦……\x01",
            "看来你们已经收集够了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        (
            "我需要十个Ｕ材料，\x01",
            "可以交给我吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        1,
        -1,
        -1,
        0,
        (
            "交出\x01",      # 0
            "不交\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5C07"),
        (1, "loc_5C0F"),
        (SWITCH_DEFAULT, "loc_5C80"),
    )


    label("loc_5C07")

    Call(0, 22)
    Jump("loc_5C80")

    label("loc_5C0F")


    #C0309
    ChrTalk(
        0x8,
        (
            "是吗，我可以理解。\x01",
            "对你们来说，这也是很重要的素材呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "不过，如果有多余的，\x01",
            "希望你们能送给我一些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C80")

    label("loc_5C80")

    Return()

    # Function_21_5AED end

    def Function_22_5C81(): pass

    label("Function_22_5C81")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(58, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 12710, 990, 10110, 90)
    SetChrPos(0x103, 13360, 1000, 7350, 90)
    SetChrPos(0x104, 12750, 1000, 8440, 90)
    SetChrPos(0x105, 13580, 1000, 9460, 90)
    SetChrPos(0x109, 12000, 1000, 9100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0xA, 15240, 1000, 9210, 180)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    #C0311
    ChrTalk(
        0x101,
        "#00000F那就交给您了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0312
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了１０个。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('Ｕ材料', 10)

    #C0313
    ChrTalk(
        0x8,
        (
            "嘿嘿，谢啦。\x01",
            "我就不跟你们客气了。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "这样一来，修理工作\x01",
            "也算是有眉目了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#00102F呵呵，很高兴能帮上您的忙。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#00300F建设工作如果需要人手，\x01",
            "我们也可以帮忙哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x109,
        (
            "#10109F没错没错，\x01",
            "如果是力气活，我还是很有自信的！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "不用了，哪能麻烦\x01",
            "你们做那种事。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "旧城区就得靠旧城区的居民\x01",
            "亲手重建。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x105,
        (
            "#10303F也对，反正有阿巴斯和圣书会的\x01",
            "各位带头工作。\x02\x03",

            "#10309F你们就多加努力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x103,
        "#00206F说得就好像事不关己一样……\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xA,
        (
            "#04102F呵呵，没关系。\x01",
            "我们和瓦吉\x01",
            "有不同的职责。\x02\x03",

            "#04100F……真是谢谢你们了，\x01",
            "特别任务支援科的各位。\x02\x03",

            "如果有时间，\x01",
            "请你们也去其它地方帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 2)
    OP_29(0x8E, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6102")

    #C0323
    ChrTalk(
        0x101,
        (
            "#00000F嗯，交给我们吧。\x02\x03",

            "#00005F不过，我们已经把\x01",
            "几个地方的事情都解决了……\x02\x03",

            "#00000F接下来，我们会在旧城区巡视一圈，\x01",
            "再给大家尽些绵力。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xA,
        (
            "#04100F那可真是多谢了。\x01",
            "……好，稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Jump("loc_6119")

    label("loc_6102")


    #C0325
    ChrTalk(
        0x101,
        "#00000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    label("loc_6119")

    SetChrPos(0x8, 13130, 1000, 6290, 180)
    SetChrPos(0xA, 15170, 1000, 8560, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 13840, 1000, 8410, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_5C81 end

    def Function_23_6176(): pass

    label("Function_23_6176")

    EventBegin(0x0)
    Fade(500)
    OP_68(14350, 2300, 8850, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x8, 15240, 1000, 7610, 0)
    SetChrPos(0xA, 15240, 1000, 9210, 180)
    SetChrPos(0x101, 13840, 1000, 8410, 90)
    SetChrPos(0x102, 13840, 1000, 9610, 90)
    SetChrPos(0x103, 13840, 1000, 7210, 90)
    SetChrPos(0x104, 12750, 1000, 8410, 90)
    SetChrPos(0x105, 12750, 1000, 9610, 90)
    SetChrPos(0x109, 12750, 1000, 7210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_0D()

    #C0326
    ChrTalk(
        0xA,
        "#04100F怎么……？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "难道已经全部\x01",
            "处理好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        "#00000F是的，已经把该做的事情都做好了。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xA,
        (
            "#04100F是吗……\x01",
            "真是辛苦你们了。\x02\x03",

            "离发放赈济餐还有一段时间。\x01",
            "在那之前，你们可以先去别处随便逛逛。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#00100F既然如此，干脆就在\x01",
            "旧城区里巡视一圈吧。\x02\x03",

            "#00104F说不定还能帮上大家\x01",
            "一些小忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xA,
        (
            "#04100F那可真是多谢了。\x01",
            "……好，稍后再见吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7101", "ed7150")
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_6176 end

    SaveToFile()

Try(main)
