package lasagna


func PreparationTime(layers []string, time int) int {
	if time == 0 {time = 2}
	return time * len(layers)
}

func Quantities(layers []string) (noodles int, sauce float64) {
	noodle_grams := 50
	sauce_litres := 0.2

	for _, layer := range layers {
		switch layer {
			case "noodles":	noodles += noodle_grams
			case "sauce": sauce += sauce_litres
		}
	}
	return
}

func AddSecretIngredient(friendsList, myList []string) {
	myList[len(myList)-1] = friendsList[len(friendsList)-1]
}

func ScaleRecipe(amounts []float64, portions int) []float64 {
	scaled := make([]float64, len(amounts))
	for i, amount := range amounts {
		scaled[i] = amount * float64(portions) / 2
	}
	return scaled
}
