package gross


func Units() map[string]int {
	return map[string]int{
		"quarter_of_a_dozen": 3,
		"half_of_a_dozen":    6,
		"dozen":              12,
		"small_gross":        120,
		"gross":              144,
		"great_gross":        1728,
	}
}

func NewBill() map[string]int {
	return map[string]int{}
}

func AddItem(bill, units map[string]int, item, unit string) bool {
	value, is_in := units[unit]
	if is_in {
		bill[item] += value
	}
	return is_in
}

func RemoveItem(bill, units map[string]int, item, unit string) bool {
	item_quantity, in_bill := bill[item]
	unit_value, in_units := units[unit]

	if !in_bill || !in_units || item_quantity < unit_value {
		return false
	}

	bill[item] -= unit_value

	if bill[item] == 0 {
		delete(bill, item)
	}
	return true
}

func GetItem(bill map[string]int, item string) (int, bool) {
	item_quantity, in_bill := bill[item]
	return item_quantity, in_bill
}
