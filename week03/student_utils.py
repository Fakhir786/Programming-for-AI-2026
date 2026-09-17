def calculate_average(marks):
    """
    Return the arithmetic mean of a non-empty marks list.
    Args: marks: Numeric marks to average.
    Returns: The arithmetic mean of the supplied marks.
    """
    return sum(marks)/len(marks)

def calculate_grade(average):
    """Return the letter grade based on the student's average."""
    if average>=85:
        return 'A'
    elif average>=70:
        return 'B'
    elif average>=60 :
        return 'C'
    elif average>=50:
        return 'D'
    else:
        return 'F'

def format_summary(name,average,grade):
    return f"{name} takes {grade} grade which makes average:{average}" 