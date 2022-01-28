from ursina import *


with open("economy.json", encoding="UTF-8") as src:
    data = eval(src.read())

app = Ursina()
##

update_boxes = dict()

def draw_storage(agent):
    bar_size = 0.2
    config = {
        "Беларусь":((0,0,5),{"Картошка": color.brown}),
        "Россия":((2,2,5),{
            "Ёлки": color.green,"Медведи":color.red,"Балалайки":color.pink,"Водка":color.white}) }

    position = config[agent][0]
    storage_items = config[agent][1]
    for key in storage_items:
        storage_color = storage_items[key]
        bar_height = data["economy"]["agents"][agent]["goods"][key]["склад"] / 1000
        box = Entity(model="cube", collider="box", texture="white_cube", scale=(bar_size,bar_height,bar_size),
               position=position,color=storage_color)
        update_boxes[key] = (box,data["economy"]["agents"][agent]["goods"][key]["производство"])
        position = position[0] + bar_size, position[1], position[2]


def update():
    for entity, production in update_boxes.values():
        entity.scale = entity.scale[0], entity.scale[1] + production / 10000, entity.scale[2]
    print("fafa")




draw_storage("Беларусь")
draw_storage("Россия")


app.run()
