from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ＳＥ制御",               # 1
        "bm3080",                 # 2
        "bm3080",                 # 3
    ))

    ATBonus("ATBonus_298", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_205D", 4,   4,   20,  0,   16,  12,  7)
    Sepith("Sepith_2065", 0,   29,  0,   0,   9,   3,   19)

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
        "BattleInfo_440", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3080", "Sepith_205D", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7402", "ed7403", "ATBonus_298"),
        )
    )

    BattleInfo(
        "BattleInfo_378", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3080", "Sepith_2065", 60, 25, 10, 5,
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
        "Function_3_76A",          # 03, 3
        "Function_4_8DB",          # 04, 4
        "Function_5_153B",         # 05, 5
        "Function_6_1FE0",         # 06, 6
        "Function_7_202B",         # 07, 7
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_733")
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
            "#56I地のセピス×２００\x01\x07\x02",

            "#57I水のセピス×２００\x01\x07\x02",

            "#58I火のセピス×２００\x01\x07\x02",

            "#59I風のセピス×２００\x01\x07\x02",

            "#60I時のセピス×２００\x01\x07\x02",

            "#61I空のセピス×２００\x01\x07\x02",

            "#62I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11E, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_758")

    label("loc_733")


    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_758")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_5F9 end

    def Function_3_76A(): pass

    label("Function_3_76A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A4")
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
            "#56I地のセピス×２００\x01\x07\x02",

            "#57I水のセピス×２００\x01\x07\x02",

            "#58I火のセピス×２００\x01\x07\x02",

            "#59I風のセピス×２００\x01\x07\x02",

            "#60I時のセピス×２００\x01\x07\x02",

            "#61I空のセピス×２００\x01\x07\x02",

            "#62I幻のセピス×２００\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x11E, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_8C9")

    label("loc_8A4")


    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8C9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_76A end

    def Function_4_8DB(): pass

    label("Function_4_8DB")

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

    def lambda_9A5():
        OP_96(0xFE, 0xFFFF7FE0, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A5)

    def lambda_9BF():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BF)

    def lambda_9D9():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0x384, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D9)
    Sleep(50)

    def lambda_9F6():
        OP_96(0xFE, 0xFFFF7680, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9F6)
    Sleep(50)

    def lambda_A13():
        OP_96(0xFE, 0xFFFF7234, 0x1770, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A13)

    def lambda_A2D():
        OP_96(0xFE, 0xFFFF7234, 0x1770, 0x258, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_A2D)
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
        "#0010F#5Pここは……！？\x02",
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
        "#0813F凄い……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0108F地の底に続く縦穴……\x01",
            "なんて大きさなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x108,
        (
            "#0901Fこれも数百年前に\x01",
            "建造された物なのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0301Fここからの目測だと\x01",
            "深さ５００アージュって所か。\x02\x03",

            "#0306Fやれやれ……\x01",
            "こいつは骨が折れそうだぜ。\x02",
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

    def lambda_D2D():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D2D)
    WaitChrThread(0x103, 2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x108, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_DAD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DAD)
    Sleep(100)

    def lambda_DBD():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DBD)

    def lambda_DCA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DCA)
    Sleep(50)

    def lambda_DDA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_DDA)
    TurnDirection(0x108, 0x103, 500)

    #C0011
    ChrTalk(
        0x101,
        "#0011F#5Pティオ、どうした？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0101F#11P大丈夫？\x01",
            "真っ青な顔をしてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#6P#0206F……問題ないです。\x02\x03",

            "#0208Fただ、昔いた場所のことを\x01",
            "少し思い出してしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0003F#5P昔いた場所……そうか。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0301F#5P共和国の西端にあったっていう\x01",
            "教団の拠点#4Rロッジ#のことだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            "#6P#0203F…………はい。\x02\x03",

            "#0208Fたぶん、この縦穴は\x01",
            "《煉獄》に続く黄泉路を見立てて\x01",
            "建造されたんだと思います。\x02\x03",

            "女神#4Rエイドス#を否定する概念としての\x01",
            "悪魔に近づき、利用するため……\x02\x03",

            "#0201Fそして彼らに供物を奉げる\x01",
            "《儀式》を執り行うために。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        "#0106F#11P……最低の連中ね。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0310F#5Pハッ、道理で\x01",
            "辛気臭い匂いがするわけだ。\x02",
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
            "#0008F#5P──だったら\x01",
            "俺たちの仕事は一つだけだ。\x02\x03",

            "#0003F俺たちの道を\x01",
            "拓いてくれた人たちのためにも。\x02\x03",

            "そして、俺たちの帰りを\x01",
            "待っているキーアのためにも……\x02\x03",

            "#0013Fその辛気臭い幻想を叩き壊して\x01",
            "陽の光の下に引きずり出してやる！\x02\x03",

            "もう誰も、辛くて哀しい思いを\x01",
            "しなくて済むように……！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x103,
        "#6P#0205F………ロイドさん…………\x02",
    )

    CloseMessageWindow()

    def lambda_11BE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11BE)
    Sleep(50)

    def lambda_11CE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11CE)
    Sleep(50)

    def lambda_11DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_11DE)
    OP_93(0x108, 0x5A, 0x1F4)
    Sleep(300)

    #C0021
    ChrTalk(
        0x104,
        (
            "#6P#0304Fったく、熱血野郎と\x01",
            "言いたいところだが……\x02\x03",

            "#0300Fま、今回ばかりは\x01",
            "そいつに一枚乗せてもらうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふ、私も乗った。\x02\x03",

            "#0103F敵は、全てを陰から操っていた\x01",
            "得体の知れない蜘蛛のような存在……\x02\x03",

            "#0100Fでも、今の私たちなら\x01",
            "きっと届くことが出来るはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#6P#0204F……はい。\x02\x03",

            "#0201F絶対に……負けません！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x107,
        "#0800F#12Pあたしたちも力を貸すわ！\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x108,
        "#0901F#6P全力で君たちを支援する！\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0000F#5Pよし……それじゃあ行こう。\x02\x03",

            "#0003Fクロスベル警察・特務支援課所属、\x01",
            "ロイド・バニングス以下４名──\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x107,
        (
            "#0801F#12P同じく遊撃士協会所属、\x01",
            "エステル・ブライト以下２名──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0028
    ChrTalk(
        0x101,
        (
            "#0007F#5Pこれより事件解決のため\x01",
            "強制潜入捜査を開始する……！\x02",
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

    # Function_4_8DB end

    def Function_5_153B(): pass

    label("Function_5_153B")

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

    def lambda_15CF():
        OP_96(0xFE, 0xFFFF7FE0, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15CF)
    Sleep(50)

    def lambda_15EC():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0xFFFFFC7C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15EC)
    Sleep(50)

    def lambda_1609():
        OP_96(0xFE, 0xFFFF7A04, 0x1770, 0x384, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1609)
    Sleep(50)

    def lambda_1626():
        OP_96(0xFE, 0xFFFF7680, 0x1770, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1626)
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
        "#0010F#5Pここは……！？\x02",
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
            "#0108F地の底に続く縦穴……\x01",
            "なんて大きさなのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#0301Fここからの目測だと\x01",
            "深さ５００アージュって所か。\x02\x03",

            "#0306Fやれやれ……\x01",
            "こいつは骨が折れそうだぜ。\x02",
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

    def lambda_18A5():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_18A5)
    WaitChrThread(0x103, 2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1901():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1901)
    Sleep(100)

    def lambda_1911():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1911)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0033
    ChrTalk(
        0x101,
        "#0011F#5Pティオ、どうした？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#0101F#11P大丈夫？\x01",
            "真っ青な顔をしてるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#6P#0206F……問題ないです。\x02\x03",

            "#0208Fただ、昔いた場所のことを\x01",
            "少し思い出してしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0003F#5P昔いた場所……そうか。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x104,
        (
            "#0301F#5P共和国の西端にあったっていう\x01",
            "連中の拠点のことだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        (
            "#6P#0203F…………はい。\x02\x03",

            "#0208Fたぶん、この縦穴は\x01",
            "《煉獄》に続く黄泉路を見立てて\x01",
            "建造されたんだと思います。\x02\x03",

            "女神#4Rエイドス#を否定する概念としての\x01",
            "悪魔に近づき、利用するため……\x02\x03",

            "#0201Fそして彼らに供物を奉げる\x01",
            "《儀式》を執り行うために。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        "#0106F#11P……最低の連中ね。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0310F#5Pハッ、道理で\x01",
            "辛気臭い匂いがするわけだ。\x02",
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
            "#0008F#5P──だったら\x01",
            "俺たちの仕事は一つだけだ。\x02\x03",

            "#0003F俺たちの道を\x01",
            "拓いてくれた人たちのためにも。\x02\x03",

            "そして、俺たちの帰りを\x01",
            "待っているあの子のためにも……\x02\x03",

            "#0013Fその辛気臭い幻想を叩き壊して\x01",
            "陽の光の下に引きずり出してやる！\x02\x03",

            "もう誰も、辛くて哀しい思いを\x01",
            "しなくて済むように……！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#6P#0205F………ロイドさん…………\x02",
    )

    CloseMessageWindow()

    def lambda_1CE1():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1CE1)
    Sleep(50)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(300)

    #C0043
    ChrTalk(
        0x104,
        (
            "#6P#0304Fったく、熱血野郎と\x01",
            "言いたいところだが……\x02\x03",

            "#0300Fま、今回ばかりは\x01",
            "そいつに一枚乗せてもらうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#0102Fふふ、私も乗った。\x02\x03",

            "#0103F敵は、全てを陰から操っていた\x01",
            "得体の知れない蜘蛛のような存在……\x02\x03",

            "#0100Fでも、今の私たちなら\x01",
            "きっと届くことが出来るはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#6P#0204F……はい。\x02\x03",

            "#0201F絶対に……負けません！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#0000F#5Pよし……それじゃあ行こう。\x02\x03",

            "#0003Fクロスベル警察・特務支援課所属、\x01",
            "ロイド・バニングス以下４名──\x02\x03",

            "#0013F#5Pこれより事件解決のため\x01",
            "強制潜入捜査を開始する……！\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_END)), "loc_1F9E")
    MiniGame(0x2A, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)

    label("loc_1F9E")

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

    # Function_5_153B end

    def Function_6_1FE0(): pass

    label("Function_6_1FE0")

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

    # Function_6_1FE0 end

    def Function_7_202B(): pass

    label("Function_7_202B")

    Sleep(3000)
    Sound(800, 0, 100, 0)
    Return()

    # Function_7_202B end

    SaveToFile()

Try(main)
