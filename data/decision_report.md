# Decision Report

- generated_at: 2026-10-06T12:01:34.405566+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16203**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16203, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_9PCT | 4/20 | 20.0% | +3.29% | **+0.66%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +4.01% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_BB3S | 6/15 | 40.0% | -0.45% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +3.40% | **+3.40%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +3.03% | **+2.27%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.75% | **+0.96%** |
| LIMIT_ATR_LONG | 7/20 | 35.0% | +2.07% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,316.41** / 初期 $100.00 (+1216.41%)
- 確定: 6245件 (Win 1831 / Loss 1996 / Flat 2418) / skip 6519件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NMR/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $1,316.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.34** / 初期 $100.00 (+176.34%)
- 確定: 3612件 (Win 1006 / Loss 845 / Flat 1761) / skip 6002件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0142 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NMR/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $276.34

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4365件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T12:01:24.579031+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=86228.6
- Funnel: target 1074 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +86.66% | $37,251,296.67 |
| US/USDT:USDT | +38.63% | $1,278,808.84 |
| ORCA/USDT:USDT | +31.20% | $3,460,647.40 |
| NMR/USDT:USDT | +30.20% | $5,070,732.17 |
| BR/USDT:USDT | +26.91% | $44,972,035.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +1.81% | +1.79% |
| SOXL/USDT:USDT | below_1h_threshold | +1.09% | +1.07% |
| CAP/USDT:USDT | below_1h_threshold | +0.95% | +0.93% |
| ORCA/USDT:USDT | below_1h_threshold | +0.94% | +0.91% |
| RLC/USDT:USDT | below_1h_threshold | +0.34% | +0.32% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
