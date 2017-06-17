from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4600.bin",                # FileName
        "e4600",                    # MapName
        "e4600",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4600",                  # 0
        "道化師カンパネルラ",     # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(188, 0)                                        # 0

    ScpFunction((
        "Function_0_BC",           # 00, 0
        "Function_1_CC",           # 01, 1
        "Function_2_CD",           # 02, 2
    ))


    def Function_0_BC(): pass

    label("Function_0_BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_CB")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_CB")

    Return()

    # Function_0_BC end

    def Function_1_CC(): pass

    label("Function_1_CC")

    Return()

    # Function_1_CC end

    def Function_2_CD(): pass

    label("Function_2_CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03600.itc", 0x1E)
    LoadEffect(0x0, "event/ev14000.eff")
    SoundLoad(3885)
    SoundLoad(3886)
    SoundLoad(969)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, -3000, 0)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFrame(0x1, "piller", 0x2, "loop")
    SetMapObjFrame(0x1, "model4", 0x2, "loop")
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "piller", 0x2, "loop")
    SetMapObjFrame(0x6, "model4", 0x2, "loop")
    SetMapObjFlags(0x7, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_F3(100000)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("声")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W──なるほど。\x01",
            "なかなか順調のようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7580", 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 3800, 12000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, -10000, 3800, -8000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_68(-330, 2000, -1650, 0)
    MoveCamera(304, 29, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(18000, 5000)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x79)
    CancelBlur(1000)
    Fade(500)
    OP_68(0, 7250, 0, 0)
    MoveCamera(0, -10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(31150, 0)
    OP_68(0, 10900, 0, 0)
    MoveCamera(358, -9, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24310, 0)
    OP_68(0, 7250, 0, 8000)
    MoveCamera(0, -5, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(20150, 8000)
    PlaceName2(340, 200, "c_plac64", 0x0, 2000)
    OP_6F(0x79)
    Fade(500)
    OP_93(0x8, 0x13B, 0x0)
    OP_68(-5610, 2000, -2300, 0)
    MoveCamera(8, 4, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19600, 0)
    MoveCamera(359, 4, 0, 30000)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("第六柱")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、こちらの準備も\x01",
            "９割がた目処が付いた。\x02\x03",

            "今回のオーダーには\x01",
            "何とか間に合わせられるだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("第一柱")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お疲れ様です、博士。\x02\x03",

            "──カンパネルラ。\x01",
            "《執行者#6Rレギオン#》たちの動きは？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    #C0004
    ChrTalk(
        0x8,
        (
            "#04804F#12Pちょっと前にブルブランが\x01",
            "遊んでいたみたいだけど、\x01",
            "もう手は引いたみたいだね。\x02\x03",

            "#04800Fレンはリベールに去ってから\x01",
            "戻ってくる気配はなさそうだ。\x02\x03",

            "#04806Fそして“彼女”については……\x01",
            "ま、様子見でいいんじゃない？\x02\x03",

            "#04802F式神は貸してくれたけど、\x01",
            "今のところ介入するつもりは\x01",
            "一切ないみたいだし。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("第一柱")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふむ、分かりました。\x02\x03",

            "マイスターと同様、\x01",
            "彼らの意志に任せて下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("第六柱")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "しかし《執行者》には\x01",
            "全ての行動の自由を与えるか……\x02\x03",

            "あの方の決めた事とはいえ、\x01",
            "いささか理不尽な《掟》だねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("第一柱")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ては《盟主》の思し召し……\x01",
            "是非を問う必要はありません。\x02\x03",

            "それより──\x01",
            "いらっしゃったようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(3, 120, -1, -1)
    SetChrName("第六柱")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おや、来たかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_93(0x8, 0x87, 0x1F4)

    #C0009
    ChrTalk(
        0x8,
        "#04809F#5Pフフ、時間通りだねぇ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(10000, -1000, -8000, 0)
    MoveCamera(100, 80, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    OP_68(10000, 2500, -8000, 5000)
    MoveCamera(97, 12, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(18000, 5000)
    Sound(969, 2, 100, 0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "piller", 0x2, "up")
    SetMapObjFrame(0x7, "model4", 0x2, "up")
    Sleep(5000)
    StopSound(969, 1000, 100)
    Sleep(1000)
    Sound(970, 0, 100, 0)
    SetMapObjFrame(0x7, "piller", 0x2, "open")
    SetMapObjFrame(0x7, "model4", 0x2, "open")
    SetCameraDistance(16000, 1000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(300)
    SetMapObjFrame(0x7, "model4", 0x2, "loop")
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 10000, 3800, -8000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sleep(500)
    OP_6F(0x79)
    CancelBlur(1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(235, 130, -1, -1)
    SetChrName("第七柱")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3885V#40W──お待たせしました。\x02\x03",

            "#3886Vもう、始めているようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xF2E)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("第一柱")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いえ、始めたばかりです。\x02\x03",

            "例の件については\x01",
            "もう宜しいのですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 130, -1, -1)
    SetChrName("第七柱")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、後は《破戒》殿に\x01",
            "全てをお任せしてきました。\x02\x03",

            "それで──\x01",
            "《クロスベル》でしたね。\x02\x03",

            "かの地に赴くのは\x01",
            "私もいささか久しぶりです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0013
    ChrTalk(
        0x8,
        (
            "#04804F#6P#Nウフフ、あまりの変わりように\x01",
            "目を丸くするんじゃない？\x02\x03",

            "#04800F現代の導力文明では\x01",
            "最先端の大都市だろうしね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 170, -1, -1)
    SetChrName("第六柱")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "私も完成前にもう一度、\x01",
            "顔を出してみるつもりだよ。\x02\x03",

            "どうだね、せっかくだから\x01",
            "現地で落ち合うとしようか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 130, -1, -1)
    SetChrName("第七柱")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、異存はありません。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_93(0x8, 0x0, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(310, 5500, -5790, 0)
    MoveCamera(359, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(26500, 0)
    SetCameraDistance(25500, 1500)
    OP_6F(0x79)
    CancelBlur(1000)
    SetCameraDistance(23500, 50000)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("第一柱")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──では、お二方。\x01",
            "以後は委細をお任せします。\x02\x03",

            "『幻焔#4Rげんえん#計画』……\x01",
            "あの方の最終計画のためには\x01",
            "欠かせないステップです。\x02\x03",

            "第一段階としての仕掛け、\x01",
            "よろしくお願いしますよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(0, 170, -1, -1)
    SetChrName("第六柱")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、了解だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(300, 170, -1, -1)
    SetChrName("第七柱")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ては《盟主》のために。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(23500, 2500)
    FadeToDark(2500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x1388)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_CD end

    SaveToFile()

Try(main)
