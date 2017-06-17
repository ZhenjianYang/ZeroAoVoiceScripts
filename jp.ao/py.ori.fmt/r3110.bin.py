from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ラウ",                   # 1
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
        "Function_4_2BE",          # 04, 4
        "Function_5_509",          # 05, 5
        "Function_6_5C0",          # 06, 6
        "Function_7_81C",          # 07, 7
        "Function_8_C45",          # 08, 8
        "Function_9_D03",          # 09, 9
        "Function_10_DB6",         # 0A, 10
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
            "扉は堅く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_3_292 end

    def Function_4_2BE(): pass

    label("Function_4_2BE")

    TalkBegin(0xFE)
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E5")
    TurnDirection(0xFE, 0x101, 0)

    label("loc_2E5")


    #C0002
    ChrTalk(
        0x101,
        "#00005Fあなたは黒月の……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "……お疲れ様です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 5)

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A")
    Call(0, 5)
    Jump("loc_3D3")

    label("loc_33A")


    #C0004
    ChrTalk(
        0xFE,
        (
            "……《赤い星座》への対策のため\x01",
            "ツァオ様もしばらくは、\x01",
            "面会の時間を作れないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "《結界》を解除したら、\x01",
            "改めてこちらに連絡をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D3")

    Jump("loc_505")

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_449")

    #C0006
    ChrTalk(
        0xFE,
        (
            "今、ツァオ様は隠れ処の方で\x01",
            "お忙しくしていらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "また、別の機会にお越し下さい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_505")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")
    Call(0, 5)
    Jump("loc_505")

    label("loc_464")


    #C0008
    ChrTalk(
        0xFE,
        (
            "状況が進展をみたら、\x01",
            "再度こちらを訪れてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "ツァオ様と面会が可能なときに\x01",
            "声をかけていただければ、\x01",
            "再び隠れ家へと案内します。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "……それでは。\x02",
    )

    CloseMessageWindow()

    label("loc_505")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BE end

    def Function_5_509(): pass

    label("Function_5_509")


    #C0011
    ChrTalk(
        0xFE,
        (
            "今なら、隠れ処にいるツァオ様と\x01",
            "面会する事が出来ます。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "……どうなさいますか？\x02",
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
            "ツァオに面会する\x01",      # 0
            "やめる\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B2"),
        (1, "loc_5BA"),
        (SWITCH_DEFAULT, "loc_5BF"),
    )


    label("loc_5B2")

    Call(0, 6)
    Jump("loc_5BF")

    label("loc_5BA")

    Jump("loc_5BF")

    label("loc_5BF")

    Return()

    # Function_5_509 end

    def Function_6_5C0(): pass

    label("Function_6_5C0")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_627")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_640")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_640")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66E")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_66E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_692")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_692")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B6")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DA")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6FE")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_722")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_722")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_746")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_746")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_76A")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_76A")

    FadeToBright(250, 0)
    OP_0D()
    Sleep(500)

    #C0013
    ChrTalk(
        0xFE,
        (
            "……分かりました。\x01",
            "では、こちらへ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "ツァオ様の元へと\x01",
            "案内させていただきます。\x02",
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

    # Function_6_5C0 end

    def Function_7_81C(): pass

    label("Function_7_81C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    EndChrThread(0x8, 0x0)
    OP_68(7430, 600, 26010, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23040, 0)
    Call(0, 8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_87B")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_87B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_894")
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    label("loc_894")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C2")
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8C2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E6")
    BeginChrThread(0x102, 1, 0, 9)
    WaitChrThread(0x102, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_90A")
    BeginChrThread(0x103, 1, 0, 9)
    WaitChrThread(0x103, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_92E")
    BeginChrThread(0x104, 1, 0, 9)
    WaitChrThread(0x104, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_952")
    BeginChrThread(0x105, 1, 0, 9)
    WaitChrThread(0x105, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_952")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_976")
    BeginChrThread(0x106, 1, 0, 9)
    WaitChrThread(0x106, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_976")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99A")
    BeginChrThread(0x109, 1, 0, 9)
    WaitChrThread(0x109, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BE")
    BeginChrThread(0x107, 1, 0, 9)
    WaitChrThread(0x107, 1)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BE")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A87")

    #C0015
    ChrTalk(
        0x8,
        (
            "#11P状況が進展をみたら、\x01",
            "再度こちらを訪れてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#11Pツァオ様と面会が可能なときに\x01",
            "声をかけていただければ、\x01",
            "再び隠れ家へと案内します。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "#11P……それでは。\x02",
    )

    CloseMessageWindow()
    Jump("loc_B87")

    label("loc_A87")


    #C0018
    ChrTalk(
        0x8,
        (
            "#11P……《赤い星座》への対策のため\x01",
            "ツァオ様もしばらくは、\x01",
            "面会の時間を作れないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#11P《結界》を解除したら、\x01",
            "改めてこちらに連絡をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F#6P分かりました。\x02\x03",

            "#00001F……そちらも気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#11P……それでは。\x02",
    )

    CloseMessageWindow()

    label("loc_B87")

    OP_93(0x8, 0x5A, 0x1F4)
    SetChrFlags(0x8, 0x40)
    Sleep(500)
    OP_74(0xF, 0xF)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)

    def lambda_BB4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BB4)
    Sleep(500)

    def lambda_BCC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BCC)
    Sleep(1000)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x8)
    Sound(118, 0, 100, 0)
    OP_79(0xF)
    Sleep(500)
    SetChrPos(0x0, 6680, 0, 25520, 89)
    SetChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C22")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_C22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3B")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_C3B")

    SetScenarioFlags(0x0, 0)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_7_81C end

    def Function_8_C45(): pass

    label("Function_8_C45")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C65")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C7A")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C8F")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CA4")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB9")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CCE")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE3")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CF8")
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF8")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Return()

    # Function_8_C45 end

    def Function_9_D03(): pass

    label("Function_9_D03")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_D31"),
        (1, "loc_D47"),
        (2, "loc_D5D"),
        (3, "loc_D73"),
        (4, "loc_D89"),
        (5, "loc_D9F"),
        (SWITCH_DEFAULT, "loc_DB5"),
    )


    label("loc_D31")

    SetChrPos(0xFE, 6190, 0, 25480, 89)
    Jump("loc_DB5")

    label("loc_D47")

    SetChrPos(0xFE, 6530, 0, 26710, 135)
    Jump("loc_DB5")

    label("loc_D5D")

    SetChrPos(0xFE, 5760, 0, 24300, 89)
    Jump("loc_DB5")

    label("loc_D73")

    SetChrPos(0xFE, 4670, 0, 25670, 89)
    Jump("loc_DB5")

    label("loc_D89")

    SetChrPos(0xFE, 5510, 0, 27070, 135)
    Jump("loc_DB5")

    label("loc_D9F")

    SetChrPos(0xFE, 4440, 0, 24100, 89)
    Jump("loc_DB5")

    label("loc_DB5")

    Return()

    # Function_9_D03 end

    def Function_10_DB6(): pass

    label("Function_10_DB6")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0022
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E85")
    OP_E2(0x2)
    MiniGame(0x6, 0x1C, 0x15F4, 0x0, 0xFFFFAA10, 0x0, 0x13D8, 0xFFFFFE0C, 0xFFFFBC30)

    label("loc_E85")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_DB6 end

    SaveToFile()

Try(main)
