class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypesSorted = sorted(boxTypes, key=lambda box: box[1], reverse=True)
        currNumberOfBoxes = 0
        currUnitsPerBox = 0
        for numberOfBoxes, numberOfUnitsPerBox in boxTypesSorted:
            if numberOfBoxes <= truckSize - currNumberOfBoxes:
                currNumberOfBoxes += numberOfBoxes
                currUnitsPerBox += numberOfUnitsPerBox*numberOfBoxes
            else:
                # Get box until be full
                for i in range(numberOfBoxes, 0, -1):
                    if truckSize > currNumberOfBoxes:
                        currUnitsPerBox += numberOfUnitsPerBox
                        currNumberOfBoxes += 1
                    else: break
                    
        return currUnitsPerBox
