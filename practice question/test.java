class test{

    private static int[] removeLastTriplet(int[] input) {
    boolean[] toRemove = new boolean[input.length];
    Map<Integer, Integer> counts = new HashMap<>();
    LinkedList<Integer> output = new LinkedList<>();
    //Count how many times each input value is found.
    for(int value : input) {
        int count;
        if (counts.containsKey(value)) {
            count = counts.get(value);
            counts.put(value, count + 1);
        } else {
            counts.put(value, 1);
        }
    }
    for (Map.Entry<Integer, Integer> kvp : counts.entrySet()) {
        //Determine how many triplets we have for this value
        int tripletCount = kvp.getValue() / 3;
        //Keep track of where we're starting
        int currentIndex = input.length - 1;
        //Remove each triplet
        for (int tripletIndex = 0; tripletIndex < tripletCount; tripletIndex++) {
            //counts the number of elements in this triplet
            int thisTripletCount = 0;
            //Mark each member of the triplet for deletion.
            for (int inputIndex = currentIndex; thisTripletCount < 3; inputIndex--) {
                if (input[inputIndex] == kvp.getKey()) {
                    //Mark this index for removal
                    toRemove[inputIndex] = true;
                    thisTripletCount++;
                }
                //Keep track of where we are in the overall input array
                currentIndex--;
            }
        }
    }
    for (int i = 0; i < input.length; i++) {
        if (!toRemove[i]) {
            output.add(input[i]);
        }
    }
    return output.stream().mapToInt(i->i).toArray();
}

}