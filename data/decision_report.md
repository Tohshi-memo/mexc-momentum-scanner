# Decision Report

- generated_at: 2026-07-31T17:11:32.656893+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10019**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10019, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.48% | **+0.33%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.01% | **+0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.58% | **+1.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.16% | **+1.46%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.05% | **+1.44%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.10% | **+1.16%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$553.17** / 初期 $100.00 (+453.17%)
- 確定: 3574件 (Win 1142 / Loss 1168 / Flat 1264) / skip 3006件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $553.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2152件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.78** / 初期 $100.00 (+11.78%)
- 確定: 848件 (Win 275 / Loss 335 / Flat 238) / pending 6件 / skip 642件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AXTISTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $111.78

## 6. Latest Market Context

- 更新: 2026-07-31T17:11:24.000326+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62847.6
- Funnel: target 921 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KOMA/USDT:USDT | +10.19% | $15,146,814.63 |
| AKE/USDT:USDT | +5.98% | $15,024,389.25 |
| SYN/USDT:USDT | +5.94% | $2,761,624.08 |
| ESPORTS/USDT:USDT | +5.57% | $4,443,577.56 |
| BTW/USDT:USDT | +5.14% | $1,298,895.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| OUSTSTOCK/USDT:USDT | below_1h_threshold | +3.59% | +3.60% |
| KOMA/USDT:USDT | below_1h_threshold | +3.26% | +3.27% |
| SNXX/USDT:USDT | below_1h_threshold | +3.18% | +3.18% |
| BTW/USDT:USDT | below_1h_threshold | +2.85% | +2.85% |
| KORU/USDT:USDT | below_1h_threshold | +2.72% | +2.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
