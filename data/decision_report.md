# Decision Report

- generated_at: 2026-08-14T21:21:20.895423+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11606**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11606, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.72%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.72% | **-0.72%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.09% | **+0.82%** |
| LIMIT_3PCT | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.78% | **+0.70%** |
| LIMIT_ATR | 9/20 | 45.0% | +1.42% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.80% | **+1.68%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.53% | **+1.41%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.83% | **+1.00%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.98% | **+0.99%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$638.55** / 初期 $100.00 (+538.55%)
- 確定: 4074件 (Win 1277 / Loss 1341 / Flat 1456) / skip 4093件
- 成長率目線: 平均log +0.000455 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $638.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$151.92** / 初期 $100.00 (+51.92%)
- 確定: 1671件 (Win 478 / Loss 404 / Flat 789) / skip 3346件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0528 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $151.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.20** / 初期 $100.00 (+17.20%)
- 確定: 1554件 (Win 472 / Loss 596 / Flat 486) / pending 5件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.20

## 6. Latest Market Context

- 更新: 2026-08-14T21:21:12.633469+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=62857.7
- Funnel: target 985 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +21.05% | $6,711,848.07 |
| ACE/USDT:USDT | +17.47% | $64,721,702.18 |
| DOLO/USDT:USDT | +15.70% | $1,532,167.87 |
| ACU/USDT:USDT | +9.08% | $2,097,600.75 |
| VELVET/USDT:USDT | +8.31% | $41,908,026.13 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +2.32% | +2.35% |
| LDO/USDT:USDT | below_1h_threshold | +0.96% | +0.99% |
| ONE/USDT:USDT | below_1h_threshold | +0.75% | +0.79% |
| EDEN/USDT:USDT | below_1h_threshold | +0.68% | +0.71% |
| BTW/USDT:USDT | below_1h_threshold | +0.57% | +0.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
