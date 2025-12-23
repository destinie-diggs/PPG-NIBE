# PPG-NIBE Dataset

The **PPG-NIBE dataset** provides carefully selected, cleaned, and organized data from the **VitalDB Open Dataset**. It has been curated to provide high-quality, relevant, accurate, and reusable data to accelerate research and development for Non-Invasive Blood Glucose Estimation (NIBE).

## Description

This work introduces a curated and organized sub-dataset from the VitalDB vital signs database specifically for photoplethysmography (PPG) based NIBE research.

**VitalDB Overview:**
- High-resolution, multi-parameter data from **6,388 cases**
- **486,451** waveform and numeric data tracks across **196** intraoperative monitoring parameters
- **73** perioperative clinical parameters
- **34** time-series laboratory result parameters

**Why VitalDB?**
- Proven to be **trustworthy and reliable**  
- Frequently used in AI/ML research across multiple domains  
- Prior research has successfully used VitalDB for **non-invasive blood glucose estimation model training and development**

**Purpose of the PPG-NIBE Dataset:**
- Filter and select **features relevant for NIBE** from the large VitalDB dataset  
- Reduce dataset size and organize relevant features for **PPG-based NIBE**  
- Lower the **barrier to entry** for researchers entering the field  

By curating a smaller, relevant dataset, researchers can quickly start model development without needing to preprocess or filter the full VitalDB dataset themselves.

## Getting Started
For detailed documentation and description of selected data and pipeline see [Wiki](https://github.com/destinie-diggs/PPG-NIBE/wiki).

### Dependencies

* Python 3
	* pandas
	* vitaldb
	* matplotlib
	* tqdm
	* scipy
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Destinie Diggs
ex. [@LinkedIn](https://www.linkedin.com/in/destinie-diggs-92630b2bb?utm_source=share_via&utm_content=profile&utm_medium=member_ios) 

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments
* [Vitaldb](https://vitaldb.net/dataset/?query=overview)

