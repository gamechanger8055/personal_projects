class HigherCapacityStrategy:
    def allocate(self, eligible_batches, student):
        eligible_batches.sort(key=lambda batch: batch.capacity, reverse=True)
        for batch in eligible_batches:
            if len(batch.students) < batch.capacity:
                batch.students.append(student)
                return batch
        return "All batches full. Please contact next year"