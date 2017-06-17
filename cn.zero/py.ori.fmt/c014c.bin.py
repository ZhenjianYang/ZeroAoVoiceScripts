from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c014c.bin",                # FileName
        "c014c",                    # MapName
        "c014c",                    # Location
        0x0006,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 6, 0, 2, 0, 3],
    )

    BuildStringList((
        "c014c",                  # 0
        "查珂",                   # 1
        "温蒂",                   # 2
        "菲尔纳德",               # 3
        "米泽特",                 # 4
        "巴吉利奥",               # 5
        "游客",                   # 6
        "游客",                   # 7
    ))

    AddCharChip((
        "chr/ch26100.itc",                   # 00
        "chr/ch27800.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch21000.itc",                   # 03
        "chr/ch20800.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch24400.itc",                   # 06
        "chr/ch33200.itc",                   # 07
    ))

    DeclNpc(9270,    0,       2650,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(9329,    0,       -1350,   270,  261,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-1519,   0,       14659,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-4480,   0,       7440,    0,    261,  0x0, 0,   5,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2299,    0,       6420,    90,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(11119,   4000,    8699,    90,   261,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-3309,   0,       790,     90,   261,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)

    DeclActor(8130,    0,       3080,    1000,    9270,    1500,    3140,    0x007E, 0,  4,  0x0000)
    DeclActor(8310,    0,       -1360,   1000,    9330,    1500,    -1350,   0x007E, 0,  7,  0x0000)

    ScpFunction((
        "Function_0_200",          # 00, 0
        "Function_1_2B8",          # 01, 1
        "Function_2_409",          # 02, 2
        "Function_3_4FB",          # 03, 3
        "Function_4_4FC",          # 04, 4
        "Function_5_678",          # 05, 5
        "Function_6_D85",          # 06, 6
        "Function_7_10DB",         # 07, 7
        "Function_8_10DF",         # 08, 8
        "Function_9_1DE0",         # 09, 9
        "Function_10_2506",        # 0A, 10
        "Function_11_2852",        # 0B, 11
        "Function_12_2B74",        # 0C, 12
        "Function_13_2EBB",        # 0D, 13
        "Function_14_2F56",        # 0E, 14
        "Function_15_32B6",        # 0F, 15
    ))


    def Function_0_200(): pass

    label("Function_0_200")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_240"),
        (1, "loc_24C"),
        (2, "loc_258"),
        (3, "loc_264"),
        (4, "loc_270"),
        (5, "loc_27C"),
        (6, "loc_288"),
        (SWITCH_DEFAULT, "loc_294"),
    )


    label("loc_240")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_24C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_258")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_264")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_270")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_27C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_288")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_294")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A0")

    label("loc_2B7")

    Return()

    # Function_0_200 end

    def Function_1_2B8(): pass

    label("Function_1_2B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_408")
    OP_95(0xFE, -4480, 0, 9380, 2000, 0x0)
    OP_95(0xFE, -1380, 0, 11120, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 9480, 2000, 0x0)
    OP_95(0xFE, 5230, 0, 6900, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(1300)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    OP_95(0xFE, 5230, 0, 1000, 2000, 0x0)
    OP_95(0xFE, 3800, 0, 930, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    OP_95(0xFE, -1350, 0, 930, 2000, 0x0)
    OP_95(0xFE, -1310, 0, -1230, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    OP_95(0xFE, -1310, 0, 2990, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 4640, 2000, 0x0)
    OP_95(0xFE, -4480, 0, 7440, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0x0, 0x190)
    Sleep(100)
    Jump("Function_1_2B8")

    label("loc_408")

    Return()

    # Function_1_2B8 end

    def Function_2_409(): pass

    label("Function_2_409")

    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_450")
    SetChrPos(0xC, 11460, 4000, 8870, 90)
    SetChrPos(0xD, 10670, 4000, 15920, 0)
    SetChrPos(0xE, 1050, 0, 3500, 90)
    Jump("loc_4FA")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_46F")
    SetChrPos(0xE, 1680, 0, 12640, 0)
    Jump("loc_4FA")

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49F")
    SetChrPos(0xD, 11460, 4000, -1040, 90)
    SetChrPos(0xE, 40, 0, 4670, 315)
    Jump("loc_4FA")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrPos(0xD, 9090, 4000, 3890, 180)
    SetChrPos(0xE, 3670, 0, -2980, 0)
    Jump("loc_4FA")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4FA")
    SetChrPos(0xD, 11040, 4000, 7060, 225)
    SetChrPos(0xE, 310, 0, -2980, 0)

    label("loc_4FA")

    Return()

    # Function_2_409 end

    def Function_3_4FB(): pass

    label("Function_3_4FB")

    Return()

    # Function_3_4FB end

    def Function_4_4FC(): pass

    label("Function_4_4FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66E")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3")

    #C0001
    ChrTalk(
        0x8,
        (
            "啊，你们就是温蒂前辈\x01",
            "的朋友吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "你们知道吗～？\x01",
            "我们最近新推出了更换\x01",
            "战术导力器外壳的服务哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "有各种时尚漂亮的款式\x01",
            "可供选择～\x01",
            "请一定要看一看～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x71, 4)

    label("loc_5C3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_666")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "更换外壳\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_621")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_621")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_642")
    Call(0, 6)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_661")

    label("loc_642")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_661")
    OP_60(0x0)
    Call(0, 5)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_661")

    Jump("loc_5CD")

    label("loc_666")

    TalkEnd(0x8)
    Jump("loc_677")

    label("loc_66E")

    TalkBegin(0x8)
    Call(0, 6)
    TalkEnd(0x8)

    label("loc_677")

    Return()

    # Function_4_4FC end

    def Function_5_678(): pass

    label("Function_5_678")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_682")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D84")
    MenuCmd(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_END)), "loc_6C0")
    MenuCmd(1, 0, "蓝色警官　　　　已购买")
    MenuCmd(3, 0, 0x0)
    Jump("loc_6DC")

    label("loc_6C0")

    MenuCmd(1, 0, "蓝色警官　　　　1000米拉")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_END)), "loc_708")
    MenuCmd(1, 0, "和平绿　　　　　已购买")
    MenuCmd(3, 0, 0x1)
    Jump("loc_724")

    label("loc_708")

    MenuCmd(1, 0, "和平绿　　　　　1000米拉")

    label("loc_724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_END)), "loc_750")
    MenuCmd(1, 0, "黑猫　　　　　　已购买")
    MenuCmd(3, 0, 0x2)
    Jump("loc_76C")

    label("loc_750")

    MenuCmd(1, 0, "黑猫　　　　　　1000米拉")

    label("loc_76C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_END)), "loc_798")
    MenuCmd(1, 0, "危险橙　　　　　已购买")
    MenuCmd(3, 0, 0x3)
    Jump("loc_7B4")

    label("loc_798")

    MenuCmd(1, 0, "危险橙　　　　　1000米拉")

    label("loc_7B4")

    MenuCmd(1, 0, "放弃")

    #A0004
    AnonymousTalk(
        0x8,
        (
            scpstr(0x18),
            "要更换为哪一个～？\x02",
        )
    )

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_803")
    Sleep(1)
    Return()

    label("loc_803")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_843")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis172.itp")
    Jump("loc_8FE")

    label("loc_843")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_883")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis173.itp")
    Jump("loc_8FE")

    label("loc_883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C3")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis174.itp")
    Jump("loc_8FE")

    label("loc_8C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FE")
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis175.itp")

    label("loc_8FE")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_993")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是罗伊德专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD5")

    label("loc_993")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A00")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是艾莉专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD5")

    label("loc_A00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6D")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是缇欧专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD5")

    label("loc_A6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD5")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这个外壳是兰迪专用的。\x01",
            "购入后，显示在[ORBMENT]菜单里的\x01",
            "战术导力器外壳即会改变。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD5")


    #A0009
    AnonymousTalk(
        0x8,
        "好的，确定要更换为这种款式吗～？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【确定更换】\x01",      # 0
            "【还是算了】\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_60(0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D67")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BB6")

    #C0010
    ChrTalk(
        0x8,
        (
            "咦～您的米拉好像不够呢。\x01",
            "这样是没办法更换的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D58")

    label("loc_BB6")


    #C0011
    ChrTalk(
        0x8,
        (
            "明白啦。\x01",
            "请稍等一下哦～⊥\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(71, 0, 100, 0)
    Sleep(800)
    FadeToBright(1000, 0)
    OP_0D()

    #C0012
    ChrTalk(
        0x8,
        "好了，让您久等啦。\x02",
    )

    CloseMessageWindow()
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了罗伊德的导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 5)
    Jump("loc_CF4")

    label("loc_C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C87")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了艾莉的导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 6)
    Jump("loc_CF4")

    label("loc_C87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC0")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了缇欧的导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF0, 7)
    Jump("loc_CF4")

    label("loc_CC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF4")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "更换了兰迪的导力器外壳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 0)

    label("loc_CF4")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2F")
    OP_DE(0x16, 0x0)

    label("loc_D2F")


    #C0017
    ChrTalk(
        0x8,
        (
            "呵呵，期待您的\x01",
            "下次光临～\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_50(0x12, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_D58")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D71")

    label("loc_D67")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D71")

    OP_CA(0x1, 0xFF, 0x0)
    FadeToDark(300, 0, 100)
    Jump("loc_682")

    label("loc_D84")

    Return()

    # Function_5_678 end

    def Function_6_D85(): pass

    label("Function_6_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6E")

    #C0018
    ChrTalk(
        0x8,
        (
            "今年的纪念庆典也没出什么大事，\x01",
            "应该可以平平安安地结束，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "和平果然比什么都重要啊。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0003F（嗯～其实发生了\x01",
            "  不少事呢……）\x02\x03",

            "#0000F（也罢，这就是所谓的\x01",
            "  警察与市民的不同视角吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E9B")

    label("loc_E6E")


    #C0021
    ChrTalk(
        0x8,
        (
            "纪念庆典似乎能够平安结束，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9B")

    Jump("loc_10DA")

    label("loc_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0D")

    #C0022
    ChrTalk(
        0x8,
        (
            "我拍了好多\x01",
            "游行时的照片呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "……用的是展品相机。\x01",
            "待会要偷偷地显像才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F4E")

    label("loc_F0D")


    #C0024
    ChrTalk(
        0x8,
        (
            "我用高级展品相机\x01",
            "拍了些游行的照片。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        "可不要告诉店长哦。\x02",
    )

    CloseMessageWindow()

    label("loc_F4E")

    Jump("loc_10DA")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_FBB")

    #C0026
    ChrTalk(
        0x8,
        (
            "店头放着一些用来\x01",
            "比较性能的样品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "先来实际确认一下\x01",
            "使用的感觉，然后再选购吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DA")

    label("loc_FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_102D")

    #C0028
    ChrTalk(
        0x8,
        "明天有游行呢。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "要不要买个相机，\x01",
            "拍些纪念照片呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "和以前相比，\x01",
            "价格已经实惠了很多哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DA")

    label("loc_102D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_107F")

    #C0031
    ChrTalk(
        0x8,
        (
            "朋友今天要去\x01",
            "米修拉姆。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "啊～要不是有工作，\x01",
            "我也很想去啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10DA")

    label("loc_107F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_10DA")

    #C0033
    ChrTalk(
        0x8,
        "哎呀，外面真是好多人啊～\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "不过，导力商店里\x01",
            "倒是同平时\x01",
            "没有多大的变化呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DA")

    Return()

    # Function_6_D85 end

    def Function_7_10DB(): pass

    label("Function_7_10DB")

    Call(0, 8)
    Return()

    # Function_7_10DB end

    def Function_8_10DF(): pass

    label("Function_8_10DF")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DDC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "提问\x01",            # 2
            "放弃\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1147")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1147")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BE")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    #C0035
    ChrTalk(
        0x9,
        (
            "对了，罗伊德，你们\x01",
            "有没有『高级回路』？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#0005F『高级回路』……？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "嗯嗯，就是威力过于强大，\x01",
            "不能镶嵌在普通结晶孔里的回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "为了镶嵌这些回路，\x01",
            "就需要强化结晶孔本身。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129B")

    #C0039
    ChrTalk(
        0x9,
        (
            "我们这里并没有\x01",
            "高级回路出售……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "不过，强化结晶孔倒是可以的。\x01",
            "如果有需要的话，就跟我说哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12EB")

    label("loc_129B")


    #C0041
    ChrTalk(
        0x9,
        (
            "我们也开始推行强化结晶孔与\x01",
            "经营高级回路的业务了，\x01",
            "如果有需要，就跟我说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EB")

    OP_5A()
    Sound(828, 0, 100, 0)
    FadeToDark(300, 0, 100)

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※可以强化结晶孔了。\x02",
        )
    )

    CloseMessageWindow()

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※选择[SLOT]，\x01",
            "  再选择已开封的结晶孔\x01",
            "  就可以强化结晶孔的等级。\x02",
        )
    )

    CloseMessageWindow()

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※强化之后，除了可以镶嵌高级回路之外，\x01",
            "  还可以让最大ＥＰ值\x01",
            "  得到提升。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xD9, 3)
    OP_C7(0x1, 0x80)

    label("loc_13BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_13CE")
    OP_AF(0xF)
    Jump("loc_1410")

    label("loc_13CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_13DE")
    OP_AF(0xE)
    Jump("loc_1410")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13EE")
    OP_AF(0xD)
    Jump("loc_1410")

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_13FE")
    OP_AF(0xC)
    Jump("loc_1410")

    label("loc_13FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_140E")
    OP_AF(0xB)
    Jump("loc_1410")

    label("loc_140E")

    OP_AF(0xA)

    label("loc_1410")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DD7")

    label("loc_141F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1440")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Jump("loc_1DD7")

    label("loc_1440")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1454")
    Jump("loc_1DD7")

    label("loc_1454")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DD7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_15B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155A")

    #C0045
    ChrTalk(
        0x9,
        (
            "罗伊德，你们今天也有调查工作？\x01",
            "警官可真够辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "对了，你回来以后，我们都没有聚过……\x01",
            "下次叫上奥斯卡，三个人一起去玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#0000F嗯，说得也是啊。\x01",
            "要是有时间的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "啊哈，我也正想\x01",
            "这么说呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15AE")

    label("loc_155A")


    #C0049
    ChrTalk(
        0x9,
        (
            "大家平时都很忙……\x01",
            "不过，要是有时间的话，\x01",
            "下次就叫上奥斯卡，三个人一起去玩吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AE")

    Jump("loc_1DD7")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_16B0")

    #C0050
    ChrTalk(
        0x9,
        "还在找走失的小男孩吗？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x9,
        (
            "要是有什么我能帮上忙的事情，请尽管说哦。\x01",
            "像导力车什么的，\x01",
            "我可以从店里直接开出去啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0006F这种事……温蒂好像真能干得出来，\x01",
            "有点可怕啊……\x02\x03",

            "#0000F线索都已经收集到了，\x01",
            "没问题的。\x01",
            "你的好意，我就心领啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD7")

    label("loc_16B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_19FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")

    #C0053
    ChrTalk(
        0x101,
        (
            "#0001F温蒂，打扰一下好吗？\x02\x03",

            "想问问你有没有\x01",
            "见过这孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        "哎？什么什么？\x02",
    )

    CloseMessageWindow()

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0056
    ChrTalk(
        0x9,
        (
            "嗯～五岁左右的孩子啊。\x01",
            "比我们家的潘莎稍微小一点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "不过，真抱歉，我没有去看游行，\x01",
            "所以不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        "#0005F如此说来，他也没来过店里吧？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "嗯，这点我倒是\x01",
            "可以肯定呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "因为我可是一直在数着那个\x01",
            "导力门的打开次数的。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#0006F是、是吗……\x01",
            "（看来是不会有错了。）\x02\x03",

            "#0000F谢啦，帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAC, 1)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    Jump("loc_19F8")

    label("loc_189C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B5")

    #C0062
    ChrTalk(
        0x9,
        (
            "外面好像人多得不得了，\x01",
            "在这种情况下走散了，可真是令人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "对了……是叫蔡特吧。\x01",
            "让那条警犬帮忙找如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#0000F嗯，已经把它\x01",
            "托付给缇欧了。\x02\x03",

            "#0008F只是人实在太多，\x01",
            "所以可能会很花时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "现在也只好耐心\x01",
            "探听情报了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        "……加油哦，罗伊德！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_19F8")

    label("loc_19B5")


    #C0067
    ChrTalk(
        0x9,
        (
            "最后还是只能\x01",
            "踏踏实实地探听情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        "……加油哦，罗伊德！\x02",
    )

    CloseMessageWindow()

    label("loc_19F8")

    Jump("loc_1DD7")

    label("loc_19FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1A99")

    #C0069
    ChrTalk(
        0x9,
        (
            "游行时使用的导力车，\x01",
            "用的到底是什么样的零件呢～……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        (
            "我这样胡思乱想着，\x01",
            "不知不觉间游行就结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        "啊哈哈，这就是所谓的职业病吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DD7")

    label("loc_1A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B74")

    #C0072
    ChrTalk(
        0x9,
        (
            "与新型的结晶回路相比，\x01",
            "便宜的旧式回路\x01",
            "更加好卖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "导力器在许多地域还没有完全普及，\x01",
            "还是旧式的结构比较简单嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "不过，就算已经加工过了，\x01",
            "只要再分解成耀晶片，\x01",
            "也能重新再利用，这点真是很好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD7")

    label("loc_1B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1C3F")

    #C0075
    ChrTalk(
        0x9,
        (
            "彩虹剧团的公演……\x01",
            "要是有空的话，真想去看看……\x01",
            "不过今年似乎是很困难啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "这里改装成导力商店以后，\x01",
            "客人确实是增加了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x9,
        (
            "虽然这是好事，\x01",
            "不过我真想更加轻松地\x01",
            "摆弄导力器啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD7")

    label("loc_1C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF1")

    #C0078
    ChrTalk(
        0x9,
        "有个客人在我工作时来搭讪。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        (
            "当时明明还有很多客人，\x01",
            "真是不懂挑选场合，\x01",
            "我差点就一扳手砸过去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#0006F你都已经是大人了，\x01",
            "要适可而止哦……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D6C")

    label("loc_1CF1")


    #C0081
    ChrTalk(
        0x9,
        (
            "嗯，打倒是没打，\x01",
            "不过因为客人越聚越多，\x01",
            "就赶快把他给打发走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "真是的，当时都已经那么忙了，\x01",
            "搭讪也该看看场合吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D6C")

    Jump("loc_1DD7")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DD7")

    #C0083
    ChrTalk(
        0x9,
        (
            "真是好多人哦，\x01",
            "不少客人都是出于兴趣\x01",
            "来看看的。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "等到太阳下山之后，\x01",
            "我也出去走走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD7")

    Jump("loc_10EC")

    label("loc_1DDC")

    TalkEnd(0x9)
    Return()

    # Function_8_10DF end

    def Function_9_1DE0(): pass

    label("Function_9_1DE0")


    #C0085
    ChrTalk(
        0x9,
        (
            "ＯＫ。\x01",
            "想问哪方面的问题呢？\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FB")
    FadeToDark(300, 0, 100)

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "关于战术导力器\x01",      # 0
            "关于回路\x01",            # 1
            "关于结晶孔\x01",          # 2
            "关于导力魔法\x01",        # 3
            "放弃\x01",                # 4
        )
    )

    MenuEnd(0x3)
    OP_60(0x1)
    FadeToBright(300, 0)
    OP_5A()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1E94"),
        (1, "loc_205B"),
        (2, "loc_2188"),
        (3, "loc_228B"),
        (SWITCH_DEFAULT, "loc_24E7"),
    )


    label("loc_1E94")


    #C0086
    ChrTalk(
        0x9,
        (
            "所谓的『战术导力器』，\x01",
            "就是一种专门用于个人战斗的\x01",
            "便携式小型导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x9,
        (
            "不仅能强化使用者的能力，\x01",
            "还可以用来发动导力魔法。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "一般情况下，我们就把它\x01",
            "简称为『导力器』啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "你们所使用的，\x01",
            "就是其中的最新型号——\x01",
            "名为『艾尼格玛』的导力器。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "为了配合每个人的具体情况与使用习惯，\x01",
            "我们会对导力器进行完美的微调，\x01",
            "所以其构造会因人而异。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "像限定属性的结晶孔啦，连接结晶孔的\x01",
            "结晶链形状啦，都会有所不同。\x01",
            "各位可以自行比较一下每个人的导力器。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F6")

    label("loc_205B")


    #C0092
    ChrTalk(
        0x9,
        (
            "所谓回路，就是将耀晶片进行精炼后\x01",
            "所制造出的，战术导力器专用的『结晶回路』。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "如果携带有足够数量的耀晶片，\x01",
            "就可以在我们这里进行合成。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "每种回路都有各自的特性效果，\x01",
            "同一条结晶链上的回路属性值达到一定数值后，\x01",
            "就可以使用特定的导力魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        "如果你们攒够了耀晶片，可以进行多种尝试呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_24F6")

    label("loc_2188")


    #C0096
    ChrTalk(
        0x9,
        (
            "导力器的结晶孔，\x01",
            "在最初时几乎都是未开封的状态。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "所以如果想要镶嵌回路，\x01",
            "首先需要开封结晶孔。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "多开封一些结晶孔，\x01",
            "不仅可以镶嵌更多的回路，\x01",
            "同时也能提升最大ＥＰ值。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "开封虽然也需要使用耀晶片，\x01",
            "但开封之后会非常便利。\x01",
            "所以请大家积极开封哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F6")

    label("loc_228B")


    #C0100
    ChrTalk(
        0x9,
        (
            "利用战术导力器发动的魔法\x01",
            "统称为导力魔法，在多数情况下，\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        "我们习惯将它简称为『魔法』。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "其实，魔法是由安置在导力器内部的机械装置\x01",
            "和回路与使用者产生连锁共鸣，\x01",
            "从而引发的现象……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        "算了，这种细节知识不说也罢。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "而可发动的魔法，是由\x01",
            "『每条结晶链上所镶嵌的回路属性总值』\x01",
            "所决定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "这个稍微有些复杂，怎么说好呢……\x01",
            "对了，举个例子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x9,
        (
            "在处于同一条结晶链上的\x01",
            "结晶孔中镶嵌回路，\x01",
            "如果地属性的总值超过了２……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "就可以使用『地震波』\x01",
            "这个魔法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        (
            "镶嵌的回路数越多，\x01",
            "可使用的魔法种类\x01",
            "也就越多。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "至于发动其它魔法所需的属性值，\x01",
            "应该都记录在魔法列表中了。\x01",
            "请随时参考吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24F6")

    label("loc_24E7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_24F6")

    label("loc_24F6")

    Jump("loc_1E0B")

    label("loc_24FB")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_1DE0 end

    def Function_10_2506(): pass

    label("Function_10_2506")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_25A0")

    #C0110
    ChrTalk(
        0xFE,
        (
            "刚才，有位帝国的游客\x01",
            "购买了一辆导力车。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "说是看到了在游行时优雅行驶的\x01",
            "导力车之后，就突然很想要了。\x01",
            "哎呀，真是多亏了游行活动呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284E")

    label("loc_25A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_262E")

    #C0112
    ChrTalk(
        0xFE,
        (
            "……仔细一想的话，\x01",
            "在无意识之中，我好像\x01",
            "一直都在依赖温蒂的知识。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "或许我也应该开始\x01",
            "认真学习一些\x01",
            "导力器方面的知识了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284E")

    label("loc_262E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26CA")

    #C0114
    ChrTalk(
        0xFE,
        (
            "我有好几次都看到\x01",
            "游客来找温蒂修理\x01",
            "坏掉的感光回路。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "唔唔……虽然让他们买新的\x01",
            "能赚更多钱，\x01",
            "不过，还是用那种方法容易吸引到回头客呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284E")

    label("loc_26CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2711")

    #C0116
    ChrTalk(
        0xFE,
        (
            "唔唔，真希望有什么手段能把\x01",
            "外面的游客吸引进来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284E")

    label("loc_2711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_27B8")

    #C0117
    ChrTalk(
        0xFE,
        (
            "温蒂那家伙……\x01",
            "居然差点就对客人\x01",
            "大打出手。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "听说她以前在工房的时候\x01",
            "也发生过好几次\x01",
            "类似的事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "真是的，那个师父\x01",
            "到底是怎么教育她的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_284E")

    label("loc_27B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_284E")

    #C0120
    ChrTalk(
        0xFE,
        (
            "虽然时不时就能卖掉\x01",
            "一两台导力相机，\x01",
            "但整体的销售额还远远不够呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "客人们都被外面的露天店吸引了吗……\x01",
            "看来我们也应该加强宣传力度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284E")

    TalkEnd(0xFE)
    Return()

    # Function_10_2506 end

    def Function_11_2852(): pass

    label("Function_11_2852")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_28F0")

    #C0122
    ChrTalk(
        0xFE,
        "今天就是最终日了吗……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "今年没怎么到外面逛，\x01",
            "一直都在这里泡着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "对阿姨我来说，\x01",
            "欣赏这里的商品，\x01",
            "就是最刺激最有趣的事情了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2956")

    #C0125
    ChrTalk(
        0xFE,
        (
            "游行时的景象\x01",
            "全都拍进相机了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "不愧是新型号的相机，\x01",
            "使用方便，真是太棒了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_2956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_29D0")

    #C0127
    ChrTalk(
        0xFE,
        (
            "说起来，好像一直没怎么去\x01",
            "二楼的柜台看过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "听说那里展示着最先进的产品……\x01",
            "还是好好地欣赏一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_29D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2A4E")

    #C0129
    ChrTalk(
        0xFE,
        "（拍照）……！\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "难得来一次，也给热闹的\x01",
            "店内拍几张照片吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "还能拍到时髦的新产品，\x01",
            "真是一举两得呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2ADE")

    #C0132
    ChrTalk(
        0xFE,
        (
            "阿姨我最怕\x01",
            "人多燥热的地方了～……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "从这点来看，这家店里的制冷设备\x01",
            "效果很好，真是很舒服呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        "一进来就待着不想出去了～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B70")

    label("loc_2ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2B70")

    #C0135
    ChrTalk(
        0xFE,
        (
            "导力相机降价了，\x01",
            "于是就狠狠心买下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "呵呵，能使用导力相机\x01",
            "是我的梦想呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "这样一来，在纪念庆典\x01",
            "就可以玩得更加开心了～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B70")

    TalkEnd(0xFE)
    Return()

    # Function_11_2852 end

    def Function_12_2B74(): pass

    label("Function_12_2B74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2BE2")

    #C0138
    ChrTalk(
        0xFE,
        (
            "查珂……\x01",
            "纪念庆典都没有请假，\x01",
            "工作真的很努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "好，爸爸下次就\x01",
            "带你去米修拉姆吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB7")

    label("loc_2BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C5E")

    #C0140
    ChrTalk(
        0xFE,
        (
            "游行队伍过来的时候，查珂\x01",
            "急忙飞奔到店外去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "感……感觉视线都对上了，\x01",
            "不过，她好像并没发现我呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB7")

    label("loc_2C5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CE7")

    #C0142
    ChrTalk(
        0xFE,
        (
            "嗯，在我犹豫的这段期间，\x01",
            "游行开始的时间越来越近了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "听说，如果不练习的话\x01",
            "很难拍到好照片。\x01",
            "这次还是先不买了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB7")

    label("loc_2CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2D68")

    #C0144
    ChrTalk(
        0xFE,
        (
            "嗯～刚才我就一直在观察，\x01",
            "查珂的前辈似乎是个\x01",
            "很会照顾人的女孩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "这样的话，应该可以放心\x01",
            "把查珂交给她了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB7")

    label("loc_2D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E28")

    #C0146
    ChrTalk(
        0xFE,
        "刚、刚才真是吓了我一跳啊……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "查珂旁边柜台的那个女孩\x01",
            "差点就拿扳手打那个\x01",
            "看上去很难缠的游客了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "在、在那么凶狠暴力的前辈手下工作，\x01",
            "查珂她不要紧吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2E61")

    label("loc_2E28")


    #C0149
    ChrTalk(
        0xFE,
        (
            "在那么凶狠暴力的前辈手下工作，\x01",
            "查珂她不要紧吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E61")

    Jump("loc_2EB7")

    label("loc_2E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EB7")

    #C0150
    ChrTalk(
        0xFE,
        (
            "唔唔……\x01",
            "最后到底该买哪个相机呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "最好能买个\x01",
            "经久耐用的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB7")

    TalkEnd(0xFE)
    Return()

    # Function_12_2B74 end

    def Function_13_2EBB(): pass

    label("Function_13_2EBB")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F55")

    #C0152
    ChrTalk(
        0x160,
        (
            "#3300F（中央广场的探听\x01",
            "  就到此为止了吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#0000F（嗯，应该足够了吧。）\x02\x03",

            "（接下来，就去站前街道\x01",
            "  问问看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)

    label("loc_2F55")

    Return()

    # Function_13_2EBB end

    def Function_14_2F56(): pass

    label("Function_14_2F56")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2FA1")

    #C0154
    ChrTalk(
        0xFE,
        (
            "我从以前开始，就一直跟\x01",
            "导力制品合不来呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301D")

    label("loc_2FA1")


    #C0155
    ChrTalk(
        0xFE,
        (
            "昨天买的导力手表，\x01",
            "刚一戴上就坏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "……现在正让修理柜台\x01",
            "的店员帮忙修理呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "唉唉，我果然是个\x01",
            "导力白痴啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_301D")

    Jump("loc_32B2")

    label("loc_3022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_30A6")

    #C0158
    ChrTalk(
        0xFE,
        (
            "店员小姐说什么\x01",
            "『只要好好爱护它就可以了』，\x01",
            "我实在是搞不懂啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "虽然她性格爽快，\x01",
            "是我喜欢的类型……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313E")

    label("loc_30A6")


    #C0160
    ChrTalk(
        0xFE,
        (
            "店员小姐刚才\x01",
            "为我做了导力制品的解说。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "……可是，那位小姐说什么\x01",
            "『只要好好爱护它就可以了』，\x01",
            "我实在是搞不懂啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "……虽然她很可爱………\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_313E")

    Jump("loc_32B2")

    label("loc_3143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_31BB")

    #C0163
    ChrTalk(
        0xFE,
        (
            "唔～这个……\x01",
            "包装上写着是高亮度的导力灯呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "而且还有多种颜色可以选择！？\x01",
            "真想买一个当土特产呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_31BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3216")

    #C0165
    ChrTalk(
        0xFE,
        (
            "这、这个好像是\x01",
            "最新型的战术导力器呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        "碰、碰一下的话不会坏掉吧！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3257")

    #C0167
    ChrTalk(
        0xFE,
        (
            "咦……？\x01",
            "楼下好像很吵闹。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "出什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_32B2")

    label("loc_3257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32B2")

    #C0169
    ChrTalk(
        0xFE,
        (
            "好厉害……！\x01",
            "这是什么啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "全是我这个导力白痴\x01",
            "完全摸不着头脑的东西啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B2")

    TalkEnd(0xFE)
    Return()

    # Function_14_2F56 end

    def Function_15_32B6(): pass

    label("Function_15_32B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3334")

    #C0171
    ChrTalk(
        0xFE,
        (
            "作为来克洛斯贝尔的纪念，\x01",
            "我买了带有导力照明灯的\x01",
            "挂坠。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "虽然还有很多稀奇的东西，\x01",
            "不过别的都很贵嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_3334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_33A2")

    #C0173
    ChrTalk(
        0xFE,
        (
            "在这个店里逛得入迷了，\x01",
            "竟然错过了游行啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "……没办法了……\x01",
            "作为代替，就看看导力车吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_33A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_341D")

    #C0175
    ChrTalk(
        0xFE,
        (
            "『保温能力超群！\x01",
            "  搭载最新的高功率结晶回路！』\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "……买、买哪个好呢？\x01",
            "说明书好复杂，\x01",
            "看了也不懂啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_341D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3478")

    #C0177
    ChrTalk(
        0xFE,
        "附带强力冷冻装置……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "唔唔……虽然很想买回去，\x01",
            "可是实在带不走呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_3478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_34CF")

    #C0179
    ChrTalk(
        0xFE,
        "自动摇头功能……？\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "哦哦，不愧是克洛斯贝尔。\x01",
            "什么都是最新型呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_351F")

    label("loc_34CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_351F")

    #C0181
    ChrTalk(
        0xFE,
        "这就是传说中的导力商店啊！\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "好，趁着这次庆典，\x01",
            "好好逛个够吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_351F")

    TalkEnd(0xFE)
    Return()

    # Function_15_32B6 end

    SaveToFile()

Try(main)
