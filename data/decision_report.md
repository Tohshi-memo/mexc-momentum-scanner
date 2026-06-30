# Decision Report

- generated_at: 2026-06-30T11:58:40.309354+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7885**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7885, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.59% | **+0.69%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.86% | **+1.77%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.77% | **+1.41%** |
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.68% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$257.84** / 初期 $100.00 (+157.84%)
- 確定: 2355件 (Win 714 / Loss 786 / Flat 855) / skip 2091件
- 成長率目線: 平均log +0.000402 / 幾何平均 +0.040% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $257.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.45** / 初期 $100.00 (+6.45%)
- 確定: 457件 (Win 120 / Loss 119 / Flat 218) / skip 839件
- 成長率目線: 平均log +0.000137 / 幾何平均 +0.014% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GWEI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.45

## 5. Latest Market Context

- 更新: 2026-06-30T11:58:33.819338+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=59140.2
- Funnel: target 813 → liquid 150 → pre 50 → checked 50 → surge 5 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 71.9 >= 65=1, 4h RSI 73.3 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +51.15% | $39,112,791.68 |
| AIGENSYN/USDT:USDT | +44.50% | $12,942,360.64 |
| BTW/USDT:USDT | +35.23% | $8,098,816.85 |
| AVAVSTOCK/USDT:USDT | +29.60% | $2,018,578.54 |
| CAP/USDT:USDT | +21.72% | $4,020,499.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAVSTOCK/USDT:USDT | below_1h_threshold | +4.02% | +4.30% |
| BASED/USDT:USDT | below_1h_threshold | +3.46% | +3.74% |
| CAP/USDT:USDT | below_1h_threshold | +3.37% | +3.64% |
| KAS/USDT:USDT | below_1h_threshold | +1.93% | +2.20% |
| KORU/USDT:USDT | below_1h_threshold | +1.67% | +1.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
