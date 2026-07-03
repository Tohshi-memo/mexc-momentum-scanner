# Decision Report

- generated_at: 2026-07-03T21:34:23.829321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8199**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8199, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +4.75% | **+2.85%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +5.07% | **+2.28%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.83% | **+2.13%** |
| ASK_LONG | 20/20 | 100.0% | +2.04% | **+2.04%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +5.00% | **+2.00%** |

## 2. $100 Live Portfolio

- 残高: **$102.10** / 初期 $100.00 (+2.10%)
- 確定トレード: 57件 (TP 20 / SL 36 / EXP 1)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$290.46** / 初期 $100.00 (+190.46%)
- 確定: 2518件 (Win 775 / Loss 839 / Flat 904) / skip 2242件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $290.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.04** / 初期 $100.00 (+6.04%)
- 確定: 611件 (Win 147 / Loss 147 / Flat 317) / skip 999件
- 成長率目線: 平均log +0.000096 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BAS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $106.04

## 5. Latest Market Context

- 更新: 2026-07-03T21:34:17.519802+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.37% price=62527.7
- Funnel: target 834 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TLM/USDT:USDT | +78.65% | $29,541,573.59 |
| ANSEM/USDT:USDT | +63.75% | $2,186,898.56 |
| MAGMA/USDT:USDT | +35.24% | $12,570,418.00 |
| BAS/USDT:USDT | +29.36% | $3,408,116.27 |
| TA/USDT:USDT | +13.64% | $2,197,818.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.19% | +2.56% |
| BAS/USDT:USDT | below_1h_threshold | +2.08% | +2.44% |
| US/USDT:USDT | below_1h_threshold | +1.83% | +2.20% |
| BLESS/USDT:USDT | below_1h_threshold | +1.71% | +2.08% |
| PEPE/USDT:USDT | below_1h_threshold | +1.65% | +2.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
