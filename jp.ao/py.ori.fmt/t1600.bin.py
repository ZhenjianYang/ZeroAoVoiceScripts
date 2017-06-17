from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1600.bin",                # FileName
        "t1600",                    # MapName
        "t1600",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1600",                  # 0
        "バッジョ",               # 1
        "シズク",                 # 2
        "セイランド教授",         # 3
        "ダイソン用務員",         # 4
        "看護師シロン",           # 5
        "看護師メイファ",         # 6
        "アリオス",               # 7
        "セルゲイ",               # 8
        "ウルスラ間道",           # 9
    ))

    AddCharChip((
        "chr/ch20400.itc",                   # 00
        "chr/ch05400.itc",                   # 01
        "chr/ch44800.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch29900.itc",                   # 04
        "chr/ch29800.itc",                   # 05
        "chr/ch05300.itc",                   # 06
    ))

    DeclNpc(-21979,  6000,    18520,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(-3589,   7000,    11229,   225,  389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4039,    7000,    2160,    270,  389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(3430,    7000,    -9159,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   4,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-26559,  6000,    14199,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 29,  -13.5,                 20.0,                  5.5,                   4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   6.75,                  -10.0,                 -1.100000023841858,    1.0])

    DeclActor(17500,   7000,    -3000,   2000,    18000,   8000,    -3000,   0x007C, 0,  22, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(712, 0)                                        # 0

    ScpFunction((
        "Function_0_2C8",          # 00, 0
        "Function_1_380",          # 01, 1
        "Function_2_512",          # 02, 2
        "Function_3_5DE",          # 03, 3
        "Function_4_690",          # 04, 4
        "Function_5_9B9",          # 05, 5
        "Function_6_D2E",          # 06, 6
        "Function_7_10C6",         # 07, 7
        "Function_8_1741",         # 08, 8
        "Function_9_1925",         # 09, 9
        "Function_10_1A65",        # 0A, 10
        "Function_11_1D50",        # 0B, 11
        "Function_12_2430",        # 0C, 12
        "Function_13_2ED5",        # 0D, 13
        "Function_14_2EFB",        # 0E, 14
        "Function_15_2F21",        # 0F, 15
        "Function_16_2F47",        # 10, 16
        "Function_17_2F6D",        # 11, 17
        "Function_18_2F93",        # 12, 18
        "Function_19_2FB9",        # 13, 19
        "Function_20_2FDF",        # 14, 20
        "Function_21_3005",        # 15, 21
        "Function_22_302B",        # 16, 22
        "Function_23_318D",        # 17, 23
        "Function_24_3600",        # 18, 24
        "Function_25_364B",        # 19, 25
        "Function_26_3696",        # 1A, 26
        "Function_27_36E1",        # 1B, 27
        "Function_28_372C",        # 1C, 28
        "Function_29_3777",        # 1D, 29
    ))


    def Function_0_2C8(): pass

    label("Function_0_2C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_308"),
        (1, "loc_314"),
        (2, "loc_320"),
        (3, "loc_32C"),
        (4, "loc_338"),
        (5, "loc_344"),
        (6, "loc_350"),
        (SWITCH_DEFAULT, "loc_35C"),
    )


    label("loc_308")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_314")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_320")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_32C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_338")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_344")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_350")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_35C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_368")

    label("loc_37F")

    Return()

    # Function_0_2C8 end

    def Function_1_380(): pass

    label("Function_1_380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A4")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 8450, 7000, -13870, 135)
    Jump("loc_4EE")

    label("loc_3A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3C8")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 13730, 7000, -3100, 90)
    Jump("loc_4EE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_411")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -26060, 6000, 14200, 0)
    SetChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -27060, 6000, 14200, 0)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_424")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_441")
    SetChrFlags(0x9, 0x10)

    label("loc_441")

    Jump("loc_4EE")

    label("loc_446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_454")
    Jump("loc_4EE")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_46C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_4EE")

    label("loc_46C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_47F")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4CD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    SetChrPos(0xC, -22110, 6000, 16760, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -20450, 6000, 17030, 315)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4EE")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E0")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_4EE")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4EE")
    ClearChrFlags(0xB, 0x80)

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_502")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)
    Jump("loc_511")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_511")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_511")

    Return()

    # Function_1_380 end

    def Function_2_512(): pass

    label("Function_2_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_524")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A8")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_5BF")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_5BF")

    label("loc_5BF")

    ClearMapObjFlags(0x5, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DD")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5DD")

    Return()

    # Function_2_512 end

    def Function_3_5DE(): pass

    label("Function_3_5DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_68C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")
    Call(0, 8)
    Jump("loc_68C")

    label("loc_5FC")


    #C0001
    ChrTalk(
        0x8,
        (
            "看護師、いいかもな。\x01",
            "男の看護師もいないわけじゃ\x01",
            "ないだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ダメ元で姉ちゃんに\x01",
            "相談に来てみたけど、\x01",
            "なんだか道が開けた気分だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C")

    TalkEnd(0xFE)
    Return()

    # Function_3_5DE end

    def Function_4_690(): pass

    label("Function_4_690")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A5")
    Call(0, 11)
    Jump("loc_9B5")

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94D")
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0003
    ChrTalk(
        0x9,
        (
            "#11200Fそういえば、皆さん。\x02\x03",

            "キーアちゃんが３日前に\x01",
            "病院に来ていたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00005Fああ……そういえば\x01",
            "シズクちゃんのお見舞いに\x01",
            "行ってたんだったか。\x02\x03",

            "#00000Fえっと、キーアが\x01",
            "どうかしたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#11208Fいえ……なんだか少し、\x01",
            "様子が変だったような\x01",
            "気がするんです。\x02\x03",

            "#11203Fどこか思いつめてるというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#00205Fキーアが……？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#00303F俺たちの前では、\x01",
            "そんな素振りは見せて\x01",
            "なかったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#10108F……キーアちゃんも、\x01",
            "クロスベルの状況に不安を\x01",
            "感じてるのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00103Fそうね……\x01",
            "私たちには心配をかけないために\x01",
            "気持ちを隠しているのかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10302Fま、何にせよ気にかけて\x01",
            "あげたほうがよさそうだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 6)
    Jump("loc_9B5")

    label("loc_94D")


    #C0011
    ChrTalk(
        0x9,
        (
            "#11200Fみなさんも大変だと思いますけど、\x01",
            "どうか頑張ってください。\x02\x03",

            "私もここから応援してますから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B5")

    TalkEnd(0xFE)
    Return()

    # Function_4_690 end

    def Function_5_9B9(): pass

    label("Function_5_9B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9CA")
    Jump("loc_D2A")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE5")

    #C0012
    ChrTalk(
        0xA,
        (
            "内科系の医師と研修医が総出で、\x01",
            "薬品の種類が不足している問題の\x01",
            "対策を進めている。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "完全とはいかないだろうが、\x01",
            "どんな時でも最善を尽くすのが\x01",
            "医者としての義務だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xA,
        (
            "薬学・神経科教授としての\x01",
            "誇りと威信を賭けて、必ずや\x01",
            "何とかすることを女神に誓おう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B93")

    label("loc_AE5")


    #C0015
    ChrTalk(
        0xA,
        (
            "内科系の医師と研修医が総出で、\x01",
            "薬品の種類が不足している問題の\x01",
            "対策を進めている。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "薬学・神経科教授としての\x01",
            "誇りと威信を賭けて、必ずや\x01",
            "何とかすることを女神に誓おう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B93")

    Jump("loc_D2A")

    label("loc_B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_BA6")
    Jump("loc_D2A")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_BB4")
    Jump("loc_D2A")

    label("loc_BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C8F")

    #C0017
    ChrTalk(
        0xA,
        (
            "シズク……\x01",
            "彼女の視力が回復する\x01",
            "可能性は限りなく低いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "……だが、患者が諦めないかぎり、\x01",
            "私も絶対に諦めない。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xA,
        (
            "セイランドの名にかけて……\x01",
            "いつか必ず、この手で治してみせる。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D2A")

    label("loc_C8F")


    #C0020
    ChrTalk(
        0xA,
        (
            "シズクの視力回復手術が\x01",
            "成功すれば、同様の障害を持つ\x01",
            "患者たちの希望にもなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "セイランドの名にかけて……\x01",
            "いつか必ず、この手で治してみせる。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2A")

    TalkEnd(0xFE)
    Return()

    # Function_5_9B9 end

    def Function_6_D2E(): pass

    label("Function_6_D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DB1")

    #C0022
    ChrTalk(
        0xB,
        (
            "あの巨大な樹はすごいな……\x01",
            "こんな所からも見えるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xB,
        (
            "……一体クロスベルは\x01",
            "どうなってしまうんだろう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10C2")

    label("loc_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_DBF")
    Jump("loc_10C2")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC8")

    #C0024
    ChrTalk(
        0xB,
        (
            "最近の研究棟での講義では、\x01",
            "実験などが殆どできないらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "サンプルを街道で採取したり、\x01",
            "レミフェリアから仕入れたりが\x01",
            "できなくなってる影響なんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xB,
        (
            "このままだと、研修医たちの教育環境も\x01",
            "段々と悪くなってしまいそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_F56")

    label("loc_EC8")


    #C0027
    ChrTalk(
        0xB,
        (
            "最近の研究棟での講義では、\x01",
            "実験などが殆どできないらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "このままだと、研修医たちの教育環境も\x01",
            "段々と悪くなってしまいそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F56")

    Jump("loc_10C2")

    label("loc_F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_F69")
    Jump("loc_10C2")

    label("loc_F69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_10C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104C")

    #C0029
    ChrTalk(
        0xB,
        (
            "この辺りで仕事をしていると、\x01",
            "ランチタイムの研修医たちの\x01",
            "噂話が聞こえるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "最近は、もっぱら\x01",
            "セイランド教授の噂が多くてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xB,
        (
            "私にはあまり縁がないが……\x01",
            "実際はどんな人なんだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_10C2")

    label("loc_104C")


    #C0032
    ChrTalk(
        0xB,
        (
            "最近、研修医の間で\x01",
            "セイランド教授が噂になっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xB,
        (
            "私にはあまり縁がないが……\x01",
            "実際はどんな人なんだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C2")

    TalkEnd(0xFE)
    Return()

    # Function_6_D2E end

    def Function_7_10C6(): pass

    label("Function_7_10C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10D7")
    Jump("loc_173D")

    label("loc_10D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10E5")
    Jump("loc_173D")

    label("loc_10E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1140")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1100")
    Call(0, 9)
    Jump("loc_113B")

    label("loc_1100")


    #C0034
    ChrTalk(
        0xC,
        (
            "えへへ、やっぱりメイファちゃんは\x01",
            "頼りになりますよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113B")

    Jump("loc_173D")

    label("loc_1140")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1337")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1282")

    #C0035
    ChrTalk(
        0xC,
        (
            "今日のシーツの干し方は\x01",
            "あたしが昨日思いついた、\x01",
            "必殺の『重ね干し』なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xC,
        (
            "なんと、２枚重ねて干す事で\x01",
            "倍の枚数のシーツを同時に\x01",
            "乾かす事ができるので～す！\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xC,
        (
            "これで、今日お休みの\x01",
            "メイファちゃんの分も\x01",
            "バッチリカバーですよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xC,
        (
            "……あれれ、でも……\x01",
            "もしかして全然乾いてない……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1332")

    label("loc_1282")


    #C0039
    ChrTalk(
        0xC,
        (
            "うう、必殺の『重ね干し』は\x01",
            "シーツが全然乾かないことが\x01",
            "発覚してしまいました……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        (
            "メイファちゃんが休みだから、\x01",
            "あたしが２人分がんばらないとって\x01",
            "思ってたんですけど～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1332")

    Jump("loc_173D")

    label("loc_1337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1345")
    Jump("loc_173D")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1353")
    Jump("loc_173D")

    label("loc_1353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1361")
    Jump("loc_173D")

    label("loc_1361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_14FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1460")

    #C0041
    ChrTalk(
        0xC,
        (
            "この間のミハイル君の退院の時、\x01",
            "泣いてたメイファちゃんに\x01",
            "私のハンカチを渡してあげたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xC,
        (
            "そしたら、なんだか急に泣き止んで、\x01",
            "じぃっとあたしを見るのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "う～ん、なんだったんだろ？\x01",
            "その後ハンカチも返してくれないし……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14F7")

    label("loc_1460")


    #C0044
    ChrTalk(
        0xC,
        (
            "メイファちゃん、あたしのハンカチ\x01",
            "どうしちゃったのかな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "前に寮の部屋で拾ってから、\x01",
            "手触りがよくてデザインもいいから\x01",
            "気に入ってたのにな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F7")

    Jump("loc_173D")

    label("loc_14FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1517")
    Call(0, 8)
    Jump("loc_15EA")

    label("loc_1517")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0046
    ChrTalk(
        0xC,
        (
            "あ、そうだ！\x01",
            "ためしにナース服着てみる？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 500)

    #C0047
    ChrTalk(
        0xC,
        (
            "ほら、メイファちゃん、\x01",
            "それ脱いで貸したげてよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xD,
        "か、貸さないわよっ！！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "（う、うーん、\x01",
            "  相変わらずだなー……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x8, 0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_15EA")

    Jump("loc_173D")

    label("loc_15EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B6")

    #C0050
    ChrTalk(
        0xC,
        (
            "ふふ、今日はいいお天気。\x01",
            "洗濯物もよく乾きそう♪\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xC,
        (
            "……は～、なんだか\x01",
            "このぽかぽか陽気……\x01",
            "眠くなってきちゃうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xC,
        (
            "また、シーツを一枚借りて\x01",
            "寝ちゃおっかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_172F")

    label("loc_16B6")


    #C0053
    ChrTalk(
        0xC,
        (
            "ここで日向ぼっこすると\x01",
            "きもちいいんですよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        (
            "今日はメイファちゃん\x01",
            "来ない気がするし……\x01",
            "うん、寝ちゃおうっと☆\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172F")

    Jump("loc_173D")

    label("loc_1734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_173D")

    label("loc_173D")

    TalkEnd(0xFE)
    Return()

    # Function_7_10C6 end

    def Function_8_1741(): pass

    label("Function_8_1741")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0055
    ChrTalk(
        0x8,
        (
            "研修医の試験も落ちちゃって……\x01",
            "いよいよ家でも肩身が狭いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "なあ、シロン姉ちゃん。\x01",
            "これから俺、どうすればいいかなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "（バッジョ君……\x01",
            "  シロンなんかに相談するなんて、\x01",
            "  よっぽど切羽詰ってるのね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xC,
        "んー、そうだなぁ……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "そんじゃ、お姉ちゃんと同じ\x01",
            "ナースになってみたりとか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_64(0xD)

    #C0060
    ChrTalk(
        0xD,
        (
            "シ、シロンにしちゃ\x01",
            "マトモな意見じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "なるほど、男性看護師か……\x01",
            "それは盲点だったなあ！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_8_1741 end

    def Function_9_1925(): pass

    label("Function_9_1925")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    #C0062
    ChrTalk(
        0xD,
        (
            "シロン、あんたね……\x01",
            "シーツを重ねて干したら\x01",
            "乾くものも乾かないでしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xD,
        (
            "まったくもう、\x01",
            "あんた何年この仕事を\x01",
            "やってんだっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "えーっと、メイファちゃんと\x01",
            "一緒に入ったから、いち、にぃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xD,
        (
            "えーい、余計なところで\x01",
            "律儀に答えなくていいのっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xD,
        "ほら、さっさと干しなおす！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_9_1925 end

    def Function_10_1A65(): pass

    label("Function_10_1A65")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A76")
    Jump("loc_1D4C")

    label("loc_1A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1A84")
    Jump("loc_1D4C")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1B1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9F")
    Call(0, 9)
    Jump("loc_1B18")

    label("loc_1A9F")


    #C0067
    ChrTalk(
        0xD,
        (
            "まったくシロンったら……\x01",
            "シーツくらい１人で\x01",
            "まともに干せないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xD,
        (
            "やっぱり私が見ていないと\x01",
            "全然ダメね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B18")

    Jump("loc_1D4C")

    label("loc_1B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1B2B")
    Jump("loc_1D4C")

    label("loc_1B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B39")
    Jump("loc_1D4C")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B47")
    Jump("loc_1D4C")

    label("loc_1B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C14")

    #C0069
    ChrTalk(
        0xD,
        (
            "シロンのやつ、今日はなんだか\x01",
            "師長に怒られてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xD,
        (
            "普段ミスばっかりするから、\x01",
            "たまにはちゃんと怒られるのも\x01",
            "大事よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xD,
        (
            "……ま、頃合いを見て\x01",
            "庇いに行ってやるか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1C92")

    label("loc_1C14")


    #C0072
    ChrTalk(
        0xD,
        (
            "シロンのやつ、今日はなんだか\x01",
            "師長に怒られてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xD,
        (
            "ま、あとで庇いに行ってやるか。\x01",
            "……あたしもつくづく甘いわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C92")

    Jump("loc_1D4C")

    label("loc_1C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1CA5")
    Jump("loc_1D4C")

    label("loc_1CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC0")
    Call(0, 8)
    Jump("loc_1D30")

    label("loc_1CC0")


    #C0074
    ChrTalk(
        0xD,
        (
            "シロンって、たま～～～～に\x01",
            "マトモなこと言うのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "……明日はレーザー光線でも\x01",
            "降るんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D30")

    Jump("loc_1D4C")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1D43")
    Jump("loc_1D4C")

    label("loc_1D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D4C")

    label("loc_1D4C")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A65 end

    def Function_11_1D50(): pass

    label("Function_11_1D50")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3510, 8300, 11470, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x104, -1400, 7000, 11230, 270)
    SetChrPos(0x102, -1990, 7000, 12030, 225)
    SetChrPos(0x101, -2790, 7000, 12830, 225)
    SetChrPos(0x103, -3590, 7000, 13630, 180)
    SetChrPos(0x109, -2590, 7000, 14030, 180)
    SetChrPos(0x105, -3400, 7000, 14840, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_0D()

    #C0076
    ChrTalk(
        0x101,
        (
            "#5P#00000Fシズクちゃん、\x01",
            "こんな所にいたのか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 500)

    #C0077
    ChrTalk(
        0x9,
        (
            "#12P#11205Fあ……もしかして、\x01",
            "支援課の皆さん？\x02\x03",

            "#11200F今日は、誰かのお見舞いに\x01",
            "来てたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        (
            "#5P#10108Fうん、フランが入院してるから。\x02\x03",

            "#10100Fあとは警察の警部さんや\x01",
            "イリアさんもお見舞いしてたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "#12P#11208Fそうでしたか……\x01",
            "フランさんの事はセシルさんに\x01",
            "聞いてましたけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    #C0080
    ChrTalk(
        0x9,
        (
            "#12P#11203Fやっぱり、街の襲撃事件は\x01",
            "相当酷かったみたいですね。\x02\x03",

            "#11208Fセシルさんたちや先生たちも、\x01",
            "ずっと忙しくしているみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#5P#00003Fああ……\x01",
            "確かにそんな感じだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        (
            "#11P#00100Fそういえばシズクちゃん、\x01",
            "アリオスさんは\x01",
            "最近、見舞いに来れてる？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#12P#11208Fいえ、襲撃事件があってからは\x01",
            "まだ一度も……\x02\x03",

            "#11200F連絡はあったんですが、\x01",
            "やっぱり色々と忙しいそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#5P#00200Fそうですか……\x01",
            "寂しいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "#12P#11200F……いいえ、私なら大丈夫です。\x02\x03",

            "#11203Fたくさんの人が犠牲になって、\x01",
            "怪我人も多く出て……\x02\x03",

            "そんな中、私だけが甘えている\x01",
            "わけにはいきませんから。\x02\x03",

            "#11208F……私も何かしたいと思って、\x01",
            "フランさんや他の患者さんたちを\x01",
            "励ましたりしてるんですけど……\x02\x03",

            "#11203F……ただ、目の見えない私には\x01",
            "それくらいしかできなくて……\x01",
            "それは、やっぱり悔しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#11P#00300F……いや、充分すぎると思うぜ。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00000F君のそういう姿は、\x01",
            "逆境に立ち向かう勇気を\x01",
            "みんなに与えていると思うよ。\x02\x03",

            "#00004F……俺たちも頑張らなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x105,
        "#5P#10302Fフフ……そうだね。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "#12P#11200Fえっと……\x01",
            "みなさんも大変だと思いますけど、\x01",
            "どうか頑張ってください。\x02\x03",

            "#11203F私もここから応援してますから……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x9, 0x10)
    OP_93(0x9, 0x5A, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x18E, 5)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2790, 7000, 12830, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_1D50 end

    def Function_12_2430(): pass

    label("Function_12_2430")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch02500.itc", 0x1F)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1900, 7000, 14600, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1300, 7000, 15610, 180)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -3100, 7000, 14600, 180)
    OP_68(-3510, 8400, 11470, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16160, 0)
    SetChrPos(0x104, -2100, 7000, 16800, 180)
    SetChrPos(0x102, -1900, 7000, 17810, 180)
    SetChrPos(0x101, -2310, 7000, 18610, 180)
    SetChrPos(0x103, -1700, 7000, 19600, 180)
    SetChrPos(0x109, -1910, 7000, 20600, 180)
    SetChrPos(0x105, -2120, 7000, 21590, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    BeginChrThread(0x9, 3, 0, 13)
    BeginChrThread(0xE, 3, 0, 14)
    BeginChrThread(0xF, 3, 0, 15)
    BeginChrThread(0x104, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x101, 3, 0, 18)
    BeginChrThread(0x103, 3, 0, 19)
    BeginChrThread(0x109, 3, 0, 20)
    BeginChrThread(0x105, 3, 0, 21)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 3)
    WaitChrThread(0xE, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)

    #C0090
    ChrTalk(
        0xE,
        "#01400Fシズク、足元に気をつけろ。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#6P#11202Fうん、ありがとうお父さん。\x02\x03",

            "#11204Fふふ、いい風……\x01",
            "それに、日の光が明るくて、\x01",
            "あったかくて気持ちいい……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00002Fはは、それはよかった。\x02\x03",

            "#00003F……そういえばさっき、\x01",
            "周囲の光が感じられるように\x01",
            "なったって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0093
    ChrTalk(
        0x9,
        (
            "#12P#11200Fええ、といっても\x01",
            "そんなに細かくは分かりませんけど。\x02\x03",

            "#11203Fあたり一面に真っ白なモヤが\x01",
            "かかったようになって、\x01",
            "明るさを感じられるくらいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        "#00108Fそう……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x104,
        (
            "#00303F光を感じられるっつっても、\x01",
            "やっぱ見えてるってレベルじゃ\x01",
            "ないみたいだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xE,
        "#01403F…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0097
    ChrTalk(
        0x9,
        (
            "#6P#11202F……え、えっと。\x01",
            "皆さん、そんなに暗く\x01",
            "ならないでください。\x02\x03",

            "#11209F私は、今回の手術の結果には\x01",
            "とても喜んでるんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        "#5P#10305Fへえ……そうなのかい？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#6P#11203F……確かに最初は、\x01",
            "完治しなかったことに\x01",
            "落ち込みもしました。\x02\x03",

            "#11208Fもう、絶対に\x01",
            "治らないんじゃないかって……\x01",
            "諦めそうになったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x103,
        "#00208Fシズクさん……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "#6P#11202Fでも、考えてみれば、\x01",
            "こうまで“治療が進んだ”のは\x01",
            "今回が初めてなんです。\x02\x03",

            "#11204Fだから私の目はゆっくりだけど、\x01",
            "きっとよくなっていく……\x01",
            "改めてそう思うことができました。\x02\x03",

            "#11200F支えてくれるお父さんや、\x01",
            "病院の皆さん、そして\x01",
            "キーアちゃんのためにも……\x02\x03",

            "#11209Fこれからも諦めずに\x01",
            "治療を続けていこうと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x109,
        "#5P#10102Fシズクちゃん……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        "#00004F……君は強いな、本当に。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0104
    ChrTalk(
        0x9,
        (
            "#6P#11205Fえ、えっと……すみません、\x01",
            "流石に偉そうですよね。\x02\x03",

            "#11203F治療費だってお父さんに\x01",
            "出してもらって、いつも\x01",
            "迷惑かけてるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xE,
        (
            "#01403F……お前が諦めないというなら、\x01",
            "俺は今まで通りに支えていくだけだ。\x02\x03",

            "#01402F余計なことを考えずに、\x01",
            "光を取り戻すことに集中するといい。\x02\x03",

            "#01404Fサヤも、それを望んでいるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "#6P#11203Fお父さん……そうだね。\x02\x03",

            "#11202F女神様の元にいる\x01",
            "お母さんのためにも……\x01",
            "これからも頑張るから。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xF,
        (
            "#01004Fクク、アリオス。\x01",
            "やはりお前の子供だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        (
            "#00309Fハハ、確かに。\x01",
            "芯の強いところがソックリだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xE,
        (
            "#01404F……きっと、\x01",
            "母親#4Rサ　ヤ#に似たんだろう。\x02\x03",

            "#01400F──そろそろ外出時間は終わりだな。\x01",
            "シズク、病室に戻るぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        "#6P#11205Fあ……うん、分かった。\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#00000Fそれじゃあ、戻るとしましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "シズクの病室で一時の歓談を楽しんだのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 0)
    NewScene("t1550", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2430 end

    def Function_13_2ED5(): pass

    label("Function_13_2ED5")


    def lambda_2EDA():
        OP_95(0xFE, -3590, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EDA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_13_2ED5 end

    def Function_14_2EFB(): pass

    label("Function_14_2EFB")


    def lambda_2F00():
        OP_95(0xFE, -2590, 7000, 11020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F00)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_14_2EFB end

    def Function_15_2F21(): pass

    label("Function_15_2F21")


    def lambda_2F26():
        OP_95(0xFE, -1500, 7000, 10030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F26)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_2F21 end

    def Function_16_2F47(): pass

    label("Function_16_2F47")


    def lambda_2F4C():
        OP_95(0xFE, -1400, 7000, 11230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F4C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_16_2F47 end

    def Function_17_2F6D(): pass

    label("Function_17_2F6D")


    def lambda_2F72():
        OP_95(0xFE, -1990, 7000, 12030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F72)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_17_2F6D end

    def Function_18_2F93(): pass

    label("Function_18_2F93")


    def lambda_2F98():
        OP_95(0xFE, -2790, 7000, 12830, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F98)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_18_2F93 end

    def Function_19_2FB9(): pass

    label("Function_19_2FB9")


    def lambda_2FBE():
        OP_95(0xFE, -3590, 7000, 13630, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FBE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_19_2FB9 end

    def Function_20_2FDF(): pass

    label("Function_20_2FDF")


    def lambda_2FE4():
        OP_95(0xFE, -2590, 7000, 14030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FE4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_20_2FDF end

    def Function_21_3005(): pass

    label("Function_21_3005")


    def lambda_300A():
        OP_95(0xFE, -3400, 7000, 14840, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_300A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_21_3005 end

    def Function_22_302B(): pass

    label("Function_22_302B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3139")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kどこに行きますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【４Ｆ 薬学・神経科研究室】\x01",      # 0
            "【やめる】\x01",                       # 1
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
        (0, "loc_30E4"),
        (1, "loc_312D"),
        (SWITCH_DEFAULT, "loc_3134"),
    )


    label("loc_30E4")

    FadeToDark(1000, 0, -1)
    OP_71(0x5, 0x0, 0x5, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x5)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311F")
    SetScenarioFlags(0x22, 0)
    NewScene("t1650", 100, 0, 0)
    IdleLoop()
    Jump("loc_3128")

    label("loc_311F")

    NewScene("t1650", 101, 0, 0)
    IdleLoop()

    label("loc_3128")

    Jump("loc_3134")

    label("loc_312D")

    EventEnd(0x3)
    Jump("loc_3134")

    label("loc_3134")

    Jump("loc_318C")

    label("loc_3139")

    EventBegin(0x2)
    ClearMapFlags(0x20)

    #C0114
    ChrTalk(
        0x101,
        (
            "#00000Fこっちは研究棟か。\x01",
            "特に用事はないし、\x01",
            "立ち入らないでおこう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    EventEnd(0x3)

    label("loc_318C")

    Return()

    # Function_22_302B end

    def Function_23_318D(): pass

    label("Function_23_318D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(14750, 9400, -3400, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15860, 0)
    SetChrPos(0x101, 18740, 7000, -3160, 270)
    SetChrPos(0x102, 18740, 7000, -3160, 270)
    SetChrPos(0x109, 18740, 7000, -3160, 270)
    SetChrPos(0x105, 18740, 7000, -3160, 270)
    SetChrPos(0x104, 18740, 7000, -3160, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(14750, 8000, -3400, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x5)
    Sleep(500)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 26)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 28)
    WaitChrThread(0x105, 3)
    Sound(107, 0, 100, 0)
    OP_71(0x5, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0115
    ChrTalk(
        0x104,
        (
            "#00301F……なんか色々判ったような、\x01",
            "謎が増えたような気分だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x109,
        "#12P#10106F何だか歯がゆいですね……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        (
            "#00108Fええ、ヨアヒム先生が亡くなった今、\x01",
            "あまりに手がかりが少なすぎる……\x02\x03",

            "#00103Fせめて教団のデータベースの解析が\x01",
            "進めば何か判るかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x105,
        (
            "#11P#10300Fま、そのあたりは\x01",
            "今後の課題ってやつかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#00001Fああ……俺たちの方でも\x01",
            "忘れずに気にかけておこう。\x02\x03",

            "#00003F──とりあえず、\x01",
            "今回の依頼はこれで達成だ。\x02\x03",

            "#00000F帰りにセシル姉のところに\x01",
            "寄ってもいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#00309Fおう、そうすっか！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【新教授の依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x70, 0x1, 0x6)
    OP_29(0x70, 0x1, 0x7)
    OP_29(0x70, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x5)
    OP_66(0x0, 0x1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 15500, 7000, -3000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ClearMapObjFlags(0x5, 0x10)
    EventEnd(0x5)
    Return()

    # Function_23_318D end

    def Function_24_3600(): pass

    label("Function_24_3600")


    def lambda_3605():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3605)

    def lambda_3616():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3616)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 13000, 7000, -3000, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_24_3600 end

    def Function_25_364B(): pass

    label("Function_25_364B")


    def lambda_3650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3650)

    def lambda_3661():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3661)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 14160, 7000, -2240, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_25_364B end

    def Function_26_3696(): pass

    label("Function_26_3696")


    def lambda_369B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_369B)

    def lambda_36AC():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36AC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 15890, 7000, -3980, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_26_3696 end

    def Function_27_36E1(): pass

    label("Function_27_36E1")


    def lambda_36E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_36E6)

    def lambda_36F7():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36F7)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 14180, 7000, -4310, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_27_36E1 end

    def Function_28_372C(): pass

    label("Function_28_372C")


    def lambda_3731():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3731)

    def lambda_3742():
        OP_98(0xFE, 0xFFFFF830, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3742)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 15840, 7000, -2650, 2000, 0x0)
    OP_93(0x105, 0x10E, 0x1F4)
    Return()

    # Function_28_372C end

    def Function_29_3777(): pass

    label("Function_29_3777")

    EventBegin(0x1)

    #C0122
    ChrTalk(
        0x101,
        (
            "#00000Fおっと、受付にも行かずに\x01",
            "病棟に入るわけにはいかないな。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -16059, 6000, 19210, 270)
    EventEnd(0x4)
    Return()

    # Function_29_3777 end

    SaveToFile()

Try(main)
