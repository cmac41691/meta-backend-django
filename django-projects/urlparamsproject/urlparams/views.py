from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def drinks(request: HttpRequest, drink_name) -> HttpResponse:

    drink = {
        "mocha": "coffee",  
        "tea": "beverage",
        "lemonade": "refreshment"         
}
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2> {drink_name}</h2>" + choice_of_drink)

# beverage = drink.get(choice_of_drink)

#drinks()