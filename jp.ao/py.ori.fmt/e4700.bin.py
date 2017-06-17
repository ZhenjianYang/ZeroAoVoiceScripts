from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4700.bin",                # FileName
        "e4700",                    # MapName
        "e4700",                    # Location
        0x0000,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -8840, 6000, 2420, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4700",                  # 0
        "ラウ",                   # 1
        "ツァオ",                 # 2
        "カメラ",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(280, 0)                                        # 0

    ScpFunction((
        "Function_0_118",          # 00, 0
        "Function_1_17C",          # 01, 1
        "Function_2_17D",          # 02, 2
        "Function_3_545",          # 03, 3
        "Function_4_603",          # 04, 4
        "Function_5_6B6",          # 05, 5
        "Function_6_702",          # 06, 6
        "Function_7_75A",          # 07, 7
        "Function_8_7A8",          # 08, 8
        "Function_9_7F6",          # 09, 9
        "Function_10_1980",        # 0A, 10
        "Function_11_2598",        # 0B, 11
    ))


    def Function_0_118(): pass

    label("Function_0_118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146")
    Event(0, 2)
    Jump("loc_17B")

    label("loc_146")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A")
    Event(0, 10)
    Jump("loc_17B")

    label("loc_16A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B")
    Event(0, 9)

    label("loc_17B")

    Return()

    # Function_0_118 end

    def Function_1_17C(): pass

    label("Function_1_17C")

    Return()

    # Function_1_17C end

    def Function_2_17D(): pass

    label("Function_2_17D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetCameraDistance(24440, 0)
    Call(0, 3)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BD")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D6")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1D6")

    OP_68(497800, -20000, 13130, 0)
    SetChrPos(0x8, 498100, -21000, 11910, 180)
    SetChrPos(0xA, 498100, -21000, 14500, 180)
    OP_6B(0xA)
    BeginChrThread(0x8, 1, 0, 6)
    BeginChrThread(0xA, 1, 0, 5)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_270")
    BeginChrThread(0x101, 1, 0, 4)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_26A")
    BeginChrThread(0x101, 1, 0, 8)
    Jump("loc_270")

    label("loc_26A")

    BeginChrThread(0x101, 1, 0, 7)

    label("loc_270")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B4")
    BeginChrThread(0x102, 1, 0, 4)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2AE")
    BeginChrThread(0x102, 1, 0, 8)
    Jump("loc_2B4")

    label("loc_2AE")

    BeginChrThread(0x102, 1, 0, 7)

    label("loc_2B4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F8")
    BeginChrThread(0x103, 1, 0, 4)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2F2")
    BeginChrThread(0x103, 1, 0, 8)
    Jump("loc_2F8")

    label("loc_2F2")

    BeginChrThread(0x103, 1, 0, 7)

    label("loc_2F8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33C")
    BeginChrThread(0x104, 1, 0, 4)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_336")
    BeginChrThread(0x104, 1, 0, 8)
    Jump("loc_33C")

    label("loc_336")

    BeginChrThread(0x104, 1, 0, 7)

    label("loc_33C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_380")
    BeginChrThread(0x105, 1, 0, 4)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_37A")
    BeginChrThread(0x105, 1, 0, 8)
    Jump("loc_380")

    label("loc_37A")

    BeginChrThread(0x105, 1, 0, 7)

    label("loc_380")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C4")
    BeginChrThread(0x106, 1, 0, 4)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3BE")
    BeginChrThread(0x106, 1, 0, 8)
    Jump("loc_3C4")

    label("loc_3BE")

    BeginChrThread(0x106, 1, 0, 7)

    label("loc_3C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_408")
    BeginChrThread(0x109, 1, 0, 4)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_402")
    BeginChrThread(0x109, 1, 0, 8)
    Jump("loc_408")

    label("loc_402")

    BeginChrThread(0x109, 1, 0, 7)

    label("loc_408")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44C")
    BeginChrThread(0x107, 1, 0, 4)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_446")
    BeginChrThread(0x107, 1, 0, 8)
    Jump("loc_44C")

    label("loc_446")

    BeginChrThread(0x107, 1, 0, 7)

    label("loc_44C")

    FadeToBright(2000, 0)
    OP_0D()

    label("loc_456")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_475")
    Jump("loc_47D")

    label("loc_475")

    Sleep(50)
    Jump("loc_456")

    label("loc_47D")

    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49F")
    EndChrThread(0x0, 0x1)

    label("loc_49F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4B2")
    EndChrThread(0x1, 0x1)

    label("loc_4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4C5")
    EndChrThread(0x2, 0x1)

    label("loc_4C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4D8")
    EndChrThread(0x3, 0x1)

    label("loc_4D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4EB")
    EndChrThread(0x4, 0x1)

    label("loc_4EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4FE")
    EndChrThread(0x5, 0x1)

    label("loc_4FE")

    OP_6B(0xFF)
    SetChrFlags(0x8, 0x80)
    OP_49()
    OP_D7(0x1E)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_522")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_522")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_53B")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_53B")

    NewScene("e4700", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_2_17D end

    def Function_3_545(): pass

    label("Function_3_545")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_565")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57A")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_58F")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_58F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A4")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5B9")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5CE")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E3")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5F8")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5F8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_3_545 end

    def Function_4_603(): pass

    label("Function_4_603")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_631"),
        (1, "loc_647"),
        (2, "loc_65D"),
        (3, "loc_673"),
        (4, "loc_689"),
        (5, "loc_69F"),
        (SWITCH_DEFAULT, "loc_6B5"),
    )


    label("loc_631")

    SetChrPos(0xFE, 497600, -21000, 14530, 180)
    Jump("loc_6B5")

    label("loc_647")

    SetChrPos(0xFE, 499000, -21000, 15240, 180)
    Jump("loc_6B5")

    label("loc_65D")

    SetChrPos(0xFE, 497600, -21000, 16120, 180)
    Jump("loc_6B5")

    label("loc_673")

    SetChrPos(0xFE, 499000, -21000, 16740, 180)
    Jump("loc_6B5")

    label("loc_689")

    SetChrPos(0xFE, 497600, -21000, 17990, 180)
    Jump("loc_6B5")

    label("loc_69F")

    SetChrPos(0xFE, 499000, -21000, 18390, 180)
    Jump("loc_6B5")

    label("loc_6B5")

    Return()

    # Function_4_603 end

    def Function_5_6B6(): pass

    label("Function_5_6B6")

    OP_95(0xFE, 498180, -21000, 3500, 2000, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 498180, -21000, 3500)
    OP_9F(0x1, 497180, -21000, 2500)
    OP_9F(0x1, 495180, -21000, 1500)
    OP_9F(0x2, 0xFE, 1000, 0x0)
    Return()

    # Function_5_6B6 end

    def Function_6_702(): pass

    label("Function_6_702")

    OP_95(0xFE, 498180, -21000, -230, 2000, 0x1)
    OP_95(0xFE, 495000, -21000, -230, 2000, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_739():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_739)
    OP_95(0xFE, 489890, -21000, -230, 2000, 0x0)
    Return()

    # Function_6_702 end

    def Function_7_75A(): pass

    label("Function_7_75A")

    OP_95(0xFE, 499000, -21000, -430, 2000, 0x0)
    OP_95(0xFE, 495000, -21000, -430, 2000, 0x1)

    def lambda_787():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_787)
    OP_95(0xFE, 489890, -21000, -430, 2000, 0x0)
    Return()

    # Function_7_75A end

    def Function_8_7A8(): pass

    label("Function_8_7A8")

    OP_95(0xFE, 497600, -21000, 0, 2000, 0x1)
    OP_95(0xFE, 495000, -21000, 0, 2000, 0x1)

    def lambda_7D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7D5)
    OP_95(0xFE, 489890, -21000, 0, 2000, 0x0)
    Return()

    # Function_8_7A8 end

    def Function_9_7F6(): pass

    label("Function_9_7F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 3)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x1F)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7900, 6000, -670, 180)
    SetChrPos(0x8, -9100, 6000, 210, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_868")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_868")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_881")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_881")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D3")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F7")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91B")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93F")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_963")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_987")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_987")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AB")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AB")

    OP_68(-20060, 6200, -53820, 0)
    MoveCamera(58, 11, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(16700, 0)
    FadeToBright(2000, 0)
    OP_68(-12270, 8000, -29610, 7000)
    MoveCamera(31, 13, 0, 7000)
    OP_6E(520, 7000)
    SetCameraDistance(20250, 7000)
    Sleep(7600)
    Fade(500)
    OP_68(-13990, 8800, -7980, 0)
    MoveCamera(46, 9, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(10780, 0)
    OP_0D()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_BBE")

    #C0001
    ChrTalk(
        0x9,
        (
            "#5P#03200Fフフ、よくおいでくださいました。\x02\x03",

            "#03204Fランディさんと\x01",
            "ノエルさんもお久しぶりです。\x02\x03",

            "#03209F紆余曲折あったようですが、\x01",
            "無事に合流できてなによりですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#12P#00306Fやれやれ、協力関係になったと\x01",
            "聞いた時は驚いたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x109,
        (
            "#12P#10100Fツァオさんも\x01",
            "相変わらずみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00001Fそれに……《太陽の砦》の内部に\x01",
            "潜んでいたんですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_BBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_D1F")

    #C0005
    ChrTalk(
        0x9,
        (
            "#5P#03200Fフフ、よくおいでくださいました。\x02\x03",

            "#03204Fランディさんもお久しぶりです。\x02\x03",

            "#03209Fレジスタンス活動に\x01",
            "勤しんでいたそうですが、\x01",
            "お変わりはありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#12P#00306Fやれやれ、協力関係になったと\x01",
            "聞いた時は驚いたが……\x02\x03",

            "#00301Fあんたも相変わらずみてえだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#12P#00001Fそれに……《太陽の砦》の内部に\x01",
            "潜んでいたんですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E20")

    label("loc_D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E20")

    #C0008
    ChrTalk(
        0x9,
        (
            "#5P#03200Fフフ、よくおいでくださいました。\x02\x03",

            "#03209Fロイドさん、やはり《黒月》に\x01",
            "来て頂ける気になりましたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x101,
        (
            "#12P#00006Fい、いや……そういうわけでは。\x02\x03",

            "#00001Fというか、《太陽の砦》の内部に\x01",
            "潜んでいたんですね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")


    #C0010
    ChrTalk(
        0x9,
        (
            "#5P#03204Fええ、『教団』の使っていた\x01",
            "施設もありますし、\x01",
            "潜伏には色々と好都合でして。\x02\x03",

            "#03200Fそれにここなら、国防軍や\x01",
            "《赤い星座》と言えども容易には\x01",
            "入り込むことはできないでしょう。\x02\x03",

            "皆さんが通ってきた隠し通路も、\x01",
            "存在には気づかれていませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x105,
        (
            "#12P#10404Fフフ、確かに。\x02\x03",

            "#10402Fそこの彼に案内された道も\x01",
            "かなり複雑なルートを\x01",
            "使ってたみたいだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#12P#00203Fそうですね……わたしたちだけで\x01",
            "もう一度ここに来れる気はしません。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "……気づいていましたか。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#5P#03204Fフフ、それは結構。\x01",
            "くれぐれも他言は無用に願いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x106,
        (
            "#12P#10701F……黒月の皆さんは、\x01",
            "しばらくはこの場所に？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#5P#03200Fええ、ここで動向を眺めながら\x01",
            "機を待つつもりでいます。\x02\x03",

            "#03203Fクロスベル市の結界……\x01",
            "あれをどうにかしない限りは\x01",
            "こちらも動くに動けません。\x02\x03",

            "#03200F国防軍や《赤い星座》を\x01",
            "正面から相手にするのも\x01",
            "いささか骨が折れますからね。\x02\x03",

            "#03206Fまあ、《銀》殿が手元にいれば\x01",
            "こちらにも方法があったのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x106,
        "#12P#10703F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        (
            "#12P#10404Fフフ、どうせ\x01",
            "ロクな方法じゃないんだろうけど。\x02\x03",

            "#10402F彼女の手が徹底的に汚れるような、\x01",
            "強引で血生臭いやり方なんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "#5P#03210Fさて、どうでしょう……\x01",
            "ご想像にお任せしますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00001F……こちらに引き取った以上、\x01",
            "リーシャには絶対に\x01",
            "そんなことはさせません。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x106,
        "#12P#10705Fロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#12P#00203Fそうですね……\x02\x03",

            "#00200Fリーシャさんの手を汚して\x01",
            "この事件を解決しても、\x01",
            "キーアは悲しむと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1494")

    #C0023
    ChrTalk(
        0x104,
        (
            "#12P#00306Fま、多少強引な方法をとった所で\x01",
            "計画通りに進むとも限らねえしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        (
            "#12P#10103Fそうですね……\x01",
            "相手はキーアちゃんの《奇蹟》を\x01",
            "手中に置いているわけですし。\x02\x03",

            "#10101Fとにかく、こうなった以上は\x01",
            "別の道を探すしか\x01",
            "ないんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1655")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_157E")

    #C0025
    ChrTalk(
        0x107,
        (
            "#12P#01200F#3Cそれに、多少強引な方法をとったとて\x01",
            "計略通りに進むとも限らんだろう。\x02\x03",

            "何せ、相手は御子の《奇蹟》を\x01",
            "手中に置いているのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#12P#00303Fとにかく、こうなった以上は\x01",
            "別の道を探すしかねえだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1655")

    label("loc_157E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1655")

    #C0027
    ChrTalk(
        0x107,
        (
            "#12P#01200F#3Cそれに、多少強引な方法をとったとて\x01",
            "計略通りに進むとも限らんだろう。\x02\x03",

            "何せ、相手は御子の《奇蹟》を\x01",
            "手中に置いているのだからな。\x02\x03",

            "#01203Fこうなった以上、別の道を\x01",
            "模索していくしかあるまい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1655")


    #C0028
    ChrTalk(
        0x9,
        (
            "#5P#03203F……ええ、分かっています。\x01",
            "実行する駒が手元にない今、\x01",
            "それに固執する理由もありませんし。\x02\x03",

            "#03200Fこの状況を打破するためには\x01",
            "もはや貴方がたに\x01",
            "頼るしかないでしょう。\x02\x03",

            "#03204F私たちのためにも、\x01",
            "せいぜい動き回って\x01",
            "大統領側を撹乱してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#12P#00001Fええ、任せてください。\x02\x03",

            "#00003Fそちらも何かあった時は\x01",
            "協力をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x106,
        "#12P#10703F……どうか、お気をつけて。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#5P#03209Fフフ、まさか《銀》殿から\x01",
            "そのような言葉を頂けるとは。\x02\x03",

            "#03204F……それでは、私はここで\x01",
            "失礼させてもらうとします。\x02\x03",

            "#03200Fラウ、彼らを元の場所まで\x01",
            "案内してあげてください。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0032
    ChrTalk(
        0x8,
        "はっ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは帰り際、ツァオから\x07\x02\x01",

            "#14Iバーストオーブ\x07\x05",
            "を受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x20C, 1)
    SetScenarioFlags(0x1BE, 6)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1951")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1951")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_196A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_196A")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7F6 end

    def Function_10_1980(): pass

    label("Function_10_1980")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 3)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    LoadChrToIndex("chr/ch06300.itc", 0x1F)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrChipByIndex(0x9, 0x1F)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7900, 6000, -670, 180)
    SetChrPos(0x8, -9100, 6000, 210, 180)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_19F2")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_19F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1A0B")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_1A0B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A39")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A5D")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1A5D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1A81")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1A81")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA5")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AC9")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AED")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1AED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B11")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B11")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B35")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1B35")

    OP_68(-20060, 6200, -53820, 0)
    MoveCamera(58, 11, 0, 0)
    OP_6E(520, 0)
    SetCameraDistance(16700, 0)
    FadeToBright(2000, 0)
    OP_68(-12270, 8000, -29610, 7000)
    MoveCamera(31, 13, 0, 7000)
    OP_6E(520, 7000)
    SetCameraDistance(20250, 7000)
    Sleep(7600)
    Fade(500)
    OP_68(-13990, 8800, -7980, 0)
    MoveCamera(46, 9, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(10780, 0)
    OP_0D()
    Sleep(1000)

    #C0034
    ChrTalk(
        0x9,
        (
            "#5P#03204F流石は特務支援課の皆さんですね。\x02\x03",

            "まさか、マクダエル議長と共に\x01",
            "『クロスベル独立国』の\x01",
            "無効宣言を成し遂げるとは……\x02\x03",

            "#03210Fここまで痛快な出来事が起こるとは\x01",
            "私も予想だにしませんでしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#00003Fええ、沢山の人の協力で\x01",
            "なんとかここまで\x01",
            "こぎつけることができました。\x02\x03",

            "#00001Fクロスベル市を守る《結界》の\x01",
            "解除方法も分かりましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#12P#00100Fあとは《結界》さえ解除できれば、\x01",
            "キーアちゃんのいるクロスベル市に\x01",
            "進入することができるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#5P#03204Fフフ、少しずつですが\x01",
            "確かに事態は好転してきていますね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E3C")

    #C0038
    ChrTalk(
        0x106,
        (
            "#12P#10701Fところで……\x01",
            "《黒月》の潜伏状況はどうですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E8C")

    label("loc_1E3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E8C")

    #C0039
    ChrTalk(
        0x105,
        (
            "#12P#10402Fところで……\x01",
            "そちらの潜伏状況はどんな感じだい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E8C")


    #C0040
    ChrTalk(
        0x9,
        (
            "#5P#03200Fええ、我々を捜索していた\x01",
            "《赤い星座》が一旦引き上げて、\x01",
            "一息ついた所ですよ。\x02\x03",

            "#03204F街道を巡回していた国防軍も、\x01",
            "一通り部隊に戻ったようです。\x02\x03",

            "#03200Fこの様子なら、\x01",
            "マインツ方面のレジスタンスも\x01",
            "ひとまず、難を逃れたかと。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FFA")

    #C0041
    ChrTalk(
        0x109,
        (
            "#12P#10103Fミレイユ三尉たちが\x01",
            "心配でしたけど……\x02\x03",

            "#10102Fこれでとりあえず\x01",
            "一安心ですね、ランディ先輩！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_1FFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_207C")

    #C0042
    ChrTalk(
        0x105,
        (
            "#12P#10404Fミレイユさんたちも、\x01",
            "とりあえず大丈夫そうだね。\x02\x03",

            "#10402Fフフ、ランディ。\x01",
            "君も安心したんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207C")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    #C0043
    ChrTalk(
        0x104,
        (
            "#12P#00303Fいや……安心はできねえな。\x02\x03",

            "#00301F国防軍はともかく、\x01",
            "叔父貴どもは無効宣言なんて\x01",
            "気にもしちゃいねえだろう。\x02\x03",

            "恐らくは、一旦引き上げたのも\x01",
            "万全な準備を整えるため……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#5P#03204F当然、その可能性は高いでしょう。\x02\x03",

            "#03201Fマインツで行われた以上の\x01",
            "徹底的な“狩り”が始まるのは、\x01",
            "もはや時間の問題のはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#12P#00010Fっ……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#12P#00208Fまったく気が抜けない状況と\x01",
            "言ってよさそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "#5P#03206Fまあ、皆さんが《結界》を\x01",
            "早々に破ってくれることを\x01",
            "期待していますよ。\x02\x03",

            "#03200Fあれさえなくなれば、\x01",
            "守り一辺倒の戦局から\x01",
            "攻めに転じることができます。\x02\x03",

            "#03204Fそうなった時は改めて、\x01",
            "我々もクロスベル市の解放に\x01",
            "協力させていただきますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00003F……分かりました。\x02\x03",

            "《結社》の守りを切り抜けて\x01",
            "結界を解除するのは\x01",
            "容易じゃないでしょうけど……\x02\x03",

            "#00000Fツァオさんたちや\x01",
            "レジスタンスの為にも、\x01",
            "必ずやり遂げてみせます。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#12P#00100Fええ……頑張りましょう！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#5P#03204Fフフ、頼もしい限りです。\x02\x03",

            "#03200F……それでは、私はここで\x01",
            "失礼させてもらうとします。\x02\x03",

            "#03204Fラウ、彼らを元の場所まで\x01",
            "案内してあげてください。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0051
    ChrTalk(
        0x8,
        "はっ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちは帰り際、ツァオから\x07\x02\x01",

            "#14Iゼラムパウダー\x07\x05",
            "を受け取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x1FE, 1)
    SetScenarioFlags(0x1BE, 7)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2569")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2582")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_2582")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1980 end

    def Function_11_2598(): pass

    label("Function_11_2598")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_25C6"),
        (1, "loc_25DC"),
        (2, "loc_25F2"),
        (3, "loc_2608"),
        (4, "loc_261E"),
        (5, "loc_2634"),
        (SWITCH_DEFAULT, "loc_264A"),
    )


    label("loc_25C6")

    SetChrPos(0xFE, -8720, 6000, -3540, 0)
    Jump("loc_264A")

    label("loc_25DC")

    SetChrPos(0xFE, -7650, 6000, -3710, 0)
    Jump("loc_264A")

    label("loc_25F2")

    SetChrPos(0xFE, -9860, 6000, -4019, 0)
    Jump("loc_264A")

    label("loc_2608")

    SetChrPos(0xFE, -6540, 6000, -3770, 0)
    Jump("loc_264A")

    label("loc_261E")

    SetChrPos(0xFE, -8820, 6000, -5420, 0)
    Jump("loc_264A")

    label("loc_2634")

    SetChrPos(0xFE, -7260, 6000, -5220, 0)
    Jump("loc_264A")

    label("loc_264A")

    Return()

    # Function_11_2598 end

    SaveToFile()

Try(main)
