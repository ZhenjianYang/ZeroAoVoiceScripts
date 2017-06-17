from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3034.bin",                # FileName
        "m3034",                    # MapName
        "m3034",                    # Location
        0x007E,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -71000, 0, 0, 0, 0, 1, 126, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3034",                  # 0
        "ガルシア",               # 1
        "SE制御",                 # 2
        "bm3040",                 # 3
    ))

    ATBonus("ATBonus_1F8", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_238", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_23C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_248", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_29C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_2D8", 0x0042, 43, 6, 180, 0, 0, 0, 0, "bm3040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_238", "MonsterBattlePostion_298", "ed7405", "ed7000", "ATBonus_1F8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50524.itc",                   # 00
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    277,  0x0, 0,   0,   0,   255, 255, 0,   2,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   -53.0,                 0.0,                   -5.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   17.666667938232422,    -0.0,                  1.0,                   1.0])

    DeclActor(15200,   5030,    6000,    2500,    15200,   6030,    6000,    0x007C, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_33C",          # 00, 0
        "Function_1_366",          # 01, 1
        "Function_2_3D1",          # 02, 2
        "Function_3_423",          # 03, 3
        "Function_4_587",          # 04, 4
        "Function_5_DC0",          # 05, 5
        "Function_6_200F",         # 06, 6
        "Function_7_2052",         # 07, 7
    ))


    def Function_0_33C(): pass

    label("Function_0_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_34B")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_365")
    SetChrPos(0x8, -5000, -4000, 3000, 270)

    label("loc_365")

    Return()

    # Function_0_33C end

    def Function_1_366(): pass

    label("Function_1_366")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_37E")

    ClearMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 6)), scpexpr(EXPR_END)), "loc_39A")
    OP_70(0x2, 0x96)
    OP_70(0x1, 0x1E)
    Jump("loc_3A2")

    label("loc_39A")

    OP_70(0x2, 0x78)
    OP_70(0x1, 0x0)

    label("loc_3A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CA")
    OP_24(0x82)
    Jump("loc_3D0")

    label("loc_3CA")

    Sound(130, 1, 100, 0)

    label("loc_3D0")

    Return()

    # Function_1_366 end

    def Function_2_3D1(): pass

    label("Function_2_3D1")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ガルシアは完全に気絶している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_2_3D1 end

    def Function_3_423(): pass

    label("Function_3_423")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 6)), scpexpr(EXPR_END)), "loc_468")
    TalkBegin(0xFF)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにレバーは下りている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_586")

    label("loc_468")

    EventBegin(0x1)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57F")
    Fade(500)
    SetChrPos(0x0, 14090, 4000, 6000, 90)
    SetChrPos(0x1, 12000, 4000, 6800, 90)
    SetChrPos(0x2, 12000, 4000, 5200, 90)
    SetChrPos(0x3, 11320, 4000, 6000, 90)
    OP_68(15910, 5800, 2130, 0)
    MoveCamera(90, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26500, 0)
    OP_0D()
    Sound(143, 0, 100, 0)
    OP_71(0x2, 0x78, 0x96, 0x0, 0x0)
    OP_79(0x2)
    Sleep(500)
    Sound(155, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x1)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    SetScenarioFlags(0xF5, 6)

    label("loc_57F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_586")

    Return()

    # Function_3_423 end

    def Function_4_587(): pass

    label("Function_4_587")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    StopBGM(0x2710)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("chr/ch02250.itc", 0x24)
    LoadChrToIndex("chr/ch02254.itc", 0x25)
    LoadChrToIndex("chr/ch02252.itc", 0x26)
    LoadEffect(0x0, "event\\ev602_00.eff")
    SoundLoad(861)
    OP_68(-40000, -3000, 0, 0)
    MoveCamera(35, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, -4000, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-5000, -2000, 0, 7000)
    MoveCamera(65, 10, 0, 7000)
    SetCameraDistance(35000, 7000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-12500, -3100, 0, 0)
    MoveCamera(90, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    SetMapObjFrame(0xFF, "moya1", 0x0, 0x1)
    SetChrPos(0x101, -25000, -4000, 0, 90)
    SetChrPos(0x102, -26000, -4000, -1500, 90)
    SetChrPos(0x103, -27500, -4000, -600, 90)
    SetChrPos(0x104, -26500, -4000, 900, 90)
    SetChrPos(0x107, -25500, -4000, 2700, 90)
    SetChrPos(0x108, -27300, -4000, 2000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    OP_68(-7500, -3100, 0, 3500)
    SetCameraDistance(22000, 3500)

    def lambda_787():
        OP_96(0xFE, 0xFFFFD508, 0xFFFFF060, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_787)
    Sleep(50)

    def lambda_7A4():
        OP_96(0xFE, 0xFFFFD120, 0xFFFFF060, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7A4)
    Sleep(50)

    def lambda_7C1():
        OP_96(0xFE, 0xFFFFCB44, 0xFFFFF060, 0xFFFFFDA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C1)
    Sleep(50)

    def lambda_7DE():
        OP_96(0xFE, 0xFFFFCF2C, 0xFFFFF060, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7DE)
    Sleep(50)

    def lambda_7FB():
        OP_96(0xFE, 0xFFFFD314, 0xFFFFF060, 0xA8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7FB)
    Sleep(50)

    def lambda_818():
        OP_96(0xFE, 0xFFFFCC0C, 0xFFFFF060, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_818)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)

    def lambda_846():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_846)
    WaitChrThread(0x108, 1)

    def lambda_857():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_857)
    WaitChrThread(0x108, 2)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_0D()
    OP_6F(0x79)

    #C0005
    ChrTalk(
        0x101,
        "#6P#0007Fガルシア・ロッシ……！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        "#6P#0301Fフン……ここに居たかよ。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#12P#0101Fやっぱり……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#12P#0208F#Nどうやら他のマフィアと同様、\x01",
            "操られてしまったみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0010
    ChrTalk(
        0x107,
        (
            "#6P#0801F……ジンさん並みに大きな人ね。\x02\x03",

            "なんかやたらと手強そうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x108,
        (
            "#6P#0903F#N元《西風の旅団》部隊長にして\x01",
            "《ルバーチェ商会》の若頭……\x02\x03",

            "#0901F戦闘力は折り紙つきだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    OP_68(-5000, -3100, 0, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    OP_82(0x96, 0x96, 0xBB8, 0x7D0)
    MoveCamera(65, 17, 0, 2000)
    SetCameraDistance(21500, 2000)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(202, 0, 100, 0)
    Sound(861, 2, 100, 0)
    OP_6F(0x79)
    Sleep(1000)

    #C0013
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F#6P#Nどうやら魔人化する\x01",
            "気配はなさそうだけど……\x02\x03",

            "手の抜ける相手じゃなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C69")

    #C0014
    ChrTalk(
        0x104,
        (
            "#0311F#6P#Nおい──キリングベア。\x02\x03",

            "#0303F聞こえてねぇかもしれねえが\x01",
            "あんたのお望み通り\x01",
            "全力で行かせてもらう……\x02\x03",

            "#0312F悪名高き《闘神の息子》の力、\x01",
            "その目に焼き付けておきな……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C99")

    label("loc_C69")


    #C0015
    ChrTalk(
        0x104,
        (
            "#0307F#6P#Nああ……\x01",
            "くれぐれも油断すんな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C99")

    OP_5A()

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40W#11P……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1838, 255, 100, 0)    #voice#Garcia
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(100)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0x8, 0x3)
    Sleep(100)

    def lambda_CFA():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CFA)
    WaitChrThread(0x8, 1)
    Sleep(500)
    Sound(1839, 255, 100, 1)    #voice#Garcia
    Sound(250, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-9000, -3100, 0, 400)
    SetCameraDistance(17000, 400)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrFlags(0x8, 0x20)

    def lambda_D5F():
        OP_96(0xFE, 0xFFFFD6FC, 0xFFFFF060, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D5F)
    SetChrSubChip(0x8, 0x4)
    Sleep(80)
    SetChrSubChip(0x8, 0x5)
    Sleep(320)
    OP_24(0x35D)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_2D8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x20)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    EndChrThread(0x8, 0xFF)
    StopEffect(0x0, 0x0)
    Call(0, 5)
    Return()

    # Function_4_587 end

    def Function_5_DC0(): pass

    label("Function_5_DC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00351.itc", 0x22)
    LoadChrToIndex("chr/ch00650.itc", 0x23)
    LoadChrToIndex("chr/ch00750.itc", 0x24)
    LoadChrToIndex("chr/ch02253.itc", 0x25)
    LoadChrToIndex("chr/ch02254.itc", 0x26)
    LoadChrToIndex("chr/ch00056.itc", 0x27)
    LoadChrToIndex("chr/ch00351.itc", 0x28)
    SoundLoad(861)
    SoundLoad(930)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x23)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x24)
    SetChrSubChip(0x108, 0x0)
    OP_68(-5000, -3100, 0, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -11000, -4000, 0, 90)
    SetChrPos(0x102, -12000, -4000, -1500, 90)
    SetChrPos(0x103, -13500, -4000, -600, 90)
    SetChrPos(0x104, -12500, -4000, 900, 90)
    SetChrPos(0x107, -11500, -4000, 2700, 135)
    SetChrPos(0x108, -13300, -4000, 2000, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, -4000, 0, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_F3C():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F3C)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_00.eff")
    LoadEffect(0x2, "event\\ev602_03.eff")
    SetMapObjFrame(0xFF, "moya1", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    #Sound(1859, 255, 100, 0)    #voice#Garcia

    #C0017
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#60W#17A……ギギ……ググ………\x02",
        )
    )
    #Auto

    Sleep(3000)
    Sleep(500)
    #Sound(1860, 255, 100, 1)    #voice#Garcia
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(100)
    Fade(500)
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)
    Sound(930, 2, 100, 0)
    OP_25(0x82, 0x32)
    OP_82(0x64, 0x0, 0xBB8, 0x5DC)
    MoveCamera(65, 17, 0, 1500)
    SetCameraDistance(22500, 1500)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    EndChrThread(0x8, 0x1)
    OP_82(0xC8, 0xC8, 0xBB8, 0x3E8)

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5S#25A#11Pガアアアアアアアアアッ！！\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0107F#6P#Nこ、これは……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0020
    ChrTalk(
        0x108,
        (
            "#0907F#6P#Nもしかして……\x01",
            "魔人化するのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0021
    ChrTalk(
        0x107,
        (
            "#0813F#6P#Nこ、こんな人がなったら\x01",
            "さすがに手に負えないわよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0022
    ChrTalk(
        0x104,
        "#0310F#6P#Nチッ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(-8370, -3000, 900, 0)
    MoveCamera(318, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x107, 0x73, 0x0)
    OP_93(0x108, 0x73, 0x0)
    SetCameraDistance(15500, 1500)
    SetChrChipByIndex(0x104, 0x28)
    SetChrSubChip(0x104, 0x0)

    def lambda_1248():
        OP_96(0xFE, 0xFFFFD634, 0xFFFFF060, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1248)
    WaitChrThread(0x104, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_6F(0x10)

    #C0023
    ChrTalk(
        0x104,
        (
            "#5P#0301F──おい、オッサン！\x02\x03",

            "百戦錬磨の元猟兵が、\x01",
            "何を腑抜けてやがるんだ！\x02\x03",

            "#0303Fしかもマフィアとはいえ、\x01",
            "あんたは一度“あの場所”から\x01",
            "抜けられたんだろうが……！？\x02\x03",

            "#0307Fその意地を見せてみろや！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#5P#0005Fランディ……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#5P#0208F……ランディさん……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-8100, -3000, 0, 0)
    MoveCamera(63, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    OP_93(0x107, 0x87, 0x0)
    OP_93(0x108, 0x87, 0x0)
    OP_0D()
    Sleep(500)
    #Sound(1860, 255, 100, 0)    #voice#Garcia
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    def lambda_13DF():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13DF)

    #C0026
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#4S#40Wガアアアアッ……！\x02\x03",

            "#50W……オオオオオオオ……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x9, 2, 0, 7)
    StopEffect(0x0, 0x2)
    PlayEffect(0x1, 0x1, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0027
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#60W……ァァアアア……オオオ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x9, 1, 0, 6)
    PlayEffect(0x2, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x1, 0x2)
    Fade(500)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x3)
    Sound(819, 0, 100, 0)
    OP_0D()
    Sleep(800)

    #C0028
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#3111F#60Wガハッ……ぐううっ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    EndChrThread(0x8, 0x1)
    OP_0D()
    Sleep(500)

    #C0029
    ChrTalk(
        0x103,
        "#3P#0202F#N……瘴気が消えた……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0030
    ChrTalk(
        0x102,
        "#6P#0102Fもしかして……元に戻ったの！？\x02",
    )

    CloseMessageWindow()

    def lambda_15CF():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15CF)
    WaitChrThread(0x8, 1)

    #C0031
    ChrTalk(
        0x8,
        (
            "#11P#3111F#50Wがはッ……げほげほ……\x02\x03",

            "#3110F#50W……はあはあはあはあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#6P#0304Fハッ……\x01",
            "やりゃあ出来んじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P#3103F#40W……フン……\x01",
            "偉そうな事を抜かしやがって……\x02\x03",

            "#3100Fだが……どうやら……\x01",
            "礼を言う必要がありそうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#0013Fやはりヨアヒムに\x01",
            "《グノーシス》を……？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#11P#3103F#40Wああ……\x01",
            "直接注射して来やがった……\x02\x03",

            "#3101F……あの野郎……最初から\x01",
            "うさんくせぇと思ってたんだ……\x02\x03",

            "#3107Fクソ……よくも俺の部下たちを……！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#0003F……彼は自分たちが逮捕する。\x02\x03",

            "#0001F悪いけど、あなたたちも\x01",
            "逮捕は避けられないと思ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#11P#3104F#40W……フン……\x01",
            "ここまで醜態さらしちゃ\x01",
            "仕方ねぇだろう……\x02\x03",

            "……たぶんあの野郎は\x01",
            "この先にいるはずだ……\x02\x03",

            "#3102F《闘神の息子》……\x01",
            "それにロイドと言ったか……\x02\x03",

            "てめえらは気に喰わねぇが……\x01",
            "あの野郎はもっと気に喰わねぇ……\x02\x03",

            "#3107F絶対に……\x01",
            "後#2Rおく#れを取るんじゃねえぞ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_194B():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_194B)
    WaitChrThread(0x8, 1)
    Fade(500)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sound(514, 0, 100, 0)
    OP_0D()
    StopBGM(0x1F40)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_68(-8100, -3000, 0, 2000)
    MoveCamera(47, 17, 0, 2000)
    SetCameraDistance(17500, 2000)

    def lambda_19B2():
        OP_96(0xFE, 0xFFFFE69C, 0xFFFFF060, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19B2)
    Sleep(600)

    def lambda_19CF():
        OP_98(0xFE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19CF)
    Sleep(100)

    def lambda_19EC():
        OP_98(0xFE, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_19EC)

    def lambda_1A06():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A06)
    Sleep(50)

    def lambda_1A23():
        OP_98(0xFE, 0x898, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A23)

    def lambda_1A3D():
        OP_98(0xFE, 0x76C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1A3D)
    WaitChrThread(0x101, 1)

    def lambda_1A5B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A5B)

    def lambda_1A68():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1A68)

    def lambda_1A75():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1A75)
    Fade(250)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    #C0038
    ChrTalk(
        0x104,
        "#5P#0306F……落ちたか。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#5P#0008Fああ……\x01",
            "完全に気絶している。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x108,
        (
            "#6P#0900F多分、魔人化に抵抗するのに\x01",
            "力を使い果たしたんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x107,
        (
            "#5P#0803Fうーん、悪人かもしれないけど、\x01",
            "一本筋は通ってる人かも……\x02\x03",

            "#0800F少なくとも、あの会長さんよりは\x01",
            "共感できそうな気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#6P#0100Fそうね……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#6P#0204F……同感です。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#5P#0304Fフン……\x01",
            "ま、さすがと言っとくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#5P#0000Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x101, 0x10E, 0x1F4)
    Fade(500)
    OP_68(-8100, -3100, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0003F#5P──どうやらこの先に\x01",
            "真の黒幕がいるみたいだ。\x02\x03",

            "#0008Fアーネストにガルシア……\x01",
            "２人の様子から判断するに\x01",
            "恐ろしく危険な相手だろう。\x02\x03",

            "#0001Fみんな……準備はいいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#12P#0101Fええ……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#12P#0201F……はい！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#6P#0307Fいつでも行けるぜ！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x107,
        "#3P#0807Fこちらも任せて！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x108,
        "#6P#0901F準備は出来ている！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0004F──よし。\x02\x03",

            "#0013Fこれより教団幹部司祭、\x01",
            "ヨアヒム・ギュンターの拘束、\x01",
            "および逮捕に踏み込む……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0053
    ChrTalk(
        0x101,
        "#0007F#5P各自、全力を尽くしてくれ！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("メンバーたち")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(1153, 255, 100, 0)    #voice#Elie
    #Sound(1249, 255, 100, 1)    #voice#Tio
    #Sound(1343, 255, 100, 2)    #voice#Randy
    #Sound(1689, 255, 100, 3)    #voice#Estelle
    #Sound(1759, 255, 100, 4)    #voice#Joshua

    #A0054
    AnonymousTalk(
        0xFF,
        "#5Sおおっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -5000, -4000, 3000, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_37()
    OP_68(-10000, -1000, 0, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(28000, 0)
    SetChrPos(0x0, -10000, -4000, 0, 90)
    SetChrPos(0x1, -10000, -4000, 0, 90)
    SetChrPos(0x2, -10000, -4000, 0, 90)
    SetChrPos(0x3, -10000, -4000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE6, 4)
    OP_29(0x4F, 0x1, 0xA)
    SetMapObjFrame(0xFF, "moya1", 0x1, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x2)
    OP_25(0x82, 0x64)
    OP_24(0x35D)
    OP_24(0x3A2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_5_DC0 end

    def Function_6_200F(): pass

    label("Function_6_200F")

    OP_25(0x35D, 0x5A)
    Sleep(200)
    OP_25(0x35D, 0x50)
    Sleep(200)
    OP_25(0x35D, 0x46)
    Sleep(200)
    OP_25(0x35D, 0x3C)
    Sleep(200)
    OP_25(0x35D, 0x32)
    Sleep(200)
    OP_25(0x35D, 0x28)
    Sleep(200)
    OP_25(0x35D, 0x1E)
    Sleep(200)
    OP_25(0x35D, 0x14)
    Sleep(200)
    OP_25(0x35D, 0xA)
    Sleep(200)
    OP_24(0x35D)
    Return()

    # Function_6_200F end

    def Function_7_2052(): pass

    label("Function_7_2052")

    OP_25(0x3A2, 0x5A)
    Sleep(400)
    OP_25(0x3A2, 0x50)
    Sleep(400)
    OP_25(0x3A2, 0x46)
    Sleep(400)
    OP_25(0x3A2, 0x3C)
    Sleep(400)
    OP_25(0x3A2, 0x32)
    Sleep(400)
    OP_25(0x3A2, 0x28)
    Sleep(400)
    OP_25(0x3A2, 0x1E)
    Sleep(400)
    OP_25(0x3A2, 0x14)
    Sleep(400)
    OP_25(0x3A2, 0xA)
    Sleep(400)
    OP_24(0x3A2)
    Return()

    # Function_7_2052 end

    SaveToFile()

Try(main)
