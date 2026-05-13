# Decision Report

- generated_at: 2026-05-13T15:53:11.074905+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4233**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4233, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.31% | **+0.31%** |
| LIMIT_BB3S | 7/18 | 38.9% | +0.63% | **+0.25%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.29% | **+0.22%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.22% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| ASK_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 452件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T15:53:07.913558+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.82% price=79072.9
- Funnel: target 765 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +46.09% | $2,267,490.52 |
| LAB/USDT:USDT | +31.21% | $154,865,570.37 |
| TRUTH/USDT:USDT | +30.82% | $4,177,868.07 |
| UB/USDT:USDT | +21.96% | $11,009,680.19 |
| NBISSTOCK/USDT:USDT | +19.14% | $1,293,781.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRUTH/USDT:USDT | below_1h_threshold | +2.38% | +3.20% |
| INX/USDT:USDT | below_1h_threshold | +1.83% | +2.65% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.64% | +2.46% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.25% | +2.07% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +1.11% | +1.93% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
