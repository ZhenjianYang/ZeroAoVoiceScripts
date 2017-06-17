from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0530.bin",                # FileName
        "t0530",                    # MapName
        "t0530",                    # Location
        0x0040,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "贝卡莱",                 # 1
        "奇米",                   # 2
        "哈罗德",                 # 3
        "艾丝蒂尔",               # 4
        "约修亚",                 # 5
        "游客鲁缇娜",             # 6
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch22700.itc",                   # 02
        "chr/ch09300.itc",                   # 03
        "chr/ch00600.itc",                   # 04
        "chr/ch00700.itc",                   # 05
        "chr/ch34300.itc",                   # 06
    ))

    DeclNpc(-129,    0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4530,   0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4670,    0,       1279,    135,  405,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4409,    0,       -839,    0,    405,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5500,    0,       -180,    315,  405,  0x0, 0,   5,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(5539,    0,       750,     45,   389,  0x0, 0,   6,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-40,     0,       2120,    1000,    -130,    1500,    3640,    0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_1A4",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_2A4",          # 02, 2
        "Function_3_2D8",          # 03, 3
        "Function_4_2DC",          # 04, 4
        "Function_5_F28",          # 05, 5
        "Function_6_14D4",         # 06, 6
        "Function_7_15A9",         # 07, 7
        "Function_8_1656",         # 08, 8
        "Function_9_1893",         # 09, 9
    ))


    def Function_0_1A4(): pass

    label("Function_0_1A4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E4"),
        (1, "loc_1F0"),
        (2, "loc_1FC"),
        (3, "loc_208"),
        (4, "loc_214"),
        (5, "loc_220"),
        (6, "loc_22C"),
        (SWITCH_DEFAULT, "loc_238"),
    )


    label("loc_1E4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1F0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_1FC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_208")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_214")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_220")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_22C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_238")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_244")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_244")

    label("loc_25B")

    Return()

    # Function_0_1A4 end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_290")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_290")
    TurnDirection(0xA, 0xB, 0)
    TurnDirection(0xC, 0xB, 0)

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A3")
    ClearChrFlags(0xD, 0x80)

    label("loc_2A3")

    Return()

    # Function_1_25C end

    def Function_2_2A4(): pass

    label("Function_2_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_2D7")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D7")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_2D7")

    Return()

    # Function_2_2A4 end

    def Function_3_2D8(): pass

    label("Function_3_2D8")

    Call(0, 4)
    Return()

    # Function_3_2D8 end

    def Function_4_2DC(): pass

    label("Function_4_2DC")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F24")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_339")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_389")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_358")
    OP_AF(0x56)
    Jump("loc_37A")

    label("loc_358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_368")
    OP_AF(0x55)
    Jump("loc_37A")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_378")
    OP_AF(0x57)
    Jump("loc_37A")

    label("loc_378")

    OP_AF(0x55)

    label("loc_37A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F1F")

    label("loc_389")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39D")
    Jump("loc_F1F")

    label("loc_39D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45F")

    #C0001
    ChrTalk(
        0x8,
        (
            "又是被魔兽袭击，又是失踪……\x01",
            "矿工们还真是不幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "霍夫曼那家伙，在这种时候\x01",
            "才更应该保持镇定啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "这正是矿山长发挥能力的时候哦。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4D8")

    label("loc_45F")


    #C0004
    ChrTalk(
        0x8,
        (
            "……我要不是因为脚受了伤，\x01",
            "也可以去帮矿工们的忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "不，矿山长已经是霍夫曼了。\x01",
            "他们一定能够\x01",
            "自己解决问题的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8")

    Jump("loc_F1F")

    label("loc_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_55E")

    #C0006
    ChrTalk(
        0x8,
        (
            "冈兹那家伙，竟然让镇长\x01",
            "亲自去接他，真是太不像样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "听说是赢了大笔米拉，\x01",
            "就变得财大气粗了啊。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_5E3")

    #C0008
    ChrTalk(
        0x8,
        (
            "冈兹那家伙，把薪水\x01",
            "几乎都贡献给『巴鲁卡』了，\x01",
            "在我这里赊了很多账。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "那家伙，要是不平安回来，\x01",
            "我可和他没完啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA")
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 500)

    #C0010
    ChrTalk(
        0x8,
        (
            "……奇米！\x01",
            "不好意思，能不能帮我从架子上把那个拿来？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0011
    ChrTalk(
        0x9,
        "好～¤是这个吧～\x02",
    )

    CloseMessageWindow()

    def lambda_65C():
        TurnDirection(0xFE, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_65C)

    def lambda_669():
        OP_93(0xFE, 0x140, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_669)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    #C0012
    ChrTalk(
        0x8,
        (
            "……把你们晾在一边，不好意思啊。\x01",
            "有什么需要吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_6F8")

    label("loc_6BA")


    #C0013
    ChrTalk(
        0x8,
        (
            "我家的女儿\x01",
            "又机灵又聪明呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "还好她像我啊，\x01",
            "哇哈哈。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F8")

    Jump("loc_F1F")

    label("loc_6FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_78E")

    #C0015
    ChrTalk(
        0x8,
        (
            "我一看到矿工们偷懒，\x01",
            "就莫名地生气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "我当矿工的时候，\x01",
            "那可是废寝忘食……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……不好不好，\x01",
            "怎么可以对无关人员说教呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7DF")

    #C0018
    ChrTalk(
        0x8,
        (
            "……稍后不如\x01",
            "去趟『红砖亭』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "我有时也会想放松一下嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_7DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_87A")

    #C0020
    ChrTalk(
        0x8,
        (
            "魔兽通常都非常喜欢七耀石。\x01",
            "打倒魔兽之所以会掉耀晶片，\x01",
            "就是因为这个道理。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "我们镇的矿山里聚集着魔兽，\x01",
            "也是因为这里是七耀石的产地吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1F")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_9C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")

    #C0022
    ChrTalk(
        0x8,
        (
            "你们几个，\x01",
            "是克洛斯贝尔市警察局的吧？\x01",
            "连这种地方都要巡逻，真是辛苦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "……任何人都有过从事底层工作的时代。\x01",
            "我当年也是扛着镐，\x01",
            "在矿山里工作的。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "我觉得，在这种时候，是选择自暴自弃，\x01",
            "还是努力奋斗，往往会直接关系到\x01",
            "将来能否成大事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9C0")

    label("loc_98B")


    #C0025
    ChrTalk(
        0x8,
        (
            "任何人都要从最基本的底层工作干起，\x01",
            "加油努力吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C0")

    Jump("loc_F1F")

    label("loc_9C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_A76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1A")

    #C0026
    ChrTalk(
        0x8,
        "噢噢，有什么需要吗？！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        "爽快一些，多买点吧，嘿！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A71")

    label("loc_A1A")


    #C0028
    ChrTalk(
        0x8,
        (
            "怎么了，你们肯定是有什么需要，\x01",
            "才会进这家店的吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "爽快一些，多买点吧，嘿！\x02",
    )

    CloseMessageWindow()

    label("loc_A71")

    Jump("loc_F1F")

    label("loc_A76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_B88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")

    #C0030
    ChrTalk(
        0x8,
        (
            "和市里那些娇生惯养的人们相比，\x01",
            "哈罗德算是很不错的人才了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "虽然有点谦虚过头，\x01",
            "但也算是瑕不掩瑜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "要干商人这行，\x01",
            "还是得有点气度才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B83")

    label("loc_B26")


    #C0033
    ChrTalk(
        0x8,
        (
            "哈罗德那家伙，\x01",
            "虽然有点谦虚过头，\x01",
            "但也算是瑕不掩瑜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "难道他就不想\x01",
            "再多赚一点吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B83")

    Jump("loc_F1F")

    label("loc_B88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_CA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C10")

    #C0035
    ChrTalk(
        0x8,
        (
            "嘁，纪念庆典临近了，\x01",
            "这些家伙个个\x01",
            "都开始浮躁起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "期待庆典是可以理解，\x01",
            "但浮躁往往是受伤之源啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CA2")

    label("loc_C10")


    #C0037
    ChrTalk(
        0x8,
        (
            "期待庆典是可以理解，\x01",
            "但这些家伙个个\x01",
            "都开始浮躁起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "为了避免由于太过兴奋而不小心受伤，\x01",
            "导致最后去不成纪念庆典，\x01",
            "他们都该多注意点啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA2")

    Jump("loc_F1F")

    label("loc_CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_CB5")
    Jump("loc_F1F")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7F")

    #C0039
    ChrTalk(
        0x8,
        (
            "话说，最近的这一代矿工，\x01",
            "素质真是越来越不行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "管他什么狼啊狗啊的，不过就是\x01",
            "一点小事罢了，怎么能吓成那副样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "既然是这个镇上的矿工，\x01",
            "就给我把胆子放大一点啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DF9")

    label("loc_D7F")


    #C0042
    ChrTalk(
        0x8,
        (
            "管他什么狼啊狗啊的，不过就是\x01",
            "一点小事罢了，怎么能吓成那副样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "既然是这个镇上的矿工，\x01",
            "就给我把胆子放大一点啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DF9")

    Jump("loc_F1F")

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_F1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E20")
    SetScenarioFlags(0x66, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC3")

    #C0044
    ChrTalk(
        0x8,
        (
            "最近好像有什么魔兽\x01",
            "在镇上晃来晃去，真让人烦躁。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "有魔兽来袭，\x01",
            "甚至还有人受了伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "要是我家的奇米有个三长两短，\x01",
            "我可绝对饶不了它们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1F")

    label("loc_EC3")


    #C0047
    ChrTalk(
        0x8,
        (
            "有魔兽来袭，\x01",
            "甚至还有人受了伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "要是我家的奇米有个三长两短，\x01",
            "我可绝对饶不了它们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1F")

    Jump("loc_2E9")

    label("loc_F24")

    TalkEnd(0x8)
    Return()

    # Function_4_2DC end

    def Function_5_F28(): pass

    label("Function_5_F28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FCB")

    #C0049
    ChrTalk(
        0xFE,
        (
            "奇米等下要去给\x01",
            "矿工叔叔们送慰问品哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "爸爸说，奇米送去的话，\x01",
            "大家会很开心，\x01",
            "所以才要我去送。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "嘿嘿，其实爸爸\x01",
            "是个很容易害羞的人呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1020")

    #C0052
    ChrTalk(
        0xFE,
        (
            "矿工叔叔们啊～\x01",
            "都对奇米很好哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "大家都说\x01",
            "很尊敬爸爸！\x01",
            "嘿嘿～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_1020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_104A")

    #C0054
    ChrTalk(
        0xFE,
        "今天的晚饭会是什么呢¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_104A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1077")

    #C0055
    ChrTalk(
        0xFE,
        (
            "奇米最喜欢\x01",
            "帮爸爸的忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_1077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_10E3")

    #C0056
    ChrTalk(
        0xFE,
        (
            "爸爸他啊～以前当过矿工，\x01",
            "所以很关心现在的矿工们。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "偶尔还会给缺钱的矿工\x01",
            "送些食材呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_10E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_114B")

    #C0058
    ChrTalk(
        0xFE,
        (
            "爸爸说，今天晚上\x01",
            "要关店出去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "纪念庆典期间一直很忙，\x01",
            "希望他能好好开心一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_114B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_119E")

    #C0060
    ChrTalk(
        0xFE,
        (
            "所谓的耀晶片，\x01",
            "就是七耀石的碎片哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        "我知道的很多吧，嘿嘿。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_119E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11D1")

    #C0062
    ChrTalk(
        0xFE,
        (
            "好想看看\x01",
            "爸爸当矿工时的样子啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_11D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_127C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1249")

    #C0063
    ChrTalk(
        0xFE,
        (
            "爸爸\x01",
            "本来不太高兴，\x01",
            "不过今天好像已经恢复了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "嘿嘿，\x01",
            "一定是因为奇米支持他的缘故吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1277")

    label("loc_1249")


    #C0065
    ChrTalk(
        0xFE,
        (
            "爸爸\x01",
            "本来不太高兴，\x01",
            "不过好像又有精神了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1277")

    Jump("loc_14D0")

    label("loc_127C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12E2")

    #C0066
    ChrTalk(
        0xFE,
        (
            "哈罗德叔叔他啊～\x01",
            "在看着奇米的时候，\x01",
            "表情好像总有点悲伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        "发生过什么事呢……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_14D0")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1349")

    #C0068
    ChrTalk(
        0xFE,
        (
            "纪念庆典快到了，\x01",
            "爸爸好像却\x01",
            "不太高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "难道是奇米做了什么坏事吗？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1374")

    label("loc_1349")


    #C0070
    ChrTalk(
        0xFE,
        (
            "只要一提到纪念庆典，\x01",
            "爸爸就会不高兴。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1374")

    Jump("loc_14D0")

    label("loc_1379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1387")
    Jump("loc_14D0")

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_142E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F9")

    #C0071
    ChrTalk(
        0xFE,
        (
            "爸爸以前\x01",
            "也是矿工哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "身材也很高大健壮，\x01",
            "听说是镇上最棒的矿工呢。\x01",
            "很厉害吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1429")

    label("loc_13F9")


    #C0073
    ChrTalk(
        0xFE,
        (
            "听说爸爸\x01",
            "以前是镇上最棒的矿工。\x01",
            "很厉害吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1429")

    Jump("loc_14D0")

    label("loc_142E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_14D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x66, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1450")
    SetScenarioFlags(0x66, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A6")

    #C0074
    ChrTalk(
        0xFE,
        "帮忙，帮忙¤\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "爸爸虽然\x01",
            "对镇上的人很凶，\x01",
            "但是对我很温柔哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_14D0")

    label("loc_14A6")


    #C0076
    ChrTalk(
        0xFE,
        (
            "爸爸对我\x01",
            "很温柔的，\x01",
            "所以不要怕他哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D0")

    TalkEnd(0xFE)
    Return()

    # Function_5_F28 end

    def Function_6_14D4(): pass

    label("Function_6_14D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_15A5")
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 3)), scpexpr(EXPR_END)), "loc_1585")

    #C0077
    ChrTalk(
        0xC,
        (
            "#0908F（艾丝蒂尔……我明白你的心情，\x01",
            "  但还是再平静一点吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        "#0806F（呜呜……我知道，可是……）\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        "#3605F…………………？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1599")

    label("loc_1585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 2)), scpexpr(EXPR_END)), "loc_1596")
    Call(0, 9)
    Jump("loc_1599")

    label("loc_1596")

    Call(0, 8)

    label("loc_1599")

    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)

    label("loc_15A5")

    TalkEnd(0xFE)
    Return()

    # Function_6_14D4 end

    def Function_7_15A9(): pass

    label("Function_7_15A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1610")

    #C0080
    ChrTalk(
        0xFE,
        (
            "哎呀，这是……\x01",
            "矿工用的安全头盔吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "竟然还卖这种东西，\x01",
            "不愧是矿山镇……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1652")

    label("loc_1610")


    #C0082
    ChrTalk(
        0xFE,
        "这个安全头盔，可以当土特产吗？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "……但还是太占地方了吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1652")

    TalkEnd(0xFE)
    Return()

    # Function_7_15A9 end

    def Function_8_1656(): pass

    label("Function_8_1656")

    EventBegin(0x0)
    Fade(500)
    OP_68(4730, 1500, 0, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(26660, 0)
    SetChrPos(0x101, 2750, 0, -1250, 45)
    SetChrPos(0x102, 2100, 0, -600, 45)
    SetChrPos(0x103, 1750, 0, -2250, 45)
    SetChrPos(0x104, 1100, 0, -1600, 45)
    OP_0D()

    #C0084
    ChrTalk(
        0xC,
        (
            "#0905F那么，哈罗德先生\x01",
            "您是在七年前创建了如今的贸易公司……？\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xA,
        (
            "#3609F哈哈，没有那么夸张，\x01",
            "不算是贸易公司哦……\x02\x03",

            "#3600F在与人来往的时候，\x01",
            "我总是注重让所有的生意伙伴\x01",
            "都能绽放出笑容。\x02\x03",

            "#3604F身为克洛斯贝尔的贸易商，\x01",
            "或许是有些不够格吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "#0904F不……\x01",
            "我认为您的工作\x01",
            "非常有意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xB,
        "#0801F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#0005F（艾丝蒂尔他们和哈罗德先生……\x01",
            "  好像正在谈话啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#0104F（打扰到他们可就不好了。）\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2750, 0, -1250, 45)
    SetScenarioFlags(0x94, 2)
    EventEnd(0x5)
    Return()

    # Function_8_1656 end

    def Function_9_1893(): pass

    label("Function_9_1893")

    EventBegin(0x0)
    Fade(500)
    OP_68(4730, 1500, 0, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(26660, 0)
    SetChrPos(0x101, 2750, 0, -1250, 45)
    SetChrPos(0x102, 2100, 0, -600, 45)
    SetChrPos(0x103, 1750, 0, -2250, 45)
    SetChrPos(0x104, 1100, 0, -1600, 45)
    OP_0D()
    TurnDirection(0xA, 0xB, 300)

    #C0090
    ChrTalk(
        0xA,
        (
            "#3605F那个……\x01",
            "您是艾丝蒂尔小姐吧？\x02\x03",

            "#3600F那个，我们曾在哪里\x01",
            "见过面吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_1982():
        TurnDirection(0xC, 0xB, 300)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1982)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    WaitChrThread(0xC, 1)

    #C0091
    ChrTalk(
        0xB,
        (
            "#0805F不，没有！\x01",
            "我只是觉得您和我认识的\x01",
            "一个人长得有点像！\x02\x03",

            "#0806F（……没想到，竟然\x01",
            "  会这么像……）\x02\x03",

            "#0808F（这个人……是真人吧？）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0xB)
    SetChrPos(0x0, 2750, 0, -1250, 45)
    SetScenarioFlags(0x94, 3)
    EventEnd(0x5)
    Return()

    # Function_9_1893 end

    SaveToFile()

Try(main)
