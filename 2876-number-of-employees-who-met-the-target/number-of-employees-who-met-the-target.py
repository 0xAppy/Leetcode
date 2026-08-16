class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        return sum(hour >= target for hour in hours)

#Optimal

#Check each employee's hours
#hour >= target? → count them
#sum(True/False) → True acts like 1, False like 0

#TC → O(n)
#SC → O(1)
# COMEON IT SUNDAY I DO NEED A FREAKIN BREAK!!!