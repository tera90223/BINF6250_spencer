# BINF6250
# Project01
# Introduction
VCF file parsing

# Pseudocode
input: vcf file
output: dictionary containing frequency of disease types

Open vcf file and read line by line 
for each line determine rarity of variant using allele frequencies from the reported AF_EXAC value in the file
If variant is not rare, do not record variant
If the variant is considered rare, record associated disease
If no disease is associated, do not record
start a running count that tracks the frequency of diseases associated with rare variants
Each time a disease associated with a rare variant is recorded, increase associated disease's tally by 1
When entire file is read, report frequency each disease associate with a rare variant appeared in the file
# Successes
Description of the team's learning points

# Struggles
Main struggles were becoming acquainted with the use of Github for the class, and identifying edge cases to test for with unit tests.

# Personal Reflections
## Group Leader
Key takeaway from this project was learning and understanding the group project structure from the perspective of the group leader. As a GitHub novice, I feel more comfortable navigating the use of GitHub in the future. I had less comfortability with aspects of the project, but leveraging open lines of communication and meetings with the group members, I feel my confidence and understanding of the task at hand was strengthened. 

## Other member
Meghana: This project helped get familiar with using GitHub since I hadn't really used it before this, especially in a collaborative way. I didn't really understand how to coordinate with my group on GitHub at first, but actually doing it made it easier for me to understand. This was the first time I worked in a team for a code-based project and I think it has helped improve my understanding of the process.

# Generative AI Appendix
As per the syllabus

