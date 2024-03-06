import sys
import requests

api = "https://api.open5e.com"


def get_monsters_by_name(keyword_name):
    results = requests.get(f"{api}/monsters/?search={keyword_name}").json()
    keyword_name = keyword_name.lower()
    results_names = []
    results_filtered = []
    for each in results["results"]:
        if keyword_name in each["name"].lower():
            results_names.append(each["name"])
            results_filtered.append(each)
    return results_filtered, results_names


def get_all_monsters():
    results = requests.get(f"{api}/monsters/").json()
    results_names = []
    for each in results["results"]:
        results_names.append(each["name"])
    return results, results_names


def get_spells_by_name(keyword_name):
    results = requests.get(f"{api}/spells/?search={keyword_name}").json()
    keyword_name = keyword_name.lower()
    results_names = []
    for each in results["results"]:
        if keyword_name in each["name"].lower():
            results_names.append(each["name"])
    return results, results_names


def get_conditions_by_name(keyword_name):
    results = requests.get(f"{api}/conditions/?search={keyword_name}").json()
    keyword_name = keyword_name.lower()
    results_names = []
    for each in results["results"]:
        if keyword_name in each["name"].lower():
            results_names.append(each["name"])
    return results, results_names


def get_magic_items_by_name(keyword_name):
    results = requests.get(f"{api}/magicitems/?search={keyword_name}").json()
    keyword_name = keyword_name.lower()
    results_names = []
    for each in results["results"]:
        if keyword_name in each["name"].lower():
            results_names.append(each["name"])
    return results, results_names


def get_instance(instance_type, slug):
    assert instance_type in [
        "monsters",
        "spells",
        "conditions",
        "magicitems",
    ], "instance_type must be monsters, spells, conditions, or magicitems"
    return requests.get(f"{api}/v1/{instance_type}/{slug}").json()
