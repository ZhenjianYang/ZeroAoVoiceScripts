from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ヨアヒム司祭",           # 1
        "アグエルゴーレム",       # 2
        "アグエルゴーレム",       # 3
        "魔人ヨアヒム",           # 4
        "レン",                   # 5
        "ダミーヨアヒム",         # 6
        "パテルマテル",           # 7
        "杖",                     # 8
        "SE制御",                 # 9
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
        "Function_8_44A3",         # 08, 8
        "Function_9_44BE",         # 09, 9
        "Function_10_80AB",        # 0A, 10
        "Function_11_8234",        # 0B, 11
        "Function_12_8263",        # 0C, 12
        "Function_13_82A2",        # 0D, 13
        "Function_14_8307",        # 0E, 14
        "Function_15_834A",        # 0F, 15
        "Function_16_8364",        # 10, 16
        "Function_17_9CD9",        # 11, 17
        "Function_18_9D17",        # 12, 18
        "Function_19_9D69",        # 13, 19
        "Function_20_9DAC",        # 14, 20
        "Function_21_9DEF",        # 15, 21
        "Function_22_9E32",        # 16, 22
        "Function_23_9E75",        # 17, 23
        "Function_24_9EB8",        # 18, 24
        "Function_25_9F19",        # 19, 25
        "Function_26_9F75",        # 1A, 26
        "Function_27_9FD1",        # 1B, 27
        "Function_28_A02D",        # 1C, 28
        "Function_29_A089",        # 1D, 29
        "Function_30_A0E5",        # 1E, 30
        "Function_31_A10A",        # 1F, 31
        "Function_32_A12F",        # 20, 32
        "Function_33_C60C",        # 21, 33
        "Function_34_C631",        # 22, 34
        "Function_35_C67C",        # 23, 35
        "Function_36_C6A4",        # 24, 36
        "Function_37_C74D",        # 25, 37
        "Function_38_C787",        # 26, 38
        "Function_39_C7BB",        # 27, 39
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
        "#6P#0013Fここは……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x2D, 0x1F4)

    #C0002
    ChrTalk(
        0x102,
        "#0108F#6P……地下の湖……？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)

    #C0003
    ChrTalk(
        0x104,
        (
            "#6P#0301Fこんなモンが\x01",
            "広がってたのかよ……\x02",
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
        "#6P#0207F皆さん、あれ……！\x02",
    )

    CloseMessageWindow()

    def lambda_B2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2A)

    def lambda_B37():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B37)
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
            "#0307F#2Pキー坊の写真に\x01",
            "映っていた……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0101F#2Pこの場所で撮られた\x01",
            "ものだったのね……\x02",
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
            "……なんかね、\x01",
            "暗くてでっかい場所が\x01",
            "アタマの中に浮かんできた。\x02\x03",

            "上の方がぼんやり光ってて\x01",
            "キレイだけど、ちょっとコワイ感じ。\x02",
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
            "#0003F#2Pそうか……\x01",
            "あれはこの場所の事だったのか。\x02",
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
        "男の声",
        "#2Pフフ……その通りさ。\x02",
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
        "#0013F#11Pヨアヒム・ギュンター……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x107,
        "#0801F#5Pい、いつの前に……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x108,
        (
            "#0901F#5P……どうやら本当に\x01",
            "只者じゃなさそうだね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x4)
    OP_68(17800, 7500, -8000, 1500)
    MoveCamera(56, 10, 0, 1500)

    def lambda_E89():
        OP_95(0xFE, 17800, 7000, -8000, 1400, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E89)
    WaitChrThread(0x8, 1)
    OP_6F(0x41)
    OP_6B(0xD)

    def lambda_EAC():
        OP_95(0xFE, -2700, -5000, -8000, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EAC)

    def lambda_EC6():
        OP_95(0xFE, -2700, 0, -8000, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EC6)
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
            "#40A#30W──ようこそ。\x01",
            "我らの起源にして聖地へ。\x02\x03",

            "#50A特務支援課の諸君、\x01",
            "そして遊撃士協会のお客人……\x02\x03",

            "#13A歓迎させてもらうよ。\x02",
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

    def lambda_10F0():
        OP_95(0xFE, -3000, 0, -8000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_10F0)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    def lambda_1114():
        OP_95(0xFE, -9500, 0, -8000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1114)
    Sleep(5)

    def lambda_1131():
        OP_96(0xFE, 0xFFFFD7C4, 0x0, 0xFFFFE570, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1131)
    Sleep(5)

    def lambda_114E():
        OP_96(0xFE, 0xFFFFD508, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_114E)

    def lambda_1168():
        OP_95(0xFE, -8500, 0, -4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1168)
    Sleep(5)

    def lambda_1185():
        OP_96(0xFE, 0xFFFFD24C, 0x0, 0xFFFFDE04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1185)

    def lambda_119F():
        OP_95(0xFE, -10200, 0, -4700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_119F)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x104, 1)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x107, 1)

    def lambda_11DA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_11DA)
    WaitChrThread(0x108, 1)
    Sound(804, 0, 100, 0)
    Sound(540, 0, 70, 0)

    def lambda_11F7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_11F7)
    WaitChrThread(0x8, 1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x103,
        "#6P#0208F#Nっ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0015
    ChrTalk(
        0x102,
        "#0101F#6P……あなたは……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#6P#0301F随分と余裕じゃねぇか……\x02",
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

    def lambda_12BA():
        OP_95(0xFE, -9200, 0, -8000, 800, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12BA)
    WaitChrThread(0x101, 1)
    Sound(31, 0, 100, 0)
    OP_6F(0x1)

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F#6P──ヨアヒム・ギュンター。\x01",
            "単刀直入に行かせてもらう。\x02\x03",

            "#0001F《グノーシス》を投与して\x01",
            "操っている人々を今すぐ解放しろ。\x02\x03",

            "どんな方法かは知らないが……\x01",
            "あんたが操ってるのは判っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#6705F#11Pああ、別に構わないよ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0011F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#6704F#11PＩＢＣビルでも言っただろう。\x02\x03",

            "#6714F──キーア様を引き渡せば\x01",
            "いくらでも手を引こうと。\x02",
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
        "#0007F#6Pふ、ふざけるな……ッ！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        "#0110F#6Pまだそんな世迷言を……！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        "#0307F#6Pてめぇ……喧嘩売ってんのか？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#6P#0211F#N……最低の犯罪者ですね。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0026
    ChrTalk(
        0x107,
        (
            "#0808F（なにコイツ……\x01",
            "  教授並みに性格が悪そうね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x108,
        (
            "#0906F（ワイスマンはここまで\x01",
            "  狂気じみてはいなかったけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0028
    ChrTalk(
        0x8,
        (
            "#6703F#11Pやれやれ……\x01",
            "これでは話にならないな。\x02\x03",

            "そもそもキーア様は\x01",
            "我らが教団の崇める御子──\x02\x03",

            "#6701Fそれを返せというのが\x01",
            "どうして理不尽なんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#0010F#6P自分たちが６年前、\x01",
            "どんな事をやったと思っている！\x02\x03",

            "そんな連中にキーアを\x01",
            "引き渡せるわけがないだろうが！\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#0107F#6Pそれよりも……\x01",
            "いい加減、キーアちゃんの\x01",
            "素性を明らかにしなさい！\x02\x03",

            "ちゃんと身元は\x01",
            "判っているのでしょう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#6702F#11Pクク……なるほど。\x02\x03",

            "#6704F──君たちはまだ、\x01",
            "キーア様がこの時代の\x01",
            "生まれだと思っているのか。\x02",
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
        "#6P#0201F#Nこ、この時代……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0034
    ChrTalk(
        0x8,
        (
            "#6704F#11Pフフ、いいだろう。\x02\x03",

            "#6700F《叡智》に至らぬ者に話すのは\x01",
            "本来禁じられているが……\x02\x03",

            "君たちには特別に教えてあげよう。\x02",
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
            "#6704F#11Pつい一月前まで\x01",
            "キーア様は眠っておられた──\x02\x03",

            "この祭壇の聖なる揺りかごで\x01",
            "まどろむように……\x02\x03",

            "#6714F５００年以上にも及ぶ、\x01",
            "永き眠りに就かれていたのさ！\x02",
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
        "#0107Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#0207F……ま、まさか……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0310Fてめえ……\x01",
            "フカシてんじゃねえぞ！？\x02",
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
            "#6702F#11Pフフ、別にそんな\x01",
            "驚くことも無いだろう？\x02\x03",

            "#6704F現代の技術では不可能でも\x01",
            "古の技術ならばそれが可能──\x02\x03",

            "……５００年前、\x01",
            "アーティファクトを研究していた\x01",
            "錬金術師の集団がこの地にあった。\x02\x03",

            "#6700Fこの祭壇は彼らの技術を元に\x01",
            "造られたと伝えられている。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 200, -1, -1)

    #A0041
    AnonymousTalk(
        0x108,
        (
            "#0901F《星見の塔》を建造した\x01",
            "中世の錬金術師たち……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0042
    AnonymousTalk(
        0x107,
        (
            "#0806Fそ、そんな繋がりが\x01",
            "あったなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0043
    ChrTalk(
        0x8,
        (
            "#6704F#11P以来、キーア様は５００年もの\x01",
            "永き眠りに就かれていた……\x02\x03",

            "当然、その素性を知る者は\x01",
            "我が教団にすら残っていない。\x02\x03",

            "#6700F……つまりはそういう事さ。\x02",
        )
    )

    CloseMessageWindow()

    #A0044
    AnonymousTalk(
        0x101,
        "#0008F……そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0045
    AnonymousTalk(
        0x104,
        "#0306F何てこった……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0046
    AnonymousTalk(
        0x102,
        (
            "#0108F……キーアちゃんの過去……\x01",
            "取り戻してあげられると思ったのに……\x02",
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
            "#6704F#11Pフフ……\x01",
            "何を哀しむことがあるんだい？\x02\x03",

            "キーア様に過去など不要……\x02\x03",

            "#6713Fなぜなら彼女はこれより、\x01",
            "真の《神》になるのだから──！\x02",
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
        "#0007Fなっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0050
    AnonymousTalk(
        0x107,
        "#0801Fか、神って……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0051
    ChrTalk(
        0x8,
        (
            "#6714F#11Pハハハ、文字通りの意味さ！\x02\x03",

            "君たちはいい加減、\x01",
            "真実に気付くべきなんだよ！\x02\x03",

            "《空の女神》エイドス！？\x01",
            "そんなものが何処にいる！？\x02\x03",

            "全ては七耀教会による\x01",
            "まやかしだと何故気付かない！？\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0x104,
        "#0310Fしょ、正気かよ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0053
    AnonymousTalk(
        0x102,
        (
            "#0101Fめ、女神の存在を\x01",
            "疑う人がいるなんて……\x02",
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
            "#6702F#11Pクク、だがそれが\x01",
            "我が《Ｄ∴Ｇ教団》の説く真理だ。\x02\x03",

            "#6704Fよく誤解されるのだが……\x01",
            "我々は別に、悪魔という存在を\x01",
            "崇拝しているわけではない。\x02\x03",

            "ただ、女神という概念を\x01",
            "否定するために好都合だから\x01",
            "概念的に利用しているにすぎない。\x02\x03",

            "#6700F毒をもって毒を制す……\x01",
            "つまりはそういう事だよ。\x02",
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
        "#5P#0207F#4Sふ、ふざけないで……！\x02",
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

    def lambda_22CF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_22CF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_22E4():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_22E4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)

    def lambda_22F9():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_22F9)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)

    def lambda_230E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_230E)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)

    def lambda_2323():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2323)
    Sound(808, 0, 80, 0)
    Sound(531, 0, 80, 0)
    Sleep(500)

    #C0056
    ChrTalk(
        0x103,
        (
            "#5P#0208F#30Wだったらどうして\x01",
            "あんな酷いことを……！\x02\x03",

            "#0210F#40W……みんな……\x01",
            "みんな泣き叫んでいた……！\x02\x03",

            "わたしがいたロッジはそれでも\x01",
            "マシだったと聞いている……！\x02\x03",

            "悪魔なんて崇拝してもいないのに\x01",
            "……どうしてそんな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#11P#0008Fティオ……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#11P#0308F……ティオすけ……\x02",
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
            "#6702F#11Pクク……ティオ・プラトー。\x01",
            "君の名前は覚えているよ。\x02\x03",

            "#6704Fアルタイル・ロッジで\x01",
            "素晴らしい感応力を示した検体……\x02\x03",

            "いやはや、まさかこんな形で\x01",
            "検体本人に会うことになるとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x103,
        "#6P#0208F#N………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_25CE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25CE)
    Sleep(50)

    def lambda_25DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_25DE)
    Sleep(50)

    def lambda_25EE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_25EE)
    Sleep(50)

    def lambda_25FE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_25FE)
    Sleep(50)

    def lambda_260E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_260E)

    #C0061
    ChrTalk(
        0x101,
        (
            "#0006F#6P……丁度いい。\x01",
            "改めて話してもらおうか……\x02\x03",

            "#0013F大陸各地のロッジで行っていた　\x01",
            "数々の非道な儀式の目的を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#6705F#11Pおや、まだ判らないのかね？\x02\x03",

            "#6704F全ては《グノーシス》の完成度を\x01",
            "高めるための実験だったのさ。\x02\x03",

            "人が極限状態の時に示す\x01",
            "想念の強さや潜在能力の開花……\x02\x03",

            "#6700Fそれが《グノーシス》の完成度を\x01",
            "高める恰好のデータだったわけだ。\x02",
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
            "#6714F#11Pちなみに子供が多かった理由は\x01",
            "単にデータサンプルの精度の問題さ。\x02\x03",

            "思春期を迎える前の\x01",
            "幼く無垢な検体の方が色々と──\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0065
    ChrTalk(
        0x103,
        "#6P#0210F#N……っ……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0066
    ChrTalk(
        0x101,
        "#0007F#6Pやめろ……！\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0110F#6Pいい加減にしなさい！\x01",
            "この人でなし……！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#3P#0311F#6P……まさか“俺ら”以上の\x01",
            "外道がいるとはな……\x02",
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

    def lambda_296D():
        OP_96(0xFE, 0xFFFFDD3C, 0x0, 0xFFFFEC78, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_296D)
    WaitChrThread(0x108, 1)
    Sleep(300)

    #C0069
    ChrTalk(
        0x108,
        (
            "#0903F#11P──ヨアヒム・ギュンター。\x02\x03",

            "#0901F察するに、あなたはそうした\x01",
            "数々の実験を統括していた\x01",
            "責任者だったみたいだね……？\x02",
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
            "#6P#6702F#Nフフ、その通りだ。\x02\x03",

            "#6704Fだからといって教団内の\x01",
            "位階が高いわけではない。\x02\x03",

            "そもそも我が教団は\x01",
            "真なる神の元、平等の──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0071
    ChrTalk(
        0x107,
        (
            "#0806F#11Pあんたたちの教義なんて\x01",
            "正直、どうでもいいわ。\x02\x03",

            "#0808F──それより、\x01",
            "だったら知ってるはずよね？\x02\x03",

            "#0801F《楽園》と呼ばれていた\x01",
            "風変わりなロッジのことを……\x02",
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

    def lambda_2BE4():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BE4)
    Sleep(50)

    def lambda_2BF4():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BF4)
    Sleep(50)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)

    def lambda_2C0C():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C0C)
    Sleep(50)

    def lambda_2C1C():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C1C)
    Sleep(300)

    #C0072
    ChrTalk(
        0x101,
        "#0005F#5Pその名前は……！？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#5P#0101Fあの黒いファイルにあった……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#6P#6705F#Nほう……\x01",
            "その存在を知っているのか？\x02\x03",

            "#6704Fあれは教団の有力者が\x01",
            "わざわざ作らせたロッジでね。\x02\x03",

            "各地の有力者を取り込み、\x01",
            "弱味を握って教団の手づるとする。\x02\x03",

            "#6700F正直、僕が考えていた実験の趣旨から\x01",
            "かけ離れてしまったロッジだったよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0075
    ChrTalk(
        0x107,
        "#0808F#11P……やっぱり……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x108,
        "#0908F#11P……推測通りだったか……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0077
    ChrTalk(
        0x101,
        (
            "#0003F#5Pなるほど……そういう事か……\x02\x03",

            "#0013Fその《楽園》とやらに引き込んで\x01",
            "議長の弱味を握ったんだな！？\x02",
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

    def lambda_2E7F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E7F)

    def lambda_2E8C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2E8C)

    def lambda_2E99():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E99)
    WaitChrThread(0x102, 1)

    #C0078
    ChrTalk(
        0x102,
        "#11P#0107Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        "#5P#0307Fそう繋がんのかよ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(150)

    #C0080
    ChrTalk(
        0x8,
        (
            "#6P#6702F#Nフフ、僕は全てのロッジの\x01",
            "実験結果に目を通していたからね。\x02\x03",

            "#6704F６年前の、あの忌々しい作戦で\x01",
            "殆んどのロッジが失われた後……\x02\x03",

            "丁度いい後ろ盾を\x01",
            "手に入れることが出来たわけだ。\x02\x03",

            "#6712F《ルバーチェ》なんていう、\x01",
            "便利な手足のオマケ付きでね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0006F#5Pやっぱりか……\x02\x03",

            "#0013F警備隊を操れているのも\x01",
            "そのあたりの関係だな……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3045():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3045)

    def lambda_3052():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3052)

    def lambda_305F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_305F)
    WaitChrThread(0x102, 1)

    #C0082
    ChrTalk(
        0x102,
        "#11P#0108Fそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#5P#0301Fどうやって《グノーシス》を\x01",
            "連中に服用させやがったんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#6P#6702F#Nああ、議長の子飼いである\x01",
            "警備隊司令に強引に回させたのさ。\x02\x03",

            "ウルスラ病院で開発された\x01",
            "画期的な栄養剤という触れ込みでね。\x02\x03",

            "#6709Fクク、まさかこんなにあっさりと\x01",
            "信じるとは思わなかったが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0085
    ChrTalk(
        0x101,
        "#0008F#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#5P#0310F阿呆司令が……\x01",
            "さすがに迂闊すぎんだろ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x8,
        (
            "#6P#6704F#N──《楽園》に話を戻すが\x01",
            "あれは妙な終わり方をしたようだな。\x02\x03",

            "どうやら例の作戦とは別に、\x01",
            "去年リベールで異変を起こした\x01",
            "《結社》とやらに潰されたようだが……\x02\x03",

            "#6700Fやれやれ、何のつもりだったのやら。\x02",
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
            "#6P#6703F#Nああ、しかし《楽園》には\x01",
            "一つだけ大きな心残りがあったな。\x02\x03",

            "天才的な適応力を持つ、\x01",
            "一人の幼い検体がいたんだが……\x02\x03",

            "#6713Fこれがまた傑作でね！\x02\x03",

            "周囲にいた別の検体の人格を\x01",
            "《グノーシス》投与をきっかけに\x01",
            "自分のものとして取り込んだのさ！\x02\x03",

            "#6709Fいや、その実験データだけでも\x01",
            "せめて回収できていれば──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0091
    ChrTalk(
        0x107,
        (
            "#0803F#11P──もういいわ。\x02\x03",

            "#0801F知りたいことは全部判った。\x01",
            "もう、それ以上話す必要はない。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x108,
        (
            "#0908F#11P……ごめん、ロイド。\x01",
            "少し出しゃばったみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        (
            "#0004F#5Pいや、おかげでこちらも\x01",
            "かなり整理できた気がする。\x02\x03",

            "#0000F──これで心置きなく\x01",
            "逮捕に踏み切れそうだ。\x02",
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

    def lambda_35E1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_35E1)
    SetCameraDistance(16000, 700)

    def lambda_35F7():
        OP_95(0xFE, -9000, 0, -8000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35F7)
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
            "#0003F#5P──《Ｄ∴Ｇ教団》幹部司祭、\x01",
            "ヨアヒム・ギュンター。\x02\x03",

            "#0007F自治州法に基づき、傷害、騒乱、\x01",
            "不法占拠、薬物使用、虐待など\x01",
            "数多の容疑で逮捕する……！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#2P#0107F#11P略式ではあるけど、捜査令状、\x01",
            "および逮捕状も既に出ているわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x104,
        "#5P#0307F大人しくお縄に付いてもらおうか！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "#6P#6704F──フフ、いいだろう。\x02\x03",

            "#6700F僕と君たちのどちらが\x01",
            "目的を達せられるのか……\x02\x03",

            "ここは一つ、\x01",
            "賭けをしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0xD, 0x32)
    SetChrSubChip(0xD, 0x1)
    SetChrPos(0xD, -3000, 0, -8000, 270)
    Sound(804, 0, 100, 0)

    def lambda_37F3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_37F3)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, -3000, 2500, -8000, 0)
    SetChrFlags(0xF, 0x8000)

    def lambda_3831():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_3831)
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

    def lambda_391F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_391F)

    def lambda_3930():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3930)
    MoveCamera(90, 33, 0, 9000)
    SetCameraDistance(15000, 9000)
    Sleep(3000)
    StopEffect(0x0, 0x2)
    PlayEffect(0x3, 0xFF, 0xF, 0x40, 0, 150, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(969, 0, 100, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_39A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_39A1)
    Sound(202, 0, 100, 0)
    OP_6F(0x79)

    def lambda_39BA():
        OP_96(0xFE, 0xFFFFF448, 0x5DC, 0xFFFFE0C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_39BA)
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

    def lambda_3AF8():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AF8)
    Sleep(10)

    def lambda_3B15():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B15)
    Sleep(10)

    def lambda_3B32():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B32)

    def lambda_3B4C():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3B4C)
    Sleep(10)

    def lambda_3B69():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B69)

    def lambda_3B83():
        OP_98(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3B83)
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
        "#0101F#6Pそ、その髪は……！？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x103,
        "#0201F#12Pしかも魔導杖の一種ですか……\x02",
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
            "フフ、僕の髪は\x01",
            "こちらの方が地の色でね……\x02\x03",

            "《グノーシス》を投与し続けて\x01",
            "少々風変わりな体質になったんだ。\x02\x03",

            "何せここ数年、まったく睡眠を\x01",
            "取っていないくらいだからねぇ。\x07\x00\x02",
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
            "#0310F#12P#Nおいおい……\x01",
            "シャレになってねぇぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0102
    ChrTalk(
        0x101,
        (
            "#6P#0008Fなるほど……\x01",
            "それで病院勤めをしながら\x01",
            "ここまでする時間が取れたのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5Pフフ、さすがは捜査官。\x01",
            "いい所に気付くじゃないか。\x02\x03",

            "#6800F──ちなみにこの杖は\x01",
            "例の錬金術師たちが造り上げた\x01",
            "魔導具の最高傑作の一つさ。\x02\x03",

            "古代遺物#8Rアーティファクト#すら凌駕する\x01",
            "力を秘めていてね……\x02",
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

    def lambda_400E():
        OP_96(0xFE, 0xFFFFF128, 0x0, 0xFFFFD5D0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_400E)

    def lambda_4028():
        OP_96(0xFE, 0xFFFFF128, 0x0, 0xFFFFEBB0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4028)

    def lambda_4042():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4042)

    def lambda_4053():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4053)
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
            "#6813F#11Pこんなものまで\x01",
            "使役できるくらいさ……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(0, 200, -1, -1)

    #A0105
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010Fくっ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0106
    AnonymousTalk(
        0x107,
        "#0807Fこれって……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0107
    AnonymousTalk(
        0x108,
        (
            "#0901F錬金術を駆使して造られた\x01",
            "中世の人形兵器#8Rオーバーマペット#か……！\x02",
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
            "#6804F#5Pさて、そろそろ\x01",
            "幕切れとさせてもらうよ。\x02\x03",

            "多分、今日という日は\x01",
            "記念すべき一日になるだろう……\x02\x03",

            "#6814Fキーア様が《神》となって\x01",
            "我らが悲願が達せられる日にね！\x02",
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
            "#6P#0007F痴#2Rし#れ言を……！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        (
            "#0207F#12Pあなたなんかに……\x01",
            "……絶対に負けない……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 415)
    BlurSwitch(0x19F, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_43C1():
        OP_95(0xFE, -2000, 0, -8000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43C1)
    Sleep(5)

    def lambda_43DE():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFE4A8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43DE)
    Sleep(5)

    def lambda_43FB():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43FB)

    def lambda_4415():
        OP_95(0xFE, -2000, 0, -7000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4415)
    Sleep(5)

    def lambda_4432():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFDCD8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4432)

    def lambda_444C():
        OP_95(0xFE, -2000, 0, -7000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_444C)
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

    def Function_8_44A3(): pass

    label("Function_8_44A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44BD")
    OP_A1(0x8, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_8_44A3")

    label("loc_44BD")

    Return()

    # Function_8_44A3 end

    def Function_9_44BE(): pass

    label("Function_9_44BE")

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
        "#0007F#6P……よし……！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#3P#0300Fハッ……\x01",
            "賭けは俺たちの勝ちだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x102,
        "#0107F#6P大人しく投降しなさい……！\x02",
    )

    CloseMessageWindow()

    def lambda_4898():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4898)
    WaitChrThread(0x8, 2)

    #C0114
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#11P#40Wクク……やれやれ。\x02\x03",

            "#6802F……一つ教えてあげよう……\x02\x03",

            "知っての通り《グノーシス》の効能は\x01",
            "単純な身体能力の強化などではない……\x02\x03",

            "感応力の強化、引いては服用者の\x01",
            "潜在能力を引き出すものだが……\x02\x03",

            "#6814Fその使い方を極めれば\x01",
            "……こんな事もできるのさ……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_49C2():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_49C2)
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

    def lambda_4D69():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D69)

    #C0115
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010Fな……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4D9A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4D9A)

    #C0116
    ChrTalk(
        0x104,
        "#11P#0307Fなんだコイツは！？\x02",
    )

    CloseMessageWindow()

    def lambda_4DD5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4DD5)

    #C0117
    ChrTalk(
        0x103,
        (
            "#11P#0208Fく、空間が……\x01",
            "呪縛されている……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E23():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4E23)

    #C0118
    ChrTalk(
        0x107,
        (
            "#0813F#5Pこ、これって……\x01",
            "ワイスマンの《魔眼》……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E78():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4E78)

    #C0119
    ChrTalk(
        0x108,
        "#0907F#5P馬鹿な……どうやって！？\x02",
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
            "#6802F#5Pクク──そちらの２人は随分と\x01",
            "興味深い体験をしているようだね。\x02\x03",

            "#6804F《リベル＝アーク》に\x01",
            "《影の国#6Rファンタズマ#》か……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_4FA0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_4FA0)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0x107, 0x2)
    OP_0D()

    #C0121
    ChrTalk(
        0x107,
        (
            "#0807F#6P#Nこいつ……\x01",
            "あたしたちの記憶を！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FF8():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4FF8)
    Sleep(250)
    Fade(250)
    SetChrSubChip(0x108, 0x2)
    OP_0D()

    #C0122
    ChrTalk(
        0x108,
        (
            "#0907F#6P#Nまさか……\x01",
            "そこから再現したのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0123
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6805F#5Pワイスマン……\x01",
            "ほう、これはなかなか\x01",
            "共感を覚える人物のようだ。\x02\x03",

            "#6800F《身喰らう蛇》の情報も\x01",
            "思っていた以上に興味深い……\x02\x03",

            "#6809Fフフ……\x01",
            "なかなか愉しませてくれそうだ。\x02",
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
        "#0801F#6P#Nくっ……こんなヤツに……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0126
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5Pクク……賭けは僕の勝ちだ。\x02\x03",

            "#6800F──さっそく君たちには\x01",
            "《グノーシス》を飲んでもらうよ？\x02\x03",

            "そうすれば\x01",
            "君たちは僕の思うがまま……\x02\x03",

            "キーア様も納得して\x01",
            "お戻りになって頂けるだろう。\x02",
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

    def lambda_52BB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_52BB)
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
            "#0310F#12P#Nてめえ……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5305():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5305)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x102, 0x35)
    SetChrSubChip(0x102, 0x0)
    OP_0D()

    #C0128
    ChrTalk(
        0x102,
        (
            "#0110F#6P#Nそ、それが狙いで\x01",
            "私たちをここまで……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0129
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#5Pクク、君たちのような愚物に\x01",
            "どうしてわざわざ面会の時間を\x01",
            "割#2Rさ#いたと思っている？\x02\x03",

            "#6814F全てはキーア様のため……\x02\x03",

            "それ以外の理由が\x01",
            "どこにあるというんだい！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_541A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_541A)
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
            "#6P#0201F#12P#N……あ、あなたは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    def lambda_5487():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5487)
    Fade(250)
    SetChrChipByIndex(0x101, 0x34)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0131
    ChrTalk(
        0x101,
        (
            "#0006F#6P#N……そこまでの力を\x01",
            "手に入れておきながら……\x02\x03",

            "#0008Fその上、キーアに拘る理由が\x01",
            "一体どこにあるんだ……？\x02",
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
            "#6805F#5Pほう……？\x02",
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

    def lambda_55A0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55A0)
    Sleep(500)

    #C0133
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#6P#N彼女が本当に５００年前の\x01",
            "時代の出身だったとしても……\x02\x03",

            "あくまで普通の女の子であるのは\x01",
            "変わらないんじゃないのか……？\x02\x03",

            "#0001Fそれだけの力を手に入れながら\x01",
            "どうしてキーアに拘る……？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0134
    ChrTalk(
        0x102,
        "#0108F#6P#Nた、確かに……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0135
    ChrTalk(
        0x108,
        "#0908F#6P#N根本的な疑問だね……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0136
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6813F#11Pクク、言っただろう。\x01",
            "彼女は《神》となる御方……\x02\x03",

            "キーア様の前には、この力など\x01",
            "比較するのもおこがましいだろう。\x02\x03",

            "#6809Fいや、クク……\x01",
            "そもそも比較すること自体、\x01",
            "意味が無いとも言えるのかな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        "#0310F#6P#Nワケの判らねぇことを……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0138
    ChrTalk(
        0x107,
        (
            "#0806F#6P#N本当に……\x01",
            "誰かさんにソックリだわ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0003F#6P#Nまあいい……\x01",
            "この際だから聞いておく。\x02\x03",

            "#0001F──どうしてキーアは\x01",
            "競売会の場にいたんだ？\x02",
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
            "#0108F#6P#N確かにそれも……\x01",
            "まだ判っていないわね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0142
    ChrTalk(
        0x103,
        (
            "#6P#0201F#6P#Nマフィアの方でも……\x01",
            "心当たりが無いそうですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0143
    ChrTalk(
        0x101,
        (
            "#0006F#6P#N……続けて聞くぞ。\x02\x03",

            "#0013F俺の兄──ガイ・バニングスを\x01",
            "殺したのはあんたか……？\x02",
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
            "#6805F#11Pほほう……\x01",
            "そうか、そうだったのか！\x02\x03",

            "#6800Fなるほど……２人きりの兄弟……\x01",
            "歳の差は１０近く……\x02\x03",

            "兄の殉職後はクロスベルを離れ、\x01",
            "再び戻ってきたというわけか……\x02\x03",

            "#6809Fはは──これは傑作だ！\x02\x03",

            "まさか君があの厄介な男の\x01",
            "弟だったとは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F#6P#N……それは肯定の言葉と\x01",
            "受け取っていいのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0146
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6804F#11Pフフ、確かに当時、\x01",
            "彼は僕の存在に迫っていた。\x02\x03",

            "#6800F厄介だからルバーチェに頼んで\x01",
            "抹殺するよう依頼したんだが……\x02\x03",

            "どうやら殺したのは\x01",
            "全く別の勢力だったようだな。\x02\x03",

            "#6804F３年前、マルコーニは\x01",
            "さも自分たちの手柄のように\x01",
            "僕に恩を着せてきたが……\x02\x03",

            "ガルシアの方は否定していたから\x01",
            "その可能性は無いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F#6P#Nなるほど……だろうと思ったよ。\x02\x03",

            "#0000F──あんたみたいな男に\x01",
            "兄貴が負けるとは思えないからな。\x02",
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

            "#6800Fほう……\x01",
            "面白い事を言うじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#6P#Nキーアが競売会の場にいた経緯……\x02\x03",

            "多分それも、あんたにとっては\x01",
            "想定外の出来事だったはずだ……\x02\x03",

            "#0001F自らが《神》と崇める存在を\x01",
            "簡単に手放すわけがないからな……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0150
    ChrTalk(
        0x102,
        "#0101F#6P#N……確かに……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0151
    ChrTalk(
        0x103,
        "#6P#0203F#6P#N余りに非合理的ですね……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0152
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6811F#11P……くっ…………\x02\x03",

            "確かにあの日……\x01",
            "キーア様は永き眠りから\x01",
            "ようやくお目覚めになった……\x02\x03",

            "#6803Fだが、僕がそれを知った時には\x01",
            "この祭壇から居なくなっていた……\x02\x03",

            "……おそらくご自分で\x01",
            "地上に彷徨い出たと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#6P#Nそして偶然、出品予定だった\x01",
            "人形のトランクに入り込んだ……？\x02\x03",

            "#0006F──馬鹿げている。\x01",
            "そんな事がありえる訳がない。\x02\x03",

            "《黒月》にもたらされた情報もある。\x02\x03",

            "#0001Fつまり──今回の事件に関しては\x01",
            "黒幕であるあんたも知らないことが\x01",
            "少なくないという事だろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0154
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6811F#11Pぐっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0309F#6P#Nはは……良いツッコミだぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0156
    ChrTalk(
        0x107,
        "#0802F#6P#Nロイド君、凄い……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x108,
        "#0902F#6P#Nさすがは捜査官だね……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0158
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6807F#11Pだ、だからどうした！\x02\x03",

            "キーア様がお戻りになれば\x01",
            "そのような瑣末な疑問は──\x02",
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
            "#0002F#6P#N《真なる叡智#10Rグ ノ ー シ ス#》？\x01",
            "冗談も大概にしたらどうだ……？\x02\x03",

            "#0003Fあんたが今していることは、\x01",
            "誰かの記憶を盗み見て、\x01",
            "誰かの力を真似ただけだろう……\x02\x03",

            "あんたが非道な実験を元に\x01",
            "完成させた薬とやらも同じ……\x02\x03",

            "#0008F罪も無い子供たちを弄んで\x01",
            "愚かな試行錯誤を繰り返した挙句、\x01",
            "偶然見つけた結果でしかない……\x02\x03",

            "#0013Fそんなものが断じて\x01",
            "“叡智”であるものか……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0160
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6811F#5Pき、貴様……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0101F#6P#N確かに“叡智”というには\x01",
            "下劣すぎるかもしれないわね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0162
    ChrTalk(
        0x103,
        (
            "#6P#0211F#12P#N……卑しいと言っても\x01",
            "いいかと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0163
    ChrTalk(
        0x107,
        (
            "#0806F#6P#Nごめん、ワイスマンの方が\x01",
            "遥かにマシだったかも……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0164
    ChrTalk(
        0x108,
        "#0903F#6P#Nああ……僕も同感だ。\x02",
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

    def lambda_64A2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_64A2)
    Sleep(500)

    #C0165
    ChrTalk(
        0x101,
        (
            "#5P#0008F……そして今もなお……\x02\x03",

            "あんたはその下らない幻想を\x01",
            "キーアに押し付けようとしている。\x02\x03",

            "#0003Fあの陽だまりのように明るくて、\x01",
            "無邪気で天真爛漫で……\x02\x03",

            "#0010Fそして思いやりもある\x01",
            "俺たちの大切なあの子に……！\x02",
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
            "#5P#0007F#4S──そんな\x01",
            "馬鹿げた事をさせるものか！！\x02",
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
            "#11P#6810Fば、馬鹿な……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6723():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6723)
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
            "#0205F#5Pあ……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_676A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_676A)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0169
    ChrTalk(
        0x104,
        "#5P#0302F身体が動くぜ……！\x02",
    )

    CloseMessageWindow()

    def lambda_67BB():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_67BB)
    Sleep(250)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0170
    ChrTalk(
        0x102,
        "#5P#0102F呪縛が……解けた……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_6815():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_6815)
    Sleep(100)

    def lambda_6831():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_6831)
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
            "#5P#0904Fそうか……彼の《魔眼》は\x01",
            "所詮コピーしただけのもの……\x02\x03",

            "#0900F動揺すれば保てない程度の\x01",
            "不完全なものだったのか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x107,
        (
            "#11P#0809Fロイド君の気合いが\x01",
            "ブチ破ったってわけね……！\x02",
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
            "#5P#0013F──ヨアヒム・ギュンター。\x01",
            "あんたの器はもう見切った。\x02\x03",

            "この上、何をして来ようとも\x01",
            "俺たちは絶対に屈しない。\x02\x03",

            "#0007F大人しく投降してもらおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_6A16():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6A16)
    WaitChrThread(0x8, 2)
    Sleep(600)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    Sleep(300)

    def lambda_6A51():
        OP_9D(0xFE, 0xFFFFF254, 0x0, 0xFFFFE5D4, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6A51)

    def lambda_6A6E():
        OP_96(0xFE, 0xFFFFF510, 0x0, 0xFFFFE0C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6A6E)
    Sound(974, 0, 100, 0)
    WaitChrThread(0xF, 1)

    def lambda_6A92():
        OP_9D(0xFE, 0xFFFFF254, 0x0, 0xFFFFE7C8, 0x12C, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_6A92)
    WaitChrThread(0x8, 1)
    Sleep(300)

    def lambda_6AB6():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6AB6)
    WaitChrThread(0x8, 2)
    Sleep(600)

    #C0174
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#6803F#40Wハハ……参ったな……\x02\x03",

            "#2S#50W……これじゃあ……\x01",
            "しか……じゃないか………\x02",
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
            "#5P#0307Fハッ……\x01",
            "何をブツブツ言ってやがる！？\x02",
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
            "#11P#6814F#4Sヒハハ……！\x01",
            "これじゃあ切り札を使うしか\x01",
            "無くなったじゃないか！！\x02",
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
            "#0007F#6P#Nな……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0179
    ChrTalk(
        0x102,
        "#0107F#6P#Nそ、それは……\x02",
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
            "#6813Fクク……教えてあげよう。\x02\x03",

            "これぞ完成した《グノーシス》の\x01",
            "最終形とも呼べるもの……\x02\x03",

            "君たちが手に入れたものが\x01",
            "《蒼#2Rあお#の叡智》と言うならば……\x02\x03",

            "さしずめこれは《紅#2Rあか#の叡智》と\x01",
            "言ったところかな……？\x02",
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
            "#0201F#12P#Nも、もしかして……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0182
    ChrTalk(
        0x104,
        (
            "#0307F#12P#N秘書野郎とマフィアどもを\x01",
            "化物に変えた……！？\x02",
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
            "#5P#6809F#4Sははは──その通り！\x02",
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
            "#0010F#6P#Nしまった……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0185
    ChrTalk(
        0x108,
        "#0907F#6P#Nあんなに大量に服用したら……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x10, 2, 0, 15)
    SetChrChipByIndex(0x8, 0x2D)
    SetChrSubChip(0x8, 0x0)

    def lambda_70B6():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_70B6)
    Sleep(300)
    OP_68(-2050, 300, -8000, 1500)

    def lambda_70E3():
        OP_96(0xFE, 0xFFFFF63C, 0x0, 0xFFFFE0C0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_70E3)
    WaitChrThread(0x8, 1)

    def lambda_7101():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7101)
    Sleep(300)

    def lambda_711D():
        OP_96(0xFE, 0xFFFFF830, 0x0, 0xFFFFE0C0, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_711D)
    WaitChrThread(0x8, 1)

    def lambda_713B():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_713B)

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
            "#0807F#6P#Nと、とにかく\x01",
            "急いで吐かせないと……！\x02",
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
            "#11P#6805F#45A#60W視#2Rみ#える……視#2Rみ#えるぞ……！\x02\x03",

            "#65A#6814F#70W……大いなる《Ｄ》……\x01",
            "……失われた力の源が……！\x02",
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
            "#11P#5S#35Aヒャハハハハハハハハハハ！\x02",
        )
    )
    #Auto

    BlurSwitch(0x1194, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1500)

    def lambda_738B():
        OP_A6(0xFE, 0x0, 0x32, 0x1770, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_738B)
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
        "#0011F#6P#Nな……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0191
    ChrTalk(
        0x102,
        "#0105F#6P#N……こ、こんな……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0305F#12P#Nおいおい……\x01",
            "……冗談だろ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0193
    ChrTalk(
        0x103,
        "#0207F#12P#Nこ、この霊圧は……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0194
    ChrTalk(
        0x107,
        "#0813F#N#6Pヨ、ヨシュア……これって……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0195
    ChrTalk(
        0x108,
        (
            "#0903F#N#6Pああ……\x02\x03",

            "#0901Fもしかしたら至宝を取り込んだ\x01",
            "ワイスマンよりも……\x02",
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
            "#60Wアア……ココチヨイ……\x02",
        )
    )

    CloseMessageWindow()

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W今コソ我ハ……\x01",
            "総テノ真実ヘト至ッタ……\x02",
        )
    )

    CloseMessageWindow()

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W世界ノ在リ方……\x01",
            "……ソノ秘メラレタ意図モ……\x02",
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
            "#0010F#N#5Pくっ……気を確かに持て……！\x02\x03",

            "#0007Fそんなものはまやかしだ！\x01",
            "“真実”というのはそう単純に\x01",
            "掴めるものなんかじゃない……！\x02",
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
            "#60Wクク……\x01",
            "ソレハ単ニ人ノ身ノ限界……\x02",
        )
    )

    CloseMessageWindow()

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W我ニハ総テガ視エルノダ……\x02",
        )
    )

    CloseMessageWindow()

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wきーあ様ノ失踪ノカラクリ……\x01",
            "ソシテ貴様ノ兄ノ死ノ真相モ……\x02",
        )
    )

    CloseMessageWindow()

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wくろすべるノ地ニ課セラレタ\x01",
            "避ケラレヌ運命モ……\x02",
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
            "#0010F#5P#Nくっ……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0205
    ChrTalk(
        0x104,
        "#0307Fハッタリを#2P#N……！\x02",
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
            "#60Wモハヤ貴様ラヲ生カシテオク\x01",
            "意味モ無クナッタ……\x02",
        )
    )

    CloseMessageWindow()

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W至レヌ身ノ不運ヲ嘆キナガラ\x01",
            "ココデ果テルガヨイ……\x02",
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
            "#0206F#12P#N……秘書さんの魔人化とは\x01",
            "格が違うみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0209
    ChrTalk(
        0x104,
        (
            "#0303F#12P#Nああ、さすがにちょいと\x01",
            "戦力差がありすぎるな……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0210
    ChrTalk(
        0x102,
        (
            "#0101F#6P#Nでも、どうやら避けられる\x01",
            "戦いでは無いみたいね……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0211
    ChrTalk(
        0x101,
        (
            "#0003F#6P#Nああ……覚悟を決めよう。\x02\x03",

            "#0013F──エリィ、ティオ、ランディ。\x02\x03",

            "それから、エステルにヨシュア。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x96, 0x0, 0xBB8, 0x190)

    #C0212
    ChrTalk(
        0x101,
        (
            "#0007F#6P#Nこれが最後の戦いだ──\x01",
            "みんなの全力を貸してくれ！！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("メンバーたち")
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
            "#5Sおおっ！\x02",
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

    # Function_9_44BE end

    def Function_10_80AB(): pass

    label("Function_10_80AB")

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

    # Function_10_80AB end

    def Function_11_8234(): pass

    label("Function_11_8234")


    def lambda_8239():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8239)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Return()

    # Function_11_8234 end

    def Function_12_8263(): pass

    label("Function_12_8263")

    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    OP_68(-9280, 900, -7620, 300)
    MoveCamera(310, 19, 0, 300)
    SetCameraDistance(17500, 300)
    OP_6F(0x79)
    CancelBlur(1000)
    Return()

    # Function_12_8263 end

    def Function_13_82A2(): pass

    label("Function_13_82A2")

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

    # Function_13_82A2 end

    def Function_14_8307(): pass

    label("Function_14_8307")

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

    # Function_14_8307 end

    def Function_15_834A(): pass

    label("Function_15_834A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8363")
    Sound(915, 0, 100, 0)
    Sleep(2000)
    Jump("Function_15_834A")

    label("loc_8363")

    Return()

    # Function_15_834A end

    def Function_16_8364(): pass

    label("Function_16_8364")

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
            "#4S#20A#60Wオオオオオオオオ……！！！\x02",
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
        "#0010F#6P#Nこ、これは……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0216
    ChrTalk(
        0x103,
        (
            "#0201F#6P#Nか、完全に暴走して\x01",
            "しまったみたいです……\x02\x03",

            "#0206Fこうなったらもう……\x01",
            "……彼の肉体は……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0217
    ChrTalk(
        0x102,
        "#0101F#6P#Nそんな……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0218
    ChrTalk(
        0x108,
        "#0901F#6P#N……くっ……\x02",
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
            "#4S#60W#15Aギイイイイイイ……！！！\x02",
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
        "#6P#0813Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x104,
        "#6P#0307Fうおっ……！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x108,
        "#0907F#6Pし、しまった……！\x02",
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
            "#4S#70W#50A……オオオオオオオ……！！！\x02",
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
        "#0108F#6P……っ……！\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x104,
        (
            "#6P#0310Fチッ……\x01",
            "このままじゃ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x107,
        (
            "#6P#0807Fこ、こんな所で……\x01",
            "諦めてたまるもんですか！\x02\x03",

            "#0806F……やっとあの子を……\x02\x03",

            "#0808F本当の意味であの子を\x01",
            "抱きしめられるのに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#6P#0007F俺たちもそうだ……！\x02\x03",

            "#0003F……絶対に……\x01",
            "何としてもあの子の元に還る……！\x02\x03",

            "#0010F……兄貴……頼む……！\x02\x03",

            "俺に力を貸してくれ……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xC, -8000, 9000, 8000, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    #N0228
    NpcTalk(
        0xC,
        "少女の声",
        "#4Pうふふ……\x02",
    )

    CloseMessageWindow()

    #N0229
    NpcTalk(
        0xC,
        "少女の声",
        (
            "#4Pお兄さんではないけれど\x01",
            "サービスで貸してあげるわ。\x02",
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

    def lambda_9112():
        OP_96(0xFE, 0xFFFFE0C0, 0xFFFFFC18, 0x1F40, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9112)
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
        "#0011Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        "#0105Fびょ、病院で見た……！？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x108,
        "#0901F《パテル＝マテル》……！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x107,
        "#0802Fレン──！\x02",
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
        "殲滅天使レン",
        (
            "#3308F#5P……哀れね。\x01",
            "でも自業自得かしら。\x02\x03",

            "#3303F今、楽にしてあげるわ。\x02",
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

    def lambda_9405():
        OP_9D(0xFE, 0xFFFFCE64, 0x352, 0x1388, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9405)
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
        "殲滅天使レン",
        (
            "#6P#3301Fパテル＝マテル！\x01",
            "薙ぎ払いなさい……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #N0236
    NpcTalk(
        0xC,
        "殲滅天使レン",
        "#6P#3307F#4S《ダブル・バスターキャノン》！！\x02",
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
        "#6P#0202F《腕》が……！\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        "#6P#0307Fよっしゃ、これで……！\x02",
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
        "殲滅天使レン",
        (
            "#3307F#13Pこれが最後のチャンスよ！\x02\x03",

            "もう“彼”は保たない！\x01",
            "止めを刺してあげなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#5P#0010Fくっ……！\x02",
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
        "#5P#0007F#4S#20A#40Wおおおおおおおおっ……！\x02",
    )
    #Auto

    Sleep(500)
    OP_68(-5700, 1100, -8000, 915)
    MoveCamera(53, 15, -9, 915)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_9BD2():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BD2)
    Sleep(5)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)

    def lambda_9BF7():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BF7)
    Sleep(5)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x102, 0x0)

    def lambda_9C1C():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C1C)
    SetChrChipByIndex(0x107, 0x26)
    SetChrSubChip(0x107, 0x0)

    def lambda_9C3E():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9C3E)
    Sleep(5)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)

    def lambda_9C63():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C63)
    SetChrChipByIndex(0x108, 0x28)
    SetChrSubChip(0x108, 0x0)

    def lambda_9C85():
        OP_96(0xFE, 0x3A98, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_9C85)
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

    # Function_16_8364 end

    def Function_17_9CD9(): pass

    label("Function_17_9CD9")

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

    # Function_17_9CD9 end

    def Function_18_9D17(): pass

    label("Function_18_9D17")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9D21():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D21)
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

    # Function_18_9D17 end

    def Function_19_9D69(): pass

    label("Function_19_9D69")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9D73():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D73)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_9D69 end

    def Function_20_9DAC(): pass

    label("Function_20_9DAC")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9DB6():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DB6)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_9DAC end

    def Function_21_9DEF(): pass

    label("Function_21_9DEF")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9DF9():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DF9)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_21_9DEF end

    def Function_22_9E32(): pass

    label("Function_22_9E32")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9E3C():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFFC18, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E3C)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_22_9E32 end

    def Function_23_9E75(): pass

    label("Function_23_9E75")

    ClearChrFlags(0xFE, 0x4)

    def lambda_9E7F():
        OP_9C(0xFE, 0x0, 0xFFFFFC18, 0x0, 0xA, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E7F)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_23_9E75 end

    def Function_24_9EB8(): pass

    label("Function_24_9EB8")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9ED4():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9ED4)

    def lambda_9EED():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EED)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x101, 0x32)
    SetChrSubChip(0x101, 0x0)
    Return()

    # Function_24_9EB8 end

    def Function_25_9F19(): pass

    label("Function_25_9F19")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9F35():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9F35)

    def lambda_9F4E():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F4E)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x3)
    Return()

    # Function_25_9F19 end

    def Function_26_9F75(): pass

    label("Function_26_9F75")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9F91():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9F91)

    def lambda_9FAA():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FAA)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x2)
    Return()

    # Function_26_9F75 end

    def Function_27_9FD1(): pass

    label("Function_27_9FD1")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_9FED():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9FED)

    def lambda_A006():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A006)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x104, 0x32)
    SetChrSubChip(0x104, 0x1)
    Return()

    # Function_27_9FD1 end

    def Function_28_A02D(): pass

    label("Function_28_A02D")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_A049():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A049)

    def lambda_A062():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A062)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x107, 0x32)
    SetChrSubChip(0x107, 0x5)
    Return()

    # Function_28_A02D end

    def Function_29_A089(): pass

    label("Function_29_A089")

    Sleep(250)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x4)

    def lambda_A0A5():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A0A5)

    def lambda_A0BE():
        OP_98(0xFE, 0x0, 0x3E8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0BE)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0x108, 0x32)
    SetChrSubChip(0x108, 0x4)
    Return()

    # Function_29_A089 end

    def Function_30_A0E5(): pass

    label("Function_30_A0E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A109")
    OP_82(0x0, 0x12C, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_30_A0E5")

    label("loc_A109")

    Return()

    # Function_30_A0E5 end

    def Function_31_A10A(): pass

    label("Function_31_A10A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A12E")
    OP_82(0x0, 0x96, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_31_A10A")

    label("loc_A12E")

    Return()

    # Function_31_A10A end

    def Function_32_A12F(): pass

    label("Function_32_A12F")

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
            "#60W……ハ……ハハ……\x01",
            "……やるじゃないか……\x02",
        )
    )

    CloseMessageWindow()

    #A0243
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W忌々しいが……最後に正気を\x01",
            "取り戻してくれた事だけは……\x01",
            "……礼を……言っておこう……\x07\x00\x02",
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
            "#0001F#5Pヨアヒム……あんた……\x02",
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
            "#60Wクク……憐れみの目で\x01",
            "僕を見ないでくれたまえ……\x02",
        )
    )

    CloseMessageWindow()

    #A0247
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60W……見届ける事は叶わないが……\x01",
            "我らが大望は成ったのだから……\x02",
        )
    )

    CloseMessageWindow()

    #A0248
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#60Wあの方は……\x01",
            "……キーア様はきっと──！\x07\x00\x02",
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
            "#0011F……あ………\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#0303Fチッ……\x01",
            "……最後まで世迷言を……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#0108Fでも……哀れね……\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x103,
        "#0206F………はい…………\x02",
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

    def lambda_A802():
        OP_95(0xFE, -9000, 0, -8000, 1200, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A802)
    Sleep(700)

    def lambda_A81F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A81F)
    Sleep(50)

    def lambda_A82F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A82F)
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
            "#0908F……気にする事はないよ。\x02\x03",

            "#0903Fあの狂気の薬を大量に飲んだ時点で\x01",
            "もう彼は助けられなかったんだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    #C0255
    ChrTalk(
        0x107,
        (
            "#5P#0806Fうん……そうね……\x02\x03",

            "#0808F出来ればあたしも\x01",
            "助けたかったけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#0008Fああ……\x02\x03",

            "#0006F最後まで……彼の妄想を\x01",
            "晴らすことが出来なかった……\x02\x03",

            "出来ればきちんと裁きを受けて\x01",
            "自分の罪を受け止めて欲しかった。\x02\x03",

            "#0008Fそうでないと……彼自身も\x01",
            "彼が犠牲にした人たちも哀しすぎる……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    #C0257
    ChrTalk(
        0x102,
        "#6P#0108Fロイド……\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x103,
        "#6P#0208F#N……ロイドさん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    OP_68(-9030, 900, -7890, 1000)

    def lambda_AAAA():
        OP_95(0xFE, -9300, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AAAA)
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
            "#12P#0307Fオラ！\x01",
            "何をしけたツラしてやがる！\x02",
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
        "#0005F#5Pランディ……？\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#12P#0303F俺たちは全能じゃねえ！\x01",
            "全てが上手くいくわけがねえんだ！\x02\x03",

            "#0301Fそれでも精一杯やって\x01",
            "ここまで来れたんだろうが！？\x02\x03",

            "ベストとは言わねぇが……\x01",
            "上出来ってもんだぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#0005F……ランディ……\x02",
    )

    CloseMessageWindow()

    def lambda_AC75():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AC75)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0263
    ChrTalk(
        0x103,
        (
            "#6P#0206F……かつてのロッジ制圧作戦では\x01",
            "多くの教団信徒たちが自決しました。\x02\x03",

            "ガイさんやアリオスさん、課長たちは\x01",
            "屍を越えてわたしを助けてくれました。\x02\x03",

            "#0202F避けられない犠牲も……\x01",
            "時にはあるのだと思います。\x02",
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
        "#0005F……ティオ……\x02",
    )

    CloseMessageWindow()

    def lambda_AD96():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD96)
    WaitChrThread(0x102, 1)

    #C0265
    ChrTalk(
        0x102,
        (
            "#6P#0103F彼は自滅してしまったけど……\x01",
            "まだまだ後始末は残っている。\x02\x03",

            "……クロスベル全域の混乱、\x01",
            "それから操られていた人の安否も……\x02\x03",

            "#0100F落ち込んでる暇は無いと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0266
    ChrTalk(
        0x101,
        "#11P#0008F……エリィ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0267
    ChrTalk(
        0x101,
        (
            "#11P#0004F……ありがとう。\x02\x03",

            "#0002Fそうだな……\x01",
            "ヘコんでる場合じゃないか。\x02\x03",

            "#0000Fそれに……\x01",
            "キーアや課長との約束も\x01",
            "ちゃんと守らないとな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#6P#0102Fええ……！\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x103,
        (
            "#6P#0204F全員で無事に\x01",
            "あの子の元に戻る約束……\x02\x03",

            "#0202Fそれと課長に一人前と\x01",
            "認めてもらう約束ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x104,
        (
            "#0309F#12Pハハ……\x01",
            "何とかどっちも守れそうだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x107,
        "#5P#0802Fふふっ……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x108,
        "#0904F……仲間か……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0273
    ChrTalk(
        0xC,
        (
            "#3300F#13Pフフ……\x01",
            "どうやら幕引きみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    def lambda_B07D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_B07D)

    def lambda_B08A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_B08A)
    Sleep(150)

    def lambda_B09A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B09A)

    def lambda_B0A7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B0A7)
    Sleep(50)

    def lambda_B0B7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B0B7)

    def lambda_B0C4():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B0C4)
    WaitChrThread(0x104, 2)

    #C0274
    ChrTalk(
        0x107,
        "#12P#0805Fえ……\x02",
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
            "#3300F#5P本当は最後まで手を貸すつもりは\x01",
            "無かったんだけど……\x02\x03",

            "#3304Fふふっ……レーヴェに\x01",
            "影響されちゃったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x108,
        "#0901Fレン……！\x02",
    )

    CloseMessageWindow()
    OP_68(-10400, 1700, 1100, 1500)
    SetCameraDistance(16500, 1500)

    def lambda_B22B():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFF8F8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_B22B)
    Sleep(200)

    def lambda_B248():
        OP_96(0xFE, 0xFFFFDCD8, 0x0, 0xFFFFF704, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_B248)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x2)
    SetChrChip(0x0, 0xC, 0x32, 0x12C)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(854, 0, 100, 0)

    def lambda_B283():
        OP_9D(0xFE, 0xFFFFD5D0, 0x7D0, 0x16A8, 0x6D6, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B283)
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
            "#3304F……これでクロスベルでの\x01",
            "レンの心残りは全部無くなった。\x02\x03",

            "#3300Fなかなか楽しかったけど\x01",
            "レンがいると混乱しそうだし、\x01",
            "そろそろ失礼するわね──\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x107,
        "#0800F#11Pレン。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    def lambda_B3F6():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B3F6)
    Sleep(800)
    OP_93(0xC, 0x5A, 0xFA)
    Sleep(300)

    #C0279
    ChrTalk(
        0xC,
        (
            "#3306F#12P……なぁに、エステル。\x02\x03",

            "#3308Fレンは……\x01",
            "まだ捕まる気はないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x107,
        (
            "#0803F#11Pううん……レン。\x02\x03",

            "#0802Fもうあんたは……\x01",
            "あたしたちに捕まってるわ。\x02",
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
            "#0808F#11P最後に別れてから半年……\x02\x03",

            "一度リベールに里帰りして\x01",
            "またここに来てから３ヶ月……\x02\x03",

            "#0800Fあたしたちはいつでも\x01",
            "レンの気配を肌で感じてたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x108,
        (
            "#0904F#11P人形工房にいた事も知っていたし、\x01",
            "ちょくちょくクロスベル市に\x01",
            "遊びに来ていたのも知っていた。\x02\x03",

            "#0900Fさすがに導力ネットで君を\x01",
            "捉えるのは難しかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xC,
        (
            "#3307F#12Pあ、当たり前じゃない……\x02\x03",

            "#3308Fレンは《仔猫》……\x01",
            "誰にも捕まらないんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x107,
        (
            "#0800Fあたしたち以外には、ね。\x02\x03",

            "#0803F──今、あたしたちは\x01",
            "レンのことを全て知った。\x02\x03",

            "あんたの過去、哀しみ。\x01",
            "そして嬉しい事や楽しい事も。\x02\x03",

            "#0802Fもう──逃げ切れないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xC,
        "#3308F#12Pっ……\x02",
    )

    CloseMessageWindow()

    def lambda_B76E():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B76E)
    Sleep(800)
    OP_93(0xC, 0xB4, 0x12C)
    Sleep(500)

    #C0287
    ChrTalk(
        0xC,
        (
            "#3312F#12P#40Wあ、あきらめると……\x01",
            "……思ったのに……\x02\x03",

            "《楽園》のことを知ったら……\x02\x03",

            "#3313F……エステルは絶対に\x01",
            "あきらめると思ったのに……っ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0288
    ChrTalk(
        0x107,
        (
            "#0806F#11P２年前のあたしだったら\x01",
            "ひょっとしたらそうだったかも。\x02\x03",

            "#0802Fでも、みんなやレーヴェ、\x01",
            "そしてレンに出会えたおかげで\x01",
            "あたしは強くなれた。\x02\x03",

            "過去のどんな出来事も……\x01",
            "今のあんたを形作っている\x01",
            "大切なものだから……\x02\x03",

            "#0809F今はただ……\x01",
            "愛おしくて仕方ないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xC,
        "#3312F#12P……ぁ………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0290
    ChrTalk(
        0x108,
        (
            "#0903F#11P──本当だったらご両親の元に\x01",
            "戻った方がいいのかもしれない。\x02\x03",

            "#0901Fでも僕たちは……\x01",
            "どんなに我儘と言われようとも\x01",
            "家族として君を引き取りたい。\x02\x03",

            "#0902Fそれがクロスベルに来て\x01",
            "僕たちが改めて出した結論だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xC,
        (
            "#3313F#12P………うううっ………\x02\x03",

            "そんな……そんなの……っ！\x02",
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
            "#3311F#6Pパテル＝マテル！？\x02\x03",

            "ど、どうして勝手に……！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x107,
        "#0805F#12P#Nも、もしかして……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0294
    ChrTalk(
        0x108,
        (
            "#0902F#12P#Nそうか……\x01",
            "君もレンのことを……\x02",
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

    def lambda_BC07():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFF1F0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BC07)
    Sleep(100)

    def lambda_BC24():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xFFFFF060, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_BC24)
    OP_79(0x1)
    OP_71(0x1, 0x1F5, 0x208, 0x0, 0x0)
    OP_93(0xC, 0xB4, 0x1F4)

    #C0295
    ChrTalk(
        0xC,
        "#11P#3310F#25A#40W#N……ダ、ダメぇ……！\x02",
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

    def lambda_BD1C():
        OP_96(0xFE, 0xFFFFDA1C, 0x0, 0xFFFFF704, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_BD1C)
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
        "#11P#0804F──捕まえた。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xC,
        "#11P#3312Fぁ……\x02",
    )

    CloseMessageWindow()

    def lambda_BDFA():
        OP_96(0xFE, 0xFFFFDC10, 0x0, 0xFFFFF2B8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_BDFA)
    WaitChrThread(0x108, 1)

    #C0298
    ChrTalk(
        0x108,
        (
            "#12P#0904Fありがとう……\x01",
            "パテル＝マテル。\x02\x03",

            "#0900Fマイスターに調整されて\x01",
            "自分の意志で動けるように\x01",
            "なったみたいだね？\x02",
        )
    )

    CloseMessageWindow()
    Sound(943, 0, 100, 0)
    Sleep(500)

    #C0299
    ChrTalk(
        0xC,
        "#11P#3313Fううううっ……\x02",
    )

    CloseMessageWindow()

    def lambda_BEB8():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_BEB8)

    #C0300
    ChrTalk(
        0x107,
        (
            "#11P#0812Fもう……\x01",
            "逃がしてあげないんだから。\x02\x03",

            "……これからどこで\x01",
            "どんな風に暮らしていくか\x01",
            "一緒に考える必要はあるけど……\x02\x03",

            "#0811Fまずは一度……\x01",
            "リベールに帰りましょ……？\x02\x03",

            "ティータもずっと……\x01",
            "レンのことを待っているわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xC,
        "#11P#3312F……あああああああっ……\x02",
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
        "#5P#3310F#4Sわああああああああっ……！\x02",
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
        "#11P#0810F……レン……！\x02",
    )

    CloseMessageWindow()
    Sleep(130)
    SetChrSubChip(0xC, 0x11)
    Sleep(130)
    SetChrSubChip(0xC, 0x10)

    #C0304
    ChrTalk(
        0xC,
        "#5P#3313Fうううっ……ああああっ……\x02",
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
        "#5P#3310F#4Sうわあああああああんんん！！\x02",
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

    def lambda_C190():
        OP_96(0xFE, 0xFFFFDBAC, 0x0, 0xFFFFECDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C190)
    Sleep(200)

    def lambda_C1AD():
        OP_96(0xFE, 0xFFFFD508, 0x0, 0xFFFFEA84, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C1AD)
    Sleep(200)

    def lambda_C1CA():
        OP_96(0xFE, 0xFFFFD828, 0x0, 0xFFFFE764, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C1CA)
    Sleep(200)

    def lambda_C1E7():
        OP_96(0xFE, 0xFFFFDECC, 0x0, 0xFFFFE958, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C1E7)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0307
    ChrTalk(
        0x101,
        "#0002F#11P……はは……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)

    #C0308
    ChrTalk(
        0x102,
        (
            "#12P#0106Fグスッ……\x01",
            "……本当に良かった……\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 1)

    #C0309
    ChrTalk(
        0x103,
        "#12P#0208F………はい…………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 1)

    #C0310
    ChrTalk(
        0x104,
        (
            "#0302Fはは……\x01",
            "さすがにジンと来ちまうな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)
    Sleep(300)

    #C0311
    ChrTalk(
        0x108,
        (
            "#0910F#5P……みんな……\x02\x03",

            "#0911Fありがとう……\x01",
            "本当に君たちにはなんて……\x02\x03",

            "#0904F……なんて\x01",
            "お礼を言ったらいいのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x101,
        (
            "#0004F#11Pいや……\x01",
            "俺たちは手伝いをしただけさ。\x02\x03",

            "君たちは君たちの手で……\x01",
            "この結果を手に入れたんだと思う。\x02\x03",

            "#0002F──ヨシュア。\x01",
            "おめでとうって言わせてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x108,
        "#0911F#5P……ありがとう、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふっ……\x01",
            "一刻も早くキーアちゃんの\x01",
            "顔が見たくなってきたわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        (
            "#12P#0204Fはい……\x01",
            "それにツァイトと課長にも……\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#0309Fはは、そんじゃあ\x01",
            "ボチボチ戻るとすっか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#0002F#11Pああ……\x02",
    )

    CloseMessageWindow()
    OP_68(-8860, 1000, -4920, 1500)
    MoveCamera(51, 17, 0, 1500)

    def lambda_C4F1():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C4F1)
    Sleep(250)

    def lambda_C501():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C501)

    def lambda_C50E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C50E)
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
        "#5P#0004F──特務支援課、撤収準備。\x02",
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
            "#5P#0000F囚われた人たちを護衛しつつ、\x01",
            "マフィアたちの身柄を確保しながら\x01",
            "地上に戻ろう……！\x02",
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

    # Function_32_A12F end

    def Function_33_C60C(): pass

    label("Function_33_C60C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C630")
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_33_C60C")

    label("loc_C630")

    Return()

    # Function_33_C60C end

    def Function_34_C631(): pass

    label("Function_34_C631")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C67B")
    PlayEffect(0x1, 0xFF, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(3000)
    Jump("Function_34_C631")

    label("loc_C67B")

    Return()

    # Function_34_C631 end

    def Function_35_C67C(): pass

    label("Function_35_C67C")

    OP_77(0x0, 0x3E8)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x5A, 0x64, 0x0, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x0)
    Return()

    # Function_35_C67C end

    def Function_36_C6A4(): pass

    label("Function_36_C6A4")

    OP_77(0x1, 0x12C)

    def lambda_C6AD():
        OP_96(0xFE, 0xFFFFE0C0, 0xFFFFFC18, 0x708, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C6AD)
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

    # Function_36_C6A4 end

    def Function_37_C74D(): pass

    label("Function_37_C74D")

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

    # Function_37_C74D end

    def Function_38_C787(): pass

    label("Function_38_C787")

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

    # Function_38_C787 end

    def Function_39_C7BB(): pass

    label("Function_39_C7BB")

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

    # Function_39_C7BB end

    SaveToFile()

Try(main)
