NBHA-(bits) (Number-Based Hash Algorithm)

NBHA is a custom-designed hashing algorithm built for Castle games and other platforms needing high-speed, sensitive, and flexible hashing without relying on traditional cryptographic libraries. This algorithm introduces chaotic mathematical transformations, making it both deterministic and unpredictable — a rare combo.

Key Features:
	•	Deterministic salt from the seed — no storage or random generation required
	•	Sensitive hashing — a +1 change in input can shift the result by trillions
	•	Stable digit output — won’t overflow or NaN, even at massive sizes
	•	Flexible structure — good for passwords, game logic, locking/unlocking systems
	•	Supports conversion to readable formats (e.g. symbols, alphanumeric strings)

Formula Overview:

Salt Formula:
Salt = (((log_base(seed) of bits) × (bytes × bits)) × seed) mod (2^bytes)

Hash Formula:
Hash = round(sin((log_base(seed × 65536) of bits + (seed × (seed / bits))) mod (2^bytes) + (Salt² / bits)) × Salt)

All operations are performed using float-safe calculations. Final hash is rounded.

Example Use:

Seed: 1000027328
Bits: 2826
Bytes: 1000

Salt output: (calculated based on formula)
Hash output: (massive, consistent, highly sensitive)

Security Notes:
	•	NBHA is not a cryptographic hash and should not be used for banking, encryption, or digital signing.
	•	It is excellent for password protection inside game systems where users can inspect source code (like Castle).
	•	The unpredictable jumpy output and deterministic salt help prevent reverse engineering, even if the logic is visible.

Readable Output (Optional):

To convert the hash to readable format:
	•	Split the number into 2-digit or 1-digit chunks.
	•	Map those to characters or symbols (A=1, B=2, …, special chars as needed).
	•	You now have a secure alphanumeric or symbol-based password.

Why Use NBHA?
	•	i Developed it for games like castle where you can insecpt code 
	•	You want fast generation even for huge inputs.
	•	You want it to look like chaotic magic while being 100% deterministic.

License:
Open for public use and improvement. Free for all devs.
Created by Pisti 
Discord: @dandyyyyyyys
