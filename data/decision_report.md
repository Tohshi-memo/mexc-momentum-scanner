# Decision Report

- generated_at: 2026-04-30T15:26:05.168806+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2712**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2712, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.04%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.04% | **-0.04%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.28% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +7.03% | **+4.69%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.73% | **+1.09%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.05% | **+0.73%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.03% | **+0.72%** |

## 2. $100 Live Portfolio

- 残高: **$100.50** / 初期 $100.00 (+0.50%)
- 確定トレード: 2件 (TP 1 / SL 1 / EXP 0)
- 最新: UB/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.50
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-04-30T15:26:03.684393+00:00 / 保存件数 31/288
- BTC: BULLISH 1h +0.23% price=76433.0
- Funnel: target 762 → liquid 226 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BR/USDT:USDT | +39.16% | $2,440,612.30 |
| BSB/USDT:USDT | +37.21% | $44,433,992.56 |
| SKYAI/USDT:USDT | +34.92% | $23,662,284.48 |
| RIVER/USDT:USDT | +21.93% | $21,013,608.68 |
| BIO/USDT:USDT | +21.70% | $3,511,798.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QCOMSTOCK/USDT:USDT | below_1h_threshold | +3.23% | +3.00% |
| POWER/USDT:USDT | below_1h_threshold | +2.97% | +2.74% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.48% | +2.25% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.01% | +1.78% |
| AKT/USDT:USDT | below_1h_threshold | +1.51% | +1.28% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
