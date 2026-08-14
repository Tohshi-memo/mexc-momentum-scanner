# Decision Report

- generated_at: 2026-08-14T17:41:31.242609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11583**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11583, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.67%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.98% | **+2.24%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.86% | **+1.67%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +5.33% | **+1.60%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.77% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.92** / 初期 $100.00 (+543.92%)
- 確定: 4051件 (Win 1272 / Loss 1331 / Flat 1448) / skip 4093件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $643.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.44** / 初期 $100.00 (+50.44%)
- 確定: 1652件 (Win 472 / Loss 398 / Flat 782) / skip 3342件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0416 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $150.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.23** / 初期 $100.00 (+17.23%)
- 確定: 1540件 (Win 468 / Loss 589 / Flat 483) / pending 5件 / skip 1512件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000218 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.23

## 6. Latest Market Context

- 更新: 2026-08-14T17:41:19.072468+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=63113.2
- Funnel: target 985 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +8.37% | $5,887,048.97 |
| CAP/USDT:USDT | +7.83% | $13,402,706.01 |
| AVNT/USDT:USDT | +5.17% | $2,947,471.73 |
| BANK/USDT:USDT | +3.80% | $2,244,828.77 |
| ACU/USDT:USDT | +3.49% | $2,716,552.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +4.13% | +4.12% |
| BANK/USDT:USDT | below_1h_threshold | +3.39% | +3.37% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.30% | +3.29% |
| EDEN/USDT:USDT | below_1h_threshold | +3.30% | +3.29% |
| AVNT/USDT:USDT | below_1h_threshold | +3.00% | +2.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
