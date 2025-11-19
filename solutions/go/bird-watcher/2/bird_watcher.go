package birdwatcher


func TotalBirdCount(birdsPerDay []int) int {
	birdsum := 0
	for i := range birdsPerDay {
		birdsum += birdsPerDay[i]
	}
	return birdsum
}

func BirdsInWeek(birdsPerDay []int, week int) int {
	return TotalBirdCount(birdsPerDay[(week-1) * 7:week * 7])
}

func FixBirdCountLog(birdsPerDay []int) []int {
	for i := 0; i < len(birdsPerDay); i += 2 {
		birdsPerDay[i]++
	}
	return birdsPerDay
}
