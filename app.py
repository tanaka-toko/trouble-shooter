import streamlit as st

st.title("製造トラブルシューティング支援システム")

# 知識ベース（複数の症状に対応した階層構造）
knowledge_base = {
    "製品潰れ": [
        {
            "priority": "高 (40%)",
            "category": "離型タイミングの確認",
            "question": "金型があがる前に離型がONしていませんか？",
            "actions": [
                {"id": 1, "text": "離型遅れを延ばしてください"}
            ]
        },
        {
            "priority": "高 (30%)",
            "category": "ノックタイミングの確認",
            "question": "金型があがる前にノックがONしていませんか？",
            "actions": [
                {"id": 2, "text": "ノック遅れを延ばしてください"}
            ]
        },
        {
            "priority": "中 (15%)",
            "category": "送りスタートのタイミング",
            "question": "シートが剥がれる前に送りスタートしていませんか？",
            "actions": [
                {"id": 3, "text": "送りスタート遅れを延ばす"},
                {"id": 4, "text": "離型のタイミングを早くする"},
                {"id": 5, "text": "ノックのタイミングを早くする"}
            ]
        },
        {
            "priority": "低 (10%)",
            "category": "成形後の冷却不足",
            "question": "成形時間＋排気時間が短すぎませんか？",
            "actions": [
                {"id": 6, "text": "排気時間を延ばして冷却時間を取る"}
            ]
        },
        {
            "priority": "低 (5%)",
            "category": "温調設定の問題",
            "question": "金型温調温度が高すぎませんか？",
            "actions": [
                {"id": 7, "text": "温調温度を低くする"}
            ]
        },
        {
            "priority": "低 (5%)",
            "category": "バルブ動作不良の問題",
            "question": "離型エアは正しく出ていますか？",
            "actions": [
                {"id": 8, "text": "離型エア圧力ゲージの針が動いているか"},
                {"id": 9, "text": "離型エアが手動で正しく出ているか"},
                {"id": 10, "text": "上排気や上真空など他のバルブにリークしていないか"}
            ]
        }
    ],
    "レインドロップの発生": [
        {
            "priority": "高 (50%)",
            "category": "温度の確認",
            "question": "設定温度が高すぎませんか？",
            "actions": [
                {"id": 11, "text": "設定温度を下げてください"}
            ]
        },
        {
            "priority": "中 (50%)",
            "category": "SSRの確認",
            "question": "SSR（ソリッド・ステート・リレー）がずっとONもしくはずっとOFFになっていませんか？",
            "actions": [
                {"id": 12, "text": "SSRの動作状態（出力・配線）を確認・交換してください"}
            ]
        }
    ]
}

# 症状の選択
symptom = st.selectbox("発生している症状を選んでください", ["選択してください"] + list(knowledge_base.keys()))

if symptom != "選択してください":
    st.subheader(f"【第1階層】「{symptom}」の原因・チェック項目の選択")
    st.write("該当しそうな確認項目を選んでください。")
    
    # 選択された症状のリストをループで表示
    for item in knowledge_base[symptom]:
        with st.expander(f"【優先度: {item['priority']}】 {item['category']} "):
            st.markdown(f"**【確認すべきこと】** {item['question']}")
            st.markdown("---")
            st.write("**【第2階層】試すべき具体的な対策（どれで直りましたか？）**")
            
            # 第2階層の具体的な対策ごとにボタンを配置
            for action in item["actions"]:
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"・ {action['text']}")
                with col2:
                    if st.button("直った！", key=f"act_{action['id']}"):
                        st.success(f"記録しました：対策ID [{action['id']}] で解決！")
                        st.balloons()