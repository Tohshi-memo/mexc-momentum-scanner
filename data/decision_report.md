# Decision Report

- generated_at: 2026-07-03T04:34:01.310830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8130**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8130, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.82% | **+0.41%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.80% | **+1.53%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +6.84% | **+0.68%** |
| ASK_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$102.62** / 初期 $100.00 (+2.62%)
- 確定トレード: 53件 (TP 19 / SL 33 / EXP 1)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.62
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$290.48** / 初期 $100.00 (+190.48%)
- 確定: 2452件 (Win 757 / Loss 817 / Flat 878) / skip 2239件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KORU/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $290.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.81** / 初期 $100.00 (+5.81%)
- 確定: 584件 (Win 141 / Loss 138 / Flat 305) / skip 957件
- 成長率目線: 平均log +0.000097 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score -0.0271 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KORU/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $105.81

## 5. Latest Market Context

- 更新: 2026-07-03T04:33:52.871588+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=61412.5
- Funnel: target 834 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +31.54% | $5,966,097.39 |
| ZKP/USDT:USDT | +31.54% | $1,955,097.20 |
| MAGMA/USDT:USDT | +24.45% | $5,644,491.52 |
| THE/USDT:USDT | +20.95% | $2,158,068.42 |
| GUA/USDT:USDT | +18.89% | $10,321,553.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_1h_threshold | +3.35% | +3.35% |
| ZKP/USDT:USDT | below_1h_threshold | +2.78% | +2.78% |
| US/USDT:USDT | below_1h_threshold | +2.64% | +2.63% |
| GUA/USDT:USDT | below_1h_threshold | +2.45% | +2.44% |
| SYN/USDT:USDT | below_1h_threshold | +2.26% | +2.25% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
