from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4100.bin",                # FileName
        "m4100",                    # MapName
        "m4100",                    # Location
        0x00C8,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 200, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4100",                  # 0
        "bm4110",                 # 1
        "bm4110",                 # 2
        "bm4110",                 # 3
    ))

    ATBonus("ATBonus_1A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2574", 2,   7,   2,   2,   0,   3,   0)
    Sepith("Sepith_257C", 2,   3,   4,   3,   2,   0,   2)
    Sepith("Sepith_2584", 3,   0,   4,   2,   3,   4,   0)

    MonsterBattlePostion("MonsterBattlePostion_1E4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_268", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_26C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_270", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_278", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_204", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 8, 14, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_284", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_2574", 40, 30, 20, 0,
        (
            ("ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x0010, 54, 6, 45, 10, 1, 40, 0, "bm4110", "Sepith_257C", 40, 30, 20, 0,
        (
            ("ms78100.dat", "ms78100.dat", 0, 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 54, 6, 45, 10, 1, 20, 0, "bm4110", "Sepith_2584", 40, 30, 20, 0,
        (
            ("ms78300.dat", "ms78300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78300.dat", "ms78300.dat", "ms78300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78300.dat", "ms78300.dat", "ms78300.dat", "ms78300.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch83450.itc",               # 10
        "monster/ch83451.itc",               # 11
        "monster/ch78150.itc",               # 12
        "monster/ch78151.itc",               # 13
        "monster/ch78350.itc",               # 14
        "monster/ch78350.itc",               # 15
    ))

    DeclMonster(-140,    176610,  0,       0x10100CC,    "BattleInfo_284", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(8140,    163790,  0,       0x10100E1,    "BattleInfo_320", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-6720,   321220,  0,       0x1010087,    "BattleInfo_3BC", 0,   20,  0xFFFF, 4,  5)

    DeclActor(2500,    0,       319000,  1200,    2500,    1000,    319000,  0x007C, 0,  2,  0x0000)
    DeclActor(3240,    0,       7750,    1200,    3240,    1500,    7750,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1000, 0, [0, 1, 2])                            # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3])                          # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5

    ScpFunction((
        "Function_0_4E0",          # 00, 0
        "Function_1_504",          # 01, 1
        "Function_2_6EA",          # 02, 2
        "Function_3_825",          # 03, 3
        "Function_4_909",          # 04, 4
        "Function_5_126B",         # 05, 5
        "Function_6_12AA",         # 06, 6
        "Function_7_12E9",         # 07, 7
        "Function_8_1322",         # 08, 8
        "Function_9_135B",         # 09, 9
        "Function_10_1391",        # 0A, 10
        "Function_11_13CA",        # 0B, 11
        "Function_12_1403",        # 0C, 12
        "Function_13_143C",        # 0D, 13
        "Function_14_24CA",        # 0E, 14
        "Function_15_250B",        # 0F, 15
    ))


    def Function_0_4E0(): pass

    label("Function_0_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4F4")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)
    Jump("loc_503")

    label("loc_4F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_503")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_503")

    Return()

    # Function_0_4E0 end

    def Function_1_504(): pass

    label("Function_1_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_570")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_541")
    Sound(120, 1, 100, 0)
    Jump("loc_547")

    label("loc_541")

    Sound(120, 1, 70, 0)

    label("loc_547")

    SoundDistance(0x6E, 0xFFFF86DE, 0x0, 0xFFFFDC38, 0xC350, 0x186A0, 0x64, 0x0)
    OP_E3(0x76C, 0x0, 0xFFFF6488)

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_588")
    OP_1B(0x1, 0x0, 0xE)
    OP_1B(0x3, 0x0, 0xF)

    label("loc_588")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656")
    OP_70(0x0, 0x0)
    Jump("loc_65A")

    label("loc_656")

    OP_70(0x0, 0x1E)

    label("loc_65A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -13730, 0, -12170, 6000, 2000, 60000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_6A3")
    SetMapObjFrame(0xFF, "shadow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x0, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    Jump("loc_6E9")

    label("loc_6A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_END)), "loc_6CB")
    SetMapObjFrame(0xFF, "shadow", 0x1, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x1, 0x1)
    Jump("loc_6E9")

    label("loc_6CB")

    SetMapObjFrame(0xFF, "shadow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x0, 0x1)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_6E9")

    Return()

    # Function_1_504 end

    def Function_2_6EA(): pass

    label("Function_2_6EA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DC")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('幻彩围巾', 1)"), scpexpr(EXPR_END)), "loc_76D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_7D7")

    label("loc_76D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '幻彩围巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7D7")

    Jump("loc_819")

    label("loc_7DC")

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

    label("loc_819")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6EA end

    def Function_3_825(): pass

    label("Function_3_825")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0004
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FA")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x1, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x1, 0x0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x1, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_8FA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_825 end

    def Function_4_909(): pass

    label("Function_4_909")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev11007.eff")
    LoadEffect(0x1, "event/ev11009.eff")
    LoadEffect(0x2, "event/ev11008.eff")
    SetMapObjFrame(0xFF, "shadow", 0x0, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x0, 0x1)
    SetMapObjFrame(0xFF, "m4100:Layer6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "black3", 0x0, 0x1)
    SoundLoad(995)
    SoundLoad(996)
    OP_68(-14090, 1300, -12840, 0)
    MoveCamera(12, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -18770, 0, -15230, 55)
    SetChrPos(0x102, -17970, 0, -16530, 55)
    SetChrPos(0x109, -20070, 0, -15930, 55)
    SetChrPos(0x105, -19270, 0, -17130, 55)
    SetCameraDistance(15000, 2500)
    FadeToBright(1000, 0)

    def lambda_A1C():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A1C)
    Sleep(100)

    def lambda_A34():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A34)
    Sleep(100)

    def lambda_A4C():
        OP_9B(0x0, 0x109, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A4C)
    Sleep(100)

    def lambda_A64():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A64)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(3140, 1300, 5290, 4000)
    MoveCamera(34, 13, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(43210, 4000)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_68(26000, 1300, 5460, 4000)
    MoveCamera(58, 11, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(43210, 4000)
    PlaceName2(340, 200, "c_plac52", 0x0, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(810, 500, 1150, 0)
    MoveCamera(22, 51, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37460, 0)
    OP_68(810, 500, 1150, 4000)
    MoveCamera(71, 41, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(30510, 4000)
    OP_6F(0x79)
    Sleep(300)

    #C0005
    ChrTalk(
        0x101,
        "#00013F#12P#N这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x109,
        (
            "#10111F#12P#N感觉……\x01",
            "确实有点不寻常呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x102,
        (
            "#00106F#12P#N地面和岩壁\x01",
            "都在隐隐发光……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-13240, 1500, -12060, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13150, 0)
    OP_0D()
    Sleep(150)
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(500)
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    #C0008
    ChrTalk(
        0x102,
        (
            "#00108F#6P而且，总觉得……\x01",
            "……空气似乎很浑浊……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x105,
        (
            "#10306F#6P嗯，说不定是\x01",
            "瘴气一类的东西。\x02\x03",

            "#10308F……另外，上级属性\x01",
            "似乎正在运作。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_D14():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D14)
    Sleep(100)

    def lambda_D24():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D24)
    Sleep(100)

    def lambda_D34():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D34)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0010
    ChrTalk(
        0x101,
        "#00011F#5P哎！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        "#00105F#11P瓦吉，你……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        (
            "#10105F#5P为、为何会说出\x01",
            "和缇欧一样的话……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xA, 0x1F4)
    Sleep(300)

    #C0013
    ChrTalk(
        0x105,
        (
            "#10304F#12P呵呵，虽然比不上那孩子，\x01",
            "但我的灵感也很强。\x02\x03",

            "#10302F该怎么办？\x01",
            "继续前往深处调查\x01",
            "似乎相当危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00006F#5P说的也是，不过……\x02",
    )

    CloseMessageWindow()
    Sound(995, 2, 70, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    def lambda_EBF():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EBF)
    Sleep(50)

    def lambda_ECF():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ECF)
    Sleep(50)

    def lambda_EDF():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EDF)
    Sleep(50)

    def lambda_EEF():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EEF)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    Sleep(300)

    #C0015
    ChrTalk(
        0x102,
        "#00105F#11P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        "#10305F#11P……这声音是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x109,
        "#10110F#5P不好！\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x37, 0x2EE)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0018
    ChrTalk(
        0x109,
        "#10107F#6P#4S大家快退后！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00010F#5P唔！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    BeginChrThread(0x101, 3, 0, 5)
    BeginChrThread(0x102, 3, 0, 6)
    BeginChrThread(0x109, 3, 0, 8)
    BeginChrThread(0x105, 3, 0, 7)
    OP_68(-8230, 1300, -8780, 1100)
    MoveCamera(46, 10, 0, 1100)
    OP_6E(700, 1100)
    SetCameraDistance(11270, 1100)
    Sleep(800)
    StopSound(995, 500, 60)
    Sound(996, 2, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, -15000, 0, -13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -15000, 0, -13000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    OP_68(-192400, 2000, 7880, 0)
    MoveCamera(67, 4, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14860, 0)
    SetChrPos(0x101, -189740, 250, 8600, 235)
    SetChrPos(0x102, -190490, 250, 10170, 235)
    SetChrPos(0x109, -188420, 250, 9380, 235)
    SetChrPos(0x105, -189230, 250, 10700, 235)
    Fade(500)
    Sound(200, 0, 100, 0)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, -184500, 0, 12500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0x3, 0xFF, 0x0, -180650, 0, 16750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x102, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 12)
    BeginChrThread(0x105, 3, 0, 11)
    Sleep(400)
    PlayEffect(0x0, 0x5, 0xFF, 0x0, -182500, 0, 20000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    CancelBlur(0)
    OP_0D()
    Sleep(500)
    Sound(196, 0, 100, 0)
    StopSound(996, 5000, 100)
    StopEffect(0x3, 0x2)
    Sleep(1200)
    Sound(833, 0, 100, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(4000)
    WaitBGM()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21205000), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125C")
    SetScenarioFlags(0x12B, 4)

    label("loc_125C")

    SetScenarioFlags(0x22, 0)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_4_909 end

    def Function_5_126B(): pass

    label("Function_5_126B")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_5_126B end

    def Function_6_12AA(): pass

    label("Function_6_12AA")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_6_12AA end

    def Function_7_12E9(): pass

    label("Function_7_12E9")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_7_12E9 end

    def Function_8_1322(): pass

    label("Function_8_1322")

    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_8_1322 end

    def Function_9_135B(): pass

    label("Function_9_135B")

    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_9_135B end

    def Function_10_1391(): pass

    label("Function_10_1391")

    Sleep(50)
    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_10_1391 end

    def Function_11_13CA(): pass

    label("Function_11_13CA")

    Sleep(100)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_11_13CA end

    def Function_12_1403(): pass

    label("Function_12_1403")

    Sleep(150)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_12_1403 end

    def Function_13_143C(): pass

    label("Function_13_143C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51115.itc", 0x1E)
    SoundLoad(841)
    SetMapObjFrame(0xFF, "shadow", 0x1, 0x1)
    SetMapObjFrame(0xFF, "rock", 0x1, 0x1)
    SetMapObjFrame(0xFF, "m4100:Layer6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "black3", 0x1, 0x1)
    OP_68(-185970, 2400, 12000, 0)
    MoveCamera(35, 1, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(50080, 0)
    SetChrPos(0x101, -184750, 0, 12750, 45)
    SetChrPos(0x109, -185000, 0, 11500, 45)
    SetChrPos(0x102, -186000, 0, 12300, 45)
    SetChrPos(0x105, -187250, 0, 11750, 45)
    FadeToBright(1000, 0)
    OP_68(-185970, 1700, 12000, 6500)
    MoveCamera(74, 22, 0, 6500)
    OP_6E(500, 6500)
    SetCameraDistance(33640, 6500)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-183110, 1000, 13310, 0)
    MoveCamera(81, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18590, 0)
    OP_0D()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0020
    ChrTalk(
        0x101,
        "#00007F#4S#12P冈兹先生！你能听到吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0021
    ChrTalk(
        0x109,
        "#10101F#4S#12P要是听到了，就请回句话！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x109)
    OP_68(-184820, 1000, 11980, 1500)
    MoveCamera(91, 28, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(18590, 1500)

    def lambda_164D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_164D)
    Sleep(150)

    def lambda_165D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_165D)
    Sleep(100)
    Sleep(200)
    OP_6F(0x79)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006F#5P不行……\x01",
            "好像完全堵死了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0x5A, 0x1F4)

    #C0023
    ChrTalk(
        0x102,
        (
            "#00106F#6P可、可是，为何会突然……\x02\x03",

            "#00108F在塌方发生之前的一瞬间，\x01",
            "我好像听到了什么声音……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x105, 0x109, 500)

    #C0024
    ChrTalk(
        0x105,
        (
            "#10305F#12P对了，你为何能\x01",
            "预料到塌方呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x109, 0x105, 500)

    def lambda_1749():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1749)

    #C0025
    ChrTalk(
        0x109,
        (
            "#10106F#11P啊，这个……\x02\x03",

            "#10101F因为我隐隐闻到一股火药的气味，\x01",
            "所以预感到了危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10301F#12P火药……？\x02\x03",

            "#10308F这么一说，好像还真有\x01",
            "些焦臭的气味。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00103F#6P不过，如今已经很少\x01",
            "有人使用火药了……\x02\x03",

            "#00101F莫非是过去用于爆破矿山\x01",
            "的火药爆炸了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F#5P……不，再怎么说，\x01",
            "应该也不会残留在这种地方的。\x02\x03",

            "#00013F我想，多半是有人\x01",
            "引爆了炸弹机关。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1917():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1917)
    Sleep(50)

    def lambda_1927():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1927)
    Sleep(50)

    def lambda_1937():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1937)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0029
    ChrTalk(
        0x102,
        "#00107F#6P机、机关！？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10108F#11P不、不过，好像也\x01",
            "只能这样解释了……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10303F#12P这样的话……\x02\x03",

            "#10301F当时那『滋滋滋』的声音，\x01",
            "就是机关启动后的火花声吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00006F#5P……应该没错。\x02\x03",

            "#00008F设置这种机关，大概是为了\x01",
            "将入内者的退路断绝吧。\x02\x03",

            "#00001F说不定是某人在附近\x01",
            "通过远程操作来引爆的。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00108F#6P可、可是，谁会做这种事情……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x102,
        (
            "#00101F#6P莫、莫非是破坏\x01",
            "入口大门的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F#5P嗯，很有可能。\x02\x03",

            "#00013F……虽然不知道是什么人，\x01",
            "但我们好像完全中了对方的圈套。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#00106F#6P怎么会……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0037
    ChrTalk(
        0x109,
        (
            "#10102F#11P不、不要紧！\x02\x03",

            "#10112F艾尼格玛就是为了\x01",
            "应对这种局面而存在的！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x109, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(500)

    def lambda_1BF8():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1BF8)
    Sleep(50)

    def lambda_1C08():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1C08)
    Sleep(50)

    def lambda_1C18():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C18)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x101, 0)
    Sound(841, 2, 100, 0)
    Sleep(2000)
    OP_24(0x349)
    Sound(840, 0, 100, 0)
    Sleep(1000)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x109,
        "#10111F#11P哎，这……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00108F#6P应该是导力波\x01",
            "无法传送的警告提示音……\x02\x03",

            "#00101F说明书上也写着，导力波\x01",
            "很难传送到密闭场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        "#10106F#11P呜呜，是这样啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x109, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0041
    ChrTalk(
        0x105,
        (
            "#10306F#12P哎呀呀，\x01",
            "看来这条路是行不通了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(300)

    #C0042
    ChrTalk(
        0x101,
        (
            "#00003F#5P没办法了，\x01",
            "既然如此，我们就继续前进吧。\x02\x03",

            "#00008F说不定还能找到\x01",
            "其它出口……\x02\x03",

            "#00013F如果一直留在此地，\x01",
            "或许还会再次发生爆炸。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E15():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E15)
    Sleep(50)

    def lambda_1E25():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E25)
    Sleep(50)

    def lambda_1E35():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1E35)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0043
    ChrTalk(
        0x109,
        (
            "#10108F#11P说、说的也是……\x01",
            "对方也许会进行远程操作。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00103F#6P虽然外面的冈兹先生\x01",
            "应该已经去帮我们\x01",
            "找帮手了……\x02\x03",

            "#00101F但考虑到犯人的意图，\x01",
            "我们的确应该离开此处。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10304F#12P哎呀呀，这就是所谓的\x01",
            "前有狼，后有虎吗？\x02\x03",

            "#10302F和你们在一起，\x01",
            "还真是不会因为无聊而发愁。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00006F#5P你这种轻松自在的口气，现在倒是能让人踏实不少。\x02\x03",

            "#00007F我们现在得不到任何补给，\x01",
            "也只能齐心协力，\x01",
            "想办法从这里脱困了！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#00101F#6P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x105,
        "#10304F#12P嗯。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10107F#11P明白！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis301.itp")
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在战斗中可以使用#2C『爆灵』#5C了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0x80FFFFFF, 0x1F4, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在各章中，当剧情进展到高潮部分时，\x01",
            "　即可在战斗中使用『爆灵』。\x02\x03",

            "※当位于战斗画面右上方的『爆灵能源槽』蓄满时，\x01",
            "　选择发动爆灵状态，在能源槽耗尽之前，\x01",
            "　#2C我方成员可以单方面地连续行动#5C。\x02\x03",

            "※此时，#2C我方全员的异常状态都会解除#5C。此外，在爆灵状态持续\x01",
            "　过程中，#2C我方全员攻击力会提升２０％，ＣＰ也会自动增加#5C\x02\x03",

            "※不仅如此，原本需要消耗驱动时间的魔法\x01",
            "　#2C也可以瞬间发动#5C。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※爆灵能源槽为我方全体成员\x01",
            "　的『情绪状态』的体现。\x02\x03",

            "※每当我方成员发动攻击时，能源槽中的能源就会上升，\x01",
            "　在连续发动攻击或共同攻击时，\x01",
            "　能源更会大幅度上升。\x02\x03",

            "※反之，在遭到敌人的攻击时，能源将会有少许降低。\x01",
            "　另外，当能源槽蓄满之后，如果在一定回合内没有\x01",
            "　发动爆灵状态，能源便会减少一格。\x02\x03",

            "※此外，#2C如有任意同伴陷入战斗不能状态，\x01",
            "　爆灵将无法发动#5C，敬请注意。\x01",
            "　　\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    OP_50(0x1F, (scpexpr(EXPR_PUSH_LONG, 0x2000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※调查手册的说明部分中增加了『爆灵』项目，\x01",
            "　今后可以随时查阅。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, -13380, 0, -11360, 45)
    SetScenarioFlags(0x12A, 2)
    OP_29(0xA2, 0x1, 0x2)
    SetBarrier(0x3, 0x0, 0x1)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_IMUL), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x349)
    EventEnd(0x5)
    Return()

    # Function_13_143C end

    def Function_14_24CA(): pass

    label("Function_14_24CA")

    EventBegin(0x1)

    #C0054
    ChrTalk(
        0x101,
        (
            "#00001F没时间了——\x01",
            "赶快前往出口吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29200, 3510, -3510, 270)
    EventEnd(0x4)
    Return()

    # Function_14_24CA end

    def Function_15_250B(): pass

    label("Function_15_250B")

    EventBegin(0x1)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00001F没时间了——\x01",
            "赶快前往出口吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1900, 0, 28210, 180)
    EventEnd(0x4)
    Return()

    # Function_15_250B end

    SaveToFile()

Try(main)
