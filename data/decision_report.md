# Decision Report

- generated_at: 2026-05-17T02:08:24.567898+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4374**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.86% / filled 20/20。**
- 全期間 MARKET基準: n=4374, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+1.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.86% | **+1.86%** |
| ASK | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 13/20 | 65.0% | +1.14% | **+0.74%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.09% | **+0.55%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.07% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.82% | **+0.45%** |
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.69% | **+0.45%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.12% | **+0.39%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.82% | **+0.33%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$98.17** / 初期 $100.00 (-1.83%)
- 確定トレード: 48件 (TP 13 / SL 32 / EXP 3)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.68** / 初期 $100.00 (+17.68%)
- 確定: 393件 (Win 97 / Loss 137 / Flat 159) / skip 542件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CGPT/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account -0.27% 残高後 $117.68

## 4. Latest Market Context

- 更新: 2026-05-17T02:08:21.255880+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=77800.0
- Funnel: target 760 → liquid 128 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIA/USDT:USDT | +23.03% | $1,785,064.50 |
| LYN/USDT:USDT | +17.87% | $3,721,390.35 |
| BSB/USDT:USDT | +9.51% | $3,835,200.55 |
| NMR/USDT:USDT | +9.40% | $1,184,967.54 |
| UP/USDT:USDT | +9.02% | $1,646,355.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +2.19% | +2.04% |
| B/USDT:USDT | below_1h_threshold | +1.19% | +1.05% |
| NMR/USDT:USDT | below_1h_threshold | +1.06% | +0.92% |
| GUA/USDT:USDT | below_1h_threshold | +0.43% | +0.28% |
| LDO/USDT:USDT | below_1h_threshold | +0.37% | +0.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
