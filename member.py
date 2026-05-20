"""Member class for the Library Management System."""


class Member:
    """Represents a library member.
    
    Attributes:
        member_id (str): Unique identifier for the member
        name (str): Name of the member
        email (str): Email address of the member
    """
    
    def __init__(self, member_id, name, email):
        """Initialize a Member object.
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
        """
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __str__(self):
        """String representation of the member.
        
        Returns:
            str: Member information
        """
        return f"{self.member_id} - {self.name} ({self.email})"
    
    def __repr__(self):
        """Official string representation.
        
        Returns:
            str: Member representation
        """
        return f"Member({self.member_id!r}, {self.name!r}, {self.email!r})"
