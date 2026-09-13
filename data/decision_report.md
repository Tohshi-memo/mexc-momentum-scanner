# Decision Report

- generated_at: 2026-09-13T01:41:27.543853+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14346**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14346, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.71% | **-0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_9PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.51% | **+0.41%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.49% | **+2.12%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.70% | **+2.02%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.08% | **+1.45%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_BB3S_LONG | 6/10 | 60.0% | +2.15% | **+1.29%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5477件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$219.63** / 初期 $100.00 (+119.63%)
- 確定: 2864件 (Win 794 / Loss 667 / Flat 1403) / skip 4893件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1717 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $219.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.18** / 初期 $100.00 (+26.18%)
- 確定: 2797件 (Win 832 / Loss 1075 / Flat 890) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000494 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.18

## 6. Latest Market Context

- 更新: 2026-09-13T01:41:15.597233+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=77258.1
- Funnel: target 1068 → liquid 127 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.9 >= 65=1, 4h RSI 91.6 >= 65=1, 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +110.00% | $66,058,791.05 |
| POWR/USDT:USDT | +45.77% | $1,070,837.65 |
| ZCAT/USDT:USDT | +23.74% | $1,098,912.35 |
| LONGXIA/USDT:USDT | +20.17% | $10,043,858.54 |
| REZ/USDT:USDT | +17.56% | $2,530,395.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOCK/USDT:USDT | below_1h_threshold | +1.77% | +1.74% |
| VTHO/USDT:USDT | below_1h_threshold | +1.74% | +1.71% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.24% | +1.21% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.19% | +1.17% |
| BSV/USDT:USDT | below_1h_threshold | +1.14% | +1.12% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
