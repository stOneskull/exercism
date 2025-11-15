// Package cars : functions to analyze the production in a car factory.
package cars


const (
	// OneCar : cost to make an individual car.
	OneCar = 10_000
	// TenCars : cost to make 10 cars in one go.
	TenCars = 95_000
)

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	return float64(productionRate) * successRate / 100
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	return int(CalculateWorkingCarsPerHour(productionRate, successRate) / 60)
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	// batches : multiples of 10 cars to get a cost discount on bulk.
	var batches = carsCount / 10
	// remainder : leftover individual cars with full cost.
	var remainder = carsCount % 10

	return uint(batches * TenCars + remainder * OneCar)
}
