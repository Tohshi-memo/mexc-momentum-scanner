# Decision Report

- generated_at: 2026-08-14T12:01:18.535459+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11550**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11550, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.36% | **+2.13%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.22% | **+0.73%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +3.01% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$641.26** / 初期 $100.00 (+541.26%)
- 確定: 4018件 (Win 1262 / Loss 1318 / Flat 1438) / skip 4093件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $641.26

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3310件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0865 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.34** / 初期 $100.00 (+18.34%)
- 確定: 1510件 (Win 457 / Loss 572 / Flat 481) / pending 3件 / skip 1508件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000276 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ACE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $118.34

## 6. Latest Market Context

- 更新: 2026-08-14T12:01:10.305364+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=62855.0
- Funnel: target 981 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +109.43% | $25,408,689.40 |
| AKE/USDT:USDT | +67.80% | $68,101,840.38 |
| VELVET/USDT:USDT | +42.56% | $32,414,467.72 |
| CAP/USDT:USDT | +24.19% | $4,591,642.17 |
| H/USDT:USDT | +22.15% | $2,580,448.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHYMSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +1.93% |
| SNXX/USDT:USDT | below_1h_threshold | +1.71% | +1.68% |
| ONDSSTOCK/USDT:USDT | below_1h_threshold | +0.98% | +0.95% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.93% | +0.90% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +0.88% | +0.85% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
