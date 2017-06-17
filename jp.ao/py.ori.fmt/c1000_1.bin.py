from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000_1.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0010,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [88, 720921, 0, -16777216, 11796682, 28573696, 256, 16777216, 256, 0, 0, 256, -65280, 1660944639, 1936291423, 12336, 11831, 29801, 112, 202, 1, 0, 0],
    )

    BuildStringList((
        "c1000_1",                # 0
    ))

    ChipFrameInfo(88, 0)                                         # 0

    ScpFunction((
        "Function_0_58",           # 00, 0
    ))


    def Function_0_58(): pass

    label("Function_0_58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis232.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis233.itp")
    SoundLoad(803)
    SoundLoad(2711)
    SoundLoad(2712)
    Sleep(500)
    Sound(803, 2, 100, 0)
    Sleep(1600)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_25(0x80, 0x28)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0001
    AnonymousTalk(
        0x101,
        (
            "#00005Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2711V#30Wどうも、ロイドさん～！\x02\x03",

            "#2712V#30W雨の中ご苦労さまですー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA98)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0003
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002Fああ、フランか。\x02\x03",

            "#00000Fどうしたんだ？\x01",
            "緊急要請でも入ったか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "えっと、それが……\x02\x03",

            "マインツのビクセン町長を\x01",
            "覚えてらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0005
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fああ、もちろん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0006
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F……ひょっとして\x01",
            "鉱山町で何かあったのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、それが鉱山に\x01",
            "魔獣が現れたらしくって……\x02\x03",

            "あ、といっても、\x01",
            "町から少し離れた場所にある\x01",
            "旧鉱山らしいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0008
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F……？\x02\x03",

            "#00001Fそんな場所なら魔獣が現れても\x01",
            "おかしくはないと思うけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、鉱員の方たちが被害に\x01",
            "遭ったわけじゃなさそうです。\x02\x03",

            "ただ内部が、どうもおかしな事に\x01",
            "なっちゃっているみたいで……\x02\x03",

            "念のため調べてもらえないかと\x01",
            "いうことでした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0010
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003Fおかしな事……\x01",
            "ちょっと要領を得ないな。\x02\x03",

            "#00000F──判った。\x01",
            "市内の緊急要請は片付けたし、\x01",
            "これからマインツに向かうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、お願いしますー。\x02\x03",

            "あ、ついでにお伝えしますが\x01",
            "先ほどマインツ山道方面に\x01",
            "手配魔獣の指定が出ました。\x02\x03",

            "余裕があったら\x01",
            "対応してみてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0012
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002Fそうか、了解だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それと、クロスベル市と違って\x01",
            "山道方面は晴れているみたいです。\x02\x03",

            "せっかくだから導力車で\x01",
            "行ってみたらどうですか～？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0014
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004Fそうなのか……判った。\x02\x03",

            "#00000Fありがとう、フラン。\x01",
            "何かあったらまた連絡してくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("フランの声")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "はい、それでは失礼しますー。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 60, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sound(804, 0, 100, 0)
    Sleep(800)
    SetMessageWindowPos(240, 110, -1, -1)

    #A0016
    AnonymousTalk(
        0x109,
        "#10105Fフランからみたいですね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(200, 40, -1, -1)

    #A0017
    AnonymousTalk(
        0x102,
        (
            "#00101Fマインツ方面で\x01",
            "何かあったみたいだけど？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0018
    AnonymousTalk(
        0x101,
        (
            "#00006Fああ、旧鉱山という所で\x01",
            "妙なことが起きたらしい。\x02\x03",

            "#00000F市内の支援要請も片付けたし、\x01",
            "準備ができたら行ってみよう。\x02\x03",

            "#00002Fあ、山道方面は晴れているそうだから\x01",
            "車で行ってもいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(130, 30, -1, -1)

    #A0019
    AnonymousTalk(
        0x105,
        "#10304F了解、リーダー。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)

    #A0020
    AnonymousTalk(
        0x109,
        (
            "#10100Fもし車で鉱山町に行くなら\x01",
            "支援課の裏口に行きましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳と支援課の端末に\x01",
            "新たな手配魔獣が追加されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6D, 0x4, 0x2)
    OP_29(0xA1, 0x1, 0x12)
    OP_CC(0x1, 0xFF, 0x0)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x128, 7)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_25(0x80, 0x64)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_0_58 end

    SaveToFile()

Try(main)
