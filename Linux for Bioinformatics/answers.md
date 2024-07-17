# Answers to questions from "Linux for Bioinformatics"

**Q1: What is your home directory?**

A: The home directory for the user `ubuntu` is `/home/ubuntu`.

**Q2: What is the output of the `ls` command in the `my_folder/` directory?**

A: The output of the `ls` command in the `my_folder/` directory is:

```shell
hello_world.txt
```
**Q3: What is the output of each `ls` command?**

- `ls my_folder`: (no output, the directory is empty)
- `ls my_folder2`: `hello_world.txt`

**Q4: What is the output of each `ls` command?**

- `ls my_folder`: (no output, the directory is empty)
- `ls my_folder2`: (no output, the directory is empty)
- `ls my_folder3`: `hello_world.txt`

**Q5: What editor did you use and what was the command to save your file changes?**

A: I used the `nano` editor. The command to save my file changes was `Ctrl + O` followed by `Enter`, and then `Ctrl + X` to exit the editor.

**Q6. What is the error?**

A : The error encountered is Permission denied (publickey).
The error occurs because `sudouser` does not have the SSH key required for login.

**Q7. What was the solution?**

A : To enable password and keyboard-interactive authentication for SSH on your server, you need to edit the SSH configuration file (`/etc/ssh/sshd_config`) by setting `PasswordAuthentication yes` and `KbdInteractiveAuthentication yes`. After saving these changes, restart the SSH service with `systemctl restart ssh.service` to apply them. Then, exit your current session and log out. Finally, SSH into the remote server using the command `ssh sudouser@54.196.151.172`. This process ensures that the server allows password and keyboard-interactive authentication methods.


**Q8: What does the `sudo docker run` part of the command do? and what does the `salmon swim` part of the command do?**

- **`sudo docker run`**: This part of the command starts a Docker container. It creates a new container from the specified image (`combinelab/salmon`), and runs the specified command within that container. In this case, it runs the `salmon` command within the `combinelab/salmon` Docker image.

- **`salmon swim`**: This part of the command is the specific command run inside the Docker container. `salmon swim` is a command in the `salmon` software that prints version information and other details about the `salmon` tool.

**Q9. What is the output of this command?** `sudo ls /root`

[sudo] password for serveruser:
serveruser is not in the sudoers file. 

**Q10. What is the output of `flask --version`?**

A: The output is:
```shell
Python 3.10.14
Flask 3.0.3
Werkzeug 3.0.3
```

**Q11. What is the output of `mamba -V`?**

A: The output is:
```shell
mamba 1.5.8
conda 24.3.0
```

**Q12. What is the output of `which python`?**

   The output :
   ```shell
   /home/serveruser/mambaforge/envs/py27/bin/python
   ```

**Q13. What is the output of `which python` now?**

   The output :
   ```shell
   /home/serveruser/mambaforge/bin/python
   ```

**Q14. What is the output of `salmon -h`?**

The output :

```shell
salmon v1.4.0

Usage:  salmon <SUBCOMMAND> [options]

Subcommands:
    index       Create a quasi-mapping-based index
    quant       Quantify a set of reads
    alevin      Quantify barcoded (single-cell) reads
    swim        Perform super-secret operation
    ... (additional commands and options)
```

**Q15. What does the `-o athal.fa.gz` part of the command do?**

A: The `-o athal.fa.gz` part of the command specifies the output file name. It tells `curl` to save the downloaded file as `athal.fa.gz`.

**Q16. What is a `.gz` file?**

A: A `.gz` file is a file compressed using the gzip compression algorithm. It is commonly used to reduce the size of files for storage and transfer.

**Q17. What does the `zcat` command do?**

A: The `zcat` command reads compressed files (with the `.gz` extension) and outputs their uncompressed contents to the standard output.

**Q18. What does the `head` command do?**

A: The `head` command displays the first part of a file. By default, it shows the first 10 lines, but this can be adjusted with a numerical argument.

**Q19. What does the number `100` signify in the command?**

A: The number `100` specifies that the `head` command should display the first 100 lines of the uncompressed file.

**Q20. What is `|` doing?**

A: The `|` (pipe) operator takes the output of the command on its left (`zcat athal.fa.gz`) and passes it as input to the command on its right (`head -n 100`).

**Q21. What is a `.fa` file? What is this file format used for?**

A: A `.fa` file is a FASTA file, a text-based format for representing nucleotide sequences or peptide sequences. Each sequence is represented by a series of lines, with the first line starting with a `>` character followed by a sequence identifier and description, and the subsequent lines containing the sequence itself. This format is commonly used in bioinformatics for storing sequence data.

**Q22. What format are the downloaded sequencing reads in?**

A: The downloaded sequencing reads are in SRA format, which is a binary format used by NCBI for storing high-throughput sequencing data.

**Q23. What is the total size of the disk?**

A:  6.8G

Filesystem      Size  Used Avail Use% Mounted on
/dev/root       6.8G  5.3G  1.5G  80% /
tmpfs           479M     0  479M   0% /dev/shm
tmpfs           192M  936K  191M   1% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/xvda16     881M   76M  744M  10% /boot
/dev/xvda15     105M  6.1M   99M   6% /boot/efi
tmpfs            96M   12K   96M   1% /run/user/1000
tmpfs            96M   12K   96M   1% /run/user/1002

**Q24. How much space is remaining on the disk?**

A: 1.5G

**Q25. What went wrong?**

A: The error message indicates that there is not enough storage space available to complete the fastq-dump process.


(2024-05-23T20:37:16 fastq-dump.2.11.0 err: storage exhausted while writing file within file system module - system bad file descriptor error fd='5'

=============================================================
An error occurred during processing.
A report was generated into the file '/home/serveruser/ncbi_error_report.txt'.
If the problem persists, you may consider sending the file
to 'sra-tools@ncbi.nlm.nih.gov' for assistance.
=============================================================

fastq-dump quit with error code 3
(sraEnv) serveruser@ip-172-31-31-230:~$)

**Q26: What was your solution?**

A: Compress the output using gzip to save disk space during conversion.

1. **Delete the Partially-Generated `.fastq` File**:
   ```bash
   rm SRR074122.fastq
   ```

2. **Modify the `fastq-dump` Command**:
   Use gzip compression to reduce disk space usage during conversion:
   ```bash
   fastq-dump --gzip SRR074122
   ```
