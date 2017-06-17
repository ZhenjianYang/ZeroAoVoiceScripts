from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r3100.bin",                # FileName
        "r3100",                    # MapName
        "r3100",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -8500, 0, -4500, 0, 0, 1, 102, 0, 0, 0, 1],
    )

    BuildStringList((
        "r3100",                  # 0
    ))

    DeclActor(-4500,   13100,   -4750,   1200,    -4500,   14100,   -4750,   0x007C, 0,  2,  0x0000)

    ScpFunction((
        "Function_0_C4",           # 00, 0
        "Function_1_C5",           # 01, 1
        "Function_2_DD",           # 02, 2
    ))


    def Function_0_C4(): pass

    label("Function_0_C4")

    Return()

    # Function_0_C4 end

    def Function_1_C5(): pass

    label("Function_1_C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D8")
    OP_70(0x0, 0x0)
    Jump("loc_DC")

    label("loc_D8")

    OP_70(0x0, 0x1E)

    label("loc_DC")

    Return()

    # Function_1_C5 end

    def Function_2_DD(): pass

    label("Function_2_DD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药', 1)"), scpexpr(EXPR_END)), "loc_15C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1C5")

    label("loc_15C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C5")

    Jump("loc_207")

    label("loc_1CA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_207")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_DD end

    SaveToFile()

Try(main)
