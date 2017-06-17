from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1060.bin",                # FileName
        "r1060",                    # MapName
        "r1060",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x05,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 0, 0, 1],
    )

    BuildStringList((
        "r1060",                  # 0
    ))

    DeclEvent(0x0000, 0, 2,   30.219999313354492,    -3.4600000381469727,   -1.0,                  3600.0,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0416666679084301,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.044000148773193,    0.14416667819023132,   0.20000000298023224,   1.0])

    ChipFrameInfo(256, 0)                                        # 0

    ScpFunction((
        "Function_0_100",          # 00, 0
        "Function_1_101",          # 01, 1
        "Function_2_2C5",          # 02, 2
    ))


    def Function_0_100(): pass

    label("Function_0_100")

    Return()

    # Function_0_100 end

    def Function_1_101(): pass

    label("Function_1_101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_113")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_113")

    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x5, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AB")
    OP_11(0xAA, 0xC3, 0xFF, 0x0, 0x8C, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, 28900, 0, 6700, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, 29360, 0, 4250, 2000, 2000, 0)
    OP_C3(0x2, 0x1, 0x3, 0x0, 0x0, 0x1, 29900, 0, 1510, 2000, 2000, 0)
    OP_C3(0x3, 0x1, 0x3, 0x0, 0x0, 0x1, 30430, 0, -1250, 2000, 2000, 0)
    OP_C3(0x4, 0x1, 0x3, 0x0, 0x0, 0x1, 30960, 0, -3990, 2000, 2000, 0)
    OP_C3(0x5, 0x1, 0x3, 0x0, 0x0, 0x1, 31500, 0, -6740, 2000, 2000, 0)
    OP_C3(0x6, 0x1, 0x3, 0x0, 0x0, 0x1, 31940, 0, -9220, 2000, 2000, 0)
    OP_C3(0x7, 0x1, 0x3, 0x0, 0x0, 0x1, 32560, 0, -12230, 2000, 2000, 0)
    OP_C3(0x8, 0x1, 0x3, 0x0, 0x0, 0x1, 32910, 0, -13570, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_2B1")

    label("loc_2AB")

    SetMapObjFlags(0x3, 0x4)

    label("loc_2B1")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C4")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_2C4")

    Return()

    # Function_1_101 end

    def Function_2_2C5(): pass

    label("Function_2_2C5")

    EventBegin(0x1)

    #C0001
    ChrTalk(
        0x101,
        (
            "#00000Fこっちはクロスベル市方面か。\x02\x03",

            "距離も距離だし、わざわざ\x01",
            "線路を辿って行くことはないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 23720, 0, -3460, 270)
    EventEnd(0x4)
    Return()

    # Function_2_2C5 end

    SaveToFile()

Try(main)
