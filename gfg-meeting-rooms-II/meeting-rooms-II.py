class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        
        room = 0
        min_room = 0
        i=0
        j=0
        start.sort()
        end.sort()
        while i<len(start) and j<len(end) :
            if start[i] < end[j]:
                room+=1
                i+=1
            elif start[i] > end[j]:
                room-=1
                j+=1
            else:
                room -=1
                j+=1
            min_room = max(room,min_room)
        return min_room

