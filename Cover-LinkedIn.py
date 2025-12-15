import matplotlib.pyplot as plt
import numpy as np


def create_banner():
    # 1. Nustatome matmenis
    dpi = 100
    width = 1584 / dpi
    height = 396 / dpi

    fig, ax = plt.subplots(figsize=(width, height), dpi=dpi)

    # 2. Fonas
    fig.patch.set_facecolor('#0B1120')
    ax.set_facecolor('#0B1120')

    # 3. Vizualūs elementai (Dešinėje)
    np.random.seed(42)
    x = np.random.normal(13, 1.5, 300)
    y = np.random.normal(5, 2, 300)
    colors = np.random.rand(300)
    sizes = np.random.rand(300) * 300

    ax.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')

    # --- PAKEITIMAS ČIA ---
    # 4. Tekstas (Pastumtas stipriai į kairę: x=2.0)

    text_x = 2.0  # Buvo 4.0, dabar 2.0 - tai standartinė kairinė paraštė

    # Pagrindinė antraštė
    plt.text(text_x, 6.0, "JUNIOR DATA ANALYST",
             fontsize=28, color='white', weight='bold', fontname='Arial')

    # Įgūdžiai (Skills)
    plt.text(text_x, 4.5, "Python  |  SQL  |  Power BI  |  Tableau  |  Excel",
             fontsize=18, color='#00d4ff', weight='regular', fontname='Arial')

    # Šūkis (Tagline)
    plt.text(text_x, 3.0, "Transforming raw data into actionable insights.",
             fontsize=14, color='#aaaaaa', style='italic', fontname='Arial')

    # 5. Išvalome ašis
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 6. Išsaugome
    plt.savefig('linkedin_banner_far_left.png', bbox_inches='tight', pad_inches=0, facecolor='#0B1120')
    plt.show()
    print("Baneris išsaugotas kaip 'linkedin_banner_far_left.png'")


create_banner()