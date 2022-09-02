package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"

	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/ethclient"
)

// "fmt"
// "log"
// "math/big"
// "github.com/ethereum/go-ethereum/core/types"
// "github.com/ethereum/go-ethereum/ethclient"
// func jsonFormat(t string, content interface{}, end bool) {
// 	fmt.Print("\"")
// 	fmt.Print(t)
// 	fmt.Print("\"")
// 	fmt.Print(":\"")
// 	fmt.Print(content)
// 	fmt.Print("\"")
// 	if !end {
// 		fmt.Print(",")
// 	}
// 	fmt.Print("\n")
// }
// func main() {
// client, err := ethclient.Dial("https://cloudflare-eth.com")
// if err != nil {
// 	log.Fatal(err)
// }
// // txHash := common.HexToHash("0x5d49fcaa394c97ec8a9c3e7bd9e8388d420fb050a52083ca52ff24b3b65bc9c2")
// // tx, _, err := client.TransactionByHash(context.Background(), txHash)
// // if err != nil {
// //   log.Fatal(err)
// // }
// // fmt.Printf("%d,%d\n", tx.Gas(), tx.GasPrice().Uint64())
// blockNumber := big.NewInt(15401067)
// block, err := client.BlockByNumber(context.Background(), blockNumber)
// if err != nil {
// 	log.Fatal(err)
// }
// // fmt.Println(block.Number().Uint64())     // 5671744
// // fmt.Println(block.Time())                // 1527211625
// // fmt.Println(block.Difficulty().Uint64()) // 3217000136609065
// // fmt.Println(block.Hash().Hex())          // 0x9e8751ebb5069389b855bba72d94902cc385042661498a415979b7b6ee9ba4b9
// // fmt.Println(len(block.Transactions()))   // 144
// // // fmt.Println("{\"data\": [")
// for _, tx := range block.Transactions() {
// // 	// fmt.Println("{")
// // 	// jsonFormat("transaction_hash", tx.Hash().Hex(), false)
// // 	// jsonFormat("value", tx.Value().String(), false)
// // 	// jsonFormat("gas", tx.Gas(), false)
// // 	// jsonFormat("gasPrice", tx.GasPrice().Uint64(), false)
// // 	// jsonFormat("nonce", tx.Nonce(), false)
// // 	// jsonFormat("data", tx.Data(), false)
// // 	// jsonFormat("hex", tx.To().Hex(), true)
// // 	fmt.Printf("%s, %d,%d\n", tx.Hash().Hex(), tx.Gas(), tx.GasPrice().Uint64())
// 	fmt.Printf("%d,%d,0\n", tx.Gas(), tx.GasPrice().Uint64())
// // 	// fmt.Println(tx.Hash().Hex())        // 0x5d49fcaa394c97ec8a9c3e7bd9e8388d420fb050a52083ca52ff24b3b65bc9c2
// // 	// fmt.Println(tx.Value().String())    // 10000000000000000
// // 	// fmt.Println(tx.Gas())               // 105000
// // 	// fmt.Println(tx.GasPrice().Uint64()) // 102000000000
// // 	// fmt.Println(tx.Nonce())             // 110644
// // 	// fmt.Println(tx.Data())              // []
// // 	// fmt.Println(tx.To().Hex())          // 0x55fE59D8Ad77035154dDd0AD0388D09Dd4047A8e
// // 	// chainID, err := client.NetworkID(context.Background())
// // 	// if err != nil {
// // 	// 	fmt.Println("}")
// // 	// 	log.Fatal(err)
// // 	// }
// // 	// if msg, err := tx.AsMessage(types.NewEIP155Signer(chainID), nil); err == nil {
// // 	// 	fmt.Print(",")
// // 	// 	jsonFormat("msg", msg.From().Hex(), true)
// // 	// 	// fmt.Println(msg.From().Hex()) // 0x0fD081e3Bb178dc45c0cb23202069ddA57064258
// // 	// }
// // 	// fmt.Println("},")
// }
// // // fmt.Println("]")
// }


type Transaction struct {
    TransactionHash  string `json:"transaction_hash"`
    TxIndex          int    `json:"tx_index"`
    BundleIndex      int    `json:"bundle_index"`
    BlockNumber      int    `json:"block_number"`
    EaoAddress       string `json:"eao_address"`
    ToAddress        string `json:"to_address"`
    GasUsed          int    `json:"gas_used"`
    GasPrice         string `json:"gas_price"`
    CoinbaseTransfer string `json:"coinbase_transfer"`
    TotalMinerReward string `json:"total_miner_reward"`
}

type Transactions struct {
    Transactions []Transaction `json:"transactions"`
}

func main() {
    jsonFile, err := os.Open("../../../../moredata.json")
    if err != nil {
        fmt.Println(err)
    }
    defer jsonFile.Close()

	client, err := ethclient.Dial("https://cloudflare-eth.com")
	if err != nil {
		log.Fatal(err)
	}

    byteValue, _ := ioutil.ReadAll(jsonFile)

    var transactions Transactions

    json.Unmarshal(byteValue, &transactions)

    for _, transaction := range transactions.Transactions {
		txHash := common.HexToHash(transaction.TransactionHash)
		tx, _, err := client.TransactionByHash(context.Background(), txHash)
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("%d,%d,%d,1\n", tx.GasPrice().Int64(), tx.Gas(), tx.Nonce())
    }
}
