import streamlit as st

def main():
    
    
    st.title("Welcome to Programming Hub!")
    st.write("")
    st.write("With thousands of online resources available to learn a language, it can be difficult to find the perfect one. We're here to help you out! Our professionals have dived into all the resources and have found the best ones for you to use.")
    st.write("So, are you ready to dive into the world of technology with us?")

    st.sidebar.header("Filter Options")
    se_category = st.sidebar.selectbox("Select Language", ["None", "Python", "C++", "Java"])
    s_format = st.sidebar.selectbox("Select Format", ["None", "Articles", "Videos",  "Online Courses"])
    s_difficulty = st.sidebar.selectbox("Select Difficulty", ["None", "Beginner", "Medium", "Advance"])

    if se_category == "Python":
        filter_python_resources(s_format, s_difficulty)
    elif se_category == "C++":
        filter_cpp_resources(s_format, s_difficulty)
    elif se_category == "Java":
        filter_java_resources(s_format, s_difficulty)
    else:
        st.write("Please select a language to display resources.")
    st.image("image1.jpg", use_column_width=True)

    return True
    

def filter_python_resources(s_format, s_difficulty):
    if s_format == "Articles" and s_difficulty == "Beginner":
        title = "Begin your Python Journey from today!"
        st.write(f"**Title:** {title}")
        st.write("Python is one the most sought after language in the programming world.\nIf you're not the lecture-type person who learns through videos, without wasting your further time we recommend you to check out [Python Official Documentation](https://docs.python.org/3/) This is the official python documentation which has all the syntaxes, formats, methods, classes, everything defined for you!")
        st.write("Also you can refer this website [pythontutorial](https://www.geeksforgeeks.org/python-programming-language/) fo the basic fundamemtals of python.")

    elif s_format == "Videos" and s_difficulty == "Beginner":
        title = "**Here are the few best videos we have filtered for you to make your learning easy peasy**"
        st.write(f"{title} : ")
        st.write("1) For beginner to advance: [YouTube Playlist](https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)")
        st.write("2) Project based Learning: [YouTube Playlist](https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl)")
        st.write("3) One-Shot: [YouTube Video](https://www.youtube.com/watch?v=ERCMXc8x7mc)")

    elif s_format == "Online Courses" and s_difficulty == "Beginner":
        title = "**The best certification course for you to take:**"
        st.write(f"{title} [edx_python_course](https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/home)")
        st.write("")
        st.write("**About the course:** This is an edX verified course which introduces you to the world of Python.\nIt has nine problem sets to solve after each video lecture and one final project to submit the end. An average person would approximately require one or one-and-a-half month to complete the course.")

    else:
        st.write("Please select filter options to display Python resources.")
    
    return "python"

def filter_cpp_resources(s_format, s_difficulty):
    if s_format == "Articles" and s_difficulty == "Beginner":
        title = "Start your C++ Journey today!"
        st.write(f"**Title:** {title}")
        st.write("If you prefer articles for learning, here's a great resource to get started with C++: [C++ Beginners Guide](https://www.geeksforgeeks.org/c-plus-plus/)\nIt covers all the basics of C++ programming language.")

    elif s_format == "Videos" and s_difficulty == "Beginner":
        title = "**Here are some beginner-friendly C++ videos to kickstart your learning journey**"
        st.write(f"{title} : ")
        st.write("1) Basics of C++: [YouTube Playlist](https://www.youtube.com/playlist?list=PLu0W_9lII9ai6fAMHp-acBmJONT7Y4BSG)")
        st.write("2) C++ Programming Tutorials: [YouTube Playlist](https://www.youtube.com/watch?v=vLnPwxZdW4Y&list=PLAE85DE8440AA6B83)")
    
    
    elif s_format == "Online Courses" and s_difficulty == "Beginner":
        title = "**Here are some beginner-friendly C++ online courses available for you to kickstart your learning journey**"
        st.write(f"{title} : ")
        st.write(f"1.Certification course: (https://www.coursera.org/specializations/hands-on-cpp) ")
        st.write(f"2.Beginner to Advance : [LearnC++](https://www.scaler.com/topics/course/cpp-beginners/)")




    else:
        st.write("Please select filter options to display C++ resources.")

    return "cpp"

    
    


def filter_java_resources(s_format, s_difficulty):
    if s_format == "Articles" and s_difficulty == "Beginner":
        title = "Start your Java Journey today!"
        st.write(f"**Title:** {title}")
        st.write("If you prefer articles for learning, here's a great resource to get started with Java: [Java Beginners Guide](https://www.geeksforgeeks.org/java/)\nIt covers all the basics of Java programming language.")
    
    elif s_format == "Videos" and s_difficulty == "Beginner":
        title = "**Here are some beginner-friendly Java videos to kickstart your learning journey**"
        st.write(f"{title} : ")
        st.write("1) Java Tutorial for Beginners: [YouTube Playlist](https://www.youtube.com/watch?v=eIrMbAQSU34&list=PLqq-6Pq4lTTaflXUL0v3TSm86nodn0c_u)")
        st.write("2)Project based Learning: [LearnJavaProjectBased](https://www.youtube.com/playlist?list=PLz5rnvLVJX5X-uNw75cIE7JeRmFEUsDTn)")

    elif s_format == "Online Courses" and s_difficulty == "Beginner":
        title = "**Here are some beginner-friendly Java online courses available for you to kickstart your learning journey**"
        st.write(f"{title} : ")
        st.write(f"1.[udemy_java_course](https://www.udemy.com/course/java-programming-complete-beginner-to-advanced/?couponCode=UPGRADE02223)")
        st.write(f"2.[edx_java_course](https://www.edx.org/learn/java/the-georgia-institute-of-technology-introduction-to-object-oriented-programming-with-java-i-foundations-and-syntax-basics?index=product&objectID=course-4383ff55-5943-4a5a-a538-06b09ac8742b&webview=false&campaign=Introduction+to+Object-Oriented+Programming+with+Java+I%3A+Foundations+and+Syntax+Basics&source=edX&product_category=course&placement_url=https%3A%2F%2Fwww.edx.org%2Flearn%2Fjava)")



    else:
        st.write("Please select filter options to display Java resources.")

    return "java"

if __name__ == "__main__":
    main()


       
      
 
