from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3001.bin",                # FileName
        "m3001",                    # MapName
        "m3001",                    # Location
        0x007B,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 19000, -24000, 48000, 0, 0, 1, 123, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3001",                  # 0
    ))

    DeclActor(-176250, -125000, 7500,    2000,    -176500, -123600, 7500,    0x007C, 0,  3,  0x0000)
    DeclActor(-176250, -125000, -7500,   2000,    -176500, -123600, -7500,   0x007C, 0,  4,  0x0000)
    DeclActor(-150000, -128000, 4000,    1200,    -150000, -126500, 4000,    0x007C, 0,  2,  0x0000)

    ScpFunction((
        "Function_0_208",          # 00, 0
        "Function_1_209",          # 01, 1
        "Function_2_2B1",          # 02, 2
        "Function_3_3A4",          # 03, 3
        "Function_4_4CA",          # 04, 4
        "Function_5_5E1",          # 05, 5
    ))


    def Function_0_208(): pass

    label("Function_0_208")

    Return()

    # Function_0_208 end

    def Function_1_209(): pass

    label("Function_1_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_END)), "loc_21B")
    OP_70(0xD, 0x1E)
    Jump("loc_21F")

    label("loc_21B")

    OP_70(0xD, 0x0)

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_END)), "loc_231")
    OP_70(0xE, 0x1E)
    Jump("loc_235")

    label("loc_231")

    OP_70(0xE, 0x0)

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_251")
    OP_70(0xC, 0x62)
    ClearMapObjFlags(0xC, 0x2)
    Jump("loc_279")

    label("loc_251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    OP_70(0xC, 0x0)
    SetMapObjFlags(0xC, 0x2)
    Jump("loc_279")

    label("loc_26F")

    OP_70(0xC, 0x32)
    SetMapObjFlags(0xC, 0x2)

    label("loc_279")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AD")
    Sound(129, 1, 100, 0)
    Jump("loc_2B0")

    label("loc_2AD")

    OP_24(0x81)

    label("loc_2B0")

    Return()

    # Function_1_209 end

    def Function_2_2B1(): pass

    label("Function_2_2B1")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xF, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xF, 0x0)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xF)
    OP_71(0xF, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0xF, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A2")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3A2")

    Return()

    # Function_2_2B1 end

    def Function_3_3A4(): pass

    label("Function_3_3A4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_END)), "loc_3E5")
    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆好像已经不能动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_4C9")

    label("loc_3E5")

    EventBegin(0x1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个拉杆。\x01",
            "扳动它吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C2")
    Fade(500)
    SetChrPos(0x0, -177540, -125000, 7320, 89)
    SetChrPos(0x1, -179090, -125000, 8210, 89)
    SetChrPos(0x2, -179330, -125000, 5940, 89)
    SetChrPos(0x3, -180460, -125000, 6800, 89)
    OP_68(-176830, -124000, 7360, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xD)
    Sleep(500)
    SetScenarioFlags(0xF4, 2)
    Call(0, 5)

    label("loc_4C2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_4C9")

    Return()

    # Function_3_3A4 end

    def Function_4_4CA(): pass

    label("Function_4_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_END)), "loc_501")
    TalkBegin(0xFF)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆好像已经不能动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_5E0")

    label("loc_501")

    EventBegin(0x1)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个拉杆。\x01",
            "扳动它吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DE")
    Fade(500)
    SetChrPos(0x0, -177400, -125000, -7380, 89)
    SetChrPos(0x1, -179030, -125000, -6250, 89)
    SetChrPos(0x2, -179260, -125000, -8750, 89)
    SetChrPos(0x3, -180450, -125000, -7750, 89)
    OP_68(-177030, -124000, -6650, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0xE, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xE)
    Sleep(500)
    SetScenarioFlags(0xF4, 3)
    Call(0, 5)

    label("loc_5DE")

    EventEnd(0x5)

    label("loc_5E0")

    Return()

    # Function_4_4CA end

    def Function_5_5E1(): pass

    label("Function_5_5E1")

    Fade(500)
    OP_68(-177510, -127000, 1020, 0)
    MoveCamera(45, 44, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65F")
    Sound(155, 2, 100, 0)
    OP_71(0xC, 0x32, 0x62, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x2)
    OP_79(0xC)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Jump("loc_697")

    label("loc_65F")

    Sound(155, 2, 100, 0)
    OP_71(0xC, 0x0, 0x32, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x2)
    Sleep(800)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    OP_79(0xC)

    label("loc_697")

    Sleep(1000)
    Return()

    # Function_5_5E1 end

    SaveToFile()

Try(main)
