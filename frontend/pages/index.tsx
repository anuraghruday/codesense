import { useState } from 'react';

export default function Home() {
    const [code, setCode] = useState('');
    const [review, setReview] = useState('');

    const analyzeCode = async () => {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code_snippet: code })
        });
        const data = await response.json();
        setReview(data.review);
    };

    return (
        <div>
            <h1>AI CodeSense</h1>
            <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="Enter your code here..."
            />
            <button onClick={analyzeCode}>Analyze</button>
            <pre>{review}</pre>
        </div>
    );
}