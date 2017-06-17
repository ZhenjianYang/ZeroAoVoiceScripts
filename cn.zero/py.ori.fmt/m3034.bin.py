from ZeroScenarioHelper import *

def main():
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
        "加尔西亚",               # 1
        "SE控制",                 # 2
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
        "Function_3_41D",          # 03, 3
        "Function_4_56B",          # 04, 4
        "Function_5_D44",          # 05, 5
        "Function_6_1E8F",         # 06, 6
        "Function_7_1ED2",         # 07, 7
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
            "加尔西亚完全失去意识了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_2_3D1 end

    def Function_3_41D(): pass

    label("Function_3_41D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 6)), scpexpr(EXPR_END)), "loc_45A")
    TalkBegin(0xFF)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拉杆已经被扳下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_56A")

    label("loc_45A")

    EventBegin(0x1)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个拉杆。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_563")
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

    label("loc_563")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_56A")

    Return()

    # Function_3_41D end

    def Function_4_56B(): pass

    label("Function_4_56B")

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

    def lambda_76B():
        OP_96(0xFE, 0xFFFFD508, 0xFFFFF060, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76B)
    Sleep(50)

    def lambda_788():
        OP_96(0xFE, 0xFFFFD120, 0xFFFFF060, 0xFFFFFA24, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_788)
    Sleep(50)

    def lambda_7A5():
        OP_96(0xFE, 0xFFFFCB44, 0xFFFFF060, 0xFFFFFDA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7A5)
    Sleep(50)

    def lambda_7C2():
        OP_96(0xFE, 0xFFFFCF2C, 0xFFFFF060, 0x384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C2)
    Sleep(50)

    def lambda_7DF():
        OP_96(0xFE, 0xFFFFD314, 0xFFFFF060, 0xA8C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_7DF)
    Sleep(50)

    def lambda_7FC():
        OP_96(0xFE, 0xFFFFCC0C, 0xFFFFF060, 0x7D0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_7FC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)

    def lambda_82A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_82A)
    WaitChrThread(0x108, 1)

    def lambda_83B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_83B)
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
        "#6P#0007F加尔西亚·罗西……！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        "#6P#0301F哼……原来在这里啊。\x02",
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
            "#12P#0101F果然……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#12P#0208F#N看上去似乎与其他黑手党相同，\x01",
            "被人操纵了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0010
    ChrTalk(
        0x107,
        (
            "#6P#0801F……他的体格简直能与金大哥媲美呢。\x02\x03",

            "看来会相当难对付……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x108,
        (
            "#6P#0903F#N原『西风旅团』部队长，\x01",
            "现『鲁巴彻商会』的副头目……\x02\x03",

            "#0901F其战斗力可想而知吧。\x02",
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
            "#0013F#6P#N目前似乎并没有\x01",
            "魔人化的征兆……\x02\x03",

            "但仍是个不可掉以轻心的对手。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BF1")

    #C0014
    ChrTalk(
        0x104,
        (
            "#0311F#6P#N喂──杀戮之熊。\x02\x03",

            "#0303F虽然你也许听不见，\x01",
            "但我会如你所愿，\x01",
            "拿出全力战斗的……\x02\x03",

            "#0312F好好见识一下\x01",
            "恶名昭著的『斗神之子』的力量吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1D")

    label("loc_BF1")


    #C0015
    ChrTalk(
        0x104,
        (
            "#0307F#6P#N是啊……\x01",
            "千万不要掉以轻心！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C1D")

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

    def lambda_C7E():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C7E)
    WaitChrThread(0x8, 1)
    Sleep(500)
    Sound(1839, 255, 100, 1)    #voice#Garcia
    Sound(250, 0, 100, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-9000, -3100, 0, 400)
    SetCameraDistance(17000, 400)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)
    SetChrFlags(0x8, 0x20)

    def lambda_CE3():
        OP_96(0xFE, 0xFFFFD6FC, 0xFFFFF060, 0x0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CE3)
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

    # Function_4_56B end

    def Function_5_D44(): pass

    label("Function_5_D44")

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

    def lambda_EC0():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EC0)
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
            "#11P#60W#17A……噫噫……唔唔………\x02",
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
            "#5S#25A#11P啊啊啊啊啊啊啊啊！！\x02",
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
            "#0107F#6P#N这、这是……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0020
    ChrTalk(
        0x108,
        (
            "#0907F#6P#N莫非……\x01",
            "要魔人化了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0021
    ChrTalk(
        0x107,
        (
            "#0813F#6P#N要、要是连他这种人都魔人化，\x01",
            "我们就根本无法应付了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0022
    ChrTalk(
        0x104,
        "#0310F#6P#N嘁……\x02",
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

    def lambda_11BE():
        OP_96(0xFE, 0xFFFFD634, 0xFFFFF060, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11BE)
    WaitChrThread(0x104, 1)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    OP_6F(0x10)

    #C0023
    ChrTalk(
        0x104,
        (
            "#5P#0301F──喂，大叔！\x02\x03",

            "你这个身经百战的原猎兵\x01",
            "怎么会这么窝囊！\x02\x03",

            "#0303F而且，虽说你现在是个黑手党，\x01",
            "但毕竟也是从『那个地方』\x01",
            "出来的人吧……！？\x02\x03",

            "#0307F拿出那个时候的韧性给我们看看啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#5P#0005F兰迪……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#5P#0208F……兰迪前辈……\x02",
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

    def lambda_133F():
        OP_A6(0xFE, 0x0, 0x1E, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_133F)

    #C0026
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#4S#40W喝啊啊啊啊啊啊……！\x02\x03",

            "#50W……噢噢噢噢噢噢噢……！\x02",
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
            "#11P#60W……啊啊啊啊啊……噢噢噢……\x02",
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
            "#11P#3111F#60W咳咳……唔唔……\x02",
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
        "#3P#0202F#N……瘴气消失了……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0030
    ChrTalk(
        0x102,
        "#6P#0102F莫非是……复原了！？\x02",
    )

    CloseMessageWindow()

    def lambda_151F():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_151F)
    WaitChrThread(0x8, 1)

    #C0031
    ChrTalk(
        0x8,
        (
            "#11P#3111F#50W哈……咳咳……\x02\x03",

            "#3110F#50W……呼……呼……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#6P#0304F哈……\x01",
            "想做还是能做到的嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P#3103F#40W……哼……\x01",
            "竟敢对我如此嚣张……\x02\x03",

            "#3100F不过……好像……\x01",
            "有必要跟你道声谢啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#6P#0013F你果然是被约亚西姆\x01",
            "强迫服下了『真知』……？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#11P#3103F#40W是啊……\x01",
            "居然给我直接注射……\x02\x03",

            "#3101F……那个混蛋……我从一开始\x01",
            "就觉得他可疑了……\x02\x03",

            "#3107F可恶……居然把我的部下们……！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#0003F……我们会负责将他逮捕的。\x02\x03",

            "#0001F很抱歉，你们大概也要\x01",
            "做好遭受逮捕的准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#11P#3104F#40W……哼……\x01",
            "出丑出到这个地步，\x01",
            "会有这种下场也是无可奈何的吧……\x02\x03",

            "……那个家伙应该\x01",
            "就在这前面……\x02\x03",

            "#3102F『斗神之子』……\x01",
            "还有，你是叫罗伊德吧……\x02\x03",

            "虽然我看你们很不顺眼……\x01",
            "但那个混蛋更加让人不爽……\x02\x03",

            "#3107F绝对……\x01",
            "不要输给他啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_1827():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1827)
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

    def lambda_188E():
        OP_96(0xFE, 0xFFFFE69C, 0xFFFFF060, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_188E)
    Sleep(600)

    def lambda_18AB():
        OP_98(0xFE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_18AB)
    Sleep(100)

    def lambda_18C8():
        OP_98(0xFE, 0x6A4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_18C8)

    def lambda_18E2():
        OP_98(0xFE, 0x7D0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18E2)
    Sleep(50)

    def lambda_18FF():
        OP_98(0xFE, 0x898, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18FF)

    def lambda_1919():
        OP_98(0xFE, 0x76C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1919)
    WaitChrThread(0x101, 1)

    def lambda_1937():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1937)

    def lambda_1944():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1944)

    def lambda_1951():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1951)
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
        "#5P#0306F……昏过去了吗？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#5P#0008F是啊……\x01",
            "完全失去意识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x108,
        (
            "#6P#0900F大概是在抵抗魔人化的时候\x01",
            "用尽了全力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x107,
        (
            "#5P#0803F嗯，虽然他也许是个恶人，\x01",
            "但可能也是个意志坚定的人吧……\x02\x03",

            "#0800F至少，比起那个会长，\x01",
            "跟他还比较能感到共鸣。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#6P#0100F是啊……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#6P#0204F……我也是同感。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#5P#0304F哼……\x01",
            "应该说他名不虚传吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#5P#0000F是啊……\x02",
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
            "#0003F#5P──真正的幕后黑手\x01",
            "似乎就在前方了。\x02\x03",

            "#0008F阿奈斯特与加尔西亚……\x01",
            "从这两人的状况来判断，\x01",
            "等待着我们的，恐怕是个相当危险的对手。\x02\x03",

            "#0001F各位……准备好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        "#12P#0101F嗯……！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#12P#0201F……是的！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        "#6P#0307F随时候命！\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x107,
        "#3P#0807F我们也没问题！\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x108,
        "#6P#0901F已经做好准备了！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0004F──好。\x02\x03",

            "#0013F接下来，将要对教团的\x01",
            "干部祭司——约亚西姆·琼塔\x01",
            "正式展开逮捕行动……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0053
    ChrTalk(
        0x101,
        "#0007F#5P各位，请全力以赴！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("各队员")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(1153, 255, 100, 0)    #voice#Elie
    #Sound(1249, 255, 100, 1)    #voice#Tio
    #Sound(1343, 255, 100, 2)    #voice#Randy
    #Sound(1689, 255, 100, 3)    #voice#Estelle
    #Sound(1759, 255, 100, 4)    #voice#Joshua

    #A0054
    AnonymousTalk(
        0xFF,
        "#5S是！\x02",
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

    # Function_5_D44 end

    def Function_6_1E8F(): pass

    label("Function_6_1E8F")

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

    # Function_6_1E8F end

    def Function_7_1ED2(): pass

    label("Function_7_1ED2")

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

    # Function_7_1ED2 end

    SaveToFile()

Try(main)
