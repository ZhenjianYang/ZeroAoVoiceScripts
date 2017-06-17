from ScenarioHelper import *

def main():
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
        "迪塔市长",               # 1
        "亚里欧斯",               # 2
        "达德利搜查官",           # 3
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
        "Function_4_1782",         # 04, 4
        "Function_5_2289",         # 05, 5
        "Function_6_28F3",         # 06, 6
        "Function_7_2AA3",         # 07, 7
        "Function_8_2F30",         # 08, 8
        "Function_9_358B",         # 09, 9
        "Function_10_3A17",        # 0A, 10
        "Function_11_41BF",        # 0B, 11
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

    MenuCmd(1, 0, "　【离  开】")
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

    MenuCmd(1, 0, "　【离  开】")
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

    MenuCmd(1, 0, "　【离  开】")
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

    MenuCmd(1, 0, "　【离  开】")
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

    MenuCmd(1, 0, "　【离  开】")

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
            "有可以操作导力梯的控制面板。\x01",
            "要操作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177A")
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1400")
    SetChrPos(0x0, 1800, 0, 100000, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_133D")
    SetChrPos(0x1, 600, 0, 100800, 90)

    label("loc_133D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_135C")
    SetChrPos(0x2, 600, 0, 99200, 90)

    label("loc_135C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137B")
    SetChrPos(0x3, -500, 0, 100000, 90)

    label("loc_137B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A4")
    SetChrPos(0x4, -1600, 0, 100800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_13A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CD")
    SetChrPos(0x5, -1600, 0, 99200, 90)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_13CD")

    OP_68(1000, 1000, 100000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Jump("loc_1505")

    label("loc_1400")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1505")
    SetChrPos(0x0, 70000, 0, 101800, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1447")
    SetChrPos(0x1, 70800, 0, 100600, 0)

    label("loc_1447")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1466")
    SetChrPos(0x2, 69200, 0, 100600, 0)

    label("loc_1466")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1485")
    SetChrPos(0x3, 70000, 0, 99500, 0)

    label("loc_1485")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AE")
    SetChrPos(0x4, 70800, 0, 98400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_14AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14D7")
    SetChrPos(0x5, 69200, 0, 98400, 0)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_14D7")

    OP_68(70000, 1000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)

    label("loc_1505")

    OP_0D()
    Sleep(500)
    Sound(159, 0, 100, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1533")
    OP_68(1000, -9000, 100000, 3000)
    Jump("loc_159A")

    label("loc_1533")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1557")
    OP_68(1000, 9000, 100000, 3000)
    Jump("loc_159A")

    label("loc_1557")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_157B")
    OP_68(70000, -9000, 101000, 3000)
    Jump("loc_159A")

    label("loc_157B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_159A")
    OP_68(70000, 9000, 101000, 3000)

    label("loc_159A")

    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C5")
    Call(0, 9)
    Return()

    label("loc_15C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1600")
    Sound(832, 2, 100, 0)
    OP_68(1000, 9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_16AC")

    label("loc_1600")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_163B")
    Sound(832, 2, 100, 0)
    OP_68(1000, -9000, 100000, 0)
    OP_68(1000, 1000, 100000, 3000)
    Jump("loc_16AC")

    label("loc_163B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1676")
    Sound(832, 2, 100, 0)
    OP_68(70000, 9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)
    Jump("loc_16AC")

    label("loc_1676")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AC")
    Sound(832, 2, 100, 0)
    OP_68(70000, -9000, 101000, 0)
    OP_68(70000, 1000, 101000, 3000)

    label("loc_16AC")

    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    StopSound(832, 1000, 100)
    Sound(160, 0, 100, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E9")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_174A")

    label("loc_16E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170B")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)
    Jump("loc_174A")

    label("loc_170B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172D")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x0)
    OP_10(0x12, 0x1)
    Jump("loc_174A")

    label("loc_172D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_174A")
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x11, 0x1)
    OP_10(0x12, 0x0)

    label("loc_174A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1762")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1762")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_177A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_177A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_1292 end

    def Function_4_1782(): pass

    label("Function_4_1782")

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
    SetChrName("迪塔的声音")

    #A0002
    AnonymousTalk(
        0xFF,
        "——原来如此。\x02",
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "我已经听达德利说了，\x01",
            "目前的局面确实很危险。\x02",
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
            "#12P#00006F是的……\x02\x03",

            "#00001F猎兵团和犯罪组织的动向，\x01",
            "以及帝国政府和共和国政府的想法都对我们不利……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#6P#00108F……企图袭击两国首脑的\x01",
            "恐怖组织也是很大的威胁。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#12P#00203F而且还出现了神秘黑客。\x02\x03",

            "#00200F他是从这里的终端中\x01",
            "将兰花塔的设计图盗走的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#02806F#5P嗯，应该是\x01",
            "侵入了兰花塔\x01",
            "的子终端。\x02\x03",

            "#02801F自ＩＢＣ那起事件以来，\x01",
            "系统部门一直在加强\x01",
            "防范黑客的措施……\x02\x03",

            "不过似乎还不够完善啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x105,
        (
            "#10303F嗯，但黑客在如今\x01",
            "还是很少见的。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#00305F犯人很有可能是与\x01",
            "爱普斯泰恩财团有关的人士吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#12P#00203F罗伯兹主任\x01",
            "正在调查这种可能性。\x02\x03",

            "#00208F但我感觉，此次事件\x01",
            "并非财团方面的人士所为……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#02804F#5P关于那方面的调查，\x01",
            "也只能慢慢来了。\x02\x03",

            "#02801F猎兵团和犯罪组织，\x01",
            "还有恐怖分子都很令人担心……\x02\x03",

            "但更让人在意的还是\x01",
            "几位首脑的目的和想法。\x02",
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
        "#12P#00001F几位首脑……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#00301F也就是通商会议\x01",
            "的与会者们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#02803F#5P我并不怎么担心与你们\x01",
            "见过面的科洛蒂娅公主\x01",
            "和奥利维特皇子。\x02\x03",

            "雷米菲利亚的大公阁下\x01",
            "也是个值得信赖的人物。\x02\x03",

            "#02801F……问题在于奥斯本宰相和\x01",
            "洛克史密斯总统这两人。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        "#6P#10108F两大国的首脑吗……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10305F的确，克洛斯贝尔的命运\x01",
            "就掌握在他们二人的手中呢。\x02\x03",

            "#10301F具体来说，他们有什么动向吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#02806F#5P不，正相反。\x02\x03",

            "#02801F在会议召开之前，\x01",
            "我把几项拟定协定和\x01",
            "国际协议等文件递交给了他们……\x02\x03",

            "他们的回应态度\x01",
            "实在是太友善了。\x02\x03",

            "简直就像是真心希望\x01",
            "西塞姆里亚大陆得到和平与发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00011F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#6P#00106F……的确非常奇怪。\x02\x03",

            "#00101F这两个国家平时\x01",
            "处处都要针锋相对……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#02803F#5P嗯，不知到了正式会议的时候，\x01",
            "事态将会如何发展。\x02\x03",

            "#02801F必须做好最坏的心理准备，\x01",
            "以便应对严峻的事态发展啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#12P#00208F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        (
            "#6P#10106F政、政治方面的状况\x01",
            "果然很复杂……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#02804F#5P哈哈，没关系，麦克道尔议长\x01",
            "一定会竭力提供支持的。\x02\x03",

            "#02800F如果顺利，也许能拉拢到\x01",
            "利贝尔和雷米菲利亚等国，\x01",
            "并以此为基础展开交涉。\x02\x03",

            "#02809F总之，我们现在就做好心理准备吧，\x01",
            "其它事情也只能祈祷女神保佑了。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#6P#00108F迪塔叔叔……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#12P#00006F真不好意思……\x01",
            "在这种非常时期，\x01",
            "还麻烦您为我们带路。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#02804F#5P哈哈，哪里的话。\x02\x03",

            "#02800F正是因为局势严峻，\x01",
            "我才想换换心情啊。\x02\x03",

            "所以才特意要求\x01",
            "为你们带路的。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#12P#00002F是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        "#6P#10101F光荣之至，市长阁下！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#00309F那我们就\x01",
            "恭敬不如从命啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        "#02809F#5P嗯，不必客气。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x0, 0x1F4)

    #C0031
    ChrTalk(
        0x8,
        "#11P#02800F哦，已经到了。\x02",
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

    # Function_4_1782 end

    def Function_5_2289(): pass

    label("Function_5_2289")

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
            "#11P#00203F嗯……嗯。\x02\x03",

            "#00202F……明白了，\x01",
            "知道这些就够了。\x02\x03",

            "#00204F辛苦了，约纳，\x01",
            "稍后再联系吧。\x02",
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
        "#5P#00001F约纳他……？\x02",
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
            "#6P#00203F他已经查到了\x01",
            "恐怖分子的逃脱路线。\x02\x03",

            "#00201F恐怖分子应该是由\x01",
            "兰花塔的基部\x01",
            "逃往地下空间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#00108F#5P基部就是……\x01",
            "大楼的地下吧？\x02\x03",

            "#00101F那里的确与地下空间\x01",
            "的各个区域相通……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            "#00603F#5P好，一定要抓到他们。\x02\x03",

            "#00610F如果让做出那种事的家伙逃之夭夭，\x01",
            "实在是有损克洛斯贝尔警察的名声！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#01403F#5P对我们而言也是一样。\x02\x03",

            "#01401F在游击士协会正式列席的国际会议中，\x01",
            "竟然发生那种暴行……\x02\x03",

            "如果让他们逃了，\x01",
            "将会成为很恶劣的前例。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        (
            "#10107F#11P嗯，一定要抓住他们！\x02\x03",

            "#10106F另外，塔顶的导力炸弹\x01",
            "也让人有些担心……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_271A():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_271A)
    Sleep(50)

    def lambda_272A():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_272A)
    Sleep(50)

    def lambda_273A():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_273A)
    Sleep(50)

    def lambda_274A():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_274A)
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
            "#00003F#5P有雾香小姐和雷克特先生负责处理，\x01",
            "应该没问题的。\x02\x03",

            "#00002F而且尤莉亚准校和穆拉少校\x01",
            "也一起过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00304F#11P哈哈，凭他们的能力，\x01",
            "应该不会出现闪失的。\x02\x03",

            "#00305F……话说回来，\x01",
            "下降时间可真长啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#6P#00204F嗯，毕竟要从地上三十五层\x01",
            "降到地下八层呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x105,
        (
            "#10302F#11P看来是要带我们去\x01",
            "克洛斯贝尔的最深处探险呢。\x02",
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

    # Function_5_2289 end

    def Function_6_28F3(): pass

    label("Function_6_28F3")

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
            "#11P#00011F那个……\x01",
            "插在这里就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        (
            "#12P#00202F是的，把刚才领到的\x01",
            "认证卡片插进那里就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(0, 1000, 1000, 800)

    def lambda_2A3F():
        OP_96(0xFE, 0x0, 0x0, 0x960, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A3F)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把临时认证卡片插进了控制面板。\x07\x00\x02",
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

    # Function_6_28F3 end

    def Function_7_2AA3(): pass

    label("Function_7_2AA3")

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
            "#6P#10305F说起来，这个控制面板上……\x02\x03",

            "并没有二十一层到三十层\x01",
            "的按钮呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#11P#00102F嗯，那些楼层\x01",
            "全都是保留楼层。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00005F#5P保留楼层？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x103,
        (
            "#00203F#11P听说那些楼层\x01",
            "基本上是中空的，目的是\x01",
            "为了维持巨型建筑的稳定。\x02\x03",

            "#00200F另外，为了应对地震，\x01",
            "还在其中建造了吸收冲击的装置。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00006F#5P好厉害啊……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        (
            "#6P#10102F果然应用了\x01",
            "最新的建筑技术呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#12P#00306F可是，有必要花费这么多精力，\x01",
            "建造如此高的建筑吗？\x02\x03",

            "#00301F反正可用楼层数都一样，\x01",
            "建座三十层的建筑不就好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#11P#00106F嗯，从当初的计划来看，\x01",
            "确实存在很多非必要性的开支……\x02\x03",

            "#00100F但接手此计划的迪塔叔叔\x01",
            "很喜欢华丽气派的东西。\x02\x03",

            "#00104F最后，不足的建造费用\x01",
            "就由库罗伊斯家族出钱补上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        "#6P#10302F嘿，出手可真阔绰啊。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00012F#5P拜其所赐，克洛斯贝尔\x01",
            "才拥有了这座新的标志性建筑，\x01",
            "看上去确实是冲击力十足……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0056
    ChrTalk(
        0x101,
        "#00002F#5P哦，好像快到了。\x02",
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

    # Function_7_2AA3 end

    def Function_8_2F30(): pass

    label("Function_8_2F30")

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
            "#00008F#5P解除了安全装置的楼层\x01",
            "就到二十一层为止吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#00206F是的，据主任说，\x01",
            "三十层设有用于阻断信号的\x01",
            "物理性控制终端。\x02\x03",

            "#00201F在将其解除之前，\x01",
            "是不可能通过导力网络\x01",
            "控制那里的。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#00303F也就是说，从二十一层到\x01",
            "三十层，我们只能步行上去了？\x02\x03",

            "#00301F但以前不是说过，\x01",
            "那些楼层是保留楼层，\x01",
            "里面都是中空的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#11P#00106F……公开的信息中\x01",
            "存在着虚假情报吧。\x02\x03",

            "#00108F此区域恐怕是\x01",
            "库罗伊斯家族的核心地带……\x02\x03",

            "#00101F在小琪雅发动的仪式中，\x01",
            "这个区域应该也起着非常重要的作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        "#12P#00307F是、是这样吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32AC")

    #C0062
    ChrTalk(
        0x10A,
        (
            "#6P#00606F……在通商会议中警备的时候，\x01",
            "我就感觉有些可疑了……\x02\x03",

            "#00610F但还是没想到他们竟会在公共设施中\x01",
            "擅自建造这种场所。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3333")

    #C0063
    ChrTalk(
        0x105,
        (
            "#6P#10403F这个区域中恐怕\x01",
            "包含了魔导科学的精华。\x02\x03",

            "#10408F我们要是在事态发展成如此地步之前，\x01",
            "先来这里看看就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3333")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_337B")

    #C0064
    ChrTalk(
        0x109,
        (
            "#6P#10103F不管怎么说……\x01",
            "我们要做好心理准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33AB")

    label("loc_337B")


    #C0065
    ChrTalk(
        0x103,
        (
            "#00203F不管怎么说……\x01",
            "我们要做好心理准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33AB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33FC")

    #C0066
    ChrTalk(
        0x106,
        (
            "#6P#10701F……是的。\x01",
            "『赤色星座』的人说不定\x01",
            "也在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3445")

    label("loc_33FC")


    #C0067
    ChrTalk(
        0x102,
        (
            "#11P#00106F是啊……\x01",
            "亚里欧斯先生和『赤色星座』的人\x01",
            "说不定也在这里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3445")


    #C0068
    ChrTalk(
        0x101,
        (
            "#00008F#5P嗯……还有琪雅。\x02\x03",

            "#00003F……无论前方有什么困难在等着我们，\x01",
            "我们都要突破阻碍。\x02\x03",

            "#00000F这也是为了不辜负把我们\x01",
            "护送到这里的科长他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#00202F……是的。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        "#11P#00102F呵呵……责任重大呢。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#12P#00304F一定要……\x01",
            "拿出全部干劲啊。\x02",
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

    # Function_8_2F30 end

    def Function_9_358B(): pass

    label("Function_9_358B")

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
            "#00003F#11P话说回来……\x02\x03",

            "#00001F这个区域中好像设有\x01",
            "用来屏蔽导力网络信号\x01",
            "的控制终端吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#00206F#5P是的，由于这个缘故，\x01",
            "想通过黑客手段来侵入\x01",
            "兰花塔上层是不可能的。\x02\x03",

            "#00201F不过，只要能把屏蔽解除，\x01",
            "主任应该就可以掌握\x01",
            "兰花塔上层的详细情报了……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#5P#00108F同时应该也能查到小琪雅所在的楼层\x01",
            "和贝尔他们的动向……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F8")

    #C0075
    ChrTalk(
        0x10A,
        (
            "#12P#00603F如此看来，我们必须\x01",
            "要成功控制那里啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3881")

    label("loc_37F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_383F")

    #C0076
    ChrTalk(
        0x109,
        (
            "#12P#10103F看来我们必须要\x01",
            "成功控制那里啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3881")

    label("loc_383F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3881")

    #C0077
    ChrTalk(
        0x106,
        (
            "#12P#10703F看来我们一定要\x01",
            "成功控制那里啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3881")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38C3")

    #C0078
    ChrTalk(
        0x105,
        "#12P#10401F屏蔽信号的终端是在三十层吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3944")

    label("loc_38C3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3906")

    #C0079
    ChrTalk(
        0x106,
        "#12P#10701F屏蔽信号的终端是在三十层吧？ \x02",
    )

    CloseMessageWindow()
    Jump("loc_3944")

    label("loc_3906")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3944")

    #C0080
    ChrTalk(
        0x109,
        "#12P#10101F屏蔽信号的终端是在三十层吧？ \x02",
    )

    CloseMessageWindow()

    label("loc_3944")


    #C0081
    ChrTalk(
        0x103,
        (
            "#00203F#5P是的，就是这个\x01",
            "中枢区域的最上层。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x104,
        (
            "#6P#00300F也就是说，\x01",
            "我们只要一直往上走就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        "#00013F#11P嗯……大家拿出干劲吧！\x02",
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

    # Function_9_358B end

    def Function_10_3A17(): pass

    label("Function_10_3A17")

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

    def lambda_3B5B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B5B)
    Sleep(50)

    def lambda_3B6B():
        TurnDirection(0xF4, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_3B6B)
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
            "#00013F喂喂？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "太、太好了……\x01",
            "你们没事啊！\x02\x03",

            "这里是『梅尔卡瓦九号机』！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C88")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0086
    AnonymousTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10102F芙兰……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3CB1")

    label("loc_3C88")

    SetMessageWindowPos(50, 30, -1, -1)

    #A0087
    AnonymousTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00102F芙兰小姐……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3CB1")

    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("阿巴斯的声音")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "你们已经冲进兰花塔了吧？\x01",
            "情况如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D6B")
    SetMessageWindowPos(90, 130, -1, -1)

    #A0089
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F嗯，就快到终点了。\x02",
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
            "#10400F我来简单说明一下状况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3DAD")

    label("loc_3D6B")

    SetMessageWindowPos(90, 130, -1, -1)

    #A0091
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F嗯，就快到终点了，\x01",
            "我来说明一下状况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3DAD")

    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将当前的状况\x01",
            "传达给了梅尔卡瓦的人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("阿巴斯的声音")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "原来如此……\x01",
            "确实临近终点了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "顶层的白色智能兵器似乎\x01",
            "在方圆１００亚矩的\x01",
            "范围内张设了『结界』。\x02\x03",

            "我们无法靠近它，\x01",
            "所以就不要期待增援了。\x02",
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
            "#00013F是吗……明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F30")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0096
    AnonymousTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#10406F呼，看来只好由我们自己\x01",
            "想办法解决了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3F6E")

    label("loc_3F30")

    SetMessageWindowPos(50, 30, -1, -1)

    #A0097
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00306F呼，看来也只能\x01",
            "靠我们自己来解决了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3F6E")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("芙兰的声音")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "顺便一说……其它两架\x01",
            "智能兵器好像已经停止了活动。\x02\x03",

            "这应该是凯文神父和\x01",
            "艾丝蒂尔他们的功劳。\x02",
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
            "#00005F是吗……\x02",
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
            "#00204F……真是捷报。\x02",
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
            "#00300F嗯……\x01",
            "竟然赢了，真了不起啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("格蕾丝的声音")

    #A0102
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "总之！\x01",
            "大家一定要量力而行！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 80, -1, -1)
    SetChrName("麦克道尔议长的声音")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "愿女神保佑各位……\x01",
            "请务必小心。\x02",
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
            "#00100F是……！\x02",
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
            "#00000F明白……！\x02",
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

    # Function_10_3A17 end

    def Function_11_41BF(): pass

    label("Function_11_41BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41F7")
    OP_82(0x0, 0x5, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0xA, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_11_41BF")

    label("loc_41F7")

    Return()

    # Function_11_41BF end

    SaveToFile()

Try(main)
