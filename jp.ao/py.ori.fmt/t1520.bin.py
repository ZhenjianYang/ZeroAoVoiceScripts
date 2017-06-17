from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1520.bin",                # FileName
        "t1520",                    # MapName
        "t1520",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 5, 0, 6],
    )

    BuildStringList((
        "t1520",                  # 0
        "マローネ",               # 1
        "アーシュラ主任",         # 2
        "診察医ベルダイン",       # 3
        "看護師メイファ",         # 4
        "セシル",                 # 5
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "apl/ch50146.itc",                   # 01
        "chr/ch29300.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch05300.itc",                   # 04
    ))

    DeclNpc(-5199,   0,       17700,   90,   261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(92529,   400,     49430,   315,  469,  0x0, 0,   1,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-98839,  0,       53500,   180,  389,  0x0, 0,   2,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(204669,  0,       53000,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(154500,  0,       53400,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)

    DeclActor(95330,   0,       56250,   1200,    95330,   550,     56250,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(400, 0)                                        # 0

    ScpFunction((
        "Function_0_190",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_2A1",          # 02, 2
        "Function_3_302",          # 03, 3
        "Function_4_32D",          # 04, 4
        "Function_5_340",          # 05, 5
        "Function_6_49E",          # 06, 6
        "Function_7_4ED",          # 07, 7
        "Function_8_59E",          # 08, 8
        "Function_9_662",          # 09, 9
        "Function_10_122F",        # 0A, 10
        "Function_11_1D96",        # 0B, 11
        "Function_12_1E85",        # 0C, 12
        "Function_13_1F92",        # 0D, 13
    ))


    def Function_0_190(): pass

    label("Function_0_190")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C8"),
        (1, "loc_1D4"),
        (2, "loc_1E0"),
        (3, "loc_1EC"),
        (4, "loc_1F8"),
        (5, "loc_204"),
        (6, "loc_210"),
        (SWITCH_DEFAULT, "loc_21C"),
    )


    label("loc_1C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_204")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_210")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_228")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_23F")

    Return()

    # Function_0_190 end

    def Function_1_240(): pass

    label("Function_1_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A0")
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -310, 0, 3650, 2000, 0x0)
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -14660, 0, 17700, 2000, 0x0)
    Jump("Function_1_240")

    label("loc_2A0")

    Return()

    # Function_1_240 end

    def Function_2_2A1(): pass

    label("Function_2_2A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_301")
    OP_95(0xFE, 79630, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 2680, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    Jump("Function_2_2A1")

    label("loc_301")

    Return()

    # Function_2_2A1 end

    def Function_3_302(): pass

    label("Function_3_302")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32C")
    OP_94(0xFE, 0xFFFE741A, 0xCD5A, 0xFFFE86D0, 0xD548, 0x3E8)
    Sleep(400)
    Jump("Function_3_302")

    label("loc_32C")

    Return()

    # Function_3_302 end

    def Function_4_32D(): pass

    label("Function_4_32D")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_4_32D end

    def Function_5_340(): pass

    label("Function_5_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_354")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_379")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_38D")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B7")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_49D")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DC")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F0")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_415")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_429")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_442")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_49D")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47D")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 4)
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49D")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_49D")
    BeginChrThread(0x8, 0, 0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49D")
    ClearChrFlags(0xC, 0x80)

    label("loc_49D")

    Return()

    # Function_5_340 end

    def Function_6_49E(): pass

    label("Function_6_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4B0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4EC")

    Return()

    # Function_6_49E end

    def Function_7_4ED(): pass

    label("Function_7_4ED")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『クロスベル郷土料理入門』がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_59A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『煮込みシチュー』\x07\x00",
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_59A")

    TalkEnd(0xFF)
    Return()

    # Function_7_4ED end

    def Function_8_59E(): pass

    label("Function_8_59E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3")
    Call(0, 9)
    Jump("loc_65E")

    label("loc_5B3")


    #C0003
    ChrTalk(
        0xC,
        (
            "#01303Fガイさんの事件の真相が分かれば、\x01",
            "私も前に進めるかもしれないけど……\x02\x03",

            "#01300F無理はしないでね。\x01",
            "あなたたちが何事もなく暮らせるのが\x01",
            "私の何よりの願いなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E")

    TalkEnd(0xFE)
    Return()

    # Function_8_59E end

    def Function_9_662(): pass

    label("Function_9_662")

    EventBegin(0x0)
    Fade(500)
    OP_68(153430, 700, 53830, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20790, 0)
    SetChrPos(0x101, 153010, 0, 53370, 90)
    SetChrPos(0x102, 152340, 0, 54310, 90)
    SetChrPos(0x104, 151800, 0, 52830, 90)
    SetChrPos(0x109, 151060, 0, 54090, 90)
    SetChrPos(0x105, 150790, 0, 53090, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis000.itp")
    OP_4B(0xC, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_0D()

    #C0004
    ChrTalk(
        0xC,
        (
            "#11P#01300F……あら、ロイドたち。\x02\x03",

            "セイランド教授の\x01",
            "お仕事は終わったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#6P#00000Fああ、ついさっきね。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        "#6P#00300Fセシルさんは休憩中ッスか？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "#11P#01302Fふふ、今日は宿直があるから\x01",
            "色々と準備に戻っていた所なの。\x02\x03",

            "#01304F眠気覚ましのためにも\x01",
            "お気に入りの紅茶を\x01",
            "持っていっておこうと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        "#00105F相変わらず忙しそうですね……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#6P#00001F本当、体には気をつけてくれよな。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xC,
        (
            "#11P#01309Fふふ、大丈夫よ。\x01",
            "こう見えて私はタフなんだから。\x02\x03",

            "#01304F……そういうところはガイさんに\x01",
            "影響された部分もあるかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0011
    ChrTalk(
        0x109,
        (
            "#6P#10105Fそういえば、さっき写真を\x01",
            "見ていたみたいでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#6P#10300Fもしかして、\x01",
            "その写真の人がそうなのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        "#11P#01300Fふふ、見てみる？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0014
    AnonymousTalk(
        0x101,
        (
            "#00003Fこの写真は３年前のものになるかな。\x02\x03",

            "#00002F右側に写っているのが\x01",
            "俺の兄貴、ガイ・バニングスだ。\x02",
        )
    )

    CloseMessageWindow()

    #A0015
    AnonymousTalk(
        0x109,
        (
            "#10105Fへえ、この人が……\x02\x03",

            "#10102Fふふ、ロイドさんのお兄さんだけあって\x01",
            "とってもまっすぐそうな方ですね。\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0x104,
        (
            "#00309Fセシルさんも相当にお美しいッス！！\x02\x03",

            "#00306Fくぅっ、俺もセシルさんの\x01",
            "幼馴染になりたかったなあ……\x02",
        )
    )

    CloseMessageWindow()

    #A0017
    AnonymousTalk(
        0x102,
        (
            "#00106Fふう、ランディったら。\x02\x03",

            "#00102Fでも、こうして見ると……\x01",
            "本当にセシルさんとお似合いの方\x01",
            "だったんだなって思います。\x02",
        )
    )

    CloseMessageWindow()

    #A0018
    AnonymousTalk(
        0xC,
        (
            "#01309Fふふ、ありがとう。\x01",
            "そう言ってくれるとうれしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #A0019
    AnonymousTalk(
        0x105,
        (
            "#10302Fフフ、それに幼いロイドもなかなか\x01",
            "カワイイ顔してるじゃない。\x02\x03",

            "#10304Fこの写真を見ただけでも、\x01",
            "純粋な婦女子を惑わす君の魔性、\x01",
            "その片鱗が見て取れる気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0x101,
        "#00011F#4Sはあっ……！？\x02",
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0x109,
        "#10106F（た、確かに……）\x02",
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0x102,
        (
            "#00111F（当時から今のノリだったとしたら、\x01",
            "  かなりの危険人物に違いないわね……）\x02",
        )
    )

    CloseMessageWindow()

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#00006F……なんだかまた妙なレッテルを\x01",
            "貼られてる気がするんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0xC,
        "#01309Fふふっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #C0025
    ChrTalk(
        0xC,
        (
            "#11P#01303F……思えばこの写真を撮った時から\x01",
            "色々なものが変わってしまったわね。\x02\x03",

            "#01308Fガイさんが亡くなった日から\x01",
            "変われないでいるのは\x01",
            "私だけなのかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00005Fセシル姉……\x02\x03",

            "#00003F少し時間はかかるかもしれないけど……\x01",
            "待っていてくれ。\x02\x03",

            "#00000F兄貴の事件の真相は、いつか必ず\x01",
            "俺が掴んでみせるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00100Fええ、私たちもその手伝いを\x01",
            "させてもらうつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        (
            "#11P#01304F……ふふ、ありがとうみんな。\x02\x03",

            "#01300Fだけど、無理はしないでね。\x01",
            "あなたたちが何事もなく暮らせるのが\x01",
            "私の何よりの願いなんだから。\x02\x03",

            "#01309Fもし病院に運び込まれたりしたら、\x01",
            "セイランド教授にお願いして\x01",
            "ニガ～いお薬を処方してもらうからね？\x02",
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

    #C0029
    ChrTalk(
        0x104,
        (
            "#6P#00306Fあの女医センセイの作る薬だったら\x01",
            "ものすごく効き目はありそうッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、本気を出したらニガさすらも\x01",
            "自在にコントロールしてきそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#6P#00012Fき、気をつけさせてもらうよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1CB, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 152510, 0, 53400, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_93(0xC, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_9_662 end

    def Function_10_122F(): pass

    label("Function_10_122F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_136B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F7")

    #C0032
    ChrTalk(
        0x8,
        "さっさっさ、さっさのさ……♪\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "外来受付が再開して\x01",
            "病院の皆さんは張り切ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "皆さんに頑張ってもらえるように、\x01",
            "いつもより気合をいれて掃除しなきゃね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1366")

    label("loc_12F7")


    #C0035
    ChrTalk(
        0x8,
        "さっさっさ、さっさのさ……♪\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "皆さんに頑張ってもらえるように、\x01",
            "いつもより気合をいれて掃除しなきゃね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1366")

    Jump("loc_1D92")

    label("loc_136B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1414")

    #C0037
    ChrTalk(
        0x8,
        (
            "最近、寮から出て行く研修医や\x01",
            "先生たちの表情が暗い気がするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "通院していた街の患者さんたちの\x01",
            "ほとんどが来れなくなっているし、\x01",
            "やっぱり心配よね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_14B9")

    #C0039
    ChrTalk(
        0x8,
        (
            "ポリセさんとタップさんが\x01",
            "寮の掃除や食事運びを\x01",
            "手伝ってくれるから助かってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "せっかくだし、このまま病院に\x01",
            "就職してくれると私も助かるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_14B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1545")

    #C0041
    ChrTalk(
        0x8,
        (
            "今はメイファさんが\x01",
            "部屋でお休みになってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "皆さん普段から働きづめだし、\x01",
            "この機にしっかりと休んで欲しいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1652")

    #C0043
    ChrTalk(
        0x8,
        (
            "ここ数日は、沢山の方が\x01",
            "襲撃事件の患者のお見舞いに\x01",
            "訪れているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "特に被害の大きかった\x01",
            "警察や警備隊の家族の方たちは、\x01",
            "表情が曇っていて……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "自分の家族があんな事件に\x01",
            "巻き込まれたら……そう思うと、\x01",
            "私も胸が引き裂かれそうだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F6")

    label("loc_1652")


    #C0046
    ChrTalk(
        0x8,
        (
            "ここ数日は、沢山の方が\x01",
            "襲撃事件の患者のお見舞いに\x01",
            "訪れているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "自分の家族があんな事件に\x01",
            "巻き込まれたら……そう思うと、\x01",
            "私も胸が引き裂かれそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F6")

    Jump("loc_1D92")

    label("loc_16FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_178C")

    #C0048
    ChrTalk(
        0x8,
        (
            "列車事故が起こって、\x01",
            "先生や研修医さんたちは\x01",
            "みんな出払ってるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "いまのうちに、すみずみまで\x01",
            "掃除しておくとしましょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_18BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1846")

    #C0050
    ChrTalk(
        0x8,
        (
            "事務長の話によると、\x01",
            "明日は朝から雨が降るらしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "なんでも、導力ネットで\x01",
            "天気予報が見られるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "はー、便利な世の中に\x01",
            "なったものよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18BA")

    label("loc_1846")


    #C0053
    ChrTalk(
        0x8,
        "明日は朝から雨が降るらしいわ。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "導力ネットを使って\x01",
            "天気予報が見られるなんて、\x01",
            "便利な世の中になったわよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BA")

    Jump("loc_1D92")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")

    #C0055
    ChrTalk(
        0x8,
        (
            "アリオスさん、\x01",
            "娘さんが手術している間は\x01",
            "ずっと落ち着かない様子だったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "《風の剣聖》だなんて言われて、\x01",
            "雲の上の人みたいに感じてる人も\x01",
            "多いだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "ああいう姿を見ると、\x01",
            "どこにでもいる娘想いの\x01",
            "お父さんなんだって思うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A64")

    label("loc_19CA")


    #C0058
    ChrTalk(
        0x8,
        (
            "アリオスさん、\x01",
            "娘さんが手術している間は\x01",
            "ずっと落ち着かない様子だったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "ああいう姿を見ると、\x01",
            "どこにでもいる娘想いの\x01",
            "お父さんなんだって思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A64")

    Jump("loc_1D92")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1AF2")

    #C0060
    ChrTalk(
        0x8,
        (
            "今日は珍しく\x01",
            "ベルダイン先生がお休みみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "近頃は本当に休みなく\x01",
            "働いてたみたいだし、\x01",
            "しっかり休んでほしいわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA4")

    #C0062
    ChrTalk(
        0x8,
        (
            "さっさっさ……♪\x01",
            "こっちは女子寮よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "男子寮よりも、\x01",
            "気持ち丁寧にお掃除しないとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "……ふふ、冗談よ。\x01",
            "私、掃除に関しては真剣なんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C3E")

    label("loc_1BA4")


    #C0065
    ChrTalk(
        0x8,
        (
            "あら、もしかして……\x01",
            "アーシュラ主任ったら\x01",
            "また寝坊してるのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "うーん、昨日も遅くまで\x01",
            "研究棟に居たみたいだし、\x01",
            "無理に起こすのも可哀想かも。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C3E")

    Jump("loc_1D92")

    label("loc_1C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1C")

    #C0067
    ChrTalk(
        0x8,
        (
            "さっさっさ……♪\x01",
            "お・そ・う・じ・楽しいな～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "……あら、誰かに用事かしら？\x01",
            "男子寮は見ての通り掃除中よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "先生や研修医さんたちなら、\x01",
            "みんな出かけてるわよ。\x01",
            "病棟を探してみたら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D92")

    label("loc_1D1C")


    #C0070
    ChrTalk(
        0x8,
        (
            "さっさっさ……♪\x01",
            "うん、とっても綺麗になったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "このままテラスにでて、\x01",
            "美味しい空気を吸ってこようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    TalkEnd(0xFE)
    Return()

    # Function_10_122F end

    def Function_11_1D96(): pass

    label("Function_11_1D96")

    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1C")

    #C0072
    ChrTalk(
        0x9,
        (
            "……導力レントゲンで\x01",
            "隅々まで調べちゃいますよ～♪\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        "……す～……すぴ～……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00006Fね、寝言か……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E6F")

    label("loc_1E1C")


    #C0075
    ChrTalk(
        0x9,
        (
            "……ありゃりゃ、\x01",
            "感光クオーツが切れちゃってる……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "……す～……すぴ～……\x02",
    )

    CloseMessageWindow()

    label("loc_1E6F")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_1D96 end

    def Function_12_1E85(): pass

    label("Function_12_1E85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F39")

    #C0077
    ChrTalk(
        0xA,
        (
            "研修医たちから\x01",
            "いい加減休めと言われてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "そういえば、ちゃんとした休日は\x01",
            "何ヶ月かぶりだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "せっかくだ、今日は全力で\x01",
            "休ませてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F8E")

    label("loc_1F39")


    #C0080
    ChrTalk(
        0xA,
        "体調管理も確かに大事だ。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "せっかくの休日だ、\x01",
            "今日は全力で休ませてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8E")

    TalkEnd(0xFE)
    Return()

    # Function_12_1E85 end

    def Function_13_1F92(): pass

    label("Function_13_1F92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FA3")
    Jump("loc_2172")

    label("loc_1FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1FB1")
    Jump("loc_2172")

    label("loc_1FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1FBF")
    Jump("loc_2172")

    label("loc_1FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D6")

    #C0082
    ChrTalk(
        0xB,
        (
            "外来が止まってるから、\x01",
            "最近はちょくちょく休みが\x01",
            "もらえてるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "こんな時だし素直に喜べないけど、\x01",
            "休めるときに休んでおけって\x01",
            "師長にも言われちゃったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "でも、シロンのやつを\x01",
            "放っておくのだけは心配だわ……\x01",
            "あとで様子を見に行こうかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2172")

    label("loc_20D6")


    #C0085
    ChrTalk(
        0xB,
        (
            "シロンのやつ……\x01",
            "私がいない間にへんてこなことを\x01",
            "していないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "……あー、やめやめ。\x01",
            "シロンの心配してたらちっとも\x01",
            "気が休まらないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2172")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F92 end

    SaveToFile()

Try(main)
