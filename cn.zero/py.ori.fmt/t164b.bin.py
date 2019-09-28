from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t164b.bin",                # FileName
        "t164b",                    # MapName
        "t164b",                    # Location
        0x0057,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 87, 0, 0, 0, 1],
    )

    BuildStringList((
        "t164b",                  # 0
        "bt162b",                 # 1
        "bt162b",                 # 2
    ))

    ATBonus("ATBonus_1BC", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_A63", 13,  13,  24,  10,  0,   0,   0)
    Sepith("Sepith_A6B", 3,   14,  4,   4,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_21C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_224", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_234", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_238", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_280", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_288", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_28C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_294", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_204", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 2, 13, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_29C", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_A63", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_21C", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1FC", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_21C", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_1FC", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
        )
    )

    BattleInfo(
        "BattleInfo_364", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_A6B", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_21C", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1FC", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_21C", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_1FC", "MonsterBattlePostion_27C", "ed7402", "ed7403", "ATBonus_1BC"),
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
        "monster/ch67550.itc",               # 10
        "monster/ch67551.itc",               # 11
        "monster/ch75750.itc",               # 12
        "monster/ch75750.itc",               # 13
    ))

    DeclMonster(108920,  1820,    0,       0x1010000,    "BattleInfo_29C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-7580,   94760,   0,       0x1010000,    "BattleInfo_364", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-60010,  94920,   0,       0x1010000,    "BattleInfo_29C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-46140,  39160,   0,       0x1010000,    "BattleInfo_364", 0,   18,  0xFFFF, 2,  3)

    DeclActor(54750,   0,       68600,   1500,    54750,   -150,    68600,   0x007C, 0,  4,  0x0000)
    DeclActor(-5000,   0,       85500,   1200,    -5000,   1000,    85500,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_470",          # 00, 0
        "Function_1_471",          # 01, 1
        "Function_2_69F",          # 02, 2
        "Function_3_74D",          # 03, 3
        "Function_4_883",          # 04, 4
    ))


    def Function_0_470(): pass

    label("Function_0_470")

    Return()

    # Function_0_470 end

    def Function_1_471(): pass

    label("Function_1_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 3)), scpexpr(EXPR_END)), "loc_483")
    OP_65(0x0, 0x1)
    Jump("loc_4CF")

    label("loc_483")

    LoadEffect(0x7, "event\\eva00_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 54750, 0, 68600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_524")
    LoadEffect(0x6, "event\\ev617_00.eff")
    PlayEffect(0x6, 0x6, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_524")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_697")
    OP_70(0x7, 0x0)
    Jump("loc_69B")

    label("loc_697")

    OP_70(0x7, 0x1E)

    label("loc_69B")

    Call(0, 2)
    Return()

    # Function_1_471 end

    def Function_2_69F(): pass

    label("Function_2_69F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C0")
    SetChrFlags(0x8, 0x8)
    Jump("loc_6C5")

    label("loc_6C0")

    ClearChrFlags(0x8, 0x8)

    label("loc_6C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F5")
    SetChrFlags(0x9, 0x8)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_700")

    label("loc_6F5")

    ClearChrFlags(0x9, 0x8)
    ClearMapObjFlags(0x7, 0x4)

    label("loc_700")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_721")
    SetChrFlags(0xA, 0x8)
    Jump("loc_726")

    label("loc_721")

    ClearChrFlags(0xA, 0x8)

    label("loc_726")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_747")
    SetChrFlags(0xB, 0x8)
    Jump("loc_74C")

    label("loc_747")

    ClearChrFlags(0xB, 0x8)

    label("loc_74C")

    Return()

    # Function_2_69F end

    def Function_3_74D(): pass

    label("Function_3_74D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('炎伤之刃', 1)"), scpexpr(EXPR_END)), "loc_7CC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_835")

    label("loc_7CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x9B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x9B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_835")

    Jump("loc_877")

    label("loc_83A")

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

    label("loc_877")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_74D end

    def Function_4_883(): pass

    label("Function_4_883")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    StopEffect(0x7, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x335),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('罗赞贝尔克人偶·Ｃ', 1)
    Fade(1000)
    OP_68(54210, 1000, 68060, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 53620, 0, 68400, 90)
    SetChrPos(0x102, 52520, 0, 69000, 90)
    SetChrPos(0x103, 52520, 0, 67800, 90)
    SetChrPos(0x104, 51320, 0, 69000, 90)
    SetChrPos(0x106, 51320, 0, 67800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0005
    ChrTalk(
        0x101,
        "#0005F#5P这是……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#0204F#6P是这栋研究楼的\x01",
            "认证卡片吧。\x02\x03",

            "#0202F应该可以解除\x01",
            "升降机的限制锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6P呵……终于能够\x01",
            "到达核心区域了吗……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 51980, 0, 68000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xE3, 3)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_4_883 end

    SaveToFile()

Try(main)
