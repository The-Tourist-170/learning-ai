### Core Concept

Chroma allows you to filter your search results based on the actual text content of your documents, rather than just relying on vector similarity or metadata. You do this using the `where_document` argument (or `whereDocument` in TypeScript, `r#where` in Rust) inside your `.get()` or `.query()` calls.

### Available Operators

You can filter your document text using four main operators:

* **`$contains`**: Checks if the document includes a specific string (Note: this is case-sensitive).
* **`$not_contains`**: Excludes documents that contain a specific string.
* **`$regex`**: Matches the document text against a regular expression pattern (e.g., finding all documents with an email address).
* **`$not_regex`**: Excludes documents that match a specific regular expression.

### Combining Filters

* **Logical Operators**: You can chain multiple text filters together using `$and` (all conditions must be met) or `$or` (at least one condition must be met).
* **Metadata Filtering**: You can use `where_document` side-by-side with the standard `where` argument. This lets you run highly specific queries that filter by both the raw text content and the attached metadata at the same time.

---