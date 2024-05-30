import os
from collections import deque

class TicketQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = deque()
    # Rest of the class remains the same


    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size

    def enqueue(self, ticket):
        if self.is_full():
            print("Maaf, antrian penuh! Anda tidak dapat menambahkan data antrian.")
        else:
            self.queue.append(ticket)
            print(f"Data antrian {ticket} berhasil ditambahkan.")

    def dequeue(self):
        if self.is_empty():
            print("Maaf, antrian kosong! Anda tidak dapat menghapus data antrian.")
        else:
            removed_ticket = self.queue.popleft()
            print(f"Data antrian {removed_ticket} berhasil dihapus.")
            return removed_ticket

    def view_queue(self):
        if self.is_empty():
            print("Data antrian kosong.")
        else:
            print("List data antrian:")
            for ticket in self.queue:
                print(ticket)

    def queue_info(self):
        print("Informasi data antrian:")
        print(f"Kapasitas antrian: {self.max_size}")
        print(f"Banyak isi antrian: {len(self.queue)}")
        if not self.is_empty():
            print(f"Data antrian terdepan: {self.queue[0]}")
            print(f"Data antrian paling belakang: {self.queue[-1]}")

def main():
    max_size = 5
    ticket_queue = TicketQueue(max_size)

    while True:
        os.system("CLS")
        print("===================================")
        print("| Program Antrian Tiket Kereta Api|")
        print("===================================")
        print("Daftar Layanan :")
        print("[1] Menambah data antrian")
        print("[2] Melihat list data antrian")
        print("[3] Menghapus data antrian terdahulu")
        print("[4] Melihat Informasi data antrian")
        print("[5] Keluar dari program\n")

        choice = input("Masukkan no layanan yang dipilih: ")

        if choice == '1':
            ticket = input("Masukkan nomor tiket: ")
            ticket_queue.enqueue(ticket)
        elif choice == '2':
            ticket_queue.view_queue()
            input("Tekan [Enter] untuk melanjutkan...")
        elif choice == '3':
            ticket_queue.dequeue()
            input("Tekan [Enter] untuk melanjutkan...")
        elif choice == '4':
            ticket_queue.queue_info()
            input("Tekan [Enter] untuk melanjutkan...")
        elif choice == '5':
            os.system("CLS")
            print("=====================================")
            print("| Anda telah keluar dari program    |")
            print("|            Terimakasih            |")
            print("=====================================")
            break
        else:
            os.system("CLS")
            print("==========================================")
            print("|              Mohon Maaf,               |")
            print("| Layanan yang Anda pilih tidak tersedia |")
            print("==========================================")
            input("Tekan [Enter] untuk melanjutkan...")

if __name__ == "__main__":
    main()