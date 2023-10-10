import time


class SnowflakeIDGenerator:
    def __init__(self, machine_id, datacenter_id):
        self.machine_id = machine_id
        self.datacenter_id = datacenter_id
        self.sequence = 0
        self.last_timestamp = -1

        # Custom epoch (optional, change this if needed)
        self.epoch = int(time.mktime(time.strptime('2023-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')))

        # Max values (adjust as needed)
        self.max_machine_id = 1023
        self.max_datacenter_id = 31
        self.sequence_mask = 4095  # 12 bits for sequence

        # Check machine_id and datacenter_id
        if self.machine_id > self.max_machine_id or self.datacenter_id > self.max_datacenter_id:
            raise ValueError("Machine ID or Datacenter ID exceeds maximum values")

    def _current_timestamp(self):
        return int(time.time() * 1000) - self.epoch

    def _wait_for_next_timestamp(self, last_timestamp):
        timestamp = self._current_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._current_timestamp()
        return timestamp

    def generate_id(self):
        timestamp = self._current_timestamp()

        if timestamp < self.last_timestamp:
            raise Exception("Clock moved backward. Refusing to generate ID.")

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.sequence_mask
            if self.sequence == 0:
                timestamp = self._wait_for_next_timestamp(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp

        # Create and return the unique ID
        unique_id = ((timestamp << 22) |
                     (self.datacenter_id << 17) |
                     (self.machine_id << 12) |
                     self.sequence)

        return unique_id

# Example usage:
machine_id = 1  # Replace with your machine ID (0 to max_machine_id)
datacenter_id = 1  # Replace with your datacenter ID (0 to max_datacenter_id)

id_generator = SnowflakeIDGenerator(machine_id, datacenter_id)


if __name__ == '__main__':
    print(id_generator.generate_id())
    print(id_generator.generate_id())
    print(id_generator.generate_id())
