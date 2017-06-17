from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1430.bin",                # FileName
        "c1430",                    # MapName
        "c1430",                    # Location
        0x0032,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 50, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1430",                  # 0
        "基约姆师傅",             # 1
        "游击士斯克特",           # 2
        "游击士温蔡尔",           # 3
        "罗伯兹主任",             # 4
    ))

    AddCharChip((
        "chr/ch26400.itc",                   # 00
        "chr/ch27200.itc",                   # 01
        "chr/ch27300.itc",                   # 02
        "chr/ch29300.itc",                   # 03
    ))

    DeclNpc(5619,    0,       5329,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(550,     0,       4179,    90,   389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(709,     0,       5539,    135,  389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-51279,  0,       15350,   270,  389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclActor(4150,    0,       4740,    1000,    5620,    1500,    5330,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_170",          # 00, 0
        "Function_1_228",          # 01, 1
        "Function_2_425",          # 02, 2
        "Function_3_5A5",          # 03, 3
        "Function_4_5C2",          # 04, 4
        "Function_5_D41",          # 05, 5
        "Function_6_25E9",         # 06, 6
        "Function_7_2915",         # 07, 7
        "Function_8_2A4F",         # 08, 8
        "Function_9_2BEC",         # 09, 9
        "Function_10_2C38",        # 0A, 10
        "Function_11_2FCE",        # 0B, 11
        "Function_12_45C5",        # 0C, 12
        "Function_13_6051",        # 0D, 13
    ))


    def Function_0_170(): pass

    label("Function_0_170")

    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B0"),
        (1, "loc_1BC"),
        (2, "loc_1C8"),
        (3, "loc_1D4"),
        (4, "loc_1E0"),
        (5, "loc_1EC"),
        (6, "loc_1F8"),
        (SWITCH_DEFAULT, "loc_204"),
    )


    label("loc_1B0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1BC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1C8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1D4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1E0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1EC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_1F8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_204")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_210")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_227")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_210")

    label("loc_227")

    Return()

    # Function_0_170 end

    def Function_1_228(): pass

    label("Function_1_228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_253")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_2B8")

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    SetChrPos(0xB, 5620, 0, 5330, 270)
    Jump("loc_2B8")

    label("loc_28C")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, 1040, 0, 7000, 270)
    SetChrPos(0xB, -490, 0, 7000, 90)
    SetChrFlags(0xB, 0x10)

    label("loc_2B8")

    Jump("loc_424")

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CB")
    Jump("loc_424")

    label("loc_2CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2E3")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_424")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_424")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_310")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_424")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_424")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_33A")
    Jump("loc_424")

    label("loc_33A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_348")
    Jump("loc_424")

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_356")
    Jump("loc_424")

    label("loc_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_364")
    Jump("loc_424")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_383")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_391")
    Jump("loc_424")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_3CA")
    SetChrPos(0x8, 14820, 1000, 8970, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 14820, 1000, 7170, 0)

    label("loc_3CA")

    Jump("loc_424")

    label("loc_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3DD")
    Jump("loc_424")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3EB")
    Jump("loc_424")

    label("loc_3EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_40A")
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    Jump("loc_424")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_424")
    SetChrPos(0x8, 15240, 1000, 7610, 90)

    label("loc_424")

    Return()

    # Function_1_228 end

    def Function_2_425(): pass

    label("Function_2_425")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_444")

    label("loc_43E")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_444")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_465")
    ClearMapObjFlags(0x0, 0x4)

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_49E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_483")
    OP_65(0x0, 0x1)
    Jump("loc_499")

    label("loc_483")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_495")
    Jump("loc_499")

    label("loc_495")

    OP_65(0x0, 0x1)

    label("loc_499")

    Jump("loc_5A4")

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4AC")
    Jump("loc_5A4")

    label("loc_4AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4BA")
    Jump("loc_5A4")

    label("loc_4BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4C8")
    Jump("loc_5A4")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4DA")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4E8")
    Jump("loc_5A4")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F6")
    Jump("loc_5A4")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_504")
    Jump("loc_5A4")

    label("loc_504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_512")
    Jump("loc_5A4")

    label("loc_512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_520")
    Jump("loc_5A4")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_52E")
    Jump("loc_5A4")

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_540")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_54E")
    Jump("loc_5A4")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_564")
    OP_65(0x0, 0x1)

    label("loc_564")

    Jump("loc_5A4")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_577")
    Jump("loc_5A4")

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_585")
    Jump("loc_5A4")

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_597")
    OP_65(0x0, 0x1)
    Jump("loc_5A4")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5A4")
    OP_65(0x0, 0x1)

    label("loc_5A4")

    Return()

    # Function_2_425 end

    def Function_3_5A5(): pass

    label("Function_3_5A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BE")
    Call(0, 10)
    Return()

    label("loc_5BE")

    Call(0, 4)
    Return()

    # Function_3_5A5 end

    def Function_4_5C2(): pass

    label("Function_4_5C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E3")
    Call(0, 11)
    Return()

    label("loc_5E3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_628")

    #C0001
    ChrTalk(
        0x8,
        (
            "哟，是你们啊。\x01",
            "……要改造些什么吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    SetScenarioFlags(0x4E, 4)
    Jump("loc_8FA")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E4")

    #C0002
    ChrTalk(
        0x8,
        (
            "哦，欢迎光临。\x01",
            "今天有何贵干？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_END)), "loc_6A6")

    #C0003
    ChrTalk(
        0x8,
        (
            "……哎，是你们啊。\x01",
            "好像是警察局『特别任务支援科』的人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F2")

    label("loc_6A6")


    #C0004
    ChrTalk(
        0x8,
        (
            "……哎，是你们啊。\x01",
            "你们不就是克洛斯贝尔时代周刊上\x01",
            "报道过的那些警察吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F2")


    #C0005
    ChrTalk(
        0x8,
        (
            "算了，不管这些，\x01",
            "有什么需要的话就来和我说。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "我们这里以修理导力制品为主，\x01",
            "但如果需要强化改造武器，\x01",
            "也可以来找我！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0005F强化改造吗……？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "没错，也就是使用各种各样的『素材』，\x01",
            "对武器的构造进行强化。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "别看我现在干的是这行，\x01",
            "但以前可是在爱普斯泰恩财团\x01",
            "专门从事材料工程学的研究工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "你们完全可以信任我的技术。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0200F曾经在财团任职吗……\x01",
            "感觉似乎挺厉害呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0300F嗯，看起来，能在这里打造出\x01",
            "其它地方买不到的强力武器呢。\x02\x03",

            "如果得到了材料，\x01",
            "就来这里改造吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 7)
    SetScenarioFlags(0x4E, 4)
    Jump("loc_8FA")

    label("loc_8E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8FA")
    Call(0, 6)
    TalkEnd(0x8)
    Return()

    label("loc_8FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x397, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99B")

    #C0013
    ChrTalk(
        0x8,
        (
            "噢，你们好像已经取得了\x01",
            "『T材料』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "如果想要为魔导杖升级，\x01",
            "就来和我说吧。\x01",
            "我这边已经基本准备好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99B")

    SetScenarioFlags(0x0, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C34")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                # 0
            "委托改造\x01",            # 1
            "委托升级魔导杖\x01",      # 2
            "放弃\x01",                # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_A0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A2A")
    OP_AF(0xAE)
    Jump("loc_A5C")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_A3A")
    OP_AF(0xAD)
    Jump("loc_A5C")

    label("loc_A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A4A")
    OP_AF(0xAC)
    Jump("loc_A5C")

    label("loc_A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_A5A")
    OP_AF(0xAB)
    Jump("loc_A5C")

    label("loc_A5A")

    OP_AF(0xAA)

    label("loc_A5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2F")

    label("loc_A6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFF")

    #C0015
    ChrTalk(
        0x8,
        (
            "如果想要为魔导杖升级，\x01",
            "就需要使用你们身上带着的材料……\x01",
            "现在就要进行改造吗？\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【是的】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x1)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9D")

    #C0016
    ChrTalk(
        0x101,
        "#0000F嗯，麻烦您了。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "好，那就开始吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    #C0018
    ChrTalk(
        0x8,
        (
            "罗伯兹，你那边\x01",
            "已经准备好了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        "噢，你已经拿到材料了啊。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        "我现在就去你那边！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 12)
    Return()

    label("loc_B9D")


    #C0021
    ChrTalk(
        0x8,
        (
            "是吗，以后要是想升级魔导杖，\x01",
            "就再来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "准备工作都已经基本就绪了。\x02",
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2F")

    label("loc_BFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C13")
    Jump("loc_C2F")

    label("loc_C13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_C2F")

    Jump("loc_9A8")

    label("loc_C34")

    Jump("loc_D3D")

    label("loc_C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_D3A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "委托改造\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CA0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_CBF")
    OP_AF(0xAE)
    Jump("loc_CF1")

    label("loc_CBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CCF")
    OP_AF(0xAD)
    Jump("loc_CF1")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_CDF")
    OP_AF(0xAC)
    Jump("loc_CF1")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CEF")
    OP_AF(0xAB)
    Jump("loc_CF1")

    label("loc_CEF")

    OP_AF(0xAA)

    label("loc_CF1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D30")

    label("loc_D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D14")
    Jump("loc_D30")

    label("loc_D14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D30")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_D30")

    Jump("loc_C4C")

    label("loc_D35")

    Jump("loc_D3D")

    label("loc_D3A")

    Call(0, 5)

    label("loc_D3D")

    TalkEnd(0x8)
    Return()

    # Function_4_5C2 end

    def Function_5_D41(): pass

    label("Function_5_D41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDA")

    #C0023
    ChrTalk(
        0x8,
        (
            "必要的材料是一种名为『T材料』\x01",
            "的特殊素材，需要一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "我们会同时进行准备工作的。\x01",
            "如果收集到素材，就来找我吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_EAD")

    #C0025
    ChrTalk(
        0x8,
        (
            "这次的改造，对我来说\x01",
            "并不是什么了不起的工作。\x01",
            "只是照着设计图来打造而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "嘿嘿，不用太在意，就按照\x01",
            "你们自己的方式善加使用吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0200F嗯，那我立刻试用一下吧。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0000F真是谢谢您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1089")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F2E")

    #C0029
    ChrTalk(
        0x8,
        "糟糕，完全都忘掉了呢。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "只要告诉那位警备员老兄\x01",
            "我是相关人员，应该就会\x01",
            "放我进去了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_104B")

    label("loc_F2E")


    #C0031
    ChrTalk(
        0x8,
        "噢，太阳都落山了吗……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "今天本来还想到\x01",
            "财团分部去露个面的，\x01",
            "结果却忘得一干二净了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#0205F您是想去爱普斯泰恩财团的分部吗？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "没错，我打算去那边和\x01",
            "罗伯兹那家伙聊聊天的。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "不过，情况还真是糟糕了，\x01",
            "分部在ＩＢＣ大厦里……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "现在这个时间，大概\x01",
            "都已经关门了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xED, 4)
    SetScenarioFlags(0x0, 0)

    label("loc_104B")

    Jump("loc_1084")

    label("loc_1050")


    #C0037
    ChrTalk(
        0x8,
        "哦、哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        "……想来改造点什么吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1084")

    Jump("loc_25E8")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1138")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10FF")

    #C0039
    ChrTalk(
        0x8,
        (
            "今天早上，总感觉街上\x01",
            "的气氛有些奇怪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "嗯～也没准是因为\x01",
            "通宵熬夜，产生错觉了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1133")

    label("loc_10FF")


    #C0041
    ChrTalk(
        0x8,
        "哦、哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "……想来改造点什么吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1133")

    Jump("loc_25E8")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11B9")

    #C0043
    ChrTalk(
        0x8,
        (
            "我已经上年纪了，\x01",
            "生活方式不会再有什么改变。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "呵呵，就在这里一直经营修理店，\x01",
            "一直干到进棺材算啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1234")

    label("loc_11B9")


    #C0045
    ChrTalk(
        0x8,
        (
            "昨天见到了\x01",
            "久别多时的温蒂呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "她说已经习惯了现在的工作。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "嘿……年轻真好啊，\x01",
            "什么样的新环境都能很快适应。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1234")

    Jump("loc_25E8")

    label("loc_1239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_13AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 2)), scpexpr(EXPR_END)), "loc_12EA")

    #C0048
    ChrTalk(
        0x8,
        (
            "爱普斯泰恩财团的罗伯兹\x01",
            "是我以前在财团时的同事。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "当时的爱普斯泰恩财团\x01",
            "聚集了许多慕名前来学习\x01",
            "导力技术的年轻人。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "我和罗伯兹都是\x01",
            "其中的一员。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13A5")

    label("loc_12EA")


    #C0051
    ChrTalk(
        0x8,
        (
            "在和罗伯兹商量了\x01",
            "不少之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "改造武器的方案也接近完成了，\x01",
            "首先是画出了令人满意的设计图。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "虽然还有不少改良余地，\x01",
            "但至少已经有了个大致构架。\x01",
            "如果愿意的话，就来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 2)

    label("loc_13A5")

    Jump("loc_25E8")

    label("loc_13AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_141B")

    #C0054
    ChrTalk(
        0x8,
        (
            "如果遇到了什么困难，\x01",
            "请不要客气，尽管开口。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "只要是我能做到的，\x01",
            "一定会尽力帮忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1512")

    label("loc_141B")


    #C0056
    ChrTalk(
        0x8,
        (
            "能为特别任务支援科服务，\x01",
            "真是倍感光荣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "我听说你们的活跃表现了哦，\x01",
            "你们好像做了\x01",
            "很危险的事吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0003F嗯……确实是呢，\x01",
            "但总算是告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "要是有什么困难的话，\x01",
            "就来和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "嘿嘿，至少我还是能\x01",
            "为你们提供藏身之处的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1512")

    Jump("loc_25E8")

    label("loc_1517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_158F")

    #C0061
    ChrTalk(
        0x8,
        (
            "过分执著的性格真是令人无奈啊……\x01",
            "总想追求更完美的作品。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        "……哈，不过那正是乐趣所在呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_161C")

    label("loc_158F")


    #C0063
    ChrTalk(
        0x8,
        (
            "我正在研究新的\x01",
            "改造武器设计图呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "嗯～这样也不行，\x01",
            "那样也不行……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "我总是想制作一款\x01",
            "真正的最高杰作。\x01",
            "但想法太多，难以决定。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_161C")

    Jump("loc_25E8")

    label("loc_1621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_168F")

    #C0066
    ChrTalk(
        0x8,
        (
            "出门的话一定要注意啊！\x01",
            "外面的人真是好多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "不过，每年游行之后，\x01",
            "都会这么混乱嘈杂呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_168F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_179E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175A")

    #C0068
    ChrTalk(
        0x8,
        (
            "今天要修理一件\x01",
            "导力玩具，还有……嗯。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "在纪念庆典期间，\x01",
            "各种各样的工作都不请自来，\x01",
            "还真是意外的忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "本想测试一下材料的强度，\x01",
            "结果也都因为时间问题而暂时搁置了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1799")

    label("loc_175A")


    #C0071
    ChrTalk(
        0x8,
        (
            "纪念庆典期间，我也没有打算停业哦。\x01",
            "不用客气，想来就来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1799")

    Jump("loc_25E8")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1827")

    #C0072
    ChrTalk(
        0x8,
        (
            "说起导力网络，那可真是和飞行船\x01",
            "有着同等地位，算是导力技术之精华啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "我也稍微有些兴趣，\x01",
            "但在这旧城区……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D5")

    label("loc_1827")


    #C0074
    ChrTalk(
        0x8,
        (
            "在旧城区这种地方，\x01",
            "不管怎么努力也都很难接触的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        "那就是导力网络。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "这里毕竟是旧城区，\x01",
            "并没有铺设导力缆线。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "我本来也对导力网络\x01",
            "有些兴趣的，可是……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18D5")

    Jump("loc_25E8")

    label("loc_18DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 4)), scpexpr(EXPR_END)), "loc_1951")

    #C0078
    ChrTalk(
        0x8,
        (
            "噢，我最喜欢你们这种\x01",
            "气势十足的家伙啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        (
            "今后也要在工作中加油啊！\x01",
            "期待你们的活跃表现！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A77")

    label("loc_1951")


    #C0080
    ChrTalk(
        0x8,
        (
            "庆典快乐～\x01",
            "祝福克洛斯贝尔～！\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "你们好啊，阻止了暗杀市长\x01",
            "行动的英雄们！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0006F……这种说法\x01",
            "也太让人难为情啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        "我就喜欢这种让人难为情的说话方式。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "你们以后也要继续努力工作啊！\x01",
            "我期待你们的活跃表现！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x104,
        "#0300F没问题～\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x102,
        (
            "#0100F呵呵，那我们就不客气地接受\x01",
            "您的夸奖了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB0, 4)

    label("loc_1A77")

    Jump("loc_25E8")

    label("loc_1A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1B5C")

    #C0087
    ChrTalk(
        0x8,
        (
            "改造时需要用到的『Ｕ材料』\x01",
            "好像有时也会从魔兽身上掉落呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "除此之外，似乎也能在一些\x01",
            "意想不到的地方取得……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "算啦，总之，如果得到了没见过\x01",
            "的珍奇材料，请一定要小心保存。\x01",
            "说不定可以用来改造些什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_1B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C14")

    #C0090
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔通了导力铁路，\x01",
            "也通了飞行船，或许会让人产生错觉，\x01",
            "以为全大陆都已经进入导力化时代了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "真是的，能得到如此眷顾的地区\x01",
            "难道就只有克洛斯贝尔吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CAE")

    label("loc_1C14")


    #C0092
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔的人在购买了\x01",
            "新的导力制品之后，\x01",
            "好像就会把旧东西给扔掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        "这实在是太浪费了。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "在这个世界上，还有很多地区\x01",
            "没有进入导力化阶段呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CAE")

    Jump("loc_25E8")

    label("loc_1CB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1E2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1D22")

    #C0095
    ChrTalk(
        0x8,
        (
            "我正在研发新式改造武器\x01",
            "的试制品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "请期待它的完成吧。\x01",
            "到时一定会给你们看的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E25")

    label("loc_1D22")


    #C0097
    ChrTalk(
        0x8,
        (
            "我造出了新式改造武器\x01",
            "的试制品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "嘿嘿，这东西可是很厉害的哦。\x01",
            "这可是我自己绘制设计图，\x01",
            "完全原创的武器！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "……真是的，总是改造各种制品，\x01",
            "最后不禁也想自己创造一款了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x8,
        (
            "虽然还只是试制品……\x01",
            "不过，敬请期待它的完成吧。\x01",
            "到时一定会给你们看的！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E25")

    Jump("loc_25E8")

    label("loc_1E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EA9")

    #C0101
    ChrTalk(
        0x8,
        "温蒂那家伙应该过得不错吧。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "要是她有空的话，\x01",
            "真希望她也能来这里帮忙。\x01",
            "……算了，毕竟很勉强吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F84")

    label("loc_1EA9")


    #C0103
    ChrTalk(
        0x8,
        "温蒂那家伙过得怎么样，还好吗？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x8,
        (
            "她是我当年在工房工作时的弟子，\x01",
            "技术相当不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "如果在导力商店里干烦了，\x01",
            "不如来我这里帮帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "最近这段时间，修理的委托\x01",
            "和改造工作真是很累人……\x01",
            "人手实在是不足啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1F84")

    Jump("loc_25E8")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_205E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 5)), scpexpr(EXPR_END)), "loc_2004")

    #C0107
    ChrTalk(
        0x8,
        (
            "从在财团学习的时代开始，\x01",
            "罗伯兹就是我的好友。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "话说回来，这家伙\x01",
            "二十年来真是一点都没变呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2059")

    label("loc_2004")


    #C0109
    ChrTalk(
        0x8,
        "喔，一大早就要出门啊？\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x8,
        (
            "虽然不知道你们要去哪里，\x01",
            "但一定要先做足准备工作啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2059")

    Jump("loc_25E8")

    label("loc_205E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_20BC")

    #C0111
    ChrTalk(
        0x8,
        (
            "今天的修理工作\x01",
            "有三件啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "嘁，人手严重不足啊。\x01",
            "要是能有个助手就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25E8")

    label("loc_20BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_END)), "loc_2175")

    #C0113
    ChrTalk(
        0x8,
        (
            "我从以前开始就一直\x01",
            "很喜欢研究导力制品。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "最近不但做修理的工作，\x01",
            "也开始受理武器改造的委托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "嘿嘿，你们也可以\x01",
            "多来光顾啊。\x01",
            "我对自己的手艺很有自信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227C")

    label("loc_2175")


    #C0116
    ChrTalk(
        0x8,
        (
            "说起来，你们最近\x01",
            "好像很出风头啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "克洛斯贝尔时代周刊上面\x01",
            "报道的那些『警察』，\x01",
            "就是你们几个吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 5)), scpexpr(EXPR_END)), "loc_2240")

    #C0118
    ChrTalk(
        0x8,
        (
            "嘿嘿，真不愧是温蒂\x01",
            "的童年玩伴啊。\x01",
            "果然值得信赖。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0000F哈哈，多谢夸奖……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2279")

    label("loc_2240")


    #C0120
    ChrTalk(
        0x8,
        (
            "嘿嘿，全靠你们，这下平静多了。\x01",
            "真要好好谢谢你们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2279")

    SetScenarioFlags(0x6B, 4)

    label("loc_227C")

    Jump("loc_25E8")

    label("loc_2281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2363")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22F9")

    #C0121
    ChrTalk(
        0x8,
        (
            "你们几个，下次一定\x01",
            "要来光顾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "因为总会接到\x01",
            "很多修理工作，\x01",
            "所以今天已经把零件用光了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_235E")

    label("loc_22F9")


    #C0123
    ChrTalk(
        0x8,
        (
            "在旧城区生活其实也不坏呢。\x01",
            "各种废旧的二手零件都随手可得。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "好，这就去发掘寻找\x01",
            "旧零件吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_235E")

    Jump("loc_25E8")

    label("loc_2363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257B")

    #C0125
    ChrTalk(
        0x8,
        (
            "我以前在市内繁华区的\x01",
            "工房中工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "但就在去年，那里变成了一家\x01",
            "叫什么导力商店的奇怪店铺。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "我不习惯那种风格的地方，\x01",
            "就开设了这家属于自己的工房。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2573")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x101,
        (
            "#0005F哎，这么说来，\x01",
            "难道温蒂所说的\x01",
            "那位师傅就是……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "嗯……？\x01",
            "你认识温蒂吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0130
    ChrTalk(
        0x8,
        (
            "是吗，原来你就是\x01",
            "温蒂说过的那个童年玩伴啊？\x01",
            "……而且是个警察！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#0000F哈哈哈……\x01",
            "她好像和您说了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "那当然，温蒂可是我以前在工房工作时\x01",
            "收下的弟子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x8,
        (
            "嘿嘿，看起来，\x01",
            "她好像过得挺不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4E, 5)

    label("loc_2573")

    SetScenarioFlags(0x0, 0)
    Jump("loc_25E8")

    label("loc_257B")


    #C0134
    ChrTalk(
        0x8,
        (
            "你们以后要是有什么需要，\x01",
            "就请再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "今天已经把零件用光了，\x01",
            "因为平时一直都会接到\x01",
            "很多修理工作呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E8")

    Return()

    # Function_5_D41 end

    def Function_6_25E9(): pass

    label("Function_6_25E9")

    EventBegin(0x0)
    Fade(500)
    OP_68(14750, 2250, 7600, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 13750, 1000, 7200, 90)
    SetChrPos(0x102, 13650, 1000, 8000, 90)
    SetChrPos(0x103, 12500, 1000, 7200, 90)
    SetChrPos(0x104, 12400, 1000, 8000, 90)
    OP_93(0x8, 0x10E, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0136
    ChrTalk(
        0x8,
        "噢，是客人吗？\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "真抱歉，今天已经\x01",
            "把零件用光了。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "要是有什么需要，\x01",
            "请下次再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0005F那个……\x01",
            "这里是工房商店吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#0203F（进行调查……）\x02\x03",

            "#0200F资料库中并没有\x01",
            "记载这个地方……\x01",
            "似乎是没有经营许可证呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "哈哈哈，确实还没有\x01",
            "递交申请呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "这里是我的个人工房，\x01",
            "并不是什么正式的商店。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "只是不时负责修理一些\x01",
            "坏掉的导力制品。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        "#0200F也就是所谓的修理店吧。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x104,
        (
            "#0300F哈～真不愧是克洛斯贝尔啊。\x01",
            "有各种各样的店呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#0103F不过……我觉得还是去申请\x01",
            "一份营业许可证更好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        "哈哈，说的没错。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        (
            "算了，反正今天已经要关门盘点了，\x01",
            "如果有什么需要，就请以后再来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "像导力灯坏掉之类的小事，\x01",
            "只需很便宜的价格就能解决！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 13750, 1000, 7600, 90)
    SetScenarioFlags(0x4A, 3)
    EventEnd(0x5)
    Return()

    # Function_6_25E9 end

    def Function_7_2915(): pass

    label("Function_7_2915")

    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)

    #A0150
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※与基约姆师傅对话，并选择『委托改造』后，\x01",
            "　便能调出可改造物品一览表。\x01",
            "  如果拥有改造所需的素材，就可以进行改造。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0151
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※经过改造的武器与防具都是\x01",
            "  无法在武器商会等地取得的强力装备，\x01",
            "  特别是有些武器还会附带特殊效果。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※改造所需的『素材』\x01",
            "  主要都是魔兽掉落的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Return()

    # Function_7_2915 end

    def Function_8_2A4F(): pass

    label("Function_8_2A4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7F")

    #C0153
    ChrTalk(
        0xFE,
        (
            "……嗯，简直就和新的没区别。\x01",
            "这家店的店主，手艺确实高超啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        (
            "#0000F斯克特先生\x01",
            "是这家店的常客吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        (
            "#0100F但、但这家店终究\x01",
            "也属于违法营业啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "哈哈，别说这么死板的话，\x01",
            "你们不是也来了嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "如果不懂得活用各种资源，\x01",
            "是无法胜任克洛斯贝尔\x01",
            "游击士这一工作的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BE8")

    label("loc_2B7F")


    #C0158
    ChrTalk(
        0xFE,
        (
            "我今天过来取之前\x01",
            "送来修理的来复枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "最近强大的魔兽\x01",
            "好像有所增多呢，\x01",
            "必须要有完善的装备才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BE8")

    TalkEnd(0xFE)
    Return()

    # Function_8_2A4F end

    def Function_9_2BEC(): pass

    label("Function_9_2BEC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2C34")

    #C0160
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "下次要是艾尼格玛坏了，\x01",
            "不如也拿到这里来修吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C34")

    TalkEnd(0xFE)
    Return()

    # Function_9_2BEC end

    def Function_10_2C38(): pass

    label("Function_10_2C38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C59")
    Call(0, 11)
    Return()

    label("loc_2C59")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF6")

    #C0161
    ChrTalk(
        0xB,
        (
            "我正在进行追加程序\x01",
            "的准备工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xB,
        (
            "毕竟算是大规模的升级啊。\x01",
            "光是各种组件的解压缩，\x01",
            "就要耗费相当多的时间呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#0200F主任，你站在柜台这里的话，\x01",
            "很容易被误认成店里的人，\x01",
            "会给客人添麻烦的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xB, 0x103, 500)
    Sleep(500)

    #C0164
    ChrTalk(
        0xB,
        (
            "抱、抱歉啊，缇欧！\x01",
            "因为这家店里太暗了嘛！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        (
            "#0106F（缇欧……不要\x01",
            "  欺负主任先生啦。）\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        "#0203F（不好意思，已经成习惯了……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E74")

    label("loc_2DF6")


    #C0167
    ChrTalk(
        0xB,
        (
            "追加程序的准备工作\x01",
            "就由我来完成，\x01",
            "不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xB,
        (
            "如果你们拿到素材了，\x01",
            "就去和基约姆说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xB,
        (
            "他应该正在做\x01",
            "改造的准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E74")

    Jump("loc_2FCA")

    label("loc_2E79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2EC6")

    #C0170
    ChrTalk(
        0xB,
        "呵呵，准备已经完全就绪啦。\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xB,
        (
            "必要的工具已经\x01",
            "都拿来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCA")

    label("loc_2EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F30")

    #C0172
    ChrTalk(
        0xB,
        (
            "我和基约姆可是老朋友了，\x01",
            "经常会进行联络。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        (
            "哈哈哈，但我都不知道\x01",
            "他开了间修理店呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCA")

    label("loc_2F30")


    #C0174
    ChrTalk(
        0xB,
        (
            "啊，缇欧，\x01",
            "传感器的状况如何啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        "要不要我给你调整一下……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            "#0200F不必了，\x01",
            "还是我自己来做更节省时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "（打击）……\x01",
            "说、说得也是啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2FCA")

    TalkEnd(0xB)
    Return()

    # Function_10_2C38 end

    def Function_11_2FCE(): pass

    label("Function_11_2FCE")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(510, 1000, 6090, 0)
    MoveCamera(42, 23, 0, 0)
    OP_6E(320, 0)
    SetCameraDistance(28680, 0)
    SetChrPos(0x101, 380, 0, 4670, 0)
    SetChrPos(0x102, -230, 0, 3500, 0)
    SetChrPos(0x103, -830, 0, 4330, 0)
    SetChrPos(0x104, 1200, 0, 4160, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3080")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 780, 0, 2600, 0)

    label("loc_3080")

    SetChrPos(0x8, 1000, 0, 7430, 270)
    SetChrPos(0xB, -400, 0, 7430, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0178
    ChrTalk(
        0x8,
        (
            "#11P噢，来了啊。\x01",
            "特别任务支援科的各位！\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#12P#0000F您好，我们是为了\x01",
            "受理支援请求而来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        (
            "#12P#0300F你好啊～修理店的大叔，\x01",
            "平时总是承蒙你的照顾。\x02\x03",

            "#0305F哎～那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x13B, 0x1F4)
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    def lambda_319B():
        OP_95(0xFE, -870, 0, 5820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_319B)

    #C0181
    ChrTalk(
        0xB,
        "#5P啊，缇欧，好久不见了啊～！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xB,
        (
            "#5P最近身体怎么样啊？\x01",
            "没有感冒什么的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#6P#0205F主任，您也来这里了啊。\x02\x03",

            "#0211F话说回来，好像\x01",
            "也并没有很久不见呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#12P#0109F啊哈哈……\x01",
            "（缇欧和这位主任之间的关系\x01",
            "  好像有些微妙呢。）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_355A")

    #C0185
    ChrTalk(
        0x10A,
        (
            "#12P#0603F爱普斯泰恩财团的罗伯兹氏……\x01",
            "还有原财团技师基约姆氏吗。\x02\x03",

            "#0600F嗯，大致情况我已经了解了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_336D():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_336D)

    def lambda_337A():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_337A)

    def lambda_3387():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3387)

    def lambda_3394():
        TurnDirection(0xFE, 0x10A, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3394)
    Sleep(300)

    #C0186
    ChrTalk(
        0x101,
        "#11P#0005F嗯……？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x10A,
        (
            "#12P#0600F我到外面去等，\x01",
            "你们把事情办完之后再出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x10A, 300, 0, -1400, 2000, 0x0)
    OP_95(0x10A, 300, 0, -3210, 2000, 0x0)

    #C0188
    ChrTalk(
        0xB,
        (
            "#5P那个人是缇欧的上司吗？\x01",
            "看起来好像是个相当精干的人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#6P#0203F呼，他是达德利警官，\x01",
            "搜查一科的人。出于某些原因，\x01",
            "现在和我们一起行动。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34B4():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34B4)

    def lambda_34C1():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_34C1)

    def lambda_34CE():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34CE)

    def lambda_34DB():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34DB)
    Sleep(500)

    #C0190
    ChrTalk(
        0x102,
        (
            "#12P#0105F话说回来……两位刚才\x01",
            "好像正在谈话呢，\x01",
            "我们是不是打扰到了？\x02\x03",

            "#0100F我们先回避一下\x01",
            "也没关系的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35CD")

    label("loc_355A")

    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
    Sleep(300)

    #C0191
    ChrTalk(
        0x102,
        (
            "#12P#0105F两位刚才好像正在谈话呢，\x01",
            "我们是不是打扰到了？\x02\x03",

            "#0100F我们先回避一下\x01",
            "也没关系的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35CD")


    #C0192
    ChrTalk(
        0x8,
        (
            "#11P不不，没必要回避。\x01",
            "其实，这次的委托是\x01",
            "罗伯兹这家伙提出的……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    TurnDirection(0xB, 0x8, 500)
    Sleep(500)
    OP_95(0xB, -210, 0, 6430, 5000, 0x0)

    #C0193
    ChrTalk(
        0xB,
        (
            "#5P哇啊啊，基约姆！？\x01",
            "不是让你保密……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        "#6P#0211F（瞪……）\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xB, 0x103, 500)
    Sleep(300)

    #C0195
    ChrTalk(
        0xB,
        (
            "#5P别、别误会啊，\x01",
            "并不是什么\x01",
            "见不得人的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "#5P那个，关于这点，\x01",
            "其实是有深刻原因的！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#12P#0005F深刻原因……吗？\x02\x03",

            "#0001F看起来，好像也和委托有关啊。\x01",
            "可以告诉我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        "#5P也、也是啊，那我就说吧。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xB,
        "#5P其实是财团那边的事情。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0200
    ChrTalk(
        0xB,
        (
            "#5P我想各位应该也知道，\x01",
            "缇欧正在克洛斯贝尔进行\x01",
            "魔导杖实战数据的收集工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xB,
        (
            "#5P而我们会以缇欧提交的数据\x01",
            "为参考，不断改良魔导杖\x01",
            "的性能哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xB,
        (
            "#5P在此过程中，\x01",
            "我们终于取得了重大进展，\x01",
            "可以开启魔导杖的新功能了。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#12P#0005F开启新功能……\x01",
            "那是怎么一回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        (
            "#12P#0305F就是说阿缇会增加\x01",
            "一些新的便利功能吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)
    Sleep(200)

    #C0205
    ChrTalk(
        0x103,
        (
            "#6P#0203F兰迪前辈，我本来就没有\x01",
            "什么便利的功能……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_39D7():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_39D7)

    def lambda_39E4():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39E4)

    def lambda_39F1():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39F1)
    Sleep(400)

    #C0206
    ChrTalk(
        0x103,
        (
            "#6P#0200F带有好几个未开启功能的\x01",
            "是这根魔导杖。\x02\x03",

            "#0203F但由于一直都没有可以\x01",
            "使它稳定启动的程序，所以……\x02\x03",

            "#0200F而现在，那程序\x01",
            "似乎是有了进展，\x01",
            "我想大概就是这样吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x102,
        "#12P#0105F究竟是什么样的功能呢？\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        (
            "#5P这个嘛，一言以蔽之，\x01",
            "大概就是关系到新战技的功能吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B0C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B0C)

    def lambda_3B19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B19)

    def lambda_3B26():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B26)

    def lambda_3B33():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B33)
    Sleep(300)

    #C0209
    ChrTalk(
        0xB,
        (
            "#5P搭配新程序，应该就可以使用\x01",
            "输出功率较高的新战技了。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "#11P关于那个，我已经看过资料了，\x01",
            "好像是威力相当强大的战技呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#11P但以魔导杖现在的配置，\x01",
            "要发动它还是太过危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#11P似乎仍然需要\x01",
            "改良一下杖身等硬件呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#12P#0003F听、听起来好像很厉害啊……\x02\x03",

            "#0005F改造之后，缇欧就能\x01",
            "使用那个新战技了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x8,
        (
            "#11P不，因为还存在着\x01",
            "一个麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x8,
        (
            "#11P财团方面准备的\x01",
            "追加程序和组件的运送\x01",
            "延迟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "#11P因为那边出了一些差错，\x01",
            "所以大概要晚上一周左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        "#5P所谓的委托，就是关于这件事的。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "#5P一直这么等下去的话，\x01",
            "我想缇欧也会很困扰……\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "#5P所以我们总要\x01",
            "尽量做点什么才行！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x104,
        (
            "#12P#0300F哦哦，所以委托名称\x01",
            "才是『新功能的开发』啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        "#12P#0100F总算听明白了呢。\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x103,
        (
            "#6P#0203F……虽然晚一周\x01",
            "倒也算不上什么困扰……\x02\x03",

            "#0200F不过我确实也想早日体验一下，\x01",
            "毕竟这个程序也算是\x01",
            "我这段时期的努力成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x101,
        (
            "#12P#0000F说得也是啊……\x01",
            "如果缇欧的战斗力得到提升，\x01",
            "我们的探索工作也会变得更轻松。\x02\x03",

            "#0005F不过，主任先生，既然财团那边\x01",
            "的发送会有所延迟，那不就无计可施了吗？\x01",
            "莫非还有其它方法？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_63(0xB, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    #C0224
    ChrTalk(
        0xB,
        (
            "#5P呵呵，问得非常好。\x01",
            "自然是有的！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)

    #C0225
    ChrTalk(
        0xB,
        (
            "#5P其实，关于这段追加程序，\x01",
            "我可以以事先取得的资料为基础，\x01",
            "在这里进行再编写。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xB,
        (
            "#5P接下来的问题就是\x01",
            "魔导杖所需要的组件……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        "#11P这里就该轮到我登场了。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "#11P修理和改造可是我的专长。\x01",
            "因为已经拿到资料了，所以只要材料一到，\x01",
            "我马上就能制造出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#12P#0000F原来如此……只要再把素材准备好，\x01",
            "就能够进行升级改造了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_40CD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_40CD)

    def lambda_40DA():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40DA)

    def lambda_40E7():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40E7)

    def lambda_40F4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40F4)
    Sleep(500)

    #C0230
    ChrTalk(
        0x101,
        (
            "#11P#0000F各位，为了缇欧，\x01",
            "我们也来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x102,
        "#12P#0100F嗯，我也赞成。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x104,
        "#12P#0300F当然没异议。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#6P#0205F这样没问题吗……？\x01",
            "也许会耽误\x01",
            "调查工作的进度……\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        (
            "#12P#0309F哈哈，只不过是找材料而已吧？\x01",
            "并不是什么大不了的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x102,
        (
            "#12P#0100F没错没错，罗伊德刚才也说过了，\x01",
            "如果能提升战斗力，我们今后的\x01",
            "探索工作也会变得更加轻松。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        (
            "#11P#0000F嗯，所以没有不接受的理由啊。\x02\x03",

            "……缇欧，怎么样？\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#6P#0203F我明白了，\x01",
            "那就拜托大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        "#12P#0300F好，那就这么决定了！\x02",
    )

    CloseMessageWindow()

    def lambda_42E7():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42E7)

    def lambda_42F4():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42F4)

    def lambda_4301():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4301)

    def lambda_430E():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_430E)
    Sleep(300)

    #C0239
    ChrTalk(
        0x103,
        (
            "#6P#0200F基约姆师傅，具体\x01",
            "需要些什么材料呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "#11P啊，是一种名叫『Ｔ材料』\x01",
            "的特殊素材……\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "#11P这个东西在克洛斯贝尔\x01",
            "好像很难取得。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        (
            "#12P#0003F是吗……\x01",
            "算了，我们先去找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xB,
        (
            "#5P嗯，只需要一个就够了，\x01",
            "那就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xB,
        (
            "#5P如果收集到了材料，\x01",
            "就去和基约姆说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xB,
        (
            "#5P我们这里会先进行\x01",
            "改造的准备工作的！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        "#6P#0200F拜托了。\x02",
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        "#12P#0100F那么，我们走吧。\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x104,
        "#12P#0300F噢，我们加油吧！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【魔导杖的新功能开发】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(115090, 1500, 58830, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, -200, 0, 3820, 0)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    SetChrPos(0xB, 5620, 0, 5330, 270)
    ClearChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45A4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_45A4")

    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_29(0x31, 0x1, 0x0)
    SetScenarioFlags(0x4E, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_2FCE end

    def Function_12_45C5(): pass

    label("Function_12_45C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0x8)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(13800, 2300, 7800, 0)
    MoveCamera(61, 26, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(24880, 0)
    SetChrPos(0x101, 12800, 1000, 7200, 90)
    SetChrPos(0x102, 12800, 1000, 8100, 90)
    SetChrPos(0x103, 12800, 1000, 9000, 90)
    SetChrPos(0x104, 12800, 1000, 6300, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_467A")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x10A, 12110, 1000, 9870, 90)

    label("loc_467A")

    SetChrPos(0x8, 15200, 1000, 8900, 225)
    SetChrPos(0xB, 15240, 1000, 7610, 270)
    OP_65(0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    FadeToBright(1000, 0)
    OP_0D()

    #C0250
    ChrTalk(
        0x8,
        (
            "#5P材料确认完毕，\x01",
            "我这边没问题了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BF6")

    #C0251
    ChrTalk(
        0x10A,
        (
            "#6P#0604F武器的改造吗……\x01",
            "似乎能见识到很罕见的技术啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_473E():

        label("loc_473E")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_473E")

    QueueWorkItem2(0x104, 1, lambda_473E)
    Sleep(50)

    def lambda_4753():

        label("loc_4753")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4753")

    QueueWorkItem2(0x101, 1, lambda_4753)

    def lambda_4765():

        label("loc_4765")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4765")

    QueueWorkItem2(0x102, 1, lambda_4765)

    def lambda_4777():

        label("loc_4777")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4777")

    QueueWorkItem2(0x103, 1, lambda_4777)

    def lambda_4789():

        label("loc_4789")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_4789")

    QueueWorkItem2(0xB, 1, lambda_4789)

    def lambda_479B():

        label("loc_479B")

        TurnDirection(0xFE, 0x10A, 400)
        Yield()
        Jump("loc_479B")

    QueueWorkItem2(0x8, 1, lambda_479B)
    Sleep(400)

    #C0252
    ChrTalk(
        0x104,
        (
            "#12P#0300F噢，达德利大叔果然也对\x01",
            "这些东西感兴趣啊？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x104, 500)
    Sleep(300)

    #C0253
    ChrTalk(
        0x10A,
        (
            "#6P#0601F……白痴，我刚刚是在讽刺！\x01",
            "在如此繁忙的时期，你们竟然\x01",
            "还有闲心干这种事情！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0254
    ChrTalk(
        0x102,
        (
            "#12P#0103F对、对不起，\x01",
            "您说的也有道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#6P#0200F没有注意到现在时间紧迫，\x01",
            "真是对不起。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(500)

    #C0256
    ChrTalk(
        0x10A,
        (
            "#6P#0603F哼……\x01",
            "但是，你们也有你们自己的事情，\x01",
            "我可以理解。\x02\x03",

            "#0601F……我先回避一下。\x01",
            "尽快把事情解决，\x01",
            "然后回来继续调查工作！\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        "#12P#0005F是、是，明白了。\x02",
    )

    CloseMessageWindow()
    OP_95(0x10A, 7200, 0, 9870, 2000, 0x0)
    Sleep(500)

    #C0258
    ChrTalk(
        0xB,
        "#11P那就是搜查一科的人吗……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0x8, 0x1)

    def lambda_4A0E():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A0E)

    def lambda_4A1B():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4A1B)

    def lambda_4A28():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A28)

    def lambda_4A35():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A35)
    OP_93(0x8, 0xE1, 0x190)
    Sleep(400)

    #C0259
    ChrTalk(
        0xB,
        (
            "#11P缇欧，不然还是算了吧？\x01",
            "你们现在好像挺忙的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x103,
        (
            "#6P#0203F不，请不必在意，\x01",
            "达德利警官平时\x01",
            "一直都是那样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        (
            "#6P#0100F而且他也表示理解了。\x01",
            "我想，现在还是应该\x01",
            "尽快开始改造比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "#5P说得也是啊，\x01",
            "那就赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xB,
        (
            "#11P好，我要用\x01",
            "最快速度来完成它。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0264
    ChrTalk(
        0xB,
        (
            "#11P这么一想，\x01",
            "好像一下就充满干劲了。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xB,
        (
            "#11P呵呵，真是期待啊～\x01",
            "缇欧手持新型魔导杖的飒爽英姿，\x01",
            "仿佛已经浮现在眼前了呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C83")

    label("loc_4BF6")


    #C0266
    ChrTalk(
        0xB,
        "#11P好，已经准备万全了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)

    #C0267
    ChrTalk(
        0xB,
        (
            "#11P呵呵，真是期待啊～\x01",
            "缇欧手持新型魔导杖的飒爽英姿，\x01",
            "仿佛已经浮现在眼前了呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C83")


    #C0268
    ChrTalk(
        0x103,
        (
            "#6P#0211F……主任。\x02\x03",

            "魔导杖要是改造失败，出现故障\x01",
            "而导致无法使用的话，\x01",
            "我可是会恨你的哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0269
    ChrTalk(
        0xB,
        (
            "#11P怎、怎么会……\x01",
            "竟然要被缇欧憎恨一生……\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xB,
        (
            "#11P呜哇～……！\x01",
            "我、我为什么要经受如此残酷的事情……！\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#12P#0006F主任先生，现在还没发生\x01",
            "任何情况呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xB, 500)
    Sleep(300)

    #C0272
    ChrTalk(
        0x8,
        "#5P罗伯兹，清醒一点。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0273
    ChrTalk(
        0xB,
        "#11P哈……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x190)
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    #C0274
    ChrTalk(
        0xB,
        (
            "#11P抱、抱歉，\x01",
            "那就赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xB,
        (
            "#11P支援科的各位，\x01",
            "请你们稍等片刻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#6P#0100F嗯，那我们就\x01",
            "在一旁参观学习了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人就这么\x01",
            "等了三十分钟左右。\x02",
        )
    )

    CloseMessageWindow()

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "虽然对具体过程不甚了解，\x01",
            "但魔导杖的改造工作\x01",
            "似乎进展得非常顺利。\x02",
        )
    )

    CloseMessageWindow()

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x103, 250, 0, 6400, 255)
    SetChrPos(0x8, -820, 0, 8210, 166)
    SetChrPos(0xB, 1100, 0, 8510, 211)
    SetChrPos(0x101, -2090, 0, 2600, 31)
    SetChrPos(0x102, -880, 0, 2190, 346)
    SetChrPos(0x104, -2730, 0, 3880, 31)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4FAA")
    SetChrPos(0x10A, 230, 0, -1850, 38)
    SetChrFlags(0x10A, 0x80)

    label("loc_4FAA")

    OP_68(-520, 1600, 5910, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16770, 0)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00257.itc", 0x1F)
    LoadChrToIndex("chr/ch0025A.itc", 0x20)
    LoadEffect(0x0, "battle\\cr002403.eff")
    LoadEffect(0x1, "battle\\cr002401.eff")
    SetChrChipByIndex(0x103, 0x1E)
    BeginChrThread(0x103, 0, 0, 13)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(3000)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    OP_A0(0x103, 1500, 0x0, 0x2)
    Sleep(300)
    OP_A0(0x103, 1500, 0x2, 0x3)
    Sound(279, 0, 100, 0)
    SetChrSubChip(0x103, 0x4)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0x103, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(363, 0, 100, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0x103, 0xC0, 200, 700, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(274, 0, 100, 0)
    Sleep(100)
    Fade(300)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(2500)
    PlayEffect(0x1, 0xFF, 0x103, 0xC0, 200, 550, 850, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(280, 0, 90, 0)
    Sound(323, 0, 90, 0)
    Sleep(4500)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x103)
    Sleep(1000)
    Fade(300)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 0, 0, 13)
    OP_0D()
    Sleep(1000)

    #C0280
    ChrTalk(
        0x8,
        (
            "#5P情况如何？\x01",
            "调整方面大概已经没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        (
            "#12P#0203F这个嘛……\x02\x03",

            "#0200F因为基本程序已经更新了，\x01",
            "所以稍微有点不太适应，\x01",
            "不过感觉并不差。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xB,
        (
            "#11P肯定是重心控制问题，\x01",
            "我想缇欧很快就会习惯的。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xB,
        (
            "#11P想换用其它魔导杖的话，\x01",
            "就利用永世系统把\x01",
            "新程序复制过去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xB,
        (
            "#11P另外也不要忘记把可装卸式\x01",
            "的新组件装上去哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x103,
        "#12P#0200F了解。\x02",
    )

    CloseMessageWindow()
    OP_68(-630, 1000, 5470, 2200)
    MoveCamera(67, 26, 0, 2200)
    SetCameraDistance(20230, 2200)
    OP_6F(0x79)

    #C0286
    ChrTalk(
        0x104,
        (
            "#6P#0305F喂，罗伊德……\x01",
            "看起来好像非常顺利啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0005F呼……以前都不知道魔导杖\x01",
            "的杖尖还可以开启啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x102,
        (
            "#12P#0100F潜藏在其中的各种新功能，\x01",
            "似乎比看上去还要多呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0289
    ChrTalk(
        0x102,
        (
            "#12P#0105F……对了。\x01",
            "缇欧，感觉怎么样呢？\x02\x03",

            "#0100F之前说过的那个新战技，\x01",
            "已经可以顺利发动了吗？\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    EndChrThread(0x103, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    OP_0D()
    Sleep(300)

    def lambda_541C():
        OP_95(0xFE, -990, 0, 4810, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_541C)
    Sleep(300)

    def lambda_5439():
        OP_95(0xFE, -1390, 0, 6630, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5439)

    def lambda_5453():
        OP_95(0xFE, 250, 0, 6400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5453)
    Sleep(2000)
    OP_93(0x8, 0xB4, 0x1F4)

    #C0290
    ChrTalk(
        0x103,
        (
            "#11P#0200F嗯，改造已经全部结束了。\x01",
            "至于性能方面，似乎也能发挥出\x01",
            "预期的威力。\x02\x03",

            "#0203F可以发射绝对零度的反能源弹，其名为\x01",
            "──『绝对零度』。\x02\x03",

            "#0200F虽然无法频繁使用，\x01",
            "但在重要的战斗中\x01",
            "应该能发挥些作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        "#12P#0000F是吗……那真是令人信心百倍呢。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x104,
        (
            "#6P#0300F哈哈，光是听上去就觉得很厉害呢，\x01",
            "很期待实战效果啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        (
            "#12P#0100F是啊，这次真是\x01",
            "承蒙两位的帮助了。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x103,
        "#11P#0200F嗯，是的。\x02",
    )

    CloseMessageWindow()

    def lambda_55FF():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_55FF)

    def lambda_560C():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_560C)
    Sleep(300)

    #C0295
    ChrTalk(
        0x103,
        (
            "#11P#0200F主任、基约姆师傅，\x01",
            "非常感谢两位。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x101,
        "#12P#0000F多谢两位费心了。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "#5P嘿嘿，没什么大不了的，\x01",
            "用不着放在心上。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xB,
        (
            "#11P啊，不必道谢啦，\x01",
            "应该是我表示感谢才对呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "#11P还有……能顺利改造成功，\x01",
            "真是太好了啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xB,
        (
            "#11P一开始我都做好了被拒绝的准备呢……\x01",
            "嗯嗯，以基约姆的名义提出委托，\x01",
            "果然是正确的决定啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(14)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x103, 0xB, 500)
    TurnDirection(0x101, 0xB, 500)
    Sleep(200)

    #C0301
    ChrTalk(
        0x103,
        "#6P#0211F……（瞪…………）\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0xB,
        (
            "#11P不不，没什么啦，\x01",
            "我什么都没说。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x1F4)
    Sleep(200)

    #C0303
    ChrTalk(
        0xB,
        (
            "#11P噢噢噢，都已经这么晚了啊……\x01",
            "那我就先告辞了！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xE1, 0x1F4)
    Sleep(200)

    #C0304
    ChrTalk(
        0xB,
        (
            "#11P缇欧，一定要让魔导杖在实战中发挥作用哦。\x01",
            "那、那么，我先走了！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58D2():

        label("loc_58D2")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_58D2")

    QueueWorkItem2(0x101, 1, lambda_58D2)

    def lambda_58E4():

        label("loc_58E4")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_58E4")

    QueueWorkItem2(0x102, 1, lambda_58E4)

    def lambda_58F6():

        label("loc_58F6")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_58F6")

    QueueWorkItem2(0x104, 1, lambda_58F6)

    def lambda_5908():

        label("loc_5908")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_5908")

    QueueWorkItem2(0x103, 1, lambda_5908)

    def lambda_591A():

        label("loc_591A")

        TurnDirection(0xFE, 0xB, 300)
        Yield()
        Jump("loc_591A")

    QueueWorkItem2(0x8, 1, lambda_591A)

    def lambda_592C():
        OP_95(0xFE, 1200, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_592C)
    WaitChrThread(0xB, 1)

    def lambda_594A():
        OP_95(0xFE, 0, 0, 1500, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_594A)
    WaitChrThread(0xB, 1)

    def lambda_5968():
        OP_95(0xFE, 0, 0, -2000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_5968)
    Sound(105, 0, 100, 0)

    def lambda_5988():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5988)
    WaitChrThread(0xB, 1)
    SetChrFlags(0xB, 0x80)
    Sleep(1100)

    #C0305
    ChrTalk(
        0x103,
        (
            "#6P#0206F呼……\x01",
            "虽然不是什么坏人，可是……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)

    #C0306
    ChrTalk(
        0x101,
        (
            "#12P#0000F呵呵，他确实是\x01",
            "发自内心地关心缇欧，\x01",
            "这点是有目共睹的。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x8,
        (
            "#5P那家伙这种过度保护的毛病，\x01",
            "真是治不好了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5E64")
    ClearChrFlags(0x10A, 0x80)

    #N0308
    NpcTalk(
        0x10A,
        "男人的声音",
        "#3P好像已经把事情办完了啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_68(-380, 1000, 4920, 3000)
    MoveCamera(14, 20, 0, 3000)

    def lambda_5B1D():

        label("loc_5B1D")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_5B1D")

    QueueWorkItem2(0x101, 1, lambda_5B1D)

    def lambda_5B2F():

        label("loc_5B2F")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_5B2F")

    QueueWorkItem2(0x102, 1, lambda_5B2F)

    def lambda_5B41():

        label("loc_5B41")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_5B41")

    QueueWorkItem2(0x104, 1, lambda_5B41)

    def lambda_5B53():

        label("loc_5B53")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_5B53")

    QueueWorkItem2(0x103, 1, lambda_5B53)

    def lambda_5B65():

        label("loc_5B65")

        TurnDirection(0xFE, 0x10A, 300)
        Yield()
        Jump("loc_5B65")

    QueueWorkItem2(0x8, 1, lambda_5B65)
    OP_95(0x10A, 730, 0, 2370, 2000, 0x0)
    OP_93(0x10A, 0x13B, 0x1F4)
    Sleep(200)
    OP_6F(0x79)

    #C0309
    ChrTalk(
        0x10A,
        (
            "#12P#0600F魔导杖的改造工作\x01",
            "成功了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x103,
        "#11P#0200F嗯，那是自然。\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#6P#0000F耽误了这么多时间，\x01",
            "实在是抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x10A,
        (
            "#12P#0603F哼，真是的。\x01",
            "竟然在如此紧急的时期\x01",
            "去维修武器……\x02\x03",

            "#0601F算了，既然已经完成了，\x01",
            "就赶快重返搜索任务。\x02\x03",

            "那边的情况十分紧急，\x01",
            "已经是刻不容缓了。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#6P#0000F明白了，\x01",
            "我们马上出发吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)

    def lambda_5CE6():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CE6)

    def lambda_5CF3():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CF3)

    def lambda_5D00():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5D00)

    def lambda_5D0D():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5D0D)
    Sleep(400)

    #C0314
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么，基约姆师傅，\x01",
            "我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#12P#0100F多谢您的帮忙。\x01",
            "如果以后再有什么事情，\x01",
            "还请多多关照啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x8,
        (
            "#5P哦，虽然不知道还能帮上什么，\x01",
            "不过我肯定会尽力而为！\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x8,
        (
            "#5P这位先生是叫达德利吧？\x01",
            "你也一样啊，有兴趣的话，\x01",
            "欢迎前来光顾啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x10A,
        (
            "#12P#0604F哼……也好，\x01",
            "我会考虑的。\x02\x03",

            "#0600F那么，以后有机会再见吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F79")

    label("loc_5E64")


    #C0319
    ChrTalk(
        0x8,
        (
            "#5P好了，这样一来，\x01",
            "暂时应该是没什么事了吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_5E9E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E9E)

    def lambda_5EAB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EAB)

    def lambda_5EB8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5EB8)

    def lambda_5EC5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5EC5)
    Sleep(300)

    #C0320
    ChrTalk(
        0x8,
        (
            "#5P嗯，那我差不多\x01",
            "也该回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x8,
        (
            "#5P那把魔导杖，\x01",
            "一定要善加使用啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x103,
        "#12P#0200F嗯，那是一定的。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x102,
        (
            "#12P#0100F以后要是再有什么事情，\x01",
            "还请您多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F79")

    AddCraft(0x2, 0xAE)
    SubItemNumber(0x397, 1)
    OP_50(0x66, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【魔导杖的新功能开发】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, 4190, 180)
    SetChrPos(0x8, 15240, 1000, 7610, 90)
    OP_4C(0x8, 0xFF)
    SetChrChipByIndex(0x103, 0xFF)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_603D")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_603D")

    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x1, 0x1)
    SetScenarioFlags(0x0, 4)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_45C5 end

    def Function_13_6051(): pass

    label("Function_13_6051")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6068")
    OP_A0(0x103, 1200, 0x0, 0x4)
    Jump("Function_13_6051")

    label("loc_6068")

    Return()

    # Function_13_6051 end

    SaveToFile()

Try(main)
