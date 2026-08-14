# Decision Report

- generated_at: 2026-08-14T18:31:30.747434+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11595**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11595, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.91% | **+0.82%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.48% | **+0.59%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.68% | **+1.52%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.94% | **+1.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$646.35** / 初期 $100.00 (+546.35%)
- 確定: 4063件 (Win 1276 / Loss 1336 / Flat 1451) / skip 4093件
- 成長率目線: 平均log +0.000459 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $646.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$152.33** / 初期 $100.00 (+52.33%)
- 確定: 1662件 (Win 477 / Loss 402 / Flat 783) / skip 3344件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0822 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $152.33

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.01** / 初期 $100.00 (+17.01%)
- 確定: 1545件 (Win 469 / Loss 592 / Flat 484) / pending 6件 / skip 1518件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000217 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.01

## 6. Latest Market Context

- 更新: 2026-08-14T18:31:19.536552+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63003.3
- Funnel: target 985 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOLO/USDT:USDT | +36.46% | $1,048,743.54 |
| US/USDT:USDT | +27.13% | $6,623,724.82 |
| ACE/USDT:USDT | +10.86% | $56,114,371.93 |
| AKE/USDT:USDT | +9.21% | $77,730,472.86 |
| ACU/USDT:USDT | +5.55% | $2,520,507.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.30% | +3.28% |
| EDEN/USDT:USDT | below_1h_threshold | +2.48% | +2.46% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.43% | +2.40% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.64% | +1.62% |
| RE/USDT:USDT | below_1h_threshold | +1.62% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
