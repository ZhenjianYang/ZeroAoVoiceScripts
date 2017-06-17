from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m0113.bin",                # FileName
        "m0113",                    # MapName
        "m0113",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0113",                  # 0
        "魔兽",                   # 1
        "魔兽",                   # 2
        "魔兽",                   # 3
        "魔兽",                   # 4
        "魔兽",                   # 5
        "魔兽",                   # 6
        "bm0112",                 # 7
    ))

    ATBonus("ATBonus_278", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_338", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_31C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_320", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_324", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_328", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_32C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_330", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_358", 0x0052, 50, 6, 0, 0, 1, 0, 0, "bm0112", 0x00000000, 100, 0, 0, 0,
        (
            ("ms71800.dat", "ms73300.dat", "ms73300.dat", "ms73101.dat", "ms73101.dat", "ms73101.dat", "ms73101.dat", 0, "MonsterBattlePostion_338", "MonsterBattlePostion_318", "ed7405", "ed7403", "ATBonus_278"),
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 4,   0.0,                   -7.5,                  0.0,                   81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  2.5,                   -0.0,                  1.0])

    DeclActor(2000,    0,       -200000, 1200,    2500,    1000,    -200000, 0x007C, 0,  8,  0x0000)
    DeclActor(0,       0,       102000,  1200,    0,       1000,    102500,  0x007C, 0,  10, 0x0000)
    DeclActor(2500,    0,       -87250,  1200,    2500,    1500,    -87250,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1

    ScpFunction((
        "Function_0_3E4",          # 00, 0
        "Function_1_400",          # 01, 1
        "Function_2_41F",          # 02, 2
        "Function_3_467",          # 03, 3
        "Function_4_745",          # 04, 4
        "Function_5_EAC",          # 05, 5
        "Function_6_11D5",         # 06, 6
        "Function_7_123E",         # 07, 7
        "Function_8_1331",         # 08, 8
        "Function_9_14B3",         # 09, 9
        "Function_10_15FA",        # 0A, 10
        "Function_11_177C",        # 0B, 11
    ))


    def Function_0_3E4(): pass

    label("Function_0_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FF")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_3E4")

    label("loc_3FF")

    Return()

    # Function_0_3E4 end

    def Function_1_400(): pass

    label("Function_1_400")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_400")

    label("loc_41E")

    Return()

    # Function_1_400 end

    def Function_2_41F(): pass

    label("Function_2_41F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 9)
    Jump("loc_466")

    label("loc_44C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_466")

    Return()

    # Function_2_41F end

    def Function_3_467(): pass

    label("Function_3_467")

    SetMapObjFrame(0x3, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x4, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_6D0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_585")
    SetMapObjFrame(0x6, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "off_kp")
    Jump("loc_6D0")

    label("loc_585")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_630")
    SetMapObjFrame(0x6, "m01gim05", 0x2, "off_kp")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "off_kp")
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "off_kp")
    OP_1B(0x1, 0x0, 0x6)
    Jump("loc_6D0")

    label("loc_630")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x34, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_6D0")
    ModifyEventFlags(1, 0, 0x80)
    SetMapObjFrame(0x6, "m01gim05", 0x2, "on_kp")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "on_kp")
    SetMapObjFlags(0x6, 0x2)
    SetMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "on_kp")

    label("loc_6D0")

    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    Return()

    # Function_3_467 end

    def Function_4_745(): pass

    label("Function_4_745")

    EventBegin(0x1)
    FadeToDark(500, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("monster/ch71850.itc", 0x22)
    LoadChrToIndex("monster/ch73350.itc", 0x23)
    LoadChrToIndex("monster/ch73150.itc", 0x24)
    OP_68(0, 1500, -8000, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 500, 0, -7500, 0)
    SetChrPos(0x102, -500, 0, -7750, 0)
    SetChrPos(0x103, 750, 0, -9000, 0)
    SetChrPos(0x104, -750, 0, -9250, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 7000, 0, 180)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 1, 0, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrChipByIndex(0xA, 0x23)
    SetChrChipByIndex(0xB, 0x24)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrPos(0x9, 3500, 0, -1500, 225)
    SetChrPos(0xA, -3500, 0, -1500, 135)
    SetChrPos(0xB, 2000, 7000, 2000, 225)
    SetChrPos(0xC, -2500, 7000, 2000, 135)
    SetChrPos(0xD, 0, 7000, -1500, 180)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0x9, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xA, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xB, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xC, 1, 0, 1)
    Sleep(50)
    BeginChrThread(0xD, 1, 0, 1)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)

    def lambda_98F():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98F)
    Sleep(50)

    def lambda_9AC():
        OP_97(0x102, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9AC)
    Sleep(50)

    def lambda_9C9():
        OP_97(0x103, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C9)
    Sleep(50)

    def lambda_9E6():
        OP_97(0x104, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E6)
    OP_68(0, 1500, -3000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)

    def lambda_A1F():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A1F)
    WaitChrThread(0x102, 1)

    def lambda_A30():
        OP_93(0x102, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A30)
    WaitChrThread(0x103, 1)

    def lambda_A41():
        OP_93(0x103, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A41)
    WaitChrThread(0x104, 1)

    def lambda_A52():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A52)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x101,
        "#11P#0005F哇，白茫茫的一片……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        (
            "#5P#0106F穿、穿成这样，\x01",
            "果然有些冷呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#12P#0301F从目前的状况来看，\x01",
            "身为冻气源头的魔兽\x01",
            "似乎就潜伏在这里……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x9C4)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_93(0x103, 0x0, 0x1F4)
    Sleep(500)

    #C0004
    ChrTalk(
        0x103,
        (
            "#12P#0201F说对了……！\x01",
            "请大家小心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B5D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5D)

    def lambda_B6A():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B6A)

    def lambda_B77():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B77)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0005
    ChrTalk(
        0x101,
        "#11P#0007F啊……！\x02",
    )

    CloseMessageWindow()
    OP_68(-450, 1300, -3140, 3000)
    MoveCamera(34, 20, 0, 3000)
    SetCameraDistance(24160, 3000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    def lambda_BD5():
        OP_98(0x8, 0x0, 0xFFFFE4A8, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BD5)
    Sleep(500)
    Sound(862, 0, 100, 0)

    def lambda_BF8():
        OP_98(0x104, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BF8)
    Sleep(50)

    def lambda_C15():
        OP_98(0x103, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C15)
    Sleep(50)

    def lambda_C32():
        OP_98(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C32)
    Sleep(50)

    def lambda_C4F():
        OP_98(0x101, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4F)
    WaitChrThread(0x104, 1)
    Fade(500)
    SetChrChipByIndex(0x104, 0x21)
    Sound(808, 0, 100, 0)
    WaitChrThread(0x103, 1)
    SetChrChipByIndex(0x103, 0x20)
    WaitChrThread(0x102, 1)
    SetChrChipByIndex(0x102, 0x1F)
    Sound(531, 0, 100, 0)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0x101, 0x1E)
    OP_0D()
    WaitChrThread(0x8, 2)
    Sound(202, 0, 100, 0)

    def lambda_CA5():
        OP_A7(0x9, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_CA5)
    Sleep(50)

    def lambda_CB9():
        OP_A7(0xA, 0x0, 0x0, 0x0, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CB9)
    Sleep(50)

    def lambda_CCD():
        OP_98(0xB, 0x0, 0xFFFFE4A8, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_CCD)
    Sleep(150)

    def lambda_CEA():
        OP_98(0xC, 0x0, 0xFFFFE4A8, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_CEA)
    Sleep(150)

    def lambda_D07():
        OP_98(0xD, 0x0, 0xFFFFE4A8, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_D07)
    WaitChrThread(0x9, 2)

    def lambda_D25():
        OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D25)
    WaitChrThread(0xA, 2)

    def lambda_D3A():
        OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D3A)
    WaitChrThread(0x9, 2)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xD, 2)

    #C0006
    ChrTalk(
        0x102,
        "#6P#0105F这、这只魔兽是……！？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#12P#0307F小心……！\x01",
            "看起来很难对付！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#12P#0007F各位，全力战斗吧！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22500, 200)
    BlurSwitch(0xC8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x32, 0x32, 0xC8, 0x7D0)

    def lambda_DFD():
        OP_95(0x9, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_DFD)
    Sleep(5)

    def lambda_E1A():
        OP_95(0xA, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_E1A)
    Sleep(5)

    def lambda_E37():
        OP_95(0xB, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E37)
    Sleep(5)

    def lambda_E54():
        OP_95(0xC, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_E54)
    Sleep(5)

    def lambda_E71():
        OP_95(0xD, 0, 0, -6000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_E71)
    Sleep(200)
    CancelBlur(0)
    Battle("BattleInfo_358", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 5)
    Return()

    # Function_4_745 end

    def Function_5_EAC(): pass

    label("Function_5_EAC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1500, 0, 0)
    MoveCamera(55, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30500, 0)
    SetChrPos(0x101, 0, 0, 1000, 0)
    SetChrPos(0x102, 1000, 0, 0, 90)
    SetChrPos(0x103, -1000, 0, 0, 270)
    SetChrPos(0x104, 0, 0, -1000, 180)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetCameraDistance(35500, 3000)
    MoveCamera(45, 28, 0, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(153, 0, 100, 0)
    SetMapObjFrame(0x6, "m01gim05", 0x2, "off")
    SetMapObjFrame(0x8, "m01gim05", 0x2, "off")
    ClearMapObjFlags(0x6, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    SetMapObjFrame(0xFF, "simo00", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice02_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice03_add", 0x2, "off")
    SetMapObjFrame(0xFF, "simo00ice00_11_add", 0x2, "off")
    Sleep(2000)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1100, 0, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    OP_0D()

    #C0009
    ChrTalk(
        0x101,
        "#5P#0005F恢复正常了……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        (
            "#11P#0105F这样一来，地下空间的异常状况\x01",
            "应该就算解决了吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#12P#0306F至少温度\x01",
            "恢复正常了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10E1():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10E1)
    Sleep(50)

    def lambda_10F1():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10F1)
    Sleep(50)

    def lambda_1101():
        TurnDirection(0x103, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1101)
    Sleep(50)

    def lambda_1111():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1111)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0012
    ChrTalk(
        0x103,
        (
            "#6P#0200F里面应该有能够\x01",
            "返回顶层的升降机。\x02\x03",

            "去看看能不能\x01",
            "正常使用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，要是能使用的话，\x01",
            "就回去向管理员报告吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 0, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_1B(0x1, 0x0, 0x6)
    OP_29(0x34, 0x1, 0x2)
    OP_DE(0x23, 0x0)
    EventEnd(0x5)
    Return()

    # Function_5_EAC end

    def Function_6_11D5(): pass

    label("Function_6_11D5")

    EventBegin(0x1)

    #C0014
    ChrTalk(
        0x103,
        (
            "#0200F刚才那个地方的最里面，\x01",
            "有一部可以返回顶层的\x01",
            "升降机。\x02\x03",

            "从那里返回吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, -110, 0, -123480, 0)
    EventEnd(0x4)
    Return()

    # Function_6_11D5 end

    def Function_7_123E(): pass

    label("Function_7_123E")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1313")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x5, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x5, 0x0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x5, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1313")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_132F")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_132F")

    Return()

    # Function_7_123E end

    def Function_8_1331(): pass

    label("Function_8_1331")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作升降机的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AB")
    Fade(500)
    SetChrPos(0x0, 600, 0, -199400, 90)
    SetChrPos(0x1, 600, 0, -200600, 90)
    SetChrPos(0x2, -600, 0, -200600, 90)
    SetChrPos(0x3, -600, 0, -199400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_140B")
    SetChrPos(0x4, -1800, 0, -200600, 90)
    SetChrPos(0x5, -1800, 0, -199400, 90)
    Jump("loc_142A")

    label("loc_140B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142A")
    SetChrPos(0x4, -1800, 0, -200000, 90)

    label("loc_142A")

    OP_68(0, 1000, -200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, 6000, -200000, 3000)
    SetMapObjFrame(0x3, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0112", 0, 0, 0)
    IdleLoop()

    label("loc_14AB")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_8_1331 end

    def Function_9_14B3(): pass

    label("Function_9_14B3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x3, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(0, 11000, -200000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, -199400, 90)
    OP_90(0x1, 600, 30000, -200600, 90)
    OP_90(0x2, -600, 30000, -200600, 90)
    OP_90(0x3, -600, 30000, -199400, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1586")
    OP_90(0x4, -1800, 30000, -200600, 90)
    OP_90(0x5, -1800, 30000, -199400, 90)
    Jump("loc_15A5")

    label("loc_1586")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A5")
    OP_90(0x4, -1800, 30000, -200000, 90)

    label("loc_15A5")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, -200000, 3000)
    SetMapObjFrame(0x3, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x3)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_14B3 end

    def Function_10_15FA(): pass

    label("Function_10_15FA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作升降机的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1774")
    Fade(500)
    SetChrPos(0x0, 600, 0, 100600, 0)
    SetChrPos(0x1, -600, 0, 100600, 0)
    SetChrPos(0x2, -600, 0, 99400, 0)
    SetChrPos(0x3, 600, 0, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16D4")
    SetChrPos(0x4, -600, 0, 98200, 0)
    SetChrPos(0x5, 600, 0, 98200, 0)
    Jump("loc_16F3")

    label("loc_16D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F3")
    SetChrPos(0x4, 0, 0, 98200, 0)

    label("loc_16F3")

    OP_68(0, 1000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(0, 6000, 100000, 3000)
    SetMapObjFrame(0x4, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D0(0x0, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_1774")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_15FA end

    def Function_11_177C(): pass

    label("Function_11_177C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x4, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(0, 11000, 100000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 100600, 0)
    OP_90(0x1, -600, 30000, 100600, 0)
    OP_90(0x2, -600, 30000, 99400, 0)
    OP_90(0x3, 600, 30000, 99400, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184F")
    OP_90(0x4, -600, 30000, 98200, 0)
    OP_90(0x5, 600, 30000, 98200, 0)
    Jump("loc_186E")

    label("loc_184F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186E")
    OP_90(0x4, 0, 30000, 98200, 0)

    label("loc_186E")

    Sound(145, 0, 100, 0)
    OP_68(0, 1000, 100000, 3000)
    SetMapObjFrame(0x4, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x4)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_177C end

    SaveToFile()

Try(main)
