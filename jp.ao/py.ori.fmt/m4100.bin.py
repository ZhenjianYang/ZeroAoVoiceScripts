from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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

    Sepith("Sepith_282C", 2,   7,   2,   2,   0,   3,   0)
    Sepith("Sepith_2834", 2,   3,   4,   3,   2,   0,   2)
    Sepith("Sepith_283C", 3,   0,   4,   2,   3,   4,   0)

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
        "BattleInfo_284", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_282C", 40, 30, 20, 0,
        (
            ("ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x0010, 54, 6, 45, 10, 1, 40, 0, "bm4110", "Sepith_2834", 40, 30, 20, 0,
        (
            ("ms78100.dat", "ms78100.dat", 0, 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            ("ms78100.dat", "ms78100.dat", "ms78100.dat", "ms78100.dat", 0, 0, "ms78100.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3BC", 0x0000, 54, 6, 45, 10, 1, 20, 0, "bm4110", "Sepith_283C", 40, 30, 20, 0,
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
        "Function_3_83B",          # 03, 3
        "Function_4_937",          # 04, 4
        "Function_5_133D",         # 05, 5
        "Function_6_137C",         # 06, 6
        "Function_7_13BB",         # 07, 7
        "Function_8_13F4",         # 08, 8
        "Function_9_142D",         # 09, 9
        "Function_10_1463",        # 0A, 10
        "Function_11_149C",        # 0B, 11
        "Function_12_14D5",        # 0C, 12
        "Function_13_150E",        # 0D, 13
        "Function_14_2772",        # 0E, 14
        "Function_15_27BB",        # 0F, 15
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EA")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x42, 1)"), scpexpr(EXPR_END)), "loc_773")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_7E5")

    label("loc_773")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x42),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_7E5")

    Jump("loc_82F")

    label("loc_7EA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_82F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6EA end

    def Function_3_83B(): pass

    label("Function_3_83B")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_928")
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

    label("loc_928")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_83B end

    def Function_4_937(): pass

    label("Function_4_937")

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

    def lambda_A4A():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A4A)
    Sleep(100)

    def lambda_A62():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A62)
    Sleep(100)

    def lambda_A7A():
        OP_9B(0x0, 0x109, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A7A)
    Sleep(100)

    def lambda_A92():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A92)
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
        "#00013F#12P#Nこれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0006
    ChrTalk(
        0x109,
        (
            "#10111F#12P#N確かに……\x01",
            "ちょっと普通じゃないですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0007
    ChrTalk(
        0x102,
        (
            "#00106F#12P#N地面や壁面がぼうっと\x01",
            "光っているみたいだけど……\x02",
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
            "#00108F#6Pそれに、何かしら……\x01",
            "……この淀#2Rよど#んだ空気は……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x105,
        (
            "#10306F#6Pうーん。\x01",
            "瘴気#4Rしょうき#のたぐいかもしれないね。\x02\x03",

            "#10308F……これは上位属性が\x01",
            "働いているかもしれないな。\x02",
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

    def lambda_D94():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D94)
    Sleep(100)

    def lambda_DA4():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DA4)
    Sleep(100)

    def lambda_DB4():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DB4)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0010
    ChrTalk(
        0x101,
        "#00011F#5Pへっ！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        "#00105F#11Pワジ君、あなた……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        (
            "#10105F#5Pど、どうしてティオちゃんと\x01",
            "同じようなことを……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xA, 0x1F4)
    Sleep(300)

    #C0013
    ChrTalk(
        0x105,
        (
            "#10304F#12Pフフ、あの子ほどじゃないけど\x01",
            "けっこう霊感はある方でね。\x02\x03",

            "#10302Fどうする？\x01",
            "このまま奥を調べるのは\x01",
            "結構ヤバそうな気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00006F#5Pそうだな、でも……\x02",
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

    def lambda_F75():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F75)
    Sleep(50)

    def lambda_F85():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F85)
    Sleep(50)

    def lambda_F95():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F95)
    Sleep(50)

    def lambda_FA5():
        OP_93(0x102, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FA5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    Sleep(300)

    #C0015
    ChrTalk(
        0x102,
        "#00105F#11Pな、なにかしら？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        "#10305F#11P……この音は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x109,
        "#10110F#5P──いけない！\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x37, 0x2EE)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0018
    ChrTalk(
        0x109,
        "#10107F#6P#4S皆さん、下がってください！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00010F#5Pくっ！？\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21205000), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132E")
    SetScenarioFlags(0x12B, 4)

    label("loc_132E")

    SetScenarioFlags(0x22, 0)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_4_937 end

    def Function_5_133D(): pass

    label("Function_5_133D")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(809, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_5_133D end

    def Function_6_137C(): pass

    label("Function_6_137C")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    Sound(844, 0, 50, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_6_137C end

    def Function_7_13BB(): pass

    label("Function_7_13BB")

    Sleep(250)
    OP_9B(0x0, 0xFE, 0xBE, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_7_13BB end

    def Function_8_13F4(): pass

    label("Function_8_13F4")

    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0xAF0, 0x1388, 0x1)
    OP_9C(0xFE, 0xBB8, 0x0, 0x7D0, 0x15E, 0x44C)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    Return()

    # Function_8_13F4 end

    def Function_9_142D(): pass

    label("Function_9_142D")

    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_9_142D end

    def Function_10_1463(): pass

    label("Function_10_1463")

    Sleep(50)
    OP_9C(0xFE, 0xFFFFF448, 0xFFFFFF06, 0xFFFFF448, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_10_1463 end

    def Function_11_149C(): pass

    label("Function_11_149C")

    Sleep(100)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_11_149C end

    def Function_12_14D5(): pass

    label("Function_12_14D5")

    Sleep(150)
    OP_9C(0xFE, 0xFFFFF830, 0xFFFFFF06, 0xFFFFF830, 0x15E, 0x190)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0xFA0, 0x1)
    Return()

    # Function_12_14D5 end

    def Function_13_150E(): pass

    label("Function_13_150E")

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
        "#00007F#4S#12Pガンツさん、聞こえますか！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0021
    ChrTalk(
        0x109,
        "#10101F#4S#12P聞こえたら返事をしてください！\x02",
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

    def lambda_1729():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1729)
    Sleep(150)

    def lambda_1739():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1739)
    Sleep(100)
    Sleep(200)
    OP_6F(0x79)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006F#5P駄目だ……\x01",
            "完全に塞がったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0x102, 0x5A, 0x1F4)

    #C0023
    ChrTalk(
        0x102,
        (
            "#00106F#6Pで、でもどうしていきなり……\x02\x03",

            "#00108F崩落する直前、\x01",
            "何か音がしてたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x105, 0x109, 500)

    #C0024
    ChrTalk(
        0x105,
        (
            "#10305F#12Pそういや、どうして君は\x01",
            "崩落するのが分かったんだい？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x109, 0x105, 500)

    def lambda_1847():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1847)

    #C0025
    ChrTalk(
        0x109,
        (
            "#10106F#11Pあ、うん。\x02\x03",

            "#10101Fかすかに火薬の匂いを感じて\x01",
            "危険だと思ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10301F#12P火薬……？\x02\x03",

            "#10308Fそういえば微かに\x01",
            "焦げ臭いような匂いがするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00103F#6Pでも、火薬なんて最近では\x01",
            "滅多に使われないはずだし……\x02\x03",

            "#00101F昔、鉱山で使われていた発破#4Rはっぱ#が\x01",
            "爆発してしまったのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F#5P……いや、いくらなんでも\x01",
            "こんな場所に残っていないだろう。\x02\x03",

            "#00013F多分、爆薬を使った\x01",
            "トラップが発動したんだと思う。\x02",
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

    def lambda_1A65():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1A65)
    Sleep(50)

    def lambda_1A75():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A75)
    Sleep(50)

    def lambda_1A85():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1A85)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0029
    ChrTalk(
        0x102,
        "#00107F#6Pト、トラップ！？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10108F#11Pで、でも確かに\x01",
            "そうとしか思えないかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10303F#12Pなるほど、そうか……\x02\x03",

            "#10301Fあの『ジジジ』というのは\x01",
            "仕掛けの火花の音だったんだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00006F#5P……おそらく。\x02\x03",

            "#00008F誰かが中に入ってから\x01",
            "退路を断つための仕掛けだろう。\x02\x03",

            "#00001Fひょっとしたら、近くに潜んで\x01",
            "遠隔操作で爆破したかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#00108F#6Pで、でも誰がそんな事を……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x102,
        (
            "#00101F#6Pま、まさか入口の扉を\x01",
            "破壊した……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F#5Pああ、その可能性は高そうだ。\x02\x03",

            "#00013F……何者かは知らないけど\x01",
            "完全に嵌#2Rは#められたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        "#00106F#6Pそんな……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0037
    ChrTalk(
        0x109,
        (
            "#10102F#11Pだ、大丈夫ですよ！\x02\x03",

            "#10112Fこういう時のために\x01",
            "エニグマがあるわけですし！\x02",
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

    def lambda_1D94():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D94)
    Sleep(50)

    def lambda_1DA4():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DA4)
    Sleep(50)

    def lambda_1DB4():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DB4)
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
        "#10111F#11Pえっと、これって……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00108F#6P多分、導力波が届いていない\x01",
            "警告音#6Rアラート#かも……\x02\x03",

            "#00101F密閉された場所だと届きにくいって\x01",
            "マニュアルに書いてあったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        "#10106F#11Pうう、そうなんですか……\x02",
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
            "#10306F#12Pやれやれ。\x01",
            "そう都合よくは行かないか。\x02",
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
            "#00003F#5P──仕方ない。\x01",
            "こうなったら先へ進もう。\x02\x03",

            "#00008Fもしかしたら、別の出口が\x01",
            "見つかるかもしれないし……\x02\x03",

            "#00013F下手にここに残っていたら\x01",
            "また爆破されるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_200D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_200D)
    Sleep(50)

    def lambda_201D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_201D)
    Sleep(50)

    def lambda_202D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_202D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0043
    ChrTalk(
        0x109,
        (
            "#10108F#11Pそ、そうですね……\x01",
            "遠隔操作の可能性もありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00103F#6P外にいたガンツさんが\x01",
            "助けを呼んでくれているとは\x01",
            "思うけれど……\x02\x03",

            "#00101F確かに、犯人の狙いを考えると\x01",
            "動いた方がいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x105,
        (
            "#10304F#12Pやれやれ、留まるは地獄、\x01",
            "進むは苦難といったところか。\x02\x03",

            "#10302F君たちといると\x01",
            "ホント退屈しなくて済むなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00006F#5Pその減らず口、今は心強いよ。\x02\x03",

            "#00007F──補給はできない。\x01",
            "とにかく力を合わせて\x01",
            "何とかこの場を切り抜けよう！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#00101F#6Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x105,
        "#10304F#12Pｊａ#4Rヤー#．\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10107F#11P了解です！\x02",
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
            "戦闘中に#2Cバースト#5Cが使用可能になりました。\x02",
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
            "※各章でストーリーが佳境に差しかかると、\x01",
            "　戦闘中に『バースト』が使用可能となります。\x02\x03",

            "※戦闘画面右上の『バーストゲージ』がＭＡＸ時に\x01",
            "　バーストを選ぶと、ゲージが切れるまでの間\x01",
            "　#2C味方が一方的に行動ができる#5Cようになります。\x02\x03",

            "※この時、#2C味方全員の状態異常が回復する#5Cほか、\x01",
            "　発動中は#2C攻撃力が２０％上昇し、ＣＰも自動上昇#5Cします。\x02\x03",

            "※さらに──本来発動に時間がかかるアーツも\x01",
            "　#2C即座に発動することが可能#5Cになります。\x02",
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
            "※なお、バーストゲージは仲間全員の\x01",
            "　『テンション』を反映しているものです。\x02\x03",

            "※味方が攻撃するたびに上昇していきますが、\x01",
            "　連続して攻撃したり、一斉攻撃をした時には\x01",
            "　ガンガン上がっていきます。\x02\x03",

            "※逆に、敵に攻撃されると少し下がるほか\x01",
            "　ＭＡＸ状態で数ターン使わないでいると、\x01",
            "　ゲージが一段階下がってしまいます。\x02\x03",

            "※なお#2C戦闘不能状態の仲間がいる時には\x01",
            "　バーストを発動することができない#5Cので\x01",
            "　注意してください。\x02",
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
            "※捜査手帳のマニュアルに『バースト』が追加され、\x01",
            "　閲覧可能になりました。\x02",
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

    # Function_13_150E end

    def Function_14_2772(): pass

    label("Function_14_2772")

    EventBegin(0x1)

    #C0054
    ChrTalk(
        0x101,
        (
            "#00001F時間がない――\x01",
            "急いで出口に向かおう！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 29200, 3510, -3510, 270)
    EventEnd(0x4)
    Return()

    # Function_14_2772 end

    def Function_15_27BB(): pass

    label("Function_15_27BB")

    EventBegin(0x1)

    #C0055
    ChrTalk(
        0x101,
        (
            "#00001F時間がない――\x01",
            "急いで出口に向かおう！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -1900, 0, 28210, 180)
    EventEnd(0x4)
    Return()

    # Function_15_27BB end

    SaveToFile()

Try(main)
