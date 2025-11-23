package chessboard


// Type File is a slice of bools which stores if a square is occupied by a piece
type File []bool

// Type Chessboard contains a map of eight Files, accessed with keys "A" to "H"
type Chessboard map[string]File


// CountInFile returns how many squares are occupied on the chessboard,
// within the given file.
func CountInFile(cb Chessboard, file string) (occupied int) {
	board_file, exists := cb[file]
	if !exists {return}

	for _, is_occupied := range board_file {
		if is_occupied {occupied++}
	}
	return
}

// CountInRank returns how many squares are occupied on the chessboard,
// within the given rank.
func CountInRank(cb Chessboard, rank int) (occupied int) {
	if rank < 1 || rank > 8 {return}
	for _, board_file := range cb {
		if board_file[rank-1] {occupied++}
	}
	return
}

// CountAll should count how many squares are present on the chessboard.
func CountAll(cb Chessboard) (present int) {
	for _, board_file := range cb {
		for range board_file {present++}
	}
	return
}

// CountOccupied returns how many squares are occupied in the chessboard.
func CountOccupied(cb Chessboard) (occupied int) {
	for board_file := range cb {
		occupied += CountInFile(cb, board_file)
	}
	return
}
