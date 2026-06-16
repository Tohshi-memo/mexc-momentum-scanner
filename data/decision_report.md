# Decision Report

- generated_at: 2026-06-16T00:57:24.780873+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6820**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6820, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +2.16% | **+1.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.10% | **+0.28%** |
| LIMIT_BB3S | 3/19 | 15.8% | +0.81% | **+0.13%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.97% | **+1.58%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.03% | **+1.32%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.76% | **+0.97%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.95% | **+0.90%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.97% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$182.91** / 初期 $100.00 (+82.91%)
- 確定: 1693件 (Win 444 / Loss 528 / Flat 721) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $182.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 76件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T00:57:19.080088+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=66217.8
- Funnel: target 772 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +24.99% | $2,670,113.00 |
| EVAA/USDT:USDT | +23.82% | $42,303,274.41 |
| SPCXSTOCK/USDT:USDT | +23.59% | $334,166,957.25 |
| VELVET/USDT:USDT | +15.09% | $11,336,226.63 |
| HOME/USDT:USDT | +14.68% | $1,345,126.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.76% | +4.87% |
| BANANAS31/USDT:USDT | below_1h_threshold | +3.80% | +3.90% |
| UNI/USDT:USDT | below_1h_threshold | +3.69% | +3.79% |
| PUFFER/USDT:USDT | below_1h_threshold | +3.67% | +3.78% |
| RIF/USDT:USDT | below_1h_threshold | +3.27% | +3.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
