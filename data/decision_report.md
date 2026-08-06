# Decision Report

- generated_at: 2026-08-06T12:16:28.714431+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10595**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.67% / filled 20/20。**
- 全期間 MARKET基準: n=10595, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.67%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| MARKET | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.51% | **+0.45%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.49% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.07% | **+1.07%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.86% | **+0.69%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |

## 2. $100 Live Portfolio

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定トレード: 175件 (TP 67 / SL 103 / EXP 5)
- 最新: COTI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.05
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$596.41** / 初期 $100.00 (+496.41%)
- 確定: 3795件 (Win 1203 / Loss 1249 / Flat 1343) / skip 3361件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $596.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$145.01** / 初期 $100.00 (+45.01%)
- 確定: 1427件 (Win 398 / Loss 336 / Flat 693) / skip 2579件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0455 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $145.01

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.91** / 初期 $100.00 (+16.91%)
- 確定: 1146件 (Win 365 / Loss 448 / Flat 333) / pending 0件 / skip 924件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.91

## 6. Latest Market Context

- 更新: 2026-08-06T12:16:18.075329+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=64463.2
- Funnel: target 955 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CTSI/USDT:USDT | +77.58% | $1,776,955.86 |
| HFT/USDT:USDT | +48.47% | $4,838,020.51 |
| HEI/USDT:USDT | +46.61% | $74,323,003.66 |
| CASHCAT/USDT:USDT | +42.61% | $1,338,696.69 |
| ZBT/USDT:USDT | +40.13% | $3,591,444.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +3.54% | +3.74% |
| TUT/USDT:USDT | below_1h_threshold | +2.47% | +2.67% |
| SYN/USDT:USDT | below_1h_threshold | +2.18% | +2.38% |
| BTW/USDT:USDT | below_1h_threshold | +1.32% | +1.52% |
| ON/USDT:USDT | below_1h_threshold | +1.07% | +1.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
