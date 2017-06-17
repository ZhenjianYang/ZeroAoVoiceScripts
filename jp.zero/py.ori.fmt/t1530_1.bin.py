from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1530_1.bin",                # FileName
        "t1530",                    # MapName
        "t1530",                    # Location
        0x004F,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 79, 0, 255, 0, 255],
    )

    BuildStringList((
        "t1530_1",                # 0
    ))

    ScpFunction((
        "Function_0_1D0",          # 00, 0
        "Function_1_1D4",          # 01, 1
        "Function_2_126E",         # 02, 2
        "Function_3_1272",         # 03, 3
        "Function_4_1F37",         # 04, 4
        "Function_5_2DE7",         # 05, 5
        "Function_6_2E95",         # 06, 6
        "Function_7_30F3",         # 07, 7
        "Function_8_400E",         # 08, 8
        "Function_9_4920",         # 09, 9
        "Function_10_4A80",        # 0A, 10
        "Function_11_5889",        # 0B, 11
        "Function_12_5E33",        # 0C, 12
        "Function_13_5F6C",        # 0D, 13
        "Function_14_6B4D",        # 0E, 14
        "Function_15_6C2B",        # 0F, 15
        "Function_16_6CB6",        # 10, 16
        "Function_17_6DE6",        # 11, 17
        "Function_18_7955",        # 12, 18
        "Function_19_7A4E",        # 13, 19
        "Function_20_8084",        # 14, 20
        "Function_21_8400",        # 15, 21
        "Function_22_84DB",        # 16, 22
        "Function_23_8584",        # 17, 23
        "Function_24_863D",        # 18, 24
        "Function_25_8A7D",        # 19, 25
        "Function_26_8A87",        # 1A, 26
        "Function_27_8C2F",        # 1B, 27
        "Function_28_8DE0",        # 1C, 28
        "Function_29_8FA1",        # 1D, 29
        "Function_30_92FE",        # 1E, 30
        "Function_31_9570",        # 1F, 31
        "Function_32_96DE",        # 20, 32
        "Function_33_984A",        # 21, 33
        "Function_34_997E",        # 22, 34
        "Function_35_9B0C",        # 23, 35
        "Function_36_9C8F",        # 24, 36
        "Function_37_9E03",        # 25, 37
        "Function_38_A0BB",        # 26, 38
        "Function_39_A238",        # 27, 39
        "Function_40_A370",        # 28, 40
        "Function_41_A640",        # 29, 41
        "Function_42_A76F",        # 2A, 42
        "Function_43_A8BD",        # 2B, 43
        "Function_44_A9FF",        # 2C, 44
        "Function_45_ACCF",        # 2D, 45
        "Function_46_AE6D",        # 2E, 46
        "Function_47_AFE7",        # 2F, 47
        "Function_48_B132",        # 30, 48
        "Function_49_B2BC",        # 31, 49
        "Function_50_B538",        # 32, 50
        "Function_51_B678",        # 33, 51
        "Function_52_B87C",        # 34, 52
        "Function_53_BA4D",        # 35, 53
        "Function_54_BC14",        # 36, 54
        "Function_55_BDB0",        # 37, 55
        "Function_56_BF39",        # 38, 56
        "Function_57_C063",        # 39, 57
        "Function_58_C1E1",        # 3A, 58
        "Function_59_C351",        # 3B, 59
        "Function_60_C4E7",        # 3C, 60
        "Function_61_C6E8",        # 3D, 61
        "Function_62_C8C2",        # 3E, 62
        "Function_63_CAAF",        # 3F, 63
        "Function_64_CC11",        # 40, 64
        "Function_65_CD84",        # 41, 65
        "Function_66_CEFC",        # 42, 66
        "Function_67_D077",        # 43, 67
        "Function_68_D0B9",        # 44, 68
        "Function_69_D0E4",        # 45, 69
        "Function_70_D1A5",        # 46, 70
        "Function_71_D327",        # 47, 71
        "Function_72_D3A4",        # 48, 72
        "Function_73_D6B9",        # 49, 73
        "Function_74_D916",        # 4A, 74
        "Function_75_E009",        # 4B, 75
        "Function_76_E6CA",        # 4C, 76
        "Function_77_F880",        # 4D, 77
        "Function_78_101DF",       # 4E, 78
    ))


    def Function_0_1D0(): pass

    label("Function_0_1D0")

    Call(1, 1)
    Return()

    # Function_0_1D0 end

    def Function_1_1D4(): pass

    label("Function_1_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EA")
    Call(0, 9)
    Jump("loc_126D")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_200")
    Call(0, 14)
    Jump("loc_126D")

    label("loc_200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D")
    Call(1, 76)
    Jump("loc_126D")

    label("loc_21D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_38D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312")

    #C0001
    ChrTalk(
        0x8,
        (
            "今朝方、黒月貿易公司の方々が\x01",
            "退院されていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "まだ完治されていなかったのですが\x01",
            "歩けるからと無理矢理に……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30A")

    #C0003
    ChrTalk(
        0x10A,
        (
            "#0603Fフン……さすがツァオの部下か。\x01",
            "なかなかタフに出来ているようだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30A")

    SetScenarioFlags(0x0, 0)
    Jump("loc_388")

    label("loc_312")


    #C0004
    ChrTalk(
        0x8,
        (
            "今朝方、黒月貿易公司の方々が\x01",
            "退院されていきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "銃を受けた傷もあるので\x01",
            "お止めしたかったんですけどね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_388")

    Jump("loc_126A")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3FC")

    #C0006
    ChrTalk(
        0x8,
        (
            "ヨアヒム先生とお話できたようで\x01",
            "なによりでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "またいつでもいらっしゃってくださいね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_484")

    #C0008
    ChrTalk(
        0x8,
        (
            "ヨアヒム先生が研究棟４階の\x01",
            "研究室でお待ちです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "……サボリに行かないうちに\x01",
            "向かった方がよろしいかと思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_484")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_76C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D5")

    #C0010
    ChrTalk(
        0x8,
        (
            "聖ウルスラ病院へようこそ。\x01",
            "本日はどういったご用件でしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x109,
        (
            "#0500Fウルスラ病院に来るのは\x01",
            "結構久しぶりですね。\x02\x03",

            "例の狼魔獣の事件以来、この辺りには\x01",
            "巡回に来る程度でしたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0000Fはは、こう言っちゃなんだけど\x01",
            "曹長は病気になんかかからなそうだしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#0504Fええ、もちろんですよ。\x02\x03",

            "#0500F警備隊に入ってからは\x01",
            "小さな病気もしないように\x01",
            "体調管理には気を遣ってますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ふふ、素晴らしいことですね。\x01",
            "一番大事なのは病院に\x01",
            "かからないようにすることですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "でも、何かあったらすぐご相談くださいね。\x01",
            "個人じゃどうにも出来ないことも\x01",
            "あると思いますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 5)
    Jump("loc_767")

    label("loc_6D5")


    #C0016
    ChrTalk(
        0x8,
        (
            "一番大事なのは病院にかからないよう\x01",
            "健康管理をすることだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "ふふ、そちらの警備隊員さんの心がけは\x01",
            "素晴らしいことだと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_767")

    Jump("loc_126A")

    label("loc_76C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_77D")
    Call(1, 26)
    Jump("loc_126A")

    label("loc_77D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7FD")

    #C0018
    ChrTalk(
        0x8,
        (
            "ヨアヒム先生の研究室は\x01",
            "研究棟の４階にありますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "病棟の屋上に出れば\x01",
            "研究棟の場所はすぐ分かるはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AC")

    #C0020
    ChrTalk(
        0x8,
        "ようこそ、ウルスラ病院へ。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "本日、教授の方々は\x01",
            "教授会のため出張となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "担当の先生をお確かめの上\x01",
            "診察手続きをお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_920")

    label("loc_8AC")


    #C0023
    ChrTalk(
        0x8,
        (
            "本日、教授の方々は\x01",
            "教授会のため出張となっております。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "担当の先生をお確かめの上\x01",
            "診察手続きをお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_920")

    Jump("loc_126A")

    label("loc_925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_A9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A06")

    #C0025
    ChrTalk(
        0x8,
        (
            "今日は観光客の方が\x01",
            "診察を受けに来ているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "最先端の医療を体験したい気持ちは\x01",
            "分かる気がするんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "それで具合の悪い患者さんの\x01",
            "診察順が遅くなるのは\x01",
            "なにか違う気がしますね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A97")

    label("loc_A06")


    #C0028
    ChrTalk(
        0x8,
        (
            "健康診断などをしに\x01",
            "観光客の方が来ているみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "……外来として来ている以上\x01",
            "無下にはしませんけど……\x01",
            "動機を知るとなんだか複雑です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A97")

    Jump("loc_126A")

    label("loc_A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_B82")
    OP_93(0x8, 0x10A, 0x0)
    OP_4B(0x17, 0xFF)

    #C0030
    ChrTalk(
        0x8,
        "まぁ、ディーター総裁……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "今年もお越しいただいて\x01",
            "本当にありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        "きっと患者の皆様も喜ばれますわ。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x17,
        (
            "#2804Fなに、気にしないでくれたまえ。\x02\x03",

            "私の個人的な我が侭なのだからね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x17, 0xFF)
    Jump("loc_126A")

    label("loc_B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C32")

    #C0034
    ChrTalk(
        0x8,
        (
            "セシルさんたち看護師の方は、\x01",
            "うまく分担して休暇を取ったとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "うらやましいです。\x01",
            "事務方は人が少ないですから\x01",
            "なかなか休めないんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1C")

    label("loc_C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CA3")

    #C0036
    ChrTalk(
        0x8,
        (
            "またなにかあったら\x01",
            "病院にお越しくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "誠意を以って\x01",
            "対応させていただきますから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1C")

    label("loc_CA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_D10")

    #C0038
    ChrTalk(
        0x8,
        (
            "ヨアヒム先生に\x01",
            "早く戻っていただかないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        "皆さん、どうかよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1C")

    label("loc_D10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_D1C")

    label("loc_D1C")

    Jump("loc_126A")

    label("loc_D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD6")

    #C0040
    ChrTalk(
        0x8,
        (
            "職員寮のキルシュ寮長や\x01",
            "マローネさんもクラーク事務長の\x01",
            "部下にあたるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "ここだけの話、事務長は\x01",
            "キルシュ寮長には\x01",
            "頭が上がらないそうです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E24")

    label("loc_DD6")


    #C0042
    ChrTalk(
        0x8,
        (
            "ここだけの話、クラーク事務長は\x01",
            "キルシュ寮長には\x01",
            "頭が上がらないそうです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E24")

    Jump("loc_126A")

    label("loc_E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_F8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF8")

    #C0043
    ChrTalk(
        0x8,
        (
            "院長は主に各国を渡り歩いて\x01",
            "技術交流や人材発掘をしているので\x01",
            "なかなか病院にいらっしゃらないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "実は、かく言う私も\x01",
            "お会いしたことがなくて……\x01",
            "どんな方なんでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F85")

    label("loc_EF8")


    #C0045
    ChrTalk(
        0x8,
        (
            "院長はとても忙しい方ですから、\x01",
            "なかなか病院に\x01",
            "いらっしゃらないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "実質、病院の経営は教授たちに\x01",
            "任されていることになりますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F85")

    Jump("loc_126A")

    label("loc_F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_FFB")

    #C0047
    ChrTalk(
        0x8,
        "本日の外来受付は終了しました。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "遅い時間になると物騒です、\x01",
            "お見舞いの方はお急ぎください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_10A0")

    #C0049
    ChrTalk(
        0x8,
        (
            "夕方が近づいて、外来のお客様も、\x01",
            "少しずつはけてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "リットンさんのこともありますし、\x01",
            "暗くならないうちに\x01",
            "皆さんが帰れるようにしないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_10A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1261")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EC")

    #C0051
    ChrTalk(
        0x8,
        "……あの、セシルさん。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "一応職場ですし、\x01",
            "人前でああいうスキンシップは\x01",
            "慎んだ方がいいと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0006F……面目ないです。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x136,
        (
            "#1305Fあら、ロイドが謝ることは\x01",
            "ないでしょう？\x02\x03",

            "#1309Fふふ……セラさん、\x01",
            "うらやましいんでしょ？\x01",
            "私にこーんな可愛い弟がいて。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        "はぁ……もう好きにしてください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_125C")

    label("loc_11EC")


    #C0056
    ChrTalk(
        0x8,
        (
            "……もう止めませんので\x01",
            "抱き合うなりなんなり\x01",
            "好きにすればいいと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0006F（呆れられてる……）\x02",
    )

    CloseMessageWindow()

    label("loc_125C")

    Jump("loc_126A")

    label("loc_1261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_126A")

    label("loc_126A")

    TalkEnd(0x8)

    label("loc_126D")

    Return()

    # Function_1_1D4 end

    def Function_2_126E(): pass

    label("Function_2_126E")

    Call(1, 3)
    Return()

    # Function_2_126E end

    def Function_3_1272(): pass

    label("Function_3_1272")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1303")

    #C0058
    ChrTalk(
        0x9,
        (
            "病院長が不在の中ですが\x01",
            "経営状態は非常に良好と言えます。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "これもひとえに、長年で培われた\x01",
            "病院への信頼のお陰でしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_139D")

    #C0060
    ChrTalk(
        0x9,
        (
            "受付に病院内の連絡係など、\x01",
            "セラくんはよく働いてくれています。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "単純な仕事量ならセシルさんにも\x01",
            "ひけをとらないんじゃないでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1421")

    #C0062
    ChrTalk(
        0x9,
        (
            "運ばれてきた患者は必ず助けるのが\x01",
            "ウルスラ病院のモットーです。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "たとえ極悪人が相手でも\x01",
            "それは変わりませんよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14D9")

    #C0064
    ChrTalk(
        0x9,
        (
            "当病院は各国各機関から\x01",
            "資金を受けていますが、\x01",
            "経営方針は実に倹約的です。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "そうした資金はできるだけ、\x01",
            "通常診察を受けられない方に\x01",
            "使われるようにしてあるのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_14D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1586")

    #C0066
    ChrTalk(
        0x9,
        (
            "この病院に勤めている以上、\x01",
            "私たち事務もやり方は違えど\x01",
            "患者さんを助ける為に動いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "患者さんたちが笑顔で退院されると\x01",
            "幸せな気持ちになりますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_162F")

    #C0068
    ChrTalk(
        0x9,
        (
            "教授たちは研修医への指導と研究、\x01",
            "回診の仕事を兼ねていますから\x01",
            "お忙しい方ばかりなのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x9,
        (
            "ヨアヒム先生を見ていると\x01",
            "そうは見えないんですけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_17A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F1")

    #C0070
    ChrTalk(
        0x9,
        (
            "私はこの病院の事務全般を\x01",
            "統括しているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "設備への予算分配から\x01",
            "導力ネットワークの整備まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x9,
        (
            "仕事が多くてなかなか大変ですが\x01",
            "やりがいはありますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_179C")

    label("loc_16F1")


    #C0073
    ChrTalk(
        0x9,
        (
            "特に、導力ネットの整備が大変なのです。\x01",
            "病院には私以外に操作できる方が\x01",
            "いらっしゃいませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "できればクロスベル市のほうから\x01",
            "技師の一人でも回して欲しい所です。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179C")

    Jump("loc_1F33")

    label("loc_17A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1869")
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0x42, 0xF, 0x0)
    OP_4B(0x42, 0xFF)

    #C0075
    ChrTalk(
        0x9,
        (
            "健康診断をご希望ですか？\x01",
            "それでは、こちらの書類に\x01",
            "サインをお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "初診ですので\x01",
            "お時間頂くと思いますが\x01",
            "お待ちいただいても？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x42,
        "ああ、構わないよ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x42, 0xFF)
    Jump("loc_1F33")

    label("loc_1869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18FD")

    #C0078
    ChrTalk(
        0x9,
        (
            "毎年、ディーター総裁には\x01",
            "入院患者全員に行き渡るほどの\x01",
            "プレゼントを寄贈して頂いています。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "いやはや、本当に出来たお方ですよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_18FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A05")

    #C0080
    ChrTalk(
        0x9,
        (
            "受付にカード制度を導入するか\x01",
            "検討しているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "事前に個人情報を登録した\x01",
            "カードキーを用意して、\x01",
            "受付の手間を削減するものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "ただ、カードの量産体制や\x01",
            "個人情報の保護などの問題もありますから\x01",
            "開発が難航しているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A90")

    label("loc_1A05")


    #C0083
    ChrTalk(
        0x9,
        (
            "受付にカード制度を導入するか\x01",
            "検討しているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "ただ、こちらはなかなか\x01",
            "開発が難航していまして……\x01",
            "当分先の話になりそうですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A90")

    Jump("loc_1F33")

    label("loc_1A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B38")

    #C0085
    ChrTalk(
        0x9,
        (
            "寮の食堂で昼食を食べていたら\x01",
            "職員が昼時に来るなと\x01",
            "叩き出されてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "いやはや……\x01",
            "キルシュ寮長には\x01",
            "頭が上がりません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B8C")

    label("loc_1B38")


    #C0087
    ChrTalk(
        0x9,
        (
            "いやはや……\x01",
            "キルシュ寮長には\x01",
            "頭が上がりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        "……女性は強し、ですね。\x02",
    )

    CloseMessageWindow()

    label("loc_1B8C")

    Jump("loc_1F33")

    label("loc_1B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C82")

    #C0089
    ChrTalk(
        0x9,
        (
            "ウルスラ病院は導力ネットワークで\x01",
            "クロスベル市と繋がっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "試験的にではあるんですが\x01",
            "導力ネットワークを使った\x01",
            "予約サービスなどもあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "ただ、普及率の問題で\x01",
            "あまり活用されていないですけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D19")

    label("loc_1C82")


    #C0092
    ChrTalk(
        0x9,
        (
            "導力ネットワークでの\x01",
            "事前予約サービスを使えば、\x01",
            "待ち時間なくスムーズに診察できます。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "ただ、普及率の問題で\x01",
            "あまり活用されていないですけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D19")

    Jump("loc_1F33")

    label("loc_1D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1DB1")

    #C0094
    ChrTalk(
        0x9,
        (
            "警察の皆様……\x01",
            "フェンスの設置にご協力\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "これで魔獣が入り込むようなことが\x01",
            "なくなればいいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1DF2")

    #C0096
    ChrTalk(
        0x9,
        (
            "警察の皆様……\x01",
            "何か捜査に進展はありましたか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1E9F")

    #C0097
    ChrTalk(
        0x9,
        (
            "病院施設に魔獣が入ることなど\x01",
            "信じたくはありませんが……\x01",
            "本当だとしたら由々しき事態です。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "リットン君が魔獣に襲われた証拠を\x01",
            "押さえてほしいと思います。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F33")

    label("loc_1E9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1F33")

    #C0099
    ChrTalk(
        0x9,
        (
            "聖ウルスラ医科大学病院へ\x01",
            "ようこそいらっしゃいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "受付はもう一方のカウンターで\x01",
            "承っております。\x01",
            "そちらをご利用くださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F33")

    TalkEnd(0x9)
    Return()

    # Function_3_1272 end

    def Function_4_1F37(): pass

    label("Function_4_1F37")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FB0")
    TurnDirection(0xFE, 0x3C, 0)

    #C0101
    ChrTalk(
        0xFE,
        "あら、今日はどういったご用件でしょう。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "初診の方は、一旦受付で\x01",
            "手続きをお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_1FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2032")

    #C0103
    ChrTalk(
        0xFE,
        (
            "運び込まれた人は、\x01",
            "今はＩＣＵ横の病室で休んでいるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "命に別状はないし、\x01",
            "明日にも歩けるようになるそうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_2032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_20E1")

    #C0105
    ChrTalk(
        0xFE,
        (
            "今日運び込まれた患者さん、\x01",
            "とりあえず一命はとりとめたみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "……怪我の様子があきらかに\x01",
            "銃や殴打によるものみたいだから\x01",
            "どうにもキナ臭いんだけどね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_20E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_215E")
    TurnDirection(0xFE, 0x35, 0)

    #C0107
    ChrTalk(
        0xFE,
        (
            "あらボク、大丈夫？\x01",
            "けっこう熱があるみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "この体温計を脇に挟んで、\x01",
            "大人しく待っててね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_215E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_23DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2341")

    #C0109
    ChrTalk(
        0xFE,
        (
            "なになに、また何か\x01",
            "トラブルに巻き込まれてるわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0006Fい、いや……\x01",
            "そこまで大したことじゃ\x01",
            "ないんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "ふふ、弟君を見てると飽きないわね。\x01",
            "話のネタ的にも。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_225C")

    #C0112
    ChrTalk(
        0x102,
        "#0100Fふふ、人気者ねぇロイド。\x02",
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_225C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22BD")

    #C0113
    ChrTalk(
        0x103,
        (
            "#0200Fロイドさんがいるから\x01",
            "色々な事件が起きているのかも\x01",
            "しれませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231B")

    label("loc_22BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_231B")

    #C0114
    ChrTalk(
        0x104,
        (
            "#0306Fナースたちの間で\x01",
            "噂になってるってのか？\x01",
            "つくづくうらやましい奴……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231B")


    #C0115
    ChrTalk(
        0x101,
        "#0006F勘弁してくれよ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23D9")

    label("loc_2341")


    #C0116
    ChrTalk(
        0xFE,
        "ふふ、弟君を見てると飽きないわ。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "で……セシル先輩とは\x01",
            "あれから進展はあったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0011Fい、今はそれどころではないので\x01",
            "失礼しますっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23D9")

    Jump("loc_2DE3")

    label("loc_23DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2553")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D6")

    #C0119
    ChrTalk(
        0xFE,
        (
            "寝てたら急患でたたき起こされるわ\x01",
            "休みの日なんて殆どないわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "考えてみればこの仕事も、\x01",
            "相当好きじゃないと\x01",
            "続けられない仕事よね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "私はあんまり根気のある方じゃ\x01",
            "ないと思ってたんだけど、\x01",
            "意外とタフなのかも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_254E")

    label("loc_24D6")


    #C0122
    ChrTalk(
        0xFE,
        (
            "この仕事を続けるには\x01",
            "相当好きじゃないと無理ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "セシル先輩なんか、看護師の仕事は\x01",
            "すごく気に入ってそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254E")

    Jump("loc_2DE3")

    label("loc_2553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278B")

    #C0124
    ChrTalk(
        0xFE,
        (
            "奥の部屋には集中治療室#10RＩ　　Ｃ　　Ｕ#や\x01",
            "レントゲン写真を撮るための\x01",
            "部屋があるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "レントゲンっていうのは\x01",
            "最近、レミフェリアの機器メーカーと\x01",
            "共同開発した最新の医療機器なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "特殊な感光クオーツを使って、\x01",
            "人間の骨や内臓の様子を透過して\x01",
            "写真に収めてしまうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "これがあれば、切開しなくても\x01",
            "病巣を発見できたりするのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x103,
        (
            "#0205F開発中とは聞いていたんですが……\x01",
            "すでに実用レベルにありましたか。\x02\x03",

            "#0204Fさすがはウルスラ病院ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0006F……は、半分くらい\x01",
            "意味分からなかったけど……\x01",
            "何となく凄いのは伝わってきたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2861")

    label("loc_278B")


    #C0130
    ChrTalk(
        0xFE,
        (
            "レントゲンっていうのは\x01",
            "人間の骨や内臓の様子を透過して\x01",
            "写真に収めてしまう医療機器なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "これがあれば、切開しなくても\x01",
            "病巣を発見できたりするのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "……まぁ、私も詳しいことは\x01",
            "殆ど分からないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2861")

    Jump("loc_2DE3")

    label("loc_2866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2913")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2881")
    Call(1, 23)
    Jump("loc_290E")

    label("loc_2881")


    #C0133
    ChrTalk(
        0xFE,
        (
            "セシル先輩はほんと働き者よ。\x01",
            "自分の仕事だけでなく\x01",
            "他人のフォローまでやってるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生あたりには\x01",
            "是非見習わせたいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290E")

    Jump("loc_2DE3")

    label("loc_2913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_29DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A0")

    #C0135
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院に勤めて数年経つけど、\x01",
            "この時期はやっぱり忙しいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "やっぱり休む暇なんて\x01",
            "ないのが普通よね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29D5")

    label("loc_29A0")


    #C0137
    ChrTalk(
        0xFE,
        (
            "今考えると、初日に休めて\x01",
            "ラッキーだったなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D5")

    Jump("loc_2DE3")

    label("loc_29DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2A7E")

    #C0138
    ChrTalk(
        0xFE,
        (
            "ゲイリー教授の息子さん、\x01",
            "クロスベル市の不良グループに\x01",
            "いるらしいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "多分、反抗期なのよね。\x01",
            "時間が経てば溝なんて\x01",
            "なくなると思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2B31")

    #C0140
    ChrTalk(
        0xFE,
        (
            "セシル先輩にアルカンシェルの\x01",
            "イリア・プラティエと\x01",
            "知り合いなのかって聞いてみたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "……普通に教えてくれちゃった。\x01",
            "べつに秘密にしてたわけじゃないみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_2B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C2E")

    #C0142
    ChrTalk(
        0xFE,
        (
            "セシル先輩って、\x01",
            "すごい有名人と知り合いらしいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        "弟君、知ってた？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF6")

    #C0144
    ChrTalk(
        0x101,
        "#0005F…………えっと……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)

    #C0145
    ChrTalk(
        0xFE,
        (
            "うーん、知らないか。\x01",
            "誰なのかしらねー？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C26")

    label("loc_2BF6")


    #C0146
    ChrTalk(
        0x101,
        "#0003F（……多分、イリアさんのことだな。）\x02",
    )

    CloseMessageWindow()

    label("loc_2C26")

    SetScenarioFlags(0x0, 2)
    Jump("loc_2C83")

    label("loc_2C2E")


    #C0147
    ChrTalk(
        0xFE,
        (
            "セシル先輩って、\x01",
            "すごい有名人と知り合いらしいわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        "誰のことなのかなぁ……\x02",
    )

    CloseMessageWindow()

    label("loc_2C83")

    Jump("loc_2DE3")

    label("loc_2C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2D0A")

    #C0149
    ChrTalk(
        0xFE,
        (
            "ゲイリー教授のお子さん、\x01",
            "妙な連中とつるんでるらしいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "あんな立派な父親がいて、\x01",
            "何が不満なのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_2D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2D63")

    #C0151
    ChrTalk(
        0xFE,
        "あら、診察待ちの方かしら？\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "受付が済んでるなら\x01",
            "座って待っててね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_2D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2D99")

    #C0153
    ChrTalk(
        0xFE,
        "……次の診察は……あの患者さんね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DE3")

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB4")
    Call(1, 5)
    Jump("loc_2DE3")

    label("loc_2DB4")


    #C0154
    ChrTalk(
        0xFE,
        (
            "この体温計を\x01",
            "脇に挟んでおいてくださいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE3")

    TalkEnd(0xFE)
    Return()

    # Function_4_1F37 end

    def Function_5_2DE7(): pass

    label("Function_5_2DE7")

    SetChrSubChip(0x19, 0x0)
    OP_4B(0xA, 0xFF)

    #C0155
    ChrTalk(
        0xA,
        "今日はどうされました？\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x19,
        (
            "ああ、どうにも熱っぽくてね……\x01",
            "どうも風邪をひいてしまったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        (
            "では、診察待ちの間に\x01",
            "お熱を測っておきましょうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    SetChrSubChip(0x19, 0x0)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_5_2DE7 end

    def Function_6_2E95(): pass

    label("Function_6_2E95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB3")
    Call(1, 11)
    Jump("loc_2ECD")

    label("loc_2EB3")


    #C0158
    ChrTalk(
        0xFE,
        "ほりゃぁあああ……！\x02",
    )

    CloseMessageWindow()

    label("loc_2ECD")

    Jump("loc_30EF")

    label("loc_2ED2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2EE0")
    Jump("loc_30EF")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2EEE")
    Jump("loc_30EF")

    label("loc_2EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2EFC")
    Jump("loc_30EF")

    label("loc_2EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2F0A")
    Jump("loc_30EF")

    label("loc_2F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2F18")
    Jump("loc_30EF")

    label("loc_2F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2F26")
    Jump("loc_30EF")

    label("loc_2F26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F41")
    Call(1, 11)
    Jump("loc_2F59")

    label("loc_2F41")


    #C0159
    ChrTalk(
        0xFE,
        "フヌギギギ……！！\x02",
    )

    CloseMessageWindow()

    label("loc_2F59")

    Jump("loc_30EF")

    label("loc_2F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2F6C")
    Jump("loc_30EF")

    label("loc_2F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F7A")
    Jump("loc_30EF")

    label("loc_2F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2F88")
    Jump("loc_30EF")

    label("loc_2F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FA3")
    Call(1, 73)
    Jump("loc_308F")

    label("loc_2FA3")

    OP_4B(0x47, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0160
    ChrTalk(
        0xB,
        (
            "ところで……例の件、\x01",
            "考えてくれたかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x47,
        (
            "あ……研究棟で\x01",
            "特別講義をして欲しいって話ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x47,
        (
            "うーん、記念祭も近づいてきて\x01",
            "段々忙しくなってますからねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xB,
        (
            "ふむ……残念だが、\x01",
            "それなら無理にとは言わんよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x47, 0xFF)
    OP_4C(0xB, 0xFF)

    label("loc_308F")

    Jump("loc_30EF")

    label("loc_3094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_30CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AF")
    Call(1, 11)
    Jump("loc_30C5")

    label("loc_30AF")


    #C0164
    ChrTalk(
        0xFE,
        "グニニニ……！！\x02",
    )

    CloseMessageWindow()

    label("loc_30C5")

    Jump("loc_30EF")

    label("loc_30CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_30D8")
    Jump("loc_30EF")

    label("loc_30D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_30E6")
    Jump("loc_30EF")

    label("loc_30E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_30EF")

    label("loc_30EF")

    TalkEnd(0xFE)
    Return()

    # Function_6_2E95 end

    def Function_7_30F3(): pass

    label("Function_7_30F3")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3187")
    Jump("loc_31D1")

    label("loc_3187")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_31A7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31D1")

    label("loc_31A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31C7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_31D1")

    label("loc_31C7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31D1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3204")
    Jump("loc_4006")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_33E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3352")

    #C0165
    ChrTalk(
        0xFE,
        (
            "内科医療の現場に臨むとき、\x01",
            "いつも考えていることだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "体の自己治癒力を助けていく\x01",
            "内科医療では間に合わない場面でも、\x01",
            "外科医術の早さに救われることがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "足りない部分を柔軟に助け合うのが\x01",
            "理想的な医療の形じゃないか、とね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "……ゲイリー教授と犬猿の仲の\x01",
            "わしが言ってもどうかとは思うがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33E3")

    label("loc_3352")


    #C0169
    ChrTalk(
        0xFE,
        (
            "……うぉっほん！　あー、なんだ。\x01",
            "今のは忘れてくれたまえ、キミ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "……さっきのわしのセリフは\x01",
            "間違ってもゲイリー教授に\x01",
            "言うんじゃないぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E3")

    Jump("loc_4006")

    label("loc_33E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3475")

    #C0171
    ChrTalk(
        0xFE,
        (
            "うぉっほん！\x01",
            "ゲイリー教授め、今朝の患者を\x01",
            "うまく外科医療で助けたそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "……フン、外科もなかなか\x01",
            "やるではないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4006")

    label("loc_3475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3508")

    #C0173
    ChrTalk(
        0xFE,
        (
            "ヨアヒム君はここ最近、\x01",
            "研究室で熱心に研究しとるようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "彼は確かにサボリの常習だが、\x01",
            "ここぞというところは\x01",
            "やる男なのだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4006")

    label("loc_3508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3569")

    #C0175
    ChrTalk(
        0xFE,
        "ん……そんなに慌ててどうしたね？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "こちらには患者以外、\x01",
            "誰も来ていないぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4006")

    label("loc_3569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_367F")

    #C0177
    ChrTalk(
        0xFE,
        (
            "うぉっほん！\x01",
            "なんだね、君たちは。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#0005Fえっと、神経・薬学科に\x01",
            "用があって来たんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        "ああ、なるほどな。\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "確かに神経・薬学科は\x01",
            "内科の範疇だが、\x01",
            "どちらかといえば研究中の部類だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "用があるならヨアヒム君を\x01",
            "たずねるがよかろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36FE")

    label("loc_367F")


    #C0182
    ChrTalk(
        0xFE,
        (
            "確かに薬学・神経科は\x01",
            "内科の範疇だが、\x01",
            "どちらかといえば研究中の部類だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "用があるならヨアヒム君を\x01",
            "たずねるがよかろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36FE")

    Jump("loc_4006")

    label("loc_3703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3711")
    Jump("loc_4006")

    label("loc_3711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_371F")
    Jump("loc_4006")

    label("loc_371F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F9")

    #C0184
    ChrTalk(
        0xFE,
        (
            "この間、グェン君に\x01",
            "内科の診察を\x01",
            "任せてみたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "彼女は技術的には申し分ないが\x01",
            "患者への配慮などはまだまだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "ウルスラ病院の研修医の\x01",
            "名に恥じぬよう、\x01",
            "もっと伸びてほしいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_386E")

    label("loc_37F9")


    #C0187
    ChrTalk(
        0xFE,
        (
            "的確な病状を知るには\x01",
            "患者と上手く付き合って行く\x01",
            "能力が必要になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "グェン君はその方面は\x01",
            "まだまだ未熟だね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_386E")

    Jump("loc_4006")

    label("loc_3873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_38FD")

    #C0189
    ChrTalk(
        0xFE,
        (
            "記念祭が始まったからか\x01",
            "研修医たちの気が\x01",
            "抜けて来ているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "うぉっほん！\x01",
            "ここはガツンと喝を\x01",
            "入れてやらんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4006")

    label("loc_38FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BC1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39A6")

    #C0191
    ChrTalk(
        0xFE,
        (
            "君たちにはすっかり\x01",
            "世話になってしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "今から講義なので、\x01",
            "失礼させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "また何かあったらよろしく頼む。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A18")

    label("loc_39A6")


    #C0194
    ChrTalk(
        0xFE,
        (
            "七耀教会で学んだ日々は\x01",
            "かけがえのないものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "いつかエラルダ大司教には\x01",
            "お礼を言いに行かねばなるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A18")

    Jump("loc_3BBC")

    label("loc_3A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_3A32")
    Call(1, 75)
    Jump("loc_3BBC")

    label("loc_3A32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3B03")

    #C0196
    ChrTalk(
        0xFE,
        (
            "クロスベル大聖堂にいらっしゃる\x01",
            "エラルダ大司教から、\x01",
            "『ルピナス草』を貰ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "あー、念のために言っておくが……\x01",
            "大司教は私以上に気難しい方だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "断じて粗相の無いようにな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BBC")

    label("loc_3B03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x13, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3B17")
    Call(1, 74)
    Jump("loc_3BBC")

    label("loc_3B17")


    #C0199
    ChrTalk(
        0xFE,
        (
            "……ふむ、あのような要請で\x01",
            "本当に来るのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "やはり、遊撃士に\x01",
            "頼むべきだったか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "いやしかし、この程度の仕事で\x01",
            "ミラをはたきたくはないし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BBC")

    Jump("loc_4006")

    label("loc_3BC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3BCF")
    Jump("loc_4006")

    label("loc_3BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3BDD")
    Jump("loc_4006")

    label("loc_3BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3C99")

    #C0202
    ChrTalk(
        0xFE,
        (
            "あの日、リットン君に\x01",
            "レポート提出を課したのは私だが……\x01",
            "まさかあのようなことになるとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "ううむ、他の研修医が\x01",
            "まだ襲われていないのが\x01",
            "不幸中の幸いというところだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4006")

    label("loc_3C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3FFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED8")

    #C0204
    ChrTalk(
        0xFE,
        (
            "うぉっほん！　……何か用かね？\x01",
            "ここの学生ではないようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "……ふむ、見ればなかなか\x01",
            "賢そうな子らじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "君達、よかったら来年の入学試験に\x01",
            "挑戦してみないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#0305Fお、見込みありそうッスか俺たち！\x02\x03",

            "#0304Fドクターランディの\x01",
            "華麗なるナースハーレム生活……\x01",
            "結構悪くねぇかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#0006Fおいおい……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x102,
        (
            "#0111Fちなみに、このウルスラ病院には\x01",
            "近隣諸国から学生が集まるから、\x01",
            "かなりの人数が試験を受けるわよ。\x02\x03",

            "#0103F去年の倍率は確か……\x01",
            "１２０倍だったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        "#0303Fムリだな、あきらめよう。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        "#0211F……即答ですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3FF8")

    label("loc_3ED8")


    #C0212
    ChrTalk(
        0xFE,
        (
            "このウルスラ病院は、\x01",
            "医療大国レミフェリアにも一目置かれる\x01",
            "最先端の医療研究所でもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "このクロスベルはもちろん\x01",
            "エレボニア帝国やカルバード共和国、\x01",
            "レミフェリア公国にリベール王国……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "各国の将来有望な若者たちが\x01",
            "骨身を削る思いで勉強することで\x01",
            "ようやく入学できる場所なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FF8")

    Jump("loc_4006")

    label("loc_3FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4006")

    label("loc_4006")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_30F3 end

    def Function_8_400E(): pass

    label("Function_8_400E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_401F")
    Jump("loc_491C")

    label("loc_401F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_408A")

    #C0215
    ChrTalk(
        0xFE,
        (
            "今日救急車で運び込まれた人、\x01",
            "もう意識が戻ってるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        "さすがはウチの先生よね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_408A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4098")
    Jump("loc_491C")

    label("loc_4098")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4165")

    #C0217
    ChrTalk(
        0xFE,
        (
            "この前、また実地研修が\x01",
            "あったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "できるだけ患者さんに\x01",
            "にこやかに接していたら、\x01",
            "Ｂ－の評価がＢ＋に上がったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "小さい進歩だけど……\x01",
            "ちょっと内科医の夢に\x01",
            "近づいたかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_4165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_42C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_424C")

    #C0220
    ChrTalk(
        0xFE,
        (
            "さっき、診察中の\x01",
            "ラゴー教授を見てて\x01",
            "気づいたことがあるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "あの気難しい教授ですら\x01",
            "患者さんの前では\x01",
            "穏やかにしていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "よく考えれば私、\x01",
            "評価ばかり気になって\x01",
            "その辺はないがしろだったかも。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_42BD")

    label("loc_424C")


    #C0223
    ChrTalk(
        0xFE,
        (
            "あの気難しいラゴー教授ですら\x01",
            "患者さんの前では\x01",
            "穏やかにしていた……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "私に足りないのは\x01",
            "そういうことかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42BD")

    Jump("loc_491C")

    label("loc_42C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_440E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4393")

    #C0225
    ChrTalk(
        0xFE,
        (
            "ラゴー教授、\x01",
            "私になかなかいい評価を\x01",
            "くれないのよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "何が悪いのか聞いてみても\x01",
            "『自分で気づけ』って言われるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "くそー、こうなったらとことん\x01",
            "教授を観察してやるわよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4409")

    label("loc_4393")


    #C0228
    ChrTalk(
        0xFE,
        (
            "こうなったらとことん\x01",
            "ラゴー教授を観察してやるわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "いい評価をもらえるヒント、\x01",
            "なんとしても見つけてやるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4409")

    Jump("loc_491C")

    label("loc_440E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_44AE")

    #C0230
    ChrTalk(
        0xFE,
        (
            "今日は教授がいないから、\x01",
            "なんとかリットン君と協力して\x01",
            "回していかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "でも……\x01",
            "別に高評価に繋がるわけでなし、\x01",
            "やる気でないのよねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_44AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_457B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_451C")

    #C0232
    ChrTalk(
        0xFE,
        "教授たち、妙に仲が悪いのよね。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "似た物同士なのに\x01",
            "何が気に入らないんだか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4576")

    label("loc_451C")


    #C0234
    ChrTalk(
        0xFE,
        (
            "ま、どこぞの病院みたいに\x01",
            "内外科のドロドロな派閥争い……\x01",
            "って感じじゃないからいっか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4576")

    Jump("loc_491C")

    label("loc_457B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_46AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462D")

    #C0235
    ChrTalk(
        0xFE,
        "昨日、実地研修だったのよ。\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "個人的には\x01",
            "上手くやれたつもりだけど\x01",
            "教授の評価はＢ－……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "くぅ、デキる女医への道は\x01",
            "とてつもなく険しいわね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_46A8")

    label("loc_462D")


    #C0238
    ChrTalk(
        0xFE,
        (
            "この間の実地研修……\x01",
            "個人的にはＡ＋を貰ってもいい出来だと\x01",
            "思ってたんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "Ｂ－かぁ……\x01",
            "もっと勉強しないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46A8")

    Jump("loc_491C")

    label("loc_46AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_46BB")
    Jump("loc_491C")

    label("loc_46BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_46C9")
    Jump("loc_491C")

    label("loc_46C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4768")

    #C0240
    ChrTalk(
        0xFE,
        (
            "リットン君、怪我が治ってから\x01",
            "張り切って仕事してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "でも、張り切りついでに\x01",
            "ヨアヒム先生の仕事まで\x01",
            "させられてるみたいなのよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_47AC")
    OP_93(0xFE, 0xB4, 0x0)

    #C0242
    ChrTalk(
        0xFE,
        (
            "きょ、教授～！\x01",
            "落ち着いてくださいってば！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_47AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4882")

    #C0243
    ChrTalk(
        0xFE,
        (
            "しかし、リットン君も\x01",
            "運が悪いわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        (
            "せっかくレポートを書きあげたのに\x01",
            "あんな目にあっちゃうなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "まさか自分が勉強してる場所に\x01",
            "入院するハメになるなんて\x01",
            "思いもよらなかったでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_4882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4913")

    #C0246
    ChrTalk(
        0xFE,
        (
            "リットン君がケガしたせいで、\x01",
            "シフトが大分キツくなったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "んもう……\x01",
            "魔獣に襲われたなんて言ってたけど\x01",
            "本当なのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_491C")

    label("loc_4913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_491C")

    label("loc_491C")

    TalkEnd(0xFE)
    Return()

    # Function_8_400E end

    def Function_9_4920(): pass

    label("Function_9_4920")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_495D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_493E")
    Call(1, 11)
    Jump("loc_4958")

    label("loc_493E")


    #C0248
    ChrTalk(
        0xFE,
        "チェストォォォ……！\x02",
    )

    CloseMessageWindow()

    label("loc_4958")

    Jump("loc_4A7C")

    label("loc_495D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_496B")
    Jump("loc_4A7C")

    label("loc_496B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4979")
    Jump("loc_4A7C")

    label("loc_4979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4987")
    Jump("loc_4A7C")

    label("loc_4987")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_4995")
    Jump("loc_4A7C")

    label("loc_4995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_49A3")
    Jump("loc_4A7C")

    label("loc_49A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_49B1")
    Jump("loc_4A7C")

    label("loc_49B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49CC")
    Call(1, 11)
    Jump("loc_49E4")

    label("loc_49CC")


    #C0249
    ChrTalk(
        0xFE,
        "ヌグヲヲヲ……！！\x02",
    )

    CloseMessageWindow()

    label("loc_49E4")

    Jump("loc_4A7C")

    label("loc_49E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_49F7")
    Jump("loc_4A7C")

    label("loc_49F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4A05")
    Jump("loc_4A7C")

    label("loc_4A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4A13")
    Jump("loc_4A7C")

    label("loc_4A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4A21")
    Jump("loc_4A7C")

    label("loc_4A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_4A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A3C")
    Call(1, 11)
    Jump("loc_4A52")

    label("loc_4A3C")


    #C0250
    ChrTalk(
        0xFE,
        "ヌグググ……！！\x02",
    )

    CloseMessageWindow()

    label("loc_4A52")

    Jump("loc_4A7C")

    label("loc_4A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_4A65")
    Jump("loc_4A7C")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_4A73")
    Jump("loc_4A7C")

    label("loc_4A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4A7C")

    label("loc_4A7C")

    TalkEnd(0xFE)
    Return()

    # Function_9_4920 end

    def Function_10_4A80(): pass

    label("Function_10_4A80")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4B14")
    Jump("loc_4B5E")

    label("loc_4B14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B34")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B5E")

    label("loc_4B34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4B54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4B5E")

    label("loc_4B54")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B5E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4B91")
    Jump("loc_5881")

    label("loc_4B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_4D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CC6")

    #C0251
    ChrTalk(
        0xFE,
        (
            "今朝の重傷患者の処置で……\x01",
            "いや、いつも思っている\x01",
            "ことなのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xFE,
        (
            "外科治療の現場でも、\x01",
            "麻酔や点滴などの内科的な医療は\x01",
            "必ず必要になってくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xFE,
        (
            "外科と内科はやはり\x01",
            "手を取り合って\x01",
            "医療に望むべきだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……ラゴー教授と\x01",
            "ケンカばかりしている\x01",
            "私が言うのも何だがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D3F")

    label("loc_4CC6")


    #C0255
    ChrTalk(
        0xFE,
        (
            "……ゴホン！\x01",
            "ガラにもないことを\x01",
            "口走ってしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "いいか、ラゴー教授にだけは\x01",
            "このことを漏らすんじゃないぞ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3F")

    Jump("loc_5881")

    label("loc_4D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0A")

    #C0257
    ChrTalk(
        0xFE,
        (
            "先ほど、クロスベル市のほうから\x01",
            "救急患者が何人も運ばれてきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        (
            "ヨアヒム君たちと一緒に\x01",
            "先ほど処置を終えたところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "ふぅ、さすがに疲れたな。\x01",
            "私も歳かね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E7C")

    label("loc_4E0A")


    #C0260
    ChrTalk(
        0xFE,
        (
            "クロスベル市からの救急患者だが、\x01",
            "とりあえず全員処置はできたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "ふぅ、さすがに疲れたな。\x01",
            "私も歳かね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E7C")

    Jump("loc_5881")

    label("loc_4E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4FF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6D")

    #C0262
    ChrTalk(
        0xFE,
        (
            "学習したことは、\x01",
            "忘れないうちに復習を繰り返すことで\x01",
            "長期的な記憶となる。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "つまり、『知識』として\x01",
            "明確に脳に蓄えられるわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "うちの研修医が優秀なのは\x01",
            "まさに復習が習慣づいている\x01",
            "おかげだろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4FEB")

    label("loc_4F6D")


    #C0265
    ChrTalk(
        0xFE,
        (
            "学習したことは、\x01",
            "忘れないうちに復習を繰り返すことで\x01",
            "『知識』として蓄えられる。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        "……ま、ヨアヒム君の受け売りだがね。\x02",
    )

    CloseMessageWindow()

    label("loc_4FEB")

    Jump("loc_5881")

    label("loc_4FF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_5179")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DE")

    #C0267
    ChrTalk(
        0xFE,
        (
            "さっき、息子のキーンツが\x01",
            "病院に来ていると\x01",
            "看護師が報せてくれてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "弁当を届けさせると\x01",
            "妻が言ってたからそのことだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xFE,
        (
            "きっと今頃憎まれ口でも\x01",
            "叩いているのかもしれないが……\x01",
            "素直に嬉しいものだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5174")

    label("loc_50DE")


    #C0270
    ChrTalk(
        0xFE,
        (
            "どうやら息子のキーンツが、\x01",
            "弁当を届けるために\x01",
            "病院を訪れているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "素直に嬉しいものだよ。\x01",
            "フフ、こんな顔は\x01",
            "ラゴー教授には見せられんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5174")

    Jump("loc_5881")

    label("loc_5179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5216")

    #C0272
    ChrTalk(
        0xFE,
        (
            "屋上から行ける研究棟には\x01",
            "今までの研究で培われた\x01",
            "貴重なデータが保管されてある。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "必要最低限、部外者は\x01",
            "入らないでいただきたいのだがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5881")

    label("loc_5216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5224")
    Jump("loc_5881")

    label("loc_5224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5232")
    Jump("loc_5881")

    label("loc_5232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_537B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530E")

    #C0274
    ChrTalk(
        0xFE,
        (
            "……昨日クロスベル市であった騒ぎに\x01",
            "息子のキーンツが参加していたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "警察の介入のおかげで\x01",
            "怪我人などは出なかったそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "……ふーっ……\x01",
            "心配をかけさせないで欲しいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5376")

    label("loc_530E")


    #C0277
    ChrTalk(
        0xFE,
        (
            "本来叱らなければいけない時に\x01",
            "その場にいられないとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "……ふーっ……\x01",
            "私は情けない父親だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5376")

    Jump("loc_5881")

    label("loc_537B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5416")

    #C0279
    ChrTalk(
        0xFE,
        (
            "明日、息子とアルカンシェルを\x01",
            "観に行くつもりだったが……\x01",
            "やはり行けそうもないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "……子供の機嫌取りなんて\x01",
            "父親として情けないがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5881")

    label("loc_5416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_55EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551E")
    SetChrSubChip(0xFE, 0x0)

    #C0281
    ChrTalk(
        0xFE,
        (
            "先々月、例の不良たちが\x01",
            "運び込まれただろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0xFE,
        (
            "患者が息子のキーンツじゃないかと\x01",
            "背筋が凍ったものだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "……あんなことがあっても\x01",
            "まだグループに\x01",
            "入っているというし……\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0xFE,
        (
            "全く、あまり心配を\x01",
            "かけさせないでほしいものだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_55EA")

    label("loc_551E")


    #C0285
    ChrTalk(
        0xFE,
        (
            "……私はどうも、息子によく\x01",
            "思われていないらしくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "昔から病院の仕事で\x01",
            "家に居ないことが多かったから、\x01",
            "尊敬はされてないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xFE,
        (
            "息子が不良になった責任の一角は\x01",
            "私にあるのかもしれないな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55EA")

    Jump("loc_5881")

    label("loc_55EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_568D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_560A")
    Call(1, 12)
    Jump("loc_5688")

    label("loc_560A")

    SetChrSubChip(0xFE, 0x0)

    #C0288
    ChrTalk(
        0xFE,
        (
            "いいかね、アーシュラ君。\x01",
            "君ももう機器関係の医療を教える\x01",
            "主任という立場なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0xFE,
        "いつまでも学生気分ではいかんぞ。\x02",
    )

    CloseMessageWindow()

    label("loc_5688")

    Jump("loc_5881")

    label("loc_568D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_569B")
    Jump("loc_5881")

    label("loc_569B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5763")

    #C0290
    ChrTalk(
        0xFE,
        (
            "外科とは、近年\x01",
            "徐々に普及してきた\x01",
            "近代的な医療のことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "ただ、なにぶん\x01",
            "新しい技術なのでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "体にメスを入れる事について\x01",
            "いまいち理解が\x01",
            "得られていないのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_580D")

    label("loc_5763")


    #C0293
    ChrTalk(
        0xFE,
        (
            "あのラゴー教授も含め、\x01",
            "外科に対して偏見的な目を持つ者も\x01",
            "少なくないのが現状だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xFE,
        (
            "近代医療の進化について来れん\x01",
            "時代遅れのジジイのことなど\x01",
            "知ったことではないがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_580D")

    Jump("loc_5881")

    label("loc_5812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5878")

    #C0295
    ChrTalk(
        0xFE,
        (
            "アーシュラ君……\x01",
            "どうやら今日も遅刻か。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xFE,
        (
            "まったく……\x01",
            "何度やっても懲りないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5881")

    label("loc_5878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5881")

    label("loc_5881")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_4A80 end

    def Function_11_5889(): pass

    label("Function_11_5889")

    OP_4B(0xB, 0xFF)
    OP_4B(0xE, 0xFF)
    TurnDirection(0xB, 0xE, 0)
    TurnDirection(0xE, 0xB, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_59F1")

    #C0297
    ChrTalk(
        0xB,
        (
            "うぉっほん！\x01",
            "誰かと思えばゲイリー教授ではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xE,
        "おやおや、そういう貴方はラゴー教授。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xB,
        (
            "……あー、なんだ。\x01",
            "昨日の重傷患者への処置だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0xE,
        (
            "おやぁ、わたしの活躍を\x01",
            "耳に入れてもらえましたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xE,
        (
            "ふっふっふ、内科の時代は\x01",
            "そろそろ終わりではないですかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xB,
        "#4S……なにをぉう！？\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xE,
        "#4S……やるのか！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E27")

    label("loc_59F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_59FF")
    Jump("loc_5E27")

    label("loc_59FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5A0D")
    Jump("loc_5E27")

    label("loc_5A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5A1B")
    Jump("loc_5E27")

    label("loc_5A1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_5A29")
    Jump("loc_5E27")

    label("loc_5A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_5A37")
    Jump("loc_5E27")

    label("loc_5A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5A45")
    Jump("loc_5E27")

    label("loc_5A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5BFF")

    #C0304
    ChrTalk(
        0xB,
        (
            "うぉっほん！　誰かと思えば\x01",
            "ゲイリー教授ではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xB,
        (
            "そのみすぼらしいヒゲは\x01",
            "今日も医者にあるまじき風貌だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xE,
        (
            "おやおや、\x01",
            "そういう貴方はラゴー教授。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xE,
        (
            "その焼け野原のごときハゲ頭、\x01",
            "未だに整備していないとは驚きだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0xB,
        (
            "……そのヒゲ……\x01",
            "お得意の外科手術で、永久に\x01",
            "取り除いてみてはどうかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xE,
        (
            "……貴方の頭こそ、\x01",
            "お得意の内科医療で\x01",
            "どうにかできなかったのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xB,
        "#4S……なにをぉう！？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xE,
        "#4S……やるのか！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E27")

    label("loc_5BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5C0D")
    Jump("loc_5E27")

    label("loc_5C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5C1B")
    Jump("loc_5E27")

    label("loc_5C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5C29")
    Jump("loc_5E27")

    label("loc_5C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5C37")
    Jump("loc_5E27")

    label("loc_5C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_5E02")

    #C0312
    ChrTalk(
        0xB,
        (
            "うぉっほん！\x01",
            "……その不潔なヒゲ面、\x01",
            "誰かと思えばゲイリー教授ではないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xE,
        (
            "おやおや、そういう貴方はラゴー教授。\x01",
            "いやぁ、そのハゲ頭は今日も眩しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xB,
        (
            "……フン！\x01",
            "全く嘆かわしいことだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xB,
        (
            "君のような男が未来ある研修医に\x01",
            "人の切り刻み方を教えているなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0xE,
        (
            "……ハン！\x01",
            "その点、貴方は楽でいいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xE,
        (
            "七耀教会譲りの枯れた技術を伝える……\x01",
            "それだけで教授ヅラが出来るんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0xB,
        "#4S……なにをぉう！？\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xE,
        "#4S……やるのか！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E27")

    label("loc_5E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5E10")
    Jump("loc_5E27")

    label("loc_5E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_5E1E")
    Jump("loc_5E27")

    label("loc_5E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_5E27")

    label("loc_5E27")

    SetScenarioFlags(0x0, 5)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_11_5889 end

    def Function_12_5E33(): pass

    label("Function_12_5E33")

    OP_4B(0x13, 0xFF)
    SetChrSubChip(0xF, 0x0)
    TurnDirection(0x13, 0xF, 0)

    #C0320
    ChrTalk(
        0xF,
        (
            "アーシュラ君……\x01",
            "また遅刻かね。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xF,
        (
            "教える立場の者が\x01",
            "遅刻するとは言語道断だぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x13,
        "す、すみませ～ん……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x13,
        (
            "昨日届いた新しい機材に\x01",
            "夢中になって弄ってるうちに\x01",
            "朝になっちゃってて。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x13,
        (
            "で、結局ついさっきまで\x01",
            "ぐっすりと……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xF,
        (
            "……ふぅ……\x01",
            "君は学生時代から\x01",
            "全く変わらんな。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_12_5E33 end

    def Function_13_5F6C(): pass

    label("Function_13_5F6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_609E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6048")
    TurnDirection(0xFE, 0x14, 0)

    #C0326
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任……\x01",
            "さすがに、ここで寝るのは\x01",
            "まずいかと思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xFE,
        (
            "ほら、ゲイリー教授たちの\x01",
            "喧嘩が終わる前に起きないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x14,
        "う～ん……あと５分……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        "だめだこりゃ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6099")

    label("loc_6048")


    #C0330
    ChrTalk(
        0xFE,
        (
            "結局はアーシュラ主任の貫徹に\x01",
            "付き合ってしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        "眠くて仕方ない……\x02",
    )

    CloseMessageWindow()

    label("loc_6099")

    Jump("loc_6B49")

    label("loc_609E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_6245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_619F")

    #C0332
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任がもっとも輝く\x01",
            "研究の時間が\x01",
            "夜にあるのはまちがいない。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        (
            "……ただそのせいで\x01",
            "主任が寝坊がちになるのも\x01",
            "また確かだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "准教授クラスの地位を持つのに\x01",
            "主任に威厳を感じないのは、\x01",
            "そのあたりに原因がありそうだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6240")

    label("loc_619F")


    #C0335
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任は夜型人間だからね。\x01",
            "そのせいで寝坊がちなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "准教授クラスの地位を持つのに\x01",
            "主任に威厳を感じないのは、\x01",
            "そのあたりに原因がありそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6240")

    Jump("loc_6B49")

    label("loc_6245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_62F5")

    #C0337
    ChrTalk(
        0xFE,
        (
            "機器開発は難しい反面、\x01",
            "新しい技術を扱っているという\x01",
            "面白さがある。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xFE,
        (
            "ここで研究されている医療機器が\x01",
            "将来の医療の現場で活躍すると思うと\x01",
            "胸がおどる思いさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_62F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6389")

    #C0339
    ChrTalk(
        0xFE,
        (
            "やれやれ……アーシュラ主任も\x01",
            "無理しないで寝坊してくればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "というか、徹夜してるのに\x01",
            "早起きなんて無理だと思うけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_6389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_6416")

    #C0341
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任が\x01",
            "寝坊するなんて予想の範疇……\x01",
            "教授も最早、怒ってすらいない。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xFE,
        (
            "まぁ、僕も来るのを\x01",
            "気長に待つとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_6416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_6494")

    #C0343
    ChrTalk(
        0xFE,
        (
            "……今日もアーシュラ主任は\x01",
            "寝坊みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xFE,
        (
            "しかたない、この僕が\x01",
            "今日の研究の準備だけでもしておこう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_6494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_651F")

    #C0345
    ChrTalk(
        0xFE,
        (
            "ゲイリー教授と\x01",
            "アーシュラ主任がいないと\x01",
            "この診察室も寂しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        (
            "人手も不足しているし、\x01",
            "フローラ君を呼んでくるか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_651F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_659D")

    #C0347
    ChrTalk(
        0xFE,
        (
            "……記念祭中とは思えないほど\x01",
            "いつもどおりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xFE,
        (
            "どうせ言ってもやめないし、\x01",
            "本でも読んでいようかな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_659D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_65AB")
    Jump("loc_6B49")

    label("loc_65AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6635")

    #C0349
    ChrTalk(
        0xFE,
        "……もう記念祭も２日目だそうだね。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任に付き合って\x01",
            "三日三晩寝ずに研究していたから\x01",
            "分からなかったよ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_6635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6720")

    #C0351
    ChrTalk(
        0xFE,
        (
            "アーシュラ主任の肩書きは\x01",
            "“主任”だけど、実際は\x01",
            "准教授並の地位があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "講義をして学生を教えるよりも\x01",
            "研究室にこもって\x01",
            "開発をしている方が多いけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0xFE,
        (
            "そういう意味では、\x01",
            "結構特殊な地位の人かもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_6720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_68DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6813")

    #C0354
    ChrTalk(
        0xFE,
        (
            "色々な国で様々な導力器の開発が\x01",
            "進められている中、医療機器の分野は\x01",
            "やはりレミフェリア公国が最先端だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        (
            "この病院で使われてる医療機器も、\x01",
            "ほとんどがレミフェリアにある\x01",
            "セイランド社というメーカーの製品なんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_68D9")

    label("loc_6813")


    #C0356
    ChrTalk(
        0xFE,
        (
            "セイランド社って言えば、\x01",
            "大陸でも有数の医療機器メーカーでね。\x01",
            "この病院のスポンサーの一つでもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0xFE,
        (
            "医療機器科では、\x01",
            "その医療機器を現場で運用しながら\x01",
            "改良の余地を模索してるという感じだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D9")

    Jump("loc_6B49")

    label("loc_68DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_68EC")
    Jump("loc_6B49")

    label("loc_68EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_6A74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69EF")

    #C0358
    ChrTalk(
        0xFE,
        (
            "この研究棟では\x01",
            "先進的な医療技術が\x01",
            "研究されているのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xFE,
        (
            "特に『医療機器科』では、\x01",
            "導力を利用した医療機器の研究が\x01",
            "日夜、進められている。\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xFE,
        (
            "……今日はまだ来ていないが、\x01",
            "アーシュラ主任という方が\x01",
            "医療機器科のトップなのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6A6F")

    label("loc_69EF")


    #C0361
    ChrTalk(
        0xFE,
        (
            "外科医療という近代的な分野の\x01",
            "更に先を行く医療機器の研究……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xFE,
        (
            "トップを担うアーシュラ主任が\x01",
            "どれだけ優秀か分かるだろう？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A6F")

    Jump("loc_6B49")

    label("loc_6A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_6B40")

    #C0363
    ChrTalk(
        0xFE,
        (
            "僕の夢は、祖国エレボニア帝国に\x01",
            "大きな病院を建てることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        (
            "このウルスラ病院は\x01",
            "僕の野望を叶えるに\x01",
            "うってつけの環境だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0xFE,
        (
            "ここには最先端の医学と\x01",
            "優秀な医師が集まっているからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B49")

    label("loc_6B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_6B49")

    label("loc_6B49")

    TalkEnd(0xFE)
    Return()

    # Function_13_5F6C end

    def Function_14_6B4D(): pass

    label("Function_14_6B4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B62")
    Call(1, 16)
    Jump("loc_6C27")

    label("loc_6B62")


    #C0366
    ChrTalk(
        0x11,
        (
            "#2400F僕も回診は手伝っているけど\x01",
            "どうしても研究がメインでね。\x02\x03",

            "ベルダイン先生にばかり\x01",
            "負担をかけてしまっている状況なんだ。\x02\x03",

            "#2406F早くリットン君に復帰してもらって\x01",
            "バリバリ働いてもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C27")

    TalkEnd(0xFE)
    Return()

    # Function_14_6B4D end

    def Function_15_6C2B(): pass

    label("Function_15_6C2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C40")
    Call(1, 16)
    Jump("loc_6CB2")

    label("loc_6C40")


    #C0367
    ChrTalk(
        0xFE,
        (
            "少々難しい患者を扱っていてな。\x01",
            "先程、診察が終わったところだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "……ふぅ……\x01",
            "食堂で紅茶でも飲んでくるか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CB2")

    TalkEnd(0xFE)
    Return()

    # Function_15_6C2B end

    def Function_16_6CB6(): pass

    label("Function_16_6CB6")

    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0369
    ChrTalk(
        0x11,
        (
            "#2400Fベルダイン先生。\x01",
            "どうやらお疲れみたいですね。\x02\x03",

            "よかったらローヤルゼリー入りの\x01",
            "栄養剤でも処方しましょうか？\x02\x03",

            "#2409Fアルモリカ産のものですから\x01",
            "効き目はバッチリですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x12,
        "いや、遠慮しておくよ。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x12,
        (
            "君の栄養剤は効きすぎるからな。\x01",
            "頼ってしまうと後が恐そうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_16_6CB6 end

    def Function_17_6DE6(): pass

    label("Function_17_6DE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_6DF7")
    Jump("loc_7951")

    label("loc_6DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_6E97")

    #C0372
    ChrTalk(
        0xFE,
        "ふんふんふん……♪\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xFE,
        (
            "うふふ、夜が近づくと眠くなくなって\x01",
            "作業能率が上がるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "さぁて、いまから１２時間……\x01",
            "みっちりやりますよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7951")

    label("loc_6E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_6FFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F60")

    #C0375
    ChrTalk(
        0xFE,
        (
            "医療系オーブメント開発では\x01",
            "まず、安全性の保持が優先されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "人体に作用する以上、\x01",
            "万が一のことがあってはいけませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0xFE,
        "医療機器開発の難しいところですねぇ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6FF7")

    label("loc_6F60")


    #C0378
    ChrTalk(
        0xFE,
        (
            "医療系オーブメント開発では\x01",
            "まず安全であることが何より大事です。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "マウス実験では人体へ影響する\x01",
            "明確なデータが取れるわけでは\x01",
            "ないですからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF7")

    Jump("loc_7951")

    label("loc_6FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_72FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7093")

    #C0380
    ChrTalk(
        0xFE,
        (
            "あ、ペンダントトップは\x01",
            "役に立ちましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        (
            "魔獣が踏んでも壊れない\x01",
            "耐久性合金なので\x01",
            "きっと長持ちすると思いますよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F7")

    label("loc_7093")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_7138")

    #C0382
    ChrTalk(
        0xFE,
        (
            "そのペンダントトップは\x01",
            "実験失敗時の爆発に巻き込まれて\x01",
            "なお無傷だった品なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xFE,
        (
            "そんな運の強い品なら、\x01",
            "きっと贈り物の材料に最適ですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72F7")

    label("loc_7138")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_714C")
    Call(1, 78)
    Jump("loc_72F7")

    label("loc_714C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7258")

    #C0384
    ChrTalk(
        0xFE,
        (
            "寝坊でシャルールくんに\x01",
            "迷惑をかけてばかりなので、\x01",
            "先週から早起きを実践してるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "朝、目覚まし１２個目くらいで\x01",
            "起きるんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0xFE,
        (
            "いやぁ、徹夜明けでも\x01",
            "なんとか起きれるもんですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0387
    ChrTalk(
        0xFE,
        "………………ぐぅ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_72F7")

    label("loc_7258")


    #C0388
    ChrTalk(
        0xFE,
        "………………はっ。\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "え、えーと……寝てませんよ？\x01",
            "ちょっとカクっとなっただけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xFE,
        "さ、さぁ！　今日も元気に研究研究です！\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        "………………ぐぅ。\x02",
    )

    CloseMessageWindow()

    label("loc_72F7")

    Jump("loc_7951")

    label("loc_72FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_730A")
    Jump("loc_7951")

    label("loc_730A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7318")
    Jump("loc_7951")

    label("loc_7318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7326")
    Jump("loc_7951")

    label("loc_7326")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7334")
    Jump("loc_7951")

    label("loc_7334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_747D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7433")
    OP_93(0xFE, 0x5A, 0x0)

    #C0392
    ChrTalk(
        0xFE,
        "…………はっ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0393
    ChrTalk(
        0xFE,
        "え、ええっと、講義を始めますね。\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xFE,
        (
            "今日は医療機器に使われる\x01",
            "結晶回路の構造について……です。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#0006F……あの。\x01",
            "俺たちは学生じゃないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        "#0100F寝ぼけてたみたいね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    BeginChrThread(0x13, 0, 0, 0)
    Jump("loc_7478")

    label("loc_7433")


    #C0397
    ChrTalk(
        0xFE,
        (
            "あ……えっと……すみません。\x01",
            "講義中は部外者立入禁止なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7478")

    Jump("loc_7951")

    label("loc_747D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_756A")
    OP_93(0xFE, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_751A")

    #C0398
    ChrTalk(
        0xFE,
        "……すー……すぴー…………\x02",
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x101,
        "#0005Fた、立ったまま寝てる……！？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x103,
        (
            "#0200F器用ですね。\x01",
            "ぜひ習得したいスキルです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7565")

    label("loc_751A")


    #C0401
    ChrTalk(
        0xFE,
        (
            "……すー……すぴー…………\x01",
            "……ふがっ。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        "……すー……すー…………\x02",
    )

    CloseMessageWindow()

    label("loc_7565")

    Jump("loc_7951")

    label("loc_756A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76A1")

    #C0403
    ChrTalk(
        0xFE,
        (
            "私、技術者として\x01",
            "とても尊敬してる人がいるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        (
            "リベールにあるＺＣＦの\x01",
            "エリカ・ラッセル博士……\x01",
            "かの有名なＡ・ラッセル博士の娘さんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "彼女は女性ながら\x01",
            "リベール王国最高峰の\x01",
            "技術力を持っているとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0xFE,
        (
            "私も女医として、医療機器の分野で\x01",
            "大きな功績を立てたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7734")

    label("loc_76A1")


    #C0407
    ChrTalk(
        0xFE,
        (
            "リベールのエリカ博士……\x01",
            "彼女はＡ・ラッセル博士と並ぶ\x01",
            "優秀な技術者なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "私も女医として、医療機器の分野で\x01",
            "大きな功績を立てたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7734")

    Jump("loc_7951")

    label("loc_7739")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_77FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7754")
    Call(1, 12)
    Jump("loc_77F5")

    label("loc_7754")


    #C0409
    ChrTalk(
        0xFE,
        (
            "（うぅ……こうなるとゲイリー教授は\x01",
            "  なかなか逃がしてくれません……）\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xF,
        "……聞いているのかね、アーシュラ君！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xF, 500)

    #C0411
    ChrTalk(
        0xFE,
        (
            "は、はひっ！\x01",
            "以後気をつけます！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77F5")

    Jump("loc_7951")

    label("loc_77FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_792C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78C5")
    OP_93(0xFE, 0x5A, 0x0)

    #C0412
    ChrTalk(
        0xFE,
        (
            "（カチャカチャカチャ\x01",
            "  カチャカチャカチャ）\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0xFE,
        (
            "……なるほど……\x01",
            "この結晶回路がこうなって……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x102,
        (
            "#0101F（こっちに全然気づいてないみたい。\x01",
            "  すごい集中力ね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7927")

    label("loc_78C5")


    #C0415
    ChrTalk(
        0xFE,
        (
            "……あら？\x01",
            "なんだか部屋の外が騒がしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xFE,
        (
            "まぁ、気にしない気にしない。\x01",
            "続き続き～♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7927")

    Jump("loc_7951")

    label("loc_792C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_793A")
    Jump("loc_7951")

    label("loc_793A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_7948")
    Jump("loc_7951")

    label("loc_7948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_7951")

    label("loc_7951")

    TalkEnd(0xFE)
    Return()

    # Function_17_6DE6 end

    def Function_18_7955(): pass

    label("Function_18_7955")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79E8")

    #C0417
    ChrTalk(
        0xFE,
        "す～……すぴ～……\x02",
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        "……うふふっ完成～…………\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xFE,
        (
            "これで……憧れのエリカ博士に\x01",
            "一歩近づいた……かも……\x01",
            "……ぐぅ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7A4A")

    label("loc_79E8")


    #C0420
    ChrTalk(
        0xFE,
        "……す～……すぴ～……\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0xFE,
        (
            "これで……憧れのエリカ博士に\x01",
            "一歩近づいた……かも……\x01",
            "……ぐぅ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A4A")

    TalkEnd(0xFE)
    Return()

    # Function_18_7955 end

    def Function_19_7A4E(): pass

    label("Function_19_7A4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_7AC7")

    #C0422
    ChrTalk(
        0xFE,
        (
            "あーあー……\x01",
            "また始まっちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0xFE,
        (
            "お互い、実力は認めてるはずなのに\x01",
            "妙に仲が悪いんだよね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8080")

    label("loc_7AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_7AD5")
    Jump("loc_8080")

    label("loc_7AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7B69")

    #C0424
    ChrTalk(
        0xFE,
        "今日は夕方までのシフトなんだ。\x02",
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生と\x01",
            "離れているだけでこの安らぎ……\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0xFE,
        (
            "うん、部屋に帰ったら\x01",
            "ノンビリしていよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8080")

    label("loc_7B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7C04")

    #C0427
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生の薬学・神経科では\x01",
            "色々な研究が行なわれてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0xFE,
        (
            "外科手術に使う麻酔や\x01",
            "滋養強壮の栄養剤なんかも\x01",
            "そこで作ってるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8080")

    label("loc_7C04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_7D7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CF8")

    #C0429
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生が受けもつ\x01",
            "薬学・神経科は\x01",
            "なかなか興味深い分野だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0xFE,
        (
            "近代医療の一つでありながら\x01",
            "心と精神に干渉する分野……\x01",
            "なかなか神秘的だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0xFE,
        (
            "僕が内科医を目指すのも、\x01",
            "ヨアヒム先生に憧れてのことなんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7D77")

    label("loc_7CF8")


    #C0432
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生が受けもつ\x01",
            "薬学・神経科は\x01",
            "なかなか興味深い分野だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0xFE,
        (
            "僕が内科医を目指すのも、\x01",
            "先生に憧れてのことなんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D77")

    Jump("loc_8080")

    label("loc_7D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_7E1F")

    #C0434
    ChrTalk(
        0xFE,
        (
            "ん、ヨアヒム先生の所に\x01",
            "行くのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xFE,
        (
            "教授や准教授の研究室は\x01",
            "研究棟の４階にあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0xFE,
        (
            "他の教授の研究室もあるから\x01",
            "まちがえないようにね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8080")

    label("loc_7E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_7F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF6")

    #C0437
    ChrTalk(
        0xFE,
        (
            "ラゴー教授たちは教授会でね。\x01",
            "今日は戻られないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xFE,
        (
            "教授会では、\x01",
            "沢山の病院の教授たちが\x01",
            "技術交流のために集まるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0xFE,
        (
            "そうして補い合うことで、\x01",
            "医学は一歩一歩前進するわけだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_7F73")

    label("loc_7EF6")


    #C0440
    ChrTalk(
        0xFE,
        (
            "教授会では、\x01",
            "沢山の病院の教授たちが\x01",
            "技術交流のために集まるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xFE,
        (
            "医学の進歩の為、\x01",
            "教授たちも日々勉強してるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F73")

    Jump("loc_8080")

    label("loc_7F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7F86")
    Jump("loc_8080")

    label("loc_7F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_7F94")
    Jump("loc_8080")

    label("loc_7F94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7FA2")
    Jump("loc_8080")

    label("loc_7FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_7FB0")
    Jump("loc_8080")

    label("loc_7FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_804D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FCB")
    Call(1, 21)
    Jump("loc_8048")

    label("loc_7FCB")

    TurnDirection(0x15, 0x16, 0)

    #C0442
    ChrTalk(
        0xFE,
        (
            "まぁ、こればっかりは\x01",
            "こっちが強制できないからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0xFE,
        (
            "お爺さんには悪くならないうちに\x01",
            "来るように言っておいてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8048")

    Jump("loc_8080")

    label("loc_804D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_805B")
    Jump("loc_8080")

    label("loc_805B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_8069")
    Jump("loc_8080")

    label("loc_8069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8077")
    Jump("loc_8080")

    label("loc_8077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8080")

    label("loc_8080")

    TalkEnd(0xFE)
    Return()

    # Function_19_7A4E end

    def Function_20_8084(): pass

    label("Function_20_8084")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8118")
    Jump("loc_8162")

    label("loc_8118")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8138")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8162")

    label("loc_8138")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8158")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8162")

    label("loc_8158")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8162")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8195")
    Jump("loc_83F8")

    label("loc_8195")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_81A3")
    Jump("loc_83F8")

    label("loc_81A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_81B1")
    Jump("loc_83F8")

    label("loc_81B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_81BF")
    Jump("loc_83F8")

    label("loc_81BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_81CD")
    Jump("loc_83F8")

    label("loc_81CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_81DB")
    Jump("loc_83F8")

    label("loc_81DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_81E9")
    Jump("loc_83F8")

    label("loc_81E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_81F7")
    Jump("loc_83F8")

    label("loc_81F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_8205")
    Jump("loc_83F8")

    label("loc_8205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_8283")

    #C0444
    ChrTalk(
        0xFE,
        (
            "おじいちゃんのお薬を\x01",
            "受け取りに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0xFE,
        "はあ……\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0xFE,
        (
            "おじいちゃんにも\x01",
            "ちゃんとお薬飲んで欲しいな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83F8")

    label("loc_8283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8291")
    Jump("loc_83F8")

    label("loc_8291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_82EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82AC")
    Call(1, 21)
    Jump("loc_82E9")

    label("loc_82AC")

    SetChrSubChip(0x16, 0x0)

    #C0447
    ChrTalk(
        0xFE,
        (
            "いつも代理のわたしばかりで……\x01",
            "先生、ごめんなさい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82E9")

    Jump("loc_83F8")

    label("loc_82EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_82FC")
    Jump("loc_83F8")

    label("loc_82FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_830A")
    Jump("loc_83F8")

    label("loc_830A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8318")
    Jump("loc_83F8")

    label("loc_8318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_83F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8398")

    #C0448
    ChrTalk(
        0xFE,
        (
            "おじいちゃんのお薬を\x01",
            "受け取りに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0xFE,
        (
            "おじいちゃん、病院嫌いで\x01",
            "自分で取りに来ないんだもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83F8")

    label("loc_8398")


    #C0450
    ChrTalk(
        0xFE,
        (
            "ウチのおじいちゃん、\x01",
            "すっごい頑固なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0xFE,
        (
            "はあ……ホントは入院って\x01",
            "言われてるのになぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83F8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_8084 end

    def Function_21_8400(): pass

    label("Function_21_8400")

    TurnDirection(0x15, 0x16, 0)
    SetChrSubChip(0x16, 0x0)
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)

    #C0452
    ChrTalk(
        0x16,
        (
            "うちのおじいちゃん、\x01",
            "やっぱり入院した方が\x01",
            "いいんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x15,
        (
            "そうなんだけどねえ……\x01",
            "あの人頑固だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x16,
        (
            "ご、ごめんなさい……\x01",
            "せめて通院するようには\x01",
            "言ってるんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_21_8400 end

    def Function_22_84DB(): pass

    label("Function_22_84DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84F0")
    Call(1, 23)
    Jump("loc_8580")

    label("loc_84F0")


    #C0455
    ChrTalk(
        0x44,
        (
            "#1305F……あ、ロイド！\x02\x03",

            "#1306Fゆっくり話したいけど、\x01",
            "今日はちょっと時間がないの。\x01",
            "……ごめんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        "#0003F（セシル姉……忙しそうだな。）\x02",
    )

    CloseMessageWindow()

    label("loc_8580")

    TalkEnd(0xFE)
    Return()

    # Function_22_84DB end

    def Function_23_8584(): pass

    label("Function_23_8584")

    OP_4B(0x44, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x44, 0xA, 0)
    TurnDirection(0xA, 0x44, 0)

    #C0457
    ChrTalk(
        0x44,
        (
            "#1300Fベルダイン先生に頼まれていた\x01",
            "例のカルテはこれね。\x02\x03",

            "後で渡しておいて貰える？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0xA,
        "あ、はい分かりました。\x02",
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x44,
        "#1309Fふふ、よろしくお願いね。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x44, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_23_8584 end

    def Function_24_863D(): pass

    label("Function_24_863D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8978")

    #C0460
    ChrTalk(
        0x101,
        "#0005Fディーター総裁……？\x02",
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x17,
        (
            "#2800Fやあ諸君か。\x01",
            "珍しい所で会うものだな。\x02\x03",

            "#2805F……もしや任務中に\x01",
            "大怪我でもしたのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x104,
        (
            "#0305Fいえ、そういう訳じゃ\x01",
            "ないッスけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        "#0200F総裁こそ、どこかお怪我でも？\x02",
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        (
            "#0102Fふふっ……\x02\x03",

            "おじさまは総裁職にいらっしゃるけど\x01",
            "個人的には慈善事業家として\x01",
            "いくつか事業を手がけてらっしゃるの。\x02\x03",

            "その一環として、毎年\x01",
            "この時期に入院している方々に\x01",
            "贈り物をなさっているのよ。\x02\x03",

            "#0102F記念祭を楽しめない代わりにってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#0005Fな……そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x17,
        (
            "#2804Fハハ……慈善事業といっても\x01",
            "金額的には大した事はないがね。\x02\x03",

            "#2800Fたまにこうして\x01",
            "仕事を抜け出しているのさ。\x02\x03",

            "人は自己満足と言うかもしれないが\x01",
            "これが私なりのルールでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        (
            "#0303F（な、なんつーか……\x01",
            "  意外な一面だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x103,
        (
            "#0200F（爽やかオジサンかと思いきや\x01",
            "  渋い考えも持っているんですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAE, 3)
    Jump("loc_8A79")

    label("loc_8978")


    #C0469
    ChrTalk(
        0x17,
        (
            "#2803F慈善事業といっても\x01",
            "金額的には大した事はない。\x01",
            "ただの私のこだわりさ。\x02\x03",

            "#2800Fそれでも……マリアベルなどは\x01",
            "毎年付き合ってくれていてね。\x02\x03",

            "ハハ、この私も周囲の理解に\x01",
            "支えられているというわけだ。\x02\x03",

            "#2803F……この感謝を少しでも\x01",
            "還元できればいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A79")

    TalkEnd(0xFE)
    Return()

    # Function_24_863D end

    def Function_25_8A7D(): pass

    label("Function_25_8A7D")

    TalkBegin(0xFE)
    Call(1, 26)
    TalkEnd(0xFE)
    Return()

    # Function_25_8A7D end

    def Function_26_8A87(): pass

    label("Function_26_8A87")

    OP_4B(0x8, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x8, 0x18, 0)
    TurnDirection(0x18, 0x8, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BA5")

    #C0470
    ChrTalk(
        0x8,
        (
            "ああ、ゲイリー先生の\x01",
            "お子さんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x8,
        (
            "先生ならすぐに\x01",
            "お呼びできますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x18,
        (
            "フ、フン……\x01",
            "あんな男、本当は\x01",
            "顔も見たくないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x18,
        (
            "弁当だけ渡しておいてくれ。\x01",
            "僕はすぐに帰らせてもらう！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x8,
        (
            "クス……いつも\x01",
            "素直じゃないんですから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8C26")

    label("loc_8BA5")


    #C0475
    ChrTalk(
        0x18,
        (
            "ぼ、僕はお袋に\x01",
            "届け物を頼まれただけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x18,
        (
            "いいから渡すだけ\x01",
            "渡しておいてくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x8,
        (
            "はいはい、それでは\x01",
            "お預かりしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C26")

    OP_4C(0x8, 0xFF)
    OP_4C(0x18, 0xFF)
    Return()

    # Function_26_8A87 end

    def Function_27_8C2F(): pass

    label("Function_27_8C2F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CC3")
    Jump("loc_8D0D")

    label("loc_8CC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8CE3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D0D")

    label("loc_8CE3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D03")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D0D")

    label("loc_8D03")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D0D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8D7B")

    #C0478
    ChrTalk(
        0xFE,
        (
            "やっぱり風邪っぽいな……\x01",
            "早めに来ておいてよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DD8")

    label("loc_8D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D96")
    Call(1, 5)
    Jump("loc_8DD8")

    label("loc_8D96")


    #C0479
    ChrTalk(
        0xFE,
        (
            "うっ、体温計か……\x01",
            "ひやっとするから\x01",
            "ちょっと苦手なんだよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_27_8C2F end

    def Function_28_8DE0(): pass

    label("Function_28_8DE0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E74")
    Jump("loc_8EBE")

    label("loc_8E74")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8E94")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EBE")

    label("loc_8E94")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8EB4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8EBE")

    label("loc_8EB4")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8EBE")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_8F51")

    #C0480
    ChrTalk(
        0xFE,
        (
            "いやぁ、料理中に火傷した時は\x01",
            "どうなるかと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0xFE,
        (
            "大したことなくて\x01",
            "よかったわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F99")

    label("loc_8F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8F99")

    #C0482
    ChrTalk(
        0xFE,
        (
            "今日は空いていて助かったわい。\x01",
            "待つのは苦手じゃからのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F99")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_28_8DE0 end

    def Function_29_8FA1(): pass

    label("Function_29_8FA1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9035")
    Jump("loc_907F")

    label("loc_9035")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9055")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_907F")

    label("loc_9055")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9075")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_907F")

    label("loc_9075")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_907F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_914D")

    #C0483
    ChrTalk(
        0xFE,
        (
            "初めて病院に来たから\x01",
            "ちょっと戸惑ってたけど、\x01",
            "ようやく診察もおわったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0xFE,
        (
            "うんうん、なかなかいい所だなここは。\x01",
            "これからも頼らせてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_92F6")

    label("loc_914D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_92A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_926A")

    #C0485
    ChrTalk(
        0xFE,
        (
            "……お、あの看護師さん\x01",
            "こっちをチラチラ見てる。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xFE,
        (
            "うーん、看護師さんは\x01",
            "レベル高い人が多いなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x104,
        (
            "#0309F全くもって同感だぜ。\x01",
            "ね、セシルさん！\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x136,
        (
            "#1309Fあらあら……ふふ。\x01",
            "そんなこと言っても何も出ないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x101,
        "#0006F（セシル姉、馴染みすぎ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_92A3")

    label("loc_926A")


    #C0490
    ChrTalk(
        0xFE,
        (
            "んー、そろそろ呼ばれそうだな。\x01",
            "心の準備をしとこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92A3")

    Jump("loc_92F6")

    label("loc_92A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_92F6")

    #C0491
    ChrTalk(
        0xFE,
        (
            "ふーん、始めてこの病院に来たけど……\x01",
            "結構小奇麗な所じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_92F6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_29_8FA1 end

    def Function_30_92FE(): pass

    label("Function_30_92FE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9392")
    Jump("loc_93DC")

    label("loc_9392")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_93B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93DC")

    label("loc_93B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93D2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_93DC")

    label("loc_93D2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_93DC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_944A")

    #C0492
    ChrTalk(
        0xFE,
        (
            "今日で通院終わりなの。\x01",
            "うふ、早く終わってよかったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9568")

    label("loc_944A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_94E7")

    #C0493
    ChrTalk(
        0xFE,
        (
            "ただ病気を治すだけなら、\x01",
            "大聖堂で調薬してもらった方が\x01",
            "安上がりなんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0xFE,
        (
            "ここなら色々と検査してもらえるから\x01",
            "安心できるのよねー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9568")

    label("loc_94E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_9568")

    #C0495
    ChrTalk(
        0xFE,
        (
            "この病院はいいところよ。\x01",
            "親身になって診てくれるからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0496
    ChrTalk(
        0xFE,
        (
            "街からちょっと遠いけど\x01",
            "バスのおかげですぐ来れるしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9568")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_30_92FE end

    def Function_31_9570(): pass

    label("Function_31_9570")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9604")
    Jump("loc_964E")

    label("loc_9604")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9624")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_964E")

    label("loc_9624")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9644")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_964E")

    label("loc_9644")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_964E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0497
    ChrTalk(
        0xFE,
        (
            "わしゃ、今まで七耀教会の薬しか\x01",
            "使うたことがないんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0xFE,
        "病院なんて、大丈夫なんかのう……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_9570 end

    def Function_32_96DE(): pass

    label("Function_32_96DE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9772")
    Jump("loc_97BC")

    label("loc_9772")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9792")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97BC")

    label("loc_9792")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97B2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_97BC")

    label("loc_97B2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97BC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0499
    ChrTalk(
        0xFE,
        (
            "へへ……綺麗な女医さんに\x01",
            "診察してもらいてぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0xFE,
        "どうか、オッサンにあたりませんように！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_96DE end

    def Function_33_984A(): pass

    label("Function_33_984A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98DE")
    Jump("loc_9928")

    label("loc_98DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_98FE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9928")

    label("loc_98FE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_991E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9928")

    label("loc_991E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9928")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0501
    ChrTalk(
        0xFE,
        (
            "こらっ！\x01",
            "病院では静かになさい！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_33_984A end

    def Function_34_997E(): pass

    label("Function_34_997E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9A12")
    Jump("loc_9A5C")

    label("loc_9A12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9A32")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A5C")

    label("loc_9A32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A52")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9A5C")

    label("loc_9A52")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9A5C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0502
    ChrTalk(
        0xFE,
        (
            "診てくれる先生は\x01",
            "教授って聞いてたから\x01",
            "少し怖い気がしてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0xFE,
        (
            "丁寧に話してくださるし、\x01",
            "なかなか良い先生じゃないかね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_34_997E end

    def Function_35_9B0C(): pass

    label("Function_35_9B0C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BA0")
    Jump("loc_9BEA")

    label("loc_9BA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9BC0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BEA")

    label("loc_9BC0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9BE0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9BEA")

    label("loc_9BE0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9BEA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0504
    ChrTalk(
        0xFE,
        (
            "あー、今日は商談があるから\x01",
            "早めに帰りたいのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0xFE,
        (
            "うむむ、まどろっこしい。\x01",
            "はやく順番が回ってこないのかね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_35_9B0C end

    def Function_36_9C8F(): pass

    label("Function_36_9C8F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D23")
    Jump("loc_9D6D")

    label("loc_9D23")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9D43")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D6D")

    label("loc_9D43")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9D63")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9D6D")

    label("loc_9D63")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9D6D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0506
    ChrTalk(
        0xFE,
        (
            "ちょっとおなかを\x01",
            "冷やしちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0xFE,
        (
            "……やっぱり、\x01",
            "夜中に窓開けっ放しで\x01",
            "寝たりしたらだめねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_36_9C8F end

    def Function_37_9E03(): pass

    label("Function_37_9E03")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E97")
    Jump("loc_9EE1")

    label("loc_9E97")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9EB7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9EE1")

    label("loc_9EB7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9ED7")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9EE1")

    label("loc_9ED7")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9EE1")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A06B")
    SetChrSubChip(0xFE, 0x0)

    #C0508
    ChrTalk(
        0xFE,
        "Ｚｚｚ……\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FB8")
    Jump("loc_A002")

    label("loc_9FB8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FD8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A002")

    label("loc_9FD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FF8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A002")

    label("loc_9FF8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A002")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0509
    ChrTalk(
        0xFE,
        (
            "……はっ！\x01",
            "あんまり待たせるもんだから\x01",
            "寝ちゃってたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_A0B3")

    label("loc_A06B")


    #C0510
    ChrTalk(
        0xFE,
        (
            "ふー、危ない危ない。\x01",
            "病院の待合室ってなんだか\x01",
            "眠っちゃうんだよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0B3")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_37_9E03 end

    def Function_38_A0BB(): pass

    label("Function_38_A0BB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A14F")
    Jump("loc_A199")

    label("loc_A14F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A16F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A199")

    label("loc_A16F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A18F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A199")

    label("loc_A18F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A199")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0511
    ChrTalk(
        0xFE,
        (
            "開会式の見物に行ったら\x01",
            "人ごみの中で腰を痛めてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0xFE,
        (
            "記念祭もこれからだ。\x01",
            "とっとと治して遊びまくるぞい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_38_A0BB end

    def Function_39_A238(): pass

    label("Function_39_A238")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A2CC")
    Jump("loc_A316")

    label("loc_A2CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A2EC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A316")

    label("loc_A2EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A30C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A316")

    label("loc_A30C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A316")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0513
    ChrTalk(
        0xFE,
        (
            "この病院は\x01",
            "相変わらず急がしそうじゃの。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_39_A238 end

    def Function_40_A370(): pass

    label("Function_40_A370")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A404")
    Jump("loc_A44E")

    label("loc_A404")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A424")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A44E")

    label("loc_A424")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A444")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A44E")

    label("loc_A444")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A44E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5EE")
    OP_52(0x27, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x27, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A511")
    Jump("loc_A55B")

    label("loc_A511")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A531")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A55B")

    label("loc_A531")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A551")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A55B")

    label("loc_A551")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A55B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x27, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0514
    ChrTalk(
        0xFE,
        (
            "これこれ、\x01",
            "静かにしてないとだめよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0xFE,
        (
            "記念祭なら熱が下がってから\x01",
            "連れてってあげるからね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x1, 6)
    Jump("loc_A638")

    label("loc_A5EE")


    #C0516
    ChrTalk(
        0xFE,
        (
            "この子、記念祭が楽しみで\x01",
            "眠れなかったせいか\x01",
            "熱を出しちゃったんです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A638")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_40_A370 end

    def Function_41_A640(): pass

    label("Function_41_A640")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A6D4")
    Jump("loc_A71E")

    label("loc_A6D4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A6F4")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A71E")

    label("loc_A6F4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A714")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A71E")

    label("loc_A714")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A71E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0517
    ChrTalk(
        0xFE,
        "うあーん、お祭りいきたいよー。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_41_A640 end

    def Function_42_A76F(): pass

    label("Function_42_A76F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A803")
    Jump("loc_A84D")

    label("loc_A803")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A823")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A84D")

    label("loc_A823")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A843")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A84D")

    label("loc_A843")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A84D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0518
    ChrTalk(
        0xFE,
        (
            "ごほごほ……\x01",
            "うー、苦しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xFE,
        "こりゃ人にうつされたかな……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_42_A76F end

    def Function_43_A8BD(): pass

    label("Function_43_A8BD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A951")
    Jump("loc_A99B")

    label("loc_A951")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A971")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A99B")

    label("loc_A971")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A991")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A99B")

    label("loc_A991")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A99B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x2)

    #C0520
    ChrTalk(
        0xFE,
        (
            "ちょっとぉ\x01",
            "わたしにまでうつさないでよね？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_43_A8BD end

    def Function_44_A9FF(): pass

    label("Function_44_A9FF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AA93")
    Jump("loc_AADD")

    label("loc_AA93")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AAB3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AADD")

    label("loc_AAB3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AAD3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AADD")

    label("loc_AAD3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AADD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC88")

    #C0521
    ChrTalk(
        0xFE,
        (
            "昨日、クロスベル市の旧市街で\x01",
            "大白熱のイベントがあってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0xFE,
        (
            "俺は観戦してたんだけど、\x01",
            "興奮のあまりすっ転んじゃって\x01",
            "このザマさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x104,
        (
            "#0306F（……これって間接的に、\x01",
            "  俺たちがケガさせたことに\x01",
            "  なっちまうのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        (
            "#0005F（え、ええと……\x01",
            "  そこまで考えすぎることは\x01",
            "  ないと思うけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0xFE,
        (
            "ま、ケガはしたけど自分のせいだし\x01",
            "何より楽しかったから、よしとするさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_ACC7")

    label("loc_AC88")


    #C0526
    ChrTalk(
        0xFE,
        (
            "あのレース、毎年やれば\x01",
            "相当盛り上がると思うんだけどなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACC7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_44_A9FF end

    def Function_45_ACCF(): pass

    label("Function_45_ACCF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AD63")
    Jump("loc_ADAD")

    label("loc_AD63")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AD83")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADAD")

    label("loc_AD83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADA3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ADAD")

    label("loc_ADA3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_ADAD")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0527
    ChrTalk(
        0xFE,
        (
            "はぁ～、再診日が今日なんて\x01",
            "ついてないよ。\x01",
            "確実にパレードを見逃しちまう。\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0xFE,
        (
            "まぁ、明日じゃないだけマシか。\x01",
            "さっさと診察を済ませて帰ろっと。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_45_ACCF end

    def Function_46_AE6D(): pass

    label("Function_46_AE6D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AF01")
    Jump("loc_AF4B")

    label("loc_AF01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_AF21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF4B")

    label("loc_AF21")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AF41")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AF4B")

    label("loc_AF41")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AF4B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0529
    ChrTalk(
        0xFE,
        (
            "予定だとわしは今日で\x01",
            "通院が終わりなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0xFE,
        (
            "診察が終わったら、\x01",
            "婆さんとゆっくり記念祭を\x01",
            "回るかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_46_AE6D end

    def Function_47_AFE7(): pass

    label("Function_47_AFE7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B07B")
    Jump("loc_B0C5")

    label("loc_B07B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B09B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B0C5")

    label("loc_B09B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B0C5")

    label("loc_B0BB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B0C5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0531
    ChrTalk(
        0xFE,
        (
            "おほほ、主人たら\x01",
            "いつまでも気持ちばっかり\x01",
            "若いんですから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_47_AFE7 end

    def Function_48_B132(): pass

    label("Function_48_B132")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B1C6")
    Jump("loc_B210")

    label("loc_B1C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B1E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B210")

    label("loc_B1E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B206")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B210")

    label("loc_B206")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B210")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0532
    ChrTalk(
        0xFE,
        (
            "今から診察受けて\x01",
            "定期バスで街に戻って\x01",
            "そこから水上バスに乗って……\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0xFE,
        (
            "うん、まだ余裕で遊べそうだな。\x01",
            "よかったよかった。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_48_B132 end

    def Function_49_B2BC(): pass

    label("Function_49_B2BC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B350")
    Jump("loc_B39A")

    label("loc_B350")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B370")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B39A")

    label("loc_B370")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B390")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B39A")

    label("loc_B390")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B39A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0534
    ChrTalk(
        0xFE,
        (
            "今日は夕方から\x01",
            "彼とミシュラムに行く予定なの。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x2E, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x2E, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B486")
    Jump("loc_B4D0")

    label("loc_B486")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B4A6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4D0")

    label("loc_B4A6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B4C6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B4D0")

    label("loc_B4C6")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B4D0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2E, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2E, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0535
    ChrTalk(
        0xFE,
        (
            "……ほら、順番は次でしょ。\x01",
            "はやく呼ばれなさいよ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_49_B2BC end

    def Function_50_B538(): pass

    label("Function_50_B538")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B5CC")
    Jump("loc_B616")

    label("loc_B5CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B5EC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B616")

    label("loc_B5EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B60C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B616")

    label("loc_B60C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B616")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0536
    ChrTalk(
        0xFE,
        (
            "記念祭最終日だってのに\x01",
            "今日も人が来てるなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_50_B538 end

    def Function_51_B678(): pass

    label("Function_51_B678")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B70C")
    Jump("loc_B756")

    label("loc_B70C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B72C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B756")

    label("loc_B72C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B74C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B756")

    label("loc_B74C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B756")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_B809")

    #C0537
    ChrTalk(
        0xFE,
        (
            "とにかく、薬に頼るよりも\x01",
            "生活を改めるよう強く言われたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0538
    ChrTalk(
        0xFE,
        (
            "仕事柄なかなか厳しいけど……\x01",
            "まぁ、健康には代えられないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B874")

    label("loc_B809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_B874")

    #C0539
    ChrTalk(
        0xFE,
        (
            "ごほごほ……やはり\x01",
            "早めに診てもらえば良かったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0xFE,
        (
            "つい仕事に\x01",
            "かまけてしまってなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B874")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_51_B678 end

    def Function_52_B87C(): pass

    label("Function_52_B87C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B910")
    Jump("loc_B95A")

    label("loc_B910")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B930")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B95A")

    label("loc_B930")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B950")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B95A")

    label("loc_B950")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B95A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_B9DC")

    #C0541
    ChrTalk(
        0xFE,
        "先生にお薬を貰ったのよ。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0xFE,
        (
            "これでお義父さんの具合も\x01",
            "良くなるかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA45")

    label("loc_B9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BA45")

    #C0543
    ChrTalk(
        0xFE,
        (
            "ロビーの順番待ちって\x01",
            "長く感じちゃうのよねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xFE,
        (
            "付き添いで来てると\x01",
            "余計に感じちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA45")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_52_B87C end

    def Function_53_BA4D(): pass

    label("Function_53_BA4D")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BAE1")
    Jump("loc_BB2B")

    label("loc_BAE1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BB01")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB2B")

    label("loc_BB01")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BB21")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BB2B")

    label("loc_BB21")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BB2B")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_BBAE")

    #C0545
    ChrTalk(
        0xFE,
        "順番的には、そろそろ次だなー。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0xFE,
        "ううむ、本でも持ってくればよかった……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BC0C")

    label("loc_BBAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BC0C")

    #C0547
    ChrTalk(
        0xFE,
        "ふーん、結構面倒なんだな。\x02",
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0xFE,
        (
            "ま、これで診察が\x01",
            "スムーズになるなら仕方ないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC0C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_53_BA4D end

    def Function_54_BC14(): pass

    label("Function_54_BC14")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BCA8")
    Jump("loc_BCF2")

    label("loc_BCA8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BCC8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BCF2")

    label("loc_BCC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCE8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BCF2")

    label("loc_BCE8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BCF2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_BD7F")

    #C0549
    ChrTalk(
        0xFE,
        (
            "持病も、かなり完治が\x01",
            "ちかづいとるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0550
    ChrTalk(
        0xFE,
        (
            "がんばって通院した甲斐が\x01",
            "あったわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDA8")

    label("loc_BD7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BDA8")

    #C0551
    ChrTalk(
        0xFE,
        "はよう順番が来んかのう……\x02",
    )

    CloseMessageWindow()

    label("loc_BDA8")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_54_BC14 end

    def Function_55_BDB0(): pass

    label("Function_55_BDB0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE44")
    Jump("loc_BE8E")

    label("loc_BE44")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BE64")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE8E")

    label("loc_BE64")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE84")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BE8E")

    label("loc_BE84")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BE8E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_BEFE")

    #C0552
    ChrTalk(
        0xFE,
        (
            "うふふ、おじいさんの具合が\x01",
            "よくなりそうでほっとしたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF31")

    label("loc_BEFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BF31")

    #C0553
    ChrTalk(
        0xFE,
        "おじいさん、落ち着いて待ちなさいな。\x02",
    )

    CloseMessageWindow()

    label("loc_BF31")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_55_BDB0 end

    def Function_56_BF39(): pass

    label("Function_56_BF39")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BFCD")
    Jump("loc_C017")

    label("loc_BFCD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BFED")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C017")

    label("loc_BFED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C00D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C017")

    label("loc_C00D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C017")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0554
    ChrTalk(
        0xFE,
        (
            "う～……\x01",
            "熱っぽいよう……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_56_BF39 end

    def Function_57_C063(): pass

    label("Function_57_C063")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C0F7")
    Jump("loc_C141")

    label("loc_C0F7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C117")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C141")

    label("loc_C117")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C137")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C141")

    label("loc_C137")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C141")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0555
    ChrTalk(
        0xFE,
        (
            "げほげほ……\x01",
            "通院を勝手にやめたら\x01",
            "すぐぶりかえしてしまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0xFE,
        (
            "やっぱり自分だけで判断するのは\x01",
            "危険だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_57_C063 end

    def Function_58_C1E1(): pass

    label("Function_58_C1E1")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C275")
    Jump("loc_C2BF")

    label("loc_C275")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C295")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2BF")

    label("loc_C295")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C2B5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C2BF")

    label("loc_C2B5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C2BF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0557
    ChrTalk(
        0xFE,
        (
            "ここの研修医さんたちは\x01",
            "熱心に勉強していていいわよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xFE,
        "おばさんつい応援したくなっちゃうわ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_58_C1E1 end

    def Function_59_C351(): pass

    label("Function_59_C351")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3E5")
    Jump("loc_C42F")

    label("loc_C3E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C405")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C42F")

    label("loc_C405")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C425")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C42F")

    label("loc_C425")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C42F")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0559
    ChrTalk(
        0xFE,
        (
            "健康の為に東方拳法の型を真似して\x01",
            "運動していたのだが……\x01",
            "勢い余ってすっ転んでしまってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xFE,
        (
            "いやはや、無理はいかんな。\x01",
            "わっはっは。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_59_C351 end

    def Function_60_C4E7(): pass

    label("Function_60_C4E7")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C57B")
    Jump("loc_C5C5")

    label("loc_C57B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C59B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C5C5")

    label("loc_C59B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5BB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C5C5")

    label("loc_C5BB")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C5C5")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C661")

    #C0561
    ChrTalk(
        0xFE,
        "そろそろ診察の順番が回ってくるなぁ。\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xFE,
        (
            "あまり遅くなるようなら\x01",
            "宿を借りた方がいいかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C6E0")

    label("loc_C661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C6E0")

    #C0563
    ChrTalk(
        0xFE,
        (
            "初めて見ちゃったよ、\x01",
            "救急車で運ばれてくる患者。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xFE,
        (
            "いやぁ……見なきゃよかった。\x01",
            "本当に痛そうなんだもんなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6E0")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_60_C4E7 end

    def Function_61_C6E8(): pass

    label("Function_61_C6E8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C77C")
    Jump("loc_C7C6")

    label("loc_C77C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C79C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7C6")

    label("loc_C79C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7BC")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C7C6")

    label("loc_C7BC")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C7C6")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_C873")

    #C0565
    ChrTalk(
        0xFE,
        (
            "先生に診てもらったけど……\x01",
            "本当にただの風邪なのかしら！？\x02",
        )
    )

    CloseMessageWindow()

    #C0566
    ChrTalk(
        0xFE,
        (
            "何か重い病気が併発してたり\x01",
            "してたらどうしましょう！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8BA")

    label("loc_C873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_C8BA")

    #C0567
    ChrTalk(
        0xFE,
        (
            "おお、女神よ。\x01",
            "娘が大病を患っていたり\x01",
            "しませぬように……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8BA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_61_C6E8 end

    def Function_62_C8C2(): pass

    label("Function_62_C8C2")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C956")
    Jump("loc_C9A0")

    label("loc_C956")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C976")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C9A0")

    label("loc_C976")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C996")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C9A0")

    label("loc_C996")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C9A0")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_CA58")

    #C0568
    ChrTalk(
        0xFE,
        (
            "……んもう、お母さんったら\x01",
            "取り乱しちゃって\x01",
            "恥ずかしいんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0569
    ChrTalk(
        0xFE,
        (
            "ただの風邪だから心配ないって、\x01",
            "先生も言っていたでしょ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CAA7")

    label("loc_CA58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_CAA7")

    #C0570
    ChrTalk(
        0xFE,
        (
            "こほこほ……\x01",
            "もう、お母さんったら心配性ね。\x01",
            "ただの風邪だってば。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_62_C8C2 end

    def Function_63_CAAF(): pass

    label("Function_63_CAAF")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CB43")
    Jump("loc_CB8D")

    label("loc_CB43")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB63")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB8D")

    label("loc_CB63")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB83")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CB8D")

    label("loc_CB83")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CB8D")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)

    #C0571
    ChrTalk(
        0xFE,
        "ふむ、そういうシステムなわけね。\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0xFE,
        (
            "いやぁ、こうまで広いと\x01",
            "何がなにやら……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_63_CAAF end

    def Function_64_CC11(): pass

    label("Function_64_CC11")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CCA5")
    Jump("loc_CCEF")

    label("loc_CCA5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CCC5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCEF")

    label("loc_CCC5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCE5")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CCEF")

    label("loc_CCE5")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CCEF")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0573
    ChrTalk(
        0xFE,
        (
            "病院ってなんか、\x01",
            "独特の匂いがするよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0xFE,
        (
            "消毒用アルコールの匂い……\x01",
            "あたし、けっこう好きかも。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_64_CC11 end

    def Function_65_CD84(): pass

    label("Function_65_CD84")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CE18")
    Jump("loc_CE62")

    label("loc_CE18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CE38")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CE62")

    label("loc_CE38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CE58")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CE62")

    label("loc_CE58")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CE62")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0575
    ChrTalk(
        0xFE,
        "まだ午前中だというのにこの賑わい……\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xFE,
        (
            "クロスベルの者にとって、\x01",
            "随分と信頼の置ける施設のようですな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_65_CD84 end

    def Function_66_CEFC(): pass

    label("Function_66_CEFC")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CF90")
    Jump("loc_CFDA")

    label("loc_CF90")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CFB0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CFDA")

    label("loc_CFB0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CFD0")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CFDA")

    label("loc_CFD0")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CFDA")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0577
    ChrTalk(
        0xFE,
        (
            "朝早くきたのに\x01",
            "こんなに待つハメになるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xFE,
        (
            "早くするザマス！\x01",
            "あたしの腰が悲鳴をあげているザマス！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_66_CEFC end

    def Function_67_D077(): pass

    label("Function_67_D077")

    TalkBegin(0xFE)

    #C0579
    ChrTalk(
        0xFE,
        (
            "うーん、おばあちゃんの病室って\x01",
            "どこにあるんだろう……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_67_D077 end

    def Function_68_D0B9(): pass

    label("Function_68_D0B9")

    TalkBegin(0xFE)

    #C0580
    ChrTalk(
        0xFE,
        "わーいわーい、病院って広いね！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_68_D0B9 end

    def Function_69_D0E4(): pass

    label("Function_69_D0E4")

    TalkBegin(0xFE)
    OP_93(0x9, 0xB4, 0x0)
    OP_93(0x42, 0xF, 0x0)
    OP_4B(0x9, 0xFF)

    #C0581
    ChrTalk(
        0x9,
        (
            "健康診断をご希望ですか？\x01",
            "それでは、こちらの書類に\x01",
            "サインをお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x9,
        (
            "初診ですので\x01",
            "お時間頂くと思いますが\x01",
            "お待ちいただいても？\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0xFE,
        "ああ、構わないよ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_69_D0E4 end

    def Function_70_D1A5(): pass

    label("Function_70_D1A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D292")

    #C0584
    ChrTalk(
        0xFE,
        (
            "んーと、なになに？\x01",
            "『人間ドックのお知らせ』……\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xFE,
        (
            "『隠れた病気の早期発見には\x01",
            "  最新機器を駆使した\x01",
            "  総合検査をおすすめします』……\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0xFE,
        (
            "なるほど、さすがは\x01",
            "名高いウルスラ病院だ。\x01",
            "他では見ないことをやってるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D323")

    label("loc_D292")


    #C0587
    ChrTalk(
        0xFE,
        (
            "人間ドック……なんて\x01",
            "今は受けてる時間ないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xFE,
        (
            "やっぱりウルスラ病院は進んでるな。\x01",
            "最新医療技術の宝庫というのは\x01",
            "ウソではなかったか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D323")

    TalkEnd(0xFE)
    Return()

    # Function_70_D1A5 end

    def Function_71_D327(): pass

    label("Function_71_D327")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_D36D")

    #C0589
    ChrTalk(
        0x45,
        (
            "や、やっぱり夜食を食べ過ぎた。\x01",
            "腹いてぇよ……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3A0")

    label("loc_D36D")


    #C0590
    ChrTalk(
        0x45,
        "は、腹いてぇ……\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x45,
        "順番はまだかぁ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)

    label("loc_D3A0")

    TalkEnd(0xFE)
    Return()

    # Function_71_D327 end

    def Function_72_D3A4(): pass

    label("Function_72_D3A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_D6B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D637")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0592
    ChrTalk(
        0x101,
        "#0005Fあれ、遊撃士の……\x02",
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x102,
        (
            "#0101Fもしかして……\x01",
            "何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0xFE,
        (
            "ああ、旅行者が茂みに入って\x01",
            "毒ヘビか何かに\x01",
            "噛まれたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xFE,
        (
            "急いで駆けつけて、\x01",
            "ここまで搬送したんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xFE,
        (
            "まぁ、エオリアが適切に処置したから\x01",
            "大丈夫だと思うけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0x104,
        (
            "#0305F処置って……\x01",
            "遊撃士ってのは\x01",
            "そんなことまでできるんッスね？\x02",
        )
    )

    CloseMessageWindow()

    #C0598
    ChrTalk(
        0xFE,
        "エオリアは特別だよ。\x02",
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0xFE,
        (
            "医療先進国のレミフェリア出身で\x01",
            "医師免許を持っているくらいだしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0x103,
        (
            "#0211F……会う度にわたしにベタベタする\x01",
            "彼女からは想像できないんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0xFE,
        (
            "はは、まぁ普段はあれだけど\x01",
            "結構凄い奴なんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_D6B5")

    label("loc_D637")


    #C0602
    ChrTalk(
        0xFE,
        (
            "エオリアはレミフェリア出身で\x01",
            "医師免許を持っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0xFE,
        (
            "普段は可愛いものに目がないけど、\x01",
            "あれで結構凄い奴なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6B5")

    TalkEnd(0xFE)
    Return()

    # Function_72_D3A4 end

    def Function_73_D6B9(): pass

    label("Function_73_D6B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_D912")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D87B")
    OP_4B(0x47, 0xFF)
    OP_4B(0xB, 0xFF)
    TurnDirection(0x47, 0xB, 0)

    #C0604
    ChrTalk(
        0xB,
        (
            "あの旅行者は集中治療室で\x01",
            "安静にしておるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0xB,
        (
            "いや、下手をしたら足を切断しなければ\x01",
            "ならない所だったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0xB,
        (
            "エオリアくんのおかげで\x01",
            "大事なく済んでよかった。\x01",
            "いつも世話になるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x47,
        (
            "いえいえ、遊撃士として\x01",
            "当然のことをしたまでですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x104,
        (
            "#0307F#4S（くそぉっ、羨ましい！！）\x02\x03",

            "#0304F（俺もエオリアさんに優しく\x01",
            "  介抱してもらいてえぜ！）\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0x103,
        "#0211F（……無駄に興奮しないでください。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    OP_4C(0x47, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_D912")

    label("loc_D87B")


    #C0610
    ChrTalk(
        0x47,
        (
            "あー！！\x01",
            "ティオちゃんたちじゃないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x47,
        (
            "うふふ、ちょっと待ってて。\x01",
            "お仕事が終わったら\x01",
            "いっぱい愛でてあげる㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x103,
        "#0206F……遠慮しておきます。\x02",
    )

    CloseMessageWindow()

    label("loc_D912")

    TalkEnd(0xFE)
    Return()

    # Function_73_D6B9 end

    def Function_74_D916(): pass

    label("Function_74_D916")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49870, 1000, 57910, 0)
    MoveCamera(64, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 48800, 0, 57000, 0)
    SetChrPos(0x102, 50000, 0, 57000, 0)
    SetChrPos(0x103, 48800, 0, 55500, 0)
    SetChrPos(0x104, 50000, 0, 55500, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0613
    ChrTalk(
        0xC,
        (
            "#5P……ふむ、あのような要請で\x01",
            "本当に来るのだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xC,
        (
            "#5Pやはり、遊撃士に\x01",
            "頼むべきだったか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xC,
        (
            "#5Pいやしかし、この程度の仕事で\x01",
            "ミラをはたきたくはないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0x101,
        (
            "#12P#0006F（うう、声をかけにくい……）\x02\x03",

            "#0000Fあ、あの……\x01",
            "クロスベル警察、\x01",
            "特務支援課の者ですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xC, 0x1)

    #C0617
    ChrTalk(
        0xC,
        "#5Pおお……来てくれたのかね！\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xC,
        (
            "#5P君たちを待っていたのだ、\x01",
            "ささ、腰掛けてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x101,
        (
            "#12P#0003Fい、いえ、このままで結構です。\x02\x03",

            "#0000Fそれより、依頼内容を\x01",
            "聞かせて頂いてもよろしいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0xC,
        "#5Pむ、そ、そうかね。\x02",
    )

    CloseMessageWindow()

    #C0621
    ChrTalk(
        0xC,
        (
            "#5P……うぉっほん。\x01",
            "いや、頼みというのは他でもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xC,
        (
            "#5P今度内科の研究に使用する、\x01",
            "とある薬草を手に入れてきて欲しいのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0xC,
        (
            "#5P『ルピナス草』と言ってな……\x01",
            "今では希少になってしまった\x01",
            "薬草なのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0624
    ChrTalk(
        0x103,
        (
            "#12P#0205Fルピナス……というと、\x01",
            "クロスベル港湾区を流れる\x01",
            "『ルピナス川』が思い浮かびますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x104,
        (
            "#12P#0300Fその珍しい薬草を俺たちに\x01",
            "採取して来いってことっスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xC,
        "#5Pいや、厳密に言えばそうではない。\x02",
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0xC,
        (
            "#5P実はその薬草は、僅かながら\x01",
            "クロスベル大聖堂に備蓄があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xC,
        (
            "#5Pすでにエラルダ大司教に\x01",
            "連絡も差し上げているから、\x01",
            "代理人として取りに行って欲しいのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xC,
        (
            "#5P……本来なら自ら出向くのだが……\x01",
            "あー……少々、忙しくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x101,
        "#12P#0005F……？\x02",
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x102,
        (
            "#12P#0100Fなるほど、分かりました。\x01",
            "クロスベル大聖堂の\x01",
            "エラルダ大司教ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0xC,
        "#5Pうむ、よろしく頼んだぞ。\x02",
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0xC,
        (
            "#5P『ルピナス草』を手に入れたら、\x01",
            "この私の所に持ってきてくれ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0634
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【稀少薬草の回収】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_29(0x13, 0x1, 0x0)
    SetChrPos(0x0, 50500, 0, 57500, 0)
    SetChrPos(0x1, 50500, 0, 57500, 0)
    SetChrPos(0x2, 50500, 0, 57500, 0)
    SetChrPos(0x3, 50500, 0, 57500, 0)
    Sleep(500)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_74_D916 end

    def Function_75_E009(): pass

    label("Function_75_E009")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49870, 1000, 57910, 0)
    MoveCamera(64, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20540, 0)
    SetChrPos(0x101, 48800, 0, 57000, 0)
    SetChrPos(0x102, 50000, 0, 57000, 0)
    SetChrPos(0x103, 48800, 0, 55500, 0)
    SetChrPos(0x104, 50000, 0, 55500, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0635
    ChrTalk(
        0xC,
        "#5Pおお、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xC,
        (
            "#5P無事、ルピナス草を\x01",
            "受け取ってきてくれたかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        (
            "#12P#0000Fええ、何とか。\x02\x03",

            "こちらがお預かりの品です。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0638
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x341),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を渡した。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x341, 1)

    #C0639
    ChrTalk(
        0xC,
        (
            "#5Pうむ、確かに。\x01",
            "礼を言わせて貰うぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0xC,
        (
            "#5Pえー……あー。\x01",
            "それでそのぅ、なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0xC,
        (
            "#5P……エラルダ大司教は、\x01",
            "私について何か言っていたかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x103,
        (
            "#12P#0203F……いえ、特には。\x02\x03",

            "#0200F教授から出した手紙にも\x01",
            "手をつけていないようでしたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0643
    ChrTalk(
        0xC,
        "#5P……うう、やはりか。\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0xC,
        (
            "#5P返事がいつまでたっても\x01",
            "返ってこないから、\x01",
            "そんな事だろうとは思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0645
    ChrTalk(
        0x104,
        (
            "#12P#0301Fなんだ、結局連絡は取ったってのは\x01",
            "ウソだったわけか。\x02\x03",

            "#0306F行ってみたらアポなしなんだから\x01",
            "肝が冷えたッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xC,
        (
            "#5Pうむ……すまんな。\x01",
            "こういう事は話しづらくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xC,
        (
            "#5P結局会いづらくて\x01",
            "自分で受け取りにも行けず、\x01",
            "諸君に依頼してしまったわけなのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x102,
        (
            "#12P#0100F司祭の方が色々と話してくれました。\x02\x03",

            "エラルダ大司教は頑固だけど、\x01",
            "ラゴー教授のことはきっと\x01",
            "認めているはずだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0xC,
        "#5P……そうかね。\x02",
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0xC,
        (
            "#5Pもちろん私も、\x01",
            "今でもエラルダ大司教を\x01",
            "尊敬しているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0xC,
        (
            "#5P将来的に先進医療が一般的になった時、\x01",
            "あらためて謝罪と感謝の言葉を\x01",
            "伝えに行こうと思っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそうですね……\x01",
            "それがいいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0xC,
        (
            "#5P……さて、すっかり\x01",
            "世話になってしまったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0xC,
        "#5Pまた何かあったらよろしく頼む。\x02",
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x101,
        "#12P#0000Fええ、お待ちしています。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0656
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【稀少薬草の回収】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50500, 1000, 57500, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_29(0x13, 0x1, 0x3)
    OP_29(0x13, 0x4, 0x10)
    SetChrPos(0x0, 50500, 0, 57500, 0)
    SetChrPos(0x1, 50500, 0, 57500, 0)
    SetChrPos(0x2, 50500, 0, 57500, 0)
    SetChrPos(0x3, 50500, 0, 57500, 0)
    Sleep(500)
    SetChrSubChip(0xC, 0x0)
    EventEnd(0x5)
    Return()

    # Function_75_E009 end

    def Function_76_E6CA(): pass

    label("Function_76_E6CA")

    OP_4B(0x8, 0xFF)
    OP_4B(0x15, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x0, 0x8, 0)
    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(15620, 400, 7920, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, 14410, 0, 6710, 90)
    SetChrPos(0x102, 13420, 0, 4760, 90)
    SetChrPos(0x103, 12160, 0, 4910, 90)
    SetChrPos(0x104, 12810, 0, 6540, 90)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    SetChrPos(0x15, 11940, 1230, 16600, 0)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0657
    ChrTalk(
        0x8,
        "#11Pはぁ……先生ったらどこに……\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        (
            "#6P#0001Fセラさん、こんにちは。\x02\x03",

            "支援要請を受けて伺ったんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0659
    ChrTalk(
        0x8,
        "#11P特務支援課の皆さん……\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x8,
        (
            "#11Pよかった、\x01",
            "来てくれて助かりました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0661
    ChrTalk(
        0x8,
        "#11P……どうされました？\x02",
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x101,
        (
            "#6P#0006Fえ、ええっと……\x02\x03",

            "#0005F准教授が行方不明だから\x01",
            "捜索を依頼されたんですよ……ね？\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x104,
        (
            "#6P#0305F何だかいやに\x01",
            "落ち着いている気がするんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x8,
        "#11Pええ、まあ。\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x8,
        (
            "#11P落ち着いている……というか、\x01",
            "あきれていると言った方が\x01",
            "正しいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0666
    ChrTalk(
        0x102,
        "#12P#0105Fあ、あきれてる……？\x02",
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x103,
        (
            "#6P#0203F……あの、できれば状況を\x01",
            "詳しく教えていただけますか。\x02\x03",

            "#0200Fわたしたちの考える行方不明事件と\x01",
            "随分温度差があるようなんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0x8,
        "#11Pああ、そうですね。\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0x8,
        (
            "#11P問題の准教授は\x01",
            "ヨアヒム・ギュンターという方\x01",
            "なのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x8,
        (
            "#11Pヨアヒム先生は、その……\x01",
            "優秀なんですけど、たまにふらりと\x01",
            "姿を消してしまうんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0671
    ChrTalk(
        0x101,
        (
            "#6P#0003Fヨアヒム先生……\x01",
            "ああ、あの青い髪でメガネを掛けた……\x02\x03",

            "#0005Fっていうか、それって……\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x104,
        "#6P#0306F要するに、サボりってやつか。\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x8,
        "#11P身も蓋もない言い方をすればそうです。\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x8,
        (
            "#11P今日もまた、大量の仕事を残して\x01",
            "どこかに行ってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x102,
        (
            "#12P#0106F……つまり……\x02\x03",

            "#0100F遊びに行ったヨアヒム先生が\x01",
            "どこにいるのか分からない……\x01",
            "そういうことですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x8,
        "#11Pそ、そうなりますね。\x02",
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x8,
        (
            "#11Pすみません、『行方不明』なんて\x01",
            "書き方をしたのは\x01",
            "少し軽率だったかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0678
    ChrTalk(
        0x101,
        "#6P#0003F……どうする、みんな？\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x103,
        (
            "#6P#0203F……正直、後回しでも良いかと。\x02\x03",

            "#0200F聞いている限りでは\x01",
            "緊急性も低そうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0680
    ChrTalk(
        0x104,
        (
            "#6P#0306Fセラさんの頼みだから\x01",
            "聞いてやりたいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x102,
        (
            "#12P#0105Fでも、万が一にだって\x01",
            "事件に巻き込まれている可能性も……\x02",
        )
    )

    CloseMessageWindow()

    #N0682
    NpcTalk(
        0x15,
        "男の声",
        "#4Sセ、セラさーん！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_EF5B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_EF5B)

    def lambda_EF68():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_EF68)

    def lambda_EF75():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_EF75)

    def lambda_EF82():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_EF82)

    def lambda_EF8F():

        label("loc_EF8F")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_EF8F")

    QueueWorkItem2(0x8, 1, lambda_EF8F)
    OP_68(14200, 600, 9330, 1500)
    MoveCamera(45, 18, 0, 1500)
    OP_6E(400, 1500)
    SetCameraDistance(25000, 1500)
    Sleep(1500)
    ClearChrFlags(0x15, 0x80)
    OP_95(0x15, 11810, 0, 9710, 7000, 0x0)

    def lambda_EFEB():
        OP_95(0xFE, 13460, 0, 8990, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_EFEB)
    OP_68(14770, 600, 8480, 500)
    MoveCamera(45, 18, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(25000, 500)
    Sleep(500)
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x0)

    #C0683
    ChrTalk(
        0x15,
        "#5Pはぁ、はぁ、はぁ……\x02",
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x8,
        (
            "#11Pあ……リットンさん。\x01",
            "だめですよ、病院内で大声だしちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x15,
        (
            "#5Pはぁ、はぁ……\x01",
            "す……すみません……\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x104,
        (
            "#6P#0300Fああ、入院してた\x01",
            "いつぞやの研修医か。\x01",
            "元気だったかい？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x104, 0)

    #C0687
    ChrTalk(
        0x15,
        (
            "#5P……あ、こ、こんにちは。\x01",
            "その節はどうも……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x8, 0)

    #C0688
    ChrTalk(
        0x15,
        (
            "#5P……じゃなくて！\x01",
            "セラさん、ヨアヒム先生は！？\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0x8,
        (
            "#11Pええっと、すみません。\x01",
            "まだ戻ってないみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x15,
        "#5Pそ、そんなぁ……\x02",
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x15,
        (
            "#5Pうう……\x01",
            "あんな仕事量、研修医の僕に\x01",
            "どうしろってんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0692
    ChrTalk(
        0x15,
        (
            "#5P……ああ、ぼやいてる暇はない！\x01",
            "少しでも片付けないと……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F25F():

        label("loc_F25F")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_F25F")

    QueueWorkItem2(0x8, 1, lambda_F25F)
    OP_95(0x15, 11810, 0, 9710, 6000, 0x0)
    OP_95(0x15, 11940, 1230, 16600, 7000, 0x0)
    SetChrFlags(0x15, 0x80)
    Sleep(800)

    #C0693
    ChrTalk(
        0x101,
        "#6P#0005Fい、今のは……？\x02",
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_F2C3():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F2C3)

    def lambda_F2D0():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F2D0)

    def lambda_F2DD():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F2DD)

    def lambda_F2EA():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F2EA)
    Sleep(100)
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x12C)
    Sleep(200)

    #C0694
    ChrTalk(
        0x8,
        (
            "#11Pリットンさん、ヨアヒム先生に\x01",
            "よく仕事を押し付けられてるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x8,
        (
            "#11P今回先生が抜けているツケも\x01",
            "彼が死に物狂いでフォローしている\x01",
            "状態なんですよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x102,
        "#12P#0106Fた、大変そうですね……\x02",
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x104,
        (
            "#6P#0306Fんー、こりゃ放っておくわけには\x01",
            "いかないかもな。\x02\x03",

            "#0300Fいくらなんでもアイツが\x01",
            "かわいそうに思えてきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x103,
        (
            "#6P#0206F……わたしもです。\x01",
            "不憫と言ったほうが正しいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x101,
        (
            "#6P#0006Fそうだな……\x02\x03",

            "#0000Fセラさん、ヨアヒム先生の\x01",
            "行きそうな場所に\x01",
            "どこか心当たりは……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0700
    ChrTalk(
        0x8,
        (
            "#11Pまぁ、引き受けて\x01",
            "いただけるんですね。\x01",
            "ありがとうございます！\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x8,
        (
            "#11P最近、ヨアヒム先生は\x01",
            "『記念祭中に釣りの大会に出る』と\x01",
            "吹聴して回ってたそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x8,
        (
            "#11Pもしかしたら、今回の行き先に\x01",
            "関係あるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x8,
        (
            "#11Pヨアヒム先生は\x01",
            "仕事中に抜け出したので\x01",
            "まだ白衣を着たままだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x8,
        "#11Pきっと遠目にも目立つはずですよ。\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#6P#0006F釣りの大会、か……\x01",
            "よっぽど釣りが好きなんだな。\x02\x03",

            "#0003F（だとすると、東通りのあの施設で\x01",
            "  なにか分かるかもしれないな。）\x02\x03",

            "#0000F……とにかく、引き受けました。\x01",
            "見つけたら連絡を入れるので、\x01",
            "待っていてもらえますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x8,
        (
            "#11P分かりました。\x01",
            "どうかよろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0707
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【准教授の捜索願い】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14410, 1000, 6710, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 14410, 0, 6710, 90)
    SetChrPos(0x1, 14410, 0, 6710, 90)
    SetChrPos(0x2, 14410, 0, 6710, 90)
    SetChrPos(0x3, 14410, 0, 6710, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x15, 0xFF)
    ClearChrFlags(0x15, 0x40)
    SetChrFlags(0x15, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    OP_29(0x16, 0x1, 0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_76_E6CA end

    def Function_77_F880(): pass

    label("Function_77_F880")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    OP_4B(0x11, 0xFF)
    OP_68(15690, 500, 7880, 0)
    MoveCamera(51, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25880, 0)
    SetChrPos(0x101, 14410, 0, 6210, 0)
    SetChrPos(0x102, 13420, 0, 4260, 0)
    SetChrPos(0x104, 12160, 0, 4410, 0)
    SetChrPos(0x103, 12810, 0, 6140, 0)
    SetChrPos(0x8, 17210, 0, 7430, 266)
    SetChrPos(0x11, 13650, 0, 7450, 90)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    Sleep(500)
    SetCameraDistance(24880, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0708
    ChrTalk(
        0x8,
        (
            "#11Pまったく……今まで一体\x01",
            "何をなさってたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0x8,
        (
            "#11P先生がいないせいで\x01",
            "どれだけ他の人に迷惑がかかったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0x11,
        (
            "#6P#2409Fははは、実はフィッシャー杯という\x01",
            "一大イベントに参加していてね。\x02\x03",

            "#2400F釣公師団に名を連ねる以上、\x01",
            "これを逃すわけにはいかないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x8,
        (
            "#11Pもう、いい加減に\x01",
            "マジメになってくださいよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x8,
        (
            "#11Pリットンさんは今も、\x01",
            "ヨアヒム先生のお仕事を\x01",
            "肩代わりしてるんですよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0713
    ChrTalk(
        0x11,
        (
            "#6P#2405Fおぉ、リットン君が！\x02\x03",

            "#2400Fいやぁ、出来のいい教え子を持って\x01",
            "僕は幸せ者だねぇ。\x02\x03",

            "#2403F彼の作業に水を差すのは悪いし……\x01",
            "何なら、このまま\x01",
            "任せてみるのはどうだろう？\x02\x03",

            "#2409Fうんうん、それがいい。\x01",
            "きっと彼の成長にも繋がるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0714
    ChrTalk(
        0x8,
        (
            "#11P#4S#200Wお　#200W仕　#200W事　#200Wに\x01",
            "#200W戻　#200Wっ　#200Wて　#200Wく　#200Wだ　#200Wさ　#200Wい　#200W。\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0x11,
        "#6P#2406F……はい。\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0716
    ChrTalk(
        0x101,
        (
            "#12P#0006F（この人……いつも\x01",
            "  こんなカンジなのかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x103,
        (
            "#12P#0200F（准教授という地位なら\x01",
            "  かなり優秀なはずですけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0x104,
        "#12P#0309F（何とかと天才は紙一重ってやつか。）\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x102,
        "#12P#0106F（ちょっと……聞こえるわよ。）\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0xB4, 0x12C)
    Sleep(300)

    #C0720
    ChrTalk(
        0x11,
        (
            "#5P#2400F……それじゃあ、諸君。\x01",
            "僕はこれで失礼するよ。\x02\x03",

            "#2409Fまた機会があったら、\x01",
            "共に釣りをたのしもうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FE44():

        label("loc_FE44")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_FE44")

    QueueWorkItem2(0x0, 1, lambda_FE44)

    def lambda_FE56():

        label("loc_FE56")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_FE56")

    QueueWorkItem2(0x1, 1, lambda_FE56)

    def lambda_FE68():

        label("loc_FE68")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_FE68")

    QueueWorkItem2(0x2, 1, lambda_FE68)

    def lambda_FE7A():

        label("loc_FE7A")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_FE7A")

    QueueWorkItem2(0x3, 1, lambda_FE7A)

    def lambda_FE8C():

        label("loc_FE8C")

        TurnDirection(0xFE, 0x11, 300)
        Yield()
        Jump("loc_FE8C")

    QueueWorkItem2(0x8, 1, lambda_FE8C)
    OP_95(0x11, 11810, 0, 9710, 2000, 0x0)
    OP_95(0x11, 11940, 1230, 16600, 2000, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(800)

    #C0721
    ChrTalk(
        0x8,
        "#11P……また？\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)

    def lambda_FEF2():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_FEF2)

    def lambda_FEFF():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_FEFF)

    def lambda_FF0C():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_FF0C)

    def lambda_FF19():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_FF19)
    Sleep(300)

    #C0722
    ChrTalk(
        0x101,
        (
            "#6P#0003Fえ、えーっと……\x01",
            "お気になさらないでください。\x02\x03",

            "#0000Fとにかく……\x01",
            "これで依頼は完了ということで\x01",
            "よろしいですか？\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x8, 0x1)
    OP_93(0x8, 0x10E, 0x12C)
    Sleep(200)

    #C0723
    ChrTalk(
        0x8,
        (
            "#11Pあ、はい。\x01",
            "どうもありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x8,
        (
            "#11P先生がこんなに早く\x01",
            "戻ってきたのは\x01",
            "皆さんのおかげです。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x8,
        (
            "#11Pまたなにかあったら\x01",
            "病院にお越しくださいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x8,
        (
            "#11P誠意を以って\x01",
            "対応させていただきますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x101,
        (
            "#6P#0000Fええ、よろしくお願いします。\x01",
            "……ではこれで。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0728
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【准教授の捜索願い】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(14410, 1000, 6710, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x0, 14410, 0, 6710, 90)
    SetChrPos(0x1, 14410, 0, 6710, 90)
    SetChrPos(0x2, 14410, 0, 6710, 90)
    SetChrPos(0x3, 14410, 0, 6710, 90)
    OP_4C(0x8, 0xFF)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x11, 0x40)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    OP_29(0x16, 0x4, 0x10)
    OP_29(0x16, 0x1, 0x6)
    SetScenarioFlags(0x0, 0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_77_F880 end

    def Function_78_101DF(): pass

    label("Function_78_101DF")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(55410, 1000, -55440, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 55250, 0, -54750, 135)
    SetChrPos(0x102, 54080, 0, -54680, 90)
    SetChrPos(0x103, 54670, 0, -57660, 45)
    SetChrPos(0x104, 53490, 0, -57740, 45)
    SetChrPos(0x109, 52630, 0, -56430, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_93(0x13, 0x10E, 0x0)
    SetChrSubChip(0x13, 0x0)
    FadeToBright(500, 0)
    OP_0D()

    #C0729
    ChrTalk(
        0x13,
        "#11Pふぁああ……\x02",
    )

    CloseMessageWindow()

    #C0730
    ChrTalk(
        0x13,
        (
            "#11P昨日は徹夜で医療機器の\x01",
            "研究をしてたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0731
    ChrTalk(
        0x13,
        (
            "#11P携帯用のとっても便利なものを\x01",
            "設計してみたんですけど、\x01",
            "うまく行かなくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x101,
        (
            "#5P#0005F（この人……\x01",
            "  医療機器を扱ってるんだな。）\x02\x03",

            "#0003F（そうだ、シズクちゃんの\x01",
            "  プレゼントの材料……\x01",
            "  なにかいい物を持ってるかも。）\x02\x03",

            "#0000Fあの……すみません。\x01",
            "ちょっと相談があるんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0733
    ChrTalk(
        0x13,
        "#11Pはい？　何でしょうか。\x02",
    )

    CloseMessageWindow()

    #A0734
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは、プレゼントの材料集めを\x01",
            "していることを説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0735
    ChrTalk(
        0x101,
        (
            "#5P#0000F……そういうわけで、\x01",
            "何か必要のないものを\x01",
            "譲っていただけないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x13,
        (
            "#11Pあぁ、なるほどー。\x01",
            "シズクちゃんも可愛いことを\x01",
            "しますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x13,
        (
            "#11Pそうですね、だったら……\x01",
            "これなんかいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0738
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x342),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x342, 1)

    #C0739
    ChrTalk(
        0x101,
        (
            "#5P#0005Fこれは……\x01",
            "宝石を嵌められる\x01",
            "ペンダントトップですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0740
    ChrTalk(
        0x13,
        "#11Pええ、そうなんです。\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x13,
        (
            "#11Pペンダント型携帯医療機器の\x01",
            "研究中に失敗した\x01",
            "副産物なんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        (
            "#12P#0205F携帯医療機器……\x01",
            "そんなものがあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x13,
        (
            "#11Pいえいえ、まだ試作の試作、\x01",
            "実用に耐えない代物ですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0744
    ChrTalk(
        0x13,
        (
            "#11P治癒効果のある結晶回路を応用して、\x01",
            "自己治癒力を促進するっていう\x01",
            "構想なんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0745
    ChrTalk(
        0x104,
        (
            "#12P#0305Fは～……\x01",
            "さすがウルスラ病院。\x01",
            "すげぇ事を研究してんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0746
    ChrTalk(
        0x109,
        (
            "#6P#0500F警備隊に実戦配備されれば\x01",
            "かなり役立ちそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x102,
        (
            "#6P#0105Fでも、さっきは\x01",
            "失敗したとか言ってましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x13,
        (
            "#11Pええ、昨晩はそれの\x01",
            "試作型を作ってたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0749
    ChrTalk(
        0x13,
        (
            "#11Pどこで間違ったか、\x01",
            "完成した試作品を起動したら\x01",
            "爆発しちゃったんですよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0750
    ChrTalk(
        0x101,
        "#5P#0006Fあ、危ないなぁ……\x02",
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0x13,
        (
            "#11Pでも、そのペンダントトップは\x01",
            "爆発の中心にあって\x01",
            "奇跡的に無傷で残った品なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0752
    ChrTalk(
        0x13,
        (
            "#11Pそんな運の強い品なら、\x01",
            "きっと贈り物の材料に最適です。\x02",
        )
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x101,
        (
            "#5P#0006F（医療機器を研究してる人にしては\x01",
            "  非科学的な発言だなぁ……）\x02\x03",

            "#0000F……でも、ありがとうございます。\x01",
            "遠慮なくいただきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x13,
        "#11Pどうぞどうぞ～。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AF3")

    #C0755
    ChrTalk(
        0x101,
        (
            "#5P#0003F（これにシズクちゃんの\x01",
            "  持っている石をはめれば\x01",
            "  お守りになりそうだな。）\x02\x03",

            "#0000F（あとはなにかチェーンみたいな\x01",
            "  ものがあればペンダントに\x01",
            "  仕立てられそうだ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AF3")

    OP_29(0x2C, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BC5")
    OP_29(0x2C, 0x1, 0x5)

    #C0756
    ChrTalk(
        0x101,
        (
            "#5P#0000F（プレゼントの材料になりそうな物も揃ったし\x01",
            "  包装用の箱とリボンも手に入ったな……）\x02\x03",

            "（よし、そろそろシズクちゃんの所に\x01",
            "  持っていってあげよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BC5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x13, 0x5A, 0x0)
    SetChrPos(0x0, 54500, 0, -55500, 90)
    SetChrPos(0x1, 54500, 0, -55500, 90)
    SetChrPos(0x2, 54500, 0, -55500, 90)
    SetChrPos(0x3, 54500, 0, -55500, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_78_101DF end

    SaveToFile()

Try(main)
