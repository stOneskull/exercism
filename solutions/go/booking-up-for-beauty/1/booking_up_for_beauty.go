package booking

import "time"


func Schedule(date string) time.Time {
	formatted, err := time.Parse("1/2/2006 15:04:05", date)
	if err != nil {panic(err)}
	return formatted
}

func HasPassed(date string) bool {
	formatted, err := time.Parse("January 2, 2006 15:04:05", date)
	if err != nil {panic(err)}
	return time.Now().After(formatted)
}

func IsAfternoonAppointment(date string) bool {
	formatted, err := time.Parse("Monday, January 2, 2006 15:04:05", date)
	if err != nil {panic(err)}
	return formatted.Hour() >= 12 && formatted.Hour() < 18
}

func Description(date string) string {
	formatted := Schedule(date).Format("Monday, January 2, 2006, at 15:04.")
	return "You have an appointment on " + formatted
}

func AnniversaryDate() time.Time {
	return time.Date(
		time.Now().Year(), time.September, 15, 0, 0, 0, 0, time.UTC)
}
