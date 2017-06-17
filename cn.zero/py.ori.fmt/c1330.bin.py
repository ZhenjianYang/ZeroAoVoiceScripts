from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c1330.bin",                # FileName
        "c1330",                    # MapName
        "c1330",                    # Location
        0x001B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1330",                  # 0
    ))

    ScpFunction((
        "Function_0_AC",           # 00, 0
        "Function_1_DC",           # 01, 1
        "Function_2_F4",           # 02, 2
        "Function_3_62D",          # 03, 3
        "Function_4_CF7",          # 04, 4
        "Function_5_162A",         # 05, 5
    ))


    def Function_0_AC(): pass

    label("Function_0_AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2")
    Event(0, 3)
    Jump("loc_DB")

    label("loc_C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8")
    Event(0, 4)
    Jump("loc_DB")

    label("loc_D8")

    Event(0, 2)

    label("loc_DB")

    Return()

    # Function_0_AC end

    def Function_1_DC(): pass

    label("Function_1_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F3")

    Return()

    # Function_1_DC end

    def Function_2_F4(): pass

    label("Function_2_F4")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x0, 2200, 0, 0, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15E")
    SetChrPos(0x1, 500, 0, -500, 90)

    label("loc_15E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D")
    SetChrPos(0x2, 500, 0, 500, 90)

    label("loc_17D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C")
    SetChrPos(0x3, -700, 0, 0, 90)

    label("loc_19C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB")
    SetChrPos(0x4, -1900, 0, -600, 90)

    label("loc_1BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA")
    SetChrPos(0x5, -1900, 0, 600, 90)

    label("loc_1DA")

    FadeToBright(500, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 6)), scpexpr(EXPR_END)), "loc_467")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★【１６Ｆ】\x01",      # 0
            "　【 １Ｆ 】\x01",      # 1
            "　【 Ｂ５ 】\x01",      # 2
            "　【 离开 】\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_300")

    label("loc_251")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AB")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【１６Ｆ】\x01",      # 0
            "★【 １Ｆ 】\x01",      # 1
            "　【 Ｂ５ 】\x01",      # 2
            "　【 离开 】\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_300")

    label("loc_2AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【１６Ｆ】\x01",      # 0
            "　【 １Ｆ 】\x01",      # 1
            "★【 Ｂ５ 】\x01",      # 2
            "　【 离开 】\x01",      # 3
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_300")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_327")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_3A4")

    label("loc_327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_360")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3A4")

    label("loc_360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_399")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_3A4")

    label("loc_399")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_3A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_404")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3CF"),
        (1, "loc_3DF"),
        (2, "loc_3EF"),
        (SWITCH_DEFAULT, "loc_3FF"),
    )


    label("loc_3CF")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_3FF")

    label("loc_3DF")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_3FF")

    label("loc_3EF")

    EventEnd(0x5)
    NewScene("c1320", 102, 0, 0)
    IdleLoop()
    Jump("loc_3FF")

    label("loc_3FF")

    Jump("loc_462")

    label("loc_404")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_420"),
        (1, "loc_436"),
        (2, "loc_44C"),
        (SWITCH_DEFAULT, "loc_462"),
    )


    label("loc_420")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_462")

    label("loc_436")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_462")

    label("loc_44C")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1320", 102, 0, 0)
    IdleLoop()
    Jump("loc_462")

    label("loc_462")

    Jump("loc_62C")

    label("loc_467")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")

    Menu(
        0,
        10,
        10,
        0,
        (
            "★【１６Ｆ】\x01",      # 0
            "　【 １Ｆ 】\x01",      # 1
            "　【 离开 】\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4FC")

    label("loc_4B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FC")

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【１６Ｆ】\x01",      # 0
            "★【 １Ｆ 】\x01",      # 1
            "　【 离开 】\x01",      # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4FC")

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_523")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_5A0")

    label("loc_523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55C")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_5A0")

    label("loc_55C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_595")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_5A0")

    label("loc_595")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_5A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EA")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_5C5"),
        (1, "loc_5D5"),
        (SWITCH_DEFAULT, "loc_5E5"),
    )


    label("loc_5C5")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_5E5")

    label("loc_5D5")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_5E5")

    label("loc_5E5")

    Jump("loc_62C")

    label("loc_5EA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_600"),
        (1, "loc_616"),
        (SWITCH_DEFAULT, "loc_62C"),
    )


    label("loc_600")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_62C")

    label("loc_616")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_62C")

    label("loc_62C")

    Return()

    # Function_2_F4 end

    def Function_3_62D(): pass

    label("Function_3_62D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2400, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x102, -4500, 0, 0, 90)
    SetChrPos(0x101, -4500, 0, -500, 90)
    SetChrPos(0x103, -4500, 0, 500, 90)
    SetChrPos(0x104, -4500, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-400, 1000, 0, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_6F9():
        OP_96(0xFE, 0x2BC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F9)

    def lambda_713():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_713)
    Sleep(500)

    def lambda_727():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_727)

    def lambda_741():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_741)
    Sleep(300)

    def lambda_755():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_755)

    def lambda_76F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76F)
    Sleep(600)

    def lambda_783():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_783)

    def lambda_79D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79D)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    def lambda_7C0():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C0)
    Sleep(50)
    TurnDirection(0x103, 0x102, 500)

    #C0001
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯……\x01",
            "总裁的房间是在顶层吧。\x02\x03",

            "对了，我们刚才收下的这张卡片\x01",
            "到底是做什么用的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x10E, 0x1F4)

    #C0002
    ChrTalk(
        0x102,
        (
            "#11P#0100F哦，是认证用的门卡。\x02\x03",

            "由于这里也入驻了其它公司，\x01",
            "为了安全起见，好像只能去\x01",
            "相关楼层。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#6P#0306F原来如此……\x01",
            "这也是安保系统的一部分吧。\x02\x03",

            "#0301F不过，总有种不吝惜最新技术，\x01",
            "任意使用的感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0004
    ChrTalk(
        0x103,
        (
            "#0203F#5P据说，在克洛斯贝尔市\x01",
            "发起的导力网络计划\x01",
            "原本就是由ＩＢＣ主导的。\x02\x03",

            "然后，好像是在自治州政府加入之后，\x01",
            "才发展成了现在这种形态。\x02\x03",

            "#0200F据传闻说，计划中６０％的资金\x01",
            "都是ＩＢＣ提供的……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#11P#0104F嗯，似乎正是如此。\x02\x03",

            "#0100F然后，剩下的３０％由自治州提供，\x01",
            "最后的１０％是由爱普斯泰恩财团\x01",
            "自行负担的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#6P#0005F好厉害啊……\x01",
            "负担了一半以上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#6P#0300F也就是说，这个资产雄厚的\x01",
            "重要角色被安排在了顶层啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        "#11P#0100F嗯……要使用门卡了哦。\x02",
    )

    CloseMessageWindow()

    def lambda_AED():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AED)
    Sleep(100)

    def lambda_AFD():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AFD)
    WaitChrThread(0x102, 2)
    OP_68(600, 1000, 0, 1000)

    def lambda_B1F():
        OP_95(0xFE, 2300, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1F)
    Sleep(500)

    def lambda_B3C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B3C)
    WaitChrThread(0x102, 1)
    OP_6F(0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾莉把卡片插进了卡槽。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    Sound(72, 0, 100, 0)
    Sleep(300)

    Menu(
        0,
        10,
        10,
        0,
        (
            "　【１６Ｆ】\x01",      # 0
            "★【 １Ｆ 】\x01",      # 1
            "　【离开】\x01",        # 2
        )
    )

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetScenarioFlags(0x82, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BED")
    FadeToDark(500, 0, -1)
    OP_0D()
    Jump("loc_C6A")

    label("loc_BED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C26")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_C6A")

    label("loc_C26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5F")
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, -14000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    Jump("loc_C6A")

    label("loc_C5F")

    FadeToDark(500, 0, -1)
    OP_0D()

    label("loc_C6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB4")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_C8F"),
        (1, "loc_C9F"),
        (SWITCH_DEFAULT, "loc_CAF"),
    )


    label("loc_C8F")

    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_CAF")

    label("loc_C9F")

    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_CAF")

    label("loc_CAF")

    Jump("loc_CF6")

    label("loc_CB4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CCA"),
        (1, "loc_CE0"),
        (SWITCH_DEFAULT, "loc_CF6"),
    )


    label("loc_CCA")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Jump("loc_CF6")

    label("loc_CE0")

    SetScenarioFlags(0x5F, 1)
    Sleep(500)
    EventEnd(0x5)
    NewScene("c1310", 101, 0, 0)
    IdleLoop()
    Jump("loc_CF6")

    label("loc_CF6")

    Return()

    # Function_3_62D end

    def Function_4_CF7(): pass

    label("Function_4_CF7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(861)
    OP_68(-2400, 1000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x102, -4500, 0, 300, 90)
    SetChrPos(0x101, -4500, 0, -300, 90)
    SetChrPos(0x103, -4500, 0, -500, 90)
    SetChrPos(0x104, -4500, 0, 500, 90)
    SetChrPos(0x138, -4500, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x138, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis121.itp")
    OP_68(600, 1000, 0, 3000)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_E3A():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x138, 1, lambda_E3A)

    def lambda_E54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x138, 2, lambda_E54)
    Sleep(900)

    def lambda_E68():
        OP_96(0xFE, 0x0, 0x0, 0x258, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E68)

    def lambda_E82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E82)
    Sleep(400)

    def lambda_E96():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFFD94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E96)

    def lambda_EB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EB0)
    Sleep(400)

    def lambda_EC4():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EC4)

    def lambda_EDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_EDE)
    Sleep(400)

    def lambda_EF2():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0xFFFFFCE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_EF2)

    def lambda_F0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F0C)
    WaitChrThread(0x138, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    Sound(72, 0, 100, 0)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    Sound(159, 0, 100, 0)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    OP_68(600, -3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(861, 2, 100, 0)
    OP_68(600, 1000, 0, 5000)
    FadeToBright(4000, 0)
    OP_0D()
    OP_6F(0x1)
    OP_93(0x138, 0x10E, 0x1F4)
    Sleep(300)

    #C0010
    ChrTalk(
        0x138,
        (
            "#11P#2903F话说回来……\x01",
            "那个家伙是叫做『银』吧。\x02\x03",

            "#2901F他到底有什么目的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x102,
        (
            "#0106F#6P这个我们目前\x01",
            "还不知道……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0012
    ChrTalk(
        0x104,
        (
            "#0305F对了，怎么样，罗伊德。\x02\x03",

            "#0300F关于这次的事件，\x01",
            "也差不多该想到什么了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1097():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1097)
    Sleep(100)
    TurnDirection(0x102, 0x101, 500)

    #C0013
    ChrTalk(
        0x101,
        "#11P#0005F啊，是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0014
    ChrTalk(
        0x101,
        (
            "#11P#0003F恐吓信与邮件……\x02\x03",

            "#0001F或许不是\x01",
            "同一个人写的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x138, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0015
    ChrTalk(
        0x104,
        "#0301F什么……？\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        "#6P#0205F怎么说……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#11P#0004F啊，很简单啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(300)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "立即中止新剧公演。\x01",
            "否则炎之舞姬\x01",
            "将会迎来悲剧──『银』\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #A0019
    AnonymousTalk(
        0x101,
        (
            "#0001F伊莉娅小姐收到的恐吓信\x01",
            "虽然感觉诡异，但措辞简单……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_DB()
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    SetMessageWindowPos(-1, 130, -1, -1)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "而来自『银』的支援请求——\x01",
            "越过试炼，至吾所在。\x01",
            "如是，将授予汝等使命。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    #A0021
    AnonymousTalk(
        0x101,
        (
            "#0003F我们收到的邮件\x01",
            "是古语腔调的挑衅……\x02\x03",

            "#0000F难道不觉得，感觉上相差很多吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0022
    AnonymousTalk(
        0x103,
        "#0201F……确实。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0023
    AnonymousTalk(
        0x104,
        "#0301F被你这么一说，的确如此……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0024
    AnonymousTalk(
        0x102,
        (
            "#0106F……收到邮件时只顾着震惊，\x01",
            "根本没有想到这一层啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0025
    AnonymousTalk(
        0x138,
        (
            "#2P#2905F……呼……\x02\x03",

            "#2901F然后呢，这又能\x01",
            "说明什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(500, 0)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#0003F这个嘛，我认为\x01",
            "存在着多种可能性……\x02\x03",

            "#0001F比如说，『银』拥有手下，\x01",
            "邮件是指派手下代发的。\x02\x03",

            "或者说，正相反。『银』为了让我们那样想，\x01",
            "故意发送了两种文风不同的信件。\x02\x03",

            "#0006F当然了，或许还有其它的可能……\x01",
            "但在目前阶段，继续推理下去\x01",
            "反而会不利于调查吧，有可能会越来越乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x138,
        (
            "#11P#2900F原来如此……\x02\x03",

            "#2904F……嗯，很有意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#6P#0005F咦……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x138,
        (
            "#11P#2902F呵呵……\x01",
            "差不多该到了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    Sound(862, 0, 100, 0)
    OP_24(0x35D)
    EndChrThread(0x101, 0x3)
    OP_68(600, 16000, 0, 2000)
    OP_0D()
    OP_6F(0x1)
    Sleep(800)
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x35D)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_CF7 end

    def Function_5_162A(): pass

    label("Function_5_162A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1662")
    OP_82(0x0, 0xA, 0xBB8, 0x1F4)
    Sleep(2000)
    OP_82(0x0, 0x14, 0x3E8, 0x1F4)
    Sleep(1000)
    Jump("Function_5_162A")

    label("loc_1662")

    Return()

    # Function_5_162A end

    SaveToFile()

Try(main)
