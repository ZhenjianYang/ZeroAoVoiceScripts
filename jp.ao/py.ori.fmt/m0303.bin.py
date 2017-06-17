from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m0303.bin",                # FileName
        "m0303",                    # MapName
        "m0303",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 0, 0, 1],
    )

    BuildStringList((
        "m0303",                  # 0
        "帝国系テロリスト",       # 1
        "帝国系テロリスト",       # 2
        "帝国系テロリスト",       # 3
        "帝国系テロリスト",       # 4
        "帝国系テロリスト",       # 5
        "帝国系テロリスト",       # 6
        "帝国系テロリスト",       # 7
        "帝国系テロリスト",       # 8
        "SE制御",                 # 9
        "bm0300",                 # 10
        "bm0300",                 # 11
        "bm0300",                 # 12
    ))

    ATBonus("ATBonus_33C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_2C14", 5,   5,   5,   5,   10,  0,   0)

    MonsterBattlePostion("MonsterBattlePostion_39C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_400", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_404", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_408", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_40C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_410", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_414", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_37C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_4B8", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_2C14", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_41C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_2C14", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_554", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_2C14", 35, 35, 30, 0,
        (
            ("ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            ("ms84300.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_37C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
            ("ms84300.dat", "ms84200.dat", "ms84100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_39C", "MonsterBattlePostion_3FC", "ed7450", "ed7453", "ATBonus_33C"),
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-22620,  -8090,   -8000,   0x101010C,    "BattleInfo_4B8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(13860,   -8070,   -8000,   0x1010110,    "BattleInfo_41C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(34140,   -24130,  -8000,   0x1010066,    "BattleInfo_554", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(390,     -13070,  -16000,  0x10100BD,    "BattleInfo_41C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-22200,  -30400,  -16000,  0x101002D,    "BattleInfo_4B8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-4030,   -37410,  -16000,  0x1010005,    "BattleInfo_554", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0000, 0, 5,   0.0,                   -14.0,                 -1.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.799999952316284,     0.20000000298023224,   1.0])

    DeclActor(-32000,  -16000,  -24000,  1200,    -32000,  -15000,  -24000,  0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_6A0",          # 00, 0
        "Function_1_6CC",          # 01, 1
        "Function_2_762",          # 02, 2
        "Function_3_8B3",          # 03, 3
        "Function_4_F48",          # 04, 4
        "Function_5_FAD",          # 05, 5
        "Function_6_1F77",         # 06, 6
        "Function_7_21F1",         # 07, 7
        "Function_8_235B",         # 08, 8
        "Function_9_24B8",         # 09, 9
        "Function_10_27B2",        # 0A, 10
        "Function_11_27DF",        # 0B, 11
        "Function_12_2806",        # 0C, 12
        "Function_13_282D",        # 0D, 13
        "Function_14_2854",        # 0E, 14
        "Function_15_287B",        # 0F, 15
        "Function_16_28A2",        # 10, 16
        "Function_17_28D8",        # 11, 17
        "Function_18_290E",        # 12, 18
        "Function_19_2944",        # 13, 19
        "Function_20_297A",        # 14, 20
        "Function_21_29B0",        # 15, 21
        "Function_22_29F5",        # 16, 22
        "Function_23_2A2B",        # 17, 23
        "Function_24_2A70",        # 18, 24
        "Function_25_2BBD",        # 19, 25
    ))


    def Function_0_6A0(): pass

    label("Function_0_6A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BA")
    Event(0, 3)

    label("loc_6BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CB")
    SetScenarioFlags(0x151, 0)

    label("loc_6CB")

    Return()

    # Function_0_6A0 end

    def Function_1_6CC(): pass

    label("Function_1_6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E0")
    OP_C9(0x0, 0x8)

    label("loc_6E0")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 0)), scpexpr(EXPR_END)), "loc_728")
    SetMapObjFrame(0x2, "lock_g", 0x1, 0x1)
    SetMapObjFrame(0x2, "lock_r", 0x0, 0x1)
    SetMapObjFlags(0x2, 0x10)
    Jump("loc_74A")

    label("loc_728")

    SetMapObjFrame(0x2, "lock_g", 0x0, 0x1)
    SetMapObjFrame(0x2, "lock_r", 0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75D")
    OP_70(0x0, 0x0)
    Jump("loc_761")

    label("loc_75D")

    OP_70(0x0, 0x1E)

    label("loc_761")

    Return()

    # Function_1_6CC end

    def Function_2_762(): pass

    label("Function_2_762")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_862")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_7EB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_85D")

    label("loc_7EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_85D")

    Jump("loc_8A7")

    label("loc_862")

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

    label("loc_8A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_762 end

    def Function_3_8B3(): pass

    label("Function_3_8B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(852)
    SetChrPos(0x101, -900, 0, 4400, 180)
    SetChrPos(0x102, 500, 0, 4400, 180)
    SetChrPos(0x103, -1900, 0, 5300, 180)
    SetChrPos(0x104, 1900, 0, 5300, 180)
    SetChrPos(0x109, -500, 0, 5900, 180)
    SetChrPos(0x105, 900, 0, 5900, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(16000, -16000, -25000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24000, 0)
    OP_68(-16000, -16000, -25000, 8000)
    SetCameraDistance(29000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-15500, -7000, -31000, 0)
    MoveCamera(27, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13500, 0)
    OP_68(-20500, -1000, -31000, 7000)
    MoveCamera(35, 17, 0, 7000)
    SetCameraDistance(32500, 7000)
    OP_0D()
    Sleep(2500)
    PlaceName2(340, 200, "c_plac53", 0x0, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1000, 5000, 0)
    MoveCamera(43, 21, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(18500, 1000)
    OP_0D()
    OP_6F(0x79)

    #C0004
    ChrTalk(
        0x101,
        "#6P#00005Fここは……地下の駐車場か？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#6P#00108Fええ、いずれ車社会が\x01",
            "クロスベルに到来した時のために\x01",
            "建造された区画なんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        (
            "#00306F#5Pいや、それにしたって\x01",
            "デカすぎねぇか？\x02\x03",

            "#00301Fそんな需要があるとは\x01",
            "とても思えねぇんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x105,
        (
            "#10302F#5P察するに議員と役人たちが\x01",
            "ありもしない需要をでっち上げて\x01",
            "工事を発注したってところかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        "#10106F#5P……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#6P#00103F……ええ。\x01",
            "残念だけどそういうことね。\x02\x03",

            "#00108F今はハルトマン議長の失脚で\x01",
            "一時中断しているみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#6P#00006Fまあ、それが正解だろうな。\x02\x03",

            "#00001Fしかし……ここまで広いと\x01",
            "追跡するのも大変そうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        "#5P#00200F………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    VolumeBGM(0x46, 0x3E8)
    Sound(2278, 255, 70, 0)    #voice#Tio
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(812, 0, 100, 0)
    OP_0D()
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 4)
    Sound(357, 0, 70, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Fade(250)
    Sound(812, 0, 100, 0)
    StopSound(852, 500, 100)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    #C0012
    ChrTalk(
        0x103,
        (
            "#5P#00203F……人らしき反応を確認。\x02\x03",

            "#00201Fどうやら８名ほどの集団が\x01",
            "この付近を移動中のようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#12P#00000F本当か……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#00302F#11Pヘッ、意外と\x01",
            "早く追いつけそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(150)

    #C0015
    ChrTalk(
        0x109,
        "#10101F#5P急ぎましょう！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 0, 0, 5000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 1)
    ModifyEventFlags(1, 0, 0x80)
    OP_24(0x354)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_3_8B3 end

    def Function_4_F48(): pass

    label("Function_4_F48")


    def lambda_F4D():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F4D)
    Sleep(50)

    def lambda_F5D():
        TurnDirection(0x109, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F5D)
    Sleep(50)

    def lambda_F6D():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F6D)
    Sleep(50)

    def lambda_F7D():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F7D)
    Sleep(50)

    def lambda_F8D():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F8D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    Return()

    # Function_4_F48 end

    def Function_5_FAD(): pass

    label("Function_5_FAD")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch42200.itc", 0x1E)
    LoadChrToIndex("chr/ch42250.itc", 0x1F)
    LoadChrToIndex("chr/ch42251.itc", 0x20)
    LoadChrToIndex("chr/ch42300.itc", 0x21)
    LoadChrToIndex("chr/ch42350.itc", 0x22)
    LoadChrToIndex("chr/ch42351.itc", 0x23)
    LoadChrToIndex("apl/ch51240.itc", 0x24)
    LoadChrToIndex("apl/ch51239.itc", 0x25)
    LoadChrToIndex("chr/ch00056.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00151.itc", 0x28)
    LoadChrToIndex("apl/ch51242.itc", 0x29)
    LoadChrToIndex("chr/ch00156.itc", 0x2A)
    LoadChrToIndex("chr/ch00250.itc", 0x2B)
    LoadChrToIndex("chr/ch00254.itc", 0x2C)
    LoadChrToIndex("chr/ch00256.itc", 0x2D)
    LoadChrToIndex("chr/ch00356.itc", 0x2E)
    LoadChrToIndex("chr/ch02950.itc", 0x2F)
    LoadChrToIndex("chr/ch02951.itc", 0x30)
    LoadChrToIndex("apl/ch51241.itc", 0x31)
    LoadChrToIndex("chr/ch0295F.itc", 0x32)
    LoadChrToIndex("chr/ch0305F.itc", 0x33)
    LoadChrToIndex("chr/ch42353.itc", 0x34)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    LoadEffect(0x2, "battle/mgaria0.eff")
    LoadEffect(0x3, "battle/mgaria1.eff")
    LoadEffect(0x4, "battle/mg040_00.eff")
    LoadEffect(0x5, "event/eva01_00.eff")
    LoadEffect(0x6, "battle/cr425100.eff")
    LoadEffect(0x7, "event/eva01_01.eff")
    LoadEffect(0x8, "event/ev17034.eff")
    SoundLoad(860)
    SoundLoad(861)
    OP_68(0, 1000, -14600, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 0, 0, -12000, 180)
    SetChrPos(0x102, 900, 0, -10800, 180)
    SetChrPos(0x103, -900, 0, -11200, 180)
    SetChrPos(0x104, 900, 0, -9400, 180)
    SetChrPos(0x109, -900, 0, -9800, 180)
    SetChrPos(0x105, 0, 0, -8600, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -25200, -8000, -7000, 90)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, -26400, -8000, -7900, 90)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, -26600, -8000, -5300, 90)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, -27200, -8000, -6400, 90)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x4)
    SetChrPos(0xC, -27000, -8000, -9000, 90)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    SetChrPos(0xD, -29100, -8000, -8400, 90)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, -28700, -8000, -7100, 90)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x4)
    SetChrPos(0xF, -28300, -8000, -5800, 90)

    def lambda_12E2():
        OP_97(0x101, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12E2)
    Sleep(100)

    def lambda_12FF():
        OP_97(0x102, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12FF)
    Sleep(100)

    def lambda_131C():
        OP_97(0x103, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_131C)
    Sleep(100)

    def lambda_1339():
        OP_97(0x104, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1339)
    Sleep(100)

    def lambda_1356():
        OP_97(0x109, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1356)
    Sleep(100)

    def lambda_1373():
        OP_97(0x105, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1373)
    SetCameraDistance(18000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0xBB8)
    WaitChrThread(0x103, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x103, 0x10E, 0x1F4)

    #C0016
    ChrTalk(
        0x103,
        (
            "#12P#00201F（あ……）\x02\x03",

            "#00207F（……皆さん、あそこです！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_140B():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_140B)
    Sleep(50)

    def lambda_141B():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_141B)
    Sleep(50)

    def lambda_142B():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_142B)
    Sleep(50)

    def lambda_143B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_143B)
    Sleep(50)

    def lambda_144B():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_144B)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x101,
        "#00007F#11P（あ──）\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x105,
        "#11P#10310F（まずい……！）\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)
    ReplaceBGM("ed7300", "ed7544")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_68(-23000, -6500, -8000, 3000)
    Sleep(2000)

    def lambda_1575():
        OP_97(0x8, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1575)
    Sleep(50)

    def lambda_1592():
        OP_97(0x9, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1592)
    Sleep(50)

    def lambda_15AF():
        OP_97(0xA, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_15AF)
    Sleep(50)

    def lambda_15CC():
        OP_97(0xB, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_15CC)
    Sleep(50)

    def lambda_15E9():
        OP_97(0xC, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_15E9)
    Sleep(50)

    def lambda_1606():
        OP_97(0xD, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1606)
    Sleep(50)

    def lambda_1623():
        OP_97(0xE, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1623)
    Sleep(50)

    def lambda_1640():
        OP_97(0xF, 0x32C8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_1640)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-14000, -6700, -7000, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_F0(0x0, 0x1)
    OP_0D()
    SetChrPos(0x101, -400, 0, -10500, 270)
    SetChrPos(0x102, 0, 0, -9500, 270)
    SetChrPos(0x103, -700, 0, -7100, 270)
    SetChrPos(0x104, 300, 0, -7900, 270)
    SetChrPos(0x109, -1000, 0, -8500, 270)
    SetChrPos(0x105, 0, 0, -6200, 270)
    WaitChrThread(0x8, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x9, 0)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    WaitChrThread(0xA, 0)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0xB, 0)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    WaitChrThread(0xC, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    WaitChrThread(0xD, 0)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    WaitChrThread(0xE, 0)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    WaitChrThread(0xF, 0)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    Sleep(1000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)

    #C0019
    ChrTalk(
        0x8,
        "#5Pなに……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "#5Pなんだ、あいつらは！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x1)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x1)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x1)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    Sleep(1000)

    #C0021
    ChrTalk(
        0x9,
        "#5P追っ手か！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        (
            "#5Pチッ……\x01",
            "どうして嗅ぎつけた！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3000, -100, -9500, 2000)
    MoveCamera(315, 33, 0, 2000)
    SetCameraDistance(15500, 2000)
    BeginChrThread(0x10, 1, 0, 25)
    BeginChrThread(0xA, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0xD, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0xF, 3, 0, 7)
    BeginChrThread(0x101, 2, 0, 6)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 13)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x105, 3, 0, 15)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 14)
    OP_6F(0x79)

    #C0023
    ChrTalk(
        0x101,
        "#12P#00010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#00301Fちいっ……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)

    #C0025
    ChrTalk(
        0x109,
        "#10107Fこの～っ……！\x02",
    )

    CloseMessageWindow()
    OP_68(-4000, -500, -9500, 1000)
    MoveCamera(323, 33, 0, 1000)
    SetCameraDistance(15000, 1000)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2F)
    SetChrSubChip(0x109, 0x0)

    def lambda_19E5():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFDF94, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19E5)
    WaitChrThread(0x109, 1)
    SetChrChipByIndex(0x109, 0x31)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x20)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    BeginChrThread(0x109, 3, 0, 8)
    PlayEffect(0x6, 0x2, 0xFF, 0x0, -11500, -8000, -7200, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x8, 0x3)

    #C0026
    ChrTalk(
        0x8,
        "#5Pうおっ……！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "小銃で武装しているぞ！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 7)

    #C0028
    ChrTalk(
        0x102,
        "#12P#00107Fどいて、ノエルさん！\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)

    def lambda_1AC5():
        OP_96(0xFE, 0xFFFFFAEC, 0x0, 0xFFFFDA1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1AC5)
    WaitChrThread(0x102, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x102, 3, 0, 9)
    OP_AD(0x0)

    #C0029
    ChrTalk(
        0x9,
        "ちいっ……！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "#5P動け！\x01",
            "その場に留まるな！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x10, 0x1)
    OP_68(15000, -6500, -7000, 6000)
    MoveCamera(45, 33, 0, 6000)
    SetCameraDistance(15000, 6000)
    BeginChrThread(0x8, 3, 0, 16)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 17)
    Sleep(100)
    StopSound(860, 600, 50)
    StopSound(861, 600, 70)
    BeginChrThread(0xA, 3, 0, 18)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 24)
    BeginChrThread(0xB, 3, 0, 19)
    Sleep(100)
    BeginChrThread(0xC, 3, 0, 20)
    Sleep(100)
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(400)
    BeginChrThread(0xD, 3, 0, 21)
    Sleep(400)
    BeginChrThread(0xF, 3, 0, 23)
    EndChrThread(0x101, 0x2)
    WaitChrThread(0xD, 3)
    StopEffect(0x2, 0x2)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x102, 0x3)

    #C0031
    ChrTalk(
        0xD,
        (
            "#11Pくっ……\x01",
            "なんだ、あのガキどもは！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF, 3)

    #C0032
    ChrTalk(
        0xF,
        (
            "#5P構うな！\x01",
            "このまま離脱するぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)

    def lambda_1C32():
        OP_97(0xFE, 0x32C8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C32)
    Sleep(100)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)

    def lambda_1C57():
        OP_97(0xFE, 0x32C8, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C57)
    WaitChrThread(0xF, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0x8, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0xB, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Fade(500)
    OP_68(500, 1000, -8500, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x20)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0x2B)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, 500, 0, -10500, 90)
    SetChrPos(0x102, -300, 0, -9700, 90)
    SetChrPos(0x103, -500, 0, -6900, 90)
    SetChrPos(0x104, 1300, 0, -7900, 90)
    SetChrPos(0x109, -1000, 0, -8300, 90)
    SetChrPos(0x105, 1000, 0, -6200, 90)
    OP_0D()

    #C0033
    ChrTalk(
        0x103,
        "#6P#00206Fふう……外しました。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        (
            "#5P#10302Fフフ、うちの女性陣は\x01",
            "揃いも揃って勇ましいねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#00007Fとにかく追いかけるぞ！\x02\x03",

            "多分、あそこまで降りる\x01",
            "ルートがあるはずだ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E67():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1E67)
    Sleep(50)

    def lambda_1E77():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1E77)
    Sleep(50)

    def lambda_1E87():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1E87)
    Sleep(50)

    def lambda_1E97():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E97)
    Sleep(50)

    def lambda_1EA7():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1EA7)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0036
    ChrTalk(
        0x104,
        (
            "#00307Fおお、こうなりゃ\x01",
            "意地でも捕まえてやるぜ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
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
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    OP_D7(0x2D)
    OP_D7(0x2E)
    OP_D7(0x2F)
    OP_D7(0x30)
    OP_D7(0x31)
    OP_D7(0x32)
    OP_D7(0x33)
    OP_D7(0x34)
    OP_37()
    SetChrPos(0x0, 0, 0, -12000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x143, 2)
    ModifyEventFlags(0, 0, 0x80)
    OP_29(0xA4, 0x1, 0x8)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_5_FAD end

    def Function_6_1F77(): pass

    label("Function_6_1F77")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_21F0")
    OP_82(0x64, 0x64, 0xBB8, 0x384)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 0, -8400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 800, -9500, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 0, -10300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 500, -7500, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 0, -9600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 500, -8800, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x64, 0xBB8, 0x384)
    Sleep(200)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 0, -7100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 800, -10000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1800, 0, -10800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -2000, 800, -8000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jump("Function_6_1F77")

    label("loc_21F0")

    Return()

    # Function_6_1F77 end

    def Function_7_21F1(): pass

    label("Function_7_21F1")

    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x20)

    label("loc_2208")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_235A")

    def lambda_2218():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2218)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 800, 1500, 0, -50, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 800, 1500, 0, -50, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 800, 1500, 0, -50, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 800, 1500, 0, -50, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 800, 1500, 0, -50, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(700)
    Jump("loc_2208")

    label("loc_235A")

    Return()

    # Function_7_21F1 end

    def Function_8_235B(): pass

    label("Function_8_235B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B7")
    Sound(539, 0, 70, 0)
    SetChrSubChip(0xFE, 0x1)

    def lambda_2375():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2375)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Jump("Function_8_235B")

    label("loc_24B7")

    Return()

    # Function_8_235B end

    def Function_9_24B8(): pass

    label("Function_9_24B8")

    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    def lambda_24C4():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24C4)
    Sound(530, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 500, 0, 30, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x8, 0xFF, 0x9, 0x1, 0, 1000, -15000, 270, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0x9, 0x1, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_2595():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2595)
    EndChrThread(0x9, 0x3)
    SetChrChipByIndex(0x9, 0x34)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)

    def lambda_25D3():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25D3)
    Sound(530, 0, 80, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 500, 0, 30, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x8, 0xFF, 0xD, 0x1, 0, 1000, -15000, 270, 25, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x7, 0xFF, 0xD, 0x1, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(501, 0, 100, 0)

    def lambda_26A4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_26A4)
    EndChrThread(0xD, 0x3)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x20)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xD, 0x2)
    Sleep(300)
    SetScenarioFlags(0x0, 0)

    label("loc_26D9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B1")
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)

    def lambda_26F0():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26F0)
    Sound(530, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)

    def lambda_2754():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2754)
    Sound(530, 0, 70, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1000, 0, 0, 45, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    Jump("loc_26D9")

    label("loc_27B1")

    Return()

    # Function_9_24B8 end

    def Function_10_27B2(): pass

    label("Function_10_27B2")


    def lambda_27B7():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27B7)
    WaitChrThread(0xFE, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_10_27B2 end

    def Function_11_27DF(): pass

    label("Function_11_27DF")


    def lambda_27E4():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27E4)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_11_27DF end

    def Function_12_2806(): pass

    label("Function_12_2806")


    def lambda_280B():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_280B)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_12_2806 end

    def Function_13_282D(): pass

    label("Function_13_282D")


    def lambda_2832():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2832)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_13_282D end

    def Function_14_2854(): pass

    label("Function_14_2854")


    def lambda_2859():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2859)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x32)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_14_2854 end

    def Function_15_287B(): pass

    label("Function_15_287B")


    def lambda_2880():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2880)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_287B end

    def Function_16_28A2(): pass

    label("Function_16_28A2")

    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_28BE():
        OP_96(0xFE, 0x8CA0, 0x0, 0xFFFFE4A8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28BE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_28A2 end

    def Function_17_28D8(): pass

    label("Function_17_28D8")

    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_28F4():
        OP_96(0xFE, 0x8CA0, 0x0, 0xFFFFE124, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_28F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_17_28D8 end

    def Function_18_290E(): pass

    label("Function_18_290E")

    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_292A():
        OP_96(0xFE, 0x8CA0, 0x0, 0xFFFFEB4C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_292A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_18_290E end

    def Function_19_2944(): pass

    label("Function_19_2944")

    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_2960():
        OP_96(0xFE, 0x8CA0, 0x0, 0xFFFFE700, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2960)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_19_2944 end

    def Function_20_297A(): pass

    label("Function_20_297A")

    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_2996():
        OP_96(0xFE, 0x8CA0, 0x0, 0xFFFFDCD8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2996)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_20_297A end

    def Function_21_29B0(): pass

    label("Function_21_29B0")

    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_29CC():
        OP_96(0xFE, 0x3A98, 0xFFFFE0C0, 0xFFFFDF30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29CC)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_21_29B0 end

    def Function_22_29F5(): pass

    label("Function_22_29F5")

    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_2A11():
        OP_96(0xFE, 0x8CA0, 0x0, 0xFFFFE444, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A11)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_29F5 end

    def Function_23_2A2B(): pass

    label("Function_23_2A2B")

    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x2)

    def lambda_2A47():
        OP_96(0xFE, 0x3A98, 0xFFFFE0C0, 0xFFFFE958, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A47)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    TurnDirection(0xFE, 0xD, 500)
    Return()

    # Function_23_2A2B end

    def Function_24_2A70(): pass

    label("Function_24_2A70")

    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    Sound(357, 0, 100, 0)
    PlayEffect(0x2, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    PlayEffect(0x3, 0x1, 0x103, 0x5, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x103, 0x3)
    Sound(2221, 255, 80, 0)    #voice#Tio
    Sound(259, 0, 50, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x5, 16300, -8000, -8400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(259, 0, 50, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x5, 16300, -8000, -5800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_24_2A70 end

    def Function_25_2BBD(): pass

    label("Function_25_2BBD")

    Sound(531, 0, 100, 0)
    Sound(861, 2, 80, 0)

    label("loc_2BC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BEB")
    Sound(860, 2, 60, 0)
    Sleep(700)
    StopSound(860, 200, 50)
    Sleep(200)
    Jump("loc_2BC9")

    label("loc_2BEB")

    Return()

    # Function_25_2BBD end

    SaveToFile()

Try(main)
