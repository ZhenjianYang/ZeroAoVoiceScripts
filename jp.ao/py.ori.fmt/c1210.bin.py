from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1210.bin",                # FileName
        "c1210",                    # MapName
        "c1210",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1210",                  # 0
        "ツァオ",                 # 1
        "ラウ",                   # 2
        "シン",                   # 3
        "黒月構成員",             # 4
        "SE制御",                 # 5
    ))

    AddCharChip((
        "chr/ch06302.itc",                   # 00
        "chr/ch31400.itc",                   # 01
        "chr/ch45000.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-72300,  0,       1900,    500,     -72300,  1500,    1900,    0x007C, 0,  14, 0x0000)
    DeclActor(-37230,  0,       7940,    500,     -37230,  1500,    7940,    0x007C, 0,  14, 0x0000)
    DeclActor(5000,    0,       6440,    500,     5000,    1500,    6440,    0x007C, 0,  14, 0x0000)
    DeclActor(3430,    0,       70,      500,     5650,    1500,    40,      0x007E, 0,  3,  0x0000)

    ChipFrameInfo(504, 0)                                        # 0

    ScpFunction((
        "Function_0_1F8",          # 00, 0
        "Function_1_2A8",          # 01, 1
        "Function_2_3C3",          # 02, 2
        "Function_3_45A",          # 03, 3
        "Function_4_51B",          # 04, 4
        "Function_5_5DC",          # 05, 5
        "Function_6_6C2",          # 06, 6
        "Function_7_805",          # 07, 7
        "Function_8_D42",          # 08, 8
        "Function_9_28B7",         # 09, 9
        "Function_10_29D8",        # 0A, 10
        "Function_11_2C9E",        # 0B, 11
        "Function_12_3CBB",        # 0C, 12
        "Function_13_4EBB",        # 0D, 13
        "Function_14_4ECE",        # 0E, 14
    ))


    def Function_0_1F8(): pass

    label("Function_0_1F8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_230"),
        (1, "loc_23C"),
        (2, "loc_248"),
        (3, "loc_254"),
        (4, "loc_260"),
        (5, "loc_26C"),
        (6, "loc_278"),
        (SWITCH_DEFAULT, "loc_284"),
    )


    label("loc_230")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_23C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_248")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_254")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_260")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_26C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_278")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_2A7")

    Return()

    # Function_0_1F8 end

    def Function_1_2A8(): pass

    label("Function_1_2A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ED")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_301")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)
    Jump("loc_310")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33F")
    Event(0, 8)

    label("loc_33F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5800, 0, 1300, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x40)

    label("loc_385")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)

    label("loc_3C2")

    Return()

    # Function_1_2A8 end

    def Function_2_3C3(): pass

    label("Function_2_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D8")

    SetMapObjFrame(0xFF, "c122_tesri02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kuro01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_459")
    OP_66(0x3, 0x1)

    label("loc_459")

    Return()

    # Function_2_3C3 end

    def Function_3_45A(): pass

    label("Function_3_45A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A")
    Call(0, 9)
    Jump("loc_517")

    label("loc_48A")


    #C0001
    ChrTalk(
        0x8,
        (
            "#03200Fそれにしても、\x01",
            "皆さんに来ていただけて\x01",
            "本当に僥倖#4R ぎょうこう #でした。\x02\x03",

            "#03204Fどうかシン様のこと、\x01",
            "よろしくお願いしましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_517")

    TalkEnd(0x8)
    Return()

    # Function_3_45A end

    def Function_4_51B(): pass

    label("Function_4_51B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54B")
    Call(0, 9)
    Jump("loc_5D8")

    label("loc_54B")


    #C0002
    ChrTalk(
        0x8,
        (
            "#03200Fそれにしても、\x01",
            "皆さんに来ていただけて\x01",
            "本当に僥倖#4R ぎょうこう #でした。\x02\x03",

            "#03204Fどうかシン様のこと、\x01",
            "よろしくお願いしましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D8")

    TalkEnd(0x8)
    Return()

    # Function_4_51B end

    def Function_5_5DC(): pass

    label("Function_5_5DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_687")

    #C0003
    ChrTalk(
        0x9,
        (
            "引き受けて下さる場合は、\x01",
            "どうかお早めにお戻り下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "シン様はもちろん、我々の待てる\x01",
            "時間にも限りがございますので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BE")

    label("loc_687")


    #C0005
    ChrTalk(
        0x9,
        (
            "シン様、どうかお気をつけて\x01",
            "行ってらっしゃいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BE")

    TalkEnd(0xFE)
    Return()

    # Function_5_5DC end

    def Function_6_6C2(): pass

    label("Function_6_6C2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_801")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_787")

    #C0006
    ChrTalk(
        0xA,
        (
            "お姉さん、\x01",
            "ボクここで待っていますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        "必ず戻ってきてくださいね！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00100Fえっと、約束はできないけど……\x01",
            "善処させてもらうわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_801")

    label("loc_787")


    #C0009
    ChrTalk(
        0xA,
        (
            "用事かなにか知らないけど、\x01",
            "さっさと済ませて来るんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "お前たちに、断るなんて\x01",
            "選択肢はゆるされないんだからな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_801")

    TalkEnd(0xFE)
    Return()

    # Function_6_6C2 end

    def Function_7_805(): pass

    label("Function_7_805")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    SoundLoad(128)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 7200, 0, 0, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6000, 0, 1500, 135)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6000, 0, 0, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(9200, 1100, 0, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 2, 50, 0)
    OP_68(7200, 1100, 0, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0x8,
        (
            "#03204F──おやおや、面白い偶然だ。\x02\x03",

            "#03210F《黒の競売会》といい\x01",
            "やはり縁があるようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        "#5Pしかしツァオ様……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#5Pエルム湖の南岸に\x01",
            "一体何があるのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#03204Fさて、ここは“彼”の勘に\x01",
            "賭けてみるしかないでしょう。\x02\x03",

            "#03200F不良リーダーの魔人化に\x01",
            "《蛇》や《教会》の介入……\x02\x03",

            "少しでも死角を潰しておくに\x01",
            "越したことはありませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        "#5P……確かに。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xB, 0x80)
    Sound(886, 0, 50, 0)
    Sleep(150)
    Sound(886, 0, 40, 0)
    Sleep(150)
    Sound(886, 0, 40, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0016
    NpcTalk(
        0xB,
        "男の声",
        "──し、失礼します！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    OP_68(-3000, 700, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17500, 0)
    OP_68(4900, 1100, 0, 2000)
    MoveCamera(40, 19, 0, 2000)
    SetCameraDistance(19500, 2000)
    Sound(103, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B80():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B80)

    def lambda_B9A():

        label("loc_B9A")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_B9A")

    QueueWorkItem2(0x8, 2, lambda_B9A)
    Sleep(50)

    def lambda_BAF():

        label("loc_BAF")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_BAF")

    QueueWorkItem2(0x9, 2, lambda_BAF)

    def lambda_BC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BC1)
    WaitChrThread(0xB, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    #C0017
    ChrTalk(
        0x9,
        (
            "#11Pなんだ、ファン！\x01",
            "その取り乱しようは！？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        "#6Pも、申し訳ありません。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "#6Pその……今しがた監視班から\x01",
            "信じがたい報告がありましたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        "#11P信じがたい報告……？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#03205F…………………………………\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    Sound(318, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(800)

    #C0022
    ChrTalk(
        0x8,
        (
            "#03201F──ファン。\x01",
            "詳しい話を聞かせてください。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_805 end

    def Function_8_D42(): pass

    label("Function_8_D42")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0xA1, 0xFF, 0xFF)
    SetChrFlags(0x1A2, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    OP_4B(0x9, 0xFF)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(21120, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0023
    ChrTalk(
        0x8,
        (
            "#11P#03200Fやあ、いらっしゃいましたね。\x02\x03",

            "#03209Fようこそ《黒月貿易公司》へ。\x01",
            "歓迎させていただきますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#6P#00001F……お邪魔します。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#6P#00103Fお言葉に甘えて\x01",
            "上がらせていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#11P#03200Fフフ……\x01",
            "ランディさんもお久しぶりです。\x02\x03",

            "#03204F復帰を心待ちにしておりましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#6P#00303F……そいつはどうも。\x01",
            "アンタも相変わらずそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#11P#03204Fハハ、誉め言葉として\x01",
            "受け取らせていただきます。\x02\x03",

            "#03209Fいや～、しかしランディさんが\x01",
            "かのクリムゾン商会の関係者とは。\x02\x03",

            "さすがの私も驚かされましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        "#6P#00301Fハン……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#6P#00001Fどうやら“彼ら”について、\x01",
            "ある程度ご存知のようですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#11P#03204Fええ、実は少々、\x01",
            "縁が無いわけではありません。\x02\x03",

            "#03200Fひょっとしたらランディさんは\x01",
            "ご存知なのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#6P#00303Fああ……１年ほど前、\x01",
            "叔父貴たちが東方人街に潜入して\x01",
            "《黒月#4Rあんたら#》とやり合ったそうだな？\x02\x03",

            "#00301F結構本格的なドンパチを\x01",
            "やらかしたそうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_121B")

    #C0033
    ChrTalk(
        0x101,
        "#6P#00003F……そうだったな。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#6P#00108Fダドリーさんもそんな事を\x01",
            "言っていたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1272")

    label("loc_121B")


    #C0035
    ChrTalk(
        0x102,
        "#6P#00105Fそういえば……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#00003Fダドリーさんもそんな事を\x01",
            "言っていたな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1272")


    #C0037
    ChrTalk(
        0x8,
        (
            "#11P#03204Fフフ、まあ色々と\x01",
            "賑#2Rにぎ#わわせてくれたのは確かです。\x02\x03",

            "#03200F幸い、手打ちとなったので\x01",
            "お互い遺恨は残していませんが……\x02\x03",

            "#03209F黒月の長老の中には、\x01",
            "いまだに彼らの名前を聞いただけで\x01",
            "憤怒のあまり卒倒する方もいるかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x109,
        "#6P#10106Fそ、そこまで……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、さぞかし\x01",
            "色々とあったんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#11P#03203Fまあ、ルバーチェ跡地については\x01",
            "非常に残念ですが諦めました。\x02\x03",

            "#03200Fマフィア組織だったルバーチェと違い、\x01",
            "直接ビジネスで対立することも\x01",
            "少ないでしょうし……\x02\x03",

            "#03210Fその点については\x01",
            "安心していただいて結構ですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#00003F……これはご丁寧に。\x01",
            "（全く信用できないけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#6P#00105Fあの、それでは、\x01",
            "“頼みたいこと”というのは？\x02\x03",

            "#00103Fてっきりクリムゾン商会の\x01",
            "一件についてかと思ったのですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "はい、実は──\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 5080, 0, 7720, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)

    #N0044
    NpcTalk(
        0x1A2,
        "男の子の声",
        (
            "#5P#Nおそいぞ、ツァオ！\x01",
            "いったい何をしている！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)

    def lambda_16EF():

        label("loc_16EF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_16EF")

    QueueWorkItem2(0x101, 1, lambda_16EF)
    Sleep(50)

    def lambda_1704():

        label("loc_1704")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1704")

    QueueWorkItem2(0x102, 1, lambda_1704)
    Sleep(50)

    def lambda_1719():

        label("loc_1719")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1719")

    QueueWorkItem2(0x104, 1, lambda_1719)
    Sleep(50)

    def lambda_172E():

        label("loc_172E")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_172E")

    QueueWorkItem2(0x109, 1, lambda_172E)
    Sleep(50)

    def lambda_1743():

        label("loc_1743")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1743")

    QueueWorkItem2(0x105, 1, lambda_1743)
    Sleep(50)

    def lambda_1758():

        label("loc_1758")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1758")

    QueueWorkItem2(0x9, 1, lambda_1758)
    Sleep(300)
    OP_68(4460, 1100, 100, 3000)

    def lambda_177E():
        OP_95(0xFE, 5800, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_177E)
    Sleep(100)

    def lambda_179B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_179B)
    WaitChrThread(0x1A2, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x1)

    #C0045
    ChrTalk(
        0x8,
        "#11P#03200Fおお、これはシン様。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        "何か不都合がございましたか？\x02",
    )

    CloseMessageWindow()

    #N0047
    NpcTalk(
        0x1A2,
        "男の子",
        (
            "不都合もなにも、\x01",
            "いつまで待たせるつもりだ！\x02",
        )
    )

    CloseMessageWindow()

    #N0048
    NpcTalk(
        0x1A2,
        "男の子",
        (
            "いつになったら案内人を\x01",
            "連れてくるつもりなのだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "ですから、わたくし共でよければ\x01",
            "いくらでもご案内を──\x02",
        )
    )

    CloseMessageWindow()

    #N0050
    NpcTalk(
        0x1A2,
        "男の子",
        "だめだ、何度もいわせるな！\x02",
    )

    CloseMessageWindow()

    #N0051
    NpcTalk(
        0x1A2,
        "男の子",
        (
            "せっかくクロスベルに遊びに来たのに\x01",
            "お前たちの案内なんて興ざめだろう！？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P#03209Fフフ、そう仰られるので\x01",
            "この通り手配をしておきました。\x02\x03",

            "#03204F“彼ら”が案内人になります。\x02",
        )
    )

    CloseMessageWindow()

    #N0053
    NpcTalk(
        0x1A2,
        "男の子",
        "なに……？\x02",
    )

    CloseMessageWindow()
    OP_68(3470, 1000, -250, 1500)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1A55():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A55)
    Sleep(50)

    def lambda_1A65():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A65)
    Sleep(50)

    def lambda_1A75():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A75)
    Sleep(50)

    def lambda_1A85():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A85)
    Sleep(50)

    def lambda_1A95():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A95)
    Sleep(300)

    #C0054
    ChrTalk(
        0x101,
        "#6P#00005Fあ、あの、ツァオ支社長……？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x109,
        (
            "#6P#10105Fひょっとして\x01",
            "“頼みたいこと”って……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(50)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(300)

    #C0056
    ChrTalk(
        0x8,
        (
            "#11P#03200Fフフ、ご紹介します。\x02\x03",

            "#03204Fこちらはシン様といいまして、\x01",
            "《黒月》のさる長老の\x01",
            "お孫さんでいらっしゃいます。\x02\x03",

            "#03209F皆さんにはぜひ、\x01",
            "シン様にクロスベル市内を\x01",
            "案内していただきたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#6P#00106Fや、やっぱり……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#6P#00306Fおいおい、マジかよ？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x105,
        "#6P#10300Fフフ、とんだお願いだね。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x1A2,
        (
            "#11Pこいつらが案内人～？\x01",
            "まだワカゾウじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x1A2,
        (
            "#11Pイリア・プラティエとか、\x01",
            "ディーター・クロイスとか、\x01",
            "連れてこられないのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)

    #C0062
    ChrTalk(
        0x8,
        (
            "#11P#03209Fハハ、さすがに\x01",
            "それは難しそうですが……\x02\x03",

            "#03200F彼らもなかなか、\x01",
            "クロスベルでは有名人ですよ？\x02\x03",

            "#03204F何しろ、例の事件を解決した\x01",
            "立役者でもありますからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0063
    ChrTalk(
        0x1A2,
        "#11Pへえ、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A2,
        (
            "#11Pお前たちが教団事件を解決した\x01",
            "《特務支援課》というわけか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x0)

    def lambda_1F03():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F03)
    Sleep(50)

    def lambda_1F13():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1F13)
    Sleep(50)

    def lambda_1F23():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1F23)
    Sleep(50)

    def lambda_1F33():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F33)
    Sleep(50)

    def lambda_1F43():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F43)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#6P#00005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#6P#00105Fど、どうしてそれを……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "長老のお孫さんだけあって\x01",
            "シン様はなかなかの情報通でして。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "クロスベルに来られるにあたって\x01",
            "一通りのお勉強はされたそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x1A2,
        "#11Pフフン、当然だ。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x1A2,
        (
            "#11P長老たるおじいさまの孫として\x01",
            "ボクはいずれ《黒月》の未来を\x01",
            "背負う立場にあるんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x1A2,
        (
            "#11Pお前たちボンゾクとは\x01",
            "心がまえからしてちがうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#6P#00306F（このガキ……）\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x109,
        "#6P#10102F（まあまあ、ランディ先輩。）\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x1A2,
        (
            "#11Pまあ、どうしてもと言うなら\x01",
            "認めてやらなくもないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x1A2,
        (
            "#11P教団事件のときの話を\x01",
            "聞いてやってもいいしな──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0076
    ChrTalk(
        0x1A2,
        "#11Pえ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0077
    ChrTalk(
        0x101,
        "#6P#00005F？？？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        "#6P#00105Fど、どうしたの？\x02",
    )

    CloseMessageWindow()

    def lambda_227E():

        label("loc_227E")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_227E")

    QueueWorkItem2(0x101, 1, lambda_227E)
    Sleep(50)

    def lambda_2293():

        label("loc_2293")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2293")

    QueueWorkItem2(0x102, 1, lambda_2293)
    Sleep(50)

    def lambda_22A8():

        label("loc_22A8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22A8")

    QueueWorkItem2(0x104, 1, lambda_22A8)
    Sleep(50)

    def lambda_22BD():

        label("loc_22BD")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22BD")

    QueueWorkItem2(0x109, 1, lambda_22BD)
    Sleep(50)

    def lambda_22D2():

        label("loc_22D2")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_22D2")

    QueueWorkItem2(0x105, 1, lambda_22D2)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    TurnDirection(0x1A2, 0x102, 500)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x1A2,
        "#11Pう、#800Wう、#800Wう……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0080
    ChrTalk(
        0x1A2,
        "#11P#5S運命の女性#4Rひと#だ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x1)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    OP_95(0x1A2, 2800, 0, 2150, 4000, 0x0)

    def lambda_23BD():
        OP_95(0xFE, 2300, 0, 470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_23BD)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_23EC():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23EC)

    def lambda_2401():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2401)

    def lambda_2416():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2416)

    def lambda_242B():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_242B)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    TurnDirection(0x101, 0x1A2, 500)

    #C0081
    ChrTalk(
        0x101,
        "#6P#00011Fわわっ……！？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#12P#00105Fきゃっ……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x1A2,
        (
            "うるわしいまなざし！\x01",
            "つややかなパールグレイの髪！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x1A2,
        (
            "そして包容力のある\x01",
            "ステキなぷろぽーしょん！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x1A2,
        (
            "こ、こんなところでボクの\x01",
            "理想のヒトに出あえるなんて！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x1A2,
        (
            "お姉さん！\x01",
            "お名前はなんていうんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#12P#00100Fえっと……\x01",
            "エリィよ、エリィ・マクダエル。\x02\x03",

            "#00109Fふふっ、よろしくね、シン君。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x1A2,
        (
            "エリィお姉さん……\x01",
            "……名前もステキだ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x1A2,
        (
            "そうか、ボクはこのヒトに会いに\x01",
            "クロスベルまで来たんだな……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x101,
        "#6P#00005F（な、何というか……）\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#6P#00306F（ったく、小生意気だけじゃなくて\x01",
            "  とんだマセガキじゃねーか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        (
            "#6P#10109F（あはは……\x01",
            "  エリィさん、モテモテですね。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0093
    ChrTalk(
        0x1A2,
        "#6Pツァオ、気にいったぞ！\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x1A2,
        (
            "#6Pこのお姉さんにさっそく\x01",
            "案内してもらうことにする！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#11P#03204Fフフ、それはようございました。\x02\x03",

            "#03209F──それでは皆さん。\x01",
            "シン様をよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#6P#00011Fちょ、ちょっと待ってください！\x02\x03",

            "#00003F（黒月長老の孫の案内……\x01",
            "  このまま受けてもいいのか？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x73, 0x4, 0x2)
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_8_D42 end

    def Function_9_28B7(): pass

    label("Function_9_28B7")

    EventBegin(0x0)
    Fade(500)
    AddParty(0xA1, 0xFF, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x1A2, 5800, 0, 1300, 270)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0097
    ChrTalk(
        0x8,
        (
            "#11P#03200Fどうです、ロイドさん？\x02\x03",

            "シン様のクロスベル案内を\x01",
            "お願いしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_9_28B7 end

    def Function_10_29D8(): pass

    label("Function_10_29D8")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "依頼を受ける\x01",        # 0
            "いったん考える\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A44"),
        (1, "loc_2A4C"),
        (SWITCH_DEFAULT, "loc_2C48"),
    )


    label("loc_2A44")

    Call(0, 11)
    Jump("loc_2C48")

    label("loc_2A4C")


    #C0098
    ChrTalk(
        0x101,
        (
            "#6P#00003Fすみません。\x01",
            "今は手を離せなくて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0099
    ChrTalk(
        0x1A2,
        (
            "#11Pな、なんだと……？\x01",
            "このボクの案内を断るのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#12P#00106Fごめんね、シン君。\x01",
            "用事が片付けばいいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#6P#00000Fえっと、後でまた改めて\x01",
            "引き受ける形でもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#11P#03204Fええ、もちろん構いませんよ。\x02\x03",

            "#03200Fただし、シン様をあまり\x01",
            "お待たせするのも忍びませんし。\x02\x03",

            "その場合は早めにお戻り下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x1A2,
        "#11P待ってるからな、早くしろよ！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0xA1, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5800, 0, 1300, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x40)
    SetScenarioFlags(0x154, 6)
    Jump("loc_2C48")

    label("loc_2C48")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 900, 0, 50, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)
    EventEnd(0x5)
    Return()

    # Function_10_29D8 end

    def Function_11_2C9E(): pass

    label("Function_11_2C9E")


    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#00003F……分かりました。\x01",
            "お引き受けしましょう。\x02\x03",

            "#00000Fそれで具体的な\x01",
            "市内案内の流れですが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_END)), "loc_2F19")

    #C0105
    ChrTalk(
        0x8,
        (
            "#11P#03200Fああ、そのあたりは\x01",
            "シン様から直接お聞き下さい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    #C0106
    ChrTalk(
        0x8,
        (
            "#11P#03209Fそれではシン様。\x01",
            "お気をつけて行ってらっしゃいませ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0107
    ChrTalk(
        0x1A2,
        "#6Pああ、分かった！\x02",
    )

    CloseMessageWindow()

    def lambda_2DC0():

        label("loc_2DC0")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DC0")

    QueueWorkItem2(0x101, 1, lambda_2DC0)
    Sleep(50)

    def lambda_2DD5():

        label("loc_2DD5")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DD5")

    QueueWorkItem2(0x102, 1, lambda_2DD5)
    Sleep(50)

    def lambda_2DEA():

        label("loc_2DEA")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DEA")

    QueueWorkItem2(0x104, 1, lambda_2DEA)
    Sleep(50)

    def lambda_2DFF():

        label("loc_2DFF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2DFF")

    QueueWorkItem2(0x109, 1, lambda_2DFF)
    Sleep(50)

    def lambda_2E14():

        label("loc_2E14")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2E14")

    QueueWorkItem2(0x105, 1, lambda_2E14)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    SetChrSubChip(0x8, 0x0)
    OP_95(0x1A2, 2800, 0, 2150, 2000, 0x0)

    def lambda_2E80():
        OP_95(0xFE, 2300, 0, 470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2E80)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2EAF():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EAF)

    def lambda_2EC4():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EC4)

    def lambda_2ED9():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2ED9)

    def lambda_2EEE():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2EEE)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)
    Jump("loc_2FAE")

    label("loc_2F19")


    #C0108
    ChrTalk(
        0x8,
        (
            "#11P#03200Fああ、そのあたりは\x01",
            "シン様から直接お聞き下さい。\x02\x03",

            "#03209Fそれではシン様。\x01",
            "お気をつけて行ってらっしゃいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1A2,
        "#6Pああ、分かった！\x02",
    )

    CloseMessageWindow()

    label("loc_2FAE")

    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0110
    ChrTalk(
        0x1A2,
        (
            "#5P──さあお姉さん、\x01",
            "さっそく行きましょう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2FEF():
        OP_95(0xFE, 1310, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2FEF)

    def lambda_3009():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3009)

    def lambda_3016():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3016)

    def lambda_3023():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3023)
    WaitChrThread(0x109, 1)

    def lambda_3034():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3034)

    def lambda_3049():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3049)

    def lambda_305E():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_305E)
    OP_68(930, 1100, -390, 1500)
    WaitChrThread(0x109, 1)

    def lambda_3088():

        label("loc_3088")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_3088")

    QueueWorkItem2(0x101, 1, lambda_3088)
    Sleep(50)

    def lambda_309D():

        label("loc_309D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_309D")

    QueueWorkItem2(0x104, 1, lambda_309D)
    Sleep(50)

    def lambda_30B2():

        label("loc_30B2")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_30B2")

    QueueWorkItem2(0x109, 1, lambda_30B2)
    Sleep(50)

    def lambda_30C7():

        label("loc_30C7")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_30C7")

    QueueWorkItem2(0x105, 1, lambda_30C7)

    def lambda_30D9():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_30D9)

    def lambda_30F3():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_30F3)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x102,
        "#11P#00105Fちょ、ちょっとシン君……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#5P#00005Fえっと、まさかそのまま\x01",
            "２人で市内を行くつもりかい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0113
    ChrTalk(
        0x1A2,
        (
            "#12Pえ～、だってぞろぞろ\x01",
            "行動するのはウザイだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1A2,
        (
            "#12Pそれに、ボクはお姉さんと\x01",
            "２人っきりがいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#5P#00001Fうーん、そうは言ってもな。\x02\x03",

            "#00003F（さすがに長老の孫だからといって\x01",
            "  狙われる事はないと思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#11P#00103F……コホン。\x02\x03",

            "#00100Fシン君、今は通商会議前だから\x01",
            "何があるか正直分からないわ。\x02\x03",

            "#00104F君の安全のことを考えると\x01",
            "護衛はいた方がいいと思うけど？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0117
    ChrTalk(
        0x1A2,
        (
            "#6Pう～ん、お姉さんが\x01",
            "そう言うのなら仕方ないか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0118
    ChrTalk(
        0x1A2,
        (
            "#12Pじゃあ、あと２名だな。\x01",
            "それでボクたちを守ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1A2,
        (
            "#12Pもう２名はそうだな……\x01",
            "つかず離れずくらいの距離で\x01",
            "見守っててくれればいいや。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x1A2,
        "#12Pそれでどうだ？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#5P#00005Fへえ……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        "#5P#00303F……何気に的を射てやがるな。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x109,
        (
            "#5P#10100Fええ、要人警護としては\x01",
            "効果的な配置ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x105,
        "#11P#10300Fフフ、決まりだね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0125
    ChrTalk(
        0x105,
        (
            "#11P#10300F護衛の一人は君として、\x01",
            "もう一人は誰にするんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#5P#00003Fそうだな……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ランディに同行してもらう】\x01",      # 0
            "【ノエルに同行してもらう】\x01",        # 1
            "【ワジに同行してもらう】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_365B"),
        (1, "loc_37C3"),
        (2, "loc_3921"),
        (SWITCH_DEFAULT, "loc_3A84"),
    )


    label("loc_365B")

    SetScenarioFlags(0x1C4, 6)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0127
    ChrTalk(
        0x101,
        (
            "#11P#00000Fそれじゃ、ランディ。\x01",
            "一緒に来てもらえるか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0128
    ChrTalk(
        0x104,
        (
            "#6P#00300Fおうよ、了解だ。\x02\x03",

            "#00304Fそんじゃま、適度に気合いを入れて\x01",
            "案内＆護衛任務と行こうぜ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0129
    ChrTalk(
        0x101,
        (
            "#11P#00000F後の２人は彼の言う通り、\x01",
            "様子を窺#2Rうかが#いながら\x01",
            "後ろから付いてきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0130
    ChrTalk(
        0x109,
        "#6P#10100F分かりました。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        "#12P#10300Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A84")

    label("loc_37C3")

    SetScenarioFlags(0x1C4, 7)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0132
    ChrTalk(
        0x101,
        (
            "#11P#00000Fそれじゃ、ノエル。\x01",
            "一緒に来てくれるかい。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0133
    ChrTalk(
        0x109,
        (
            "#6P#10100Fええ、分かりました。\x02\x03",

            "#10101F観光だからと気を抜かず\x01",
            "しっかり護衛して行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#11P#00000F後の２人は彼の言う通り、\x01",
            "様子を窺#2Rうかが#いながら\x01",
            "後ろから付いてきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0135
    ChrTalk(
        0x104,
        "#6P#00300Fおうよ、任せとけ。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x105,
        "#12P#10300Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A84")

    label("loc_3921")

    SetScenarioFlags(0x1C5, 0)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0137
    ChrTalk(
        0x101,
        (
            "#5P#00000Fそれじゃ、ワジ。\x01",
            "一緒に来てもらっていいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、了解。\x02\x03",

            "#10302Fこうなったら、とことん\x01",
            "付き合おうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0139
    ChrTalk(
        0x101,
        (
            "#11P#00000F後の２人は彼の言う通り、\x01",
            "様子を窺#2Rうかが#いながら\x01",
            "後ろから付いてきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A28():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A28)
    Sleep(50)

    def lambda_3A38():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A38)
    Sleep(300)

    #C0140
    ChrTalk(
        0x104,
        "#6P#00300Fおうよ、任せとけ。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x109,
        "#6P#10100F了解です。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A84")

    label("loc_3A84")

    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        (
            "#5P#00000F……さてと。\x01",
            "こんな所でいいか、シン君？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3ACA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3ACA)
    Sleep(50)

    def lambda_3ADA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3ADA)
    Sleep(50)

    def lambda_3AEA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3AEA)
    Sleep(300)

    #C0143
    ChrTalk(
        0x1A2,
        "#12Pああ、いいぞ。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x1A2,
        (
            "#12Pそれとボクのことはシンと呼べ。\x01",
            "お前たちは別に黒月じゃないしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#5P#00009Fはは……分かった、シン。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x1A2,
        (
            "#12Pよし！\x01",
            "それじゃ、早く外に行くぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x1A2,
        (
            "#12P行きたいトコとか、\x01",
            "詳しい話は外でするからな！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【シン少年への市街地案内】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 1)
    OP_29(0x73, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 900, 0, 50, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_2C9E end

    def Function_12_3CBB(): pass

    label("Function_12_3CBB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3420, 0, 3170, 180)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x1A2, 5800, 0, 1300, 180)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0149
    AnonymousTalk(
        0x8,
        (
            "#11P#03204F#N──フフ、楽しんで\x01",
            "来られたようで何よりです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_END)), "loc_3E15")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_END)), "loc_3E28")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_END)), "loc_3E3B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_3E4E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_END)), "loc_3E61")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_3E74")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_END)), "loc_3E87")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_END)), "loc_3E9A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_END)), "loc_3EAD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3F6C")

    #C0150
    ChrTalk(
        0x1A2,
        "#5Pああ、とても有意義だった！\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1A2,
        (
            "#5Pクロスベルは、アルカンシェルや\x01",
            "テーマパークだけじゃないんだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x1A2,
        (
            "#5Pお前のようなキレモノが\x01",
            "こだわる理由もわかる気がするぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4047")

    label("loc_3F6C")


    #C0153
    ChrTalk(
        0x1A2,
        "#5Pああ、とても有意義だった！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x1A2,
        (
            "#5P実はもう少し\x01",
            "見たいところもあったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x1A2,
        (
            "#5Pクロスベルは、アルカンシェルや\x01",
            "テーマパークだけじゃないんだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x1A2,
        (
            "#5Pお前のようなキレモノが\x01",
            "こだわる理由もわかる気がするぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4047")


    #C0157
    ChrTalk(
        0x8,
        "#11P#03200Fはは、これは恐れ入ります。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0158
    ChrTalk(
        0x8,
        (
            "#11P#03200Fロイドさん、エリィさん。\x01",
            "他の皆さんも。\x02\x03",

            "#03209Fこんなにシン様が喜ばれるとは\x01",
            "思ってもおりませんでしたよ。\x02\x03",

            "#03204Fありがとうございます。\x01",
            "どうもお疲れさまでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#6P#00000Fいえ、そんな。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#6P#00102Fふふ、私たちも\x01",
            "楽しませてもらいました。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 2580, 0, 1630, 2000, 0x0)

    def lambda_41A0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_41A0)
    Sleep(50)

    def lambda_41B0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41B0)
    Sleep(50)

    def lambda_41C0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_41C0)
    Sleep(50)

    def lambda_41D0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41D0)
    Sleep(50)

    def lambda_41E0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41E0)
    Sleep(50)

    def lambda_41F0():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_41F0)
    Sleep(300)

    #C0161
    ChrTalk(
        0x9,
        (
            "──ささやかですが\x01",
            "こちらをお受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ、自分たちは警察なので\x01",
            "そういったものを受け取るわけには──\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#11P#03204Fフフ、そう仰るだろうと思って\x01",
            "ミラでの謝礼は止めておきました。\x02\x03",

            "#03210Fわたくしどもではなく\x01",
            "シン様との#10R㈲  ㈲  ㈲  ㈲  ㈲#お近づきの印として\x01",
            "受け取っていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_43B6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43B6)
    Sleep(50)

    def lambda_43C6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43C6)
    Sleep(50)

    def lambda_43D6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43D6)
    Sleep(50)

    def lambda_43E6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43E6)
    Sleep(50)

    def lambda_43F6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43F6)
    Sleep(300)

    #C0164
    ChrTalk(
        0x101,
        "#6P#00011Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#6P#00105Fそれは……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0166
    ChrTalk(
        0x1A2,
        "#5Pツァオ、気がきくじゃないか！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0167
    ChrTalk(
        0x1A2,
        (
            "#11Pうんうん、遠慮はいらない！\x01",
            "もっていくがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        "#6P#00306F（やりやがるな……）\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        (
            "#6P#10302F（フフ、そんな風に言われたら\x01",
            "  受け取らざるを得ないよね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        "#6P#10106F（た、確かに。）\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#6P#00001F……分かりました。\x01",
            "ミラでないのであれば。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        "#6P#00100Fありがたく頂戴しますね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4604")
    OP_29(0x73, 0x1, 0xD)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x53),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x53, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_4657")

    label("loc_4604")

    OP_29(0x73, 0x1, 0xE)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0174
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x47),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x47, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4657")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0175
    ChrTalk(
        0x101,
        (
            "#6P#00000Fそれでは自分たちは\x01",
            "このあたりで失礼します。\x02\x03",

            "#00009F──シン、またな？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0176
    ChrTalk(
        0x102,
        "#6P#00109Fふふっ、元気でね？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0177
    ChrTalk(
        0x1A2,
        "#11Pああ、お姉さんたちも壮健でな！\x02",
    )

    CloseMessageWindow()

    def lambda_471A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_471A)
    Sleep(100)

    def lambda_472A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_472A)
    Sleep(100)

    def lambda_473A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_473A)
    Sleep(100)

    def lambda_474A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_474A)
    Sleep(100)

    def lambda_475A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_475A)
    WaitChrThread(0x104, 1)

    def lambda_476B():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_476B)
    WaitChrThread(0x109, 1)

    def lambda_4789():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4789)
    WaitChrThread(0x105, 1)

    def lambda_47A7():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_47A7)
    WaitChrThread(0x101, 1)

    def lambda_47C5():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47C5)
    WaitChrThread(0x102, 1)

    def lambda_47E3():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_47E3)

    def lambda_47FD():

        label("loc_47FD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_47FD")

    QueueWorkItem2(0x9, 1, lambda_47FD)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)
    OP_68(4059, 1100, 340, 4000)
    MoveCamera(41, 23, 0, 4000)
    OP_6E(380, 4000)
    SetCameraDistance(21210, 4000)
    BeginChrThread(0xC, 1, 0, 13)
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x102, 1)
    Sleep(2000)
    OP_64(0xFFFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    EndChrThread(0x9, 0x1)

    #C0178
    ChrTalk(
        0x1A2,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    def lambda_48A8():

        label("loc_48A8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_48A8")

    QueueWorkItem2(0x9, 1, lambda_48A8)
    Sleep(300)

    #C0179
    ChrTalk(
        0x8,
        (
            "#11P#03200Fフフ、街歩きをされて\x01",
            "お疲れになったようですね。\x02\x03",

            "#03204Fお部屋の方に珍しいお菓子を\x01",
            "用意させておりますよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0180
    ChrTalk(
        0x1A2,
        (
            "#5Pそ、そうか。\x01",
            "お前は本当に気がきくな。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x1A2,
        (
            "#5Pうんうん、おじいさまにも\x01",
            "ちゃんと報告しておくからな！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4950, 1100, 3350, 3000)
    OP_95(0x1A2, 5000, 0, 5850, 2000, 0x0)
    OP_6F(0x1)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)

    def lambda_4A01():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_4A01)
    Sleep(500)

    def lambda_4A1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_4A1E)
    Sleep(500)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)
    OP_6F(0x1)
    EndChrThread(0x9, 0x1)
    OP_68(5090, 1100, 880, 3000)
    OP_6F(0x1)

    #C0182
    ChrTalk(
        0x8,
        (
            "#11P#03204Fフフ、幼いながらも聡明で\x01",
            "大器の片鱗をうかがわせますね。\x02\x03",

            "#03202F将来私の力となリ得るのか……\x01",
            "なかなか楽しみですよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    #C0183
    ChrTalk(
        0x9,
        "#6P……はい。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "#6Pしかし、それならば\x01",
            "今回の件はやりすぎでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "#6P万が一“彼ら”が\x01",
            "シン様を狙ったりすれば、\x01",
            "ツァオ様の責任問題にも……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0186
    ChrTalk(
        0x8,
        (
            "#11P#03200Fフフ、そうなれば彼と私の天運も\x01",
            "そこまでだっただけのこと。\x02\x03",

            "#03204Fそれに“彼ら”も、このタイミングで\x01",
            "事を起こすほど愚かではないでしょう。\x02\x03",

            "#03201Fそれで──動きはありましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "#6Pは、シン様たちを尾行していた\x01",
            "対象者２名を捕捉。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "#6P現在それぞれ監視を付けています。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "#11P#03204F結構、そのまま気づかれないよう\x01",
            "泳がせておいてください。\x02\x03",

            "#03200F“商会”の方々からの横槍には\x01",
            "くれぐれも気を付けるように。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        "#6Pかしこまりました。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【シン少年への市街地案内】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x1000)
    OP_49()
    OP_D7(0x1E)
    RemoveParty(0xA1, 0xFF)
    OP_29(0x73, 0x4, 0x10)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_4DE2")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E0B")

    label("loc_4DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_4DF9")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_4E0B")

    label("loc_4DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_4E0B")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4E0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4E24")
    OP_2C(0x73, 0x3)
    Jump("loc_4E92")

    label("loc_4E24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E51")
    OP_2C(0x73, 0x2)
    Jump("loc_4E92")

    label("loc_4E51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E7E")
    OP_2C(0x73, 0x1)
    Jump("loc_4E92")

    label("loc_4E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_4E92")
    OP_2C(0x73, 0x0)

    label("loc_4E92")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0xFA0)
    WaitBGM()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 6)
    NewScene("c1200", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3CBB end

    def Function_13_4EBB(): pass

    label("Function_13_4EBB")

    Sleep(1300)
    Sound(103, 0, 100, 0)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    Return()

    # Function_13_4EBB end

    def Function_14_4ECE(): pass

    label("Function_14_4ECE")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_4ECE end

    SaveToFile()

Try(main)
