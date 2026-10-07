class PersonTracker:
    def __init__(self):
        self.person_ids = set()

    def process(self, result):
        current_ids = []

        if result.boxes is None:
            return current_ids

        if result.boxes.id is not None:
            ids = result.boxes.id.int().cpu().tolist()

            for person_id in ids:
                self.person_ids.add(person_id)
                current_ids.append(person_id)

        return current_ids

    def get_total_count(self):
        return len(self.person_ids)