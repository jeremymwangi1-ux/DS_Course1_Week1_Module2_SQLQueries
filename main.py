import pandas as pd
import sqlite3

# Connections
conn1 = sqlite3.connect('planets.db')
conn2 = sqlite3.connect('dogs.db')
conn3 = sqlite3.connect('babe_ruth.db')

# Step 1
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0
""", conn1)

# Step 2
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7
""", conn1)

# Step 3
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00
""", conn1)

# Step 4
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1 AND mass < 1.00
""", conn1)

# Step 5
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE '%blue%'
""", conn1)

# Step 6
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC
""", conn2)

# Step 7
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1 AND age BETWEEN 2 AND 7
ORDER BY name ASC
""", conn2)

# Step 8 (IMPORTANT: avoid pandas sorting)
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC, breed ASC
LIMIT 4
""", conn2)

# Step 9
df_ruth_years = pd.read_sql("""
SELECT COUNT(*) AS total_years
FROM babe_ruth_stats
""", conn3)

# Step 10
df_hr_total = pd.read_sql("""
SELECT SUM(HR) AS total_home_runs
FROM babe_ruth_stats
""", conn3)

# Step 11
df_teams_years = pd.read_sql("""
SELECT team, COUNT(*) AS number_years
FROM babe_ruth_stats
GROUP BY team
""", conn3)

# Step 12
df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200
""", conn3)

# Close connections
conn1.close()
conn2.close()
conn3.close()