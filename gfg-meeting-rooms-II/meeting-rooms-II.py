class Solution:
    def minMeetingRooms(self, start, end):
        # code here
        
        room = 0
        max_room = 0
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
            max_room = max(room,min_room)
        return max_room

