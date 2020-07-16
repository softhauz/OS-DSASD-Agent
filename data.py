from location import *
from model import *
from knowledge import *

POSSIBLE_SOURCES_AT_LOC_1 = ["AA", "BA", "CA", "DA", "EA", "FA", "GA"]
POSSIBLE_SOURCES_AT_LOC_2 = ["AB", "BB"]
POSSIBLE_SOURCES_AT_LOC_3 = ["AB", "BB"]
POSSIBLE_SOURCES_AT_LOC_4 = ["CB", "EB"]
POSSIBLE_SOURCES_AT_LOC_5 = ["CB", "EB"]
POSSIBLE_SOURCES_AT_LOC_6 = ["CB", "EB"]

QUARANTINES = [
    Location(1,["office","gym","grocery store","house"]),
    Location(2,["house"]),
    Location(3,["house"]),
    Location(4,["restaurant"]),
    Location(5,["gas station"]),
    Location(6,["campground"])
]

MODEL_1 = Model(
    Knowledge(
        QUARANTINES[0],
        ["AA","BA","CA"],
        "office"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 from AA, BA, or CA in the office meeting."
)

MODEL_2 = Model(
    Knowledge(
        QUARANTINES[0],
        ["AA"],
        "office"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 from AA in the office meeting.")

MODEL_3 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA"],
        "office"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 from BA in the office meeting.")

MODEL_4 = Model(
    Knowledge(
        QUARANTINES[0],
        ["CA"],
        "office"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 from CA in the office meeting.")

MODEL_5 = Model(
    Knowledge(
        QUARANTINES[0],
        ["EA"],
        "grocery store"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 through consumption of food that came in contact with EA from the grocery store.")

MODEL_6 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA"],
        "house"
    ))

MODEL_7 = Model(
    Knowledge(
        QUARANTINES[0],
        ["CA"],
        "house"
    ))

MODEL_8 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA","CA"],
        "house"
    ))

MODEL_9 = Model(
    Knowledge(
        QUARANTINES[0],
        ["DA"],
        "gym"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 from DA through the jazz dance routine in the gym's dance studio.")

MODEL_10 = Model(
    Knowledge(
        QUARANTINES[5],
        ["six friends"],
        "campground"
    ))

MODEL_11 = Model(
    Knowledge(
        QUARANTINES[5],
        ["CB"],
        "campground"
    ))

MODEL_12 = Model(
    Knowledge(
        QUARANTINES[5],
        ["EB"],
        "campground"
    ))

MODEL_13 = Model(
    Knowledge(
        QUARANTINES[5],
        ["CB","EB"],
        "campground"
    ))

MODEL_14 = Model(
    Knowledge(
        QUARANTINES[1],
        ["AB"],
        "home"
    ))

MODEL_15 = Model(
    Knowledge(
        QUARANTINES[1],
        ["BB"],
        "home"
    ))

MODEL_16 = Model(
    Knowledge(
        QUARANTINES[1],
        ["AB","BB"],
        "home"
    ))

MODEL_17 = Model(
    Knowledge(
        QUARANTINES[2],
        ["AB"],
        "home"
    ))

MODEL_18 = Model(
    Knowledge(
        QUARANTINES[2],
        ["BB"],
        "home"
    ))

MODEL_19 = Model(
    Knowledge(
        QUARANTINES[2],
        ["AB","BB"],
        "home"
    ))

MODEL_20 = Model(
    Knowledge(
        QUARANTINES[3],
        ["CB"],
        "restaurant"
    ))

MODEL_21 = Model(
    Knowledge(
        QUARANTINES[3],
        ["EB"],
        "restaurant"
    ))

MODEL_22 = Model(
    Knowledge(
        QUARANTINES[3],
        ["CB","EB"],
        "restaurant"
    ))

MODELS = [
    MODEL_1, MODEL_2, MODEL_3, MODEL_4, MODEL_5,
    MODEL_6, MODEL_7, MODEL_8, MODEL_9, MODEL_10,
    MODEL_11, MODEL_12, MODEL_13, MODEL_14, MODEL_15,
    MODEL_16, MODEL_17, MODEL_18, MODEL_19, MODEL_20,
    MODEL_21, MODEL_22
]