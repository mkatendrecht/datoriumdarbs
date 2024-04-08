import random
import timeit

def generate_random_dates(num_dates):
    dates = []
    for _ in range(num_dates):
        # Ģenerē gadskārtu datumus
        mēnesis = random.randint(1, 12)
        if mēnesis in [1, 3, 5, 7, 8, 10, 12]:
            diena = random.randint(1, 31)
        elif mēnesis in [4, 6, 9, 11]:
            diena = random.randint(1, 30)
        else:  # Februāris
            diena = random.randint(1, 28)
        gads = random.randint(2000, 2023)  # Ņemot vērā gadus no 2000 līdz 2023
        dates.append((diena, mēnesis, gads))
    return dates

def lineārā_meklēšana_martā(dates):
    martadatumi = []
    for datums in dates:
        if datums[1] == 3:  # Ja mēnesis ir marts
            martadatumi.append(datums)
    return len(martadatumi)

def binārā_meklēšana_martā(dates):
    martadatumi = []
    sakārtoti_datumi = sorted(dates, key=lambda x: x[1])  # Sakārto pēc mēneša binārajai meklēšanai
    kreisais, labais = 0, len(sakārtoti_datumi) - 1
    while kreisais <= labais:
        vidus = (kreisais + labais) // 2
        if sakārtoti_datumi[vidus][1] == 3:  # Ja mēnesis ir marts
            martadatumi.append(sakārtoti_datumi[vidus])
            # Pārbauda citas martā datuma vietas kreisajā pusē
            i = vidus - 1
            while i >= kreisais and sakārtoti_datumi[i][1] == 3:
                martadatumi.append(sakārtoti_datumi[i])
                i -= 1
            # Pārbauda citas martā datuma vietas labajā pusē
            i = vidus + 1
            while i <= labais and sakārtoti_datumi[i][1] == 3:
                martadatumi.append(sakārtoti_datumi[i])
                i += 1
            break
        elif sakārtoti_datumi[vidus][1] < 3:
            kreisais = vidus + 1
        else:
            labais = vidus - 1
    return len(martadatumi)

# Ģenerē 200 gadskārtu datumus
random_dates = generate_random_dates(200)

# Izmēra laiku lineārai meklēšanai
linear_time = timeit.timeit(lambda: lineārā_meklēšana_martā(random_dates), number=1)

# Izmēra laiku binārai meklēšanai
binary_time = timeit.timeit(lambda: binārā_meklēšana_martā(random_dates), number=1)

# Izvada rezultātus
print("Izmantojot Lineāro Meklēšanu:")
print("Laiks lineārai meklēšanai:", linear_time, "sekundes")

print("\nIzmantojot Bināro Meklēšanu:")
print("Laiks binārai meklēšanai:", binary_time, "sekundes")

# Nosaka, kura algoritma veica labāk
if linear_time < binary_time:
    print("\nLineārā meklēšana veica labāk.")
elif binary_time < linear_time:
    print("\nBinārā meklēšana veica labāk.")
else:
    print("\nAbi algoritmi veica vienlīdz labi.") 
