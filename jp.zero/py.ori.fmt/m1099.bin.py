from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1099.bin",                # FileName
        "m1099",                    # MapName
        "m1099",                    # Location
        0x00A2,                     # MapIndex
        "ed7304",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, -10000, 0, 0, 1, 162, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1099",                  # 0
        "銀",                     # 1
        "銀",                     # 2
        "符",                     # 3
        "BM1010",                 # 4
    ))

    ATBonus("ATBonus_158", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_218", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_224", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_234", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_200", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_204", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_208", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_210", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_238", 0x0052, 22, 6, 0, 0, 0, 0, 0, "BM1010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02800.dat", 0, 0, 0, 0, 0, "ms02801.dat", 0, "MonsterBattlePostion_218", "MonsterBattlePostion_1F8", "ed7404", "ed7000", "ATBonus_158"),
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
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_2B4",          # 00, 0
        "Function_1_2DA",          # 01, 1
        "Function_2_2DB",          # 02, 2
        "Function_3_F87",          # 03, 3
        "Function_4_FFC",          # 04, 4
        "Function_5_331B",         # 05, 5
        "Function_6_3333",         # 06, 6
        "Function_7_33BC",         # 07, 7
        "Function_8_3421",         # 08, 8
        "Function_9_342C",         # 09, 9
        "Function_10_3437",        # 0A, 10
        "Function_11_3442",        # 0B, 11
        "Function_12_344D",        # 0C, 12
        "Function_13_3458",        # 0D, 13
    ))


    def Function_0_2B4(): pass

    label("Function_0_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_2CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_2D9")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_2D9")

    Return()

    # Function_0_2B4 end

    def Function_1_2DA(): pass

    label("Function_1_2DA")

    Return()

    # Function_1_2DA end

    def Function_2_2DB(): pass

    label("Function_2_2DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00850.itc", 0x26)
    LoadChrToIndex("chr/ch00851.itc", 0x27)
    LoadChrToIndex("chr/ch00500.itc", 0x28)
    LoadChrToIndex("chr/ch00501.itc", 0x29)
    LoadChrToIndex("chr/ch00550.itc", 0x2A)
    LoadChrToIndex("chr/ch00551.itc", 0x2B)
    SetChrPos(0x101, -270, 0, -22390, 0)
    SetChrPos(0x102, -1130, 0, -23750, 0)
    SetChrPos(0x103, 530, 0, -23830, 0)
    SetChrPos(0x104, 540, 0, -25330, 0)
    SetChrPos(0x109, -1210, 0, -25020, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 6120, 6160, 15750, 180)
    SetChrFlags(0x8, 0x8000)
    ClearMapFlags(0x10000000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    FadeToBright(1000, 0)
    OP_68(0, 1800, -20000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(24000, 0)
    OP_68(0, 1800, 0, 10000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_4A5():
        OP_95(0xFE, -270, 0, 1610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A5)

    def lambda_4BF():
        OP_95(0xFE, -1130, 0, 250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BF)

    def lambda_4D9():
        OP_95(0xFE, 530, 0, 170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D9)

    def lambda_4F3():
        OP_95(0xFE, 540, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4F3)

    def lambda_50D():
        OP_95(0xFE, -1210, 0, -1020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_50D)
    OP_0D()
    Sleep(3000)
    Fade(1000)
    OP_68(710, 1100, 11810, 0)
    MoveCamera(57, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(41050, 0)
    OP_68(-200, 1100, 0, 9000)
    MoveCamera(45, 28, 0, 9000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-20, 1100, 810, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18050, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_0D()
    Sleep(500)

    #C0001
    ChrTalk(
        0x101,
        "#0005F#5Pここは……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#0105F#6P巨大な書棚に……\x01",
            "あれは天球儀のようなものかしら？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    #Sound(1629, 255, 100, 0)    #voice#Yin
    Sleep(800)

    #N0003
    NpcTalk(
        0x8,
        "声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4Pフフ……\x01",
            "古の錬金術師どもが造った\x01",
            "夢の跡といったところか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(8400, 6400, 15410, 3000)
    MoveCamera(60, 16, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(17440, 3000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6F(0x79)

    #C0004
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0007F#1Pお前は……！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#0101F#1P黒装束に仮面……！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        "#0307F#1P出やがったな……！\x02",
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P初めまして、特務支援課の諸君。\x02\x03",

            "どうやら余計な者が一人、\x01",
            "紛れ込んでいるようだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0501F#1P……自分はただのサポートです。\x01",
            "気にしないでください。\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0x8,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5Pフ……まあいいだろう。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 3)
    OP_68(740, 1000, 2780, 2500)
    MoveCamera(14, 13, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(22410, 1450)
    OP_6F(0x10)
    SetCameraDistance(20410, 1050)
    SetChrPos(0x109, -420, 0, -960, 315)
    SetChrPos(0x104, 740, 0, -1400, 315)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x103, 0x8, 0)
    TurnDirection(0x104, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x8, 0x104, 0)
    OP_6F(0x79)
    WaitChrThread(0x8, 3)
    Sleep(500)
    #Sound(1627, 255, 100, 0)    #voice#Yin
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0010
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "お初にお目にかかる──\x01",
            "《銀#2Rイン#》という者だ。\x02\x03",

            "まずはここまで\x01",
            "足労願ったことを労#2Rねぎら#おう。\x07\x00\x02",
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

    #C0011
    ChrTalk(
        0x101,
        (
            "#0006F#6P……ああ、随分と\x01",
            "引きずり回してくれたもんだな。\x02\x03",

            "#0001Fちなみに、塔にいる奇妙な魔獣は\x01",
            "あんたが用意したものなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pフフ……あれは元から\x01",
            "この塔の中に徘徊していた。\x02\x03",

            "腕を鈍らせないよう、\x01",
            "歯ごたえのある狩場を捜して\x01",
            "この塔を見つけたのだが……\x02\x03",

            "中々どうして、面白い場所だ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0005F#6P……あんたの仕業じゃないのか。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#0203F#12Pまあ、個人がどうこう\x01",
            "できるものでもありませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5Pさて、色々と\x01",
            "疑問はあるだろうが……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrPos(0x8, 1290, 0, 6620, 180)
    OP_68(1340, 1000, 3930, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21410, 0)
    SetCameraDistance(20410, 1000)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pまずはその前に、\x01",
            "最後の試しをさせてもらおう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x101,
        "#0007F#6Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0101F#11Pどういうつもり……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(500)
    PlayBGM("ed7404", 0)

    #C0019
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P──弱き者には興味はない。\x02\x03",

            "お前たちが、わが望みに\x01",
            "適う強さを持っているか……\x02\x03",

            "その身で証明してもらうぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0013F#6Pくっ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0021
    ChrTalk(
        0x103,
        "#0206F#2Pやっぱりお約束ですか……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#0304F#2Pヘッ、多勢に無勢と\x01",
            "言いたいところだが……\x02\x03",

            "#0307F気をつけろ！\x01",
            "コイツ、凄まじく強いぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x109,
        (
            "#0501F#2Pどうやら手加減する必要は\x01",
            "なさそうですね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#0107F#2Pええ、全力で行きましょう！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pふふ……いい闘志だ。\x02\x03",

            "#0707F──それでは行くぞ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(15500, 400)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)

    def lambda_F56():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F56)
    Sleep(400)
    Battle("BattleInfo_238", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 4)
    Return()

    # Function_2_2DB end

    def Function_3_F87(): pass

    label("Function_3_F87")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_FA1():
        OP_9D(0xFE, 0x4D8, 0x0, 0x14A0, 0x6D6, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA1)
    Sound(814, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrSubChip(0xFE, 0x3)
    SetChrFlags(0xFE, 0x1)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    Sound(43, 0, 100, 0)
    Sleep(50)
    Sound(30, 0, 100, 0)
    Return()

    # Function_3_F87 end

    def Function_4_FFC(): pass

    label("Function_4_FFC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00850.itc", 0x26)
    LoadChrToIndex("chr/ch00851.itc", 0x27)
    LoadChrToIndex("chr/ch00500.itc", 0x28)
    LoadChrToIndex("chr/ch00501.itc", 0x29)
    LoadChrToIndex("chr/ch00550.itc", 0x2A)
    LoadChrToIndex("chr/ch00551.itc", 0x2B)
    LoadChrToIndex("chr/ch00553.itc", 0x2C)
    LoadChrToIndex("apl/ch50221.itc", 0x2D)
    OP_68(-2770, 1100, -50, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21470, 0)
    SetChrPos(0x101, -2590, 0, -90, 270)
    SetChrPos(0x102, -1330, 0, -790, 270)
    SetChrPos(0x103, -150, 0, 490, 270)
    SetChrPos(0x104, -240, 0, -1700, 270)
    SetChrPos(0x109, 970, 0, -440, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0xA, 0x2D)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -6220, 600, 450, 90)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x3)
    SetChrPos(0x9, -6220, 0, 450, 90)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -470, 0, 13300, 180)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadEffect(0x0, "event\\ev200_00.eff")
    LoadEffect(0x1, "event\\ev202_00.eff")
    FadeToBright(1000, 0)
    SetCameraDistance(19470, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0026
    ChrTalk(
        0x101,
        "#0007F#11Pはあはあ……どうだ！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0110F#11Pや、やったの……？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        "#0206F#11P……疲れました。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#0500F#11Pでも、これで何とか……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#0301F#11Pいや……駄目だ。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        "#0505F#11Pえ……\x02",
    )

    CloseMessageWindow()
    Sound(1628, 255, 100, 0)    #voice#Yin
    Sleep(500)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("銀の声")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "そちらの彼は\x01",
            "なかなか出来るようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_68(-4230, 1100, 300, 1500)
    Sleep(1200)
    PlayEffect(0x0, 0xFF, 0x9, 0x0, 0, 650, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 13)

    def lambda_1358():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1358)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x9, 0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(750)

    #C0033
    ChrTalk(
        0x101,
        "#0005F#11Pな……！？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#0205F#11P《符》……！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 50, 0, 9990, 180)
    OP_68(160, 500, 7640, 2000)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_1484():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1484)

    def lambda_1495():
        OP_95(0xFE, 50, 0, 7710, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1495)
    Sleep(300)

    def lambda_14B2():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14B2)
    Sleep(50)

    def lambda_14C2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14C2)

    def lambda_14CF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14CF)
    Sleep(50)

    def lambda_14DF():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14DF)

    def lambda_14EC():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14EC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    OP_6F(0x1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 100, 0)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-400, 1400, 3860, 0)
    MoveCamera(145, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x9, 50, -500, 7710, 180)
    SetChrPos(0x101, -260, 0, 760, 0)
    SetChrPos(0x102, -800, 0, -280, 0)
    SetChrPos(0x103, -900, 0, -1750, 0)
    SetChrPos(0x104, 1130, 0, -130, 0)
    SetChrPos(0x109, 660, 0, -1760, 0)
    OP_0D()

    #C0035
    ChrTalk(
        0x102,
        "#0105F#11Pい、いつの間に……！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        "#0501F#11Pき、気付かなかった……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0303F#11P戦闘中に分身だけ残して\x01",
            "そこで高見の見物ってわけか。\x02\x03",

            "#0301F恐ろしく腕が立つようだが……\x01",
            "あまり良い趣味とは言えねぇな？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5Pふふ……\x01",
            "気に障ったのなら謝罪しよう。\x02\x03",

            "#0702Fしかし戦闘中に\x01",
            "私の動きを見切れるとは。\x02\x03",

            "なかなか大した動体視力だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0306F#11Pま、これでも実戦経験は\x01",
            "それなりに積んでるんでね。\x02\x03",

            "#0301Fそれで……まだ、やんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5Pフ……まあ、いいだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x28)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
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
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3108")

    #C0041
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F#11P……あんたの強さは本物だ。\x01",
            "今の俺たちじゃ勝てないだろう。\x02\x03",

            "#0001Fそんなあんたが、俺たちに何の用だ？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pフフ……\x01",
            "ロイド・バニングス。\x02\x03",

            "薄々、見当は付いているのだろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F#11P……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#0105F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#0205F#11Pどういうことですか……？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1Pお前のことは調べている。\x02\x03",

            "どうやら捜査官として\x01",
            "それなりに勘が働くようだな。\x02\x03",

            "ならば私の用件も分かるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#11Pああ……そうだな。\x02\x03",

            "#0001Fあんたの用件というのは──\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6A")
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K銀の用件とは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【アルカンシェルについて】\x01",      # 0
            "【ルバーチェについて】\x01",          # 1
            "【脅迫状について】\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AE5"),
        (1, "loc_1B7E"),
        (2, "loc_1BEB"),
        (SWITCH_DEFAULT, "loc_1C65"),
    )


    label("loc_1AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF9")
    OP_2C(0x42, 0x1)

    label("loc_1AF9")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0006F#11P（いや、関係なくはないけど\x01",
            "  アルカンシェルそのものじゃない……）\x02\x03",

            "#0001F（関係があるとすれば……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1C65")

    label("loc_1B7E")


    #C0050
    ChrTalk(
        0x101,
        (
            "#0006F#11P（いや、これは今回は\x01",
            "  全く関係ない……）\x02\x03",

            "#0001F（関係があるとすれば……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1C65")

    label("loc_1BEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFF")
    OP_2C(0x42, 0x2)

    label("loc_1BFF")


    #C0051
    ChrTalk(
        0x101,
        (
            "#0003F#11P最初にアルカンシェルの\x01",
            "イリアさんに宛てた脅迫状……\x02\x03",

            "#0001Fそれについての話だな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C65")

    label("loc_1C65")

    Jump("loc_1A2A")

    label("loc_1C6A")


    #C0052
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pクク、その通り……\x02\x03",

            "では、その脅迫状の“何”について\x01",
            "話があるというのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#11Pそれは……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F0C")
    SetScenarioFlags(0x0, 0)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K脅迫状の何について話がある？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【脅迫状の文体】\x01",          # 0
            "【脅迫状の差出人】\x01",        # 1
            "【脅迫状の真の狙い】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1DAC"),
        (1, "loc_1E15"),
        (2, "loc_1E7E"),
        (SWITCH_DEFAULT, "loc_1F07"),
    )


    label("loc_1DAC")


    #C0055
    ChrTalk(
        0x101,
        (
            "#0006F#11P（いや、これは\x01",
            "  あまり関係ない……）\x02\x03",

            "#0001F（関係があるとすれば……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1F07")

    label("loc_1E15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E29")
    OP_2C(0x42, 0x2)

    label("loc_1E29")


    #C0056
    ChrTalk(
        0x101,
        (
            "#0003F#11Pあの脅迫状を送った人物……\x02\x03",

            "#0001Fそれは、あんたじゃないんだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F07")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E92")
    OP_2C(0x42, 0x1)

    label("loc_1E92")


    #C0057
    ChrTalk(
        0x101,
        (
            "#0008F#11P（いや、関係なくはないけど\x01",
            "  その前に指摘すべき事がある……）\x02\x03",

            "#0001F（それは……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1F07")

    label("loc_1F07")

    Jump("loc_1CEF")

    label("loc_1F0C")

    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x102,
        "#0105F#11Pえ……！？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        "#0305F#11Pどういう事だ……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0201F#11Pまさか……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pふふ、その通り……\x02\x03",

            "#0700Fあれをイリア・プラティエに\x01",
            "送ったのは、この《銀》ではない。\x02\x03",

            "私の名を騙#2Rかた#る何者かというわけだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0006F#11Pやっぱりか……\x02\x03",

            "#0008F……捜査をしている最中、\x01",
            "どうも違和感があったんだ。\x02\x03",

            "伝説の凶手……東方人街の魔人……\x02\x03",

            "調べて行けば行くほど\x01",
            "その存在感は強くなっていった。\x02\x03",

            "#0013Fだが、それに比べて\x01",
            "最初の脅迫状は何というか……\x01",
            "あまりにコケ脅しな匂いがした。\x02\x03",

            "イリアさんがイタズラだと\x01",
            "決め付けてしまうくらいに。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pふふ……その通り。\x02\x03",

            "イリア・プラティエは天才だ。\x02\x03",

            "おそらく直感的に、あの脅迫状が\x01",
            "本気で自分を狙ったものではないと\x01",
            "気付いたのだろう。\x02\x03",

            "#0700Fだが──ならば何故、\x01",
            "あんなものがアルカンシェルに\x01",
            "送られたかという話になる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#0506F#11Pそ、その……\x01",
            "よく判らないんですけど。\x02\x03",

            "#0501Fそれこそアンチあたりの\x01",
            "ただのイタズラじゃないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0003F#11Pいや、《銀》が\x01",
            "このクロスベルに来ていることを\x01",
            "知っている者は限られているんだ。\x02\x03",

            "#0001F黒月、ルバーチェ、捜査一課……\x02\x03",

            "あとはその関係者くらいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        (
            "#0505F#11Pなるほど……\x02\x03",

            "#0506Fそうなると確かに\x01",
            "イタズラって線は無さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1Pそう……だが脅迫状一つで、\x01",
            "アルカンシェルが新作の公開を\x01",
            "中止することはありえない。\x02\x03",

            "さらに名指しでイリアを狙うと\x01",
            "宣告したことについても不可解だ。\x02\x03",

            "その結果、捜査一課の介入を招き\x01",
            "イリア周辺の安全に関しては\x01",
            "万全の体制が敷かれる事になった。\x02\x03",

            "それこそ舞台中に狙われても\x01",
            "未然に防げるくらいにな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#0208F#11Pという事は……\x02\x03",

            "脅迫状を送って\x01",
            "この状況を作り上げることで\x01",
            "何か別の狙いを達成した……\x02\x03",

            "#0201Fあるいはこれから\x01",
            "達成しようとしている……？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1Pその可能性は高いだろう。\x02\x03",

            "#0702F──改めてお前たちに依頼する。\x02\x03",

            "我が名を騙ったその何者かの\x01",
            "企みを阻止してもらいたい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0070
    ChrTalk(
        0x101,
        "#0011F#11Pなに……！？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0301F#11Pおいおい。\x01",
            "何、ムシのいい事言ってやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pクク……\x01",
            "そんな事を言っていいのかな？\x02\x03",

            "その誰かが、何を狙っているのか\x01",
            "私にも見当は付かないが……\x02\x03",

            "ロクでもないことであるのは\x01",
            "目に見えているのではないか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        "#0303F#11Pチッ……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0106F#11P確かにその可能性は高そうね。\x02\x03",

            "#0101Fでも……どうして私たちに\x01",
            "わざわざそんな依頼を頼むの？\x02\x03",

            "あなた自身がやればいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P……………………………………\x02\x03",

            "#0702Fフフ、こう見えても\x01",
            "私はそれなりに忙しくてね。\x02\x03",

            "たとえばルバーチェどもの相手とか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#0013F#11Pっ……\x02\x03",

            "やっぱり《黒月》に協力して\x01",
            "マフィアと暗闘しているんだな……\x02\x03",

            "#0007F俺たちクロスベル警察が\x01",
            "手を出せないことをいいことに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pクク、そう恐い顔をするな。\x02\x03",

            "ギルドも面倒だし、一応民間人は\x01",
            "巻き込まぬように配慮しているさ。\x02\x03",

            "もっともルバーチェの方が\x01",
            "そこまで殊勝かどうかは知らないが。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#0013F#11Pお前……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1Pいずれにせよ、我が名を騙って\x01",
            "勝手な事をさせるわけにはいかない。\x02\x03",

            "依頼を受けるか否か──答えてもらおう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0080
    ChrTalk(
        0x101,
        (
            "#0006F#11P分かった……\x02\x03",

            "#0001Fあんたの頼みに応じるわけじゃないが\x01",
            "真犯人の企みの阻止には協力しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pふふ……それでいい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#0201F#11P……でも、どうするんですか？\x02\x03",

            "いつ、誰が何をしようとしているのか\x01",
            "全く見当も付かないというのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1Pいつ、というのは心当たりがある。\x02\x03",

            "もしその真犯人が\x01",
            "アルカンシェルに関することで\x01",
            "何かを仕掛けてくるとすれば……\x02\x03",

            "本公演の初日か、プレ公演だろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0005F#11P本公演の初日と、プレ公演……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0306F#11Pそいつは同感だな。\x02\x03",

            "#0301Fやっぱり最高に盛り上がるとしたら\x01",
            "本公演の初日になるだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#0101F#11P……関係者一同が招待されて、\x01",
            "お披露目をするプレ公演も\x01",
            "格好のターゲットというわけね？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pフフ、その通りだ。\x02\x03",

            "#0700Fお前たちに頼みたいのは\x01",
            "その両日における警戒活動……\x02\x03",

            "捜査一課が裏をかかれた時のため、\x01",
            "劇場内を密かに巡回するという事だ。\x02\x03",

            "そして、いざ何かあった時は\x01",
            "迅速な対処をしてもらいたい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0006F#11P……勝手を言う……\x02\x01",

            "#0000Fけど、筋は通ってるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0104F#11Pアルカンシェル方面に頼めば\x01",
            "劇場内の巡回は問題なさそうね。\x02\x03",

            "#0108F問題は一課の目を\x01",
            "誤魔化せるかくらいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        (
            "#0206F#11Pそうですね……見つかったら\x01",
            "つまみ出されそうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#0300F#11Pま、出たとこ勝負で\x01",
            "何とかするっきゃないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1Pフフ、引き受けてくれて何よりだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(300)

    #C0093
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11P──それでは私は\x01",
            "このあたりで失礼しよう。\x02\x03",

            "朗報を期待しているぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        "#0005F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        "#0501F#11Pちょ、ちょっと……！\x02",
    )

    CloseMessageWindow()

    label("loc_3108")

    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(17020, 1000)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    OP_95(0x8, -110, 0, 13100, 6000, 0x0)
    OP_6F(0x79)

    #C0096
    ChrTalk(
        0x101,
        "#0007F#11Pま、待て……！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        "#0307F#11P逃がすかよ……！\x02",
    )

    CloseMessageWindow()
    OP_68(-400, 1400, 4860, 1500)

    def lambda_318B():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_318B)
    Sleep(50)

    def lambda_31A3():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31A3)
    Sleep(50)

    def lambda_31BB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_31BB)
    Sleep(50)

    def lambda_31D3():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_31D3)
    Sleep(50)

    def lambda_31EB():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_31EB)
    Sleep(1500)
    Fade(500)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    SetChrPos(0x101, -680, 0, 3260, 270)
    SetChrPos(0x102, -2630, 0, 1420, 270)
    SetChrPos(0x103, 1040, 0, 0, 270)
    SetChrPos(0x104, -1850, 0, -1950, 270)
    SetChrPos(0x109, 970, 0, -3890, 270)
    OP_68(-2029, 3200, 9500, 0)
    MoveCamera(39, 3, 0, 0)
    SetCameraDistance(19380, 0)
    OP_68(11760, 12500, 14190, 8000)
    MoveCamera(340, 39, 0, 8000)
    SetCameraDistance(21130, 8000)
    BeginChrThread(0x8, 3, 0, 6)
    BeginChrThread(0x101, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x109, 3, 0, 12)
    BeginChrThread(0x103, 3, 0, 10)
    BeginChrThread(0x104, 3, 0, 11)
    OP_6F(0x1)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x8, 3)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("m1090", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_FFC end

    def Function_5_331B(): pass

    label("Function_5_331B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3332")
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    Jump("Function_5_331B")

    label("loc_3332")

    Return()

    # Function_5_331B end

    def Function_6_3333(): pass

    label("Function_6_3333")

    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x4)
    BeginChrThread(0xFE, 0, 0, 5)
    OP_95(0xFE, -1580, 4560, 23840, 7000, 0x1)
    OP_95(0xFE, 6950, 6760, 23080, 7000, 0x1)
    OP_95(0xFE, 12690, 8390, 20300, 7000, 0x1)
    OP_95(0xFE, 17630, 10020, 16290, 7000, 0x1)
    OP_95(0xFE, 21340, 11580, 11360, 7000, 0x1)
    EndChrThread(0xFE, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_6_3333 end

    def Function_7_33BC(): pass

    label("Function_7_33BC")

    OP_95(0xFE, -1580, 4560, 23840, 5000, 0x1)
    OP_95(0xFE, 6950, 6760, 23080, 5000, 0x1)
    OP_95(0xFE, 12690, 8390, 20300, 5000, 0x1)
    OP_95(0xFE, 17630, 10020, 16290, 5000, 0x1)
    OP_95(0xFE, 21340, 11580, 11360, 5000, 0x1)
    Return()

    # Function_7_33BC end

    def Function_8_3421(): pass

    label("Function_8_3421")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_8_3421 end

    def Function_9_342C(): pass

    label("Function_9_342C")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_9_342C end

    def Function_10_3437(): pass

    label("Function_10_3437")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_3437 end

    def Function_11_3442(): pass

    label("Function_11_3442")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_3442 end

    def Function_12_344D(): pass

    label("Function_12_344D")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_344D end

    def Function_13_3458(): pass

    label("Function_13_3458")


    def lambda_345D():
        OP_97(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_345D)

    def lambda_3477():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3477)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_3458 end

    SaveToFile()

Try(main)
