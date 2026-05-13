# Decision Report

- generated_at: 2026-05-13T14:07:36.717633+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4227**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4227, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_2PCT | 15/20 | 75.0% | -0.05% | **-0.04%** |
| LIMIT_BB3S | 9/18 | 50.0% | -0.25% | **-0.13%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.27% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.25% | **+0.75%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +2.55% | **+0.64%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 447件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T14:07:34.038037+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=79704.9
- Funnel: target 765 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +41.20% | $133,456,985.29 |
| COS/USDT:USDT | +34.20% | $1,849,782.48 |
| JCT/USDT:USDT | +27.69% | $1,107,511.08 |
| TRUTH/USDT:USDT | +26.93% | $3,803,304.50 |
| UB/USDT:USDT | +26.56% | $10,488,915.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +2.21% | +2.10% |
| BABASTOCK/USDT:USDT | below_1h_threshold | +1.61% | +1.50% |
| LAB/USDT:USDT | below_1h_threshold | +1.33% | +1.22% |
| STX/USDT:USDT | below_1h_threshold | +1.19% | +1.08% |
| AKT/USDT:USDT | below_1h_threshold | +1.10% | +0.99% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
