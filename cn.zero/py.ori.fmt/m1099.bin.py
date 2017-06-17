from ZeroScenarioHelper import *

def main():
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
        "银",                     # 1
        "银",                     # 2
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
        "Function_3_F05",          # 03, 3
        "Function_4_F7A",          # 04, 4
        "Function_5_310F",         # 05, 5
        "Function_6_3127",         # 06, 6
        "Function_7_31B0",         # 07, 7
        "Function_8_3215",         # 08, 8
        "Function_9_3220",         # 09, 9
        "Function_10_322B",        # 0A, 10
        "Function_11_3236",        # 0B, 11
        "Function_12_3241",        # 0C, 12
        "Function_13_324C",        # 0D, 13
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
        "#0005F#5P这里是……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#0105F#6P巨大的书架，还有……\x01",
            "那个好像是类似天球仪的东西？\x02",
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
        "声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4P呵呵……\x01",
            "此处可谓是古代炼金术师们\x01",
            "所建造的梦之遗迹。\x02",
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
            "#0007F#1P你是……！\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        "#0101F#1P黑衣，还有面具……！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        "#0307F#1P终于出现了啊……！\x02",
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P初次见面，特别任务支援科的诸位。\x02\x03",

            "看起来，似乎还混进了\x01",
            "一位多余之人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0501F#1P……我只负责后援而已，\x01",
            "请不要在意。\x02",
        )
    )

    CloseMessageWindow()

    #N0009
    NpcTalk(
        0x8,
        "黑衣男子",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P呵……算了，无妨。\x02",
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
            "初次会面──\x01",
            "吾名为『银』。\x02\x03",

            "首先，要向应吾之邀\x01",
            "远道而来的诸位表示慰问。\x07\x00\x02",
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
            "#0006F#6P……嗯，我们确实是\x01",
            "被你牵着鼻子东奔西跑了一番呢。\x02\x03",

            "#0001F顺便一问，塔内那些诡异的魔兽\x01",
            "都是你布置的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P呵呵……它们一直以来\x01",
            "都在这座塔中徘徊。\x02\x03",

            "为避免自己的技艺有所生疏，\x01",
            "吾时常会寻找具有挑战性的修炼场，\x01",
            "于是便发现了这座塔……\x02\x03",

            "此处实在是个让人兴趣颇深的地方啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0005F#6P……原来那不是你布置的吗。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#0203F#12P嗯，这种规模确实也不是\x01",
            "一个人就可以轻松布置的。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P那么，虽然诸位必定\x01",
            "尚有不少疑问……\x07\x00\x02",
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
            "#0702F#5P但在那之前，\x01",
            "请先通过最后一道试炼吧。\x07\x00\x02",
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
        "#0007F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0101F#11P你想做什么……！？\x02",
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
            "#0700F#5P──吾对弱者并无兴趣。\x02\x03",

            "而诸位的实力究竟能否\x01",
            "回应吾之期待……\x02\x03",

            "还请亲自向吾证明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0013F#6P呜……\x02",
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
        "#0206F#2P果然免不了这一关吗……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#0304F#2P嘿，虽然想说不愿意\x01",
            "以多欺少，不过……\x02\x03",

            "#0307F大家要小心啊！\x01",
            "这家伙实在是强得惊人！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x109,
        (
            "#0501F#2P看起来，似乎没有\x01",
            "手下留情的必要呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#0107F#2P嗯，全力迎战吧！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P呵呵……有此斗志，实属上佳。\x02\x03",

            "#0707F──那么，失敬了！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(15500, 400)
    BlurSwitch(0x190, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)

    def lambda_ED4():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_ED4)
    Sleep(400)
    Battle("BattleInfo_238", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 4)
    Return()

    # Function_2_2DB end

    def Function_3_F05(): pass

    label("Function_3_F05")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x3)
    ClearChrFlags(0xFE, 0x1)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_F1F():
        OP_9D(0xFE, 0x4D8, 0x0, 0x14A0, 0x6D6, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F1F)
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

    # Function_3_F05 end

    def Function_4_F7A(): pass

    label("Function_4_F7A")

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
        "#0007F#11P呼、呼……怎么样！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0110F#11P赢、赢了吗……？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        "#0206F#11P……好累。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#0500F#11P不过，我们总算是……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        "#0301F#11P不……我们还是不行。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        "#0505F#11P哎……\x02",
    )

    CloseMessageWindow()
    Sound(1628, 255, 100, 0)    #voice#Yin
    Sleep(500)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("银的声音")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "那边那位兄台\x01",
            "似乎颇具实力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_68(-4230, 1100, 300, 1500)
    Sleep(1200)
    PlayEffect(0x0, 0xFF, 0x9, 0x0, 0, 650, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 13)

    def lambda_12C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_12C8)
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
        "#0005F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#0205F#11P『符』……！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 50, 0, 9990, 180)
    OP_68(160, 500, 7640, 2000)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_13F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_13F6)

    def lambda_1407():
        OP_95(0xFE, 50, 0, 7710, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1407)
    Sleep(300)

    def lambda_1424():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1424)
    Sleep(50)

    def lambda_1434():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1434)

    def lambda_1441():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1441)
    Sleep(50)

    def lambda_1451():
        TurnDirection(0xFE, 0x8, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1451)

    def lambda_145E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_145E)
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
        "#0105F#11P究、究竟是什么时候……！？\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        "#0501F#11P完、完全没注意到……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0303F#11P在战斗中只留下分身，\x01",
            "然后就站在高处旁观吗。\x02\x03",

            "#0301F你的实力的确强得可怕……\x01",
            "但这种兴趣实在是令人难以恭维吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P呵呵……\x01",
            "若使阁下产生不快，吾便在此谢罪了。\x02\x03",

            "#0702F然而，竟然能在战斗中\x01",
            "看穿吾之一招一式。\x02\x03",

            "的确是值得赞赏的动态视力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0306F#11P哈，毕竟我也积累了\x01",
            "不少实战经验嘛。\x02\x03",

            "#0301F那么……还要继续再打吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P呵……算了，就到此为止吧。\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2EF8")

    #C0041
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F#11P……你的实力之强的确毋庸置疑。\x01",
            "凭现在的我们，恐怕难以取胜。\x02\x03",

            "#0001F既然你如此厉害，找我们又能有什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵……\x01",
            "罗伊德·班宁斯。\x02\x03",

            "阁下应该已经隐约得出结论了吧？\x02",
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
        "#0105F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        "#0205F#11P这是怎么回事呢……？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P吾对阁下进行过调查。\x02\x03",

            "身为一名搜查官，阁下之直觉\x01",
            "似乎在办案过程中起到了相当的作用。\x02\x03",

            "既然如此，阁下应当也已明白吾之要事为何了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#11P是啊……说的没错。\x02\x03",

            "#0001F你找我们是因为──\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAC")
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
            "#1K银的要事是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【关于彩虹剧团】\x01",      # 0
            "【关于鲁巴彻】\x01",        # 1
            "【关于恐吓信】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A39"),
        (1, "loc_1AC8"),
        (2, "loc_1B35"),
        (SWITCH_DEFAULT, "loc_1BA7"),
    )


    label("loc_1A39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A4D")
    OP_2C(0x42, 0x1)

    label("loc_1A4D")


    #C0049
    ChrTalk(
        0x101,
        (
            "#0006F#11P（不对，虽然并不是完全没关系，\x01",
            "  但重点并不是彩虹剧团……）\x02\x03",

            "#0001F（真正有关系的是……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1BA7")

    label("loc_1AC8")


    #C0050
    ChrTalk(
        0x101,
        (
            "#0006F#11P（不对，这和此次事件\x01",
            "  完全没有任何关系……）\x02\x03",

            "#0001F（真正有关系的是……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1BA7")

    label("loc_1B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B49")
    OP_2C(0x42, 0x2)

    label("loc_1B49")


    #C0051
    ChrTalk(
        0x101,
        (
            "#0003F#11P最初寄给彩虹剧团的\x01",
            "伊莉娅小姐的那封恐吓信……\x02\x03",

            "#0001F是关于这件事情的吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA7")

    label("loc_1BA7")

    Jump("loc_1996")

    label("loc_1BAC")


    #C0052
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵，正是如此……\x02\x03",

            "那么，吾之要事，是与\x01",
            "那封恐吓信的『何种方面』有关呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#11P那是……\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E34")
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
            "#1K是关于恐吓信的什么方面呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【恐吓信的文风】\x01",          # 0
            "【恐吓信的寄信人】\x01",        # 1
            "【恐吓信的真正目的】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1CE8"),
        (1, "loc_1D4D"),
        (2, "loc_1DA2"),
        (SWITCH_DEFAULT, "loc_1E2F"),
    )


    label("loc_1CE8")


    #C0055
    ChrTalk(
        0x101,
        (
            "#0006F#11P（不对，和这个\x01",
            "  并没有多大关系……）\x02\x03",

            "#0001F（真正有关系的是……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1E2F")

    label("loc_1D4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D61")
    OP_2C(0x42, 0x2)

    label("loc_1D61")


    #C0056
    ChrTalk(
        0x101,
        (
            "#0003F#11P寄出那封恐吓信的……\x02\x03",

            "#0001F其实并不是你吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2F")

    label("loc_1DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB6")
    OP_2C(0x42, 0x1)

    label("loc_1DB6")


    #C0057
    ChrTalk(
        0x101,
        (
            "#0008F#11P（不对，虽然并不是完全无关，\x01",
            "  但在那之前，应该先指出另一件事……）\x02\x03",

            "#0001F（那是……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_1E2F")

    label("loc_1E2F")

    Jump("loc_1C2D")

    label("loc_1E34")

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
        "#0105F#11P哎……！？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        "#0305F#11P这是怎么一回事……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#0201F#11P难道……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵，正是如此……\x02\x03",

            "#0700F将那封恐吓信寄至伊莉娅·普拉提耶\x01",
            "处的，并非本人——『银』。\x02\x03",

            "而是某个假借吾之名号之人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#0006F#11P果然如此吗……\x02\x03",

            "#0008F……在调查的过程中，\x01",
            "我就觉得非常不对劲。\x02\x03",

            "传说中的杀手……东方人街的魔人……\x02\x03",

            "越是深入调查，\x01",
            "越是觉得他的存在感不断变强。\x02\x03",

            "#0013F但是，与其相比，\x01",
            "最初的那封恐吓信，该怎么说呢……\x01",
            "给人的感觉却只像是虚张声势而已。\x02\x03",

            "甚至连伊莉娅小姐自己\x01",
            "都坚信那只是个恶作剧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵……正是如此。\x02\x03",

            "伊莉娅·普拉提耶是个天才。\x02\x03",

            "恐怕她凭借着直觉，\x01",
            "就已经察觉到那封信其实\x01",
            "并非以自己为目标了。\x02\x03",

            "#0700F然而──新的问题便由此而生：\x01",
            "既然如此，为何犯人要将那种东西\x01",
            "特意送至彩虹剧团呢？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x109,
        (
            "#0506F#11P这、这个……\x01",
            "虽然我不太清楚。\x02\x03",

            "#0501F不过，也许正是因为这样胡乱寄出，\x01",
            "所以才是一个普通的恶作剧吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#0003F#11P不，寄信者明显是\x01",
            "知道『银』已经来到\x01",
            "克洛斯贝尔的人。\x02\x03",

            "#0001F黑月、鲁巴彻、搜查一科……\x02\x03",

            "再有就是与他们有所关联的人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        (
            "#0505F#11P原来如此……\x02\x03",

            "#0506F这样一想，确实就\x01",
            "不像是普通的恶作剧了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P不错……然而，\x01",
            "区区一封恐吓信，是无法让\x01",
            "彩虹剧团的新剧公演中止的。\x02\x03",

            "此外，指名道姓地宣告要对\x01",
            "伊莉娅下手，也令人费解。\x02\x03",

            "其结果，只会招来搜查一科的介入，\x01",
            "使他们在伊莉娅周边采取防护措施，\x01",
            "形成万无一失的保护体制。\x02\x03",

            "如此一来，犯人即使想袭击\x01",
            "舞台上的目标，也无从下手。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#0208F#11P也就是说……\x02\x03",

            "犯人寄出这封恐吓信，\x01",
            "正是想要造成这样的状况，\x01",
            "以便让自己达成其它目的……\x02\x03",

            "#0201F或者说，以便让自己今后\x01",
            "可以顺利达成某些目的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P那种可能恐怕相当之高。\x02\x03",

            "#0702F──于此，吾正式向诸位提出委托。\x02\x03",

            "希望诸位可以查明假借吾之名号之人，\x01",
            "并阻止其野心。\x07\x00\x02",
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
        "#0011F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0301F#11P喂喂，\x01",
            "你想得也太美了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵……\x01",
            "阁下所言，未免有些不妥吧？\x02\x03",

            "此人身份，以及其目的到底为何，\x01",
            "虽然吾亦无法猜透……\x02\x03",

            "然而，事态并非无足轻重，\x01",
            "仅此一点，诸位应当也心知肚明吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        "#0303F#11P嘁……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0106F#11P确实，那种可能性很高呢。\x02\x03",

            "#0101F不过……为什么要特意\x01",
            "向我们提出这种委托呢？\x02\x03",

            "你自己去调查不就好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P……………………………………\x02\x03",

            "#0702F呵呵，吾毕竟亦可谓\x01",
            "任务繁重，无暇分身呢。\x02\x03",

            "例如，要对付鲁巴彻之辈。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#0013F#11P唔……\x02\x03",

            "你果然在协助『黑月』，\x01",
            "参与黑手党的暗斗吗……\x02\x03",

            "#0007F竟然利用我们克洛斯贝尔警察\x01",
            "无法对其出手这一点……！\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵，不必如此剑拔弩张。\x02\x03",

            "游击士协会相当棘手，因此吾亦会\x01",
            "尽量注意，不将民间人士牵连至此。\x02\x03",

            "不过，鲁巴彻那边是否也会如此\x01",
            "善良，可就不得而知了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#0013F#11P你……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P无论如何，竟敢假借吾之名号\x01",
            "肆意妄为，此等行为绝不可姑息。\x02\x03",

            "是否接受吾之委托──请回答。\x07\x00\x02",
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
            "#0006F#11P明白了……\x02\x03",

            "#0001F虽然并不是为了你的委托，\x01",
            "但我们会协助你，阻止真凶的企图。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵……如此即可。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#0201F#11P……不过，要怎么做呢？\x02\x03",

            "什么人，在什么时候，要做什么事，\x01",
            "这些问题我们还都没有任何线索……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#1P吾对『何时』这个问题，倒是有些估量。\x02\x03",

            "若那个真犯人企图\x01",
            "利用彩虹剧团\x01",
            "来实行其计划……\x02\x03",

            "恐怕会选择正式公演的初日，或是预演当日吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0005F#11P正式公演的初日，和预演当日……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        (
            "#0306F#11P我也有同感啊。\x02\x03",

            "#0301F要说最热闹的日子，\x01",
            "显然还是正式公演的第一天……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#0101F#11P……而特别预演将会邀请所有相关人员，\x01",
            "并首次公开新剧目，\x01",
            "所以也是一个相当好的目标吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵，正是如此。\x02\x03",

            "#0700F吾对诸位的委托，\x01",
            "其内容便是在那两日进行警戒……\x02\x03",

            "为防止搜查一科有所察觉，\x01",
            "还请诸位在剧场内秘密巡视。\x02\x03",

            "此外，若发生紧急状况，\x01",
            "请务必迅速采取适当对策。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0006F#11P……真是自说自话……\x02\x01",

            "#0000F不过，你说的也确实有道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        (
            "#0104F#11P彩虹剧团那边，只要提出申请，\x01",
            "在剧场内巡逻应该是没有问题的。\x02\x03",

            "#0108F主要问题是能否\x01",
            "混过一科那边的耳目啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        (
            "#0206F#11P是啊……如果被他们发现，\x01",
            "肯定会被赶出剧场的。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#0300F#11P算了，万全之策是不存在的，\x01",
            "到时候只要随机应变，总会有办法解决的。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#1P呵呵，诸位既然愿意接受委托，便是再好不过。\x07\x00\x02",
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
            "#0702F#11P──那么，吾便\x01",
            "先行告辞了。\x02\x03",

            "衷心期待诸位的捷报。\x07\x00\x02",
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
        "#0005F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        "#0501F#11P等、等一下……！\x02",
    )

    CloseMessageWindow()

    label("loc_2EF8")

    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(17020, 1000)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    OP_95(0x8, -110, 0, 13100, 6000, 0x0)
    OP_6F(0x79)

    #C0096
    ChrTalk(
        0x101,
        "#0007F#11P慢、慢着……！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        "#0307F#11P怎么会让你逃走……！\x02",
    )

    CloseMessageWindow()
    OP_68(-400, 1400, 4860, 1500)

    def lambda_2F7F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F7F)
    Sleep(50)

    def lambda_2F97():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F97)
    Sleep(50)

    def lambda_2FAF():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FAF)
    Sleep(50)

    def lambda_2FC7():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FC7)
    Sleep(50)

    def lambda_2FDF():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FDF)
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

    # Function_4_F7A end

    def Function_5_310F(): pass

    label("Function_5_310F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3126")
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    Jump("Function_5_310F")

    label("loc_3126")

    Return()

    # Function_5_310F end

    def Function_6_3127(): pass

    label("Function_6_3127")

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

    # Function_6_3127 end

    def Function_7_31B0(): pass

    label("Function_7_31B0")

    OP_95(0xFE, -1580, 4560, 23840, 5000, 0x1)
    OP_95(0xFE, 6950, 6760, 23080, 5000, 0x1)
    OP_95(0xFE, 12690, 8390, 20300, 5000, 0x1)
    OP_95(0xFE, 17630, 10020, 16290, 5000, 0x1)
    OP_95(0xFE, 21340, 11580, 11360, 5000, 0x1)
    Return()

    # Function_7_31B0 end

    def Function_8_3215(): pass

    label("Function_8_3215")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_8_3215 end

    def Function_9_3220(): pass

    label("Function_9_3220")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_9_3220 end

    def Function_10_322B(): pass

    label("Function_10_322B")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_10_322B end

    def Function_11_3236(): pass

    label("Function_11_3236")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_11_3236 end

    def Function_12_3241(): pass

    label("Function_12_3241")

    BeginChrThread(0xFE, 2, 0, 7)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_12_3241 end

    def Function_13_324C(): pass

    label("Function_13_324C")


    def lambda_3251():
        OP_97(0xFE, 0x0, 0xFFFFFDA8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3251)

    def lambda_326B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_326B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_324C end

    SaveToFile()

Try(main)
