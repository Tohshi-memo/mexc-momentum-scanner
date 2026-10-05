# Decision Report

- generated_at: 2026-10-05T10:26:30.700259+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16153**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16153, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/12 | 41.7% | +3.20% | **+1.33%** |
| LIMIT_8PCT | 6/20 | 30.0% | +1.28% | **+0.39%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.13% | **+0.34%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.47% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.69% | **+0.93%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.11% | **+0.55%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +1.26% | **+0.44%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +0.73% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,305.64** / 初期 $100.00 (+1205.64%)
- 確定: 6212件 (Win 1824 / Loss 1988 / Flat 2400) / skip 6502件
- 成長率目線: 平均log +0.000414 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,305.64

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3610件 (Win 1005 / Loss 845 / Flat 1760) / skip 5954件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0830 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4315件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-05T10:26:18.879005+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=86089.3
- Funnel: target 1074 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +98.65% | $12,273,393.61 |
| MOVR/USDT:USDT | +32.25% | $6,780,370.14 |
| ADA/USDT:USDT | +10.49% | $74,102,212.54 |
| AIN/USDT:USDT | +9.72% | $1,216,655.09 |
| ORCA/USDT:USDT | +9.32% | $1,379,581.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FILECOIN/USDT:USDT | below_1h_threshold | +1.66% | +1.48% |
| JTO/USDT:USDT | below_1h_threshold | +1.47% | +1.29% |
| SKY/USDT:USDT | below_1h_threshold | +1.17% | +0.99% |
| MOVR/USDT:USDT | below_1h_threshold | +1.11% | +0.93% |
| SOXS/USDT:USDT | below_1h_threshold | +1.07% | +0.89% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
