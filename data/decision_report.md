# Decision Report

- generated_at: 2026-09-11T23:31:20.334378+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14262**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14262, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.61% | **-0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +0.57% | **+0.48%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.02% | **+0.02%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.14% | **+1.61%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +5.08% | **+1.27%** |
| MARKET_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.73% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,113.42** / 初期 $100.00 (+1013.42%)
- 確定: 5418件 (Win 1635 / Loss 1754 / Flat 2029) / skip 5405件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $1,113.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$209.84** / 初期 $100.00 (+109.84%)
- 確定: 2832件 (Win 780 / Loss 656 / Flat 1396) / skip 4841件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1381 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $209.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$125.08** / 初期 $100.00 (+25.08%)
- 確定: 2753件 (Win 817 / Loss 1054 / Flat 882) / pending 3件 / skip 2976件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000433 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $125.08

## 6. Latest Market Context

- 更新: 2026-09-11T23:31:07.212351+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77164.0
- Funnel: target 1067 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +54.07% | $15,017,495.24 |
| LAB/USDT:USDT | +28.65% | $11,961,932.76 |
| CYS/USDT:USDT | +19.38% | $1,291,995.30 |
| BEAT/USDT:USDT | +14.85% | $11,351,708.16 |
| LSK/USDT:USDT | +14.67% | $3,183,213.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STONK/USDT:USDT | below_1h_threshold | +4.94% | +4.87% |
| BTW/USDT:USDT | below_1h_threshold | +2.42% | +2.35% |
| RAY/USDT:USDT | below_1h_threshold | +2.22% | +2.15% |
| LSK/USDT:USDT | below_1h_threshold | +1.97% | +1.90% |
| CNPY/USDT:USDT | below_1h_threshold | +1.90% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
