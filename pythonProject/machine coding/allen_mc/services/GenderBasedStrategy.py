class GenderBasedStrategy:
    def allocate(self, eligible_batches, student):
        eligible_batches.sort(key=lambda batch: batch.timing)
        for batch in eligible_batches:
            if student.gender == "Female" and len(batch.students) < batch.capacity:
                batch.students.append(student)
                return batch
        return "All batches full. Please contact next year"