def dictionary(word, mean):
    
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
                "type": "text",
                "weight": "bold",
                "size": "xxl",
                "wrap": True,
                "text": word
            },
            {
                "type": "box",
                "layout": "vertical",
                "margin": "lg",
                "spacing": "sm",
                "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "spacing": "sm",
                    "contents": [
                    {
                        "type": "text",
                        "text": "意味",
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 1
                    },
                    {
                        "type": "text",
                        "text": mean,
                        "wrap": True,
                        "color": "#666666",
                        "size": "sm",
                        "flex": 5
                    }
                    ]
                }
                ]
            }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
            {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "margin": "sm"
            }
            ],
            "flex": 0
        }
    }


