# Decision Report

- generated_at: 2026-05-03T14:06:57.876693+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3077**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3077, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 19/20 | 95.0% | +1.15% | **+1.10%** |
| LIMIT_BB3S | 10/16 | 62.5% | +1.62% | **+1.01%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.88% | **+0.75%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.81% | **+0.65%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.91% | **+2.18%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +4.79% | **+2.16%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.45% | **+2.00%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.27% | **+1.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T14:06:56.397173+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78725.7
- Funnel: target 755 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +43.02% | $3,910,161.78 |
| TAC/USDT:USDT | +40.89% | $3,101,556.05 |
| NAORIS/USDT:USDT | +27.80% | $4,592,434.06 |
| FHE/USDT:USDT | +22.89% | $4,367,084.13 |
| BABY/USDT:USDT | +20.87% | $21,013,298.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +3.17% | +3.05% |
| BABY/USDT:USDT | below_1h_threshold | +2.56% | +2.44% |
| BSB/USDT:USDT | below_1h_threshold | +1.38% | +1.27% |
| REZ/USDT:USDT | below_1h_threshold | +1.37% | +1.25% |
| B/USDT:USDT | below_1h_threshold | +0.85% | +0.73% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
