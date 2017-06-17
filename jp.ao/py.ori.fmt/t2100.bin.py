from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2100.bin",                # FileName
        "t2100",                    # MapName
        "t2100",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 1, 0, 2],
    )

    BuildStringList((
        "t2100",                  # 0
        "ブルード隊員",           # 1
        "ダリア隊員",             # 2
        "チルル",                 # 3
        "帝国軍戦車",             # 4
        "帝国軍戦車",             # 5
        "帝国軍戦車",             # 6
        "帝国軍戦車",             # 7
        "帝国軍戦車",             # 8
        "SE制御",                 # 9
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch34100.itc",                   # 01
        "chr/ch20500.itc",                   # 02
    ))

    DeclNpc(-13829,  10000,   -2960,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-14060,  10000,   2900,    270,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-18600,  5000,    -17350,  270,  389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(516, 0)                                        # 0

    ScpFunction((
        "Function_0_204",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_33D",          # 02, 2
        "Function_3_47A",          # 03, 3
        "Function_4_5CB",          # 04, 4
        "Function_5_DE9",          # 05, 5
        "Function_6_191C",         # 06, 6
        "Function_7_197C",         # 07, 7
        "Function_8_1D4D",         # 08, 8
        "Function_9_1D5D",         # 09, 9
        "Function_10_1D6D",        # 0A, 10
        "Function_11_1D8A",        # 0B, 11
        "Function_12_1DAA",        # 0C, 12
        "Function_13_1DCA",        # 0D, 13
        "Function_14_1DEA",        # 0E, 14
        "Function_15_1E0A",        # 0F, 15
        "Function_16_1E55",        # 10, 16
    ))


    def Function_0_204(): pass

    label("Function_0_204")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_23C"),
        (1, "loc_248"),
        (2, "loc_254"),
        (3, "loc_260"),
        (4, "loc_26C"),
        (5, "loc_278"),
        (6, "loc_284"),
        (SWITCH_DEFAULT, "loc_290"),
    )


    label("loc_23C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_248")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_254")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_260")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_26C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_278")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_29C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_29C")

    label("loc_2B3")

    Return()

    # Function_0_204 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C2")
    Jump("loc_316")

    label("loc_2C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D0")
    Jump("loc_316")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DE")
    Jump("loc_316")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EC")
    Jump("loc_316")

    label("loc_2EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FA")
    Jump("loc_316")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_308")
    Jump("loc_316")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_316")
    ClearChrFlags(0xA, 0x80)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_32D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)
    Jump("loc_33C")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_33C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 16)

    label("loc_33C")

    Return()

    # Function_1_2B4 end

    def Function_2_33D(): pass

    label("Function_2_33D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_357")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_385")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_373")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_385")

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_385")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_385")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_409")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0xE6, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_420")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_420")

    label("loc_420")

    SetMapObjFrame(0xFF, "open", 0x0, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475")
    OP_70(0x2, 0x0)
    Jump("loc_479")

    label("loc_475")

    OP_70(0x2, 0x1E)

    label("loc_479")

    Return()

    # Function_2_33D end

    def Function_3_47A(): pass

    label("Function_3_47A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x2D, 1)"), scpexpr(EXPR_END)), "loc_503")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1ED, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_575")

    label("loc_503")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x2D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_575")

    Jump("loc_5BF")

    label("loc_57A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_5BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_47A end

    def Function_4_5CB(): pass

    label("Function_4_5CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BB")

    #C0004
    ChrTalk(
        0xFE,
        (
            "クロスベル市を襲撃した\x01",
            "猟兵団を、帝国が雇っていた……\x01",
            "そんな噂があるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "警備隊の仲間たちを傷つけた奴らは、\x01",
            "どうあっても許しちゃおけない。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "帝国がそういうつもりなら、\x01",
            "俺も腹を括ってやるさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_741")

    label("loc_6BB")


    #C0007
    ChrTalk(
        0xFE,
        (
            "帝国方面で大規模な\x01",
            "演習が行われるなんて\x01",
            "噂があるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "……上等だよ。\x01",
            "帝国がそういうつもりなら、\x01",
            "俺も腹を括ってやるさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741")

    Jump("loc_DE5")

    label("loc_746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7C1")

    #C0009
    ChrTalk(
        0xFE,
        (
            "小雨でもやっぱり\x01",
            "視界が悪くなるなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "幻獣もまだ目撃情報が\x01",
            "出ているようだし……\x01",
            "注意しなくちゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE5")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_883")

    #C0011
    ChrTalk(
        0xFE,
        (
            "やれやれ、最近は忙しくて\x01",
            "休む暇もないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "……でも、司令や三尉たちは\x01",
            "俺たちより大変なんだろうな。\x01",
            "あのタフさには敬服するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        "俺も、もっと頑張らないと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_8F1")

    label("loc_883")


    #C0014
    ChrTalk(
        0xFE,
        (
            "司令や三尉たちは\x01",
            "俺たちより大変なんだろうな。\x01",
            "あのタフさには敬服するよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        "俺も、もっと頑張らないと。\x02",
    )

    CloseMessageWindow()

    label("loc_8F1")

    Jump("loc_DE5")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CC")

    #C0016
    ChrTalk(
        0xFE,
        (
            "市長が独立提唱をしてから、\x01",
            "帝国や共和国が露骨に圧力を\x01",
            "かけてくるようになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "正直、この緊張状態は胃が痛いよ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "早いうちになんらかの決着を\x01",
            "見せてくれるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A2F")

    label("loc_9CC")


    #C0019
    ChrTalk(
        0xFE,
        "正直、この緊張状態は胃が痛いよ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "早いうちになんらかの決着を\x01",
            "見せてくれるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F")

    Jump("loc_DE5")

    label("loc_A34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_AD8")

    #C0021
    ChrTalk(
        0xFE,
        (
            "情報によると、帝国方面から\x01",
            "テロリストが侵入してくる\x01",
            "可能性が高いそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "さすがに緊張してくるよ。\x01",
            "何事もなく一日が終われば\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE5")

    label("loc_AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10")

    #C0023
    ChrTalk(
        0xFE,
        (
            "タングラム門にいるバレルは\x01",
            "俺の友人なんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "鬼のように厳しい副司令に\x01",
            "毎日シゴかれているらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "でも、上司が無能なのに比べたら\x01",
            "厳しいだなんてのは贅沢な悩みだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令もかなり厳しいけど、\x01",
            "前の司令の方がよかったなんて\x01",
            "１リジュたりとも思わないからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CB5")

    label("loc_C10")


    #C0027
    ChrTalk(
        0xFE,
        (
            "上司が無能なのに比べたら\x01",
            "厳しいだなんてのは贅沢な悩みだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令もかなり厳しいけど、\x01",
            "前の司令の方がよかったなんて\x01",
            "１リジュたりとも思わないからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB5")

    Jump("loc_DE5")

    label("loc_CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_DE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5C")

    #C0029
    ChrTalk(
        0xFE,
        (
            "ソーニャ司令が来てくれて、\x01",
            "ベルガード門での警備にも\x01",
            "俄然やる気がでるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "上司が有能っていうのは、\x01",
            "本当に幸せなことなんだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_DE5")

    label("loc_D5C")


    #C0031
    ChrTalk(
        0xFE,
        (
            "前の司令がいたときは、\x01",
            "これほど充実した気分で\x01",
            "仕事ができたことはなかった。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "上司が有能っていうのは、\x01",
            "本当に幸せなことなんだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DE5")

    TalkEnd(0xFE)
    Return()

    # Function_4_5CB end

    def Function_5_DE9(): pass

    label("Function_5_DE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")

    #C0033
    ChrTalk(
        0xFE,
        (
            "国家独立の気運が高まるこの情勢、\x01",
            "今の緊張状態は不戦条約以前と\x01",
            "同等以上と言えるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "もし帝国との対立が極限に達すれば、\x01",
            "再びあの『列車砲』が現れる可能性は\x01",
            "充分にあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "やはり……帝国と共和国との\x01",
            "争いは避けられないのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_FD2")

    label("loc_F02")


    #C0036
    ChrTalk(
        0xFE,
        (
            "……近頃、ソーニャ司令も\x01",
            "よく考え事に耽っているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "警備隊の再編について、\x01",
            "ディーター市長やマクダエル議長とも\x01",
            "話し合っているそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "２大国との対立も含めて、\x01",
            "問題は山積みですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD2")

    Jump("loc_1918")

    label("loc_FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_113B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")

    #C0039
    ChrTalk(
        0xFE,
        (
            "昨日の脱線事故……\x01",
            "本当にひどいものでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "もしあの巨大な化物が\x01",
            "犯人なのだとしたら……\x01",
            "また起こらないか心配です。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "やはり、化物の捜索と退治は\x01",
            "なんとかしておきたいところですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1136")

    label("loc_10B4")


    #C0042
    ChrTalk(
        0xFE,
        (
            "横断鉄道の位置づけを考えると、\x01",
            "再発防止は最優先事項です。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "やはり、化物の捜索と退治は\x01",
            "なんとかしておきたいところですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1136")

    Jump("loc_1918")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_13CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1226")

    #C0044
    ChrTalk(
        0xFE,
        (
            "ブルードさんが気晴らしにと\x01",
            "本を譲ってくれたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "なかなか面白かったので、\x01",
            "もしよかったら皆さんも\x01",
            "読んでみてください。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 7)
    Jump("loc_13C6")

    label("loc_1226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1328")

    #C0047
    ChrTalk(
        0xFE,
        (
            "あの岩盤の内部にある\x01",
            "《ガレリア要塞》には、\x01",
            "様々な兵器が配備されています。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "過去、極限の緊張状態の際に\x01",
            "行われた大規模な演習では、\x01",
            "『列車砲』も稼動していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "この緊張状態がそこまでの\x01",
            "事態を招かないことを\x01",
            "祈りたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_13C6")

    label("loc_1328")


    #C0050
    ChrTalk(
        0xFE,
        (
            "過去、極限の緊張状態の際に\x01",
            "帝国で行われた演習では、\x01",
            "『列車砲』も稼動していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "この緊張状態がそこまでの\x01",
            "事態を招かないことを\x01",
            "祈りたいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C6")

    Jump("loc_1918")

    label("loc_13CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148D")

    #C0052
    ChrTalk(
        0xFE,
        (
            "あの独立提唱には\x01",
            "私も驚いたものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "ですが……クロスベルを\x01",
            "これからも守っていくためには\x01",
            "必要なことなのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        "なんとか実現するといいですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_14FF")

    label("loc_148D")


    #C0055
    ChrTalk(
        0xFE,
        (
            "あの独立提唱には\x01",
            "私も驚いたものですが……\x01",
            "必要なことなのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "なんとか実現するといいですね。\x02",
    )

    CloseMessageWindow()

    label("loc_14FF")

    Jump("loc_1918")

    label("loc_1504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164F")

    #C0057
    ChrTalk(
        0xFE,
        (
            "テロリストの情報を受けて、\x01",
            "国境付近の警備は最大限に\x01",
            "努力させてもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "空路からの進入を防ぐために、\x01",
            "付近に設置された特別な施設が\x01",
            "運用されているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "加えて、軍隊の持つような対空砲があれば\x01",
            "万全を期することができるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "……無いものねだりをしても\x01",
            "仕方ありませんよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_16E6")

    label("loc_164F")


    #C0061
    ChrTalk(
        0xFE,
        (
            "軍隊の持つような対空砲があれば\x01",
            "空路からの進入に対しても\x01",
            "万全を期することができるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "……無いものねだりをしても\x01",
            "仕方ありませんよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E6")

    Jump("loc_1918")

    label("loc_16EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1869")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E4")

    #C0063
    ChrTalk(
        0xFE,
        (
            "今朝、門の下を通っていく\x01",
            "真紅の導力列車を見かけました。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "あれは帝国政府専用の列車……\x01",
            "あの《鉄血宰相》とオリヴァルト皇子が\x01",
            "乗っていたのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "通商会議がいよいよ始まった……\x01",
            "そんな感覚がひしひしとします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1864")

    label("loc_17E4")


    #C0066
    ChrTalk(
        0xFE,
        (
            "今朝、門の下を通っていく\x01",
            "真紅の導力列車を見かけました。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "通商会議がいよいよ始まった……\x01",
            "そんな感覚がひしひしとします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1864")

    Jump("loc_1918")

    label("loc_1869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1918")

    #C0068
    ChrTalk(
        0xFE,
        (
            "通商会議が近づいてきて、\x01",
            "私たち警備隊が持つ責任も\x01",
            "さらに大きくなってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "クロスベル入りする\x01",
            "各国の首脳を守るためにも……\x01",
            "国境の警備は厳にしなければ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1918")

    TalkEnd(0xFE)
    Return()

    # Function_5_DE9 end

    def Function_6_191C(): pass

    label("Function_6_191C")

    TalkBegin(0xFE)

    #C0070
    ChrTalk(
        0xFE,
        "この渓谷は、やっぱり凄い……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "落ちたら無事じゃすまなそう。\x01",
            "どきどきしてくる……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_191C end

    def Function_7_197C(): pass

    label("Function_7_197C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_04a.pmf", 0x22C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    OP_F3(200000)
    LoadEffect(0x0, "event/ev15060.eff")
    SoundLoad(825)
    SoundLoad(923)
    OP_68(-66820, 1000, -14120, 0)
    MoveCamera(307, 12, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(75270, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x22C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "close", 0x0, 0x1)
    SetMapObjFrame(0xFF, "open", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x1, 0x1)
    OP_68(-69430, 11500, -13600, 0)
    MoveCamera(297, 8, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(65000, 0)
    SetCameraDistance(71000, 5500)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -122940, 200, -1170, 0)
    SetMapObjFlags(0x5, 0x1000)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0xB)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -139790, 200, -2770, 0)
    SetMapObjFlags(0x4, 0x1000)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0xC)
    OP_93(0xC, 0x5A, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -156790, 200, 2770, 0)
    SetMapObjFlags(0x3, 0x1000)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xD)
    OP_93(0xD, 0x5A, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -177000, 200, 1140, 0)
    SetMapObjFlags(0x6, 0x1000)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x6, 0xE)
    OP_93(0xE, 0x5A, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -198000, 200, -1150, 0)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0xF)
    OP_93(0xF, 0x5A, 0x0)
    OP_75(0x6, 0x1, 0x0)
    OP_75(0x7, 0x1, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    PlaceName2(340, 200, "c_plac66", 0x0, 0)
    OP_6F(0x79)
    BeginChrThread(0xB, 0, 0, 10)
    BeginChrThread(0xC, 0, 0, 11)
    BeginChrThread(0xD, 0, 0, 12)
    BeginChrThread(0xE, 0, 0, 13)
    BeginChrThread(0xF, 0, 0, 14)
    BeginChrThread(0x10, 1, 0, 15)
    OP_68(-91380, 15200, 2180, 0)
    MoveCamera(331, 11, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(83380, 0)
    Fade(500)
    OP_0D()
    OP_68(-90600, 7400, 2210, 7500)
    MoveCamera(331, 5, 0, 7500)
    OP_6E(450, 7500)
    SetCameraDistance(77550, 7200)
    OP_6F(0x79)
    SetCameraDistance(40000, 5000)
    OP_68(-85000, 4700, 1860, 8200)
    Sleep(4500)
    MoveCamera(317, -1, 0, 3500)
    OP_6F(0x79)
    OP_68(-32549, 4800, -7710, 18500)
    SetCameraDistance(42000, 4000)
    Sleep(6000)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    OP_68(-54250, 2570, -1160, 0)
    MoveCamera(270, 10, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(14060, 0)
    Fade(500)
    BeginChrThread(0xB, 1, 0, 9)
    BeginChrThread(0xC, 1, 0, 9)
    BeginChrThread(0xD, 1, 0, 9)
    BeginChrThread(0xE, 1, 0, 9)
    BeginChrThread(0xF, 1, 0, 9)
    OP_68(-43550, 2570, -690, 8000)
    MoveCamera(266, 7, 0, 8000)
    OP_6E(450, 8000)
    SetCameraDistance(17940, 8000)
    Sleep(1500)
    OP_75(0x6, 0x2, 0x2BC)
    Sleep(3500)
    OP_75(0x7, 0x2, 0x2BC)
    Sleep(2000)
    StopSound(923, 1000, 60)
    StopSound(825, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_197C end

    def Function_8_1D4D(): pass

    label("Function_8_1D4D")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0xBB8, 0x0)
    Return()

    # Function_8_1D4D end

    def Function_9_1D5D(): pass

    label("Function_9_1D5D")

    OP_9B(0x1, 0xFE, 0x0, 0x1D4C0, 0x7D0, 0x0)
    Return()

    # Function_9_1D5D end

    def Function_10_1D6D(): pass

    label("Function_10_1D6D")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)

    label("loc_1D76")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D89")
    Sleep(5000)
    Jump("loc_1D76")

    label("loc_1D89")

    Return()

    # Function_10_1D6D end

    def Function_11_1D8A(): pass

    label("Function_11_1D8A")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(1200)

    label("loc_1D96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DA9")
    Sleep(5000)
    Jump("loc_1D96")

    label("loc_1DA9")

    Return()

    # Function_11_1D8A end

    def Function_12_1DAA(): pass

    label("Function_12_1DAA")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(2400)

    label("loc_1DB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DC9")
    Sleep(5000)
    Jump("loc_1DB6")

    label("loc_1DC9")

    Return()

    # Function_12_1DAA end

    def Function_13_1DCA(): pass

    label("Function_13_1DCA")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(3600)

    label("loc_1DD6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DE9")
    Sleep(5000)
    Jump("loc_1DD6")

    label("loc_1DE9")

    Return()

    # Function_13_1DCA end

    def Function_14_1DEA(): pass

    label("Function_14_1DEA")

    Sleep(1500)
    BeginChrThread(0xFE, 1, 0, 8)
    Sleep(4800)

    label("loc_1DF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E09")
    Sleep(5000)
    Jump("loc_1DF6")

    label("loc_1E09")

    Return()

    # Function_14_1DEA end

    def Function_15_1E0A(): pass

    label("Function_15_1E0A")

    Sound(923, 2, 10, 0)
    Sound(825, 2, 20, 0)
    Sleep(1500)
    OP_25(0x39B, 0x14)
    OP_25(0x339, 0x1E)
    Sleep(1000)
    OP_25(0x39B, 0x1E)
    OP_25(0x339, 0x28)
    Sleep(1000)
    OP_25(0x39B, 0x28)
    OP_25(0x339, 0x32)
    Sleep(500)
    OP_25(0x39B, 0x32)
    OP_25(0x339, 0x3C)
    Sleep(500)
    OP_25(0x39B, 0x3C)
    OP_25(0x339, 0x46)
    Sleep(500)
    OP_25(0x339, 0x50)
    Return()

    # Function_15_1E0A end

    def Function_16_1E55(): pass

    label("Function_16_1E55")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "close", 0x0, 0x1)
    SetMapObjFrame(0xFF, "open", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "amor0b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cano0", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kage01", 0x1, 0x1)
    OP_68(-100000, 0, 0, 0)
    MoveCamera(300, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(80000, 0)
    FadeToBright(1000, 0)
    OP_68(-100000, 10000, 0, 7000)
    Sleep(5000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1E55 end

    SaveToFile()

Try(main)
