# Decision Report

- generated_at: 2026-09-16T07:46:21.699105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14650**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14650, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 6/14 | 42.9% | +2.71% | **+1.16%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.69% | **+0.38%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.75% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.83% | **+1.46%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.30% | **+0.87%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 214件 (TP 79 / SL 130 / EXP 5)
- 最新: SHROOM/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,050.73** / 初期 $100.00 (+950.73%)
- 確定: 5529件 (Win 1647 / Loss 1787 / Flat 2095) / skip 5682件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,050.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$229.61** / 初期 $100.00 (+129.61%)
- 確定: 3057件 (Win 839 / Loss 720 / Flat 1498) / skip 5004件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0009 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $229.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.66** / 初期 $100.00 (+24.66%)
- 確定: 2939件 (Win 874 / Loss 1152 / Flat 913) / pending 4件 / skip 3179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000345 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $124.66

## 6. Latest Market Context

- 更新: 2026-09-16T07:46:12.869435+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.29% price=75782.7
- Funnel: target 1054 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SYN/USDT:USDT | +122.18% | $7,497,676.37 |
| LSK/USDT:USDT | +20.04% | $19,873,479.19 |
| USELESS/USDT:USDT | +17.38% | $5,944,066.01 |
| LONGXIA/USDT:USDT | +14.00% | $2,597,643.48 |
| MARSCOIN/USDT:USDT | +9.46% | $1,591,538.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +1.36% | +1.65% |
| USELESS/USDT:USDT | below_1h_threshold | +1.00% | +1.28% |
| LSK/USDT:USDT | below_1h_threshold | +0.94% | +1.23% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.91% | +1.20% |
| SNXX/USDT:USDT | below_1h_threshold | +0.89% | +1.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
