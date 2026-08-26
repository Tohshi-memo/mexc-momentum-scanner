# Decision Report

- generated_at: 2026-08-26T12:06:24.473845+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12703**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12703, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 8/18 | 44.4% | +1.72% | **+0.76%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.57% | **+0.49%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.60% | **+0.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.26%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.52% | **+0.91%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.71% | **+0.68%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.62% | **+0.52%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.67% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$700.48** / 初期 $100.00 (+600.48%)
- 確定: 4603件 (Win 1400 / Loss 1513 / Flat 1690) / skip 4661件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $700.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.16** / 初期 $100.00 (+58.16%)
- 確定: 1998件 (Win 544 / Loss 480 / Flat 974) / skip 4116件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1181 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $158.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.82** / 初期 $100.00 (+16.82%)
- 確定: 1975件 (Win 580 / Loss 752 / Flat 643) / pending 5件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000374 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.82

## 6. Latest Market Context

- 更新: 2026-08-26T12:06:13.679119+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=78420.0
- Funnel: target 1023 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +256.75% | $17,409,074.08 |
| TAC/USDT:USDT | +50.84% | $7,202,680.68 |
| BMT/USDT:USDT | +50.09% | $15,699,485.51 |
| LONGXIA/USDT:USDT | +32.04% | $1,987,671.78 |
| PORTAL/USDT:USDT | +18.51% | $4,092,070.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +3.60% | +3.63% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.82% | +2.85% |
| EDEN/USDT:USDT | below_1h_threshold | +1.19% | +1.23% |
| SOXS/USDT:USDT | below_1h_threshold | +0.85% | +0.88% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +0.73% | +0.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
