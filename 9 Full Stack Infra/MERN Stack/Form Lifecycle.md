---
tags: [mern, integration, intermediate]
---

# Form Lifecycle

> A form's data crosses three trust boundaries: client UI → server handler → database. Each boundary needs validation; each layer's failure has a different UX.

## The three layers
```
[UI input]  →  [client validation]  →  [server validation]  →  [DB constraint]
   feedback ←      instant             ←  field/global error  ← surfaced as 4xx
```

## Layer 1: client validation (instant feedback)
```tsx
// React Hook Form + Zod
const schema = z.object({ email: z.string().email(), password: z.string().min(8) });
type FormValues = z.infer<typeof schema>;

const { register, handleSubmit, formState } = useForm<FormValues>({
  resolver: zodResolver(schema),
});

<input {...register('email')} />
{formState.errors.email && <p>{formState.errors.email.message}</p>}
```

## Layer 2: server validation (authoritative)
```ts
app.post('/signup', async (req, res, next) => {
  const parsed = schema.safeParse(req.body);
  if (!parsed.success) return res.status(400).json({ error: parsed.error.flatten() });
  try {
    const user = await createUser(parsed.data);
    res.status(201).json(user);
  } catch (e) { next(e); }
});
```

## Layer 3: DB constraint (last line)
```sql
-- unique email constraint
ALTER TABLE users ADD CONSTRAINT users_email_unique UNIQUE (email);
```
or in Mongoose: `email: { type: String, required: true, unique: true, lowercase: true }`.

## Surfacing errors back to UI
- 400 with `{ field: { email: '...' } }` → set field-level errors
- 409 (conflict — duplicate email) → top-level error
- 422 (semantic invalid) → form-level error
- 500 → toast "Something went wrong, try again"

## Real World Usage
- Signup / login
- Checkout (address, payment)
- Multi-step wizards
- File uploads with metadata
- Anywhere data leaves the browser

## Common Mistakes
- Skipping server validation because "the client already did it" — attackers bypass UI
- Using two different schemas client and server — drift bugs
- Showing raw DB errors (`E11000 duplicate key error collection users.$email_1 dup key`) to the user
- Submitting again before previous request resolves (no `isSubmitting` guard)
- No optimistic UX → forms feel laggy on slow networks
- Not preventing default form submit → page reloads

## Prerequisites
- [[Forms in React]] · [[Validation]] · [[Type Sharing]]

## What To Learn Next
- [[Full-Stack Auth Flow]] · [[Cross-Domain Cookies]]

## Best Learning Resources

### Official Documentation
- [React Hook Form](https://react-hook-form.com/)
- [Zod docs](https://zod.dev/)
- [TanStack Form](https://tanstack.com/form)

### Best YouTube Resource
- [Jack Herrington — RHF + Zod patterns](https://www.youtube.com/@jherr)
- [Web Dev Simplified — Forms](https://www.youtube.com/c/WebDevSimplified)

### Best Free Course
- [React Hook Form tutorial in docs](https://react-hook-form.com/get-started)
- [Total TypeScript — Zod validation chapter](https://www.totaltypescript.com/)

### Best Advanced Resource
- [Building accessible forms — Sara Soueidan](https://www.sarasoueidan.com/blog/) — a11y is part of UX
- [Conform (form lib by the Remix team)](https://conform.guide/) — modern alternative

### Best Practice Project
Build a multi-step signup wizard: step 1 email/password, step 2 profile, step 3 review. Use shared Zod schemas. Show field errors instantly, server errors surfaced inline, network errors as toast. Add disabled states + spinners.

### Recommended Order to Learn
1. Native `<form>` + `FormData`
2. React Hook Form + Zod
3. Server-side validation parity
4. Error display patterns
5. Optimistic + pending states
6. Multi-step + conditional fields

## Interview Questions
**Q. Why validate on both client and server?**
A. Client = UX, server = trust boundary. Client validation can be bypassed; server validation is authoritative.

**Q. How do you keep schemas in sync?**
A. Share Zod (or similar) schemas via a workspace package. Single source.

**Q. How do you handle a duplicate-email DB error gracefully?**
A. Catch the unique constraint violation in the handler, return 409 with `{ field: { email: 'already in use' } }`.

## Related
- [[Forms in React]] · [[Validation]] · [[Type Sharing]] · [[API Contract]]
