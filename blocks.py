def get_base_blocks(text):
    base_block = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": text
            }
        }
    ]
    return base_block


def get_command_view_blocks(value):
    register_action = {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "42mate 등록하기"
        },
        "style": "primary",
        "value": "register"
    }

    join_action = {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "내일 만나기"
        },
        "style": "primary",
        "value": "join"
    }

    unjoin_action = {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "내일 만나지 않기"
        },
        "style": "danger",
        "value": "unjoin"
    }

    unregister_action = {
        "type": "button",
        "text": {
            "type": "plain_text",
            "text": "42mate 휴식하기"
        },
        "style": "danger",
        "value": "unregister",
        "confirm": {
            "title": {
                "type": "plain_text",
                "text": "정말 휴식하시겠어요?"
            },
            "text": {
                "type": "mrkdwn",
                "text": "언제라도 다시 돌아오세요"
            },
            "confirm": {
                "type": "plain_text",
                "text": "휴식하기"
            },
            "deny": {
                "type": "plain_text",
                "text": "더 생각해보기"
            }
        }
    }
    blocks = get_base_blocks("42MATE에 오신걸 환영합니다!!")
    actions = {
        "type": "actions",
        "elements": []
    }

    if value == "register" or value == "registered" or value is None:
        actions['elements'] = [join_action, unregister_action]
    elif value == "join" or value == "joined":
        actions['elements'] = [unjoin_action, unregister_action]
    elif value == "unjoin" or value == "unjoined":
        actions['elements'] = [join_action, unregister_action]
    elif value == "unregister" or value == "unregistered":
        actions['elements'] = [register_action]

    blocks.append(actions)

    return blocks