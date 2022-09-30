import json


def load_json():
    with open('posts.json', 'r', encoding="utf-8") as file:
        return json.load(file)


def search_name(s):
    result = []
    for name in load_json():
        if s in name['content']:
            result.append(name)
    return result


def post_save(post: dict):
    posts = load_json()
    posts.append(post)
    with open('posts.json', 'w', encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
