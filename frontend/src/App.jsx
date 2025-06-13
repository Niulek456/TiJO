import React, { useState } from "react";
import axios from "axios";

const assistants = [
    { key: "review", label: "Przejrzyj kod" },
    { key: "generate", label: "Stwórz testy" },
    { key: "issues", label: "Znajdź problemy" },
    { key: "architecture", label: "Sprawdź architekturę" },
    { key: "security", label: "Audyt bezpieczeństwa" },
];

const assistantDescriptions = {
    review: "Szybka analiza i przegląd kodu źródłowego.",
    generate: "Generuje testy jednostkowe dla Twojego kodu.",
    issues: "Wskazuje problemy i antywzorce w kodzie.",
    architecture: "Sprawdza zgodność z zasadami SOLID i architekturę.",
    security: "Identyfikuje potencjalne luki bezpieczeństwa.",
};

const prompts = {
    review: `Jestem ekspertem od analizy kodu. Przejrzyj poniższy kod i wskaż błędy, dobre praktyki oraz ewentualne sugestie.\nKod:\n`,
    generate: `Jestem ekspertem QA. Wygeneruj testy jednostkowe do poniższego kodu.\nKod:\n`,
    issues: `Jestem ekspertem od jakości. Przeanalizuj poniższy kod pod kątem potencjalnych problemów, antywzorców i nieoptymalnych konstrukcji.\nKod:\n`,
    architecture: `Jestem ekspertem architektury. Oceń kod pod kątem zasad SOLID i dobrej struktury aplikacji.\nKod:\n`,
    security: `Jestem specjalistą ds. bezpieczeństwa. Zidentyfikuj potencjalne podatności w tym kodzie.\nKod:\n`,
};

export default function App() {
    const [selected, setSelected] = useState("review");
    const [code, setCode] = useState("");
    const [result, setResult] = useState("");

    const handleClick = async () => {
        if (!code.trim()) {
            setResult("⚠️ Wklej kod do analizy.");
            return;
        }

        setResult("⏳ Analiza w toku...");

        try {
            const payload = { codeSnippet: `${prompts[selected]}${code}` };
            const res = await axios.post("http://localhost:4000/analyze", payload);
            setResult(res.data.analysis);
        } catch (err) {
            console.error(err);
            setResult("❌ Błąd komunikacji z backendem.");
        }
    };

    return (
        <div
            style={{
                display: "flex",
                gap: "2rem",
                maxWidth: 1100,
                width: "90%",
                margin: "2rem auto",
                padding: "2rem",
                backgroundColor: "#1e1e1e",
                borderRadius: "16px",
                boxShadow: "0 10px 30px rgba(0, 0, 0, 0.6)",
                color: "#e0e0e0",
            }}
        >
            {/* BOCZNY PANEL */}
            <aside style={{ minWidth: 200 }}>
                <h3 style={{ fontSize: "1.2em", marginBottom: "1rem" }}>Asystenci</h3>
                <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
                    {assistants.map((item) => (
                        <button
                            key={item.key}
                            onClick={() => setSelected(item.key)}
                            style={{
                                backgroundColor: selected === item.key ? "#2a3f7a" : "#2b2b2b",
                                color: selected === item.key ? "#fff" : "#e0e0e0",
                                border: "1px solid #555",
                                borderRadius: "10px",
                                padding: "0.6em 1.2em",
                                fontSize: "1em",
                                fontWeight: 500,
                                cursor: "pointer",
                                transition: "background-color 0.3s, transform 0.2s",
                            }}
                        >
                            {item.label}
                        </button>
                    ))}
                </div>
            </aside>

            {/* GŁÓWNA CZĘŚĆ */}
            <main style={{ flex: 1 }}>
                <h1 style={{ fontSize: "2.2em", marginBottom: "1rem" }}>
                    CodeIntel – Twój Asystent Programisty
                </h1>

                <p style={{ color: "#aaa", fontStyle: "italic", marginBottom: "1rem" }}>
                    {assistantDescriptions[selected]}
                </p>

                <textarea
                    value={code}
                    onChange={(e) => setCode(e.target.value)}
                    placeholder="Wklej tutaj kod do analizy..."
                    style={{
                        width: "100%",
                        minHeight: 140,
                        borderRadius: "10px",
                        border: "1px solid #444",
                        backgroundColor: "#121212",
                        color: "#f1f1f1",
                        fontFamily: "monospace",
                        fontSize: 15,
                        padding: 10,
                        marginBottom: 16,
                    }}
                />

                <div style={{ textAlign: "right", marginBottom: "1rem" }}>
                    <button
                        onClick={handleClick}
                        style={{
                            backgroundColor: "#2a3f7a",
                            color: "#fff",
                            border: "1px solid #555",
                            borderRadius: "10px",
                            padding: "0.6em 1.6em",
                            fontSize: "1em",
                            fontWeight: 600,
                            cursor: "pointer",
                            transition: "background-color 0.3s, transform 0.2s",
                        }}
                    >
                        Analizuj kod
                    </button>
                </div>

                <div
                    style={{
                        backgroundColor: "#222",
                        border: "1px solid #444",
                        borderRadius: "10px",
                        padding: "1rem",
                        minHeight: 100,
                        whiteSpace: "pre-wrap",
                        fontSize: 15,
                    }}
                >
                    {result}
                </div>
            </main>
        </div>
    );
}
