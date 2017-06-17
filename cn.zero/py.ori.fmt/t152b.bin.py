from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t152b.bin",                # FileName
        "t152b",                    # MapName
        "t152b",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t152b",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "梅菲尔护士",             # 3
        "希伦护士",               # 4
        "塞茜尔",                 # 5
        "bt152b",                 # 6
    ))

    ATBonus("ATBonus_22C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_26C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_30C", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt152b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31003.dat", "ms31103.dat", "ms67101.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch29800.itc",                   # 00
        "chr/ch29900.itc",                   # 01
        "apl/ch50362.itc",                   # 02
        "apl/ch50363.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   3,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(204550,  0,       53200,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(204550,  0,       52250,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  100.0,                 9.0,                   -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -12.5,                 -3.0,                  0.20000001788139343,   1.0])

    DeclActor(155770,  0,       53330,   1500,    155770,  1500,    53330,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_38C",          # 00, 0
        "Function_1_444",          # 01, 1
        "Function_2_46E",          # 02, 2
        "Function_3_4B2",          # 03, 3
        "Function_4_4DE",          # 04, 4
        "Function_5_5E5",          # 05, 5
        "Function_6_6C1",          # 06, 6
        "Function_7_2678",         # 07, 7
        "Function_8_26BE",         # 08, 8
        "Function_9_26DB",         # 09, 9
        "Function_10_26F6",        # 0A, 10
        "Function_11_2715",        # 0B, 11
        "Function_12_29E4",        # 0C, 12
        "Function_13_2A5F",        # 0D, 13
        "Function_14_2E8C",        # 0E, 14
    ))


    def Function_0_38C(): pass

    label("Function_0_38C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3CC"),
        (1, "loc_3D8"),
        (2, "loc_3E4"),
        (3, "loc_3F0"),
        (4, "loc_3FC"),
        (5, "loc_408"),
        (6, "loc_414"),
        (SWITCH_DEFAULT, "loc_420"),
    )


    label("loc_3CC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3D8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3E4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3F0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_3FC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_408")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_414")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_420")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_42C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_443")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_42C")

    label("loc_443")

    Return()

    # Function_0_38C end

    def Function_1_444(): pass

    label("Function_1_444")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45E")
    Event(0, 13)

    label("loc_45E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_46D")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 6)

    label("loc_46D")

    Return()

    # Function_1_444 end

    def Function_2_46E(): pass

    label("Function_2_46E")

    SetMapObjFrame(0xFF, "BED01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "BED02", 0x0, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B1")
    Call(0, 12)

    label("loc_4B1")

    Return()

    # Function_2_46E end

    def Function_3_4B2(): pass

    label("Function_3_4B2")

    TalkBegin(0xFE)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "黑手党成员失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_3_4B2 end

    def Function_4_4DE(): pass

    label("Function_4_4DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D")

    #C0002
    ChrTalk(
        0xFE,
        (
            "我们工作结束之后\x01",
            "就在房间里聊天……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "突然间就有黑衣人和狗闯进来，\x01",
            "我们吓得动都不敢动。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "还好你们来了，\x01",
            "总算是放心了。\x01",
            "谢谢，真的很感谢你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5E1")

    label("loc_58D")

    TurnDirection(0xFE, 0xB, 0)

    #C0005
    ChrTalk(
        0xFE,
        (
            "……那些黑衣人和狗\x01",
            "还在外面四处晃悠呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "希伦，可不能离开这里哦。\x02",
    )

    CloseMessageWindow()

    label("loc_5E1")

    TalkEnd(0xFE)
    Return()

    # Function_4_4DE end

    def Function_5_5E5(): pass

    label("Function_5_5E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_669")

    #C0007
    ChrTalk(
        0xFE,
        (
            "塞茜尔前辈和其他护士们\x01",
            "都在值夜班，还留在病房楼里。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "请、请努力救出她们吧。\x01",
            "我和梅菲尔\x01",
            "就躲在这里……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6BD")

    label("loc_669")


    #C0009
    ChrTalk(
        0xFE,
        (
            "呼～…………\x01",
            "安下心之后，就全身无力了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "咦、咦……\x01",
            "脚在发抖，都动不了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BD")

    TalkEnd(0xFE)
    Return()

    # Function_5_5E5 end

    def Function_6_6C1(): pass

    label("Function_6_6C1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("apl/ch50411.itc", 0x1F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05500.itp")
    OP_68(151770, 800, 52760, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21940, 0)
    SetChrPos(0x101, 148870, 0, 55580, 45)
    SetChrPos(0x102, 149220, 0, 54230, 0)
    SetChrPos(0x104, 151350, 0, 55460, 315)
    SetChrPos(0x103, 150150, 100, 57600, 270)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x1F)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 150080, 0, 55940, 0)
    SetMapObjFrame(0xFF, "BED02", 0x1, 0x1)
    FadeToBright(1000, 0)
    OP_68(150040, 800, 56760, 4000)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0xC,
        (
            "#1309F#11P呵呵……\x01",
            "太好了，只是贫血。\x02\x03",

            "#1300F我想她很快\x01",
            "就会醒来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0006F#6P是吗……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        "#0102F#12P太、太好了……\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#0306F#11P嗯……\x01",
            "还以为她会有个三长两短呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0015
    ChrTalk(
        0xC,
        (
            "#1306F#11P不过，真对不起，\x01",
            "只能先让她睡我的床。\x02\x03",

            "#1301F因为病房楼那边\x01",
            "现在没有空着的单间了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8FE():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8FE)
    Sleep(50)

    def lambda_90E():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_90E)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        (
            "#0002F#6P哪里，真是帮大忙了。\x02\x03",

            "在这里的话，\x01",
            "缇欧说不定能更加安心地休息……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0104F#12P塞茜尔小姐……\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)

    #C0018
    ChrTalk(
        0xC,
        (
            "#1309F#5P呵呵，不必放在心上。\x02\x03",

            "#1300F反正我今晚也要值夜班，\x01",
            "让她一直睡到\x01",
            "早上也没关系的。\x02\x03",

            "那么，我先失陪了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#0002F#6P啊，好的……辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x104,
        (
            "#0302F#11P谢啦～！\x01",
            "辛苦了！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(150040, 800, 55260, 3000)

    def lambda_A6C():

        label("loc_A6C")

        TurnDirection(0x101, 0xC, 500)
        Yield()
        Jump("loc_A6C")

    QueueWorkItem2(0x101, 1, lambda_A6C)

    def lambda_A7E():

        label("loc_A7E")

        TurnDirection(0x102, 0xC, 500)
        Yield()
        Jump("loc_A7E")

    QueueWorkItem2(0x102, 1, lambda_A7E)

    def lambda_A90():

        label("loc_A90")

        TurnDirection(0x104, 0xC, 500)
        Yield()
        Jump("loc_A90")

    QueueWorkItem2(0x104, 1, lambda_A90)
    BeginChrThread(0xC, 3, 0, 7)
    WaitChrThread(0xC, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_6F(0x79)
    Sleep(1000)

    def lambda_AC7():
        OP_92(0xFE, 0x24A40, 0xD890, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC7)
    WaitChrThread(0x102, 1)
    OP_68(150000, 800, 57600, 3500)
    MoveCamera(33, 21, 0, 3500)

    def lambda_AFA():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AFA)

    def lambda_B07():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B07)

    def lambda_B14():
        OP_95(0xFE, 150080, 0, 55440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B14)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    TurnDirection(0x102, 0x103, 500)
    OP_6F(0x79)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0008F#6P……缇欧……\x01",
            "我要是能早点察觉的话……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0106F#12P仔细想来，在听约亚西姆医生\x01",
            "说话的时候，她的样子\x01",
            "好像就有点不对劲呢……\x02\x03",

            "#0108F当时正在谈的是……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0306F#11P那些崇拜恶魔的家伙们\x01",
            "制造的药物吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)

    #C0024
    ChrTalk(
        0x103,
        (
            "#5P#40W#2S──没关系，\x01",
            "你们可以尽管问我……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    BeginChrThread(0x103, 0, 0, 8)
    OP_0D()
    Sleep(500)

    #C0025
    ChrTalk(
        0x101,
        "#0002F#6P缇欧……你醒了啊。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        "#0102F#12P太好了……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0304F#12P真是的……\x01",
            "真会让人担心。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x103, 0x0)
    Fade(250)
    Sound(1276, 255, 90, 0)    #voice#Tio
    Sound(804, 0, 100, 0)
    OP_A1(0x103, 0x3E8, 0x6, 0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23)
    OP_0D()
    Sleep(300)
    OP_A1(0x103, 0x3E8, 0x5, 0x24, 0x25, 0x1A, 0x1B, 0x1C)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(800)

    #A0028
    AnonymousTalk(
        0x103,
        (
            "#40W请不用……\x01",
            "太过顾虑我。\x02\x03",

            "身为药物调查任务的负责人，\x01",
            "各位有必要了解……\x02\x03",

            "我所知道的情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0029
    ChrTalk(
        0x101,
        (
            "#0006F#6P……我说啊，缇欧。\x02\x03",

            "#0000F你觉得我们会特意去问那些\x01",
            "你不愿意提起的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        "#5505F#5P#40W哎……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#0100F#12P当然了，调查的确也很重要，\x01",
            "但这完全是两回事。\x02\x03",

            "#0104F对我们来说，你当然是\x01",
            "一起工作的同事……\x02\x03",

            "#0102F但在那之上，你更是\x01",
            "无可替代的同伴啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        "#5508F#5P#40W……啊………\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0300F#12P每个人都会有一些\x01",
            "不想被他人知道的隐情啦。\x02\x03",

            "#0306F嗯，虽说我的过去\x01",
            "已经曝光了一点点……\x02\x03",

            "#0303F阿缇，如果你不愿意\x01",
            "让别人知道你的过去……\x02\x03",

            "#0302F我们肯定会全力支持你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#5506F#5P#40W艾莉前辈……兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#0000F#6P……就是这样。\x02\x03",

            "#0003F但是，如果缇欧\x01",
            "愿意对我们说……\x02\x03",

            "觉得说出来能让心情\x01",
            "变得轻松一点的话……\x02\x03",

            "#0002F那就请务必\x01",
            "让我们帮你分担这个包袱。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#5508F#5P#40W……罗伊德前辈………\x02\x03",

            "#5510F#40W……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sleep(500)

    #C0037
    ChrTalk(
        0x103,
        (
            "#5504F#5P#30W呵呵……亏你说得出\x01",
            "这么令人脸红的台词呢。\x02\x03",

            "不光是罗伊德前辈，\x01",
            "还有艾莉前辈和兰迪前辈……\x02\x03",

            "#5511F你们两位不会也受了\x01",
            "罗伊德前辈的影响吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#0309F#12P哈哈，可能是吧。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#0104F#12P嗯～的确是\x01",
            "无法否认呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0006F#6P你们还是否认吧……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0041
    ChrTalk(
        0x103,
        "#5509F#5P#40W……呵呵…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    Sound(820, 0, 100, 0)
    SetChrPos(0x103, 150000, 200, 56750, 270)
    OP_A1(0x103, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    OP_0D()
    Sleep(500)
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sleep(500)

    #C0042
    ChrTalk(
        0x103,
        (
            "#5506F#5P其实我以前和罗伊德前辈\x01",
            "稍微说过一点点……\x02\x03",

            "我在五岁的时候，\x01",
            "就和父母分离了。\x02\x03",

            "#5508F因为被某个狂热宗教团体\x01",
            "绑架了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    SetCameraDistance(21000, 100000)

    #C0043
    ChrTalk(
        0x101,
        "#0013F#6P！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#0101F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        "#0310F#12P……这……\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0x2, 0x1, 0x0)
    Sleep(300)

    #C0046
    ChrTalk(
        0x103,
        (
            "#5508F#5P那个教团的真正教义与目的，\x01",
            "直到现在也不清楚……\x02\x03",

            "不过，他们当时企图\x01",
            "通过否定女神并崇拜恶魔，\x01",
            "来获取某些东西。\x02\x03",

            "#5506F包括我在内的所有孩子……\x01",
            "应该都是他们的『供品』。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        "#0001F#6P供品……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#5502F#5P虽说是供品，\x01",
            "但并非活祭品……\x02\x03",

            "#5506F……不过，或许也有一些孩子\x01",
            "惨遭那种毒手吧……\x02\x03",

            "总之，那个教团拥有数个据点，\x01",
            "每个据点都用不同的方法\x01",
            "尝试着各种『仪式』。\x02\x03",

            "#5508F而我被带去的\x01",
            "那个据点所进行的……\x02\x03",

            "是被冠名为『仪式』的人体实验。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0107F#12P人、人体实验……！？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#0301F#12P难道说，\x01",
            "你的感应力就是……？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)

    #C0051
    ChrTalk(
        0x103,
        (
            "#5503F#5P#30W……是的。\x02\x03",

            "被迫服用药物……\x01",
            "全身装满传感器……\x02\x03",

            "利用能想出的一切方法，\x01",
            "进行提高五感的实验。\x02\x03",

            "#5508F更以强制性的暗示\x01",
            "和施加精神负荷的方法\x01",
            "来提高所谓的灵感……\x02\x03",

            "三年间……\x01",
            "每天都在重复着这些。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0013F#6P………啊…………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#0108F#12P……怎、怎么会…………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#0303F#12P………………………………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x2, 0x2A, 0x2B)

    #C0055
    ChrTalk(
        0x103,
        (
            "#5502F#5P#30W即使如此……\x01",
            "我或许都还算是幸运的。\x02\x03",

            "除了我以外的孩子……\x01",
            "全都没能忍受下去。\x02\x03",

            "#5508F周围的孩子们\x01",
            "一个接一个地离开……\x02\x03",

            "就在只剩下我一个人的时候，\x01",
            "我终于获得了……\x02\x03",

            "#5506F即使透过坚厚的岩壁，\x01",
            "也能听到其他孩子发出临终哀嚎\x01",
            "的感应能力……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0010F#6P…………！！\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#0106F#12P缇欧…………\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#0308F#12P……这些禽兽………\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#5508F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x7, 0x2B, 0x2A, 0x4, 0x3, 0x2, 0x1, 0x0)

    #C0060
    ChrTalk(
        0x103,
        (
            "#5502F#5P──就在那个时候。\x02\x03",

            "罗伊德前辈的哥哥……\x01",
            "盖伊先生潜入了\x01",
            "我所在的据点。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0061
    ChrTalk(
        0x101,
        "#0011F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#5503F#5P盖伊先生所在的小队\x01",
            "一路制服教团的信徒们，\x01",
            "捣毁了据点。\x02\x03",

            "他们当时遭到了激烈抵抗。据说，到捣毁行动结束时，\x01",
            "几乎所有还活着的教团信徒都自行了断了。\x02\x03",

            "#5508F然后，他们踏过重重尸体，\x01",
            "到达了『仪式堂』……\x02\x03",

            "在那里，盖伊先生发现了\x01",
            "唯一一个幸存下来的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#0008F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        (
            "#5506F#5P被盖伊先生救出的时候……　\x01",
            "我已经衰弱到了极点。\x02\x03",

            "于是便被带到这间医院里，\x01",
            "进行了几个月的疗养……\x02\x03",

            "#5508F……那之后的事情，\x01",
            "就如以前告诉过罗伊德前辈的那样。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0003F#6P……是吗………\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#0106F#12P……缇欧………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Sleep(300)

    #C0067
    ChrTalk(
        0x103,
        (
            "#5504F#5P……真是讽刺呢。\x02\x03",

            "身为受了他这么多照顾，\x01",
            "对他万分感激的人……\x02\x03",

            "#5502F在三年前，听说\x01",
            "盖伊先生不幸殉职的时候，\x01",
            "我却并没有感到十分悲伤。\x02\x03",

            "#5508F简直就像是作为获得力量的代价一般，\x01",
            "我仿佛因此失去了人类应有的感情……\x02\x03",

            "我甚至有过这种不可思议的感慨。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0008F#6P缇欧……\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        "#0308F#12P………………………………\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        (
            "#5504F#5P……或许我\x01",
            "是想问问他吧。\x02\x03",

            "问问那个乐观到耀眼，\x01",
            "并如此坚强的人……\x02\x03",

            "像我这种『有缺陷的存在』\x01",
            "到底该如何生存下去……\x02\x03",

            "#5508F但最终，我没有问到答案\x01",
            "就被爱普斯泰恩财团收留……\x02\x03",

            "然后来到支援科，\x01",
            "和大家一起生活……\x02\x03",

            "#5506F#40W时至今日……\x01",
            "我也还是不太明白。\x02\x03",

            "#40W到底该怎么生存下去才好……\x02\x03",

            "#40W……为什么……\x01",
            "我还活着呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0071
    ChrTalk(
        0x102,
        "#0101F#12P……缇欧……！\x02",
    )

    CloseMessageWindow()
    OP_68(150220, 800, 57570, 1200)
    BeginChrThread(0x102, 3, 0, 10)
    WaitChrThread(0x102, 3)
    StopBGM(0xFA0)
    Sleep(500)
    OP_A1(0x103, 0x3E8, 0x3, 0x5, 0x6, 0x7)
    Sleep(300)
    Fade(1000)
    SetCameraDistance(20500, 0)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrSubChip(0x103, 0x8)
    Sound(820, 0, 100, 0)
    OP_0D()
    #Sound(1269, 255, 65, 0)    #voice#Tio

    #C0072
    ChrTalk(
        0x103,
        "#5P#30W……啊………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x4, 0x8, 0x9, 0xA, 0x9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    #N0073
    NpcTalk(
        0x103,
        "艾莉",
        (
            "#0103F#11P没关系啊……！\x01",
            "不明白也没关系啊……！\x02\x03",

            "#0107F因为我们也和你一样，\x01",
            "有很多事情都不明白啊……！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x103,
        "#5505F#5P#30W………哎…………\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0003F#6P……为什么活着，\x01",
            "怎样活下去才好……\x02\x03",

            "其实根本就没有多少人\x01",
            "知道这个问题的答案。\x02\x03",

            "#0000F我、艾莉，还有兰迪……\x01",
            "大家都是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0304F#12P哈哈，其实我更严重呢，\x01",
            "连自己的道路都要迷失了……\x02\x03",

            "#0302F话说回来，阿缇，\x01",
            "你也太爱钻牛角尖了。\x02\x03",

            "这么困难的问题，\x01",
            "怎么能这么急着寻找答案呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0xA, 0xB, 0xC)

    #C0077
    ChrTalk(
        0x103,
        "#5506F#5P#30W……但、但是………\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#0004F#6P如果你仍然在意的话……\x01",
            "那就继续寻找答案好了。\x02\x03",

            "只是，不需要急躁，\x01",
            "也没必要自己一个人去寻找。\x02\x03",

            "#0000F我们可以陪你一起找嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#5508F#5P#40W………啊……………\x02",
    )

    CloseMessageWindow()

    #N0080
    NpcTalk(
        0x103,
        "艾莉",
        (
            "#0104F#11P我自然不用说……\x02\x03",

            "兰迪、科长、\x01",
            "小琪雅和蔡特，\x01",
            "大家都会帮助你……\x02\x03",

            "陪你一起去寻找\x01",
            "这个难题的答案……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        "#5510F#5P#40W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_A1(0x103, 0x3E8, 0x4, 0xF, 0x10, 0x11, 0x12)

    #C0082
    ChrTalk(
        0x103,
        (
            "#5508F#5P#40W……艾莉前辈和兰迪前辈\x01",
            "好像也都被罗伊德前辈感化了呢……\x02\x03",

            "#5513F真的……我光是听着……\x01",
            "就觉得好难为情……\x02\x03",

            "……为什么会如此………\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0309F#12P嗯，这也是缘分嘛。\x02\x03",

            "从选择留在支援科的那一刻开始，\x01",
            "我们就都成了某人的受害者啦。\x02",
        )
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x103,
        "艾莉",
        (
            "#0109F#11P呵呵，是啊……\x02\x03",

            "#0102F这种难为情的时光\x01",
            "也要大家一起分享才行呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0085
    ChrTalk(
        0x101,
        (
            "#0012F#6P虽然不明白我为什么\x01",
            "变成了加害者……\x02\x03",

            "#0000F不过，我也赞成\x01",
            "大家一起分享时光啦。\x02\x03",

            "#0004F要分享的不光是难为情的时光，\x01",
            "难过的时光、痛苦的时光也一样……\x02\x03",

            "当然了，还有\x01",
            "开心的时光、快乐的时光。\x02\x03",

            "#0002F这不就是『同伴』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x3, 0x12, 0x13, 0x14)
    #Sound(1277, 255, 100, 0)    #voice#Tio
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    OP_A1(0x103, 0x5DC, 0x4, 0x15, 0x16, 0x17, 0x16)
    Sleep(150)

    #C0086
    ChrTalk(
        0x103,
        (
            "#5512F#5P#40W……真是的………\x02\x03",

            "好难为情……好肉麻……\x01",
            "……都这么难堪了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x3E8, 0x4, 0x17, 0x18, 0x19, 0x18)
    Sleep(150)

    #C0087
    ChrTalk(
        0x103,
        (
            "#5513F#5P#40W……但是……\x01",
            "感觉却并不坏……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 0, 0, 9)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(22000, 3000)
    OP_6F(0x10)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人和缇欧一起\x01",
            "乘巴士返回了入夜的克洛斯贝尔市。\x02\x03",

            "到达支援科，让疲惫的缇欧\x01",
            "先回自己的房间休息后……\x02\x03",

            "罗伊德等人才将情况报告给赛尔盖。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    EndChrThread(0x103, 0x3)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    ClearChrFlags(0x103, 0x4)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 6)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_6C1 end

    def Function_7_2678(): pass

    label("Function_7_2678")


    def lambda_267D():
        OP_95(0xFE, 150120, 0, 49160, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_267D)
    Sleep(2700)
    Sound(103, 0, 100, 0)
    Sleep(300)

    def lambda_26A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26A3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sound(104, 0, 100, 0)
    Return()

    # Function_7_2678 end

    def Function_8_26BE(): pass

    label("Function_8_26BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26DA")
    OP_A1(0xFE, 0x3E8, 0x3, 0x1F, 0x1E, 0x1D)
    Sleep(4000)
    Jump("Function_8_26BE")

    label("loc_26DA")

    Return()

    # Function_8_26BE end

    def Function_9_26DB(): pass

    label("Function_9_26DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26F5")
    OP_A1(0xFE, 0x3E8, 0x4, 0x15, 0x16, 0x17, 0x16)
    Jump("Function_9_26DB")

    label("loc_26F5")

    Return()

    # Function_9_26DB end

    def Function_10_26F6(): pass

    label("Function_10_26F6")


    def lambda_26FB():
        OP_96(0xFE, 0x24BBC, 0x0, 0xDB92, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26FB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_26F6 end

    def Function_11_2715(): pass

    label("Function_11_2715")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch31000.itc", 0x23)
    LoadChrToIndex("chr/ch31050.itc", 0x24)
    LoadChrToIndex("chr/ch31051.itc", 0x25)
    LoadChrToIndex("chr/ch31100.itc", 0x26)
    LoadChrToIndex("chr/ch31150.itc", 0x27)
    LoadChrToIndex("chr/ch31151.itc", 0x28)
    OP_68(99060, 1000, 12500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 97690, 0, 11720, 270)
    SetChrPos(0x102, 98330, 0, 10890, 270)
    SetChrPos(0x103, 99270, 0, 12710, 270)
    SetChrPos(0x104, 100540, 0, 12610, 270)
    SetChrPos(0x106, 99810, 0, 10770, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x25)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, 85000, 0, 12690, 90)
    SetChrPos(0x9, 85000, 0, 11100, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(92640, 1000, 12400, 0)
    OP_68(97340, 1000, 12400, 1750)
    SetCameraDistance(17500, 1750)

    def lambda_28F7():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_28F7)

    def lambda_290C():
        OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_290C)
    Sleep(750)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(500)
    Battle("BattleInfo_30C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 12)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    SetChrPos(0x0, 98700, 0, 11800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE1, 1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_2715 end

    def Function_12_29E4(): pass

    label("Function_12_29E4")

    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x1)
    SetChrPos(0x8, 93740, 0, 13280, 270)
    SetChrPos(0x9, 94870, 0, 10340, 90)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    Return()

    # Function_12_29E4 end

    def Function_13_2A5F(): pass

    label("Function_13_2A5F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(200880, 900, 52400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 199450, 0, 49200, 0)
    SetChrPos(0x102, 200570, 0, 49200, 0)
    SetChrPos(0x103, 199450, 0, 47900, 0)
    SetChrPos(0x104, 200570, 0, 47900, 0)
    SetChrPos(0x106, 200000, 0, 46600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_68(201940, 900, 53610, 3000)

    def lambda_2B56():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B56)

    def lambda_2B6B():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B6B)

    def lambda_2B80():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B80)

    def lambda_2B95():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B95)

    def lambda_2BAA():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2BAA)
    Sleep(200)

    def lambda_2BC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BC2)

    def lambda_2BD3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2BD3)
    Sleep(500)

    def lambda_2BE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2BE7)

    def lambda_2BF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2BF8)
    Sleep(500)

    def lambda_2C0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2C0C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_2C25():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C25)

    def lambda_2C32():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C32)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_2C47():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C47)

    def lambda_2C54():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C54)
    WaitChrThread(0x106, 1)

    def lambda_2C65():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2C65)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2CE2():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2CE2)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_2D04():
        TurnDirection(0xFE, 0x101, 600)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D04)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)

    #C0089
    ChrTalk(
        0xA,
        "#5P咿……！\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        "#11P不、不要……！\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#0100F#6P请放心吧，\x01",
            "我们是警察。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0092
    ChrTalk(
        0xB,
        "#11P女、女人……？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#5P警察……\x01",
            "是来救我们的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x102,
        (
            "#0103F#6P嗯，我们正在制服入侵者，\x01",
            "确保这里的安全。\x02\x03",

            "#0101F请你们暂时\x01",
            "留在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xA,
        "#5P明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        "#11P请、请加油吧～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_2C(0x4D, 0x1)
    SetChrPos(0x0, 200200, 0, 52410, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0xE1, 2)
    OP_29(0x4D, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_13_2A5F end

    def Function_14_2E8C(): pass

    label("Function_14_2E8C")

    TalkBegin(0xFF)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis000.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "塞茜尔和罗伊德，\x01",
            "还有一位面容精悍的青年\x01",
            "的合影照片摆在这里。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2FB1")

    #A0098
    AnonymousTalk(
        0x101,
        (
            "#0008F（……是和塞茜尔姐姐\x01",
            "  还有大哥一起拍的照片。）\x02\x03",

            "（我一直都寸步不离地带在身上，\x01",
            "  原来塞茜尔姐姐也一直摆着啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_303A")

    label("loc_2FB1")


    #A0099
    AnonymousTalk(
        0x101,
        (
            "#0005F（啊……是和塞茜尔姐姐\x01",
            "  还有大哥一起拍的照片。）\x02\x03",

            "#0003F（既然摆着这张照片，\x01",
            "  也就是说，这里莫非是\x01",
            "  塞茜尔姐姐的宿舍吗？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_303A")

    SetScenarioFlags(0x69, 5)

    label("loc_303D")

    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_2E8C end

    SaveToFile()

Try(main)
