// Package weather : forecasts weather conditions of cities in Goblinocus.
package weather


// CurrentCondition : weather conditions.
var CurrentCondition string

// CurrentLocation : the city in Goblinocos.
var	CurrentLocation  string


// Forecast : returns weather conditions for a city in Goblinocus.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
