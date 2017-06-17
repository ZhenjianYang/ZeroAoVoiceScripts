from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3500.bin",                # FileName
        "e3500",                    # MapName
        "e3500",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 3, 0, 4],
    )

    BuildStringList((
        "e3500",                  # 0
        "セルゲイ課長",           # 1
        "キーア",                 # 2
        "ツァイト",               # 3
        "ロイド",                 # 4
        "エリィ",                 # 5
        "ティオ",                 # 6
        "ランディ",               # 7
        "キーア影",               # 8
        "ロイド影",               # 9
        "エリィ影",               # 10
        "ティオ影",               # 11
        "ランディ影",             # 12
    ))

    AddCharChip((
        "chr/ch02500.itc",                   # 00
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_218",          # 00, 0
        "Function_1_234",          # 01, 1
        "Function_2_253",          # 02, 2
        "Function_3_30B",          # 03, 3
        "Function_4_31B",          # 04, 4
        "Function_5_31C",          # 05, 5
        "Function_6_147D",         # 06, 6
        "Function_7_14A2",         # 07, 7
        "Function_8_1571",         # 08, 8
        "Function_9_15CD",         # 09, 9
        "Function_10_161E",        # 0A, 10
        "Function_11_1690",        # 0B, 11
    ))


    def Function_0_218(): pass

    label("Function_0_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_233")
    OP_A1(0xFE, 0x4B0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_218")

    label("loc_233")

    Return()

    # Function_0_218 end

    def Function_1_234(): pass

    label("Function_1_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_252")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_1_234")

    label("loc_252")

    Return()

    # Function_1_234 end

    def Function_2_253(): pass

    label("Function_2_253")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_293"),
        (1, "loc_29F"),
        (2, "loc_2AB"),
        (3, "loc_2B7"),
        (4, "loc_2C3"),
        (5, "loc_2CF"),
        (6, "loc_2DB"),
        (SWITCH_DEFAULT, "loc_2E7"),
    )


    label("loc_293")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_29F")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2AB")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2B7")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2C3")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2CF")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2DB")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2E7")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_2F3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30A")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F3")

    label("loc_30A")

    Return()

    # Function_2_253 end

    def Function_3_30B(): pass

    label("Function_3_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E, 0)), scpexpr(EXPR_END)), "loc_31A")
    ClearScenarioFlags(0x5E, 0)
    Event(0, 5)

    label("loc_31A")

    Return()

    # Function_3_30B end

    def Function_4_31B(): pass

    label("Function_4_31B")

    Return()

    # Function_4_31B end

    def Function_5_31C(): pass

    label("Function_5_31C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("apl/ch50561.itc", 0x1F)
    LoadChrToIndex("apl/ch50563.itc", 0x20)
    LoadChrToIndex("apl/ch50564.itc", 0x21)
    LoadChrToIndex("apl/ch50565.itc", 0x22)
    LoadChrToIndex("apl/ch50567.itc", 0x23)
    LoadChrToIndex("apl/ch50568.itc", 0x24)
    LoadChrToIndex("apl/ch50569.itc", 0x25)
    LoadChrToIndex("apl/ch50570.itc", 0x26)
    LoadChrToIndex("apl/ch50571.itc", 0x27)
    LoadChrToIndex("apl/ch50572.itc", 0x28)
    SetChrPos(0x101, -300, 0, 2200, 90)
    SetChrPos(0x102, -300, 0, 1200, 45)
    SetChrPos(0x104, -1100, 0, 3400, 135)
    SetChrPos(0x103, 0, 0, 3600, 135)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 1900, 0, 2200, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, 2000, 0, 4100, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 4000, 30, 2200, 270)
    BeginChrThread(0xA, 0, 0, 1)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0xA)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis177.itp")
    CreatePortrait(1, 13, 87, 269, 215, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis178.itp")
    CreatePortrait(2, 13, 178, 269, 306, 0, 0, 256, 128, 0, 0, 256, 128, 0xFFFFFF, 0x1, "c_vis179.itp")
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30Wそして────\x02\x03",

            "白熱した市長選が終わり、\x01",
            "俺たちが通常業務に戻った日……\x02\x03",

            "特務支援課の玄関に\x01",
            "真新しいカバンを持った\x01",
            "キーアの姿があった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7105", 0)
    OP_68(1010, 1100, 2620, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(20500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0002
    ChrTalk(
        0x101,
        (
            "#6P#0006Fうーん、本当に大丈夫か？\x02\x03",

            "#0001Fやっぱり初日くらいは\x01",
            "俺も付いていった方が……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#11P#1103Fだいじょうぶ。\x01",
            "ちゃんと道も覚えたモン。\x02\x03",

            "#1100Fそれにリュウとアンリも\x01",
            "いっしょに行くんだし。\x02\x03",

            "#1110Fロイド、心配しょーすぎ！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        "#6P#0011Fで、でもなぁ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0005
    ChrTalk(
        0x102,
        (
            "#12P#0106Fまったくもう……\x01",
            "本当に親バカなんだから。\x02\x03",

            "#0111Fあなただって小さな頃は\x01",
            "子供たちだけで日曜学校に\x01",
            "通っていたんでしょう？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    #C0006
    ChrTalk(
        0x101,
        "#5P#0012Fまあ、それはそうだけど……\x02",
    )

    CloseMessageWindow()

    def lambda_7A5():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7A5)
    Sleep(100)

    def lambda_7B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7B5)
    Sleep(50)

    def lambda_7C5():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7C5)
    WaitChrThread(0x104, 2)

    #C0007
    ChrTalk(
        0x103,
        (
            "#5P#0202F……そういうエリィさんも\x01",
            "そわそわしまくってませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#12P#0112Fう……\x02\x03",

            "#0113Fこ、これはその、\x01",
            "保護者の性#2Rさが#というか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#5P#0304F……やれやれ。\x01",
            "せっかくのキー坊の晴れの日だ。\x02\x03",

            "#0300Fもう狙われる事も無いんだし、\x01",
            "せめてきちんと見送ってやろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        "#11P#1200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0011
    ChrTalk(
        0x101,
        (
            "#12P#0006Fいやまあ……\x01",
            "分かっちゃいるんだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#12P#0106F……何だか子供を持つ\x01",
            "親の気持ちが判る気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P#1004Fクク……\x02\x03",

            "#1002F──お前らこそ、新市長から\x01",
            "相談に呼ばれてるんだろう？\x02\x03",

            "そろそろ出かけたらどうだ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9F9():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9F9)
    Sleep(100)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)

    def lambda_A11():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A11)

    def lambda_A1E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A1E)
    Sleep(50)

    def lambda_A2E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A2E)
    Sleep(50)

    def lambda_A3E():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A3E)
    WaitChrThread(0x104, 2)

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ、はい……\x02\x03",

            "#0000F……それなんですけど\x01",
            "課長、ご存知なんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        "#6P#0205F一体どんな相談なんですか？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#5P#1004Fクク、それは新市長から\x01",
            "直接聞いた方がいいだろう。\x02\x03",

            "#1002F──とにかく今日は\x01",
            "お前たち全員にとって\x01",
            "新たな一日になるはずだ。\x02\x03",

            "せいぜいしっかりやって来い。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#6P#0002F……分かりました。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#3P#0309Fやれやれ。\x01",
            "また忙しくなりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#6P#0204Fまあ、忙しいのは\x01",
            "いつもの事ですけれど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)

    #C0020
    ChrTalk(
        0x102,
        (
            "#6P#0102Fそれじゃあ、キーアちゃん。\x01",
            "通りまで一緒に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    def lambda_C4D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C4D)
    Sleep(50)

    def lambda_C5D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C5D)
    Sleep(50)

    def lambda_C6D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_C6D)
    Sleep(50)

    def lambda_C7D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_C7D)
    Sleep(50)

    def lambda_C8D():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C8D)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 6)
    Sleep(500)

    #C0021
    ChrTalk(
        0x9,
        "#11P#1109Fうんっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x1)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xC, 0x1)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x2)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x1)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x1)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x212), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0x9, 301000, 0, 2500, 0)
    SetChrPos(0xB, 300250, 0, 2650, 0)
    SetChrPos(0xC, 299700, 0, 3600, 0)
    SetChrPos(0xD, 301750, 0, 2700, 0)
    SetChrPos(0xE, 302300, 0, 3900, 0)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x1)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x100)
    SetChrFlags(0xF, 0x800)
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0xF, 0xFFFEA070, 0x2BF20, 0x0, 0x0)
    OP_52(0xF, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x100)
    SetChrFlags(0x10, 0x800)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x10, 0xFFFEA070, 0x2BF20, 0xFFFFEC78, 0x0)
    OP_52(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x1)
    SetChrChipByIndex(0x11, 0x26)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x100)
    SetChrFlags(0x11, 0x800)
    OP_52(0x11, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x11, 0xFFFEA070, 0x2BF20, 0xFFFFCD38, 0x0)
    OP_52(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x12, 0x1)
    SetChrChipByIndex(0x12, 0x24)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x100)
    SetChrFlags(0x12, 0x800)
    OP_52(0x12, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x12, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x12, 0xFFFEA070, 0x2BF20, 0x1388, 0x0)
    OP_52(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x2)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x13, 0x1)
    SetChrChipByIndex(0x13, 0x25)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x100)
    SetChrFlags(0x13, 0x800)
    OP_52(0x13, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x80, 0x0)
    OP_D3(0x13, 0xFFFEA070, 0x2BF20, 0x32C8, 0x0)
    OP_52(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    OP_E3(0xA)
    WaitBGM()
    Sleep(10)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ed.pmf", 0x3, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(500)
    Sound(2043, 255, 90, 0)    #voice#KeA
    Sleep(1600)
    Sound(2179, 255, 90, 1)    #voice#KeA
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_57(0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    Sleep(500)
    OP_DE(0x29, 0x0)
    OP_DE(0x1B, 0x0)
    OP_DE(0x1C, 0x0)
    OP_DE(0x1D, 0x0)
    OP_DE(0x80, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1387")
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "ＥＸＴＲＡモードが開放されました。\x02",
        )
    )

    CloseMessageWindow()

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "タイトル画面から\x01",
            "ＥＸＴＲＡモードに入ることができます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    label("loc_1387")

    SetMessageWindowPos(14, 280, 60, 3)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　　　　　 ～　クリアデータのセーブについて　～\x01",
            "　　  クリアデータを作成し、タイトル画面からロードすると\x01",
            "　　  各種データを引き継いだまま２周目を開始できます。",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveClearMenu()
    OP_57(0x0)
    OP_5A()
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C7(0x1, 0x10)
    OP_B7(0x0)
    Return()

    # Function_5_31C end

    def Function_6_147D(): pass

    label("Function_6_147D")

    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x3)
    Sleep(110)
    SetChrSubChip(0x9, 0x4)
    Sleep(110)
    SetChrSubChip(0x9, 0x5)
    Sleep(110)
    SetChrSubChip(0x9, 0x4)
    Sleep(110)
    SetChrSubChip(0x9, 0x3)
    Return()

    # Function_6_147D end

    def Function_7_14A2(): pass

    label("Function_7_14A2")

    Sleep(150)
    SetChrChipByIndex(0xF, 0x27)
    SetChrSubChip(0xFE, 0x7)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(400)
    SetChrSubChip(0xFE, 0xF)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(110)
    SetChrSubChip(0xFE, 0xE)
    Sleep(110)
    SetChrSubChip(0xFE, 0xD)
    Sleep(110)
    SetChrSubChip(0xFE, 0x10)
    Sleep(110)
    SetChrSubChip(0xFE, 0x21)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(110)
    SetChrSubChip(0xFE, 0x22)
    Sleep(110)
    SetChrSubChip(0xFE, 0x23)
    Sleep(110)
    SetChrSubChip(0xFE, 0x24)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(110)
    SetChrSubChip(0xFE, 0x25)
    Sleep(110)
    SetChrSubChip(0xFE, 0x20)
    Sleep(110)
    SetChrSubChip(0xFE, 0x21)
    OP_A7(0xF, 0x0, 0x0, 0x0, 0x50, 0x0)
    Return()

    # Function_7_14A2 end

    def Function_8_1571(): pass

    label("Function_8_1571")

    Sleep(300)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    OP_A7(0x10, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(1400)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(3100)
    Return()

    # Function_8_1571 end

    def Function_9_15CD(): pass

    label("Function_9_15CD")

    Sleep(600)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(500)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(3000)
    Return()

    # Function_9_15CD end

    def Function_10_161E(): pass

    label("Function_10_161E")

    Sleep(900)
    SetChrSubChip(0xFE, 0x0)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    OP_A7(0x13, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(700)
    SetChrSubChip(0xFE, 0x6)
    Sleep(50)
    SetChrSubChip(0xFE, 0x7)
    Sleep(50)
    SetChrSubChip(0xFE, 0x8)
    Sleep(50)
    SetChrSubChip(0xFE, 0x9)
    Sleep(3000)
    Return()

    # Function_10_161E end

    def Function_11_1690(): pass

    label("Function_11_1690")

    Sleep(450)
    SetChrSubChip(0xFE, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x1)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x50, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    Sleep(70)
    SetChrSubChip(0xFE, 0x4)
    OP_A7(0x11, 0x0, 0x0, 0x0, 0x80, 0x0)
    Sleep(70)
    SetChrSubChip(0xFE, 0x5)
    Sleep(70)
    SetChrSubChip(0xFE, 0x6)
    Sleep(1100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x7)
    Sleep(100)
    SetChrSubChip(0xFE, 0x6)
    Sleep(2300)
    Return()

    # Function_11_1690 end

    SaveToFile()

Try(main)
