#Problem 1

def split_logs(machines):
    """
    Split each machine's log into info.log, warning.log, and error.log.

    Args:
        Machines: Dict mapping machine name -> Log file name

    Returns:
        dict {machine: {"INFO": n, "WARNING": n, "ERROR": n}}
    """
    counts = {}
    with open("info.log", "w") as info_log, open("warning.log", "w") as warning_log, open("error.log", "w") as error_log:
        for machine, log_name in machines.items():
            counts[machine] = {"INFO": 0, "WARNING": 0, "ERROR": 0}
            with open(log_name, "r") as log:
                for line in log:
                    line = line.strip()
                    if line == "":
                        continue
                    entry = f"{machine} | {line}\n"
                    if "[ERROR]" in line:
                        error_log.write(entry)
                        counts[machine]["ERROR"] += 1
                    elif "[WARNING]" in line:
                        warning_log.write(entry)
                        counts[machine]["WARNING"] += 1
                    elif "[INFO]" in line:
                        info_log.write(entry)
                        counts[machine]["INFO"] += 1
    return counts

def print_report(counts, error_file="error.log"):
    """Print the security status report."""
    print("SECURITY LOG REPORT")
    print("=" * 40)

    totals = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for machine, levels in counts.items():
        total = levels["INFO"] + levels["WARNING"] + levels["ERROR"]
        if levels["ERROR"] >= 2:
            status = "CRITICAL"
        elif levels["ERROR"] >= 1 or levels["WARNING"] >= 1:
            status = "NEEDS ATTENTION"
        else:
            status = "OK"
        print(f"{machine}: {total} entries | INFO {levels['INFO']} | WARNING {levels['WARNING']} | ERROR {levels['ERROR']} | Status: {status}")
        totals["INFO"] += levels["INFO"]
        totals["WARNING"] += levels["WARNING"]
        totals["ERROR"] += levels["ERROR"]

    print("-" * 40)
    grand_total = totals["INFO"] + totals["WARNING"] + totals["ERROR"]
    print(f"Total: {grand_total} entries | INFO {totals['INFO']} | WARNING {totals['WARNING']} | ERROR {totals['ERROR']}")

    print(f"Errors ({error_file}):")
    with open(error_file, "r") as errors:
        for line in errors:
            print(f"  {line.strip()}")

#Test Cases

with open("server_a.log", "w") as f:
    f.write("2026-10-05 08:01:12 [INFO] User alice logged in\n")
    f.write("2026-10-05 08:03:45 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:03:59 [WARNING] Failed login attempt for user root\n")
    f.write("2026-10-05 08:04:10 [ERROR] Account root locked after repeated failures\n")
    f.write("2026-10-05 08:15:30 [INFO] Firewall rules reloaded\n")
    f.write("2026-10-05 09:02:11 [INFO] User alice logged out\n")

with open("server_b.log" , "w") as f:
    f.write("2026-10-05 08:00:05 [INFO] System boot complete\n")
    f.write("2026-10-05 08:20:41 [ERROR] Disk encryption service failed to start\n")
    f.write("2026-10-05 08:21:02 [WARNING] Unencrypted volume mounted\n")
    f.write("2026-10-05 08:45:19 [INFO] User bob logged in\n")
    f.write("2026-10-05 09:10:33 [ERROR] Unauthorized access attempt on port 22\n")
    f.write("\n")
    f.write("2026-10-05 09:30:00 [INFO] Backup completed\n")

counts = split_logs({"server_a": "server_a.log", "server_b": "server_b.log"})
print(counts)

with open("warning.log", "r") as f:
    print(f.read())

print_report(counts)


#Problem 2

import json
import pickle
import os

def load_incidents(csv_file):
    """Return a list of incident dicts read from the CSV file."""
    incidents = []
    with open(csv_file, "r") as incidents_csv:
        incidents_csv.readline()
        for line in incidents_csv:
            values = line.strip().split(",")
            incidents.append({
                "id": int(values[0]),
                "machine": values[1],
                "severity": values[2],
                "description": values[3]
            })
    return incidents

def save_summary(incidents, json_file):
    """Save a summary to a JSON file and return the summary dict."""
    by_machine = {}
    by_severity = {}
    high_ids = []
    for incident in incidents:
        machine = incident["machine"]
        severity = incident["severity"]
        if machine in by_machine:
            by_machine[machine] += 1
        else:
            by_machine[machine] = 1
        if severity in by_severity:
            by_severity[severity] += 1
        else:
            by_severity[severity] = 1
        if severity == "high":
            high_ids.append(incident["id"])

    summary = {
        "total": len(incidents),
        "by_machine": by_machine,
        "by_severity": by_severity,
        "high_ids": high_ids
    }
    with open(json_file, "w") as summary_json:
        json.dump(summary, summary_json, indent=2)
    return summary

