# Decision Report

- generated_at: 2026-07-18T09:41:23.898918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8928**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=8928, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.52% | **+0.50%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.43% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.51% | **+0.61%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.49% | **+0.37%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.84% | **+0.34%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.90% | **+0.28%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$367.73** / 初期 $100.00 (+267.73%)
- 確定: 3043件 (Win 945 / Loss 968 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET` TP_HIT account +1.00% 残高後 $367.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.49** / 初期 $100.00 (+10.49%)
- 確定: 890件 (Win 210 / Loss 181 / Flat 499) / skip 1449件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $110.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.25** / 初期 $100.00 (+0.25%)
- 確定: 183件 (Win 59 / Loss 97 / Flat 27) / pending 4件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000472 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $100.25

## 6. Latest Market Context

- 更新: 2026-07-18T09:41:15.394530+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63944.8
- Funnel: target 885 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +35.78% | $63,684,966.42 |
| TRADOOR/USDT:USDT | +30.65% | $3,801,669.71 |
| ROAM/USDT:USDT | +16.78% | $1,009,892.22 |
| ESPORTS/USDT:USDT | +15.55% | $14,682,550.02 |
| XEC/USDT:USDT | +12.89% | $3,708,239.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +2.85% | +2.90% |
| ROAM/USDT:USDT | below_1h_threshold | +1.78% | +1.83% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.60% | +1.65% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.30% | +1.35% |
| BULLA/USDT:USDT | below_1h_threshold | +0.91% | +0.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
