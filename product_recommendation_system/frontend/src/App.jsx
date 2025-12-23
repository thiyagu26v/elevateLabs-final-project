import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
    const [products, setProducts] = useState([]);
    const [recommendations, setRecommendations] = useState([]);
    const [selectedProduct, setSelectedProduct] = useState('');
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        fetchProducts();
    }, []);

    const fetchProducts = async () => {
        try {
            const res = await axios.get('http://localhost:8001/api/products/');
            setProducts(res.data);
        } catch (err) {
            console.error('Error fetching products', err);
        }
    };

    const fetchRecommendations = async (name) => {
        setLoading(true);
        setSelectedProduct(name);
        try {
            const res = await axios.post('http://localhost:8001/api/recommend/', {
                product_name: name
            });
            setRecommendations(res.data);
        } catch (err) {
            console.error('Error fetching recommendations', err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', maxWidth: '1200px', margin: '0 auto' }}>
            <h1 style={{ textAlign: 'center', color: '#333' }}>Product Recommendation System</h1>

            <div style={{ display: 'flex', gap: '30px', marginTop: '30px' }}>
                {/* Product List Section */}
                <div style={{ flex: 2 }}>
                    <h2>Available Products</h2>
                    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '15px' }}>
                        {products.map((product) => (
                            <div
                                key={product.id}
                                style={{
                                    border: '1px solid #ddd',
                                    padding: '15px',
                                    borderRadius: '8px',
                                    backgroundColor: selectedProduct === product.name ? '#f0f7ff' : '#fff',
                                    cursor: 'pointer',
                                    transition: '0.3s'
                                }}
                                onClick={() => fetchRecommendations(product.name)}
                            >
                                <h3 style={{ margin: '0 0 10px 0', fontSize: '1.1rem' }}>{product.name}</h3>
                                <span style={{
                                    fontSize: '0.8rem',
                                    backgroundColor: '#eee',
                                    padding: '2px 8px',
                                    borderRadius: '10px',
                                    display: 'inline-block',
                                    marginBottom: '10px'
                                }}>
                                    {product.category}
                                </span>
                                <p style={{ margin: 0, fontSize: '0.9rem', color: '#666' }}>{product.description}</p>
                            </div>
                        ))}
                    </div>
                </div>

                {/* Recommendations Section */}
                <div style={{ flex: 1, backgroundColor: '#f9f9f9', padding: '20px', borderRadius: '8px', minHeight: '400px' }}>
                    <h2>Recommendations</h2>
                    {selectedProduct ? (
                        <div>
                            <p>People who liked <strong>{selectedProduct}</strong> also liked:</p>
                            {loading ? (
                                <p>Loading suggestions...</p>
                            ) : (
                                <div style={{ marginTop: '15px' }}>
                                    {recommendations.length > 0 ? (
                                        recommendations.map((rec) => (
                                            <div key={rec.id} style={{ backgroundColor: '#fff', padding: '15px', marginBottom: '10px', borderRadius: '5px', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
                                                <h4 style={{ margin: '0 0 5px 0' }}>{rec.name}</h4>
                                                <p style={{ margin: 0, fontSize: '0.85rem', color: '#666' }}>{rec.description}</p>
                                            </div>
                                        ))
                                    ) : (
                                        <p>No similar products found.</p>
                                    )}
                                </div>
                            )}
                        </div>
                    ) : (
                        <p style={{ color: '#999', marginTop: '50px', textAlign: 'center' }}>Click on a product to see recommendations</p>
                    )}
                </div>
            </div>
        </div>
    );
};

export default App;
