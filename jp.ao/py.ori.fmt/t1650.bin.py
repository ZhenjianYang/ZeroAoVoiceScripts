from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1650.bin",                # FileName
        "t1650",                    # MapName
        "t1650",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 88, 0, 0, 0, 1],
    )

    BuildStringList((
        "t1650",                  # 0
        "セイランド教授",         # 1
    ))

    AddCharChip((
        "chr/ch44802.itc",                   # 00
    ))

    DeclNpc(110690,  150,     57000,   270,  453,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)

    DeclActor(109380,  0,       57000,   1500,    110690,  1500,    57000,   0x007E, 0,  2,  0x0000)

    ChipFrameInfo(264, 0)                                        # 0

    ScpFunction((
        "Function_0_108",          # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_1CA",          # 02, 2
        "Function_3_1CE",          # 03, 3
        "Function_4_493",          # 04, 4
        "Function_5_1197",         # 05, 5
        "Function_6_11E2",         # 06, 6
        "Function_7_122D",         # 07, 7
        "Function_8_1278",         # 08, 8
        "Function_9_12C9",         # 09, 9
        "Function_10_1314",        # 0A, 10
        "Function_11_2F8B",        # 0B, 11
    ))


    def Function_0_108(): pass

    label("Function_0_108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)

    label("loc_13E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_14D")
    ClearScenarioFlags(0x22, 0)
    Event(0, 4)

    label("loc_14D")

    Return()

    # Function_0_108 end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_160")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_160")

    OP_1B(0x1, 0x0, 0xB)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D")
    OP_66(0x0, 0x1)

    label("loc_18D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C9")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 30, 0)

    label("loc_1C9")

    Return()

    # Function_1_14E end

    def Function_2_1CA(): pass

    label("Function_2_1CA")

    Call(0, 3)
    Return()

    # Function_2_1CA end

    def Function_3_1CE(): pass

    label("Function_3_1CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA")
    Call(0, 10)
    Return()

    label("loc_1FA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_399")

    #C0001
    ChrTalk(
        0x8,
        (
            "あの薬物の患者については\x01",
            "ほとんど処置は終わったが、\x01",
            "問診表を出していない者がいる。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "まず、クロスベル市、\x01",
            "旧市街に住むディーノ少年。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "次に、劇団アルカンシェルの\x01",
            "アーティスト、ニコル団員。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "そして、クロスベル警備隊\x01",
            "ベルガード門勤務のクレス隊員。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "彼らに事情を話して、\x01",
            "問診表を回収してほしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "全て集まったら、\x01",
            "もう一度ここに報告に来てくれ。\x01",
            "それでは、よろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_48F")

    label("loc_399")


    #C0007
    ChrTalk(
        0x8,
        (
            "クロスベル市、\x01",
            "旧市街に住むディーノ少年。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "劇団アルカンシェルの\x01",
            "アーティスト、ニコル団員。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "そして、クロスベル警備隊\x01",
            "ベルガード門勤務のクレス隊員。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "彼らに事情を話して、\x01",
            "問診表を回収してほしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        "それでは、よろしく頼んだぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_48F")

    TalkEnd(0x8)
    Return()

    # Function_3_1CE end

    def Function_4_493(): pass

    label("Function_4_493")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x8, 59520, 0, 59900, 0)
    OP_68(57330, 1000, 58820, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 57250, 0, 59010, 90)
    SetChrPos(0x102, 56500, 0, 57980, 90)
    SetChrPos(0x109, 56600, 0, 59920, 135)
    SetChrPos(0x105, 54680, 0, 57620, 90)
    SetChrPos(0x104, 55270, 0, 59030, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0012
    ChrTalk(
        0x101,
        (
            "#6P#00000F──すみません、失礼します。\x01",
            "特務支援課の者ですが……\x02",
        )
    )

    CloseMessageWindow()

    #N0013
    NpcTalk(
        0x8,
        "女性の声",
        "入りたまえ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, 110690, 150, 57000, 270)
    SetChrSubChip(0x8, 0x1)
    OP_68(100830, 1250, 48810, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 98390, 0, 49590, 90)
    SetChrPos(0x102, 98390, 0, 49590, 90)
    SetChrPos(0x104, 98390, 0, 49590, 90)
    SetChrPos(0x109, 98390, 0, 49590, 90)
    SetChrPos(0x105, 98390, 0, 49590, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 7)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 8)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 9)
    OP_68(105790, 1250, 52080, 3000)
    MoveCamera(62, 24, 0, 3000)
    OP_6E(440, 3000)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)

    #N0014
    NpcTalk(
        0x8,
        "女医",
        "ふむ、ようやく来たようだな。\x02",
    )

    CloseMessageWindow()

    #N0015
    NpcTalk(
        0x8,
        "女医",
        (
            "予想していた時刻より\x01",
            "約２分オーバーだが……\x01",
            "まあ優秀といってよさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#00306F（な、なんだかおっかなそうだな……\x01",
            "　美人には違いないが。）\x02",
        )
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0x8,
        "女医",
        (
            "まあ、とりあえずこっちに来てくれ。\x01",
            "この距離では話がしにくいのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00000Fそ、そうですね。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    OP_68(108640, 950, 57250, 5000)
    MoveCamera(45, 28, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(20000, 5000)

    def lambda_8D2():
        OP_95(0xFE, 107920, 0, 57770, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D2)
    Sleep(500)

    def lambda_8EF():
        OP_95(0xFE, 107840, 0, 56600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8EF)
    Sleep(500)

    def lambda_90C():
        OP_95(0xFE, 106710, 0, 58390, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90C)
    Sleep(700)

    def lambda_929():
        OP_95(0xFE, 106120, 0, 57330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_929)
    Sleep(500)

    def lambda_946():
        OP_95(0xFE, 106680, 0, 56190, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_946)
    WaitChrThread(0x101, 1)

    def lambda_964():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_964)
    WaitChrThread(0x102, 1)

    def lambda_975():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_975)
    WaitChrThread(0x109, 1)

    def lambda_986():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_986)
    WaitChrThread(0x104, 1)

    def lambda_997():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_997)
    WaitChrThread(0x105, 1)

    def lambda_9A8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A8)
    OP_6F(0x79)
    OP_0D()

    #C0019
    ChrTalk(
        0x102,
        (
            "#6P#00100Fえっと、あなたが\x01",
            "セイランド教授ですね？\x02\x03",

            "#00103Fグノーシスの成分の\x01",
            "分析結果が出たとのことでしたが──\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#11P──悪いが、その前に\x01",
            "頼みたいことがあるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#11P君たちには、まずそちらを\x01",
            "先に片付けてもらいたいのだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        (
            "#6P#10303F依頼に出されていた件だね。\x02\x03",

            "#10301Fグノーシスの分析結果を\x01",
            "渡してもらってからでは\x01",
            "だめなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#11P今回の分析結果にも関わるから\x01",
            "先に片付けておきたいのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#11Pというのも、グノーシスの被害にあった\x01",
            "患者たちに関係あることでな。\x02",
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

    #C0025
    ChrTalk(
        0x109,
        "#6P#10105Fなるほど、そうでしたか。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00003F……分かりました、\x01",
            "先にそちらをあたらせていただきます。\x02\x03",

            "#00000F依頼内容をお聞かせ願えますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#11Pうむ、君たちに頼みたいのは\x01",
            "『問診表の回収』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#11P……例の教団事件のあと、\x01",
            "病院は“グノーシス”被害者の\x01",
            "アフターケアに力を注いだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#11Pほとんどの患者の処置は\x01",
            "一通り終わったのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P最後に書いてもらった問診表を、\x01",
            "何名かの患者が提出していなくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#6P#00003Fなるほど……\x01",
            "確かに分析結果にも\x01",
            "関わりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "#11Pうむ、迅速にお願いしたい。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P……問診表が帰ってきてない\x01",
            "患者たちは３名だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#11Pまず、クロスベル市、\x01",
            "旧市街に住む少年、ディーノ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#11P次に、劇団アルカンシェルの\x01",
            "アーティスト、ニコル。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#11Pそして、クロスベル警備隊\x01",
            "ベルガード門勤務の隊員、クレス。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#11P以上の患者に事情を話し、\x01",
            "問診表を回収してきて欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#6P#00300Fなるほど、知った名前ばかりみたいだな。\x02\x03",

            "#00303F旧市街とアルカンシェルの２人は\x01",
            "街で探せばすぐ見つかるだろう。\x02\x03",

            "#00302Fクレス先輩も、多分ベルガード門の食堂で\x01",
            "メシでも食ってる所だろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#6P#00000Fああ、早速行ってみるとしよう。\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#11Pでは、よろしく頼んだぞ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#11P回収が終わったら、もう一度ここに\x01",
            "報告に来てくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#11Pその時、グノーシスの分析結果について\x01",
            "改めて話をさせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【新教授の依頼】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x152, 2)
    OP_29(0x70, 0x1, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 107500, 0, 57000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_4_493 end

    def Function_5_1197(): pass

    label("Function_5_1197")


    def lambda_119C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_119C)

    def lambda_11AD():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11AD)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 105730, 0, 50340, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_5_1197 end

    def Function_6_11E2(): pass

    label("Function_6_11E2")


    def lambda_11E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11E7)

    def lambda_11F8():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11F8)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 104600, 0, 50890, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_6_11E2 end

    def Function_7_122D(): pass

    label("Function_7_122D")


    def lambda_1232():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1232)

    def lambda_1243():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1243)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 105690, 0, 48970, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_7_122D end

    def Function_8_1278(): pass

    label("Function_8_1278")


    def lambda_127D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_127D)

    def lambda_128E():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_128E)
    WaitChrThread(0x109, 1)
    Sound(107, 0, 100, 0)
    OP_95(0x109, 104810, 0, 49520, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_8_1278 end

    def Function_9_12C9(): pass

    label("Function_9_12C9")


    def lambda_12CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12CE)

    def lambda_12DF():
        OP_98(0xFE, 0x10CC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_12DF)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 103660, 0, 49780, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_9_12C9 end

    def Function_10_1314(): pass

    label("Function_10_1314")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(108640, 950, 57250, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 107920, 0, 57770, 90)
    SetChrPos(0x102, 107840, 0, 56600, 90)
    SetChrPos(0x109, 106120, 0, 57330, 90)
    SetChrPos(0x105, 106680, 0, 56190, 90)
    SetChrPos(0x104, 106710, 0, 58390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0044
    ChrTalk(
        0x8,
        "#11P……戻ってきたか。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#11P予想時刻より約５分オーバーだが……\x01",
            "まあ及第点だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x104,
        "#6P#00306F（や、やっぱりおっかねぇ……）\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#6P#00000Fえっと、問診表の回収が\x01",
            "終わりました……こちらです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "問診表をセイランド教授に渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x32D, 1)
    SubItemNumber(0x32E, 1)
    SubItemNumber(0x32F, 1)

    #C0049
    ChrTalk(
        0x8,
        "#11P……ふむ……………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    #C0050
    ChrTalk(
        0x102,
        (
            "#6P#00101Fあ、あの……\x01",
            "なにか問題がありましたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    Sleep(500)

    #C0051
    ChrTalk(
        0x8,
        "#11P……いや、逆だ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P問診表を見た限りでは、\x01",
            "後遺症などもないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#11Pこれでひとまず\x01",
            "グノーシス服用者全員の\x01",
            "治療が完了したことになる。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "#11Pご苦労だったな。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#6P#00002Fそ、そうですか……！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x109,
        "#6P#10109Fふふ、よかったですね。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x105,
        (
            "#6P#10300Fなかなか手間だったけど\x01",
            "お役に立てて光栄だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#11Pでは早速だが、グノーシスの\x01",
            "分析結果を君たちに報告しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        "#11P少々、付き合ってもらおうか。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0060
    ChrTalk(
        0x101,
        (
            "#6P#00001Fあ……\x01",
            "はい、お願いします！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch02902.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    OP_68(103000, 1050, 57370, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(22900, 0)
    SetChrPos(0x8, 103000, 150, 58690, 180)
    SetChrPos(0x109, 102150, 150, 58690, 180)
    SetChrPos(0x102, 103850, 150, 58690, 180)
    SetChrPos(0x105, 102150, 150, 55850, 0)
    SetChrPos(0x101, 103000, 150, 55880, 0)
    SetChrPos(0x104, 103850, 150, 55890, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5P──グノーシスを\x01",
            "徹底的に分析した結果……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "#5Pまず第一に、グノーシスには\x01",
            "“脳のリミッター”を強制的に\x01",
            "外す効果があることが分かった。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#00005F脳のリミッター……\x01",
            "というと？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "#5Pそもそも人間というものは、\x01",
            "本来持っている身体能力の\x01",
            "半分も使えないとされている。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#5P身体への負荷を減らすため、\x01",
            "脳が引き出せる能力に\x01",
            "無意識の制限をかけるからだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "#5Pこのリミッターを\x01",
            "意図的に解除することが\x01",
            "もし可能なら……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#5P理論上、その個人が持つ\x01",
            "限界までの能力を\x01",
            "発揮できるようになるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        (
            "#12P#10303Fつまり、グノーシスとは\x01",
            "単に筋力を強化する薬ではなく……\x02\x03",

            "#10301F普段は使われていない潜在能力を\x01",
            "強引に引き出す薬というわけだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "#5Pその通り。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5P無論、無意識にかかっていた\x01",
            "リミッターを外せば、\x01",
            "体への負担は相当なものだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#12P#00301F確かに、教団事件の後\x01",
            "警備隊のやつらは\x01",
            "相当疲弊してたみたいだからな。\x02\x03",

            "#00303Fしばらくは指一本も動かすのも\x01",
            "キツイ有様だったようだし……\x02\x03",

            "#00302Fま、みっちりリハビリ訓練を\x01",
            "やったおかげで、ようやく\x01",
            "カンを取り戻せたみてえだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x109,
        "#5P#10104Fはい……そうみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#11P#00103F……カン、といえば。\x02\x03",

            "#00101F高まったツキとカンを頼りに\x01",
            "ギャンブルで連勝を\x01",
            "していた人もいましたね。\x02\x03",

            "#00108Fそれと同時に性格や言動が\x01",
            "豹変したようでしたが……\x02\x03",

            "#00101Fそれらも、グノーシスが\x01",
            "脳のリミッターを外しているから、\x01",
            "で説明がつくのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        "#5Pうむ、そう考えていい。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "#5Pこの薬には五感の働きを\x01",
            "飛躍的に高める作用も\x01",
            "確認されているからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#5P副作用として神経質になり、\x01",
            "情緒不安定な状態に\x01",
            "なることも分かっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "#5Pそれが凶暴な性格への変化に\x01",
            "つながるのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        "#12P#00003Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        (
            "#5P#10100F確かに一通り\x01",
            "説明が付きそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "#5P──だが、あくまで生化学的に\x01",
            "説明できるのはここまでだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0081
    ChrTalk(
        0x101,
        "#12P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#5Pいくつかの効能については\x01",
            "非科学的としか言いようがない。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#5P具体的には、先ほども話に出た\x01",
            "ツキを呼び込むという効能……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "#5Pそして、君たちも何度か目撃したという\x01",
            "“魔人化#6Rデモナイズ#”という肉体変異現象だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#11P#00105F……た、確かに……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#12P#00303Fそいつがあったか……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#12P#00003F……魔人化を引き起こすのは\x01",
            "紅いタイプのグノーシス……\x02\x03",

            "#00001Fやはり蒼いタイプのものとは\x01",
            "異なる成分だったわけですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        "#5Pそれなんだが……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "#5P実は、蒼いタイプのグノーシスも\x01",
            "紅いタイプのグノーシスも\x01",
            "成分的には何ら変わりはない。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        "#5P少なくとも生化学的にはな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x101,
        "#12P#00005Fそ、そうなんですか！？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "#5Pああ、あの色の違いは\x01",
            "精製時の処理の差によるものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "#5P主成分に何ら違いはないし、\x01",
            "分子構造もほぼ一致している……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#5Pにも関わらず、紅いタイプは\x01",
            "肉体変異などという説明不可能な\x01",
            "現象を引き起こしている……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P──正直、魔人化というのが\x01",
            "君たちが恐怖のあまり見た“幻覚”と\x01",
            "考えるのが一番しっくり来るくらいだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x104,
        "#12P#00306Fいや、そいつはさすがに……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x109,
        (
            "#5P#10108Fアーネスト秘書の魔人化は\x01",
            "あたしも目撃していますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "#5P判っている。\x01",
            "──だからここまでが限界なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#5Pグノーシスという薬物の正体を\x01",
            "生化学という分野からのみで\x01",
            "解き明かすというアプローチではな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x101,
        "#12P#00003F……なるほど……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x105,
        (
            "#12P#10302F最先端の近代医療の担い手にしては\x01",
            "ずいぶん殊勝な意見だね？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#5P近代医療は万能ではないさ。\x01",
            "こと心と魂の問題についてはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#5Pそしてグノーシスはおそらく、\x01",
            "それらと肉体を共鳴させるような\x01",
            "何らかの働きを秘めているんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "#5P多分、ヨアヒムもグノーシスの全貌は\x01",
            "掴めていなかったに違いあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "#5P教団に伝わっていた秘儀を元に\x01",
            "試行錯誤しながら完成させ、\x01",
            "量産化に成功しただけのはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        (
            "#11P#00101F確かに、そのようなことを\x01",
            "本人も認めていたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ、各地で行われた儀式の\x01",
            "データを元に、試行錯誤しながら\x01",
            "完成させたと言っていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        "#5Pふむ、やはりそうか。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "#5Pヤツは有能で熱意もあったが\x01",
            "天才というほどズバ抜けた\x01",
            "発想の持ち主ではなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        "#5Pそれが悪い方に出てしまったか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x101,
        "#12P#00005Fひょっとして……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#12P#00305Fあのヨアヒムと個人的な\x01",
            "知り合いだったりするんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#5Pああ、ヤツがレミフェリアの\x01",
            "医科大学で学んでいた頃の同輩さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#5P卒業してからは会っていなかったが\x01",
            "たまに最新の研究成果などについて\x01",
            "手紙でやり取りはしていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#5Pだが、まさかこのような形で\x01",
            "医の技術を悪用し、自らの身まで\x01",
            "滅ぼすことになるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#11P#00108F教授……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x109,
        "#5P#10103F……お察しします。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "#5Pいや、詮ないことを言った。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "#5P──いずれにせよ、\x01",
            "私から報告できるのはここまでだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#5Pグノーシスの真相に迫るには\x01",
            "別のアプローチが必要になるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "#5Pこれは完全に私のカンだが……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "#5Pグノーシスの原料であるという\x01",
            "《プレロマ草》なる植物の特質が\x01",
            "鍵になるのではないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        "#12P#00001F《プレロマ草》……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#11P#00103F教団のデータベースに\x01",
            "記されていた名前ですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        (
            "#12P#00306Fしかし、結局どんな植物で\x01",
            "どこから手に入れていたのかも\x01",
            "判ってねぇんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#5Pああ、私も知り合いの\x01",
            "植物学者などに当たってみたが\x01",
            "該当するものは見付からなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#5P教団にのみ伝わっていた新種か、\x01",
            "それとも……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#5Pいずれにせよ、薬の効能を考えると、\x01",
            "その植物も“あり得ない”性質を\x01",
            "持っているのではないかと推測できる。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        "#11P#00101F“あり得ない性質”ですか……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x105,
        (
            "#12P#10309Fフフ、何だかオカルティックで\x01",
            "面白くなってきたじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0131
    ChrTalk(
        0x101,
        (
            "#12P#00003F──セイランド教授。\x01",
            "どうもありがとうございました。\x02\x03",

            "#00000Fおかげで、今まで漠然としていた事が\x01",
            "ある程度整理できた気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        "#5Pそうか、ならばよかった。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "#5Pグノーシスの成分調査については\x01",
            "こちらでは一旦打ち切るが……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#5Pまた、何か判ったことがあれば\x01",
            "遠慮なく訪ねてくるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#5Pあくまで医者の立場からでよければ\x01",
            "意見くらいは言わせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1314 end

    def Function_11_2F8B(): pass

    label("Function_11_2F8B")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【研究棟から出る】\x01",      # 0
            "【やめる】\x01",              # 1
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
        (0, "loc_2FF0"),
        (1, "loc_3009"),
        (SWITCH_DEFAULT, "loc_3021"),
    )


    label("loc_2FF0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Jump("loc_3021")

    label("loc_3009")

    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x5)
    Jump("loc_3021")

    label("loc_3021")

    Return()

    # Function_11_2F8B end

    SaveToFile()

Try(main)