def archive(incidents, folder):
    """Pickle all incidents and write one JSON file per machine into folder."""
    os.makedirs(folder, exist_ok=True)

    with open(os.path.join(folder, "incidents.pkl"), "wb") as incidents_pkl:
        pickle.dump(incidents, incidents_pkl)

    by_machine = {}
    for incident in incidents:
        machine = incident["machine"]
        if machine in by_machine:
            by_machine[machine].append(incident)
        else:
            by_machine[machine] = [incident]

    for machine, machine_incidents in by_machine.items():
        with open(os.path.join(folder, f"{machine}.json"), "w") as machine_json:
            json.dump(machine_incidents, machine_json, indent=2)

    return sorted(os.listdir(folder))

def load_archive(folder):
    """Return the incident list stored in folder/incidents.pkl."""
    with open(os.path.join(folder, "incidents.pkl"), "rb") as incidents_pkl:
        incidents = pickle.load(incidents_pkl)
    return incidents

#Test Cases

with open("incidents.csv", "w") as f:
    f.write("id,machine,severity,description\n")
    f.write("1,server_a,high,Account root locked\n")
    f.write("2,server_b,high,Disk encryption failed\n")
    f.write("3,server_b,low,Unencrypted volume mounted\n")
    f.write("4,server_a,medium,Repeated failed logins\n")
    f.write("5,server_b,high,Unauthorized access on port 22\n")

incidents = load_incidents("incidents.csv")
print(len(incidents))
print(incidents[0])

summary = save_summary(incidents, "summary.json")
print(summary)

with open("summary.json", "r") as f:
    print(json.load(f) == summary)

print(archive(incidents, "archive"))

with open(os.path.join("archive", "server_a.json"), "r") as f:
    print([item["id"] for item in json.load(f)])

restored = load_archive("archive")
print(restored == incidents)

#Problem 3

import shutil

def organize(folder):
    """Move files into logs/, data/, pickles/, other/ by extension."""
    moved = {"logs": [], "data": [], "pickles": [], "other": []}
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            extension = os.path.splitext(name)[1]
            if extension == ".log":
                subfolder = "logs"
            elif extension == ".csv" or extension == ".json":
                subfolder = "data"
            elif extension == ".pkl":
                subfolder = "pickles"
            else:
                subfolder = "other"

            os.makedirs(os.path.join(folder, subfolder), exist_ok=True)
            shutil.move(path, os.path.join(folder, subfolder, name))
            moved[subfolder].append(name)

    for subfolder in moved:
        moved[subfolder].sort()
    return moved

def create_backup(source_dir, backup_root, label):
    """Copy source_dir to backup_root/backup_<label>; return the new path."""
    os.makedirs(backup_root, exist_ok=True)
    backup_dir = os.path.join(backup_root, f"backup_{label}")
    shutil.copytree(source_dir, backup_dir)
    return backup_dir

def verify_backup(source_dir, backup_dir):
    """Return True if every file under source_dir is in backup_dir with the same size."""
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            relative_path = os.path.relpath(source_path, source_dir)
            backup_path = os.path.join(backup_dir, relative_path)
            if not os.path.exists(backup_path):
                return False
            if os.path.getsize(source_path) != os.path.getsize(backup_path):
                return False
    return True

def cleanup_old_backups(backup_root, keep):
    """Delete all but the newest `keep` backups; return sorted names deleted."""
    backups = sorted(os.listdir(backup_root))
    deleted = []
    if len(backups) > keep:
        deleted = backups[:len(backups) - keep]
    for name in deleted:
        shutil.rmtree(os.path.join(backup_root, name))
    return deleted

#Test Cases

for old in ["workspace", "backups"]:
    if os.path.exists(old):
        shutil.rmtree(old)

os.mkdir("workspace")
for name in ["a.log", "b.log", "incidents.csv", "summary.json", "incidents.pkl", "notes.txt"]:
    with open(os.path.join("workspace", name), "w") as f:
        f.write(f"Test file: {name}\n")

print(organize("workspace"))

print(sorted(os.listdir("workspace")))

for label in ["2026-10-01", "2026-10-02", "2026-10-03"]:
    path = create_backup("workspace", "backups", label)
    print(os.path.basename(path), verify_backup("workspace", path))

os.remove(os.path.join("backups", "backup_2026-10-03", "logs", "a.log"))
print(verify_backup("workspace", os.path.join("backups", "backup_2026-10-03")))

print(cleanup_old_backups("backups", 2))

print(sorted(os.listdir("backups")))
