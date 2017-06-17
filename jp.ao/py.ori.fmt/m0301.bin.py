from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0301.bin",                # FileName
        "m0301",                    # MapName
        "m0301",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("m0301", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 1, 0, 2],
    )

    BuildStringList((
        "m0301",                  # 0
        "列車",                   # 1
        "SE制御",                 # 2
        "トライアタッカーＳⅡ",   # 3
        "bm0300",                 # 4
        "bm0300",                 # 5
        "bm0300",                 # 6
        "bm0300",                 # 7
    ))

    ATBonus("ATBonus_300", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_20E9", 5,   5,   5,   5,   10,  0,   0)

    MonsterBattlePostion("MonsterBattlePostion_360", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_340", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_518", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_20E9", 35, 35, 30, 0,
        (
            ("ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            ("ms84300.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            ("ms84300.dat", "ms84200.dat", "ms84100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3E0", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_20E9", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_47C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_20E9", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_360", "MonsterBattlePostion_3C0", "ed7450", "ed7453", "ATBonus_300"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_5B4", 0x0000, 64, 6, 45, 0, 1, 0, 0, "bm0300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "MonsterBattlePostion_340", "MonsterBattlePostion_3C0", "ed7451", "ed7453", "ATBonus_300"),
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
        "monster/ch84150.itc",               # 10
        "monster/ch84150.itc",               # 11
        "monster/ch84250.itc",               # 12
        "monster/ch84250.itc",               # 13
        "monster/ch84350.itc",               # 14
        "monster/ch84350.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(316000,  500,     -429000, 0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(1180,    -188330, -6000,   0x1010106,    "BattleInfo_518", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(298360,  -453460, 0,       0x1010150,    "BattleInfo_3E0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(298190,  -563160, 0,       0x10100C9,    "BattleInfo_47C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(301660,  -592270, -6000,   0x10100B2,    "BattleInfo_518", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(298800,  -201160, 0,       0x101013B,    "BattleInfo_518", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(513059,  -398170, 2530,    0x101010D,    "BattleInfo_3E0", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 13,  298.0,                 -453.0,                -11.0,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -29.80000114440918,    151.0,                 2.200000047683716,     1.0])

    DeclActor(316000,  0,       -429000, 1200,    316000,  1000,    -429000, 0x007C, 0,  3,  0x0000)
    DeclActor(0,       0,       -600000, 1200,    0,       1000,    -600000, 0x007C, 0,  4,  0x0000)
    DeclActor(5500,    0,       -3500,   1200,    5500,    1000,    -3500,   0x007C, 0,  6,  0x0000)
    DeclActor(498000,  0,       7500,    1200,    498000,  1000,    7500,    0x007C, 0,  8,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_688",          # 00, 0
        "Function_1_6A4",          # 01, 1
        "Function_2_716",          # 02, 2
        "Function_3_8A8",          # 03, 3
        "Function_4_ABF",          # 04, 4
        "Function_5_C10",          # 05, 5
        "Function_6_C14",          # 06, 6
        "Function_7_D74",          # 07, 7
        "Function_8_E83",          # 08, 8
        "Function_9_FE3",          # 09, 9
        "Function_10_10F2",        # 0A, 10
        "Function_11_1306",        # 0B, 11
        "Function_12_195C",        # 0C, 12
        "Function_13_19C1",        # 0D, 13
        "Function_14_1AB9",        # 0E, 14
        "Function_15_1ADB",        # 0F, 15
        "Function_16_1FA6",        # 10, 16
        "Function_17_2060",        # 11, 17
    ))


    def Function_0_688(): pass

    label("Function_0_688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A3")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_688")

    label("loc_6A3")

    Return()

    # Function_0_688 end

    def Function_1_6A4(): pass

    label("Function_1_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_6B3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_6B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CD")
    Event(0, 11)

    label("loc_6CD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E7")
    Event(0, 15)

    label("loc_6E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE")
    Event(0, 7)

    label("loc_6FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_715")
    Event(0, 9)

    label("loc_715")

    Return()

    # Function_1_6A4 end

    def Function_2_716(): pass

    label("Function_2_716")

    OP_C9(0x1, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_730")
    OP_C9(0x0, 0x8)

    label("loc_730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_743")
    OP_1B(0x5, 0x0, 0xA)

    label("loc_743")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_757")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_757")

    SetMapObjFlags(0x2, 0x4)
    SetScenarioFlags(0x0, 0)
    SetMapObjFrame(0xFF, "Null_onoff", 0x2, "on")
    OP_10(0x0, 0x0)
    OP_10(0x15, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B5")
    SetMapObjFrame(0x13, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x13, "Null_color2", 0x1, 0x1)
    Jump("loc_7DA")

    label("loc_7B5")

    SetMapObjFrame(0x13, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x13, "Null_color2", 0x0, 0x1)

    label("loc_7DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_818")
    SetMapObjFrame(0x14, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x14, "Null_color2", 0x0, 0x1)
    Jump("loc_83D")

    label("loc_818")

    SetMapObjFrame(0x14, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x14, "Null_color2", 0x1, 0x1)

    label("loc_83D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_850")
    OP_70(0x3, 0x0)
    Jump("loc_854")

    label("loc_850")

    OP_70(0x3, 0x1E)

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_867")
    OP_70(0x4, 0x0)
    Jump("loc_86B")

    label("loc_867")

    OP_70(0x4, 0x1E)

    label("loc_86B")

    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0x5, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A7")
    SoundLoad(825)
    SoundLoad(455)
    SoundLoad(451)

    label("loc_8A7")

    Return()

    # Function_2_716 end

    def Function_3_8A8(): pass

    label("Function_3_8A8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A79")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A7")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_905():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_905)

    def lambda_91F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_91F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_5B4", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_988"),
        (2, "loc_997"),
        (1, "loc_9A4"),
        (SWITCH_DEFAULT, "loc_9A7"),
    )


    label("loc_988")

    SetScenarioFlags(0x21B, 5)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_9A7")

    label("loc_997")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_9A4")

    OP_B9(0x0)
    Return()

    label("loc_9A7")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA0, 1)"), scpexpr(EXPR_END)), "loc_A04")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_A74")

    label("loc_A04")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A74")

    Jump("loc_AB3")

    label("loc_A79")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_AB3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8A8 end

    def Function_4_ABF(): pass

    label("Function_4_ABF")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBF")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_B48")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_BBA")

    label("loc_B48")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BBA")

    Jump("loc_C04")

    label("loc_BBF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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

    label("loc_C04")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_ABF end

    def Function_5_C10(): pass

    label("Function_5_C10")

    Call(1, 6)
    Return()

    # Function_5_C10 end

    def Function_6_C14(): pass

    label("Function_6_C14")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リフトの制御パネルがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6C")
    Fade(500)
    SetChrPos(0x0, 5000, 0, -5000, 0)
    SetChrPos(0x1, 6000, 0, -5000, 0)
    SetChrPos(0x2, 5000, 0, -6000, 0)
    SetChrPos(0x3, 6000, 0, -6000, 0)
    OP_68(4019, 0, -5780, 0)
    MoveCamera(18, 50, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x13, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(6000, 2000, 12000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0300", 126, 0, 0)
    IdleLoop()

    label("loc_D6C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_C14 end

    def Function_7_D74(): pass

    label("Function_7_D74")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x13, 0x64)
    Sleep(1)
    OP_68(6230, 2760, 4000, 0)
    MoveCamera(21, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, 2750, 7000, 270)
    OP_90(0x1, 3500, 2750, 6000, 270)
    OP_90(0x2, 4500, 2750, 7000, 270)
    OP_90(0x3, 4500, 2750, 6000, 270)
    Sound(145, 0, 100, 0)
    OP_68(6170, 0, -4200, 3200)
    MoveCamera(57, 27, 0, 3200)
    OP_71(0x13, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x13)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x13, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x13, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_7_D74 end

    def Function_8_E83(): pass

    label("Function_8_E83")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リフトの制御パネルがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDB")
    Fade(500)
    SetChrPos(0x0, 498500, 0, 7000, 270)
    SetChrPos(0x1, 498500, 0, 8000, 270)
    SetChrPos(0x2, 499500, 0, 7000, 270)
    SetChrPos(0x3, 499500, 0, 8000, 270)
    OP_68(501400, 0, 7660, 0)
    MoveCamera(51, 52, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x14, 0x2F8, 0x3B6, 0x0, 0x0)
    Sleep(200)
    OP_68(488000, -2000, 8000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0309", 107, 0, 0)
    IdleLoop()

    label("loc_FDB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_E83 end

    def Function_9_FE3(): pass

    label("Function_9_FE3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x14, 0x352)
    Sleep(1)
    OP_68(488270, -2500, 6610, 0)
    MoveCamera(61, 43, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 487500, -2500, 5500, 180)
    OP_90(0x1, 486500, -2500, 5500, 180)
    OP_90(0x2, 487500, -2500, 6500, 180)
    OP_90(0x3, 486500, -2500, 6500, 180)
    Sound(145, 0, 100, 0)
    OP_68(503180, -2500, 4750, 3200)
    MoveCamera(40, 45, 0, 3200)
    OP_71(0x14, 0x352, 0x2F8, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x14)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x14, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x14, "Null_color2", 0x1, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_FE3 end

    def Function_10_10F2(): pass

    label("Function_10_10F2")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(30500, -2000, -400000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 29500, -3000, -400500, 90)
    SetChrPos(0x102, 29500, -3000, -399500, 90)
    SetChrPos(0x103, 28400, -3000, -401000, 90)
    SetChrPos(0x104, 28400, -3000, -399000, 90)
    SetChrPos(0x109, 27300, -3000, -400500, 90)
    SetChrPos(0x105, 27300, -3000, -399500, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sound(196, 0, 80, 0)
    Sound(200, 0, 40, 0)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x101,
        "#6P#00013Fなんだ！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x109,
        (
            "#6P#10110Fこれは……\x01",
            "導力爆弾の起爆音！？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        "#00307Fその先だ、行ってみるぞ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 29000, -3000, -400000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 3)
    OP_1B(0x5, 0xFF, 0xFFFF)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_10F2 end

    def Function_11_1306(): pass

    label("Function_11_1306")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch51216.itc", 0x1E)
    SetChrPos(0x101, 276000, 0, -436400, 90)
    SetChrPos(0x102, 276000, 0, -437600, 90)
    SetChrPos(0x103, 275000, 0, -436000, 90)
    SetChrPos(0x104, 274800, 0, -438000, 90)
    SetChrPos(0x105, 273800, 0, -436400, 90)
    SetChrPos(0x109, 273800, 0, -437600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0x2E, 0x30, 0x30, 0x28, 0xB4, 0x0)
    OP_68(294000, -16500, -434000, 0)
    MoveCamera(30, 11, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(35500, 0)
    OP_68(294000, -1000, -434000, 9000)
    MoveCamera(30, 17, 0, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2500)

    def lambda_1442():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1442)
    Sleep(100)

    def lambda_145F():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_145F)
    Sleep(100)

    def lambda_147C():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_147C)
    Sleep(100)

    def lambda_1499():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1499)
    Sleep(100)

    def lambda_14B6():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14B6)
    Sleep(100)

    def lambda_14D3():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_14D3)

    def lambda_14ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14ED)
    Sleep(100)

    def lambda_1501():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1501)
    Sleep(100)

    def lambda_1515():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1515)
    Sleep(100)

    def lambda_1529():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1529)
    Sleep(100)

    def lambda_153D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_153D)
    Sleep(100)

    def lambda_1551():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1551)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(281000, 1000, -437000, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0013
    ChrTalk(
        0x105,
        (
            "#10308Fここは……\x01",
            "地下の貨物路線かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#6P#00101Fええ、オルキスタワー方面に\x01",
            "資材と貨物を運んでいるのだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x103, 0x2D, 0x1F4)

    #C0015
    ChrTalk(
        0x103,
        "#00201F#6P皆さん、あれを……！\x02",
    )

    CloseMessageWindow()
    OP_68(298000, 0, -409500, 3000)
    OP_6E(660, 3000)
    SetCameraDistance(22500, 3000)

    def lambda_1678():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1678)
    Sleep(50)

    def lambda_1688():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1688)
    Sleep(50)

    def lambda_1698():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1698)
    Sleep(50)

    def lambda_16A8():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_16A8)
    Sleep(50)

    def lambda_16B8():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16B8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    Sleep(500)
    OP_68(298000, -4500, -409500, 4000)
    MoveCamera(65, 20, 0, 4000)
    SetCameraDistance(30000, 4000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(298000, 0, -414500, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 298000, 0, -422100, 0)
    SetChrPos(0x102, 296200, 0, -423600, 0)
    SetChrPos(0x103, 296600, 0, -424900, 0)
    SetChrPos(0x104, 299000, 0, -423200, 0)
    SetChrPos(0x105, 298300, 0, -424500, 0)
    SetChrPos(0x109, 297600, 0, -423700, 0)
    OP_68(298000, 0, -410500, 2500)

    def lambda_17B5():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17B5)
    Sleep(100)

    def lambda_17D2():
        OP_97(0x104, 0x0, 0x0, 0x2710, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_17D2)
    Sleep(100)

    def lambda_17EF():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17EF)
    Sleep(100)

    def lambda_180C():
        OP_97(0x102, 0x0, 0x0, 0x2710, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_180C)
    Sleep(100)

    def lambda_1829():
        OP_97(0x105, 0x0, 0x0, 0x2710, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1829)
    Sleep(100)

    def lambda_1846():
        OP_97(0x103, 0x0, 0x0, 0x2710, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1846)
    WaitChrThread(0x101, 0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x103, 0)
    OP_6F(0x79)

    #C0016
    ChrTalk(
        0x109,
        "#10107F#11Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#00301F#11Pチッ……\x01",
            "追撃を振り切るつもりか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0018
    ChrTalk(
        0x101,
        (
            "#5P#00007F他にルートはないか\x01",
            "調べてみるぞ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 298000, 0, -413500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_11(0x2E, 0x30, 0x30, 0x19, 0x50, 0x0)
    SetScenarioFlags(0x143, 4)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_1306 end

    def Function_12_195C(): pass

    label("Function_12_195C")


    def lambda_1961():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1961)
    Sleep(50)

    def lambda_1971():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1971)
    Sleep(50)

    def lambda_1981():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1981)
    Sleep(50)

    def lambda_1991():
        OP_93(0x105, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1991)
    Sleep(50)

    def lambda_19A1():
        OP_93(0x109, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19A1)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    Return()

    # Function_12_195C end

    def Function_13_19C1(): pass

    label("Function_13_19C1")

    ClearChrFlags(0x8, 0x80)
    OP_78(0x2, 0x8)
    Sleep(1)
    SetChrPos(0x8, 290000, -18000, -500000, 0)
    OP_D5(0x8, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetScenarioFlags(0x143, 5)
    ModifyEventFlags(0, 0, 0x80)
    ClearScenarioFlags(0x0, 0)
    SetMapObjFrame(0xFF, "Null_onoff", 0x2, "off_")
    OP_C9(0x0, 0x20)
    MoveCamera(40, 15, 0, 2000)
    OP_6E(700, 2000)
    SetCameraDistance(35000, 2000)
    BeginChrThread(0x9, 1, 0, 14)
    OP_82(0x64, 0x64, 0xBB8, 0x1F40)
    OP_96(0x8, 0x46CD0, 0xFFFFB9B0, 0xFFFC2F70, 0x7530, 0x0)
    OP_6F(0x79)
    MoveCamera(45, 40, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(30000, 2000)
    OP_6F(0x79)
    OP_C9(0x1, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAC")
    SetMapObjFrame(0xFF, "Null_onoff", 0x2, "on_")

    label("loc_1AAC")

    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x2, 0x1000)
    Return()

    # Function_13_19C1 end

    def Function_14_1AB9(): pass

    label("Function_14_1AB9")

    Sound(455, 0, 100, 0)
    Sound(451, 2, 100, 0)
    Sound(825, 2, 80, 0)
    Sleep(6000)
    StopSound(451, 1000, 100)
    StopSound(825, 1000, 80)
    Return()

    # Function_14_1AB9 end

    def Function_15_1ADB(): pass

    label("Function_15_1ADB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_68(281000, -3000, -397000, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 276000, -4000, -397600, 90)
    SetChrPos(0x102, 276000, -4000, -396400, 90)
    SetChrPos(0x104, 275000, -4000, -396000, 90)
    SetChrPos(0x103, 274800, -4000, -398000, 90)
    SetChrPos(0x109, 273800, -4000, -396400, 90)
    SetChrPos(0x105, 273800, -4000, -397600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetCameraDistance(18000, 2000)
    FadeToBright(2000, 0)

    def lambda_1BEA():
        OP_97(0x101, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BEA)
    Sleep(150)

    def lambda_1C07():
        OP_97(0x103, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C07)
    Sleep(150)

    def lambda_1C24():
        OP_97(0x105, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1C24)
    Sleep(150)

    def lambda_1C41():
        OP_97(0x102, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C41)
    Sleep(150)

    def lambda_1C5E():
        OP_97(0x104, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C5E)
    Sleep(150)

    def lambda_1C7B():
        OP_97(0x109, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1C7B)

    def lambda_1C95():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C95)
    Sleep(300)

    def lambda_1CA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1CA9)
    Sleep(300)

    def lambda_1CBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1CBD)
    Sleep(300)

    def lambda_1CD1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CD1)
    Sleep(300)

    def lambda_1CE5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CE5)
    Sleep(300)

    def lambda_1CF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1CF9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(600)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)

    def lambda_1DBB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DBB)

    def lambda_1DC8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1DC8)
    Sleep(50)

    def lambda_1DD8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1DD8)

    def lambda_1DE5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1DE5)
    Sleep(50)

    def lambda_1DF5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DF5)

    def lambda_1E02():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1E02)
    Sleep(150)

    #C0019
    ChrTalk(
        0x109,
        "#10100Fあ……！\x02",
    )

    CloseMessageWindow()
    OP_68(298000, 0, -409500, 3000)
    MoveCamera(30, 25, 0, 3000)
    OP_6E(660, 3000)
    SetCameraDistance(22500, 3000)
    OP_6F(0x79)
    SetChrPos(0x104, 280000, -10000, -396000, 135)
    SetChrPos(0x105, 278800, -10000, -397600, 135)
    Sleep(300)

    #C0020
    ChrTalk(
        0x104,
        "#00302Fよっしゃ、回りこめたか！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、連中はこちらを\x01",
            "撒#2Rま#けたと思っているだろうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x104, 280000, -4000, -396000, 135)
    SetChrPos(0x105, 278800, -4000, -397600, 135)
    Fade(250)
    OP_68(281000, -3000, -397000, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0022
    ChrTalk(
        0x101,
        (
            "#00000F#11Pああ……\x01",
            "追いつくチャンスだ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 280500, -4000, -397000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_1ADB end

    def Function_16_1FA6(): pass

    label("Function_16_1FA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    SoundLoad(931)
    SoundLoad(825)
    OP_68(292000, -13500, -457000, 0)
    MoveCamera(33, 31, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(25000, 0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_75(0x15, 0x2, 0x1B58)
    OP_7D(0xFF, 0xFF, 0x69, 0x0, 0x2328)
    Sound(930, 0, 100, 0)
    OP_68(292000, -13500, -407000, 9000)
    MoveCamera(33, 27, 10, 9000)
    SetCameraDistance(27000, 9000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x9, 1, 0, 17)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1FA6 end

    def Function_17_2060(): pass

    label("Function_17_2060")

    Sound(931, 2, 30, 0)
    Sound(825, 2, 30, 0)
    Sleep(400)
    OP_25(0x3A3, 0x28)
    OP_25(0x339, 0x28)
    Sleep(400)
    OP_25(0x3A3, 0x32)
    OP_25(0x339, 0x32)
    Sleep(400)
    OP_25(0x3A3, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(400)
    OP_25(0x3A3, 0x46)
    OP_25(0x339, 0x46)
    Sleep(400)
    OP_25(0x3A3, 0x50)
    OP_25(0x339, 0x50)
    Sleep(400)
    OP_25(0x339, 0x5A)
    Sleep(400)
    OP_25(0x339, 0x64)
    Sleep(4200)
    StopSound(931, 1000, 80)
    StopSound(825, 1000, 100)
    Return()

    # Function_17_2060 end

    SaveToFile()

Try(main)
