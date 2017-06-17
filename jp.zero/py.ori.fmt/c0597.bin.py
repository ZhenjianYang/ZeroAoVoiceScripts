from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0597.bin",                # FileName
        "c0597",                    # MapName
        "c0597",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0597",                  # 0
        "マフィア",               # 1
        "マフィア",               # 2
        "マフィア",               # 3
        "マフィア",               # 4
        "マフィア",               # 5
        "ガルシア",               # 6
        "マルコーニ会長",         # 7
        "レジェネンコフ",         # 8
        "ムスタング",             # 9
        "ムスタング",             # 10
        "ランディ",               # 11
        "エリィ",                 # 12
        "ティオ",                 # 13
        "ダドリー捜査官",         # 14
        "bc0510",                 # 15
    ))

    ATBonus("ATBonus_38C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_430", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_434", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_438", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_440", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_444", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_46C", 0x0012, 34, 6, 180, 0, 0, 0, 0, "bc0510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68200.dat", "ms68300.dat", "ms68300.dat", 0, 0, 0, "ms68300.dat", 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_42C", "ed7402", "ed7403", "ATBonus_38C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00300.itc",                   # 00
        "chr/ch00100.itc",                   # 01
        "chr/ch00200.itc",                   # 02
        "chr/ch00900.itc",                   # 03
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
        "monster/ch68250.itc",               # 10
        "monster/ch68251.itc",               # 11
        "monster/ch68350.itc",               # 12
        "monster/ch68350.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-6599,   0,       112099,  0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4000,    0,       106000,  90,   389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3019,   29,      111360,  90,   389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6699,    0,       101599,  90,   389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclEvent(0x0000, 0, 13,  0.0,                   48.0,                  -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -16.0,                 0.20000000298023224,   1.0])

    DeclActor(0,       0,       114800,  1200,    0,       1100,    116500,  0x007C, 0,  6,  0x0000)
    DeclActor(7700,    0,       113500,  1200,    7700,    1500,    113500,  0x007C, 0,  17, 0x0000)
    DeclActor(6000,    0,       6000,    1200,    6000,    1500,    6000,    0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       64000,   1200,    0,       1500,    64000,   0x007C, 0,  20, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_538",          # 00, 0
        "Function_1_5F0",          # 01, 1
        "Function_2_60F",          # 02, 2
        "Function_3_62B",          # 03, 3
        "Function_4_67D",          # 04, 4
        "Function_5_716",          # 05, 5
        "Function_6_821",          # 06, 6
        "Function_7_A08",          # 07, 7
        "Function_8_B44",          # 08, 8
        "Function_9_CE6",          # 09, 9
        "Function_10_E7B",         # 0A, 10
        "Function_11_FBE",         # 0B, 11
        "Function_12_1C43",        # 0C, 12
        "Function_13_25A3",        # 0D, 13
        "Function_14_3132",        # 0E, 14
        "Function_15_3561",        # 0F, 15
        "Function_16_3DA9",        # 10, 16
        "Function_17_3DFE",        # 11, 17
        "Function_18_3E52",        # 12, 18
        "Function_19_405A",        # 13, 19
        "Function_20_5CEE",        # 14, 20
        "Function_21_6076",        # 15, 21
    ))


    def Function_0_538(): pass

    label("Function_0_538")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_578"),
        (1, "loc_584"),
        (2, "loc_590"),
        (3, "loc_59C"),
        (4, "loc_5A8"),
        (5, "loc_5B4"),
        (6, "loc_5C0"),
        (SWITCH_DEFAULT, "loc_5CC"),
    )


    label("loc_578")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_584")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_590")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_59C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5EF")

    Return()

    # Function_0_538 end

    def Function_1_5F0(): pass

    label("Function_1_5F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_5F0")

    label("loc_60E")

    Return()

    # Function_1_5F0 end

    def Function_2_60F(): pass

    label("Function_2_60F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62A")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_60F")

    label("loc_62A")

    Return()

    # Function_2_60F end

    def Function_3_62B(): pass

    label("Function_3_62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_645")
    Event(0, 15)

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_659")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)
    Jump("loc_67C")

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_66D")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 12)
    Jump("loc_67C")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_67C")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 14)

    label("loc_67C")

    Return()

    # Function_3_62B end

    def Function_4_67D(): pass

    label("Function_4_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_692")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_692")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6AA")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C8")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_6C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6D5")
    OP_70(0x11, 0xA)

    label("loc_6D5")

    SetMapObjFlags(0x13, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6F3")
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x10, 0x10)
    Jump("loc_6FD")

    label("loc_6F3")

    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x10, 0x10)

    label("loc_6FD")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_715")
    OP_1B(0x2, 0x0, 0x15)

    label("loc_715")

    Return()

    # Function_4_67D end

    def Function_5_716(): pass

    label("Function_5_716")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_803")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_81F")

    Return()

    # Function_5_716 end

    def Function_6_821(): pass

    label("Function_6_821")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 1000, 116100, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 0, 115100, 0)
    OP_0D()
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には頑丈そうな鍵が掛かっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_928")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "宝箱の鍵を使う\x01",      # 0
            "止めておく\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_903"),
        (1, "loc_90B"),
        (SWITCH_DEFAULT, "loc_923"),
    )


    label("loc_903")

    Call(0, 19)
    Jump("loc_923")

    label("loc_90B")

    SetChrPos(0x0, 0, 0, 114700, 180)
    EventEnd(0x5)
    Jump("loc_923")

    label("loc_923")

    Jump("loc_A07")

    label("loc_928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_975")

    #C0003
    ChrTalk(
        0x101,
        (
            "#0001F#11P（鍵が必要だな……\x01",
            "  部屋の中を調べてみるか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EE")

    label("loc_975")


    #C0004
    ChrTalk(
        0x101,
        (
            "#0003F#11P（ピッキングツールで\x01",
            "  解除するのは難しそうだな。）\x02\x03",

            "#0000F（となると……\x01",
            "  部屋の中を捜してみるか。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9EE")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 114700, 180)
    SetScenarioFlags(0xC6, 3)
    EventEnd(0x5)

    label("loc_A07")

    Return()

    # Function_6_821 end

    def Function_7_A08(): pass

    label("Function_7_A08")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A98")

    #C0005
    ChrTalk(
        0xFE,
        (
            "#0306Fラインフォルトからヴェルヌまで\x01",
            "最新の武器を仕入れまくりかよ……\x02\x03",

            "#0301Fどんだけミラを\x01",
            "溜め込んでんだって話だな。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    Jump("loc_B40")

    label("loc_A98")


    #C0006
    ChrTalk(
        0xFE,
        (
            "#0308F武器の密輸ルートに関する\x01",
            "ファイルがあるな……\x02\x03",

            "#0303F俺の知ってるルートも\x01",
            "ほぼ網羅されてやがる……\x02\x03",

            "#0300Fガルシアのオッサンの\x01",
            "猟兵時代の人脈って所かね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B40")

    TalkEnd(0xFE)
    Return()

    # Function_7_A08 end

    def Function_8_B44(): pass

    label("Function_8_B44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BCE")

    #C0007
    ChrTalk(
        0x13,
        (
            "#0105F今年の目録もあったけど\x01",
            "散々な結果だったみたいね……\x02\x03",

            "#0106F微妙に後ろめたい気分だけど\x01",
            "まあ、自業自得よね。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 1)
    Jump("loc_CE2")

    label("loc_BCE")


    #C0008
    ChrTalk(
        0x13,
        (
            "#0108F例の《黒の競売会#10Rシュバルツオークション#》の\x01",
            "目録があるわね……\x02\x03",

            "入手経路から落札者に至るまで\x01",
            "詳細にまとめられているけど……\x02\x03",

            "#0106Fあの《怪盗Ｂ》が盗んだという\x01",
            "稀代の名画まで扱っていたなんて……\x02\x03",

            "#0101Fこれが公になったら周辺諸国でも\x01",
            "大騒ぎになりそうだわ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_CE2")

    TalkEnd(0xFE)
    Return()

    # Function_8_B44 end

    def Function_9_CE6(): pass

    label("Function_9_CE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_D7F")

    #C0009
    ChrTalk(
        0x14,
        (
            "#0205Fあ、最近のものでは\x01",
            "警察局長と共和国派議員の\x01",
            "名前もあるみたいです。\x02\x03",

            "#0206F一課に圧力が掛かったのも\x01",
            "当然かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    Jump("loc_E77")

    label("loc_D7F")


    #C0010
    ChrTalk(
        0x14,
        (
            "#0208Fクロスベルの政財界との\x01",
            "贈収賄リストがありますね。\x02\x03",

            "#0203F例の議長さんだけでなく、\x01",
            "帝国派議員、局長クラスの役人、\x01",
            "更には警備隊の司令ですか……\x02\x03",

            "#0211F逆に幾つかの企業からは\x01",
            "暴力でトラブルを解決する事で\x01",
            "多額の謝礼を受け取っていますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_E77")

    TalkEnd(0xFE)
    Return()

    # Function_9_CE6 end

    def Function_10_E7B(): pass

    label("Function_10_E7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EED")

    #C0011
    ChrTalk(
        0xFE,
        (
            "#0603Fここにあるのは\x01",
            "密貿易に関する証拠だ……\x02\x03",

            "#0610Fクッ……\x01",
            "正式な礼状さえあれば……！\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    Jump("loc_FBA")

    label("loc_EED")


    #C0012
    ChrTalk(
        0xFE,
        (
            "#0608Fここにあるのは密貿易に\x01",
            "関するファイルか……\x02\x03",

            "#0606Fおおよそ把握してたとはいえ、\x01",
            "ここまでの規模だったとはな……\x02\x03",

            "#0610Fクッ、正式な礼状があれば\x01",
            "確実に禁固１００年は\x01",
            "喰らわせてやれるのに……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_FBA")

    TalkEnd(0xFE)
    Return()

    # Function_10_E7B end

    def Function_11_FBE(): pass

    label("Function_11_FBE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    LoadChrToIndex("chr/ch06202.itc", 0x21)
    OP_68(150, 930, 108140, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(26500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1800, 30, 106500, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -2700, 30, 108400, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -3000, 20, 107100, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1700, 30, 105400, 45)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -1500, 30, 108200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 900, 30, 108000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -200, 100, 112500, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("豪胆な声")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "てめぇら……\x01",
            "どの面下げて帰ってきた？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("スーツ姿の巨漢")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "てめぇらを保釈させるのに\x01",
            "どれだけのミラを使ったか……\x02\x03",

            "議員どもに鼻薬を効かせるのも\x01",
            "タダじゃねえんだぞ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0015
    ChrTalk(
        0xB,
        "#6Pす、すみません、若頭……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#6Pまさかあんな場所に\x01",
            "警察がいるとは思わずに……\x02",
        )
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        (
            "#11P#3103Fフン……\x01",
            "《特務支援課》と言ったか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(300)

    #N0018
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        (
            "#5P#3100F──ファビオ、モラン。\x02\x03",

            "てめぇらが下手を打ったのも\x01",
            "そのガキどもだったな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#6Pは、はい……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "#12Pその……旧市街の\x01",
            "ガキ共も含めてですが……\x02",
        )
    )

    CloseMessageWindow()

    #N0021
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        (
            "#5P#3104Fハッ、聞けば女子供を集めた\x01",
            "新米どもだそうじゃねぇか。\x02\x03",

            "#3100Fそんなガキ共に遅れを取って……\x01",
            "プロとして恥ずかしくねぇのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "#6Pい、いえっ！！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "#12Pこの落とし前……\x01",
            "必ず付けさせてもらいます！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "#6P聞けばあのガキども、\x01",
            "中央広場の外れにあるボロビルを\x01",
            "拠点にしているみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "#6Pお許しさえいただければ\x01",
            "すぐにでも殴りこみを……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #N0026
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        "#11P#3107F#4S馬鹿野郎！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        "#6Pひっ……\x02",
    )

    CloseMessageWindow()

    #N0028
    NpcTalk(
        0xD,
        "スーツ姿の巨漢",
        (
            "#11P#3107F警察のガキどもなんぞ\x01",
            "いざとなりゃ何とでもなる！\x02\x03",

            "俺たちが潰さなきゃならねぇ\x01",
            "本当の相手は《黒月#4Rヘイユエ#》……\x02\x03",

            "あの忌々しい、\x01",
            "東方人街からの手先だろうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        "#6Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #N0030
    NpcTalk(
        0xE,
        "太った男",
        (
            "#3004F#1P──まあまあ、ガルシア。\x01",
            "そういきり立つものではない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_171E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_171E)
    WaitChrThread(0xD, 2)

    def lambda_172F():
        OP_96(0xFE, 0x12C, 0x1E, 0x1A900, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_172F)
    OP_68(-200, 930, 110500, 2000)
    Sleep(50)

    def lambda_175D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_175D)

    def lambda_176A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_176A)
    Sleep(50)

    def lambda_177A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_177A)

    def lambda_1787():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1787)
    Sleep(50)

    def lambda_1797():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1797)
    WaitChrThread(0xD, 1)
    OP_6F(0x1)

    #C0031
    ChrTalk(
        0xD,
        "#2P#3101F会長、ですが……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0032
    AnonymousTalk(
        0xE,
        (
            "確かに先日、連中のせいで\x01",
            "共和国方面のルートの１つを\x01",
            "失ったばかりだ。\x02\x03",

            "だが、我々の背後には\x01",
            "あのハルトマン議長が付いておる。\x02\x03",

            "このクロスベルにおいて\x01",
            "我々の優位は覆しようがなかろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0033
    ChrTalk(
        0xD,
        (
            "#2P#3107Fですが……\x01",
            "“あの男”だけは危険です！\x02\x03",

            "黒衣で身を包んだあの男だけは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xE,
        (
            "#3002F#5Pグフフ……\x01",
            "お前を翻弄したという刺客か。\x02\x03",

            "百戦錬磨の元猟兵をあしらうとは\x01",
            "相当の手練のようだな。\x02\x03",

            "ツァオもさぞ大枚を叩#2Rはた#いた事だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xD,
        "#2P#3101Fか、会長……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xE,
        (
            "#3004F#5Pまあ、そう心配せずとも\x01",
            "《黒月》への対策はしておるさ。\x02\x03",

            "軍用犬の目処も付いたし、\x01",
            "今後は遅れを取ることもなかろう。\x02\x03",

            "#3001F──それより問題は\x01",
            "来月に迫った《競売会#6Rオークション#》だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0xD,
        "#2P#3103Fええ、心得ております。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xE,
        (
            "#3003F#5Pいかに奴らが調子に乗ろうと\x01",
            "今年の《競売会》だけは\x01",
            "邪魔されるわけにはいかん……\x02\x03",

            "#3001F警察とギルドは放っておけ。\x01",
            "どうせ両方とも手出しはできん。\x02\x03",

            "くれぐれも《黒月》に……\x01",
            "その刺客とやらに邪魔されぬよう、\x01",
            "万全の体制を敷いておくのだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xD,
        "#2P#3101F承知しました……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_FBE end

    def Function_12_1C43(): pass

    label("Function_12_1C43")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    LoadChrToIndex("chr/ch06202.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis159.itp")
    OP_68(-200, 1530, 110500, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -1500, 20, 108400, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 700, 20, 108400, 0)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -200, 30, 108900, 0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -200, 100, 112500, 180)
    Sound(818, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男の声")

    #A0040
    AnonymousTalk(
        0xFF,
        "#4Sまったく、何たる失態だッ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-200, 1030, 110500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0041
    ChrTalk(
        0xE,
        (
            "#5P#3007Fたかが警察ごときに手打ちを\x01",
            "申し入れる羽目になるとは……！\x02\x03",

            "ええい……\x01",
            "お前たちが不甲斐ないせいでッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xD,
        "#11P#3103F……言葉もありません。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#6Pで、ですが例の人形は\x01",
            "会長が御自ら手に入れて……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xE,
        "#5P#3001Fなにぃ……？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "#3103F#11P……黙ってろ。\x02\x03",

            "#3101Fいずれにせよ侵入者を\x01",
            "許したのは俺たちの責任だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#6Pは、はい……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        (
            "#5P#3001Fフン……\x02\x03",

            "#3003Fあれ以来、ハルトマン議長も\x01",
            "こちらとの連絡を避けておるし……\x02\x03",

            "《黒月》どもの攻勢も\x01",
            "本格化しそうだというではないか！\x02\x03",

            "ええい……このままでは……ッ！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xD,
        (
            "#11P#3104F会長、どうかご安心を。\x02\x03",

            "#3100Fいまだクロスベルにおける\x01",
            "我々の優位は揺るぎありません。\x02\x03",

            "ここで《黒月》の攻勢を\x01",
            "何とか凌#2Rしの#げれば議長も……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0049
    ChrTalk(
        0xE,
        (
            "#5P#3007Fええい、凌げる保証が\x01",
            "どこにあるというのだ！？\x02\x03",

            "いまだ《銀》とやらの首一つ\x01",
            "取る事のできないお前たちが！？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xD,
        "#11P#3103Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xE,
        (
            "#5P#3001Fクッ、議長の支援も\x01",
            "しばらくはアテにできん……\x02\x03",

            "#3003F……ええい、どうすれば……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Sleep(500)

    #C0052
    ChrTalk(
        0xE,
        (
            "#5P#3004Fこうなったら手段は選ばん……\x02\x03",

            "#3002F決めた──奥の手を使うとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x9,
        "#12P奥の手……！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "#6Pま、まさか……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xD,
        "#11P#3105F会長、それは……！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xE,
        (
            "#5P#3002Fクク……何を驚いている？\x02\x03",

            "こういう時のための保険を\x01",
            "使うというだけの話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "#11P#3107Fで、ですが……\x01",
            "あれはリスクが高すぎます！\x02\x03",

            "警察はともかく、ギルドに\x01",
            "嗅ぎ付けられる危険も……！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xE,
        (
            "#5P#3004Fクク、その前にとっとと\x01",
            "《黒月》を叩き潰せばよい。\x02\x03",

            "前に用意した流通網も\x01",
            "せっかくだから試すとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0059
    AnonymousTalk(
        0xE,
        (
            "#3002Fクロスベルの裏社会の覇権──\x01",
            "断じて余所#4Rよ　そ#者などに渡すものか！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x48, 0x4, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x25, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245B")
    OP_29(0x25, 0x4, 0x40)

    label("loc_245B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2479")
    OP_29(0x26, 0x4, 0x40)
    Jump("loc_248B")

    label("loc_2479")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_248B")
    OP_29(0x26, 0x4, 0x40)

    label("loc_248B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A9")
    OP_29(0x27, 0x4, 0x40)
    Jump("loc_24BB")

    label("loc_24A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BB")
    OP_29(0x27, 0x4, 0x40)

    label("loc_24BB")

    SubItemNumber(0x358, 1)
    Sleep(1000)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1C43 end

    def Function_13_25A3(): pass

    label("Function_13_25A3")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("monster/ch68250.itc", 0x23)
    LoadChrToIndex("monster/ch68252.itc", 0x24)
    LoadChrToIndex("monster/ch68350.itc", 0x25)
    LoadEffect(0x0, "event\\ev502_00.eff")
    OP_68(0, 1130, 51000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 30, 48000, 0)
    SetChrPos(0x102, -100, 30, 46300, 0)
    SetChrPos(0x104, 900, 30, 45800, 0)
    SetChrPos(0x103, -1200, 30, 46500, 0)
    SetChrPos(0x10A, 1300, 30, 47800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)

    def lambda_26C7():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26C7)

    def lambda_26E1():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_26E1)
    Sleep(50)

    def lambda_26FE():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26FE)

    def lambda_2718():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2718)
    Sleep(50)

    def lambda_2735():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2735)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1130, 62000, 2000)
    OP_6F(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0005Fひょっとしてそこが\x01",
            "マルコーニ会長の部屋……？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0300F無駄に豪華そうだし、\x01",
            "それっぽいかもしれねぇな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(740, 1130, 51250, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19360, 0)
    OP_0D()
    Sleep(300)

    #C0062
    ChrTalk(
        0x10A,
        (
            "#0603F#11P……とにかく中に入るぞ。\x02\x03",

            "#0601Fいい加減、連中が消えた\x01",
            "手がかりを見つけなくては──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(943, 0, 100, 0)
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("音声")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40WＰＰＰＰＰ……\x01",
            "未登録ノ侵入者ヲ感知……\x02",
        )
    )

    CloseMessageWindow()

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "待機もーどヲ解除シマス……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x10A,
        "#0605F#11P！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        "#12P#0201Fみんな、下がってください！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 2430, 55000, 0)
    MoveCamera(25, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(14500, 0)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xF, 0x100)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 1000, 55000, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    MoveCamera(45, 21, 0, 3500)
    SetCameraDistance(15500, 3500)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x0, 0xF, 0x40, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_2AEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2AEE)
    Sound(202, 0, 100, 0)
    WaitChrThread(0xF, 2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_68(0, 1430, 55000, 300)

    def lambda_2B22():
        OP_9D(0xFE, 0x0, 0x0, 0xD6D8, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2B22)

    def lambda_2B3F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B3F)
    Sleep(50)

    def lambda_2B5C():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2B5C)
    Sleep(50)

    def lambda_2B79():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B79)
    Sleep(50)

    def lambda_2B96():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B96)
    Sleep(50)

    def lambda_2BB3():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BB3)
    WaitChrThread(0xF, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19500, 1500)
    OP_82(0x0, 0x2BC, 0xBB8, 0x5DC)
    Sound(813, 0, 80, 0)
    Sound(944, 0, 100, 0)
    OP_6F(0x10)
    Sleep(500)
    Fade(500)
    OP_68(0, 1430, 51300, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    CancelBlur(0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x101,
        "#0011F#12Pなああっ！？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0068
    ChrTalk(
        0x102,
        "#0105F#12Pこ、これって……！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0307F#12Pカラクリどもの\x01",
            "親玉ってわけかよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(945, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 3, 0, 1)
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sound(943, 0, 100, 0)
    SetMessageWindowPos(30, 70, -1, -1)
    SetChrName("音声")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "迎撃もーどニ移行……\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "対象者数５名……\x01",
            "武装ヲ確認シマシタ……\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『むすたんぐ』ヲ展開……\x01",
            "コレヨリ迎撃行動ニ入リマス……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 2600, 0, 53500, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    BeginChrThread(0x10, 3, 0, 2)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, -2600, 0, 53500, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    BeginChrThread(0x11, 3, 0, 2)
    OP_82(0x96, 0x96, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x0, 0x10, 0x40, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x11, 0x40, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_2EBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2EBC)

    def lambda_2ECD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2ECD)
    Sound(202, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)

    #C0073
    ChrTalk(
        0x103,
        "#0207F#12P#N遠隔操作の攻撃ユニット……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0074
    ChrTalk(
        0x10A,
        (
            "#0607F#12Pお前たち、気合いを入れろ！\x02\x03",

            "総力をもって\x01",
            "このデカブツを撃破する！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#0007F#12Pはいっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xF, 0x3)
    Fade(250)
    Sound(945, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x1)
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)

    def lambda_309B():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_309B)
    WaitChrThread(0xF, 2)
    SetChrFlags(0xF, 0x20)
    Sound(947, 0, 100, 0)
    BlurSwitch(0x15E, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(30, 15, 0, 350)
    SetCameraDistance(14500, 350)

    def lambda_30E9():
        OP_96(0xFE, 0x0, 0x0, 0xB798, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_30E9)
    Sleep(50)
    SetChrSubChip(0xF, 0x2)
    Sleep(300)
    Battle("BattleInfo_46C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    Call(0, 14)
    Return()

    # Function_13_25A3 end

    def Function_14_3132(): pass

    label("Function_14_3132")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00056.itc", 0x1E)
    LoadChrToIndex("chr/ch00156.itc", 0x1F)
    LoadChrToIndex("chr/ch00256.itc", 0x20)
    LoadChrToIndex("chr/ch00356.itc", 0x21)
    LoadChrToIndex("chr/ch00953.itc", 0x22)
    LoadChrToIndex("monster/ch68250.itc", 0x23)
    LoadChrToIndex("monster/ch68252.itc", 0x24)
    LoadChrToIndex("monster/ch68350.itc", 0x25)
    OP_68(440, 1130, 51170, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, 0, 30, 51000, 0)
    SetChrPos(0x102, -100, 30, 49300, 0)
    SetChrPos(0x104, 900, 30, 48800, 0)
    SetChrPos(0x103, -1200, 30, 49500, 0)
    SetChrPos(0x10A, 1300, 30, 50800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x3)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_68(440, 1130, 50170, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0076
    ChrTalk(
        0x101,
        (
            "#0006F#5Pはあはあ……\x01",
            "とんでもない相手だったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#0306F#11Pああ……なんで今のを\x01",
            "《黒月》にぶつけなかったのか\x01",
            "不思議なくらいだぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        (
            "#6P#0206Fまあ……恐らく制御が\x01",
            "難しかったからではないかと……\x02\x03",

            "#0211F専門の技術者がいなければ\x01",
            "暴走する危険もありますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#12P#0106Fもし市街地に放たれていたら\x01",
            "大変だったでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x10A,
        "#11P#0606Fああ、まったくだ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x10A, 0x101, 400)

    #C0081
    ChrTalk(
        0x10A,
        (
            "#11P#0603Fよし……\x01",
            "最後の障害も突破した。\x02\x03",

            "#0601F部屋の中を調べるぞ……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_347D():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_347D)
    Sleep(150)

    def lambda_348D():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_348D)
    Sleep(50)
    TurnDirection(0x102, 0x10A, 500)

    #C0082
    ChrTalk(
        0x101,
        "#6P#0000Fはい……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_37()
    OP_68(0, 1280, 51000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 0, 30, 51000, 0)
    SetChrPos(0x1, 0, 30, 51000, 0)
    SetChrPos(0x2, 0, 30, 51000, 0)
    SetChrPos(0x3, 0, 30, 51000, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC6, 1)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_3132 end

    def Function_15_3561(): pass

    label("Function_15_3561")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 111500, 0)
    MoveCamera(47, 30, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 300, 0, 99000, 0)
    SetChrPos(0x102, -500, 0, 99000, 0)
    SetChrPos(0x104, -500, 0, 99000, 0)
    SetChrPos(0x103, 300, 0, 99000, 0)
    SetChrPos(0x10A, 800, 0, 99000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1100, 104500, 6000)
    MoveCamera(27, 17, 0, 6000)
    SetCameraDistance(19500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_3668():
        OP_96(0xFE, 0x1F4, 0x0, 0x1912C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3668)

    def lambda_3682():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3682)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 16)
    Sleep(500)

    def lambda_369F():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x1912C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_369F)

    def lambda_36B9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_36B9)
    Sleep(500)

    def lambda_36CD():
        OP_96(0xFE, 0x1F4, 0x0, 0x18B50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36CD)

    def lambda_36E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_36E7)
    Sleep(500)

    def lambda_36FB():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x18B50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36FB)

    def lambda_3715():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3715)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(780, 1000, 102610, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(17950, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_37DF")

    #C0083
    ChrTalk(
        0x102,
        (
            "#6P#0101F豪奢#4Rごうしゃ#な部屋ね……\x02\x03",

            "#0103Fさすがにハルトマン議長の\x01",
            "部屋ほどではないけれど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B8")

    label("loc_37DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_384E")

    #C0084
    ChrTalk(
        0x103,
        (
            "#12P#0201F贅沢そうな部屋ですね……\x02\x03",

            "#0203Fさすがにあの議長さんの\x01",
            "部屋ほどではありませんが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B8")

    label("loc_384E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_38B8")

    #C0085
    ChrTalk(
        0x104,
        (
            "#6P#0302Fへえ……\x01",
            "豪勢な部屋じゃねえか。\x02\x03",

            "#0309Fさすがにあの議長の\x01",
            "部屋ほどじゃねえけどよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B8")


    #C0086
    ChrTalk(
        0x101,
        (
            "#11P#0012Fまあ、あれと比べたらなぁ。\x02\x03",

            "#0011Fって……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_3941():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3941)

    def lambda_394E():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_394E)

    def lambda_395B():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_395B)

    def lambda_3968():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3968)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_39C3")

    #C0087
    ChrTalk(
        0x102,
        "#6P#0108Fあ……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#6P#0306Fお嬢……迂闊だろ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A56")

    label("loc_39C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3A0C")

    #C0089
    ChrTalk(
        0x103,
        "#12P#0205Fあ。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#6P#0306Fティオすけ……迂闊だろ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A56")

    label("loc_3A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3A56")

    #C0091
    ChrTalk(
        0x104,
        "#6P#0305Fヤベ……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#12P#0211Fランディさん……迂闊です。\x02",
    )

    CloseMessageWindow()

    label("loc_3A56")

    OP_93(0x10A, 0x10E, 0x1F4)
    Sleep(300)

    #C0093
    ChrTalk(
        0x10A,
        (
            "#11P#0604Fフン……\x01",
            "何を今さら焦っている？\x02\x03",

            "#0602F《黒の競売会#10Rシュバルツオークション#》についての\x01",
            "経緯などとっくに聞いている。\x02\x03",

            "一課としては\x01",
            "長年狙っていた獲物を\x01",
            "横取りされた気分だがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0012F#6Pはは……\x02\x03",

            "#0003Fそ、それはともかく、\x01",
            "やはりここが会長室みたいですね。\x02\x03",

            "#0001Fどうやらルバーチェ商会の中は\x01",
            "一通り調べつくしたようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10A,
        (
            "#11P#0608Fああ……結局マフィアは\x01",
            "一人も残っていなかったし、\x01",
            "失踪者もここには居ないようだ。\x02\x03",

            "#0603F何か手がかりがあるとしたら\x01",
            "この部屋以外にはありえん……\x02\x03",

            "#0601F時間が惜しい──\x01",
            "全員で手分けをして調べるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#0013F#6Pはい！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#3P#0103F#6Pさぞ色々なものが\x01",
            "見つかりそうですね……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    RemoveParty(0x9, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_68(0, 1200, 101500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, 0, 0, 101500, 0)
    SetMapFlags(0x2000)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0xC6, 2)
    OP_29(0x4C, 0x1, 0x1A)
    OP_1B(0x2, 0x0, 0x15)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_3561 end

    def Function_16_3DA9(): pass

    label("Function_16_3DA9")


    def lambda_3DAE():
        OP_96(0xFE, 0x320, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3DAE)

    def lambda_3DC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3DC8)
    WaitChrThread(0x10A, 1)

    def lambda_3DDD():
        OP_95(0xFE, 2000, 0, 102400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3DDD)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x0, 0x1F4)
    Return()

    # Function_16_3DA9 end

    def Function_17_3DFE(): pass

    label("Function_17_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E14")
    Call(0, 18)
    Jump("loc_3E51")

    label("loc_3E14")

    TalkBegin(0xFF)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戸棚にはビンテージ物の高級酒が並んでいる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3E51")

    Return()

    # Function_17_3DFE end

    def Function_18_3E52(): pass

    label("Function_18_3E52")

    EventBegin(0x0)
    Fade(1000)
    OP_68(7700, 1200, 113000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6700, 0, 113000, 90)
    OP_0D()
    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戸棚にはビンテージ物の高級酒が並んでいる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0100
    ChrTalk(
        0x101,
        (
            "#0005F#6P（さすがに高そうな\x01",
            "  酒ばっかりだけど……）\x02\x03",

            "#0000F（……ひょっとしたら……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはボトルを１本ずつ持ち上げて下を確かめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0102
    ChrTalk(
        0x101,
        "#0002F#6P（ビンゴ……！）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x32F, 1)

    #C0104
    ChrTalk(
        0x101,
        (
            "#0004F#6P（手下たちが間違っても\x01",
            "  触れそうにはない場所……）\x02\x03",

            "#0000F（まあ、定番の隠し場所だよな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6700, 0, 113000, 90)
    SetScenarioFlags(0xC6, 4)
    EventEnd(0x5)
    Return()

    # Function_18_3E52 end

    def Function_19_405A(): pass

    label("Function_19_405A")

    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis092.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis093.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")
    Sound(809, 0, 100, 0)
    Sleep(600)
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)

    #C0105
    ChrTalk(
        0x101,
        (
            "#0000F#11P（よし……開いたか。）\x02\x03",

            "#0008F（幾つかファイルがあるけど……\x01",
            "  ……どれどれ……）\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x331, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x332),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x332, 1)

    #A0108
    AnonymousTalk(
        0x101,
        (
            "#0005F（あった……！）\x02\x03",

            "#0003F（やはりマフィアが薬物を……）\x02\x03",

            "（そして《グノーシス》……\x01",
            "  例の教団が造った薬物か……）\x02\x03",

            "#0013F（いったいどういう関係が……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x101,
        (
            "#0001F#11P（あれ、宝箱の隅に何か……）\x02\x03",

            "（……これは、警察の……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x333),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x333, 1)

    #A0111
    AnonymousTalk(
        0x101,
        "#0005F（…………え……………）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_C9(0x3, 0x0, 0xFFFDF0A8, 0xFFFDF0A8, 0x0)
    OP_C9(0x3, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(0, 0, -1)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0xBB8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    OP_68(0, 900, 110000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -200, 20, 107400, 0)
    SetChrPos(0x102, -1900, 30, 108500, 0)
    SetChrPos(0x103, -1500, 30, 107700, 0)
    SetChrPos(0x104, 1200, 30, 108100, 330)
    SetChrPos(0x10A, 0, 20, 109200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFrame(0xFF, "sakebin", 0x0, 0x1)
    ClearMapObjFlags(0x13, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7122", 0)
    SetCameraDistance(18000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0112
    ChrTalk(
        0x10A,
        (
            "#0603F#11P──失踪した市民たちは\x01",
            "全てリストに記載されていた。\x02\x03",

            "これでマフィアが薬物を\x01",
            "広めた裏付けは取れたわけだ。\x02\x03",

            "#0601Fそして例の教団が造ったという\x01",
            "《グノーシス》とやらか……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#12P#0208F………………………………\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x102,
        (
            "#12P#0106F一体どうしてマフィアが\x01",
            "そんなものを……\x02\x03",

            "#0108F入荷リストによると\x01",
            "何者かの提供を受けているのは\x01",
            "間違いなさそうだけど……\x02\x03",

            "#0101Fやはりその人物が\x01",
            "教団関係者なのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0003F──間違いないだろう。\x02\x03",

            "#0001F書類によると、数年前から\x01",
            "付き合いのある人物みたいだな。\x02\x03",

            "軍用犬に薬物を投与して\x01",
            "簡単にコントロールする技術なんかも\x01",
            "提供していたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#0306Fなるほど、軍用犬を訓練するのは\x01",
            "猟兵団でもかなりの手間がかかる。\x02\x03",

            "#0301Fあれだけ大量に使ってたのは\x01",
            "ちょいと違和感があったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x10A,
        (
            "#0603F#11P全てはその教団関係者が\x01",
            "協力していたというわけか。\x02\x03",

            "#0608Fしかし一体、何者だ……？\x02\x03",

            "やり取りの頻度から見て\x01",
            "クロスベルの人間であるのは\x01",
            "間違いないようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#0003F……分かりません。\x02\x03",

            "#0013Fですが、失踪者たちの行方も\x01",
            "マフィアたちの不在の理由も……\x02\x03",

            "全てはその人物が握って\x01",
            "いるのではないかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#12P#0206F……わたしも同感です。\x02\x03",

            "#0208Fおそらく、あの蒼色の錠剤は\x01",
            "数年前に使われていた\x01",
            "《グノーシス》の改良版……\x02\x03",

            "#0201Fその人物が完成させて……\x01",
            "マフィアに提供したのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A7F():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A7F)
    WaitChrThread(0x103, 2)
    Sleep(300)

    def lambda_4A9F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A9F)
    Sleep(50)

    def lambda_4AAF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AAF)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0120
    ChrTalk(
        0x102,
        "#5P#0101Fティオちゃん……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0004F#11P大丈夫だ……\x01",
            "俺たちが付いている。\x02\x03",

            "#0000Fもう二度と──\x01",
            "ティオに悪夢は見させない。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0122
    ChrTalk(
        0x103,
        "#6P#0202Fロイドさん……\x02",
    )

    CloseMessageWindow()

    def lambda_4B6B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4B6B)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0123
    ChrTalk(
        0x104,
        (
            "#0304Fま、どうやらブチのめす事、\x01",
            "確定の外道みてぇだしな。\x02\x03",

            "#0301Fしかしそうなると……\x01",
            "どう炙り出すかが問題か。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#5P#0108Fそうね……\x01",
            "人手が圧倒的に足りないわ。\x02\x03",

            "消えたマフィアへの対処と\x01",
            "失踪者の捜索に加えて、\x01",
            "空港の爆破予告もあるし……\x02\x03",

            "#0106F……上層部の圧力がなかったら\x01",
            "何とかなったんでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x10A,
        (
            "#0606F#11Pクッ……まさか警察局長までもが\x01",
            "完全に取り込まれていたとはな。\x02\x03",

            "そうでなければ全警察を挙げた\x01",
            "対策本部を設立できたものを……\x02\x03",

            "#0610F恥を知るがいい……！\x01",
            "警察のツラ汚しが……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D76():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D76)
    Sleep(50)

    def lambda_4D86():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D86)
    Sleep(50)

    def lambda_4D96():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D96)
    Sleep(50)
    TurnDirection(0x104, 0x10A, 500)

    #C0126
    ChrTalk(
        0x101,
        "#12P#0005Fダドリーさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#0003F──提案があります。\x02\x03",

            "#0001F遊撃士協会に\x01",
            "協力を要請しませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    MoveCamera(43, 21, 0, 1200)
    OP_68(250, 900, 108770, 1200)

    def lambda_4EBC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4EBC)
    Sleep(100)

    def lambda_4ECC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4ECC)
    Sleep(50)

    def lambda_4EDC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4EDC)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)
    OP_6F(0x1)

    #C0128
    ChrTalk(
        0x102,
        "#5P#0100Fあ……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#11P#0302Fおお……！\x01",
            "その手があるじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x10A,
        (
            "#0607F#5Pば、馬鹿なことを言うな！\x02\x03",

            "そんな事をしたら、\x01",
            "警察内部の恥をギルドに\x01",
            "暴露することにも──\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#12P#0006F仕方ないでしょう……\x01",
            "警察全体のツケなんですから。\x02\x03",

            "見てみぬフリをしていた\x01",
            "俺たち全員の責任です。\x02\x03",

            "#0013F恥くらい、甘んじて\x01",
            "受けるべきではありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x10A,
        "#0610F#5Pぐっ……\x02",
    )

    CloseMessageWindow()

    def lambda_5062():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5062)
    Sleep(50)

    def lambda_5072():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5072)
    Sleep(50)

    def lambda_5082():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5082)
    Sleep(300)

    #C0133
    ChrTalk(
        0x103,
        (
            "#6P#0211F確かに、こうしている内に\x01",
            "失踪者たちがどんな目に\x01",
            "遭っているか分かりませんし……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#12P#0300F消えたマフィアどもが\x01",
            "何をしでかすかも判らねぇよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#6P#0101Fもう、体面を気にしている\x01",
            "場合ではないと思います。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    #C0136
    ChrTalk(
        0x10A,
        "#0603F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10A)
    Sleep(100)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    #C0137
    ChrTalk(
        0x10A,
        (
            "#0604F#5Pフン……セルゲイさんも\x01",
            "とんだ部下どもを集めたものだ。\x02\x03",

            "#0600Fいいだろう──\x01",
            "ギルドとの交渉はお前たちに任せた。\x02\x03",

            "私は私で、上層部の目を盗んで\x01",
            "動ける人間を一課から確保しよう。\x02\x03",

            "#0603F場合によっては二課からの\x01",
            "協力も得られるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#12P#0002Fダドリーさん……\x02\x03",

            "#0004F……感謝します。\x01",
            "聞き入れてくださって。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10A,
        (
            "#0602F#5Pフン……勘違いするな。\x02\x03",

            "現状ではそうする以外、\x01",
            "選択肢がないというだけだ。\x02\x03",

            "#0603Fそれよりも──バニングス。\x02\x03",

            "#0601Fそのバッジの事はいいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#12P#0008Fあ……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    #A0141
    AnonymousTalk(
        0x102,
        "#0108F傷付いた警察徽章……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0142
    AnonymousTalk(
        0x104,
        (
            "#0301F本当にお前の\x01",
            "兄貴のバッジなのか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0143
    AnonymousTalk(
        0x101,
        (
            "#0006Fああ、多分そうだと思う。\x02\x03",

            "#0000Fティオも見覚えが\x01",
            "あるんじゃないか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0144
    AnonymousTalk(
        0x103,
        (
            "#0204Fはい……\x02\x03",

            "多分、例のロッジ制圧の時に\x01",
            "付いた傷だと思います……\x02\x03",

            "#0202F勲章だって言ってました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0145
    AnonymousTalk(
        0x10A,
        (
            "#0606Fフン、なるほどな……\x02\x03",

            "#0608F……道理でうるさく言っても\x01",
            "新品と交換しなかったわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0146
    ChrTalk(
        0x101,
        (
            "#12P#0000Fダドリーさんは……\x01",
            "兄貴と同僚だったんですよね？\x02\x03",

            "兄貴が捜査一課に移ってから。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x10A,
        (
            "#0603F#5Pまあな……\x02\x03",

            "#0601F正直、一課の水には\x01",
            "まったく合わない男だった。\x02\x03",

            "強引かつ無鉄砲、\x01",
            "独断専行ばかりが目立って……\x02\x03",

            "私とは特にソリが合わずに、\x01",
            "事件を巡って衝突ばかりしていた。\x02\x03",

            "#0604Fだが──優秀な捜査官だったのは\x01",
            "一課の誰もが認めていた。\x02\x03",

            "もちろん私も含めてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#12P#0005Fダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x10A,
        (
            "#0606F#5P……ヤツが殉職した時、\x01",
            "私たち一課の人間の喪失感は\x01",
            "予想以上のものだった。\x02\x03",

            "ソリは合わなかったが……\x01",
            "どこかヤツの破天荒な行動力に\x01",
            "期待していた所もあったんだろう。\x02\x03",

            "#0608F必死になって犯人を捜したが\x01",
            "結局、手がかりは見つからず……\x02\x03",

            "#0603F──すまない。\x01",
            "お前には辛い想いをさせたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#12P#0011Fよ、よしてくださいよ。\x02\x03",

            "#0006F単独捜査をしてた兄貴にも\x01",
            "問題はあったみたいだし……\x02\x03",

            "#0002Fそんな風に兄貴の死を\x01",
            "受け止めてくれていただけで\x01",
            "俺としては十分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x10A,
        (
            "#0602F#5Pそうか……\x02\x03",

            "#0603F──しかしここに来て\x01",
            "改めて容疑者が浮上したわけだ。\x02\x03",

            "もちろん当時からも、\x01",
            "その可能性は疑われていたが……\x02\x03",

            "#0601Fこれでやっとお前も\x01",
            "兄の無念を晴らすことが──\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#12P#0004Fいえ……\x01",
            "今は兄貴のことはいいんです。\x02\x03",

            "#0008Fそれよりも、解決しなくては\x01",
            "いけない問題が山ほどある……\x02\x03",

            "#0000Fそれを片付けてから考えます。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A3D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5A3D)
    Sleep(50)

    def lambda_5A4D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5A4D)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0153
    ChrTalk(
        0x103,
        "#6P#0202Fロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#6P#0104F本当にもう……\x01",
            "生真面目なんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#11P#0309Fま、それがコイツの\x01",
            "コイツたる由縁だろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10A,
        (
            "#0604F#5Pフッ──分かった。\x02\x03",

            "#0602Fそれでは今はお互い、\x01",
            "やるべき事をやるとしよう。\x02\x03",

            "あの癪にさわるくらい\x01",
            "破天荒で前向きだった男に\x01",
            "負けないためにもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        "#12P#0000Fはい……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis161.itp")
    OP_29(0x4C, 0x4, 0x10)
    SubItemNumber(0x32F, 1)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x28, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x9)
    RemoveParty(0x9, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    ReplaceBGM("ed7000", "ed7000")
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t3010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_405A end

    def Function_20_5CEE(): pass

    label("Function_20_5CEE")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 1150, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 0, 30, 62300, 0)
    SetChrPos(0x102, -1400, 30, 60500, 0)
    SetChrPos(0x104, -1400, 30, 59400, 0)
    SetChrPos(0x103, -100, 30, 59400, 0)
    SetChrPos(0x10A, 1000, 30, 61000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0003F（マフィアのボスの部屋……\x01",
            "  ついにここまで辿り付いたか。）\x02\x03",

            "#0008F（多分、この部屋を調べたら\x01",
            "  色々な意味で後戻りできないだろう。）\x02\x03",

            "#0013F（どうする……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この扉の中に入ると、クロスベル市の外には\x01",
            "自由に出られなくなってしまいます。\x02\x03",

            "やり残したクエストなどが達成できなくなる\x01",
            "可能性があるため注意してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【扉を開いて部屋の中に入る】\x01",      # 0
            "【いったん離れる】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F52"),
        (1, "loc_6020"),
        (SWITCH_DEFAULT, "loc_6073"),
    )


    label("loc_5F52")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    FadeToDark(1000, 0, -1)

    def lambda_5F76():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F76)
    Sleep(100)

    def lambda_5F93():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5F93)
    Sleep(100)

    def lambda_5FB0():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5FB0)
    Sleep(100)

    def lambda_5FCD():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5FCD)
    Sleep(100)

    def lambda_5FEA():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5FEA)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_65(0x3, 0x1)
    Call(0, 15)
    Jump("loc_6073")

    label("loc_6020")

    SetChrPos(0x0, 0, 30, 61800, 180)
    SetChrPos(0x1, 0, 30, 61800, 180)
    SetChrPos(0x2, 0, 30, 61800, 180)
    SetChrPos(0x3, 0, 30, 61800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_6073")

    label("loc_6073")

    EventEnd(0x5)
    Return()

    # Function_20_5CEE end

    def Function_21_6076(): pass

    label("Function_21_6076")

    EventBegin(0x1)

    #C0160
    ChrTalk(
        0x101,
        (
            "#0013F外に出ている場合じゃない……\x01",
            "今はこの部屋を徹底的に調べよう！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 100500, 0)
    EventEnd(0x4)
    Return()

    # Function_21_6076 end

    SaveToFile()

Try(main)
