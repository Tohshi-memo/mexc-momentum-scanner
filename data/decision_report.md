# Decision Report

- generated_at: 2026-06-18T03:16:06.829005+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6994**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6994, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +0.73% | **+0.15%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.06% | **-0.01%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.27% | **-0.09%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.64% | **-0.26%** |
| LIMIT_7PCT | 5/20 | 25.0% | -1.28% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.97% | **+2.97%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.82% | **+1.37%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.06% | **+1.24%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$210.90** / 初期 $100.00 (+110.90%)
- 確定: 1840件 (Win 509 / Loss 580 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $210.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.60** / 初期 $100.00 (+5.60%)
- 確定: 267件 (Win 74 / Loss 68 / Flat 125) / skip 138件
- 成長率目線: 平均log +0.000204 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0889 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLO/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $105.60

## 5. Latest Market Context

- 更新: 2026-06-18T03:16:01.275359+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=64490.1
- Funnel: target 790 → liquid 171 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.6 >= 65=1, 4h RSI 76.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +101.44% | $31,310,087.02 |
| O/USDT:USDT | +70.67% | $1,675,365.36 |
| SYN/USDT:USDT | +46.48% | $4,479,601.21 |
| H/USDT:USDT | +22.75% | $36,805,048.98 |
| UP/USDT:USDT | +20.39% | $2,974,797.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +3.52% | +3.77% |
| US/USDT:USDT | below_1h_threshold | +3.35% | +3.60% |
| EVAA/USDT:USDT | below_1h_threshold | +2.21% | +2.46% |
| OPN/USDT:USDT | below_1h_threshold | +1.43% | +1.68% |
| CLO/USDT:USDT | below_1h_threshold | +0.98% | +1.24% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
