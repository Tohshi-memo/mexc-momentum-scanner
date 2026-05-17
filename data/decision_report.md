# Decision Report

- generated_at: 2026-05-17T18:48:35.571677+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4416**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4416, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.03% | **+0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/11 | 18.2% | +5.17% | **+0.94%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.14% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.82% | **+1.27%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.58% | **+1.18%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.21% | **+0.67%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.71% | **+0.57%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.85** / 初期 $100.00 (+19.85%)
- 確定: 413件 (Win 107 / Loss 140 / Flat 166) / skip 564件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $119.85

## 4. Latest Market Context

- 更新: 2026-05-17T18:48:30.693558+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78081.0
- Funnel: target 760 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +20.40% | $1,725,871.43 |
| UB/USDT:USDT | +10.91% | $12,893,018.49 |
| BUILDONBOB/USDT:USDT | +4.38% | $1,069,002.07 |
| ASTEROID/USDT:USDT | +3.37% | $4,139,694.22 |
| BEAT/USDT:USDT | +2.76% | $3,599,856.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BILL/USDT:USDT | below_1h_threshold | +3.19% | +3.14% |
| BEAT/USDT:USDT | below_1h_threshold | +1.98% | +1.93% |
| HYPE/USDT:USDT | below_1h_threshold | +1.91% | +1.87% |
| LYN/USDT:USDT | below_1h_threshold | +1.20% | +1.16% |
| FIDA/USDT:USDT | below_1h_threshold | +1.07% | +1.03% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
