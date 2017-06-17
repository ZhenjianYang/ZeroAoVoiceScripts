from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1140.bin",                # FileName
        "m1140",                    # MapName
        "m1140",                    # Location
        0x006E,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 110, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1140",                  # 0
        "剛毅のアイネス",         # 1
        "ヴァンガード",           # 2
        "ヴァンガード",           # 3
        "ヴァンガード",           # 4
        "ヴァンガード",           # 5
        "SE制御",                 # 6
        "bm1040",                 # 7
        "bm1040",                 # 8
        "bm1040",                 # 9
        "bm1040",                 # 10
    ))

    ATBonus("ATBonus_3FC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_40C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_34A7", 8,   8,   21,  13,  0,   0,   0)
    Sepith("Sepith_34AF", 6,   6,   0,   0,   13,  13,  13)

    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 4, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 12, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_50C", 0x0000, 90, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_34A7", 60, 25, 10, 5,
        (
            ("ms65000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms65000.dat", "ms65000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms65000.dat", "ms65000.dat", "ms62700.dat", "ms65000.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
        )
    )

    BattleInfo(
        "BattleInfo_5D4", 0x0000, 90, 6, 60, 8, 1, 25, 0, "bm1040", "Sepith_34AF", 60, 25, 10, 5,
        (
            ("ms62700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
            ("ms62700.dat", "ms62700.dat", "ms65000.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_42C", "MonsterBattlePostion_4AC", "ed7450", "ed7453", "ATBonus_3FC"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_69C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms43200.dat", "ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4CC", "MonsterBattlePostion_4AC", "ed7452", "ed7453", "ATBonus_40C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6E0", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bm1040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80000.dat", "ms80000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4EC", "MonsterBattlePostion_4AC", "ed7451", "ed7453", "ATBonus_40C"),
            (),
            (),
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
        "monster/ch65050.itc",               # 10
        "monster/ch65050.itc",               # 11
        "monster/ch62750.itc",               # 12
        "monster/ch62750.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(20770,   2670,    -28000,  0x1010000,    "BattleInfo_50C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(7940,    18540,   -29190,  0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-1260,   21090,   -29200,  0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-12520,  16300,   -29190,  0x1010000,    "BattleInfo_50C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-21210,  -550,    -28000,  0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(4300,    4670,    -27200,  0x1010000,    "BattleInfo_50C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-7580,   4170,    -27200,  0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(320,     -6970,   -27200,  0x1010000,    "BattleInfo_5D4", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 7,   0.0,                   -21.0,                 -29.0,                 784.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  5.25,                  5.800000190734863,     1.0])
    DeclEvent(0x0000, 0, 16,  0.03999999910593033,   -27.989999771118164,   -28.0,                 784.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0028571428265422583, 6.997499942779541,     5.599999904632568,     1.0])

    DeclActor(489750,  900,     10650,   1500,    489750,  2400,    10650,   0x007C, 0,  2,  0x0000)
    DeclActor(518900,  -900,    -10,     1500,    518900,  600,     -10,     0x007C, 0,  3,  0x0000)
    DeclActor(-3530,   -27200,  -850,    1800,    -3530,   -25200,  -850,    0x007C, 0,  5,  0x0000)
    DeclActor(3040,    -27200,  -120,    1800,    3040,    -25200,  -120,    0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_808",          # 01, 1
        "Function_2_93B",          # 02, 2
        "Function_3_AD5",          # 03, 3
        "Function_4_C6F",          # 04, 4
        "Function_5_D0E",          # 05, 5
        "Function_6_F15",          # 06, 6
        "Function_7_110E",         # 07, 7
        "Function_8_1DDB",         # 08, 8
        "Function_9_1DF7",         # 09, 9
        "Function_10_1E12",        # 0A, 10
        "Function_11_1E58",        # 0B, 11
        "Function_12_1E77",        # 0C, 12
        "Function_13_1E9D",        # 0D, 13
        "Function_14_1EB0",        # 0E, 14
        "Function_15_272A",        # 0F, 15
        "Function_16_2734",        # 10, 16
        "Function_17_2F80",        # 11, 17
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_7F1")
    ClearScenarioFlags(0x22, 0)
    SetChrPos(0x0, -930, -27200, -2910, 0)
    SetChrPos(0x1, -930, -27200, -2910, 0)
    SetChrPos(0x2, -930, -27200, -2910, 0)
    SetChrPos(0x3, -930, -27200, -2910, 0)
    Jump("loc_807")

    label("loc_7F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    Event(0, 17)

    label("loc_807")

    Return()

    # Function_0_79C end

    def Function_1_808(): pass

    label("Function_1_808")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_855")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_855")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 0, -29200, 27500, 10000, 3000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 7)), scpexpr(EXPR_END)), "loc_893")
    SetMapObjFrame(0xFF, "Null_books", 0x2, "open_")
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 7)), scpexpr(EXPR_END)), "loc_8B1")
    SetMapObjFrame(0x1, "Null_color00", 0x2, "off_")

    label("loc_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 0)), scpexpr(EXPR_END)), "loc_8CF")
    SetMapObjFrame(0x2, "Null_color00", 0x2, "off_")

    label("loc_8CF")

    Call(0, 4)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EF")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_8EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_919")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_919")

    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_808 end

    def Function_2_93B(): pass

    label("Function_2_93B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 7)), scpexpr(EXPR_END)), "loc_972")
    TalkBegin(0xFF)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_AD4")

    label("loc_972")

    EventBegin(0x1)

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "光り輝く光玉がある。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "光玉を手に取る\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACD")
    Fade(500)
    SetChrPos(0x0, 492000, 900, 11930, 253)
    SetChrPos(0x1, 491780, 900, 12980, 253)
    SetChrPos(0x2, 493000, 900, 11740, 253)
    SetChrPos(0x3, 493140, 900, 13270, 253)
    OP_68(489540, 2400, 10310, 0)
    MoveCamera(28, 34, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17020, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(173, 0, 100, 0)
    SetMapObjFrame(0x1, "Null_color00", 0x2, "off")
    Sleep(500)
    SetMapObjFrame(0x1, "Null_color00", 0x2, "off_")
    SetScenarioFlags(0x1B7, 7)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_ACD")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_AD4")

    Return()

    # Function_2_93B end

    def Function_3_AD5(): pass

    label("Function_3_AD5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 0)), scpexpr(EXPR_END)), "loc_B0C")
    TalkBegin(0xFF)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_C6E")

    label("loc_B0C")

    EventBegin(0x1)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "光り輝く光玉がある。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "光玉を手に取る\x01",      # 0
            "やめておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C67")
    Fade(500)
    SetChrPos(0x0, 516049, -900, -10, 101)
    SetChrPos(0x1, 514760, -900, -1470, 101)
    SetChrPos(0x2, 515049, -900, 970, 101)
    SetChrPos(0x3, 513850, -900, -490, 101)
    OP_68(516740, 600, -1300, 0)
    MoveCamera(56, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17020, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(173, 0, 100, 0)
    SetMapObjFrame(0x2, "Null_color00", 0x2, "off")
    Sleep(500)
    SetMapObjFrame(0x2, "Null_color00", 0x2, "off_")
    SetScenarioFlags(0x1B8, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x33F, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C67")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_C6E")

    Return()

    # Function_3_AD5 end

    def Function_4_C6F(): pass

    label("Function_4_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8D")
    OP_71(0x3, 0xCD, 0xD2, 0x0, 0x20)
    Jump("loc_D0D")

    label("loc_C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_CB7")
    OP_71(0x3, 0x9B, 0xA0, 0x0, 0x20)
    SetMapObjFrame(0x3, "ten_li02", 0x0, 0x1)
    Jump("loc_D0D")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_CE1")
    OP_71(0x3, 0x37, 0x3C, 0x0, 0x20)
    SetMapObjFrame(0x3, "ten_li01", 0x0, 0x1)
    Jump("loc_D0D")

    label("loc_CE1")

    OP_71(0x3, 0x0, 0xA, 0x0, 0x20)
    SetMapObjFrame(0x3, "ten_li01", 0x0, 0x1)
    SetMapObjFrame(0x3, "ten_li02", 0x0, 0x1)

    label("loc_D0D")

    Return()

    # Function_4_C6F end

    def Function_5_D0E(): pass

    label("Function_5_D0E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_D51")
    TalkBegin(0xFF)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "皿に光玉が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_F14")

    label("loc_D51")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EEC")
    EventBegin(0x1)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "天秤の皿がある。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "光玉を置く\x01",      # 0
            "やめておく\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE0")
    Fade(500)
    SetChrPos(0x0, -5190, -27200, 1010, 89)
    SetChrPos(0x1, -5940, -27200, 2040, 89)
    SetChrPos(0x2, -6660, -27200, -170, 89)
    SetChrPos(0x3, -7420, -27200, 630, 89)
    OP_68(-560, -25700, -850, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(22500, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(632, 0, 100, 0)
    SetMapObjFrame(0x3, "ten_li01", 0x1, 0x1)
    Sleep(500)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_E7E")
    Sound(879, 0, 70, 0)
    OP_71(0x3, 0x3C, 0x69, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x69, 0x6E, 0x0, 0x0)
    Jump("loc_E9F")

    label("loc_E7E")

    Sound(879, 0, 70, 0)
    OP_71(0x3, 0x6E, 0x9B, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x9B, 0xA0, 0x0, 0x0)

    label("loc_E9F")

    SetScenarioFlags(0x1B8, 5)
    SubItemNumber(0x33F, 1)
    Sleep(1000)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_EE0")
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23500, 2000)
    OP_0D()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m1150", 0, 0, 0)
    IdleLoop()

    label("loc_EE0")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_F14")

    label("loc_EEC")

    TalkBegin(0xFF)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "天秤の皿がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_F14")

    Return()

    # Function_5_D0E end

    def Function_6_F15(): pass

    label("Function_6_F15")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 6)), scpexpr(EXPR_END)), "loc_F58")
    TalkBegin(0xFF)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "皿に光玉が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_110D")

    label("loc_F58")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33F, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E5")
    EventBegin(0x1)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "天秤の皿がある。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "光玉を置く\x01",      # 0
            "やめておく\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D9")
    Fade(500)
    SetChrPos(0x0, 5060, -27200, -1860, 270)
    SetChrPos(0x1, 6460, -27200, -60, 270)
    SetChrPos(0x2, 5990, -27200, -2950, 270)
    SetChrPos(0x3, 7190, -27200, -1530, 270)
    OP_68(260, -25700, 520, 0)
    MoveCamera(41, 23, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(22500, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sound(632, 0, 100, 0)
    SetMapObjFrame(0x3, "ten_li02", 0x1, 0x1)
    Sleep(500)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_1082")
    Sound(879, 0, 70, 0)
    OP_71(0x3, 0xA0, 0xCD, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0xCD, 0xD2, 0x0, 0x0)
    Jump("loc_10A3")

    label("loc_1082")

    Sound(879, 0, 70, 0)
    OP_71(0x3, 0xA, 0x37, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x37, 0x3C, 0x0, 0x0)

    label("loc_10A3")

    SetScenarioFlags(0x1B8, 6)
    SubItemNumber(0x33F, 1)
    Sleep(1000)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B8, 5)), scpexpr(EXPR_END)), "loc_10D9")
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23500, 2000)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m1150", 0, 0, 0)
    IdleLoop()

    label("loc_10D9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_110D")

    label("loc_10E5")

    TalkBegin(0xFF)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "天秤の皿がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_110D")

    Return()

    # Function_6_F15 end

    def Function_7_110E(): pass

    label("Function_7_110E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    SetChrFlags(0x15, 0x80)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1183")
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)

    label("loc_1183")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11A1")
    LoadChrToIndex("chr/ch03150.itc", 0x26)
    LoadChrToIndex("chr/ch03151.itc", 0x27)

    label("loc_11A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BF")
    LoadChrToIndex("chr/ch03250.itc", 0x26)
    LoadChrToIndex("chr/ch03251.itc", 0x27)

    label("loc_11BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11DD")
    LoadChrToIndex("chr/ch02950.itc", 0x28)
    LoadChrToIndex("chr/ch02951.itc", 0x29)

    label("loc_11DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11FB")
    LoadChrToIndex("chr/ch03150.itc", 0x28)
    LoadChrToIndex("chr/ch03151.itc", 0x29)

    label("loc_11FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1219")
    LoadChrToIndex("chr/ch03250.itc", 0x28)
    LoadChrToIndex("chr/ch03251.itc", 0x29)

    label("loc_1219")

    LoadChrToIndex("chr/ch43200.itc", 0x2A)
    LoadChrToIndex("chr/ch43250.itc", 0x2B)
    LoadChrToIndex("chr/ch43251.itc", 0x2C)
    LoadChrToIndex("monster/ch80050.itc", 0x2E)
    LoadChrToIndex("monster/ch80051.itc", 0x2F)
    LoadChrToIndex("chr/ch43254.itc", 0x30)
    LoadEffect(0x1, "event/ev10007.eff")
    SoundLoad(825)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, -28000, -22000, 0)
    SetChrPos(0x102, 1030, -28000, -22690, 0)
    SetChrPos(0x103, -500, -28000, -23240, 0)
    SetChrPos(0x104, 450, -28000, -23850, 0)
    SetChrPos(0xF4, -950, -28000, -24340, 0)
    SetChrPos(0xF5, -1390, -28000, -22780, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -27200, -3000, 180)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x2E)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 0, 0, 8)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3000, -27200, -4000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2E)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 8)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -3000, -27200, -4000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, -27000, -18000, 0)
    MoveCamera(48, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 3000)

    def lambda_13CF():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13CF)
    Sleep(30)

    def lambda_13E7():
        OP_9B(0x0, 0x102, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13E7)
    Sleep(30)

    def lambda_13FF():
        OP_9B(0x0, 0x103, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_13FF)
    Sleep(30)

    def lambda_1417():
        OP_9B(0x0, 0x104, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1417)
    Sleep(30)

    def lambda_142F():
        OP_9B(0x0, 0xF4, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_142F)
    Sleep(30)

    def lambda_1447():
        OP_9B(0x0, 0xF5, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1447)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #N0013
    NpcTalk(
        0x8,
        "騎士装束の娘",
        (
            "#4P──フフ。\x01",
            "待っていたぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    ClearChrFlags(0x8, 0x8)
    OP_68(0, -26500, -3500, 3000)
    MoveCamera(30, 26, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(15000, 3000)
    OP_6F(0x79)

    #C0014
    ChrTalk(
        0x104,
        "#00307F#1Pお出ましか……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x26)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x28)
    SetChrSubChip(0xF5, 0x0)
    Fade(500)
    OP_68(0, -25200, -6500, 0)
    OP_68(0, -26100, -6500, 3000)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    BeginChrThread(0xD, 1, 0, 12)

    def lambda_1611():
        OP_9B(0x0, 0x101, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1611)
    Sleep(50)

    def lambda_1629():
        OP_9B(0x0, 0x102, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1629)
    Sleep(50)

    def lambda_1641():
        OP_9B(0x0, 0x103, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1641)
    Sleep(50)

    def lambda_1659():
        OP_9B(0x0, 0x104, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1659)
    Sleep(50)

    def lambda_1671():
        OP_9B(0x0, 0xF4, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1671)
    Sleep(50)

    def lambda_1689():
        OP_9B(0x0, 0xF5, 0x0, 0x2134, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1689)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()

    #N0015
    NpcTalk(
        0x8,
        "騎士装束の娘",
        (
            "#5P鉄機隊が隊士、\x01",
            "《剛毅#4Rごう き #》のアイネスという。\x02",
        )
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0x8,
        "騎士装束の娘",
        (
            "#5Pアリアンロード様の命により、\x01",
            "まずは先鋒を務めさせていただく。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(805, 0, 80, 0)
    Sound(531, 0, 80, 0)
    SetCameraDistance(16800, 500)
    OP_6F(0x79)
    CancelBlur(500)
    OP_0D()

    #N0017
    NpcTalk(
        0x8,
        "騎士装束の娘",
        "#5P見知り置き願おうか。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00003F#6P──特務支援課、\x01",
            "ロイド・バニングスだ。\x02\x03",

            "#00013F話し合いをする余地は\x01",
            "どうやら無いみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#5Pフフ、無論だ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#5P湿地帯の時はいささか、\x01",
            "未熟にも感じたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#5P今のお前たちならば十分\x01",
            "我ら《鉄機隊》の\x01",
            "相手として不足はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    SetChrChipByIndex(0x8, 0x30)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    OP_68(0, -26400, -3000, 4000)
    MoveCamera(0, 25, 0, 4000)
    OP_6E(550, 4000)
    SetCameraDistance(18700, 4000)
    OP_82(0x64, 0x64, 0x1770, 0xBB8)
    Sound(825, 2, 50, 0)
    Sleep(400)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)
    Fade(150)
    Sound(817, 0, 100, 0)
    StopSound(825, 2000, 50)
    BeginChrThread(0xD, 1, 0, 13)
    BeginChrThread(0x9, 3, 0, 10)
    BeginChrThread(0xA, 3, 0, 10)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    Sleep(500)
    Fade(250)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    Sound(805, 0, 80, 0)
    Sound(531, 0, 80, 0)
    SetCameraDistance(16500, 500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CancelBlur(500)
    OP_0D()

    #C0022
    ChrTalk(
        0x8,
        (
            "#5Pアリアンロード様の前に\x01",
            "辿り着く資格があるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        "#5P我が斧槍#4Rハルバード#で試させてもらうぞ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -26400, -7000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16800, 0)
    OP_0D()

    #C0024
    ChrTalk(
        0x101,
        "#00007F#12P望む所だ……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B70")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B14")
    OP_FC(0xC)
    Jump("loc_1B29")

    label("loc_1B14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B29")
    OP_FC(0xC)

    label("loc_1B29")


    #C0025
    ChrTalk(
        0x105,
        (
            "#10407F#13P#N《鉄機隊》の隊士相手なら\x01",
            "こちらも不足はない……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1B70")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BF6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B9A")
    OP_FC(0xC)
    Jump("loc_1BAF")

    label("loc_1B9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAF")
    OP_FC(0xC)

    label("loc_1BAF")


    #C0026
    ChrTalk(
        0x106,
        (
            "#10701F#13P#N《銀#2Rイン#》の力……\x01",
            "とくとご覧にいれましょう！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C61")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C20")
    OP_FC(0xC)
    Jump("loc_1C35")

    label("loc_1C20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C35")
    OP_FC(0x6)

    label("loc_1C35")


    #C0027
    ChrTalk(
        0x109,
        "#10107F#13P#Nいざ、尋常に勝負です！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1C61")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, -26400, -6000, 500)
    SetCameraDistance(10500, 500)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 0, 0, 11)

    def lambda_1C9F():
        OP_9B(0x1, 0xFE, 0x0, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C9F)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 0x2F)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 0, 0, 9)

    def lambda_1CC7():
        OP_9B(0x1, 0xFE, 0xF, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CC7)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x2F)
    SetChrSubChip(0xA, 0x0)
    BeginChrThread(0xA, 0, 0, 9)

    def lambda_1CEF():
        OP_9B(0x1, 0xFE, 0xFFF1, 0xFA0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CEF)

    def lambda_1D04():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D04)

    def lambda_1D19():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D19)

    def lambda_1D2E():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D2E)

    def lambda_1D43():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D43)

    def lambda_1D58():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_1D58)

    def lambda_1D6D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_1D6D)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xF4, 0x1)
    EndChrThread(0xF5, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0x9, 0x0)
    EndChrThread(0xA, 0x0)
    OP_24(0x339)
    Battle("BattleInfo_69C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Call(0, 14)
    Return()

    # Function_7_110E end

    def Function_8_1DDB(): pass

    label("Function_8_1DDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF6")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_8_1DDB")

    label("loc_1DF6")

    Return()

    # Function_8_1DDB end

    def Function_9_1DF7(): pass

    label("Function_9_1DF7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E11")
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_9_1DF7")

    label("loc_1E11")

    Return()

    # Function_9_1DF7 end

    def Function_10_1E12(): pass

    label("Function_10_1E12")

    PlayEffect(0x1, 0xFF, 0xFE, 0x5, 0, 100, 0, 0, 0, 0, 1650, 1650, 1650, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
    Return()

    # Function_10_1E12 end

    def Function_11_1E58(): pass

    label("Function_11_1E58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E76")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_11_1E58")

    label("loc_1E76")

    Return()

    # Function_11_1E58 end

    def Function_12_1E77(): pass

    label("Function_12_1E77")

    Sleep(2200)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E9C")
    Sound(540, 0, 50, 0)

    label("loc_1E9C")

    Return()

    # Function_12_1E77 end

    def Function_13_1E9D(): pass

    label("Function_13_1E9D")

    Sleep(900)
    Sound(223, 0, 100, 0)
    Sleep(600)
    Sound(936, 0, 70, 0)
    Return()

    # Function_13_1E9D end

    def Function_14_1EB0(): pass

    label("Function_14_1EB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EEE")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_1EEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F06")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_1F06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F1E")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_1F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F36")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_1F36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F4E")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_1F4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F66")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_1F66")

    LoadChrToIndex("chr/ch43250.itc", 0x24)
    LoadChrToIndex("chr/ch43253.itc", 0x25)
    LoadChrToIndex("chr/ch43254.itc", 0x26)
    LoadChrToIndex("chr/ch43200.itc", 0x27)
    LoadEffect(0x0, "event/ev10006.eff")
    LoadEffect(0x1, "event/ev10007.eff")
    SoundLoad(832)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, -27200, -8000, 0)
    SetChrPos(0x102, 1030, -27200, -8690, 0)
    SetChrPos(0x103, -500, -27200, -9240, 0)
    SetChrPos(0x104, 450, -27300, -9850, 0)
    SetChrPos(0xF4, -950, -27470, -10340, 0)
    SetChrPos(0xF5, -1390, -27210, -8780, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x22)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x23)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -27200, -3000, 180)
    OP_68(0, -26400, -5500, 0)
    OP_68(0, -26400, -4000, 3000)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18700, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0028
    ChrTalk(
        0x8,
        (
            "#5P──見事。\x01",
            "よくぞ我が斧槍を凌いだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "#5P約束通り、道を空けよう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(400)
    SetCameraDistance(18200, 800)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(100)
    Sound(805, 0, 70, 0)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0x8, 0x26)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Fade(500)
    SetCameraDistance(17800, 0)
    Sound(832, 2, 100, 0)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x8,
        (
            "#5Pだが、後に控える２人も\x01",
            "百戦錬磨の使い手だ……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#5P慢心せずに挑むことだな。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#00105F#12Pあ……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16800, 2000)
    BeginChrThread(0xD, 1, 0, 15)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x0, 0x8, 0x5, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Fade(500)
    SetCameraDistance(18700, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(936, 0, 100, 0)
    StopSound(832, 500, 100)

    def lambda_2329():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xFA)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2329)
    WaitChrThread(0x8, 2)
    CancelBlur(1000)
    OP_6F(0x79)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    Sleep(700)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2370")
    Sound(540, 0, 50, 0)

    label("loc_2370")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    OP_0D()
    OP_68(0, -26400, -3500, 1500)

    def lambda_23B7():
        OP_9B(0x0, 0x101, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23B7)
    Sleep(50)

    def lambda_23CF():
        OP_9B(0x0, 0x102, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23CF)
    Sleep(50)

    def lambda_23E7():
        OP_9B(0x0, 0x103, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23E7)
    Sleep(50)

    def lambda_23FF():
        OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_23FF)
    Sleep(50)

    def lambda_2417():
        OP_9B(0x0, 0xF4, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_2417)
    Sleep(50)

    def lambda_242F():
        OP_9B(0x0, 0xF5, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_242F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0033
    ChrTalk(
        0x102,
        "#00101F#30W#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#00206F#12P#N……気配をロスト。\x01",
            "転位して消え去ったようです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00301F#12Pふう……\x01",
            "とんでもねぇ娘だったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_255E")

    #C0036
    ChrTalk(
        0x105,
        (
            "#10406F#12P#Nああ……\x01",
            "彼女らの噂は聞いてたけど\x01",
            "まさかここまでとは。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_25AC")

    label("loc_255E")


    #C0037
    ChrTalk(
        0x106,
        (
            "#10706F#12P#Nはい……\x01",
            "噂には聞いていましたが\x01",
            "あそこまでの使い手とは。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_25AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2606")

    #C0038
    ChrTalk(
        0x109,
        (
            "#10101F#12P#Nでも、全力を尽くせば\x01",
            "勝てない相手じゃないです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_2649")

    label("loc_2606")


    #C0039
    ChrTalk(
        0x106,
        (
            "#10701F#12P#Nでも、全力を尽くせば\x01",
            "太刀打ちは出来そうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2649")

    OP_93(0x101, 0xB4, 0x1F4)

    #C0040
    ChrTalk(
        0x101,
        (
            "#00013F#5Pああ……\x01",
            "この調子で先に進もう！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00108F#12P（やっぱり何かが\x01",
            "  引っかかるような……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_37()
    SetChrPos(0x0, 400, -27200, -7930, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 7)
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFrame(0xFF, "Null_books", 0x2, "open_")
    SetBarrier(0x2, 0x0, 0x1)
    OP_24(0x340)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_14_1EB0 end

    def Function_15_272A(): pass

    label("Function_15_272A")

    Sleep(1100)
    Sound(222, 0, 80, 0)
    Return()

    # Function_15_272A end

    def Function_16_2734(): pass

    label("Function_16_2734")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-170, -26500, -25960, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(21320, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27F8")
    SetChrPos(0x101, 120, -28010, -26300, 0)
    SetChrPos(0x102, -1480, -28010, -26550, 0)
    SetChrPos(0x103, 1470, -28010, -26550, 0)
    SetChrPos(0x104, -1480, -28010, -27930, 0)
    SetChrPos(0x109, -120, -28010, -27930, 0)
    SetChrPos(0x105, 1470, -28010, -27930, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_2857")

    label("loc_27F8")

    SetChrPos(0x101, -930, -28010, -26550, 0)
    SetChrPos(0x102, 590, -28010, -26550, 0)
    SetChrPos(0x104, -1480, -28010, -27930, 0)
    SetChrPos(0x109, -120, -28010, -27930, 0)
    SetChrPos(0x105, 1470, -28010, -27930, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2857")

    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28B9")
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    label("loc_28B9")

    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x101,
        "#00005F……あっ！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        "#00105Fこ、これって……\x02",
    )

    CloseMessageWindow()
    OP_68(-3050, -25900, 21430, 4000)
    MoveCamera(31, 20, 0, 4000)
    OP_6E(590, 4000)
    SetCameraDistance(22500, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29EE")
    SetChrPos(0x101, -120, -28010, 10000, 0)
    SetChrPos(0x102, -1480, -28010, 10000, 0)
    SetChrPos(0x103, 1470, -28010, 10000, 0)
    SetChrPos(0x104, -1480, -28010, 8620, 0)
    SetChrPos(0x109, -120, -28010, 8620, 0)
    SetChrPos(0x105, 1470, -28010, 8620, 0)
    Jump("loc_2A43")

    label("loc_29EE")

    SetChrPos(0x101, -930, -28010, 10000, 0)
    SetChrPos(0x102, 590, -28010, 10000, 0)
    SetChrPos(0x104, -1480, -28010, 8620, 0)
    SetChrPos(0x109, -120, -28010, 8620, 0)
    SetChrPos(0x105, 1470, -28010, 8620, 0)

    label("loc_2A43")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B04")

    def lambda_2A59():
        OP_95(0xFE, 120, -28010, 22100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A59)
    Sleep(50)

    def lambda_2A76():
        OP_95(0xFE, -1480, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A76)
    Sleep(50)

    def lambda_2A93():
        OP_95(0xFE, 1470, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A93)
    Sleep(50)

    def lambda_2AB0():
        OP_95(0xFE, -1480, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2AB0)
    Sleep(50)

    def lambda_2ACD():
        OP_95(0xFE, -120, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2ACD)
    Sleep(50)

    def lambda_2AEA():
        OP_95(0xFE, 1470, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2AEA)
    Jump("loc_2B92")

    label("loc_2B04")


    def lambda_2B09():
        OP_95(0xFE, -930, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B09)
    Sleep(50)

    def lambda_2B26():
        OP_95(0xFE, 590, -28010, 21930, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B26)
    Sleep(50)

    def lambda_2B43():
        OP_95(0xFE, -1480, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B43)
    Sleep(50)

    def lambda_2B60():
        OP_95(0xFE, -120, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B60)
    Sleep(50)

    def lambda_2B7D():
        OP_95(0xFE, 1470, -28010, 20550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B7D)

    label("loc_2B92")

    Sleep(3000)
    OP_68(-3340, -25900, 19680, 5000)
    MoveCamera(31, 20, 0, 5000)
    OP_6E(590, 5000)
    SetCameraDistance(13470, 5000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)

    #C0044
    ChrTalk(
        0x105,
        (
            "#10305F本棚っていうのはこれかい？\x02\x03",

            "#10301F肝心の中身がスッカラカンだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00006Fい、いや……\x01",
            "前に見たときは確かに、\x01",
            "ここにも本があったんだ。\x02\x03",

            "#00001F調査の情報もある以上、\x01",
            "つい最近まであったのは\x01",
            "間違いないはずなんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2D54")

    #C0046
    ChrTalk(
        0x103,
        (
            "#00203F何者かが本を運び出した……\x01",
            "そういうことでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x109,
        (
            "#10105Fで、でもそんなこと、\x01",
            "警備隊が気づいていないはずは……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD0")

    label("loc_2D54")


    #C0048
    ChrTalk(
        0x109,
        (
            "#10105F何者かが本を運び出した……\x01",
            "そういうことですか！？\x02\x03",

            "#10103Fで、でもそんなこと、\x01",
            "警備隊が気づいていないはずは……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DD0")


    #C0049
    ChrTalk(
        0x104,
        (
            "#00301Fああ……\x01",
            "それに何の為に本なんぞを\x01",
            "持ち出すってんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E57")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2E57")

    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EA9")
    OP_64(0x103)

    label("loc_2EA9")

    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0050
    ChrTalk(
        0x101,
        (
            "#00003F……とにかく、\x01",
            "今は考えていても仕方が無い。\x02\x03",

            "#00001F本棚は最上階にもあったはずだ。\x01",
            "そちらを確認しに行ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#00101Fええ……そうしましょう。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -2680, -29200, 20900, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x4)
    SetScenarioFlags(0x153, 3)
    ModifyEventFlags(0, 1, 0x80)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_16_2734 end

    def Function_17_2F80(): pass

    label("Function_17_2F80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("monster/ch80050.itc", 0x1E)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FAA")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)

    label("loc_2FAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FC2")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)

    label("loc_2FC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FDA")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)

    label("loc_2FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FF2")
    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_2FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_300A")
    LoadChrToIndex("chr/ch02950.itc", 0x1F)

    label("loc_300A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3022")
    LoadChrToIndex("chr/ch03150.itc", 0x1F)

    label("loc_3022")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_303A")
    LoadChrToIndex("chr/ch03250.itc", 0x1F)

    label("loc_303A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3052")
    LoadChrToIndex("chr/ch00950.itc", 0x1F)

    label("loc_3052")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_306A")
    LoadChrToIndex("chr/ch00050.itc", 0x20)

    label("loc_306A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3082")
    LoadChrToIndex("chr/ch00150.itc", 0x20)

    label("loc_3082")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_309A")
    LoadChrToIndex("chr/ch00250.itc", 0x20)

    label("loc_309A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30B2")
    LoadChrToIndex("chr/ch00350.itc", 0x20)

    label("loc_30B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30CA")
    LoadChrToIndex("chr/ch02950.itc", 0x20)

    label("loc_30CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30E2")
    LoadChrToIndex("chr/ch03150.itc", 0x20)

    label("loc_30E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30FA")
    LoadChrToIndex("chr/ch03250.itc", 0x20)

    label("loc_30FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3112")
    LoadChrToIndex("chr/ch00950.itc", 0x20)

    label("loc_3112")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_312A")
    LoadChrToIndex("chr/ch00050.itc", 0x21)

    label("loc_312A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3142")
    LoadChrToIndex("chr/ch00150.itc", 0x21)

    label("loc_3142")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_315A")
    LoadChrToIndex("chr/ch00250.itc", 0x21)

    label("loc_315A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3172")
    LoadChrToIndex("chr/ch00350.itc", 0x21)

    label("loc_3172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_318A")
    LoadChrToIndex("chr/ch02950.itc", 0x21)

    label("loc_318A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31A2")
    LoadChrToIndex("chr/ch03150.itc", 0x21)

    label("loc_31A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31BA")
    LoadChrToIndex("chr/ch03250.itc", 0x21)

    label("loc_31BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D2")
    LoadChrToIndex("chr/ch00950.itc", 0x21)

    label("loc_31D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31EA")
    LoadChrToIndex("chr/ch00050.itc", 0x22)

    label("loc_31EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3202")
    LoadChrToIndex("chr/ch00150.itc", 0x22)

    label("loc_3202")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_321A")
    LoadChrToIndex("chr/ch00250.itc", 0x22)

    label("loc_321A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3232")
    LoadChrToIndex("chr/ch00350.itc", 0x22)

    label("loc_3232")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_324A")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_324A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3262")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_3262")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_327A")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_327A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3292")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_3292")

    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 499000, 0, -4900, 180)
    BeginChrThread(0xB, 0, 0, 8)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 501000, 0, -4900, 180)
    BeginChrThread(0xC, 0, 0, 8)
    SetChrPos(0x0, 499000, 0, -10500, 0)
    SetChrPos(0x1, 501000, 0, -10500, 0)
    SetChrPos(0x2, 498000, 0, -12500, 0)
    SetChrPos(0x3, 502000, 0, -12500, 0)
    OP_68(499000, 1500, -10280, 0)
    MoveCamera(46, 28, 1, 0)
    OP_6E(500, 0)
    SetCameraDistance(23620, 0)
    OP_68(499000, 1500, -6910, 1500)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33FC")
    Sound(540, 0, 50, 0)

    label("loc_33FC")

    SetChrChipByIndex(0x0, 0x1F)
    SetChrChipByIndex(0x1, 0x20)
    SetChrChipByIndex(0x2, 0x21)
    SetChrChipByIndex(0x3, 0x22)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    OP_0D()
    Sleep(1000)
    Battle("BattleInfo_6E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrChipByIndex(0x1, 0xFF)
    SetChrChipByIndex(0x2, 0xFF)
    SetChrChipByIndex(0x3, 0xFF)
    Sleep(100)
    SetScenarioFlags(0x1B8, 7)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_17_2F80 end

    SaveToFile()

Try(main)
