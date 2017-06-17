from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c121b.bin",                # FileName
        "c121b",                    # MapName
        "c121b",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 0, 0, 1],
    )

    BuildStringList((
        "c121b",                  # 0
        "ツァオ",                 # 1
        "ラウ",                   # 2
        "銀",                     # 3
        "構成員",                 # 4
        "構成員",                 # 5
        "SE制御",                 # 6
    ))

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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_1EC",          # 01, 1
        "Function_2_1ED",          # 02, 2
        "Function_3_EEB",          # 03, 3
        "Function_4_1C35",         # 04, 4
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_1DC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_1EB")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_1EB")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 3)

    label("loc_1EB")

    Return()

    # Function_0_1C8 end

    def Function_1_1EC(): pass

    label("Function_1_1EC")

    Return()

    # Function_1_1EC end

    def Function_2_1ED(): pass

    label("Function_2_1ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06302.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch00500.itc", 0x20)
    OP_68(4450, 900, 130, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 0, 0, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 7300, 0, 3300, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00700.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    LoadEffect(0x0, "event\\ev202_00.eff")
    SetCameraDistance(23000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sleep(300)

    #C0001
    ChrTalk(
        0x9,
        "#5P──以上が今週の成果です。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            "#5P連中が投入してきた軍用犬が\x01",
            "いささか厄介ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#5P《銀#2Rイン#》殿さえいれば、戦力面での\x01",
            "不足は補えるのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "#11P#3203Fふむ、分かりました。\x02\x03",

            "#3200F市内での体制はこのまま継続。\x02\x03",

            "あとはそうですね……\x01",
            "アルタイル市に派遣した人員を\x01",
            "半分ほど呼び戻してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        "#5P承知しました。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#5Pそれではツァオ様。\x01",
            "お休みなさいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "#11P#3209Fええ、お疲れさま。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x10E, 0x1F4)
    OP_68(2790, 900, 630, 2000)

    def lambda_50F():
        OP_95(0xFE, -4500, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_50F)
    Sleep(3000)
    Sound(103, 0, 100, 0)

    def lambda_532():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_532)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Sleep(200)
    Sound(104, 0, 100, 0)
    Sleep(1300)
    Fade(500)
    OP_68(5030, 900, 220, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20760, 0)
    OP_0D()
    Sleep(500)

    #C0008
    ChrTalk(
        0x8,
        (
            "#11P#3201Fふう……困りましたね。\x02\x03",

            "長老方の助けを借りるのは\x01",
            "さすがに後が恐いですし……\x02\x03",

            "#3206Fやれやれ……\x01",
            "《銀》殿がもう少し\x01",
            "協力的だと助かるんですが。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1628, 255, 100, 0)    #voice#Yin
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    Sleep(500)

    #N0009
    NpcTalk(
        0xA,
        "声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#N……契約分はきちんと\x01",
            "働いているつもりだがな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(5680, 900, 1890, 3000)
    MoveCamera(47, 15, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(18500, 3000)
    PlayEffect(0x0, 0xFF, 0xA, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    ClearChrFlags(0xA, 0x8)
    SetChrChip(0x0, 0xA, 0x1E, 0x12C)

    def lambda_720():
        OP_95(0xFE, 5800, 0, 3300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_720)

    def lambda_73A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_73A)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    SetChrChip(0x1, 0xA, 0x0, 0x0)
    SetChrSubChip(0x8, 0x2)
    OP_93(0xA, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(300)

    #C0010
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3205Fおお……\x01",
            "いらしてたんですか。\x02\x03",

            "#3204Fいやはや、失言でしたね。\x02",
        )
    )

    CloseMessageWindow()
    #Sound(1627, 255, 100, 0)    #voice#Yin
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("黒衣の男")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30Wフン……\x01",
            "わざと聞かせたのだろう？\x02\x03",

            "相変わらず喰えない男だ。\x02",
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

    #C0012
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3204Fいやいや、貴方ほどでは。\x02\x03",

            "#3200Fところで今宵は\x01",
            "どのようなご用件で？\x02\x03",

            "軍用犬への対処をする気に\x01",
            "なっていただけましたか？\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0xA,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700Fあの程度、お前の部下どもで\x01",
            "何とかできるだろう。\x02\x03",

            "私が相手をするのは\x01",
            "ガルシアを始めとする\x01",
            "ルバーチェの主力のみ……\x02\x03",

            "そういう契約だったはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3206Fやれやれ、つれないですねぇ。\x02\x03",

            "#3201F何やら《アルカンシェル》に\x01",
            "拘ってらっしゃるようですが……\x02\x03",

            "ここの警察はなかなか優秀だ。\x01",
            "こちらへの面倒事は困りますよ？\x02",
        )
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0xA,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0702Fクク、心配は無用だ。\x02\x03",

            "それよりも……\x01",
            "《特務支援課》、どう感じた。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3205Fふむ……用件というのは\x01",
            "彼らについてでしたか。\x02\x03",

            "#3204Fそうですね──\x01",
            "興味深い若者たちでしたよ。\x02\x03",

            "#3200F特にリーダーらしき、\x01",
            "ロイドさんがいいですねぇ。\x02\x03",

            "自分の力不足を痛感しながらも\x01",
            "ひた向きに前に進もうとする……\x02\x03",

            "#3209Fカンも悪くないようですし、\x01",
            "なかなか好みのタイプです。\x02",
        )
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0xA,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700Fお前の趣味は聞いていない。\x02\x03",

            "他のメンバーはどうだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3204Fフフ、これがまた\x01",
            "なかなか興味深い面々でして。\x02\x03",

            "#3200Fマクダエル市長のお孫さん……\x01",
            "相当な政治センスをお持ちのようで\x01",
            "参謀役と言ってもいいでしょう。\x02\x03",

            "エプスタイン財団の娘さん……\x01",
            "魔導杖そのものも興味深いですが\x01",
            "特殊な資質を持っているようです。\x02\x03",

            "#3204Fそして赤毛の彼は……\x01",
            "フフ、これは私のカンですが\x01",
            "我々と似たような匂いがしますね。\x02",
        )
    )

    CloseMessageWindow()

    #N0019
    NpcTalk(
        0xA,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700F……なるほど。\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#4P#3200Fしかし……\x01",
            "どうしてまた彼らに興味を？\x02",
        )
    )

    CloseMessageWindow()

    #N0021
    NpcTalk(
        0xA,
        "黒衣の男",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0702Fなに……\x01",
            "少々、試したくなってな。\x02\x03",

            "この私の──\x01",
            "《銀》の依頼を託すのに\x01",
            "ふさわしい相手であるのかを。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1ED end

    def Function_3_EEB(): pass

    label("Function_3_EEB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    LoadChrToIndex("apl/ch50406.itc", 0x22)
    SoundLoad(940)
    SoundLoad(941)
    SoundLoad(942)
    OP_68(5800, 900, 0, 0)
    MoveCamera(50, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 7300, 0, 0, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6100, 0, -2100, 0)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -4500, 0, 0, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -4500, 0, 0, 90)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年の声")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            "──ルバーチェの\x01",
            "裏ルートが復活している？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(7300, 900, 0, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0023
    ChrTalk(
        0x9,
        "#11P……はい。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        (
            "#11Pここ１週間で、我々が潰した\x01",
            "３つのルートが立て直されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "#11Pこちらも妨害しようとしたのですが\x01",
            "思っていた以上に抵抗が激しく……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#3203F#5Pふむ……妙ですね。\x02\x03",

            "この状況で、失ったルートを\x01",
            "わざわざ取り戻すだけの余力が\x01",
            "彼らにあるとも思えませんが……\x02\x03",

            "#3200Fあちらの営業本部長殿が\x01",
            "わざわざ動いたのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "#11Pいえ……それが。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x9,
        (
            "#11P《キリングベア》の姿はなく、\x01",
            "配下の構成員だけだったそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#11Pそれも軍用犬は連れておらず、\x01",
            "数名程度の少人数だったようで……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0030
    ChrTalk(
        0x8,
        (
            "#3205Fふむ、ますます奇妙ですね。\x02\x03",

            "#3203F構成員一人一人の戦闘力ならば\x01",
            "我々《黒月#4Rヘイユエ#》の方が上のはず……\x02\x03",

            "#3201F例のラインフォルト社製の\x01",
            "重機関銃を持ち出したのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#11Pええ、確かにその武装も\x01",
            "持ち出してきたようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#11Pそれ以上に、戦闘能力そのものが\x01",
            "大幅に向上しているとの報告です。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        "#3203F#5Pなるほど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0034
    ChrTalk(
        0x8,
        (
            "#3204F#5P現在、マルコーニ会長は\x01",
            "議長閣下のお怒りを静めようと\x01",
            "躍起になっているようです。\x02\x03",

            "どこぞの猟兵団を\x01",
            "新たに雇った様子もありませんし、\x01",
            "大規模な戦闘訓練の報告もない……\x02\x03",

            "#3210Fふむ、なかなか興味深いですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#11P……我々の知らない切り札を\x01",
            "持っていたという事でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#3200Fええ、間違いないでしょう。\x02\x03",

            "#3204Fしかも私の見立てでは……\x01",
            "尋常な切り札ではなさそうです。\x02\x03",

            "#3210Fそれこそ《銀》殿のような、\x01",
            "状況を一気にひっくり返せるほどの\x01",
            "“鬼札#4Rジョーカー#”かもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        "#11Pくっ、一体どんな手を……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(940, 2, 80, 0)
    OP_82(0x32, 0x0, 0xBB8, 0x7D0)
    Sleep(500)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(941, 2, 80, 0)

    def lambda_1697():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1697)
    Sleep(50)
    OP_93(0x9, 0x10E, 0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    #C0038
    ChrTalk(
        0x9,
        "#11Pい、今のは……！？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        "#11P#3201F噂をすれば影、ですか。\x02",
    )

    CloseMessageWindow()
    Sound(942, 2, 80, 0)
    OP_68(6300, 800, 0, 1500)
    MoveCamera(50, 15, 0, 1500)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1742():
        OP_95(0xFE, 2100, 0, 0, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1742)

    def lambda_175C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_175C)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    OP_64(0xB)
    OP_6F(0x79)

    #C0040
    ChrTalk(
        0xB,
        "#6Pた、大変です！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "#6Pルバーチェと思われる\x01",
            "黒ずくめの一団による襲撃です！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "#6Pその数、およそ１０！\x01",
            "《キリングベア》の姿はありません！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#11Pたかが１０名ごとき、\x01",
            "返り討ちにしてしまえ！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            "#11P警察は心配するな！\x01",
            "正当防衛で何とでもなる！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        "#6Pそ、それが……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "#6P襲撃者の戦闘力は尋常ではなく、\x01",
            "重機関銃を片手で軽々と振り回して……\x02",
        )
    )

    CloseMessageWindow()
    Sound(834, 0, 100, 0)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sleep(1000)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_63(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_191C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_191C)

    def lambda_192D():
        OP_95(0xFE, 2200, 0, -1100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_192D)
    WaitChrThread(0xC, 1)
    OP_64(0xC)
    OP_93(0xC, 0x5A, 0x1F4)
    WaitChrThread(0xC, 2)

    #C0047
    ChrTalk(
        0xC,
        "#6P１階が突破されました！\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        (
            "#6Pこちらに迫ってくるのは\x01",
            "時間の問題かと思われます！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#11Pくっ……\x01",
            "《銀#2Rイン#》殿がいれば……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(7300, 800, 0, 1500)
    SetCameraDistance(22500, 1500)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(130)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    Sound(882, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(500)
    OP_6F(0x11)

    #C0050
    ChrTalk(
        0x8,
        (
            "#11P#3204F……フフ、やれやれ。\x02\x03",

            "#3200Fどうやら頭脳派を気取っている\x01",
            "訳にも行かないようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0x0, 0x1F4)

    #C0051
    ChrTalk(
        0x9,
        "#11Pツァオ様、まさか──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_25(0x3AC, 0x3C)
    OP_25(0x3AD, 0x3C)
    OP_25(0x3AE, 0x3C)
    Sleep(300)
    SetCameraDistance(21500, 800)
    Fade(250)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sound(939, 0, 100, 0)
    OP_6F(0x10)
    OP_25(0x3AC, 0x46)
    OP_25(0x3AD, 0x46)
    OP_25(0x3AE, 0x46)

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P#3203F──出ますよ、ラウ。\x02\x03",

            "#3210Fこの程度で《銀》殿に頼っては\x01",
            "《黒月》の名折れ……\x02\x03",

            "東方人街を支配する我らの力、\x01",
            "存分に見せ付けてやりましょう。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xD, 1, 0, 4)
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    WaitChrThread(0xD, 1)
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    OP_CA(0x1, 0xFF, 0x0)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    OP_24(0x3AC)
    OP_24(0x3AD)
    OP_24(0x3AE)
    SetScenarioFlags(0x5D, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_EEB end

    def Function_4_1C35(): pass

    label("Function_4_1C35")

    OP_25(0x3AC, 0x50)
    OP_25(0x3AD, 0x50)
    OP_25(0x3AE, 0x50)
    Sleep(300)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    Sleep(300)
    OP_25(0x3AC, 0x64)
    OP_25(0x3AD, 0x64)
    OP_25(0x3AE, 0x64)
    Sleep(1500)
    OP_25(0x3AC, 0x5A)
    OP_25(0x3AD, 0x5A)
    OP_25(0x3AE, 0x5A)
    Sleep(300)
    OP_25(0x3AC, 0x50)
    OP_25(0x3AD, 0x50)
    OP_25(0x3AE, 0x50)
    Sleep(300)
    OP_25(0x3AC, 0x46)
    OP_25(0x3AD, 0x46)
    OP_25(0x3AE, 0x46)
    Sleep(300)
    OP_25(0x3AC, 0x3C)
    OP_25(0x3AD, 0x3C)
    OP_25(0x3AE, 0x3C)
    Sleep(300)
    OP_25(0x3AC, 0x32)
    OP_25(0x3AD, 0x32)
    OP_25(0x3AE, 0x32)
    Sleep(300)
    OP_25(0x3AC, 0x28)
    OP_25(0x3AD, 0x28)
    OP_25(0x3AE, 0x28)
    Sleep(300)
    OP_25(0x3AC, 0x1E)
    OP_25(0x3AD, 0x1E)
    OP_25(0x3AE, 0x1E)
    Sleep(300)
    OP_25(0x3AC, 0x14)
    OP_25(0x3AD, 0x14)
    OP_25(0x3AE, 0x14)
    Sleep(300)
    OP_25(0x3AC, 0xA)
    OP_25(0x3AD, 0xA)
    OP_25(0x3AE, 0xA)
    Sleep(300)
    OP_24(0x3AC)
    OP_24(0x3AD)
    OP_24(0x3AE)
    Return()

    # Function_4_1C35 end

    SaveToFile()

Try(main)
