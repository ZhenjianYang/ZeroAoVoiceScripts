from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r3110.bin",                # FileName
        "r3110",                    # MapName
        "r3110",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x17,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 102, 0, 1, 0, 2],
    )

    BuildStringList((
        "r3110",                  # 0
        "刘",                     # 1
    ))

    AddCharChip((
        "chr/ch31400.itc",                   # 00
    ))

    DeclNpc(8170,    0,       25590,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)

    DeclActor(5620,    0,       -22000,  1200,    5080,    -500,    -17360,  0x007C, 0,  10, 0x0000)
    DeclActor(9050,    0,       25630,   1000,    8590,    1500,    25370,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_1D8",          # 01, 1
        "Function_2_204",          # 02, 2
        "Function_3_292",          # 03, 3
        "Function_4_2B8",          # 04, 4
        "Function_5_4A1",          # 05, 5
        "Function_6_53C",          # 06, 6
        "Function_7_77C",          # 07, 7
        "Function_8_B67",          # 08, 8
        "Function_9_C25",          # 09, 9
        "Function_10_CD8",         # 0A, 10
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_160"),
        (1, "loc_16C"),
        (2, "loc_178"),
        (3, "loc_184"),
        (4, "loc_190"),
        (5, "loc_19C"),
        (6, "loc_1A8"),
        (SWITCH_DEFAULT, "loc_1B4"),
    )


    label("loc_160")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_16C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_178")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_184")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_190")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_19C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C0")

    label("loc_1D7")

    Return()

    # Function_0_128 end

    def Function_1_1D8(): pass

    label("Function_1_1D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_1F4")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1F4")
    ClearChrFlags(0x8, 0x80)

    label("loc_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_203")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)

    label("loc_203")

    Return()

    # Function_1_1D8 end

    def Function_2_204(): pass

    label("Function_2_204")

    ClearMapObjFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_21C")
    OP_66(0x1, 0x1)
    Jump("loc_241")

    label("loc_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_23D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_238")
    OP_65(0x1, 0x1)
    ClearChrFlags(0x8, 0x80)

    label("loc_238")

    Jump("loc_241")

    label("loc_23D")

    OP_66(0x1, 0x1)

    label("loc_241")

    Sound(127, 1, 100, 0)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 5080, -500, -17360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_2_204 end

    def Function_3_292(): pass

    label("Function_3_292")

    TalkBegin(0xFF)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门牢固地关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_3_292 end

    def Function_4_2B8(): pass

    label("Function_4_2B8")

    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DF")
    TurnDirection(0xFE, 0x101, 0)

    label("loc_2DF")


    #C0002
    ChrTalk(
        0x101,
        "#00005F你是黑月的……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "……辛苦了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 5)

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A")
    Call(0, 5)
    Jump("loc_3AB")

    label("loc_32A")


    #C0004
    ChrTalk(
        0xFE,
        (
            "……曹先生要制订\x01",
            "对抗『赤色星座』的对策，\x01",
            "在接下来的一段时间内恐怕无法和各位见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "将『结界』解除之后\x01",
            "再和我们联络吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB")

    Jump("loc_49D")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3FD")

    #C0006
    ChrTalk(
        0xFE,
        (
            "曹先生正在\x01",
            "隐蔽之处操劳。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "请你们以后有机会时再来吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49D")

    label("loc_3FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_49D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_418")
    Call(0, 5)
    Jump("loc_49D")

    label("loc_418")


    #C0008
    ChrTalk(
        0xFE,
        (
            "如果情况有了什么进展，\x01",
            "还请各位再度来此拜访。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "如果你们来的时候，\x01",
            "曹先生刚好有空，\x01",
            "我就会再次给各位带路。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "……请慢走。\x02",
    )

    CloseMessageWindow()

    label("loc_49D")

    TalkEnd(0xFE)
    Return()

    # Function_4_2B8 end

    def Function_5_4A1(): pass

    label("Function_5_4A1")


    #C0011
    ChrTalk(
        0xFE,
        (
            "曹先生就在里面，\x01",
            "现在可以与各位见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "……各位要去见他吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "与曹会面\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_52E"),
        (1, "loc_536"),
        (SWITCH_DEFAULT, "loc_53B"),
    )


    label("loc_52E")

    Call(0, 6)
    Jump("loc_53B")

    label("loc_536")

    Jump("loc_53B")

    label("loc_53B")

    Return()

    # Function_5_4A1 end

    def Function_6_53C(): pass

    label("Function_6_53C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x10E, 0x0)
    ClearChrFlags(0x8, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(7430, 600, 26010, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23040, 0)
    Call(0, 8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5A3")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_5A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5BC")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_5BC")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5EA")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_60E")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_60E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_632")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_632")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_656")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_656")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67A")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_67A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69E")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_69E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C2")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E6")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E6")

    FadeToBright(250, 0)
    OP_0D()
    Sleep(500)

    #C0013
    ChrTalk(
        0xFE,
        (
            "……明白了，\x01",
            "请各位跟我来。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "我带你们\x01",
            "去见曹先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(500)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    Sleep(700)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(127, 1000, 30)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e4700", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_6_53C end

    def Function_7_77C(): pass

    label("Function_7_77C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(7430, 600, 26010, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23040, 0)
    Call(0, 8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7DB")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_7DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_7F4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_822")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_822")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_846")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_846")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86A")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_86A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_88E")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_88E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8B2")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D6")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FA")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_91E")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91E")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CB")

    #C0015
    ChrTalk(
        0x8,
        (
            "#11P如果情况有了什么进展，\x01",
            "还请各位再度来此拜访。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#11P如果你们来的时候，\x01",
            "曹先生刚好有空，\x01",
            "我就会再次给各位带路。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "#11P……请慢走。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA9")

    label("loc_9CB")


    #C0018
    ChrTalk(
        0x8,
        (
            "#11P……曹先生要制订\x01",
            "对抗『赤色星座』的对策，\x01",
            "在接下来的一段时间内恐怕无法和各位见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#11P将『结界』解除之后\x01",
            "再和我们联络吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F#6P明白了。\x02\x03",

            "#00001F……你们也要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#11P……嗯，请各位慢走。\x02",
    )

    CloseMessageWindow()

    label("loc_AA9")

    OP_93(0x8, 0x5A, 0x1F4)
    SetChrFlags(0x8, 0x40)
    Sleep(500)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)

    def lambda_AD6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AD6)
    Sleep(500)

    def lambda_AEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AEE)
    Sleep(1000)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)
    Sleep(500)
    SetChrPos(0x0, 6680, 0, 25520, 89)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B44")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_B44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_B5D")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_B5D")

    SetScenarioFlags(0x0, 0)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_7_77C end

    def Function_8_B67(): pass

    label("Function_8_B67")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B87")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B9C")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BB1")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BC6")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BDB")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BF0")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C05")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C05")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C1A")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C1A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_8_B67 end

    def Function_9_C25(): pass

    label("Function_9_C25")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_C53"),
        (1, "loc_C69"),
        (2, "loc_C7F"),
        (3, "loc_C95"),
        (4, "loc_CAB"),
        (5, "loc_CC1"),
        (SWITCH_DEFAULT, "loc_CD7"),
    )


    label("loc_C53")

    SetChrPos(0xFE, 6190, 0, 25480, 89)
    Jump("loc_CD7")

    label("loc_C69")

    SetChrPos(0xFE, 6530, 0, 26710, 135)
    Jump("loc_CD7")

    label("loc_C7F")

    SetChrPos(0xFE, 5760, 0, 24300, 89)
    Jump("loc_CD7")

    label("loc_C95")

    SetChrPos(0xFE, 4670, 0, 25670, 89)
    Jump("loc_CD7")

    label("loc_CAB")

    SetChrPos(0xFE, 5510, 0, 27070, 135)
    Jump("loc_CD7")

    label("loc_CC1")

    SetChrPos(0xFE, 4440, 0, 24100, 89)
    Jump("loc_CD7")

    label("loc_CD7")

    Return()

    # Function_9_C25 end

    def Function_10_CD8(): pass

    label("Function_10_CD8")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0022
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(4120, 1000, -18910, 1500)
    MoveCamera(45, 34, 0, 1500)
    OP_6E(400, 1500)
    SetCameraDistance(30000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9B")
    OP_E2(0x2)
    MiniGame(0x6, 0x1C, 0x15F4, 0x0, 0xFFFFAA10, 0x0, 0x13D8, 0xFFFFFE0C, 0xFFFFBC30)

    label("loc_D9B")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_CD8 end

    SaveToFile()

Try(main)
