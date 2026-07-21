# Decision Report

- generated_at: 2026-07-21T02:26:31.624361+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9142**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.51% / filled 20/20。**
- 全期間 MARKET基準: n=9142, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.51% | **+1.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +1.66% | **+1.41%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.60% | **+1.20%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +4.18% | **+1.04%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.52% | **+0.47%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.50% | **+0.40%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.42% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$408.42** / 初期 $100.00 (+308.42%)
- 確定: 3204件 (Win 1003 / Loss 1020 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $408.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$128.58** / 初期 $100.00 (+28.58%)
- 確定: 1103件 (Win 289 / Loss 228 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1064 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $128.58

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.92** / 初期 $100.00 (+0.92%)
- 確定: 337件 (Win 118 / Loss 150 / Flat 69) / pending 4件 / skip 274件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000209 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.92

## 6. Latest Market Context

- 更新: 2026-07-21T02:26:20.762299+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=65267.2
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.6 >= 65=1, 4h RSI 74.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +56.54% | $1,436,931.96 |
| JIMOTHY/USDT:USDT | +26.44% | $2,797,765.25 |
| BLESS/USDT:USDT | +18.80% | $1,778,058.77 |
| HEMI/USDT:USDT | +10.33% | $3,176,272.56 |
| LDO/USDT:USDT | +9.12% | $6,243,451.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.31% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.07% | +0.98% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +0.94% | +0.84% |
| BULLA/USDT:USDT | below_1h_threshold | +0.91% | +0.81% |
| AKE/USDT:USDT | below_1h_threshold | +0.60% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
