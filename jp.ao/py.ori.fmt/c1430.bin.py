from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ギヨーム親方",           # 1
        "ロバーツ主任",           # 2
        "アッバス",               # 3
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
        "Function_6_851",          # 06, 6
        "Function_7_21EB",         # 07, 7
        "Function_8_27E6",         # 08, 8
        "Function_9_2921",         # 09, 9
        "Function_10_3082",        # 0A, 10
        "Function_11_3B69",        # 0B, 11
        "Function_12_4056",        # 0C, 12
        "Function_13_4060",        # 0D, 13
        "Function_14_443E",        # 0E, 14
        "Function_15_4B57",        # 0F, 15
        "Function_16_5094",        # 10, 16
        "Function_17_5822",        # 11, 17
        "Function_18_5CEB",        # 12, 18
        "Function_19_5EEA",        # 13, 19
        "Function_20_5FEE",        # 14, 20
        "Function_21_686E",        # 15, 21
        "Function_22_6A5C",        # 16, 22
        "Function_23_6FAF",        # 17, 23
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
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

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B8")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 0)
    MenuCmd(1, 0, "話をする")
    MenuCmd(1, 0, "改造を頼む")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_598")
    MenuCmd(1, 0, "Ｕマテリアルを渡す")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C0")
    MenuCmd(1, 0, "金属探知機について聞く")

    label("loc_5C0")

    MenuCmd(1, 0, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_601")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_601")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_625")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_625")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648")
    OP_AF(0xAD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_671")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_671")
    Call(0, 21)
    Return()

    label("loc_671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    Return()

    label("loc_6A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B3")

    label("loc_6B3")

    Jump("loc_53E")

    label("loc_6B8")

    Jump("loc_850")

    label("loc_6BD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_738")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "改造を頼む\x01",            # 1
            "武器の作成を頼む\x01",      # 2
            "やめる\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_778")

    label("loc_738")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",        # 0
            "改造を頼む\x01",      # 1
            "やめる\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_778")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_778")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_794")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_794")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_804")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_7B3")
    OP_AF(0xAE)
    Jump("loc_7F5")

    label("loc_7B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7C3")
    OP_AF(0xAD)
    Jump("loc_7F5")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7D3")
    OP_AF(0xAC)
    Jump("loc_7F5")

    label("loc_7D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7EC")
    OP_AF(0xAF)
    Jump("loc_7EE")

    label("loc_7EC")

    OP_AF(0xAB)

    label("loc_7EE")

    Jump("loc_7F5")

    label("loc_7F3")

    OP_AF(0xAA)

    label("loc_7F5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84B")

    label("loc_804")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81B")
    Call(0, 10)
    Jump("loc_84B")

    label("loc_81B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82F")
    Jump("loc_84B")

    label("loc_82F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 6)

    label("loc_84B")

    Jump("loc_6C7")

    label("loc_850")

    Return()

    # Function_5_514 end

    def Function_6_851(): pass

    label("Function_6_851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986")

    #C0001
    ChrTalk(
        0x8,
        (
            "あんなものが現れるたぁ……\x01",
            "一難去ってまた一難ってヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "……お前ぇら、あの《大樹》に\x01",
            "乗り込むつもりなら、\x01",
            "徹底的に準備を整えていけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "化物みてえな奴らを\x01",
            "相手にしようってんなら、武器の強化も\x01",
            "しすぎるってこたぁねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#00000Fええ……よろしくお願いします！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A10")

    label("loc_986")


    #C0005
    ChrTalk(
        0x8,
        (
            "お前ぇらも大変だろうが……\x01",
            "絶対に挫けんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "俺も武器の改造くらいしかできねえが、\x01",
            "出来る限りのことをさせてもらうからよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A10")

    Jump("loc_21EA")

    label("loc_A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBC")

    #C0007
    ChrTalk(
        0x8,
        (
            "お前ぇら……\x01",
            "はは、無事だったか！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "ダドリーたちとは\x01",
            "無事に合流できたみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00000Fええ、おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#00304Fギヨームのオッサン、\x01",
            "《ベルゼルガー》の修理……\x01",
            "改めてあんがとよ。\x02\x03",

            "#00300Fおかげで市外にいる間は\x01",
            "随分と助けられたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "へへ、いいってことよ。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ただ、機関部に弱点があるって事を\x01",
            "ちゃんと頭に入れておけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "その化け物ライフルは、\x01",
            "今度壊れたらすぐに直せる\x01",
            "保証はねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#00300Fああ、使うときは\x01",
            "ここぞの時だけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "よーし、分かってるならいい。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "大統領側も、どんな手を\x01",
            "使ってくるか分からねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "お前ぇらも武器のメンテナンスは\x01",
            "しっかりしておけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00000Fええ、またお世話になります。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 3)
    Jump("loc_D2A")

    label("loc_CBC")


    #C0019
    ChrTalk(
        0x8,
        (
            "大統領側も、どんな手を\x01",
            "使ってくるか分からねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "お前ぇらも武器のメンテナンスは\x01",
            "しっかりしておけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A")

    Jump("loc_21EA")

    label("loc_D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_F2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EAF")

    #C0021
    ChrTalk(
        0x8,
        (
            "クロスベル独立国に国防軍か……\x01",
            "こりゃまた、えれぇ事になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "お前らはこの話を聞かされてたのか？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00003Fいえ、俺たちも全くの初耳でした。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00101Fそれで、とにかく今は\x01",
            "情報を集めている所なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "そうか……お前らも大変だな。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "この先も色々あるとは思うが、\x01",
            "へこたれねえよう気張ってけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00304Fああ。\x01",
            "ありがとな、オッサン。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F29")

    label("loc_EAF")


    #C0028
    ChrTalk(
        0x8,
        (
            "しかしまあ、２大国を相手に\x01",
            "こうも堂々と喧嘩を売るたぁな。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "とにかく……しばらくは\x01",
            "成り行きを見守るっきゃねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F29")

    Jump("loc_21EA")

    label("loc_F2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1220")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FEB")

    #C0030
    ChrTalk(
        0x8,
        (
            "今んとこ昼間は復興関係、\x01",
            "夜は工房関係って感じで\x01",
            "仕事をさばかせてもらってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "おかげで休む暇はねえが、\x01",
            "なんつうか、頼りにされるってのは\x01",
            "嬉しいもんだよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1071")
    TurnDirection(0x8, 0x104, 0)

    #C0032
    ChrTalk(
        0x8,
        (
            "ブレードライフルの方は\x01",
            "何とか明後日中には\x01",
            "修理しちまうつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "ま、それまで\x01",
            "せいぜい待っててな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121B")

    label("loc_1071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_END)), "loc_10E3")

    #C0034
    ChrTalk(
        0x8,
        (
            "さてと、さっそく\x01",
            "Ｕマテリアルを加工しちまうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        "お前たち、本当にありがとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1189")

    label("loc_10E3")


    #C0036
    ChrTalk(
        0x8,
        (
            "今んとこ昼間は復興関係、\x01",
            "夜は工房関係って感じで\x01",
            "仕事をさばかせてもらってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "おかげで休む暇はねえが、\x01",
            "なんつうか、頼りにされるってのは\x01",
            "嬉しいもんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1189")

    Jump("loc_121B")

    label("loc_118E")


    #C0038
    ChrTalk(
        0x8,
        (
            "さっき俺も豚汁ってのを\x01",
            "いただいてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "たっぷりエネルギーを\x01",
            "充填させてもらったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "へへっ、おかげで\x01",
            "作業もはかどるってもんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121B")

    Jump("loc_21EA")

    label("loc_1220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_12B7")

    #C0041
    ChrTalk(
        0x8,
        (
            "ランディのヤツ、随分と\x01",
            "思いつめた顔をしてやがった。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "詳しい事情は知らんが……\x01",
            "こういう時こそ、お前たち仲間が\x01",
            "支えてやるんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_12B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_141B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138C")

    #C0043
    ChrTalk(
        0x8,
        "昨日、導力鉄道が脱線したんだってな。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "何でもデケエ化物が突然現れて\x01",
            "列車をぶっ飛ばしたらしいが……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "列車相手に力自慢でもしたかったのか？\x01",
            "なんつうか、ワケの分からん話だよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1416")

    label("loc_138C")


    #C0046
    ChrTalk(
        0x8,
        (
            "列車を襲った化物ってのは\x01",
            "一体何がしたかったんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "まさか力自慢ってワケじゃあるめえし……\x01",
            "なんつうか、よく分からん話だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1416")

    Jump("loc_21EA")

    label("loc_141B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_154A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C4")

    #C0048
    ChrTalk(
        0x8,
        "うし、これで導力灯の修理は完了っと。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "お次は……\x01",
            "戦術オーブメントのメンテナンスだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "まずは検査用の\x01",
            "結晶回路を準備して、と……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1545")

    label("loc_14C4")


    #C0051
    ChrTalk(
        0x8,
        (
            "結晶回路、結晶回路……\x01",
            "おっと、こいつは\x01",
            "一世代前の規格じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "ったく、いつもながら\x01",
            "紛らわしいったらありゃしねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1545")

    Jump("loc_21EA")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15D6")

    #C0053
    ChrTalk(
        0x8,
        (
            "ええと、お次は導力灯の修理を……\x01",
            "確か５件ほど溜めちまってたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "さ～て、昼飯時までに\x01",
            "サクッと片付けちまうとするか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_15D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_171A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1699")

    #C0055
    ChrTalk(
        0x8,
        (
            "色々議論されてはいるが、\x01",
            "独立問題ってのは恐ろしく\x01",
            "デリケートな問題だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "既に賛成派多数って話だが、\x01",
            "一定どれだけの人間が事の重要性を\x01",
            "把握してるんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1715")

    label("loc_1699")


    #C0057
    ChrTalk(
        0x8,
        (
            "独立の提唱が何をもたらすのか……\x01",
            "正直俺にもよく分からねえぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "だが、とにもかくにも\x01",
            "２大国の動向が気になる所だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1715")

    Jump("loc_21EA")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD6")

    #C0059
    ChrTalk(
        0x8,
        (
            "よう、嬢ちゃん。\x01",
            "どうやら財団の仕事は\x01",
            "区切りが付いたみてえだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        (
            "#00203Fはい、どちらかというと\x01",
            "無理やり付けた感じですが。\x02\x03",

            "#00200Fそういえば……\x01",
            "主任は定期的にここへ\x01",
            "顔を出しているんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "はは、まあな。\x01",
            "この前も新型魔導杖の設計図を\x01",
            "置いていきやがった所だぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x8,
        (
            "おっと、この話は嬢ちゃんには\x01",
            "言っちゃいけないんだったっけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "ロバーツのヤツ、うるせえからなあ。\x01",
            "俺が言ったってことは内緒だぜ？\x02",
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
            "#00203F……いえ、気にしないで下さい。\x02\x03",

            "#00211F主任が魔導杖の改造に\x01",
            "関わっている事は、\x01",
            "ほとんど確信していたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        "はは、確かにそりゃそうか。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "嬢ちゃんも知っての通り、\x01",
            "魔導杖ってヤツの構造は\x01",
            "とんでもなく複雑だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "流石の俺でも、誰の協力もなしに\x01",
            "おいそれといじれねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x109,
        (
            "#10105Fえっと、私には\x01",
            "よく分からないんですが……\x02\x03",

            "#10100Fロバーツさんはどうして\x01",
            "そのことをティオちゃんに\x01",
            "内緒にするんでしょうか？\x02\x03",

            "#10106Fそれも随分やり方が\x01",
            "遠回しというか何というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#00302Fはは、なんつったらいいのかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#00000F俺たちもあの人のことを\x01",
            "分かってるワケじゃないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#00100Fええ……でもおそらく\x01",
            "これも一種の親心なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        (
            "#00204F………………………………\x01",
            "理解したくはありませんが、\x01",
            "そんな所だと思います。\x02\x03",

            "#00200Fともかく、魔導杖のやり取りに#18R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#\x01",
            "関しては#8R㈲　㈲　㈲　㈲#もう慣れました。\x02\x03",

            "#00204F皆さんもあまり気にしないで下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14D, 3)
    Jump("loc_1D41")

    label("loc_1CD6")


    #C0073
    ChrTalk(
        0x8,
        (
            "ま、とりあえず嬢ちゃんの魔導杖も\x01",
            "さっそく改造してやれるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "必要な時はいつでも言ってくれよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1D41")

    Jump("loc_21EA")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E44")

    #C0075
    ChrTalk(
        0x8,
        (
            "さっきオルキスタワーってのを\x01",
            "チラッと見て来たんだが、\x01",
            "なんつうか……とんでもねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "最新鋭の設備なんかは\x01",
            "技術屋として興味はあるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "なんつうか、\x01",
            "“力”を誇示してるみてえで\x01",
            "どうにも好きになれねえんだよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EDB")

    label("loc_1E44")


    #C0078
    ChrTalk(
        0x8,
        (
            "オルキスタワーてのは、\x01",
            "まったくとんでもねえ建物だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "最新鋭の設備なんかは\x01",
            "技術屋として興味はあるんだが……\x01",
            "オレはどうにも好きになれねえや。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDB")

    Jump("loc_21EA")

    label("loc_1EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1F69")

    #C0080
    ChrTalk(
        0x8,
        (
            "特務支援課も、\x01",
            "あとはティオ嬢ちゃんを\x01",
            "残すのみってわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "へっ、早くまたあの魔導杖を\x01",
            "いじってみてえモンだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EA")

    label("loc_1F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_20A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2037")

    #C0082
    ChrTalk(
        0x8,
        "今日は珍しく雨が降ってやがるな。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "湿っぽくて敵わねえ……\x01",
            "つうか、この湿気ってヤツは\x01",
            "精密機械にとって何かと厄介でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "機関部をいじる時なんかは\x01",
            "けっこう神経を使うぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A3")

    label("loc_2037")


    #C0085
    ChrTalk(
        0x8,
        (
            "湿気ってヤツは、\x01",
            "精密機械にとって何かと厄介でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "機関部をいじる時なんかは\x01",
            "けっこう神経を使うぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A3")

    Jump("loc_21EA")

    label("loc_20A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217C")

    #C0087
    ChrTalk(
        0x8,
        (
            "武器の改造を頼みてえ時は\x01",
            "気軽に声を掛けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "前にも言ったが、これでも昔は\x01",
            "エプスタイン財団で材料工学を\x01",
            "専門にしていた事もあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        "腕は信用してもらって構わねえぜ？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21EA")

    label("loc_217C")


    #C0090
    ChrTalk(
        0x8,
        (
            "武器の改造を頼みてえ時は\x01",
            "気軽に声を掛けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "こんなナリだが、\x01",
            "腕は信用してもらって構わねえぜ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EA")

    Return()

    # Function_6_851 end

    def Function_7_21EB(): pass

    label("Function_7_21EB")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x104, 0)
    Sleep(1000)

    #C0092
    ChrTalk(
        0x8,
        "おう、そういやランディ。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "頼まれてたブレードライフルの\x01",
            "修理の件なんだがよ……\x01",
            "もう少し待っちゃくれねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#00305Fもちろん構わねえが……\x02\x03",

            "#00301F何か問題でもあったかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "問題っつうか、ありゃあ\x01",
            "ほぼオリジナルパーツだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "パーツの代替も利かねえし、\x01",
            "再現しようとすると、どうしても\x01",
            "時間がかかっちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "ま、お前の従妹が使ってたとかいう\x01",
            "チェーンソーライフルなんてモンよりは\x01",
            "まだ何とかなりそうだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#00306F《テスタ＝ロッサ》か……\x01",
            "ありゃ、とんでもねぇ代物だからな。\x02\x03",

            "#00301Fまさか小娘ごときに使いこなせるとは\x01",
            "思ってもみなかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "『赤い頭#6Rテスタ＝ロッサ#』……\x01",
            "帝国あたりの昔話に出てくる\x01",
            "千の武器を持つ魔人の名前だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "俺も、前に仕上げた武器に\x01",
            "同じ名前を付けた事があるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "どうやら完全に\x01",
            "位負けしちまってるようだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、気にすんなって。\x02\x03",

            "#00308Fいずれにしても、出所は\x01",
            "かなり特殊な武器工房でな……\x02\x03",

            "#00301Fしかも特注品だから\x01",
            "そりゃあ確かに大変だわな。\x02\x03",

            "#00306Fすまねぇ、オッサン。\x01",
            "手間をかけさせちまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "へっ、まあおかげで\x01",
            "勉強させてもらってら。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "改造武具に使えそうな技術も\x01",
            "色々発見できたしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "ま、流石にもう一週間は\x01",
            "かからねえと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#00300Fそうか、だが今は復興関係の\x01",
            "仕事もあって大忙しなんだろ？\x02\x03",

            "#00304F俺の方は焦んねえから、\x01",
            "あんまし急がなくていいぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "へっ、ガキがいっちょ前に\x01",
            "オッサンを気遣ってんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "とにかく、修理が終わったら\x01",
            "またこちらから連絡するからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        "それまで、せいぜい待っていやがれ。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x104,
        (
            "#00302Fはは……\x01",
            "助かるぜ、オッサン。\x02\x03",

            "そんじゃまあ、任せたぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x18D, 5)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_7_21EB end

    def Function_8_27E6(): pass

    label("Function_8_27E6")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 0)

    #C0111
    ChrTalk(
        0x8,
        (
            "おう、ランディじゃねえか。\x01",
            "ようやく支援課に復帰ってわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00300Fああ、おかげさんでな。\x02\x03",

            "#00304Fとりあえずまた機会があったら\x01",
            "武器の強化でも頼むぜ、オッサン。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "おうよ、素材さえありゃあ\x01",
            "いつでも引き受けてやらあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "ま、お前さんも\x01",
            "せいぜい飛ばし過ぎんなよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x14D, 2)
    Return()

    # Function_8_27E6 end

    def Function_9_2921(): pass

    label("Function_9_2921")

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
            "#11Pしかし、とんでもないことに\x01",
            "なっちまったもんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#11P俺も、おまえたちになにか\x01",
            "手伝いをしてやりてえが……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        "#11P……『あれ』さえあればなあ。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#6P#00005F『あれ』……？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#11P『ゼムリアストーン』っつう、\x01",
            "古代文明の遺物なんて\x01",
            "言われてる金属があってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#11P以前、どっかの偉い学者さんが\x01",
            "ようやく加工法を発見した、\x01",
            "途轍もなく硬い代物なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#11Pそいつがあれば、俺が今設計している\x01",
            "ものすげえ武器を造ってやれるはずだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEF, 7)), scpexpr(EXPR_END)), "loc_2C42")

    #C0122
    ChrTalk(
        0x8,
        (
            "#11P以前、お前たちに造ってやった\x01",
            "武器よりもさらにすげえヤツをな。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#6P#00105F以前よりもさらに……！？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        "#6P#00300Fそいつはすげえな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C86")

    label("loc_2C42")


    #C0125
    ChrTalk(
        0x104,
        "#6P#00305Fものすげえ武器……！？\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#6P#00105F本当ですか！？\x02",
    )

    CloseMessageWindow()

    label("loc_2C86")


    #C0127
    ChrTalk(
        0x103,
        (
            "#12P#00202Fこんな状況ですし、強い武器は\x01",
            "喉から手が出るほど欲しいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#11Pああ、材料さえあれば\x01",
            "すぐにでも作ってやれるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#11Pそうだな、小さな欠片でも\x01",
            "５つくらいありゃあ、武器を造るには\x01",
            "十分な量になるはずなんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_2ECE")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x394, 0x0)"), scpexpr(EXPR_END)), "loc_2E31")

    #C0130
    ChrTalk(
        0x101,
        (
            "#6P#00000F（ゼムリアストーン……\x01",
            "  ちょうど占い師さんに\x01",
            "  もらったところだったな。）\x02\x03",

            "#00003F（それに欠片か……\x01",
            "  ちょうどそんなものを\x01",
            "  持っていたような。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC9")

    label("loc_2E31")


    #C0131
    ChrTalk(
        0x101,
        (
            "#6P#00000F（ゼムリアストーン……\x01",
            "  ちょうど占い師さんに\x01",
            "  もらったところだったな。）\x02\x03",

            "#00003F（それに欠片か……\x01",
            "  探してみてもいいかもしれない。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC9")

    Jump("loc_2F17")

    label("loc_2ECE")


    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#00003F（欠片か……そういえば、\x01",
            "  そんなものを持っていたような。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F17")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x8,
        (
            "#11Pおおっ、\x01",
            "もしかして心あたりがあんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#11Pよっしゃ、そんじゃあ俺は\x01",
            "武器を造る準備をしておくぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#11P『ゼムリアストーン』か\x01",
            "その『欠片』を５つ手に入れたら、\x01",
            "改めて俺に話しかけな。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        "#11Pすぐにでも武器を造ってやるからよ。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#6P#00000Fええ、分かりました。\x02",
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

    # Function_9_2921 end

    def Function_10_3082(): pass

    label("Function_10_3082")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3323")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_31D9")

    #C0138
    ChrTalk(
        0x8,
        (
            "#11Pそいつはゼムリアストーン……！\x01",
            "ハハ、手に入れてきやがったか！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#11Pそいつを使えば、\x01",
            "１人分の武器を造ってやれるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3255")

    label("loc_31D9")


    #C0140
    ChrTalk(
        0x8,
        (
            "#11Pおお、ゼムリアストーンの欠片……\x01",
            "５つ集まったみてえだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#11Pそいつを使えば、\x01",
            "１人分の武器を造ってやれるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3255")


    #C0142
    ChrTalk(
        0x8,
        (
            "#11Pいつでも作成に取り掛かれるが……\x01",
            "……どうだ、試してみるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#6P#00000Fええ、是非よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        "#11Pへへっ、よしきた！\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#11Pどの武器を造るか、\x01",
            "よく考えて選んでくんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_334F")

    label("loc_3323")


    #C0146
    ChrTalk(
        0x8,
        "#11Pおっ、造りたい武器が決まったのか？\x02",
    )

    CloseMessageWindow()

    label("loc_334F")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "インフィニティ　　　（ロイド）\x01",        # 0
            "エクスシアレイ　　　（エリィ）\x01",        # 1
            "コスモコラプサー　　（ティオ）\x01",        # 2
            "ディノティックアビス（ランディ）\x01",      # 3
            "アークソレイユ　　　（ノエル）\x01",        # 4
            "セブンスアーム　　　（ワジ）\x01",          # 5
            "曳影之剣　　　　　　（リーシャ）\x01",      # 6
            "ヒンメルトロア　　　（ダドリー）\x01",      # 7
            "やめる\x01",                                # 8
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AD1")

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそれでは、この武器を\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x396, 0x0)"), scpexpr(EXPR_END)), "loc_3518")
    SubItemNumber(0x396, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_3566")

    label("loc_3518")

    SubItemNumber(0x394, 5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0149
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を５個渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_3566")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0150
    ChrTalk(
        0x8,
        (
            "#11Pよっしゃ、そんじゃあ一丁\x01",
            "腕を振るってやろうじゃねえか！\x02",
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
            "#11P……よ～し、できたぜ。\x01",
            "受け取ってくんな！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3681")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3681")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E2")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0153
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x409),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x409, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_36E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3743")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0154
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x41D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37A4")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x431),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x431, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_37A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3805")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0156
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x459),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x459, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3805")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3866")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0157
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x445),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x445, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_3866")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C7")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0158
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x464),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x464, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3923")

    label("loc_38C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3923")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0159
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x469),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x469, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A39")

    #C0160
    ChrTalk(
        0x101,
        (
            "#6P#00000Fありがとうございます、ギヨーム親方。\x01",
            "必ず有効に使わせてもらいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#11Pヘヘっ、いいってことよ。\x01",
            "こんな素材が扱えるなんて\x01",
            "俺も技師冥利に尽きるってモンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "#11Pこいつを使って、クロスベルの事件を\x01",
            "しっかり解決に導いてやってくれや！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E0(0x14, 0x0)
    SetScenarioFlags(0x18B, 1)
    Jump("loc_3AC9")

    label("loc_3A39")


    #C0163
    ChrTalk(
        0x8,
        (
            "#11Pこんな時だからこそ\x01",
            "こいつも役に立つはずだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        "#11Pつうわけで、しっかりやれよ！\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        "#6P#00000Fはい、大切に使わせていただきます。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3AC9")

    ClearScenarioFlags(0x0, 3)
    Jump("loc_3B39")

    label("loc_3AD1")


    #C0166
    ChrTalk(
        0x8,
        "#11Pそうか？　まあ迷うのも仕方ねえ。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "#11P造りたい武器が決まったら\x01",
            "もう一度声をかけてくれや。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_3B39")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 380, 0, 3940, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_10_3082 end

    def Function_11_3B69(): pass

    label("Function_11_3B69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA2")
    Call(0, 17)
    Return()

    label("loc_3BA2")

    Call(0, 19)
    Return()

    label("loc_3BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC8")
    Call(0, 23)
    Return()

    label("loc_3BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FE8")
    SetScenarioFlags(0x191, 5)
    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0x105,
        (
            "#10300Fそれで、アッバスはここで\x01",
            "何の手伝いをしているんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "#04100Fああ、今は出来る範囲で\x01",
            "建材の修理と加工を\x01",
            "手伝わせてもらっている。\x02\x03",

            "#04102F意外と細かい作業も多いが、\x01",
            "なかなかに楽しいぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#00005F楽しい、か……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00100F確か、アッバスさんは\x01",
            "トリニティで料理も\x01",
            "されていましたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "#04100Fああ、以前にな。\x02\x03",

            "最近はリャンとアゼルに\x01",
            "任せきりだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、アッバスはこう見えて\x01",
            "手先が器用だからね。\x02\x03",

            "#10304F料理や工作はもちろん、\x01",
            "裁縫だってお手の物なのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00305Fへえ、そいつはまた\x01",
            "新たな一面って感じだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        (
            "#00200Fなんていうか……\x01",
            "良い主夫になれそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x109,
        (
            "#10106Fう～ん、ですがまだまだ\x01",
            "他にも隠されていそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、言っておくけど\x01",
            "アッバスは僕だけの\x01",
            "ものだからね㈱\x02\x03",

            "#10304Fま、レンタルくらいなら\x01",
            "考えてあげてもいいけど。\x02",
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
            "#04100F……いったい何の話をしている。\x02\x03",

            "とにかく、俺はしばらく\x01",
            "ここでギヨーム親方の手伝いを\x01",
            "させてもらう予定だ。\x02\x03",

            "何かあれば、いつでも来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#00002Fあ、ああ……\x02\x03",

            "#00003F（アッバスか……\x01",
            "  ほんと謎の多い人だよな。）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_4055")

    label("loc_3FE8")

    TalkBegin(0xFE)

    #C0180
    ChrTalk(
        0xA,
        (
            "#04100F俺はしばらくここで\x01",
            "ギヨーム親方の手伝いを\x01",
            "させてもらう予定だ。\x02\x03",

            "何かあれば、いつでも来い。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_4055")

    Return()

    # Function_11_3B69 end

    def Function_12_4056(): pass

    label("Function_12_4056")

    TalkBegin(0xFE)
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    # Function_12_4056 end

    def Function_13_4060(): pass

    label("Function_13_4060")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4356")

    #C0181
    ChrTalk(
        0x9,
        (
            "それで、これが\x01",
            "今ティオ君の使っている\x01",
            "魔導杖の設計図なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "おお、こいつはまた高出力が\x01",
            "期待できそうな造りだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "おし、嬢ちゃんが帰ったら\x01",
            "利用できるようにしとくぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        "いやあ、本当に助かるよ～。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "これでティオ君が戻った後も\x01",
            "滞りなく魔導杖を使ってもらえそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "そういや嬢ちゃん、なにやら帰りが\x01",
            "長引いちまってるんだってな？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "ああっ、そうなんだよ～！\x01",
            "色々仕事が増えちゃったみたいでさ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        (
            "最近は一時間おきに通信をかけても\x01",
            "めったに応答してくれないから、\x01",
            "心配でならないんだよ～！\x02",
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
        "……そりゃ、構いすぎが原因だな。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        "#00012F（ロバーツ主任、相変わらずだなあ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_4435")

    label("loc_4356")


    #C0191
    ChrTalk(
        0x9,
        (
            "ティオ君、ごはんは\x01",
            "ちゃんと食べてるのかな？\x01",
            "無理なんかして体を壊したりは……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "ああっ、また心配になってきたよ～！\x01",
            "財団に帰ったらまた通信してみないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        (
            "#00106F（う、う～ん……\x01",
            "  さすがに過保護すぎるわよね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4435")

    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_13_4060 end

    def Function_14_443E(): pass

    label("Function_14_443E")

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
            "#11Pおう、お前らか。\x01",
            "こりゃまた久しぶりだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2990, 1300, 3770, 2000)
    MoveCamera(49, 15, 0, 2000)
    OP_6E(440, 2000)
    SetCameraDistance(19900, 2000)

    def lambda_4541():
        OP_96(0xFE, 0xBB8, 0x0, 0xEBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4541)
    Sleep(400)

    def lambda_455E():
        OP_96(0xFE, 0x6A4, 0x0, 0xDF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_455E)
    Sleep(400)

    def lambda_457B():
        OP_96(0xFE, 0xCE4, 0x0, 0xAD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_457B)
    Sleep(400)

    def lambda_4598():
        OP_96(0xFE, 0x7D0, 0x0, 0x8DE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4598)
    WaitChrThread(0x101, 1)

    def lambda_45B6():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45B6)
    WaitChrThread(0x102, 1)

    def lambda_45C7():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_45C7)
    WaitChrThread(0x109, 1)

    def lambda_45D8():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45D8)
    WaitChrThread(0x105, 1)

    def lambda_45E9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_45E9)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0195
    ChrTalk(
        0x101,
        "#6P#00000Fこんにちは、親方さん。\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x102,
        "#6P#00100Fご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "#11Pはは、まあそんなに\x01",
            "かしこまることはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "#11Pだが噂にゃ聞いていたが、\x01",
            "テスタメンツのリーダーが\x01",
            "特務支援課にお仲間入りとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        "#11Pまったく、ぶったまげたぜ。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、それはどうも。\x02\x03",

            "#10302Fちなみに前は断られたけど、\x01",
            "今後は僕の得物の改造も\x01",
            "引き受けてくれるんだよね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4771():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4771)

    def lambda_477E():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_477E)
    TurnDirection(0x102, 0x105, 500)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x101,
        "#00006Fワジ、ちゃっかりそんなことを……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        "#11Pはは、まあそうだな。\x02",
    )

    CloseMessageWindow()

    def lambda_4810():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4810)

    def lambda_481D():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_481D)
    TurnDirection(0x102, 0x8, 500)

    #C0203
    ChrTalk(
        0x8,
        (
            "#11Pケンカに使うってんじゃなきゃ\x01",
            "頼まれてやってもいいぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x109,
        (
            "#12P#10100F修理屋《ギヨーム工房》。\x02\x03",

            "#10104F導力製品の修理だけでなく、\x01",
            "武器の改造なども\x01",
            "請け負っているそうですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x109, 500)

    #C0205
    ChrTalk(
        0x8,
        "#5Pお、嬢ちゃんも新顔だな。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "#5Pまあ、改造っつっても\x01",
            "せいぜい危険のない範囲で\x01",
            "強化する程度のモンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x8,
        (
            "#5P一応最近は営業許可も取ったし、\x01",
            "法に触れるような真似もしちゃいねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x8,
        (
            "#5Pま、何か良い素材が手に入ったら\x01",
            "気軽に頼んでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        "#10100F#12Pは、はい、分かりました。\x02",
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
            "※《ギヨーム工房》では、\x01\x07\x02",

            "　Ｕマテリアル\x07\x05",
            "などの素材アイテムを利用して\x01",
            "　通常より効果の高い装備品が入手できます。\x02\x03",

            "※カウンターにいるギヨームに話しかけて\x01",
            "　『改造を頼む』を選択すると、\x01",
            "　メニューが表示され、改造を行えます。\x07\x00\x02",
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

    # Function_14_443E end

    def Function_15_4B57(): pass

    label("Function_15_4B57")

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
        "#11Pおう、お前ら！\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#11Pランディのヤツ、\x01",
            "一体どうしやがったんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "#11Pなんか尋常じゃねぇモンの\x01",
            "整備を頼まれたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#6P#00006Fやっぱりそうですか……\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        "#6P#00101F今朝のことですよね？\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "#11Pああ、５時くらいに\x01",
            "いきなり店を訪ねてきてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "#11Pちょうど徹夜明けだったから\x01",
            "勢いで引き受けちまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        (
            "#6P#00201Fそれで……\x01",
            "『尋常じゃないモノ』とは？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x109,
        (
            "#6P#10101Fやっぱり……\x01",
            "重火器の類いでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "#11Pああ……と言っても、\x01",
            "バラしたユニットだけだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x8,
        (
            "#11Pしばらく使ってなかった\x01",
            "機関部や排気ユニットやらを\x01",
            "一通り整備してやったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "#11Pありゃあ、組み立てたら\x01",
            "とんでもねぇ化物になると思うぜ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_4EE3")

    #C0223
    ChrTalk(
        0x105,
        (
            "#10308Fランディが使ってたっていう\x01",
            "導力ライフルに間違いなさそうだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F2B")

    label("loc_4EE3")


    #C0224
    ChrTalk(
        0x105,
        (
            "#10308F察するに、ランディが使ってた\x01",
            "特注の導力ライフルあたりかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F2B")


    #C0225
    ChrTalk(
        0x101,
        (
            "#6P#00006Fああ……\x01",
            "間違いないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#6P#00101Fギヨームさん。\x01",
            "情報ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        "#11Pああ、いいってことよ。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#11P事情は知らんが……\x01",
            "ずいぶんと思いつめた顔を\x01",
            "してやがった。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "#11P仲間のお前たちが\x01",
            "出来るかぎり力になってやんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        "#6P#00000Fはい！\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        "#6P#10100F了解です！\x02",
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

    # Function_15_4B57 end

    def Function_16_5094(): pass

    label("Function_16_5094")

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
            "#00000Fえっと、ギヨーム親方……\x01",
            "金属探知機のようなものを\x01",
            "もってませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        "金属探知機だあ……？\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x8,
        (
            "以前確かにそんなものを\x01",
            "作った覚えはあるが。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x104,
        (
            "#00309Fお、ビンゴだな。\x01",
            "さすがオーブメント技師だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "ま、ほとんど遊び半分で\x01",
            "作ったもんだんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        "しかし、ンなもん何に使うんだ？\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        "#00000Fええ、それが……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カノンの手伝いで\x01",
            "廃材回収を行うことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0240
    ChrTalk(
        0x8,
        (
            "なるほど……\x01",
            "そりゃ確かに必要そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "分かった、お前らに\x01",
            "あれを貸してやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "待ってな、確か奥のほうに\x01",
            "しまってたはずだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5365():

        label("loc_5365")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5365")

    QueueWorkItem2(0x109, 0, lambda_5365)

    def lambda_5377():

        label("loc_5377")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5377")

    QueueWorkItem2(0x102, 0, lambda_5377)

    def lambda_5389():

        label("loc_5389")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5389")

    QueueWorkItem2(0x104, 0, lambda_5389)

    def lambda_539B():

        label("loc_539B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_539B")

    QueueWorkItem2(0x101, 0, lambda_539B)

    def lambda_53AD():

        label("loc_53AD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53AD")

    QueueWorkItem2(0x105, 0, lambda_53AD)

    def lambda_53BF():

        label("loc_53BF")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_53BF")

    QueueWorkItem2(0x103, 0, lambda_53BF)
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
            "あったあった。\x01",
            "ほれ、受け取りな。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x375),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x375, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0245
    ChrTalk(
        0x103,
        (
            "#00205F意外と本格的な作りですね。\x02\x03",

            "#00203F警察で使われてるものにも\x01",
            "匹敵するかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#00105Fそ、それって結構\x01",
            "すごいわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "がはは、まあ見た目くらいは\x01",
            "しっかり整えるさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        (
            "実際、導力の燃費も悪いし\x01",
            "あんまり自慢できた\x01",
            "モンじゃねえんだがよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        "そんで、使い方は分かるか？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x109,
        (
            "#10103F出入国検査で何度か\x01",
            "使ったことがあります。\x02\x03",

            "#10102F金属がありそうな場所で\x01",
            "起動するといいんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        "だいたいそんなとこだな。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "反応のありそうなところを\x01",
            "念入りに調べれば\x01",
            "金属が見つかるはずだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "あと、運が良けりゃあ\x01",
            "他のモンも見つかるかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#00004Fなるほど……\x01",
            "分かりました。\x02\x03",

            "#00000Fそれじゃ、借りていきますね。\x02",
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
            "※金属探知機は、旧市街の\x01",
            "  屋外マップでのみ使用可能です。\x01",
            "  『△ボタン＋Ｌボタン』で使用します。\x02\x03",

            "※また、キャンプメニューの\x01",
            "  [ITEMS]から使用することもできます。\x07\x00\x02",
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

    # Function_16_5094 end

    def Function_17_5822(): pass

    label("Function_17_5822")

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
        "#10300Fフフ、やってるね。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xA,
        (
            "#04100Fワジ……\x01",
            "それに支援課の面々か。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        "よお、依頼を見てくれたんだな？\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x101,
        (
            "#00000Fええ、とりあえず\x01",
            "状況を伺おうと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#00103F外の様子を見る限り、\x01",
            "復興はまだまだこれからという\x01",
            "印象ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xA,
        (
            "#04100Fああ、その通りだ。\x02\x03",

            "テスタメンツが先導し、\x01",
            "旧市街の住民総出で\x01",
            "作業に当たっているが……\x02\x03",

            "いまだ襲撃の傷跡は大きく、\x01",
            "進捗も芳しくない状況でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x104,
        (
            "#00303Fそういや、旧市街は\x01",
            "魔人化したヴァルドが\x01",
            "襲撃したんだったよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x109,
        (
            "#10101F住民の皆さんは\x01",
            "そのことをご存知なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xA,
        (
            "#04100Fいや……バイパー以外に\x01",
            "気付いている者など\x01",
            "ほとんどいないだろう。\x02\x03",

            "なにせ、あのような\x01",
            "異形の姿で現れたのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#00203Fショックが大きいでしょうし……\x01",
            "公言しないほうが無難でしょうね。\x02",
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
            "#04100F……ひとまず、\x01",
            "その話は捨て置こう。\x02\x03",

            "今重要なのは、復興作業を\x01",
            "如何にして進めていくかだ。\x02\x03",

            "この旧市街においては、\x01",
            "行政の協力を期待できない上に\x01",
            "業者などを雇う資金もない。\x02\x03",

            "できれば、特務支援課の力を\x01",
            "貸してもらえると助かるのだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x101,
        "#00003Fそうだな……\x02",
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_17_5822 end

    def Function_18_5CEB(): pass

    label("Function_18_5CEB")

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
            "旧市街の復興を手伝う\x01",      # 0
            "いったん考える\x01",            # 1
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
        (0, "loc_5D5F"),
        (1, "loc_5D6F"),
        (SWITCH_DEFAULT, "loc_5EE9"),
    )


    label("loc_5D5F")

    OP_29(0x8E, 0x4, 0x2)
    SetScenarioFlags(0x196, 0)
    Call(0, 20)
    Jump("loc_5EE9")

    label("loc_5D6F")


    #C0269
    ChrTalk(
        0x101,
        (
            "#00006Fできれば協力したいんだが……\x01",
            "他の仕事次第って所もあるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x105,
        (
            "#10300Fちなみに、あとで改めて\x01",
            "引き受けることもできるのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xA,
        (
            "#04100Fああ、協力してもらえるなら\x01",
            "タイミングはいつでも構わない。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "ま、無理にとは言わねえ。\x01",
            "手が空いたら助けてくれるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        (
            "#00000F分かりました、\x01",
            "なるべく善処はしてみます。\x02",
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
    Jump("loc_5EE9")

    label("loc_5EE9")

    Return()

    # Function_18_5CEB end

    def Function_19_5EEA(): pass

    label("Function_19_5EEA")

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
            "#04100Fふむ、旧市街の復興作業を\x01",
            "手伝ってくれるのか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Return()

    # Function_19_5EEA end

    def Function_20_5FEE(): pass

    label("Function_20_5FEE")


    #C0275
    ChrTalk(
        0x101,
        "#00000Fああ、任せてくれ。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xA,
        "#04100Fふむ、ありがたい。\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x8,
        (
            "へへっ、お前たちなら\x01",
            "そう言ってくれると思ってたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        (
            "#10300Fそれで、僕たちは\x01",
            "何を手伝えばいいんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xA,
        (
            "#04100Fああ、今は主に３つの場所で\x01",
            "作業を行っていてな。\x02\x03",

            "１つは《ロータスハイツ》で\x01",
            "行われている炊き出し。\x02\x03",

            "１つはメゾン・イメルダ跡で\x01",
            "行われている廃材回収作業。\x02\x03",

            "最後はこの場所――\x01",
            "《ギヨーム工房》での\x01",
            "建材の収集、加工作業だ。\x02\x03",

            "支援課には各場所に赴き、\x01",
            "それぞれが必要としている\x01",
            "手伝いを行ってもらいたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#00103Fなるほど……\x01",
            "どれも重要そうな作業ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x109,
        (
            "#10105Fちなみに、こちらで\x01",
            "行っている作業というのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "ああ、ここでは壊れた建物を\x01",
            "直すための建材を見繕ってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "一応、工房で余った\x01",
            "素材なんかも使えそうなんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        "さっき、重大な問題に気付いてな。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x103,
        "#00205F問題？　それはどういう……\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "ズバリ、建材を組むための\x01",
            "ネジやら釘やらが足りねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "このままじゃ、修繕すら\x01",
            "ままならねえ状況ってこった。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x104,
        (
            "#00305F外に色々散らばってるが……\x01",
            "落ちてる廃品なんかは\x01",
            "利用できたりしねえのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xA,
        (
            "#04100Fふむ、一応カノンという子供に\x01",
            "頼んではいるのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "ま、あれはどちらかというと\x01",
            "資金調達のために\x01",
            "やってもらってる事でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x8,
        (
            "それに強度の問題もあって、\x01",
            "なるべく新品を使いてえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x105,
        (
            "#10306Fやれやれ、難儀なことだね。\x02\x03",

            "#10300Fそれじゃあ、どこかから\x01",
            "ネジや釘を仕入れてこいって\x01",
            "ことなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "いや、それより断然に\x01",
            "いいものがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x8,
        (
            "武具の改造などに使ってる\x01",
            "“Ｕマテリアル”を使うんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x8,
        (
            "あの素材があれば、\x01",
            "その辺のものは作れちまうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#00203F“Ｕマテリアル”ですか……\x01",
            "あれも調達が大変そうですが。\x02\x03",

            "#00200Fいくつくらい必要なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "そうさな……\x01",
            "１０個もありゃ釣りが来るだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        "どうだ、調達を頼めるか？\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#00000F分かりました。\x01",
            "集められたら持ってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xA,
        "#04100F頼んだぞ、特務支援課。\x02",
    )

    CloseMessageWindow()
    Sleep(50)

    def lambda_66BE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_66BE)
    Sleep(250)

    def lambda_66CE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_66CE)
    Sleep(50)

    def lambda_66DE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_66DE)
    Sleep(50)

    def lambda_66EE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_66EE)
    Sleep(50)

    def lambda_66FE():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_66FE)
    Sleep(500)

    #C0301
    ChrTalk(
        0x101,
        (
            "#00004Fさて、それじゃさっそく\x01",
            "手伝いを始めるとするか。\x02\x03",

            "#00000F炊き出しと廃材回収の方にも\x01",
            "話を聞きに行こう。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x105,
        (
            "#10300F了解、リーダー。\x02\x03",

            "古巣が大変な時だ、\x01",
            "一肌脱がせてもらうよ。\x02",
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
            "クエスト【旧市街の復興支援】\x07\x00",
            "を開始した！\x02",
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

    # Function_20_5FEE end

    def Function_21_686E(): pass

    label("Function_21_686E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x38E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6910")

    #C0304
    ChrTalk(
        0x8,
        "Ｕマテリアルを譲ってくれるのか？\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "……って、\x01",
            "数が足りてねえじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "こっちが必要な数は１０個だ。\x01",
            "どうかよろしく頼んだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A5B")

    label("loc_6910")


    #C0307
    ChrTalk(
        0x8,
        (
            "おっ……\x01",
            "どうやら集まったみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x8,
        (
            "Ｕマテリアル計１０個、\x01",
            "こっちに譲ってくれんのか？\x02",
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
            "渡す\x01",          # 0
            "渡さない\x01",      # 1
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
        (0, "loc_69D0"),
        (1, "loc_69D8"),
        (SWITCH_DEFAULT, "loc_6A5B"),
    )


    label("loc_69D0")

    Call(0, 22)
    Jump("loc_6A5B")

    label("loc_69D8")


    #C0309
    ChrTalk(
        0x8,
        (
            "そうか、まあ仕方ねえか。\x01",
            "お前たちにも必要なものだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "ま、もしも余裕があるってんなら\x01",
            "譲ってくれると助かるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A5B")

    label("loc_6A5B")

    Return()

    # Function_21_686E end

    def Function_22_6A5C(): pass

    label("Function_22_6A5C")

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
        "#00000Fそれじゃ、お渡ししますね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0312
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "１０個を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x38E, 10)

    #C0313
    ChrTalk(
        0x8,
        (
            "へへっ、ありがてえ。\x01",
            "遠慮なくいただくぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "これで修繕の目処は\x01",
            "ついたも同然だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#00102Fふふ、お役に立てて嬉しいです。\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#00300F修繕工事をやるってんなら\x01",
            "手伝ってもいいぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x109,
        (
            "#10109Fそうそう、\x01",
            "力仕事なら自信がありますし！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "いや、流石に\x01",
            "そこまでは頼まねえよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "旧市街は旧市街の住民で\x01",
            "キッチリ直すとするさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x105,
        (
            "#10303Fアッバスとテスタメンツが\x01",
            "先導するだろうしね。\x02\x03",

            "#10309Fま、がんばってよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x103,
        "#00206F他人事みたいに言いますね……\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xA,
        (
            "#04102Fフフ、いいのだ。\x01",
            "我々とワジでは既に\x01",
            "役割が違うからな。\x02\x03",

            "#04100F……改めて礼を言うぞ、\x01",
            "特務支援課。\x02\x03",

            "まだ手が空いていたら\x01",
            "他の場所も手伝ってやってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x198, 2)
    OP_29(0x8E, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F2B")

    #C0323
    ChrTalk(
        0x101,
        (
            "#00000Fああ、任せてくれ。\x02\x03",

            "#00005Fって、主だった場所は\x01",
            "ほとんど手伝い終わったな……\x02\x03",

            "#00000Fあとは旧市街を回りつつ\x01",
            "細かい手伝いでもしているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xA,
        (
            "#04100Fそうしてもらえると助かる。\x01",
            "……ではまた後でな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c140D", 100, 0, 0)
    IdleLoop()
    Jump("loc_6F52")

    label("loc_6F2B")


    #C0325
    ChrTalk(
        0x101,
        "#00000Fああ、そうさせてもらうよ。\x02",
    )

    CloseMessageWindow()

    label("loc_6F52")

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

    # Function_22_6A5C end

    def Function_23_6FAF(): pass

    label("Function_23_6FAF")

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
        "#04100Fどうした……？\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x8,
        (
            "もしかして、\x01",
            "手伝いが済んじまったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x101,
        "#00000Fええ、主だった所は一通り。\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xA,
        (
            "#04100Fそうか……\x01",
            "ご苦労だったな。\x02\x03",

            "炊き出しまで時間がある。\x01",
            "それまで時間を潰しておくといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#00100Fだったら、しばらく\x01",
            "旧市街を回ってましょうか。\x02\x03",

            "#00104Fまだ細かい手伝いが\x01",
            "残ってるかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xA,
        (
            "#04100Fそうしてもらえると助かる。\x01",
            "……ではまた後でな。\x02",
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

    # Function_23_6FAF end

    SaveToFile()

Try(main)
