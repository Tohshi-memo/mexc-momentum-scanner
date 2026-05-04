# Decision Report

- generated_at: 2026-05-04T17:03:30.829284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3239**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3239, expectancy=-0.18%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +2.66% | **+1.73%** |
| LIMIT_6PCT | 6/20 | 30.0% | +4.94% | **+1.48%** |
| LIMIT_4PCT | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.78% | **+0.98%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +8.00% | **+4.00%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.66% | **+2.56%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.91% | **+1.62%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.07% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$102.36** / 初期 $100.00 (+2.36%)
- 確定トレード: 14件 (TP 5 / SL 7 / EXP 2)
- 最新: B/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T17:03:28.860570+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=80172.2
- Funnel: target 761 → liquid 199 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TST/USDT:USDT | +17.26% | $20,481,578.11 |
| BSB/USDT:USDT | +16.56% | $34,244,247.83 |
| TAG/USDT:USDT | +13.02% | $17,800,506.17 |
| FHE/USDT:USDT | +9.80% | $2,679,096.52 |
| B3/USDT:USDT | +7.22% | $1,016,282.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +1.92% | +1.69% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.43% | +1.19% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.34% | +1.10% |
| FHE/USDT:USDT | below_1h_threshold | +1.10% | +0.87% |
| 4/USDT:USDT | below_1h_threshold | +1.05% | +0.81% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
