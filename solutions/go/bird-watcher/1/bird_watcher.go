package birdwatcher


func TotalBirdCount(birdsPerDay []int) int {
	birdsum := 0
	for i := range birdsPerDay {
		birdsum += birdsPerDay[i]
	}
	return birdsum
}

func BirdsInWeek(birdsPerDay []int, week int) int {
	birdsum := 0
	for i := (week - 1) * 7; i < (week * 7); i++ {
		birdsum += birdsPerDay[i]
	}
	return birdsum
}

func FixBirdCountLog(birdsPerDay []int) []int {
	for i := 0; i < len(birdsPerDay); i += 2 {
		birdsPerDay[i]++
	}
	return birdsPerDay
}
