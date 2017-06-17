from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t4020.bin",                # FileName
        "t4020",                    # MapName
        "t4020",                    # Location
        0x005D,                     # MapIndex
        "ed7124",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 260000, 0, 0, 0, 0, 1, 93, 0, 2, 0, 3],
    )

    BuildStringList((
        "t4020",                  # 0
        "クイント老人",           # 1
    ))

    AddCharChip((
        "chr/ch20000.itc",                   # 00
    ))

    DeclNpc(260260,  0,       250,     0,    257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)

    ScpFunction((
        "Function_0_E8",           # 00, 0
        "Function_1_1A0",          # 01, 1
        "Function_2_1CB",          # 02, 2
        "Function_3_31C",          # 03, 3
        "Function_4_32F",          # 04, 4
        "Function_5_CCC",          # 05, 5
        "Function_6_FB1",          # 06, 6
        "Function_7_10A9",         # 07, 7
        "Function_8_194E",         # 08, 8
        "Function_9_1F31",         # 09, 9
        "Function_10_2171",        # 0A, 10
        "Function_11_21A4",        # 0B, 11
        "Function_12_21D4",        # 0C, 12
    ))


    def Function_0_E8(): pass

    label("Function_0_E8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_128"),
        (1, "loc_134"),
        (2, "loc_140"),
        (3, "loc_14C"),
        (4, "loc_158"),
        (5, "loc_164"),
        (6, "loc_170"),
        (SWITCH_DEFAULT, "loc_17C"),
    )


    label("loc_128")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_134")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_140")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_14C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_158")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_164")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_170")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_17C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_188")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_188")

    label("loc_19F")

    Return()

    # Function_0_E8 end

    def Function_1_1A0(): pass

    label("Function_1_1A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CA")
    OP_94(0xFE, 0x3F516, 0xFFFFFA38, 0x3FD0E, 0x8B6, 0x3E8)
    Sleep(600)
    Jump("Function_1_1A0")

    label("loc_1CA")

    Return()

    # Function_1_1A0 end

    def Function_2_1CB(): pass

    label("Function_2_1CB")

    BeginChrThread(0x8, 0, 0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9")
    Event(0, 9)

    label("loc_1E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_209")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204")
    SetChrFlags(0x8, 0x80)

    label("loc_204")

    Jump("loc_31B")

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_242")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23D")
    SetChrPos(0x8, 260000, 0, 2000, 270)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_23D")

    Jump("loc_31B")

    label("loc_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_27B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_276")
    SetChrPos(0x8, 260000, 0, 2000, 270)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_276")

    Jump("loc_31B")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_28E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_28E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B4")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C2")
    Jump("loc_31B")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_31B")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_31B")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_304")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31B")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_31B")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_31B")

    label("loc_31B")

    Return()

    # Function_2_1CB end

    def Function_3_31C(): pass

    label("Function_3_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_32E")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_32E")

    Return()

    # Function_3_31C end

    def Function_4_32F(): pass

    label("Function_4_32F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C6")
    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "お前たちのおかげで\x01",
            "大事な友人たちに墓参りもできた。\x01",
            "本当にありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "また何かあったら\x01",
            "連絡させていただこう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_3C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F4")
    Call(0, 8)
    Return()

    label("loc_3F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E8")
    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "何度も依頼を確認するのは\x01",
            "未熟を曝すようで感心しないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "花の場所は手帳に\x01",
            "メモをとっていたのだろう？\x01",
            "そちらを確認するといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "３つの花を全て集めたら、\x01",
            "私の所に持ってきてほしい。\x01",
            "よろしく頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_4E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_501")
    Call(0, 5)
    Return()

    label("loc_501")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_70C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xEA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FD")

    #C0006
    ChrTalk(
        0xFE,
        (
            "こんな夕方は、\x01",
            "ガイのことを思い出すな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ロイド、お前がいつか\x01",
            "一人前になったら……\x01",
            "そのときは一緒に酒を飲もう。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "私がガイの好きだった酒を\x01",
            "おごろうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#0004Fええ、楽しみにしています。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xEA, 0)
    Jump("loc_68F")

    label("loc_5FD")


    #C0010
    ChrTalk(
        0xFE,
        (
            "ガイが休みの日は、\x01",
            "よく酒を持ち込んで\x01",
            "ここで飲み明かしたものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "ロイド、お前がいつか\x01",
            "一人前になったら……\x01",
            "そのときは一緒に酒を飲もう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68F")

    Jump("loc_707")

    label("loc_694")


    #C0012
    ChrTalk(
        0xFE,
        (
            "こんな夕方は、\x01",
            "奴のことを思い出すな……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "……ほっほっほ、\x01",
            "ムダ話をしてしまったようだ。\x01",
            "忘れてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_707")

    Jump("loc_CC8")

    label("loc_70C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_781")

    #C0014
    ChrTalk(
        0xFE,
        "さて……今日も一日が始まるな。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "随分昔に家族を亡くした私には\x01",
            "この墓守の仕事がすべてなのだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC8")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7F6")

    #C0016
    ChrTalk(
        0xFE,
        (
            "この国には口には出さなくとも、\x01",
            "大きな傷を抱えた者がごまんといる。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "……心に留めておくといい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC8")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_804")
    Jump("loc_CC8")

    label("loc_804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_812")
    Jump("loc_CC8")

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_820")
    Jump("loc_CC8")

    label("loc_820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_8C8")

    #C0018
    ChrTalk(
        0xFE,
        (
            "さっき街へ買出しに行ったら\x01",
            "港湾区に人だかりができていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ミシュラム保養地で\x01",
            "遊んで回るつもりなのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "……私ももう少し若ければな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CC8")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_8D6")
    Jump("loc_CC8")

    label("loc_8D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_967")

    #C0021
    ChrTalk(
        0xFE,
        (
            "墓参りに来ている夫人に\x01",
            "記念祭中くらいは\x01",
            "楽しんではどうかと言ってみたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……差し出がましい真似を\x01",
            "してしまったかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC8")

    label("loc_967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A35")

    #C0023
    ChrTalk(
        0xFE,
        (
            "昨日は思った以上に\x01",
            "賑やかなミサになった。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "参拝客の殆どは、\x01",
            "ミサの後にこの墓地に\x01",
            "祈りに来ていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "創立７０年……\x01",
            "やはり今年は誰にとっても、\x01",
            "特別な年なのだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A7B")

    label("loc_A35")


    #C0026
    ChrTalk(
        0xFE,
        (
            "創立７０年……\x01",
            "やはり今年は誰にとっても、\x01",
            "特別な年なのだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7B")

    Jump("loc_CC8")

    label("loc_A80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_A8E")
    Jump("loc_CC8")

    label("loc_A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_B85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B27")

    #C0027
    ChrTalk(
        0xFE,
        (
            "そういえば、\x01",
            "来月はもう創立記念祭か。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "……時が経つのは早いもんだ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "こんな所で過ごしているから\x01",
            "かもしれんがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B80")

    label("loc_B27")


    #C0030
    ChrTalk(
        0xFE,
        "来月はもう創立記念祭か……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "去年の記念祭が\x01",
            "まるで昨日のことのように思えるわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B80")

    Jump("loc_CC8")

    label("loc_B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")

    #C0032
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州では\x01",
            "帝国と共和国の狭間で\x01",
            "数々の争いに巻き込まれてきた……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "時代の奔流に飲み込まれ\x01",
            "潰えてしまった命も多い。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "どうか彼らのために\x01",
            "祈りを捧げてやって欲しい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CC8")

    label("loc_C58")


    #C0035
    ChrTalk(
        0xFE,
        (
            "クロスベル市は発展において\x01",
            "多くの命を犠牲にしてきた……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "どうか彼らのために\x01",
            "祈りを捧げてやって欲しい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC8")

    TalkEnd(0xFE)
    Return()

    # Function_4_32F end

    def Function_5_CCC(): pass

    label("Function_5_CCC")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D74")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_D74")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECB")

    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#0000Fすみません。\x01",
            "クイントさん、でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x8,
        "#5P……警察かな？\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#0000Fあ、はい。\x01",
            "支援要請を受けてきました\x01",
            "特務支援課の者です。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#5P……ふむ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#5P君たちに任せたい仕事は、\x01",
            "お供えをするための\x01",
            "３種類の花を集める事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "#5P早速、引き受けてもらえるかね？\x02",
    )

    CloseMessageWindow()
    OP_29(0x2E, 0x1, 0x0)
    Jump("loc_F63")

    label("loc_ECB")


    #C0043
    ChrTalk(
        0x8,
        (
            "#5Pふむ、他の用事は\x01",
            "片付いたのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#5P君たちに任せたい仕事は、\x01",
            "お供えをするための\x01",
            "３種類の花を集める事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        "#5P引き受けてもらえるかね？\x02",
    )

    CloseMessageWindow()

    label("loc_F63")

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78")
    Call(0, 7)

    label("loc_F78")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F92")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_F92")

    SetChrPos(0x0, 259600, 0, -300, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_CCC end

    def Function_6_FB1(): pass

    label("Function_6_FB1")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A8")

    #C0046
    ChrTalk(
        0x101,
        (
            "#12P#0006F申し訳ないんですが……\x01",
            "今、別件の用事があって\x01",
            "すぐには……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#5Pふむ、そうか。\x01",
            "しかたあるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "#5P引き受けられるようになったら\x01",
            "再び訪ねてきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A8")

    Return()

    # Function_6_FB1 end

    def Function_7_10A9(): pass

    label("Function_7_10A9")


    #C0049
    ChrTalk(
        0x101,
        (
            "#12P#0000F了解しました、\x01",
            "お引き受けします。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        "#5Pうむ、よろしい。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#5P早速だが、\x01",
            "君たちに集めてほしい\x01",
            "３種類の花を教えよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "#5Pメモの準備はよろしいかな？\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#12P#0005Fあ、はい。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0054
    ChrTalk(
        0x101,
        "#12P#0000Fティオ、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#12P#0203F了解です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0056
    ChrTalk(
        0x8,
        (
            "#5P１つは『レヴァスの花』。\x01",
            "西クロスベル街道の\x01",
            "警察学校付近に咲いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#5P２つめは『リクエムの花』。\x01",
            "こちらはクロスベル市西通りの\x01",
            "タリーズ商店で取り扱っている。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "#5P最後に『フィネルの花』。\x01",
            "東クロスベル街道に出てすぐの\x01",
            "見張り台の足元に咲いている。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P付近には似た花が咲いているかもしれん。\x01",
            "見落とさぬよう、気を付けることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "#5P……これらを全て集めたら、\x01",
            "私の所に持ってきてほしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#12P#0203F……場所はメモしました。\x02\x03",

            "#0200Fところで……\x01",
            "なぜこの３種類の花なのですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)

    #C0062
    ChrTalk(
        0x102,
        (
            "#0100Fこのクロスベル自治州では\x01",
            "黄、青、白の３色は\x01",
            "『鎮魂』を表すとされているの。\x02\x03",

            "葬儀の際にはその３色の花で\x01",
            "花束を作って、死者に手向けるのが\x01",
            "クロスベルの伝統なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        "#12P#0305Fへぇ、花言葉ってやつか？\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#12P#0203F微妙に違うと\x01",
            "思いますけど……\x02\x03",

            "#0200Fどちらかというと\x01",
            "クロスベルの土地柄に\x01",
            "よるものかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#0003F（そういえば、兄貴の葬式でも\x01",
            "  ３色の花束が手向けられたっけ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#5P…………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x101,
        "#12P#0005Fあ、あの……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#12P#0305Fどうしたんッスか、黙って。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "#5Pいや、なに。\x01",
            "物を知らない若者たちに\x01",
            "少しばかり落胆していたのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "#5Pそんなことでは\x01",
            "先が思いやられるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#12P#0005Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        (
            "#12P#0300Fはは、すいませんねぇ。\x01",
            "俺なんかはクロスベル出身じゃ\x01",
            "ないもんで。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        "#5Pふむ、まぁいいわい。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "#5P用件は伝えた。\x01",
            "早速取り掛かってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#12P#0005Fりょ、了解しました。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_18EA")

    #C0076
    ChrTalk(
        0x10A,
        "#6P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_17A5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A5)
    Sleep(50)

    def lambda_17B5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17B5)
    Sleep(50)

    def lambda_17C5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17C5)
    Sleep(50)

    def lambda_17D5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_17D5)

    #C0077
    ChrTalk(
        0x101,
        (
            "#11P#0012Fえっと……\x01",
            "そういうわけ、なんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x10A,
        (
            "#6P#0600F……フン。\x01",
            "なにがそういうわけ、だ。\x02\x03",

            "#0606Fまぁいい、ここまで聞いて\x01",
            "依頼を受けないわけにもいくまい。\x02\x03",

            "#0600Fやるならやるで、完璧に片付けて\x01",
            "さっさと捜査を再開するぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        "#12P#0309Fあいよ、了解ッス！\x02",
    )

    CloseMessageWindow()

    label("loc_18EA")

    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【鎮魂の花集め】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x2E, 0x1, 0x1)
    Return()

    # Function_7_10A9 end

    def Function_8_194E(): pass

    label("Function_8_194E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_4B(0x8, 0xFF)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_19FF")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_19FF")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x40)
    FadeToBright(500, 0)
    OP_0D()

    #C0081
    ChrTalk(
        0x101,
        (
            "#12P#0000Fクイントさん、\x01",
            "ただいま戻りました。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "#5Pうむ。\x01",
            "なかなか早かったじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "#5P花は全て集まったのかな？\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#12P#0000Fええ、確認をお願いします。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x349),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02\x03",
            scpstr(SCPSTR_CODE_ITEM, 0x34A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02\x03",
            scpstr(SCPSTR_CODE_ITEM, 0x34B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x349, 1)
    SubItemNumber(0x34A, 1)
    SubItemNumber(0x34B, 1)

    #C0086
    ChrTalk(
        0x8,
        (
            "#5P……うむ、確かに。\x01",
            "３種類すべて集まっているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "#5Pご苦労だったな、\x01",
            "特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#12P#0000Fいえいえ、\x01",
            "依頼は依頼ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        (
            "#12P#0306Fは～、意外と大変だったな。\x02\x03",

            "雑貨屋に花がねぇなんて\x01",
            "ハプニングもあったしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x103,
        "#12P#0200Fまぁ、なんとかなりましたけどね。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#0100Fお爺さん、一つ聞いてもいいですか？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        "#5P……なんだね？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        (
            "#0103F最近の風習では、\x01",
            "葬儀でもないのに３色の花を揃える\x01",
            "ということは珍しいことです。\x02\x03",

            "#0100F今回は、なぜ３色の花束を？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "#5Pふむ、確かに今回は\x01",
            "葬儀があるわけでもなんでもないが……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#5P……折角だ、今からこの花を供えるから\x01",
            "君たちもついてきたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "#5P理由はそのときに話そう。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 11)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 11)
    BeginChrThread(0x104, 3, 0, 12)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E07")
    Sleep(200)

    def lambda_1DFF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1DFF)

    label("loc_1E07")

    WaitChrThread(0x8, 3)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x103,
        "#6P#0205F……どういうことですか？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#5P#0005Fさ、さあ……\x02\x03",

            "#0003Fよく分からないけど、\x01",
            "とにかく行ってみようか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F16")

    #C0099
    ChrTalk(
        0x10A,
        "#6P#0603F（……まさか……）\x02",
    )

    CloseMessageWindow()

    label("loc_1F16")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x2E, 0x1, 0x7)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_194E end

    def Function_9_1F31(): pass

    label("Function_9_1F31")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(259100, 1700, -800, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33530, 0)
    SetChrPos(0x101, 259000, 0, -300, 0)
    SetChrPos(0x102, 260200, 0, -300, 0)
    SetChrPos(0x103, 259000, 0, -1500, 0)
    SetChrPos(0x104, 260200, 0, -1500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FDA")
    SetChrPos(0x10A, 257760, 0, -580, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_1FDA")

    OP_93(0x8, 0xB4, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(30720, 3000)
    FadeToBright(500, 0)
    OP_0D()

    #C0100
    ChrTalk(
        0x8,
        (
            "#5Pお前たちのおかげで\x01",
            "大事な友人たちに墓参りもできた。\x01",
            "本当にありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "#5Pまた何かあったら\x01",
            "連絡させていただこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、お待ちしています。\x01",
            "……それでは。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【鎮魂の花集め】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -350, 0, 12250, 0)
    OP_29(0x2E, 0x4, 0x10)
    SetScenarioFlags(0x0, 1)
    Sleep(500)
    SetChrPos(0x0, 259600, 0, -300, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_216E")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_216E")

    EventEnd(0x5)
    Return()

    # Function_9_1F31 end

    def Function_10_2171(): pass

    label("Function_10_2171")


    def lambda_2176():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2176)
    Sleep(2500)

    def lambda_2193():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2193)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_2171 end

    def Function_11_21A4(): pass

    label("Function_11_21A4")


    def lambda_21A9():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21A9)
    WaitChrThread(0xFE, 1)

    def lambda_21C7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21C7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_21A4 end

    def Function_12_21D4(): pass

    label("Function_12_21D4")


    def lambda_21D9():
        OP_98(0xFE, 0x12C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21D9)
    WaitChrThread(0xFE, 1)

    def lambda_21F7():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21F7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_21D4 end

    SaveToFile()

Try(main)
