from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3002.bin",                # FileName
        "m3002",                    # MapName
        "m3002",                    # Location
        0x007B,                     # MapIndex
        "ed7510",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, -79500, 0, 0, 0, 0, 1, 123, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3002",                  # 0
        "ＳＥ控制",               # 1
        "bm3080",                 # 2
        "bm3080",                 # 3
    ))

    ATBonus("ATBonus_298", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1E3D", 4,   4,   20,  0,   16,  12,  7)
    Sepith("Sepith_1E45", 0,   29,  0,   0,   9,   3,   19)

    MonsterBattlePostion("MonsterBattlePostion_2F8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_35C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_360", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_364", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_368", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_36C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_370", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 5, 5, 45)

    # monster count: 4

    BattleInfo(
        "BattleInfo_440", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3080", "Sepith_1E3D", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
        )
    )

    BattleInfo(
        "BattleInfo_378", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3080", "Sepith_1E45", 60, 25, 10, 5,
        (
            ("ms68600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms68600.dat", "ms68600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms68600.dat", "ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
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
        "monster/ch68650.itc",               # 10
        "monster/ch68651.itc",               # 11
        "monster/ch60650.itc",               # 12
        "monster/ch60650.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-7710,   26930,   10,      0x1010000,    "BattleInfo_440", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19430,   -70,     -12000,  0x1010000,    "BattleInfo_378", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-35270,  -28040,  -228000, 0x1010000,    "BattleInfo_440", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-36100,  27760,   -228000, 0x1010000,    "BattleInfo_378", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 4,   -46.0,                 0.0,                   5.0,                   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.333333969116211,    -0.0,                  -1.0,                  1.0])
    DeclEvent(0x0000, 0, 5,   -46.0,                 0.0,                   5.0,                   56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.333333969116211,    -0.0,                  -1.0,                  1.0])

    DeclActor(-7500,   -228000, 24500,   1200,    -7500,   -227000, 24500,   0x007C, 0,  2,  0x0000)
    DeclActor(-23250,  -228000, 28500,   1200,    -23250,  -227000, 28500,   0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_558",          # 00, 0
        "Function_1_559",          # 01, 1
        "Function_2_5F9",          # 02, 2
        "Function_3_75C",          # 03, 3
        "Function_4_8BF",          # 04, 4
        "Function_5_1409",         # 05, 5
        "Function_6_1DC0",         # 06, 6
        "Function_7_1E0B",         # 07, 7
    ))


    def Function_0_558(): pass

    label("Function_0_558")

    Return()

    # Function_0_558 end

    def Function_1_559(): pass

    label("Function_1_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_END)), "loc_56B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x131), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57E")
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_57E")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AE")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_5AE")

    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7")
    OP_70(0x11, 0x0)
    Jump("loc_5DB")

    label("loc_5D7")

    OP_70(0x11, 0x1E)

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EE")
    OP_70(0x12, 0x0)
    Jump("loc_5F2")

    label("loc_5EE")

    OP_70(0x12, 0x1E)

    label("loc_5F2")

    Sound(129, 1, 100, 0)
    Return()

    # Function_1_559 end

    def Function_2_5F9(): pass

    label("Function_2_5F9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72D")
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x11, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11E, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_74A")

    label("loc_72D")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_74A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5F9 end

    def Function_3_75C(): pass

    label("Function_3_75C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890")
    Sound(14, 0, 100, 0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x12, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11E, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_8AD")

    label("loc_890")


    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8AD")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_75C end

    def Function_4_8BF(): pass

    label("Function_4_8BF")

    EventBegin(0x0)
    OP_E0(0x1)
    SoundLoad(800)
    Fade(1000)
    OP_68(-38000, 7000, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -39800, 6000, 0, 90)
    SetChrPos(0x102, -41300, 6000, -900, 90)
    SetChrPos(0x103, -42200, 6000, 0, 90)
    SetChrPos(0x104, -41300, 6000, 900, 90)
    SetChrPos(0x107, -43300, 6000, -600, 90)
    SetChrPos(0x108, -43300, 6000, 600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-33000, 7000, 0, 3000)

    def lambda_989():
        OP_96(0xFE, 0xFFFF7FE0, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_989)

    def lambda_9A3():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A3)

    def lambda_9BD():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0x384, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9BD)
    Sleep(50)

    def lambda_9DA():
        OP_96(0xFE, 0xFFFF7680, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9DA)
    Sleep(50)

    def lambda_9F7():
        OP_96(0xFE, 0xFFFF7234, 0x1770, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9F7)

    def lambda_A11():
        OP_96(0xFE, 0xFFFF7234, 0x1770, 0x258, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A11)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    #C0005
    ChrTalk(
        0x101,
        "#0010F#5P这里是……！？\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 7000, 0, 3000)
    SetCameraDistance(42000, 3000)
    OP_6F(0x11)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 7)
    Fade(1000)
    OP_68(-10000, 5000, 0, 0)
    MoveCamera(100, 25, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(38000, 0)
    OP_68(-14000, -5000, 0, 10000)
    MoveCamera(55, 50, 0, 10000)
    SetCameraDistance(36000, 10000)
    OP_6F(0x79)
    EndChrThread(0x8, 0x0)

    #C0006
    ChrTalk(
        0x107,
        "#0813F好惊人……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0108F一直延伸到地底深处的竖坑……\x01",
            "竟然有这么大。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x108,
        (
            "#0901F这也是在数百年前\x01",
            "建造的吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0301F从这里目测的话，\x01",
            "深度至少有五百亚矩吧。\x02\x03",

            "#0306F哎呀呀……\x01",
            "似乎相当麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        "#0208F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-33000, 7100, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -31800, 6000, 0, 90)
    SetChrPos(0x102, -33900, 6000, -900, 90)
    SetChrPos(0x103, -34800, 6000, 0, 90)
    SetChrPos(0x104, -33900, 6000, 900, 90)
    SetChrPos(0x107, -35900, 6000, -600, 90)
    SetChrPos(0x108, -35900, 6000, 600, 90)
    OP_0D()

    def lambda_CF3():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CF3)
    WaitChrThread(0x103, 2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D73():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D73)
    Sleep(100)

    def lambda_D83():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D83)

    def lambda_D90():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D90)
    Sleep(50)

    def lambda_DA0():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_DA0)
    TurnDirection(0x108, 0x103, 500)

    #C0011
    ChrTalk(
        0x101,
        "#0011F#5P缇欧，你怎么了？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0101F#11P没事吧？\x01",
            "脸色那么苍白。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#6P#0206F……我没事。\x02\x03",

            "#0208F只是这里让我想起了\x01",
            "以前曾经待过的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0003F#5P以前曾经待过的地方吗……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0301F#5P是指位于共和国西部\x01",
            "的教团据点吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#6P#0203F…………是的。\x02\x03",

            "#0208F我想，这个竖坑大概是\x01",
            "仿照通向『炼狱』的\x01",
            "黄泉之路而建造的。\x02\x03",

            "目的是企图接近并利用\x01",
            "作为否定女神的概念而存在的恶魔……\x02\x03",

            "#0201F然后也是为了向其献上祭品，\x01",
            "举行『仪式』。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        "#0106F#11P……太过分了。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0310F#5P哼，难怪这里有一种\x01",
            "令人厌恶的感觉。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7305", 0)

    #C0019
    ChrTalk(
        0x101,
        (
            "#0008F#5P──既然如此，\x01",
            "我们的任务便只有一个。\x02\x03",

            "#0003F为了那些帮我们\x01",
            "开拓道路的人们。\x02\x03",

            "也为了等着我们\x01",
            "回去的琪雅……\x02\x03",

            "#0013F一定要彻底粉碎那令人作呕的幻想，\x01",
            "并使其暴露在阳光之下！\x02\x03",

            "不再让任何人\x01",
            "遭受悲伤与痛苦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        "#6P#0205F………罗伊德前辈…………\x02",
    )

    CloseMessageWindow()

    def lambda_10DE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10DE)
    Sleep(50)

    def lambda_10EE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_10EE)
    Sleep(50)

    def lambda_10FE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_10FE)
    OP_93(0x108, 0x5A, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0x104,
        (
            "#6P#0304F真是的，\x01",
            "本想说你是个热血笨蛋……\x02\x03",

            "#0300F不过，这次就\x01",
            "让我也加入吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵，也算我一个。\x02\x03",

            "#0103F敌人是躲在暗处操纵一切，\x01",
            "不露出真实面目，蜘蛛般的存在……\x02\x03",

            "#0100F但是，凭现在的我们，\x01",
            "一定可以将他揪出。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#6P#0204F……是的。\x02\x03",

            "#0201F我们……绝不会输的！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x107,
        "#0800F#12P我们也来帮忙！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x108,
        "#0901F#6P我们会全力支援你们！\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0000F#5P好……那就出发吧。\x02\x03",

            "#0003F克洛斯贝尔警察局·特别任务支援科，\x01",
            "罗伊德·班宁斯等四名队员──\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x107,
        (
            "#0801F#12P以及游击士协会，\x01",
            "艾丝蒂尔·布莱特等两名成员──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0028
    ChrTalk(
        0x101,
        (
            "#0007F#5P为解决本次事件，\x01",
            "正式开始强行潜入调查……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-34800, 9000, 0, 0)
    MoveCamera(90, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(37000, 0)
    SetChrPos(0x0, -34800, 6000, 0, 90)
    SetChrPos(0x1, -34800, 6000, 0, 90)
    SetChrPos(0x2, -34800, 6000, 0, 90)
    SetChrPos(0x3, -34800, 6000, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE4, 7)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_4_8BF end

    def Function_5_1409(): pass

    label("Function_5_1409")

    EventBegin(0x0)
    OP_E0(0x1)
    SoundLoad(800)
    Fade(1000)
    OP_68(-38000, 7000, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -39800, 6000, 0, 90)
    SetChrPos(0x102, -41300, 6000, -900, 90)
    SetChrPos(0x103, -42200, 6000, 0, 90)
    SetChrPos(0x104, -41300, 6000, 900, 90)
    OP_68(-33000, 7000, 0, 3000)

    def lambda_149D():
        OP_96(0xFE, 0xFFFF7FE0, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149D)
    Sleep(50)

    def lambda_14BA():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BA)
    Sleep(50)

    def lambda_14D7():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0x384, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14D7)
    Sleep(50)

    def lambda_14F4():
        OP_96(0xFE, 0xFFFF7680, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14F4)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x102, 1)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    WaitChrThread(0x103, 1)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x101,
        "#0010F#5P这里是……！？\x02",
    )

    CloseMessageWindow()
    OP_68(-20000, 7000, 0, 3000)
    SetCameraDistance(42000, 3000)
    OP_6F(0x11)
    Sleep(300)
    BeginChrThread(0x8, 0, 0, 7)
    Fade(1000)
    OP_68(-10000, 5000, 0, 0)
    MoveCamera(100, 25, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(38000, 0)
    OP_68(-14000, -5000, 0, 10000)
    MoveCamera(55, 50, 0, 10000)
    SetCameraDistance(36000, 10000)
    OP_6F(0x79)
    EndChrThread(0x8, 0x0)

    #C0030
    ChrTalk(
        0x102,
        (
            "#0108F通向地底深处的竖坑……\x01",
            "竟然有这么大。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0301F从这里目测的话，\x01",
            "深度至少有五百亚矩吧。\x02\x03",

            "#0306F哎呀呀……\x01",
            "似乎相当麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#0208F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-33000, 7100, 0, 0)
    MoveCamera(90, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -31800, 6000, 0, 90)
    SetChrPos(0x102, -33900, 6000, -900, 90)
    SetChrPos(0x103, -34800, 6000, 0, 90)
    SetChrPos(0x104, -33900, 6000, 900, 90)
    OP_0D()

    def lambda_1757():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1757)
    WaitChrThread(0x103, 2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_17B3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17B3)
    Sleep(100)

    def lambda_17C3():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_17C3)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0033
    ChrTalk(
        0x101,
        "#0011F#5P缇欧，你怎么了？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#0101F#11P没事吧？\x01",
            "脸色那么苍白。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#6P#0206F……我没事。\x02\x03",

            "#0208F只是这里让我想起了\x01",
            "以前曾经待过的地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0003F#5P以前曾经待过的地方吗……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0301F#5P是指那些家伙位于\x01",
            "共和国西部的据点吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0203F…………是的。\x02\x03",

            "#0208F我想，这个竖坑大概是\x01",
            "仿照通向『炼狱』的\x01",
            "黄泉之路而建造的。\x02\x03",

            "目的是企图接近并利用\x01",
            "作为否定女神的概念而存在的恶魔……\x02\x03",

            "#0201F然后也是为了向其献上祭品，\x01",
            "举行『仪式』。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#0106F#11P……太过分了。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0310F#5P哼，难怪这里有一种\x01",
            "令人厌恶的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0008F#5P──既然如此，\x01",
            "我们的任务便只有一个。\x02\x03",

            "#0003F为了那些帮我们\x01",
            "开拓道路的人们。\x02\x03",

            "也为了等着我们\x01",
            "回去的那个孩子……\x02\x03",

            "#0013F一定要彻底粉碎那令人作呕的幻想，\x01",
            "并使其暴露在阳光之下！\x02\x03",

            "不再让任何人\x01",
            "遭受悲伤与痛苦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#6P#0205F………罗伊德前辈…………\x02",
    )

    CloseMessageWindow()

    def lambda_1AFF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1AFF)
    Sleep(50)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(300)

    #C0043
    ChrTalk(
        0x104,
        (
            "#6P#0304F真是的，\x01",
            "本想说你是个热血笨蛋……\x02\x03",

            "#0300F不过，这次就\x01",
            "让我也加入吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#0102F呵呵，也算我一个。\x02\x03",

            "#0103F敌人是躲在暗处操纵一切，\x01",
            "不露出真实面目，蜘蛛般的存在……\x02\x03",

            "#0100F但是，凭现在的我们，\x01",
            "一定可以将他揪出。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#6P#0204F……是的。\x02\x03",

            "#0201F我们……绝不会输的！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0000F#5P好……那就出发吧。\x02\x03",

            "#0003F克洛斯贝尔警察局·特别任务支援科，\x01",
            "罗伊德·班宁斯等四名队员──\x02\x03",

            "#0013F#5P为解决本次事件，\x01",
            "正式开始强行潜入调查……！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 6)
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x8, 0x0)
    OP_32(0x0, 0x10, 0x3)
    OP_32(0x1, 0x10, 0x3)
    OP_32(0x2, 0x10, 0x3)
    OP_32(0x3, 0x10, 0x3)
    OP_BA(0x0)
    OP_BA(0x1)
    OP_BA(0x2)
    OP_BA(0x3)
    RemoveCraft(0x0, 0xFFFF)
    RemoveCraft(0x1, 0xFFFF)
    RemoveCraft(0x2, 0xFFFF)
    RemoveCraft(0x3, 0xFFFF)
    AddCraft(0x0, 0xFFFF)
    AddCraft(0x1, 0xFFFF)
    AddCraft(0x2, 0xFFFF)
    AddCraft(0x3, 0xFFFF)
    OP_38(0x0, 0x7F, 0x0)
    OP_38(0x1, 0x7F, 0x0)
    OP_38(0x2, 0x7F, 0x0)
    OP_38(0x3, 0x7F, 0x0)
    OP_38(0x0, 0x80, 0x1)
    OP_38(0x1, 0x80, 0x1)
    OP_38(0x2, 0x80, 0x1)
    OP_38(0x3, 0x80, 0x1)
    SubItemNumber(0x270F, 99)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_1D7E")
    MiniGame(0x2A, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_1D7E")

    AddItemNumber(0x5, 1)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x5C, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1409 end

    def Function_6_1DC0(): pass

    label("Function_6_1DC0")

    OP_25(0x81, 0x64)
    Sleep(200)
    OP_25(0x81, 0x5A)
    Sleep(200)
    OP_25(0x81, 0x50)
    Sleep(200)
    OP_25(0x81, 0x46)
    Sleep(200)
    OP_25(0x81, 0x3C)
    Sleep(200)
    OP_25(0x81, 0x32)
    Sleep(200)
    OP_25(0x81, 0x28)
    Sleep(200)
    OP_25(0x81, 0x1E)
    Sleep(200)
    OP_25(0x81, 0x14)
    Sleep(200)
    OP_25(0x81, 0xA)
    Sleep(200)
    OP_25(0x81, 0x0)
    Return()

    # Function_6_1DC0 end

    def Function_7_1E0B(): pass

    label("Function_7_1E0B")

    Sleep(3000)
    Sound(800, 0, 100, 0)
    Return()

    # Function_7_1E0B end

    SaveToFile()

Try(main)
