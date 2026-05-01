# Decision Report

- generated_at: 2026-05-01T22:22:29.785560+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2838**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.05% / filled 20/20。**
- 全期間 MARKET基準: n=2838, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.54% | **+1.54%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.44% | **+1.37%** |
| MARKET | 20/20 | 100.0% | +1.05% | **+1.05%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.81% | **+0.65%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.62% | **+0.81%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.55% | **+0.25%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +0.49% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RLS/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.02
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T22:22:28.074214+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=78349.8
- Funnel: target 755 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +30.89% | $8,714,674.83 |
| CHILLGUY/USDT:USDT | +14.99% | $1,019,909.33 |
| RLS/USDT:USDT | +10.05% | $2,443,721.66 |
| TRB/USDT:USDT | +8.17% | $2,997,297.76 |
| ZEC/USDT:USDT | +7.82% | $273,102,061.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHILLGUY/USDT:USDT | below_1h_threshold | +2.51% | +2.27% |
| B/USDT:USDT | below_1h_threshold | +2.45% | +2.21% |
| TAG/USDT:USDT | below_1h_threshold | +1.92% | +1.68% |
| LAB/USDT:USDT | below_1h_threshold | +1.73% | +1.49% |
| TRB/USDT:USDT | below_1h_threshold | +1.50% | +1.26% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
