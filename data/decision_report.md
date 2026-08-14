# Decision Report

- generated_at: 2026-08-14T18:21:35.543627+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11594**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11594, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +0.85% | **+0.76%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.76% | **+0.72%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$649.60** / 初期 $100.00 (+549.60%)
- 確定: 4062件 (Win 1276 / Loss 1335 / Flat 1451) / skip 4093件
- 成長率目線: 平均log +0.000461 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $649.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.87** / 初期 $100.00 (+52.87%)
- 確定: 1661件 (Win 477 / Loss 401 / Flat 783) / skip 3344件
- 成長率目線: 平均log +0.000256 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0978 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $152.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.22** / 初期 $100.00 (+17.22%)
- 確定: 1544件 (Win 469 / Loss 591 / Flat 484) / pending 6件 / skip 1518件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000244 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $117.22

## 6. Latest Market Context

- 更新: 2026-08-14T18:21:21.716518+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=63010.0
- Funnel: target 985 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +36.41% | $6,407,236.42 |
| AKE/USDT:USDT | +21.15% | $74,444,838.79 |
| ACE/USDT:USDT | +10.39% | $55,698,307.88 |
| ACU/USDT:USDT | +5.05% | $2,501,720.25 |
| BANK/USDT:USDT | +3.88% | $2,321,283.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.62% | +3.59% |
| EDEN/USDT:USDT | below_1h_threshold | +3.49% | +3.46% |
| BTW/USDT:USDT | below_1h_threshold | +2.93% | +2.89% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.61% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.59% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
