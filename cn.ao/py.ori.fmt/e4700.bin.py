from ScenarioHelper import *

def main():
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
        "刘",                     # 1
        "曹",                     # 2
        "相机",                   # 3
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
        "Function_10_1784",        # 0A, 10
        "Function_11_2206",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B8C")

    #C0001
    ChrTalk(
        0x9,
        (
            "#5P#03200F呵呵，你们来了啊。\x02\x03",

            "#03204F兰迪先生，诺艾尔小姐，\x01",
            "我们也很久不见了。\x02\x03",

            "#03209F虽然经历了无数波折，\x01",
            "但你们总算是顺利会合了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#12P#00306F呼，听说和你结成协作关系时，\x01",
            "我真是吃了一惊……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x109,
        (
            "#12P#10100F曹先生似乎还是\x01",
            "老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#12P#00001F你们好像……一直潜藏在这\x01",
            "『太阳堡垒』的内部吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_CC9")

    #C0005
    ChrTalk(
        0x9,
        (
            "#5P#03200F呵呵，你们来了啊。\x02\x03",

            "#03204F兰迪先生，我们也好久不见了。\x02\x03",

            "#03209F听说你之前一直\x01",
            "在努力组织反抗战斗。\x01",
            "看起来，你似乎没什么变化呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#12P#00306F呼，听说和你结成协作关系时，\x01",
            "我真是吃了一惊……\x02\x03",

            "#00301F你好像也还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#12P#00001F你们好像……一直潜藏在这\x01",
            "『太阳堡垒』的内部吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DBA")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_DBA")

    #C0008
    ChrTalk(
        0x9,
        (
            "#5P#03200F呵呵，你们来了啊。\x02\x03",

            "#03209F罗伊德警官，莫非你已经\x01",
            "决定要加入我们『黑月』了吗？\x02",
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
            "#12P#00006F不、不不……并不是为此而来的。\x02\x03",

            "#00001F话说回来……你们好像一直潜藏在这\x01",
            "『太阳堡垒』的内部吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DBA")


    #C0010
    ChrTalk(
        0x9,
        (
            "#5P#03204F嗯，『教团』曾经使用的\x01",
            "设施都还留在原处，\x01",
            "这里真是个适合藏身的好地方。\x02\x03",

            "#03200F而且无论是国防军\x01",
            "还是『赤色星座』，\x01",
            "都无法轻易闯进来。\x02\x03",

            "因为他们都没有发现\x01",
            "各位刚才通行的暗道。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x105,
        (
            "#12P#10404F呵呵，的确是条隐秘的通路呢。\x02\x03",

            "#10402F另外，这位先生刚才\x01",
            "带我们进来的时候，\x01",
            "似乎故意东走西绕。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#12P#00203F是啊……恐怕是不希望\x01",
            "我们以后擅自进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "……原来各位察觉到了啊。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#5P#03204F呵呵，请不要介意。\x01",
            "另外，请务必不要把此处的信息泄漏给他人。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x106,
        (
            "#12P#10701F……也就是说，黑月的各位\x01",
            "要暂时留在这个地方？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#5P#03200F嗯，我们准备在这里静观其变，\x01",
            "等待时机的到来。\x02\x03",

            "#03203F在笼罩着克洛斯贝尔市的\x01",
            "结界消除之前，\x01",
            "我们也无法做出什么行动。\x02\x03",

            "#03200F与国防军或『赤色星座』\x01",
            "正面冲突，实在是有些\x01",
            "棘手呢。\x02\x03",

            "#03206F呼，但如果『银』大人没有离开，\x01",
            "终究还是有一些可行的办法。\x02",
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
            "#12P#10404F呵呵，反正不会是\x01",
            "什么光明正大的办法呢。\x02\x03",

            "#10402F想必是那种会彻底玷污她的双手，\x01",
            "极其血腥残暴的做法吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "#5P#03210F嗯，这个嘛……\x01",
            "就任由你们随意想象吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00001F……莉夏已经是我们的人了，\x01",
            "我们绝不会让她\x01",
            "参与那种事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x106,
        "#12P#10705F罗伊德警官……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#12P#00203F是啊……\x02\x03",

            "#00200F如果玷污了莉夏小姐的双手，\x01",
            "就算能将这起事情解决，\x01",
            "琪雅也一定会很伤心的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1354")

    #C0023
    ChrTalk(
        0x104,
        (
            "#12P#00306F而且，就算采用强硬手段，\x01",
            "也未必就能照计划顺利达到目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        (
            "#12P#10103F是啊……\x01",
            "毕竟对手掌握着琪雅那种\x01",
            "可以创造『奇迹』的力量。\x02\x03",

            "#10101F总之，在这种情况下，\x01",
            "我们也只能努力思考\x01",
            "一些其它的战术了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_1354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1420")

    #C0025
    ChrTalk(
        0x107,
        (
            "#12P#01200F#3C而且，就算采取强硬手段，\x01",
            "也未必就能照计划顺利达到目的。\x02\x03",

            "毕竟对手掌握着圣子那种\x01",
            "可以创造『奇迹』的力量。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#12P#00303F总之，在这种情况下，\x01",
            "我们也只能想点其它的办法了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DD")

    label("loc_1420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_14DD")

    #C0027
    ChrTalk(
        0x107,
        (
            "#12P#01200F#3C而且，就算采取强硬手段，\x01",
            "也未必就能照计划顺利达到目的。\x02\x03",

            "毕竟对手掌握着圣子那种\x01",
            "可以创造『奇迹』的力量。\x02\x03",

            "#01203F在这种情况下，我们也只能\x01",
            "努力摸索其它的方法了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DD")


    #C0028
    ChrTalk(
        0x9,
        (
            "#5P#03203F……嗯，我明白。\x01",
            "既然手中没有用来实行计划的棋子，\x01",
            "也没有理由固执于此。\x02\x03",

            "#03200F要想打破如今这种状况，\x01",
            "也只能依靠\x01",
            "你们各位了。\x02\x03",

            "#03204F请大家多多采取行动，\x01",
            "尽力扰乱总统一党吧，\x01",
            "这也算是帮了我们的忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#12P#00001F嗯，交给我们吧。\x02\x03",

            "#00003F在形势需要时，\x01",
            "也请你们提供援助。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x106,
        "#12P#10703F……请各位多加小心。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#5P#03209F呵呵，没想到能从\x01",
            "『银』大人的口中听到这种话。\x02\x03",

            "#03204F……好，那我就此\x01",
            "失陪了。\x02\x03",

            "#03200F刘，把他们带回\x01",
            "原来的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0032
    ChrTalk(
        0x8,
        "是。\x02",
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
            "在罗伊德等人辞别时，曹将\x07\x02\x01",

            "#14I爆灵宝玉\x07\x05",
            "赠给大家。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('爆灵宝玉', 1)
    SetScenarioFlags(0x1BE, 6)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1755")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_1755")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_176E")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_176E")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_7F6 end

    def Function_10_1784(): pass

    label("Function_10_1784")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_17F6")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_17F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_180F")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_180F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_183D")
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_183D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1861")
    BeginChrThread(0x102, 1, 0, 11)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1861")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1885")
    BeginChrThread(0x103, 1, 0, 11)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1885")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18A9")
    BeginChrThread(0x104, 1, 0, 11)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_18A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18CD")
    BeginChrThread(0x105, 1, 0, 11)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_18CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18F1")
    BeginChrThread(0x106, 1, 0, 11)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_18F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1915")
    BeginChrThread(0x109, 1, 0, 11)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1915")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1939")
    BeginChrThread(0x107, 1, 0, 11)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_1939")

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
            "#5P#03204F真不愧是特别任务支援科的各位啊。\x02\x03",

            "居然联合麦克道尔议长，\x01",
            "成功发表了克洛斯贝尔独立\x01",
            "无效宣言……\x02\x03",

            "#03210F连我都没料到能发生\x01",
            "如此痛快的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，在很多人的协助下，\x01",
            "总算取得了\x01",
            "如今的进展。\x02\x03",

            "#00001F现在也已经知道该如何消除\x01",
            "笼罩在克洛斯贝尔市的『结界』了……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#12P#00100F接下来，只要能将『结界』消除，\x01",
            "我们就可以突入\x01",
            "琪雅所在的克洛斯贝尔市了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "#5P#03204F呵呵，虽然进展缓慢，\x01",
            "但事态确实有所好转呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BD6")

    #C0038
    ChrTalk(
        0x106,
        (
            "#12P#10701F话说回来……\x01",
            "『黑月』的潜伏状况如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1C")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C1C")

    #C0039
    ChrTalk(
        0x105,
        (
            "#12P#10402F话说回来……\x01",
            "你们最近的潜伏状况如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1C")


    #C0040
    ChrTalk(
        0x9,
        (
            "#5P#03200F哦，搜寻我们的\x01",
            "『赤色星座』部队已经\x01",
            "暂时撤退休整。\x02\x03",

            "#03204F之前一直在郊外巡逻的国防军士兵\x01",
            "似乎也都返回部队了。\x02\x03",

            "#03200F从这种状况来看，\x01",
            "玛因兹地区的反抗军\x01",
            "也可以逃过一劫了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D52")

    #C0041
    ChrTalk(
        0x109,
        (
            "#12P#10103F本来一直都很担心\x01",
            "米蕾优三尉他们……\x02\x03",

            "#10102F但现在至少可以\x01",
            "暂时安心了呢，兰迪前辈！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC0")

    label("loc_1D52")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DC0")

    #C0042
    ChrTalk(
        0x105,
        (
            "#12P#10404F看来米蕾优小姐他们\x01",
            "暂时不会有事了。\x02\x03",

            "#10402F呵呵，兰迪，\x01",
            "你总算可以安心了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC0")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x104)

    #C0043
    ChrTalk(
        0x104,
        (
            "#12P#00303F不……现在还不能安心。\x02\x03",

            "#00301F国防军倒也罢了，\x01",
            "但叔叔他们恐怕并不会\x01",
            "在意什么无效宣言。\x02\x03",

            "他们暂时撤退，也许只是\x01",
            "为了做好万全的战斗准备……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#5P#03204F嗯，那种可能性也很高。\x02\x03",

            "#03201F他们发动比玛因兹那一次\x01",
            "更加彻底的围剿行动，\x01",
            "大概也只是时间问题而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#12P#00010F这……！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#12P#00208F看来如今的状况还是很紧张，\x01",
            "仍然不容有丝毫松懈呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "#5P#03206F总之，期待各位\x01",
            "尽早将那个『结界』\x01",
            "消除。\x02\x03",

            "#03200F只要能做到这一点，\x01",
            "我们就可以由守转攻，\x01",
            "摆脱这种一面倒的被动战局了。\x02\x03",

            "#03204F等到『结界』消除之后，\x01",
            "我们也会在解放克洛斯贝尔市的\x01",
            "作战行动中提供援助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00003F……明白了。\x02\x03",

            "要想攻破『结社』的防线，\x01",
            "将结界消除，\x01",
            "自然没那么容易……\x02\x03",

            "#00000F但为了你们\x01",
            "和反抗军的各位，\x01",
            "我们必须要成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#12P#00100F嗯……加油吧！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#5P#03204F呵呵，真可靠啊。\x02\x03",

            "#03200F……好，那我就此\x01",
            "失陪了。\x02\x03",

            "#03204F刘，把他们带回\x01",
            "原来的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0051
    ChrTalk(
        0x8,
        "是。\x02",
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
            "在罗伊德等人辞别时，曹将\x07\x02\x01",

            "#14I还魂粉\x07\x05",
            "赠给大家。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('还魂粉', 1)
    SetScenarioFlags(0x1BE, 7)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21D7")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_21D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21F0")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_21F0")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("r3110", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1784 end

    def Function_11_2206(): pass

    label("Function_11_2206")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_2234"),
        (1, "loc_224A"),
        (2, "loc_2260"),
        (3, "loc_2276"),
        (4, "loc_228C"),
        (5, "loc_22A2"),
        (SWITCH_DEFAULT, "loc_22B8"),
    )


    label("loc_2234")

    SetChrPos(0xFE, -8720, 6000, -3540, 0)
    Jump("loc_22B8")

    label("loc_224A")

    SetChrPos(0xFE, -7650, 6000, -3710, 0)
    Jump("loc_22B8")

    label("loc_2260")

    SetChrPos(0xFE, -9860, 6000, -4019, 0)
    Jump("loc_22B8")

    label("loc_2276")

    SetChrPos(0xFE, -6540, 6000, -3770, 0)
    Jump("loc_22B8")

    label("loc_228C")

    SetChrPos(0xFE, -8820, 6000, -5420, 0)
    Jump("loc_22B8")

    label("loc_22A2")

    SetChrPos(0xFE, -7260, 6000, -5220, 0)
    Jump("loc_22B8")

    label("loc_22B8")

    Return()

    # Function_11_2206 end

    SaveToFile()

Try(main)
