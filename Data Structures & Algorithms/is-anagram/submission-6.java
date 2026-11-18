class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap <Character, Integer> mapS= new HashMap<>();
        HashMap <Character, Integer> mapT= new HashMap<>();
        for (int i = 0; i<=s.length()-1;i++){
            mapS.put(s.charAt(i),mapS.getOrDefault(s.charAt(i),0)+1);
        }
        for (int i = 0; i<=t.length()-1;i++){
            mapT.put(t.charAt(i),mapT.getOrDefault(t.charAt(i),0)+1);
        }
        if(s.length()!=t.length()){
            return false;
        }
        for (char c : mapS.keySet()){
            if(!(mapS.getOrDefault(c,0).equals(mapT.getOrDefault(c,0)))){
                return false;
            }
        }
        return true;

}
}