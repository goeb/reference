// With go1.26.8 (and probably since go1.24):
// - If random is nil, ecdsa.Sign will produce a deterministic
//   signature (not in this program)
// - If random is not nil (as in this program):
//     - if GODEBUG=cryptocustomrand=1 is set, ecdsa.Sign uses the
//       fixed random source
//     - otherwise, the signature is randomized.
// Ref: https://pkg.go.dev/crypto/ecdsa#PrivateKey.Sign
//
// With go1.23.12:
// - If random is not nil, ecdsa.Sign uses the fixed random source
// - If random is nil, ecdsa.Sign panics (not this program)
 
package main

import (
	"bytes"
	"crypto"
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/sha256"
	"fmt"
)

// Instead of rand.Reader, we want deterministic (and known) random bytes
var fixedRandomReader *bytes.Reader

func init() {
	buf := []byte("yyyyyyyyyyyyyyyy") // size 16
	buf = append(buf, buf...)         // size 32
	buf = append(buf, buf...)         // size 64
	buf = append(buf, buf...)         // size 128
	buf = append(buf, buf...)         // size 256
	fixedRandomReader = bytes.NewReader(buf)
}

func main() {
	// Generate an ECDSA private key.
	// *ecdsa.PrivateKey implements the crypto.Signer interface.
	privateKey, err := ecdsa.GenerateKey(elliptic.P256(), fixedRandomReader)
	if err != nil {
		fmt.Println("failed to generate key:", err)
	}
	fmt.Printf("privateKey: %x\n", privateKey)

	// Cast or assign to the crypto.Signer interface.
	var signer crypto.Signer = privateKey

	message := []byte("Hello, Go crypto.Signer!")
	testSign(signer, message)
	testSign(signer, message)
	testSign(signer, message)
	testSign(signer, message)
}

func testSign(signer crypto.Signer, message []byte) {
	fmt.Println("testSign...")

	hashed := sha256.Sum256(message)
	
	// Sign using crypto.Signer.
	signature, err := signer.Sign(fixedRandomReader, hashed[:], crypto.SHA256)
	if err != nil {
		fmt.Println("failed to sign message:", err)
		return
	}

	fmt.Println("Message:", message)
	fmt.Printf("Signature (%d bytes): %x\n", len(signature), signature)

	// Extract the public key
	// crypto.Signer.Public() returns a crypto.PublicKey interface.
	pubKey, ok := signer.Public().(*ecdsa.PublicKey)
	if !ok {
		fmt.Println("public key is not an ECDSA public key")
		return
	}

	// Verify the signature against the hash digest.
	// ecdsa.VerifyASN1 expects ASN.1 DER encoded signatures (which crypto.Signer produces).
	valid := ecdsa.VerifyASN1(pubKey, hashed[:], signature)
	if valid {
		fmt.Println("Signature verification SUCCESSFUL!")
	} else {
		fmt.Println("Signature verification FAILED!")
	}
}
