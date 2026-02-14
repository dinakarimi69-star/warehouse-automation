import random
import matplotlib.pyplot as plt
from typing import List, Tuple


class Robot:
    

    def __init__(self, robot_id: int, start_position: Tuple[int, int]):
        self.robot_id = robot_id
        self.position = start_position
        self.path = [start_position]
        self.total_distance = 0
        self.tasks_completed = 0

    def move_to(self, target: Tuple[int, int]) -> None:
      
        distance = abs(self.position[0] - target[0]) + abs(self.position[1] - target[1])
        self.total_distance += distance
        self.position = target
        self.path.append(target)
        self.tasks_completed += 1


class Warehouse:
    

    def __init__(self, size: int, num_robots: int):
        self.size = size
        self.robots = [
            Robot(robot_id=i, start_position=(0, 0))
            for i in range(num_robots)
        ]
        self.tasks = self._generate_tasks()

    def _generate_tasks(self) -> List[Tuple[int, int]]:
        """Generate random shelf locations as tasks."""
        return [
            (random.randint(1, self.size - 1), random.randint(1, self.size - 1))
            for _ in range(15)
        ]

    def assign_tasks(self) -> None:
        for index, task in enumerate(self.tasks):
            robot = self.robots[index % len(self.robots)]
            robot.move_to(task)

    def debug_system(self) -> None:
     
        print("\n--- DEBUG REPORT ---")
        for robot in self.robots:
            if robot.tasks_completed == 0:
                print(f"⚠️ Robot {robot.robot_id} is idle.")
            if robot.total_distance > 50:
                print(f"⚠️ Robot {robot.robot_id} has excessive travel distance.")

    def visualize_paths(self) -> None:
   
        plt.figure(figsize=(8, 8))
        for robot in self.robots:
            x, y = zip(*robot.path)
            plt.plot(x, y, marker="o", label=f"Robot {robot.robot_id}")

        plt.title("Warehouse Robot Paths (Debug Visualization)")
        plt.xlabel("X Position")
        plt.ylabel("Y Position")
        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_performance(self) -> None:
    
        robot_ids = [robot.robot_id for robot in self.robots]
        distances = [robot.total_distance for robot in self.robots]

        plt.figure()
        plt.bar(robot_ids, distances)
        plt.title("Robot Travel Distance (Debug Monitor)")
        plt.xlabel("Robot ID")
        plt.ylabel("Total Distance")
        plt.show()


def main() -> None:
  
    warehouse = Warehouse(size=10, num_robots=3)
    warehouse.assign_tasks()
    warehouse.debug_system()
    warehouse.visualize_paths()
    warehouse.visualize_performance()


if __name__ == "__main__":
    main()

