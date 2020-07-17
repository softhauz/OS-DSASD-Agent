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
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 through a social interaction with BA in the dinner party.")

MODEL_7 = Model(
    Knowledge(
        QUARANTINES[0],
        ["CA"],
        "house"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 through a social interaction with CA in the dinner party.")

MODEL_8 = Model(
    Knowledge(
        QUARANTINES[0],
        ["BA","CA"],
        "house"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 1 through a social interaction with BA or CA in the dinner party.")

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
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 6 from a social interaction with one or more of Couple 2's six friends in the camp bonfire.")

MODEL_11 = Model(
    Knowledge(
        QUARANTINES[5],
        ["CB"],
        "campground"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 6 from a social interaction with one or more of Couple 2's six friends in the camp bonfire.")

MODEL_12 = Model(
    Knowledge(
        QUARANTINES[5],
        ["EB"],
        "campground"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 6 from a social interaction with EB in the camp bonfire.")

MODEL_13 = Model(
    Knowledge(
        QUARANTINES[5],
        ["CB","EB"],
        "campground"
    ),
    "You have acquired Covid-19 disease on January 9, 2020 at Location 6 from a social interaction with CB or EB in the camp bonfire.")

MODEL_14 = Model(
    Knowledge(
        QUARANTINES[1],
        ["AB"],
        "house"
    ),
    "You have acquired Covid-19 disease at Location 2 through a close contact with AB during Couple 1's home visit on January 9, 2020.")

MODEL_15 = Model(
    Knowledge(
        QUARANTINES[1],
        ["BB"],
        "house"
    ),
    "You have acquired Covid-19 disease at Location 2 through a close contact with BB during Couple 1's home visit on January 9, 2020.")

MODEL_16 = Model(
    Knowledge(
        QUARANTINES[1],
        ["AB","BB"],
        "house"
    ),
    "You have acquired Covid-19 disease at Location 2 through a close contact with AB or BB during Couple 1's home visit on January 9, 2020.")

MODEL_17 = Model(
    Knowledge(
        QUARANTINES[2],
        ["AB"],
        "house"
    ),
    "You have acquired Covid-19 disease at Location 3 through a close contact with AB during Couple 1's home visit on January 9, 2020.")

MODEL_18 = Model(
    Knowledge(
        QUARANTINES[2],
        ["BB"],
        "house"
    ),
    "You have acquired Covid-19 disease at Location 3 through a close contact with BB during Couple 1's home visit on January 9, 2020.")

MODEL_19 = Model(
    Knowledge(
        QUARANTINES[2],
        ["AB","BB"],
        "house"
    ),
    "You have acquired Covid-19 disease at Location 3 through a close contact with AB or BB during Couple 1's home visit on January 9, 2020.")

MODEL_20 = Model(
    Knowledge(
        QUARANTINES[3],
        ["CB"],
        "restaurant"
    ),
    "You have acquired Covid-19 disease at Location 4 through a close contact with CB from the afternoon snack on January 9, 2020.")

MODEL_21 = Model(
    Knowledge(
        QUARANTINES[3],
        ["EB"],
        "restaurant"
    ),
    "You have acquired Covid-19 disease at Location 4 through a close contact with EB from the afternoon snack on January 9, 2020.")

MODEL_22 = Model(
    Knowledge(
        QUARANTINES[3],
        ["CB","EB"],
        "restaurant"
    ),
    "You have acquired Covid-19 disease at Location 4 through a close contact with CB or EB from the afternoon snack on January 9, 2020.")

MODELS = [
    MODEL_1, MODEL_2, MODEL_3, MODEL_4, MODEL_5,
    MODEL_6, MODEL_7, MODEL_8, MODEL_9, MODEL_10,
    MODEL_11, MODEL_12, MODEL_13, MODEL_14, MODEL_15,
    MODEL_16, MODEL_17, MODEL_18, MODEL_19, MODEL_20,
    MODEL_21, MODEL_22
]