# Decision Report

- generated_at: 2026-08-16T11:51:45.023551+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11734**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11734, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 3/20 | 15.0% | +0.95% | **+0.14%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.05% | **+0.03%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.03% | **-0.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | -0.09% | **-0.08%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.28% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.68% | **+1.35%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.96% | **+1.27%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.91% | **+0.87%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.23% | **+0.62%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.53** / 初期 $100.00 (+21.53%)
- 確定トレード: 183件 (TP 71 / SL 107 / EXP 5)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.53
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$620.90** / 初期 $100.00 (+520.90%)
- 確定: 4183件 (Win 1292 / Loss 1363 / Flat 1528) / skip 4112件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CROSS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $620.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.89** / 初期 $100.00 (+54.89%)
- 確定: 1783件 (Win 495 / Loss 417 / Flat 871) / skip 3362件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $154.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.38** / 初期 $100.00 (+19.38%)
- 確定: 1636件 (Win 496 / Loss 619 / Flat 521) / pending 6件 / skip 1569件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000182 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $119.38

## 6. Latest Market Context

- 更新: 2026-08-16T11:51:28.126866+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62949.8
- Funnel: target 986 → liquid 138 → pre 50 → checked 50 → surge 5 → strict 3
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1, 4h RSI 66.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKYAI/USDT:USDT | +16.83% | $9,320,418.24 |
| SPORTFUN/USDT:USDT | +15.71% | $4,770,732.34 |
| BICO/USDT:USDT | +15.60% | $4,216,028.47 |
| CHIP/USDT:USDT | +14.81% | $4,701,631.17 |
| VELVET/USDT:USDT | +14.22% | $30,702,791.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ROBO/USDT:USDT | below_1h_threshold | +2.72% | +2.77% |
| XAI/USDT:USDT | below_1h_threshold | +2.03% | +2.08% |
| WLFI/USDT:USDT | below_1h_threshold | +1.27% | +1.32% |
| UAI/USDT:USDT | below_1h_threshold | +1.08% | +1.13% |
| AEON1/USDT:USDT | below_1h_threshold | +1.03% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
