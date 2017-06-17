from ZeroScenarioHelper import *

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
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 94, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0000_1",                # 0
    ))

    ScpFunction((
        "Function_0_188",          # 00, 0
    ))


    def Function_0_188(): pass

    label("Function_0_188")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_628")
    ClearScenarioFlags(0x7B, 7)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3F), scpexpr(EXPR_AND), scpexpr(EXPR_END)),
        (0, "loc_226"),
        (1, "loc_274"),
        (2, "loc_2C2"),
        (3, "loc_310"),
        (4, "loc_35E"),
        (5, "loc_3AC"),
        (6, "loc_3FA"),
        (7, "loc_448"),
        (8, "loc_496"),
        (9, "loc_4E4"),
        (10, "loc_532"),
        (11, "loc_580"),
        (SWITCH_DEFAULT, "loc_5CE"),
    )


    label("loc_226")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0002
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
    Jump("loc_623")

    label("loc_274")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0003
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
    Jump("loc_623")

    label("loc_2C2")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0004
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
    Jump("loc_623")

    label("loc_310")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6F, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_623")

    label("loc_35E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0006
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
    Jump("loc_623")

    label("loc_3AC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0007
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
    Jump("loc_623")

    label("loc_3FA")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0008
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
    Jump("loc_623")

    label("loc_448")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7B, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_623")

    label("loc_496")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0010
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
    Jump("loc_623")

    label("loc_4E4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0011
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
    Jump("loc_623")

    label("loc_532")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0012
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
    Jump("loc_623")

    label("loc_580")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x87, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_623")

    label("loc_5CE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を10個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x7B, 7)
    Jump("loc_623")

    label("loc_623")

    Jump("loc_1B02")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF4")
    ClearScenarioFlags(0x7B, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_AND), scpexpr(EXPR_END)),
        (0, "loc_6BB"),
        (1, "loc_709"),
        (2, "loc_757"),
        (3, "loc_7A5"),
        (4, "loc_7F3"),
        (5, "loc_841"),
        (6, "loc_88F"),
        (7, "loc_8DD"),
        (8, "loc_92B"),
        (9, "loc_979"),
        (10, "loc_9C7"),
        (11, "loc_A15"),
        (12, "loc_A63"),
        (13, "loc_AB1"),
        (14, "loc_AFF"),
        (15, "loc_B4D"),
        (SWITCH_DEFAULT, "loc_B9B"),
    )


    label("loc_6BB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0015
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
    Jump("loc_BEF")

    label("loc_709")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0016
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
    Jump("loc_BEF")

    label("loc_757")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x6B, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_7A5")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0018
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
    Jump("loc_BEF")

    label("loc_7F3")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0019
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
    Jump("loc_BEF")

    label("loc_841")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0020
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
    Jump("loc_BEF")

    label("loc_88F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0021
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x77),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x77, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_8DD")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0022
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
    Jump("loc_BEF")

    label("loc_92B")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0023
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
    Jump("loc_BEF")

    label("loc_979")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0024
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
    Jump("loc_BEF")

    label("loc_9C7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0025
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x83),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x83, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_A15")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_A63")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0027
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_AB1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_AFF")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_B4D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_BEF")

    label("loc_B9B")

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
            "を5個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 5)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x7B, 6)
    Jump("loc_BEF")

    label("loc_BEF")

    Jump("loc_1B02")

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 5)), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B7")
    ClearScenarioFlags(0x7B, 5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_AND), scpexpr(EXPR_END)),
        (0, "loc_C7E"),
        (1, "loc_CCC"),
        (2, "loc_D1A"),
        (3, "loc_D68"),
        (4, "loc_DB6"),
        (5, "loc_E04"),
        (6, "loc_E52"),
        (7, "loc_EA0"),
        (8, "loc_EEE"),
        (9, "loc_F3C"),
        (10, "loc_F8A"),
        (11, "loc_FD8"),
        (12, "loc_1026"),
        (13, "loc_1074"),
        (14, "loc_10C2"),
        (15, "loc_1110"),
        (SWITCH_DEFAULT, "loc_115E"),
    )


    label("loc_C7E")

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
    Jump("loc_11B2")

    label("loc_CCC")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_11B2")

    label("loc_D1A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0034
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
    Jump("loc_11B2")

    label("loc_D68")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0035
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
    Jump("loc_11B2")

    label("loc_DB6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0036
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
    Jump("loc_11B2")

    label("loc_E04")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x73, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_11B2")

    label("loc_E52")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0038
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
    Jump("loc_11B2")

    label("loc_EA0")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0039
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
    Jump("loc_11B2")

    label("loc_EEE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0040
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
    Jump("loc_11B2")

    label("loc_F3C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x7F, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_11B2")

    label("loc_F8A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0042
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
    Jump("loc_11B2")

    label("loc_FD8")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0043
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
    Jump("loc_11B2")

    label("loc_1026")

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
    Jump("loc_11B2")

    label("loc_1074")

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
    Jump("loc_11B2")

    label("loc_10C2")

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
    Jump("loc_11B2")

    label("loc_1110")

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
    Jump("loc_11B2")

    label("loc_115E")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を3個拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F4, 3)
    SetMessageWindowPos(14, 280, 60, 3)
    ClearScenarioFlags(0x7B, 5)
    Jump("loc_11B2")

    label("loc_11B2")

    Jump("loc_1B02")

    label("loc_11B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CD")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_END)),
        (0, "loc_120A"),
        (1, "loc_1258"),
        (2, "loc_12A6"),
        (3, "loc_12F4"),
        (4, "loc_1342"),
        (5, "loc_1390"),
        (6, "loc_13DE"),
        (7, "loc_142C"),
        (SWITCH_DEFAULT, "loc_147A"),
    )


    label("loc_120A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0049
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
    Jump("loc_14C8")

    label("loc_1258")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0050
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
    Jump("loc_14C8")

    label("loc_12A6")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0051
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
    Jump("loc_14C8")

    label("loc_12F4")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0052
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
    Jump("loc_14C8")

    label("loc_1342")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0053
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
    Jump("loc_14C8")

    label("loc_1390")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0054
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
    Jump("loc_14C8")

    label("loc_13DE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0055
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
    Jump("loc_14C8")

    label("loc_142C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0056
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
    Jump("loc_14C8")

    label("loc_147A")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0057
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
    Jump("loc_14C8")

    label("loc_14C8")

    Jump("loc_1B02")

    label("loc_14CD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_AND), scpexpr(EXPR_END)),
        (0, "loc_159D"),
        (16, "loc_159D"),
        (23, "loc_159D"),
        (1, "loc_15FB"),
        (17, "loc_15FB"),
        (24, "loc_15FB"),
        (2, "loc_1659"),
        (18, "loc_1659"),
        (25, "loc_1659"),
        (3, "loc_16B7"),
        (19, "loc_16B7"),
        (26, "loc_16B7"),
        (4, "loc_1715"),
        (20, "loc_1715"),
        (27, "loc_1715"),
        (5, "loc_1773"),
        (21, "loc_1773"),
        (28, "loc_1773"),
        (30, "loc_1773"),
        (6, "loc_17D1"),
        (22, "loc_17D1"),
        (29, "loc_17D1"),
        (31, "loc_17D1"),
        (7, "loc_182F"),
        (8, "loc_187D"),
        (9, "loc_18CB"),
        (10, "loc_191C"),
        (11, "loc_196D"),
        (12, "loc_19BE"),
        (13, "loc_1A0F"),
        (14, "loc_1A60"),
        (15, "loc_1AB1"),
        (SWITCH_DEFAULT, "loc_1B02"),
    )


    label("loc_159D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0058
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
    Jump("loc_1B02")

    label("loc_15FB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0059
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
    Jump("loc_1B02")

    label("loc_1659")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0060
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
    Jump("loc_1B02")

    label("loc_16B7")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0061
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
    Jump("loc_1B02")

    label("loc_1715")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0062
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
    Jump("loc_1B02")

    label("loc_1773")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0063
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
    Jump("loc_1B02")

    label("loc_17D1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0064
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
    Jump("loc_1B02")

    label("loc_182F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0065
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x186),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x186, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B02")

    label("loc_187D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を拾った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x187, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1B02")

    label("loc_18CB")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0067
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
    Jump("loc_1B02")

    label("loc_191C")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0068
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
    Jump("loc_1B02")

    label("loc_196D")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0069
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
    Jump("loc_1B02")

    label("loc_19BE")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0070
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
    Jump("loc_1B02")

    label("loc_1A0F")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0071
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
    Jump("loc_1B02")

    label("loc_1A60")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0072
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
    Jump("loc_1B02")

    label("loc_1AB1")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0073
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
    Jump("loc_1B02")

    label("loc_1B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B1C")
    ClearScenarioFlags(0x7B, 7)
    Jump("loc_1B47")

    label("loc_1B1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B36")
    ClearScenarioFlags(0x7B, 6)
    Jump("loc_1B47")

    label("loc_1B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 5)), scpexpr(EXPR_END)), "loc_1B47")
    ClearScenarioFlags(0x7B, 5)
    Jump("loc_1B47")

    label("loc_1B47")

    Return()

    # Function_0_188 end

    SaveToFile()

Try(main)
