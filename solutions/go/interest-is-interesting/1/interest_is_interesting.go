package interest


func InterestRate(balance float64) (rate float32) {
	switch {
	case balance < 0: rate = 3.213
	case balance < 1000: rate = 0.5
	case balance < 5000: rate = 1.621
	default: rate = 2.475
	}
	return
}

func Interest(balance float64) float64 {
	return balance * float64(InterestRate(balance)) / 100
}

func AnnualBalanceUpdate(balance float64) float64 {
	return balance + Interest(balance)
}

func YearsBeforeDesiredBalance(balance, targetBalance float64) (years int) {
	for balance < targetBalance {
		balance = AnnualBalanceUpdate(balance)
		years++
	}
	return
}
