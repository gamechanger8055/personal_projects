from services.batchController import BatchController


def main():
    system=BatchController()
    student1 = system.register("Akhilesh", "Male", "Student")
    student2 = system.register("Komal", "Female", "Student")
    student3 = system.register("Rajnish", "Male", "Student")
    student4 = system.register("Mayuri", "Female", "Student")
    #print(student1,student2,student3,student4, system.students)
    system.enroll(student1, "IIT")
    system.enroll(student2, "IIT")
    system.enroll(student3, "NEET")
    system.enroll(student4, "IIT")
    admin1 = system.register("Kamesh", "Male", "Admin")
    admin2 = system.register("Madhur", "Male", "Admin")
    batch1 = system.createBatch(admin1, 3, "IIT", "Morning")
    batch2 = system.createBatch(admin1, 2, "NEET", "Evening")
    batch3 = system.createBatch(admin1, 4, "IIT", "Evening")
    allocated_batch1 = system.allocateBatch(admin2, student2, "Gender Based")
    allocated_batch2 = system.allocateBatch(admin2, student4, "Higher capacity")
    allocated_batch3 = system.allocateBatch(admin1, student1, "Higher capacity")
    allocated_batch4 = system.allocateBatch(admin1, student3, "Higher capacity")

    print("Student 1 allocated to Batch of capacity :", allocated_batch3.capacity)
    print("Student 2 allocated to Batch of capacity :", allocated_batch1.capacity)
    print("Student 3 allocated to Batch of capacity :", allocated_batch4.capacity)
    print("Student 4 allocated to Batch of capacity :", allocated_batch2.capacity)




if __name__=="__main__":
    main()
