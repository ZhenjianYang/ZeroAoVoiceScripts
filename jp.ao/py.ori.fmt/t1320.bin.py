from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1320.bin",                # FileName
        "t1320",                    # MapName
        "t1320",                    # Location
        0x00BC,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 188, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1320",                  # 0
        "受付嬢カルミナ",         # 1
        "観光客",                 # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "監視員ウェイブ",         # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "水着カタログ",           # 8
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch24402.itc",                   # 01
        "chr/ch44200.itc",                   # 02
        "chr/ch48200.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch48200.itc",                   # 05
        "chr/ch48300.itc",                   # 06
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

    DeclNpc(-2000,   0,       5150,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-319,    200,     -5050,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1750,    0,       3230,    45,   385,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(106769,  0,       102819,  0,    385,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   104.0,                 4.5,                   -1.0,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -26.0,                 -2.25,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  8.850000381469727,     1.0,                   -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.425000190734863,    -0.25,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  88.52999877929688,     1.0,                   -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -44.26499938964844,    -0.25,                 0.20000000298023224,   1.0])

    DeclActor(-2000,   0,       4650,    2000,    -2000,   1500,    5150,    0x007E, 0,  3,  0x0000)
    DeclActor(99280,   0,       3850,    1200,    99070,   1500,    4220,    0x007C, 0,  8,  0x0000)
    DeclActor(104000,  0,       4600,    1200,    104000,  1500,    4600,    0x007C, 0,  24, 0x0000)
    DeclActor(94000,   0,       4600,    1200,    94000,   1500,    4600,    0x007C, 0,  24, 0x0000)

    ChipFrameInfo(1024, 0)                                       # 0

    ScpFunction((
        "Function_0_400",          # 00, 0
        "Function_1_4B0",          # 01, 1
        "Function_2_5AD",          # 02, 2
        "Function_3_686",          # 03, 3
        "Function_4_68A",          # 04, 4
        "Function_5_843",          # 05, 5
        "Function_6_894",          # 06, 6
        "Function_7_8D9",          # 07, 7
        "Function_8_A03",          # 08, 8
        "Function_9_B78",          # 09, 9
        "Function_10_CB6",         # 0A, 10
        "Function_11_DC2",         # 0B, 11
        "Function_12_E34",         # 0C, 12
        "Function_13_1009",        # 0D, 13
        "Function_14_218A",        # 0E, 14
        "Function_15_21AF",        # 0F, 15
        "Function_16_21D4",        # 10, 16
        "Function_17_3D69",        # 11, 17
        "Function_18_40D1",        # 12, 18
        "Function_19_4A5B",        # 13, 19
        "Function_20_4BBE",        # 14, 20
        "Function_21_7357",        # 15, 21
        "Function_22_7B96",        # 16, 22
        "Function_23_7BD3",        # 17, 23
        "Function_24_7C10",        # 18, 24
    ))


    def Function_0_400(): pass

    label("Function_0_400")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_438"),
        (1, "loc_444"),
        (2, "loc_450"),
        (3, "loc_45C"),
        (4, "loc_468"),
        (5, "loc_474"),
        (6, "loc_480"),
        (SWITCH_DEFAULT, "loc_48C"),
    )


    label("loc_438")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_444")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_450")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_45C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_468")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_474")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_48C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_4AF")

    Return()

    # Function_0_400 end

    def Function_1_4B0(): pass

    label("Function_1_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_4BE")
    SetChrFlags(0x8, 0x80)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0x8, 96490, 0, 1360, 90)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_542")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)
    Jump("loc_551")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_551")
    ClearScenarioFlags(0x22, 3)
    Event(0, 21)

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AC")
    Event(0, 12)

    label("loc_5AC")

    Return()

    # Function_1_4B0 end

    def Function_2_5AD(): pass

    label("Function_2_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F8")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_5F8")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_61D")
    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_61D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_64B")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_663")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_678")
    OP_65(0x0, 0x1)

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_685")
    OP_65(0x0, 0x1)

    label("loc_685")

    Return()

    # Function_2_5AD end

    def Function_3_686(): pass

    label("Function_3_686")

    Call(0, 4)
    Return()

    # Function_3_686 end

    def Function_4_68A(): pass

    label("Function_4_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A1")
    Call(0, 13)
    Return()

    label("loc_6A1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A1")

    #C0001
    ChrTalk(
        0x8,
        (
            "水着切り裂き魔を撃退してくださり、\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "相手は魔獣ですから、\x01",
            "完全に出なくなったとは\x01",
            "言い切れないかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "今後はミシュラム事業部のほうで\x01",
            "対策を行っていかないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_831")

    label("loc_7A1")


    #C0004
    ChrTalk(
        0x8,
        (
            "水着切り裂き魔を撃退してくださり、\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "今後はミシュラム事業部のほうで\x01",
            "対策を行っていかないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_831")

    Jump("loc_83F")

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_83F")

    label("loc_83F")

    TalkEnd(0x8)
    Return()

    # Function_4_68A end

    def Function_5_843(): pass

    label("Function_5_843")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        "今、カノジョが水着選んでんだ。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "……はやく決めてくんないかなあ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_843 end

    def Function_6_894(): pass

    label("Function_6_894")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        "やーん、かわいい水着が沢山ね。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "どれにしようかな～。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_894 end

    def Function_7_8D9(): pass

    label("Function_7_8D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_999")
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0xFE,
        "どわあああああっ！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "だ、男子更衣室に\x01",
            "女の子を入れるなよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005Fそ、そういえば。\x01",
            "……すいませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x153,
        "#01105Fほえー？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9FF")

    label("loc_999")


    #C0014
    ChrTalk(
        0xFE,
        (
            "ま、まったく……\x01",
            "油断もスキもありゃしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "危うく、女の子にお尻を\x01",
            "見られるところだったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF")

    TalkEnd(0xFE)
    Return()

    # Function_7_8D9 end

    def Function_8_A03(): pass

    label("Function_8_A03")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　湖水浴を楽しむ際のご注意\x01",
            "──────────────────\x01",
            "・必ず準備運動をして下さい。\x01",
            "・服を着たまま水に入らないで下さい。\x01",
            "  （水着は受付で貸し出しています）\x01",
            "・監視員の指示に従ってください。\x01",
            "──────────────────\x01",
            "  マナーを守って楽しく遊びましょう。\x01",
            "  　　　　　──ミシュラム事業部より\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_A03 end

    def Function_9_B78(): pass

    label("Function_9_B78")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCA")

    #C0017
    ChrTalk(
        0x101,
        (
            "#12500F……こっちは女子更衣室だ。\x01",
            "誤解されない内に離れよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C66")

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000F……っと。\x01",
            "こっちは女子更衣室だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x153,
        "#01105Fロイド、入っちゃうのー？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00006Fい、いやいや、入らないから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CA2")

    label("loc_C66")


    #C0021
    ChrTalk(
        0x101,
        (
            "#00000Fこっちは女子更衣室だ。\x01",
            "……入るのはやめとこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    SetChrPos(0x0, 104470, 0, 2310, 180)
    EventEnd(0x4)
    Return()

    # Function_9_B78 end

    def Function_10_CB6(): pass

    label("Function_10_CB6")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1E")

    #C0022
    ChrTalk(
        0x101,
        (
            "#00000Fまだ水着も借りていないのに\x01",
            "この先には行けないな。\x02\x03",

            "まずは受付を済ませよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAE")

    #C0023
    ChrTalk(
        0x101,
        (
            "#00003Fもう一度ビーチに入っている暇はないな。\x02\x03",

            "#00000Fそろそろテーマパークに向かおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x153,
        "#01109Fうん、れっつごー！！\x02",
    )

    CloseMessageWindow()

    label("loc_DAE")

    SetChrPos(0x0, 7010, 0, 1020, 270)
    EventEnd(0x4)
    Return()

    # Function_10_CB6 end

    def Function_11_DC2(): pass

    label("Function_11_DC2")

    EventBegin(0x1)

    #C0025
    ChrTalk(
        0x101,
        (
            "#12500Fおっと、この格好であまり\x01",
            "ウロウロするわけにもいかないな。\x02\x03",

            "早くビーチに出よう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91160, 0, 690, 90)
    EventEnd(0x4)
    Return()

    # Function_11_DC2 end

    def Function_12_E34(): pass

    label("Function_12_E34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -9000, 0, 1000, 90)
    SetChrPos(0x104, -9500, 0, 2130, 90)
    SetChrPos(0x105, -9500, 0, 130, 90)
    OP_68(2400, 1600, 1130, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_68(-5400, 1600, 1130, 5000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(-9350, 3500, 1480, 0)
    MoveCamera(316, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18050, 0)
    OP_68(-9350, 1500, 1480, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00002F#5Pへえ……\x01",
            "ここがビーチの受付か。\x02\x03",

            "#00000Fここで水着とかも\x01",
            "借りられるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00309F#5Pいや～、こんな場所が\x01",
            "作られてるなんて\x01",
            "夢にも思ってなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、早速、\x01",
            "受付を済ませておこうか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -8000, 0, 1130, 90)
    SetScenarioFlags(0x144, 6)
    EventEnd(0x5)
    Return()

    # Function_12_E34 end

    def Function_13_1009(): pass

    label("Function_13_1009")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51090.itc", 0x1E)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x9)
    SetChrPos(0xF, -1500, 1000, 3500, 0)
    SetChrFlags(0xF, 0x8)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, -2000, 0, 2500, 0)
    SetChrPos(0x104, -3000, 0, 2350, 0)
    SetChrPos(0x105, -1000, 0, 2450, 0)
    SetMapObjFlags(0x0, 0x1000)
    FadeToBright(1000, 0)
    OP_68(-2000, 1000, 3850, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18500, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0029
    ChrTalk(
        0x8,
        (
            "#11Pこんにちは、\x01",
            "ようこそ湖水浴場#8Rレイク・ビーチ#へ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P特務支援課の方々で\x01",
            "いらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#00005F#6Pあ、そうですけど。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#00302F#6Pマリアベルのお嬢さんが\x01",
            "伝えといてくれてたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11Pはい、本日の昼過ぎまで\x01",
            "貸し切りとなっております。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x0, 0x8, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(300)
    Sound(18, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0xF, 0x8)
    OP_0D()

    #C0034
    ChrTalk(
        0x8,
        (
            "#11P水着については、こちらの方に\x01",
            "写真#4Rサンプル#を用意しましたので\x01",
            "お好きなものをお選びください。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00002F#6Pへえ、それじゃあ……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#00309F#6Pさ～て、どれにすっかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x105,
        "#10308F#6P……………ふむ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    OP_49()
    OP_D7(0x1E)
    Sleep(1000)
    LoadChrToIndex("chr/ch15000.itc", 0x1E)
    LoadChrToIndex("chr/ch15300.itc", 0x1F)
    LoadChrToIndex("chr/ch15400.itc", 0x20)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    SetChrPos(0x101, 100000, 0, 100300, 0)
    SetChrPos(0x104, 100000, 0, 101700, 180)
    SetChrPos(0x105, 109000, 0, 101000, 270)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_68(94020, 1500, 4870, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22000, 4000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(100000, 2200, 101000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    OP_68(100000, 1200, 101000, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0038
    ChrTalk(
        0x104,
        (
            "#00316F#11Pしっかし、ロイド……\x02\x03",

            "#00315F特務支援課に入ってから\x01",
            "最大のご褒美って感じだよな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00012F#6Pさ、さすがに大げさだろ。\x02\x03",

            "#00002F確かにみんな、\x01",
            "どんな格好をしてくるか\x01",
            "ちょっと楽しみだけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00309F#11Pそうだろ、そうだろ㈱\x02\x03",

            "#00301Fしかもイリアさんや\x01",
            "セシルさんの水着だぞ！？\x02\x03",

            "#00307F加えてリーシャちゃんみたいな\x01",
            "超有望株なんかもいるし！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00011F#6Pお、落ち着けって。\x02\x03",

            "#00006F……うーん、でも何気に\x01",
            "俺たちの周りって\x01",
            "スタイルのいい女性が多いよな。\x02\x03",

            "#00002Fセシル姉やリーシャもそうだけど\x01",
            "エリィもかなりグラマーだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00304F#11Pイリアさんはモデルみたいだし、\x01",
            "ノエルやフランちゃんも\x01",
            "出るトコ出てるしなぁ。\x02\x03",

            "#00302Fまあティオすけやシュリぞうは\x01",
            "これからに期待ってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00006F#6P失礼だぞ、ランディ。\x02\x03",

            "#00005Fあ……そういえば\x01",
            "キーアって泳げるのかな？\x02\x03",

            "#00001F聞いたことは無かったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00303F#11Pんー、大昔の事だし、\x01",
            "本人も覚えてねぇんだろう。\x02\x03",

            "#00300F一応、溺れないように\x01",
            "誰か見てた方がいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2434, 255, 80, 0)    #voice#Lazy
    Sleep(800)

    #C0046
    ChrTalk(
        0x105,
        "#1Pフフ、ホント親バカだねぇ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_187B():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_187B)
    Sleep(50)

    def lambda_188B():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_188B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetCameraDistance(19500, 3000)
    OP_68(102000, 1000, 101000, 3000)
    Sleep(500)
    OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(40, 120, -1, -1)

    #A0047
    AnonymousTalk(
        0x101,
        "#00005Fワジ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 140, -1, -1)

    #A0048
    AnonymousTalk(
        0x104,
        "#00305Fも、もう着替えたのかよ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 35, 3)

    #A0049
    AnonymousTalk(
        0x105,
        "ああ、外で待ってるよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Sound(2424, 255, 100, 0)    #voice#Lazy
    Sleep(500)
    MoveCamera(325, 18, 0, 4000)

    def lambda_19D9():

        label("loc_19D9")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_19D9")

    QueueWorkItem2(0x101, 2, lambda_19D9)

    def lambda_19EB():

        label("loc_19EB")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_19EB")

    QueueWorkItem2(0x104, 2, lambda_19EB)

    def lambda_19FD():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19FD)
    WaitChrThread(0x105, 1)

    def lambda_1A1B():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A1B)
    Sound(121, 0, 100, 0)
    Sleep(500)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x105, 1)
    Sound(890, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Fade(500)
    OP_68(100410, 1000, 101610, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16640, 0)
    OP_68(100240, 1000, 101490, 0)
    MoveCamera(311, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    OP_0D()

    #C0050
    ChrTalk(
        0x104,
        "#00301F#5P──怪しい。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    #C0051
    ChrTalk(
        0x101,
        (
            "#00005F#6P怪しいって……ワジが？\x02\x03",

            "#00012Fそりゃいつも基本的に\x01",
            "怪しいヤツだとは思うけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0052
    ChrTalk(
        0x104,
        (
            "#00306F#11Pいや、そうじゃねぇ。\x02\x03",

            "#00303F俺たちが喋っている間に\x01",
            "素早く着替える手際のよさ。\x02\x03",

            "そして男女兼用にもなる\x01",
            "セパレートタイプの水着……\x02\x03",

            "#00301F……怪しくないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00011F#6Pどこが怪しいんだか\x01",
            "サッパリ判らないんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00306F#11Pったく、朴念仁#6Rボクネンジン#め。\x02\x03",

            "#00300F……ま、いいか。\x01",
            "俺たちも早く着替えようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F#6Pだな、待たせても悪いし。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(94150, 1200, 1070, 0)
    MoveCamera(316, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    SetChrPos(0x101, 94020, 0, 5870, 180)
    SetChrPos(0x104, 94020, 0, 5870, 180)
    SetChrPos(0x105, 94020, 0, 370, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x8)
    Sleep(300)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_79(0x0)
    OP_68(94380, 1200, 1630, 3500)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(1500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x8)
    Sleep(300)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sound(2088, 255, 100, 0)    #voice#Lloyd
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0056
    AnonymousTalk(
        0x101,
        "ワジ、お待たせ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sound(2364, 255, 100, 0)    #voice#Randy
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0057
    AnonymousTalk(
        0x104,
        "おし、そんじゃあ行くか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0058
    ChrTalk(
        0x105,
        "#12905F#6P……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        "#12505F#5Pえ、なんだ？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#12805F#11Pなんか変なとこでもあるか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2429, 255, 100, 0)    #voice#Lazy
    Sleep(600)

    #C0061
    ChrTalk(
        0x105,
        (
            "#12904F#6Pいや、男の水着姿ってのは\x01",
            "さして面白くないと思ってね。\x02\x03",

            "#12902Fまあ２人とも、体格はいいから\x01",
            "ガッカリはされないと思うよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x101,
        "#12513F#5Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        "#12801F#11P余計なお世話だっつーの。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#12909F#6Pフフ、それじゃあ\x01",
            "ビーチに出るとしようか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipPat(0x0, 0x1, 0x60)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x61)
    LoadChrChipPat()
    SetChrChipPat(0x4, 0x1, 0x62)
    LoadChrChipPat()
    OP_C7(0x1, 0x17)
    SetChrPos(0x0, 94020, 0, 1060, 90)
    SetScenarioFlags(0x144, 7)
    OP_29(0xA5, 0x1, 0x2)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_1009 end

    def Function_14_218A(): pass

    label("Function_14_218A")


    def lambda_218F():
        OP_9B(0x1, 0xFE, 0xA, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_218F)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_218A end

    def Function_15_21AF(): pass

    label("Function_15_21AF")


    def lambda_21B4():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21B4)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_21AF end

    def Function_16_21D4(): pass

    label("Function_16_21D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03000.itc", 0x1E)
    LoadChrToIndex("apl/ch51322.itc", 0x1F)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, 100000, 0, 100300, 0)
    SetChrPos(0x104, 100000, 0, 101700, 180)
    SetChrPos(0x105, 109000, 0, 101000, 270)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    OP_68(100000, 2200, 101000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    FadeToBright(1000, 0)
    OP_68(100000, 1200, 101000, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0065
    ChrTalk(
        0x104,
        (
            "#12809F#11Pいや～、疲れたけど\x01",
            "存分に堪能#4Rたんのう#させてもらったぜ。\x02\x03",

            "#12801Fうーん、欲を言えば\x01",
            "セシルさんやリーシャちゃんにも\x01",
            "ビーチバレーに参加して欲しかったが！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#12505F#6Pへ、なんで……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1300)
    OP_64(0x101)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0067
    ChrTalk(
        0x101,
        "#12513F#6Pこ、こらランディ！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#12802F#11Pんー、ロイドきゅんは\x01",
            "何を想像したのかなぁ～？\x02\x03",

            "#12806Fったく、お前ときたら\x01",
            "ちゃっかりお嬢やセシルさんたちの\x01",
            "日焼け止めなんか塗ってるしよ～。\x02\x03",

            "#12801Fオラオラ、どんなだった？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#12512F#6Pい、いや～……\x02\x03",

            "なんか凄かったとしか\x01",
            "言いようがないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#12807F#11Pんだと～！？\x02\x03",

            "#12810Fこの～、一人だけ\x01",
            "美味しい目に遭いやがって！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x0, 0x104, 0x0, 0x3E8, 0xBB8, 0x0)
    Fade(350)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    OP_A1(0x101, 0x3E8, 0x2, 0x0, 0x1)
    OP_63(0x101, 0x96, 1400, 0x28, 0x2B, 0x64, 0x0)
    Sound(908, 0, 70, 0)
    OP_A1(0x101, 0x1F4, 0x6, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3)
    OP_64(0x101)
    OP_0D()

    #C0071
    ChrTalk(
        0x101,
        "#12511F#6Pうわっ、ギブギブ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 100000, 0, 100300, 90)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 100000, 0, 101000, 180)

    def lambda_25E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25E6)
    OP_9B(0x1, 0x104, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()

    #C0072
    ChrTalk(
        0x104,
        (
            "#12803F#11P──で、ロイド？\x02\x03",

            "#12802F誰の水着姿に\x01",
            "一番グッときたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(4131, 255, 100, 0)    #voice#Lloyd

    #C0073
    ChrTalk(
        0x101,
        (
            "#12511F#6Pええっ！？\x02\x03",

            "#12508F（うーん……\x01",
            "  誰かって言われても……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K誰の水着姿が一番だった？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "エリィ\x01",        # 0
            "ティオ\x01",        # 1
            "ノエル\x01",        # 2
            "フラン\x01",        # 3
            "キーア\x01",        # 4
            "セシル\x01",        # 5
            "イリア\x01",        # 6
            "リーシャ\x01",      # 7
            "シュリ\x01",        # 8
            "ランディ\x01",      # 9
            "ワジ\x01",          # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27BB"),
        (1, "loc_290E"),
        (2, "loc_2A4C"),
        (3, "loc_2BA3"),
        (4, "loc_2CEA"),
        (5, "loc_2E6D"),
        (6, "loc_2FB4"),
        (7, "loc_30FE"),
        (8, "loc_324C"),
        (9, "loc_3418"),
        (10, "loc_355A"),
        (SWITCH_DEFAULT, "loc_36A6"),
    )


    label("loc_27BB")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12600.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0075
    AnonymousTalk(
        0x101,
        (
            "#3C（うーん、スタイルがいいとは\x01",
            "  前から思ってたけど……）\x02\x03",

            "（困ったな……\x01",
            "  これから仕事で一緒の時に\x01",
            "  意識しないといいんだけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_290E")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12700.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0076
    AnonymousTalk(
        0x101,
        (
            "#3C（控えめな水着だったけど\x01",
            "  可憐な感じだったよな……）\x02\x03",

            "（黒のワンピが色白の肌に\x01",
            "  映えていたっていうか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_2A4C")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13001.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0077
    AnonymousTalk(
        0x101,
        (
            "#3C（ノエルはイメージ通り\x01",
            "  スポーティな感じだったな。）\x02\x03",

            "（それでいて何ていうか\x01",
            "  普段は抑えられていた魅力が\x01",
            "  弾けてるっていうか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_2BA3")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13100.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0078
    AnonymousTalk(
        0x101,
        (
            "#3C（うーん、やっぱり\x01",
            "  可愛らしい水着姿っていったら\x01",
            "  フランかな？）\x02\x03",

            "（ピンクの水玉……\x01",
            "  彼女の雰囲気に合ってたな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_2CEA")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13200.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0079
    AnonymousTalk(
        0x101,
        (
            "#3C（うんうん、やっぱり\x01",
            "  キーアの水着姿が一番だよな。）\x02\x03",

            "（あの水着、エリィやティオが\x01",
            "  見つくろってあげたのかな？）\x02\x03",

            "（動きやすくてシンプルだけど\x01",
            "  どこか洒落てるっていうか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_2E6D")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13300.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0080
    AnonymousTalk(
        0x101,
        (
            "#3C（セシル姉……\x01",
            "  あれはちょっと反則だろ……）\x02\x03",

            "（今まであんまり\x01",
            "  セシル姉のスタイルとか\x01",
            "  意識してなかったけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_2FB4")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13400.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0081
    AnonymousTalk(
        0x101,
        (
            "#3C（イリアさん……\x01",
            "  やっぱりスターって感じだよな。）\x02\x03",

            "（どんな時でもキラキラ輝いて……\x01",
            "  みんなが憧れるのも納得だよな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_30FE")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13500.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0082
    AnonymousTalk(
        0x101,
        (
            "#3C（うーん、リーシャの背丈で\x01",
            "  あのスタイルは反則だよな……）\x02\x03",

            "（考えてみればあれに近い露出度で\x01",
            "  舞台衣装を着てるわけで……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_324C")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13600.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_335B")

    #A0083
    AnonymousTalk(
        0x101,
        (
            "#3C（はは、男の子っぽいけど\x01",
            "  やっぱり女の子なんだよな。）\x02\x03",

            "（初体面の時、とんでもない形で\x01",
            "  間違えてしまったけど……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D0")

    label("loc_335B")


    #A0084
    AnonymousTalk(
        0x101,
        (
            "#3C（はは、男の子っぽいけど\x01",
            "  やっぱり女の子なんだよな。）\x02\x03",

            "（初めて紹介された時、\x01",
            "  間違えそうになったけど。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D0")

    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_3418")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0085
    AnonymousTalk(
        0x101,
        (
            "#3C（しかしランディ……\x01",
            "  やっぱりガタイがいいよな。）\x02\x03",

            "（よく見ると古傷が多いけど……\x01",
            "  猟兵時代に付いたのかな？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_355A")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0086
    AnonymousTalk(
        0x101,
        (
            "#3C（ワジか……言われてみれば\x01",
            "  何となく気になる水着だよな。）\x02\x03",

            "（男女兼用のセパレート……\x01",
            "  単なる趣味だとは思うんだけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_36A6")

    label("loc_36A6")

    Sleep(300)

    #C0087
    ChrTalk(
        0x105,
        (
            "#1Pやれやれ、男２人して\x01",
            "なにジャレあってるんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#12511F#6Pっ！\x02",
    )

    CloseMessageWindow()

    def lambda_36FA():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_36FA)
    Sleep(50)

    def lambda_370A():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_370A)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetCameraDistance(19500, 3000)
    OP_68(102000, 1000, 101000, 3000)
    Sleep(500)
    OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x101,
        "#12505F#5Pワジ……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        (
            "#12805F#5Pおいおい。\x01",
            "もう着替えたのかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        (
            "#10306F#12Pま、若いんだから\x01",
            "妄想を膨らませるのは\x01",
            "仕方ないと思うけど。\x02\x03",

            "#10302Fもうちょっと余裕があった方が\x01",
            "女の子のウケはいいんじゃない？\x02\x03",

            "#10309Fその上で、相手に興味があると\x01",
            "思わせられればバッチリかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#12511F#5Pい、いや！\x01",
            "そんな話をしてたんじゃ！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#12801F#5Pおおむね同意だが……\x01",
            "随分、上から目線じゃねーか。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        "#10302F#12Pうん、だって僕モテるし。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x105,
        (
            "#10304F#12Pフフ、一足先に\x01",
            "ホテルの部屋に戻ってるよ。\x02\x03",

            "#10300Fテーマパークに行く前に\x01",
            "一休みしておきたいからね。\x02\x03",

            "#10302Fアデュー#8Rそ れ じ ゃ あ#。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xB4, 0x1F4)
    MoveCamera(325, 18, 0, 4000)

    def lambda_39E3():

        label("loc_39E3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_39E3")

    QueueWorkItem2(0x101, 2, lambda_39E3)

    def lambda_39F5():

        label("loc_39F5")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_39F5")

    QueueWorkItem2(0x104, 2, lambda_39F5)

    def lambda_3A07():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A07)
    WaitChrThread(0x105, 1)

    def lambda_3A25():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3A25)
    Sound(121, 0, 100, 0)
    Sleep(500)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x105, 1)
    Sound(890, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(100410, 1000, 101610, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16640, 0)
    OP_68(100240, 1000, 101490, 0)
    MoveCamera(311, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    OP_0D()

    #C0096
    ChrTalk(
        0x104,
        (
            "#12807F#11Pおおっ、納得いかねー！\x02\x03",

            "#12806F着替えも確認し損ねたし\x01",
            "なんだよこの敗北感は！？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#12506F#5Pまあ、相手が悪いかもな。\x02\x03",

            "#12500Fいまだに気が向いたら\x01",
            "夜、ホストのバイトをしに\x01",
            "外出してるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#12801F#11Pなんて羨ましい──\x01",
            "じゃなくてケシカラン！\x02\x03",

            "#12803Fこりゃ一度、尾行でもして\x01",
            "素行をチェックしないとな！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#12512F#5P（全然説得力がないなぁ……）\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17720, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "ホテルに戻って一休みした後……\x02\x03",

            "それぞれショッピングなどを楽しんでから\x01",
            "テーマパーク前に集合することにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrChipPat(0x0, 0x1, 0x0)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()
    SetChrChipPat(0x4, 0x1, 0x4)
    LoadChrChipPat()
    OP_C7(0x1, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_21D4 end

    def Function_17_3D69(): pass

    label("Function_17_3D69")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-5720, 1600, 1240, 0)
    MoveCamera(312, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25730, 0)
    SetChrPos(0x101, -12960, 0, 640, 90)
    SetChrPos(0x153, -12960, 0, 1770, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 98840, 0, 1140, 270)
    OP_68(-9290, 1100, 1300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x2, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)

    def lambda_3E3E():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E3E)
    Sleep(500)

    def lambda_3E5B():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3E5B)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x2, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    Sleep(500)
    TurnDirection(0x153, 0x101, 500)
    Sleep(100)

    #C0101
    ChrTalk(
        0x153,
        (
            "#11P#01105Fロイド、テーマパークには\x01",
            "行かないのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#00000Fいや、そういう訳じゃないけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)

    #C0103
    ChrTalk(
        0x101,
        "#6P#00005Fなんだか閑散としてるな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#00003F受付の人もいないし……\x01",
            "一体どこに行ったんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6090, 1600, 50, 4000)
    OP_6F(0x1)
    Sleep(100)

    #N0105
    NpcTalk(
        0xE,
        "女性の声",
        "#4P#N#2S……どういうことなの……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0106
    NpcTalk(
        0x8,
        "女性の声",
        "#4P#N#2S……も、申し訳ありません……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x153, 0x5A, 0x0)
    Fade(500)
    OP_68(-9290, 1100, 1300, 0)
    MoveCamera(312, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25730, 0)
    OP_0D()

    #C0107
    ChrTalk(
        0x153,
        "#11P#01105F声が聞こえてくるよー？\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、なんだか\x01",
            "揉めてるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x15B, 4)
    SetChrPos(0x0, -9420, 0, 610, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_3D69 end

    def Function_18_40D1(): pass

    label("Function_18_40D1")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch48200.itc", 0x1F)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x8, 96490, 0, 1360, 90)
    SetChrPos(0xC, 96150, 0, 60, 90)
    SetChrPos(0xD, 99300, 0, -400, 315)
    SetChrPos(0xE, 98840, 0, 1140, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C6")
    OP_68(96990, 1600, 210, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    SetChrPos(0x101, 90240, 0, 570, 90)
    SetChrPos(0x153, 90020, 0, 1390, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0xE,
        (
            "せっかく来たビーチで\x01",
            "こんな目にあうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xE,
        (
            "一体このビーチの管理は\x01",
            "どうなってるのよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        "本当に申し訳ありません……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xC,
        (
            "#6P俺も監視が行き届いて\x01",
            "いませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xD,
        (
            "ま、まあまあ。\x01",
            "謝ってくれてるんだし\x01",
            "いいじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "怪我をしたってワケでも\x01",
            "ないんだしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xE,
        (
            "いーや、そんなんじゃ\x01",
            "気が治まらないっ！\x02",
        )
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0x101,
        "ロイドの声",
        "あの、どうかしましたか？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(96820, 1700, -360, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    TurnDirection(0xD, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)

    def lambda_43D3():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43D3)
    Sleep(200)

    def lambda_43F0():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_43F0)
    Sleep(500)
    WaitChrThread(0x153, 1)

    #C0117
    ChrTalk(
        0x153,
        "#5P#01100Fケンカしちゃってるのー？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "#12Pあんたらはビーチに来てた、\x01",
            "マリアベルさんの招待客っていう……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "ああ、すみません！\x01",
            "受付を開け放してしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#5P#00000Fいえ、それはいいんですけど……\x01",
            "何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        "どうもこうもないわよ！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xE,
        (
            "さっきビーチで泳いでたら、\x01",
            "私の水着が何者かに切られちゃったの！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        "#5P#00005Fみ、水着を……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "実は、ビーチの開設以来\x01",
            "女性の水着が切り裂かれる案件が\x01",
            "２、３度起こっていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "今朝、貸切の時間帯では\x01",
            "出没しなかったようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xD,
        (
            "#12P俺たちも噂くらいは聞いてたけど、\x01",
            "当事者になるとはね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(100)
    TurnDirection(0xE, 0xD, 500)
    Sleep(1000)

    #C0127
    ChrTalk(
        0xE,
        (
            "彼女が水着を切られて、\x01",
            "公衆の面前で恥ずかしい思いを\x01",
            "させられたのよっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xE,
        (
            "あんたも文句の一つでも\x01",
            "言ってやりなさいよ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    #C0129
    ChrTalk(
        0xD,
        "#6Pそ、そんな事言ったってさ～……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    Sleep(500)

    #C0130
    ChrTalk(
        0xE,
        (
            "とにかく……\x01",
            "あなた達ミシュラム側で\x01",
            "犯人をフン捕まえなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xE,
        (
            "じゃないと、責任問題で\x01",
            "訴えてやるんだから！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47C4():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_47C4)
    Sleep(100)

    def lambda_47D4():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_47D4)
    Sleep(1000)

    #C0132
    ChrTalk(
        0x8,
        "#5Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "#5P正直、難しそうですね……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        (
            "#5P今までは犯人の姿すら\x01",
            "確認されていませんし。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x153,
        (
            "#5P#01111F（ほえ～……\x01",
            "  なんだか大変そうだねー。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0136
    ChrTalk(
        0x153,
        "#11P#01100F（ロイドー、手伝ってあげないの？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A35")

    label("loc_48C6")

    OP_68(96820, 1700, -360, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 91240, 0, 570, 90)
    SetChrPos(0x153, 91020, 0, 1390, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0137
    ChrTalk(
        0xE,
        (
            "早くあたしの水着を切り裂いた\x01",
            "犯人をフン捕まえなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xE,
        (
            "じゃないと、責任問題で\x01",
            "訴えてやるんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        "#5Pそ、それは……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        "#5P正直、難しそうですね……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        (
            "#5P今までは犯人の姿すら\x01",
            "確認されていませんし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0142
    ChrTalk(
        0x153,
        "#11P#01100F（ロイドー、手伝ってあげないの？）\x02",
    )

    CloseMessageWindow()

    label("loc_4A35")

    Call(0, 19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7230, 0, 790, 270)
    EventEnd(0x5)
    Return()

    # Function_18_40D1 end

    def Function_19_4A5B(): pass

    label("Function_19_4A5B")


    #C0143
    ChrTalk(
        0x101,
        (
            "#5P#00003F（どうする……？\x01",
            "  テーマパークに向かってる\x01",
            "  途中だったけど……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【犯人探しを手伝う】\x01",      # 0
            "【やめておく】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B22")
    Call(0, 20)
    Jump("loc_4BBD")

    label("loc_4B22")


    #C0144
    ChrTalk(
        0x101,
        (
            "#5P#00003F（テーマパークで\x01",
            "  待ち合わせをしているし……\x01",
            "  俺たちの出る幕じゃないだろう。）\x02\x03",

            "#00000F（ここはミシュラム事業部に\x01",
            "  任せるとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15B, 5)

    label("loc_4BBD")

    Return()

    # Function_19_4A5B end

    def Function_20_4BBE(): pass

    label("Function_20_4BBE")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x101,
        (
            "#5P#00000F……皆さん、できれば事件について\x01",
            "もう詳しく聞かせて頂けますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4C8A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4C8A)
    Sleep(100)

    def lambda_4C9A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4C9A)
    Sleep(100)

    def lambda_4CAA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4CAA)
    Sleep(500)

    #C0146
    ChrTalk(
        0x101,
        (
            "#5P#00004F警察の人間として、\x01",
            "こんな卑劣な犯罪を\x01",
            "見過ごすわけにはいきません。\x02\x03",

            "#00000F犯人像の特定くらいは\x01",
            "できるかもしれませんし、\x01",
            "協力させてもらえませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "まあ……\x01",
            "是非よろしくおねがいします！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    #C0148
    ChrTalk(
        0xD,
        (
            "#12Pはは、犯人を捜してくれるってさ。\x01",
            "よかったじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xE,
        "ふん、せいぜいよろしく頼むわね。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        (
            "#12Pそれなら、廊下で喋るのもなんだし\x01",
            "一旦更衣室に場所を移そうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#5P#00000Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x153,
        "#11P#01109Fがんばろーね、ロイド！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【水着切り裂き事件の捜査】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7E, 0x4, 0x2)
    OP_29(0x7E, 0x1, 0x0)
    OP_68(3220, 1500, 100150, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16620, 0)
    SetChrPos(0x101, 3570, 0, 99420, 0)
    SetChrPos(0x153, 4410, 0, 100170, 315)
    SetChrPos(0x8, 1210, 0, 101710, 135)
    SetChrPos(0xC, 840, 0, 100620, 135)
    SetChrPos(0xD, 2970, 0, 102410, 180)
    SetChrPos(0xE, 3930, 0, 102440, 180)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0154
    ChrTalk(
        0x101,
        (
            "#6P#00001Fそれではまず、事件発生時の\x01",
            "状況を教えてもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xE,
        "ええ、いいわ。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        (
            "……私は彼氏と一緒に、\x01",
            "ビーチで水遊びをしていたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xE,
        (
            "ビーチボールをトスし合ったり、\x01",
            "泳ぎの練習をしたりね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "その後しばらくして、\x01",
            "僕が売店に飲み物を\x01",
            "買いに行く事になったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        (
            "それで、しばらく目を離してたら、\x01",
            "彼女の悲鳴が聞こえてきて……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "戻ってみたら、\x01",
            "彼女が水着を切られて\x01",
            "湖に屈みこんでいたってわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "周りの人は集まってくるし、\x01",
            "もう、サイテーだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xE,
        (
            "そこの監視員さんが急いで\x01",
            "タオルを持ってきてくれたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        "#6P#00003Fなるほど……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(500)

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00001F監視員さんは、何かを\x01",
            "目撃してはいなかったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "俺は湖一帯を監視してたが、\x01",
            "気になるものは見なかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "悲鳴を聞いて駆けつけるまで\x01",
            "水着が切られたってことにも\x01",
            "気づかなかったくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "騒ぎになってから\x01",
            "周りの観光客に聞いてみたが、\x01",
            "犯人を見た者もいなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xE,
        (
            "被害者であるあたしも\x01",
            "犯人を見ちゃいないわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    #C0169
    ChrTalk(
        0xE,
        (
            "彼氏が買い出しに行ってから\x01",
            "何気なく辺りを見回したけど、\x01",
            "誰も近づいていなかったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xE,
        (
            "切られた瞬間は驚いて、\x01",
            "慌てて屈みこんじゃったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#6P#00006Fそれは、その……\x01",
            "仕方ないですよね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0172
    ChrTalk(
        0x101,
        (
            "#6P#00001F今までの切り裂き事件でも\x01",
            "目撃者はいないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "ええ、いずれも今回のように\x01",
            "浜辺で起きていたんですが、\x01",
            "誰も犯人を見ていないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "ただ、水着はいつも\x01",
            "刃物のようなもので切られていて、\x01",
            "事故とも考えにくくて……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "それに、同じような手口で\x01",
            "何度も事件が起こっている以上\x01",
            "同一犯と考えるのが自然なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "客の名簿を見ても、事件のときに\x01",
            "共通して来ている人物はいなくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "事故だったんだろうと\x01",
            "忘れかけられてたときに、\x01",
            "また起こっちまったってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#12P#00003Fなるほど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0179
    ChrTalk(
        0x153,
        "#12P#01111Fロイドー、犯人は分かりそう？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    #C0180
    ChrTalk(
        0xD,
        (
            "おいおい、お嬢ちゃん。\x01",
            "急かしてやっちゃダメだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xD,
        (
            "いくら警察と言っても、\x01",
            "話を聞いたくらいで\x01",
            "そこまで分かるわけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00003F……いえ、犯人像には\x01",
            "目星がつきました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)
    Sleep(500)

    #C0183
    ChrTalk(
        0xD,
        "マ、マジで！？\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "現場検証などはなさらなくても\x01",
            "よろしいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#12P#00003Fもちろん本来なら必要ですが……\x01",
            "多分、大した証拠は出ないと思います。\x02\x03",

            "#00001F現場が浜辺である以上、\x01",
            "発生から時間が経った今では\x01",
            "波に消された可能性が高いはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        "な、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "だが、それを踏まえた上でも\x01",
            "犯人が分かるってんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#6P#00000Fええ、今までの皆さんの話を\x01",
            "組み合わせて考えれば、\x01",
            "自ずと犯人像が見えてきます。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0x153,
        "#12P#01109Fロイド、かっこいー！\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0190
    ChrTalk(
        0xE,
        (
            "もったいぶってないで、\x01",
            "答えてもらおうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xE,
        (
            "あたしの水着を\x01",
            "切り裂いた犯人は……\x01",
            "一体誰だっていうの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    #C0192
    ChrTalk(
        0x101,
        (
            "#6P#00001F（目撃者がいないことと、\x01",
            "  今までの犯行が水辺で\x01",
            "  行われていること……）\x02\x03",

            "（そして、水着が\x01",
            "  刃物のような物で\x01",
            "  切り裂かれていること。）\x02\x03",

            "#00003F（これらから考えれば、\x01",
            "  恐らく犯人は……）\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D48")
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K水着切り裂き事件の犯人は？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "被害者自身\x01",        # 0
            "被害者の彼氏\x01",      # 1
            "監視員\x01",            # 2
            "全く別の誰か\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C1A")

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#00003F状況から考えて、\x01",
            "犯人はここにいる人や\x01",
            "他の観光客ではありえません。\x02\x03",

            "#00001Fおそらく今回の犯人は、\x01",
            "ビーチに潜んでいる……\x01",
            "何らかの“魔獣”だと思われます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C15")
    OP_2C(0x7E, 0x1)

    label("loc_5C15")

    Jump("loc_5D43")

    label("loc_5C1A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#00003F（いや、状況的にその人が\x01",
            "  犯人ではありえない。\x01",
            "  ……考え直してみよう。）\x02\x03",

            "#00001F（目撃者がいないことと、\x01",
            "  今までの犯行が水辺で\x01",
            "  行われていること……）\x02\x03",

            "（そして、水着が\x01",
            "  刃物のような物で\x01",
            "  切り裂かれていること。）\x02\x03",

            "#00003F（これらから考えれば、\x01",
            "  恐らく犯人は……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D43")

    Jump("loc_5AC2")

    label("loc_5D48")

    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0196
    ChrTalk(
        0xD,
        "ま、魔獣……！？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        (
            "魔獣が彼女の水着を\x01",
            "切り裂いたっていうのかい！？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xE,
        (
            "い、いくらなんでも\x01",
            "突飛すぎる話じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        "根拠はあるの、根拠は！！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0200
    ChrTalk(
        0x101,
        (
            "#12P#00000F順番にお話しましょう。\x02\x03",

            "#00003Fまずは切り裂かれた\x01",
            "水着についてですが……\x02\x03",

            "#00001Fこれは、刃物のようなもので\x01",
            "切られていたそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "え、ええ……\x01",
            "今までの事件でも同様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#12P#00000Fでは、お聞きしますが……\x01",
            "このビーチにそのような物を\x01",
            "“持ち込む”事は可能ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "い、いえ……\x01",
            "それは難しいはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "受付でも呼びかけて、\x01",
            "厳重にチェックしていますし……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        (
            "ああ、俺たち職員も保安上、\x01",
            "小型の簡易的な金属探知機を\x01",
            "持ち歩いているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xC,
        (
            "だからこそ、そんな物を\x01",
            "どうやって持ち込んだか\x01",
            "全く分からなくて…………\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        "…………あ。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#6P#00000F……そう、つまり……\x01",
            "犯人は“刃物を持ちこんだ”\x01",
            "わけではないんです。\x02\x03",

            "#00003Fおそらく、犯人自身の体に\x01",
            "水着を切り裂くための武器を\x01",
            "“あらかじめ備えていた”……\x02\x03",

            "#00001F恐らく……\x01",
            "鋭い爪や歯のようなものを。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xD,
        (
            "そ、それが犯人を魔獣とする\x01",
            "根拠ってわけか……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#6P#00003Fいえ、これだけなら\x01",
            "単に奇天烈な発想というだけです。\x02\x03",

            "#00000Fただ、他の要素と組み合わせた場合……\x01",
            "それは徐々に真実味を増すはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xE,
        "他の要素……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        (
            "#6P#00001Fそもそも今回の事件は、\x01",
            "今まで起きている切り裂き事件と\x01",
            "共通点が多いそうですね。\x02\x03",

            "#00003F目撃者がいないこと……\x01",
            "犯行が水辺で行われていること……\x01",
            "手口が全く同じな事……\x02\x03",

            "#00001Fそのことから考えても、\x01",
            "犯人は同一犯の可能性が高い。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "ええ、にもかかわらず\x01",
            "お客様の名簿には事件時に\x01",
            "一貫して来られている方は……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそう、つまり……\x01",
            "正規の手段で入ってきた\x01",
            "客の中には、犯人はいないんです。\x02\x03",

            "#00000Fそして、監視員がいる以上は\x01",
            "湖を経由して進入することもできない……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "まあ、流石にそんなヤツが\x01",
            "紛れ込んだら気づくと思うが……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#6P#00001Fそう考えれば……\x01",
            "犯人が現場に現れるルートは\x01",
            "一つしかありません。\x02\x03",

            "エルム湖の沖……\x01",
            "そのあたりに棲み処を持つ\x01",
            "水棲魔獣ならば可能でしょう。\x02\x03",

            "#00003Fそして、小型の水棲魔獣なら\x01",
            "水中を泳ぐことで監視員に気づかれずに\x01",
            "ビーチの人間に近づけるはずです。\x02\x03",

            "#00001F逆に言えば……\x01",
            "それ以外の方法で今回の事件を\x01",
            "起こす事はできません。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xD,
        (
            "つ、つまり今回の事件は、\x01",
            "魔獣にしか起こせなかった……\x01",
            "そういうことかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        "筋は通っているみたいですね……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    Sleep(500)

    #C0219
    ChrTalk(
        0xE,
        (
            "ちょ、ちょっと待ってよ。\x01",
            "大事なことを忘れてない？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xE,
        (
            "なんで魔獣なんかが、\x01",
            "女の子の水着を切り裂く\x01",
            "必要があるわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "た、確かにそれもある……\x01",
            "あんた、どうなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        (
            "やっぱり……\x01",
            "どっかのヘンタイ男の\x01",
            "仕業なんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0223
    ChrTalk(
        0x101,
        (
            "#12P#00006Fさ、さすがに動機は\x01",
            "分かりませんが……\x02\x03",

            "#00001F今回の事件が魔獣にしか\x01",
            "起こせないという\x01",
            "事実は変わりません。\x02\x03",

            "#00003Fとなると、現時点では\x01",
            "『そういう習性を持つ魔獣』、\x01",
            "というしかないですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "でも……\x01",
            "そうするとどうしましょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "魔獣が出没するとなると、\x01",
            "ミシュラム事業部の信用にも\x01",
            "つながってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "なんとかこの機会に\x01",
            "退治できるといいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        "だが、相手は神出鬼没だ。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "現れるまで待っていたら、\x01",
            "とてもビーチなんかは\x01",
            "運営できないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xE,
        (
            "うーん、あたしも被害にあったし\x01",
            "また安心して来れるかというと\x01",
            "さすがにイヤね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)
    Sleep(500)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0230
    ChrTalk(
        0x153,
        (
            "#12P#01100Fだったら……\x01",
            "キーアがオトリになろっかー？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_6AB5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AB5)
    Sleep(100)

    def lambda_6AC5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6AC5)
    Sleep(100)

    def lambda_6AD5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6AD5)
    Sleep(100)

    def lambda_6AE5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6AE5)
    Sleep(100)

    def lambda_6AF5():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6AF5)
    Sleep(500)

    #C0231
    ChrTalk(
        0x101,
        "#6P#00011Fキ、キーア、何を言ってるんだ！？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x153,
        (
            "#12P#01105Fだって、その魔獣って\x01",
            "女の子の水着を切りたいんだよねー？\x02\x03",

            "#01103Fキーアが水辺で遊んでたら、\x01",
            "また出てきてくれるかもしれないし。\x02\x03",

            "#01109Fその時は、ロイドが守ってくれれば\x01",
            "キーアも大丈夫だしー。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#00001Fあ、あのな……\x01",
            "キーアをそんな危ない目に\x01",
            "遭わせられるわけないだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xD,
        "そ、そうだよお嬢ちゃん。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xD,
        (
            "今まで水着だけが切られてるけど、\x01",
            "次はどうなるか分からないんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x153,
        (
            "#12P#01108Fんー、でも……\x01",
            "このまま魔獣がいると\x01",
            "ベルが困っちゃうんだよねー？\x02\x03",

            "#01106F招待してくれたお礼に\x01",
            "なんとか退治してあげたいし……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        "#6P#00003Fそ、それはそうだけど……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0238
    ChrTalk(
        0x101,
        (
            "#6P#00003F……わかった。\x02\x03",

            "#00001Fキーアのその作戦、\x01",
            "成功するかは分からないけど\x01",
            "やれるだけやってみよう。\x02\x03",

            "#00003Fただし、囮役はキーアじゃなくて、\x01",
            "俺たちの中の他の誰かに頼むことにする。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x153,
        "#12P#01101Fうん！\x02",
    )

    CloseMessageWindow()

    def lambda_6E5B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6E5B)
    Sleep(100)

    def lambda_6E6B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6E6B)
    Sleep(100)

    def lambda_6E7B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6E7B)
    Sleep(100)

    def lambda_6E8B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6E8B)
    Sleep(500)

    #C0240
    ChrTalk(
        0x8,
        (
            "そんな……\x01",
            "大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#00000Fはい、支援課の仲間なら\x01",
            "魔獣との戦闘にも慣れてますし……\x01",
            "大事にはならないと思います。\x02\x03",

            "#00003F問題は、囮役を\x01",
            "誰にやってもらうかだけど……\x02\x03",

            "#00000F協力を頼めそうなのは、\x01",
            "エリィかティオ、ノエルか。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x153,
        "#12P#01105Fロイド、誰を呼ぶのー？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0243
    ChrTalk(
        0x101,
        "#6P#00003Fそうだな……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K誰に囮役を頼む？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【エリィ】\x01",      # 0
            "【ティオ】\x01",      # 1
            "【ノエル】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7075"),
        (1, "loc_70B0"),
        (2, "loc_70EB"),
        (SWITCH_DEFAULT, "loc_7126"),
    )


    label("loc_7075")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 6)

    #C0245
    ChrTalk(
        0x101,
        "#6P#00000F……エリィに頼んでみよう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7126")

    label("loc_70B0")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 7)

    #C0246
    ChrTalk(
        0x101,
        "#6P#00000F……ティオに頼んでみよう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7126")

    label("loc_70EB")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C4, 5)

    #C0247
    ChrTalk(
        0x101,
        "#6P#00000F……ノエルに頼んでみよう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7126")

    label("loc_7126")


    #C0248
    ChrTalk(
        0x153,
        "#12P#01109Fうん、だったら大丈夫そうだねー！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0249
    ChrTalk(
        0x101,
        (
            "#6P#00003Fというわけで……\x01",
            "今からビーチで魔獣退治を\x01",
            "始めたいと思います。\x02\x03",

            "#00000F職員の皆さん、\x01",
            "人払いをお願いできますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        "ええ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xC,
        (
            "点検時間ってことにして\x01",
            "観光客たちにはしばらく\x01",
            "避難していてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xD,
        "君達、気をつけてくれよ～！\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xE,
        (
            "あたしの水着を切り裂いた魔獣を\x01",
            "叩きのめしてやってちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    #C0254
    ChrTalk(
        0x101,
        "#6P#00000Fはい、任せて下さい！\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x153,
        "#12P#01109Fそれじゃ、れっつごー！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7328")
    AddParty(0x1, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x1)
    Jump("loc_734A")

    label("loc_7328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7340")
    AddParty(0x2, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x2)
    Jump("loc_734A")

    label("loc_7340")

    AddParty(0x8, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x3)

    label("loc_734A")

    SetScenarioFlags(0x22, 3)
    NewScene("t1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4BBE end

    def Function_21_7357(): pass

    label("Function_21_7357")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1330, 3100, 1380, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch48200.itc", 0x1F)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x101, -3160, 0, 1570, 45)
    SetChrPos(0x153, -2960, 0, -40, 45)
    SetChrPos(0xEF, -4480, 0, 1090, 45)
    SetChrPos(0xC, 490, 0, 1750, 270)
    SetChrPos(0xD, -570, 0, -680, 315)
    SetChrPos(0xE, -390, 0, 320, 315)
    SetChrPos(0x8, -2000, 0, 5150, 180)
    OP_68(-1330, 1600, 1380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0256
    ChrTalk(
        0x8,
        "皆さん、お疲れ様でした。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "おかげさまで、ミシュラム事業部の\x01",
            "信用を失わずにすみそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#00002Fはは、お役に立てて光栄です。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "本当にありがとうございました。\x01",
            "なんとお礼を言っていいか……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "それと、開発の関係で魔獣が\x01",
            "出ていた件については、\x01",
            "マリアベル様に報告しておきます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_75CC")

    #C0261
    ChrTalk(
        0x102,
        "#00100Fええ、そのほうがいいでしょうね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_762F")

    label("loc_75CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_75FD")

    #C0262
    ChrTalk(
        0x103,
        "#00200Fそれがいいでしょうね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_762F")

    label("loc_75FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_762F")

    #C0263
    ChrTalk(
        0x109,
        "#10100Fはい、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    label("loc_762F")


    #C0264
    ChrTalk(
        0x101,
        (
            "#00000Fはは、マリアベルさんなら\x01",
            "何かしらの対策を考えてくれそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    #C0265
    ChrTalk(
        0xE,
        "#12Pふふ、お疲れ様㈱\x02",
    )

    CloseMessageWindow()

    def lambda_76A2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76A2)
    Sleep(100)

    def lambda_76B2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_76B2)
    Sleep(100)

    def lambda_76C2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_76C2)
    Sleep(100)

    def lambda_76D2():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_76D2)
    Sleep(500)

    #C0266
    ChrTalk(
        0xE,
        (
            "#12Pとりあえず、水着切り裂き事件の\x01",
            "犯人だった魔獣は退治できたのよね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 500)
    Sleep(500)

    #C0267
    ChrTalk(
        0xE,
        (
            "#12Pよーし、そうときまれば\x01",
            "ビーチ遊びの続きに行きましょ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    #C0268
    ChrTalk(
        0xD,
        (
            "#6Pええっ、また行くつもりなの！？\x01",
            "懲りたかと思ってたのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xE,
        (
            "#12Pトーゼンでしょ！\x01",
            "せっかく来たんだから\x01",
            "遊ばなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    #C0270
    ChrTalk(
        0xE,
        (
            "#12Pふふ、それじゃあ\x01",
            "あたしたちはこれでね。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(2000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Sleep(500)

    #C0271
    ChrTalk(
        0xC,
        (
            "#12Pそんじゃあ俺も\x01",
            "監視の仕事に戻るとするよ。\x01",
            "あんたたち、ありがとうな。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0xC, 0xB4, 0x1388, 0x7D0, 0x0)
    Sleep(1000)
    OP_68(-3510, 1300, 960, 3000)
    OP_6F(0x1)
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0272
    ChrTalk(
        0x101,
        (
            "#00000Fよし、それじゃあ俺たちも\x01",
            "そろそろ行くとするか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0273
    ChrTalk(
        0x153,
        "#6P#01100Fうん！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7996")

    #C0274
    ChrTalk(
        0x102,
        (
            "#00104F私はもう少し\x01",
            "ブティックを見てからいくわ。\x02\x03",

            "#00100Fふふ、また後でね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A7C")

    label("loc_7996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7A18")

    #C0275
    ChrTalk(
        0x103,
        (
            "#00204Fわたしは一足先に\x01",
            "テーマパークへ行っています。\x02\x03",

            "#00202Fツァイトやシュリさんを\x01",
            "待たせているので、これで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A7C")

    label("loc_7A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7A7C")

    #C0276
    ChrTalk(
        0x109,
        (
            "#10100Fあたしはもう少しフランと\x01",
            "宝飾店を見て行きますね。\x02\x03",

            "#10109Fそれでは、また後で！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A7C")


    def lambda_7A81():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A81)
    Sleep(200)

    def lambda_7A91():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_7A91)
    Sleep(500)

    #C0277
    ChrTalk(
        0x101,
        "#00000Fああ、それじゃあな。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x153,
        "#12P#01109Fまたあとでー！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【水着切り裂き事件の捜査】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7E, 0x1, 0x4)
    OP_29(0x7E, 0x1, 0x5)
    OP_29(0x7E, 0x4, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_7B6A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_7B87")

    label("loc_7B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_7B7B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_7B87")

    label("loc_7B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_7B87")
    RemoveParty(0x8, 0xFF)

    label("loc_7B87")

    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("t1020", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_21_7357 end

    def Function_22_7B96(): pass

    label("Function_22_7B96")

    OP_95(0xE, 4990, 0, 50, 2000, 0x0)
    OP_95(0xE, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xE, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_22_7B96 end

    def Function_23_7BD3(): pass

    label("Function_23_7BD3")

    OP_95(0xD, 4990, 0, 50, 2000, 0x0)
    OP_95(0xD, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xD, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_23_7BD3 end

    def Function_24_7C10(): pass

    label("Function_24_7C10")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_7C10 end

    SaveToFile()

Try(main)
