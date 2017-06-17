from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0000_1.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [100, 0, 0, 0, 83952996, 83952897, 5, 1, 1380, 1281, 1281, 1281, 84215045, 5, 83887460, 1280, 512, 5, 0, 2, 0, 0, 0],
    )

    BuildStringList((
        "r0000_1",                # 0
    ))

    ChipFrameInfo(356, 0)                                        # 0

    ScpFunction((
        "Function_0_164",          # 00, 0
        "Function_1_1FA",          # 01, 1
        "Function_2_24C",          # 02, 2
        "Function_3_D36",          # 03, 3
        "Function_4_14D3",         # 04, 4
        "Function_5_18D4",         # 05, 5
        "Function_6_1C2D",         # 06, 6
        "Function_7_1C6E",         # 07, 7
    ))


    def Function_0_164(): pass

    label("Function_0_164")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "何かを見つけた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF")
    Call(1, 5)
    Jump("loc_1F9")

    label("loc_1AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7")
    Call(1, 4)
    Jump("loc_1F9")

    label("loc_1D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3D, 5)), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F6")
    Call(1, 3)
    Jump("loc_1F9")

    label("loc_1F6")

    Call(1, 2)

    label("loc_1F9")

    Return()

    # Function_0_164 end

    def Function_1_1FA(): pass

    label("Function_1_1FA")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_224")
    Call(1, 5)
    Jump("loc_24B")

    label("loc_224")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_248")
    Call(1, 4)
    Jump("loc_24B")

    label("loc_248")

    Call(1, 3)

    label("loc_24B")

    Return()

    # Function_1_1FA end

    def Function_2_24C(): pass

    label("Function_2_24C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60A")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_2AB"),
        (1, "loc_2F9"),
        (2, "loc_347"),
        (3, "loc_395"),
        (4, "loc_3E3"),
        (5, "loc_431"),
        (6, "loc_47F"),
        (7, "loc_4CD"),
        (8, "loc_51B"),
        (9, "loc_569"),
        (SWITCH_DEFAULT, "loc_5B7"),
    )


    label("loc_2AB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x200),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x200, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_2F9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x201),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x201, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_347")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x202),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x202, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_395")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x203),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x203, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_3E3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x204),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x204, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_431")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x205),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x205, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_47F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x206),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x206, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_4CD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x207),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x207, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_51B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x208),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x208, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_569")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x209),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x209, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_5B7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_605")

    label("loc_605")

    Jump("loc_D35")

    label("loc_60A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_6DA"),
        (18, "loc_6DA"),
        (25, "loc_6DA"),
        (1, "loc_738"),
        (19, "loc_738"),
        (26, "loc_738"),
        (2, "loc_796"),
        (20, "loc_796"),
        (27, "loc_796"),
        (3, "loc_7F4"),
        (21, "loc_7F4"),
        (28, "loc_7F4"),
        (4, "loc_852"),
        (22, "loc_852"),
        (29, "loc_852"),
        (5, "loc_8B0"),
        (23, "loc_8B0"),
        (30, "loc_8B0"),
        (6, "loc_90E"),
        (24, "loc_90E"),
        (31, "loc_90E"),
        (7, "loc_96C"),
        (8, "loc_9BD"),
        (9, "loc_A0E"),
        (10, "loc_A5F"),
        (11, "loc_AB0"),
        (12, "loc_B01"),
        (13, "loc_B52"),
        (14, "loc_BA3"),
        (15, "loc_BF4"),
        (16, "loc_C45"),
        (17, "loc_C96"),
        (SWITCH_DEFAULT, "loc_CE7"),
    )


    label("loc_6DA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x0, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_738")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#57I水のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x1, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_796")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#58I火のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x2, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_7F4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#59I風のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x3, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_852")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x4, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_8B0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#61I空のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x5, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_90E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#62I幻のセピス\x07\x00",
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddSepith(0x6, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_96C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x186),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x186, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_9BD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x187, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_A0E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x188),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x188, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_A5F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_AB0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0024
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12C, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_B01")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12D, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_B52")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12E, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_BA3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0027
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12F, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_BF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x130),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x130, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_C45")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x131),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x131, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_C96")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x132),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x132, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_CE7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_D35")

    label("loc_D35")

    Return()

    # Function_2_24C end

    def Function_3_D36(): pass

    label("Function_3_D36")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_DD0"),
        (1, "loc_E1E"),
        (2, "loc_E6C"),
        (3, "loc_EBA"),
        (4, "loc_F08"),
        (5, "loc_F56"),
        (6, "loc_FA4"),
        (7, "loc_FF2"),
        (8, "loc_1040"),
        (9, "loc_108E"),
        (10, "loc_10DC"),
        (11, "loc_112A"),
        (12, "loc_1178"),
        (13, "loc_11C6"),
        (14, "loc_1214"),
        (15, "loc_1262"),
        (16, "loc_12B0"),
        (17, "loc_12FE"),
        (18, "loc_134C"),
        (19, "loc_139A"),
        (20, "loc_13E8"),
        (21, "loc_1436"),
        (22, "loc_1484"),
        (SWITCH_DEFAULT, "loc_14D2"),
    )


    label("loc_DD0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x64, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_E1E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x68),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x68, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_E6C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_EBA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x70),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x70, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_F08")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x74),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x74, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_F56")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x78),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x78, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_FA4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0038
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_FF2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x80),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x80, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1040")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x84),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x84, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_108E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x88),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x88, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_10DC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0042
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x8C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_112A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x92, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1178")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_11C6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1214")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1262")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3F, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_12B0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x40),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x40, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_12FE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0049
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x41, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_134C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x42, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_139A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x43),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x43, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_13E8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x44),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x44, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1436")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0053
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x45),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x45, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_1484")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x46),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x46, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_14D2")

    label("loc_14D2")

    Return()

    # Function_3_D36 end

    def Function_4_14D3(): pass

    label("Function_4_14D3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_152B"),
        (1, "loc_1579"),
        (2, "loc_15C7"),
        (3, "loc_1615"),
        (4, "loc_1663"),
        (5, "loc_16B1"),
        (6, "loc_16FF"),
        (7, "loc_174D"),
        (8, "loc_179B"),
        (9, "loc_17E9"),
        (10, "loc_1837"),
        (11, "loc_1885"),
        (SWITCH_DEFAULT, "loc_18D3"),
    )


    label("loc_152B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x65, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1579")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x69),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x69, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_15C7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1615")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0058
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x71),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x71, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1663")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0059
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x75),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x75, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_16B1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0060
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x79, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_16FF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_174D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0062
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x81, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_179B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0063
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x85, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_17E9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0064
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x89),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x89, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1837")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x8D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_1885")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x93),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x93, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_18D3")

    label("loc_18D3")

    Return()

    # Function_4_14D3 end

    def Function_5_18D4(): pass

    label("Function_5_18D4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1920"),
        (1, "loc_196E"),
        (2, "loc_19BC"),
        (3, "loc_1A0A"),
        (4, "loc_1A58"),
        (5, "loc_1AA6"),
        (6, "loc_1AF4"),
        (7, "loc_1B42"),
        (8, "loc_1B90"),
        (9, "loc_1BDE"),
        (SWITCH_DEFAULT, "loc_1C2C"),
    )


    label("loc_1920")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x66),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x66, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_196E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0068
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6A, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_19BC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0069
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1A0A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x72, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1A58")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x76, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1AA6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7A, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1AF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1B42")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x82, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1B90")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x8A, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1BDE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x94),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x94, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1C2C")

    label("loc_1C2C")

    Return()

    # Function_5_18D4 end

    def Function_6_1C2D(): pass

    label("Function_6_1C2D")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    TalkBegin(0xFF)
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "何かを見つけた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 7)
    TalkEnd(0xFF)
    ClearMapFlags(0x80)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1C2D end

    def Function_7_1C6E(): pass

    label("Function_7_1C6E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20E3")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1CD9"),
        (1, "loc_1D2A"),
        (2, "loc_1D7B"),
        (3, "loc_1DCC"),
        (4, "loc_1E1D"),
        (5, "loc_1E6E"),
        (6, "loc_1EBC"),
        (7, "loc_1F0A"),
        (8, "loc_1F58"),
        (9, "loc_1FA6"),
        (10, "loc_1FF4"),
        (11, "loc_2042"),
        (SWITCH_DEFAULT, "loc_2090"),
    )


    label("loc_1CD9")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0078
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x186),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x186, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1D2A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x187, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1D7B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x188),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x188, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1DCC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1E1D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x18A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18A, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1E6E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0083
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1EBC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12D, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1F0A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12E, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1F58")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0086
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12F, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1FA6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x130),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x130, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_1FF4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x131),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x131, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_2042")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0089
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x132),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x132, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_2090")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x12C, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_20DE")

    label("loc_20DE")

    Jump("loc_2915")

    label("loc_20E3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_217D"),
        (1, "loc_21CE"),
        (2, "loc_221F"),
        (3, "loc_2270"),
        (4, "loc_22C1"),
        (5, "loc_2312"),
        (6, "loc_2363"),
        (7, "loc_23B4"),
        (8, "loc_2405"),
        (9, "loc_2456"),
        (10, "loc_24A7"),
        (11, "loc_24F8"),
        (12, "loc_2549"),
        (13, "loc_259A"),
        (14, "loc_25EB"),
        (15, "loc_263C"),
        (16, "loc_268D"),
        (17, "loc_26DE"),
        (18, "loc_272F"),
        (19, "loc_2780"),
        (20, "loc_27D1"),
        (21, "loc_2822"),
        (22, "loc_2873"),
        (SWITCH_DEFAULT, "loc_28C4"),
    )


    label("loc_217D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0091
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x134),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x134, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_21CE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0092
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x135),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x135, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_221F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0093
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x136),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x136, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2270")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0094
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x137),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x137, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_22C1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x138),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x138, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2312")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0096
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x139),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x139, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2363")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13A, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_23B4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13B, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2405")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0099
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13C, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2456")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0100
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13D, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_24A7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0101
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を8個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13E, 8)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_24F8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0102
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x13F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を4個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x13F, 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2549")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x140),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を4個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x140, 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_259A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0104
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x141),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を4個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x141, 4)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_25EB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0105
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x142),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x142, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_263C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0106
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x143),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x143, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_268D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0107
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x144),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x144, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_26DE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0108
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x145),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x145, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_272F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0109
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x146),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x146, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2780")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x147),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を5個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x147, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_27D1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x148),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x148, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2822")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x149),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x149, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2873")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14A, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_28C4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0114
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を2個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14A, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_2915")

    label("loc_2915")

    Return()

    # Function_7_1C6E end

    SaveToFile()

Try(main)
