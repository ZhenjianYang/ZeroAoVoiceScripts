from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1520.bin",                # FileName
        "c1520",                    # MapName
        "c1520",                    # Location
        0x00AA,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 170, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1520",                  # 0
        "ディーター市長",         # 1
        "アリオス",               # 2
        "ダドリー捜査官",         # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3200,    0,       100000,  2000,    3300,    900,     100000,  0x007C, 0,  3,  0x0000)
    DeclActor(70000,   0,       103200,  2000,    70000,   900,     103300,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(352, 0)                                        # 0

    ScpFunction((
        "Function_0_160",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_2AF",          # 02, 2
        "Function_3_1292",         # 03, 3
        "Function_4_1792",         # 04, 4
        "Function_5_2439",         # 05, 5
        "Function_6_2B4F",         # 06, 6
        "Function_7_2D0B",         # 07, 7
        "Function_8_3250",         # 08, 8
        "Function_9_395B",         # 09, 9
        "Function_10_3E1F",        # 0A, 10
        "Function_11_466F",        # 0B, 11
    ))


    def Function_0_160(): pass

    label("Function_0_160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_174")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_1B9")

    label("loc_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1B9")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E")
    Event(0, 6)
    Jump("loc_1B9")

    label("loc_19E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B9")
    Event(0, 2)

    label("loc_1B9")

    Return()

    # Function_0_160 end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D3")
    VolumeBGM(0x46, 0xC8)
    Jump("loc_21C")

    label("loc_1D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_20A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21C")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_235")
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_27B")

    label("loc_235")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E")
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_27B")

    label("loc_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)
    Jump("loc_27B")

    label("loc_267")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27B")
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)

    label("loc_27B")

    OP_70(0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE")
    Sound(927, 1, 100, 0)

    label("loc_2AE")

    Return()

    # Function_1_1BA end

    def Function_2_2AF(): pass

    label("Function_2_2AF")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E3")
    SetScenarioFlags(0x0, 0)
    OP_68(0, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 0, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34E")
    SetChrPos(0x1, 800, 0, 600, 0)

    label("loc_34E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36D")
    SetChrPos(0x2, -800, 0, 600, 0)

    label("loc_36D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38C")
    SetChrPos(0x3, 0, 0, -500, 0)

    label("loc_38C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x4, 800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DE")
    SetChrPos(0x5, -800, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_3DE")

    Jump("loc_5F8")

    label("loc_3E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F0")
    SetScenarioFlags(0x0, 1)
    OP_68(70000, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 70000, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45B")
    SetChrPos(0x1, 70800, 0, 600, 0)

    label("loc_45B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47A")
    SetChrPos(0x2, 69200, 0, 600, 0)

    label("loc_47A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_499")
    SetChrPos(0x3, 70000, 0, -500, 0)

    label("loc_499")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C2")
    SetChrPos(0x4, 70800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EB")
    SetChrPos(0x5, 69200, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_4EB")

    Jump("loc_5F8")

    label("loc_4F0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_GE), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F8")
    SetScenarioFlags(0x0, 2)
    OP_68(140000, 1000, 1000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x0, 140000, 0, 1800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_568")
    SetChrPos(0x1, 140800, 0, 600, 0)

    label("loc_568")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_587")
    SetChrPos(0x2, 139200, 0, 600, 0)

    label("loc_587")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A6")
    SetChrPos(0x3, 140000, 0, -500, 0)

    label("loc_5A6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF")
    SetChrPos(0x4, 140800, 0, -1600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F8")
    SetChrPos(0x5, 139200, 0, -1600, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_5F8")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_63E")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_63E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_65B")
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65B")

    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7B0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_695")
    MenuCmd(1, 0, "★【４０Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A5")

    label("loc_695")

    MenuCmd(1, 0, "　【４０Ｆ】")

    label("loc_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    MenuCmd(1, 0, "★【３６Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E3")

    label("loc_6D3")

    MenuCmd(1, 0, "　【３６Ｆ】")

    label("loc_6E3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_710")
    MenuCmd(1, 0, "★【２１Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_720")

    label("loc_710")

    MenuCmd(1, 0, "　【２１Ｆ】")

    label("loc_720")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74E")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_75E")

    label("loc_74E")

    MenuCmd(1, 0, "　【 １Ｆ 】")

    label("loc_75E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    MenuCmd(1, 0, "★【Ｂ８Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79B")

    label("loc_78B")

    MenuCmd(1, 0, "　【Ｂ８Ｆ】")

    label("loc_79B")

    MenuCmd(1, 0, "　【降りる】")
    Jump("loc_AC2")

    label("loc_7B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_8C5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E7")
    MenuCmd(1, 0, "★【４０Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7F7")

    label("loc_7E7")

    MenuCmd(1, 0, "　【４０Ｆ】")

    label("loc_7F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_825")
    MenuCmd(1, 0, "★【３６Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_835")

    label("loc_825")

    MenuCmd(1, 0, "　【３６Ｆ】")

    label("loc_835")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_862")
    MenuCmd(1, 0, "★【２１Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_872")

    label("loc_862")

    MenuCmd(1, 0, "　【２１Ｆ】")

    label("loc_872")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B0")

    label("loc_8A0")

    MenuCmd(1, 0, "　【 １Ｆ 】")

    label("loc_8B0")

    MenuCmd(1, 0, "　【降りる】")
    Jump("loc_AC2")

    label("loc_8C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_95E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    MenuCmd(1, 0, "★【２１Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90B")

    label("loc_8FB")

    MenuCmd(1, 0, "　【２１Ｆ】")

    label("loc_90B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_939")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_949")

    label("loc_939")

    MenuCmd(1, 0, "　【 １Ｆ 】")

    label("loc_949")

    MenuCmd(1, 0, "　【降りる】")
    Jump("loc_AC2")

    label("loc_95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_9F8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_995")
    MenuCmd(1, 0, "★【４０Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A5")

    label("loc_995")

    MenuCmd(1, 0, "　【４０Ｆ】")

    label("loc_9A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D3")
    MenuCmd(1, 0, "★【 １Ｆ 】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9E3")

    label("loc_9D3")

    MenuCmd(1, 0, "　【 １Ｆ 】")

    label("loc_9E3")

    MenuCmd(1, 0, "　【降りる】")
    Jump("loc_AC2")

    label("loc_9F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A26")
    MenuCmd(1, 0, "★【３６Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A36")

    label("loc_A26")

    MenuCmd(1, 0, "　【３６Ｆ】")

    label("loc_A36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A64")
    MenuCmd(1, 0, "★【３５Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A74")

    label("loc_A64")

    MenuCmd(1, 0, "　【３５Ｆ】")

    label("loc_A74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA2")
    MenuCmd(1, 0, "★【３４Ｆ】")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AB2")

    label("loc_AA2")

    MenuCmd(1, 0, "　【３４Ｆ】")

    label("loc_AB2")

    MenuCmd(1, 0, "　【降りる】")

    label("loc_AC2")

    MenuCmd(2, 0, 10, 10, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B8F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_AF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B17")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B35")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B53")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B71")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B8A")

    label("loc_B71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B8A")

    Jump("loc_D67")

    label("loc_B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_C2E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_BB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_BF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C10")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C29")

    label("loc_C10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C29")

    Jump("loc_D67")

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_C91")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C55")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8C")

    label("loc_C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C73")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C8C")

    label("loc_C73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8C")

    Jump("loc_D67")

    label("loc_C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_END)), "loc_CF4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CEF")

    label("loc_CB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CEF")

    label("loc_CD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CEF")

    Jump("loc_D67")

    label("loc_CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D12")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D67")

    label("loc_D12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D67")

    label("loc_D30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D67")

    label("loc_D4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D86")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_EC7")

    label("loc_D86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E21")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x64, 0x87, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DDD")
    OP_68(0, 4000, 1000, 2000)
    Jump("loc_E16")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DFC")
    OP_68(70000, 4000, 1000, 2000)
    Jump("loc_E16")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E16")
    OP_68(140000, 4000, 1000, 2000)

    label("loc_E16")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_EC7")

    label("loc_E21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EBC")
    Sound(159, 0, 100, 0)
    OP_71(0x0, 0x0, 0x23, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E78")
    OP_68(0, -3500, 1000, 2000)
    Jump("loc_EB1")

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E97")
    OP_68(70000, -3500, 1000, 2000)
    Jump("loc_EB1")

    label("loc_E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_EB1")
    OP_68(140000, -3500, 1000, 2000)

    label("loc_EB1")

    OP_0D()
    OP_6F(0x1)
    Sleep(300)
    Jump("loc_EC7")

    label("loc_EBC")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_EC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1092")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_F0A"),
        (1, "loc_F51"),
        (2, "loc_F98"),
        (3, "loc_FDF"),
        (4, "loc_1026"),
        (5, "loc_1036"),
        (6, "loc_107D"),
        (SWITCH_DEFAULT, "loc_108D"),
    )


    label("loc_F0A")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F23")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_F4C")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F3A")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_F4C")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F4C")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_F4C")

    Jump("loc_108D")

    label("loc_F51")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F6A")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_F93")

    label("loc_F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F81")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_F93")

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F93")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_F93")

    Jump("loc_108D")

    label("loc_F98")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FB1")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_FDA")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FC8")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_FDA")

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FDA")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_FDA")

    Jump("loc_108D")

    label("loc_FDF")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FF8")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_1021")

    label("loc_FF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_100F")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_1021")

    label("loc_100F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1021")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_1021")

    Jump("loc_108D")

    label("loc_1026")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Jump("loc_108D")

    label("loc_1036")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_104F")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_1078")

    label("loc_104F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1066")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_1078")

    label("loc_1066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1078")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_1078")

    Jump("loc_108D")

    label("loc_107D")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_108D")

    label("loc_108D")

    Jump("loc_1291")

    label("loc_1092")

    SetScenarioFlags(0x25, 1)
    Sleep(500)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_10CC"),
        (1, "loc_113F"),
        (2, "loc_1186"),
        (3, "loc_11CD"),
        (4, "loc_1214"),
        (5, "loc_123A"),
        (6, "loc_1281"),
        (SWITCH_DEFAULT, "loc_1291"),
    )


    label("loc_10CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E2")
    Call(0, 7)
    Jump("loc_113A")

    label("loc_10E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F8")
    Call(0, 10)
    Jump("loc_113A")

    label("loc_10F8")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1111")
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Jump("loc_113A")

    label("loc_1111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1128")
    NewScene("c1583", 110, 0, 0)
    IdleLoop()
    Jump("loc_113A")

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_113A")
    NewScene("c1583", 111, 0, 0)
    IdleLoop()

    label("loc_113A")

    Jump("loc_1291")

    label("loc_113F")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1158")
    NewScene("c1550", 100, 0, 0)
    IdleLoop()
    Jump("loc_1181")

    label("loc_1158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_116F")
    NewScene("c1550", 101, 0, 0)
    IdleLoop()
    Jump("loc_1181")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1181")
    NewScene("c1550", 102, 0, 0)
    IdleLoop()

    label("loc_1181")

    Jump("loc_1291")

    label("loc_1186")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_119F")
    NewScene("c1540", 100, 0, 0)
    IdleLoop()
    Jump("loc_11C8")

    label("loc_119F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11B6")
    NewScene("c1540", 101, 0, 0)
    IdleLoop()
    Jump("loc_11C8")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11C8")
    NewScene("c1540", 102, 0, 0)
    IdleLoop()

    label("loc_11C8")

    Jump("loc_1291")

    label("loc_11CD")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11E6")
    NewScene("c1530", 100, 0, 0)
    IdleLoop()
    Jump("loc_120F")

    label("loc_11E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11FD")
    NewScene("c1530", 101, 0, 0)
    IdleLoop()
    Jump("loc_120F")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_120F")
    NewScene("c1530", 102, 0, 0)
    IdleLoop()

    label("loc_120F")

    Jump("loc_1291")

    label("loc_1214")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122A")
    Call(0, 8)
    Jump("loc_1235")

    label("loc_122A")

    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()

    label("loc_1235")

    Jump("loc_1291")

    label("loc_123A")

    EventEnd(0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1253")
    NewScene("c1510", 103, 0, 0)
    IdleLoop()
    Jump("loc_127C")

    label("loc_1253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_126A")
    NewScene("c1510", 104, 0, 0)
    IdleLoop()
    Jump("loc_127C")

    label("loc_126A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_127C")
    NewScene("c1510", 105, 0, 0)
    IdleLoop()

    label("loc_127C")

    Jump("loc_1291")

    label("loc_1281")

    EventEnd(0x5)
    NewScene("m0400", 100, 0, 0)
    IdleLoop()
    Jump("loc_1291")

    label("loc_1291")

    Return()

    # Function_2_2AF end

    def Function_3_1292(): pass

    label("Function_3_1292")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(832)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
            "操作しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_178A")
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1410")
    SetChrPos(0x0, 1800, 0, 100000, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_134D")
    SetChrPos(0x1, 600, 0, 100800, 90)

    label("loc_134D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136C")
    SetChrPos(0x2, 600, 0, 99200, 90)

    label("loc_136C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138B")
    SetChrPos(0x3, -500, 0, 100000, 90)

    label("loc_138B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B4")
    SetChrPos(0x4, -1600, 0, 100800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_13B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13DD")
    SetChrPos(0x5, -1600, 0, 99200, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_13DD")

    OP_68(1000, 1000, 100000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_1515")

    label("loc_1410")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1515")
    SetChrPos(0x0, 70000, 0, 101800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1457")
    SetChrPos(0x1, 70800, 0, 100600, 0)

    label("loc_1457")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1476")
    SetChrPos(0x2, 69200, 0, 100600, 0)

    label("loc_1476")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1495")
    SetChrPos(0x3, 70000, 0, 99500, 0)

    label("loc_1495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14BE")
    SetChrPos(0x4, 70800, 0, 98400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_14BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E7")
    SetChrPos(0x5, 69200, 0, 98400, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_14E7")

    OP_68(70000, 1000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)

    label("loc_1515")

    OP_0D()
    Sleep(500)
    Sound(159, 0, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1543")
    OP_68(1000, -9000, 100000, 3000)
    Jump("loc_15AA")

    label("loc_1543")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1567")
    OP_68(1000, 9000, 100000, 3000)
    Jump("loc_15AA")

    label("loc_1567")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158B")
    OP_68(70000, -9000, 101000, 3000)
    Jump("loc_15AA")

    label("loc_158B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AA")
    OP_68(70000, 9000, 101000, 3000)

    label("loc_15AA")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D5")
    Call(0, 9)
    Return()

    label("loc_15D5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1610")
    Sound(832, 2, 100, 0)
    OP_68(1000, 9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_16BC")

    label("loc_1610")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164B")
    Sound(832, 2, 100, 0)
    OP_68(1000, -9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_16BC")

    label("loc_164B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1686")
    Sound(832, 2, 100, 0)
    OP_68(70000, 9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)
    Jump("loc_16BC")

    label("loc_1686")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BC")
    Sound(832, 2, 100, 0)
    OP_68(70000, -9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)

    label("loc_16BC")

    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    StopSound(832, 1000, 100)
    Sound(160, 0, 100, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16F9")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_175A")

    label("loc_16F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_171B")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_175A")

    label("loc_171B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173D")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)
    Jump("loc_175A")

    label("loc_173D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_175A")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)

    label("loc_175A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1772")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1772")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_178A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_178A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_1292 end

    def Function_4_1792(): pass

    label("Function_4_1792")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    SoundLoad(832)
    OP_68(70000, 2100, 1000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 70000, 0, 0, 0)
    SetChrPos(0x102, 68700, 0, -600, 0)
    SetChrPos(0x103, 69300, 0, -1600, 0)
    SetChrPos(0x104, 70600, 0, -1000, 315)
    SetChrPos(0x109, 67400, 0, -600, 45)
    SetChrPos(0x105, 71600, 0, -1600, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 70000, 0, 1800, 180)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    VolumeBGM(0x50, 0x3E8)
    Sound(832, 2, 100, 0)
    Sleep(1000)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("ディーターの声")

    #A0002
    AnonymousTalk(
        0xFF,
        "──なるほど。\x02",
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "ダドリー君からも聞いたが\x01",
            "確かに危うい状況だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(70000, 1100, 1000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00006Fはい……\x02\x03",

            "#00001F猟兵団と犯罪組織の動向に\x01",
            "帝国政府と共和国政府の思惑……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#6P#00108F……そして両国首脳を狙う\x01",
            "テロリストの脅威もあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#12P#00203Fそれと謎のハッカーですね。\x02\x03",

            "#00200F奪われたタワーの図面は\x01",
            "やはりこちらの端末から？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#02806F#5Pああ、どうやら\x01",
            "オルキスタワーのサブ端末を\x01",
            "ハッキングしたらしい。\x02\x03",

            "#02801FＩＢＣの一件があって以来、\x01",
            "システム部門でもハッキング対策は\x01",
            "強化していたつもりだったが……\x02\x03",

            "まだまだ不十分だったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x105,
        (
            "#10303Fふむ、ハッカーなんて\x01",
            "まだまだ数は少なそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#00305Fやっぱりエプスタイン財団の\x01",
            "関係者の可能性が高いのかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#12P#00203F現在、ロバーツ主任が\x01",
            "その可能性を探ってくれています。\x02\x03",

            "#00208Fただ、今回は財団の関係者では\x01",
            "無いような気がしますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#02804F#5Pまあ、そちらの調査は\x01",
            "おいおいするしかないだろう。\x02\x03",

            "#02801F猟兵団や犯罪組織、\x01",
            "テロリストたちも心配だが……\x02\x03",

            "それ以上に気になるのが\x01",
            "首脳たちの狙いと思惑でね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x101,
        "#12P#00001F首脳たちの狙いと思惑……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00301Fつまり通商会議の\x01",
            "参加者ってことッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#02803F#5P君たちが会ったクローディア姫と\x01",
            "オリヴァルト皇子については\x01",
            "私もあまり心配していない。\x02\x03",

            "レミフェリアの大公閣下も\x01",
            "やはり信頼に足る人物だろう。\x02\x03",

            "#02801F……問題は、オズボーン宰相と\x01",
            "ロックスミス大統領の２人でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#6P#10108F２大国の首脳ですか……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10305Fたしかにクロスベルの命運を\x01",
            "握っている２人だとは思うけど。\x02\x03",

            "#10301F具体的に、何か動きでも？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#02806F#5Pいや、その逆だ。\x02\x03",

            "#02801F──会議の開催に当たって\x01",
            "幾つかの取り決めや国際協定などの\x01",
            "提案を事前に送ったのだが……\x02\x03",

            "そこで返ってきた返答が\x01",
            "両国とも好意的すぎたのだよ。\x02\x03",

            "まるで本気で、西ゼムリアの平和と\x01",
            "発展を望んでいるかのように。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00011Fそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#6P#00106F……さすがに不自然ですね。\x02\x03",

            "#00101Fいつも事あるごとに\x01",
            "反発し合っている２国なのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#02803F#5Pああ、正直会議そのものが\x01",
            "どう流れるか予想も付かない。\x02\x03",

            "#02801Fかなり厳しい展開になることも\x01",
            "覚悟する必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#12P#00208Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        (
            "#6P#10106Fや、やっぱり政治的にも\x01",
            "大変な状況なんですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#02804F#5Pはは、まあマクダエル議長も\x01",
            "力になってくださるだろう。\x02\x03",

            "#02800F上手くいけばリベールや\x01",
            "レミフェリアなどを味方にして\x01",
            "交渉できるかもしれない。\x02\x03",

            "#02809Fとにかく腹を括った上で\x01",
            "女神#4Rエイドス#に祈るしかないだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#6P#00108Fおじさま……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#12P#00006Fすみません……\x01",
            "そんな大変な時に\x01",
            "案内なんてさせてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#02804F#5Pハハ、とんでもない。\x02\x03",

            "#02800F逆にそんな状況だから\x01",
            "気分転換しておきたくてね。\x02\x03",

            "わざわざ君たちの案内を\x01",
            "買って出たというわけなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#12P#00002Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        "#6P#10101F光栄です、市長閣下！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#00309Fそんじゃ、喜んで\x01",
            "案内してもらうッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "#02809F#5Pああ、任せたまえ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)

    #C0031
    ChrTalk(
        0x8,
        "#11P#02800Fおっと、到着だな。\x02",
    )

    CloseMessageWindow()
    StopSound(832, 1000, 100)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x37, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    Sound(160, 0, 100, 0)
    VolumeBGM(0x64, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(107, 0, 100, 0)
    Sleep(500)
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1792 end

    def Function_5_2439(): pass

    label("Function_5_2439")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("apl/ch51255.itc", 0x20)
    SoundLoad(832)
    OP_68(0, -10000, 0, 0)
    MoveCamera(45, 11, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -600, 0, 0, 225)
    SetChrPos(0x102, 500, 0, 0, 225)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrFlags(0x103, 0x20)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x2)
    SetChrPos(0x103, -1500, 0, -1500, 270)
    SetChrPos(0x104, 1600, 0, -1000, 270)
    SetChrPos(0x109, 400, 0, -1300, 270)
    SetChrPos(0x105, 900, 0, -2200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -700, 0, 1500, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -1900, 0, 1300, 180)
    OP_71(0x0, 0x87, 0x9A, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    BlurSwitch(0x1B58, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 20000, 0, 7000)
    MoveCamera(45, 33, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, -900, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    CancelBlur(0)
    OP_68(0, 1100, 0, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0032
    ChrTalk(
        0x103,
        (
            "#11P#00203Fええ……ええ。\x02\x03",

            "#00202F……分かりました。\x01",
            "そこまで判れば十分です。\x02\x03",

            "#00204Fご苦労でした、ヨナ。\x01",
            "それではまた後で──\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x0)
    Sleep(300)
    Sound(804, 0, 100, 0)
    Sleep(400)

    #C0033
    ChrTalk(
        0x101,
        "#5P#00001Fヨナはなんて……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x20)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x2)
    OP_0D()
    OP_93(0x103, 0x2D, 0x1F4)

    #C0034
    ChrTalk(
        0x103,
        (
            "#6P#00203Fテロリストたちの逃走ルートを\x01",
            "割り出せたそうです。\x02\x03",

            "#00201Fオルキスタワー基部──\x01",
            "そこからジオフロント方面に\x01",
            "逃走したみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00108F#5P基部ということは……\x01",
            "タワーの地下部分になるのね。\x02\x03",

            "#00101F確かに、ジオフロントの各区画と\x01",
            "接続されているはずだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "#00603F#5Pよし、必ず捕らえるぞ。\x02\x03",

            "#00610Fあんな真似をされて逃がしたら\x01",
            "クロスベル警察の名折れだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#01403F#5P──それはこちらも同じだ。\x02\x03",

            "#01401Fギルドが正式に立ち会った\x01",
            "国際会議においてあの暴挙……\x02\x03",

            "見逃したとあっては\x01",
            "悪しき前例を作りかねん。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10107F#11Pええ、絶対に捕まえましょう！\x02\x03",

            "#10106F屋上の導力爆弾も\x01",
            "ちょっと心配ですけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_294E():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_294E)
    Sleep(50)

    def lambda_295E():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_295E)
    Sleep(50)

    def lambda_296E():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_296E)
    Sleep(50)

    def lambda_297E():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_297E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    Sleep(100)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00003F#5Pキリカさんとレクターさんなら\x01",
            "たぶん大丈夫だろう。\x02\x03",

            "#00002Fユリア准佐やミュラー少佐も\x01",
            "付いて行ってくれてるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00304F#11Pハハ、確かにあのメンツなら\x01",
            "間違いはあり得なさそうだな。\x02\x03",

            "#00305F……しかし随分と\x01",
            "長いこと降り続けてるな？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#6P#00204Fまあ、地上３５Ｆから\x01",
            "地下８Ｆまで降りますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x105,
        (
            "#10302F#11Pクロスベルの最深部に\x01",
            "ご案内ってわけだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 3100, 0, 2000)
    FadeToDark(2000, 0, -1)
    StopSound(832, 2000, 100)
    OP_0D()
    OP_6F(0x1)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("m0400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_2439 end

    def Function_6_2B4F(): pass

    label("Function_6_2B4F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1000, 700, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22250, 0)
    SetChrPos(0x101, 0, 0, 1300, 0)
    SetChrPos(0x102, 800, 0, 0, 0)
    SetChrPos(0x103, -800, 0, 0, 0)
    SetChrPos(0x104, 0, 0, -1600, 0)
    SetChrPos(0x109, 1200, 0, -1000, 0)
    SetChrPos(0x105, -1200, 0, -1000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(21500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0043
    ChrTalk(
        0x101,
        (
            "#11P#00011Fえっと……\x01",
            "ここでいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#12P#00202Fはい、先ほどの認証カードを\x01",
            "そこにかざしてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, 1000, 800)

    def lambda_2CA3():
        OP_96(0xFE, 0x0, 0x0, 0x960, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CA3)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "一時認証カードをパネルにかざした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(72, 0, 100, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x164, 5)
    Call(0, 2)
    Return()

    # Function_6_2B4F end

    def Function_7_2D0B(): pass

    label("Function_7_2D0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0x109, -1100, 0, 600, 135)
    SetChrPos(0x105, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    Sleep(500)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0046
    ChrTalk(
        0x105,
        (
            "#6P#10305Fそういえば、そのパネル……\x02\x03",

            "２１Ｆから３０Ｆまでの\x01",
            "ボタンがないみたいだけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#11P#00102Fああ、そのあたりは全て\x01",
            "メンテナンスフロアみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00005F#5Pメンテナンスフロア？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#00203F#11P何でも、巨大な構造物の\x01",
            "重量バランスを取るために\x01",
            "ほぼ中空になっているのだとか。\x02\x03",

            "#00200Fそれ以外に、地震が起こった時の\x01",
            "衝撃吸収装置があるらしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00006F#5Pそりゃ凄いな……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        (
            "#6P#10102Fやはり最新の建造技術が\x01",
            "盛り込まれているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#12P#00306Fしっかし、そうまでして\x01",
            "巨大なビルを建てる必要あんのか？\x02\x03",

            "#00301F同じフロア数なら、３０Ｆ建てくらいに\x01",
            "しときゃあいいじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#11P#00106Fまあ、当初の計画からして\x01",
            "無駄が多かったみたいだから……\x02\x03",

            "#00100F計画を引き継いだおじさまも\x01",
            "派手なものが大好きな人ではあるし。\x02\x03",

            "#00104F結局、不足していた建造費は\x01",
            "クロイス家の資産で補填したそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        "#6P#10302Fへえ、そりゃまた豪勢だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00012F#5Pまあ、おかげでクロスベル市の\x01",
            "新たなランドマークとしては\x01",
            "相当インパクトがあると思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        "#00002F#5Pおっと、そろそろ到着だな。\x02",
    )

    CloseMessageWindow()
    MoveCamera(35, 30, 0, 4000)
    SetCameraDistance(19000, 4000)
    Sleep(3000)
    StopSound(832, 2000, 100)
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0x37, 0x5A, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x164, 6)
    OP_24(0x340)
    EventEnd(0x5)
    NewScene("c1583", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2D0B end

    def Function_8_3250(): pass

    label("Function_8_3250")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0xF4, -1100, 0, 600, 135)
    SetChrPos(0xF5, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00008F#5P──結局、セキュリティが\x01",
            "解除できたのは２１Ｆまでか……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#00206Fはい、主任が言うには、\x01",
            "３０Ｆに物理的な遮断を行う\x01",
            "制御ターミナルがあるらしいです。\x02\x03",

            "#00201Fそれを解除しない限り、\x01",
            "導力ネットからの制御は\x01",
            "不可能だと言っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#00303Fって事は、２１Ｆから３０Ｆまでは\x01",
            "自分たちで上がる必要があるわけか。\x02\x03",

            "#00301Fしかし、確かそのあたりは\x01",
            "殆んどメンテナンス用のフロアで\x01",
            "空っぽとか言ってなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#11P#00106F……公式発表に\x01",
            "偽りがあったみたいね。\x02\x03",

            "#00108Fどうやらその一角こそが\x01",
            "クロイス家の深奥……\x02\x03",

            "#00101Fキーアちゃんの儀式においても\x01",
            "重要な役割を果たした区画らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#12P#00307Fそ、そうなのかよ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3648")

    #C0062
    ChrTalk(
        0x10A,
        (
            "#6P#00606F……通商会議の警備の時も\x01",
            "妙に不自然だとは思ったが……\x02\x03",

            "#00610Fまさか公的施設にそんな場所を\x01",
            "勝手に建造していたとはな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3648")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36D3")

    #C0063
    ChrTalk(
        0x105,
        (
            "#6P#10403F恐らく魔導科学の精華が\x01",
            "詰まっている区画だろうね。\x02\x03",

            "#10408Fできればこうなる前に\x01",
            "下見しておきたかったけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_371F")

    #C0064
    ChrTalk(
        0x109,
        (
            "#6P#10103Fいずれにせよ……\x01",
            "覚悟が必要そうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3753")

    label("loc_371F")


    #C0065
    ChrTalk(
        0x103,
        (
            "#00203F……いずれにせよ\x01",
            "覚悟が必要そうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3753")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37B2")

    #C0066
    ChrTalk(
        0x106,
        (
            "#6P#10701F……はい。\x01",
            "《赤い星座》の面々などが\x01",
            "いるかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37FF")

    label("loc_37B2")


    #C0067
    ChrTalk(
        0x102,
        (
            "#11P#00106Fそうね……\x01",
            "アリオスさんや《赤い星座》も\x01",
            "いるかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37FF")


    #C0068
    ChrTalk(
        0x101,
        (
            "#00008F#5Pああ……それとキーアもだ。\x02\x03",

            "#00003F……何が待ち受けていようと\x01",
            "絶対に突破してみせる。\x02\x03",

            "#00000F俺たちをここに送り出してくれた\x01",
            "課長たちに応えるためにも。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#00202F……はい。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        "#11P#00102Fふふ……責任重大ね。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#12P#00304F気合い……\x01",
            "入れるっきゃねぇな。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, -1700, 0, 3000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    OP_6F(0x79)
    WaitBGM()
    ReplaceBGM("ed7352", "ed7000")
    SetScenarioFlags(0x1A6, 1)
    OP_29(0xB1, 0x1, 0xA)
    OP_24(0x340)
    SetScenarioFlags(0x25, 1)
    EventEnd(0x5)
    NewScene("c1580", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_3250 end

    def Function_9_395B(): pass

    label("Function_9_395B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(832)
    OP_68(0, 2300, 100000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 1500, 0, 100000, 270)
    SetChrPos(0x102, 600, 0, 101100, 225)
    SetChrPos(0x103, -1000, 0, 101100, 135)
    SetChrPos(0x104, -1500, 0, 100000, 90)
    SetChrPos(0xF4, 600, 0, 98900, 315)
    SetChrPos(0xF5, -1000, 0, 98900, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    BeginChrThread(0x101, 3, 0, 11)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 100000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F#11Pそういえば……\x02\x03",

            "#00001F導力ネットを遮断している\x01",
            "制御ターミナルが\x01",
            "あるって言ってたよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#00206F#5Pはい、その場所のせいで\x01",
            "タワー上層へのハッキングが\x01",
            "不可能になっています。\x02\x03",

            "#00201Fそこを解除さえすれば\x01",
            "主任がタワー上層の詳しい情報を\x01",
            "掴んでくれると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#5P#00108Fキーアちゃんのいるフロアや\x01",
            "ベルたちの動向も分かりそうね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BEA")

    #C0075
    ChrTalk(
        0x10A,
        (
            "#12P#00603F何とか押さえる必要が\x01",
            "ありそうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7B")

    label("loc_3BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C33")

    #C0076
    ChrTalk(
        0x109,
        (
            "#12P#10103F何とか押さえる必要が\x01",
            "ありますね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C7B")

    label("loc_3C33")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C7B")

    #C0077
    ChrTalk(
        0x106,
        (
            "#12P#10703F何とか押さえる必要が\x01",
            "ありそうですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CB9")

    #C0078
    ChrTalk(
        0x105,
        "#12P#10401Fたしか３０Ｆだったっけ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D2E")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3CF5")

    #C0079
    ChrTalk(
        0x106,
        "#12P#10701Fたしか３０Ｆでしたね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D2E")

    label("loc_3CF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D2E")

    #C0080
    ChrTalk(
        0x109,
        "#12P#10101Fたしか３０Ｆだったよね？\x02",
    )

    CloseMessageWindow()

    label("loc_3D2E")


    #C0081
    ChrTalk(
        0x103,
        (
            "#00203F#5Pはい、つまりこの中枢区画の\x01",
            "最上層にあるのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#6P#00300Fだったらこのまま\x01",
            "上を目指せばいいって訳だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#00013F#11Pああ……気合いを入れよう！\x02",
    )

    CloseMessageWindow()
    OP_68(0, -8700, 100000, 2000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x1A6, 3)
    Sound(160, 0, 100, 0)
    Sleep(500)
    OP_24(0x340)
    EventEnd(0x5)
    ClearMapFlags(0x8000000)
    NewScene("c1582", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_395B end

    def Function_10_3E1F(): pass

    label("Function_10_3E1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(832)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(0, 2300, 0, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 0, 1500, 180)
    SetChrPos(0x102, 1100, 0, 600, 225)
    SetChrPos(0x103, 1100, 0, -1000, 315)
    SetChrPos(0x104, 0, 0, -1500, 0)
    SetChrPos(0xF4, -1100, 0, 600, 135)
    SetChrPos(0xF5, -1100, 0, -1000, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x0, 0x23, 0x36, 0x0, 0x20)
    Sound(832, 2, 100, 0)
    OP_68(0, 1300, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3F63():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F63)
    Sleep(50)

    def lambda_3F73():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3F73)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2085, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0084
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013Fもしもし？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "よ、よかった……\x01",
            "無事だったんですね！\x02\x03",

            "こちら《メルカバ玖#2Rきゅう#号機》です！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_40AE")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0086
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10102Fフラン……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_40D9")

    label("loc_40AE")

    SetMessageWindowPos(50, 30, -1, -1)

    #A0087
    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102Fフランさん……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_40D9")

    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("アッバスの声")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "タワーに突入したようだが\x01",
            "状況はどうなっている？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_419B")
    SetMessageWindowPos(90, 130, -1, -1)

    #A0089
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003Fああ、大詰めだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0090
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10400F軽く状況説明しとくよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_41DD")

    label("loc_419B")

    SetMessageWindowPos(90, 130, -1, -1)

    #A0091
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001Fああ、大詰めだ。\x01",
            "状況説明をしておくよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_41DD")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "メルカバのブリッジに\x01",
            "現在の状況について伝えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("アッバスの声")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なるほど……\x01",
            "確かに大詰めのようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "屋上の白い人形だけど\x01",
            "どうやら周囲１００アージュに\x01",
            "《結界》を展開しているらしい。\x02\x03",

            "こっちからは近付けないから\x01",
            "援護とかは期待すんなよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0095
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013Fそうか……了解だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4390")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0096
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10406Fま、こっちで何とか\x01",
            "するしか無さそうだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_43CE")

    label("loc_4390")

    SetMessageWindowPos(50, 30, -1, -1)

    #A0097
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00306Fま、こっちで\x01",
            "何とかするしかねぇな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_43CE")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ちなみに他の２機ですが……\x01",
            "どうやら沈黙したみたいです。\x02\x03",

            "ケビン神父やエステルさんたちが\x01",
            "頑張ってくれたのではないかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0099
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fそうなのか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0100
    AnonymousTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00204F……朗報ですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0101
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00300Fああ……\x01",
            "よく勝てたもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("グレイスの声")

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──とにかく！\x01",
            "無茶だけはしないこと！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("マクダエル議長の声")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "女神#4Rエイドス#の加護を……\x01",
            "くれぐれも気をつけたまえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0104
    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00100Fはい……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0105
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F了解しました……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_68(0, -1700, 0, 3000)
    StopSound(832, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x323)
    OP_24(0x340)
    SetScenarioFlags(0x22, 0)
    NewScene("e4201", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3E1F end

    def Function_11_466F(): pass

    label("Function_11_466F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46A7")
    OP_82(0x0, 0x5, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0xA, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_11_466F")

    label("loc_46A7")

    Return()

    # Function_11_466F end

    SaveToFile()

Try(main)
