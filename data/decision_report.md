# Decision Report

- generated_at: 2026-05-08T11:02:34.880914+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3774**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.38% / filled 20/20。**
- 全期間 MARKET基準: n=3774, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+2.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.38% | **+2.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.38% | **+2.38%** |
| ASK | 20/20 | 100.0% | +2.29% | **+2.29%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.74% | **+1.48%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_2PCT | 13/20 | 65.0% | +0.69% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +0.21% | **+0.10%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.04% | **-0.01%** |

## 2. $100 Live Portfolio

- 残高: **$99.32** / 初期 $100.00 (-0.68%)
- 確定トレード: 26件 (TP 7 / SL 17 / EXP 2)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 191件 (Win 48 / Loss 64 / Flat 79) / skip 144件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHAROS/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T11:02:31.826968+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=80181.6
- Funnel: target 773 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +46.70% | $7,218,116.72 |
| BSB/USDT:USDT | +37.43% | $9,585,226.14 |
| PLAY/USDT:USDT | +33.07% | $9,580,113.99 |
| STRK/USDT:USDT | +32.64% | $20,027,333.17 |
| AGT/USDT:USDT | +26.53% | $5,589,125.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.62% | +1.59% |
| BILL/USDT:USDT | below_1h_threshold | +1.10% | +1.07% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +0.91% | +0.88% |
| PHAROS/USDT:USDT | below_1h_threshold | +0.81% | +0.79% |
| PENDLE/USDT:USDT | below_1h_threshold | +0.77% | +0.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
