package blackjack


func ParseCard(card string) int {
	switch card {
		case "ace":	return 11
		case "king", "queen", "jack", "ten": return 10
		case "nine": return 9
		case "eight": return 8
		case "seven": return 7
		case "six":	return 6
		case "five": return 5
		case "four": return 4
		case "three": return 3
		case "two":	return 2
		default: return 0
	}
}

func FirstTurn(card1, card2, dealerCard string) string {
	player := ParseCard(card1) + ParseCard(card2)
	dealer := ParseCard(dealerCard)
	switch {
		case player == 22: return "P"
		case player == 21 && dealer < 10: return "W"
		case player > 16: return "S"
		case player > 11 && dealer < 7: return "S"
		default: return "H"
	}
}
