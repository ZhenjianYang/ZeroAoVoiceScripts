from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9014.bin",                # FileName
        "m9014",                    # MapName
        "m9014",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9014",                  # 0
        "キーア",                 # 1
        "キーア",                 # 2
        "SE制御",                 # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(336, 0)                                        # 0

    ScpFunction((
        "Function_0_150",          # 00, 0
        "Function_1_160",          # 01, 1
        "Function_2_165",          # 02, 2
        "Function_3_17F7",         # 03, 3
        "Function_4_1833",         # 04, 4
        "Function_5_1853",         # 05, 5
        "Function_6_1877",         # 06, 6
        "Function_7_18A2",         # 07, 7
        "Function_8_18DA",         # 08, 8
        "Function_9_190C",         # 09, 9
        "Function_10_1930",        # 0A, 10
        "Function_11_1954",        # 0B, 11
        "Function_12_1993",        # 0C, 12
        "Function_13_19B7",        # 0D, 13
        "Function_14_19E2",        # 0E, 14
        "Function_15_1A06",        # 0F, 15
        "Function_16_1A38",        # 10, 16
        "Function_17_1A9F",        # 11, 17
        "Function_18_1AD1",        # 12, 18
        "Function_19_1B4B",        # 13, 19
        "Function_20_1B75",        # 14, 20
        "Function_21_1C06",        # 15, 21
        "Function_22_1C97",        # 16, 22
        "Function_23_1D28",        # 17, 23
        "Function_24_1D6C",        # 18, 24
        "Function_25_1DA0",        # 19, 25
    ))


    def Function_0_150(): pass

    label("Function_0_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_15F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_15F")

    Return()

    # Function_0_150 end

    def Function_1_160(): pass

    label("Function_1_160")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_160 end

    def Function_2_165(): pass

    label("Function_2_165")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10800.itc", 0x1E)
    LoadChrToIndex("chr/ch10801.itc", 0x1F)
    LoadChrToIndex("apl/ch51757.itc", 0x21)
    LoadChrToIndex("apl/ch51753.itc", 0x22)
    LoadChrToIndex("apl/ch51754.itc", 0x23)
    LoadEffect(0x0, "battle/cr036301.eff")
    SoundLoad(3336)
    SoundLoad(3649)
    SoundLoad(3650)
    SoundLoad(3651)
    SoundLoad(3652)
    SoundLoad(3653)
    SoundLoad(3654)
    SoundLoad(111)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, -2250, 0, 2500, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xD0, 0xD0, 0xD0, 0xFF, 0x0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 400, 0, 0, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 400, -500, 0, 180)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x1)
    SetMapObjFrame(0xFF, "point16_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break00_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break01_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break02_add", 0x2, "night")
    SetMapObjFrame(0xFF, "break03_add", 0x2, "night")
    SetMapObjFrame(0xFF, "yuka00", 0x2, "night")
    SetMapObjFrame(0xFF, "point_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm02_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm03_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm04_add", 0x2, "night")
    SetMapObjFrame(0xFF, "pnrm05_add", 0x2, "night")
    OP_68(400, 850, 0, 0)
    MoveCamera(330, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(48000, 0)
    Sound(111, 2, 50, 0)
    FadeToBright(3000, 0)
    SetCameraDistance(38000, 9000)
    PlaceName2(340, 200, "c_plac69", 0x0, 3000)
    Sleep(6000)
    OP_A7(0x8, 0xE0, 0xE0, 0xE0, 0xFF, 0xBB8)
    OP_6F(0x79)
    Fade(1000)
    SetCameraDistance(15000, 0)
    SetCameraDistance(14000, 2000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#11P#60W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #N0002
    NpcTalk(
        0x101,
        "声",
        "#3336V#5P#N#40W#16A───見付けた。\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_68(-200, 850, 460, 2500)
    MoveCamera(330, 17, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(12800, 2500)
    BeginChrThread(0x101, 0, 0, 3)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12305F#11P#60W#15A………………………………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0004
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#3649V#11P#60W#25A……どう……して………？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(800)

    #C0005
    ChrTalk(
        0x101,
        (
            "#00000F#5P#30W声が、聞こえたからさ。\x02\x03",

            "#00004Fいつだって俺は……\x01",
            "キーアの声が聞こえていた。\x02\x03",

            "耳を澄ませて、感じていたら……\x02\x03",

            "#00002Fキーアの心の声が……\x01",
            "……何処にいるかが分かったよ。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)

    #C0006
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12314F#11P#40Wそっか……えへへ……\x02\x03",

            "#12308F……でもキーア……\x01",
            "ロイドにそんな風にしてもらう\x01",
            "資格なんてない……\x02\x03",

            "#12306Fだって……だってキーアは……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#00003F#5P#30Wキーア、それは違う。\x02\x03",

            "#00013F生まれがどうであろうと──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0008
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12311F#3650V#11P#4S#30W#20Aちがわないよう！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetCameraDistance(11500, 30000)
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    #C0009
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#40Wキーアは本物の人間じゃないし、\x01",
            "心や魂だって本物じゃない……！\x02\x03",

            "そんな風に優しくしてもらえる、\x01",
            "守ってもらえる資格なんてなかった！\x02\x03",

            "#12311Fそれなのに……\x01",
            "……それなのにキーアは……っ！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    def lambda_7E1():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7E1)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_801():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_801)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0010
    ChrTalk(
        0x101,
        "#00008F#5P#40W……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x8, 0)
    SetCameraDistance(10400, 100000)
    PlayBGM("ed7581", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x245), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)

    #C0011
    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W──なあ、キーア。\x02\x03",

            "キーアが俺たちの所に来てから\x01",
            "半年以上経って……\x02\x03",

            "#00004Fどれだけの幸せを\x01",
            "俺たちにくれたと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    #C0013
    ChrTalk(
        0x101,
        (
            "#00000F#5P#30W多分それはキーアが感じた\x01",
            "幸せと同じか、それ以上だと思う。\x02\x03",

            "#00002Fキーアはさ……\x01",
            "俺たちといて楽しくなかったか？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0014
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12307F#12P#30W楽しかった……！\x01",
            "すごく……シアワセだった……！\x02\x03",

            "#12311Fでもそれは……\x01",
            "ロイドたちがそう感じるように\x01",
            "キーアが仕向けただけかもしれない！\x02\x03",

            "大切なみんなの心を\x01",
            "操っていただけかもしれない！\x02\x03",

            "#12316F#40Wそんなのって……\x01",
            "………そんなのって……………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_AE8():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AE8)
    WaitChrThread(0x8, 2)
    Sleep(500)

    def lambda_B08():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B08)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0015
    ChrTalk(
        0x101,
        "#00001F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0)
    BeginChrThread(0x101, 1, 0, 10)
    WaitChrThread(0x101, 1)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 11)
    WaitChrThread(0x101, 1)

    #C0016
    ChrTalk(
        0x101,
        "#00003F#5P#30Wこら。\x02",
    )

    CloseMessageWindow()

    def lambda_B8D():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B8D)
    WaitChrThread(0x8, 2)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    BeginChrThread(0x101, 1, 0, 14)
    WaitChrThread(0x101, 1)

    #C0017
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30Wあのな……\x01",
            "きっかけはどうかは知らないよ。\x02\x03",

            "#00004F俺たちには操られた実感も無いし、\x01",
            "それに、そんな風にだったら\x01",
            "別に操られたって構わないと思う。\x02\x03",

            "#00000F仔猫や人間の赤ちゃんだって\x01",
            "無条件に愛らしくて\x01",
            "守りたくなる存在だろう？\x02\x03",

            "キーアのそうした“力”だって\x01",
            "せいぜいその程度じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#12P#40W…………ぁ……………\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00004F#5Pそして、俺たちの過ごした時間は\x01",
            "そんな“力”なんかじゃ測れない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis311.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0020
    AnonymousTalk(
        0x101,
        (
            "#40W#3C俺と一緒に、料理の練習をしたり\x01",
            "同じベッドで寝て寝坊したこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis386.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)

    #A0021
    AnonymousTalk(
        0x101,
        (
            "#40W#3Cエリィと一緒に本を読んだり、\x01",
            "みんなの洗濯物を屋上に干したこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis387.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)

    #A0022
    AnonymousTalk(
        0x101,
        (
            "#40W#3Cティオと一緒に掃除をしたり、\x01",
            "みっしぃの限定グッズを買ったこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis388.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#40W#3Cランディと一緒にポーカーをしたり、\x01",
            "露店街に買い出しに行ったこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis389.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(500)

    #A0024
    AnonymousTalk(
        0x101,
        (
            "#40W#3C課長と洗い物をしたり、\x01",
            "ツァイトたちと昼寝をしたこと。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    CreatePortrait(1, 0, 8, 480, 264, 0, 8, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis390.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x5DC, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    #C0025
    ChrTalk(
        0x101,
        (
            "#00000F#5P──それが“嘘”だったなんて\x01",
            "本当にキーアは思うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12308F#12P#40W………それ……は……………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)
    BeginChrThread(0x8, 1, 0, 16)
    WaitChrThread(0x8, 1)
    Sleep(300)

    #C0027
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12306F#12P#40W………嘘じゃ……ないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00002F#5P#30Wだったらそれが\x01",
            "俺たちにとっての“真実”だ。\x02\x03",

            "#00004Fそしてその“真実”がある限り……\x02\x03",

            "この先、どんな困難が迫ろうと\x01",
            "俺たちは決して負けはしない。\x02\x03",

            "#00000Fだからキーア……\x01",
            "一人で全部背負う必要はないんだ。\x02\x03",

            "それは、キーアも含めて\x01",
            "俺たち全員で頑張ればいいんだから。\x02\x03",

            "#00009Fそれが“仲間”で……\x01",
            "“家族”っていうものだろう？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 15)
    WaitChrThread(0x101, 1)
    OP_C9(0x0, 0x80000000)

    #C0029
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12317F#3651V#12P#40W#40A……ロイ……ド…………\x02\x03",

            "#12316F#3652V#50W#60Aロイド……ロイドおおぉっ……！\x02",
        )
    )
    #Auto

    Sleep(3000)
    BeginChrThread(0x8, 1, 0, 17)
    WaitChrThread(0x8, 1)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0xA, 1, 0, 25)
    PlayEffect(0x0, 0xFF, 0x8, 0x41, 0, 350, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x10)
    Sleep(1000)
    OP_68(-400, 850, 400, 1000)
    MoveCamera(330, 17, 0, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(10000, 1000)
    BeginChrThread(0x8, 1, 0, 18)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0030
    ChrTalk(
        0x8,
        (
            "#05817F#3653V#12P#40W#58A……ぅぅっ……ぁぁああっ……！\x02\x03",

            "#3654V#45A#4Sわぁぁぁぁぁぁぁっ……！\x02",
        )
    )
    #Auto

    Sleep(8000)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(500)

    #C0031
    ChrTalk(
        0x101,
        (
            "#00002F#5P#30W……キーア………\x02\x03",

            "#00004Fはは……\x01",
            "相変わらずいいタックルだ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 19)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 1, 0, 20)
    BeginChrThread(0x8, 1, 0, 21)
    Sleep(1000)
    BeginChrThread(0xA, 1, 0, 24)
    SetMapObjFrame(0xFF, "point16_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break00_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break01_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break02_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "break03_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "yuka00", 0x2, "to_d")
    SetMapObjFrame(0xFF, "point_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm02_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm03_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm04_add", 0x2, "to_d")
    SetMapObjFrame(0xFF, "pnrm05_add", 0x2, "to_d")
    Sleep(2500)

    #C0032
    ChrTalk(
        0x101,
        (
            "#00004F#5P#55A#30W──さあ、帰ろう。\x01",
            "みんなが俺たちを待っている。\x02\x03",

            "#00002F#40Aこのまま抱っこするから\x01",
            "ちゃんと掴まっているんだぞ？\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0033
    ChrTalk(
        0x8,
        "#05818F#12P#25A#40Wうんっ……うんっ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 22)
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 1, 0, 23)
    Sleep(700)
    OP_68(0, 500, 0, 4000)
    MoveCamera(205, 13, 0, 4000)
    OP_6E(700, 4000)
    SetCameraDistance(11500, 4000)
    OP_6F(0x79)
    Sleep(1500)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(111, 1000, 40)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("m9012", 0, 20, 0)
    IdleLoop()
    Return()

    # Function_2_165 end

    def Function_3_17F7(): pass

    label("Function_3_17F7")

    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    def lambda_1808():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1808)
    OP_9B(0x1, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
    CancelBlur(0)
    Sleep(300)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_3_17F7 end

    def Function_4_1833(): pass

    label("Function_4_1833")

    Sleep(300)

    def lambda_183B():
        OP_A6(0xFE, 0x19, 0x0, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_183B)
    Sleep(500)
    Return()

    # Function_4_1833 end

    def Function_5_1853(): pass

    label("Function_5_1853")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(111)
    SetChrSubChip(0xFE, 0x2)
    Sleep(111)
    SetChrSubChip(0xFE, 0x3)
    Sleep(333)
    Return()

    # Function_5_1853 end

    def Function_6_1877(): pass

    label("Function_6_1877")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(300)
    Return()

    # Function_6_1877 end

    def Function_7_18A2(): pass

    label("Function_7_18A2")

    OP_9B(0x0, 0xFE, 0xD, 0x6A4, 0x3E8, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(200)
    Sound(812, 0, 60, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x14)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Fade(250)
    OP_0D()
    Return()

    # Function_7_18A2 end

    def Function_8_18DA(): pass

    label("Function_8_18DA")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x14)
    Sleep(167)
    SetChrSubChip(0xFE, 0x13)
    Sleep(167)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_8_18DA end

    def Function_9_190C(): pass

    label("Function_9_190C")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0x1)
    Sleep(167)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    Return()

    # Function_9_190C end

    def Function_10_1930(): pass

    label("Function_10_1930")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0x6)
    Sleep(167)
    SetChrSubChip(0xFE, 0x7)
    Sleep(500)
    Return()

    # Function_10_1930 end

    def Function_11_1954(): pass

    label("Function_11_1954")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(571)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x8, 0x7)
    BeginChrThread(0x8, 1, 0, 12)
    SetChrSubChip(0xFE, 0xA)
    Sleep(429)
    WaitChrThread(0x8, 1)
    Return()

    # Function_11_1954 end

    def Function_12_1993(): pass

    label("Function_12_1993")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    Sleep(429)
    Return()

    # Function_12_1993 end

    def Function_13_19B7(): pass

    label("Function_13_19B7")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0xC)
    Sleep(571)
    Return()

    # Function_13_19B7 end

    def Function_14_19E2(): pass

    label("Function_14_19E2")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_14_19E2 end

    def Function_15_1A06(): pass

    label("Function_15_1A06")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x2)
    Sleep(429)
    Return()

    # Function_15_1A06 end

    def Function_16_1A38(): pass

    label("Function_16_1A38")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xF)
    Sleep(100)
    SetChrSubChip(0xFE, 0xE)
    Sleep(100)
    SetChrSubChip(0xFE, 0xD)
    Sleep(100)
    SetChrSubChip(0xFE, 0xC)
    Return()

    # Function_16_1A38 end

    def Function_17_1A9F(): pass

    label("Function_17_1A9F")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xC)
    Sleep(125)
    SetChrSubChip(0xFE, 0xB)
    Sleep(125)
    SetChrSubChip(0xFE, 0xA)
    Sleep(125)
    SetChrSubChip(0xFE, 0x9)
    Sleep(125)
    SetChrSubChip(0xFE, 0x8)
    Sleep(500)
    Return()

    # Function_17_1A9F end

    def Function_18_1AD1(): pass

    label("Function_18_1AD1")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0xFE, 0x10)
    Sleep(125)
    SetChrSubChip(0xFE, 0x11)
    Sleep(125)
    SetChrSubChip(0xFE, 0x12)
    Sleep(125)
    SetChrFlags(0xFE, 0x20)
    OP_9D(0xFE, 0x96, 0x0, 0x0, 0x32, 0x3E8)
    ClearChrFlags(0xFE, 0x20)
    Sound(812, 0, 100, 0)

    def lambda_1B26():
        OP_A6(0xFE, 0x1E, 0x0, 0x3E8, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B26)
    SetChrSubChip(0xFE, 0x13)
    Sleep(50)
    Sound(811, 0, 80, 0)
    Sleep(325)
    Return()

    # Function_18_1AD1 end

    def Function_19_1B4B(): pass

    label("Function_19_1B4B")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 20, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_19_1B4B end

    def Function_20_1B75(): pass

    label("Function_20_1B75")

    SetChrChipByIndex(0x101, 0x23)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0x11)
    Sleep(130)
    SetChrSubChip(0xFE, 0x10)
    Sleep(130)
    SetChrSubChip(0xFE, 0xF)
    Sleep(130)
    SetChrSubChip(0xFE, 0xE)
    Return()

    # Function_20_1B75 end

    def Function_21_1C06(): pass

    label("Function_21_1C06")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x16)
    Sleep(130)
    SetChrSubChip(0xFE, 0x15)
    Sleep(130)
    SetChrSubChip(0xFE, 0x14)
    Sleep(130)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_21_1C06 end

    def Function_22_1C97(): pass

    label("Function_22_1C97")

    Fade(500)
    OP_68(-400, 950, 400, 800)
    SetCameraDistance(11000, 800)
    Sound(802, 0, 50, 0)
    Sound(898, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xF)
    SetChrFlags(0x8, 0x8)
    OP_0D()
    SetChrSubChip(0xFE, 0xF)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(167)
    SetChrSubChip(0xFE, 0xC)
    Sleep(500)
    SetChrSubChip(0xFE, 0x10)
    Sleep(167)
    SetChrSubChip(0xFE, 0x11)
    Sleep(167)
    SetChrSubChip(0xFE, 0x10)
    Sleep(167)
    SetChrSubChip(0xFE, 0xF)
    Sleep(833)
    Return()

    # Function_22_1C97 end

    def Function_23_1D28(): pass

    label("Function_23_1D28")

    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    OP_93(0xFE, 0xB4, 0x0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x1F)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x1)
    Return()

    # Function_23_1D28 end

    def Function_24_1D6C(): pass

    label("Function_24_1D6C")

    Sleep(100)
    Sound(1022, 0, 100, 0)
    Sleep(3300)
    Sound(1022, 0, 100, 0)
    Sleep(3300)
    Sound(1022, 0, 100, 0)
    Sleep(3400)
    Sound(1022, 0, 100, 0)
    Sleep(1500)
    Sound(934, 0, 70, 0)
    Sound(1002, 0, 100, 0)
    Return()

    # Function_24_1D6C end

    def Function_25_1DA0(): pass

    label("Function_25_1DA0")

    Sound(934, 0, 100, 0)
    Sleep(1000)
    Sound(222, 0, 50, 0)
    Sleep(500)
    Sound(928, 0, 100, 0)
    Return()

    # Function_25_1DA0 end

    SaveToFile()

Try(main)
