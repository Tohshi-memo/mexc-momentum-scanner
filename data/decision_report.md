# Decision Report

- generated_at: 2026-08-01T16:56:43.630847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10104**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=10104, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.48% | **+0.43%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.32% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.58% | **+1.93%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.28% | **+1.02%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.60% | **+0.52%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.45% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.82** / 初期 $100.00 (+470.82%)
- 確定: 3638件 (Win 1158 / Loss 1191 / Flat 1289) / skip 3027件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $570.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2236件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.15** / 初期 $100.00 (+11.15%)
- 確定: 914件 (Win 289 / Loss 358 / Flat 267) / pending 5件 / skip 659件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000072 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.15

## 6. Latest Market Context

- 更新: 2026-08-01T16:56:28.911495+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=62894.2
- Funnel: target 922 → liquid 143 → pre 50 → checked 50 → surge 6 → strict 3
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.0 >= 65=1, 4h RSI 67.6 >= 65=1, 4h RSI 82.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AEVO/USDT:USDT | +11.41% | $1,438,307.15 |
| UAI/USDT:USDT | +11.29% | $7,239,108.69 |
| FIGHT/USDT:USDT | +7.56% | $2,297,295.95 |
| AKE/USDT:USDT | +7.02% | $17,815,058.35 |
| IDOL/USDT:USDT | +6.90% | $1,527,446.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +4.99% | +5.12% |
| GIGGLE/USDT:USDT | below_1h_threshold | +4.20% | +4.33% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.14% | +4.27% |
| BLESS/USDT:USDT | below_1h_threshold | +3.07% | +3.20% |
| TAG/USDT:USDT | below_1h_threshold | +2.74% | +2.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
