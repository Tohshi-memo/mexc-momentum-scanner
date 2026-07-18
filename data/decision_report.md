# Decision Report

- generated_at: 2026-07-18T09:21:16.717077+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8927**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=8927, expectancy=+0.01%
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
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.01% | **+0.81%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.21% | **+0.48%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.49% | **+0.37%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$111.25** / 初期 $100.00 (+11.25%)
- 確定トレード: 115件 (TP 43 / SL 68 / EXP 4)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $111.25
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$364.09** / 初期 $100.00 (+264.09%)
- 確定: 3042件 (Win 944 / Loss 968 / Flat 1130) / skip 2446件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $364.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$110.49** / 初期 $100.00 (+10.49%)
- 確定: 889件 (Win 210 / Loss 181 / Flat 498) / skip 1449件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0135 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $110.49

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.90** / 初期 $100.00 (-0.10%)
- 確定: 182件 (Win 58 / Loss 97 / Flat 27) / pending 4件 / skip 212件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000422 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $99.90

## 6. Latest Market Context

- 更新: 2026-07-18T09:21:10.098204+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=63938.8
- Funnel: target 885 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +59.70% | $60,884,005.71 |
| TRADOOR/USDT:USDT | +35.21% | $3,518,259.96 |
| ESPORTS/USDT:USDT | +27.21% | $14,299,818.44 |
| XEC/USDT:USDT | +15.12% | $3,678,972.43 |
| BSB/USDT:USDT | +12.47% | $1,435,295.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRADOOR/USDT:USDT | below_1h_threshold | +3.23% | +3.29% |
| CXMTSTOCK/USDT:USDT | below_1h_threshold | +0.75% | +0.81% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.43% | +0.49% |
| VVV/USDT:USDT | below_1h_threshold | +0.40% | +0.46% |
| UKOIL/USDT:USDT | below_1h_threshold | +0.27% | +0.33% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
