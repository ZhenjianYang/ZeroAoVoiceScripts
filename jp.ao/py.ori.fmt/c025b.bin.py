from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c025b.bin",                # FileName
        "c025b",                    # MapName
        "c025b",                    # Location
        0x000E,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c025b",                  # 0
        "レイテ",                 # 1
        "パンセ",                 # 2
        "コウケン",               # 3
    ))

    AddCharChip((
        "chr/ch10300.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch22302.itc",                   # 02
        "chr/ch32700.itc",                   # 03
        "chr/ch32702.itc",                   # 04
        "apl/ch50148.itc",                   # 05
        "chr/ch21000.itc",                   # 06
        "chr/ch21002.itc",                   # 07
    ))

    DeclNpc(51830,   0,       115930,  0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-54310,  0,       52840,   90,   261,  0x0, 0,   1,   0,   0,   1,   0,   5,   255,  0)
    DeclNpc(-51919,  0,       108370,  90,   261,  0x0, 0,   6,   0,   0,   0,   0,   6,   255,  0)

    ChipFrameInfo(292, 0)                                        # 0

    ScpFunction((
        "Function_0_124",          # 00, 0
        "Function_1_1D4",          # 01, 1
        "Function_2_1FF",          # 02, 2
        "Function_3_226",          # 03, 3
        "Function_4_227",          # 04, 4
        "Function_5_29E",          # 05, 5
        "Function_6_3AF",          # 06, 6
    ))


    def Function_0_124(): pass

    label("Function_0_124")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_15C"),
        (1, "loc_168"),
        (2, "loc_174"),
        (3, "loc_180"),
        (4, "loc_18C"),
        (5, "loc_198"),
        (6, "loc_1A4"),
        (SWITCH_DEFAULT, "loc_1B0"),
    )


    label("loc_15C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_168")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_174")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_180")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_18C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_198")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1BC")

    label("loc_1D3")

    Return()

    # Function_0_124 end

    def Function_1_1D4(): pass

    label("Function_1_1D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FE")
    OP_94(0xFE, 0xFFFF28BA, 0xC9A4, 0xFFFF30C6, 0xD2C8, 0x3E8)
    Sleep(300)
    Jump("Function_1_1D4")

    label("loc_1FE")

    Return()

    # Function_1_1D4 end

    def Function_2_1FF(): pass

    label("Function_2_1FF")

    SetChrPos(0x9, -58130, 0, 58620, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    SetChrFlags(0x9, 0x10)

    label("loc_21F")

    BeginChrThread(0x9, 0, 0, 0)
    Return()

    # Function_2_1FF end

    def Function_3_226(): pass

    label("Function_3_226")

    Return()

    # Function_3_226 end

    def Function_4_227(): pass

    label("Function_4_227")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "あら、いつの間にか\x01",
            "空がすっかり暗くなったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "お父さんも帰ってくるし、\x01",
            "急いで食事の支度をしないと。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_227 end

    def Function_5_29E(): pass

    label("Function_5_29E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344")

    #C0003
    ChrTalk(
        0xFE,
        (
            "……あっ！\x01",
            "あたしのファッション誌の棚に\x01",
            "鉄道の本が混ざってる……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "絶対おとーさんの仕業ね。\x01",
            "何度おんなじ手を\x01",
            "使うつもりなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xFE, 0x10)
    Jump("loc_3AB")

    label("loc_344")


    #C0005
    ChrTalk(
        0xFE,
        (
            "おとーさん、時々こうやって\x01",
            "あたしを鉄道好きにしようとするの。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "まったく、コシャクなんだから。\x02",
    )

    CloseMessageWindow()

    label("loc_3AB")

    TalkEnd(0xFE)
    Return()

    # Function_5_29E end

    def Function_6_3AF(): pass

    label("Function_6_3AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B")

    #C0007
    ChrTalk(
        0xFE,
        (
            "リュウにはいつか問屋の仕事を\x01",
            "継がせたいと思っておるのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "こやつときたら\x01",
            "遊ぶ事ばかり覚えおってな。\x01",
            "やれやれじゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4BF")

    label("loc_44B")


    #C0009
    ChrTalk(
        0xFE,
        (
            "リュウの奴は日曜学校の成績も\x01",
            "さっぱりなのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "遊ばせるばかりじゃなくて、\x01",
            "少しは勉強させなければのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BF")

    TalkEnd(0xFE)
    Return()

    # Function_6_3AF end

    SaveToFile()

Try(main)
