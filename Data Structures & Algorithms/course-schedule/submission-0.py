class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency_graph: list = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        
        for course, pre_req in prerequisites:
            dependency_graph[pre_req].append(course)
            indegree[course] += 1
        
        q=deque()
        completed = 0
        for i, dep_count in enumerate(indegree):
            if dep_count == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            completed+=1
            for dep_course in dependency_graph[course]:
                indegree[dep_course]-=1
                if indegree[dep_course] == 0:
                    q.append(dep_course)
        return completed == numCourses