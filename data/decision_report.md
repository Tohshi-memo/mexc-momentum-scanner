# Decision Report

- generated_at: 2026-08-14T17:36:26.537960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11582**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11582, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.02% | **+0.86%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.40% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +4.98% | **+2.24%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +5.33% | **+1.60%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +4.97% | **+1.49%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.64% | **+1.48%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.92** / 初期 $100.00 (+543.92%)
- 確定: 4050件 (Win 1272 / Loss 1331 / Flat 1447) / skip 4093件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_FIB1272_LONG` TP_HIT account +1.00% 残高後 $643.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3342件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0264 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.43** / 初期 $100.00 (+17.43%)
- 確定: 1539件 (Win 468 / Loss 588 / Flat 483) / pending 5件 / skip 1512件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000155 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.43

## 6. Latest Market Context

- 更新: 2026-08-14T17:36:16.956924+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=63154.9
- Funnel: target 985 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +10.78% | $5,871,431.94 |
| CAP/USDT:USDT | +8.91% | $12,901,378.26 |
| ACU/USDT:USDT | +5.72% | $2,699,135.55 |
| AVNT/USDT:USDT | +4.02% | $2,938,063.75 |
| BANK/USDT:USDT | +3.72% | $2,234,942.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BANK/USDT:USDT | below_1h_threshold | +3.41% | +3.33% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.30% | +3.22% |
| HOME/USDT:USDT | below_1h_threshold | +2.18% | +2.10% |
| AVNT/USDT:USDT | below_1h_threshold | +1.88% | +1.80% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.81% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
