(ns cars-assemble)

(def base-rate 221)

(defn- success-rate
  [speed]
  (cond
    (zero? speed) 0.0
    (<= speed 4)  1.0
    (<= speed 8) 0.9
    (== speed 9)  0.8
    (== speed 10) 0.77
    :else 0.0))

(defn production-rate
  [speed]
  (* base-rate speed (success-rate speed)))

(defn working-items
  "Calculates how many working cars are produced per minute"
  [speed]
  (cond 
    (zero? speed) 0
    :else (int (/ (production-rate speed) 60)))
  )
