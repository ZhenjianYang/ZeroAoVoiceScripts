from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "00sys.bin",                # FileName
        "a0000",                    # MapName
        "a0000",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [88, 34479618, 26369, 130066688, 34066601, 16917534, 118, -1459109463, 2001, 7682, 550, 34049, -1459617792, -760674366, 656278023, 258, 148, 0, 51881, 7, 169, 218, 7],
    )

    BuildStringList((
        "00sys",                  # 0
    ))

    ScpFunction((
        "Function_0_58",           # 00, 0
    ))


    def Function_0_58(): pass

    label("Function_0_58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_67")
    SetScenarioFlags(0xF8, 0)
    SetScenarioFlags(0xFA, 0)

    label("loc_67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 4)), scpexpr(EXPR_END)), "loc_76")
    SetScenarioFlags(0xF8, 1)
    SetScenarioFlags(0xFA, 1)

    label("loc_76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_END)), "loc_85")
    SetScenarioFlags(0xF8, 2)
    SetScenarioFlags(0xFA, 2)

    label("loc_85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 7)), scpexpr(EXPR_END)), "loc_94")
    SetScenarioFlags(0xF9, 2)
    SetScenarioFlags(0xFB, 2)

    label("loc_94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_END)), "loc_A3")
    SetScenarioFlags(0xF9, 0)
    SetScenarioFlags(0xFB, 0)

    label("loc_A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_END)), "loc_B2")
    SetScenarioFlags(0xF9, 1)
    SetScenarioFlags(0xFB, 1)

    label("loc_B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 5)), scpexpr(EXPR_END)), "loc_C1")
    SetScenarioFlags(0xF8, 3)
    SetScenarioFlags(0xFA, 3)

    label("loc_C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 3)), scpexpr(EXPR_END)), "loc_D0")
    SetScenarioFlags(0xF8, 5)
    SetScenarioFlags(0xFA, 5)

    label("loc_D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 2)), scpexpr(EXPR_END)), "loc_DF")
    SetScenarioFlags(0xF8, 6)
    SetScenarioFlags(0xFA, 6)

    label("loc_DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_END)), "loc_EE")
    SetScenarioFlags(0xF8, 7)
    SetScenarioFlags(0xFA, 7)

    label("loc_EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_101")
    SetScenarioFlags(0xF9, 3)
    SetScenarioFlags(0xFB, 3)

    label("loc_101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 7)), scpexpr(EXPR_END)), "loc_110")
    SetScenarioFlags(0xF8, 4)
    SetScenarioFlags(0xFA, 4)

    label("loc_110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_161")
    SetScenarioFlags(0xF8, 0)
    SetScenarioFlags(0xF8, 1)
    SetScenarioFlags(0xF8, 2)
    SetScenarioFlags(0xF8, 3)
    SetScenarioFlags(0xF8, 4)
    SetScenarioFlags(0xF8, 5)
    SetScenarioFlags(0xF8, 6)
    SetScenarioFlags(0xF8, 7)
    SetScenarioFlags(0xF9, 0)
    SetScenarioFlags(0xF9, 1)
    SetScenarioFlags(0xF9, 2)
    SetScenarioFlags(0xF9, 3)
    SetScenarioFlags(0xFA, 0)
    SetScenarioFlags(0xFA, 1)
    SetScenarioFlags(0xFA, 2)
    SetScenarioFlags(0xFA, 3)
    SetScenarioFlags(0xFA, 4)
    SetScenarioFlags(0xFA, 5)
    SetScenarioFlags(0xFA, 6)
    SetScenarioFlags(0xFA, 7)
    SetScenarioFlags(0xFB, 0)
    SetScenarioFlags(0xFB, 1)
    SetScenarioFlags(0xFB, 2)
    SetScenarioFlags(0xFB, 3)

    label("loc_161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_172")
    SetScenarioFlags(0xF9, 4)
    Jump("loc_175")

    label("loc_172")

    ClearScenarioFlags(0xF9, 4)

    label("loc_175")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_186")
    SetScenarioFlags(0xFA, 7)
    Jump("loc_247")

    label("loc_186")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_19B")
    ClearScenarioFlags(0xFA, 7)

    label("loc_19B")

    Jump("loc_247")

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_21A")
    SetScenarioFlags(0xFA, 0)
    SetScenarioFlags(0xFA, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 6)), scpexpr(EXPR_END)), "loc_1BB")
    SetScenarioFlags(0xFA, 2)

    label("loc_1BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44, 7)), scpexpr(EXPR_END)), "loc_1C7")
    SetScenarioFlags(0xFB, 2)

    label("loc_1C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 0)), scpexpr(EXPR_END)), "loc_1D3")
    SetScenarioFlags(0xFB, 0)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 3)), scpexpr(EXPR_END)), "loc_1DF")
    SetScenarioFlags(0xFB, 1)

    label("loc_1DF")

    SetScenarioFlags(0xFA, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 3)), scpexpr(EXPR_END)), "loc_1EE")
    SetScenarioFlags(0xFA, 5)

    label("loc_1EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 2)), scpexpr(EXPR_END)), "loc_1FA")
    SetScenarioFlags(0xFA, 6)

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 4)), scpexpr(EXPR_END)), "loc_206")
    SetScenarioFlags(0xFA, 7)

    label("loc_206")

    SetScenarioFlags(0xFB, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 7)), scpexpr(EXPR_END)), "loc_215")
    SetScenarioFlags(0xFA, 4)

    label("loc_215")

    Jump("loc_247")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_END)), "loc_247")
    ClearScenarioFlags(0xFA, 0)
    ClearScenarioFlags(0xFA, 1)
    ClearScenarioFlags(0xFA, 2)
    SetScenarioFlags(0xFA, 3)
    ClearScenarioFlags(0xFA, 4)
    ClearScenarioFlags(0xFA, 5)
    ClearScenarioFlags(0xFA, 6)
    ClearScenarioFlags(0xFA, 7)
    ClearScenarioFlags(0xFB, 0)
    ClearScenarioFlags(0xFB, 1)
    ClearScenarioFlags(0xFB, 2)
    SetScenarioFlags(0xFB, 3)

    label("loc_247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_261")
    ClearScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_27B")
    SetScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    SetScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_295")
    ClearScenarioFlags(0xFB, 4)
    ClearScenarioFlags(0xFB, 5)
    ClearScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2AF")
    SetScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    SetScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_2AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2C9")
    ClearScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 0)), scpexpr(EXPR_END)), "loc_2E3")
    ClearScenarioFlags(0xFB, 4)
    ClearScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2FD")
    ClearScenarioFlags(0xFB, 4)
    ClearScenarioFlags(0xFB, 5)
    ClearScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_317")
    SetScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    SetScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_331")
    ClearScenarioFlags(0xFB, 4)
    ClearScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_34B")
    ClearScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    ClearScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_365")
    ClearScenarioFlags(0xFB, 4)
    ClearScenarioFlags(0xFB, 5)
    ClearScenarioFlags(0xFB, 6)
    ClearScenarioFlags(0xFB, 7)
    Jump("loc_365")

    label("loc_365")

    Return()

    # Function_0_58 end

    SaveToFile()

Try(main)
