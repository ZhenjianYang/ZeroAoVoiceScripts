from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1560.bin",                # FileName
        "c1560",                    # MapName
        "c1560",                    # Location
        0x00AC,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 172, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1560",                  # 0
        "ディーター大統領",       # 1
        "戦鬼シグムント",         # 2
        "シャーリィ",             # 3
        "ヴァルド",               # 4
        "マリアベル",             # 5
        "アリオス長官",           # 6
        "警備員",                 # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_1AC",          # 01, 1
        "Function_2_24B",          # 02, 2
        "Function_3_17C1",         # 03, 3
        "Function_4_180B",         # 04, 4
        "Function_5_1855",         # 05, 5
        "Function_6_1B09",         # 06, 6
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_1AB")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1AB")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1AB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_1AB")

    Return()

    # Function_0_174 end

    def Function_1_1AC(): pass

    label("Function_1_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_200")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_24A")

    Return()

    # Function_1_1AC end

    def Function_2_24B(): pass

    label("Function_2_24B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch03300.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    LoadChrToIndex("chr/ch03800.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 150, 116200, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16800, 0, 111600, 90)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 18000, 0, 111300, 90)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19600, 0, 111800, 90)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    VolumeBGM(0x46, 0x7D0)
    OP_68(19500, 2000, 111500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(250, 90, -1, -1)
    SetChrName("グレイス")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──ここから先は\x01",
            "わたくしの方から数々のスクープを\x01",
            "お伝えさせていただきます。\x02\x03",

            "まずは２ヶ月前に起こった\x01",
            "クロスベル市襲撃事件ですが……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(18000, 1200, 113500, 2000)
    MoveCamera(39, 18, 0, 2000)
    SetCameraDistance(15000, 2000)
    OP_6F(0x79)
    SetChrSubChip(0x8, 0x2)

    #C0002
    ChrTalk(
        0x8,
        (
            "#11301F#5P……この不快な映像は\x01",
            "いったい何時#4Rい つ#まで続くのかね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E9():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_4E9)
    Sleep(100)

    def lambda_4F9():
        OP_93(0xD, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_4F9)
    Sleep(100)

    def lambda_509():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_509)
    Sleep(100)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0x9, 0)

    #C0003
    ChrTalk(
        0xC,
        (
            "#12P#02913F侵入経路は掴めたため、\x01",
            "物理的な遮断を\x01",
            "行っている最中ですわ。\x02\x03",

            "#02912Fあと２分ほどでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xD,
        (
            "#10503F街頭スクリーンについても\x01",
            "既に撤収を開始させています。\x02\x03",

            "#10500F程なく市民も退去するでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "#5P#11303Fふむ……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#12P#04500Fフフ、いい不意打ちでしたな。\x02\x03",

            "#04504F虚実を織り交ぜた妙手#4Rみょうしゅ#……\x01",
            "老兵の意地といったところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#11306F#5P何を他人事のような……\x02\x03",

            "#11310F君たちが議長を逃がしたから\x01",
            "このような事になったのだろうが？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#12P#04504Fいや、それについては\x01",
            "お詫びするしかありませんな。\x02\x03",

            "#04502Fもっとも、こちらの主張通り、\x01",
            "全ての禍根#10R㈲　㈲　㈲　㈲　㈲#を潰しておけば\x01",
            "こうはならなかった筈ですが？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#11303F……御子#4Rみ こ#殿の機嫌もある。\x02\x03",

            "#11301F支援課の関係者に\x01",
            "思い切ったことまでは出来ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xC,
        (
            "#12P#02913Fフフ、歯がゆいですけど\x01",
            "こればかりは仕方ないですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xD,
        (
            "#10503F……市外の国防軍にも\x01",
            "少なからず影響がある筈です。\x02\x03",

            "#10500F何とか立て直してみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        "#5P#11303Fああ、よろしく頼む。\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    MoveCamera(39, 18, 0, 4000)
    OP_68(18000, 1200, 108500, 4000)

    def lambda_902():
        OP_96(0xFE, 0x4650, 0x0, 0x182B8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_902)
    Sleep(500)

    def lambda_91F():

        label("loc_91F")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_91F")

    QueueWorkItem2(0x9, 2, lambda_91F)
    Sleep(100)

    def lambda_934():

        label("loc_934")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_934")

    QueueWorkItem2(0xC, 2, lambda_934)
    WaitChrThread(0xD, 1)
    Sound(103, 0, 100, 0)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(18000, 1200, 113500, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sound(104, 0, 100, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_9A7():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_9A7)
    Sleep(100)

    def lambda_9B7():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_9B7)
    Sleep(100)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    #C0013
    ChrTalk(
        0x9,
        (
            "#12P#04503F──では、我々の方も\x01",
            "本腰を入れさせてもらいましょう。\x02\x03",

            "#04504F《黒月#4Rヘイユエ#》にレジスタンスども……\x02\x03",

            "#04502F本気#4R㈲　㈲#で狩らせてもらいますよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        (
            "#12P#02912Fわたくしは《結社》の方々と\x01",
            "連絡を取っておきますわ。\x02\x03",

            "#02913F教会の船と支援課たち……\x01",
            "何とかする必要がありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        "#5P#11301Fああ、行きたまえ。\x02",
    )

    CloseMessageWindow()

    def lambda_B1D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_B1D)
    WaitChrThread(0xC, 2)
    SetCameraDistance(16000, 3000)

    def lambda_B37():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_B37)
    Sleep(100)

    def lambda_B54():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B54)
    WaitChrThread(0x9, 2)

    def lambda_B65():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B65)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, 13000, 0, 3000, 180)
    SetChrPos(0xC, 13000, 0, 3000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    OP_68(13000, 1300, -1100, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    MoveCamera(41, 21, 0, 4000)
    SetCameraDistance(16000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_C3E():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C3E)

    def lambda_C58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C58)
    Sleep(1000)

    def lambda_C6C():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C6C)

    def lambda_C86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C86)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(300)

    #C0016
    ChrTalk(
        0x9,
        (
            "#5P#04504Fフフ、やれやれ。\x02\x03",

            "#04500Fお父上はどうも\x01",
            "思い切りが足らぬようだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    #C0017
    ChrTalk(
        0xC,
        (
            "#12P#02906Fまあ、深謀遠慮とでも\x01",
            "思っていただきたいですわ。\x02\x03",

            "#02913F大陸全土の秩序を組み替える\x01",
            "壮大なる計画……\x02\x03",

            "#02902Fお父様一人ではどうしても\x01",
            "限界がありますもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#5P#04504Fだから優秀なスタッフが\x01",
            "色々と力を貸しているわけだ。\x02\x03",

            "#04500F剣聖や、あの御仁#8R㈲　㈲　㈲　㈲#のような。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xC,
        "#12P#02913Fフフ、そういう事ですわ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27500, 0, -600, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, -1500, 270)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #N0020
    NpcTalk(
        0xA,
        "少女の声",
        "パパ、話は終わったのー？\x02",
    )

    CloseMessageWindow()

    def lambda_ED1():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_ED1)
    Sleep(50)

    def lambda_EEE():
        OP_96(0xFE, 0x4010, 0x0, 0xFFFFFA24, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_EEE)

    def lambda_F08():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_F08)
    Sleep(50)

    def lambda_F18():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_F18)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    Fade(500)
    OP_68(24500, 1100, -1100, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    OP_68(14500, 1100, -1100, 4500)
    SetCameraDistance(16500, 4500)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0021
    ChrTalk(
        0xA,
        (
            "#11P#04609Fあ、ベルお嬢さんだ！\x01",
            "やっほー！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        "#01608F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xC,
        (
            "#6P#02909Fふふ、シャーリィさんは\x01",
            "いつも元気ですわね。\x02\x03",

            "#02902F例の話については\x01",
            "考えてくださったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xA,
        (
            "#11P#04605Fああ、お嬢さんの私設部隊の\x01",
            "トップだったっけ？\x02\x03",

            "#04606Fんー、面白そうだけど\x01",
            "今の環境も気に入ってるしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    #C0025
    ChrTalk(
        0x9,
        (
            "#5P#04501Fやれやれ、俺の目の前で\x01",
            "堂々と引き抜きをしないで\x01",
            "もらいたいもんですな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    #C0026
    ChrTalk(
        0xC,
        (
            "#12P#02904Fあら、これは失礼。\x02\x03",

            "#02912Fそれではシグムントさん。\x01",
            "今後の段取りについては\x01",
            "以前お話した通りに。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "#5P#04504Fああ、承知した。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    #C0028
    ChrTalk(
        0x9,
        (
            "#04500F#5P──小僧。\x01",
            "お前の方はどうする？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1209():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1209)

    #C0029
    ChrTalk(
        0xB,
        (
            "#01603F#11P……俺はアンタらの\x01",
            "仲間になった覚えはねぇ。\x02\x03",

            "#01600F勝手にやらせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x9,
        "#04504Fフ……まあいいだろう。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0031
    ChrTalk(
        0xA,
        (
            "#5P#04602Fヴァルド、その気があれば\x01",
            "とことん鍛えてあげるから\x01",
            "いつでも来なよね～？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        "#01601F#11Pケッ……\x02",
    )

    CloseMessageWindow()
    OP_68(19500, 1200, -1100, 4000)
    MoveCamera(51, 17, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0xA, 3, 0, 4)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(500)

    def lambda_1343():

        label("loc_1343")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1343")

    QueueWorkItem2(0xB, 2, lambda_1343)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(14700, 1200, -1650, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    EndChrThread(0xB, 0x2)

    #C0033
    ChrTalk(
        0xC,
        (
            "#6P#02913Fフフ……\x01",
            "頼もしい方々ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "#5P#01603F……化物父娘#4Rおやこ#の間違いだろ。\x02\x03",

            "#01602F対等に渡り合ってるアンタも\x01",
            "相当なタマだと思うがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "#6P#02909Fウフフ……\x02\x03",

            "#02912F後悔していますか？\x01",
            "わたくしの誘いに乗った事。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0036
    ChrTalk(
        0xB,
        (
            "#11P#01604Fハッ……んなワケねえだろ。\x02\x03",

            "#01603Fアンタがくれた薬のおかげで\x01",
            "俺は“チカラ”を手に入れた……\x02\x03",

            "#01602F誰もが使いこなせないような\x01",
            "圧倒的な“チカラ”をな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "#6P#02913Fフフ、そうですわね。\x02\x03",

            "魔人化した時のヴァルドさんは\x01",
            "膂力#4Rりょりょく#ならば人として最強……\x02\x03",

            "#02902Fわたくしたちにとっても\x01",
            "またとないサンプルですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "#11P#01604Fクク、せいぜい喜んで\x01",
            "モルモットになってやるよ。\x02\x03",

            "#01601Fあの野郎をブッ潰して……\x01",
            "誰が一番か証明するためにもな。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(500)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──こうして、独立国の\x01",
            "無効宣言が出された事による余波は\x01",
            "徐々に国内外に広がっていった。\x02\x03",

            "結界に包まれた市内の動きは\x01",
            "杳#2Rよう#として知れなかったが……\x02\x03",

            "国防軍兵士たちの動揺は少なくなく、\x01",
            "ベルガード門、タングラム門などでは\x01",
            "指揮系統の乱れも表面化し始めた。\x02\x03",

            "そんな中──\x01",
            "ロイドたちの乗艦するメルカバに\x01",
            "ある人物からの連絡が入ってきた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x23, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_24B end

    def Function_3_17C1(): pass

    label("Function_3_17C1")


    def lambda_17C6():
        OP_95(0xFE, 35000, 0, -100, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17C6)
    WaitChrThread(0x9, 1)

    def lambda_17E4():
        OP_95(0xFE, 40000, 0, -100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17E4)

    def lambda_17FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_17FE)
    Return()

    # Function_3_17C1 end

    def Function_4_180B(): pass

    label("Function_4_180B")


    def lambda_1810():
        OP_95(0xFE, 35000, 0, -700, 2800, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1810)
    WaitChrThread(0xA, 1)

    def lambda_182E():
        OP_95(0xFE, 40000, 0, -700, 2800, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_182E)

    def lambda_1848():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1848)
    Return()

    # Function_4_180B end

    def Function_5_1855(): pass

    label("Function_5_1855")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    OP_68(18000, 1300, 104100, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 100, 116250, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 18000, 0, 90000, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x4)
    Sound(103, 0, 100, 0)
    OP_68(18000, 1300, 114100, 7000)
    SetCameraDistance(14500, 7000)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1942():
        OP_96(0xFE, 0x4650, 0x0, 0x1B580, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1942)
    WaitChrThread(0xE, 1)
    OP_64(0xE)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    def lambda_1991():
        OP_96(0xFE, 0x4650, 0x96, 0x1C520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1991)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrSubChip(0x8, 0x1)
    Sound(886, 0, 100, 0)
    Sleep(500)

    #C0040
    ChrTalk(
        0x8,
        (
            "#5P#11307F#4S《結界》が消滅しただと！？\x02\x03",

            "#11310Fくっ……\x01",
            "《結社》の連中も不甲斐ない。\x02\x03",

            "#11303Fこうなったら全ての《神機#4Rアイオーン#》を\x01",
            "都市防衛に回すべきか……\x02\x03",

            "#11307F──国防長官を呼べ！\x01",
            "ベルとシグムントたちもだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xE,
        "#12Pしょ、承知しました！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_93(0xE, 0xB4, 0x1F4)

    def lambda_1AE0():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1AE0)
    OP_0D()
    EndChrThread(0xE, 0xFF)
    OP_6F(0x79)
    SetScenarioFlags(0x23, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1855 end

    def Function_6_1B09(): pass

    label("Function_6_1B09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 18000, 200, 116400, 180)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    OP_68(18000, 1200, 115600, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_6_1B09 end

    SaveToFile()

Try(main)
