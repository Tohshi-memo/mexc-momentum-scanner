# Decision Report

- generated_at: 2026-07-18T10:11:08.065960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8932**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.90% / filled 20/20。**
- 全期間 MARKET基準: n=8932, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.90%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.90% | **+0.90%** |
| LIMIT_BB3S | 4/17 | 23.5% | +2.52% | **+0.59%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.03% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.01% | **+0.40%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.46% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.73% | **+0.61%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.12% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.42% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$110.69** / 初期 $100.00 (+10.69%)
- 確定トレード: 116件 (TP 43 / SL 69 / EXP 4)
- 最新: B/USDT:USDT SL_HIT PnL -3.30% 残高後 $110.69
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$362.38** / 初期 $100.00 (+262.38%)
- 確定: 3047件 (Win 946 / Loss 971 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $362.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.73** / 初期 $100.00 (+10.73%)
- 確定: 893件 (Win 212 / Loss 181 / Flat 500) / skip 1450件
- 成長率目線: 平均log +0.000114 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0411 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: B/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.09% 残高後 $110.73

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.77** / 初期 $100.00 (-0.23%)
- 確定: 187件 (Win 60 / Loss 100 / Flat 27) / pending 5件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000311 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: B/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.77

## 6. Latest Market Context

- 更新: 2026-07-18T10:11:03.080353+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63968.7
- Funnel: target 885 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.7 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +36.79% | $66,530,437.60 |
| TRADOOR/USDT:USDT | +28.69% | $4,165,357.26 |
| B/USDT:USDT | +21.36% | $2,530,911.48 |
| ROAM/USDT:USDT | +14.48% | $1,019,229.37 |
| ESPORTS/USDT:USDT | +12.64% | $14,781,013.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +2.67% | +2.66% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.65% | +2.64% |
| B/USDT:USDT | below_1h_threshold | +2.32% | +2.31% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.93% | +1.91% |
| ROAM/USDT:USDT | below_1h_threshold | +1.60% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
