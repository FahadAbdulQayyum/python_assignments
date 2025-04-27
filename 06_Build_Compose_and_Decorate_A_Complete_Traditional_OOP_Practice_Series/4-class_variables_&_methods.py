class Position:
    role_name = "Frontend Developer"

    @classmethod
    def switch_position(cls, name):
        cls.role_name = name

# Example usage
print(Position.role_name)  # Output: Frontend Developer
Position.switch_position("AI Full Stack Developer")
print(Position.role_name)  # Output: AI Full Stack Developer