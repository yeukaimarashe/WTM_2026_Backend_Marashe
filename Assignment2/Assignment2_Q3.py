# Backend Data Processing & User Audit Tool

# Raw user records: (User ID, Name, Role, Is_Active, Login_Attempts)

users = [(101, "Alice", "admin", True, 1),
         (102, "Bob", "member", True, 4),
         (103, "Charlie", "editor", False, 0),
         (104, "Diana", "admin", False, 6),
         (105, "Evan", "member", True, 2),
         (106, "Fiona", "guest", True, 0), ]


active_users_count = 0
inactive_users_count = 0
flagged_users_count = 0

for user_id, name, role, is_active, login_attempts in users:

    if is_active and role == "admin":
        print(f"[GRANT] Full system access granted to {name} (ID: {user_id})")
        active_users_count += 1

    elif is_active and (role == "member" or role == "editor"):
        print(f"[GRANT] Standard access granted to {name} (ID: {user_id})")
        active_users_count += 1

    elif not is_active:
        print(f"[DENIED] Account {name} is inactive.")
        inactive_users_count += 1

        if login_attempts >= 5:
            print(
                f"[ALERT] Account {name} is LOCKED due to excessive failed logins ({login_attempts} attempts).")
            flagged_users_count += 1


print("\n AUDIT SUMMARY REPORT")
print("=" * 40)

print(f"Total Active Users: {active_users_count}")
print(f"Total Inactive Users: {inactive_users_count}")
print(f"Total Security Alerts: {flagged_users_count}")
