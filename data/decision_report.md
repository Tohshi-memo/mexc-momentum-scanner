# Decision Report

- generated_at: 2026-08-01T10:36:19.768469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10083**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.26% / filled 20/20。**
- 全期間 MARKET基準: n=10083, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.26%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +1.69% | **+1.52%** |
| MARKET | 20/20 | 100.0% | +1.26% | **+1.26%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.17% | **+0.70%** |
| LIMIT_BB3S | 4/20 | 20.0% | +2.96% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.85% | **+0.43%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.19% | **+0.11%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.17% | **+0.09%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.08% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$573.69** / 初期 $100.00 (+473.69%)
- 確定: 3629件 (Win 1158 / Loss 1190 / Flat 1281) / skip 3015件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $573.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2215件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.11** / 初期 $100.00 (+11.11%)
- 確定: 894件 (Win 285 / Loss 353 / Flat 256) / pending 5件 / skip 656件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000039 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SATS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $111.11

## 6. Latest Market Context

- 更新: 2026-08-01T10:36:11.615029+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=63011.6
- Funnel: target 921 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +46.26% | $16,971,443.20 |
| BTW/USDT:USDT | +40.23% | $6,562,486.62 |
| JIMOTHY/USDT:USDT | +36.69% | $1,412,496.40 |
| TAKE/USDT:USDT | +31.66% | $1,077,026.70 |
| ICNT/USDT:USDT | +20.92% | $1,056,516.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +2.61% | +2.63% |
| EVAA/USDT:USDT | below_1h_threshold | +2.02% | +2.04% |
| TAKE/USDT:USDT | below_1h_threshold | +1.95% | +1.97% |
| AKE/USDT:USDT | below_1h_threshold | +1.58% | +1.59% |
| UB/USDT:USDT | below_1h_threshold | +1.56% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
