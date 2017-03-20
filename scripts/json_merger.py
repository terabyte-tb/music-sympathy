# Be cautious when run this file!!!

from utils import read_from_json, write_to_json

jp = read_from_json("data/jp.json")
uk = read_from_json("data/uk.json")
us = read_from_json("data/us.json")

data = jp + uk + us

write_to_json(data, "data/data.json")
