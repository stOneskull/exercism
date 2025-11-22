package interest


func InterestRate(balance float64) float32 {
	switch {
	case balance < 0: return 3.213
	case balance < 1000: return 0.5
	case balance < 5000: return 1.621
	default: return 2.475
	}
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
