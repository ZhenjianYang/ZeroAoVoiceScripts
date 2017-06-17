from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3099.bin",                # FileName
        "m3099",                    # MapName
        "m3099",                    # Location
        0x00A3,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -100000, 0, -7000, 0, 0, 1, 163, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3099",                  # 0
        "约亚西姆祭司",           # 1
        "支配者·炎天使",         # 2
        "支配者·炎天使",         # 3
        "魔人约亚西姆",           # 4
        "玲",                     # 5
        "假约亚西姆",             # 6
        "帕蒂尔·玛蒂尔",         # 7
        "魔导杖",                 # 8
        "SE控制",                 # 9
        "bm3050",                 # 10
        "bm3060",                 # 11
        "bm3070",                 # 12
    ))

    ATBonus("ATBonus_298", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_2A8", 100, 5, 0, 5, 0, 5, 0, 0, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_268", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_358", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 13, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 3, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 13, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 0, 0, 180)

    # monster count: 0

    # event battle count: 3

    BattleInfo(
        "BattleInfo_3B8", 0x0042, 44, 6, 0, 0, 0, 0, 0, "bm3050", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02000.dat", "ms72600.dat", "ms72600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_358", "MonsterBattlePostion_358", "ed7404", "ed7403", "ATBonus_298"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x00DA, 45, 6, 0, 0, 0, 0, 0, "bm3060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89900.dat", "ms69600.dat", "ms61600.dat", 0, 0, 0, 0, "ms70100.dat", "MonsterBattlePostion_378", "MonsterBattlePostion_378", "ed7406", "ed7403", "ATBonus_2A8"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_440", 0x00CA, 45, 6, 0, 0, 0, 0, 0, "bm3070", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_398", "MonsterBattlePostion_398", "ed7406", "ed7403", "ATBonus_268"),
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    484,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 3,   -45.5,                 -8.0,                  -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.166666984558105,    0.800000011920929,     0.20000000298023224,   1.0])

    ScpFunction((
        "Function_0_524",          # 00, 0
        "Function_1_540",          # 01, 1
        "Function_2_578",          # 02, 2
        "Function_3_5AD",          # 03, 3
        "Function_4_5C6",          # 04, 4
        "Function_5_5DC",          # 05, 5
        "Function_6_5EF",          # 06, 6
        "Function_7_5FF",          # 07, 7
        "Function_8_4067",         # 08, 8
        "Function_9_4082",         # 09, 9
        "Function_10_78BD",        # 0A, 10
        "Function_11_7A46",        # 0B, 11
        "Function_12_7A75",        # 0C, 12
        "Function_13_7AB4",        # 0D, 13
        "Function_14_7B19",        # 0E, 14
        "Function_15_7B5C",        # 0F, 15
        "Function_16_7B76",        # 10, 16
        "Function_17_94A5",        # 11, 17
        "Function_18_94E3",        # 12, 18
        "Function_19_9535",        # 13, 19
        "Function_20_9578",        # 14, 20
        "Function_21_95BB",        # 15, 21
        "Function_22_95FE",        # 16, 22
        "Function_23_9641",        # 17, 23
        "Function_24_9684",        # 18, 24
        "Function_25_96E5",        # 19, 25
        "Function_26_9741",        # 1A, 26
        "Function_27_979D",        # 1B, 27
        "Function_28_97F9",        # 1C, 28
        "Function_29_9855",        # 1D, 29
        "Function_30_98B1",        # 1E, 30
        "Function_31_98D6",        # 1F, 31
        "Function_32_98FB",        # 20, 32
        "Function_33_BB92",        # 21, 33
        "Function_34_BBB7",        # 22, 34
        "Function_35_BC02",        # 23, 35
        "Function_36_BC2A",        # 24, 36
        "Function_37_BCD3",        # 25, 37
        "Function_38_BD0D",        # 26, 38
        "Function_39_BD41",        # 27, 39
    ))


    def Function_0_524(): pass

    label("Function_0_524")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_53F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_524")

    label("loc_53F")

    Return()

    # Function_0_524 end

    def Function_1_540(): pass

    label("Function_1_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_554")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)
    Jump("loc_577")

    label("loc_554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_568")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_577")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_577")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 6)

    label("loc_577")

    Return()

    # Function_1_540 end

    def Function_2_578(): pass

    label("Function_2_578")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFrame(0xFF, "broken0", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_5AC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5AC")

    Return()

    # Function_2_578 end

    def Function_3_5AD(): pass

    label("Function_3_5AD")

    Call(0, 7)
    Call(0, 9)
    Call(0, 16)
    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5AD end

    def Function_4_5C6(): pass

    label("Function_4_5C6")

    Call(0, 9)
    Call(0, 16)
    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_5C6 end

    def Function_5_5DC(): pass

    label("Function_5_5DC")

    Call(0, 16)
    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5DC end

    def Function_6_5EF(): pass

    label("Function_6_5EF")

    Call(0, 32)
    SetScenarioFlags(0x5C, 0)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_5EF end

    def Function_7_5FF(): pass

    label("Function_7_5FF")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("chr/ch09600.itc", 0x2A)
    LoadChrToIndex("chr/ch02000.itc", 0x2B)
    LoadChrToIndex("monster/ch72650.itc", 0x2C)
    LoadChrToIndex("monster/ch72650.itc", 0x2D)
    LoadChrToIndex("chr/ch02050.itc", 0x2E)
    LoadChrToIndex("chr/ch02054.itc", 0x2F)
    LoadChrToIndex("chr/ch02056.itc", 0x30)
    LoadChrToIndex("apl/ch50014.itc", 0x31)
    LoadChrToIndex("apl/ch50525.itc", 0x32)
    LoadChrToIndex("apl/ch50526.itc", 0x33)
    SoundLoad(861)
    OP_68(-41300, 3500, -8000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x101, -41300, 0, -8000, 90)
    SetChrPos(0x102, -42400, 0, -7700, 90)
    SetChrPos(0x103, -42800, 0, -9100, 90)
    SetChrPos(0x104, -43900, 0, -8600, 90)
    SetChrPos(0x107, -43500, 0, -7000, 90)
    SetChrPos(0x108, -44700, 0, -7700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 28500, -66000, 2000, 180)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2C)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -3800, -1000, -10800, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -3800, -1000, -5200, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xF6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06700.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis104.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06800.itp")
    LoadEffect(0x0, "event\\ev618_00.eff")
    LoadEffect(0x1, "battle\\mgaria0.eff")
    LoadEffect(0x2, "event\\ev618_01.eff")
    LoadEffect(0x3, "event\\ev618_02.eff")
    LoadEffect(0x4, "event\\ev618_01.eff")

    def lambda_92D():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_92D)
    Sleep(50)

    def lambda_94A():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94A)
    Sleep(50)

    def lambda_967():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_967)
    Sleep(50)

    def lambda_984():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_984)
    Sleep(50)

    def lambda_9A1():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9A1)
    Sleep(50)

    def lambda_9BE():
        OP_97(0xFE, 0x4E20, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9BE)
    FadeToBright(1000, 0)
    OP_68(-15000, 500, -8000, 7000)
    MoveCamera(60, 34, 0, 7000)
    OP_6E(700, 7000)
    SetCameraDistance(55000, 7000)
    OP_6F(0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(-21300, 900, -8000, 0)
    MoveCamera(34, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    Sleep(1)
    SetCameraDistance(20500, 2000)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(500)
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(750)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(500)
    OP_6F(0x10)

    #C0001
    ChrTalk(
        0x101,
        "#6P#0013F这里是……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x2D, 0x1F4)

    #C0002
    ChrTalk(
        0x102,
        "#0108F#6P……地下湖……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)

    #C0003
    ChrTalk(
        0x104,
        (
            "#6P#0301F这下面竟然有\x01",
            "这么大一片湖啊……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0004
    ChrTalk(
        0x103,
        "#6P#0207F各位，那是……！\x02",
    )

    CloseMessageWindow()

    def lambda_B24():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B24)

    def lambda_B31():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B31)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_68(28000, 14000, -8000, 4000)
    MoveCamera(34, 30, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(26500, 4000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(27500, 14000, -8000, 0)
    MoveCamera(115, -10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    MoveCamera(65, -10, 0, 7000)
    SetCameraDistance(23000, 7000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xAAFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)

    #C0005
    ChrTalk(
        0x104,
        (
            "#0307F#2P出现在阿琪那张\x01",
            "照片里的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0101F#2P原来就是在\x01",
            "这个地方拍的啊……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "……该怎么说呢，\x01",
            "脑子里好像浮现出\x01",
            "一个又黑暗又广阔的地方。\x02\x03",

            "上方模模糊糊的，有光照下来，\x01",
            "很漂亮，但是又有点可怕。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    FadeToBright(300, 0)
    OP_0D()

    #C0008
    ChrTalk(
        0x101,
        (
            "#0003F#2P是吗……\x01",
            "她说的就是这里啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x8, 19200, 7000, -10000, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Sleep(300)
    #Sound(1956, 255, 100, 0)    #voice#Joachim
    Sleep(800)

    #N0009
    NpcTalk(
        0x8,
        "男人的声音",
        "#2P呵呵……正是如此。\x02",
    )

    CloseMessageWindow()
    OP_68(19200, 8000, -10000, 2000)
    MoveCamera(90, 10, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(15500, 2000)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)
    SetChrPos(0xD, 17800, 4000, -8000, 90)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Sleep(500)

    #C0010
    ChrTalk(
        0x101,
        "#0013F#11P约亚西姆·琼塔……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x107,
        "#0801F#5P什、什么时候出现的……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x108,
        (
            "#0901F#5P……看来果然\x01",
            "不是泛泛之辈啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    OP_68(17800, 7500, -8000, 1500)
    MoveCamera(56, 10, 0, 1500)

    def lambda_E55():
        OP_95(0xFE, 17800, 7000, -8000, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E55)
    WaitChrThread(0x8, 1)
    OP_6F(0x41)
    OP_6B(0xD)

    def lambda_E78():
        OP_95(0xFE, -2700, -5000, -8000, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E78)

    def lambda_E92():
        OP_95(0xFE, -2700, 0, -8000, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E92)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    #Sleep(500)

    #A0013
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#40A#30W──欢迎。\x01",
            "欢迎来到吾等起源之圣地。\x02\x03",

            "#50A特别任务支援科的诸位，\x01",
            "以及游击士协会的客人……\x02\x03",

            "#13A欢迎你们的到来。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetChrPos(0x101, -19300, 0, -8000, 90)
    SetChrPos(0x102, -20400, 0, -7700, 90)
    SetChrPos(0x103, -20800, 0, -9100, 90)
    SetChrPos(0x104, -21900, 0, -8600, 90)
    SetChrPos(0x107, -20500, 0, -6000, 90)
    SetChrPos(0x108, -21700, 0, -6700, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Fade(1000)
    OP_6B(0xFF)
    OP_68(-6150, 1000, -7560, 0)
    MoveCamera(57, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    EndChrThread(0x8, 0x1)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 0, 0, -8000, 270)

    def lambda_10B4():
        OP_95(0xFE, -3000, 0, -8000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10B4)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_10D8():
        OP_95(0xFE, -9500, 0, -8000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10D8)
    Sleep(5)

    def lambda_10F5():
        OP_96(0xFE, 0xFFFFD7C4, 0x0, 0xFFFFE570, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F5)
    Sleep(5)

    def lambda_1112():
        OP_96(0xFE, 0xFFFFD508, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1112)

    def lambda_112C():
        OP_95(0xFE, -8500, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_112C)
    Sleep(5)

    def lambda_1149():
        OP_96(0xFE, 0xFFFFD24C, 0x0, 0xFFFFDE04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1149)

    def lambda_1163():
        OP_95(0xFE, -10200, 0, -4700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1163)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x104, 1)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x107, 1)

    def lambda_119E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_119E)
    WaitChrThread(0x108, 1)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 70, 0)

    def lambda_11BB():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_11BB)
    WaitChrThread(0x8, 1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x103,
        "#6P#0208F#N……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0015
    ChrTalk(
        0x102,
        "#0101F#6P……你……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#6P#0301F真是从容不迫啊……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#0013F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(-5700, 1000, -7320, 1000)

    def lambda_1270():
        OP_95(0xFE, -9200, 0, -8000, 800, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1270)
    WaitChrThread(0x101, 1)
    Sound(31, 0, 100, 0)
    OP_6F(0x1)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F#6P──约亚西姆·琼塔，\x01",
            "我就开门见山地说吧。\x02\x03",

            "#0001F立即放了那些服用过『真知』，\x01",
            "被你操纵的人们。\x02\x03",

            "虽然不清楚具体方法……\x01",
            "但我知道操纵者就是你。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#6705F#11P哦，可以啊。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0011F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#6704F#11P在ＩＢＣ大楼时也说过吧。\x02\x03",

            "#6714F──只要将琪雅大人交出来，\x01",
            "我立刻收手。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0022
    ChrTalk(
        0x101,
        "#0007F#6P开、开什么玩笑……！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        "#0110F#6P又在胡言乱语……！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0307F#6P你这混蛋……想找打吗？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#6P#0211F#N……真是恶劣至极的犯罪者。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0026
    ChrTalk(
        0x107,
        (
            "#0808F（这家伙是什么人啊……\x01",
            "  性格好像和教授一样差劲呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x108,
        (
            "#0906F（但连怀斯曼也没有\x01",
            "  疯狂到如此地步……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0028
    ChrTalk(
        0x8,
        (
            "#6703F#11P哎呀呀……\x01",
            "这样可没法交流啊。\x02\x03",

            "琪雅大人原本就是\x01",
            "本教团所侍奉的圣子——\x02\x03",

            "#6701F把她交还给我，\x01",
            "不是很合情合理吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0010F#6P想想你们在六年前\x01",
            "做的那些事吧！\x02\x03",

            "我们怎么能把琪雅\x01",
            "交给你这种人！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#0107F#6P别说废话了……\x01",
            "快把小琪雅的\x01",
            "身世说出来！\x02\x03",

            "你应该很清楚\x01",
            "她的来历吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#6702F#11P呵呵……原来如此。\x02\x03",

            "#6704F──莫非你们\x01",
            "还以为琪雅大人是\x01",
            "出生在这个时代的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0032
    ChrTalk(
        0x101,
        "#0005F#6P！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#6P#0201F#N这、这个时代……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0034
    ChrTalk(
        0x8,
        (
            "#6704F#11P呵呵，好吧。\x02\x03",

            "#6700F这些原本是严禁向\x01",
            "未及『睿智』领域之人透露的……\x02\x03",

            "但这次就特别告诉你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(22000, 12000, -8000, 3000)
    MoveCamera(90, -10, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(23000, 3000)
    OP_93(0x8, 0x5A, 0x190)
    OP_6F(0x79)
    Sleep(300)

    #C0035
    ChrTalk(
        0x8,
        (
            "#6704F#11P直至一个月之前，\x01",
            "琪雅大人都还一直在沉睡着——\x02\x03",

            "就在这祭坛的神圣摇篮中，\x01",
            "仿如浅眠一般……\x02\x03",

            "#6714F沉浸在五百年以上的\x01",
            "漫长睡眠之中！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0036
    ChrTalk(
        0x101,
        "#0007F！！！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#0107F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#0207F……不、不可能……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0310F你这混蛋……\x01",
            "少在这里胡说八道啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-2900, 1000, -8000, 0)
    MoveCamera(33, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    Sleep(1)
    MoveCamera(65, 17, 0, 50000)
    SetCameraDistance(19500, 50000)
    OP_0D()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    #C0040
    ChrTalk(
        0x8,
        (
            "#6702F#11P呵呵，你们也不用\x01",
            "这么惊讶吧？\x02\x03",

            "#6704F即使凭现代的技术不可能实现，\x01",
            "但以古代的技术来说，却是可能的——\x02\x03",

            "……五百年前，\x01",
            "此地曾经存在着研究\x01",
            "古代遗物的炼金术师集团。\x02\x03",

            "#6700F传说，这个祭坛就是以\x01",
            "他们的技术为基础而建造的。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 200, -1, -1)

    #A0041
    AnonymousTalk(
        0x108,
        (
            "#0901F建造了『星见之塔』的\x01",
            "中世纪炼金术师们……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0042
    AnonymousTalk(
        0x107,
        (
            "#0806F竟、竟然会有\x01",
            "这样的联系……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0043
    ChrTalk(
        0x8,
        (
            "#6704F#11P此后，琪雅大人\x01",
            "就陷入了长达五百年的漫长睡眠……\x02\x03",

            "当然，即使在本教团之中，\x01",
            "也没有知晓其身世的人。\x02\x03",

            "#6700F……事情就是如此。\x02",
        )
    )

    CloseMessageWindow()

    #A0044
    AnonymousTalk(
        0x101,
        "#0008F……怎么会……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0045
    AnonymousTalk(
        0x104,
        "#0306F搞什么啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0046
    AnonymousTalk(
        0x102,
        (
            "#0108F……小琪雅的过去……\x01",
            "本以为能帮她找回来……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0047
    AnonymousTalk(
        0x103,
        "#0208F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0048
    ChrTalk(
        0x8,
        (
            "#6704F#11P呵呵……\x01",
            "有什么好悲伤的？\x02\x03",

            "琪雅大人不需要什么过去……\x02\x03",

            "#6713F因为她即将\x01",
            "成为真正的『神』──！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #A0049
    AnonymousTalk(
        0x101,
        "#0007F什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0050
    AnonymousTalk(
        0x107,
        "#0801F神、神是指……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0051
    ChrTalk(
        0x8,
        (
            "#6714F#11P哈哈哈，当然就是字面上的意思啊！\x02\x03",

            "你们差不多也该\x01",
            "察觉到真相了吧！\x02\x03",

            "『空之女神』爱德丝！？\x01",
            "那种东西根本就不存在啊！\x02\x03",

            "一切都是七耀教会所编造的\x01",
            "谎言，为何还不明白！？\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0x104,
        "#0310F你、你疯了吗……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0053
    AnonymousTalk(
        0x102,
        (
            "#0101F竟、竟然会有人\x01",
            "怀疑女神的存在……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0054
    ChrTalk(
        0x8,
        (
            "#6702F#11P呵呵，难以置信吗……然而，\x01",
            "那正是我们『Ｄ∴Ｇ教团』的真理。\x02\x03",

            "#6704F虽然常遭误解……\x01",
            "但吾等并非\x01",
            "崇拜恶魔的教团。\x02\x03",

            "只是因为恶魔这一概念\x01",
            "刚好适合用来否定女神，\x01",
            "所以便稍加利用罢了。\x02\x03",

            "#6700F以毒攻毒……\x01",
            "就是这么一回事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-10000, 1000, -9700, 0)
    MoveCamera(295, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrPos(0x104, -11700, 0, -8300, 90)
    SetChrPos(0x103, -10000, 0, -9700, 90)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_49()
    SetCameraDistance(14500, 500)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0055
    ChrTalk(
        0x103,
        "#5P#0207F#4S开、开什么玩笑……！\x02",
    )

    CloseMessageWindow()
    OP_6F(0x10)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_20C3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20C3)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_20D8():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20D8)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_20ED():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20ED)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)

    def lambda_2102():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2102)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)

    def lambda_2117():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2117)
    Sound(808, 0, 80, 0)
    Sound(531, 0, 80, 0)
    Sleep(500)

    #C0056
    ChrTalk(
        0x103,
        (
            "#5P#0208F#30W既然如此……又为何要做\x01",
            "那么残酷的事情……！\x02\x03",

            "#0210F#40W……大家……\x01",
            "大家都痛苦地哭喊着……！\x02\x03",

            "而且，听说还有比我\x01",
            "所在的据点更加残忍的……！\x02\x03",

            "既然不是崇拜恶魔……\x01",
            "……为什么还要做那种……！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#11P#0008F缇欧……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#11P#0308F……阿缇……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5700, 1000, -7320, 0)
    MoveCamera(57, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x104, -11700, 0, -8700, 90)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    #C0059
    ChrTalk(
        0x8,
        (
            "#6702F#11P呵呵……缇欧·普拉托，\x01",
            "我记得你的名字哦。\x02\x03",

            "#6704F在阿尔泰尔的据点\x01",
            "展现了出色感应能力的实验体……\x02\x03",

            "哎呀呀，没想到会以这种形式\x01",
            "和实验体本人见面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#6P#0208F#N………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_238A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_238A)
    Sleep(50)

    def lambda_239A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_239A)
    Sleep(50)

    def lambda_23AA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23AA)
    Sleep(50)

    def lambda_23BA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_23BA)
    Sleep(50)

    def lambda_23CA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_23CA)

    #C0061
    ChrTalk(
        0x101,
        (
            "#0006F#6P……正好，\x01",
            "再来说说这个话题吧……\x02\x03",

            "#0013F你们在大陆各地的据点进行\x01",
            "种种残忍的仪式，目的究竟是什么……！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#6705F#11P哎呀，难道你还不明白吗？\x02\x03",

            "#6704F一切实验都是为了提高\x01",
            "『真知』的完成度啊。\x02\x03",

            "人类在极限状态时所展现的\x01",
            "强烈意念与潜在能力的爆发……\x02\x03",

            "#6700F那些实验数据对于提高『真知』的\x01",
            "完成度，真是再适合不过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0010F#6P……！\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#6714F#11P顺带一提，实验体之所以会以儿童居多，\x01",
            "只是单纯考虑到了数据样本的精度问题。\x02\x03",

            "未进入青春期的实验体年幼纯洁，\x01",
            "所以在各方面都比较——\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0065
    ChrTalk(
        0x103,
        "#6P#0210F#N…………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0066
    ChrTalk(
        0x101,
        "#0007F#6P别再说了……！\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0110F#6P给我适可而止吧！\x01",
            "你这毫无人性的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#3P#0311F#6P……没想到，还有比『我们』\x01",
            "更加邪恶的家伙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x108, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x107)
    OP_64(0x108)
    Fade(500)
    OP_68(-8090, 900, -6540, 0)
    MoveCamera(270, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x107, -8000, 0, -4100, 135)
    SetChrPos(0x108, -9900, 0, -4500, 135)
    MoveCamera(280, 17, 0, 50000)
    SetCameraDistance(18000, 50000)

    def lambda_2715():
        OP_96(0xFE, 0xFFFFDD3C, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2715)
    WaitChrThread(0x108, 1)
    Sleep(300)

    #C0069
    ChrTalk(
        0x108,
        (
            "#0903F#11P──约亚西姆·琼塔。\x02\x03",

            "#0901F如果我所料不差，\x01",
            "你应该就是统管各项实验的\x01",
            "负责人吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x13B, 0x1F4)

    #C0070
    ChrTalk(
        0x8,
        (
            "#6P#6702F#N呵呵，没错。\x02\x03",

            "#6704F话虽如此，但这并不意味着\x01",
            "我在教团中的地位有多高。\x02\x03",

            "毕竟本教团的理念是：\x01",
            "在真神面前，人人平等——\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0071
    ChrTalk(
        0x107,
        (
            "#0806F#11P老实说，我对你们的教义\x01",
            "一点兴趣也没有。\x02\x03",

            "#0808F──先不提那些，\x01",
            "既然你身为负责人，应该是知道的吧？\x02\x03",

            "#0801F关于那个被称作『乐园』的\x01",
            "特殊据点……\x02",
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
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2962():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2962)
    Sleep(50)

    def lambda_2972():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2972)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_298A():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_298A)
    Sleep(50)

    def lambda_299A():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_299A)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#0005F#5P那个名字是……！？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#5P#0101F那份黑皮文件里的……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#6P#6705F#N啊……\x01",
            "原来你们两位也知道它的存在吗？\x02\x03",

            "#6704F那是加入教团的权势者\x01",
            "特意建立的据点。\x02\x03",

            "用来拉拢各地的有权人士，\x01",
            "从而掌握其弱点，使之为教团所用。\x02\x03",

            "#6700F说实话，那个据点已经偏离了\x01",
            "我所构想的实验主旨。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0075
    ChrTalk(
        0x107,
        "#0808F#11P……果然……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x108,
        "#0908F#11P……和我们推测的一样吗……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0077
    ChrTalk(
        0x101,
        (
            "#0003F#5P原来如此……是这样吗……\x02\x03",

            "#0013F你们把议长引诱进『乐园』，\x01",
            "然后握住了他的把柄吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2BC7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BC7)

    def lambda_2BD4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BD4)

    def lambda_2BE1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BE1)
    WaitChrThread(0x102, 1)

    #C0078
    ChrTalk(
        0x102,
        "#11P#0107F啊……！\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        "#5P#0307F原来你们之前还有这种牵连啊……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    #C0080
    ChrTalk(
        0x8,
        (
            "#6P#6702F#N呵呵，因为我可是看过\x01",
            "所有据点的实验结果的。\x02\x03",

            "#6704F在六年前的那次可恨的作战行动中，\x01",
            "我们几乎丧失了所有据点……\x02\x03",

            "在那之后，我便得到了这个\x01",
            "正好适合利用的后盾。\x02\x03",

            "#6712F而且还附带一个叫做『鲁巴彻』的\x01",
            "便利爪牙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0006F#5P果然是这样吗……\x02\x03",

            "#0013F你能操纵警备队，\x01",
            "也是靠了这层关系吧……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D75():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D75)

    def lambda_2D82():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D82)

    def lambda_2D8F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D8F)
    WaitChrThread(0x102, 1)

    #C0082
    ChrTalk(
        0x102,
        "#11P#0108F如、如此说来……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0301F你是怎样让他们\x01",
            "服下『真知』的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#6P#6702F#N哦，是让议长手下的\x01",
            "警备队司令强行下发给队员们的。\x02\x03",

            "名义上说的是乌尔斯拉医院\x01",
            "开发的划时代营养剂。\x02\x03",

            "#6709F哼哼，但真没想到他\x01",
            "这么容易就相信了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0085
    ChrTalk(
        0x101,
        "#0008F#5P呜……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#5P#0310F那个蠢货司令……\x01",
            "糊涂也要有个限度吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x8,
        (
            "#6P#6704F#N──还是回到『乐园』这个话题吧，\x01",
            "那个据点的灭亡形式倒是有点奇怪呢。\x02\x03",

            "它的灭亡似乎并不是因为那次作战，\x01",
            "好像是被去年在利贝尔引发异变的\x01",
            "那个什么『结社』摧毁的……\x02\x03",

            "#6700F哎呀呀，他们到底有什么目的啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0088
    ChrTalk(
        0x107,
        "#0808F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x108,
        "#0903F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "#6P#6703F#N啊，对了，关于『乐园』，\x01",
            "我还有一个极大的遗憾呢。\x02\x03",

            "那里有一个拥有天才适应能力的\x01",
            "年幼实验体……\x02\x03",

            "#6713F那也是个难得的杰作啊！\x02\x03",

            "竟然能通过服用『真知』，\x01",
            "将周围其他实验体的人格\x01",
            "吸收为己用呢！\x02\x03",

            "#6709F哎呀，哪怕只有实验数据也好，\x01",
            "要是能回收的话——\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0091
    ChrTalk(
        0x107,
        (
            "#0803F#11P──够了。\x02\x03",

            "#0801F我们想知道的已经都知道了，\x01",
            "没必要再说下去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x108,
        (
            "#0908F#11P……抱歉，罗伊德，\x01",
            "好像打断了你的问话。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0004F#5P没那回事，多亏你们，\x01",
            "我这边似乎也更有头绪了。\x02\x03",

            "#0000F──这样的话，就能\x01",
            "毫无顾忌地进行正式逮捕了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)
    Fade(500)
    OP_68(-7500, 1000, -8000, 0)
    MoveCamera(270, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -9700, 0, -8000, 90)

    def lambda_327B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_327B)
    SetCameraDistance(16000, 700)

    def lambda_3291():
        OP_95(0xFE, -9000, 0, -8000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3291)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x31)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sound(18, 0, 80, 0)
    OP_6F(0x10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)

    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F#5P──『Ｄ∴Ｇ教团』的干部祭司，\x01",
            "约亚西姆·琼塔。\x02\x03",

            "#0007F根据自治州法，以人身伤害、引发暴乱、\x01",
            "非法侵占、使用违禁药物、虐待等\x01",
            "众多嫌疑，在此将你逮捕……！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#2P#0107F#11P虽然形式较为简略，\x01",
            "但搜查令以及逮捕令都在这里！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#5P#0307F老老实实束手就擒吧！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "#6P#6704F──呵呵，好吧。\x02\x03",

            "#6700F我与你们，\x01",
            "究竟谁才能达成目的……\x02\x03",

            "不如就在此\x01",
            "赌一赌吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0xD, 0x32)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xD, -3000, 0, -8000, 270)
    Sound(804, 0, 100, 0)

    def lambda_3459():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3459)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3000, 2500, -8000, 0)
    SetChrFlags(0xF, 0x8000)

    def lambda_3497():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3497)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x32)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    Sound(1960, 255, 100, 0)    #voice#Joachim
    Fade(500)
    OP_68(-3000, 1500, -8000, 0)
    MoveCamera(225, 40, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(968, 0, 100, 0)

    def lambda_3585():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3585)

    def lambda_3596():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3596)
    MoveCamera(90, 33, 0, 9000)
    SetCameraDistance(15000, 9000)
    Sleep(3000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x3, 0xFF, 0xF, 0x40, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(969, 0, 100, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_3607():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3607)
    Sound(202, 0, 100, 0)
    OP_6F(0x79)

    def lambda_3620():
        OP_96(0xFE, 0xFFFFF448, 0x5DC, 0xFFFFE0C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3620)
    WaitChrThread(0xF, 1)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrPos(0x107, -8500, 0, -4100, 135)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x108, -10100, 0, -5100, 135)
    Sound(808, 0, 100, 0)
    OP_68(-3000, 300, -8000, 1500)
    MoveCamera(90, 14, 0, 1500)
    SetCameraDistance(22000, 1500)
    Sleep(1000)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_6F(0x1)
    OP_6F(0x40)
    OP_6F(0x10)

    def lambda_375E():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_375E)
    Sleep(10)

    def lambda_377B():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_377B)
    Sleep(10)

    def lambda_3798():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3798)

    def lambda_37B2():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_37B2)
    Sleep(10)

    def lambda_37CF():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37CF)

    def lambda_37E9():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_37E9)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x108, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_0D()
    Sleep(500)

    #C0098
    ChrTalk(
        0x102,
        "#0101F#6P那、那头发……！？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        "#0201F#12P还有，那是魔导杖的一种吗……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0100
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "呵呵，这才是我\x01",
            "原本的发色……\x02\x03",

            "因为持续服用『真知』，\x01",
            "体质也发生了变异。\x02\x03",

            "以至于，在这几年来，\x01",
            "我从来都没有睡过觉呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0101
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0310F#12P#N喂喂……\x01",
            "这可让人完全笑不出来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0102
    ChrTalk(
        0x101,
        (
            "#6P#0008F原来如此……\x01",
            "所以才有时间一边在医院工作，\x01",
            "一边做出这么多事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5P呵呵，不愧是搜查官，\x01",
            "立刻就察觉到了啊。\x02\x03",

            "#6800F──顺带一提，这根手杖\x01",
            "便是那些炼金术师制造的魔导具，\x01",
            "并且是其中的最高杰作之一。\x02\x03",

            "它甚至蕴藏着凌驾于\x01",
            "古代遗物之上的力量……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x2F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sound(808, 0, 100, 0)
    OP_0D()
    PlayEffect(0x1, 0x0, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    Sound(861, 2, 100, 0)
    BeginChrThread(0x8, 2, 0, 8)
    Sleep(500)
    Sound(1921, 255, 100, 0)    #voice#Joachim
    Sleep(500)
    Fade(250)
    OP_68(-3490, 900, -7360, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    MoveCamera(45, 30, 0, 3000)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x2, 0x1, 0xFF, 0x0, -3800, 0, -10800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, 0x0, -3800, 0, -5200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    OP_24(0x35D)

    def lambda_3C20():
        OP_96(0xFE, 0xFFFFF128, 0x0, 0xFFFFD5D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C20)

    def lambda_3C3A():
        OP_96(0xFE, 0xFFFFF128, 0x0, 0xFFFFEBB0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C3A)

    def lambda_3C54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3C54)

    def lambda_3C65():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_3C65)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
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
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    EndChrThread(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x2E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    #C0104
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6813F#11P现在的我，就连这种东西\x01",
            "也都能随意差遣……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 200, -1, -1)

    #A0105
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F呜……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0106
    AnonymousTalk(
        0x107,
        "#0807F这是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0107
    AnonymousTalk(
        0x108,
        (
            "#0901F用炼金术制造的\x01",
            "中世纪人偶兵器吗……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0x1194)
    Fade(300)
    OP_68(-3000, 300, -8000, 0)
    MoveCamera(90, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xA, 0xE1, 0x0)
    OP_93(0x9, 0x13B, 0x0)
    SetChrChipByIndex(0x8, 0x30)
    SetChrSubChip(0x8, 0x1)
    Sleep(600)
    Sound(1959, 255, 100, 0)    #voice#Joachim
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(20500, 300)
    SetChrSubChip(0x8, 0x2)
    Sleep(80)
    SetChrSubChip(0x8, 0x3)
    Sound(808, 0, 100, 0)
    Sound(540, 0, 70, 0)
    Sleep(500)
    OP_6F(0x10)
    CancelBlur(0)

    #C0108
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5P好了，差不多\x01",
            "也该收场了。\x02\x03",

            "今天大概将会成为\x01",
            "值得纪念的一天吧……\x02\x03",

            "#6814F也就是琪雅大人化身为『神』，\x01",
            "达成吾等夙愿之日！\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7404", 0)

    #C0109
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0007F痴人说梦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#0207F#12P我们绝对不会……\x01",
            "……输给你这种人……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 415)
    BlurSwitch(0x19F, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_3F85():
        OP_95(0xFE, -2000, 0, -8000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F85)
    Sleep(5)

    def lambda_3FA2():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFE4A8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FA2)
    Sleep(5)

    def lambda_3FBF():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FBF)

    def lambda_3FD9():
        OP_95(0xFE, -2000, 0, -7000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3FD9)
    Sleep(5)

    def lambda_3FF6():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FF6)

    def lambda_4010():
        OP_95(0xFE, -2000, 0, -7000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4010)
    Sleep(400)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x35D)
    Battle("BattleInfo_3B8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x107, 0x1)
    EndChrThread(0x108, 0x1)
    Return()

    # Function_7_5FF end

    def Function_8_4067(): pass

    label("Function_8_4067")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4081")
    OP_A1(0x8, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_8_4067")

    label("loc_4081")

    Return()

    # Function_8_4067 end

    def Function_9_4082(): pass

    label("Function_9_4082")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("chr/ch02053.itc", 0x2A)
    LoadChrToIndex("chr/ch02050.itc", 0x2B)
    LoadChrToIndex("chr/ch02054.itc", 0x2C)
    LoadChrToIndex("chr/ch02000.itc", 0x2D)
    LoadChrToIndex("chr/ch00053.itc", 0x2E)
    LoadChrToIndex("chr/ch00153.itc", 0x2F)
    LoadChrToIndex("chr/ch00253.itc", 0x30)
    LoadChrToIndex("chr/ch00353.itc", 0x31)
    LoadChrToIndex("chr/ch00653.itc", 0x32)
    LoadChrToIndex("chr/ch00753.itc", 0x33)
    LoadChrToIndex("chr/ch00056.itc", 0x34)
    LoadChrToIndex("chr/ch00156.itc", 0x35)
    LoadChrToIndex("chr/ch00256.itc", 0x36)
    LoadChrToIndex("chr/ch00356.itc", 0x37)
    LoadChrToIndex("chr/ch00059.itc", 0x3A)
    LoadChrToIndex("chr/ch00054.itc", 0x3B)
    LoadChrToIndex("monster/ch72050.itc", 0x3C)
    LoadChrToIndex("apl/ch50526.itc", 0x3D)
    LoadChrToIndex("apl/ch50527.itc", 0x3E)
    LoadChrToIndex("apl/ch50528.itc", 0x3F)
    SoundLoad(861)
    SoundLoad(971)
    SoundLoad(930)
    OP_68(-6100, 1000, -8000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x101, -9500, 0, -8000, 90)
    SetChrPos(0x102, -10300, 0, -6600, 90)
    SetChrPos(0x103, -10800, 0, -10400, 90)
    SetChrPos(0x104, -11500, 0, -8900, 90)
    SetChrPos(0x107, -8500, 0, -4400, 135)
    SetChrPos(0x108, -10200, 0, -4700, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrSubChip(0x8, 0x3)
    SetChrPos(0x8, -3000, 0, -8000, 270)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 0x3D)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3500, 500, -6700, 0)
    SetChrFlags(0xF, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0xB)
    OP_49()
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x2, 0xF)
    OP_70(0x2, 0xA)
    OP_CA(0x1, 0xFF, 0x0)
    OP_49()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis112.itp")
    LoadEffect(0x0, "event\\ev611_01.eff")
    LoadEffect(0x1, "event\\ev611_02.eff")
    LoadEffect(0x2, "event\\ev602_01.eff")
    LoadEffect(0x3, "event\\ev602_02.eff")
    LoadEffect(0x4, "event\\ev612_00.eff")
    LoadEffect(0x5, "event\\ev611_00.eff")
    LoadEffect(0x6, "event\\ev607_00.eff")
    LoadEffect(0x7, "battle\\mgaria0.eff")
    SetCameraDistance(18500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0111
    ChrTalk(
        0x101,
        "#0007F#6P……好……！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#3P#0300F哈……\x01",
            "看来这场赌局是我们赢了啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        "#0107F#6P老老实实地投降吧……！\x02",
    )

    CloseMessageWindow()

    def lambda_4456():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4456)
    WaitChrThread(0x8, 2)

    #C0114
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#11P#40W呵呵……哎呀呀。\x02\x03",

            "#6802F……让我告诉你们一件事吧……\x02\x03",

            "如你们所知，『真知』的效果\x01",
            "并非只是单纯强化身体能力……\x02\x03",

            "它还能强化感应能力，进而引发出\x01",
            "服用者的潜在能力……\x02\x03",

            "#6814F只要将这种使用方法发挥到极致，\x01",
            "即使是这种事也可以做到……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_456E():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_456E)
    SetChrSubChip(0x8, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(80)
    SetChrSubChip(0x8, 0x1)
    Sound(808, 0, 100, 0)
    Sleep(80)
    Fade(250)
    OP_68(-3200, 1000, -8000, 0)
    MoveCamera(91, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(20000, 2000)
    SetChrChipByIndex(0x8, 0x2C)
    SetChrSubChip(0x8, 0x0)
    BeginChrThread(0x8, 2, 0, 8)
    OP_0D()
    PlayEffect(0x6, 0xFF, 0x8, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x0, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(357, 0, 100, 0)
    Sound(861, 2, 100, 0)
    Sound(506, 0, 90, 0)
    Sound(565, 0, 90, 0)
    Sleep(2000)
    PlayEffect(0x5, 0x1, 0x8, 0x0, -2500, 3200, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(970, 0, 100, 0)
    Sleep(1200)
    Sound(972, 0, 100, 0)
    Sleep(700)
    PlayEffect(0x0, 0x2, 0x101, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x102, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0x103, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0x104, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x6, 0x107, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0x108, 0x40, 200, 0, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(969, 0, 100, 0)
    Sound(971, 2, 100, 0)
    Sound(1030, 255, 100, 0)    #voice#Lloyd
    Sound(1128, 255, 100, 1)    #voice#Elie
    Sound(1223, 255, 100, 2)    #voice#Tio
    Sound(1317, 255, 100, 3)    #voice#Randy
    Sound(1670, 255, 100, 4)    #voice#Estelle
    Sound(1739, 255, 100, 5)    #voice#Joshua
    OP_82(0xC8, 0xC8, 0x3E8, 0x3E8)
    Fade(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2E)
    BeginChrThread(0x101, 3, 0, 11)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    SetChrChipByIndex(0x102, 0x2F)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x30)
    BeginChrThread(0x103, 3, 0, 11)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    SetChrChipByIndex(0x104, 0x31)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrChipByIndex(0x107, 0x32)
    BeginChrThread(0x107, 3, 0, 11)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    SetChrChipByIndex(0x108, 0x33)
    BeginChrThread(0x108, 3, 0, 11)
    OP_0D()
    StopEffect(0x1, 0x2)
    Sleep(1500)

    def lambda_4915():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4915)

    #C0115
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F什么……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4948():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4948)

    #C0116
    ChrTalk(
        0x104,
        "#11P#0307F这是什么！？\x02",
    )

    CloseMessageWindow()

    def lambda_497D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_497D)

    #C0117
    ChrTalk(
        0x103,
        (
            "#11P#0208F空、空间……\x01",
            "被封住了……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49C3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_49C3)

    #C0118
    ChrTalk(
        0x107,
        (
            "#0813F#5P这、这是……\x01",
            "怀斯曼的『魔眼』……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A10():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4A10)

    #C0119
    ChrTalk(
        0x108,
        "#0907F#5P不可能……怎么做到的！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetCameraDistance(18000, 60000)
    StopEffect(0x0, 0x2)
    OP_24(0x35D)
    Fade(250)
    EndChrThread(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(800)

    #C0120
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6802F#5P呵呵──你们两位似乎有着\x01",
            "相当有趣的经历呢。\x02\x03",

            "#6804F『利贝尔方舟』和\x01",
            "『影之国』吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4B12():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4B12)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0x107, 0x2)
    OP_0D()

    #C0121
    ChrTalk(
        0x107,
        (
            "#0807F#6P#N这家伙……\x01",
            "可以窥视我们的记忆！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4B6A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4B6A)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0x108, 0x2)
    OP_0D()

    #C0122
    ChrTalk(
        0x108,
        (
            "#0907F#6P#N难道说……\x01",
            "这是从我们的记忆中再现的吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0123
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6805F#5P怀斯曼……\x01",
            "哦，这个人似乎\x01",
            "和我很有共鸣啊。\x02\x03",

            "#6800F『噬身之蛇』的情报\x01",
            "也远比想象中更有趣……\x02\x03",

            "#6809F呵呵……\x01",
            "似乎能让我好好开心一下啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x108,
        "#0901F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0125
    ChrTalk(
        0x107,
        "#0801F#6P#N呜……竟被这种家伙……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0126
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5P呵呵……赌局是我赢了。\x02\x03",

            "#6800F──现在立刻就让你们\x01",
            "服下『真知』如何？\x02\x03",

            "这样一来，\x01",
            "你们就会任凭我摆布……\x02\x03",

            "而琪雅大人应该也会理解我的\x01",
            "一片苦心，从而回归教团吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4DFD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4DFD)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x37)
    SetChrSubChip(0x104, 0x0)
    OP_0D()

    #C0127
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0310F#12P#N你这混蛋……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E49():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4E49)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x0)
    OP_0D()

    #C0128
    ChrTalk(
        0x102,
        (
            "#0110F#6P#N这、这就是你\x01",
            "引诱我们来此的目的吗……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0129
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5P呵呵，不然\x01",
            "我为何要特意抽出时间来\x01",
            "见你们这些蠢货？\x02\x03",

            "#6814F一切都是为了琪雅大人……\x02\x03",

            "除此以外，\x01",
            "还能有其它理由吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F32():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4F32)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x103, 0x36)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    #C0130
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6P#0201F#12P#N……你、你这……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    def lambda_4F9B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F9B)
    Fade(250)
    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0131
    ChrTalk(
        0x101,
        (
            "#0006F#6P#N……你既然已经有\x01",
            "如此强大的力量了……\x02\x03",

            "#0008F到底还有什么理由\x01",
            "要执著于琪雅……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0132
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6805F#5P此话怎讲……？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-6100, 1000, -8000, 0)
    MoveCamera(57, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    MoveCamera(33, 15, 0, 85000)
    SetCameraDistance(20000, 85000)
    OP_0D()

    def lambda_50A2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50A2)
    Sleep(500)

    #C0133
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#6P#N就算她真的出生在\x01",
            "五百年以前的时代……\x02\x03",

            "但终究也只是个\x01",
            "普通的小女孩吧……？\x02\x03",

            "#0001F你都已经这么强大了，\x01",
            "为什么还要对琪雅如此执著……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0134
    ChrTalk(
        0x102,
        "#0108F#6P#N的、的确……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0135
    ChrTalk(
        0x108,
        "#0908F#6P#N这真是最根本的疑问呢……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0136
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6813F#11P呵呵，我不是说过吗，\x01",
            "她将会成为真正的『神』……\x02\x03",

            "竟拿我这点力量与琪雅大人\x01",
            "进行比较，实在是愚蠢至极。\x02\x03",

            "#6809F不，呵呵……\x01",
            "应该说，这种比较本身\x01",
            "就毫无意义吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        "#0310F#6P#N莫名其妙……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0138
    ChrTalk(
        0x107,
        (
            "#0806F#6P#N真是……\x01",
            "跟某人如出一辙啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0003F#6P#N也罢……\x01",
            "事到如今，我就直接问了。\x02\x03",

            "#0001F──琪雅为什么\x01",
            "会出现在竞拍会的会场？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0140
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6801F#11P……………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0108F#6P#N的确……\x01",
            "关于这一点，仍还是个谜呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0142
    ChrTalk(
        0x103,
        (
            "#6P#0201F#6P#N那些黑手党……\x01",
            "似乎也毫无头绪……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0006F#6P#N……我再问你。\x02\x03",

            "#0013F杀害我哥哥──盖伊·班宁斯的人\x01",
            "是你吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0144
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6805F#11P哦哦……\x01",
            "是吗，原来是这样啊！\x02\x03",

            "#6800F原来如此……相依为命的两兄弟……\x01",
            "年龄相差将近十岁……\x02\x03",

            "哥哥殉职之后，弟弟离开了克洛斯贝尔，\x01",
            "然后又回来了吗……\x02\x03",

            "#6809F哈哈──这可真是太有意思了！\x02\x03",

            "没想到你就是\x01",
            "那个棘手男人的弟弟……！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F#6P#N……可以将你的回答\x01",
            "理解为承认吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0146
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#11P呵呵，当时他的确\x01",
            "已经快要查到了我头上。\x02\x03",

            "#6800F因为他实在是个麻烦，我就指示鲁巴彻\x01",
            "去消灭他……\x02\x03",

            "但是，最终杀死他的\x01",
            "似乎是其它势力。\x02\x03",

            "#6804F三年前，马尔克尼\x01",
            "将其当作自己的功劳，\x01",
            "想卖我个人情……\x02\x03",

            "但加尔西亚却对此表示否定，\x01",
            "所以不可能是他们干的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F#6P#N原来如此……我想也是这样。\x02\x03",

            "#0000F──因为大哥他才不会\x01",
            "败给你这种人。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0148
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6801F#11P！！\x02\x03",

            "#6800F哦……\x01",
            "你这话倒是很有趣嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#6P#N琪雅出现在竞拍会场的来龙去脉……\x02\x03",

            "对你来说，大概也是\x01",
            "预料之外的突发事件……\x02\x03",

            "#0001F因为你不可能轻易放手，\x01",
            "将自己尊为『神』的存在交予他人……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0150
    ChrTalk(
        0x102,
        "#0101F#6P#N……的确……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0151
    ChrTalk(
        0x103,
        "#6P#0203F#6P#N那样就太不合理了呢……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0152
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6811F#11P……呜…………\x02\x03",

            "的确，那一天……\x01",
            "琪雅大人终于\x01",
            "从漫长的沉睡中苏醒……\x02\x03",

            "#6803F可是，当我得知此事时，\x01",
            "她便已经不在这座祭坛了……\x02\x03",

            "……我想，恐怕她是迷路乱走，\x01",
            "无意中走到了地面之上……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#6P#N然后偶然钻进了那口\x01",
            "原本装有展品人偶的箱子……？\x02\x03",

            "#0006F──太荒唐了，\x01",
            "那是根本不可能的。\x02\x03",

            "而且『黑月』事先就得知了这个情报。\x02\x03",

            "#0001F也就是说──在这次的事件中，\x01",
            "连你这个身为幕后黑手的人\x01",
            "也有很多事情并不清楚。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0154
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6811F#11P唔……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0309F#6P#N哈哈……戳到要害啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0156
    ChrTalk(
        0x107,
        "#0802F#6P#N罗伊德，好厉害……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x108,
        "#0902F#6P#N不愧是搜查官呢……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0158
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6807F#11P那、那又怎么样！\x02\x03",

            "只要琪雅大人能回来，\x01",
            "像这种细枝末节的疑问——\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-3200, 1000, -8000, 0)
    MoveCamera(91, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(16500, 30000)
    OP_0D()

    #C0159
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0002F#6P#N『真之睿智（真知）』？\x01",
            "开玩笑也要有个限度吧……？\x02\x03",

            "#0003F你现在的所作所为，\x01",
            "不过就是偷看别人的记忆，\x01",
            "模仿别人的能力而已吧……\x02\x03",

            "你以残酷实验为基础\x01",
            "完成的药品也一样……\x02\x03",

            "#0008F那只不过是折磨无辜的孩子们，\x01",
            "反复进行愚蠢的试验，在经过无数次错误之后，\x01",
            "最后偶然得到的结果……\x02\x03",

            "#0013F那种东西，\x01",
            "又岂能算是什么『睿智』……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0160
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6811F#5P你、你小子……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0101F#6P#N的确，以『睿智』来说，\x01",
            "未免也太下作了……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0162
    ChrTalk(
        0x103,
        (
            "#6P#0211F#12P#N……我觉得就算\x01",
            "说是下贱也没有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0163
    ChrTalk(
        0x107,
        (
            "#0806F#6P#N抱歉，我觉得怀斯曼的品格\x01",
            "好像都比你强得多……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0164
    ChrTalk(
        0x108,
        "#0903F#6P#N嗯……我也有同感。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    LoadEffect(0x5, "event\\ev621_00.eff")
    LoadEffect(0x6, "event\\ev619_00.eff")
    LoadEffect(0x7, "event\\ev610_00.eff")
    Fade(500)
    OP_68(-9600, 700, -8000, 0)
    MoveCamera(310, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrSubChip(0x107, 0x3)
    SetChrPos(0x108, -10000, 0, -4700, 135)
    SetChrSubChip(0x108, 0x3)
    SetChrPos(0x102, -10300, 0, -6300, 90)
    SetChrPos(0x8, -3500, 0, -8000, 270)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MoveCamera(310, 19, 5, 6500)
    SetCameraDistance(16000, 6500)
    OP_0D()
    PlayEffect(0x7, 0x1, 0x101, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 100, 0)

    def lambda_5DFD():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DFD)
    Sleep(500)

    #C0165
    ChrTalk(
        0x101,
        (
            "#5P#0008F……而且，现在……\x02\x03",

            "你还企图将那无聊的幻想\x01",
            "强加在琪雅的身上。\x02\x03",

            "#0003F强加给那个如阳光般明朗，\x01",
            "纯洁善良，天真烂漫……\x02\x03",

            "#0010F而且温柔体贴，\x01",
            "对我们来说最重要的孩子……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    PlayEffect(0x4, 0xFF, 0x101, 0x0, 0, 136000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(506, 0, 90, 0)
    Sound(565, 0, 90, 0)
    Sleep(2000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x3A)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    SetChrChipByIndex(0x101, 0x3A)
    SetChrSubChip(0x101, 0x1)
    BeginChrThread(0x101, 3, 0, 12)
    BeginChrThread(0x8, 3, 0, 10)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7533", 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0166
    ChrTalk(
        0x101,
        (
            "#5P#0007F#4S──我们绝不会\x01",
            "让你的愚蠢计划得逞！！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x8, 3)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0167
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#6810F不、不可能……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_605A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_605A)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0168
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0205F#5P啊……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60A1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_60A1)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0169
    ChrTalk(
        0x104,
        "#5P#0302F身体能动了……！\x02",
    )

    CloseMessageWindow()

    def lambda_60F0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_60F0)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0170
    ChrTalk(
        0x102,
        "#5P#0102F束缚……解开了……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_6148():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_6148)
    Sleep(100)

    def lambda_6164():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_6164)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(540, 0, 80, 0)
    OP_0D()
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0171
    ChrTalk(
        0x108,
        (
            "#5P#0904F原来如此……他的『魔眼』\x01",
            "终归只是复制品而已……\x02\x03",

            "#0900F一旦内心动摇就无法维持，\x01",
            "只是这种程度的未完成品吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x107,
        (
            "#11P#0809F罗伊德凭借着气势，\x01",
            "把它打破了呢……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-6640, 1000, -7610, 1000)
    MoveCamera(305, 15, 0, 1000)
    SetCameraDistance(17000, 1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x3B)
    SetChrSubChip(0x101, 0x4)
    Sound(808, 0, 90, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_6F(0x79)

    #C0173
    ChrTalk(
        0x101,
        (
            "#5P#0013F──约亚西姆·琼塔，\x01",
            "你的伎俩已经被我完全看穿了。\x02\x03",

            "接下来，不管你再怎么挣扎，\x01",
            "也绝对无法使我们屈服。\x02\x03",

            "#0007F还是老老实实地投降吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_6333():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6333)
    WaitChrThread(0x8, 2)
    Sleep(600)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Sleep(300)

    def lambda_636E():
        OP_9D(0xFE, 0xFFFFF254, 0x0, 0xFFFFE5D4, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_636E)

    def lambda_638B():
        OP_96(0xFE, 0xFFFFF510, 0x0, 0xFFFFE0C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_638B)
    Sound(974, 0, 100, 0)
    WaitChrThread(0xF, 1)

    def lambda_63AF():
        OP_9D(0xFE, 0xFFFFF254, 0x0, 0xFFFFE7C8, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_63AF)
    WaitChrThread(0x8, 1)
    Sleep(300)

    def lambda_63D3():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_63D3)
    WaitChrThread(0x8, 2)
    Sleep(600)

    #C0174
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#6803F#40W哈哈……伤脑筋啊……\x02\x03",

            "#2S#50W……这样一来……\x01",
            "只有……了吗………\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#0001F……？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        (
            "#5P#0307F喂……\x01",
            "你在嘟囔些什么啊！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0177
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#6814F#4S呀哈哈……！\x01",
            "这样的话，我岂不是\x01",
            "只有拿出杀手锏了吗！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2500, 300, -8000, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, -3000, 0, -8000, 270)
    SetChrPos(0x101, -9600, 0, -8000, 90)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x102, -10300, 0, -6600, 90)
    SetChrPos(0x103, -10800, 0, -10400, 90)
    SetChrPos(0x104, -11500, 0, -8900, 90)
    SetChrPos(0x107, -9500, 0, -4100, 135)
    SetChrPos(0x108, -11100, 0, -5100, 135)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    SetCameraDistance(21000, 1000)
    Sleep(750)
    Fade(250)
    SetChrChipByIndex(0x8, 0x3E)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sound(975, 0, 100, 0)
    OP_6F(0x10)
    CancelBlur(0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0007F#6P#N什么……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0179
    ChrTalk(
        0x102,
        "#0107F#6P#N那、那是……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x320)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #A0180
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6813F呵呵……告诉你们吧。\x02\x03",

            "这才是真正的完成品，才是有资格\x01",
            "被称为『真知』的最终形态……\x02\x03",

            "如果将你们得到的那个称为\x01",
            "『蓝之睿智』……\x02\x03",

            "那么，这个便可称为\x01",
            "『红之睿智』吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0181
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0201F#12P#N难、难道说……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0182
    ChrTalk(
        0x104,
        (
            "#0307F#12P#N那就是把混账秘书和那些黑手党\x01",
            "变成怪物的……！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(1959, 255, 100, 0)    #voice#Joachim
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0183
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#6809F#4S哈哈哈──完全没错！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x3F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sound(975, 0, 100, 0)
    OP_0D()
    Sleep(500)
    StopBGM(0x1F40)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0184
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F#6P#N糟了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0185
    ChrTalk(
        0x108,
        "#0907F#6P#N一次服用那么多的话……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x10, 2, 0, 15)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)

    def lambda_6983():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6983)
    Sleep(300)
    OP_68(-2050, 300, -8000, 1500)

    def lambda_69B0():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE0C0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_69B0)
    WaitChrThread(0x8, 1)

    def lambda_69CE():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_69CE)
    Sleep(300)

    def lambda_69EA():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFE0C0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_69EA)
    WaitChrThread(0x8, 1)

    def lambda_6A08():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6A08)

    #C0186
    ChrTalk(
        0x103,
        "#0207F#12P#N中毒症状……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0187
    ChrTalk(
        0x107,
        (
            "#0807F#6P#N总、总而言之，\x01",
            "必须让他快点吐出来……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_E5()
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(1000, 300, -8000, 5000)
    MoveCamera(90, 13, 0, 5000)
    SetCameraDistance(19000, 5000)

    #C0188
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#6805F#45A#60W看见了……我看见了……！\x02\x03",

            "#65A#6814F#70W……伟大的『Ｄ』……\x01",
            "……失落的力量之源……！\x02",
        )
    )
    #Auto

    OP_6F(0x79)
    Fade(500)
    OP_68(-2000, 900, -8000, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_EE(0x0, 0x1)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x3C)
    SetChrSubChip(0x8, 0x0)
    CancelBlur(0)
    OP_68(-2000, 1500, -8000, 8000)
    MoveCamera(50, 13, 10, 8000)
    SetCameraDistance(10500, 8000)
    Sleep(6300)
    Sleep(120)
    SetChrSubChip(0x8, 0x1)
    Sleep(120)
    SetChrSubChip(0x8, 0x2)
    BeginChrThread(0x101, 3, 0, 13)
    Sound(868, 0, 100, 0)
    Sound(930, 2, 100, 0)
    Sound(861, 2, 100, 0)
    #Sound(1961, 255, 100, 0)    #voice#Joachim
    PlayEffect(0x2, 0x0, 0x8, 0x40, 0, 100, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    #C0189
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#5S#35A呀哈哈哈哈哈哈哈哈哈哈！\x02",
        )
    )
    #Auto

    BlurSwitch(0x1194, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1500)

    def lambda_6C48():
        OP_A6(0xFE, 0x0, 0x32, 0x1770, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_6C48)
    Sleep(1000)
    Sound(976, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(150)
    SetChrSubChip(0x8, 0x4)
    Sleep(150)
    SetChrSubChip(0x8, 0x5)
    Sleep(150)
    SetChrSubChip(0x8, 0x6)
    Sleep(150)
    SetChrSubChip(0x8, 0x7)
    Sleep(150)
    SetChrSubChip(0x8, 0x8)
    Sleep(150)
    SetChrSubChip(0x8, 0x9)
    Sleep(150)
    SetChrSubChip(0x8, 0xA)
    Sleep(150)
    SetChrSubChip(0x8, 0xB)
    Sleep(150)
    SetChrSubChip(0x8, 0xC)
    Sleep(150)
    SetChrSubChip(0x8, 0xD)
    Sleep(150)
    SetChrSubChip(0x8, 0xE)
    Sleep(150)
    PlayEffect(0x6, 0x1, 0x8, 0x40, 0, 100, 0, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0x8, 0xF)
    Sleep(150)
    SetChrSubChip(0x8, 0x10)
    Sleep(150)
    SetChrSubChip(0x8, 0x11)
    Sleep(150)
    SetChrSubChip(0x8, 0x12)
    Sleep(150)
    SetChrSubChip(0x8, 0x13)
    Sleep(150)
    SetChrSubChip(0x8, 0x14)
    Sleep(150)
    SetChrSubChip(0x8, 0x15)
    Sleep(150)
    SetChrSubChip(0x8, 0x16)
    Sleep(150)
    SetChrSubChip(0x8, 0x17)
    Sleep(150)
    FadeToDark(1500, 16777215, -1)
    Sound(937, 0, 100, 0)
    SetChrSubChip(0x8, 0x18)
    Sleep(150)
    SetChrSubChip(0x8, 0x19)
    Sleep(150)
    SetChrSubChip(0x8, 0x1A)
    Sleep(150)
    SetChrSubChip(0x8, 0x1B)
    Sleep(150)
    SetChrSubChip(0x8, 0x1C)
    Sleep(150)
    SetChrSubChip(0x8, 0x1D)
    Sleep(150)
    SetChrSubChip(0x8, 0x1E)
    PlayEffect(0x3, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrSubChip(0x8, 0x1F)
    OP_0D()
    EndChrThread(0x8, 0x3)
    EndChrThread(0x101, 0x3)
    Sleep(1000)
    BeginChrThread(0x10, 1, 0, 14)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x107, 0x8)
    SetChrFlags(0x108, 0x8)
    SetChrPos(0xB, -2000, 0, -8000, 0)
    ClearChrFlags(0xB, 0x80)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0xA)
    OP_71(0x2, 0x41A, 0x42E, 0x0, 0x20)
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    CancelBlur(0)
    OP_68(-3000, 3100, -8000, 0)
    MoveCamera(270, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(6000, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-3000, 2100, -8000, 5000)
    FadeToBright(2000, 16777215)
    OP_6F(0x1)
    Sleep(500)
    Fade(1000)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-3700, 1300, -8000, 0)
    MoveCamera(180, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(5500, 0)
    OP_68(-3700, 2300, -8000, 5000)
    OP_6F(0x1)
    Sleep(500)
    EndChrThread(0x10, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7406", 0)
    Fade(1000)
    Sound(976, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-3700, 2500, -8000, 0)
    MoveCamera(55, -3, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(7000, 0)
    MoveCamera(65, -13, 0, 5000)
    SetCameraDistance(10000, 5000)
    OP_74(0x2, 0xF)
    ClearMapObjFlags(0x2, 0x20)
    OP_71(0x2, 0x334, 0x384, 0x0, 0x0)
    OP_79(0x2)
    OP_71(0x2, 0xA, 0x31, 0x0, 0x20)
    OP_6F(0x50)
    Sleep(500)
    EndChrThread(0x10, 0x1)
    Fade(1000)
    Sound(977, 0, 90, 0)
    Sound(978, 0, 100, 0)
    OP_24(0x35D)
    OP_68(-3000, 3000, -8000, 0)
    MoveCamera(90, -10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(5500, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(13000, 2000)
    OP_6F(0x10)
    Sleep(1500)
    CancelBlur(0)
    OP_E6()

    #C0190
    ChrTalk(
        0x101,
        "#0011F#6P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0191
    ChrTalk(
        0x102,
        "#0105F#6P#N……这、这……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0305F#12P#N喂喂……\x01",
            "……开玩笑吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0193
    ChrTalk(
        0x103,
        "#0207F#12P#N这、这种灵压是……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0194
    ChrTalk(
        0x107,
        "#0813F#N#6P约、约修亚……这是……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0195
    ChrTalk(
        0x108,
        (
            "#0903F#N#6P嗯……\x02\x03",

            "#0901F说不定，比与至宝融合的\x01",
            "怀斯曼更加……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-6000, 1500, -8000, 0)
    MoveCamera(295, 31, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(16000, 0)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x107, 0x8)
    ClearChrFlags(0x108, 0x8)
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
    Sleep(1)
    MoveCamera(245, 31, 0, 30000)
    SetCameraDistance(18000, 30000)
    OP_0D()
    Sleep(1000)
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(978, 0, 100, 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0196
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W啊啊……真畅快……\x02",
        )
    )

    CloseMessageWindow()

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W此刻……\x01",
            "吾终于掌握了万物之真实……\x02",
        )
    )

    CloseMessageWindow()

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W世界的根源本质……\x01",
            "……与那些被隐藏的意图……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_C7(0x1, 0x800)
    Sleep(300)

    #C0199
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F#N#5P呜……快醒醒吧……！\x02\x03",

            "#0007F那些都是虚幻的假象而已！\x01",
            "所谓的『真实』，绝不是\x01",
            "如此轻易就能掌握的……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(978, 0, 100, 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W呵呵……\x01",
            "那只是人类的能力极限……\x02",
        )
    )

    CloseMessageWindow()

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W而吾能看到一切……\x02",
        )
    )

    CloseMessageWindow()

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W琪雅大人失踪的经过……\x01",
            "以及你哥哥死亡的真相……\x02",
        )
    )

    CloseMessageWindow()

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W还有克洛斯贝尔这片土地\x01",
            "无法逃避的命运……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sleep(300)

    #C0204
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F#5P#N唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0205
    ChrTalk(
        0x104,
        "#0307F虚张声势……！\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(978, 0, 100, 0)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W已经没有让你们活下去\x01",
            "的意义了……\x02",
        )
    )

    CloseMessageWindow()

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W哀叹着未至真理之境地的不幸命运，\x01",
            "葬身于此吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sleep(300)
    Fade(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-4010, 2300, -7660, 0)
    MoveCamera(90, -2, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(14000, 2000)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1750)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    CancelBlur(0)
    SetCameraDistance(13000, 20000)
    Sleep(500)

    #C0208
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0206F#12P#N……和秘书先生的魔人化\x01",
            "似乎不是一个档次呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0209
    ChrTalk(
        0x104,
        (
            "#0303F#12P#N嗯，这战斗力的差距\x01",
            "好像太大了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0210
    ChrTalk(
        0x102,
        (
            "#0101F#6P#N但是，这场战斗\x01",
            "似乎是无可避免的呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0211
    ChrTalk(
        0x101,
        (
            "#0003F#6P#N嗯……拿出全部的觉悟吧。\x02\x03",

            "#0013F──艾莉、缇欧、兰迪，\x02\x03",

            "还有艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x96, 0x0, 0xBB8, 0x190)

    #C0212
    ChrTalk(
        0x101,
        (
            "#0007F#6P#N这是最后的战斗了──\x01",
            "请大家全力以赴吧！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("众队友")
    #Sound(1153, 255, 100, 0)    #voice#Elie
    #Sound(1249, 255, 100, 1)    #voice#Tio
    #Sound(1343, 255, 100, 2)    #voice#Randy
    #Sound(1689, 255, 100, 3)    #voice#Estelle
    #Sound(1759, 255, 100, 4)    #voice#Joshua
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5S好！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(13000, 1000)
    Sleep(300)
    Sound(979, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xC)
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x196), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x35D)
    OP_24(0x3CB)
    OP_24(0x3A2)
    OP_50(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle("BattleInfo_3FC", 0x30200010, 0x0, 0x4, 0xA, 0xFF)
    FadeToDark(0, 0, -1)
    StopBGM(0x1388)
    WaitBGM()
    Return()

    # Function_9_4082 end

    def Function_10_78BD(): pass

    label("Function_10_78BD")

    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    OP_24(0x3CB)
    OP_24(0x35D)
    Sound(973, 0, 100, 0)
    Sound(969, 0, 100, 0)
    Sound(204, 0, 80, 0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x1, 0xFF, 0x101, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x102, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x104, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x107, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x108, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_78BD end

    def Function_11_7A46(): pass

    label("Function_11_7A46")


    def lambda_7A4B():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7A4B)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Return()

    # Function_11_7A46 end

    def Function_12_7A75(): pass

    label("Function_12_7A75")

    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_68(-9280, 900, -7620, 300)
    MoveCamera(310, 19, 0, 300)
    SetCameraDistance(17500, 300)
    OP_6F(0x79)
    CancelBlur(1000)
    Return()

    # Function_12_7A75 end

    def Function_13_7AB4(): pass

    label("Function_13_7AB4")

    OP_82(0x64, 0x64, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0x96, 0x96, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0xFA, 0xFA, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sleep(1500)
    Return()

    # Function_13_7AB4 end

    def Function_14_7B19(): pass

    label("Function_14_7B19")

    OP_25(0x3A2, 0x5A)
    Sleep(200)
    OP_25(0x3A2, 0x50)
    Sleep(200)
    OP_25(0x3A2, 0x46)
    Sleep(200)
    OP_25(0x3A2, 0x3C)
    Sleep(200)
    OP_25(0x3A2, 0x32)
    Sleep(200)
    OP_25(0x3A2, 0x28)
    Sleep(200)
    OP_25(0x3A2, 0x1E)
    Sleep(200)
    OP_25(0x3A2, 0x14)
    Sleep(200)
    OP_25(0x3A2, 0xA)
    Sleep(200)
    OP_24(0x3A2)
    Return()

    # Function_14_7B19 end

    def Function_15_7B5C(): pass

    label("Function_15_7B5C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B75")
    Sound(915, 0, 100, 0)
    Sleep(2000)
    Jump("Function_15_7B5C")

    label("loc_7B75")

    Return()

    # Function_15_7B5C end

    def Function_16_7B76(): pass

    label("Function_16_7B76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("apl/ch50547.itc", 0x2A)
    LoadChrToIndex("chr/ch00653.itc", 0x2B)
    LoadChrToIndex("chr/ch00753.itc", 0x2C)
    LoadChrToIndex("chr/ch00056.itc", 0x2D)
    LoadChrToIndex("chr/ch00156.itc", 0x2E)
    LoadChrToIndex("chr/ch00256.itc", 0x2F)
    LoadChrToIndex("chr/ch00356.itc", 0x30)
    LoadChrToIndex("apl/ch50338.itc", 0x31)
    LoadChrToIndex("apl/ch50548.itc", 0x32)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x108, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SoundLoad(930)
    OP_68(-2000, 2700, -8000, 0)
    MoveCamera(45, -5, 0, 0)
    OP_6E(760, 0)
    SetCameraDistance(11500, 0)
    OP_EE(0x0, 0xA)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x101, -11300, 0, -8000, 90)
    SetChrPos(0x102, -12200, 0, -6600, 90)
    SetChrPos(0x103, -12700, 0, -10400, 90)
    SetChrPos(0x104, -13400, 0, -8900, 90)
    SetChrPos(0x107, -11400, 0, -4100, 135)
    SetChrPos(0x108, -13000, 0, -5100, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x0, 0x5, 0xC8)
    OP_32(0x1, 0x5, 0xC8)
    OP_32(0x2, 0x5, 0xC8)
    OP_32(0x3, 0x5, 0xC8)
    OP_32(0x6, 0x5, 0xC8)
    OP_32(0x7, 0x5, 0xC8)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, -2000, 0, -8000, 0)
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0xF)
    OP_70(0x0, 0x65)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    OP_78(0x1, 0xE)
    OP_49()
    OP_74(0x1, 0xF)
    OP_CA(0x1, 0xFF, 0x0)
    LoadEffect(0x0, "event\\ev620_00.eff")
    LoadEffect(0x1, "event\\ev614_01.eff")
    LoadEffect(0x2, "event\\eva03_01.eff")
    LoadEffect(0x3, "event\\ev613_00.eff")
    LoadEffect(0x4, "event\\ev613_01.eff")
    LoadEffect(0x5, "event\\ev613_02.eff")
    LoadEffect(0x6, "event\\ev613_03.eff")
    LoadEffect(0x7, "event\\eva04_00.eff")
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    BeginChrThread(0xB, 3, 0, 30)
    MoveCamera(70, 25, 0, 6000)
    SetCameraDistance(14500, 6000)
    OP_7D(0xFF, 0xC8, 0xBE, 0x0, 0x1770)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x64, 0x1770)
    Sound(930, 2, 100, 0)
    PlayBGM("ed7406", 0)
    FadeToBright(1000, 0)
    Sound(978, 0, 100, 0)
    Sound(948, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    #Sound(1962, 255, 100, 0)    #voice#Joachim

    #A0214
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#20A#60W噢噢噢噢噢噢噢噢噢……！！！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(2000)
    OP_6F(0x50)
    Fade(500)
    OP_68(-7300, 1700, -8000, 0)
    MoveCamera(60, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    CancelBlur(0)
    OP_0D()

    #C0215
    ChrTalk(
        0x101,
        "#0010F#6P#N这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0216
    ChrTalk(
        0x103,
        (
            "#0201F#6P#N好、好像已经完全\x01",
            "失控了……\x02\x03",

            "#0206F既然到了这个地步……\x01",
            "……他的肉体恐怕已经……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0217
    ChrTalk(
        0x102,
        "#0101F#6P#N怎么会……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0218
    ChrTalk(
        0x108,
        "#0901F#6P#N……呜……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-300, 2500, -8000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    BeginChrThread(0xB, 3, 0, 31)
    SetCameraDistance(16500, 1500)
    OP_0D()
    ClearMapObjFlags(0x0, 0x20)
    OP_71(0x0, 0xBF, 0xE6, 0x0, 0x0)
    Sound(976, 0, 90, 0)
    Sound(978, 0, 100, 0)
    Sound(948, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    #Sound(1963, 255, 100, 0)    #voice#Joachim

    #A0219
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#60W#15A叽咿咿咿咿咿咿……！！！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x10)
    OP_79(0x0)
    OP_68(-10800, 700, -8000, 1000)
    MoveCamera(47, 23, 0, 1000)
    SetCameraDistance(13000, 1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xE7, 0xF0, 0x0, 0x0)
    Sound(977, 0, 90, 0)
    OP_79(0x0)
    PlayEffect(0x0, 0x6, 0xB, 0x0, -3300, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0xB, 0x0, -3600, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xF1, 0x118, 0x0, 0x20)
    OP_6F(0x79)
    OP_68(-10800, 1700, -8000, 1000)
    MoveCamera(47, 17, 0, 1000)
    SetCameraDistance(14500, 1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(981, 0, 100, 0)
    Sound(1029, 255, 100, 0)    #voice#Lloyd
    Sound(1129, 255, 100, 1)    #voice#Elie
    Sound(1224, 255, 100, 2)    #voice#Tio
    Sound(1319, 255, 100, 3)    #voice#Randy
    Sound(1671, 255, 100, 4)    #voice#Estelle
    Sound(1741, 255, 100, 5)    #voice#Joshua
    PlayEffect(0x1, 0x0, 0x101, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(100)
    PlayEffect(0x1, 0x1, 0x102, 0x0, 0, 0, 0, 30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x102, 3, 0, 25)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0x103, 0x0, 0, 0, 0, 70, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x103, 3, 0, 26)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0x104, 0x0, 0, 0, 0, 130, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(100)
    PlayEffect(0x1, 0x4, 0x107, 0x0, 0, 0, 0, 200, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x107, 3, 0, 28)
    Sleep(100)
    PlayEffect(0x1, 0x5, 0x108, 0x0, 0, 0, 0, 170, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x108, 3, 0, 29)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x107, 3)
    WaitChrThread(0x108, 3)
    SetCameraDistance(11000, 20000)
    Sleep(500)

    #C0220
    ChrTalk(
        0x107,
        "#6P#0813F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        "#6P#0307F啊……！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x108,
        "#0907F#6P糟、糟了……！\x02",
    )

    CloseMessageWindow()
    Sound(978, 0, 100, 0)
    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName("")
    #Sound(1962, 255, 100, 0)    #voice#Joachim

    #A0223
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S#70W#50A……噢噢噢噢噢噢噢……！！！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0224
    ChrTalk(
        0x102,
        "#0108F#6P…………！\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        (
            "#6P#0310F嘁……\x01",
            "这样下去的话……！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x107,
        (
            "#6P#0807F怎、怎么可以……\x01",
            "怎么可以在这里放弃呢！\x02\x03",

            "#0806F……好不容易才能……\x02\x03",

            "#0808F才能在真正意义上\x01",
            "将那孩子紧拥在怀中……！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#6P#0007F我们也一样……！\x02\x03",

            "#0003F……一定要……\x01",
            "无论如何也一定要回到那孩子的身边……！\x02\x03",

            "#0010F……大哥……拜托了……！\x02\x03",

            "请借给我力量吧……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, -8000, 9000, 8000, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    #N0228
    NpcTalk(
        0xC,
        "少女的声音",
        "#4P呵呵……\x02",
    )

    CloseMessageWindow()

    #N0229
    NpcTalk(
        0xC,
        "少女的声音",
        (
            "#4P虽然我不是你的哥哥，\x01",
            "不过也可以提供一次特别服务哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(500)
    EndChrThread(0xB, 0x3)
    Sleep(500)
    Fade(500)
    OP_68(-8000, 27500, 8000, 0)
    MoveCamera(310, -10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x1, 0x4)
    OP_D1(0xC, 0x1, "Null_ren(52)")
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xE, -8000, 35000, 8000, 0)
    OP_D3(0xE, 0x0, 0x249F0, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0xF1, 0x104, 0x0, 0x20)
    PlayEffect(0x2, 0x6, 0xE, 0x40, 0, 0, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x7, 0xE, 0x40, 0, 0, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(980, 0, 100, 0)

    def lambda_8908():
        OP_96(0xFE, 0xFFFFE0C0, 0xFFFFFC18, 0x1F40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_8908)
    OP_0D()
    OP_68(-8000, 12500, 8000, 4000)
    MoveCamera(310, 70, 0, 4000)
    SetCameraDistance(13000, 4000)
    OP_6F(0x79)
    Fade(250)
    OP_68(-8000, 400, 8000, 0)
    MoveCamera(290, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11500, 0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    OP_70(0x1, 0xDD)
    OP_77(0x1, 0x3E8)
    WaitChrThread(0xE, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(-8000, 2400, 8000, 2000)
    MoveCamera(290, 13, 0, 2000)
    SetCameraDistance(17500, 2000)
    PlayEffect(0x7, 0xFF, 0xE, 0x40, 0, 0, 0, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_24(0x3A2)
    Sound(944, 0, 100, 0)
    Sound(813, 0, 100, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x5DC)
    OP_71(0x1, 0xDD, 0xF0, 0x0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0x17D, 0x1A4, 0x0, 0x20)
    OP_6F(0x79)
    Fade(1000)
    CancelBlur(0)
    OP_0D()

    #C0230
    ChrTalk(
        0x101,
        "#0011F啊……！\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        "#0105F在、在医院见过的……！？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x108,
        "#0901F『帕蒂尔·玛蒂尔』……！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x107,
        "#0802F玲──！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-9300, 2700, 4800, 0)
    MoveCamera(5, 9, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    OP_EE(0x0, 0x5)
    PlayEffect(0x0, 0x6, 0xB, 0x0, -3300, 0, 3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x7, 0xB, 0x0, -3600, 0, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()

    #N0234
    NpcTalk(
        0xC,
        "歼灭天使玲",
        (
            "#3308F#5P……真可怜呢，\x01",
            "但这也是自作自受吧。\x02\x03",

            "#3303F立刻就让你彻底解脱哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_D1(0xC, 0xFF, "")
    OP_93(0xC, 0x96, 0x0)
    SetChrFlags(0xC, 0x4)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x31)
    SetChrSubChip(0xC, 0x2)
    SetChrChip(0x0, 0xC, 0x32, 0x12C)
    Sound(854, 0, 100, 0)

    def lambda_8BF9():
        OP_9D(0xFE, 0xFFFFCE64, 0x352, 0x1388, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8BF9)
    WaitChrThread(0xC, 1)
    PlayEffect(0x7, 0xFF, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(50)
    Sound(31, 0, 100, 0)
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    Fade(500)
    OP_68(-9300, 2100, 3300, 0)
    MoveCamera(100, -3, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(12500, 0)
    OP_0D()
    MoveCamera(108, -3, 0, 1000)
    SetCameraDistance(10500, 1000)
    OP_77(0x1, 0x12C)
    OP_71(0x1, 0x79, 0x8C, 0x0, 0x0)
    Sound(945, 0, 100, 0)
    Sleep(600)
    Sound(947, 0, 100, 0)
    OP_79(0x1)
    Sound(945, 0, 100, 0)
    OP_6F(0x79)

    #N0235
    NpcTalk(
        0xC,
        "歼灭天使玲",
        (
            "#6P#3301F帕蒂尔·玛蒂尔！\x01",
            "清除目标……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #N0236
    NpcTalk(
        0xC,
        "歼灭天使玲",
        "#6P#3307F#4S『双重加农炮强打』！！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(943, 0, 100, 0)
    Sleep(800)
    Fade(250)
    OP_68(-6900, 3100, 4000, 0)
    MoveCamera(0, 12, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(9500, 0)
    OP_EE(0x0, 0xA)
    OP_D3(0xE, 0x0, 0x27100, 0x0, 0x0)
    OP_93(0xE, 0xA0, 0x0)
    SetChrPos(0xB, -1000, 0, -8000, 0)
    SetCameraDistance(8500, 4750)
    OP_82(0x32, 0x32, 0xBB8, 0x128E)
    OP_0D()
    PlayEffect(0x5, 0xFF, 0xE, 0x0, 2700, 4500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xE, 0x0, -100, 4500, -4300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(982, 0, 100, 0)
    Sleep(3000)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 2700, 4500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, -100, 4500, -4300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(860, 0, 100, 0)
    Sleep(1500)
    OP_68(-3200, 1600, -2000, 500)
    MoveCamera(24, 15, 0, 500)
    SetCameraDistance(17500, 500)
    Sleep(150)
    PlayEffect(0x4, 0xFF, 0xE, 0x140, -1700, 4500, 4000, 5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0xFF, 0xE, 0x140, 900, 4500, 4300, 5, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    PlayEffect(0x6, 0xFF, 0xB, 0x0, -3500, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xB, 0x0, -1000, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(983, 0, 100, 0)
    OP_82(0x190, 0x190, 0xBB8, 0x3E8)
    BeginChrThread(0xB, 1, 0, 17)
    Sleep(500)
    OP_71(0x1, 0x8D, 0xA0, 0x0, 0x0)
    Sleep(500)
    BeginChrThread(0xB, 3, 0, 31)
    Sound(930, 2, 100, 0)
    OP_6F(0x79)
    Sleep(500)
    OP_79(0x1)
    Fade(500)
    OP_68(-11700, 2000, -8000, 0)
    MoveCamera(38, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_0D()
    LoadEffect(0x2, "event\\ev614_02.eff")
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    PlayEffect(0x2, 0xFF, 0x101, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x102, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x103, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x104, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x107, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0x108, 0x0, 0, -1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(816, 0, 100, 0)
    Sleep(250)
    OP_68(-11700, 1000, -8000, 300)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x102, 3, 0, 19)
    BeginChrThread(0x103, 3, 0, 20)
    BeginChrThread(0x104, 3, 0, 21)
    BeginChrThread(0x107, 3, 0, 22)
    BeginChrThread(0x108, 3, 0, 23)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x107, 3)
    WaitChrThread(0x108, 3)
    Sleep(500)

    #C0237
    ChrTalk(
        0x103,
        "#6P#0202F『手臂』已经……！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        "#6P#0307F好，这样的话……！\x02",
    )

    CloseMessageWindow()
    OP_71(0x1, 0xA1, 0xB4, 0x0, 0x0)
    Sound(945, 0, 100, 0)
    Sleep(600)
    Sound(947, 0, 100, 0)
    Sound(945, 0, 100, 0)
    OP_79(0x1)
    OP_71(0x1, 0x17D, 0x1A4, 0x0, 0x20)
    OP_93(0xC, 0xB4, 0x1F4)

    #N0239
    NpcTalk(
        0xC,
        "歼灭天使玲",
        (
            "#3307F#13P这是最后的机会了！\x02\x03",

            "『他』已经撑不住了！\x01",
            "快给他致命一击吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#5P#0010F唔……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 90, 0)
    Sound(804, 0, 100, 0)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)
    #Sound(1019, 255, 100, 0)    #voice#Lloyd

    #C0241
    ChrTalk(
        0x101,
        "#5P#0007F#4S#20A#40W噢噢噢噢噢噢噢噢……！\x02",
    )
    #Auto

    Sleep(500)
    OP_68(-5700, 1100, -8000, 915)
    MoveCamera(53, 15, -9, 915)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_939E():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_939E)
    Sleep(5)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_93C3():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_93C3)
    Sleep(5)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x102, 0x0)

    def lambda_93E8():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_93E8)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)

    def lambda_940A():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_940A)
    Sleep(5)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_942F():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_942F)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)

    def lambda_9451():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9451)
    Sleep(900)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x107, 0x1)
    EndChrThread(0x108, 0x1)
    OP_24(0x3A2)
    Battle("BattleInfo_440", 0x30200010, 0x0, 0x4, 0xB, 0xFF)
    FadeToDark(0, 0, -1)
    StopBGM(0x1388)
    WaitBGM()
    Return()

    # Function_16_7B76 end

    def Function_17_94A5(): pass

    label("Function_17_94A5")

    OP_71(0x0, 0x33, 0x37, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)
    OP_74(0x0, 0xA)
    Sound(948, 0, 100, 0)
    Sound(978, 0, 100, 0)
    OP_71(0x0, 0x123, 0x136, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x137, 0x15E, 0x0, 0x20)
    Return()

    # Function_17_94A5 end

    def Function_18_94E3(): pass

    label("Function_18_94E3")

    ClearChrFlags(0xFE, 0x4)

    def lambda_94ED():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_94ED)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(50)
    Sound(31, 0, 100, 0)
    Return()

    # Function_18_94E3 end

    def Function_19_9535(): pass

    label("Function_19_9535")

    ClearChrFlags(0xFE, 0x4)

    def lambda_953F():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_953F)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_9535 end

    def Function_20_9578(): pass

    label("Function_20_9578")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9582():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9582)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_9578 end

    def Function_21_95BB(): pass

    label("Function_21_95BB")

    ClearChrFlags(0xFE, 0x4)

    def lambda_95C5():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_95C5)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_95BB end

    def Function_22_95FE(): pass

    label("Function_22_95FE")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9608():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9608)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_22_95FE end

    def Function_23_9641(): pass

    label("Function_23_9641")

    ClearChrFlags(0xFE, 0x4)

    def lambda_964B():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_964B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_23_9641 end

    def Function_24_9684(): pass

    label("Function_24_9684")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_96A0():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_96A0)

    def lambda_96B9():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_96B9)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_24_9684 end

    def Function_25_96E5(): pass

    label("Function_25_96E5")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9701():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9701)

    def lambda_971A():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_971A)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x3)
    Return()

    # Function_25_96E5 end

    def Function_26_9741(): pass

    label("Function_26_9741")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_975D():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_975D)

    def lambda_9776():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9776)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x2)
    Return()

    # Function_26_9741 end

    def Function_27_979D(): pass

    label("Function_27_979D")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_97B9():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_97B9)

    def lambda_97D2():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97D2)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x1)
    Return()

    # Function_27_979D end

    def Function_28_97F9(): pass

    label("Function_28_97F9")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9815():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9815)

    def lambda_982E():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_982E)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x107, 0x32)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_28_97F9 end

    def Function_29_9855(): pass

    label("Function_29_9855")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9871():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9871)

    def lambda_988A():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_988A)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x108, 0x32)
    SetChrSubChip(0x108, 0x4)
    Return()

    # Function_29_9855 end

    def Function_30_98B1(): pass

    label("Function_30_98B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98D5")
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_30_98B1")

    label("loc_98D5")

    Return()

    # Function_30_98B1 end

    def Function_31_98D6(): pass

    label("Function_31_98D6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98FA")
    OP_82(0x0, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_31_98D6")

    label("loc_98FA")

    Return()

    # Function_31_98D6 end

    def Function_32_98FB(): pass

    label("Function_32_98FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00650.itc", 0x26)
    LoadChrToIndex("chr/ch00651.itc", 0x27)
    LoadChrToIndex("chr/ch00750.itc", 0x28)
    LoadChrToIndex("chr/ch00751.itc", 0x29)
    LoadChrToIndex("apl/ch50547.itc", 0x2A)
    LoadChrToIndex("chr/ch09500.itc", 0x2B)
    LoadChrToIndex("apl/ch50338.itc", 0x2C)
    LoadChrToIndex("apl/ch50529.itc", 0x2D)
    LoadChrToIndex("apl/ch50531.itc", 0x2E)
    LoadChrToIndex("apl/ch50536.itc", 0x2F)
    SoundLoad(930)
    SoundLoad(986)
    OP_68(-3000, 2300, -8000, 0)
    MoveCamera(120, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, -10000, 0, -8000, 90)
    SetChrPos(0x102, -11300, 0, -6600, 90)
    SetChrPos(0x103, -12100, 0, -10400, 90)
    SetChrPos(0x104, -12800, 0, -8900, 90)
    SetChrPos(0x107, -9700, 0, -4000, 135)
    SetChrPos(0x108, -11900, 0, -5000, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -12700, 850, 5000, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetMapObjFlags(0x0, 0x1000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x0, 0xB)
    OP_49()
    SetChrPos(0xB, -2000, 0, -8000, 0)
    OP_D3(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    OP_74(0x0, 0xA)
    OP_70(0x0, 0x137)
    OP_71(0x0, 0x137, 0x15E, 0x0, 0x20)
    OP_7D(0xFF, 0xC8, 0xBE, 0x0, 0x0)
    OP_11(0xA0, 0x0, 0x2D, 0xF, 0x64, 0x0)
    SetMapObjFrame(0xFF, "normal0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "broken0", 0x1, 0x1)
    OP_78(0x1, 0xE)
    OP_49()
    OP_74(0x1, 0xF)
    SetChrPos(0xE, -8000, -1000, 8000, 0)
    OP_D3(0xE, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0x1, 0x17D, 0x1A4, 0x0, 0x20)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "event\\ev616_00.eff")
    LoadEffect(0x1, "event\\ev615_00.eff")
    LoadEffect(0x2, "event\\eva04_00.eff")
    MoveCamera(60, 19, 0, 15000)
    SetCameraDistance(17000, 15000)
    BeginChrThread(0xB, 3, 0, 33)
    BeginChrThread(0xB, 2, 0, 34)
    PlayBGM("ed7534", 0)
    Sleep(1500)
    BeginChrThread(0x10, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, 120, -1, -1)

    #A0242
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W……哈……哈哈……\x01",
            "……干得不错啊……\x02",
        )
    )

    CloseMessageWindow()

    #A0243
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W虽然可恨……但你们最后\x01",
            "让我恢复了神智……\x01",
            "……只有这点……我要表示感谢……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(210, 200, -1, -1)

    #A0244
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F#5P约亚西姆……你……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 200, -1, -1)

    #A0245
    AnonymousTalk(
        0x107,
        "#0808F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 120, -1, -1)

    #A0246
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W呵呵……不要用那种\x01",
            "怜悯的目光望着我……\x02",
        )
    )

    CloseMessageWindow()

    #A0247
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W……虽然未能守望到最后……\x01",
            "但吾等宏愿已然实现……\x02",
        )
    )

    CloseMessageWindow()

    #A0248
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W那位大人……\x01",
            "……琪雅大人一定会──！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x10, 0x1)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xB, 0x2)
    BeginChrThread(0xB, 3, 0, 35)
    BeginChrThread(0x10, 1, 0, 37)
    PlayEffect(0x0, 0xFF, 0xB, 0x40, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(250)
    OP_68(-2500, 2100, -8000, 0)
    MoveCamera(90, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13500, 0)
    OP_0D()
    Sleep(2000)
    SetCameraDistance(22500, 1500)
    Fade(1000)
    SetMapObjFlags(0x0, 0x4)
    OP_6F(0x10)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(1000)
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
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
    OP_11(0x61, 0x8D, 0x9E, 0x14, 0x64, 0x5DC)
    Sleep(1500)

    #C0249
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F……啊………\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#0303F嘁……\x01",
            "……直到最后还在说胡话……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#0108F但是……真可悲啊……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x103,
        "#0206F………是啊…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x10, 0x1)
    Fade(500)
    OP_68(-9280, 900, -7900, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(300)
    SetCameraDistance(19000, 2500)

    def lambda_9FA8():
        OP_95(0xFE, -9000, 0, -8000, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FA8)
    Sleep(700)

    def lambda_9FC5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9FC5)
    Sleep(50)

    def lambda_9FD5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9FD5)
    WaitChrThread(0x101, 1)
    Sleep(300)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    Sleep(250)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_6F(0x10)
    SetCameraDistance(18000, 10000)
    Sleep(300)

    #C0253
    ChrTalk(
        0x101,
        "#0008F#40W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x108,
        (
            "#0908F……不必放在心上。\x02\x03",

            "#0903F在他大量服下那种致人疯狂的药物时，\x01",
            "就已经注定没救了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    #C0255
    ChrTalk(
        0x107,
        (
            "#5P#0806F嗯……是啊……\x02\x03",

            "#0808F如果可能的话，\x01",
            "我也想救他的……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#0008F嗯……\x02\x03",

            "#0006F直到最后……我们也没能让他\x01",
            "从妄想中解脱出来……\x02\x03",

            "可能的话，本想让他正式接受制裁，\x01",
            "认清自己犯下的罪孽呢。\x02\x03",

            "#0008F否则……无论是他自己，\x01",
            "还是那些被他害死的人们，都太悲哀了……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    #C0257
    ChrTalk(
        0x102,
        "#6P#0108F罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x103,
        "#6P#0208F#N……罗伊德前辈……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    OP_68(-9030, 900, -7890, 1000)

    def lambda_A228():
        OP_95(0xFE, -9300, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A228)
    WaitChrThread(0x104, 1)
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x9)
    SetChrSubChip(0x101, 0x1)
    Sleep(140)
    OP_82(0x32, 0x0, 0xBB8, 0x64)
    SetChrSubChip(0x104, 0xA)
    SetChrSubChip(0x101, 0x2)
    Sleep(140)
    SetChrSubChip(0x104, 0xB)
    SetChrSubChip(0x101, 0x3)
    Sound(819, 0, 100, 0)
    Sleep(140)
    SetChrSubChip(0x104, 0xD)
    SetChrSubChip(0x101, 0x4)
    Sleep(140)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrSubChip(0x101, 0x5)

    #C0259
    ChrTalk(
        0x104,
        (
            "#12P#0307F喂！\x01",
            "不要一脸垂头丧气的表情啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    SetChrSubChip(0x101, 0x6)
    Sleep(100)
    SetChrSubChip(0x101, 0x7)
    Sleep(300)

    #C0260
    ChrTalk(
        0x101,
        "#0005F#5P兰迪……？\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#12P#0303F我们并不是万能的！\x01",
            "不可能把所有的事情都完美解决！\x02\x03",

            "#0301F但我们还是拼尽全力，\x01",
            "走到了这一步，不是吗！？\x02\x03",

            "虽然结果不算最好……\x01",
            "但已经算是不错了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#0005F……兰迪……\x02",
    )

    CloseMessageWindow()

    def lambda_A3DB():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A3DB)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0263
    ChrTalk(
        0x103,
        (
            "#6P#0206F……当年，在捣毁教团据点的作战行动中，\x01",
            "许多教团信徒都自行了断了。\x02\x03",

            "盖伊先生、亚里欧斯先生和科长他们\x01",
            "跨过了重重尸体，才救出了我。\x02\x03",

            "#0202F无可避免的牺牲……\x01",
            "我想偶尔也会有的。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x103, 500)

    #C0264
    ChrTalk(
        0x101,
        "#0005F……缇欧……\x02",
    )

    CloseMessageWindow()

    def lambda_A4E4():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4E4)
    WaitChrThread(0x102, 1)

    #C0265
    ChrTalk(
        0x102,
        (
            "#6P#0103F他虽然已经自取灭亡了……\x01",
            "但是还有很多善后工作需要处理。\x02\x03",

            "……要处理蔓延于整个克洛斯贝尔的混乱，\x01",
            "以及确认被操纵的众人是否安好……\x02\x03",

            "#0100F我想，现在并没有时间去消沉哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0266
    ChrTalk(
        0x101,
        "#11P#0008F……艾莉……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0267
    ChrTalk(
        0x101,
        (
            "#11P#0004F……谢谢。\x02\x03",

            "#0002F是啊……\x01",
            "现在可不是沮丧的时候。\x02\x03",

            "#0000F而且……\x01",
            "还要遵守\x01",
            "跟琪雅和科长的约定呢……！\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#6P#0102F嗯……！\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x103,
        (
            "#6P#0204F大家一起平安\x01",
            "回到那孩子身边的约定……\x02\x03",

            "#0202F还有让科长承认\x01",
            "我们已经有能力独当一面的约定吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        (
            "#0309F#12P哈哈……\x01",
            "看样子，总算是把这两条约定都守住了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x107,
        "#5P#0802F呵呵……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x108,
        "#0904F……这就是同伴吧……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0273
    ChrTalk(
        0xC,
        (
            "#3300F#13P呵呵……\x01",
            "看来已经该落幕了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_A7BF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_A7BF)

    def lambda_A7CC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_A7CC)
    Sleep(150)

    def lambda_A7DC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A7DC)

    def lambda_A7E9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A7E9)
    Sleep(50)

    def lambda_A7F9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A7F9)

    def lambda_A806():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A806)
    WaitChrThread(0x104, 2)

    #C0274
    ChrTalk(
        0x107,
        "#12P#0805F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-12700, 1700, 5000, 0)
    MoveCamera(35, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearMapObjFlags(0x1, 0x4)
    SetChrPos(0x107, -10000, 0, -6800, 0)
    SetChrPos(0x108, -9000, 0, -7300, 0)
    OP_0D()
    Sleep(500)

    #C0275
    ChrTalk(
        0xC,
        (
            "#3300F#5P本来是打算直到最后\x01",
            "都不插手的……\x02\x03",

            "#3304F呵呵……或许是受了莱维\x01",
            "的影响吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x108,
        "#0901F玲……！\x02",
    )

    CloseMessageWindow()
    OP_68(-10400, 1700, 1100, 1500)
    SetCameraDistance(16500, 1500)

    def lambda_A94B():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFF8F8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A94B)
    Sleep(200)

    def lambda_A968():
        OP_96(0xFE, 0xFFFFDCD8, 0x0, 0xFFFFF704, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A968)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x2)
    SetChrChip(0x0, 0xC, 0x32, 0x12C)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(854, 0, 100, 0)

    def lambda_A9A3():
        OP_9D(0xFE, 0xFFFFD5D0, 0x7D0, 0x16A8, 0x6D6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A9A3)
    WaitChrThread(0xC, 1)
    Sound(30, 0, 100, 0)
    Sleep(30)
    Sound(31, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_93(0xC, 0x0, 0x0)
    OP_D1(0xC, 0x1, "Null_ren(52)")
    SetChrChipByIndex(0xC, 0x2A)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0xC, 0x2B)
    SetChrSubChip(0xC, 0x0)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 70, 0)
    OP_0D()
    Sleep(500)

    #C0277
    ChrTalk(
        0xC,
        (
            "#3304F……这样一来，玲在克洛斯贝尔\x01",
            "就再无遗憾了。\x02\x03",

            "#3300F虽然在这里玩得还挺开心，\x01",
            "但有玲在的话，以后也许会更加混乱，\x01",
            "所以差不多也该告辞了——\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x107,
        "#0800F#11P玲。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_AB10():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AB10)
    Sleep(800)
    OP_93(0xC, 0x5A, 0xFA)
    Sleep(300)

    #C0279
    ChrTalk(
        0xC,
        (
            "#3306F#12P……什么事，艾丝蒂尔。\x02\x03",

            "#3308F玲还没打算……\x01",
            "被你抓住哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x107,
        (
            "#0803F#11P不对……玲。\x02\x03",

            "#0802F你啊……\x01",
            "都已经被我们抓住啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xC,
        "#3305F#12P……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7520", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x208), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-10400, 2100, 1800, 25000)
    MoveCamera(29, 1, 0, 25000)
    SetCameraDistance(17500, 25000)

    #C0282
    ChrTalk(
        0x107,
        (
            "#0808F#11P自最后分别以来，已经过去了半年……\x02\x03",

            "我们中途回过一趟利贝尔，\x01",
            "之后再次来到这里，又过了三个月……\x02\x03",

            "#0800F在这段时间，我们一直都能\x01",
            "感受到玲的气息就在附近。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x108,
        (
            "#0904F#11P我们知道你在人偶工房，\x01",
            "也知道你时不时就会来\x01",
            "克洛斯贝尔市玩。\x02\x03",

            "#0900F但想在导力网络上抓到你\x01",
            "实在是不容易呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "#3307F#12P那、那还用说……\x02\x03",

            "#3308F玲可是『小猫』……\x01",
            "谁都抓不到的！\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x107,
        (
            "#0800F除了我们以外，对吧。\x02\x03",

            "#0803F──现在，我们已经\x01",
            "知道了关于玲的一切。\x02\x03",

            "知道你的过去，你的悲伤，\x01",
            "还有你的开心和你的快乐。\x02\x03",

            "#0802F你再也……逃不掉了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        "#3308F#12P……\x02",
    )

    CloseMessageWindow()

    def lambda_AE2C():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AE2C)
    Sleep(800)
    OP_93(0xC, 0xB4, 0x12C)
    Sleep(500)

    #C0287
    ChrTalk(
        0xC,
        (
            "#3312F#12P#40W我、我还以为……\x01",
            "……你会放弃的……\x02\x03",

            "在知道了『乐园』的事情之后……\x02\x03",

            "#3313F……我以为艾丝蒂尔\x01",
            "一定会放弃的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0288
    ChrTalk(
        0x107,
        (
            "#0806F#11P如果是两年前的我，\x01",
            "说不定还真会放弃呢。\x02\x03",

            "#0802F但是，多亏与大家，\x01",
            "莱维，还有玲的相遇，\x01",
            "使我变得坚强了。\x02\x03",

            "无论过去发生过什么……\x01",
            "都造就了现在的你，\x01",
            "是很重要的回忆……\x02\x03",

            "#0809F如今，我只觉得……\x01",
            "你所有的一切都是那么惹人爱怜。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        "#3312F#12P……啊………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0290
    ChrTalk(
        0x108,
        (
            "#0903F#11P──其实，让你回到父母的身边\x01",
            "可能会更好。\x02\x03",

            "#0901F但是，我们……\x01",
            "就算是任性妄为也好，\x01",
            "也希望你能成为我们的家人。\x02\x03",

            "#0902F这是在来到克洛斯贝尔之后，\x01",
            "我们再次确定的结论。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "#3313F#12P………呜呜呜………\x02\x03",

            "怎么会……这样……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(943, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0xE, 3, 0, 36)
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_93(0xC, 0xF0, 0x1F4)

    #C0292
    ChrTalk(
        0xC,
        (
            "#3311F#6P帕蒂尔·玛蒂尔！？\x02\x03",

            "为、为什么擅自……！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x107,
        "#0805F#12P#N莫、莫非……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0294
    ChrTalk(
        0x108,
        (
            "#0902F#12P#N是吗……\x01",
            "你也一直在关心着玲……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0xE, 3)
    Fade(500)
    OP_68(-9600, 800, -1900, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    OP_93(0xC, 0x10E, 0x0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x107, -10000, 0, -2600, 0)
    SetChrPos(0x108, -9200, 0, -3000, 0)
    SetCameraDistance(17000, 2000)
    OP_0D()
    Sound(943, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x10, 1, 0, 38)
    OP_71(0x1, 0x1CD, 0x1F4, 0x0, 0x0)
    Sleep(500)

    def lambda_B265():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFF1F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B265)
    Sleep(100)

    def lambda_B282():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xFFFFF060, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B282)
    OP_79(0x1)
    OP_71(0x1, 0x1F5, 0x208, 0x0, 0x0)
    OP_93(0xC, 0xB4, 0x1F4)

    #C0295
    ChrTalk(
        0xC,
        "#11P#3310F#25A#40W#N……不、不要……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_79(0x1)
    Fade(500)
    OP_D1(0xC, 0xFF, "")
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, -9600, 0, -1700, 0)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x2E)
    SetChrSubChip(0xC, 0x0)
    OP_71(0x1, 0x209, 0x212, 0x0, 0x0)
    OP_79(0x1)
    OP_0D()
    OP_71(0x1, 0x213, 0x226, 0x0, 0x0)
    OP_79(0x1)
    OP_6F(0x10)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x108, 1)
    EndChrThread(0x10, 0x1)
    OP_68(-9530, 800, -1690, 1000)

    def lambda_B378():
        OP_96(0xFE, 0xFFFFDA1C, 0x0, 0xFFFFF704, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B378)
    Sleep(1300)
    Fade(500)
    SetChrPos(0xC, -9600, 0, -1800, 0)
    SetChrSubChip(0xC, 0xA)
    OP_A7(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x410), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)
    Sound(910, 0, 100, 0)
    SetChrSubChip(0xC, 0xB)
    Sleep(130)
    SetChrSubChip(0xC, 0xC)
    Sleep(130)
    SetChrSubChip(0xC, 0xD)
    Sound(804, 0, 70, 0)
    Sleep(130)
    SetChrSubChip(0xC, 0xE)
    Sleep(130)
    SetChrSubChip(0xC, 0xF)
    Sleep(300)
    MoveCamera(57, 17, 0, 30000)
    SetCameraDistance(16000, 30000)

    #C0296
    ChrTalk(
        0x107,
        "#11P#0804F──抓到你了。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        "#11P#3312F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_B456():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xFFFFF2B8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B456)
    WaitChrThread(0x108, 1)

    #C0298
    ChrTalk(
        0x108,
        (
            "#12P#0904F谢谢你……\x01",
            "帕蒂尔·玛蒂尔。\x02\x03",

            "#0900F经过大师的调整之后，\x01",
            "你似乎能以自己的意志\x01",
            "行动了吧？\x02",
        )
    )

    CloseMessageWindow()
    Sound(943, 0, 100, 0)
    Sleep(500)

    #C0299
    ChrTalk(
        0xC,
        "#11P#3313F呜呜呜呜……\x02",
    )

    CloseMessageWindow()

    def lambda_B500():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_B500)

    #C0300
    ChrTalk(
        0x107,
        (
            "#11P#0812F我们……\x01",
            "不会再让你逃掉了。\x02\x03",

            "……今后要去哪里，\x01",
            "要怎样生活，\x01",
            "还需要大家一起好好商量……\x02\x03",

            "#0811F不过……\x01",
            "还是先回利贝尔一趟吧……？\x02\x03",

            "提妲也一直……\x01",
            "在等着玲呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        "#11P#3312F……啊啊啊啊啊啊啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    Sound(804, 0, 100, 0)
    Sound(819, 0, 60, 0)
    Sleep(110)
    SetChrSubChip(0xC, 0x3)
    Sleep(110)
    SetChrSubChip(0xC, 0x4)
    Sleep(110)
    SetChrSubChip(0xC, 0x5)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0302
    ChrTalk(
        0xC,
        "#5P#3310F#4S哇啊啊啊啊啊啊啊啊……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x10)
    Sound(820, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0xC, 0x11)
    Sleep(130)
    SetChrSubChip(0xC, 0x12)

    #C0303
    ChrTalk(
        0x107,
        "#11P#0810F……玲……！\x02",
    )

    CloseMessageWindow()
    Sleep(130)
    SetChrSubChip(0xC, 0x11)
    Sleep(130)
    SetChrSubChip(0xC, 0x10)

    #C0304
    ChrTalk(
        0xC,
        "#5P#3313F呜呜呜……啊啊啊啊……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x7)
    Sleep(100)
    SetChrSubChip(0xC, 0x8)
    Sleep(100)
    SetChrSubChip(0xC, 0x9)
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)

    #C0305
    ChrTalk(
        0xC,
        "#5P#3310F#4S呜哇啊啊啊啊啊啊啊啊啊啊！！\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x108,
        "#0910F#11P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x101, -9300, 0, -7900, 0)
    SetChrPos(0x102, -11000, 0, -8500, 0)
    SetChrPos(0x103, -10200, 0, -9300, 0)
    SetChrPos(0x104, -8500, 0, -8800, 0)
    OP_68(-9170, 1000, -3990, 3000)
    SetCameraDistance(17000, 3000)

    def lambda_B79C():
        OP_96(0xFE, 0xFFFFDBAC, 0x0, 0xFFFFECDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B79C)
    Sleep(200)

    def lambda_B7B9():
        OP_96(0xFE, 0xFFFFD508, 0x0, 0xFFFFEA84, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B7B9)
    Sleep(200)

    def lambda_B7D6():
        OP_96(0xFE, 0xFFFFD828, 0x0, 0xFFFFE764, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B7D6)
    Sleep(200)

    def lambda_B7F3():
        OP_96(0xFE, 0xFFFFDECC, 0x0, 0xFFFFE958, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B7F3)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0307
    ChrTalk(
        0x101,
        "#0002F#11P……哈哈……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)

    #C0308
    ChrTalk(
        0x102,
        (
            "#12P#0106F呜……\x01",
            "……真是太好了……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 1)

    #C0309
    ChrTalk(
        0x103,
        "#12P#0208F………是呀…………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)

    #C0310
    ChrTalk(
        0x104,
        (
            "#0302F哈哈……\x01",
            "还真是相当感人啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)
    Sleep(300)

    #C0311
    ChrTalk(
        0x108,
        (
            "#0910F#5P……各位……\x02\x03",

            "#0911F谢谢……\x01",
            "真是不知该如何……\x02\x03",

            "#0904F……如何\x01",
            "感谢你们才好……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#0004F#11P不……\x01",
            "我们也只是帮了一点忙而已。\x02\x03",

            "你们是靠自己的努力……\x01",
            "才迎来了这样的结果。\x02\x03",

            "#0002F──约修亚，\x01",
            "就让我说声恭喜你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x108,
        "#0911F#5P……谢谢你，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵……\x01",
            "突然好想快点见到\x01",
            "琪雅的小脸呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        (
            "#12P#0204F是呀……\x01",
            "还有蔡特和科长……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，那我们还等什么，\x01",
            "赶快回去吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#0002F#11P嗯……\x02",
    )

    CloseMessageWindow()
    OP_68(-8860, 1000, -4920, 1500)
    MoveCamera(51, 17, 0, 1500)

    def lambda_BA8D():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BA8D)
    Sleep(250)

    def lambda_BA9D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BA9D)

    def lambda_BAAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BAAA)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    OP_6F(0x1)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x2F)
    SetChrSubChip(0x101, 0x4)
    Sleep(130)
    SetChrSubChip(0x101, 0x3)
    Sleep(130)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)

    #C0318
    ChrTalk(
        0x101,
        "#5P#0004F──特别任务支援科，准备撤退。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x3)
    Sleep(130)
    SetChrSubChip(0x101, 0x4)
    Sleep(300)

    #C0319
    ChrTalk(
        0x101,
        (
            "#5P#0000F保护好被囚禁的人们，\x01",
            "拘捕黑手党成员，\x01",
            "返回地上吧……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_24(0x3A2)
    OP_24(0x3DA)
    Return()

    # Function_32_98FB end

    def Function_33_BB92(): pass

    label("Function_33_BB92")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BBB6")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_33_BB92")

    label("loc_BBB6")

    Return()

    # Function_33_BB92 end

    def Function_34_BBB7(): pass

    label("Function_34_BBB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BC01")
    PlayEffect(0x1, 0xFF, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    Jump("Function_34_BBB7")

    label("loc_BC01")

    Return()

    # Function_34_BBB7 end

    def Function_35_BC02(): pass

    label("Function_35_BC02")

    OP_77(0x0, 0x3E8)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x5A, 0x64, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x0)
    Return()

    # Function_35_BC02 end

    def Function_36_BC2A(): pass

    label("Function_36_BC2A")

    OP_77(0x1, 0x12C)

    def lambda_BC33():
        OP_96(0xFE, 0xFFFFE0C0, 0xFFFFFC18, 0x708, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BC33)
    OP_71(0x1, 0x1A5, 0x1CC, 0x0, 0x0)
    Sleep(500)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    Sleep(1200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    OP_79(0x1)
    OP_71(0x1, 0x1A5, 0x1CC, 0x0, 0x0)
    Sleep(500)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    Sleep(1200)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sound(944, 0, 80, 0)
    OP_79(0x1)
    WaitChrThread(0xE, 1)
    Return()

    # Function_36_BC2A end

    def Function_37_BCD3(): pass

    label("Function_37_BCD3")

    Sound(202, 0, 100, 0)
    Sound(977, 0, 100, 0)
    Sound(946, 0, 100, 0)
    OP_24(0x3A2)
    OP_24(0x3DA)
    Sleep(1000)
    Sound(969, 0, 100, 0)
    Sleep(1400)
    Sound(984, 0, 100, 0)
    Sleep(300)
    Sound(973, 0, 100, 0)
    Sound(985, 0, 100, 0)
    Return()

    # Function_37_BCD3 end

    def Function_38_BD0D(): pass

    label("Function_38_BD0D")

    Sound(987, 0, 100, 0)
    Sleep(1900)
    Sound(945, 0, 80, 0)
    Sleep(600)
    Sound(987, 0, 100, 0)
    Sleep(1600)
    Sound(945, 0, 80, 0)
    Sleep(400)
    Sound(987, 0, 100, 0)
    Sleep(1700)
    Sound(945, 0, 80, 0)
    Return()

    # Function_38_BD0D end

    def Function_39_BD41(): pass

    label("Function_39_BD41")

    Sound(930, 2, 0, 0)
    Sound(986, 2, 0, 0)
    Sleep(100)
    OP_25(0x3A2, 0xA)
    OP_25(0x3DA, 0xA)
    Sleep(100)
    OP_25(0x3A2, 0x14)
    OP_25(0x3DA, 0x14)
    Sleep(100)
    OP_25(0x3A2, 0x1E)
    OP_25(0x3DA, 0x1E)
    Sleep(100)
    OP_25(0x3A2, 0x28)
    OP_25(0x3DA, 0x28)
    Sleep(100)
    OP_25(0x3A2, 0x32)
    OP_25(0x3DA, 0x32)
    Sleep(100)
    OP_25(0x3A2, 0x3C)
    OP_25(0x3DA, 0x3C)
    Sleep(100)
    OP_25(0x3A2, 0x46)
    OP_25(0x3DA, 0x46)
    Sleep(100)
    OP_25(0x3A2, 0x50)
    OP_25(0x3DA, 0x50)
    Sleep(100)
    OP_25(0x3A2, 0x5A)
    OP_25(0x3DA, 0x5A)
    Sleep(100)
    OP_25(0x3A2, 0x64)
    OP_25(0x3DA, 0x64)
    Return()

    # Function_39_BD41 end

    SaveToFile()

Try(main)
